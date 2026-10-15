# Evaluation criteria — session udm-ideation-01

Defined by the facilitator on 2026-10-15 **before any idea from the independent
round was read** (criteria were fixed while wave 1 was still running). No score
has been seen at the time of writing. Weights will not change after scores exist.

Scale: integer 1–5 on every criterion, with `low`/`high` bounds allowed where
the rater is uncertain. `not assessable` and abstention are permitted instead
of forced precision. Machine-readable form: `criteria.json` (consumed by
`evaluate_matrix.py`).

## Criteria, direction, anchors, weight

### 1. information_gain — weight 3, higher is better
Ability of the outcome to discriminate between live explanations or resolve a
genuine open question of the project.
- 1: produces another instance of a pattern already documented; no live question moves.
- 3: addresses an open question, but the outcome is roughly predictable from the repo as it stands.
- 5: the result would visibly shift belief between competing explanations of a headline finding (e.g. deep-grammar-vs-tradition, genre-vs-nation).

### 2. feasibility — weight 3, higher is better
For the decision owner: one PhD student, CPU-only local rig + optional Kaggle
GPU (30 h/week), no large budget, ~1–3 months of focused work.
- 1: requires new large-scale recruitment, multi-year ethics cycles, paid corpora, or a consortium.
- 3: requires a modest new data collection or substantial new coding, but is doable solo.
- 5: reuses frozen repo data/code; completable in weeks on existing compute.

### 3. rigor_disconfirmability — weight 2, higher is better
Measurable outcome, sharp disconfirming observation, pre-registerable analysis,
fit with the repo's ledger/gate discipline.
- 1: outcome is narrative or unfalsifiable ("would enrich our understanding").
- 3: measurable, but alternative explanations would remain hard to separate.
- 5: competing predictions stated in advance; analysis derivable from existing repo tooling; null result still informative.

### 4. synergy_relevance — weight 2, higher is better
Direct extension, strengthening, or productive challenge of a *named* finding of
the atlas or its experiment, versus an adjacent topic.
- 1: tangent — official documents are the setting, not the object.
- 3: connects to the 14-slot model generally, no specific claim.
- 5: directly tests, extends, or threatens a numbered finding or the scoped universality claim.

### 5. coverage_breadth — weight 1, higher is better
Adds geographic, cultural, or genre breadth, or de-centres the metropolitan
axis. (Decision owner's stated priority; deliberately lowest weight so it can
narrow, not decide.)
- 1: adds only traditions already well represented in the 28 systems.
- 3: adds one modestly underrepresented region or genre.
- 5: opens a genuinely underrepresented tradition, a non-documentary system, or a non-European axis of comparison.

## Weight rationale
information_gain and feasibility carry the most weight because the owner needs
new knowledge per unit of a very tight resource budget. rigor_disconfirmability
and synergy_relevance follow: this project's identity is traceable claims.
coverage_breadth is a stated preference of the owner, hence included but
marginal.

## Disclosed conflicts and dependencies
- information_gain and feasibility are expected to be negatively correlated; the compensatory formula will trade them off explicitly.
- synergy_relevance partially overlaps coverage_breadth (both reward staying close to the atlas); double-counting risk disclosed, weights kept unequal (2 vs 1).
- coverage_breadth encodes the owner's preference, not a scientific property of the idea; rankings sensitive to it should be read accordingly.

## Noncompensatory gates (outside the formula; never averaged away)
- `ethics_status`: not-applicable | not-assessed | review-required | redesign-required | stop. Any idea needing new human participants is `review-required` until an authorized body acts; approval can never be issued by this session.
- `evidence_status`: not-checked | search-incomplete | support-located | challenge-located | mixed. Absence from a bounded search does not establish novelty.
- Resource veto: an idea rated feasibility 1 cannot be the recommended *next action* regardless of total score; it may be logged as deferred.

## Process rules
- Ratings come from independent reviewers who did not originate the idea they score; raw per-rater scores are kept, disagreement is reported, medians feed the matrix.
- Sensitivity: one-at-a-time weight perturbation, delta 0.10, via `evaluate_matrix.py`.
- `decision` stays null in all machine outputs: the human owner decides.
