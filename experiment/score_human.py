#!/usr/bin/env python3
"""Score participant exports from human_survey.html and run the pre-registered analysis.

Trust nothing from the client: the correctness of every answer is recomputed here
from stimuli.json, and the pre-specified exclusions (PREREGISTRATION.md §4) are
applied here, not in the browser.

Usage
  python3 experiment/score_human.py exports/*.json          # participant files
  python3 experiment/score_human.py --dir exports/          # whole directory
  python3 experiment/score_human.py --dir exports/ --min-n 20
  python3 experiment/score_human.py --fixture FILE          # dev harness: see below

--fixture marks the input as the machine-generated test record from
test_survey_headless.py. Outputs are then written with TEST_*_NOT_DATA names and the
verdict is labelled FIXTURE, so a test run can never be mistaken for participant data.

Writes
  results/human_tidy.csv      one row per item-administration
  results/HUMAN_RESULTS.md    the pre-registered report (confirmatory at N >= min,
                              explicitly exploratory below it)
"""
import argparse
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analysis_core as A  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
MIN_DURATION_MIN = 8
MAX_DURATION_MIN = 60


def key_table():
    stim = json.load(open(os.path.join(HERE, "stimuli.json"), encoding="utf-8"))
    keys, kinds = {}, {}
    for d in stim["documents"]:
        for it in d["items"]:
            keys[it["id"]] = it["answer"]
            kinds[it["id"]] = it["kind"]
    return keys, kinds


def read_export(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate(part, keys):
    """Return (ok, reason). Structural problems are fatal to the session."""
    if not isinstance(part, dict):
        return False, "not a JSON object"
    for field in ("participant", "trials"):
        if field not in part:
            return False, "missing %s" % field
    if not isinstance(part["trials"], list) or not part["trials"]:
        return False, "no trials"
    for tr in part["trials"]:
        for field in ("item", "document", "register", "lang", "response"):
            if field not in tr:
                return False, "trial missing %s" % field
        if tr["item"] not in keys:
            return False, "unknown item %r" % tr["item"]
    return True, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--dir", default=None)
    ap.add_argument("--min-n", type=int, default=20)
    ap.add_argument("--fixture", action="store_true",
                    help="input is the machine-generated fixture, not participant data")
    args = ap.parse_args()

    paths = list(args.files)
    if args.dir:
        for fn in sorted(os.listdir(args.dir)):
            if fn.endswith(".json"):
                paths.append(os.path.join(args.dir, fn))
    if not paths:
        print("no participant files given (see --help)")
        return 1

    tag = "TEST_" if args.fixture else ""
    suffix = "_NOT_DATA" if args.fixture else ""
    tidy_name = "%shuman_tidy%s.csv" % (tag, suffix)
    summary_name = "%shuman_summary%s.json" % (tag, suffix)
    report_name = "%sHUMAN_RESULTS%s.md" % (tag, suffix)

    keys, kinds = key_table()
    os.makedirs(RESULTS, exist_ok=True)

    rows, excluded, kept = [], [], []
    for p in paths:
        part = read_export(p)
        ok, why = validate(part, keys)
        if not ok:
            excluded.append((os.path.basename(p), why))
            continue
        dur = part.get("duration_min")
        attempted = sum(1 for tr in part["trials"] if tr.get("response"))
        reason = None
        if attempted < len(part["trials"]):
            reason = "incomplete (%d/%d attempted)" % (attempted, len(part["trials"]))
        elif dur is not None and dur < MIN_DURATION_MIN:
            reason = "duration %.1f min < %d" % (dur, MIN_DURATION_MIN)
        elif dur is not None and dur > MAX_DURATION_MIN:
            reason = "duration %.1f min > %d" % (dur, MAX_DURATION_MIN)
        elif part.get("not_attempted"):
            reason = "self-reported non-attempt"
        if args.fixture:
            reason = None            # a fixture is a pipeline test, not a session
        if reason:
            excluded.append((part["participant"], reason))
            continue
        kept.append(part)
        for tr in part["trials"]:
            if not tr.get("response"):
                continue
            ans = keys[tr["item"]]
            rows.append({
                "participant": part["participant"], "item": tr["item"],
                "document": tr["document"], "register": tr["register"],
                "lang": tr["lang"], "kind": kinds[tr["item"]],
                "response": tr["response"], "correct": int(tr["response"] == ans),
                "keyed": ans, "rt_ms": tr.get("rt_ms"), "confidence": tr.get("confidence"),
            })

    tidy = os.path.join(RESULTS, tidy_name)
    with open(tidy, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["participant", "item", "document", "register",
                                          "lang", "kind", "response", "correct", "keyed",
                                          "rt_ms", "confidence"])
        w.writeheader()
        w.writerows(rows)

    print("%s files: %d | kept: %d | excluded: %d"
          % ("fixture" if args.fixture else "participant", len(paths), len(kept), len(excluded)))
    for who, why in excluded:
        print("  excluded %s: %s" % (who, why))
    print("item-administrations: %d -> %s" % (len(rows), os.path.relpath(tidy, os.path.dirname(HERE))))
    if not rows:
        return 1

    acc = A.accuracy([{"correct": r["correct"], "register": r["register"]} for r in rows], ["register"])
    for k, (c, n, p) in sorted(acc.items()):
        print("  accuracy %s: %.3f (%d/%d)" % (k[0], p, c, n))

    obs = [{"reader": r["participant"], "item": r["item"], "document": r["document"],
            "register": r["register"], "lang": r["lang"], "kind": r["kind"],
            "correct": r["correct"], "rt_ms": r["rt_ms"], "extra": r} for r in rows]
    rep = A.arm_report(obs, "human")
    confirmatory = (len(kept) >= args.min_n) and not args.fixture
    perm = rep["permutation"]
    eq = rep["equivalence"]
    supported = bool(perm["mean"] > 0 and perm["p"] < 0.05 and perm["mean"] >= A.SESOI_PP)
    falsified = bool(eq["equivalent"])

    if args.fixture:
        verdict = ("FIXTURE (machine-generated test record, N=%d): pipeline check only, "
                   "no inferential claim" % len(kept))
    elif not confirmatory:
        verdict = ("EXPLORATORY (N=%d < pre-registered minimum %d): H1 is not tested "
                   "confirmatorily; estimates only" % (len(kept), args.min_n))
    elif supported:
        verdict = "H1 SUPPORTED (mean difference %+.3f >= SESOI %.2f, exact p = %.4f)" % (
            perm["mean"], A.SESOI_PP, perm["p"])
    elif falsified:
        verdict = "H1 FALSIFIED (TOST rejects differences of +/-%.2f pp)" % (A.SESOI_PP * 100)
    else:
        verdict = "INCONCLUSIVE (mean %+.3f, p = %.4f, CI [%+.3f, %+.3f])" % (
            perm["mean"], perm["p"], rep["bootstrap_ci"][0], rep["bootstrap_ci"][1])

    with open(os.path.join(RESULTS, summary_name), "w", encoding="utf-8") as f:
        json.dump({"n_participants": len(kept), "excluded": excluded, "verdict": verdict,
                   "confirmatory": confirmatory, "fixture": bool(args.fixture),
                   "report": rep}, f, ensure_ascii=False, indent=2)

    L = ["# Results — human arm%s" % (" (FIXTURE, not data)" if args.fixture else ""), "",
         "**Participants kept:** %d (excluded %d) · **item-administrations:** %d · "
         "**confirmatory:** %s" % (len(kept), len(excluded), len(rows), confirmatory), "",
         "## Verdict", "", verdict, "",
         "## Pre-registered quantities", "",
         "| quantity | value |", "|---|---|"]
    for k, (c, n, p) in sorted(rep["accuracy_by_register"].items()):
        L.append("| accuracy, %s | %.3f (%d/%d) |" % (k, p, c, n))
    L += ["| mean item difference (plain - formal) | %+.3f |" % perm["mean"],
          "| exact sign-flip p (two-sided) | %.4f |" % perm["p"],
          "| 95%% bootstrap CI | [%+.3f, %+.3f] |" % (rep["bootstrap_ci"][0], rep["bootstrap_ci"][1]),
          "| TOST vs +/-%.0f pp | %s |" % (A.SESOI_PP * 100,
                                           "equivalent" if eq["equivalent"] else "not equivalent")]
    if rep["logit_fe"]:
        c = rep["logit_fe"]["coef"]["register_plain"]
        L.append("| logistic FE (item dummies): beta | %+.3f (OR %.2f, Wald p %.4f) |"
                 % (c["beta"], c["or"], c["p"]))
        L.append("| logistic FE: average marginal effect | %+.1f pp |" % (rep["logit_fe"]["ame_pp"] * 100))
    L += ["", "## Secondary (BH-FDR family)"]
    for (name, p), (_, thr, rej) in zip(rep["secondary_pvalues"], rep["secondary_bh"]):
        L.append("- %s: p = %.4f, BH threshold %.4f, reject = %s" % (name, p, thr, rej))
    L += ["", "## Accuracy by language and register", "", "| cell | accuracy | n |", "|---|---|---|"]
    for k, (c, n, p) in sorted(rep["accuracy_by_lang_register"].items()):
        L.append("| %s | %.3f | %d |" % (k, p, n))
    L += ["", "## Exclusions", ""]
    for who, why in excluded:
        L.append("- %s: %s" % (who, why))
    if not excluded:
        L.append("- none")
    L += ["", "## Item-level differences", "", "| item | difference |", "|---|---|"]
    for it, d in zip(rep["items"], rep["item_diffs"]):
        L.append("| %s | %+.3f |" % (it, d))
    with open(os.path.join(RESULTS, report_name), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    print("\nVERDICT: %s" % verdict)
    print("wrote %s and %s" % (os.path.relpath(tidy, os.path.dirname(HERE)),
                               os.path.relpath(os.path.join(RESULTS, report_name),
                                               os.path.dirname(HERE))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
