# Participant exports — drop the returned JSON files here

One file per participant, exactly as it was downloaded (`comprehension_<id>.json`).
Do not rename them: the filename carries the random participant id, and the scoring
script reads the id from inside the file anyway, so renaming only makes the trail
harder to follow.

## Quick check when a file arrives

- it is a `.json` file, not a screenshot or a pasted message;
- it parses as JSON and has a `trials` list of 24 entries;
- its `duration_min` looks plausible (the pre-registration excludes sessions under
  8 minutes or over 60).

`score_human.py` re-checks all of this and reports anything it excludes, so a rough
check is enough.

## Keep a manifest

Record each session in `MANIFEST.csv` as it arrives. Columns: participant id, file
name, date returned, language, self-reported duration, usable yes/no, exclusion
reason, notes. This is what makes an exclusion auditable later — the pre-registration
promises exclusions are counted and reported.

## Score when collection closes

```bash
python3 experiment/score_human.py --dir experiment/exports/ --min-n 20
```

Writes `experiment/results/human_tidy.csv`, `human_summary.json` and
`HUMAN_RESULTS.md` with the pre-registered verdict. With 36 participants the arm is
confirmatory at the registered N; with 20-35 it is still confirmatory but less
powerful; below 20 the script reports descriptively instead. "FALSIFIED" means the
data exclude a plain-language advantage of 10 pp or more — not that formal beat
plain.

Run it as often as you like while collecting: nothing is written to these raw files.

## Publication

The exports contain a random id and item responses only — no names, no free text,
nothing identifying. Publishing them is good practice (data access is part of the
DA-RT transparency the pre-registration situates itself in), so committing them
after collection is recommended. If you promised participants that the files would
stay private, add `experiment/exports/*.json` to `.gitignore` instead and commit only
the tidy CSV and the report.
