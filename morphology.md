# Universal document morphology — the analytical model

Date: 2026-10-06. Companion files: `requisites.csv` (the mapping data),
`STANDARDS.md` (the standardised landscape), `cases/` (per-system detail),
`ledger.json` (source-backed claims).

## 0. The question

Is there a universal structure to official documents, or is it a tangled mass
of national traditions? And if a structure is universal, is it universal
because it is the *most efficient* way to carry official information?

Short answer: there is a convergent deep grammar; it is not universal because
it is efficient (it evolved for validity and authenticity); and the surface
is where the traditions genuinely diverge.

## 1. Premise: a document is a serialised control record

A document is a device for reconstituting an action across space and time, for
readers who were not present when it was made. In cybernetic terms it must
carry variety at least equal to the situation it has to discriminate (Ashby).
Its fixed slots ("requisites" in the Ukrainian/Russian tradition) are the
control alphabet: an attribute schema that turns a unique event into a
comparable record. The project of a "unified system of documentation"
(ДСТУ / ГОСТ / ЕГСД) is, strictly, the canonicalisation of a record type for
the state's database.

## 2. The fourteen canonical slots

Every requisite catalogued in `requisites.csv` maps onto one of these
functional slots:

| id | slot | carries |
|----|------|---------|
| S1 | identity | what kind of document this is (+ title) |
| S2 | identifier | the document's unique, retrievable ID |
| S3 | origin | who issues it, under whose competence |
| S4 | authority-mark | emblem / logo / form code / issuing-organ mark |
| S5 | temporal | date and place of issue |
| S6 | destination | the addressee |
| S7 | reference | links to other documents (your ref / our ref / CC / legal basis) |
| S8 | subject | heading or subject line |
| S9 | setting / preamble | justification, recitals, legal basis ("whereas", 依据) |
| S10 | body | the free substance |
| S11 | dispositif | the binding operative act (enumerated decisions/commands) |
| S12 | authentication | signature, seal, visa, endorsement, approval |
| S13 | annex | enclosures and subordinate matter |
| S14 | trace / audit | registration, receipt, execution and acquaintance marks |

The slots are ordered, not arbitrary: identity → origin → temporal →
destination → reference → subject → (setting) → body/dispositif →
authentication → annex → trace. That ordering is the *syntax* of the document.

## 3. Two declensions

The universal stem splits by genre into two paradigms that differ in exactly
two slots:

- Epistolary (correspondence): fills **S6 destination** and **S7 reference**,
  leaves **S9 setting** empty. (UA letter, DE DIN 5008 letter, CN 信函格式.)
- Normative (act): fills **S9 setting/preamble**, leaves **S6 destination**
  empty, because a normative act is addressed to no one in particular —
  *erga omnes* or *ad intra* — and instead justifies itself. (UN resolution,
  EU regulation/directive/decision, UA наказ, CN 命令.)

Both share the stem: S1, S3, S5, S10/S11, S12, S13. The destination slot and
the setting slot are in complementary distribution — the clearest single
structural finding in this atlas.

## 4. Convergence matrix

Legend: ● present and obligatory · ○ present, optional or genre-bound ·
— absent · ? not verified (see `cases/ru.md`).

| slot | UA | RU? | DE | CN | UN | EU |
|------|----|-----|----|----|----|----|
| S1 identity  | ● | ? | ● | ● | ● | ● |
| S2 identifier| ● | ? | ○ | ● | ● | ○ |
| S3 origin    | ● | ? | ● | ● | ● | ● |
| S4 auth-mark | ○ | ? | ● | ● | ● | ○ |
| S5 temporal  | ● | ? | ● | ● | ● | ● |
| S6 destination| ○ | ? | ● | ○ | — | — |
| S7 reference | ○ | ? | ○ | ○ | ○ | ● |
| S8 subject   | ● | ? | ○ | ● | ● | ● |
| S9 setting   | — | ? | — | — | ● | ● |
| S10 body     | ● | ? | ● | ● | ○ | ● |
| S11 dispositif| ● | ? | — | ● | ● | ● |
| S12 authentication| ● | ? | ● | ● | ● | ● |
| S13 annex    | ○ | ? | ○ | ○ | ● | ● |
| S14 trace    | ● | ? | — | ○ | ● | ○ |

## 5. Findings

1. **Universal stem.** S1, S3, S5, S10/S11, S12, S13 appear in every system,
   across four continents and three centuries. This is the closest thing to a
   universal document structure, and diplomatics (see §7) has described it
   normatively since the 17th century.

2. **Genre, not nation, is the main axis of variation.** The biggest
   difference between a Ukrainian letter and a UN resolution is not
   Ukrainian-vs-UN but epistolary-vs-normative. National standards mostly
   differ *within* a genre, over surface detail.

3. **Trace/audit density tracks the strength of the central recordkeeping
   regime.** Ukraine's ДСТУ 4163:2020 devotes eight of its thirty-two
   requisites to S14 (control, receipt, execution, acquaintance, filing) —
   the densest audit layer in the sample — because Постанова КМУ №55 and
   ДСТУ 4163 are a complete state делопроизводство system. DIN 5008, written
   for the private sector, has essentially none. The UN resolves the problem
   by one central identifier and a meeting/date-of-adoption line.

4. **Identifier formality is a spectrum.** At one end DIN 5008 barely cares
   about a document ID. At the other the UN symbol is a decomposed,
   meaningful grammar (organ / subsidiary body / series / number / year), and
   the Chinese 版头 head carries copy number, secrecy classification and
   urgency — the most "database-like" identifier block in the sample.

5. **Nothing in the standards is optimised for comprehension.** Every slot in
   every system above is there for validity, attribution, procedure or
   retrievability. The first ISO standard aimed at *comprehension* — ISO
   24495-1:2023 (plain language) — is three centuries younger than
   diplomatics and is not yet wired into any of the national document formats
   here. That gap between "legally valid" and "actually understood" is the
   real structural inefficiency, and it is not addressed by any of the
   formatting traditions.

## 6. What "efficient" could even mean

The premise "proven most efficient information carrier" is false as stated:
these formats were never competitively tested. Efficiency would need a metric
— parsing cost, ambiguity, error rate in downstream action, time-to-complete
for the citizen. The administrative-burden literature measures exactly such
costs (Herd & Moynihan) but studies the *procedures*, not the document
grammar. A genuinely empirical comparison of document morphologies is an open
question.

## 7. The theoretical tradition this belongs to

- **Diplomatics** (Mabillon 1681; refounded as archival diplomatics by
  Luciana Duranti) is the formal science of the document's "inner
  constitution": act, persons, procedure, form. It is the ancestor of the
  slot model in §2, built to test authenticity rather than efficiency.
- **Archival theory split** between the Anglo lifecycle model (record is born,
  lives, dies, is archived) and the Australian records continuum (Upward), in
  which the record has no single life-stage. This is a genuine conceptual
  fork about what a "document" even is.
- **The digital turn**: ISO 15489 / ISO 16175 / MoReq2010 formalise records
  *management*; "Rules as Code" / digital-ready legislation formalises the
  document's *content as executable logic*. Both are attempts to make the
  record machine-operable — a return, in a sense, to the ЕГСД ambition of a
  single unified system.

## 8. Open threads

- **Diversity test.** The six systems above are related (UA/RU share a Soviet
  ancestor; DE/UN/EU share Western legal culture; CN is the one outsider). The
  universality claim is re-tested against unrelated traditions — Islamicate
  chancery, India, Brazil, Japan, Estonia, the Inka khipu, South Africa — in
  `diversity.md`, which also adds: authentication as the most variable slot, a
  15th *scalar* dimension (rank/urgency/secrecy), the file as a unit larger
  than the document, and the model's boundary at the khipu.
- Fill the RU/GOST column once a non-blocked mirror is available (see
  `cases/ru.md`); note it is deliberately de-emphasised — the atlas treats it
  as one tradition among many, not a centre.
- Add India, Brazil (already in), Japan and a code-civil vs common-law contrast.
- Test finding 5 empirically: measure comprehension of the same obligation
  rendered in UN/EU/UA plain vs formal register.
