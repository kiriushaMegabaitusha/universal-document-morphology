# Finding 5 — empirical comprehension test

The atlas's finding 5 (`morphology.md` §5) says the document traditions are built
for validity, attribution, procedure and retrieval — **nothing in them is optimised
for comprehension** — and `morphology.md` §8 sets the test: *measure comprehension
of the same obligation rendered in plain vs formal register*. This directory is that
test.

It is the first component of the atlas that is **not** source-based: the claim under
test is empirical, so it gets a design, a pre-registration, stimuli, code and data
rather than a citation.

## Status

| item | state |
|---|---|
| design + pre-registration | done, committed **before** any data (`3c1469e`); revised to v2 pre-collection (`DEVIATIONS.md` Revision 1) |
| stimuli (6 obligations × 4 registers, 18 items) | done, gated by `check_stimuli.py` |
| analysis code, run on simulated data first | done (`simulate_data.py`); power at the 10 pp SESOI is 0.92 at N = 24 and 0.98 at N = 36 |
| human instrument | built, and end-to-end tested headlessly (19 checks incl. regressions for the two v1 GUI bugs); **no participants yet** |
| machine arm (12 reader models, 864 item-administrations) | **run on v2** — exploratory; result below |
| **human arm (N = 36 target)** | **paused by owner decision (2026-10-27) — no collection** |

## What the machine arm found (exploratory, not evidence about people)

860 of 864 item-administrations parsed (compliance 99.5%, strict JSON 95.1%; one
re-run pass at a higher token budget — see `DEVIATIONS.md`). Cost: **$0.0314** in
total for all 12 reader models.

- accuracy: formal **0.928** vs plain **0.926** — mean item-level difference
  **−0.2 pp**, exact sign-flip p = **1.00**, 95% CI [−1.8, +1.2] pp;
- TOST against the pre-registered ±10 pp margin: **equivalent**;
- the item-fixed-effects logistic model still reports a small positive coefficient
  (β = +0.62, OR 1.9, Wald p = 0.009, AME +4.5 pp) while the pre-registered primary
  test reports nothing — the same pooling artefact as on v1, driven by the cells
  where the weakest reader is guessing;
- the harder inference items do bite (extraction 0.948 vs inference 0.910) but
  **6 of 12 reader models still scored 100%** in both registers, and only
  llama-3.2-1b (41.7%) and llama-3.1-8b (88.9%) have real headroom;
- two of the new hard items (D2-Q3, D5-Q3) show formal *better* by 8.3 pp — one
  model's worth of difference, i.e. noise at this reader count, and reported as such.

**Reading.** For capable machine readers the item set is still near ceiling, so the
arm cannot measure a register effect: it neither supports nor refutes anything about
human comprehension, and as a proxy it is the wrong instrument at this difficulty.
What it does say is that formal register does not impede machine extraction of these
obligations — the documents are already machine-legible in either register. For the
human arm the useful signal is the difficulty gradient: the reasoning items
discriminate (0.91 vs 0.95), which is the headroom the registered MDE needs.

## Running the pieces

```bash
cd <project root>

python3 experiment/check_stimuli.py       # structure, content preservation, answer key
python3 experiment/simulate_data.py       # registered pipeline on simulated data, power/MDE
python3 experiment/build_survey.py        # regenerate human_survey.html from stimuli.json
python3 experiment/test_survey_headless.py  # drive the instrument in Chromium (needs playwright)
python3 experiment/dryrun_confirmatory.py   # exercise the confirmatory path at N=36 on synthetic data

python3 experiment/machine_arm.py         # collect the machine arm (needs OPENROUTER_API_KEY
                                          # in ~/.hermes/.env; ~$0.02, ~5 minutes, resumable)
python3 experiment/analyze.py             # -> results/RESULTS.md + machine_summary.json
```

## Running the human arm

**Paused by owner decision (2026-10-27): no participants are being recruited.**
The runbook below is retained unchanged so the arm can restart without redesign.
No human data exists; the machine arm cannot substitute for it (§7 of the
pre-registration), so finding 5 remains untested in people.

A session is 12 screens of three questions each (36 questions, 15–20 minutes). Each
participant reads each obligation in both registers, but the two readings are placed
in different halves of the session, never fewer than four screens apart, so the
formal and plain versions are never seen back to back.

1. Send participants `human_survey.html` (35 KB, single file, works offline; it is
   generated from `stimuli.json`, so no text is retyped).
2. Each participant picks Ukrainian or English, reads 12 screens (each obligation
   in both registers, order randomised per participant), answers 36 questions plus a
   confidence rating per screen, and downloads a JSON file.
3. Collect the JSONs and score them:
   ```bash
   python3 experiment/score_human.py --dir exports/ --min-n 20
   ```
   Correctness is recomputed from `stimuli.json` (never trusted from the client) and
   the pre-registered exclusions are applied. Writes `results/human_tidy.csv` and
   `results/HUMAN_RESULTS.md` with the pre-registered verdict:
   supported / falsified / inconclusive. Below `--min-n` participants the arm is
   reported as exploratory instead. "Falsified" means the data exclude a plain
   advantage of 10 pp or more — it is not a finding that formal beats plain.
4. Target **N = 36** complete sessions (registered; ~10–15 minutes each).

## Files

| file | what |
|---|---|
| `PREREGISTRATION.md` | hypotheses, design, SESOI, decision rules, power, contingencies, limitations |
| `stimuli.json` | 6 obligations × {en,uk} × {formal,plain}, gold fact tuples, 12 items |
| `check_stimuli.py` | gate: structure, content preservation across registers, independent answer key, manipulation check |
| `analysis_core.py` | shared analysis: exact sign-flip test, logistic FE, TOST, bootstrap CIs, BH-FDR |
| `simulate_data.py` | pipeline check, null calibration, power/MDE (the basis for design B and the 10 pp SESOI) |
| `machine_arm.py` | OpenRouter runner, 12 registered reader models, resumable JSONL |
| `analyze.py` | machine-arm analysis → `results/RESULTS.md` |
| `build_survey.py` | generates the participant instrument from `stimuli.json` |
| `human_survey.html` | the instrument (generated — do not hand-edit) |
| `test_survey_headless.py` | dev harness: drives the instrument in Chromium |
| `dryrun_confirmatory.py` | dev harness: runs the confirmatory path at N = 36 on synthetic data and asserts the decision rule (SESOI-sized effect detected; sub-SESOI and null never "supported"; all three branches reachable) |
| `score_human.py` | scores participant exports, applies exclusions, writes the human report |
| `DEVIATIONS.md` | deviation and erratum log (both entries reported side by side) |
| `recruitment/` | the pack to send: bilingual invitation and debrief, plus the no-priming rule and order of contact |
| `exports/` | where returned participant JSON files go, with the collection note and `MANIFEST.csv` |
| `results/` | raw JSONL, summaries, reports, manipulation check, cost table |

## Honest limitations

Declared in advance in `PREREGISTRATION.md` §10 and repeated here because they
matter: the stimuli (including the plain renderings) were written by the
experimenter; register is visible to participants; twelve items; a convenience
sample; no external registry (a git commit is the timestamp); and the machine arm
measures machine legibility, never human comprehension. The ceiling finding above
adds a thirteenth: this item set may be too easy for the intended human readers.
