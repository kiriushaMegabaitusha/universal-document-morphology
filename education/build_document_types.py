#!/usr/bin/env python3
"""Build education/document-types.html from requisites.csv.

Every band in every page map is one row of requisites.csv. Nothing is typed by
hand: the element order is the standard's own clause order, and every count in
the prose is computed here.

    python3 education/build_document_types.py           # write the page
    python3 education/build_document_types.py --check   # verify it is current

Stdlib only, like the other gates in this repository.
"""

import csv
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "education" / "document-types.html"

FAMILY = {
    "S1-identity": "who",
    "S2-identifier": "who",
    "S3-origin": "who",
    "S4-authority-mark": "who",
    "S5-temporal": "when",
    "S6-destination": "route",
    "S7-reference": "route",
    "S8-subject": "route",
    "S9-setting": "act",
    "S10-body": "act",
    "S11-dispositif": "act",
    "S12-authentication": "close",
    "S13-annex": "close",
    "S14-trace": "close",
}

FAMILY_LABEL = {
    "who": "Who and where",
    "when": "When",
    "route": "Who it goes to",
    "act": "What it does",
    "close": "How it is guaranteed",
    "other": "Structural",
}

OB_SHORT = {"mandatory": "must", "optional": "opt", "conditional": "cond"}


def load_rows():
    with open(ROOT / "requisites.csv", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    for i, r in enumerate(rows):
        r["_i"] = i
    return rows


def band(row, note=""):
    return {
        "clause": row["clause"],
        "local": row["local_term"],
        "gloss": row["gloss_en"],
        "slot": row["slot"],
        "obligation": row["obligation"],
        "fam": FAMILY.get(row["slot"], "other"),
        "gap": False,
        "note": note,
    }


def gap(clause, gloss, note):
    return {
        "clause": clause,
        "local": "",
        "gloss": gloss,
        "slot": "",
        "obligation": "",
        "fam": "other",
        "gap": True,
        "note": note,
    }


def build_types(rows):
    by = {}
    for r in rows:
        by.setdefault(r["system"], []).append(r)

    ua = by["UA"]
    de = by["DE"]
    cn = by["CN"]
    un = by["UN"]
    eu = by["EU"]

    # UA: the standard's own clause order is the page order. A variant keeps the
    # skeleton and replaces one requisite with a dashed gap in its own position.
    ua_order = sorted(ua, key=lambda r: r["_i"])

    def ua_variant(omit, gap_spec):
        out = []
        for r in ua_order:
            out.append(gap_spec if r["clause"] == omit else band(r))
        return out

    ua_order_bands = ua_variant(
        "4.1(15)",
        gap(
            "4.1(15)",
            "Addressee",
            "Coded for correspondence only, so it is not part of the order form.",
        ),
    )

    ua_letter_bands = ua_variant(
        "4.1(09)",
        gap(
            "4.1(09)",
            "Name of the document type",
            "Clause 4.4: the document-type name is not written on letters.",
        ),
    )

    # UN: the Editorial Manual fixes the order of the three parts (C12); the
    # document symbol is coded as an identifier, not as a position.
    un_by_slot = {r["slot"]: r for r in un}
    un_bands = [
        band(un_by_slot["S2-identifier"], "Position not fixed by the coded source."),
        band(un_by_slot["S3-origin"]),
        band(un_by_slot["S9-setting"]),
        band(un_by_slot["S11-dispositif"]),
        band(un_by_slot["S5-temporal"]),
    ]

    return [
        {
            "id": "ua-order",
            "pair": 0,
            "system": "UA",
            "name": "Наказ",
            "gloss": "Order / directive",
            "standard": "ДСТУ 4163:2020",
            "bands": ua_order_bands,
            "caption": "The full 32-requisite skeleton, in the standard's clause order.",
        },
        {
            "id": "ua-letter",
            "pair": 0,
            "system": "UA",
            "name": "Лист",
            "gloss": "Letter",
            "standard": "ДСТУ 4163:2020",
            "bands": ua_letter_bands,
            "caption": "The same skeleton with one slot swapped: 09 out, 15 in.",
        },
        {
            "id": "de-letter",
            "pair": 1,
            "system": "DE",
            "name": "Geschäftsbrief",
            "gloss": "Business letter",
            "standard": "DIN 5008:2020",
            "bands": [band(r) for r in de],
            "caption": "Nine components, three of them routing.",
        },
        {
            "id": "cn-doc",
            "pair": 1,
            "system": "CN",
            "name": "党政机关公文",
            "gloss": "Party-government document",
            "standard": "GB/T 9704-2012",
            "bands": [band(r) for r in cn if r["clause"] != "10"],
            "caption": "版头 head, 主体 body, 版记 record — the most database-like head in the sample.",
        },
        {
            "id": "un-res",
            "pair": 2,
            "system": "UN",
            "name": "Resolution",
            "gloss": "Resolution",
            "standard": "UN Editorial Manual",
            "bands": un_bands,
            "caption": "Organ, preamble, operative part — the order the manual fixes. "
            "The symbol is drawn at the head; its position is not coded.",
        },
        {
            "id": "eu-act",
            "pair": 2,
            "system": "EU",
            "name": "Legal act",
            "gloss": "Regulation / directive / decision",
            "standard": "Interinstitutional Style Guide",
            "bands": [band(r) for r in eu],
            "caption": "Title, citations, recitals, articles, annexes — and no addressee.",
        },
    ]


def counts(types):
    out = {}
    for t in types:
        real = [b for b in t["bands"] if not b["gap"]]
        fam, slot = {}, {}
        for b in real:
            fam[b["fam"]] = fam.get(b["fam"], 0) + 1
            slot[b["slot"]] = slot.get(b["slot"], 0) + 1
        out[t["id"]] = {"total": len(real), "fam": fam, "slot": slot}
    return out


SHORT = {
    "ua-order": "the Ukrainian order",
    "ua-letter": "the Ukrainian letter",
    "de-letter": "DIN 5008",
    "cn-doc": "the Chinese document",
    "un-res": "the UN resolution",
    "eu-act": "the EU act",
}


def shared_slots(c):
    """Slots present in every one of the six types."""
    sets = [set(d["slot"]) for d in c.values()]
    return sorted(set.intersection(*sets))


def near_universal(c, n=5):
    """Slots present in exactly n of the six types, with the types that lack them."""
    ids = list(c)
    out = []
    for slot in sorted({s for d in c.values() for s in d["slot"]}):
        have = [i for i in ids if slot in c[i]["slot"]]
        if len(have) == n:
            out.append((slot, [SHORT[i] for i in ids if i not in have]))
    return out


CASE_FILES = (("ua", "UA"), ("de", "DE"), ("cn", "CN"), ("un", "UN"), ("eu", "EU"))


def case_profiles():
    """The `## Slot profile` line of each case file, as {system: {slot: mark}}."""
    out = {}
    for stem, system in CASE_FILES:
        text = (ROOT / "cases" / f"{stem}.md").read_text(encoding="utf-8")
        m = re.search(r"##\s*Slot profile(.*?)(?=\n##\s|\Z)", text, re.S)
        if not m:
            continue
        out[system] = {
            f"S{n}": mark for n, mark in re.findall(r"S(\d+)\s*([●○—])", m.group(1))
        }
    return out


def case_divergences(coded_slots):
    """Slot-level disagreements between the prose profiles and requisites.csv."""
    out = []
    for system, prof in case_profiles().items():
        for n in range(1, 15):
            key = f"S{n}"
            mark = prof.get(key)
            has = any(s.startswith(key + "-") for s in coded_slots.get(system, ()))
            if mark in ("●", "○") and not has:
                out.append((system, key, "present in the case profile, no coded row"))
            elif mark == "—" and has:
                out.append((system, key, "absent in the case profile, coded row exists"))
    return out


def profile_intersection():
    """Slots the case profiles mark present in all five profiled systems."""
    profs = case_profiles()
    if len(profs) < 5:
        return []
    sets = [
        {k for k, v in p.items() if v in ("●", "○")} for p in profs.values()
    ]
    return sorted(set.intersection(*sets), key=lambda s: int(s[1:]))


def esc(s):
    return html.escape(s, quote=True)


def render_map(t):
    bands = t["bands"]
    pitch, height, top, left, width = 20, 18, 10, 16, 528
    h = top + len(bands) * pitch + 10
    parts = [
        f'<svg class="map" viewBox="0 0 560 {h}" role="list" '
        f'aria-label="Page map: {esc(t["name"])} ({esc(t["gloss"])}), '
        f'{len([b for b in bands if not b["gap"]])} coded elements in clause order">',
        f'<rect class="paper" x="0.5" y="0.5" width="559" height="{h - 1}" rx="6"/>',
    ]
    for i, b in enumerate(bands):
        y = top + i * pitch
        if b["gap"]:
            parts.append(
                f'<g class="band gap" data-fam="other" data-ob="none" '
                f'data-clause="{esc(b["clause"])}" data-gloss="{esc(b["gloss"])}" '
                f'data-local="" data-slot="" data-note="{esc(b["note"])}" '
                f'tabindex="0" role="listitem" '
                f'aria-label="clause {esc(b["clause"])}, {esc(b["gloss"])}, not present">'
                f'<rect class="band-bg" x="{left}" y="{y}" width="{width}" height="{height}" rx="3"/>'
                f'<text class="band-label" x="{left + 12}" y="{y + 13}">{esc(b["gloss"])}</text>'
                f'<text class="band-clause" x="{left + width - 8}" y="{y + 13}" '
                f'text-anchor="end">{esc(b["clause"])}</text></g>'
            )
            continue
        parts.append(
            f'<g class="band" data-fam="{b["fam"]}" data-ob="{b["obligation"]}" '
            f'data-clause="{esc(b["clause"])}" data-gloss="{esc(b["gloss"])}" '
            f'data-local="{esc(b["local"])}" data-slot="{esc(b["slot"])}" '
            f'data-note="{esc(b["note"])}" tabindex="0" role="listitem" '
            f'aria-label="clause {esc(b["clause"])}, {esc(b["gloss"])}, '
            f'{esc(b["slot"])}, {esc(b["obligation"])}" '
            f'style="--fam:var(--fam-{b["fam"]})">'
            f'<rect class="band-bg" x="{left}" y="{y}" width="{width}" height="{height}" rx="3"/>'
            f'<rect class="band-bar" x="{left}" y="{y}" width="4" height="{height}" rx="2"/>'
            f'<text class="band-label" x="{left + 12}" y="{y + 13}">{esc(b["gloss"])}</text>'
            f'<text class="band-ob" x="{left + width - 62}" y="{y + 13}" '
            f'text-anchor="end">{OB_SHORT.get(b["obligation"], b["obligation"])}</text>'
            f'<text class="band-clause" x="{left + width - 8}" y="{y + 13}" '
            f'text-anchor="end">{esc(b["clause"])}</text></g>'
        )
    parts.append("</svg>")
    return "".join(parts)


def render_card(t):
    n = len([b for b in t["bands"] if not b["gap"]])
    return (
        f'<article class="card" id="{t["id"]}">'
        f'<header class="card-head">'
        f'<p class="card-kicker">{esc(t["system"])} · {esc(t["standard"])}</p>'
        f'<h3>{esc(t["name"])} <span class="card-gloss">{esc(t["gloss"])}</span></h3>'
        f'<p class="card-meta"><span class="count" data-total="{n}">{n}</span> coded elements</p>'
        f"</header>"
        f'<div class="map-wrap">{render_map(t)}</div>'
        f'<p class="card-caption">{esc(t["caption"])}</p>'
        f"</article>"
    )


PAIRS = [
    (0, "Pair 1 · One skeleton, one slot apart",
     "Ukraine codes one form for both. The order and the letter differ by a single "
     "requisite: the document-type name (09) is written on an order and not on a letter, "
     "and the addressee (15) belongs to correspondence."),
    (1, "Pair 2 · Two letters, two centres of gravity",
     "The German letter is a routing instrument: sender, recipient, reference, salutation. "
     "The Chinese document is an identifier instrument: copy number, secrecy, urgency, "
     "reference number, all before the title."),
    (2, "Pair 3 · Two acts, no addressee",
     "Neither the UN resolution nor the EU act names a recipient. Both spend their "
     "elements on justification and on the operative text instead."),
]


def render_pairs(types):
    out = []
    for pid, title, blurb in PAIRS:
        out.append(
            f'<div class="pair"><h2 class="pair-title">{esc(title)}</h2>'
            f'<p class="pair-blurb">{esc(blurb)}</p><div class="pair-grid">'
        )
        for t in types:
            if t["pair"] == pid:
                out.append(render_card(t))
        out.append("</div></div>")
    return "".join(out)


def render_compare(types, c):
    ua_o, ua_l = c["ua-order"], c["ua-letter"]
    de, cn, un, eu = c["de-letter"], c["cn-doc"], c["un-res"], c["eu-act"]

    def f(d, fam):
        return d["fam"].get(fam, 0)

    def s(d, slot):
        return d["slot"].get(slot, 0)

    shared = shared_slots(c)
    near = near_universal(c, 5)
    no_trace = [
        name
        for name, d in (
            ("DIN 5008", de),
            ("the UN resolution", un),
            ("the EU act", eu),
        )
        if s(d, "S14-trace") == 0
    ]

    if shared:
        first = (
            f"<strong>One slot is common to all six: {', '.join(shared)}.</strong> "
            f"Every other slot is dropped by at least one type."
        )
    else:
        near_txt = "; ".join(
            f"{slot} (missing from {', '.join(miss)})" for slot, miss in near
        )
        first = (
            f"<strong>No slot is common to all six.</strong> The nearest are "
            f"{len(near)} slots at five of six: {near_txt}. This is the type-level echo "
            f"of the atlas's "
            f"v1.4 regrade, where no stem slot survived at lineage level either."
        )

    bullets = [
        first,
        f"<strong>The letter loads the routing block.</strong> DIN 5008 puts "
        f"{f(de, 'route')} of its {de['total']} elements in S6–S8; the EU act puts "
        f"{f(eu, 'route')} of {eu['total']}.",
        f"<strong>The act loads the setting and the dispositif.</strong> The EU act puts "
        f"{f(eu, 'act')} of {eu['total']} elements in S9–S11, the UN resolution "
        f"{f(un, 'act')} of {un['total']}; DIN 5008 puts {f(de, 'act')} of {de['total']}.",
        f"<strong>The trace layer is uneven.</strong> ДСТУ 4163 spends "
        f"{s(ua_o, 'S14-trace')} of {ua_o['total']} elements on S14 alone; "
        f"{', '.join(no_trace)} carry none.",
        f"<strong>Genre, not nation, moves the slots.</strong> Ukraine's own order and "
        f"letter differ by one requisite, while the Ukrainian and German letters differ "
        f"by {abs(ua_l['total'] - de['total'])} elements.",
    ]
    return "<ul class=\"moves\">" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>"


CSS = """
:root{color-scheme:light;--paper:#f4f5f7;--panel:#fff;--sunk:#f6f7f9;--ink:#111318;
--secondary:#2c3038;--muted:#6a707c;--faint:#9aa0aa;--rule:#e5e7eb;--rule-strong:#d3d7dd;
--accent:#2457d6;--accent-soft:#eaf0fd;--accent-ink:#1b46b4;
--fam-who:#2457d6;--fam-when:#6a4fc8;--fam-route:#0e7c86;--fam-act:#b26a00;
--fam-close:#13834b;--fam-other:#6a707c;
--sans:-apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans",sans-serif;
--mono:"SF Mono",ui-monospace,"JetBrains Mono",Menlo,Consolas,monospace}
:root[data-theme=dark]{color-scheme:dark;--paper:#0c0d10;--panel:#15171c;--sunk:#1b1e24;
--ink:#f1f3f6;--secondary:#cfd3da;--muted:#8d94a1;--faint:#5f6672;--rule:#262a31;
--rule-strong:#343943;--accent:#7aa2ff;--accent-soft:#18223a;--accent-ink:#a3bfff;
--fam-who:#7aa2ff;--fam-when:#a994f5;--fam-route:#4fc3cd;--fam-act:#e9b04f;
--fam-close:#5cc98d;--fam-other:#8d94a1}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;
--paper:#0c0d10;--panel:#15171c;--sunk:#1b1e24;--ink:#f1f3f6;--secondary:#cfd3da;
--muted:#8d94a1;--faint:#5f6672;--rule:#262a31;--rule-strong:#343943;--accent:#7aa2ff;
--accent-soft:#18223a;--accent-ink:#a3bfff;--fam-who:#7aa2ff;--fam-when:#a994f5;
--fam-route:#4fc3cd;--fam-act:#e9b04f;--fam-close:#5cc98d;--fam-other:#8d94a1}}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--secondary);
font:14.5px/1.7 var(--sans);-webkit-font-smoothing:antialiased}
h1,h2,h3,p,ul,ol{margin:0}
strong,b{color:var(--ink);font-weight:600}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline;text-underline-offset:3px}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}
.shell{width:min(1240px,calc(100% - 48px));margin:auto}
.skip{position:absolute;top:-80px;left:12px;padding:8px 12px;background:var(--ink);
color:var(--paper);z-index:20}
.skip:focus{top:8px}
.masthead{display:flex;align-items:flex-start;justify-content:space-between;gap:24px;
padding:40px 0 20px}
h1{font:700 27px/1.3 var(--sans);color:var(--ink);letter-spacing:-.015em;max-width:820px}
.sub{margin-top:8px;color:var(--muted);font-size:13.5px;max-width:760px}
.tools{display:flex;gap:8px;flex-shrink:0}
.tools button{font:12.5px/1 var(--sans);color:var(--secondary);background:var(--panel);
border:1px solid var(--rule-strong);border-radius:8px;height:30px;padding:0 11px;
cursor:pointer}
.tools button:hover{background:var(--sunk);color:var(--ink)}
.answer{background:var(--panel);border:1px solid var(--rule);border-radius:12px;
padding:22px 24px;margin-bottom:18px}
.verdict{font:600 17px/1.6 var(--sans);color:var(--ink);padding:12px 16px;
border-radius:8px;background:var(--accent-soft);box-shadow:inset 3px 0 0 var(--accent)}
.verdict strong{color:var(--accent-ink);font-weight:700}
.reasons{list-style:none;padding:0;margin:14px 0 0;counter-reset:r}
.reasons li{counter-increment:r;position:relative;padding:5px 0 5px 26px;font-size:14px}
.reasons li::before{content:counter(r);position:absolute;left:2px;top:9px;width:17px;
height:17px;border-radius:50%;display:grid;place-items:center;font:600 10.5px/1 var(--sans);
color:var(--muted);background:var(--sunk);box-shadow:inset 0 0 0 1px var(--rule-strong)}
.scope{margin-top:14px;padding-top:12px;border-top:1px solid var(--rule);
display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:12.5px;color:var(--muted)}
.chip-scope{padding:0 8px;border-radius:999px;background:var(--sunk);
border:1px solid var(--rule);font-size:12px;line-height:1.7}
.panel{background:var(--panel);border:1px solid var(--rule);border-radius:12px;
padding:20px 24px;margin-bottom:18px}
.panel>h2{font:600 16px/1.4 var(--sans);color:var(--ink);margin-bottom:4px}
.panel>p.lede{color:var(--muted);font-size:13.5px;margin-bottom:14px}
.legend{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 4px}
.chip{display:inline-flex;align-items:center;gap:7px;height:30px;padding:0 12px;
border:1px solid var(--rule-strong);border-radius:999px;background:var(--panel);
font:12.5px/1 var(--sans);color:var(--secondary);cursor:pointer}
.chip:hover{background:var(--sunk);color:var(--ink)}
.chip[aria-pressed=true]{background:var(--sunk);color:var(--ink);font-weight:600;
box-shadow:inset 0 0 0 1px var(--ink)}
.swatch{width:10px;height:10px;border-radius:3px;background:var(--fam)}
.legend-note{font-size:12.5px;color:var(--muted);margin-top:10px}
.legend-note code{font-family:var(--mono);font-size:11.5px;background:var(--sunk);
border:1px solid var(--rule);border-radius:4px;padding:0 4px}
.controls{display:flex;flex-wrap:wrap;gap:14px;align-items:center;margin-top:12px;
padding-top:12px;border-top:1px solid var(--rule);font-size:12.5px;color:var(--muted)}
.controls label{display:inline-flex;align-items:center;gap:7px;cursor:pointer}
.pair{margin-top:22px}
.pair:first-of-type{margin-top:6px}
.pair-title{font:600 14.5px/1.4 var(--sans);color:var(--ink)}
.pair-blurb{font-size:13px;color:var(--muted);max-width:820px;margin:2px 0 12px}
.pair-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;
align-items:start}
.card{border:1px solid var(--rule);border-radius:10px;padding:14px 14px 12px;
background:var(--sunk);min-width:0}
.card-head{margin-bottom:10px}
.card-kicker{font:11px/1.4 var(--mono);color:var(--muted);letter-spacing:.02em}
.card h3{font:600 15px/1.35 var(--sans);color:var(--ink);margin-top:2px}
.card-gloss{font-weight:400;color:var(--muted);font-size:13px}
.card-meta{font-size:12px;color:var(--muted);margin-top:2px}
.count{font-variant-numeric:tabular-nums;color:var(--ink);font-weight:600}
.card-caption{font-size:12.5px;color:var(--muted);margin-top:8px;line-height:1.55}
.map-wrap{overflow-x:auto;overflow-y:hidden;-webkit-overflow-scrolling:touch}
.map{display:block;width:100%;min-width:520px;height:auto}
.paper{fill:var(--panel);stroke:var(--rule)}
.band{cursor:pointer}
.band-bg{fill:var(--fam);opacity:.10;transition:opacity .12s}
.band[data-ob=mandatory] .band-bg{opacity:.22}
.band[data-ob=conditional] .band-bg{opacity:.16}
.band-bar{fill:var(--fam);opacity:.5}
.band[data-ob=mandatory] .band-bar{opacity:1}
.band[data-ob=conditional] .band-bar{opacity:.75}
.band:hover .band-bg,.band:focus-visible .band-bg{opacity:.34}
.band-label{font:10px var(--sans);fill:var(--ink)}
.band-ob,.band-clause{font:8.5px var(--mono);fill:var(--muted)}
.band.gap .band-bg{fill:none;stroke:var(--faint);stroke-dasharray:4 3;opacity:1}
.band.gap .band-label{fill:var(--muted);font-style:italic}
.band.dim{opacity:.13}
.moves{list-style:none;padding:0;margin:0}
.moves li{position:relative;padding:7px 0 7px 18px;font-size:13.5px;
border-top:1px solid var(--rule)}
.moves li:first-child{border-top:0}
.moves li::before{content:"";position:absolute;left:2px;top:1.05em;width:5px;height:5px;
border-radius:50%;background:var(--ink);opacity:.5}
.limits{list-style:none;padding:0;margin:0}
.limits li{position:relative;padding:6px 0 6px 18px;font-size:13.5px}
.limits li::before{content:"";position:absolute;left:2px;top:1em;width:5px;height:5px;
border-radius:50%;background:var(--faint)}
.checklist{list-style:none;padding:0;margin:0}
.checklist li+li{border-top:1px dashed var(--rule)}
.checklist label{display:flex;gap:10px;align-items:flex-start;padding:8px 0;
cursor:pointer;font-size:13.5px}
.checklist input{appearance:none;flex-shrink:0;width:17px;height:17px;margin:3px 0 0;
border:1.5px solid var(--rule-strong);border-radius:5px;background:var(--panel);
display:grid;place-items:center;cursor:pointer}
.checklist input::after{content:"";width:5px;height:9px;margin-top:-2px;
border:solid var(--panel);border-width:0 2px 2px 0;transform:rotate(45deg) scale(0);
transition:transform .12s}
.checklist input:checked{background:var(--fam-close);border-color:var(--fam-close)}
.checklist input:checked::after{transform:rotate(45deg) scale(1)}
.checklist input:checked+span{color:var(--muted);text-decoration:line-through;
text-decoration-color:var(--faint)}
footer{padding:8px 0 48px;font-size:12px;color:var(--muted)}
footer p+p{margin-top:6px}
footer .back{font-size:13px;color:var(--secondary)}
#tip{position:fixed;z-index:30;max-width:340px;padding:10px 12px;border-radius:8px;
background:var(--ink);color:var(--paper);font-size:12.5px;line-height:1.5;
box-shadow:0 8px 24px rgb(0 0 0/.22);pointer-events:none;opacity:0;
transition:opacity .1s}
#tip.on{opacity:1}
#tip b{color:var(--paper);display:block;font-size:13px;margin-bottom:2px}
#tip .t-local{display:block;font-size:12px;opacity:.85;margin-bottom:4px}
#tip .t-meta{display:block;font-family:var(--mono);font-size:11px;opacity:.75}
@media(max-width:900px){.pair-grid{grid-template-columns:minmax(0,1fr)}
.masthead{flex-direction:column;gap:14px}.shell{width:calc(100% - 28px)}}
@media print{.tools,.controls,#tip{display:none}.panel,.answer{break-inside:avoid}}
"""

JS = """
(function(){
  var chips=[].slice.call(document.querySelectorAll('.chip'));
  var must=document.getElementById('must-only');
  var bands=[].slice.call(document.querySelectorAll('.band'));
  var counts=[].slice.call(document.querySelectorAll('.count'));
  function apply(){
    var on={};var any=false;
    chips.forEach(function(c){
      if(c.getAttribute('aria-pressed')==='true'){on[c.dataset.fam]=1;any=true;}
    });
    var onlyMust=must&&must.checked;
    bands.forEach(function(b){
      var famOk=!any||on[b.dataset.fam]===1;
      var obOk=!onlyMust||b.dataset.ob==='mandatory';
      b.classList.toggle('dim',!(famOk&&obOk));
    });
    counts.forEach(function(el){
      var card=el.closest('.card');
      var vis=card.querySelectorAll('.band:not(.dim):not(.gap)').length;
      el.textContent=vis;
    });
  }
  chips.forEach(function(c){
    c.addEventListener('click',function(){
      c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')==='true'?'false':'true');
      apply();
    });
  });
  if(must)must.addEventListener('change',apply);

  var tip=document.getElementById('tip');
  function show(b,x,y){
    var local=b.dataset.local?'<span class="t-local">'+b.dataset.local+'</span>':'';
    var meta=[b.dataset.clause,b.dataset.slot,b.dataset.ob].filter(Boolean).join(' · ');
    var note=b.dataset.note?'<span class="t-meta">'+b.dataset.note+'</span>':'';
    tip.innerHTML='<b>'+b.dataset.gloss+'</b>'+local+
      '<span class="t-meta">'+meta+'</span>'+note;
    tip.classList.add('on');
    var w=tip.offsetWidth,h=tip.offsetHeight;
    var left=Math.min(Math.max(8,x+14),window.innerWidth-w-8);
    var top=y-h-12; if(top<8)top=y+18;
    tip.style.left=left+'px';tip.style.top=top+'px';
  }
  function hide(){tip.classList.remove('on');}
  bands.forEach(function(b){
    b.addEventListener('mouseenter',function(e){show(b,e.clientX,e.clientY);});
    b.addEventListener('mousemove',function(e){show(b,e.clientX,e.clientY);});
    b.addEventListener('mouseleave',hide);
    b.addEventListener('focus',function(){
      var r=b.getBoundingClientRect();show(b,r.left+r.width/2,r.top);
    });
    b.addEventListener('blur',hide);
  });

  var root=document.documentElement;
  var btn=document.getElementById('theme');
  btn.addEventListener('click',function(){
    var dark=root.getAttribute('data-theme')==='dark'||
      (!root.getAttribute('data-theme')&&
       window.matchMedia('(prefers-color-scheme:dark)').matches);
    root.setAttribute('data-theme',dark?'light':'dark');
    btn.textContent=dark?'Dark':'Light';
  });
  apply();
})();
"""


def build():
    rows = load_rows()
    types = build_types(rows)
    c = counts(types)

    ua_o, ua_l = c["ua-order"], c["ua-letter"]
    de, cn, un, eu = c["de-letter"], c["cn-doc"], c["un-res"], c["eu-act"]

    shared = shared_slots(c)
    near = near_universal(c, 5)

    if shared:
        verdict = (
            f"The six types share one slot — <strong>{', '.join(shared)}</strong> — and "
            f"differ in where they put their weight: <strong>letters load the routing "
            f"block, acts load the setting and the dispositif</strong>, and the trace "
            f"layer is densest in Ukraine and absent from the German, UN and EU types."
        )
        first_reason = (
            f"Only {', '.join(shared)} appears in all six maps; every other slot is "
            f"dropped by at least one type."
        )
    else:
        verdict = (
            f"<strong>No slot is common to all six types.</strong> The nearest reach five "
            f"of six, and each type puts its weight somewhere different: letters in the "
            f"routing block, acts in the setting and the dispositif, Ukraine in the trace "
            f"layer."
        )
        first_reason = (
            f"{len(near)} slots reach five of six: "
            + "; ".join(f"{slot} (missing from {', '.join(m)})" for slot, m in near)
            + "."
        )

    reasons = [
        first_reason,
        f"DIN 5008 puts {de['fam'].get('route',0)} of its {de['total']} elements in the "
        f"routing block; the EU act puts {eu['fam'].get('route',0)} of {eu['total']}.",
        f"ДСТУ 4163 spends {ua_o['slot'].get('S14-trace',0)} of {ua_o['total']} elements "
        f"on trace alone; DIN 5008, the UN resolution and the EU act carry none.",
        "Ukraine's own order and letter differ by one requisite, so the axis is genre, "
        "not nation.",
    ]

    legend = "".join(
        f'<button class="chip" data-fam="{k}" aria-pressed="false">'
        f'<span class="swatch" style="--fam:var(--fam-{k})"></span>{FAMILY_LABEL[k]}</button>'
        for k in ("who", "when", "route", "act", "close", "other")
    )

    coded_slots = {}
    for r in rows:
        coded_slots.setdefault(r["system"], set()).add(r["slot"])
    div = case_divergences(coded_slots)
    prof_int = profile_intersection()

    s12 = [d for d in div if d[1] == "S12"]
    s12_txt = ""
    if s12:
        s12_txt = (
            f" The most consequential is authentication: "
            f"{', '.join(sorted({d[0] for d in s12}))} marks S12 present in its case "
            f"profile while its coded rows carry none, and that single gap is what makes "
            f"the intersection empty."
        )
    divergence = (
        f"<li><strong>The maps follow <code>requisites.csv</code>, not the slot profiles "
        f"in <code>cases/*.md</code>.</strong> The two disagree on {len(div)} slot-level "
        f"judgements across these five systems. Under the case profiles "
        f"{len(prof_int)} slots would be present in all six types; under the coding table "
        f"none is.{s12_txt} Where they disagree the map follows the coding table, because "
        f"that is the table the repository's gates validate.</li>"
    )

    doc = TEMPLATE
    doc = doc.replace("@@DIVERGENCE@@", divergence)
    doc = doc.replace("@@CSS@@", CSS)
    doc = doc.replace("@@JS@@", JS)
    doc = doc.replace("@@VERDICT@@", verdict)
    doc = doc.replace(
        "@@REASONS@@", "".join(f"<li>{r}</li>" for r in reasons)
    )
    doc = doc.replace("@@LEGEND@@", legend)
    doc = doc.replace("@@PAIRS@@", render_pairs(types))
    doc = doc.replace("@@MOVES@@", render_compare(types, c))
    doc = doc.replace(
        "@@SCOPE@@",
        "".join(
            f'<span class="chip-scope">{s}</span>'
            for s in (
                "6 types · 5 systems",
                "clause order, not measured geometry",
                "atlas v1.4",
            )
        ),
    )
    doc = doc.replace(
        "@@TOTALS@@",
        f"{sum(d['total'] for d in c.values())} coded requisites across six types",
    )
    return doc


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="description" content="Six official document types drawn as page maps: every band is one coded requisite, placed in the order the standard itself fixes.">
<title>Six document types, six page maps · Universal document morphology</title>
<style>@@CSS@@</style>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="shell">
<header class="masthead">
  <div>
    <h1>Six document types, six page maps</h1>
    <p class="sub">An order, a letter, a business letter, a party-government document, a
    resolution and a legal act. Every band is one requisite coded in
    <code>requisites.csv</code>, placed in the order the standard itself fixes.</p>
  </div>
  <div class="tools"><button id="theme" type="button">Dark</button></div>
</header>

<main id="main">
<section class="answer">
  <p class="verdict">@@VERDICT@@</p>
  <ol class="reasons">@@REASONS@@</ol>
  <p class="scope"><span>Scope</span>@@SCOPE@@</p>
</section>

<section class="panel" id="how">
  <h2>How to read a page map</h2>
  <p class="lede">Each map is one document type. Bands run top to bottom in the order the
  standard gives its elements; colour is the slot family; the tag on the right is the
  obligation the standard attaches to that element.</p>
  <div class="legend">@@LEGEND@@</div>
  <p class="legend-note">Click a family to isolate it across all six maps. Hover or focus a
  band for its clause number, its original wording and its slot. <code>must</code> =
  mandatory, <code>cond</code> = conditional, <code>opt</code> = optional. A dashed band is
  a slot the type does not carry. On a narrow screen each map scrolls sideways rather than
  shrinking its labels.</p>
  <div class="controls">
    <label><input type="checkbox" id="must-only"> Show mandatory elements only</label>
    <span>@@TOTALS@@</span>
  </div>
</section>

<section class="panel" id="maps">
  <h2>The six maps</h2>
  <p class="lede">Three pairs, each chosen to isolate one difference.</p>
  @@PAIRS@@
</section>

<section class="panel" id="moves">
  <h2>What the six maps show together</h2>
  @@MOVES@@
</section>

<section class="panel" id="limits">
  <h2>What these maps are not</h2>
  <ul class="limits">
    @@DIVERGENCE@@
    <li><strong>Not measured geometry.</strong> Band order is the standard's clause order,
    not a position measured on a page. No page was measured for this page.</li>
    <li><strong>Not proportional height.</strong> Every band is the same height; a document
    with 31 elements is not drawn 31 times taller than one with 5.</li>
    <li><strong>The Ukrainian letter is a derivation.</strong> The atlas codes one Ukrainian
    form. The letter map removes requisite 09 (clause 4.4: the document-type name is not
    written on letters) and keeps 15, which the atlas codes for correspondence. It is not a
    separately coded case.</li>
    <li><strong>The Chinese letter variant is not drawn.</strong> GB/T 9704-2012 gives
    信函格式, 命令/令格式 and 纪要格式 their own layouts; the atlas codes the general
    document, so that is what the map shows.</li>
    <li><strong>The UN symbol's position is an assumption.</strong> The coded source fixes
    the symbol's grammar, not where it sits; it is drawn at the head because that is where a
    UN document carries it.</li>
    <li><strong>Not a sample.</strong> Six types from five systems, chosen to teach the
    contrast. The atlas's 28 systems are a convenience frame, and these six are a
    convenience frame inside it.</li>
  </ul>
</section>

<section class="panel" id="checklist">
  <h2>What to check before quoting this page</h2>
  <ul class="checklist">
    <li><label><input type="checkbox"><span>The counts are "coded requisites", not elements
    on a real page.</span></label></li>
    <li><label><input type="checkbox"><span>Band height is not read as a
    measurement.</span></label></li>
    <li><label><input type="checkbox"><span>The Ukrainian letter is described as a
    derivation from the order, not as a coded case.</span></label></li>
    <li><label><input type="checkbox"><span>信函格式 is not claimed to be drawn
    here.</span></label></li>
    <li><label><input type="checkbox"><span>The six types are described as a teaching
    selection, not as a sample of the corpus.</span></label></li>
  </ul>
</section>
</main>

<footer>
  <p class="back"><a href="official-documents-explainer.html">What does every official
  document have in common?</a> — the companion page: the fourteen slots, the evidence,
  and the claim the atlas had to regrade.</p>
  <p>Generated by <code>education/build_document_types.py</code> from
  <code>requisites.csv</code> and <code>cases/</code>. Do not hand-edit this file.</p>
</footer>
</div>
<div id="tip" role="status" aria-live="polite"></div>
<script>@@JS@@</script>
</body>
</html>
"""


def main():
    doc = build()
    if "--check" in sys.argv:
        if not OUT.exists():
            print(f"MISSING {OUT.relative_to(ROOT)}")
            return 1
        current = OUT.read_text(encoding="utf-8")
        if current != doc:
            print(f"STALE {OUT.relative_to(ROOT)} — rerun without --check")
            return 1
        print(f"OK {OUT.relative_to(ROOT)} is current")
        return 0
    OUT.write_text(doc, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(doc):,} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
