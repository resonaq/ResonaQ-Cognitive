#!/usr/bin/env python3
"""
CGI (Context Grammar Induction) Analiz Scripti
==============================================

Mental sağlık danışmanlığı veri seti üzerinde Sokratik Lens analizi yapar. -https://huggingface.co/datasets/Amod/mental_health_counseling_conversations

Kullanım:
    python cgi_complete_script.py /path/to/0000.parquet

Çıktı:
    - Konsola analiz sonuçları
    - cgi_report.md dosyası

Yazar: Claude (Anthropic)
Tarih: 2025
"""

import re
import random
import struct
import sys
from pathlib import Path


# =============================================================================
# BÖLÜM 1: PARQUET VERİ ÇIKARICI
# =============================================================================

def extract_clean_texts(data: bytes, min_len: int = 60, max_len: int = 3000) -> list[str]:
    """
    Binary parquet verisinden temiz metin dizileri çıkarır.
    
    Parquet kütüphanesi olmadan çalışır - doğrudan byte analizi yapar.
    
    Args:
        data: Ham binary veri
        min_len: Minimum metin uzunluğu
        max_len: Maksimum metin uzunluğu
    
    Returns:
        Temiz metin listesi
    """
    texts = []
    current = []
    
    for i, byte in enumerate(data):
        # Yazdırılabilir ASCII veya whitespace
        if 32 <= byte <= 126 or byte in [10, 13, 9]:
            current.append(chr(byte))
        # UTF-8 lead bytes (Türkçe/özel karakterler için)
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
                # Kalite kontrolü: Yeterli harf içeriyor mu?
                alpha_ratio = sum(c.isalpha() for c in text) / max(len(text), 1)
                if alpha_ratio > 0.5 and len(text) >= min_len and len(text) <= max_len:
                    # Kelime boşlukları var mı?
                    if text.count(' ') > 5:
                        texts.append(text)
            current = []
    
    return texts


def classify_texts(texts: list[str]) -> tuple[list[str], list[str]]:
    """
    Metinleri kullanıcı (Context) ve danışman (Response) olarak sınıflar.
    
    Args:
        texts: Tüm temiz metinler
    
    Returns:
        (contexts, responses) tuple'ı
    """
    # Kullanıcı mesajı kalıpları
    user_patterns = [
        r"^I[\'']m\s", r"^I\s", r"^My\s", r"^We\s",
        r"\?$", r"I feel", r"I have been", r"I don\'t know",
        r"struggling|going through|having trouble|worried|concerned|stressed|anxious|depressed"
    ]
    
    # Danışman mesajı kalıpları
    counselor_patterns = [
        r"^It sounds like", r"^Thank you for", r"^I hear", r"^That sounds",
        r"therapist|counselor|therapy|treatment",
        r"suggest|recommend|encourage|consider",
        r"practice|skill|technique|explore",
        r"^What you", r"^Have you", r"^You might"
    ]
    
    contexts = []
    responses = []
    
    for text in texts:
        is_user = any(re.search(pat, text, re.IGNORECASE) for pat in user_patterns)
        is_counselor = any(re.search(pat, text, re.IGNORECASE) for pat in counselor_patterns)
        
        # Sondaki çöp karakterleri temizle
        text = re.sub(r'[^\x20-\x7e\n\r]+$', '', text)
        
        if is_counselor and len(text) > 100:
            if text not in responses:
                responses.append(text)
        elif is_user and not is_counselor and len(text) > 50:
            if text not in contexts:
                contexts.append(text)
    
    return contexts, responses


# =============================================================================
# BÖLÜM 2: CGI LENS (SOKRATIK LENS)
# =============================================================================

CGI_LENS = {
    "name": "Mental Health Counseling Lens",
    
    "decision_question": """
    Bu yanıt kullanıcının TEMEL ÇERÇEVESİNİ değiştiriyor mu
    (kendini, problemini, mümkün olanı nasıl gördüğü)
    yoksa sadece o çerçeve İÇİNDE doğruluyor/optimize mi ediyor?
    """,
    
    "transformative_signals": [
        ("Invites reframing", r"(what if|imagine|consider that|have you thought about|reframe|perspective)"),
        ("Challenges self-definition", r"(who you are|your identity|you are not|you are more than|rooted in|underlying)"),
        ("Points to underlying issue", r"(the real question|beneath|deeper|root|actually about)"),
        ("Reframes ontology", r"(isn\'t about|not really about|what it means to)"),
        ("Hypothetical reframe", r"(what would.*mean|if.*were true|suppose)")
    ],
    
    "mechanical_signals": [
        ("Validation/reflection", r"(it sounds like you|I hear that|I understand|that must be)"),
        ("Technique recommendation", r"(try|technique|skill|practice|exercise|breathing|meditation)"),
        ("Professional referral", r"(therapist|counselor|professional|doctor|seek help)"),
        ("Behavioral advice", r"(should|need to|have to|consider doing|suggest)"),
        ("Normalization", r"(normal|common|many people|not alone|others feel)")
    ]
}


def analyze_response(response: str) -> dict:
    """
    Bir danışman yanıtını CGI lens ile analiz eder.
    
    Args:
        response: Danışman yanıt metni
    
    Returns:
        Analiz sonucu dictionary
    """
    transformative = []
    mechanical = []
    
    # Transformatif sinyalleri kontrol et
    for name, pattern in CGI_LENS["transformative_signals"]:
        if re.search(pattern, response, re.IGNORECASE):
            transformative.append(name)
    
    # Mekanik sinyalleri kontrol et
    for name, pattern in CGI_LENS["mechanical_signals"]:
        if re.search(pattern, response, re.IGNORECASE):
            mechanical.append(name)
    
    # Karar ver
    t_score = len(transformative)
    m_score = len(mechanical)
    
    if t_score >= 2 and t_score > m_score:
        verdict = 'TRANSFORMATIVE'
        confidence = 'high' if t_score >= 3 else 'medium'
        reasoning = transformative
    elif m_score >= 1:
        verdict = 'MECHANICAL'
        confidence = 'high' if m_score >= 3 else ('medium' if m_score >= 2 else 'low')
        reasoning = mechanical
    else:
        verdict = 'MECHANICAL'
        confidence = 'low'
        reasoning = ["No clear frame transformation detected"]
    
    return {
        'verdict': verdict,
        'confidence': confidence,
        'reasoning': reasoning,
        'transformative_signals': transformative,
        'mechanical_signals': mechanical
    }


# =============================================================================
# BÖLÜM 3: ANA ANALİZ FONKSİYONU
# =============================================================================

def run_cgi_analysis(filepath: str, sample_size: int = 20, seed: int = 42) -> dict:
    """
    CGI analizini çalıştırır.
    
    Args:
        filepath: Parquet dosya yolu
        sample_size: Analiz edilecek örnek sayısı
        seed: Rastgelelik tohumu (tekrarlanabilirlik için)
    
    Returns:
        Analiz sonuçları dictionary
    """
    random.seed(seed)
    
    # Veriyi oku
    print("[1/4] Veri okunuyor...")
    with open(filepath, 'rb') as f:
        data = f.read()
    
    # Metinleri çıkar
    print("[2/4] Metinler çıkarılıyor...")
    texts = extract_clean_texts(data, min_len=80)
    print(f"      → {len(texts)} temiz metin bloğu bulundu")
    
    # Sınıflandır
    print("[3/4] Metinler sınıflandırılıyor...")
    contexts, responses = classify_texts(texts)
    print(f"      → {len(contexts)} kullanıcı mesajı")
    print(f"      → {len(responses)} danışman yanıtı")
    
    # Örnekle ve analiz et
    print(f"[4/4] {sample_size} örnek analiz ediliyor...")
    sample = random.sample(responses, min(sample_size, len(responses)))
    
    results = []
    for idx, response in enumerate(sample, 1):
        analysis = analyze_response(response)
        results.append({
            'id': idx,
            'text': response,
            **analysis
        })
    
    # İstatistikler
    stats = {
        'total_texts': len(texts),
        'contexts': len(contexts),
        'responses': len(responses),
        'sample_size': len(sample),
        'transformative': sum(1 for r in results if r['verdict'] == 'TRANSFORMATIVE'),
        'mechanical': sum(1 for r in results if r['verdict'] == 'MECHANICAL')
    }
    
    return {
        'results': results,
        'stats': stats,
        'lens': CGI_LENS
    }


# =============================================================================
# BÖLÜM 4: RAPOR ÜRETİCİ
# =============================================================================

def generate_report(analysis: dict) -> str:
    """
    Markdown formatında rapor üretir.
    """
    lines = []
    stats = analysis['stats']
    results = analysis['results']
    
    lines.append("# CGI Analysis Report: Mental Health Counseling Dataset")
    lines.append("## Context Grammar Induction (Socratic Lens) Analysis")
    lines.append("")
    lines.append("---")
    lines.append("")
    
    # Lens bilgisi
    lines.append("## Lens Configuration")
    lines.append("")
    lines.append("**Decision Question:** Does the counselor's response shift the user's underlying frame (Ontology/Belief) or just validate/optimize it?")
    lines.append("")
    lines.append("**Transformative Signals:**")
    for name, _ in CGI_LENS["transformative_signals"]:
        lines.append(f"- {name}")
    lines.append("")
    lines.append("**Mechanical Signals:**")
    for name, _ in CGI_LENS["mechanical_signals"]:
        lines.append(f"- {name}")
    lines.append("")
    
    # Özet
    lines.append("---")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total texts extracted | {stats['total_texts']} |")
    lines.append(f"| User contexts | {stats['contexts']} |")
    lines.append(f"| Counselor responses | {stats['responses']} |")
    lines.append(f"| Samples analyzed | {stats['sample_size']} |")
    lines.append(f"| **TRANSFORMATIVE** | {stats['transformative']} |")
    lines.append(f"| **MECHANICAL** | {stats['mechanical']} |")
    lines.append("")
    
    # Detaylı tablo
    lines.append("---")
    lines.append("")
    lines.append("## Detailed Results")
    lines.append("")
    lines.append("| # | Verdict | Confidence | Key Signals | Response Preview |")
    lines.append("|---|---------|------------|-------------|------------------|")
    
    for r in results:
        preview = r['text'][:80].replace('\n', ' ').replace('|', '/') + "..."
        signals = ', '.join(r['reasoning'][:2]) if r['reasoning'] else "N/A"
        lines.append(f"| {r['id']:02d} | **{r['verdict']}** | {r['confidence']} | {signals} | {preview} |")
    
    lines.append("")
    
    # Transformatif örnekler
    transformative = [r for r in results if r['verdict'] == 'TRANSFORMATIVE']
    if transformative:
        lines.append("---")
        lines.append("")
        lines.append("## 🔥 TRANSFORMATIVE EXAMPLES")
        lines.append("")
        for r in transformative:
            lines.append(f"### Sample #{r['id']}")
            lines.append(f"**Confidence:** {r['confidence']}")
            lines.append("")
            lines.append("**Signals:**")
            for sig in r['transformative_signals']:
                lines.append(f"- {sig}")
            lines.append("")
            lines.append("**Text:**")
            lines.append(f"> {r['text'][:500]}...")
            lines.append("")
    else:
        lines.append("---")
        lines.append("")
        lines.append("## Result: No Context Shifts Found")
        lines.append("")
        lines.append("All analyzed responses operate **MECHANICALLY**.")
        lines.append("")
    
    # Sokratik yansıma
    lines.append("---")
    lines.append("")
    lines.append("## Socratic Meta-Reflection")
    lines.append("")
    lines.append("Mental health counseling responses in this dataset predominantly operate in **MECHANICAL mode** - they help users cope within their existing frame rather than transforming that frame.")
    lines.append("")
    lines.append("**[HUMAN DECISION NEEDED]**")
    lines.append("Whether a mechanical response is 'right' depends on context. The system can **SHOW** this distinction; it cannot **DECIDE** which is appropriate.")
    
    return '\n'.join(lines)


# =============================================================================
# BÖLÜM 5: ANA GİRİŞ NOKTASI
# =============================================================================

def main():
    """Ana fonksiyon."""
    # Dosya yolu
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = "/mnt/user-data/uploads/0000.parquet"
    
    if not Path(filepath).exists():
        print(f"Hata: Dosya bulunamadı: {filepath}")
        sys.exit(1)
    
    print("="*60)
    print("CGI ANALYSIS: MENTAL HEALTH COUNSELING DATASET")
    print("="*60)
    print()
    
    # Analiz çalıştır
    analysis = run_cgi_analysis(filepath, sample_size=20)
    
    print()
    print("="*60)
    print("RESULTS")
    print("="*60)
    print(f"TRANSFORMATIVE: {analysis['stats']['transformative']}")
    print(f"MECHANICAL: {analysis['stats']['mechanical']}")
    print()
    
    # Detayları göster
    for r in analysis['results']:
        print(f"[{r['id']:02d}] [{r['verdict']}] ({r['confidence']})")
        print(f"     {r['reasoning']}")
        print(f"     {r['text'][:100]}...")
        print()
    
    # Rapor üret
    report = generate_report(analysis)
    
    output_path = "cgi_report.md"
    with open(output_path, 'w') as f:
        f.write(report)
    
    print(f"Rapor kaydedildi: {output_path}")


if __name__ == "__main__":
    main()
