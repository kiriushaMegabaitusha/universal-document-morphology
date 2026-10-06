#!/usr/bin/env python3
"""Dry run: exercise the CONFIRMATORY path of score_human.py at the registered N.

The fixture path in test_survey_headless.py deliberately bypasses the confirmatory
branch, so until the first real participants arrive that branch is untested. This
generates synthetic participant exports in a temporary directory (never in the repo,
never mixed with real data), scores them through the real scorer, and checks the
pre-registered decision rule against known ground truth.

Scenarios (36 participants unless noted):

  A. true plain advantage 14 pp  -> must be H1 SUPPORTED
  B. true plain advantage  5 pp  -> must NOT be supported
  C. no true difference          -> must NOT be supported
  D. true plain advantage  8 pp  -> must NOT be supported
  E. true plain advantage  8 pp, N = 20 -> must NOT be supported

Invariants asserted (not a per-scenario verdict table): a SESOI-sized effect is
detected; sub-SESOI and null effects are never declared supported; and all three
branch types are reachable, so the inconclusive branch is not dead code.

Why not demand a specific verdict for B/D/E: with a real but sub-SESOI effect the
registered rule returns FALSIFIED when the data can exclude a 10 pp advantage and
INCONCLUSIVE when they cannot. Both are correct outcomes - only "SUPPORTED" would be
an error. The registered semantics of FALSIFIED is "a plain advantage of 10 pp or
more is excluded", never "formal beat plain".

Determinism: seeds come from zlib.crc32 of the scenario label. (An earlier version
used hash(), which is randomised per process and made the script irreproducible -
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


def seed_of(label):
    return zlib.crc32(label.encode("utf-8")) % 100000


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


def run_scenario(label, stim, effect_pp, root, n=36):
    d = os.path.join(root, "in_%s" % label)
    o = os.path.join(root, "out_%s" % label)
    os.makedirs(d, exist_ok=True)
    os.makedirs(o, exist_ok=True)
    for part in make_participants(stim, n=n, effect_pp=effect_pp, seed=seed_of(label)):
        with open(os.path.join(d, "comprehension_%s.json" % part["participant"]), "w",
                  encoding="utf-8") as f:
            json.dump(part, f, ensure_ascii=False)
    res = subprocess.run([sys.executable, SCORER, "--dir", d, "--min-n", "20", "--outdir", o],
                         capture_output=True, text=True)
    print("=" * 74)
    print("SYNTHETIC DRY RUN - %s: true plain advantage %.0f pp, N = %d"
          % (label, effect_pp * 100, n))
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

    scenarios = [("A_effect14pp", 0.14, 36), ("B_effect5pp", 0.05, 36),
                 ("C_null", 0.0, 36), ("D_effect8pp", 0.08, 36),
                 ("E_effect8pp_n20", 0.08, 20)]
    results, codes = {}, []
    for label, eff, n in scenarios:
        branch, code = run_scenario(label, stim, eff, root, n=n)
        results[label] = branch
        codes.append(code)

    seen = {b for b in results.values() if b}
    print("=" * 74)
    print("branches by scenario:", results)
    print("distinct branches reached:", sorted(seen))
    checks = [
        ("SESOI-sized effect detected (A supported)",
         results.get("A_effect14pp") == "H1 SUPPORTED"),
        ("sub-SESOI effect never declared supported",
         all(results.get(k) != "H1 SUPPORTED"
             for k in ("B_effect5pp", "D_effect8pp", "E_effect8pp_n20"))),
        ("null never declared supported", results.get("C_null") != "H1 SUPPORTED"),
        ("all three branches reachable", len(seen) == 3),
        ("every scenario exited 0", all(c == 0 for c in codes)),
    ]
    ok = True
    for label, passed in checks:
        print("  %-45s %s" % (label, "ok" if passed else "FAIL"))
        ok = ok and passed
    print("\n%s" % ("OK - confirmatory path behaves as registered on synthetic data at N = 36"
                    if ok else "CHECK - see the FAIL rows above"))
    shutil.rmtree(root, ignore_errors=True)
    print("cleaned up %s" % root)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
