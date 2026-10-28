# 05.4 — Universal document morphology

**Version 1.4 — 2026-10-28.** A comparative atlas of how the world
formats official documents, and whether a universal document structure exists.

A one-page overview is in `EXECUTIVE_SUMMARY.md`. The plan — what is finished,
what is live, what comes next, and which document wins when they disagree — is in
`PLAN.md`. A teaching version (interactive, self-contained HTML) is in
`education/`, and is served at
<https://kiriushaMegabaitusha.github.io/universal-document-morphology/>.

## Question

Are there frameworks, legislations and traditions that fix what goes into an
official document — and is there a universal structure that is *proven* the
most efficient carrier of official information, or just a tangle of traditions?

## Answer in one paragraph

There is a convergent **deep grammar** (identity, origin, date, body/dispositif,
authentication, annex) recurring across six continents and six centuries; it
recurs because it encodes what *law* requires — attribution, competence,
procedure — not because it is the most efficient information channel; the
surface (layout, wording rituals) is where the traditions genuinely diverge; and
the axis of variation is **genre** (letter vs normative act) more than nation.
The regularity is **system-level, not lineage-universal**: no stem slot is
present in every documented lineage, and no lineage clustering is detectable
(B3, `lineage/RESULTS.md`). The claim is also **scoped** to the written official
document, not to record-keeping as such (two non-documentary record systems,
the khipu and wampum, bound it). See `morphology.md`.

## Coverage

**28 systems, six continents, c. 1412–2024.** Full list in `diversity.md`
§1–2 and the per-system case files in `cases/`.

## Files

| file | what |
|------|------|
| `PLAN.md` | the project plan and single source of truth for status: precedence, current state, active workstream, backlog, standing rules, open decisions |
| `education/` | interactive teaching page (archify): the model, the evidence, and the regrade — open the HTML in a browser |
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
| `experiment/` | the empirical test of finding 5: pre-registration, stimuli, analysis code, machine-arm data and the participant instrument — see `experiment/README.md` |
| `sources/` | retrieved primary/near-primary texts (PDFs + extracted text); **not redistributed in this public snapshot** — see `sources/README.md`, URLs are in `ledger.json` |

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

1. A convergent stem at **system level** — identity, origin, date,
   body/dispositif, authentication, annex — with **authentication the
   highest-ranked slot** (17 of 25 slot-coded systems; 13 of 18 documented
   lineages). It is **not lineage-universal**: no stem slot is present in every
   lineage (B3, `lineage/RESULTS.md`).
2. The **epistolary/normative fork is a formal negation of the pattern, not six
   separate laws**: the census fact is unchanged — in the 25 slot-coded systems
   the preamble (S9) carries none of authority-mark, addressee, reference,
   subject, body or trace, and the addressee (S6) never co-occurs with the
   preamble — and the registered exact-null audit (`audit/RESULTS.md`,
   2026-10-15) regrades how it counts: no individual "never" edge is surprising
   at these margins (all BH q ≥ 0.45; each becomes informative only at 44–94
   systems), while the joint pattern of all six rejects independence (exact
   p = 10/300). The fork is therefore reported as ONE joint population-level
   pattern; under a tradition-blocked null the joint pattern does not reject
   (p = 1/3 over 6 within-block placements) — its surprise is between-tradition.
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
  what an empirical test would require. That test is now designed, pre-registered
  and half-run (`experiment/`): the machine arm found no detectable register effect
  and hit a ceiling for 9 of 12 reader models, so it is reported as exploratory and
  says nothing about human comprehension; the human arm has not been run, and its
  current status is tracked in `PLAN.md`.
- **The stem is system-level, not lineage-universal.** B3 (`lineage/RESULTS.md`,
  2026-10-27) found no stem slot present in every documented lineage (0 of 6 under
  both readings) and no detectable lineage clustering (p = 0.518); authentication
  ranks first at 13 of 18 lineages, but its 95 % interval (0.465–0.903) does not
  license a majority claim.

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
| 1.1 | finding 5 given an empirical test (`experiment/`): pre-registered design, stimuli, analysis code, machine arm run over 12 reader models (no detectable register effect; item set at ceiling for 9 of them); human instrument built and awaiting participants | 28 |
| 1.2 | test revised to v2 before any data: 18 items instead of 12 (harder reasoning items added), and the two registers of an obligation are no longer presented consecutively; instrument bugs fixed (language switch, skip control); power at the pre-registered SESOI now 0.92 at N = 24, 0.98 at N = 36; machine arm re-run on v2 (still no detectable register effect, still near ceiling for 6 of 12 readers) | 28 |
| 1.3 | finding 2 regraded by the registered exact-null audit (`audit/`): the fork is reported as one joint population-level pattern (exact p = 10/300), each individual "never" edge carries an informativeness threshold n* = 44–94 systems, and the tradition-blocked sensitivity (joint p = 1/3) is noted; `EXECUTIVE_SUMMARY.md` and `morphology.md` §3 aligned | 28 |
| 1.4 | stem regraded by the registered B3 lineage audit (`lineage/`, registered `bfd6ffc`, run once): "universal stem" → **system-level, lineage-conditional** (no stem slot present in every documented lineage, 0/6); no detectable lineage clustering (base p = 0.518); authentication remains rank 1 (13 of 18 lineages) without a majority claim; README, `morphology.md`, `EXECUTIVE_SUMMARY.md` and `analysis/findings.md` wording aligned | 28 |

## Method and provenance

Built with the reusable skill **`comparative-standards-atlas`** (research/):
fixed vocabulary → CSV mapping → claim ledger → gate. Every claim is traceable
to a source; unretrieved sources are labelled, never invented.
