#!/usr/bin/env python3
"""Registered analysis for P06-2 — see PREREGISTRATION.md (same directory).

Implements §6 of the registration exactly: assertions first, family A (6 negation
edges), family B (4 implications), family C (joint fork), tradition-blocked
secondary null (§5.2), deterministic informativeness thresholds n* (§6.6), BH and
BY corrections, registered predictions R1–R4 (§2), decision labels (§7).

Run once after registration. --self-test exercises the pipeline on a synthetic
frame only and never reads the registered matrix.
Writes results.json next to itself and prints the registered tables.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SLOT_MATRIX = REPO / "analysis" / "slot_matrix.csv"
REQS = REPO / "requisites.csv"
BLOCKS_CSV = HERE / "tradition_blocks.csv"

SHA256_SLOT = "c29d0234ffb657e3c3bc580816c119bd2c439b721489892383cd671a2c74a6a3"
SHA256_REQ = "ab501702a4e54bab151859d686bad752e61a3938b809b6b951d07b59990a82cd"

SLOTS = [f"S{i}" for i in range(1, 15)]
EXPECTED_MARGINS = {"S9": 2, "S4": 9, "S6": 8, "S7": 9, "S8": 10,
                    "S10": 14, "S12": 17, "S14": 11}
EXPECTED_ROWS = 25

FAMILY_A = [("S9", "S4"), ("S9", "S6"), ("S9", "S7"), ("S9", "S8"),
            ("S9", "S10"), ("S9", "S14")]
FAMILY_B = [("S6", "S12"), ("S6", "S8"), ("S6", "S10"), ("S8", "S12")]
PARTNERS = ["S4", "S6", "S7", "S8", "S10", "S14"]

ALPHA = Fraction(1, 20)
MC_DRAWS = 100_000
SEED = 20261015
N_MAX = 500

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()

def load_matrix() -> tuple[list[str], dict[str, set[str]]]:
    with open(SLOT_MATRIX, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        cols = reader.fieldnames or []
        assert cols == ["system"] + SLOTS, f"column set drifted: {cols}"
        rows = list(reader)
    assert len(rows) == EXPECTED_ROWS, f"row count drifted: {len(rows)}"
    data: dict[str, set[str]] = {}
    for r in rows:
        data[r["system"]] = {s for s in SLOTS if r[s].strip() == "1"}
    margins = {s: sum(1 for v in data.values() if s in v) for s in EXPECTED_MARGINS}
    assert margins == EXPECTED_MARGINS, f"margin drift: {margins}"
    return list(data.keys()), data

def load_blocks(systems: list[str]) -> dict[str, str]:
    with open(BLOCKS_CSV, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    blocks = {r["system"]: r["block"] for r in rows}
    missing = [s for s in systems if s not in blocks]
    extra = [s for s in blocks if s not in systems]
    assert not missing and not extra, f"block table mismatch: missing={missing} extra={extra}"
    return blocks

# ---------- exact tests (rational arithmetic) ----------

def hyper_pmf(N: int, K: int, n: int, x: int) -> Fraction:
    if x < 0 or x > K or x > n or (N - K) < (n - x):
        return Fraction(0)
    return Fraction(math.comb(K, x) * math.comb(N - K, n - x), math.comb(N, n))

def p_depletion(N: int, K: int, n: int, obs: int) -> Fraction:
    """P(X <= obs): fewer co-occurrences than independence predicts."""
    return sum((hyper_pmf(N, K, n, x) for x in range(0, obs + 1)), Fraction(0))

def p_enrichment(N: int, K: int, n: int, obs: int) -> Fraction:
    """P(X >= obs): more co-occurrences / full support than independence predicts."""
    return sum((hyper_pmf(N, K, n, x) for x in range(obs, min(K, n) + 1)), Fraction(0))

def p_two_sided(N: int, K: int, n: int, obs: int) -> Fraction:
    p_obs = hyper_pmf(N, K, n, obs)
    total = Fraction(0)
    for x in range(0, min(K, n) + 1):
        px = hyper_pmf(N, K, n, x)
        if px <= p_obs:
            total += px
    return min(total, Fraction(1))

def bh_q(ps: list[Fraction]) -> list[Fraction]:
    m = len(ps)
    order = sorted(range(m), key=lambda i: ps[i])
    q = [Fraction(0)] * m
    running = Fraction(1)
    for rank in range(m, 0, -1):
        i = order[rank - 1]
        running = min(running, ps[i] * m / rank)
        q[i] = min(running, Fraction(1))
    return q

def by_q(ps: list[Fraction]) -> list[Fraction]:
    Hm = sum((Fraction(1, i) for i in range(1, len(ps) + 1)), Fraction(0))
    return bh_q([min(p * Hm, Fraction(1)) for p in ps])

def haldane_or(a: int, b: int, c: int, d: int) -> float:
    return ((a + 0.5) * (d + 0.5)) / ((b + 0.5) * (c + 0.5))

def rnd(x: float) -> int:
    """Registered margin scaling: floor(x + 0.5)."""
    return int(x + 0.5)

# ---------- analysis sections ----------

def run_families(data: dict[str, set[str]]) -> dict:
    systems = list(data.keys())
    N = len(systems)

    # Family A: negation edges (one-sided depletion + BH + BY + two-sided)
    A_rows = []
    for x, y in FAMILY_A:
        n = sum(1 for s in systems if x in data[s])
        K = sum(1 for s in systems if y in data[s])
        a = sum(1 for s in systems if x in data[s] and y in data[s])
        b, c = n - a, K - a
        d = N - a - b - c
        A_rows.append({
            "edge": f"{x}⊥{y}", "x": x, "y": y,
            "overlap": a, "expected": n * K / N,
            "p_dep": p_depletion(N, K, n, a),
            "p_two_sided": p_two_sided(N, K, n, a),
            "or_haldane": haldane_or(a, b, c, d),
        })
    q_bh = bh_q([r["p_dep"] for r in A_rows])
    q_by = by_q([r["p_dep"] for r in A_rows])
    for r, q1, q2 in zip(A_rows, q_bh, q_by):
        r["q_bh"], r["q_by"] = q1, q2
        r["reject_bh"] = q1 < ALPHA

    # Family B: implications (one-sided enrichment + BH + BY; assert full support)
    B_rows = []
    for x, y in FAMILY_B:
        aN = sum(1 for s in systems if x in data[s])
        bN = sum(1 for s in systems if y in data[s])
        s_xy = sum(1 for s in systems if x in data[s] and y in data[s])
        assert s_xy == aN, f"{x}⇒{y} no longer confidence 1.00 in the frozen matrix: {s_xy}/{aN}"
        B_rows.append({
            "rule": f"{x}⇒{y}", "x": x, "y": y,
            "support": f"{s_xy}/{aN}", "antecedent": aN, "consequent": bN,
            "p_enrich": p_enrichment(N, bN, aN, s_xy),
        })
    q_bh = bh_q([r["p_enrich"] for r in B_rows])
    q_by = by_q([r["p_enrich"] for r in B_rows])
    for r, q1, q2 in zip(B_rows, q_bh, q_by):
        r["q_bh"], r["q_by"] = q1, q2
        r["reject_bh"] = q1 < ALPHA

    # Family C: joint fork — exact enumeration of all C(25,2) placements of S9
    s9 = [s for s in systems if "S9" in data[s]]
    assert len(s9) == EXPECTED_MARGINS["S9"]
    carriers = {s: any(p in data[s] for p in PARTNERS) for s in systems}
    assert all(not carriers[s] for s in s9), "frozen matrix no longer shows the joint fork"
    pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    total = len(pairs)
    assert total == math.comb(N, 2) == 300, total
    t_zero = 0
    for i, j in pairs:
        t = int(carriers[systems[i]]) + int(carriers[systems[j]])
        if t == 0:
            t_zero += 1
    C = {"placements": total, "t_zero": t_zero, "p": Fraction(t_zero, total),
         "floor": Fraction(1, total)}

    return {"A": A_rows, "B": B_rows, "C": C, "systems": systems, "data": data}

def run_blocked(res: dict, blocks: dict[str, str]) -> dict:
    """Secondary null (§5.2): S9 placements enumerated exactly within blocks;
    family B via Monte Carlo (100k, seed 20261015), consequent permuted in-block."""
    systems, data = res["systems"], res["data"]
    N = len(systems)

    by_block: dict[str, list[str]] = {}
    for s in systems:
        by_block.setdefault(blocks[s], []).append(s)
    k_by_block = {b: sum(1 for s in ss if "S9" in data[s]) for b, ss in by_block.items()}

    # enumerate all within-block placements of the S9 vector
    placements: list[set[str]] = [set()]
    for b, ss in by_block.items():
        k = k_by_block[b]
        if k == 0:
            continue
        combos = [set(c) for c in _combos(ss, k)]
        placements = [p | c for p in placements for c in combos]
    total = len(placements)

    out = {"placements": total,
           "degenerate": total <= 1,
           "note": "single observed placement — no permutation space" if total <= 1 else ""}
    carriers = {s: any(p in data[s] for p in PARTNERS) for s in systems}
    obs_zero = 0
    out["A"] = {}
    for x, y in FAMILY_A:
        obs = sum(1 for s in systems if "S9" in data[s] and y in data[s])
        cnt = sum(1 for pl in placements
                  if sum(1 for s in pl if y in data[s]) <= obs)
        out["A"][f"{x}⊥{y}"] = {"p": Fraction(cnt, total), "obs": obs}
    cnt_t = sum(1 for pl in placements
                if sum(1 for s in pl if carriers[s]) <= 0)
    out["C"] = {"p": Fraction(cnt_t, total)}

    out["B"] = {}
    for rule_i, (x, y) in enumerate(FAMILY_B):
        aN = sum(1 for s in systems if x in data[s])
        bN = sum(1 for s in systems if y in data[s])
        y_by_block = {b: [s for s in ss if y in data[s]] for b, ss in by_block.items()}
        rng = random.Random(SEED + rule_i)
        ge = 0
        for _ in range(MC_DRAWS):
            hit = 0
            for b, ylist in y_by_block.items():
                if not ylist:
                    continue
                shuffled = by_block[b][:]
                rng.shuffle(shuffled)
                yset = set(shuffled[:len(ylist)])
                hit += sum(1 for s in yset if x in data[s])
                if hit > aN:  # can't exceed observed full support; early exit safe
                    break
            if hit >= aN:
                ge += 1
        p = Fraction(1 + ge, 1 + MC_DRAWS)
        out["B"][f"{x}⇒{y}"] = {"p": p, "draws": MC_DRAWS, "seed": SEED + rule_i,
                                "formula": "(1 + #{stat >= observed}) / (1 + draws)"}
    return out

def _combos(items: list[str], k: int):
    if k == 0:
        yield ()
        return
    n = len(items)
    def rec(start: int, need: int, acc: tuple):
        if need == 0:
            yield acc
            return
        for i in range(start, n - need + 1):
            yield from rec(i + 1, need - 1, acc + (items[i],))
    yield from rec(0, k, ())

def run_thresholds(res: dict) -> dict:
    """n* (§6.6): deterministic; margins scaled at current proportions."""
    systems, data = res["systems"], res["data"]
    thresholds = {"A": {}, "B": {}}
    for x, y in FAMILY_A:
        k9_0 = EXPECTED_MARGINS["S9"]
        kj_0 = EXPECTED_MARGINS[y]
        star = None
        for N in range(25, N_MAX + 1):
            k9, kj = rnd(k9_0 * N / 25), rnd(kj_0 * N / 25)
            p = Fraction(math.comb(N - kj, k9), math.comb(N, k9)) if k9 <= N - kj else Fraction(0)
            if p < ALPHA:
                star = N
                break
        thresholds["A"][f"{x}⊥{y}"] = star
    for x, y in FAMILY_B:
        a_0 = {"S6": 8, "S8": 10}[x]  # registered antecedent margins
        b_0 = EXPECTED_MARGINS[y]
        star = None
        for N in range(25, N_MAX + 1):
            aN, bN = rnd(a_0 * N / 25), rnd(b_0 * N / 25)
            if aN > bN:
                p = Fraction(0)
            else:
                p = Fraction(math.comb(bN, aN), math.comb(N, aN))
            if p < ALPHA:
                star = N
                break
        thresholds["B"][f"{x}⇒{y}"] = star
    return thresholds

def r_verdicts(A_rows, B_rows, C, thresholds) -> dict:
    r1 = sum(1 for r in A_rows if r["reject_bh"]) == 0
    r2 = C["p"] < ALPHA
    r3 = any(r["reject_bh"] for r in B_rows)
    nstars = [v for v in thresholds["A"].values()]
    r4 = any(v is not None and v > 100 for v in nstars) or any(v is None for v in nstars)
    return {"R1_no_A_rejections": r1, "R2_joint_rejects": r2,
            "R3_any_B_rejects": r3, "R4_some_nstar_gt_100": r4}

def serialise(obj):
    if isinstance(obj, Fraction):
        return {"num": obj.numerator, "den": obj.denominator, "value": float(obj)}
    if isinstance(obj, set):
        return sorted(obj)
    if isinstance(obj, dict):
        return {k: serialise(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [serialise(v) for v in obj]
    return obj

def git_head() -> str:
    try:
        return subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"

def real_run() -> dict:
    # §6.1 assertions first — including registered file hashes
    assert sha256(SLOT_MATRIX) == SHA256_SLOT, "slot_matrix.csv hash mismatch — amendment required before any test"
    assert sha256(REQS) == SHA256_REQ, "requisites.csv hash mismatch — amendment required before any test"
    systems, data = load_matrix()
    blocks = load_blocks(systems)
    res = run_families(data)
    blocked = run_blocked(res, blocks)
    thresholds = run_thresholds(res)
    verdicts = r_verdicts(res["A"], res["B"], res["C"], thresholds)
    out = {"registration_commit": git_head(), "input_hashes": {"slot_matrix": SHA256_SLOT,
                                                                "requisites": SHA256_REQ},
           "n_systems": len(systems), "families": res, "blocked": blocked,
           "thresholds": thresholds, "R_verdicts": verdicts,
           "alpha": float(ALPHA), "mc_draws": MC_DRAWS, "seed": SEED,
           "deviations": "see DEVIATIONS.md"}
    out = serialise(out)
    (HERE / "results.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print_tables(res, blocked, thresholds, verdicts)
    print(f"\nregistration commit: {out['registration_commit']}")
    print("results.json written:", HERE / "results.json")
    return out

def print_tables(res, blocked, thresholds, verdicts) -> None:
    print("Family A — negation edges (one-sided depletion, primary null)")
    print(f"{'edge':<10} {'obs':>3} {'exp':>5} {'p':>9} {'q_BH':>9} {'q_BY':>9} {'p_blk':>9} {'n*':>5}")
    for r in res["A"]:
        key = r["edge"]
        pb = blocked["A"][key]["p"]
        star = thresholds["A"][key]
        print(f"{key:<10} {r['overlap']:>3} {r['expected']:>5.2f} "
              f"{float(r['p_dep']):>9.4f} {float(r['q_bh']):>9.4f} {float(r['q_by']):>9.4f} "
              f"{float(pb):>9.4f} {str(star) if star else '>500':>5}")
    print("\nFamily B — implications at confidence 1.00 (one-sided enrichment)")
    print(f"{'rule':<10} {'supp':>6} {'p':>9} {'q_BH':>9} {'q_BY':>9} {'p_blk(MC)':>10} {'n*':>5}")
    for r in res["B"]:
        key = r["rule"]
        pb = blocked["B"][key]["p"]
        star = thresholds["B"][key]
        print(f"{key:<10} {r['support']:>6} {float(r['p_enrich']):>9.4f} "
              f"{float(r['q_bh']):>9.4f} {float(r['q_by']):>9.4f} {float(pb):>10.4f} "
              f"{str(star) if star else '>500':>5}")
    C = res["C"]
    print(f"\nFamily C — joint fork: p = {C['t_zero']}/{C['placements']} = {float(C['p']):.4f} "
          f"(floor {float(C['floor']):.4f}) | blocked p = {float(blocked['C']['p']):.4f} "
          f"over {blocked['placements']} within-block placements"
          + (f" [{blocked['note']}]" if blocked["note"] else ""))
    print("\nRegistered predictions:")
    for k, v in verdicts.items():
        print(f"  {k}: {'confirmed' if v else 'NOT confirmed'}")

def self_test() -> None:
    """Synthetic frame only; never reads the registered matrix (§ house pattern).
    The frame is constructed to satisfy the registered data asserts: exactly two
    S9 systems carrying no partner slot, and confidence-1.00 support on family B."""
    rng = random.Random(7)
    systems = [f"sys{i:02d}" for i in range(25)]
    data = {s: {sl for sl in SLOTS if rng.random() < 0.4} for s in systems}
    # fork rows: sys00/sys01 carry S9 and no partner slot
    for s in systems:
        data[s].discard("S9")
    for s in systems[:2]:
        data[s] = {sl for sl in data[s] if sl not in PARTNERS}
        data[s].add("S9")
    # family B closure: every antecedent carrier gets its consequent
    for x, y in FAMILY_B:
        for s in systems:
            if x in data[s]:
                data[s].add(y)
    res = run_families(data)
    blocks = {s: f"blk{i % 4}" for i, s in enumerate(systems)}
    blocked = run_blocked(res, blocks)
    th = run_thresholds(res)
    v = r_verdicts(res["A"], res["B"], res["C"], th)
    out = serialise({"families": res, "blocked": blocked, "thresholds": th, "R": v})
    json.dumps(out)  # must serialise
    print("SELFTEST OK — families, blocked null, thresholds and verdicts all ran on synthetic data")
    print_tables(res, blocked, th, v)

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true",
                    help="run the pipeline on synthetic data only; never reads the registered matrix")
    args = ap.parse_args()
    if args.self_test:
        self_test()
    else:
        real_run()
    return 0

if __name__ == "__main__":
    sys.exit(main())