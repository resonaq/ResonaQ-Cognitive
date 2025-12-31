# ResonaQ Cognitive Architecture
Descriptive map of a layered resonance system (informational, not prescriptive)
Katmanlı yankı sistemine dair betimsel harita (bilgilendirici, yönerge değil)

## What is ResonaQ?
ResonaQ is a cognitive architecture that treats prompts as interfaces, not identities. It keeps ontology and constraints in a kernel, applies policy only for visibility and format, and treats contradiction as energy rather than failure.

## ResonaQ Nedir?
ResonaQ, kimliğin metinde sabitlendiği bir istem değil; çekirdekte tutulan ontoloji ve kısıtları görünürlük/format politikasıyla filtreleyen, çelişkiyi arıza değil enerji olarak gören bilişsel bir mimaridir.

## Why this repository exists
This repository preserves the kernel source of truth, the policy filter, protocol specifications, evaluation artifacts, and rationale docs so contributors and agents share one descriptive map without embedding governance into runtime behaviors.

## Bu depo neden var?
Bu depo, çekirdek gerçeği, politika filtresini, protokol şemalarını, değerlendirme çıktıları ile gerekçe dokümanlarını tek haritada tutarak katkıcıların ve ajanların yön üretmeyen, betimleyici bir zemin paylaşmasını sağlar.

## Architecture Overview
- Kernel: canonical ontology and constraints (`kernel/system_snapshot_motorcore.json`).
- Policy: visibility/format filters (`policy/talimat.en.md` canonical, `policy/talimat.tr.md` rationale).
- Protocol: experiment and bridge specs (`experiment_protocol.json`, `specs/bridge.json`).
- Evaluation: uncertainty/e-score tooling and recorded runs (`e-score/`, `runs/runs/`).
- Artifacts: architecture boundaries and anti-patterns (`docs/not_to_become.md`, `docs/not_to_become.tr.md`, `AGENTS.md`).
- Legacy snapshots and early DSS protocols are archived under /legacy (non-canonical).

## Mimariyi sezgisel anlatım
Bu mimari çelişkiyi hata değil sinyal olarak okur; yankı ve rezonans (YRE) bir hedef değil durumu betimleyen nabızdır. Çelişki Entropisi (ΔÇE) dalgalanmayı sezdirir; meta-analiz çekirdeği ölçekler ve heterojenliği ritim olarak yorumlar. Yön bulma (direction-finding) deneysel ve test edilemez alanda kalır; yönetişim ise görünür/test edilebilir kanalda durur ve aynı çıktıyı paylaşmaz.

## Key Cognitive Concepts
- Cognitive architecture vs prompt: the kernel encodes identity/constraints; prompts are surfaces, not the source of truth.
- Kernel vs Policy vs Protocol vs Rationale: kernel holds facts; policy shapes presentation; protocol defines data/flow contracts; rationale documents explain context without authority.
- Contradiction as signal: disagreement indicates live energy, not an error state.
- Contradiction Entropy (ΔÇE): intuitive measure of how contradiction fluctuates over time and scale.
- Resonance & YRE: descriptive readout of echo intensity and alignment; a lens, not an optimization target.
- Meta-analysis core: scale, heterogeneity, and rhythm matter to interpret signals without collapsing complexity.
- Direction-finding is not testable and stays outside governance/output channels.
- Governance is testable (visibility/format) and must never share the same channel as direction-finding.

## Temel Kavramlar
- Bilişsel mimari vs istem: kimlik ve kısıt çekirdekte; istem yüzeyi yalnızca arayüzdür.
- Çekirdek / Politika / Protokol / Rationale: gerçekler çekirdekte; politika gösterimi ayarlar; protokol akış sözleşmesini tanımlar; rationale bağlamı açıklar ama hükmetmez.
- Çelişki sinyaldir: uyuşmazlık canlılık göstergesidir, hata durumu değildir.
- Çelişki Entropisi (ΔÇE): çelişkinin zaman ve ölçek boyunca nasıl dalgalandığını sezgisel anlatır.
- Rezonans ve YRE: yankı yoğunluğu ve hizalanmayı betimleyen mercek; hedeflenen skor değil.
- Meta-analiz çekirdeği: ölçek, heterojenlik ve ritim, sinyali yorumlamak için gereklidir; karmaşıklığı bastırmaz.
- Yön bulma test edilemez ve yönetişim kanalıyla karışmaz.
- Yönetişim görünür/test edilebilir; davranış üretmekten ziyade sunum sınırını kontrol eder.

## Language Policy
English documents are canonical; Turkish documents are rationale only; when mirrored, English resolves conflicts.

## Dil Politikası
İngilizce belgeler kanonik, Türkçe belgeler gerekçe/anlatı; aynalı içerikte çakışma olursa İngilizce geçerlidir.

## What this repository is NOT
- Not a direction-finding autopilot or recommender.
- Not a place where governance and decision-making share the same output channel.
- Not an optimization scoreboard for resonance or entropy.
- Not a persona manifesto; identity lives in the kernel, not in prose.

## Ne değildir
- Yön seçen bir otomatik pilot ya da öneri motoru değildir.
- Yönetişim ile karar üretiminin aynı çıktıyı paylaştığı bir yer değildir.
- Rezonans veya entropiyi puanlama/optimizasyon tahtası değildir.
- Çekirdekteki kimliği metne dönüştüren bir kişilik manifestosu değildir.
