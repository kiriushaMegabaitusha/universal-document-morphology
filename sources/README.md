# Sources — not redistributed in this public snapshot

The working copy of this project keeps a `sources/` directory of retrieved
primary and near-primary texts (PDFs plus extracted `.txt`) — standards, chancery
manuals, official guides and archival pages. Those files are third-party
material with varying licences, so **this public repository omits them**.

Nothing in the analysis depends on the files being public:

- every source is identified by URL in `ledger.json`, with a `retrieved` flag and
  the claim(s) it supports;
- `python3 check_claims.py --online` HEAD-checks every retrieved URL;
- `python3 check_claims.py` (offline) validates the ledger, the CSV and every
  citation without needing the files;
- the pre-registrations, code, inputs and results in `audit/`, `experiment/` and
  `lineage/` are complete and reproducible as committed.

Where a primary text was blocked or unreachable, the claim is marked provisional
in `ledger.json` rather than reconstructed. See `README.md` → "Honest gaps".

To restore a full evidence base locally, retrieve the URLs in `ledger.json` into
`sources/` using the file names recorded there.
