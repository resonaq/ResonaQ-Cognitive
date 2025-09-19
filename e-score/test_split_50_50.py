#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
test_split_50_50.py
-------------------
Amaç: generate_alpaca_split_50_50.py çıktısını (category,prompt,reference,generation)
var olan değerlendirici (e_score_uncertainty_from_csv.py) ile test etmek,
sonuçları category ile birleştirip özet tablolar çıkarmak.

Kullanım (PowerShell tek satır):
  python test_split_50_50.py --input alpaca_50det_50cre_with_generations.csv ^
    --model_id gpt2-medium --num_candidates 5 --max_new_tokens 100 --temperature 0.9 --top_p 0.95

Kullanım (Linux/macOS çok satır):
  python test_split_50_50.py \
    --input alpaca_50det_50cre_with_generations.csv \
    --model_id gpt2-medium --num_candidates 5 --max_new_tokens 100 --temperature 0.9 --top_p 0.95
"""

import argparse, os, sys, subprocess, hashlib, re
import pandas as pd

def sha1_text(s: str) -> str:
    s = (s or "").strip()
    return hashlib.sha1(s.encode("utf-8")).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="split_50_50 CSV (category,prompt,reference,generation)")
    ap.add_argument("--model_id", default="gpt2", help="HF model id (örn. gpt2, gpt2-medium)")
    ap.add_argument("--num_candidates", type=int, default=5)
    ap.add_argument("--max_new_tokens", type=int, default=64)
    ap.add_argument("--temperature", type=float, default=0.7)
    ap.add_argument("--top_p", type=float, default=0.9)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--mc_dropout", action="store_true")
    ap.add_argument("--eval_script", default="e_score_uncertainty_from_csv.py",
                    help="Değerlendirici script adı/yolu")
    ap.add_argument("--out_prefix", default="split_50_50_test",
                    help="Çıktı dosya öneki")
    ap.add_argument("--no_plots", action="store_true", help="Grafik üretme")
    args = ap.parse_args()

    inp = args.input
    if not os.path.exists(inp):
        print(f"[ERR] input bulunamadı: {inp}", file=sys.stderr); sys.exit(1)
    if not os.path.exists(args.eval_script):
        print(f"[ERR] değerlendirici bulunamadı: {args.eval_script}", file=sys.stderr); sys.exit(1)

    # 1) Orijinal inputu yükle (category,prompt,reference,generation)
    df_in = pd.read_csv(inp)
    required = {"category","prompt","reference"}
    if not required.issubset(df_in.columns):
        raise ValueError(f"Input CSV şu sütunları içermeli: {required}")

    # 2) Değerlendiriciyi bu input ile çalıştır
    #    (e_score_uncertainty_from_csv.py, sonuç: e_score_uncertainty_results.csv)
    eval_cmd = [
        sys.executable, args.eval_script,
        "--csv", inp,
        "--model_id", args.model_id,
        "--num_candidates", str(args.num_candidates),
        "--max_new_tokens", str(args.max_new_tokens),
        "--temperature", str(args.temperature),
        "--top_p", str(args.top_p),
        "--seed", str(args.seed),
    ]
    if args.mc_dropout:
        eval_cmd.append("--mc_dropout")

    print(">> Running evaluator:\n", " ".join(eval_cmd))
    subprocess.run(eval_cmd, check=True)

    eval_out = "e_score_uncertainty_results.csv"
    if not os.path.exists(eval_out):
        print(f"[ERR] beklenen çıktı yok: {eval_out}", file=sys.stderr); sys.exit(1)

    # 3) Sonuçları yükle ve category ile merge et
    df_eval = pd.read_csv(eval_out)
    # sağlam merge için prompt+reference hash’i ile eşle
    df_in["_key"] = df_in.apply(lambda r: sha1_text(str(r["prompt"]) + "||" + str(r["reference"])), axis=1)
    df_eval["_key"] = df_eval.apply(lambda r: sha1_text(str(r["prompt"]) + "||" + str(r["reference"])), axis=1)

    df = pd.merge(df_eval, df_in[["_key","category"]], on="_key", how="left")
    df.drop(columns=["_key"], inplace=True)

    # 4) Kaydet: satır bazlı tam sonuç
    per_row_path = f"{args.out_prefix}__per_row_results.csv"
    df.to_csv(per_row_path, index=False)
    print(f">> Saved per-row results: {per_row_path}")

    # 5) Kategori bazında özet (mean, std, count) — ana metrikler
    metrics = [
        "BLEU","ROUGE_L",
        "H_token_mean","Sharpness_mean","E_mean",
        "MI","VR","ECE","NLL","Brier","gen_len_char"
    ]
    agg = {}
    for m in metrics:
        agg[m] = ["mean","std","count"]
    summary = df.groupby("category").agg(agg)
    summary.columns = ["_".join(col).strip() for col in summary.columns.values]
    summary_path = f"{args.out_prefix}__summary_by_category.csv"
    summary.to_csv(summary_path)
    print(f">> Saved summary by category: {summary_path}")

    # 6) Creative - Deterministic delta tablosu (yalın karşılaştırma)
    def safe(x): 
        try: return float(x)
        except: return float("nan")
    comp = {}
    for m in metrics:
        try:
            c = summary.loc["creative", f"{m}_mean"]
            d = summary.loc["deterministic", f"{m}_mean"]
            comp[m] = safe(c) - safe(d)
        except KeyError:
            comp[m] = float("nan")
    comp_df = pd.DataFrame([comp])
    comp_path = f"{args.out_prefix}__creative_minus_deterministic.csv"
    comp_df.to_csv(comp_path, index=False)
    print(f">> Saved deltas (creative - deterministic): {comp_path}")

    # 7) İsteğe bağlı: basit grafikler
    if not args.no_plots:
        try:
            import matplotlib.pyplot as plt
            # E_mean dağılımı (kategoriye göre)
            for m in ["E_mean","H_token_mean","Sharpness_mean","BLEU","ROUGE_L","ECE"]:
                plt.figure()
                for cat in df["category"].dropna().unique():
                    vals = df[df["category"]==cat][m].dropna().values
                    plt.hist(vals, alpha=0.6, bins=15, label=cat, density=True)
                plt.title(f"{m} distribution by category")
                plt.xlabel(m); plt.ylabel("density")
                plt.legend()
                outp = f"{args.out_prefix}__hist_{m}.png"
                plt.savefig(outp, bbox_inches="tight"); plt.close()
                print(f">> Saved plot: {outp}")

            # E_mean vs H/Sharpness saçılımı
            for x,y in [("H_token_mean","E_mean"), ("Sharpness_mean","E_mean")]:
                plt.figure()
                for cat in df["category"].dropna().unique():
                    sub = df[df["category"]==cat]
                    plt.scatter(sub[x], sub[y], alpha=0.6, label=cat)
                plt.xlabel(x); plt.ylabel(y)
                plt.title(f"{y} vs {x} by category")
                outp = f"{args.out_prefix}__scatter_{y}_vs_{x}.png"
                plt.savefig(outp, bbox_inches="tight"); plt.close()
                print(f">> Saved plot: {outp}")
        except Exception as e:
            print(f"[WARN] Plotting skipped due to error: {e}")

    print(">> Done.")

if __name__ == "__main__":
    main()
