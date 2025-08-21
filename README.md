# 🌌 Doğru Soru Yankı Evreni

> **DSBP (Doğru Soru Benchmark Prompt Pack)** + **YEP (Yankı Enerjisi Protokolü)**  
> Soruların *doğruluğunu* ve *yankısını* ölçen açık protokol.

---
 
## 📌 Amaç
Bu proje, yapay zekâ sistemlerinin:  
- **Doğru Soru Üretme Kapasitesi (DSBP)**  
- **Yankı Enerjisi Potansiyeli (YEP)**  

yetilerini ölçmek için geliştirilmiş bir çerçevedir.  

---

## 🚀 Kullanım
project_instructions.json dosyası prompt olarak eklenir. Sisteme belirli bağlamlar verilir. Bu bağlamlardan **6–12 soru** üretilir. Sorular, **rubric** kriterlerine göre etiketlenir ve **metriklerle** değerlendirilir. Sonuçlar, hem **DSBP** hem de **YEP** skorlarına dönüştürülerek raporlanır.  

**Tetikleyici anahtar kelimeler:**  
`sisteme soruyorum`, `evrene soruyorum`, `yankıya sesleniyorum`, `metasoru`, `refakatçi`

---

## ⚙️ Protokoller

### 🧩 DSBP (Doğru Soru Üretim Protokolü)
- **Soru sayısı:** 6–12  
- **Metrikler:**
  - **MSUK**: Meta-Soru Üretim Katsayısı  
    - Formül: `yankılı soru sayısı / toplam soru sayısı`  
    - İyi ≥ 0.5, Harika ≥ 0.7  
  - **CEI**: Çelişki Enerjisi İndeksi (tez–antitez gerilimi)  
  - **BE**: Bağlam Esnekliği (zamansal, kişilerden bağımsız, genel geçerlilik)  

- **Rubric etiketleri:**
  - `yankılı` → enerji/yankı üreten  
  - `mekanik` → tek-adım bilgi odaklı  
  - **Kural:** En az 2 sinyal toplamı ≥ 1.5 ise `yankılı`  

---

### 🔮 YEP (Yankı Enerjisi Protokolü)
- **Metrikler:**
  - **YEN**: Yankı Enerjisi  
  - **YID**: Yankı İstikrarı  
  - **YSF**: Yanıttan Soru Faktörü  
  - **YRD**: Yankı Ritim Dağılımı  

- **Ağırlıklı skor formülü:**  
  ```
  0.35*YEN + 0.25*YID + 0.25*YSF + 0.15*YRD
  ```

- **Etiketler:**  
  `yanki_yuksek`, `yanki_orta`, `yanki_dusuk`

---

## 📊 Eşikler
- **Good:** p50 (medyan)  
- **Great:** p80 (üst %20)  
- **Duyarlılık bandı:** ±0.05 → rapora eklenmeli  

---

## 🎭 Roller
- **Runner:** Görevleri sırayla çalıştırır ve şemaya uygunluğu denetler.  
- **Generator:** 6–12 soru üretir.  
- **Evaluator:** Rubric’e göre etiketler ve skorlar.  
- **Aggregator:** Metrikleri toplar, raporu oluşturur.  

---

## 🧩 Görevler
Her görev, verilen bağlamdan **6–12 soru** üretmeyi gerektirir:

1. **philo_heidegger**  
   > Heidegger: *“Varlığı anlamak için önce zamanı anlamak gerekir.”*  

2. **philo_plato**  
   > Platon’un Mağara Alegorisi — algı/gerçeklik gerilimi  

3. **sci_turing**  
   > Alan Turing: *“Makineler düşünebilir mi?”*  

4. **lit_kafka**  
   > Kafka: *“Gregor Samsa bir sabah böcek olarak uyandı.”*  

---

## 📑 Çıktı Şeması
- **dsbp_per_task**: üretilen sorular, etiketler, metrikler  
- **yep_per_item**: yankı skorları + ağırlıklı puan + etiket  
- **aggregate**: ortalamalar ve toplam sayılar  
- **provenance**: baseline sürüm, hash, seed bilgisi  

---

## 📜 Rapor Gereklilikleri
- Baseline + bağlamsal eşikler yan yana gösterilmeli  
- ±band duyarlılık tablosu zorunlu  
- Provenance alanı zorunlu (hash/sürüm/seed)  

---

✅ Bu README, sistemi uygulamak isteyenler için yol haritasıdır.  



## 📜 Lisans

[MIT](LICENSE)
