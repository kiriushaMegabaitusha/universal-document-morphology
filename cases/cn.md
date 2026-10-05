# Case: China — GB/T 9704-2012

- **Standard:** GB/T 9704-2012, "Layout key for official document of Party and
  government organs" (党政机关公文格式) [S-GBT9704]. Replaced GB/T 9704-1999;
  applies to documents of Party and government organs at all levels.
- Arguably the most rigorously *single* enforced official-document format in
  the world: one national standard covering the whole Party-state apparatus.

## Structure: 版头 / 主体 / 版记

**版头 (head):**
7.2.1 份号 copy number · 7.2.2 密级和保密期限 secrecy classification and term ·
7.2.3 紧急程度 urgency · 7.2.4 发文机关标志 issuing-organ mark ·
7.2.5 发文字号 document reference number · 7.2.6 签发人 signatory ·
7.2.7 红色分隔线 red separator line.

**主体 (main body):**
7.3.1 标题 title · 7.3.2 主送机关 principal addressee organ · 7.3.3 正文 body ·
7.3.4 附件说明 annex description · 7.3.5 发文机关署名、成文日期和印章 issuing-organ
signature, date and seal · 7.3.6 附注 special note · 7.3.7 附件 annex.

**版记 (record):**
7.4.2 抄送机关 CC organs · 7.4.3 印发机关和印发日期 printing organ and date.

Plus page numbers, and **special-format variants** for the letter (信函格式),
the order (命令/令格式) and the minutes (纪要格式) — genre variants inside one
national format [C08, C09, C10].

## The interesting contrast

China's head block (copy number + secrecy classification + urgency +
reference number) is the most **database-like** identifier block in the
sample: an official document here is explicitly a numbered, classified,
time-prioritised object. The atlas's S2 slot is at its most developed here,
and 版记 gives it a modest audit layer folded into the footer.

## Slot profile

S1 ● (type variants) · S2 ● (份号/密级/紧急/发文字号) · S3 ● (发文机关) ·
S4 ● (发文机关标志) · S5 ● · S6 ○ (主送机关; absent for acts) · S7 ○ (抄送) ·
S8 ● (标题) · S9 — · S10 ● · S11 ● (命令/令) · S12 ● (署名印章) ·
S13 ○ (附件) · S14 ○ (附注/印发)
