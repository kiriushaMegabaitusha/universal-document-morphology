#!/usr/bin/env python3
"""Shared analysis for the finding-5 comprehension test (machine and human arms).

Everything the pre-registration names lives here, so both arms are analysed by
exactly the same code path:

  * accuracy tables by register / language / reader
  * exact sign-flip permutation test on item-level paired differences (PRIMARY)
  * logistic regression with item fixed effects, fitted by IRLS, with Wald
    inference and the average marginal effect in percentage points
  * equivalence test (TOST) against the pre-registered 5 pp margin
  * bootstrap CIs (percentile, seeded), reader-clustered for the model estimate
  * Benjamini-Hochberg FDR for the secondary family

Only numpy + stdlib. Every random draw is seeded; the functions are pure.
"""
import json
import math
from collections import defaultdict

import numpy as np

SESOI_PP = 0.05      # pre-registered smallest effect size of interest
BOOT = 20000         # bootstrap resamples
PERM_SEED = 20261006


# ---------------------------------------------------------------- loading ----
def load_machine(path):
    """Read machine_arm JSONL -> observations. One row per (model, document, item)."""
    obs = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            r = json.loads(line)
            if r.get("correct") is None:      # unparsable answer: excluded, counted separately
                continue
            obs.append({
                "reader": r["model"], "item": r["item"], "document": r["document"],
                "register": r["register"], "lang": r["lang"], "kind": r["kind"],
                "correct": int(r["correct"]),
                "rt_ms": r.get("latency_ms"), "extra": r,
            })
    return obs


def load_human(exports):
    """Read participant exports (dicts) -> observations."""
    obs = []
    for part in exports:
        pid = part["participant"]
        for tr in part["trials"]:
            if tr.get("response") in (None, "", "skip"):
                continue
            obs.append({
                "reader": pid, "item": tr["item"], "document": tr["document"],
                "register": tr["register"], "lang": tr["lang"], "kind": tr["kind"],
                "correct": int(tr["correct"]),
                "rt_ms": tr.get("rt_ms"), "extra": tr,
            })
    return obs


# ------------------------------------------------------------- descriptives --
def accuracy(obs, by):
    """accuracy by one or more grouping keys"""
    if isinstance(by, str):
        by = [by]
    out = {}
    for o in obs:
        out.setdefault(tuple(o[k] for k in by), []).append(o["correct"])
    return {k: (sum(v), len(v), sum(v) / len(v)) for k, v in sorted(out.items())}


def item_differences(obs, register_plain="plain", register_formal="formal"):
    """Paired per-item difference in proportion correct: plain - formal.

    Aggregates over readers within an item, which is the unit the pre-registration
    names (the item is the thing whose wording was manipulated). This also handles
    the human arm's incomplete design, where the two registers of an item are read
    by different participants."""
    per = defaultdict(lambda: defaultdict(list))
    for o in obs:
        per[o["item"]][o["register"]].append(o["correct"])
    diffs, items = [], []
    for item, d in sorted(per.items()):
        if register_plain in d and register_formal in d:
            p = sum(d[register_plain]) / len(d[register_plain])
            f = sum(d[register_formal]) / len(d[register_formal])
            diffs.append(p - f)
            items.append(item)
    return items, np.array(diffs, dtype=float)


# ------------------------------------------------------------------ tests ----
def signflip_test(diffs, two_sided=True, max_exact=16):
    """Exact sign-flip randomization test on the mean of paired differences.

    Under H0 the sign of each item's difference is exchangeable, so all 2^n sign
    patterns are equally likely; for n <= max_exact we enumerate them exactly and
    report the exact p-value, otherwise we sample (seeded)."""
    diffs = np.asarray(diffs, dtype=float)
    n = len(diffs)
    if n == 0:
        return {"n": 0, "mean": float("nan"), "p": float("nan"), "exact": True}
    obs = float(diffs.mean())
    if n <= max_exact:
        tot = 1 << n
        signs = ((np.arange(tot)[:, None] >> np.arange(n)[None, :]) & 1) * 2 - 1
        means = (signs * diffs).mean(axis=1)
        p = float(np.mean(np.abs(means) >= abs(obs) - 1e-12)) if two_sided else float(np.mean(means >= obs - 1e-12))
        exact = True
    else:
        rng = np.random.default_rng(PERM_SEED)
        means = (rng.choice([-1.0, 1.0], size=(BOOT, n)) * diffs).mean(axis=1)
        p = float(np.mean(np.abs(means) >= abs(obs))) if two_sided else float(np.mean(means >= obs))
        exact = False
    return {"n": n, "mean": obs, "p": p, "exact": exact}


def bootstrap_ci(diffs, level=0.95, n_boot=BOOT, seed=PERM_SEED):
    diffs = np.asarray(diffs, dtype=float)
    if len(diffs) == 0:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(diffs), size=(n_boot, len(diffs)))
    means = diffs[idx].mean(axis=1)
    lo, hi = np.percentile(means, [(1 - level) / 2 * 100, (1 + level) / 2 * 100])
    return float(lo), float(hi)


def tost_equivalence(diffs, margin=SESOI_PP, level=0.05, n_boot=BOOT, seed=PERM_SEED):
    """Two one-sided tests on the mean difference against +/- margin (percentile bootstrap)."""
    diffs = np.asarray(diffs, dtype=float)
    if len(diffs) == 0:
        return {"equivalent": False, "p_lower": float("nan"), "p_upper": float("nan")}
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(diffs), size=(n_boot, len(diffs)))
    dist = diffs[idx].mean(axis=1) - diffs.mean()       # bootstrap distribution of the mean's error
    p_lower = float(np.mean(dist <= -margin + diffs.mean()))   # H0: mean <= -margin
    p_upper = float(np.mean(dist >= margin + diffs.mean()))    # H0: mean >= +margin
    return {"equivalent": bool(max(p_lower, p_upper) < level),
            "p_lower": p_lower, "p_upper": p_upper}


# ------------------------------------------------------- logistic + item FE --
def logit_fe(obs, interact=None, interact_name="x"):
    """Fit logit P(correct) = a_item + b*plain [+ g*(plain x interact)] by IRLS.

    Always includes item fixed effects (one dummy per item minus a reference), so
    the register contrast is estimated within items. `interact` is an optional
    callable o -> 0/1 producing an interaction column (used for the pre-specified
    secondary tests: language moderation and item-type moderation).

    Returns coefficients with Wald inference and the average marginal effect (pp)
    of the register contrast.
    """
    items = sorted({o["item"] for o in obs})
    readers = sorted({o["reader"] for o in obs})
    if len(items) < 2 or len(readers) < 1:
        return None
    cols, names = [], []
    for it in items[:-1]:                    # drop one item as the reference level
        cols.append([1.0 if o["item"] == it else 0.0 for o in obs])
        names.append("item:" + it)
    cols.append([1.0 if o["register"] == "plain" else 0.0 for o in obs])
    names.append("register_plain")
    if interact is not None:
        cols.append([(1.0 if o["register"] == "plain" else 0.0) * float(interact(o)) for o in obs])
        names.append("register_plain:" + interact_name)
    y = np.array([o["correct"] for o in obs], dtype=float)
    X = np.column_stack(cols)
    beta = np.zeros(X.shape[1])
    W = np.full(len(y), 0.25)
    for _ in range(200):                      # IRLS
        eta = X @ beta
        p = 1.0 / (1.0 + np.exp(-np.clip(eta, -30, 30)))
        W = np.clip(p * (1 - p), 1e-9, None)
        z = eta + (y - p) / W
        WX = X * W[:, None]
        try:
            beta_new = np.linalg.solve(X.T @ WX + 1e-8 * np.eye(X.shape[1]), X.T @ (W * z))
        except np.linalg.LinAlgError:
            return None
        if np.max(np.abs(beta_new - beta)) < 1e-10:
            beta = beta_new
            break
        beta = beta_new
    WX = X * W[:, None]
    try:
        cov = np.linalg.inv(X.T @ WX + 1e-8 * np.eye(X.shape[1]))
    except np.linalg.LinAlgError:
        cov = np.full((X.shape[1], X.shape[1]), np.nan)
    se = np.sqrt(np.clip(np.diag(cov), 0, None))
    zz = beta / np.where(se > 0, se, np.nan)
    pv = 2 * (1 - 0.5 * (1 + np.vectorize(math.erf)(np.abs(zz) / math.sqrt(2))))
    coef = {}
    for i, nm in enumerate(names):
        if nm.startswith("item:"):
            continue
        coef[nm] = {"beta": float(beta[i]), "se": float(se[i]), "z": float(zz[i]),
                    "p": float(pv[i]), "or": float(math.exp(beta[i]))}
    j = names.index("register_plain")
    Xp, Xf = X.copy(), X.copy()
    Xp[:, j] = 1.0
    Xf[:, j] = 0.0
    ame = float((1.0 / (1.0 + np.exp(-(Xp @ beta))) - 1.0 / (1.0 + np.exp(-(Xf @ beta)))).mean())
    return {"coef": coef, "ame_pp": ame, "n_obs": len(obs), "n_items": len(items),
            "n_readers": len(readers)}


def reader_cluster_boot(obs, n_boot=2000, seed=PERM_SEED):
    """Bootstrap the register coefficient by resampling READERS (the independent unit)."""
    readers = sorted({o["reader"] for o in obs})
    if len(readers) < 2:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    bs = []
    for _ in range(n_boot):
        pick = set(rng.choice(readers, size=len(readers), replace=True))
        sub = [o for o in obs if o["reader"] in pick]
        r = logit_fe(sub)
        if r:
            bs.append(r["coef"]["register_plain"]["beta"])
    if not bs:
        return (float("nan"), float("nan"))
    lo, hi = np.percentile(bs, [2.5, 97.5])
    return float(lo), float(hi)


def bh_fdr(pvals, alpha=0.05):
    """Benjamini-Hochberg. Returns [(p, threshold, reject)] in the input order."""
    m = len(pvals)
    res = [(float(p), 1.0, False) for p in pvals]
    order = sorted(range(m), key=lambda i: pvals[i])
    prev = 1.0
    for rank, i in enumerate(reversed(order), start=1):
        k = m - rank + 1
        thr = min(1.0, pvals[i] * m / k)
        prev = min(prev, thr)
        res[i] = (float(pvals[i]), float(prev), bool(pvals[i] <= prev and pvals[i] <= alpha))
    return res


# ------------------------------------------------------------------ report ---
def arm_report(obs, arm_label):
    """All pre-registered numbers for one arm, as a dict (consumed by analyze.py)."""
    items, diffs = item_differences(obs)
    fe = logit_fe(obs)
    fe_lang = logit_fe(obs, interact=lambda o: 1.0 if o["lang"] == "uk" else 0.0, interact_name="uk")
    fe_kind = logit_fe(obs, interact=lambda o: 1.0 if o["kind"] == "inference" else 0.0,
                       interact_name="inference")
    sec = []
    if fe_lang and "register_plain:uk" in fe_lang["coef"]:
        sec.append(("register x language (uk)", fe_lang["coef"]["register_plain:uk"]["p"]))
    if fe_kind and "register_plain:inference" in fe_kind["coef"]:
        sec.append(("register x item type (inference)", fe_kind["coef"]["register_plain:inference"]["p"]))
    lo, hi = bootstrap_ci(diffs)
    return {
        "arm": arm_label,
        "n_obs": len(obs),
        "n_items": len(items),
        "n_readers": len({o["reader"] for o in obs}),
        "items": items,
        "item_diffs": [float(x) for x in diffs],
        "accuracy_by_register": {"|".join(k): v for k, v in accuracy(obs, ["register"]).items()},
        "accuracy_by_lang_register": {"|".join(k): v for k, v in accuracy(obs, ["lang", "register"]).items()},
        "accuracy_by_kind_register": {"|".join(k): v for k, v in accuracy(obs, ["kind", "register"]).items()},
        "permutation": signflip_test(diffs),
        "bootstrap_ci": [lo, hi],
        "equivalence": tost_equivalence(diffs),
        "logit_fe": fe,
        "secondary_pvalues": sec,
        "secondary_bh": bh_fdr([p for _, p in sec]) if sec else [],
        "reader_cluster_boot_beta": reader_cluster_boot(obs),
    }
