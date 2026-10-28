# Licensing

This repository uses two licences, split by what the file is.

| material | licence | file |
|---|---|---|
| Software: Python gates and analyses (`check_claims.py`, `analysis/recompute.py`, `audit/null_audit.py`, `lineage/lineage_audit.py`, `experiment/*.py`, `brainstorm/*.py`), workflows | **MIT** | `LICENSE` |
| Atlas content: prose (`README.md`, `morphology.md`, `diversity.md`, `STANDARDS.md`, `EXECUTIVE_SUMMARY.md`, `PLAN.md`, `cases/`), coded data (`requisites.csv`, `ledger.json`, `analysis/*.csv`), pre-registrations, results, and the teaching page (`education/`) | **CC BY 4.0** | `LICENSE-CONTENT` |
| Retrieved third-party sources | **not covered** — their own terms | see below |
| Archify viewer runtime embedded in the teaching page | **Apache-2.0** | `third_party/ARCHIFY-LICENSE.txt` |

## What this means in practice

- **Reuse the code** under MIT: keep the copyright notice and permission text.
- **Reuse the atlas** under CC BY 4.0: any use, including adaptation, with
  attribution. Suggested form:

  > Universal document morphology (05.4), Kyrylo Yasuda, CC BY 4.0 —
  > https://github.com/kiriushaMegabaitusha/universal-document-morphology

- If you quote a coded figure or a case finding, cite the repository and, where
  the atlas itself cites a source, keep that citation. CC BY covers this
  repository's expression, not the underlying standards.

## What is not licensed here

- **`sources/`** in the private working copy holds retrieved standards, manuals
  and archival pages. Those are third-party works with their own rights. The
  public repository does not redistribute them; every URL is in `ledger.json`.
  Nothing in this repository's licences grants rights over them.
- **The Archify runtime** inside `education/official-documents-explainer.html`
  is © tt-a1i and contributors, Apache-2.0; its notices are preserved in the
  file and in `THIRD_PARTY_NOTICES.md`.

## A note on the split

A single licence cannot sensibly cover both a Python gate and an essay. MIT is
the conventional choice for the tooling and asks only for attribution; CC BY 4.0
is the conventional choice for research prose and data and also asks only for
attribution, while explicitly permitting adaptation. Neither adds a
non-commercial or share-alike restriction.
