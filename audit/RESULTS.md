# Results — P06-2 exact-null audit (registered run)

**Registration:** commit `2d262cf720aab89f1cf0cf3ffee819e135a0ab35`, 2026-10-15,
`audit/PREREGISTRATION.md` · **Run:** executed once, immediately after registration,
exit 0 · **Deviations:** none (`DEVIATIONS.md`) · **Inputs:** both registered sha256
hashes verified by the script before any test; margins asserted equal to the eight
registered counts · **Machine output:** `results.json` (exact rationals preserved) ·
Arithmetic: exact (`fractions.Fraction`) throughout; no floating point in any
p-value or q-value comparison.

Sanity check before interpretation: the registered hand-worked example reproduces
exactly — S9⊥S6 depletion p = 136/300 = 0.4533.

## Decision table (per §7)

| claim | primary p | BH q | label (registered rule) |
|---|---|---|---|
| **Family C — joint fork** | **10/300 = 0.0333** (floor 0.0033) | single test | **regraded: supported as ONE joint population-level pattern**, replacing the six-census-facts framing |
| S9⊥S4 | 0.4000 | 0.4533 | individually unsurprising; n* = 82 |
| S9⊥S6 | 0.4533 | 0.4533 | individually unsurprising; n* = 94 |
| S9⊥S7 | 0.4000 | 0.4533 | individually unsurprising; n* = 82 |
| S9⊥S8 | 0.3500 | 0.4533 | individually unsurprising; n* = 69 |
| S9⊥S10 | 0.1833 | 0.4533 | individually unsurprising; n* = 44 |
| S9⊥S14 | 0.3033 | 0.4533 | individually unsurprising; n* = 57 |
| S6⇒S12 | 0.0225 | 0.0225 (BY 0.0468) | **inference-supported**; n* = 25 |
| S6⇒S8 | 1/24035 ≈ 0.000042 | 0.0002 (BY 0.0003) | **inference-supported**; n* = 25 |
| S6⇒S10 | 0.0028 | 0.0056 (BY 0.0116) | **inference-supported**; n* = 25 |
| S8⇒S12 | 0.0059 | 0.0079 (BY 0.0165) | **inference-supported**; n* = 25 |

BY (dependence-robust) q-values agree with BH for every family-B rule and reject
nothing extra in family A, as registered (§6.5).

## Registered predictions (§2) — scored whatever way they fell

| prediction | outcome |
|---|---|
| **R1** no family-A edge rejects after BH | **confirmed** (0 of 6) |
| **R2** joint test rejects | **confirmed** (p = 0.0333 < 0.05) |
| **R3** ≥1 family-B rule rejects | **confirmed** (4 of 4) |
| **R4** ≥1 family-A edge with n* > 100 | **NOT confirmed** — largest threshold is 94 (S9⊥S6); every negation edge becomes individually informative before 100 systems |

Three of four. The miss is informative rather than embarrassing: per-edge negations
become testable sooner than P06-2 expected, so corpus expansion (target ≈ 50–95
systems, not 4×) is a cheaper route to per-edge inference than assumed.

## The registered disagreement (§5.2: verdicts follow primary; the disagreement is the finding)

The tradition-blocked secondary null does **not** reproduce the primary result
anywhere it matters:

| family | primary | blocked | reading |
|---|---|---|---|
| A (6 edges) | all q ≥ 0.45 | all p ≥ 0.33 | **agree** — "individually unsurprising" is robust to null choice |
| C (joint fork) | **rejects** (10/300) | **does not** (2/6 = 0.333; only **6** within-block placements exist — tradition nearly fixes the S9 pair) | the fork's marginal surprise is largely *between*-tradition structure; *within* tradition, the observed placement is ordinary at n = 25 |
| B (4 implications) | **4 of 4 reject** (q ≤ 0.0225) | only **S6⇒S8** stays < 0.05 (0.0449); S6⇒S10 0.0871, S8⇒S12 0.2234, S6⇒S12 0.4453 | three of four implications look like tradition-level confounding: within a tradition, destination-marking systems authenticate at rates no higher than within-tradition chance |

Per the registered rule the primary verdicts stand and are reported above; the
blocked column travels beside them in any write-up. The honest one-line summary:
**the fork survives as a joint pattern under the registered primary null, but at
n = 25 its evidence is a between-tradition contrast with thin within-tradition
support, and three of the four perfect implications are tradition-confounded.**

## n* — corpus size at which each claim first becomes individually informative

Negation edges (zero-overlap p < 0.05 at scaled margins): S9⊥S10 44 · S9⊥S14 57 ·
S9⊥S8 69 · S9⊥S4 82 · S9⊥S7 82 · S9⊥S6 94. Implications: all four already
informative at n = 25 (consistent with their p-values). Per-edge α = 0.05, not
multiplicity-adjusted (registered, §6.6).

## Provenance and implementation (registered or declared in advance)

- Tradition blocks: README §Coverage grouping, written at v1.1 (2026-10-06) —
  pre-existing, slot-value-blind, committed as `tradition_blocks.csv` at
  registration. (HN = Haudenosaunee wampum; PE = Inka khipu.)
- Blocked null: S9 placements enumerated exactly within blocks (6 placements);
  family B Monte Carlo 100,000 draws, seed 20261015 + rule index, p =
  (1 + #{stat ≥ observed}) / (1 + draws).
- Margin scaling for n*: floor(x + 0.5); deterministic, closed form, no simulation.
- Code exercised only on synthetic data (`--self-test`) before registration; see
  `DEVIATIONS.md`.

## Limitations (echoing §10, plus what the run showed)

1. Convenience corpus — inference conditional on the atlas's sampling frame.
2. Coding treated as fixed (P06-1 is the separate layer).
3. The blocked null has almost no permutation space for family C (6 placements) —
   its p is real but coarse (multiples of 1/6); blocks are prose groupings, not
   ground truth (§10.3).
4. Dependence within families; BH and BY both reported and agreeing.
5. Prior art for the method stands (E02 challenge-located); the contribution is
   the application, stated so here.
6. Statistical surprise is not mechanism — the historical explanation of the fork
   stays in the atlas's prose layer.
7. `matrix.json`-style selection logic played no part: this file reports a
   registered analysis whose decision rules were fixed before the commit above.