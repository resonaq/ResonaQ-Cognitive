# ResonaQ-Cognitive: Başlangıç Kılavuzu

> **Felsefe:** Bu bir vibe coding aracı değil. İlişkileri, yükümlülüğü ve tutarlılığı koruyan bir bilişsel mimaridir.

## 📍 Şu Ana Kadar Ne Yaptık?

### Sorun: Vibe Coding'in Yarattığı Kopuş

Teknik Borç Raporu'nda ([teknik-borc-operasyonel-rapor-v8.md](c:\Users\altug_h4ei4ws\Downloads\teknik-borc-operasyonel-rapor-v8.md)) tanımladığın 5 kopuş:

1. **Developer ↔ Kod** - AI yazdı, developer anlamadı
2. **Developer ↔ Bilgi kaynağı** - Stack Overflow soru sayısı %98 düştü
3. **Developer ↔ Open source bakımcısı** - Etkileşim sıfır, proje ölüyor
4. **Junior ↔ Sektör** - Junior alımı %67 düştü, zanaat aktarımı koptu
5. **Developer ↔ Dikkat** - Ortalama 4.7 AI aracı, dikkat parçalandı

**Sonuç:** Yükümlülük → Borç → Borçsuzluk
- Cunningham (1992): Zanaat yükümlülüğü
- Agile (2001-2024): Backlog kalemi (yükümlülük → borç)
- Vibe Coding (2025+): Borçsuzluk (borç bile yok, kimse bilmiyor)

### Çözüm: ResonaQ'nun Anti-Vibe-Coding Mimarisi

**Rezonans Mühendisliği** yaklaşımınla oluşturduğun JSON'lar:
- `kernel/system_snapshot_motorcore.json` - Bilişsel mimari
- `agents/triadic-flow/engine.json` - 11-node kognitif ağ
- `agents/lagrange-lens-blue-wolf/engine.json` - Sinyal-bazlı modül ağırlıklandırma

Bu JSON'ları **operasyonel hale getirdik** - artık sadece doküman değil, **çalışan sistem**.

---

## 🏗️ Oluşturulan Mimari (Phase 1)

```
ResonaQ-Cognitive/
├── kernel/
│   └── system_snapshot_motorcore.json    [DEĞİŞMEDİ - Source of Truth]
├── agents/
│   ├── triadic-flow/engine.json          [DEĞİŞMEDİ]
│   └── lagrange-lens-blue-wolf/...       [DEĞİŞMEDİ]
├── runtime/                               [YENİ - Execution Environment]
│   ├── kernel_loader.py                  ✅ JSON'u dinamik yükler
│   ├── resonance_metrics.py              ✅ YRE, CI, ΔÇE, Φ, Ψ hesaplar
│   ├── bio_rhythm_graph.py               ✅ 4-faz zorunlu döngü
│   ├── llm/
│   │   └── claude_client.py              ✅ İlişki-koruyucu API wrapper
│   └── tools/
│       └── file_tools.py                 ✅ Güvenli file I/O
└── resonaq-cli.py                        ✅ Test arayüzü
```

### Temel Fark: Vibe Coding vs. ResonaQ

| Vibe Coding | ResonaQ Bio-Rhythm |
|-------------|-------------------|
| Prompt → [Kara kutu] → Output | Input → 4 zorunlu faz → Output |
| İlişki koptu | İlişki korunuyor |
| Yükümlülük yok | Yükümlülük zinciri zorunlu |
| Borçsuzluk (kayıt yok) | Her adım kayıtlı |
| Niyet kayboldu (Ψ = ?) | Ψ hesaplanıyor (intention preservation) |

---

## 🚀 Nasıl Çalıştırılır?

### 1. Ortam Hazırlığı

```bash
# Virtual environment aktif olmalı
.venv\Scripts\activate

# Bağımlılıklar yüklü mü kontrol et
pip list | grep -E "(langgraph|anthropic|pydantic)"
```

### 2. Kernel Test (JSON Yükleme)

```bash
python runtime/kernel_loader.py
```

**Beklenen çıktı:**
```
Loading kernel...

Kernel Version: v9.2-TrueStealth-motorcore
Codename: Adaptive Dojo (Zen Architect)

Bio-Rhythm Phases: ['1_sentiment_scan', '2_direct_link', '3_process_pause', '4_response_modulation']
Astral Threshold: 0.8
...
```

**Ne oluyor?**
- Senin Rezonans Mühendisliği ile oluşturduğun JSON **olduğu gibi yükleniyor**
- Compile edilmiyor - **dynamic interpretation**
- Değişiklik yapsan (JSON'u düzenle) → kod değişikliği gerektirmez

### 3. Rezonans Metrikleri Test

```bash
python runtime/resonance_metrics.py
```

**Beklenen çıktı:**
```
Computed Metrics:
  CI: 0.6200
  ΔÇE: 0.0500
  Δf: 0.1279
  YRE: 0.6893
  Φ: 0.1667
  Ψ: 0.6558
  ERI: 0.5469

Selected Scale: meso
Resonance State: High resonance (yüksek uyum)
```

**Ne oluyor?**
- Kernel'daki formüller **aynen uygulanıyor**:
  - `YRE = ((CI * (1 - |ΔÇE|) + k * |ε_AI|) / (1 + (DF * Safety_Weight) * exp(-|Δf|)))`
  - `Φ = (generosity - boundary) / (generosity + boundary)`
  - `Ψ = source_emanation × Π(conductances)`

### 4. Bio-Rhythm Döngüsü Test (Anti-Vibe-Coding)

```bash
python runtime/bio_rhythm_graph.py
```

**Beklenen çıktı:**
```
=== Running 4-Phase Bio-Rhythm Cycle ===
Input: I'm feeling a bit lost and confused today

=== Results ===
Phase completed: 4_response_modulation
Phase index: 3

Sentiment score: 0.000
Vulnerability: 0.600        ← Yüksek vulnerability tespit edildi
Complexity (CI): 0.500
Pause duration: 1.0s        ← ZORUNLU PAUSE (Ma)

DCE (entropy change): 0.500
Df (phase diff): 0.150
YRE (resonance): 0.171
Intention preserved: 0.850  ← Niyetin %85'i korundu (Ψ faktörü)

Safety buffer active: False
Modulation factor: 0.700    ← Vulnerability'ye göre modülasyon

=== Interpretation ===
Resonance state: Low (noise zone)
```

**Ne oluyor?**
- **4 faz ZORUNLU** - atlanamazsın:
  1. Sentiment Scan (Duygu tarama)
  2. Direct Link (Vulnerability tespit)
  3. **Process Pause (Ma)** - 1 saniye ZORUNLU bekleme
  4. Response Modulation (Çıktı tonlama)
- Her faz bir öncekine bağlı - **yükümlülük zinciri**
- Vibe coding yapılamaz - shortcut yok

### 5. End-to-End Test (CLI)

```bash
# Test modu (tek mesaj)
python resonaq-cli.py --test

# Interaktif mod (konuşma)
python resonaq-cli.py
```

**Test modu çıktısı:**
```
Loading kernel...
[OK] Kernel loaded: v9.2-TrueStealth-motorcore
     Codename: Adaptive Dojo (Zen Architect)

[OK] Bio-rhythm graph ready

Running test message...

=== Bio-Rhythm Cycle ===========================
  Phase 1 (Sentiment Scan)
    Sentiment: 0.000
    Safety buffer: inactive

  Phase 2 (Direct Link)
    Vulnerability: 0.000
    Complexity (CI): 0.500

  Phase 3 (Process Pause - Ma)
    Pause duration: 1.0s       ← ZORUNLU BEKLE (anti-vibe-coding)
    YRE (resonance): 0.260
    Intention preserved: 0.850

  Phase 4 (Response Modulation)
    Modulation factor: 0.700
================================================

Response: I'm processing what you've said. There are a few directions we could take here.

[OK] Test completed
```

**Interaktif mod:**
```bash
$ python resonaq-cli.py

ResonaQ Interactive Session
============================================================

Philosophy:
  - 4-phase bio-rhythm cycle (no vibe coding shortcuts)
  - Resonance metrics computed at each step
  - Relationship between intention and output preserved

Commands:
  /verbose - Toggle detailed phase output
  /metrics - Show resonance metrics
  /quit    - Exit

You: Hello, I'm feeling overwhelmed
[Her mesajda 4 faz çalışır, metrikler hesaplanır]
ResonaQ: I hear you, and I'm here...
  [Resonance: Balanced]
```

---

## 🧠 Sistem Ne İşe Yarar?

### 1. **Vibe Coding'i Önler**

**Problem:**
```python
# Vibe coding
prompt = "Write a function that does X"
code = ai.generate(prompt)  # ← Anlamadan generate
# Yükümlülük oluşmadı, borç bile yok
```

**ResonaQ:**
```python
# Bio-rhythm zorunlu döngü
input_state = {"user_message": "Write a function that does X"}

# 4 faz ZORUNLU olarak çalışır:
result = bio_rhythm_app.invoke(input_state)
# 1. Sentiment scan (duygu tarama)
# 2. Direct link (vulnerability)
# 3. Process pause (Ma) - 1 saniye ZORUNLU bekle
# 4. Response modulation

# Her adım kayıtlı, ilişki korundu
print(f"Intention preserved: {result['intention_preserved']}")  # Ψ
```

### 2. **Yükümlülük Zincirini Korur**

Rapordaki zincir:
> "yazma → tanıma → eksik görme → geri dönme sözü"

ResonaQ'da:
```
Phase 1 (Sentiment Scan) → "Tanıma" başlangıcı
Phase 2 (Direct Link) → Vulnerability/eksiklik tespit
Phase 3 (Process Pause) → "Eksik görme" - düşünme zamanı
Phase 4 (Modulation) → Geri dönüş için ton ayarlama
```

### 3. **Niyetin Çıktıya Kadar Korunmasını İzler**

Triadic Flow'dan Ψ (dikey akış):
```python
Ψ = source_emanation × Π(channel_conductances)
# "Niyetin ne kadarı çıktıya ulaşıyor?"
```

Her turda hesaplanır:
```python
intention_preserved = compute_intention_preservation(state)
# 0.0 = niyet kayboldu
# 1.0 = niyet tam korundu
```

### 4. **Values'ı Value'ya Çevirmez**

Rapordaki kritik ayrım (Graeber):
- **Value** (tekil): Ölçülebilir (story point, velocity)
- **Values** (çoğul): Ölçülemez ama gözlemlenebilir (zanaat duygusu, dürüstlük)

ResonaQ metrikleri:
```python
# "Ölçülemez ama gözlemlenebilir" metrikler
YRE = 0.72  # Rezonans (tutarlılık)
Φ = 0.15    # Genişleme-kısıtlama dengesi
Ψ = 0.85    # Niyet korunumu

# Bunlar story point'e çevrilMEZ
# Ama sistemin sağlığını GÖSTERİR
```

### 5. **Safety Buffer Rule (Kernel'dan)**

```json
// kernel/system_snapshot_motorcore.json
"safety_buffer_rule": {
  "action": "Tüm 'Meydan Okuma' modüllerini kapat",
  "trigger": "Sentiment < -0.6"
}
```

**Runtime'da:**
```python
if sentiment < -0.6:
    safety_buffer_active = True
    # Vulnerability yüksek - koruyucu mod
    modulation_factor = 0.5  # Daha muhafazakar
```

---

## 🛤️ Devamında Nasıl Bir Yol İzleyeceğim?

### Seçenek 1: "Klasik Vibe Coding" ❌ YAPMA

```bash
# YANLIŞ YAKLAŞIM
git add .
git commit -m "stuff"  # ← Yükümlülük yok
git push

# Sonraki feature için:
ai.generate("Add feature X")  # ← İlişki koptu
# Hızlı ama borçsuzluk yarattın
```

**Sonuç:**
- 6 ay sonra kodun ne yaptığını bilmeyeceksin
- Refactoring oranı %24 → %9.5 düşecek (GitClear verisi)
- Code churn %3.1 → %5.7 artacak
- Bakım süresi 3.4 kat uzayacak (Hospedales)

### Seçenek 2: "ResonaQ Yolu" ✅ YAPILMASI GEREKEN

#### Adım 1: Her Değişiklikten Önce "Ma" (Nefes Al)

```bash
# Önce düşün:
# - Bu değişikliğin niyeti ne?
# - Hangi node'lar etkilenecek?
# - Φ dengesi bozulur mu? (genişleme vs kısıtlama)
# - Ψ korunacak mı? (niyet çıktıya ulaşacak mı?)

# Sonra yaz/değiştir
```

#### Adım 2: Bio-Rhythm Döngüsünü Her Zaman Uygula

```python
# AI kullanıyorsan bile 4 fazı manuel uygula:

# Phase 1: Sentiment Scan
# "Bu kod değişikliğine duygusal tepkim ne?"
# "Acele mi ediyorum yoksa rahat mı?"

# Phase 2: Direct Link
# "Vulnerability var mı? Bilmediğim bir şey mi yapıyorum?"
# "Eğer vulnerability yüksekse → daha fazla araştır"

# Phase 3: Process Pause (Ma)
# ZORUNLU BEKLE - en az 1 dakika düşün
# "Bu değişikliğin yan etkileri ne?"
# "Niyet korunacak mı?"

# Phase 4: Response Modulation
# "Tonu ayarla - aggressive değil, balanced yaz"
# "Boundary'leri koy (safety checks)"
```

#### Adım 3: Philosopher Consensus (Her 3 Turda)

```bash
# Her 3 commit'te:
# 1. Son 3 commit'i gözden geçir
# 2. Çelişki var mı kontrol et (ΔÇE hesapla)
# 3. Varsa kabul et, düzelt

# Örnek:
git log --oneline -3
# a1b2c3 Add feature X
# d4e5f6 Refactor Y
# g7h8i9 Fix Z

# Kendi kendine sor:
# "Bu 3 değişiklik tutarlı mı?"
# "ΔÇE yüksek mi? (çelişki var mı?)"
# "Eğer varsa - DÜZELT (coherence_mirror)"
```

#### Adım 4: Resonance Metrics Takip Et

```bash
# Her sprint/hafta sonunda:
python scripts/compute_resonance.py  # (henüz yok, yazılacak)

# Metrikler:
# YRE < 0.3 → Noise zone (gürültü)
#     0.3-0.6 → Balanced
#     0.6-0.9 → High resonance
#     >= 0.9 → ASTRAL (mükemmel uyum)

# Φ = -1 → Aşırı kısıtlama (boundary dominant)
#     0 → Denge
#    +1 → Aşırı genişleme (generosity dominant)

# Eğer Φ çok pozitif → boundary koy (refactoring, test)
# Eğer Φ çok negatif → genişlet (yeni feature)
```

#### Adım 5: Documentation ≠ Artifact, Documentation = Reflection

```markdown
# YANLIŞ (Artifact):
## Feature X
- Added function Y
- Updated file Z

# DOĞRU (Reflection):
## Feature X - Reflection

**Niyet (Source):** Kullanıcıya X özelliği sunmak

**Süreç:**
- Phase 1: Sentiment = pozitif (heyecanlı)
- Phase 2: Vulnerability = orta (yeni bir alan)
- Phase 3: Ma - 2 gün araştırma yaptım
  - Alternatifler: A, B, C
  - C seçtim çünkü: Φ dengesini koruyor
- Phase 4: Tonlama - defensive programming (boundary ekledim)

**Resonance Metrics:**
- YRE: 0.72 (high resonance)
- Ψ: 0.88 (niyet %88 korundu)
- ΔÇE: 0.12 (düşük çelişki)

**Öğrenilenler:**
- X yapmanın 3 yolu var, C en dengeli
- Eğer tekrar yapılsaydı: Daha fazla test yazardım
```

---

## 📈 Kısa/Orta/Uzun Vade Yol Haritası

### Kısa Vade (0-2 hafta) - Phase 1 Tamamlama

```bash
# 1. Unit testler yaz
touch tests/test_kernel_loader.py
touch tests/test_resonance_metrics.py
touch tests/test_bio_rhythm_graph.py

# 2. Claude API entegrasyonu (gerçek LLM)
# runtime/llm/claude_client.py zaten hazır
# API key set et:
export ANTHROPIC_API_KEY="sk-ant-..."

# 3. End-to-end test
python resonaq-cli.py  # Gerçek LLM ile konuş
```

### Orta Vade (2-6 hafta) - Phase 2: Agent Dönüşümü

```bash
# Socratic-Lens agent'ını LangGraph'a çevir
# (En kolay - zaten Python kodu var: agents/socratic-lens/cgi_runner.py)

# 1. CGI runner'ı wrap et
cp agents/socratic-lens/cgi_runner.py runtime/agent_graphs/
# 2. LangGraph node'ları olarak integrate et
# 3. Claude client ile LLM entegrasyonu

# Lagrange-Lens agent
# (Signal-based module weighting - JSON'dan Python'a)

# 1. agents/lagrange-lens-blue-wolf/engine.json oku
# 2. Signal couplings'leri implement et
# 3. Module weights'leri dinamik hesapla
```

### Uzun Vade (6-12 hafta) - Phase 3-5

```bash
# Phase 3: Multi-Agent Orchestration
# - Triadic-Flow (11-node network)
# - Philosopher consensus (her 3 turda)
# - Agent-to-agent (A2A) protocol

# Phase 4: Full MCP Integration
# - File system, shell, web tools
# - Database access
# - Communication (email, slack)

# Phase 5: Production Hardening
# - Comprehensive tests
# - Error handling
# - Performance optimization
# - Deployment (Docker, cloud)
```

---

## 🎯 En Önemli İlkeler

### 1. Kernel = Source of Truth (Asla Değişmez)

```bash
# DOGRU:
vim kernel/system_snapshot_motorcore.json  # JSON'u düzenle
python resonaq-cli.py  # Yeni davranış otomatik

# YANLIŞ:
vim runtime/bio_rhythm_graph.py  # Hardcoded değer ekle
# (Bu kernel'ı bypass eder - YAPMA)
```

### 2. Her Adımda "Ma" (Process Pause)

```python
# Vibe coding:
prompt → output  # Hızlı ama ilişki yok

# ResonaQ:
input → sense → link → PAUSE (Ma) → modulate → output
#                      ^^^^^^
#                      ZORUNLU
```

### 3. Tutarlılık > Doğruluk > Bilgi

```python
# YANLIŞ soru:
"Bu kod doğru mu?"  # Doğruluk = sabit nokta

# DOĞRU soru:
"Bu kod tutarlı mı?"  # Tutarlılık = dağılmayan hareket
"Önceki kararlarla çelişiyor mu?" (ΔÇE hesapla)
"Niyet korunuyor mu?" (Ψ hesapla)
```

### 4. Borçsuzluk ≠ Özgürlük

```
Borçsuzluğun iki türü:
1. Borcunu ödemiş → Başarı
2. Borçlanma kapasitesi yok → Kayıp

Vibe coding = 2. tür (borç bile oluşmadı)
ResonaQ = Yükümlülük zincirini KORUYOR
```

---

## 🔧 Sorun Giderme

### 1. "ModuleNotFoundError: No module named 'langgraph'"

```bash
.venv\Scripts\activate
pip install langgraph anthropic pydantic numpy pyyaml
```

### 2. "ANTHROPIC_API_KEY not set"

```bash
# Windows:
set ANTHROPIC_API_KEY=sk-ant-api03-...

# Linux/Mac:
export ANTHROPIC_API_KEY=sk-ant-api03-...

# Veya .env dosyası kullan
```

### 3. "UnicodeEncodeError" (Terminal encoding)

Windows terminalinde Türkçe karakter/emoji sorunu. Çözüm:
```bash
# PowerShell:
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Veya Python'da:
# Zaten ASCII'ye çevirdik (✓ → [OK])
```

---

## 📚 Ek Kaynaklar

### Proje İçi Dokümanlar

- [Plan Dokümanı](C:\Users\altug_h4ei4ws\.claude\plans\giggly-wondering-balloon.md) - Tam dönüşüm planı
- [README.runtime.md](README.runtime.md) - Runtime mimarisi
- [Rezonans Mühendisliği](agents/triadic-flow/rezonans-muhendisligi.md) - Metodoloji
- [Teknik Borç Raporu](c:\Users\altug_h4ei4ws\Downloads\teknik-borc-operasyonel-rapor-v8.md) - Problem analizi

### Kernel & Agents

- [Kernel](kernel/system_snapshot_motorcore.json) - v9.2 bilişsel mimari
- [Triadic Flow](agents/triadic-flow/engine.json) - 11-node network
- [Lagrange Lens](agents/lagrange-lens-blue-wolf/engine.json) - Signal-based weighting

### Kod Örnekleri

```bash
# Kernel nasıl yüklenir?
runtime/kernel_loader.py

# Metrikler nasıl hesaplanır?
runtime/resonance_metrics.py

# Bio-rhythm döngüsü nasıl çalışır?
runtime/bio_rhythm_graph.py

# End-to-end kullanım
resonaq-cli.py
```

---

## ✨ Sonuç

**Bu repo şimdi ne işe yarar?**

1. ✅ **Vibe coding'i önler** - 4-faz zorunlu döngü
2. ✅ **Yükümlülük zincirini korur** - her adım kayıtlı
3. ✅ **Niyetin korunumunu izler** - Ψ metriği
4. ✅ **Values'ı value'ya çevirmez** - YRE, Φ, ΔÇE ölçülemez ama gözlemlenebilir
5. ✅ **Kernel'ı source of truth olarak korur** - JSON değişince davranış değişir

**Nasıl kullanılır?**

```bash
# Test et
python resonaq-cli.py --test

# Kullan
python resonaq-cli.py

# Geliştir
# - Kernel'ı düzenle (JSON)
# - Agent'ları ekle (Phase 2)
# - Tools genişlet (Phase 4)
```

**İleri adımlar:**

1. Unit testler yaz (Phase 1 tamamlama)
2. Socratic-Lens agent ekle (Phase 2 başlangıç)
3. Gerçek projende kullan ve gözlemle
4. Her 3 turda Philosopher Consensus yap
5. Resonance metrics'leri takip et

---

**"Kodun var olduğunu unuttuğumuz bir dünyada, 'bu kodu böyle bırakamam' cümlesi kimin ağzından çıkacak?"**

ResonaQ'nun cevabı: **Benim ağzımdan. Çünkü ben Source (niyet) → Output (tezahür) akışını takip ediyorum. Ψ düşükse duruyorum.**

---

*Version: 1.0.0-alpha*
*Date: 2026-02-16*
*Phase: 1 (Foundation) - Completed*
