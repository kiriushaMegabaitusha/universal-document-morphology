#!/usr/bin/env python3
"""Merge independent rater CSVs into the scores.csv consumed by evaluate_matrix.py.

Contract (fixed when reviewers were dispatched):
  raw/review_R0{1..4}.csv, header:
  idea_id,information_gain,information_gain_low,information_gain_high,
  feasibility,feasibility_low,feasibility_high,
  rigor_disconfirmability,rigor_disconfirmability_low,rigor_disconfirmability_high,
  synergy_relevance,synergy_relevance_low,synergy_relevance_high,
  coverage_breadth,coverage_breadth_low,coverage_breadth_high,
  qualitative_review,uncertainties,evidence_status,ethics_status

Aggregation (declared in CRITERIA.md, decided before any score existed):
  central per rater -> median (even count: lower-middle of the two, integer scale)
  low  = min over raters' lows      high = max over raters' highs
  spread flag = (max central - min central) >= 2 on any criterion
  ethics_status = review-required if ANY rater says review-required, else strictest present
  evidence_status = taken from raw/evidence_E0*.md statuses when provided via
                    --evidence map file (idea_id<TAB>status), else not-checked

Outputs: scores.csv (+ scores_disagreement.csv with per-rater centrals preserved).
Exit non-zero if any expected reviewer file/row/ID is missing.
"""
from __future__ import annotations

import csv
import glob
import statistics
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
RAW = BASE / "raw"

CRITERIA = ["information_gain", "feasibility", "rigor_disconfirmability",
            "synergy_relevance", "coverage_breadth"]
EXPECTED_IDS = [
    "P01-1", "P02-1", "P02-2", "P02-4", "P02-6", "P03-1", "P04-1", "P04-3",
    "P05-2", "P05-6", "P06-1", "P06-2", "P06-3", "P06-4", "P06-5", "P07-1",
    "P07-3", "P07-5", "P08-1", "P08-2", "P08-3", "P08-5", "P08-6",
]
REQUIRED_HEADER = ["idea_id"]
for c in CRITERIA:
    REQUIRED_HEADER += [c, f"{c}_low", f"{c}_high"]
REQUIRED_HEADER += ["qualitative_review", "uncertainties", "evidence_status",
                    "ethics_status"]

ETHICS_ORDER = ["not-applicable", "not-assessed", "review-required",
                "redesign-required", "stop"]


def load_ratings() -> dict[str, list[dict[str, str]]]:
    files = sorted(glob.glob(str(RAW / "review_R0*.csv")))
    if len(files) < 3:
        sys.exit(f"ERROR: expected >=3 rater CSVs, found {len(files)}: {files}")
    by_idea: dict[str, list[dict[str, str]]] = {}
    for f in files:
        with open(f, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames != REQUIRED_HEADER:
                sys.exit(f"ERROR: {f} header mismatch:\n  got      {reader.fieldnames}\n  expected {REQUIRED_HEADER}")
            rows = list(reader)
        ids = [r["idea_id"] for r in rows]
        missing = set(EXPECTED_IDS) - set(ids)
        extra = set(ids) - set(EXPECTED_IDS)
        if missing or extra or len(ids) != len(EXPECTED_IDS):
            sys.exit(f"ERROR: {f} id set wrong (missing={sorted(missing)} extra={sorted(extra)} n={len(ids)})")
        for r in rows:
            for c in CRITERIA:
                s, lo, hi = int(r[c]), int(r[f"{c}_low"]), int(r[f"{c}_high"])
                if not (lo <= s <= hi):
                    sys.exit(f"ERROR: {f} {r['idea_id']}.{c}: low {lo} > score {s} or score > high {hi}")
                if not (1 <= s <= 5):
                    sys.exit(f"ERROR: {f} {r['idea_id']}.{c} out of 1-5: {s}")
            r["__rater__"] = Path(f).stem
            by_idea.setdefault(r["idea_id"], []).append(r)
    return by_idea


def main() -> int:
    by_idea = load_ratings()

    ev_path = BASE / "evidence_status.tsv"
    evidence: dict[str, str] = {}
    if ev_path.exists():
        for line in ev_path.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#"):
                idea, status = line.split("\t")[:2]
                evidence[idea.strip()] = status.strip()

    scores_rows, raw_rows = [], []
    for idea in EXPECTED_IDS:
        raters = by_idea[idea]
        row: dict[str, str] = {"idea_id": idea}
        spreads = []
        for c in CRITERIA:
            centrals = [int(r[c]) for r in raters]
            lows = [int(r[f"{c}_low"]) for r in raters]
            highs = [int(r[f"{c}_high"]) for r in raters]
            central = int(statistics.median(centrals))
            row[c] = str(central)
            row[f"{c}_low"] = str(min(lows))
            row[f"{c}_high"] = str(max(highs))
            spreads.append(max(centrals) - min(centrals))
            raw_rows.append({"idea_id": idea, "rater": raters[0]["__rater__"] + "+",
                             "criterion": c,
                             "central": ";".join(f"{r['__rater__']}={r[c]}" for r in raters),
                             "low": str(lows), "high": str(highs)})
        max_spread = max(spreads)
        reasons = " | ".join(r["qualitative_review"].strip() for r in raters if r["qualitative_review"].strip())
        unc = " | ".join(dict.fromkeys(r["uncertainties"].strip() for r in raters if r["uncertainties"].strip()))
        note = f"raters={len(raters)}; max_central_spread={max_spread}"
        row["qualitative_review"] = (reasons[:900] + " …") if len(reasons) > 900 else reasons
        row["uncertainties"] = f"[{note}] " + ((unc[:600] + " …") if len(unc) > 600 else unc)
        row["evidence_status"] = evidence.get(idea, "not-checked")
        ethics = [r["ethics_status"].strip() for r in raters]
        chosen = "not-assessed"
        for cand in reversed(ETHICS_ORDER):  # strictest wins
            if cand in ethics:
                chosen = cand
                break
        row["ethics_status"] = chosen
        scores_rows.append(row)

    out = BASE / "scores.csv"
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=REQUIRED_HEADER)
        w.writeheader()
        w.writerows(scores_rows)

    raw_out = BASE / "scores_raw_by_rater.csv"
    with open(raw_out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["idea_id", "rater", "criterion",
                                           "central", "low", "high"])
        w.writeheader()
        w.writerows(raw_rows)

    print(f"merged {len(scores_rows)} ideas from {len(load_ratings()[EXPECTED_IDS[0]])} raters -> {out}")
    print(f"raw per-rater records -> {raw_out}")
    print(f"evidence statuses mapped: {len(evidence)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
