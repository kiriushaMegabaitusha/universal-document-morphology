#!/usr/bin/env python3
"""Write the pre-registered results for the machine arm.

Reads results/machine_raw.jsonl (produced by machine_arm.py) and emits
  results/machine_summary.json   every pre-registered number, machine-readable
  results/RESULTS.md             the same, readable, with the decision mapping

The machine arm is EXPLORATORY (PREREGISTRATION.md §7: power 0.15 at a 10 pp gap
with 4 readers, ~0.4 with 12). This script therefore reports estimates with
confidence intervals and compliance/cost descriptives, and explicitly does not
issue a confirmatory verdict.

Run:  python3 experiment/analyze.py
"""
import json
import os
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analysis_core as A  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
RAW = os.path.join(RESULTS, "machine_raw.jsonl")


def load_records():
    recs = []
    if not os.path.exists(RAW):
        return recs
    for line in open(RAW, encoding="utf-8"):
        line = line.strip()
        if line:
            recs.append(json.loads(line))
    return recs


def cost_table(recs):
    meta_path = os.path.join(RESULTS, "machine_models.json")
    meta = json.load(open(meta_path, encoding="utf-8")) if os.path.exists(meta_path) else {}
    agg = defaultdict(lambda: {"prompt": 0, "completion": 0, "calls": 0})
    for r in recs:
        a = agg[r["model"]]
        a["calls"] += 1
        a["prompt"] += r.get("prompt_tokens") or 0
        a["completion"] += r.get("completion_tokens") or 0
    rows, total = [], 0.0
    for m, a in sorted(agg.items()):
        p = meta.get(m, {})
        pin, pout = p.get("prompt_usd_per_mtok"), p.get("completion_usd_per_mtok")
        usd = None
        if pin is not None and pout is not None:
            usd = a["prompt"] / 1e6 * pin + a["completion"] / 1e6 * pout
            total += usd
        rows.append({"model": m, "name": p.get("name", ""), "calls": a["calls"],
                     "prompt_tokens": a["prompt"], "completion_tokens": a["completion"],
                     "est_usd": usd})
    return rows, total


def main():
    recs_all = load_records()
    if not recs_all:
        print("no data at %s - run experiment/machine_arm.py first" % RAW)
        return 1
    # one record per cell: the last win (a deviation pass supersedes a failed cell)
    by_cell = {}
    for r in recs_all:
        by_cell[(r["model"], r["document"], r["item"], r["lang"], r["register"])] = r
    recs = list(by_cell.values())
    by_setting = defaultdict(lambda: {"calls": 0, "parsed": 0, "errors": 0})
    for r in recs_all:
        s = by_setting[r.get("setting_max_tokens", 40)]
        s["calls"] += 1
        s["errors"] += 1 if r.get("error") else 0
        s["parsed"] += 1 if (r.get("correct") is not None) else 0

    obs = A.load_machine(RAW)
    # guard against a cell appearing twice (should not happen; kept cheap)
    seen, dedup = set(), []
    for o in obs:
        k = (o["reader"], o["item"], o["lang"], o["register"], o["document"])
        if k in seen:
            dedup = [x for x in dedup if (x["reader"], x["item"], x["lang"], x["register"], x["document"]) != k]
        seen.add(k)
        dedup.append(o)
    obs = dedup
    n_raw = len(recs)
    n_parsed = len(obs)
    compliance = n_parsed / n_raw if n_raw else float("nan")
    strict = sum(1 for r in recs if r.get("parse_ok"))
    errors = sum(1 for r in recs if r.get("error"))

    rep = A.arm_report(obs, "machine (exploratory)")
    per_model = {}
    for m in sorted({o["reader"] for o in obs}):
        sub = [o for o in obs if o["reader"] == m]
        _, d = A.item_differences(sub)
        fe = A.logit_fe(sub)
        per_model[m] = {
            "n": len(sub), "accuracy": sum(o["correct"] for o in sub) / len(sub),
            "mean_item_diff": float(d.mean()) if len(d) else None,
            "logit_beta": (fe["coef"]["register_plain"]["beta"] if fe else None),
            "logit_ame_pp": (fe["ame_pp"] if fe else None),
        }
    costs, total_usd = cost_table(recs)

    summary = {
        "arm": "machine",
        "status": "exploratory (no confirmatory claim)",
        "n_calls": n_raw, "n_parsed": n_parsed, "n_errors": errors,
        "strict_json_compliance": strict / n_raw if n_raw else None,
        "parse_compliance": compliance,
        "compliance_by_setting": {str(k): v for k, v in sorted(by_setting.items())},
        "report": rep,
        "per_model": per_model,
        "cost": {"per_model": costs, "estimated_total_usd": round(total_usd, 4)},
    }
    with open(os.path.join(RESULTS, "machine_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    # ---- readable report ---------------------------------------------------
    acc = rep["accuracy_by_register"]
    L = []
    L.append("# Results — machine arm (exploratory)")
    L.append("")
    L.append("**Reader models:** %d · **item-administrations:** %d parsed of %d calls "
             "(compliance %.1f%%, strict JSON %.1f%%) · **errors:** %d"
             % (rep["n_readers"], n_parsed, n_raw, 100 * compliance,
                100 * (strict / n_raw if n_raw else 0), errors))
    L.append("")
    L.append("**Status: exploratory.** Per the pre-registration (§7) this arm is underpowered "
             "for the effect sizes of interest and issues no confirmatory verdict; it "
             "measures machine legibility, not comprehension.")
    L.append("")
    L.append("**Compliance by completion budget** (the registered setting is `max_tokens=40`; "
             "deviation #1 re-runs one model's empty-content cells at 1024):")
    L.append("")
    for st, s in sorted(by_setting.items()):
        L.append("- `max_tokens=%d`: %d calls, %d parsed, %d errors" % (st, s["calls"], s["parsed"], s["errors"]))
    L.append("")
    L.append("## Pre-registered quantities")
    L.append("")
    L.append("| quantity | value |")
    L.append("|---|---|")
    for k, (c, n, p) in sorted(acc.items()):
        L.append("| accuracy, %s | %.3f (%d/%d) |" % (k, p, c, n))
    perm = rep["permutation"]
    L.append("| primary test: mean item difference (plain − formal) | %+.3f |" % perm["mean"])
    L.append("| primary test: exact sign-flip p (two-sided) | %.4f (%s) |"
             % (perm["p"], "exact" if perm["exact"] else "sampled"))
    L.append("| 95%% bootstrap CI on the mean item difference | [%+.3f, %+.3f] |"
             % (rep["bootstrap_ci"][0], rep["bootstrap_ci"][1]))
    fe = rep["logit_fe"]
    if fe:
        c = fe["coef"]["register_plain"]
        L.append("| logistic FE: beta (plain) | %+.3f (OR %.2f, Wald p %.4f) |" % (c["beta"], c["or"], c["p"]))
        L.append("| logistic FE: average marginal effect | %+.1f pp |" % (fe["ame_pp"] * 100))
    eq = rep["equivalence"]
    L.append("| TOST vs ±%.0f pp (SESOI) | %s (p_lo=%.4f, p_hi=%.4f) |"
             % (A.SESOI_PP * 100, "equivalent" if eq["equivalent"] else "not equivalent",
                eq["p_lower"], eq["p_upper"]))
    L.append("| reader-cluster bootstrap 95%% CI on beta | [%+.3f, %+.3f] |"
             % rep["reader_cluster_boot_beta"])
    L.append("")
    L.append("## Accuracy by language and register")
    L.append("")
    L.append("| cell | accuracy | n |")
    L.append("|---|---|---|")
    for k, (c, n, p) in sorted(rep["accuracy_by_lang_register"].items()):
        L.append("| %s | %.3f | %d |" % (k, p, n))
    L.append("")
    L.append("## Accuracy by item type and register")
    L.append("")
    L.append("| cell | accuracy | n |")
    L.append("|---|---|---|")
    for k, (c, n, p) in sorted(rep["accuracy_by_kind_register"].items()):
        L.append("| %s | %.3f | %d |" % (k, p, n))
    L.append("")
    L.append("## Secondary (pre-specified, machine arm = exploratory)")
    L.append("")
    for (name, p), (_, thr, rej) in zip(rep["secondary_pvalues"], rep["secondary_bh"]):
        L.append("- %s: p = %.4f, BH threshold %.4f, reject = %s" % (name, p, thr, rej))
    L.append("")
    L.append("## Per model")
    L.append("")
    L.append("| model | n | accuracy | item diff (pp) | logistic AME (pp) |")
    L.append("|---|---|---|---|---|")
    for m, s in sorted(per_model.items(), key=lambda kv: -(kv[1]["accuracy"] or 0)):
        L.append("| %s | %d | %.3f | %s | %s |"
                 % (m, s["n"], s["accuracy"],
                    "%+.1f" % (100 * s["mean_item_diff"]) if s["mean_item_diff"] is not None else "n/a",
                    "%+.1f" % (100 * s["logit_ame_pp"]) if s["logit_ame_pp"] is not None else "n/a"))
    L.append("")
    L.append("## Cost")
    L.append("")
    L.append("| model | calls | prompt tok | completion tok | est. USD |")
    L.append("|---|---|---|---|---|")
    for r in costs:
        L.append("| %s | %d | %d | %d | %s |"
                 % (r["model"], r["calls"], r["prompt_tokens"], r["completion_tokens"],
                    ("%.4f" % r["est_usd"]) if r["est_usd"] is not None else "n/a"))
    L.append("| **total** | | | | **%.4f** |" % total_usd)
    L.append("")
    L.append("## Item-level differences (plain − formal, proportion correct)")
    L.append("")
    L.append("| item | difference |")
    L.append("|---|---|")
    for it, d in zip(rep["items"], rep["item_diffs"]):
        L.append("| %s | %+.3f |" % (it, d))
    L.append("")
    with open(os.path.join(RESULTS, "RESULTS.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L))

    print("\n".join(L[:40]))
    print("\n... full report: %s" % os.path.join("experiment", "results", "RESULTS.md"))
    print("summary JSON : %s" % os.path.join("experiment", "results", "machine_summary.json"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
