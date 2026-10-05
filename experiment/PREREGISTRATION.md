# Pre-registration — Finding 5 comprehension test

**Status: locked before data collection.** This document, `stimuli.json` and the
analysis code (`analysis_core.py`, `analyze.py`, `simulate_data.py`) are committed
to the project repository *before* the first machine-arm observation and before any
human participant is recruited. The commit hash and date are the registration
timestamp. There is no external registry entry; that limitation is stated in §10
(and an OSF registration is the obvious follow-up if the human arm is run).

Author of the study design: Kyrylo Yasuda. Analysis code written and executed by
the project's Hermes agent; the same agent is the analyst (§10).

## 1. Study information

| field | value |
|---|---|
| title | Does formal register reduce comprehension of the same official obligation? An empirical test of finding 5 |
| project | `05.4_universal_document_morphology` (comparative atlas of official-document standards) |
| claim under test | atlas finding 5: "Nothing in the standards is optimised for comprehension" (`morphology.md` §5, `EXECUTIVE_SUMMARY.md`), and the open thread in `morphology.md` §8: "measure comprehension of the same obligation rendered in UN/EU/UA plain vs formal register" |
| population | human readers (convenience sample) and, separately, language models |
| design | within-item; 6 obligations × 4 registers (2 registers × 2 languages); 12 four-option items |
| registration | this file at git commit (hash in the results file); no external registry |

Two arms are run and reported separately, never pooled:

- **H (human)** — confirmatory. Not yet collected at registration time.
- **M (machine)** — exploratory. Collected by an OpenRouter API script immediately
  after registration; reader = language model.

## 2. Background and hypotheses

The atlas catalogues how 28 systems format official documents. Finding 5 is that
every slot of every format is there for validity, attribution, procedure or
retrievability — none for comprehension — and that the first standard aimed at
comprehension (ISO 24495-1:2023, plain language) is not wired into any of them.
The test is the minimal empirical version of that claim: hold the obligation
constant, vary only the register, and measure how much of it readers extract.

**H1 (primary, confirmatory, arm H).** For the same obligation, accuracy on
four-option items is higher when the obligation is rendered in plain register than
in formal register. Directional.

- *conceptual*: plain register lowers the parsing and inference cost of identical
  content.
- *operational*: difference in proportion of items answered correctly,
  plain − formal, per item, aggregated over readers.
- *statistical*: mean of the 12 item-level differences > 0; exact sign-flip
  randomization test on those 12 paired differences (§6).

**H2 (secondary, arm H).** The register contrast does not differ between English
and Ukrainian renderings. Tested as the register × language interaction;
non-directional; exploratory in direction but with a pre-specified test.

**H3 (secondary, arm H).** The register gap is larger for *inference* items (which
require combining two facts) than for *extraction* items (single-fact lookup).
Directional; pre-specified test.

**M1 (exploratory, arm M).** Language models show the same direction of register
effect. Reported with confidence intervals; **no confirmatory claim**, because the
registered power simulation (§7) shows the machine arm is underpowered for the
effect sizes of interest.

## 3. Design

**Stimuli.** Six obligations (`experiment/stimuli.json`), each rendered in four
registers: `en-formal`, `en-plain`, `uk-formal`, `uk-plain`. The formal renderings
follow the drafting conventions of the corpus (UN/EU legislative style in English;
ДСТУ/наказ chancery style in Ukrainian); the plain renderings follow the four
ISO 24495-1 principles (relevant, findable, understandable, usable) as published by
the International Plain Language Federation.

Every obligation is **constructed for this test**, modelled on named atlas sources
and labelled `verbatim: false`; none is a quotation. Content is held constant by
construction and checked mechanically: `check_stimuli.py` asserts that the numeric
tokens in the formal and plain renderings of the same language are identical, that
they equal the set declared in the gold fact tuple, and that the answer-key letters
point to the correct option text in both languages. **Numbers are written as digits
in all four registers**, deliberately, so that number form is never a second
manipulation.

**Items.** Two per obligation, four options, exactly one correct: Q1 typically an
extraction item, Q2 an inference item (applying two facts together). Answer key is
balanced 3/3/3/3 across A–D to blunt response bias.

**Arm M (machine).** Each reader model answers every item of every document: 6
obligations × 4 registers × 2 items = 48 item-administrations per model; with R
models, 48R observations. Reader models are fixed at registration (§8 of the
runner: model list), temperature 0, single completion per item, one JSON object
requested per item.

**Arm H (human).** Design B from the registered power simulation: each participant
reads, for **each** of the 6 obligations, **both** registers of their chosen
language — 12 documents, 24 items, ≈ 10–15 minutes. Register order within a document
is randomized per participant with a seeded permutation derived from the participant
id, and document order is randomized the same way, so order effects cannot align
with the register contrast. Condition labels are never shown to participants.

## 4. Sampling and recruitment (arm H)

Convenience sample: the author's colleagues and students. **Documented as
non-representative**; no claim about any population. Target N = 36, minimum N = 20
for the locked confirmatory analysis; if fewer than 20 complete sessions are
collected the arm is reported as exploratory and H1 is not tested confirmatorily.

Pre-specified exclusions, applied before analysis: incomplete sessions; sessions
shorter than 8 minutes or longer than 60 minutes; sessions in which the participant
reports not having attempted the questions; mismatched language selection. Excluded
sessions are counted and reported.

## 5. Variables

| variable | arm | definition |
|---|---|---|
| `correct` | H, M | 1 if the chosen option is the keyed answer |
| `register` | H, M | formal / plain (manipulated) |
| `lang` | H, M | en / uk |
| `kind` | H, M | extraction / inference |
| `item`, `document` | H, M | identifiers of the stimulus cell |
| `reader` | H, M | participant id / model id |
| `rt_ms` | H, M | milliseconds from document display to answer submit |
| `confidence` | H | 1–5, self-reported after each document |
| `parse_ok`, `latency_ms`, `completion_tokens` | M | answer-format compliance and cost/latency |

Primary outcome: `correct`. Everything else is secondary or descriptive.

## 6. Analysis plan

All code is registered and was run on simulated data before collection
(`simulate_data.py`); the functions are `analysis_core.py`.

**Locked (confirmatory, arm H).**

1. **Primary test.** Per item, proportion correct in plain minus in formal,
   aggregated over participants; exact sign-flip randomization test on the 12
   paired differences (two-sided p; all 2^12 sign patterns enumerated). Reported:
   the mean difference in percentage points with a 95% percentile bootstrap CI.
2. **Complement (same hypothesis, different estimator).** Logistic regression with
   **item fixed effects** (`logit_fe`): `logit P(correct) = a_item + b·plain`;
   report b, odds ratio, the average marginal effect in percentage points, and the
   Wald p. The sign-flip test decides; the model quantifies.
3. **Equivalence.** TOST against the SESOI (±10 pp, §7) on the item-level
   differences: reported as support for "no decision-relevant difference" only if
   both one-sided tests reject at α = 0.05.

**Locked (secondary family).** H2 and H3, each tested as an interaction coefficient
in `logit_fe` (register × language; register × item kind), p-values corrected by
Benjamini–Hochberg across the family {H2, H3} at α = 0.05.

**Conditional.** If `check_stimuli.py` shows the manipulation does not raise every
surface complexity proxy in both languages, the manipulation is reported as failed,
H1 is still reported (the ITT analogue) and the failure is discussed, but no
mechanism claim is made.

**Exploratory (clearly labelled, no error-rate control).** Arm M in full; the
relationship between model size/family and the register gap; latency and verbosity
differences; item-level difficulty diagnostics; the correlation between confidence
and correctness in arm H.

**Decision rule for H1.** Supported if: mean item difference > 0, exact two-sided
p < 0.05, and the point estimate ≥ 10 pp. Falsified if the TOST rejects differences
of ±10 pp. Otherwise **inconclusive** — reported as such, with the CI, and no claim.

**Multiple testing.** Two hypotheses families, corrected separately: the
confirmatory family is a single test (H1), so no correction; the secondary family
{H2, H3} uses BH-FDR at α = 0.05. Arm M results are exploratory and carry no
corrected p-value claims.

## 7. SESOI and power (from the registered simulation)

`simulate_data.py` (seeded, run before collection) gives, for a true plain
advantage, the rejection rate of the primary test at α = 0.05:

| design | shape | power at 5 pp | at 10 pp | at 15 pp |
|---|---|---|---|---|
| A | split: each participant reads each obligation in one register (12 trials) | 0.10 | 0.32 | 0.62 |
| B | both: each participant reads both registers of every obligation (24 trials) | 0.18 | 0.75 | 0.98 |

(all at N = 24; design B reaches ≥ 0.80 power at a true 10 pp gap by N = 36)

Consequences, decided before data collection:

- **Design B is pre-registered** for arm H.
- **SESOI = 10 pp.** A 5 pp gap is not detectable at any feasible sample size
  (power 0.35 at N = 36), so it cannot be the smallest effect of interest here.
  10 pp is the smallest gap this design can test at the planned N, and is
  decision-relevant for document-format policy: on a 4-option item, moving a
  reader from 70% to 80% correct is roughly a one-third reduction in the error rate.
- **Target N = 36** in arm H.
- **Arm M is exploratory**, not confirmatory: the machine-arm shape with 4 reader
  models has power 0.15 at a 10 pp gap — with 12 models it is ≈ 0.40. Using the
  machine arm to claim a comprehension effect would be a misuse of a design that
  cannot support it.

Null calibration (200 simulated datasets, true effect 0): rejection rate 0.020 at
α = 0.05 — conservative, as expected for an exact test with 12 discrete paired units.

## 8. Contingencies

| contingency | pre-specified response |
|---|---|
| manipulation check fails in one language | report manipulation failure; restrict the H1 claim to the language where it held; no mechanism claim |
| arm H under-recruits (< 20 complete sessions) | report as exploratory; do not test H1 confirmatorily; report the achieved MDE |
| > 15% of sessions excluded for any single reason | report the exclusion analysis and both analyses (with and without) |
| a model returns unparsable answers | excluded from accuracy, counted in a reported compliance rate; never imputed |
| a model refuses or errors on an item | recorded with the error, excluded from accuracy, reported |
| arm H not run at all | the machine arm alone cannot support the comprehension claim (it measures machine legibility); say so explicitly |

## 9. Deviations

Any deviation from §3–§7 is reported with all four elements: what changed, why, the
effect on the severity of the test, and the effect on validity. Both the registered
analysis and the deviated analysis are reported side by side; the registered one is
never replaced. Deviations so far: none (see the results file for the deviation log).

## 10. Limitations declared in advance

1. **The experimenter wrote the stimuli**, including the plain renderings. A
   "plain wins" result could in principle be construction sympathy rather than a
   register effect. Arm M is immune to that specific worry (a language model has no
   stake in my prose), so agreement between arms is the mitigating evidence;
   cross-arm agreement is reported but is not confirmatory for H1.
2. **Register is visible.** Participants can tell a formal text from a plain one.
   Demand characteristics cannot be eliminated, only unlabelled (the instrument
   never names the conditions) and bounded by the fact that the correct answers are
   verifiable against the document, not against expectations.
3. **Twelve items.** The design tests twelve wordings of six obligations. Generalising
   to "official documents" would need a wider item sample.
4. **Convenience sample.** Ukrainian-/English-reading students and colleagues;
   results describe them, not the public.
5. **No external registration.** A git commit is auditable but is not a third-party
   timestamp, and the analyst is also the code author. Anyone rerunning the scripts
   has everything needed to check the analysis independently.
6. **The machine arm measures machine legibility, not comprehension.** It is a
   proxy for one thing the atlas's cybernetic framing cares about (documents as
   state-machine-readable control records), and it is never presented as evidence
   about human understanding.
