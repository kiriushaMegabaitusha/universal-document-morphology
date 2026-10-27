#!/usr/bin/env python3
"""Merge the B1 wave-2 rater JSONs into the scores the protocol declares.

Input : brainstorm/wave2/raw/review_R01.json .. R04.json
Output: brainstorm/wave2/scores.csv, scores_raw_by_rater.csv, matrix.json

Aggregation is fixed in PROTOCOL.md before any score existed:
  central = median over raters (even count -> lower-middle, integer scale)
  low = min of raters' lows, high = max of raters' highs
  score = 100 * sum(w*(c-1)) / (4*sum(w))       [verified against wave 1]
  sensitivity = one-at-a-time weight perturbation +/-10%, rank range
  decision = null: the matrix is a decision aid, not a selector.
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
RAW = BASE / "raw"

CRITERIA = [
    ("information_gain", 3),
    ("feasibility", 3),
    ("rigor_disconfirmability", 2),
    ("synergy_relevance", 2),
    ("coverage_breadth", 1),
]
IDS = ["P09-1", "P09-3", "P10-1", "P10-2", "P10-3", "P11-1", "P11-2"]
RATERS = ["R01", "R02", "R03", "R04"]
ETHICS_ORDER = ["not-applicable", "assessed", "review-required"]
HEADER = ["idea_id"]
for name, _ in CRITERIA:
    HEADER += [name, f"{name}_low", f"{name}_high"]
HEADER += ["qualitative_review", "uncertainties", "evidence_status", "ethics_status"]


def weighted(central: dict[str, int], mult: dict[str, float] | None = None) -> float:
    num = 0.0
    den = 0.0
    for name, w in CRITERIA:
        ww = w * (mult or {}).get(name, 1.0)
        num += ww * (central[name] - 1)
        den += ww
    return 100.0 * num / (4.0 * den)


def rank_of(scores: dict[str, float]) -> dict[str, int]:
    order = sorted(scores, key=lambda k: (-scores[k], k))
    return {k: i + 1 for i, k in enumerate(order)}


def main() -> int:
    ratings: dict[str, list[dict]] = {i: [] for i in IDS}
    for r in RATERS:
        path = RAW / f"review_{r}.json"
        if not path.exists():
            sys.exit(f"missing rater file: {path}")
        data = json.loads(path.read_text(encoding="utf-8"))
        seen = set()
        for row in data:
            iid = row.get("idea_id")
            if iid not in ratings:
                sys.exit(f"{r}: unexpected idea_id {iid!r}")
            if iid in seen:
                sys.exit(f"{r}: duplicate idea_id {iid}")
            seen.add(iid)
            for name, _ in CRITERIA:
                cell = row.get(name)
                if not cell:
                    sys.exit(f"{r} {iid}: missing criterion {name}")
                s, lo, hi = cell["score"], cell["low"], cell["high"]
                for v in (s, lo, hi):
                    if not isinstance(v, int) or not 1 <= v <= 5:
                        sys.exit(f"{r} {iid}.{name}: value {v!r} outside 1..5 integer")
                if not lo <= s <= hi:
                    sys.exit(f"{r} {iid}.{name}: low {lo} <= score {s} <= high {hi} violated")
            row["_rater"] = r
            ratings[iid].append(row)
        missing = set(IDS) - seen
        if missing:
            sys.exit(f"{r}: missing ideas {sorted(missing)}")

    central_scores: dict[str, dict[str, int]] = {}
    rows, raw_rows = [], []
    for iid in IDS:
        rs = ratings[iid]
        if len(rs) != len(RATERS):
            sys.exit(f"{iid}: {len(rs)} ratings, expected {len(RATERS)}")
        row = {"idea_id": iid}
        central = {}
        for name, _ in CRITERIA:
            cs = sorted(r[name]["score"] for r in rs)
            central[name] = cs[(len(cs) - 1) // 2]           # lower-middle
            row[name] = central[name]
            row[f"{name}_low"] = min(r[name]["low"] for r in rs)
            row[f"{name}_high"] = max(r[name]["high"] for r in rs)
            for r in rs:
                raw_rows.append({"idea_id": iid, "rater": r["_rater"], "criterion": name,
                                 "score": r[name]["score"], "low": r[name]["low"],
                                 "high": r[name]["high"]})
        spread = max(max(r[n]["score"] for r in rs) - min(r[n]["score"] for r in rs)
                     for n, _ in CRITERIA)
        row["qualitative_review"] = " | ".join(
            f"[{r['_rater']}] {r.get('qualitative_review','')}".strip() for r in rs)
        row["uncertainties"] = " | ".join(
            f"[{r['_rater']}] {r.get('uncertainties','')}".strip() for r in rs)
        row["evidence_status"] = "not-checked"
        eth = max((r.get("ethics_status", "not-applicable") for r in rs),
                  key=lambda e: ETHICS_ORDER.index(e) if e in ETHICS_ORDER else 0)
        row["ethics_status"] = eth
        row["_spread"] = spread
        rows.append(row)
        central_scores[iid] = central

    base = {i: weighted(central_scores[i]) for i in IDS}
    base_rank = rank_of(base)
    sens: dict[str, dict[str, float]] = {}
    for name, _ in CRITERIA:
        ranks = []
        for factor in (0.9, 1.1):
            sc = {i: weighted(central_scores[i], {name: factor}) for i in IDS}
            ranks.append(rank_of(sc))
        sens[name] = {i: (min(ranks[0][i], ranks[1][i]), max(ranks[0][i], ranks[1][i]))
                      for i in IDS}

    rows.sort(key=lambda r: (-base[r["idea_id"]], r["idea_id"]))
    with open(BASE / "scores.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=HEADER, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    with open(BASE / "scores_raw_by_rater.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["idea_id", "rater", "criterion", "score", "low", "high"])
        w.writeheader()
        w.writerows(raw_rows)

    matrix = {
        "schema_version": "2.0",
        "wave": "B1 post-check rating wave",
        "date": "2026-10-28",
        "method": {"criteria": [{"name": n, "weight": w} for n, w in CRITERIA],
                   "aggregation": "median central (lower-middle), min low, max high",
                   "score": "100 * sum(w*(c-1)) / (4*sum(w))"},
        "raters": len(RATERS),
        "results": [
            {"idea_id": r["idea_id"], "score": round(base[r["idea_id"]], 1),
             "rank": base_rank[r["idea_id"]],
             "central": central_scores[r["idea_id"]],
             "low": {n: r[f"{n}_low"] for n, _ in CRITERIA},
             "high": {n: r[f"{n}_high"] for n, _ in CRITERIA},
             "rater_spread": r["_spread"],
             "rank_range": {n: list(v[r["idea_id"]]) for n, v in sens.items()}}
            for r in rows
        ],
        "decision": None,
        "limitations": [
            "Four AI raters, no human expertise: consensus is not evidence.",
            "Seven items, two resolved ideas excluded.",
            "Scores are decision aids; the owner selects, not the matrix.",
            "Sensitivity is one-weight-at-a-time and does not cover model-form uncertainty.",
        ],
    }
    (BASE / "matrix.json").write_text(json.dumps(matrix, indent=1) + "\n", encoding="utf-8")

    print(f"merged {len(IDS)} ideas from {len(RATERS)} raters")
    print(f"{'idea':7} {'score':>6} {'rank':>4}  spread  rank-range-under-weight-perturbation")
    for r in rows:
        rr = matrix["results"][[x["idea_id"] for x in matrix["results"]].index(r["idea_id"])]
        lo = min(v[0] for v in rr["rank_range"].values())
        hi = max(v[1] for v in rr["rank_range"].values())
        print(f"{r['idea_id']:7} {base[r['idea_id']]:6.1f} {base_rank[r['idea_id']]:4d}  "
              f"{r['_spread']:^6}  {lo}-{hi}")
    print("\nwrote scores.csv, scores_raw_by_rater.csv, matrix.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
