#!/usr/bin/env python3
"""B3 — lineage-restricted re-derivation of the document-morphology atlas.

Implements `brainstorm/B3_PREREGISTRATION_DRAFT.md` §6, in the house pattern of
`audit/null_audit.py`: assertions first, registered families only, exact arithmetic
where it is cheap, Monte Carlo where it is not, and a `--self-test` that runs on a
synthetic frame and never opens the real matrix.

Run once after registration. `--self-test` is the only mode that may be run before
the registration commit.

Outputs (real mode): results.json next to this file, plus the printed tables.

Dependencies: Python standard library only.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import math
import random
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
SLOT_MATRIX = REPO / "analysis" / "slot_matrix.csv"
REQS = REPO / "requisites.csv"
BLOCKS = HERE / "lineage_blocks.csv"
MANDATORY = HERE / "mandatory_only.csv"

SHA_SLOT = "c29d0234ffb657e3c3bc580816c119bd2c439b721489892383cd671a2c74a6a3"
SHA_REQ = "ab501702a4e54bab151859d686bad752e61a3938b809b6b951d07b59990a82cd"

SLOTS = [f"S{i}" for i in range(1, 15)]
PARTNERS = ["S4", "S6", "S7", "S8", "S10", "S14"]
STEM = ["S1", "S3", "S5", "S10", "S12", "S13"]
IMPLICATIONS = [("S6", "S12"), ("S6", "S8"), ("S6", "S10"), ("S8", "S12")]
VARIANTS = ("narrow", "base", "broad")

MC_DRAWS = 100_000
MC_MAX_ENUM = 200_000
SEED = 20261101
ALPHA = Fraction(1, 20)


# ---------------------------------------------------------------- utilities ----
def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def bh_q(ps: list[Fraction]) -> list[Fraction]:
    """Benjamini–Hochberg adjusted q-values, exact rationals."""
    m = len(ps)
    order = sorted(range(m), key=lambda i: ps[i])
    q = [Fraction(1)] * m
    prev = Fraction(1)
    for rank in range(m, 0, -1):
        i = order[rank - 1]
        val = ps[i] * Fraction(m, rank)
        prev = min(prev, val)
        q[i] = prev
    return q


def by_q(ps: list[Fraction]) -> list[Fraction]:
    """Benjamini–Yekutieli adjusted q-values, exact rationals."""
    m = len(ps)
    harm = sum(Fraction(1, k) for k in range(1, m + 1))
    order = sorted(range(m), key=lambda i: ps[i])
    q = [Fraction(1)] * m
    prev = Fraction(1)
    for rank in range(m, 0, -1):
        i = order[rank - 1]
        val = ps[i] * Fraction(m, rank) * harm
        prev = min(prev, val)
        q[i] = prev
    return q


def rnd(x: Fraction | float, nd: int = 4) -> float:
    return round(float(x), nd)


# -------------------------------------------------------------- data loading ----
def load_matrix(path: Path) -> tuple[list[str], dict[str, set[str]]]:
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        cols = reader.fieldnames or []
        assert cols == ["system"] + SLOTS, f"column set drifted: {cols}"
        rows = list(reader)
    systems = [r["system"] for r in rows]
    assert len(systems) == 25, f"expected 25 rows, got {len(systems)}"
    data = {r["system"]: {s for s in SLOTS if r[s] == "1"} for r in rows}
    return systems, data


def load_blocks(path: Path, variant: str) -> dict[str, str]:
    assert variant in VARIANTS, variant
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        need = {"system", "narrow", "base", "broad", "confidence", "basis"}
        assert need <= set(reader.fieldnames or []), f"blocks columns: {reader.fieldnames}"
        rows = list(reader)
    assert len(rows) == 25, f"expected 25 systems in lineage table, got {len(rows)}"
    assert len({r["system"] for r in rows}) == 25, "duplicate system in lineage table"
    for r in rows:
        assert r[variant].strip(), f"{r['system']}: empty {variant} lineage"
        if r["confidence"] in ("documented", "documented-singleton"):
            assert ".md" in r["basis"] or "cases/" in r["basis"], (
                f"{r['system']}: documented membership without a citation")
    return {r["system"]: r[variant] for r in rows}


def mandatory_matrix(systems: list[str], path: Path) -> dict[str, set[str]]:
    """Frozen rule: cell = 1 iff >=1 mandatory requisite maps to that slot."""
    out = {s: set() for s in systems}
    with open(path, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            if r["obligation"] != "mandatory" or r["system"] not in out:
                continue
            slot = r["slot"].split("-", 1)[0]
            if slot in SLOTS:
                out[r["system"]].add(slot)
    return out


def write_mandatory(systems: list[str], data: dict[str, set[str]], path: Path) -> None:
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["system"] + SLOTS)
        for s in systems:
            w.writerow([s] + [1 if x in data[s] else 0 for x in SLOTS])


# ------------------------------------------------------------- block algebra ----
def block_sizes(blocks: dict[str, str], systems: list[str]) -> list[int]:
    counts: dict[str, int] = defaultdict(int)
    for s in systems:
        counts[blocks[s]] += 1
    return sorted(counts.values(), reverse=True)


def pair_counts(sizes: list[int], n: int) -> tuple[int, int]:
    within = sum(k * (k - 1) // 2 for k in sizes)
    total = n * (n - 1) // 2
    return within, total - within


def smc(a: set[str], b: set[str], slots: list[str]) -> int:
    return sum(1 for s in slots if (s in a) == (s in b))


def agreement_table(systems: list[str], data: dict[str, set[str]],
                    slots: list[str]) -> tuple[dict[tuple[int, int], int], int]:
    A: dict[tuple[int, int], int] = {}
    total = 0
    for i, j in itertools.combinations(range(len(systems)), 2):
        v = smc(data[systems[i]], data[systems[j]], slots)
        A[(i, j)] = v
        total += v
    return A, total


def within_sum(labels: list[str], A: dict[tuple[int, int], int]) -> int:
    groups: dict[str, list[int]] = defaultdict(list)
    for i, lab in enumerate(labels):
        groups[lab].append(i)
    s = 0
    for members in groups.values():
        for i, j in itertools.combinations(members, 2):
            s += A[(i, j)]
    return s


def clustering_stat(systems: list[str], data: dict[str, set[str]],
                    blocks: dict[str, str], slots: list[str]) -> float:
    A, total = agreement_table(systems, data, slots)
    s = within_sum([blocks[s] for s in systems], A)
    sizes = block_sizes(blocks, systems)
    n_in, n_out = pair_counts(sizes, len(systems))
    if n_in == 0:
        return float("nan")
    return s / n_in - (total - s) / n_out


def permute_blocks(systems: list[str], blocks: dict[str, str],
                   rng: random.Random) -> dict[str, str]:
    """Shuffle block labels across systems, preserving block sizes."""
    labels = [blocks[s] for s in systems]
    rng.shuffle(labels)
    return dict(zip(systems, labels))


def clustering_test(systems: list[str], data: dict[str, set[str]],
                    blocks: dict[str, str], slots: list[str],
                    draws: int, seed: int) -> dict:
    A, total = agreement_table(systems, data, slots)
    sizes = block_sizes(blocks, systems)
    n_in, n_out = pair_counts(sizes, len(systems))
    if n_in == 0:
        return {"stat": None, "p": None, "draws": 0, "note": "no within-lineage pairs"}
    labels = [blocks[s] for s in systems]

    def stat(labs: list[str]) -> float:
        s = within_sum(labs, A)
        return s / n_in - (total - s) / n_out

    obs = stat(labels)
    rng = random.Random(seed)
    ge = 0
    null = []
    for _ in range(draws):
        perm = labels[:]
        rng.shuffle(perm)
        t = stat(perm)
        null.append(t)
        if t >= obs - 1e-12:
            ge += 1
    p = Fraction(ge + 1, draws + 1)
    null.sort()
    q = lambda frac: null[min(len(null) - 1, int(frac * (len(null) - 1)))]
    return {"stat": obs, "p": p, "draws": draws,
            "null_q025": q(0.025), "null_q500": q(0.5), "null_q975": q(0.975)}


# ----------------------------------------------------- deterministic lineage ----
def lineage_counts(systems: list[str], data: dict[str, set[str]],
                   blocks: dict[str, str], slots: list[str]) -> dict:
    by_block: dict[str, list[str]] = defaultdict(list)
    for s in systems:
        by_block[blocks[s]].append(s)
    nb = len(by_block)
    rows = {}
    for slot in slots:
        present = uni = maj = 0
        for members in by_block.values():
            k = sum(1 for s in members if slot in data[s])
            if k > 0:
                present += 1
            if k == len(members):
                uni += 1
            if k * 2 > len(members):
                maj += 1
        system_n = sum(1 for s in systems if slot in data[s])
        rows[slot] = {"system_n": system_n, "lineage_present": present,
                      "lineage_universal": uni, "lineage_majority": maj}
    return {"n_blocks": nb, "slots": rows}


# ------------------------------------------------------------ identification ----
def placements(by_block: dict[str, list[str]], carriers: set[str]) -> list[tuple[str, ...]] | None:
    """All within-block placements of the carrier set; None if too many to enumerate."""
    per_block = []
    total = 1
    for members in by_block.values():
        k = sum(1 for s in members if s in carriers)
        if k == 0:
            continue
        combos = list(itertools.combinations(sorted(members), k))
        per_block.append(combos)
        total *= len(combos)
        if total > MC_MAX_ENUM:
            return None
    return list(itertools.product(*per_block)) if per_block else []


def joint_fork_stat(data: dict[str, set[str]], carrier_set: set[str]) -> int:
    return sum(1 for s in carrier_set if data[s] & set(PARTNERS))


def fork_blocked(systems: list[str], data: dict[str, set[str]],
                 blocks: dict[str, str], draws: int, seed: int) -> dict:
    by_block: dict[str, list[str]] = defaultdict(list)
    for s in systems:
        by_block[blocks[s]].append(s)
    carriers = {s for s in systems if "S9" in data[s]}
    obs = joint_fork_stat(data, carriers)
    allp = placements(by_block, carriers)
    if allp is None:
        rng = random.Random(seed)
        sizes = [(members, sum(1 for s in members if s in carriers))
                 for members in by_block.values()]
        sizes = [(m, k) for m, k in sizes if k > 0]
        hits = 0
        for _ in range(draws):
            chosen = set()
            for members, k in sizes:
                chosen |= set(rng.sample(members, k))
            if joint_fork_stat(data, chosen) <= obs:
                hits += 1
        p = Fraction(hits + 1, draws + 1)
        return {"observed_T": obs, "p": p, "floor": Fraction(1, draws + 1),
                "placements": None, "exact": False}
    hits = sum(1 for combo in allp
               if joint_fork_stat(data, set(itertools.chain.from_iterable(combo))) <= obs)
    n = len(allp) or 1
    return {"observed_T": obs, "p": Fraction(hits, n), "floor": Fraction(1, n),
            "placements": len(allp), "exact": True}


def implication_blocked(systems: list[str], data: dict[str, set[str]],
                        blocks: dict[str, str], x: str, y: str,
                        draws: int, seed: int) -> dict:
    by_block: dict[str, list[str]] = defaultdict(list)
    for s in systems:
        by_block[blocks[s]].append(s)
    carriers = {s for s in systems if y in data[s]}
    antecedent = [s for s in systems if x in data[s]]

    def support(ys: set[str]) -> int:
        return sum(1 for s in antecedent if s in ys)

    obs = support(carriers)
    allp = placements(by_block, carriers)
    if allp is None:
        rng = random.Random(seed)
        sizes = [(m, sum(1 for s in m if s in carriers)) for m in by_block.values()]
        sizes = [(m, k) for m, k in sizes if k > 0]
        hits = 0
        for _ in range(draws):
            chosen = set()
            for members, k in sizes:
                chosen |= set(rng.sample(members, k))
            if support(chosen) >= obs:
                hits += 1
        p = Fraction(hits + 1, draws + 1)
        return {"rule": f"{x}=>{y}", "observed_support": obs, "p": p,
                "floor": Fraction(1, draws + 1), "exact": False}
    hits = sum(1 for combo in allp
               if support(set(itertools.chain.from_iterable(combo))) >= obs)
    n = len(allp) or 1
    return {"rule": f"{x}=>{y}", "observed_support": obs, "p": Fraction(hits, n),
            "floor": Fraction(1, n), "placements": len(allp), "exact": True}


# ------------------------------------------------------------- unblocked fork ----
def hyper_pmf(N: int, K: int, n: int, x: int) -> Fraction:
    if x < max(0, n - (N - K)) or x > min(n, K):
        return Fraction(0)
    return Fraction(math.comb(K, x) * math.comb(N - K, n - x), math.comb(N, n))


def fork_unblocked(systems: list[str], data: dict[str, set[str]]) -> dict:
    carriers = [s for s in systems if "S9" in data[s]]
    partners = [s for s in systems if data[s] & set(PARTNERS)]
    observed = sum(1 for s in carriers if s in partners)
    N, K, n = len(systems), len(partners), len(carriers)
    p = sum(hyper_pmf(N, K, n, x) for x in range(0, observed + 1))
    return {"observed_T": observed, "p": p, "N": N, "K": K, "n": n}


# ------------------------------------------------------------------ intervals ----
def binom_cdf(k: int, n: int, p: float) -> float:
    if k < 0:
        return 0.0
    if k >= n:
        return 1.0
    return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k + 1))


def clopper_pearson(x: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Exact binomial interval by bisection on the binomial CDF. Stdlib only."""
    if x == 0:
        lo = 0.0
    else:
        a, b = 0.0, 1.0
        for _ in range(80):
            mid = (a + b) / 2
            if binom_cdf(x - 1, n, mid) > 1 - alpha / 2:
                a = mid
            else:
                b = mid
        lo = (a + b) / 2
    if x == n:
        hi = 1.0
    else:
        a, b = 0.0, 1.0
        for _ in range(80):
            mid = (a + b) / 2
            if binom_cdf(x, n, mid) < alpha / 2:
                b = mid
            else:
                a = mid
        hi = (a + b) / 2
    return lo, hi


def prevalence(systems: list[str], data: dict[str, set[str]],
               blocks: dict[str, str], slots: list[str]) -> dict:
    out = {}
    for slot in slots:
        x = sum(1 for s in systems if slot in data[s])
        lo, hi = clopper_pearson(x, len(systems))
        by_block: dict[str, list[str]] = defaultdict(list)
        for s in systems:
            by_block[blocks[s]].append(s)
        lb = sum(1 for m in by_block.values() if any(slot in data[s] for s in m))
        lblo, lbhi = clopper_pearson(lb, len(by_block))
        out[slot] = {"system_n": x, "system_prev": x / len(systems),
                     "ci": [lo, hi], "lineage_n": lb, "n_blocks": len(by_block),
                     "lineage_prev": lb / len(by_block), "lineage_ci": [lblo, lbhi],
                     "majority_claim_ok": lo > 0.5}
    return out


# ------------------------------------------------------------------- holdout ----
def holdout(systems: list[str], data: dict[str, set[str]],
            blocks: dict[str, str], draws: int, seed: int) -> dict:
    """LOOCV Brier: prevalence baseline vs lineage-mean. Exploratory (§6.8)."""
    def brier(model: str, bl: dict[str, str]) -> float:
        total = 0.0
        for held in systems:
            others = [s for s in systems if s != held]
            for slot in SLOTS:
                base = sum(1 for s in others if slot in data[s]) / len(others)
                if model == "lineage":
                    same = [s for s in others if bl[s] == bl[held]]
                    pred = (sum(1 for s in same if slot in data[s]) / len(same)
                            if same else base)
                else:
                    pred = base
                y = 1.0 if slot in data[held] else 0.0
                total += (pred - y) ** 2
        return total / (len(systems) * len(SLOTS))

    prev = brier("prevalence", blocks)
    lin = brier("lineage", blocks)
    rng = random.Random(seed)
    null = []
    labels = [blocks[s] for s in systems]
    for _ in range(draws):
        rng.shuffle(labels)
        bl = dict(zip(systems, labels))
        null.append(brier("lineage", bl))
    null.sort()
    ge = sum(1 for v in null if v <= lin)
    return {"brier_prevalence": prev, "brier_lineage": lin,
            "delta": lin - prev,
            "null_median": null[len(null) // 2],
            "p_shuffle": Fraction(ge + 1, len(null) + 1), "draws": draws}


# ------------------------------------------------------------------- drivers ----
def run_variant(systems, data, blocks, variant, label, draws, seed) -> dict:
    det = lineage_counts(systems, data, blocks, SLOTS)
    clus = clustering_test(systems, data, blocks, SLOTS, draws, seed)
    part = clustering_test(systems, data, blocks, PARTNERS, draws, seed)
    epist = clustering_test(systems, data, blocks, ["S6"], draws, seed)
    qs = bh_q([part["p"], epist["p"]])
    qby = by_q([part["p"], epist["p"]])
    fb = fork_blocked(systems, data, blocks, draws, seed)
    fu = fork_unblocked(systems, data)
    imp = [implication_blocked(systems, data, blocks, x, y, draws, seed)
           for x, y in IMPLICATIONS]
    prev = prevalence(systems, data, blocks, SLOTS)
    stem_universal = [s for s in STEM
                      if det["slots"][s]["lineage_universal"] == det["n_blocks"]]
    return {
        "variant": variant, "matrix": label, "n_blocks": det["n_blocks"],
        "deterministic": det,
        "stem_universal": stem_universal,
        "s9_lineages": det["slots"]["S9"]["lineage_present"],
        "clustering_full": clus,
        "clustering_partners": part,
        "clustering_epistolary": epist,
        "bh_partner_epist": [qs[0], qs[1]],
        "by_partner_epist": [qby[0], qby[1]],
        "fork_unblocked": fu,
        "fork_blocked": fb,
        "implications_blocked": imp,
        "prevalence": prev,
    }


def real_run(draws: int, seed: int) -> dict:
    assert sha256(SLOT_MATRIX) == SHA_SLOT, "slot_matrix.csv hash mismatch — stop"
    assert sha256(REQS) == SHA_REQ, "requisites.csv hash mismatch — stop"
    systems, data = load_matrix(SLOT_MATRIX)
    mand = mandatory_matrix(systems, REQS)
    if MANDATORY.exists():
        fresh = {s: {x for x in SLOTS if x in mand[s]} for s in systems}
        prev = load_matrix(MANDATORY)[1]
        assert fresh == prev, "mandatory_only.csv is out of date — regenerate"
    out = {"variants": {}, "inputs": {"slot_sha": SHA_SLOT, "req_sha": SHA_REQ}}
    for variant in VARIANTS:
        blocks = load_blocks(BLOCKS, variant)
        assert set(blocks) == set(systems), "lineage table does not cover the matrix"
        out["variants"][variant] = {
            "all": run_variant(systems, data, blocks, variant, "all", draws, seed),
            "mandatory": run_variant(systems, mand, blocks, variant, "mandatory", draws, seed),
        }
    out["holdout"] = holdout(systems, data, load_blocks(BLOCKS, "base"), 1000, seed)
    return out


# ------------------------------------------------------------------ self-test ----
def make_fixture(strong: bool) -> tuple[list[str], dict[str, set[str]], dict[str, str]]:
    systems = [f"X{i:02d}" for i in range(25)]
    blocks: dict[str, str] = {}
    for i in range(25):
        blocks[systems[i]] = "blk%d" % (i // 3) if i < 12 else f"single{i}"
    data: dict[str, set[str]] = {}
    if strong:
        # Four disjoint 3-4 slot "cluster signatures": members are identical,
        # clusters nearly disjoint, so within >> between.
        sigs = [set(SLOTS[c::4]) for c in range(4)]
        for i, s in enumerate(systems):
            if i < 12:
                data[s] = set(sigs[i // 3])
            else:
                data[s] = {SLOTS[(i + j) % 14] for j in range(5)}
    else:
        for i, s in enumerate(systems):
            data[s] = {slot for j, slot in enumerate(SLOTS) if (i * 7 + j) % 3 == 0}
    return systems, data, blocks


def self_test() -> int:
    systems, data, blocks = make_fixture(True)
    sizes = block_sizes(blocks, systems)
    assert sizes == [3, 3, 3, 3] + [1] * 13, sizes
    within, between = pair_counts(sizes, len(systems))
    assert within == 12 and between == 288, (within, between)

    # Deterministic counts on a hand-computed 2-system, 1-block fixture.
    det2 = lineage_counts(["A", "B"], {"A": {"S1", "S2"}, "B": {"S1"}}, {"A": "z", "B": "z"}, ["S1", "S2"])
    assert det2["n_blocks"] == 1
    assert det2["slots"]["S1"] == {"system_n": 2, "lineage_present": 1,
                                   "lineage_universal": 1, "lineage_majority": 1}
    assert det2["slots"]["S2"]["lineage_universal"] == 0
    assert det2["slots"]["S2"]["lineage_majority"] == 0

    det = lineage_counts(systems, data, blocks, SLOTS)
    assert det["n_blocks"] == 17, det["n_blocks"]
    for slot in SLOTS:
        assert det["slots"][slot]["lineage_universal"] <= det["slots"][slot]["lineage_present"]

    clus = clustering_test(systems, data, blocks, SLOTS, 2000, SEED)
    assert clus["p"] < Fraction(1, 20), f"strong fixture not detected: {clus}"
    assert 0 <= clus["p"] <= 1

    _, rand_data, _ = make_fixture(False)
    rand = clustering_test(systems, rand_data, blocks, SLOTS, 2000, SEED)
    assert rand["p"] > Fraction(1, 100), f"random fixture looks clustered: {rand}"

    # Clopper–Pearson sanity: endpoints, bracketing, monotonicity.
    assert clopper_pearson(0, 25)[0] == 0.0
    assert clopper_pearson(25, 25)[1] == 1.0
    lo, hi = clopper_pearson(12, 25)
    assert lo < 12 / 25 < hi, (lo, hi)
    assert 0.27 < lo < 0.29 and 0.68 < hi < 0.70, (lo, hi)

    # Fork machinery on a hand-computed fixture: S9 in 2 systems, neither a partner.
    sys3 = ["A", "B", "C"]
    d3 = {"A": {"S9"}, "B": {"S9"}, "C": {"S4"}}
    fu = fork_unblocked(sys3, d3)
    # P(T=0) = C(1,0)*C(2,2)/C(3,2) = 1/3 — the "never" is unsurprising at this n.
    assert fu["observed_T"] == 0 and fu["p"] == Fraction(1, 3), fu

    # Blocked machinery: singleton blocks cannot move the carriers -> floor 1.
    b3 = {"A": "a", "B": "b", "C": "c"}
    fb = fork_blocked(sys3, d3, b3, 100, SEED)
    assert fb["exact"] and fb["floor"] == 1 and fb["p"] == 1, fb

    # A documented row without a citation must fail validation.
    bad = Path("/tmp/_b3_bad_blocks.csv")
    bad.write_text("system,narrow,base,broad,confidence,basis\nA,a,a,a,documented,\n"
                   + "".join(f"X{i:02d},s{i},s{i},s{i},unresolved,none\n" for i in range(24)),
                   encoding="utf-8")
    try:
        load_blocks(bad, "base")
    except AssertionError:
        pass
    else:
        raise AssertionError("citation check did not fire")
    bad.unlink()

    # Mandatory matrix builder on a tiny fixture.
    tiny = Path("/tmp/_b3_reqs.csv")
    tiny.write_text(
        "system,standard,clause,local_term,gloss_en,slot,obligation,genre,note\n"
        "A,x,1,t,g,S1-identity,mandatory,all,\n"
        "A,x,2,t,g,S12-authentication,optional,all,\n"
        "A,x,3,t,g,structural,mandatory,all,\n"
        "B,x,1,t,g,S3-origin,mandatory,all,\n", encoding="utf-8")
    m = mandatory_matrix(["A", "B"], tiny)
    assert m == {"A": {"S1"}, "B": {"S3"}}, m
    tiny.unlink()

    # Holdout and prevalence run end to end.
    h = holdout(systems, data, blocks, 50, SEED)
    assert math.isfinite(h["brier_prevalence"]) and math.isfinite(h["brier_lineage"])
    p = prevalence(systems, data, blocks, SLOTS)
    x1 = sum(1 for s in systems if "S1" in data[s])
    assert p["S1"]["system_n"] == x1
    assert p["S1"]["majority_claim_ok"] == (p["S1"]["ci"][0] > 0.5)
    assert all(p[s]["ci"][0] <= p[s]["system_prev"] <= p[s]["ci"][1] for s in SLOTS)

    print("self-test OK: block algebra, deterministic counts, clustering (strong vs random),")
    print("             Clopper–Pearson, fork machinery, floor behaviour, citation gate,")
    print("             mandatory-matrix rule, holdout, prevalence.")
    return 0


# -------------------------------------------------------------------- report ----
def print_report(res: dict) -> None:
    print("\n=== B3 lineage-restricted re-derivation ===")
    for variant in VARIANTS:
        for matrix in ("all", "mandatory"):
            r = res["variants"][variant][matrix]
            print(f"\n[{variant}/{matrix}] blocks={r['n_blocks']} "
                  f"stem-universal={len(r['stem_universal'])}/6 S9-lineages={r['s9_lineages']}")
            fc = r["clustering_full"]
            print(f"  clustering full: T={rnd(fc['stat'])} p={rnd(fc['p'])}")
            print(f"  partner q={rnd(r['bh_partner_epist'][0])} "
                  f"epistolary q={rnd(r['bh_partner_epist'][1])}")
            fb = r["fork_blocked"]
            print(f"  fork blocked: p={rnd(fb['p'])} floor={rnd(fb['floor'])} "
                  f"exact={fb['exact']}")
            print(f"  fork unblocked: p={rnd(r['fork_unblocked']['p'])}")
    h = res["holdout"]
    print(f"\n[holdout] Brier prevalence={h['brier_prevalence']:.4f} "
          f"lineage={h['brier_lineage']:.4f} delta={h['delta']:+.4f} "
          f"p_shuffle={rnd(h['p_shuffle'])}")


def serialise(obj):
    if isinstance(obj, Fraction):
        return {"num": obj.numerator, "den": obj.denominator, "float": float(obj)}
    if isinstance(obj, set):
        return sorted(obj)
    raise TypeError(type(obj))


def freeze_inputs() -> int:
    """Write the frozen derived inputs used by the registered run. No statistic."""
    assert sha256(REQS) == SHA_REQ, "requisites.csv hash mismatch — stop"
    systems = sorted(load_blocks(BLOCKS, "base"))
    assert len(systems) == 25
    mand = mandatory_matrix(systems, REQS)
    write_mandatory(systems, mand, MANDATORY)
    sums = {s: len(mand[s]) for s in systems}
    print(f"wrote {MANDATORY} ({len(systems)} rows)")
    print("mandatory-only row sums:",
          " ".join(f"{s}={sums[s]}" for s in systems))
    empty = [s for s in systems if sums[s] == 0]
    print(f"systems with no mandatory cell: {empty or 'none'}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--freeze-inputs", action="store_true",
                    help="write mandatory_only.csv from requisites; computes nothing")
    ap.add_argument("--draws", type=int, default=MC_DRAWS)
    ap.add_argument("--seed", type=int, default=SEED)
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.freeze_inputs:
        return freeze_inputs()
    res = real_run(args.draws, args.seed)
    print_report(res)
    out = HERE / "results.json"
    out.write_text(json.dumps(res, indent=1, default=serialise), encoding="utf-8")
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
