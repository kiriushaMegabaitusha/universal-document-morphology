# Deviation and erratum log — finding-5 comprehension test

The pre-registration (`PREREGISTRATION.md` §9) commits to documenting every
departure from the registered plan with four elements: **what** changed, **why**,
the effect on **severity** (does the test become more or less able to falsify the
hypothesis?), and the effect on **validity** (does the inference improve or
degrade?). Both the registered and the deviated analysis are reported; the
registered one is never replaced.

Two entries so far. Neither touches a hypothesis, a stimulus, an item, the answer
key, the primary test or the SESOI.

---

## Deviation 1 — completion budget raised for one reader's empty-content cells

*Logged 2026-10-06, during the machine arm. Machine arm only.*

- **What.** Under the registered setting (`max_tokens = 40`) 47 of the 48
  item-administrations of one reader model (`qwen/qwen3.5-9b`) returned **empty
  content** — no answer text at all, so no answer could be parsed. Those 47 cells
  were re-run with `max_tokens = 1024`. For that model the re-run supersedes the
  failed attempt; every record carries `setting_max_tokens`, so both passes stay
  auditable in `results/machine_raw.jsonl`.
- **Why.** An empty completion is a harness outcome, not an answer: the model
  almost certainly consumed the whole budget before emitting content (it is a
  reasoning-style model, 28 258 completion tokens across 48 calls at the higher
  setting). Raising the cap lets the model answer, which is what the arm is
  supposed to measure. This is a principled infrastructure fix, not a
  results-driven one — it was applied uniformly to all of that model's failed
  cells before any accuracy was computed.
- **Severity.** Unchanged. The hypothesis, the items, the primary test and the
  SESOI are untouched; more parsable answers for one reader cannot reduce the
  test's ability to falsify H1 in the human arm.
- **Validity.** Improved. Without the fix, that reader's accuracy would have
  measured the token cap rather than the model, and the compliance figure would
  have described the harness rather than the reader.
- **Both reported.** Registered setting: 576 calls, 529 parsed (91.8%).
  Deviation pass: 47 calls, 46 parsed. One cell of that model returned empty
  content even at 1024 tokens; it is recorded as an error and excluded, and it is
  the single remaining error in the final analysis (575 parsed of 576 cells,
  99.8%). `results/RESULTS_registered_max40.md` is the registered-setting run.

---

## Erratum 1 — SESOI constant in the analysis code (not a design change)

*Logged 2026-10-06, during the machine arm. No human data existed.*

- **What.** `analysis_core.SESOI_PP` was initialised to `0.05` (5 pp) while
  `PREREGISTRATION.md` §7 fixes the equivalence margin at **10 pp**. The first
  machine-arm run therefore reported "TOST vs ±5 pp". The constant is now `0.10`
  and the corrected run reports "TOST vs ±10 pp".
- **Why.** A coding slip, caught by comparing the report against the registered
  document — exactly the failure the erratum log exists for.
- **Severity.** Unchanged for the decision rule (the pre-registered rule is the
  one now applied). The earlier, wrongly-specified equivalence test is reported
  alongside rather than deleted.
- **Validity.** Improved: the reported equivalence test now matches the
  registered margin.
- **Both reported.** `results/RESULTS_registered_max40.md` is the pre-fix run
  (registered `max_tokens`, but the 5 pp margin by mistake);
  `results/RESULTS.md` is the final run (10 pp margin, deviation pass included).

---

## Nothing else deviated

The human arm has not been run, so no participant-facing procedure has been
modified. Design B, the target N = 36, the exclusions, the primary test, the
secondary family and the decision rule are exactly as registered.
