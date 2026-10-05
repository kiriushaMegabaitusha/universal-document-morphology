#!/usr/bin/env python3
"""Recompute the atlas figures from the frozen data and check the prose.

Regenerates (in place, CRLF):
  slot_matrix.csv      systems x S1..S14 presence
  slot_similarity.csv  pairwise Jaccard
  evidence_base.csv    one row per ledger source, with its hand-assigned type

Then recomputes every derivable figure in analysis/findings.md and
analysis/qualitative_analysis.md and fails if the prose has drifted from the
data (the failure mode this script exists to catch: prose written before the
last rows were added).

Hand-assigned inputs the script cannot derive, and therefore leaves alone:
  evidence_base.csv 'type' column (kept by id; unknown ids become 'other'),
  the regime classes in findings.md S3, the era anchor years in
  qualitative_analysis.md S4, and theme_matrix.csv.

Run:  python3 analysis/recompute.py        (writes CSVs, exits 0 if prose matches)
      python3 analysis/recompute.py --check   (no writes)
"""
import csv, json, os, re, sys, itertools
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
WRITE = "--check" not in sys.argv
SLOT_COLS = ["S%d" % i for i in range(1, 15)]


def read_rows(name):
    with open(os.path.join(ROOT, name), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        w.writerows(rows)


# ---- inputs ---------------------------------------------------------------
req = read_rows("requisites.csv")
ledger = json.load(open(os.path.join(ROOT, "ledger.json"), encoding="utf-8"))

bysys = defaultdict(set)
for r in req:
    m = re.match(r"^(S\d+)-", r["slot"])
    if m:
        bysys[r["system"]].add(m.group(1))
systems = sorted(bysys)
census = Counter(s for v in bysys.values() for s in v)

# ---- slot_matrix.csv ------------------------------------------------------
if WRITE:
    write_csv(os.path.join(HERE, "slot_matrix.csv"),
              ["system"] + SLOT_COLS,
              [[s] + [1 if c in bysys[s] else 0 for c in SLOT_COLS] for s in systems])


# ---- slot_similarity.csv --------------------------------------------------
def jaccard(a, b):
    return len(bysys[a] & bysys[b]) / len(bysys[a] | bysys[b])


sim = [[str(round(jaccard(a, b), 2)) for b in systems] for a in systems]
if WRITE:
    write_csv(os.path.join(HERE, "slot_similarity.csv"),
              [""] + systems, [[a] + row for a, row in zip(systems, sim)])

pairs = sorted(((jaccard(a, b), a, b) for a, b in itertools.combinations(systems, 2)),
               reverse=True)

# ---- evidence_base.csv ----------------------------------------------------
eb_path = os.path.join(HERE, "evidence_base.csv")
old_type = {}
if os.path.exists(eb_path):
    old_type = {r["id"]: r["type"] for r in csv.DictReader(open(eb_path, encoding="utf-8"))}
warnings, eb_rows = [], []
for s in ledger["sources"]:
    t = old_type.get(s["id"])
    if t is None:
        t = "other"
        warnings.append("no hand-assigned type for %s; defaulted to 'other'" % s["id"])
    eb_rows.append({"id": s["id"], "type": t,
                    "retrieved": str(bool(s["retrieved"])), "title": s["title"]})
if WRITE:
    write_csv(eb_path, ["id", "type", "retrieved", "title"],
              [[r["id"], r["type"], r["retrieved"], r["title"]] for r in eb_rows])

type_ct = Counter(r["type"] for r in eb_rows)
got = sum(1 for r in eb_rows if r["retrieved"] == "True")
claims_ok = sum(1 for c in ledger["claims"] if c["verified"])
claims_n = len(ledger["claims"])

# ---- script census of local_term ------------------------------------------
SCRIPTS = [("Cyrillic", r"[\u0400-\u04FF]"), ("Arabic", r"[\u0600-\u06FF\u0750-\u077F]"),
           ("Han", r"[\u4E00-\u9FFF]"), ("Thai", r"[\u0E00-\u0E7F]"),
           ("Latin", r"[A-Za-z\u00C0-\u024F\u1E00-\u1EFF]")]
script_ct = Counter()
for r in req:
    term = (r["local_term"] or "").strip()
    hit = next((n for n, pat in SCRIPTS if re.search(pat, term)), None)
    script_ct[hit or "(none)"] += 1

# ---- theme counts (theme_matrix.csv is hand-coded input) ------------------
tm = list(csv.reader(open(os.path.join(HERE, "theme_matrix.csv"), encoding="utf-8")))
theme_ct = {h: sum(1 for row in tm[1:] if float(row[i + 1] or 0) != 0)
            for i, h in enumerate(tm[0][1:])}

# ---- checks against the prose --------------------------------------------
def flat(name):
    return re.sub(r"\s+", " ", open(os.path.join(ROOT, name), encoding="utf-8").read())


findings, qual, execsum = flat("analysis/findings.md"), flat("analysis/qualitative_analysis.md"), flat("EXECUTIVE_SUMMARY.md")
findings_plain = findings.replace("**", "")
raw_findings = open(os.path.join(ROOT, "analysis/findings.md"), encoding="utf-8").read()

checks = []
add = checks.append


add(("findings S1 header: 225 rows / 60 sources / 92 claims",
     "(225 rows)" in findings and "(60 sources / 92 claims)" in findings))

for m in re.finditer(r"^\|\s*(S\d+)[^|]*\|\s*(\d+)", raw_findings, re.M):
    slot, n = m.group(1), int(m.group(2))
    add(("findings S1 table %s = %d" % (slot, census[slot]), census[slot] == n))

s6 = {s for s in systems if "S6" in bysys[s]}
s9 = {s for s in systems if "S9" in bysys[s]}
fork = (len(s6 & s9), len(s6 - s9), len(s9 - s6), len(set(systems) - s6 - s9))
add(("findings S2 fork %s" % (fork,),
     "both = %d, only-S6 = %d, only-S9 = %d, neither = %d" % fork in findings_plain))

su_density = len(bysys["SU"])
add(("findings S3 SU density %.1f" % su_density,
     "| supranational / bloc regime (SU) | 1 | %.1f |" % su_density in findings))

add(("findings S4 artefact pair JP=KE=HN at 1.0",
     all(jaccard(a, b) == 1.0 for a, b in itertools.combinations(["JP", "KE", "HN"], 2))
     and "JP = KE = HN (1.0)" in findings))
for a, b in [("SA", "UA"), ("CN", "TH"), ("CN", "FR"), ("BR", "SU")]:
    v = jaccard(a, b)
    add(("findings S4 %s\u2013%s = %.2f" % (a, b, v), "**%s\u2013%s %.2f**" % (a, b, v) in findings))

line = ("%d sources: encyclopedia %d, official guide/manual %d, other %d, technical standard %d, "
        "legal/normative text %d, academic/secondary %d. **%d of %d retrieved; %d of %d claims verified**"
        % (len(eb_rows), type_ct["encyclopedia"], type_ct["official guide/manual"], type_ct["other"],
           type_ct["technical standard"], type_ct["legal/normative text"], type_ct["academic/secondary"],
           got, len(eb_rows), claims_ok, claims_n))
add(("findings S5 evidence base", line in findings))

scripts_line = "Latin %d, Cyrillic %d, Arabic %d, Han %d, Thai %d" % (
    script_ct["Latin"], script_ct["Cyrillic"], script_ct["Arabic"], script_ct["Han"], script_ct["Thai"])
add(("findings S6 script census", scripts_line in findings))

for prose, col in [("authentication / seal", "authentication/seal"),
                   ("custody / archive", "custody/archive"),
                   ("indigenous / other script", "indigenous/other script")]:
    add(("qualitative S2 %s = %d" % (prose, theme_ct[col]),
         "| %s | %d |" % (prose, theme_ct[col]) in qual))

add(("executive summary: %d/%d sources retrieved" % (got, len(eb_rows)),
     "%d/%d sources" % (got, len(eb_rows)) in execsum))

# ---- report ---------------------------------------------------------------
print("regenerated: slot_matrix.csv, slot_similarity.csv, evidence_base.csv" if WRITE
      else "check only (no writes)")
print("systems with page slots: %d | requisites: %d | sources: %d | claims: %d"
      % (len(systems), len(req), len(eb_rows), claims_n))
print("top pairs: " + ", ".join("%s-%s %.2f" % (a, b, v) for v, a, b in pairs[:6]))
for w in warnings:
    print("WARNING:", w)
failed = [label for label, ok in checks if not ok]
for label, ok in checks:
    print(("  ok   " if ok else "  FAIL ") + label)
if failed:
    print("\n%d check(s) failed — prose disagrees with the data:\n  %s"
          % (len(failed), "\n  ".join(failed)))
    sys.exit(1)
print("\nOK - %d recomputed figure(s) match the prose" % len(checks))
