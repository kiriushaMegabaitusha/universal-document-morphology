# Deviations — B3 lineage audit

House rule (`experiment/PREREGISTRATION.md` §9): every departure from
`PREREGISTRATION.md` §3–§7 is logged with four elements — what changed, why, the
effect on **severity** (does the test become more or less able to falsify the
hypothesis?), and the effect on **validity** — and both the registered and the
deviated analysis are reported side by side; the registered one is never replaced.

**Pre-registration activity (not deviations):**

- Two revisions were made *before* registration and are recorded in the header of
  `PREREGISTRATION.md`: Revision 1 (after the bounded literature check) and
  Revision 2 (at code time).
- `lineage_audit.py --self-test` ran on a synthetic frame only. It never opened the
  real matrix, and it caught two real bugs (an inverted Clopper–Pearson lower
  bound and mis-flattened placement tuples) before registration.
- `lineage_audit.py --freeze-inputs` wrote `mandatory_only.csv` from
  `requisites.csv`. It computes no statistic; it is a frozen derived input.

**Deviations from the registered analysis: none yet.** The registered run has not
been executed at the time this file was committed.
