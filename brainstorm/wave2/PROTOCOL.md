# B1 — rating wave 2: the nine post-check ideas

**Status: protocol frozen before any score exists.** Date 2026-10-28. Owner:
Kyrylo Yasuda. Facilitator: the project's agent (non-accountable). This wave is
the execution of `brainstorm/DECISION_LOG.md` → revisit trigger "Rating wave
requested for post-check ideas → new evaluation round, same criteria".

It does **not** reopen wave 1: the 23 rated ideas, their scores, `criteria.json`,
`CRITERIA.md` and `matrix.json` are unchanged and are not edited by this wave.

## 1. Scope, fixed before rating

Nine ideas were recorded unrated in `brainstorm/raw/P09.md`, `P10.md`, `P11.md`.
Since then, B3 (registered `bfd6ffc`, reported `7852cd8`) executed part of that
programme. Scope is therefore fixed as follows **before any score exists**:

| idea | status | rated? |
|---|---|---|
| P09-1 vocabulary re-induction | open | **yes** |
| P09-2 descent-controlled convergence test | executed as B3 | no — resolved |
| P09-3 universality as compulsion | **partial**: B3 ran the mandatory-only re-derivation; the leave-one-out mandate-share predictor was **not** run | **yes, on what remains** |
| P10-1 load-bearing-cell adjudication | open | **yes** |
| P10-2 one registered specification curve | **partial**: B3 ran a six-cell curve for its own families only; P06-2/3/4/P07-5 are **not** merged | **yes, on what remains** |
| P10-3 cheapest-bin-first fork falsification | open | **yes** |
| P11-1 vocabulary bounds + open extraction | **partial**: B3 reported prevalence intervals and the mandatory-only matrix; the 24 off-vocabulary rows' bounds analysis and the open-extraction pass were **not** run | **yes, on what remains** |
| P11-2 sensitivity gate before register nulls | open (human arm paused, so pre-recruitment) | **yes** |
| P11-3 lineage-aware nulls | executed as B3 | no — resolved |

Raters are told the **status**, not B3's results: the question is whether the
remaining work is worth doing, not whether the finished part succeeded.

## 2. Criteria — unchanged

The five criteria, directions, anchors and weights are exactly those frozen on
2026-10-15 in `brainstorm/CRITERIA.md` and `brainstorm/criteria.json`:
`information_gain` 3, `feasibility` 3, `rigor_disconfirmability` 2,
`synergy_relevance` 2, `coverage_breadth` 1. No anchor, weight or definition is
changed. Scale: integer 1–5, with `low`/`high` uncertainty bounds
(`1 ≤ low ≤ score ≤ high ≤ 5`); abstention is permitted.

Score formula (the one wave 1 used, verified against its published scores):
`100 · Σ wᵢ(cᵢ − 1) / (4 · Σ wᵢ)`.

## 3. Raters

Four independent non-originator raters (R01–R04), each in a separate session,
blind to each other and to wave 1's scores. They must not open `scores.csv`,
`scores_raw_by_rater.csv`, `matrix.json`, `tables_fragment.md` or
`dispositions.json`. No literature search: the rating judges the design, not its
novelty, and the original wave rated before the evidence check for the same
reason. Evidence status is therefore `not-checked` at rating time.

## 4. Aggregation — declared now

- central per rater → **median**; with four raters, the lower-middle of the two
  middle values (integer scale, as wave 1).
- `low` = min over raters' lows; `high` = max over raters' highs.
- spread flag when max central − min central ≥ 2 on any criterion.
- `ethics_status` = the strictest any rater assigns; `not-applicable` unless a
  rater says otherwise.
- weighted score per idea from the median centrals; sensitivity = one-at-a-time
  weight perturbation ±0.10, reported as the rank range.
- **`decision: null`.** The matrix is a decision aid. Machines do not select; the
  owner records any decision separately in `DECISION_LOG.md`.

## 5. Evidence wave — bounded, after rating

Bounded check for the **top three** by weighted score only (one or two queries
each, snippets-first, queries and sources recorded). The other four carry
`not-checked`. No claim of novelty or absence rests on the check.

## 6. Gates

No human, community or Indigenous data is used by any rated idea; all are
CPU-only on frozen repo artefacts or public texts. P10-3 and P11-1 retrieve only
public documents. Ethics: `not-applicable` unless a rater finds otherwise.
No idea in this wave clears the P03-1 / P08-1 / P08-2 / P04-3 gates by itself.

## 7. Contract and outputs

Each rater writes `brainstorm/wave2/raw/review_R0{1..4}.json`:

```json
[{"idea_id": "P09-1",
  "information_gain": {"score": 4, "low": 3, "high": 5},
  "...": "one object per criterion",
  "qualitative_review": "2-4 sentences",
  "uncertainties": "1-3 sentences",
  "ethics_status": "not-applicable"}]
```

Then `python3 brainstorm/wave2/merge.py` writes `scores.csv`,
`scores_raw_by_rater.csv`, `matrix.json` and the console table. `RESULTS.md` is
written by the facilitator from the merged output, with the wave-1 caveats: scores
are decision aids, consensus among AI raters is not evidence, and no hypothesis is
validated by this wave.

## 8. Limitations, stated in advance

- One rater population (language models), no human expertise; wave 1 had the same
  limitation and it is not repaired here.
- Seven items instead of nine; two ideas are resolved and are not re-scored.
- Partial-execution status is a judgment by the facilitator; the status table is
  frozen above to keep it auditable.
- The analyst ran B3, which executes parts of three ideas; the raters see only the
  status line, never B3's numbers.
