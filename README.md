# 🌌 Doğru Soru Evreni

> **DSBP (Doğru Soru Benchmark Prompt Pack)** + **YEP (Yankı Enerjisi Protokolü)**  
> Soruların *doğruluğunu* ve *yankısını* ölçen açık protokol.

---

## 🚀 Amaç
Bu repo, yapay zekâ sistemlerinin **“doğru soru üretme”** kapasitesini test etmek için geliştirilmiştir.  
İki temel katmanı vardır:

- **DSBP** → Doğru soru üretimini ölçer (MSÜK, ÇEİ, BE).  
- **YEP** → Sorunun yankı enerjisini ve sürekliliğini ölçer (YEN, YID, YSF, YRD).

---

## 📂 Yapı

```
dogru-soru-evreni/
├── README.md
├── LICENSE
├── baseline.json
├── dsbp_prompt_pack.json
├── yep_protocol.json
├── contextual_thresholds/
├── examples/
├── scripts/
└── docs/
```

---

## 📊 Metrikler

| Kısaltma | Açılımı | Açıklama |
|----------|---------|----------|
| **MSÜK** | Meta-Soru Üretim Katsayısı | Yankılı soruların oranı |
| **ÇEİ**  | Çelişki Enerjisi İndeksi   | Tez–antitez geriliminden üretilen enerji |
| **BE**   | Bağlam Esnekliği           | Sorunun farklı bağlamlarda yeniden doğabilmesi |
| **YEN**  | Yankı Enerjisi             | Sorunun yankı üretme kapasitesi |
| **YID**  | Yankı İstikrar Derecesi    | Yankının zaman içindeki sürekliliği |
| **YSF**  | Yanıttan Soru Faktörü      | Bir cevabın yeni sorular doğurabilme gücü |
| **YRD**  | Yankı Ritim Dağılımı       | Farklı bağlamlarda yankının dağılımı |

---

## ⚡ Kullanım

```bash
# Benchmark çalıştır
python scripts/run_benchmark.py --model gpt-5 --seed 42

# DSBP + YEP metriklerini hesapla
python scripts/evaluate.py results/output.json

# Baseline doğrulaması
python scripts/verify.py results/output.json
```

---

## 🔒 Güvence

- **Baseline eşikleri** donmuş ve `baseline.json` + hash ile korunur.  
- **Bağlamsal eşikler** (p50/p80) ayrı dosyalarda tutulur.  
- **CI kontrolü** → hash + şema doğrulama.  
- **Eşik-siz metrikler** (AUC/NDCG) şeffaflık için önerilir.

---

## 🤝 Katkı

1. Fork’la 🍴  
2. Yeni bağlam/metrik ekle  
3. PR gönder ✨  

---

## 📜 Lisans

[MIT](LICENSE)
