# Deviation and erratum log — finding-5 comprehension test

The pre-registration (`PREREGISTRATION.md` §9) commits to documenting every
departure from the registered plan with four elements: **what** changed, **why**,
the effect on **severity** (does the test become more or less able to falsify the
hypothesis?), and the effect on **validity** (does the inference improve or
degrade?). Both the registered and the deviated analysis are reported; the
registered one is never replaced.

Three entries so far: one pre-collection revision of the stimuli and presentation,
one deviation in how the machine arm was run, and one erratum in the analysis code.
A fourth (Erratum 2) records bookkeeping corrections to the v2 text and one open
code condition; none of the four touches a hypothesis, the decision rule, the
SESOI, the exclusions or the target N. The revision does change the stimulus set,
and says so explicitly.

---

## Revision 1 — v1 → v2 of the stimuli and presentation (pre-collection)

*Logged 2026-10-06, before any data existed, human or machine.*

- **What.** Three changes: (1) each obligation gained a third, harder item (date
  arithmetic, conditional application, or two-fact combination), taking the item set
  from 12 to 18; (2) the two registers of an obligation are no longer presented
  consecutively — they are placed in different halves of the session, at least four
  screens apart; (3) per-trial records gained `position`, `pair_pos` and `skipped`,
  and the analysis gained a locked exposure-robustness check (§6.4 of the
  pre-registration).
- **Why.** The instrument was tested by hand and the machine arm piloted, both
  before any human data. Two defects surfaced. Back-to-back presentation made the
  manipulation visible and let the second version be answered from memory of the
  first; and the item set sat at ceiling (9 of 12 machine readers scored 100% in
  both registers; every capable reader did), leaving no variance for an effect to
  appear in. Both are validity problems, not result-dependent adjustments: no
  outcome was known when the change was made.
- **Severity.** Increased. Eighteen items instead of twelve, with three of them
  reasoning items, give the primary test more independent paired units (18 vs 12)
  and a wider spread of difficulty; the power simulation puts the design at 0.92
  power at the SESOI for N = 24 and 0.98 at N = 36 (v1: 0.75 and 0.83).
- **Validity.** Improved on both counts: the register contrast is less discoverable
  and less answerable from memory, and the items now discriminate rather than
  ceiling. The residual threat — every participant still reads each obligation twice
  — is declared in §10.7 and bounded by the locked exposure check.
- **Both reported.** The machine arm was piloted on v1. The register texts themselves
  are unchanged between v1 and v2 (only items and metadata changed), so the v1
  observations for items Q1–Q2 remain valid measurements of the same stimuli and are
  kept; the v2 collection adds the new Q3 cells. `results/RESULTS.md` says which
  cells came from which pass.

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

## Erratum 2 — v1 item counts left in the v2 pre-registration text

*Logged 2026-10-27, after registration and after the v2 machine run; no human data exists.*

- **What.** Four places in `PREREGISTRATION.md` still quoted the v1 item counts after
  Revision 1 moved the design to three items per obligation: the §1 design row
  ("12 four-option items"), the §2 H1 statistical statement ("12 item-level
  differences … 12 paired differences"), §3 arm M ("× 2 items = 48 … 48R
  observations") and §3 arm H ("12 documents, 24 items"), plus the §6 primary test
  ("all 2^12 sign patterns"). They are corrected to 18 items, 72 item-administrations
  per model, 36 questions per participant and 2^18 sign patterns. Nothing else in
  the file changed.
- **Why.** Bookkeeping, not design: v2 has 3 items per obligation, 6 obligations,
  18 items; the analysis code, `stimuli.json` (`items_per_document: 3`), the
  simulation (18 paired units) and `README.md` all already used those counts. The
  registration text was simply inconsistent with the registration it describes.
- **Severity.** Unchanged. No hypothesis, decision rule, SESOI, exclusion or target N
  is touched, and no human data exists, so no reported result depends on the fix.
- **Validity.** Improved as a record: a pre-registration that contradicts itself on
  the item count is a free reviewer objection.
- **Open condition, stated rather than hidden.** `analysis_core.signflip_test` has
  `max_exact = 16`, so at 18 paired differences the code samples 100,000 sign
  patterns instead of enumerating all 2^18. The registered wording now promises
  enumeration. The condition must be resolved **before any collection** — either
  raise `max_exact` to 18 (2^18 = 262,144 patterns, cheap) or amend §6 to state the
  seeded Monte Carlo estimator explicitly. It is recorded here, not silently fixed,
  because it is a change to registered analysis code and the human arm is paused.
- **Both reported.** The registered text as committed at `7f6b068` (through the v2
  revision) is recoverable from git; this entry records every change made after it.

---

## Nothing else deviated

The human arm has not been run, so no participant-facing procedure has been
modified. Design B, the target N = 36, the exclusions, the primary test, the
secondary family and the decision rule are exactly as registered.
