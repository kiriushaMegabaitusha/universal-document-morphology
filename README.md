# 05.4 — Universal document morphology

**Version 1.0.1 — frozen 2026-10-06.** A comparative atlas of how the world
formats official documents, and whether a universal document structure exists.

A one-page overview is in `EXECUTIVE_SUMMARY.md`.

## Question

Are there frameworks, legislations and traditions that fix what goes into an
official document — and is there a universal structure that is *proven* the
most efficient carrier of official information, or just a tangle of traditions?

## Answer in one paragraph

There is a convergent **deep grammar** (identity, origin, date, body/dispositif,
authentication, annex) shared across six continents and six centuries; it is
universal because it encodes what *law* requires — attribution, competence,
procedure — not because it is the most efficient information channel; the
surface (layout, wording rituals) is where the traditions genuinely diverge; and
the axis of variation is **genre** (letter vs normative act) more than nation.
The universality claim is **scoped**: it holds for the written official
document, not for record-keeping as such (two non-documentary record systems,
the khipu and wampum, bound it). See `morphology.md`.

## Coverage

**28 systems, six continents, c. 1412–2024.** Full list in `diversity.md`
§1–2 and the per-system case files in `cases/`.

## Files

| file | what |
|------|------|
| `EXECUTIVE_SUMMARY.md` | the whole atlas on one page |
| `morphology.md` | the analytical model: 14 canonical slots, two declensions, convergence matrix, findings |
| `diversity.md` | the diversity test across five tranches + the cross-cutting findings (§10–§13) |
| `STANDARDS.md` | inventory of the standardised landscape, in four layers, with citations |
| `requisites.csv` | the mapping data: every requisite of every system → canonical slot (225 rows) |
| `cases/` | 28 case files, one per system (see `cases/` listing) |
| `ledger.json` | every claim paired with its sources; provisional claims flagged |
| `check_claims.py` | the gate |
| `analysis/` | `findings.md` (slot census, complementarity, similarity, evidence base) · `qualitative_analysis.md` (implication rules, thematic coding, onomastics, diachrony) · CSVs: `slot_matrix`, `slot_similarity`, `theme_matrix`, `document_types`, `evidence_base` |
| `analysis/recompute.py` | rebuilds `slot_matrix`, `slot_similarity` and `evidence_base` from the frozen data, then fails if any figure quoted in `findings.md`, `qualitative_analysis.md` or `EXECUTIVE_SUMMARY.md` has drifted from it |
| `sources/` | retrieved primary/near-primary texts (PDFs + extracted text) |

## The gate

    python3 check_claims.py                  # structure + internal consistency
    python3 check_claims.py --online         # also HEAD-check every retrieved source URL
    python3 analysis/recompute.py            # rebuild the analysis CSVs; fail on drifted figures
    python3 analysis/recompute.py --check    # verify the figures, write nothing

**Status: 60 sources, 92 claims (88 verified, 4 provisional), 225 mapped
requisites across 28 systems. All checks pass.** The gate validates the ledger
schema, the closed slot vocabulary, the 9-field CSV integrity, internal
consistency, and that every claim-id / source-id citation in every `.md` (root,
`cases/`, `analysis/`) resolves to a ledger entry. `analysis/recompute.py`
derives the analysis figures from `requisites.csv` + `ledger.json` and checks
all 28 of them against the prose, so the two can no longer drift apart.

## Key findings (headline)

1. A universal stem — identity, origin, date, body/dispositif, authentication,
   annex — with **authentication (S12) the most universal slot** (17 of 25
   slot-coded systems).
2. The **epistolary/normative fork is a formal negation**: the preamble (S9)
   never co-occurs with authority-mark, addressee, reference, subject, body or
   trace; the addressee (S6) never co-occurs with the preamble.
3. **Genre, not nation**, is the main axis of variation.
4. **Rank is a scalar, not a slot** — encoded in layout (Ottoman blank space),
   in grammar (Saudi), in type names (Senegal, Thailand).
5. Five "kinds of document law": **layout** (Anglophone/Germanic/Sinosphere),
   **formulas** (Francophone), **naming** (UAE), **function** (Soviet/CIS) — plus
   three regime dimensions: **trace**, **access**, **persistence/appraisal**.
6. Two **non-documentary boundaries** (khipu, wampum) that scope the claim — and
   show authority need not live in writing.

## Honest gaps

- **RU / ГОСТ Р 7.0.97-2016 is provisional** (primary text on blocked hosts);
  kept as a labelled placeholder in `cases/ru.md`, not invented. Deliberately
  de-emphasised at the author's request.
- **One provisional Gulf claim** (the UAE guideline index page is JS-only);
  the UAE case itself rests on a retrieved TDRA guide.
- Grounding tiers differ: strong primary anchors (UA, CN, IN, BR, SA, TH, ID,
  VN, BJ, SE, SN, SU); secondary/encyclopedia-based thin cases (PE, HN, ET, WA
  partly) — flagged in each case file.
- Theme coding is keyword-based (no inter-rater kappa); diachronic dating is an
  approximate regime-anchor year with small bins.
- The regime classes and era anchors behind `analysis/` are hand-assigned and
  not derivable from the CSVs, so `recompute.py` checks the figures it can
  derive and leaves those tables alone.
- "Efficiency" is measured nowhere in the standards; `morphology.md` §6 states
  what an empirical test would require.

## Version history

| version | change | systems |
|---------|--------|---------|
| 0.1 | initial set: UA, RU, DE, CN, UN, EU | 6 |
| 0.2 | + Islamic chancery, IN, BR, JP, EE, khipu, ZA | 13 |
| 0.3 | + VN, ID, TH, ET, NG, KE, West African Ajami | 20 |
| 0.4 | + SA, AE, SN, Francophone tradition | 24 |
| 0.5 | + BJ, SE, Haudenosaunee wampum; UAE resolved | 27 |
| 0.6 | + Soviet bloc (ЄДСД/ГОСТ 6.38/ОКУД) | 28 |
| 0.7 | structural + qualitative analyses → `analysis/` | 28 |
| 1.0 | onomastic gap closed (НК 010:2021); gate extended to `analysis/`; frozen | 28 |
| 1.0.1 | analysis figures resynced to the 225-row data (S1 census, SU density, Jaccard, script census, evidence base); `analysis/recompute.py` added as a second gate | 28 |

## Method and provenance

Built with the reusable skill **`comparative-standards-atlas`** (research/):
fixed vocabulary → CSV mapping → claim ledger → gate. Every claim is traceable
to a source; unretrieved sources are labelled, never invented.
