# Deviations — P06-2 exact-null audit

House rule (`experiment/PREREGISTRATION.md` §9): every deviation from
`PREREGISTRATION.md` §3–§7 is logged with four elements — what changed, why,
effect on the severity of the test, effect on validity — and both the registered
and the deviated analysis are reported side by side; the registered one is never
replaced.

**Pre-registration activity (not deviations):**

- The analysis code was syntax-checked and exercised with `--self-test` on a
  synthetic 25 × 14 frame (seeded, no registered data read, no statistic computed
  on the real matrix). This mirrors the house pattern (`experiment/simulate_data.py`
  ran on simulated data before collection) and is recorded here for completeness.
- Two pre-registration edits were made to the session draft before this file was
  registered (both recorded in the header of `PREREGISTRATION.md`): the status
  header, and the §5.2 block-source widening to the README §Coverage grouping.

**Deviations from the registered analysis: none so far.** The registered analysis
runs once after registration; any departure will be appended here before the
deviated result is examined.