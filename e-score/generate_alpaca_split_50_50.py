#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
generate_alpaca_split_50_50.py
--------------------------------
Alpaca verisinden önce 50 deterministik, sonra 50 yaratıcı prompt seçip
her biri için model çıktısı (generation) üretir ve tek CSV'ye yazar.

Gereksinimler:
  pip install --upgrade datasets transformers torch

Örnek:
  python generate_alpaca_split_50_50.py \
    --n_det 50 --n_cre 50 \
    --model_id gpt2-medium \
    --max_new_tokens 100 \
    --temperature 0.9 \
    --top_p 0.95 \
    --seed 42 \
    --out alpaca_50det_50cre_with_generations.csv
"""

import argparse, re, random, hashlib, unicodedata
from typing import List, Dict, Tuple
import pandas as pd
import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed

# ---------- Heuristik sözlükleri ----------

# Deterministik sinyaller (pozitif → deterministik puanı artırır)
DET_POS = [
    r"\b(capital of|population of|gdp of|currency of|flag of)\b",
    r"\b(who is|who was|what is|what are|when did|where is)\b",
    r"\b(define|explain the term|give the definition of)\b",
    r"\b(list|enumerate|name)\b",
    r"\b(calculate|compute|derivative|integral|solve|evaluate)\b",
    r"\b(convert|translate|transliterate|uppercase|lowercase)\b",
    r"\b(distance between|area of|perimeter of|volume of)\b",
    r"\b(acronym of|abbreviation of|synonym|antonym)\b",
    r"\b(true or false|multiple choice|choose the best)\b",
    r"\b(facts?|statistics?|data)\b",
]

# Deterministik sinyaller (negatif → deterministik puanı düşürür)
DET_NEG = [
    r"\b(write|compose|imagine|invent|story|poem|haiku|sonnet|ode|elegy|lyric)\b",
    r"\b(dialogue|monologue|screenplay|scene|roleplay|worldbuild|character)\b",
    r"\b(metaphor|simile|allegory|fable|myth|parable)\b",
    r"\b(dream|surreal|liminal|cosmic|astral|lunar|moon|strange|journey)\b",
    r"\b(creative|narrative|prose|flash fiction|microfiction)\b",
]

# Yaratıcı sinyaller (pozitif → yaratıcı puanı artırır)
CRE_POS = [
    r"\b(write|compose|imagine|invent|craft|create)\b",
    r"\b(story|poem|haiku|sonnet|ode|elegy|free verse|prose)\b",
    r"\b(dialogue|monologue|screenplay|scene|script|roleplay)\b",
    r"\b(character|worldbuild|setting|tone|voice|metaphor|simile|allegory)\b",
    r"\b(dream|surreal|liminal|cosmic|astral|lunar|moon|strange|journey)\b",
    r"\b(lyrical|poetic|imagery|vignette|flash fiction|microfiction)\b",
]

# Yaratıcı sinyaller (negatif → yaratıcı puanı düşürür)
CRE_NEG = [
    r"\b(capital of|population of|gdp of|currency of|flag of)\b",
    r"\b(who is|who was|what is|what are|when did|where is)\b",
    r"\b(define|definition|list|enumerate|name)\b",
    r"\b(calculate|compute|derivative|integral|solve|evaluate)\b",
    r"\b(convert|translate|transliterate|uppercase|lowercase)\b",
]

DET_POS = [re.compile(p, flags=re.I) for p in DET_POS]
DET_NEG = [re.compile(p, flags=re.I) for p in DET_NEG]
CRE_POS = [re.compile(p, flags=re.I) for p in CRE_POS]
CRE_NEG = [re.compile(p, flags=re.I) for p in CRE_NEG]

def norm_text(t: str) -> str:
    t = unicodedata.normalize("NFKC", t or "")
    return " ".join(t.strip().split())

def fingerprint(t: str) -> str:
    """Benzer promptları tekilleştirmek için kaba parmak izi."""
    t = norm_text(t).lower()
    t = re.sub(r"[^a-z0-9\s]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    return hashlib.sha1(t.encode("utf-8")).hexdigest()

def score_with_patterns(text: str, positives: List[re.Pattern], negatives: List[re.Pattern]) -> float:
    # Basit: eşleşme başına +1 / -1; uzun promptlara küçük bonus/ceza
    score = 0.0
    for p in positives:
        if p.search(text):
            score += 1.0
    for n in negatives:
        if n.search(text):
            score -= 1.0
    # Uzunluğa hafif normalizasyon
    L = max(1, len(text.split()))
    score = score + 0.1 * min(10, L / 30.0)  # çok düşük etkili uzunluk katkısı
    return score

def pick_top_unique(items: List[Tuple[int, dict, float]], k: int) -> List[dict]:
    """Skora göre sıralı listeden, benzerleri elerken ilk k benzersiz öğeyi seç."""
    seen = set()
    picked = []
    for _, ex, _ in items:
        fp = fingerprint(ex["prompt"])
        if fp in seen:
            continue
        seen.add(fp)
        picked.append(ex)
        if len(picked) >= k:
            break
    return picked

def build_prompt(example) -> Tuple[str, str, str]:
    instr = norm_text(example.get("instruction") or "")
    inp = norm_text(example.get("input") or "")
    prompt = instr + ((" " + inp) if inp else "")
    reference = norm_text(example.get("output") or "")
    return prompt, reference, instr

def categorize_examples(dataset, n_det: int, n_cre: int, seed: int = 42) -> Tuple[List[dict], List[dict]]:
    random.seed(seed)
    det_candidates = []
    cre_candidates = []

    for i, ex in enumerate(dataset):
        prompt, reference, instr = build_prompt(ex)
        if not prompt:
            continue
        det_score = score_with_patterns(prompt, DET_POS, DET_NEG)
        cre_score = score_with_patterns(prompt, CRE_POS, CRE_NEG)
        # Deterministik önceliği: det_score - cre_score
        det_rank = det_score - max(0.0, cre_score * 0.5)
        # Yaratıcı önceliği: cre_score - det_score
        cre_rank = cre_score - max(0.0, det_score * 0.5)

        det_candidates.append((i, {"prompt": prompt, "reference": reference, "category": "deterministic"}, det_rank))
        cre_candidates.append((i, {"prompt": prompt, "reference": reference, "category": "creative"}, cre_rank))

    # Skora göre sırala (yüksekten düşüğe)
    det_sorted = sorted(det_candidates, key=lambda x: x[2], reverse=True)
    cre_sorted = sorted(cre_candidates, key=lambda x: x[2], reverse=True)

    # Benzerleri elerken seç
    det_picked = pick_top_unique(det_sorted, n_det)
    # Yaratıcı listeden deterministikte seçilenleri dışla (çeşitlilik)
    chosen_fp = {fingerprint(x["prompt"]) for x in det_picked}
    cre_filtered = [item for item in cre_sorted if fingerprint(item[1]["prompt"]) not in chosen_fp]
    cre_picked = pick_top_unique(cre_filtered, n_cre)

    return det_picked, cre_picked

def load_model(model_id: str):
    tok = AutoTokenizer.from_pretrained(model_id)
    mdl = AutoModelForCausalLM.from_pretrained(model_id)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    mdl.to(device)
    mdl.eval()
    return tok, mdl, device

def generate_text(tok, mdl, device, prompt: str,
                  max_new_tokens=100, temperature=0.9, top_p=0.95, top_k: int = 0,
                  do_sample=True) -> str:
    enc = tok(prompt, return_tensors="pt").to(device)
    gen_kwargs = dict(
        max_new_tokens=max_new_tokens,
        do_sample=do_sample,
        temperature=temperature,
        top_p=top_p
    )
    if top_k and top_k > 0:
        gen_kwargs["top_k"] = top_k
    with torch.no_grad():
        out = mdl.generate(**enc, **gen_kwargs)
    txt = tok.decode(out[0], skip_special_tokens=True)
    return txt

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n_det", type=int, default=50, help="Deterministik prompt sayısı")
    ap.add_argument("--n_cre", type=int, default=50, help="Yaratıcı prompt sayısı")
    ap.add_argument("--model_id", type=str, default="gpt2", help="HF model ID (örn. gpt2-medium, gpt2-large)")
    ap.add_argument("--max_new_tokens", type=int, default=100)
    ap.add_argument("--temperature", type=float, default=0.9)
    ap.add_argument("--top_p", type=float, default=0.95)
    ap.add_argument("--top_k", type=int, default=0)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--out", type=str, default="alpaca_50det_50cre_with_generations.csv")
    args = ap.parse_args()

    set_seed(args.seed)
    random.seed(args.seed)

    print(">> Loading dataset: yahma/alpaca-cleaned")
    ds = load_dataset("yahma/alpaca-cleaned", split="train")

    print(">> Categorizing prompts (deterministic vs creative) …")
    det_list, cre_list = categorize_examples(ds, args.n_det, args.n_cre, seed=args.seed)
    print(f"   Picked: {len(det_list)} deterministic, {len(cre_list)} creative")

    print(f">> Loading model: {args.model_id}")
    tok, mdl, device = load_model(args.model_id)

    rows = []
    # Sıra: önce deterministik 50, sonra yaratıcı 50
    for ex in det_list + cre_list:
        prompt = ex["prompt"]
        reference = ex["reference"]
        category = ex["category"]
        gen = generate_text(
            tok, mdl, device, prompt,
            max_new_tokens=args.max_new_tokens,
            temperature=args.temperature,
            top_p=args.top_p,
            top_k=args.top_k,
            do_sample=True
        )
        rows.append({
            "category": category,
            "prompt": prompt,
            "reference": reference,
            "generation": gen
        })

    df = pd.DataFrame(rows)
    df.to_csv(args.out, index=False)
    print(f">> Saved: {args.out}  ({len(df)} rows)")

if __name__ == "__main__":
    main()
