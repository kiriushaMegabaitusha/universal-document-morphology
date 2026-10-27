# Results — ideation swarm session udm-ideation-01

**Date:** 2026-10-15 · **Question:** Which new research directions could most extend,
strengthen, or productively challenge this project? · **Decision owner:** Kyrylo Yasuda ·
**Decision (recorded same day):** **P06-2 selected** as the next research direction —
see `DECISION_LOG.md` D002; pre-registration draft at
`P06-2_PREREGISTRATION_DRAFT.md`, **registered at `2d262cf` and run once the same
day** (results at `d6e32bd`, reported in `audit/RESULTS.md`) ·
**Method:** scientific-brainstorming skill, all 10 workflow stages.

*Status correction, appended 2026-10-27: this line originally ended "awaiting
approval before any analysis runs". The study was approved, registered and executed
on 2026-10-15, so the session record would otherwise misstate its own outcome. The
authoritative account is `DECISION_LOG.md` → "Update — registered and run"; nothing
else in this record was altered.*

**Swarm deployed:** 19 subagents total — 8 independent ideators (P01–P08, blind to each
other), 4 independent raters/adversarial reviewers (R01–R04, none an originator),
4 evidence checkers (E01–E04), 3 post-check re-open participants (P09–P11).
Output: **57 ideas** (48 independent + 9 re-open), 23 rated, 23 adversarially reviewed,
23 literature-checked, 11 clusters.

## Process integrity (what was locked, and when)

| control | when fixed |
|---|---|
| focal question, participants, constraints | before any agent ran (session scaffold, validated) |
| 5 criteria, anchors, weights (3/3/2/2/1) | before any idea was read, before any score existed (`CRITERIA.md`) |
| independent generation | no cross-talk, no literature search, no examples given |
| rating | 4 non-originator raters, integer 1–5 + low/high bounds, blind to each other |
| aggregation | declared in advance: median central, min low, max high, strictest ethics status |
| literature check | after rating, bounded search, snippets-first, statuses recorded |
| decision | `decision: null` in `matrix.json` — machine output cannot select a winner |

## The rated 23 (weighted matrix, one-at-a-time weight sensitivity ±0.10)

| rk | idea | score | input interval | sens. rank | rater spread | evidence | ethics | adversarial |
|---:|---|---:|---|---|---:|---|---|---|
| 1 | P06-2 | 90.9 | 68–93 | 1 | 0 | challenge-located | — | retain |
| 2 | P06-4 | 88.6 | 64–98 | 2 | 1 | challenge-located | — | retain |
| 3 | P06-3 | 79.5 | 57–93 | 3–4 | 1 | mixed | — | retain |
| 4 | P07-5 | 79.5 | 57–91 | 3–4 | 0 | challenge-located | — | retain |
| 5 | P08-1 | 77.3 | 43–93 | 5 | 1 | mixed | review-required | external review |
| 6 | P01-1 | 72.7 | 45–89 | 6 | 1 | support-located | — | revise |
| 7 | P08-6 | 70.5 | 39–98 | 7 | 1 | mixed | — | retain |
| 8 | P02-1 | 68.2 | 45–93 | 8–10 | 1 | challenge-located | — | revise |
| 9 | P02-2 | 68.2 | 43–89 | 8–14 | 1 | mixed | — | revise |
| 10 | P02-6 | 68.2 | 45–93 | 9–12 | 1 | challenge-located | — | revise |
| 11 | P04-1 | 68.2 | 45–93 | 8–13 | 1 | mixed | — | revise |
| 12 | P06-1 | 68.2 | 45–91 | 10–13 | 1 | challenge-located | — | retain |
| 13 | P06-5 | 68.2 | 45–91 | 9–14 | 1 | challenge-located | assessed | retain |
| 14 | P08-3 | 68.2 | 39–93 | 8–14 | 2 | mixed | — | revise |
| 15 | P02-4 | 63.6 | 41–80 | 15–17 | 1 | challenge-located | — | retain |
| 16 | P07-3 | 63.6 | 41–89 | 15–17 | 1 | mixed | — | revise |
| 17 | P08-2 | 63.6 | 39–89 | 15–17 | 1 | mixed | review-required | external review |
| 18 | P03-1 | 61.4 | 32–84 | 18 | 1 | mixed | review-required | pause |
| 19 | P04-3 | 61.4 | 20–89 | 19 | 1 | challenge-located | — | pause |
| 20 | P07-1 | 61.4 | 39–95 | 20 | 1 | challenge-located | — | revise |
| 21 | P05-2 | 56.8 | 34–91 | 21 | 1 | mixed | — | revise |
| 22 | P08-5 | 54.5 | 30–93 | 22 | 1 | mixed | — | revise |
| 23 | P05-6 | 47.7 | 23–80 | 23 | 1 | mixed | — | revise |

Scores are decision aids, not evidence. Reading rules:

- **Ranks 1–7 are reasonably separated and stable** (P06-2 and P06-4 do not move under
  any single-weight perturbation; P06-2's own raters agreed exactly — spread 0).
- **Ranks 8–14 are a tie class**, not an ordering: six ideas share score 68.2 and their
  sensitivity ranges interleave (8–14). Treat them as one tier.
- **Input intervals overlap almost everywhere** — they come from the raters' honest
  low/high bounds; a wide interval (P04-3: 20–89) means the raters themselves were
  unsure.
- Only P08-3 had a rater spread of 2 on any criterion; every other idea's central
  ratings agreed within 1 point. Raw per-rater scores: `scores_raw_by_rater.csv`.

## Adversarial dispositions (23 reviews, strongest version first)

**8 retain** (P06-1, P06-2, P06-3, P06-4, P06-5, P07-5, P02-4, P08-6) ·
**11 revise** · **2 pause** (P03-1, P04-3) · **2 external review** (P08-1, P08-2).

The recurring revision demand is the same in almost every case: *freeze the definition,
null model, coding rule, and corpus manifest before computation*, and pre-state the
falsifier — deletion artefacts, detector failure, unblinded coding, and service
non-equivalence could each fake the predicted result. Full templates: `raw/adversarial_R0*.md`.

## Evidence wave (bounded literature check, 2026-10-15)

**1 support-located** (P01-1: diplomatics already documents pre-modern addressee+recital
coexistence — the fork's universality is genuinely at risk) · **10 challenge-located** ·
**12 mixed**.

The challenge pattern is specific and useful: the *methods* proposed are mostly mature
prior art (LLM second coders, Monte Carlo error propagation, form-field ablations,
claim-entailment checking, permutation nulls for typology, retention-codec comparisons),
while the *application to this corpus and its claims* is where novelty would live. Two
challenges are substantive rather than novelty notes: low LLM–human agreement undermines
P02-1's assumption, and published ДСТУ/ГОСТ edition diffs already exist for P04-3.
Absence of results never established novelty — each file records queries, sources seen
and limits (`raw/evidence_E0*.md`).

## Gates (noncompensatory — never averaged into the score)

- **P03-1** — pause: new human participants; ethics review required before any data.
- **P08-1, P08-2** — external review: coding living Indigenous record heritage or
  community governance needs community/subject-matter authorisation this session cannot
  supply. P08-1 ranks 5th on score alone — the gate binds regardless.
- **P04-3** — pause: retrieval/licence probe needed before the design exists.
- This session issues no approvals; `not-assessed` remains honest for the rest.

## Post-check re-open (skill step 8) — 9 new ideas, unrated

After the evidence wave, ideation was deliberately reopened with that knowledge
(`raw/P09.md`–`P11.md`, cluster C11):

- **P09-1** — does the 14-slot grammar re-emerge from the requisites' own vocabulary
  under unsupervised clustering + permutation null, or exist only in the codebook?
- **P09-2** — lineage-blocked nulls: partition the "deep grammar" into convergent
  structure vs common descent.
- **P09-3** — the `obligation` column as predictor of slot presence (leave-one-system-out
  vs prevalence baseline): the stem = what every standard compels.
- **P10-1** — one week-long study: flip-breaking load-bearing cells of the "perfect"
  rules → re-adjudicate only those against `sources/` → decidable/undecidable verdict.
- **P10-2** — merge P06-2/3/4 and P07-5 into a single pre-registered specification
  curve: one robustness-mass per claim instead of four audits.
- **P10-3** — one frozen S6/S9 protocol against three out-of-sample bins, cheapest
  falsifier first, early stopping.
- **P11-1** — bounds analysis of the 24 requisites outside the canonical 14 slots;
  absence-headlines that move inside the bounds get reported as vocabulary-conditional.
- **P11-2** — instrument-sensitivity gate: no register-equivalence verdict (including
  the nulls already printed in README v1.1/v1.2) unless the machine panel shows ≥10 pp
  dynamic range.
- **P11-3** — lineage-restricted re-derivation of convergence claims; effective n =
  independent origins, not systems.

These are candidates, deliberately not rated — the rating round is frozen. A rating
wave for them is one request away.

## Cross-cutting findings about the project itself

1. **The cheapest high-value moves are internal.** The top of the matrix is entirely
   "audit the frozen data properly" (exact nulls, prevalence intervals, hold-out
   prediction, tier-restricted recompute) — the atlas's claims are ready to be regraded
   from census statements to inference, on data already in the repo, CPU-only.
2. **Method novelty is scarce; application novelty is available.** The evidence wave
   says every technique proposed has a literature. Framing must claim the application
   ("first test of a universal document grammar's structural rules under exact nulls"),
   not the technique.
3. **The swarm converged on pre-registration hygiene.** 11 of 23 dispositions say the
   same thing: freeze definitions/nulls/coding rules before computation. That is also
   the owner's own standing preference.
4. **Human-subjects and community-facing ideas cluster low on feasibility** — consistent
   with the constraints given, not with their importance. P03-1's pause and P08-1's
   external review are gate outcomes, not downvotes.
5. **The fork (S6⊥S9) is the most-attacked claim from every direction** — pre-modern
   instruments (P01-1), document-scale corpora (P02-2), a proposed third declension
   (P08-6), lineage blocking (P09-2/P11-3). If one claim deserves a defence plan, it is
   that one.

## What this session is not

No hypothesis was validated; no study was approved; no novelty was established (bounded
searches only); scores are traceable decision aids, not rankings of truth; consensus
among AI raters is not evidence. The decision belongs to the owner.

## File map

- `session.json` — validated register (57 ideas, 11 clusters, 4 decisions; `validation.json`: 0 errors)
- `IDEAS.md` — all 57 ideas by cluster · `CLUSTERS.md` — cluster logic, shortlist, reserves
- `CRITERIA.md` / `criteria.json` — frozen criteria · `scores.csv` + `scores_raw_by_rater.csv`
- `matrix.json` — weighted matrix + sensitivity, `decision: null` · `merge_reviews.py`, `populate_register.py`
- `evidence_status.tsv` · `dispositions.json` · `tables_fragment.md`
- `raw/P01.md`–`P11.md` (registers) · `raw/review_R0*.csv`, `raw/adversarial_R0*.md`,
  `raw/evidence_E0*.md` · `DECISION_LOG.md`
