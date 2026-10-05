#!/usr/bin/env python3
"""Claim + data gate for the universal document morphology atlas.

Validates:
  1. ledger.json schema and source resolution (every claim -> existing source ids)
  2. requisites.csv structure and controlled slot vocabulary
  3. internal consistency: the UA mandatory requisite set in the CSV equals the
     set asserted by ledger claim C02
Run:  python3 check_claims.py [--online]
"""
import csv, json, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))

# controlled vocabulary of canonical morphological slots
SLOTS = {
    "S1-identity", "S2-identifier", "S3-origin", "S4-authority-mark",
    "S5-temporal", "S6-destination", "S7-reference", "S8-subject",
    "S9-setting", "S10-body", "S11-dispositif", "S12-authentication",
    "S13-annex", "S14-trace", "structural", "mixed",
    # cross-cutting dimensions and non-slot categories (see diversity.md)
    "rank-modifier", "infrastructure", "meta-structure", "access",
}

errors, warnings = [], []

# ---- ledger ----
with open(os.path.join(HERE, "ledger.json"), encoding="utf-8") as f:
    ledger = json.load(f)
src_ids = {s["id"] for s in ledger["sources"]}
for s in ledger["sources"]:
    for k in ("id", "title", "url", "retrieved"):
        if k not in s:
            errors.append(f"source {s.get('id')!r} missing field {k!r}")
claim_ids = set()
for c in ledger["claims"]:
    for k in ("id", "text", "sources", "verified"):
        if k not in c:
            errors.append(f"claim {c.get('id')!r} missing field {k!r}")
    if c["id"] in claim_ids:
        errors.append(f"duplicate claim id {c['id']!r}")
    claim_ids.add(c["id"])
    if not c["sources"]:
        errors.append(f"claim {c['id']!r} has no sources")
    for sid in c["sources"]:
        if sid not in src_ids:
            errors.append(f"claim {c['id']!r} references unknown source {sid!r}")
    if not c["verified"] and "note" not in c:
        warnings.append(f"claim {c['id']!r} unverified without a note explaining why")

# ---- requisites.csv ----
raw = list(csv.reader(open(os.path.join(HERE, "requisites.csv"), encoding="utf-8")))
for i, line in enumerate(raw, 1):
    if len(line) != 9:
        errors.append(f"requisites.csv line {i}: {len(line)} fields, expected 9")
rows = list(csv.DictReader(open(os.path.join(HERE, "requisites.csv"), encoding="utf-8")))
required_cols = {"system", "standard", "clause", "local_term", "gloss_en",
                 "slot", "obligation", "genre", "note"}
missing = required_cols - set(rows[0].keys())
if missing:
    errors.append(f"requisites.csv missing columns {sorted(missing)}")
for i, r in enumerate(rows, 2):
    if r["slot"] not in SLOTS:
        errors.append(f"requisites.csv line {i}: slot {r['slot']!r} outside vocabulary")
    if not r["system"] or not r["standard"] or not r["gloss_en"]:
        errors.append(f"requisites.csv line {i}: empty required cell")

# ---- cross-check UA mandatory set against claim C02 ----
c02 = next((c for c in ledger["claims"] if c["id"] == "C02"), None)
asserted = set()
if c02:
    import re
    asserted = set(re.findall(r"\b(\d{2})\b", c02["text"]))  # 04,09,...
csv_mand = {r["clause"].split("(")[-1].rstrip(")") for r in rows
            if r["system"] == "UA" and r["obligation"] == "mandatory"
            and "(" in r["clause"]}
if asserted and csv_mand and asserted != csv_mand:
    errors.append(f"UA mandatory set mismatch: ledger says {sorted(asserted)}, "
                  f"csv says {sorted(csv_mand)}")

# ---- optional online URL check ----
if "--online" in sys.argv:
    import urllib.request
    for s in ledger["sources"]:
        if not s["retrieved"]:
            continue
        try:
            req = urllib.request.Request(s["url"], method="HEAD",
                                         headers={"User-Agent": "Mozilla/5.0"})
            code = urllib.request.urlopen(req, timeout=20).status
            print(f"  online {s['id']}: {code}")
        except urllib.error.HTTPError as e:
            if e.code in (403, 405):
                print(f"  online {s['id']}: {e.code} (bot-block on HEAD; URL is canonical)")
            else:
                warnings.append(f"online check failed for {s['id']}: {e}")
        except Exception as e:
            warnings.append(f"online check failed for {s['id']}: {e}")

# ---- markdown cross-references in prose files ----
import re, glob
known_claim = claim_ids
known_src = src_ids
for md in (glob.glob(os.path.join(HERE, "*.md"))
           + glob.glob(os.path.join(HERE, "cases", "*.md"))
           + glob.glob(os.path.join(HERE, "analysis", "*.md"))):
    text = open(md, encoding="utf-8").read()
    rel = os.path.relpath(md, HERE)
    for cid in set(re.findall(r"\bC\d{2}\b", text)):
        if cid not in known_claim:
            errors.append(f"{rel}: references claim {cid} not in ledger")
    for sid in set(re.findall(r"\bS-[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\b", text)):
        if sid not in known_src:
            errors.append(f"{rel}: references source {sid} not in ledger")

# ---- report ----
sys_on = sorted({r["system"] for r in rows})
print(f"ledger: {len(ledger['sources'])} sources, {len(ledger['claims'])} claims "
      f"({sum(1 for c in ledger['claims'] if c['verified'])} verified, "
      f"{sum(1 for c in ledger['claims'] if not c['verified'])} provisional)")
print(f"requisites.csv: {len(rows)} rows across systems {sys_on}")
if warnings:
    print("\nWARNINGS:")
    for w in warnings:
        print("  -", w)
if errors:
    print("\nERRORS:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("\nOK - all checks passed")
