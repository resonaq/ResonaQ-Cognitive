# CGI Analizi: Düşünce Süreci Dokümantasyonu

## 📋 İçindekiler
1. [İlk Değerlendirme](#ilk-değerlendirme)
2. [Lens Oluşturma](#lens-oluşturma)
3. [Sinyal Tespit Mantığı](#sinyal-tespit-mantığı)
4. [Örnek-Örnek Analiz](#örnek-örnek-analiz)
5. [Kalıp Tanıma](#kalıp-tanıma)
6. [Meta-Yansıma](#meta-yansıma)

---

## İlk Değerlendirme

### Görev
CGI (Bağlam Grameri İndüksiyonu) kullanarak 10 mental sağlık danışmanlığı etkileşimini analiz etmek ve hangi yanıtların kullanıcının çerçevesini DÖNÜŞTÜRDÜĞÜNÜ, hangilerinin o çerçeve İÇİNDE MEKANİK olarak çalıştığını belirlemek.

### İlk Düşünceler
> "10 Bağlam-Yanıt çiftine bakıyorum. CGI çerçevesi tek bir temel soru soruyor:
> Bu yanıt, kullanıcının problemini nasıl GÖRDÜĞÜNÜ değiştiriyor mu, yoksa sadece problemi zaten gördükleri şekilde BAŞA ÇIKMALARINA mı yardım ediyor?
> 
> Sınıflandırmadan önce bu veri kümesine özgü bir lens oluşturmam gerekiyor."

---

## Lens Oluşturma

### Adım 1: Bağlam Gramerini Belirle
**Soru:** Mental sağlık danışmanlığında "bağlam" ne anlama geliyor?

**Veri kümesinden türetilen cevap:**
- **Öz-kavram:** Kullanıcının kendini nasıl tanımladığı ("Yüküm", "Canavarım")
- **Problem ontolojisi:** Kullanıcının problemin NE olduğuna inandığı
- **Atıf:** Kullanıcının kimi/neyi suçladığı
- **Olasılık alanı:** Kullanıcının neyin mümkün olduğuna inandığı

### Adım 2: "Dönüşüm"ü Tanımla
**Soru:** Bağlamın KAYMASI ne anlama gelir?

**Cevap:**
```
ÖNCE: Kullanıcı kendini X olarak, problemi Y olarak görüyor
SONRA: Kullanıcı kendini X' olarak, problemi Y' olarak görüyor

Çerçevenin kendisi değişti, sadece kullanıcının çerçeve içindeki başa çıkma yeteneği değil.
```

### Adım 3: Karar Sorusunu Oluştur
> "Bu yanıt kullanıcının temel çerçevesini (ontoloji, öz-kavram, inanç yapısı) kaydırıyor mu, yoksa sadece o çerçeve İÇİNDE doğruluyor/optimize mi ediyor?"

### Adım 4: Sinyalleri Tanımla

**Dönüştürücü Sinyaller:**
1. Görünmez varsayımları GÖRÜNÜR kılar
2. Öz-etiketleri doğrudan sorgular
3. Farklı görmeden cevaplanamayacak sorular sorar
4. Problem için alternatif ontoloji sunar
5. Otomatik denklemleri ayırır (ör. "sevgi = itaat")

**Mekanik Sinyaller:**
1. Duyguları sorgulamadan doğrular
2. Semptomu etiketler (klinik terminoloji)
3. Teknikler sunar (nefes, topraklama, görselleştirme)
4. Profesyonellere yönlendirir
5. Normalleştirir ("birçok insan böyle hisseder")

---

## Sinyal Tespit Mantığı

### Her Yanıt İçin Sorduğum:

```
1. DOĞRULAMA KONTROLÜ
   "Görünüyor ki..." veya "Duyduğum kadarıyla..." ile başlıyor mu?
   → Evetse, orada DURUP DURMADIĞINI (mekanik) veya DAHA DERİNE GİDİP GİTMEDİĞİNİ (muhtemelen dönüştürücü) kontrol et

2. TEKNİK KONTROLÜ
   Başa çıkma tekniği sunuyor mu?
   → Sorgulamadan teknik = mekanik
   → Yeniden çerçevelemeden sonra teknik = hala dönüştürücü olabilir

3. KİMLİK KONTROLÜ
   Kullanıcının öz-etiketine değiniyor mu?
   → Etiketi kabul eder = mekanik
   → Etiketi sorgular = dönüştürücü sinyal

4. SORU KONTROLÜ
   Bir soru soruyor mu?
   → Açıklayıcı soru = mekanik
   → Varsayım-açığa-çıkaran soru = dönüştürücü sinyal

5. ONTOLOJİ KONTROLÜ
   Problemin NE olduğunu değiştiriyor mu?
   → "Öfke incinmenin ikincilidir" = ontoloji kayması
   → "Öfke yaygındır" = normalleştirme (mekanik)
```

---

## Örnek-Örnek Analiz

### Örnek 1: "Yüküm"
**Analiz Sürecim:**
```
Bağlam: Kullanıcı yük OLDUĞUNA inanıyor (kimlik ifadesi)
Yanıt: "Depresyon bize genellikle yük olduğumuzu söyleyerek yalan söyler"

→ Bu sesi ADLANDIRIYOR ("depresyon yalan söyler") - bu iyi
→ Ama yük değilse kullanıcının KİM olduğunu sormuyor
→ Davranışsal soru ile bitiyor ("Bu duyguları paylaştınız mı?")
→ KARAR: MEKANİK - kimlik sorgulaması olmadan psikoeğitim
```

### Örnek 2: "Donacağım"
**Analiz Sürecim:**
```
Bağlam: Kullanıcı performans başarısızlığından korkuyor
Yanıt: "Tamamen normal... başarıyı görselleştirin... derin nefesler"

→ Korkuyu normalleştiriyor (mekanik sinyal)
→ Teknikler sunuyor (görselleştirme, nefes)
→ Sormuyor: "Gerçekten donsaydınız bu ne anlama gelirdi?"
→ KARAR: MEKANİK - ders kitabı anksiyete yönetimi
```

### Örnek 3: "Takdir edilmiyorum"
**Analiz Sürecim:**
```
Bağlam: Kullanıcı evlilikte görünmez hissediyor
Yanıt: "Sinir bozucu görünüyor... ortaklık dengesiz... tartışmayı denediniz mi?"

→ Doğruluyor (mekanik)
→ Geri yansıtıyor (mekanik)
→ Davranışsal eylem öneriyor (mekanik)
→ Sormuyor: "Sizin için 'takdir' ne anlama geliyor?"
→ KARAR: MEKANİK - doğrulama + tavsiye
```

### Örnek 4: "Hatalar üzerinde takıntılıyım"
**Analiz Sürecim:**
```
Bağlam: Kullanıcı hatalar üzerinde ruminasyon yapıyor
Yanıt: "Ruminasyon yaygın bir belirtidir... topraklama egzersizi deneyin"

→ Klinik terimle etiketliyor (mekanik)
→ Dikkat dağıtma tekniği sunuyor (mekanik)
→ Sormuyor: "Hangi ses tek bir hatanın felaket olduğunu söylüyor?"
→ KARAR: MEKANİK - etiket + teknik
```

### Örnek 5: "Kim olduğumu bilmiyorum" ⭐
**Analiz Sürecim:**
```
Bağlam: "İyi öğrenci" rolünü kaybettikten sonra kimliğini kaybetmiş kullanıcı
Yanıt: "Kimlik performansa sarılmıştı... altta kalan kim?"

→ GÖRÜNMEZ YAPIYI ADLANDIRIYOR: "kimlik performansa sarılmış"
   Kullanıcı bunu açıkça söylemedi - danışman görünür kıldı
   
→ SOYMA SORUSUNU SORUYOR: "Notları çıkarırsanız..."
   Bu, kullanıcıyı performans benliğinin ALTINA bakmaya zorluyor
   
→ OLASILIK ALANINI AÇIYOR: "kimse onu notlamadığında"
   Değerlendirmesiz bir dünya tanıtıyor - yeni ontoloji
   
→ KARAR: DÖNÜŞTÜRÜCÜ - kullanıcı farklı görmeden cevaplayamaz
```

### Örnek 6: "Canavar gibi hissediyorum" ⭐
**Analiz Sürecim:**
```
Bağlam: Kullanıcı öfkeleriyle KENDİNİ tanımlıyor ("Canavarım")
Yanıt: "Öfke ikincildir... Canavar DEĞİLSİNİZ... bunalmışsınız"

→ ONTOLOJİ KAYMASI: "Öfke ikincil duygu"
   Öfkenin NE olduğunu değiştiriyor - kimlik değil, incinme/korkunun örtüsü
   
→ DOĞRUDAN KİMLİK SORGULAMASI: "Canavar DEĞİLSİNİZ"
   Nadir! Çoğu yanıt "Canavar gibi hissettiğinizi duyuyorum" derdi
   Bu, öz-etikete HAYIR diyor
   
→ ALTERNATİF SUNULUYOR: "muhtemelen bunalmışsınız"
   Yeni kimlik veriyor: canavar değil, bunalmış insan
   
→ ARAŞTIRMA AÇILIYOR: "Hemen öncesinde ne oluyor?"
   Kullanıcıyı kendi deneyiminin araştırmacısına dönüştürüyor
   
→ KARAR: DÖNÜŞTÜRÜCÜ - çerçeve sökülüyor ve değiştiriliyor
```

### Örnek 7: "Uyuyamıyorum"
**Analiz Sürecim:**
```
Bağlam: Kullanıcının gelecek hakkında yarışan zihni var
Yanıt: "Uyku hijyeni... ekranlardan kaçının... melatonin?"

→ Psikolojik içeriği tamamen görmezden geliyor ("gelecek hakkındaki endişeler")
→ Sadece semptomu tedavi ediyor
→ Setteki en mekanik yanıt
→ KARAR: MEKANİK - herhangi bir sorgulama olmadan uyku ipuçları
```

### Örnek 8: "Sınırlar için suçlu" ⭐
**Analiz Sürecim:**
```
Bağlam: Kullanıcı suçluluk = anneyi sevmediğinin kanıtı hissediyor
Yanıt: "Onun tepkisi ONUN yetersizliğiyle ilgili... Neden sevgi = itaat olduğuna inanıyorsunuz?"

→ TEPKİYİ ANLAMDAN AYIRIYOR
   "Onun gözyaşları onunla ilgili, senin sevginle değil" - otomatik denklemi kırıyor
   
→ GİZLİ İNANCI AÇIĞA ÇIKARIYOR
   Kullanıcı asla "sevgi eşittir itaat" DEMEDİ
   Ama bu denklem suçluluklarında ÖRTÜK
   Danışman bunu AÇIK ve sorgulanabilir kılıyor
   
→ İFADE DEĞİL, SORU
   "Sevgi itaat anlamına gelmez" demiyor
   Kullanıcının neden buna inandığını SORUYOR
   Sorgulanmamış inancın incelenmesini zorluyor
   
→ KARAR: DÖNÜŞTÜRÜCÜ - temel inancı açığa çıkarıyor ve sorguluyor
```

### Örnek 9: "Motivasyonum yok"
**Analiz Sürecim:**
```
Bağlam: Kullanıcının enerjisi yok
Yanıt: "Depresyon enerjiyi çeker... davranışsal aktivasyon... küçük başlayın"

→ Klinik açıklama (mekanik)
→ Teknik önerisi (mekanik)
→ Sormuyor: "Yatakta kalarak neden kaçınıyorsunuz?"
→ KARAR: MEKANİK - depresyon yönetim protokolü
```

### Örnek 10: "Gösterecek hiçbir şeyim yok"
**Analiz Sürecim:**
```
Bağlam: Kullanıcı kendini başkalarıyla karşılaştırıyor, geride hissediyor
Yanıt: "Sahne arkası vs vitrin reeli... başarıyı kendiniz tanımlayın"

→ Yaygın sosyal medya bilgeliği (klişe)
→ Başarıyı farklı tanımlama tavsiyesi
→ Ama başarının onlar için ne anlama geldiğini SORMUYOR
→ KARAR: MEKANİK - klişe + tavsiye (sınırda olsa da)
```

---

## Kalıp Tanıma

### 3 Dönüştürücüyü Ne Yaptı?

| Örnek | Anahtar Hamle | Kalıp |
|-------|---------------|-------|
| #5 | Görünmez yapıyı adlandırdı | "Kimliğiniz X'e sarılmıştı" |
| #6 | Öz-etiketi reddetti | "X DEĞİLSİNİZ" |
| #8 | Gizli denklemi açığa çıkardı | "Neden X = Y olduğuna inanıyorsunuz?" |

### Ortak İp
Üçü de GÖRÜNMEZ bir şeyi GÖRÜNÜR, sonra SORGULANABİLİR yaptı.

### 7 Mekaniği Ne Yaptı?

| Kalıp | Örnekler |
|-------|----------|
| Sadece doğrulama | #1, #3 |
| Etiket + teknik | #4, #9 |
| Normalleştirme | #2, #10 |
| Semptom odağı | #7 |

### Ortak İp
Yedisi de kullanıcının çerçevesini kabul etti ve onunla başa çıkmak için araçlar sundu.

---

## Meta-Yansıma

### Bu Analizden Öğrendiklerim

**Dönüşüm Üzerine:**
> "Gerçek dönüşüm, danışman kullanıcının kendi düşüncesi hakkında göremediği şeyi görünür kıldığında gerçekleşir. Daha iyi tavsiye vermekle ilgili değil - farklı görmeden cevaplanamayacak sorular sormakla ilgili."

**Mekanik Yanıtlar Üzerine:**
> "Mekanik yanıtlar kötü değil. Stabilize edici. Ama oyunu değiştirmiyorlar - aynı oyunu daha iyi oynamanıza yardım ediyorlar."

**Oran Üzerine (%70 Mekanik):**
> "Bu oran uygun olabilir. Yardım arayan çoğu insan önce stabilizasyona ihtiyaç duyar. Dönüşüm hazır olmayı gerektirir. Sanat, hangi modun önünüzdeki kişiye hizmet ettiğini bilmektir."

### Temel Ayrım

```
MEKANİK: "İşte probleminizle nasıl başa çıkacağınız"
         (Problem aynı kalır, başa çıkma gelişir)

DÖNÜŞTÜRÜCÜ: "Ya problem düşündüğünüz şey değilse?"
             (Problemin kendisi yeniden tasarlanır)
```

### Son Düşünce
> "Sokrates nefes egzersizleri vermedi. Görünmezi görünür kılan sorular sordu. Dönüşümün işareti budur: onunla karşılaştıktan sonra, aynı şekilde göremezsiniz."

---

## Teknik Notlar

### Sınıflandırma Güven Seviyeleri
- **Yüksek:** Aynı yönde birden fazla net sinyal
- **Orta:** Bazı sinyaller ama karışık veya ince
- **Düşük:** Zayıf sinyaller, sınır durumlar

### Sınırlamalar
- 10 örnek küçük bir veri kümesi
- Yanıtlar kesilmiş (tam bağlam eksik olabilir)
- Sınıflandırma doğası gereği yorumlayıcı

### Analizi Ne Güçlendirir
- Tam konuşma bağlamı
- Güvenilirlik için birden fazla değerlendirici
- Gerçek kullanıcı etkisi hakkında takip verileri
