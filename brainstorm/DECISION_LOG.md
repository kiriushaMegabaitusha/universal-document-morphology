# Decision log — session udm-ideation-01

**Date:** 2026-10-15 · **Scope:** selection of the next research direction(s) for the
universal document morphology project · **Decision owner:** Kyrylo Yasuda (human,
accountable) · **Facilitator:** Hermes agent (AI, non-accountable) ·
**Status: DECISION RECORDED 2026-10-15 — P06-2 selected by the owner (see D002).
Status corrected after the fact: the pre-registration was approved, registered at
commit `2d262cf`, and executed once the same day — outcome appended below under
"Update — registered and run".** The weighted matrix itself still carries
`decision: null` — machines do not select; this log does.

Mirrors `session.json` decisions D001–D005.

## D001 — shortlist (facilitator action, not a scientific decision)

23 of 48 ideas advanced to rating; 25 kept as reserves.
Candidates: P01-1, P02-1, P02-2, P02-4, P02-6, P03-1, P04-1, P04-3, P05-2, P05-6,
P06-1, P06-2, P06-3, P06-4, P06-5, P07-1, P07-3, P07-5, P08-1, P08-2, P08-3, P08-5, P08-6.
Criteria used: the ones frozen in `CRITERIA.md` before any idea was read — one or two
representatives per cluster, feasibility floor ≈3 under the stated constraints, both
"strengthen" and "challenge" directions kept. Revisit trigger: any shortlisted idea shown
infeasible or duplicate → promote a reserve. Reserves: P01-2…P08-4 (see `CLUSTERS.md`),
kept live (D003).

## D002 — no winner selected; matrix produced as a decision aid

**Candidates:** the 23. **Criteria/weights:** information_gain 3, feasibility 3,
rigor_disconfirmability 2, synergy_relevance 2, coverage_breadth 1 (anchors in
`CRITERIA.md`; weight rationale and disclosed conflicts recorded there). **Scale:** 1–5
integers with low/high bounds. **Aggregation (pre-declared):** median of 4 rater
centrals, min of lows, max of highs; strictest ethics status wins; evidence status taken
from the post-rating evidence wave. **Sensitivity:** one-at-a-time weight perturbation,
delta 0.10 (`matrix.json`).

**Raw ratings kept:** `scores.csv` (aggregated), `scores_raw_by_rater.csv` (per-rater
centrals and bounds). **Dissent:** maximal central spread was 2 points on one criterion
for one idea (P08-3); all others ≤1. **Missing ratings:** none — all 4 raters scored all
23.

**Evidence-check protocol:** 4 checkers, 1–3 queries per idea incl. one aimed at
challenging novelty, 2026-10-15, snippets-first, no invented sources; queries/sources/
limits in `raw/evidence_E0*.md`; statuses in `evidence_status.tsv`
(1 support-located, 10 challenge-located, 12 mixed). Limit: bounded search; no claim of
novelty or absence rests on it.

**Adversarial review:** every shortlisted idea reviewed by a non-originator
(`raw/adversarial_R0*.md`); dispositions 8 retain / 11 revise / 2 pause / 2 external
review (`dispositions.json`). Required revisions are recorded per idea in those files and
are conditions, not preferences.

**Feasibility/ethics gates (outside the formula):** P03-1 pause (human subjects →
external ethics review), P08-1 and P08-2 external review (community/Indigenous
consultation), P04-3 pause (retrieval/licence probe). No approval was or can be issued
by this session. Gate status per idea: `session.json → feasibility_and_ethics_reviews`.

**Decision:** **P06-2 selected as the next research direction, chosen by Kyrylo
Yasuda on 2026-10-15.** It was the most robust candidate on every recorded axis:
rank 1 (90.9), rank never moves under any single-weight perturbation, zero rater
disagreement on any criterion, adversarial disposition "retain", desk-only and
CPU-only on frozen data, no ethics gate. Evidence status is challenge-located —
exact/permutation nulls for typological co-occurrence are established prior art —
so the contribution is framed as application to this corpus's rules, and that
framing is carried into the pre-registration. **What the machine produced (the
matrix, the sensitivity, the gates) remains unchanged; this entry is the human
decision on top of it.**

**Outcomes for the rest of the candidate set (all remain eligible):**

- 18 rated, non-gated ideas → `deferred` in the register.
- 4 gate-bound ideas → stay `paused`: P03-1 (human-subjects ethics), P04-3
  (licence/retrieval probe), P08-1 and P08-2 (community/ethics review).
- 25 reserves → remain candidates (D003); 9 post-check ideas → remain candidates,
  unrated (D004).

**Next action (labelled per skill §10): protocol development → preregistration.**
Draft at `brainstorm/P06-2_PREREGISTRATION_DRAFT.md`: claims, nulls, FDR families,
decision rules and contingencies are all fixed on paper before any test statistic
is computed. Sequence: owner approves the draft → files promoted into the repo and
committed (the commit hash is the registration timestamp, house pattern) → analysis
runs once → deviations logged, never silent.

**Rejected/deferred alternatives:** the other 22 rated ideas, deferred not rejected
(rationale in D001/D003 and `CLUSTERS.md`). **Revisit triggers:** owner approval or
amendment of the preregistration before run; any gate cleared re-opens its idea; a
full literature review overturning an evidence status appends a correction here.

## D003 — reserves deferred, not rejected

25 ideas not advanced this round; remain eligible. Trigger: shortlist attrition or owner
preference.

## D004 — post-check re-open after the evidence check (skill step 8)

3 participants (P09 novelty-pivot, P10 synthesis/sequencing, P11 kill-criteria), 9 ideas,
recorded as candidates with `recorded_stage: post-check`, **deliberately unrated** to
keep the rating round frozen. Trigger: owner requests a rating wave for them.

## Amendments and deviations (logged, not hidden)

1. **Rater training on two neutral examples (skill §6) was skipped.** Anchors were
   documented in `CRITERIA.md` instead; raters were instructed to score against anchors
   and to widen bounds when unsure. Effect: possible scale drift between raters; the
   median aggregation and per-rater file let the owner re-calibrate or re-rate.
2. **`evidence_status` was injected into `scores.csv` after the evidence wave**, by
   design (rating stayed blind to literature). Original rater rows all say
   `not-checked`; nothing else was altered post-rating.
3. **Post-check ideas were not rated** (D004) — recorded so nobody mistakes them for
   vetted candidates.
4. **No discrete assumption records were created** (57 structural warnings in
   `validation.json` say exactly this). Assumptions live as free text in each idea's
   `uncertainties` field and in `raw/P*.md`; the validator's warnings are accepted
   rather than papered over with machine-generated assumption entries.
5. **No criteria or weights changed after any score existed.** No idea text was edited
   after generation. Original IDs and wording preserved throughout.

## Revisit triggers (summary)

- Owner records his selection in D002 → execution begins; if a confirmatory study
  results, preregister it before data (existing `experiment/PREREGISTRATION.md` pattern).
- Any gate cleared (ethics determination, licence probe) → re-open the affected idea.
- Full literature review overturns an `evidence_status` → append correction here, do not
  rewrite this log.
- Rating wave requested for post-check ideas → new evaluation round, same criteria (or
  explicitly amended criteria, logged as a new decision entry D006+).

## Update — registered and run (2026-10-15, appended after the outcome was known)

Appended, not rewritten, per the skill's log rule.

- **Registered:** commit `2d262cf720aab89f1cf0cf3ffee819e135a0ab35` —
  `audit/PREREGISTRATION.md`, `audit/tradition_blocks.csv`, `audit/null_audit.py`,
  `audit/DEVIATIONS.md`, committed before any statistic on the real matrix.
  Two pre-registration edits are recorded in the file header: the status flip, and
  the §5.2 block-source widening to the README §Coverage grouping (the draft's
  `diversity.md` §1–§2 source cannot label the base systems DE/CN/UA/EU/UN; the
  README list predates the session and is equally slot-value-blind).
- **Ran once,** exit 0, both sha256 assertions and all eight margin assertions
  passing; exact rational arithmetic; `--self-test` on synthetic data preceded
  registration (it caught one real bug: unserialisable sets in results output).
  **Deviations from §3–§7: none.**
- **Results commit:** `d6e32bd` — `audit/RESULTS.md` + `audit/results.json`.
- **Registered verdicts:** joint fork rejects under the primary null
  (p = 10/300 = 0.0333) → regraded as ONE joint population-level pattern;
  0/6 negation edges reject after BH (all individually unsurprising; n* = 44–94);
  4/4 implications inference-supported (q_BY ≤ 0.047). R1–R3 confirmed,
  **R4 not confirmed** (largest n* = 94 < the predicted > 100).
- **Registered disagreement (§5.2):** the tradition-blocked null does not reject
  the joint fork (p = 1/3 over only 6 within-block placements) and keeps only
  S6⇒S8 of the four implications (blocked p: 0.0449 / 0.0871 / 0.2234 / 0.4453).
  Verdicts follow the primary as registered; the disagreement is reported as the
  finding: at n = 25 the fork's evidence is a between-tradition contrast, and
  three of four perfect implications are tradition-confounded.
- **Open follow-on decision (owner):** whether to reframe headline findings 1–2 in
  `README.md`/`morphology.md` as one joint pattern — the registered decision rule
  requires that prose amendment in a later version, but the atlas is frozen v1.1
  and the edit is his call (session.json D005 carries the same open item).
