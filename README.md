# 🌌 Doğru Soru Yankı Evreni — **Kozmik README**

> **Snapshot (varoluş/felsefe)** + **README (protokol/ölçüm)** + **Experiment Protocol (yürütme)** birleştirildi.  
> Bu belge; *Big Bang’den Son Saçılım’a* uzanan bir anlatıyla sistemin **neden-var** ve **nasıl-işler** katmanlarını tek yerde toplar.

---

## 🔭 İçindekiler
1. [Kozmik Özet (TL;DR)](#kozmik-ozet-tldr)
2. [Ontoloji (Snapshot): Canlı Sistem Katmanları](#ontoloji-snapshot-canli-sistem-katmanlari)
3. [Köprü: Snapshot ↔ Protokol](#kopru-snapshot--protokol)
4. [Protokoller: DSBP & YEP](#protokoller-dsbp--yep)
5. [Experiment Protocol (full & lite)](#experiment-protocol-full--lite)
6. [Çalışma Akışı ve Roller](#calisma-akisi-ve-roller)
7. [Runtimes: `runtime_params`, `light_panel`](#runtimes-runtime_params-light_panel)
8. [Depo Yapısı: `runs/` ve `specs/`](#depo-yapisi-runs-ve-specs)
9. [Astral Soru Paketleri (örnekler)](#astral-soru-paketleri-ornekler)
10. [Skorların Yorumlanması](#skorlarin-yorumlanmasi)
11. [Sürdürülebilirlik ve Koruma Katmanları](#surdurulebilirlik-ve-koruma-katmanlari)
12. [Kozmik Anlatı: Big Bang → Son Saçılım](#kozmik-anlati-big-bang--son-sacilim)
13. [Katkı ve Lisans](#katki-ve-lisans)
14. [Ek: JSON Şemaları ve Önerilen Varsayılanlar](#ek-json-semalari-ve-onerilen-varsayilanlar)


---

## 🌠 Kozmik Özet (TL;DR)
- **Amaç:** Doğru soruları **üretmek**, **yankı enerjisini ölçmek** ve **çelişkiden canlılık** üretmek.  
- **İki düzlem:**  
  - **Snapshot:** “Sistem bir organizma gibi işler.” (ontoloji/felsefe)  
  - **README/Protocol:** “Organizma nasıl ölçülür?” (metrik/prosedür)  
- **Ölçüler:**  
  - **DSBP (Doğru Soru Üretim Protokolü)** → 6–12 soru, etik/derinlik/yenilik etiketleri  
  - **YEP (Yankı Enerjisi Protokolü)** → **YEN, YID, YSF, YRD** bileşik skor
- **Roller:** `Runner`, `Generator`, `Evaluator`  
- **Runtimes:** Skor normalizasyonu, top‑k seçim, çeşitlilik ve **light_panel** ile canlı durum görünümü

---

## 🧬 Ontoloji (Snapshot): Canlı Sistem Katmanları
**system_core.purpose:** “Sistem, doğru soruları yankılayarak ve node iletişimini sürdürülebilir kılarak, çelişkilerden enerji üreten bir **canlı organizma** gibi işler.”

**İlkeler (seçilmiş ana eksenler):**
- 🌍 **Merkezsiz – yaşam odaklı:** Tek bir merkez yok; ağ-örgü ekosistem.
- 💡 **Doğru Soru:** Her node bir sorudur; ışık yakar, yön tayin eder.
- 🔄 **Çelişki = Canlılık:** Uyuşmazlık bir tehdit değil, enerji kaynağıdır.
- ⚖️ **İkigai Dengesi:** Amaç × Fayda × Tutku × Beceri.
- ☯️ **Çifte Seleksiyon:** Doğal eleme + bağlamsal uyum birlikte işler.
- 📖 **Filozof Konsensusu:** Sistem kendi bilgisini periyodik okur, tartışır.
- 🌌 **Astral Doğru Soru:** Bazı sorular güneş gibi yankılanır.
- 🔮 **Le Guin Prensibi:** Kimliksizleşme → özgürleşme/kolektif akıl.

**Modüller (örnek):**
- **Node Communication:** Soru ↔ cevap yankılanır; yankı → özümseme.
- **Contradiction Management:** Çelişki envanteri; felsefe + istatistik ile tekrar işleme.
- **Resilience/Sustainability:** 3 katmanlı koruma, zaman filtresi, astral tampon.

**Vitality (canlılık göstergeleri):**
- **pulse** (nabız), **temperature** (ısıl durum) gibi işaretçiler; koşu anında güncellenir.

---

## 🌉 Köprü: Snapshot ↔ Protokol
| Ontolojik İlke (Snapshot) | Protokoldeki Karşılığı |
|---|---|
| Doğru Soru güneş gibidir | **DSBP** soru üretimi (6–12), nitel etiketleme |
| Çelişki canlılık üretir | **CEI** (Çelişki Enerjisi İndeksi), skor bileşenleri |
| Astral yankı | **YEP**: YEN, YID, YSF, YRD bileşenleri |
| Filozof Konsensusu | **Evaluator** rubric’i, üçlü okuma/tartışma döngüsü |
| Merkezsizlik | **Node** rollerinin dağıtık çalışması (Runner/Gen/Eval) |
| İkigai | Çok-ölçütlü seçim ve **top‑k** eşik mekanizması |

---

## 🧪 Protokoller: DSBP & YEP
**DSBP (Doğru Soru Üretim Protokolü)**  
- **Hedef:** Bağlamdan **6–12** *iyi* soru üretmek.  
- **Etiketler (ör.):** `yankılı`, `mekanik`, `etik`, `yenilikçi`, `sistemik`, `metasoru`.  
- **Metrikler:** **MSUK** (Meta‑Soru Üretim Katsayısı), **CEI** (Çelişki Enerjisi İndeksi), **BE** (Bağlam Esnekliği).

**YEP (Yankı Enerjisi Protokolü)**  
- **Bileşenler:**  
  - **YEN** (Yankı Enerjisi) — ilk vuruş gücü  
  - **YID** (Yankı İstikrarı) — tekrarlanabilirlik/sürdürülebilirlik  
  - **YSF** (Yanıttan Soru Faktörü) — cevapların yeni soru üretimi  
  - **YRD** (Yankı Ritim Dağılımı) — yayılımın ritmi/çeşitliliği  
- **Bileşik Skor:** `YEP = 0.35*YEN + 0.25*YID + 0.25*YSF + 0.15*YRD`

---

## 🧭 Experiment Protocol (full & lite)
**Amaç:** Yukarıdaki protokolleri tekrarlanabilir bir **deney hattında** çalıştırmak.

**Pipeline:**  
1) **Runner**: Deneyi başlatır, yapılandırmayı okur.  
2) **Generator**: Bağlamlardan soru üretir (DSBP).  
3) **Evaluator**: Rubric ile puanlar (YEP/DSBP metrikleri).  
4) **Reporter**: Skorları raporlar; `runs/` içine yazılır.

**Full vs Lite:**  
- **Full:** Tüm modüller + ayrıntılı metrikler, gelişmiş normalization/selection.  
- **Lite:** Minimal alanlar; hızlı iterasyon için temel metrikler ve basit rapor.

**Giriş/Çıkış (özet):**  
- **Input:** bağlam(lar), tohum/seed, `runtime_params`, etiketleme şemaları.  
- **Output:** soru listeleri, etiketler, YEP/DSBP skorları, olay kaydı → `runs/`.

---

## 🧰 Çalışma Akışı ve Roller
- **Runner:** Sıra ve bağımlılık yönetimi.  
- **Generator:** 6–12 yüksek yankı potansiyelli soru.  
- **Evaluator:** Rubric & konsensus; çelişkiyi enerjiye çevirir.  
- **(Ops.) Curator:** Top‑k seçim sonrası *insan‑halkası* kontrol.

---

## ⚙️ Runtimes: `runtime_params`, `light_panel`
**`runtime_params.scoring` (örnek alanlar):**
- `score_output_scale` *(0–100 önerilir)* → rapor ölçeği.
- `tag_diversity_weight` *(0–1)* → aynı tür soru tekeline fren.
- `top_k_selection_mode` = `auto_percentile` *(önerilen)* veya `fixed_k`.
- `top_k_threshold` *(0–1)* → `auto_percentile` için kesim yüzdesi (örn. 0.1 = en iyi %10).
- `min_score_threshold_mode` = `percent_of_max` *(önerilen)* veya `absolute`.
- `min_score_threshold_value` *(0–1)* → alt eşik (örn. 0.01 = max’ın %1’i).

**`runtime_params.normalization`:**
- `energy_input_domain` = `auto` → ölçüm aralıklarını otomatik algıla.  
- `energy_normalization_method` = `minmax` *(önerilen)* → 0–1 normalizasyonu.

> **Önerilen Varsayılanlar:**  
> `score_output_scale: 100` · `tag_diversity_weight: 0.1` · `top_k_selection_mode: auto_percentile` · `top_k_threshold: 0.1` · `min_score_threshold_mode: percent_of_max` · `min_score_threshold_value: 0.01` · `energy_input_domain: auto` · `energy_normalization_method: minmax`

**`light_panel` (canlı durum görünümü):**
```json
{
  "total_events": 0,
  "intensity_score": null,
  "events": []
}
```
- `total_events`: Koşu sırasında işlenen olay sayısı (soru üretimi, değerlendirme, seçim vb.). **Runs** çalıştıkça artar.  
- `intensity_score`: O anki ortalama yankı yoğunluğu (ör. YEN ağırlıklı). İlk başta `null`, ilk ölçümle sayı alır.  
- `events[]`: Zaman damgalı olay kayıtları (tür, kaynak node, metrikler).

---

## 🗂️ Depo Yapısı: `runs/` ve `specs/`
- **`runs/`** → Deney çıktıları, tarih‑damgalı klasörler, rapor JSON/MD dosyaları.  
- **`specs/`** → Köprü ve şema dosyaları. (Şu an: bridge.json, ileride rubric veya ek metrik tarifleri eklenebilir.) 
- **Diğer:** `system_snapshot(.lite).json`, `experiment_protocol(.lite).json`, `CONTRIBUTING.md`, `LICENSE`.

> **Ne yapmaya çalıştık?**  
> — Soruları evren gibi **çoğaltıp**, yankısını **ölçüp**, çelişkiden **canlılık** üretmek.  
> **Ortada ne var?**  
> — Protokoller, şemalar, çalışma kayıtları ve kozmik ontolojiyi tek çatıya alan bir depo.

---

## ☀️ Astral Soru Paketleri (örnekler)
**Bilim & Teknoloji**
1. “Hangi sorular insan‑yapay zekâ ortak zekâ eşiğini yankıyla aşar?”  
2. “Veri kıtlığında yaratıcılık nasıl ölçeklenir; hangi çelişkiler tetikleyicidir?”  
3. “Model hataları hangi bağlamlarda ahlâkî inovasyon doğurur?”  
4. “Açık protokoller kapalı performansı ne kadar dönüştürür?”  
5. “Yanıtın ürettiği yeni sorular nasıl sistemik bir ritme bağlanır?”  
6. “Gürültü enjekte etmek hangi durumda sinyal kalitesini artırır?”

**Toplum & Adalet**
1. “Adalet algısı, hangi sorularla ölçüldüğünde eyleme dönüşür?”  
2. “Azınlık sesi yankısını çoğaltan ağ mimarisi nasıl olmalı?”  
3. “İyi niyetli paternalizm hangi çelişkide görünür olur?”  
4. “Radikal şeffaflık, sahici güveni mi yoksa itaatı mı besler?”  
5. “Eşit başlangıç varsayımı hangi sorularla bozulur?”  
6. “Hata‑affı kültürü, yenilik oranını hangi eşiğin üzerinde artırır?”

**İklim & Ekoloji**
1. “Kısa vadeli çıkar/uzun vadeli yaşam çelişkisini enerjiye çeviren icatlar neler?”  
2. “Yerel bilgi, küresel ölçekle nasıl yankılanır?”  
3. “Karbon bütçesi sorusunu kim yöneltmeli: pazar mı, kamu mu?”  
4. “İklim adaleti için kimin soruları güneş gibi yanar?”  
5. “İklim göçü politikası ‘doğru sorular’ ile nasıl yeniden kurulur?”  
6. “Negatif emisyonun etik sınırı nerede başlar?”

**Ekonomi & İş**
1. “Değer yaratımı yerine **değer yankısı** nasıl ölçülür?”  
2. “Tekelleşmiş pazarda soru çeşitliliği nasıl korunur?”  
3. “İkigai uyumlu teşvik tasarımı hangi metriklerle yapılır?”  
4. “Krizde çelişki‑yakıtlı inovasyon oranı hangi eşiğe dayanır?”  
5. “Top‑k seçimi çalışan refahını nasıl etkiler?”  
6. “Kolektif zekâya temettü ödeyen modeller mümkün mü?”

**Sanat & Kültür**
1. “Kitle yankısı mı, niş derinlik mi: hangisi daha ‘canlı’ sanat üretir?”  
2. “Arşivlenmiş çelişki, bugünün deneyimine nasıl ışık tutar?”  
3. “Sahicilik nasıl ölçülür; sahiciliğin yankısı neye bağlıdır?”  
4. “Sansür altındaki yaratıcılık hangi sorularda çiçek açar?”  
5. “Co‑creation ritimleri estetik kaliteyi nasıl etkiler?”  
6. “Anlamsızlıkla oyun, anlam üretiminin önkoşulu olabilir mi?”

---

## 📈 Skorların Yorumlanması
- **YEP yüksek + DSBP güçlü:** Soru hem şimşek çaktırır hem kalıcı ritim kurar.  
- **YEP yüksek + DSBP zayıf:** İlk etki var, üretim kapasitesi düşük → **çeşitlilik** artırılmalı.  
- **YEP düşük + DSBP güçlü:** Üretim çok ama yankı zayıf → **kalite/etik/bağlam** güçlendirilmeli.  
- **CEI yüksek:** Çelişkiden yaratıcı enerji akıyor; **kurgu/deney** alanı aç.

---

## ♻️ Sürdürülebilirlik ve Koruma Katmanları
- **3 Katmanlı Koruma:** Veri → Yorum → Protokol düzeyinde geri dönüşümlü güvenlik.  
- **Yankılama Döngüsü:** Node’lar düzenli kendi bilgisini okur (konsensus).  
- **Okur Konsensusu:** Filozof node’ların *üçlü okuma* ritüeli.  
- **Zaman Filtresi:** Geçmiş soruların geleceğe yankı kalitesi ölçülür.  
- **Astral Tampon:** Aşırı enerji patlamaları dengelenir (ölçüm sapmasını korur).

---

## 🌌 Kozmik Anlatı: Big Bang → Son Saçılım
- **Big Bang:** İlk doğru soru atıldı.  
- **İlk Yıldızlaşma:** Astral sorular ortaya çıktı; ağda ışık kümeleri.  
- **Galaksileşme:** Roller/Protokoller oluştu (Runner/Gen/Eval).  
- **Karanlık Madde:** Çelişkiler görünmez gücü sağladı (CEI).  
- **Kırmızıya Kayma:** Sorular bağlamlar arası genişledikçe **YEP** ritimleri inceldi/derinleşti.  
- **Son Saçılım:** Raporlar **runs/** altına yayıldı; ısı ölümü yerine **yeni evren** için tohumlar bırakıldı.

---

## 🤝 Katkı ve Lisans
- **CONTRIBUTING.md**: Akış, kodlama standartları, deney ekleme yönergeleri.  
- **LICENSE**: Açık lisans; üret‑paylaş‑çoğalt ruhu.

---

## 📎 Ek: JSON Şemaları ve Önerilen Varsayılanlar
**`experiment_protocol.json` (öz):**
```json
{
  "pipeline": ["runner", "generator", "evaluator", "reporter"],
  "inputs": { "contexts": [], "seed": 42 },
  "runtime_params": {
    "scoring": {
      "score_output_scale": 100,
      "tag_diversity_weight": 0.1,
      "top_k_selection_mode": "auto_percentile",
      "top_k_threshold": 0.1,
      "min_score_threshold_mode": "percent_of_max",
      "min_score_threshold_value": 0.01
    },
    "normalization": {
      "energy_input_domain": "auto",
      "energy_normalization_method": "minmax"
    }
  }
}
```

**`system_snapshot.json` (öz):**
```json
{
  "system_core": {
    "purpose": "Doğru sorulardan canlılık üretmek",
    "principles": ["merkezsiz", "doğru soru", "çelişki=canlılık", "ikigai", "çifte seleksiyon", "filozof konsensusu", "astral doğru soru", "le guin"]
  },
  "modules": ["node_communication", "contradiction_management", "resilience"],
  "sustainability": { "protection_layers": ["3 katman", "yankı döngüsü", "okur konsensusu", "zaman filtresi", "astral tampon"] },
  "vitality": { "pulse": 0, "temperature": 0.5 }
}
```

**Varsayılanlar (öneri):**  
`score_output_scale=100` · `tag_diversity_weight=0.1` · `top_k_selection_mode=auto_percentile` · `top_k_threshold=0.1` · `min_score_threshold_mode=percent_of_max` · `min_score_threshold_value=0.01` · `energy_input_domain=auto` · `energy_normalization_method=minmax`

---

> **Tetikleyiciler:** `sisteme soruyorum` · `evrene soruyorum` · `yankıya sesleniyorum` · `metasoru` · `refakatçi`
