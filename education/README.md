# Teaching material

An interactive one-page explainer for students and teachers in law, archival
science, public administration and information science. It teaches the atlas's
structural model, its evidence, and — deliberately — the claim it had to regrade.

Open `official-documents-explainer.html` in any browser. It is self-contained:
no network, no build step, works offline and from a USB stick. The toolbar
switches light/dark and the editorial/clean/swiss styles; each diagram has an
"Open interactive view" for pan, zoom and step-through.

## What it covers

1. What counts as an official document, and where the claim stops (khipu, wampum).
2. The fourteen slots, grouped by the question each answers.
3. How often each slot appears in the 25 slot-coded systems.
4. The two declensions — letter vs normative act — and the one joint pattern behind them.
5. Whether the grammar is universal: the B3 lineage audit, 0 of 6 stem slots,
   and the 2026 regrade.
6. How the atlas is built: corpus, coding, claim ledger, gates, pre-registered audits.
7. What the material does not establish.
8. A six-pass reading exercise for any document the reader can inspect.
9. A checklist for quoting the page correctly.

## Document-type page maps

`document-types.html` is a second, standalone page: six document types drawn as
page maps — a Ukrainian order and letter, a German business letter, a Chinese
party-government document, a UN resolution and an EU legal act. Each band is one
row of `requisites.csv`, placed in the order the standard itself fixes; colour is
the slot family, the right-hand tag is the obligation. Clicking a family isolates
it across all six maps; hovering or focusing a band shows its clause number, its
original wording and its slot.

It is generated, not hand-written:

```bash
python3 education/build_document_types.py           # write the page
python3 education/build_document_types.py --check   # fail if it is stale
```

Every count in the prose is computed from the data at build time, so a change to
`requisites.csv` either updates the page or fails `--check`.

The two pages link to each other: the explainer's declensions panel points here,
and this page's footer points back. Archify rejects relative links, so the
explainer carries the absolute Pages URL; the back-link is relative and works
both locally and on Pages, because the workflow publishes the explainer under
both `index.html` and its own filename.

**The maps follow `requisites.csv`, not the `## Slot profile` lines in
`cases/*.md`.** The two disagree on 22 slot-level judgements across these five
systems. The consequence is visible in the page's headline: under the case
profiles nine slots would be present in all six types, while under the coding
table none is — the UN resolution's case profile marks S12 authentication
present, but its coded rows carry no authentication element. The page states
this in its limits panel rather than resolving it; reconciling the two sources is
a data change, not a teaching-page change.

## Rebuilding

The page is generated from `official-documents-explainer.archify.md` with
[archify](https://github.com/tt-a1i/archify) (Node 18+). From the repo root:

```bash
git clone --depth 1 https://github.com/tt-a1i/archify.git /tmp/archify
node /tmp/archify/archify/bin/archify.mjs finalize explainer \
  education/official-documents-explainer.archify.md \
  education/official-documents-explainer.html --json
```

The command validates the draft, delivers atomically, runs the structural
checks, and writes a delivery receipt. Run `browser-check` separately with a
real Chromium when changing layout:

```bash
ARCHIFY_CHROME=/path/to/chrome \
  node /tmp/archify/archify/bin/archify.mjs browser-check \
  education/official-documents-explainer.html --out-dir /tmp/edu-browser --json
```

Do not hand-edit the HTML: change the `.archify.md` source and regenerate.

## Editorial rule

Every number on the page comes from the atlas or its registered studies
(`README.md`, `analysis/findings.md`, `audit/RESULTS.md`, `lineage/RESULTS.md`).
If the atlas changes, the page changes with it; the page never introduces a
claim the repository does not support.
