# B3 — lineage-restricted re-derivation

**Status: registered, NOT yet run.** No test statistic has been computed on the real
matrix, and no results file exists. The registration is the commit that adds this
directory together with the pre-registration; the run happens once after it.

The registration text is `PREREGISTRATION.md` in this directory. The literature
check is `brainstorm/raw/evidence_B3.md`.

## Files

| file | what |
|---|---|
| `lineage_audit.py` | the registered analysis: deterministic lineage counts, clustering tests, identification bounds, compelled-requisites re-derivation, spec curve, estimation, exploratory holdout |
| `lineage_blocks.csv` | the frozen lineage coding — 25 systems × {narrow, base, broad}, one citation per documented edge |
| `mandatory_only.csv` | frozen derived input: cell = 1 iff ≥1 **mandatory** requisite maps to that slot (no statistic) |
| `results.json` | **absent by design.** Written only by the registered one-shot run |

## Modes

```bash
python3 lineage/lineage_audit.py --self-test      # synthetic frame only; never opens the real matrix
python3 lineage/lineage_audit.py --freeze-inputs  # regenerate mandatory_only.csv from requisites.csv; computes nothing
python3 lineage/lineage_audit.py                  # the registered run — only after registration
```

`--self-test` is the gate before registration; it covers block algebra,
deterministic counts, clustering on strong vs random fixtures, Clopper–Pearson,
the fork machinery, p-floor behaviour on singleton blocks, the citation gate, the
mandatory-matrix rule, and the exploratory holdout.

## Rules this directory inherits

- Inputs are pinned by SHA-256 in the script; a mismatch stops the run.
- The lineage table is frozen before any statistic, and a `documented` row without a
  citation fails validation.
- The registered run happens once. Deviations go in a `DEVIATIONS.md` created at
  registration, with what/why/severity/validity, and both analyses are reported.
- `mandatory_only.csv` is regenerated and asserted equal to the committed file
  before the run; it is never hand-edited.

## Known state of the frozen inputs

- Two systems have no mandatory cell: **HN** (non-documentary record system) and
  **PE** (thin primary coding). They are kept, not dropped; their emptiness is part
  of the compelled-requisites finding.
- Base has **18** lineage blocks (effective n), narrow 19, broad 12. Only four
  clusters are documented in the atlas; everything else is a singleton in base.
