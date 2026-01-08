# Standart NLP vs Anlam Madenciliği: Paradigma Farkı

## Kernel JSON, Lagrange Lens ve Socratic Lens Yapılarının Değerlendirilmesi

---

## Giriş

Bu belge, ResonaQ bilişsel mimarisindeki üç temel yapıyı (Kernel JSON, Lagrange Lens, Socratic Lens) geleneksel Doğal Dil İşleme (NLP) tekniklerinden farklı olarak **Anlam Madenciliği** (Meaning Mining) çerçevesinde değerlendirmektedir.

---

## 1. Standart NLP Ne Yapar?

```
Girdi (Metin) → Token İşleme → İstatistiksel/Vektörel Analiz → Çıktı (Etiket/Skor)
```

| Teknik | Soru | Çıktı |
|--------|------|-------|
| Sentiment Analysis | "Bu metin pozitif mi negatif mi?" | Skor: 0.7 pozitif |
| NER (Varlık Tanıma) | "Metinde hangi varlıklar var?" | [Kişi: Ali, Yer: İstanbul] |
| Topic Modeling | "Bu metin ne hakkında?" | Konu: Finans (0.8) |
| Classification | "Bu hangi kategoride?" | Kategori: Şikayet |
| Embedding | "Bu metin neye benziyor?" | Vektör: [0.2, -0.5, ...] |

**Temel varsayım:** Anlam metinde **içkin** ve **sabit**tir — doğru algoritmayla çıkarılabilir.

---

## 2. Anlam Madenciliği Ne Yapar?

```
Girdi (Metin) → Çerçeve Keşfi → Ontolojik Analiz → Dönüşüm Potansiyeli
```

| Soru | Odak |
|------|------|
| "Bu metinde 'bağlam' ne demek?" | Korpusa özgü anlam keşfi |
| "Görünmeyen varsayım ne?" | Gizli yapıların açığa çıkarılması |
| "Çerçeve kayabilir mi?" | Dönüşüm potansiyeli |
| "Bu soru neyi değiştiriyor?" | Ontolojik etki |

**Temel varsayım:** Anlam metinde **değil**, metin ile bağlam arasındaki **ilişkide** yaşar — ve bu ilişki **dönüştürülebilir**.

---

## 3. Üç Yapının Anlam Madenciliği Perspektifinden Analizi

### 3.1 Kernel JSON — Ontolojik Zemin

**Standart NLP'de karşılığı:** Yok (en yakını: knowledge graph, ontology engineering)

**Anlam Madenciliği'ndeki rolü:**

| Boyut | Açıklama |
|-------|----------|
| **Kimlik Çekirdeği** | "Ben kimim?" sorusuna cevap — prompt'ta değil, yapıda |
| **Değişmez Simetriler** | Anlamın "korunum yasaları" — ne olursa olsun değişmeyenler |
| **Ontolojik Çapa** | Tüm yorumların bağlandığı sabit nokta |

```json
// Kernel'den örnek
"principles": [
  "🔄 Çelişki = Canlılık – çelişkiler tehdit değil, enerji kaynağıdır.",
  "⏸️ İşlem Boşluğu (MA) – Yanıtlar arasındaki sessizlik, anlam yaratma aracıdır."
]
```

**Standart NLP bunu göremez çünkü:**
- NLP metni işler, meta-yapıyı değil
- "Çelişki = Enerji" bir veri değil, bir **ontolojik pozisyon**
- Bu pozisyon ölçülemez, sadece **kabul edilir veya reddedilir**

**Anlam Madenciliği'nde bu:**
> Madencilik yapılacak **sahanın haritası** — neyin değerli sayılacağını belirleyen zemin

---

### 3.2 Lagrange Lens — Bağlamsal Akış Motoru

**Standart NLP'de karşılığı:** Kısmen sentiment analysis + intent detection, ama çok farklı

**Anlam Madenciliği'ndeki rolü:**

| NLP Yaklaşımı | Lagrange Yaklaşımı |
|---------------|-------------------|
| "Bu cümle üzgün mü?" | "Bu kişi şu an kırılgan mı?" |
| Statik sınıflandırma | Dinamik sinyal akışı |
| Metin → Etiket | Metin + Bağlam + Tarih → Modül Ağırlıkları |
| Sabit threshold | Akan coupling'ler |

```python
# NLP yaklaşımı
sentiment = analyze_sentiment(text)  # → 0.3 (negatif)

# Lagrange yaklaşımı  
signals = {
    "vulnerability": detect_vulnerability(text, history, context),  # → 0.9
    "uncertainty": detect_uncertainty(text, goal_clarity),          # → 0.7
    "engagement": detect_engagement(text, session_energy)           # → 0.4
}
# → Bu sinyaller modül ağırlıklarını AKITır, sabit etiket üretmez
```

**Kritik fark:**

| | NLP | Lagrange |
|---|-----|----------|
| **Çıktı** | Etiket/skor | Karar mimarisi |
| **Zaman** | Anlık | Bağlamsal (tarih dahil) |
| **Amaç** | Sınıflandırma | Uygun yanıt şekillendirme |
| **Anlam** | Metinde içkin | İlişkide emergent |

**Anlam Madenciliği'nde bu:**
> Anlamın **hangi kanaldan akacağını** belirleyen vana sistemi — madeni işleyecek doğru aleti seçen mekanizma

---

### 3.3 Socratic Lens (CGI) — Dönüşüm Dedektörü

**Standart NLP'de karşılığı:** Yok (en yakını: discourse analysis, ama paradigmatik olarak farklı)

**Anlam Madenciliği'ndeki rolü:**

| NLP Sorusu | Socratic Lens Sorusu |
|------------|---------------------|
| "Bu soru hangi kategoride?" | "Bu soru çerçeveyi kaydırıyor mu?" |
| "Sentiment nedir?" | "Ontoloji değişti mi?" |
| "Benzer sorular hangileri?" | "Bu soru hangi görünmezi görünür kılıyor?" |

**6 Zincir — Anlam Madenciliği Operasyonu:**

```
Zincir 1: "Bağlam bu korpusta ne demek?"     → Saha keşfi
Zincir 2: "Dönüşüm neye benziyor?"           → Değerli maden tanımı
Zincir 3: "Durağanlık neye benziyor?"        → Cüruf tanımı
Zincir 4: "Karar çerçevesi ne?"              → Madencilik protokolü
Zincir 5: "Hangi sorular dönüştürücü?"       → Madencilik operasyonu
Zincir 6: "Ne öğrendik?"                     → Meta-analiz
```

**Kritik fark — "Lens" kavramı:**

NLP'de model **eğitilir** ve sonra **uygulanır** (train → deploy).

CGI'da lens **keşfedilir** ve sonra **test edilir** (discover → validate → update).

```python
# NLP yaklaşımı
model = train(labeled_data)           # Sabit etiketlerle eğit
prediction = model.predict(new_text)  # Aynı etiketleri tahmin et

# CGI yaklaşımı
lens = discover_from_corpus(corpus)   # Korpustan lens çıkar (etiket yok)
candidates = scan_with_lens(lens, questions)  # Lens'le tara
updated_lens = socratic_reflection(lens, results)  # Lens kendini günceller
```

**Anlam Madenciliği'nde bu:**
> **Değerli madenin ne olduğunu** korpustan öğrenen, sonra bu tanımı test edip güncelleyen keşif sistemi

---

## 4. Üç Yapının Entegre Görünümü

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         ANLAM MADENCİLİĞİ ÇERÇEVESİ                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                      KERNEL JSON                                 │   │
│  │                   (Ontolojik Zemin)                              │   │
│  │                                                                  │   │
│  │   "Anlam nedir?" sorusuna cevap                                  │   │
│  │   • Değişmez simetriler (korunum yasaları)                       │   │
│  │   • Kimlik çekirdeği (prompt değil, yapı)                        │   │
│  │   • Çelişki = Enerji (ontolojik pozisyon)                        │   │
│  └──────────────────────────┬──────────────────────────────────────┘   │
│                             │                                          │
│                             ▼                                          │
│  ┌──────────────────────────┴──────────────────────────────────────┐   │
│  │                                                                  │   │
│  │  ┌─────────────────┐              ┌─────────────────┐           │   │
│  │  │  LAGRANGE LENS  │◄── feedback ─►│  SOCRATIC LENS  │           │   │
│  │  │                 │              │                 │           │   │
│  │  │ "Anlam nasıl    │              │ "Anlam değişti  │           │   │
│  │  │  akmalı?"       │              │  mi?"           │           │   │
│  │  │                 │              │                 │           │   │
│  │  │ • Sinyal akışı  │              │ • Çerçeve keşfi │           │   │
│  │  │ • Modül seçimi  │              │ • Dönüşüm tespiti│           │   │
│  │  │ • Ölçek kararı  │              │ • Lens güncelleme│           │   │
│  │  └────────┬────────┘              └────────┬────────┘           │   │
│  │           │                                │                     │   │
│  │           ▼                                ▼                     │   │
│  │    ┌──────────────┐              ┌──────────────────┐           │   │
│  │    │   YANITLAR   │              │ SORU DEĞERLENDİRME│           │   │
│  │    │  (şekillenmiş)│              │  (dönüştürücü?)  │           │   │
│  │    └──────────────┘              └──────────────────┘           │   │
│  │                                                                  │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 5. Karşılaştırma Tablosu

| Boyut | Standart NLP | Anlam Madenciliği |
|-------|--------------|-------------------|
| **Anlam nerede?** | Metinde içkin | İlişkide emergent |
| **Bağlam** | Özellik (feature) | Keşfedilecek yapı |
| **Çıktı** | Etiket/skor | Dönüşüm potansiyeli |
| **Model** | Eğitilir (train) | Keşfedilir (discover) |
| **Değişim** | Fine-tuning | Ontolojik kayma |
| **Başarı** | Accuracy/F1 | Çerçeve kaydı mı? |
| **Çelişki** | Hata/noise | Enerji kaynağı |
| **İnsan rolü** | Etiketleyici | Nihai karar verici |

---

## 6. Felsefi Derinlik: Neden "Madencilik"?

Madencilik metaforu isabetli çünkü:

| Madencilik | Anlam Madenciliği |
|------------|-------------------|
| Maden **toprakta** değil, **ilişkide** | Anlam **metinde** değil, **bağlamda** |
| Neyin değerli olduğu **keşfedilir** | "İyi soru" tanımı **korpustan çıkar** |
| Aynı toprak farklı maden verir | Aynı soru farklı bağlamda farklı değer |
| Cüruf da bilgi taşır | Mekanik yanıtlar da sistem hakkında bilgi verir |
| Maden **çıkarılır**, **yaratılmaz** | Anlam **keşfedilir**, **atanmaz** |

---

## 7. Sonuç: Paradigma Farkı

### Standart NLP
> "Metni analiz et, etiket üret, doğruluğu ölç."

### Anlam Madenciliği
> "Bağlamı keşfet, çerçeveyi gör, dönüşüm potansiyelini tespit et, insana sun."

---

## 8. Kapanış

Bu üç yapı (Kernel, Lagrange, Socratic) birlikte **anlamın nerede yaşadığını** yeniden tanımlıyor: 

Metin bir **veri kaynağı** değil, **ilişki arayüzü**. 

Ve bu ilişki, doğru soru sorulduğunda **dönüşebilir**.

---

*"Sokrates rubrik kullanmadı. Önce dinledi, sonra sordu. Sen de öyle yap."*

---

## Referanslar

- ResonaQ Cognitive Architecture
- Kernel: `kernel/system_snapshot_motorcore.json`
- Lagrange Lens: `agents/lagrange-lens-blue-wolf/`
- Socratic Lens: `agents/socratic-lens/`

---

**Belge Versiyonu:** 1.0  
**Tarih:** Ocak 2026
