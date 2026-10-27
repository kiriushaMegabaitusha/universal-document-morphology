# Results — B3 lineage-restricted re-derivation (registered run)

**Registration:** commit `bfd6ffc`, 2026-10-27, `PREREGISTRATION.md` · **Run:**
executed once, immediately after registration, exit 0 · **Deviations:** none
(`DEVIATIONS.md`) · **Inputs:** both sha256 hashes verified by the script; 25 rows;
`mandatory_only.csv` regenerated from `requisites.csv` and asserted equal ·
**Arithmetic:** exact `Fraction` for every hypergeometric and BH/BY value; the
clustering tests are 100,000 label permutations, seed `20261101`; Clopper–Pearson by
bisection on the binomial CDF · **Machine output:** `results.json`.

**Pipeline sanity check.** The unblocked joint-fork test reproduces the audit
exactly: p = **1/30 = 10/300**, the same value reported in `audit/RESULTS.md`. Two
independently written scripts agreeing on that number is the check that this
pipeline reads the same matrix the same way.

## Decision table (§8)

| prediction | registered | observed (base) | verdict |
|---|---|---|---|
| **R1** stem present in every lineage | 6/6 | **0/6** | **not confirmed — regrade required** |
| **R2** authentication rank 1 by lineages | rank 1 | **13/18 lineages, 17/25 systems — rank 1** | confirmed |
| **R3** the fork is not lineage-universal | S9 absent from ≥1 lineage | **2/18 lineages carry S9** | confirmed |
| **R4** descent clustering, p < 0.05 | p < 0.05 | **p = 0.518; T = −0.062** | **not confirmed** |
| **R5** partner slots not clustered (q ≥ 0.05) | q ≥ 0.05 while R4 rejects | **q = 1.00; R4 did not reject** | partial — see below |
| **R6** mandatory-only fork does not reject | p ≥ 0.05 | **p = 6/25 = 0.24** | confirmed |

R5's directional prediction held (the partner slots are not lineage-clustered), but
its premise did not: it was framed as a contrast against a rejecting R4, and R4 did
not reject. It is reported as **not interpretable as framed**, not as support.

## R1 — the stem does not survive de-duplication

Both registered readings agree, which matters because the draft defines two:

- **presence** (≥1 carrier per lineage): **0 of 6** stem slots;
- **universality** (every member of every lineage): **0 of 6**.

Base variant, 18 lineage blocks, all requisites:

| slot | systems (of 25) | lineages present (of 18) | lineages universal (of 18) |
|---|---:|---:|---:|
| S1 identity | 11 | 8 | 5 |
| S3 origin | 8 | 7 | 4 |
| S5 temporal | 8 | 6 | 3 |
| S10 body | 14 | 11 | 8 |
| S12 authentication | 17 | 13 | 11 |
| S13 annex | 9 | 8 | 4 |

No stem slot is present in every lineage under either definition. This is the
registered trigger for the regrade: the "universal stem" is a **system-level
regularity, not a lineage-invariant one**.

## R4 — no detectable descent clustering

| variant | blocks | T | permutation p |
|---|---:|---:|---:|
| narrow | 19 | +0.375 | 0.356 |
| **base** | **18** | **−0.062** | **0.518** |
| broad | 12 | −0.306 | 0.687 |

T is the within-lineage minus between-lineage agreement on the 14-slot profile. It
is **negative** in base and broad: systems in the same documented lineage are, if
anything, slightly *less* similar than systems in different lineages. Under the
narrow variant T is positive but not distinguishable from the null.

Partner-slot clustering and epistolary clustering are likewise null (BH q = 1.00 in
base; 0.92–0.95 in the other variants). The exploratory holdout agrees: the
lineage-mean predictor is **worse** than the prevalence baseline (Brier 0.2755 vs
0.2321, delta +0.0433; label-shuffle p = 27/91 ≈ 0.30).

## Identification bounds (§6.4, no verdicts)

- **Joint fork, lineage-blocked:** narrow and base admit **one** within-block
  placement of the S9 pair (both carriers sit in singleton blocks), so p = floor =
  **1/1**: structurally **not identifiable**. Broad admits 3 placements: p = 1/3
  (all requisites), 2/3 (mandatory), floor 1/3 — still uninformative.
- **Implications, lineage-blocked** (no verdict by §7): base S6⇒S12 p = 2/9
  (floor 1/9); S6⇒S8 p = **1/27** (at the floor); S6⇒S10 p = 2/27 (floor 1/27);
  S8⇒S12 p = 2/9 (floor 1/9). S6⇒S8 is the only rule that reaches its enumeration
  floor; it carries **no confirmatory claim** and is flagged for the owner rather
  than read as a result.

## Compelled requisites (§6.5)

Mandatory-only matrix: 25 rows, 150 mandatory requisites; **HN and PE have no
mandatory cell** and are kept, as registered.

- joint fork: p = **6/25 = 0.24** — does not reject, as predicted (R6);
- S9 carriers drop to **1** system, so R3's contrast survives the restriction;
- S12 is present in 13 of 18 lineages on the full matrix and in fewer on the
  mandatory one; the compulsory core is narrower than the observed pattern.

## Estimation (§6.7) — the prose rule bites

S12 authentication, the best slot:

| level | n | proportion | 95 % Clopper–Pearson | "most systems" licensed? |
|---|---:|---:|---|---|
| systems | 17/25 | 0.680 | 0.465 – 0.851 | **no** |
| lineages | 13/18 | 0.722 | 0.465 – 0.903 | **no** |

The pre-registered rule (§6.7) requires a lower bound above 0.5 for "most systems".
Neither level clears it. The count "17 of 25" may be quoted; "most systems", "the
most universal slot" as a majority claim, may not.

## Specification curve (§6.6)

| variant | matrix | stem present in all | S9 lineages | clustering p | fork p (unblocked) | fork p (blocked) |
|---|---|---:|---:|---:|---:|---:|
| narrow | all | 0/6 | 2/19 | 0.356 | 1/30 | 1 (floor 1) |
| narrow | mandatory | 0/6 | 1/19 | 0.566 | 6/25 | 1 (floor 1) |
| **base** | **all** | **0/6** | **2/18** | **0.518** | **1/30** | **1 (floor 1)** |
| base | mandatory | 0/6 | 1/18 | 0.596 | 6/25 | 1 (floor 1) |
| broad | all | 0/6 | 1/12 | 0.687 | 1/30 | 1/3 (floor 1/3) |
| broad | mandatory | 0/6 | 1/12 | 0.656 | 6/25 | 2/3 (floor 1/3) |

Every specification agrees on the two headline facts: the stem is not
lineage-universal, and there is no detectable lineage clustering.

## Reading (interpretation, clearly labelled)

1. **The universal stem is a system-level regularity.** It does not survive
   de-duplication under any variant. This is the outcome the registration
   pre-committed to regrade.
2. **Descent does not explain the pattern either.** No clustering, and a slightly
   negative signal in the primary variant. Document morphology in this corpus does
   not track the transmission clusters the atlas itself documents.
3. **Authentication survives best** (rank 1, 13/18 lineages) but not as a majority
   claim under the registered CI rule.
4. **The genre fork is not lineage-universal** (2/18 lineages), consistent with
   finding 3; but the lineage-blocked tests cannot add evidence, by construction.
5. **Compulsion narrows the picture** (R6): restricting to mandatory requisites
   loses the joint-fork signal entirely.
6. Taken together, the results weaken both available explanations — universal
   grammar and descent — and leave instrument type / genre / function as the
   remaining candidate, which this study cannot test.

## What this does not show

- **Not** that descent is irrelevant: the partition is coarse (only four clusters
  are documented), the blocks are small, and the method literature warns that
  transmission is graph-like, not a partition (§12.9–.10).
- **Not** convergence: nothing here shows the stem arises independently.
- **Not** a verdict on the blocked implications: §6.4 carries none by registration.
- **Not** generalisable beyond the convenience corpus.

## Consequence for the atlas (required by §8)

R1 failed, so the registered decision rule requires a prose regrade in a later
version: **"universal stem" → "system-level majority, lineage-conditional"**, with
the amendment logged. The proposed minimal edits are in `PLAN.md` as the next
owner decision; this results file does not edit the frozen atlas prose.

**Deviations: none.** One clarification for the record: R1 was computed under both
the presence and the universality definition because the draft uses both; they agree
at 0/6, so no choice between them affects the verdict.
