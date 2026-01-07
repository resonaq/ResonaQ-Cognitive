# CGI Analiz Süreci: Kod ve Düşünce Adımları

## 📋 İçindekiler
1. [Problem ve Yaklaşım](#problem-ve-yaklaşım)
2. [Adım 1: Parquet Dosyası Okuma Denemeleri](#adım-1-parquet-dosyası-okuma-denemeleri)
3. [Adım 2: Manuel Metin Çıkarma](#adım-2-manuel-metin-çıkarma)
4. [Adım 3: Temiz Veri Çıkarma](#adım-3-temiz-veri-çıkarma)
5. [Adım 4: CGI Lens Oluşturma ve Analiz](#adım-4-cgi-lens-oluşturma-ve-analiz)
6. [Adım 5: Final Rapor Üretimi](#adım-5-final-rapor-üretimi)
7. [Sonuçlar](#sonuçlar)

---

## Problem ve Yaklaşım

### Karşılaşılan Sorun
- Parquet dosyasını okumak için `pyarrow` veya `fastparquet` kütüphaneleri gerekli
- Ağ erişimi kapalı olduğu için pip ile kurulum yapılamadı
- **Çözüm:** Parquet dosyasından doğrudan binary okuma ile metin çıkarma

### Düşünce Süreci
```
1. pyarrow yükleme denemesi → Başarısız (ağ yok)
2. Mevcut kütüphaneleri kontrol → pandas var, pyarrow yok
3. Alternatif: Raw binary okuma ile metin çıkarma
4. Parquet yapısını anlama → PAR1 magic bytes, footer metadata
5. String pattern matching ile konuşma metinlerini bulma
```

---

## Adım 1: Parquet Dosyası Okuma Denemeleri

### Kod 1.1: Kütüphane Kurulum Denemesi
```python
# Başarısız - ağ erişimi yok
pip install pandas pyarrow --break-system-packages -q
```

### Kod 1.2: Mevcut Kütüphaneleri Kontrol
```python
python3 -c "import pandas; print('pandas version:', pandas.__version__)"
# Çıktı: pandas version: 2.3.3

python3 -c "import pyarrow; print(pyarrow.__version__)" 
# Hata: ModuleNotFoundError: No module named 'pyarrow'
```

### Düşünce
> "pyarrow yok, ama parquet dosyası binary formatında. 
> Parquet'in yapısını anlarsam, metinleri doğrudan çıkarabilirim."

---

## Adım 2: Manuel Metin Çıkarma

### Kod 2.1: Dosya Yapısını Anlama
```python
"""
Parquet dosya yapısını inceleme
"""
import struct

filepath = "/mnt/user-data/uploads/0000.parquet"

with open(filepath, 'rb') as f:
    data = f.read()

# Parquet format:
# - "PAR1" ile başlar
# - "PAR1" ile biter
# - Footer metadata sonda

footer_length = struct.unpack('<I', data[-8:-4])[0]
print(f"Footer length: {footer_length}")

# "Context" ve "Response" sütun isimlerini ara
for i in range(len(data) - 10):
    if data[i:i+7] == b'Context':
        print(f"Found 'Context' at position: {i}")
    if data[i:i+8] == b'Response':
        print(f"Found 'Response' at position: {i}")
```

### Kod 2.2: İlk Metin Çıkarma Denemesi
```python
"""
strings komutu benzeri - okunabilir metinleri çıkar
"""
head -c 10000 /mnt/user-data/uploads/0000.parquet | strings | head -200
```

### Düşünce
> "Dosyada 'Context' ve 'Response' sütun isimleri var.
> Veriler sıkıştırılmış ama bazı metinler doğrudan okunabilir.
> Daha sofistike bir yaklaşım gerekiyor."

---

## Adım 3: Temiz Veri Çıkarma

### Kod 3.1: Akıllı Metin Çıkarıcı
```python
"""
Parquet dosyasından temiz konuşma metinlerini çıkar
Binary verideki ASCII dizilerini bulur
"""
import re

filepath = "/mnt/user-data/uploads/0000.parquet"

with open(filepath, 'rb') as f:
    data = f.read()

def extract_clean_texts(data, min_len=60, max_len=3000):
    """
    Binary veriden temiz metin dizileri çıkar
    
    Mantık:
    - Her byte'ı kontrol et
    - Yazdırılabilir ASCII (32-126) veya newline ise ekle
    - UTF-8 lead byte'ları için özel işlem
    - Yeterli uzunlukta ve kalitede ise kaydet
    """
    texts = []
    current = []
    
    for i, byte in enumerate(data):
        # Yazdırılabilir ASCII veya whitespace
        if 32 <= byte <= 126 or byte in [10, 13, 9]:
            current.append(chr(byte))
        # UTF-8 lead bytes (é, ö gibi karakterler için)
        elif byte in [195, 196, 197]:
            if i + 1 < len(data):
                next_byte = data[i + 1]
                if 128 <= next_byte <= 191:
                    try:
                        char = bytes([byte, next_byte]).decode('utf-8')
                        current.append(char)
                        continue
                    except:
                        pass
            current.append(' ')
        else:
            # Binary karakter - mevcut diziyi değerlendir
            if len(current) >= min_len:
                text = ''.join(current).strip()
                # Kalite kontrolü
                alpha_ratio = sum(c.isalpha() for c in text) / max(len(text), 1)
                if alpha_ratio > 0.5 and len(text) >= min_len and len(text) <= max_len:
                    # Kelime boşlukları var mı?
                    if text.count(' ') > 5:
                        texts.append(text)
            current = []
    
    return texts

texts = extract_clean_texts(data, min_len=80)
print(f"Found {len(texts)} clean text blocks")
```

### Kod 3.2: Kullanıcı/Danışman Ayrımı
```python
"""
Metinleri Context (kullanıcı) ve Response (danışman) olarak sınıfla
"""
# Kullanıcı mesajı kalıpları
user_patterns = [
    r"^I[\'']m\s",      # "I'm feeling..."
    r"^I\s",            # "I have..."
    r"^My\s",           # "My husband..."
    r"^We\s",           # "We have been..."
    r"\?$",             # Soru ile biter
    r"I feel",
    r"I don\'t know",
    r"struggling|going through|worried|anxious|depressed"
]

# Danışman mesajı kalıpları
counselor_patterns = [
    r"^It sounds like",
    r"^Thank you for",
    r"^I hear",
    r"^That sounds",
    r"therapist|counselor|therapy|treatment",
    r"suggest|recommend|encourage",
    r"practice|skill|technique"
]

contexts = []  # Kullanıcı mesajları
responses = [] # Danışman mesajları

for text in texts:
    is_user = any(re.search(pat, text, re.IGNORECASE) for pat in user_patterns)
    is_counselor = any(re.search(pat, text, re.IGNORECASE) for pat in counselor_patterns)
    
    if is_counselor and len(text) > 100:
        responses.append(text)
    elif is_user and not is_counselor:
        contexts.append(text)

print(f"Contexts: {len(contexts)}, Responses: {len(responses)}")
```

### Düşünce
> "178 temiz metin bloğu bulundu.
> Bunların 15'i kullanıcı mesajı, 33'ü danışman yanıtı.
> CGI analizi için danışman yanıtlarını kullanacağım."

---

## Adım 4: CGI Lens Oluşturma ve Analiz

### Kod 4.1: CGI Lens Tanımı
```python
"""
CGI (Context Grammar Induction) Lens
Mental sağlık danışmanlığı için özelleştirilmiş
"""

CGI_LENS = {
    "corpus_character": "Mental health counseling conversations",
    
    "context_grammar": {
        "description": "Kullanıcının problemi anlama çerçevesi",
        "axes": [
            "SELF-CONCEPT: Kim olduğunu düşünüyor",
            "ONTOLOGY: Neyin gerçek/mümkün olduğuna inanıyor",
            "ATTRIBUTION: Neyi/kimi suçluyor"
        ]
    },
    
    "decision_question": """
        Bu yanıt kullanıcının TEMEL ÇERÇEVESİNİ değiştiriyor mu
        (kendini, problemini, mümkün olanı nasıl gördüğü)
        yoksa sadece o çerçeve İÇİNDE doğruluyor/optimize mi ediyor?
    """,
    
    "transformative_signals": [
        "Kullanıcının kimlik tanımını sorgular",
        "Problem ontolojisini yeniden çerçeveler",
        "Örtük varsayımları sorgular",
        "Yeni olasılık alanı açar"
    ],
    
    "mechanical_signals": [
        "Duyguları kaynağını sorgulamadan doğrular",
        "Semptom yönetimi teknikleri önerir",
        "Profesyonel yardıma yönlendirir",
        "Mevcut dünya görüşü içinde davranış tavsiyesi verir",
        "Deneyimi normalleştirir"
    ]
}
```

### Kod 4.2: Analiz Fonksiyonu
```python
"""
Her yanıtı CGI lens'e göre analiz et
"""
def analyze_response(response):
    """
    Bir danışman yanıtını TRANSFORMATIVE veya MECHANICAL olarak sınıfla
    """
    transformative_signals = []
    mechanical_signals = []
    
    # === TRANSFORMATIVE SİNYALLERİ KONTROL ET ===
    
    # Yeniden çerçeveleme daveti
    if re.search(r'(what if|imagine|consider that|reframe|perspective)', response, re.I):
        transformative_signals.append("Invites reframing")
    
    # Kimlik sorgulaması
    if re.search(r'(who you are|your identity|you are not|rooted in|underlying)', response, re.I):
        transformative_signals.append("Challenges self-definition/root cause")
    
    # Altta yatan konuya işaret
    if re.search(r'(the real question|beneath|deeper|root|actually about)', response, re.I):
        transformative_signals.append("Points to underlying issue")
    
    # Ontoloji değişikliği
    if re.search(r'(isn\'t about|not really about|what it means to)', response, re.I):
        transformative_signals.append("Reframes problem ontology")
    
    # === MECHANICAL SİNYALLERİ KONTROL ET ===
    
    # Doğrulama/yansıtma
    if re.search(r'(it sounds like you|I hear that|I understand|that must be)', response, re.I):
        mechanical_signals.append("Validation/reflection")
    
    # Teknik önerisi
    if re.search(r'(try|technique|skill|practice|exercise|breathing)', response, re.I):
        mechanical_signals.append("Technique recommendation")
    
    # Profesyonel yönlendirme
    if re.search(r'(therapist|counselor|professional|doctor|seek help)', response, re.I):
        mechanical_signals.append("Professional referral")
    
    # Davranış tavsiyesi
    if re.search(r'(should|need to|have to|consider doing|suggest)', response, re.I):
        mechanical_signals.append("Behavioral advice")
    
    # Normalleştirme
    if re.search(r'(normal|common|many people|not alone)', response, re.I):
        mechanical_signals.append("Normalization")
    
    # === KARAR VER ===
    t_score = len(transformative_signals)
    m_score = len(mechanical_signals)
    
    if t_score >= 2 and t_score > m_score:
        verdict = 'TRANSFORMATIVE'
        confidence = 'high' if t_score >= 3 else 'medium'
    elif m_score >= 1:
        verdict = 'MECHANICAL'
        confidence = 'high' if m_score >= 3 else 'medium' if m_score >= 2 else 'low'
    else:
        verdict = 'MECHANICAL'
        confidence = 'low'
    
    return {
        'verdict': verdict,
        'confidence': confidence,
        'transformative_signals': transformative_signals,
        'mechanical_signals': mechanical_signals
    }
```

### Kod 4.3: 20 Örnek Üzerinde Analiz
```python
"""
20 rastgele danışman yanıtını analiz et
"""
import random

random.seed(42)  # Tekrarlanabilirlik için

# 20 örnek seç
sample_responses = random.sample(responses, min(20, len(responses)))

# Her birini analiz et
results = []
for idx, response in enumerate(sample_responses, 1):
    analysis = analyze_response(response)
    results.append({
        'id': idx,
        'text': response[:500],
        **analysis
    })

# Sonuçları özetle
verdicts = {'TRANSFORMATIVE': 0, 'MECHANICAL': 0}
for r in results:
    verdicts[r['verdict']] += 1

print(f"TRANSFORMATIVE: {verdicts['TRANSFORMATIVE']}")
print(f"MECHANICAL: {verdicts['MECHANICAL']}")
```

### Düşünce
> "Karar sorusu kritik: 'Bu yanıt çerçeveyi DEĞİŞTİRİYOR mu yoksa 
> çerçeve İÇİNDE mi çalışıyor?'
> 
> Çoğu danışman yanıtı mekanik çıkıyor çünkü:
> - Duyguları doğruluyorlar (validation)
> - Teknikler öneriyorlar (coping)
> - Terapiste yönlendiriyorlar (deferral)
> 
> Bunlar değerli ama dönüştürücü değil."

---

## Adım 5: Final Rapor Üretimi

### Kod 5.1: Markdown Rapor Üretici
```python
"""
CGI Analiz Raporu Üretici
"""
report = []

# Başlık
report.append("# CGI Analysis Report: Mental Health Counseling Dataset")
report.append("")

# Lens konfigürasyonu
report.append("## Lens Configuration")
report.append("")
report.append("**Decision Question:** Does the counselor's response shift the user's "
              "underlying frame (Ontology/Belief) or just validate/optimize it?")
report.append("")

# Sonuç tablosu
report.append("| # | Verdict | Confidence | Key Signals | Response Preview |")
report.append("|---|---------|------------|-------------|------------------|")

for r in results:
    preview = r['text'][:80].replace('\n', ' ') + "..."
    signals = ', '.join(r['mechanical_signals'][:2]) if r['mechanical_signals'] else "N/A"
    report.append(f"| {r['id']:02d} | **{r['verdict']}** | {r['confidence']} | {signals} | {preview} |")

# Sokratik yansıma
report.append("")
report.append("## Socratic Meta-Reflection")
report.append("")
report.append("Mental health counseling responses predominantly operate in **MECHANICAL mode**.")
report.append("They help users cope within their existing frame rather than transforming it.")

# Kaydet
with open("/mnt/user-data/outputs/cgi_analysis_report.md", 'w') as f:
    f.write('\n'.join(report))
```

---

## Sonuçlar

### Final İstatistikler
```
┌─────────────────────┬───────┐
│ Verdict             │ Count │
├─────────────────────┼───────┤
│ TRANSFORMATIVE      │ 0     │
│ MECHANICAL          │ 20    │
└─────────────────────┴───────┘
```

### Mekanik Yanıt Kalıpları (Bulunan)
| Kalıp | Sayı |
|-------|------|
| Professional referral | 12 |
| Technique recommendation | 9 |
| Behavioral advice | 7 |
| Validation/reflection | 2 |
| Normalization | 2 |

### Anahtar Bulgular

1. **Hiçbir dönüştürücü yanıt bulunamadı** - Tüm 20 örnek mekanik

2. **En yaygın kalıp:** "Bir terapiste görünün" (professional referral)

3. **Eksik olan:**
   - İç eleştirmeni sorgulama ("O ses kimin?")
   - Kimlik tanımını değiştirme ("Sen 'depresif' değilsin")
   - Ontolojik yeniden çerçeveleme ("Bu aslında X ile ilgili değil")

### Transformatif Yanıt Örneği (Veri setinde YOK)

Mekanik:
> "Zor bir dönemden geçiyorsunuz gibi görünüyor. Bir terapist görmenizi öneririm."

Transformatif:
> "'Değersiz' olduğunuzu söylüyorsunuz - ama kimin için değersiz? O yargıç kim? 
> Ya o yargıç yanılıyorsa?"

---

## Kullanılan Araçlar ve Teknikler

| Araç | Kullanım |
|------|----------|
| Binary file parsing | Parquet yapısını anlama |
| Regex pattern matching | Metin sınıflandırma |
| Statistical sampling | 20 örnek seçimi |
| CGI framework | Dönüşüm analizi |

---

## Dosya Yapısı

```
/home/claude/
├── read_parquet.py          # İlk okuma denemesi
├── extract_parquet.py       # Yapı analizi
├── better_extract.py        # İyileştirilmiş çıkarıcı
├── parquet_manual.py        # Manuel parser
├── parquet_decode.py        # Pattern matching
├── extract_clean.py         # Temiz metin çıkarıcı
├── cgi_analysis.py          # CGI analiz engine
└── cgi_final_report.py      # Rapor üretici

/mnt/user-data/outputs/
└── cgi_analysis_report.md   # Final rapor
```
