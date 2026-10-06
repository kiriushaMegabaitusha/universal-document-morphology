#!/usr/bin/env python3
"""Simulated-data check of the pre-registered analysis.

Registered analysis code must run, and must behave, before real data arrives.
This does three things:

1. PIPELINE. Generates a machine-arm-shaped dataset with a known plain-language
   advantage, writes it as JSONL, and runs the full pre-registered analysis
   (sign-flip test, logistic FE, TOST equivalence, reader-clustered bootstrap).
   The estimate must recover the simulated effect.

2. NULL CALIBRATION. 200 simulated datasets with NO effect -> the rejection rate
   of the primary test at alpha = 0.05 must sit near 5%. (The sign-flip test is
   exact, so this is a check on the implementation, not on the method.)

3. POWER / MDE for the human arm. The human arm is not yet run; the sample size
   has to be justified before recruitment. Simulates the pre-registered incomplete
   design (each participant reads each obligation in one register, own language)
   at N = 12 / 24 / 36 participants for a 10 pp and a 15 pp true gap, reporting
   power and the minimum detectable effect at the planned N = 24.

Everything is seeded. Run:  python3 experiment/simulate_data.py
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import analysis_core as A  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
SEED = 20261006

# The simulation mirrors the real instrument's structure, read from the stimuli, so
# that adding or removing items updates the power numbers automatically.
_STIM = json.load(open(os.path.join(HERE, "stimuli.json"), encoding="utf-8"))
OBLIGATIONS = [d["id"] for d in _STIM["documents"]]
ITEMS = {d["id"]: [(i["id"], i["kind"]) for i in d["items"]] for d in _STIM["documents"]}
NI = sum(len(v) for v in ITEMS.values())          # items per participant per register


def simulate(seed, effect_pp, n_readers=4, item_sd=0.12, reader_sd=0.10,
             design="both", lang="en"):
    """Simulated observations.

    design='both' : every reader sees every obligation in BOTH registers
                    (machine-arm shape; also the within-reader human shape)
    design='split': every reader sees each obligation in ONE register only
                    (incomplete/Latin-square shape, 12 items per reader)
    effect_pp     : true plain-minus-formal advantage in probability
    """
    rng = np.random.default_rng(seed)
    obs, item_eff, reader_eff = [], {}, {}
    for it in OBLIGATIONS:
        item_eff[it] = rng.normal(0, item_sd)
    for r in range(n_readers):
        reader_eff[r] = rng.normal(0, reader_sd)
    base = 0.72 - effect_pp / 2
    for r in range(n_readers):
        for j, it in enumerate(OBLIGATIONS):
            if design == "both":
                regs = ["formal", "plain"]
            else:
                regs = [["plain", "formal"][(j + r) % 2]]
            for reg in regs:
                for q, kind in ITEMS[it]:
                    p = base + (effect_pp if reg == "plain" else 0.0) + item_eff[it] + reader_eff[r]
                    p = min(0.99, max(0.01, p))
                    obs.append({
                        "model": "sim-r%d" % r, "item": q, "document": it,
                        "register": reg, "lang": lang, "kind": kind,
                        "correct": int(rng.random() < p),
                        "latency_ms": int(rng.normal(1200, 250)),
                    })
    return obs


def to_jsonl(obs, path):
    with open(path, "w", encoding="utf-8") as f:
        for o in obs:
            f.write(json.dumps(o, ensure_ascii=False) + "\n")


def primary_p(diffs):
    return A.signflip_test(diffs)["p"]


def main():
    os.makedirs(RESULTS, exist_ok=True)

    # ---- 1. pipeline on a known effect -----------------------------------
    obs = simulate(SEED, effect_pp=0.20)
    path = os.path.join(RESULTS, "simulated_machine.jsonl")
    to_jsonl(obs, path)
    loaded = A.load_machine(path)
    rep = A.arm_report(loaded, "simulated (effect = +20 pp)")
    perm = rep["permutation"]
    fe = rep["logit_fe"]
    print("1. PIPELINE (simulated effect +20 pp, 4 readers, full design)")
    print("   obs=%d items=%d  mean item diff = %+.3f  sign-flip p = %.5f (%s)"
          % (rep["n_obs"], rep["n_items"], perm["mean"], perm["p"],
             "exact" if perm["exact"] else "sampled"))
    print("   logistic FE: beta=%+.3f OR=%.2f AME=%+.1f pp (Wald p=%.4f)"
          % (fe["coef"]["register_plain"]["beta"], fe["coef"]["register_plain"]["or"],
             fe["ame_pp"] * 100, fe["coef"]["register_plain"]["p"]))
    print("   95%% CI on item diffs: [%+.3f, %+.3f] | TOST equivalent-to-zero: %s"
          % (rep["bootstrap_ci"][0], rep["bootstrap_ci"][1], rep["equivalence"]["equivalent"]))
    ok = (perm["p"] < 0.05 and perm["mean"] > 0.10)

    # ---- 2. null calibration ---------------------------------------------
    print("\n2. NULL CALIBRATION (200 datasets, true effect 0)")
    rej = 0
    for s in range(200):
        o = simulate(1000 + s, effect_pp=0.0)
        _, d = A.item_differences(o)
        if primary_p(d) < 0.05:
            rej += 1
    rate = rej / 200
    print("   rejection rate at alpha=0.05: %.3f (%d/200)  [expect ~0.05]" % (rate, rej))
    ok = ok and 0.015 <= rate <= 0.11

    # ---- 3. power for the human arm: two candidate designs ---------------
    def power(eff, n, design, seed0, n_sims=60):
        hits = 0
        for s in range(n_sims):
            _, d = A.item_differences(simulate(seed0 + s, effect_pp=eff, n_readers=n, design=design))
            if primary_p(d) < 0.05 and d.mean() > 0:
                hits += 1
        return hits / n_sims

    print("\n3. POWER FOR THE HUMAN ARM (%d obligations, %d items)" % (len(OBLIGATIONS), NI))
    print("   A = split: each participant reads each obligation in ONE register (%d trials)" % NI)
    print("   B = both : each participant reads BOTH registers of every obligation (%d trials)" % (2 * NI))
    print("   %-7s %-14s %-14s" % ("true pp", "A split N=24", "B both N=24"))
    for eff in (0.05, 0.10, 0.15):
        print("   %-7.2f %-14.2f %-14.2f"
              % (eff, power(eff, 24, "split", 5000), power(eff, 24, "both", 6000)))
    print("   design B at the pre-registered effect sizes:")
    print("   %-7s %-8s %-8s %-8s" % ("true pp", "N=12", "N=24", "N=36"))
    for eff in (0.05, 0.10, 0.15):
        print("   %-7.2f %-8.2f %-8.2f %-8.2f"
              % (eff, power(eff, 12, "both", 6100), power(eff, 24, "both", 6200),
                 power(eff, 36, "both", 6300)))
    pm = power(0.10, 4, "both", 6500, n_sims=100)
    print("   machine-arm shape (4 readers, both registers, 96 obs): power at 10 pp = %.2f" % pm)
    for n_target in (24, 36, 48):
        if power(0.10, n_target, "both", 7000) >= 0.80:
            print("   design B reaches >= 80%% power at a true 10 pp gap by N = %d" % n_target)
            break
    print("   (design A would need several times that N, so B is the pre-registered design)")

    print("\n%s" % ("OK - registered analysis runs on simulated data, recovers a known "
                    "effect, and controls the null at nominal alpha" if ok else
                    "PROBLEM - see the numbers above"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
