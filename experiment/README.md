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
| design + pre-registration | done, committed **before** any data (`3c1469e`) |
| stimuli (6 obligations × 4 registers, 12 items) | done, gated by `check_stimuli.py` |
| analysis code, run on simulated data first | done (`simulate_data.py`) |
| human instrument | built and end-to-end tested headlessly; **no participants yet** |
| machine arm (12 reader models) | **run** — exploratory; result below |
| **human arm (N = 36 target)** | **not run — waiting on participants** |

## What the machine arm found (exploratory, not evidence about people)

575 of 576 item-administrations parsed (compliance 99.8%, strict JSON 95.8%;
one re-run pass at a higher token budget — see `DEVIATIONS.md`). Cost: **$0.0198**
in total for all 12 reader models.

- accuracy: formal **0.937** vs plain **0.944** — mean item-level difference
  **+0.7 pp**, exact sign-flip p = **0.50**, 95% CI [+0.0, +1.8] pp;
- TOST against the pre-registered ±10 pp margin: **equivalent**;
- the item-fixed-effects logistic model does show a small positive coefficient
  (β = +0.86, OR 2.4, Wald p = 0.005, AME +5.3 pp), driven entirely by the cells
  where a weak model was still guessing — the pre-registered primary test does not
  corroborate it;
- **9 of 12 reader models scored 100%** on every item, in both registers. Only
  llama-3.2-1b (43.8%), llama-3.1-8b (91.7%) and qwen-2.5-7b (93.8%) had any
  headroom.

**Reading.** For capable machine readers this item set is at ceiling, so it cannot
measure a register effect; the honest conclusion is that the machine arm neither
supports nor refutes anything about human comprehension — and that, as a proxy, it
was the wrong instrument at this difficulty. It does say something useful for the
human arm: the items are easy for a competent reader, so human accuracy may sit
near ceiling too, which is exactly the risk the pre-registered power analysis
assumed away (it modelled a base rate of 0.72). If human accuracy lands above ~0.90
the registered MDE will not be met, and the honest move is a harder stimulus
version (v2), not a reinterpretation.

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

1. Send participants `human_survey.html` (29 KB, single file, works offline; it is
   generated from `stimuli.json`, so no text is retyped).
2. Each participant picks Ukrainian or English, reads 12 documents (each obligation
   in both registers, order randomised per participant), answers 24 questions plus a
   confidence rating, and downloads a JSON file.
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
