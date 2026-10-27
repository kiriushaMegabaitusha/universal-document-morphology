# Structural & evidence analysis of the atlas data (rerun with 28 systems)

Derived from `requisites.csv` (225 rows) and `ledger.json` (60 sources / 92
claims). Rerun after adding the Soviet bloc (`SU`) and its type taxonomy.
Outputs: `slot_matrix.csv`, `slot_similarity.csv`, `evidence_base.csv` — all
regenerable with `recompute.py`, which also checks the figures below.

## 1. Slot frequency

Of the **28 systems, 25 have page-slot data** (ZA, SE, HN are regimes /
boundary cases with no page slots — by design).

| slot | systems (of 25) |
|------|-----------------|
| S12 authentication | 17 |
| S10 body | 14 |
| S1 identity | 11 |
| S2 identifier | 11 |
| S14 trace | 11 |
| S8 subject | 10 |
| S4 authority-mark | 9 |
| S7 reference | 9 |
| S13 annex | 9 |
| S3 origin | 8 |
| S5 temporal | 8 |
| S6 destination | 8 |
| S11 dispositif | 4 (EU, IN, UA, UN) |
| S9 setting | 2 (EU, UN) |

**Authentication is still the highest-ranked slot (17/25)**; the Soviet bloc's
ОКУД classifier, ГОСТ 6.38 index and type taxonomy pushed **identity (S1),
identifier (S2) and trace (S14) into a joint third (11 each)** — the bloc is
the only regime coded on classifier *and* requisites at once.

## 2. The epistolary/normative fork (unchanged, now on 25 systems)

S6 (destination) × S9 (setting): **both = 0**, only-S6 = 8, only-S9 = 2,
neither = 15. Perfect complementary distribution holds with the 28th system.

The preamble slot's profile is now fully specified: S9 **never** co-occurs with
S4, S6, S7, S8, S10 or S14, and **does** co-occur with S1, S2, S3, S5, S11,
S12, S13. A normative act is therefore, structurally: identity + identifier +
origin + date + preamble + dispositif + authentication + annex, and *no*
authority-mark, addressee, reference, subject, body or trace.

## 3. Coding density by regime class

| class | n | mean slots |
|-------|---|-----------|
| supranational / bloc regime (SU) | 1 | 9.0 |
| page-format standards | 13 | 7.3 |
| normative/institutional | 2 | 5.0 |
| digital-first | 1 | 3.0 |
| pre-modern / non-documentary | 5 | 1.8 |
| records / legal regimes | 3 | 1.7 |

The Soviet bloc is the **densest single regime** in the corpus (9.0) — it codes
requisites, classifier and workflow together. The instrument's domain edge is
unchanged: regimes and non-documentary records score low because they are not
page documents.

## 4. Similarity structure

Jaccard on slot presence. Highest pairs: **JP = KE = HN (1.0)** — a sparsity
artifact (each coded with only S12 + a non-slot category); then **SA–UA 0.85**,
**CN–TH 0.82**, **CN–FR 0.80**, and **BR–SU 0.78** (Brazil's *padrão ofício* and
the Soviet regime remain the widest non-artefact pair, but the bloc's added
identity row pulls it below the 0.88 it scored before the type taxonomy).
Clustering still collapses to one trunk: a common core plus variable periphery,
not discrete families.

## 5. Evidence base

60 sources: encyclopedia 15, official guide/manual 14, other 14, technical
standard 8, legal/normative text 7, academic/secondary 2. **57 of 60
retrieved; 88 of 92 claims verified**, 4 provisional (all from structurally
blocked sources).

## 6. Script families retained in the term data

Latin 120, Cyrillic 56, Arabic 21, Han 17, Thai 10, plus 1 non-script cell (the
blocked AE row). Caveat: many `local_term` cells hold an English gloss, so this
measures source-language terminology retained, not full script coverage.

## 7. What this supports and undercuts

- **Supports:** authentication as the leading anchor (17/25); the
  epistolary/normative fork as a hard fact (S6 ⊥ S9); convergence across
  unrelated bureaucracies (SA–UA, and BR–SU).
- **Undercuts / cautions:** no discrete families (clustering collapses); the
  slot model's domain excludes regimes and non-documentary records; some
  "similarity" is a sparsity artifact; the encyclopedia share of the evidence
  base stands at 15/60 — the Soviet additions were the encyclopedia-heavy ones
  (secondary Ukrainian sources).
