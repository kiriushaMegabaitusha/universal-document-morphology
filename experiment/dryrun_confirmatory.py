#!/usr/bin/env python3
"""Dry run: exercise the CONFIRMATORY path of score_human.py at the registered N.

The fixture path in test_survey_headless.py deliberately bypasses the confirmatory
branch, so until the first real participants arrive that branch is untested. This
generates synthetic participant exports in a temporary directory (never in the repo,
never mixed with real data), scores them through the real scorer, and checks the
pre-registered decision rule against known ground truth.

Scenarios (36 participants unless noted):

  A. true plain advantage 14 pp  -> must be detected (supported in nearly every draw)
  B. true plain advantage  5 pp  -> boundary case, reported descriptively
  C. no true difference          -> must essentially never be supported
  D. true plain advantage  8 pp  -> boundary case, reported descriptively
  E. true plain advantage  8 pp, N = 20 -> boundary case, reported descriptively

Invariants asserted (rates over repeated draws, not single-draw verdicts):

  * a SESOI-sized (14 pp) effect is detected in nearly every draw;
  * a null effect is essentially never declared supported;
  * all three branch types are reachable, so the inconclusive branch is not dead code;
  * every run exits 0.

Why rates and not verdicts: the registered decision rule is a threshold on the
OBSERVED estimate (+10 pp with p < 0.05). A true effect just below the SESOI will
sometimes draw an estimate above 10 pp and be declared supported — that is sampling
noise at the boundary of a threshold rule, not a bug, and it is why the estimate and
its confidence interval are always reported alongside the verdict. An earlier version
of this harness asserted "sub-SESOI never supported" and failed on exactly that,
correctly.

Determinism: seeds come from zlib.crc32 of the scenario label plus the draw index.
(hash() is randomised per process and made an earlier version irreproducible -
the same scenario flipped verdict between runs.)

Run:  python3 experiment/dryrun_confirmatory.py
"""
import json
import os
import random
import shutil
import subprocess
import sys
import tempfile
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
SCORER = os.path.join(HERE, "score_human.py")


def seed_of(label, draw=0):
    return zlib.crc32(("%s|%d" % (label, draw)).encode("utf-8")) % 100000


def make_participants(stim, n=36, effect_pp=0.14, seed=7):
    rng = random.Random(seed)
    docs = stim["documents"]
    out = []
    for i in range(n):
        pid = "dry%02d" % i
        lang = "uk" if rng.random() < 0.85 else "en"      # convenience sample is mostly uk
        reader_eff = rng.gauss(0, 0.10)
        item_eff = {d["id"]: rng.gauss(0, 0.12) for d in docs}
        trials = []
        for d in docs:
            for reg in ("formal", "plain"):
                for it in d["items"]:
                    p = 0.72 - effect_pp / 2 + (effect_pp if reg == "plain" else 0.0) \
                        + reader_eff + item_eff[d["id"]]
                    p = min(0.995, max(0.005, p))
                    key = it["answer"]
                    resp = key if rng.random() < p else rng.choice([c for c in "ABCD" if c != key])
                    trials.append({
                        "item": it["id"], "document": d["id"], "register": reg,
                        "lang": lang, "kind": it["kind"], "response": resp,
                        "correct": int(resp == key), "keyed": key,
                        "rt_ms": rng.randint(4000, 20000),
                        "confidence": rng.choice([1, 2, 3, 4, 5]) if rng.random() < p
                        else rng.choice([1, 2, 3]),
                    })
        out.append({
            "participant": pid, "lang": lang,
            "started": "2026-10-06T12:00:00", "finished": "2026-10-06T12:13:00",
            "n_trials": len(trials), "n_attempted": len(trials),
            "duration_min": round(rng.uniform(9.5, 18.0), 1),
            "design": "within: both registers of every obligation",
            "stimuli_version": stim["meta"]["created"], "trials": trials,
        })
    return out


def run_scenario(label, stim, effect_pp, root, n=36, draw=0):
    d = os.path.join(root, "in_%s" % label)
    o = os.path.join(root, "out_%s" % label)
    os.makedirs(d, exist_ok=True)
    os.makedirs(o, exist_ok=True)
    for part in make_participants(stim, n=n, effect_pp=effect_pp, seed=seed_of(label, draw)):
        with open(os.path.join(d, "comprehension_%s.json" % part["participant"]), "w",
                  encoding="utf-8") as f:
            json.dump(part, f, ensure_ascii=False)
    res = subprocess.run([sys.executable, SCORER, "--dir", d, "--min-n", "20", "--outdir", o],
                         capture_output=True, text=True)
    print("=" * 74)
    print("SYNTHETIC DRY RUN - %s draw %d: true plain advantage %.0f pp, N = %d"
          % (label, draw, effect_pp * 100, n))
    print("=" * 74)
    for line in res.stdout.strip().splitlines():
        if any(k in line for k in ("files:", "accuracy", "VERDICT")):
            print("  " + line)
    rep = os.path.join(o, "HUMAN_RESULTS.md")
    branch = None
    if os.path.exists(rep):
        for line in open(rep, encoding="utf-8"):
            if "mean item difference" in line or "sign-flip" in line or "TOST vs" in line:
                print("  " + line.strip())
            for tag in ("H1 SUPPORTED", "H1 FALSIFIED", "INCONCLUSIVE"):
                if line.startswith(tag):
                    branch = tag
    if res.returncode != 0:
        print("  scorer exit %d: %s" % (res.returncode, res.stderr[-300:]))
    return branch, res.returncode


def main():
    stim = json.load(open(os.path.join(HERE, "stimuli.json"), encoding="utf-8"))
    root = tempfile.mkdtemp(prefix="udm_dryrun_")
    print("synthetic exports and outputs live in %s (outside the repository)\n" % root)

    # (label, true effect, N, draws)
    scenarios = [("A_effect14pp", 0.14, 36, 6), ("C_null", 0.0, 36, 8),
                 ("B_effect5pp", 0.05, 36, 6), ("D_effect8pp", 0.08, 36, 6),
                 ("E_effect8pp_n20", 0.08, 20, 6)]
    rates, seen, codes = {}, set(), []
    for label, eff, n, draws in scenarios:
        hits = 0
        for draw in range(draws):
            branch, code = run_scenario(label, stim, eff, root, n=n, draw=draw)
            codes.append(code)
            if branch:
                seen.add(branch)
            hits += 1 if branch == "H1 SUPPORTED" else 0
        rates[label] = (hits, draws)
        print("  -> %s: supported in %d/%d draws\n" % (label, hits, draws))

    print("=" * 74)
    print("supported rate by scenario:", {k: "%d/%d" % v for k, v in rates.items()})
    print("distinct branches reached:", sorted(seen))
    checks = [
        ("SESOI-sized effect detected (A supported in >= %d/%d)"
         % (rates["A_effect14pp"][1] - 1, rates["A_effect14pp"][1]),
         rates["A_effect14pp"][0] >= rates["A_effect14pp"][1] - 1),
        ("null rarely declared supported (C <= 2/%d)" % rates["C_null"][1],
         rates["C_null"][0] <= 2),
        ("all three branches reachable", len(seen) == 3),
        ("every run exited 0", all(c == 0 for c in codes)),
    ]
    ok = True
    for label, passed in checks:
        print("  %-52s %s" % (label, "ok" if passed else "FAIL"))
        ok = ok and passed
    print("\nboundary note: sub-SESOI scenarios (B/D/E) are reported above without a "
          "hard expectation;\na true effect near the SESOI can be declared supported "
          "when sampling noise pushes the\nobserved estimate over +10 pp. That is the "
          "registered rule working, not a defect.")
    print("\n%s" % ("OK - confirmatory path behaves as registered on synthetic data"
                    if ok else "CHECK - see the FAIL rows above"))
    shutil.rmtree(root, ignore_errors=True)
    print("cleaned up %s" % root)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
