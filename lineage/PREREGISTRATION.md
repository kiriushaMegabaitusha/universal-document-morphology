# Pre-registration — B3: from 25 systems to independent origins

**Status: LOCKED before run.** Owner approval: Kyrylo Yasuda, 2026-10-27. Promoted
from the draft `brainstorm/B3_PREREGISTRATION_DRAFT.md` with three changes, all
recorded here: (a) this status header; (b) Revision 1, the four changes forced by
the bounded literature check; (c) Revision 2, the two clarifications forced at code
time. This file, `lineage_blocks.csv`, `mandatory_only.csv`, `lineage_audit.py` and
`DEVIATIONS.md` are committed together; that commit hash and date are the
registration timestamp, the house pattern (`audit/PREREGISTRATION.md`,
`experiment/PREREGISTRATION.md`). No test statistic has been computed and
`results.json` does not exist. There is no external registry; §12 states that
limitation.

**Provenance, stated plainly.** This study is assembled from three ideas that the
ideation session left **unrated and not evidence-checked** (`brainstorm/RESULTS.md`,
post-check ideas P09-2, P11-3, P09-3). No rating round has been run for them. The
bounded literature check required before promotion has now been run and is recorded
in `brainstorm/raw/evidence_B3.md` (verdict: challenge-located — methods mature,
application not located). What is claimed as new is the application to this
corpus's claims, never the method: lineage-aware inference, phylogenetic signal and
"Galton's problem" are mature prior art and are named as such.

**Revision 1 (pre-registration, 2026-10-27, after the evidence check).** Four
changes were made before registration, none after any statistic: the method is
framed as **transmission clustering, not a phylogeny**; Japan moved from the base
lineage to the broad variant (the case documents seal practice, not format
transmission); West African Ajami was settled as its own tradition, not Islamicate
(`cases/west_african_ajami.md`: "neither European nor simply Islamic"); and the
variant rule was rewritten because the original base/narrow split collapsed once
the documented edges were actually listed.

**Revision 2 (pre-registration, 2026-10-27, at code time).** Two clarifications
forced by writing the analysis, neither after any statistic: (a) §6.8's "genre
rule" is **not computable** from the frozen data without a new system-level genre
coding layer, so the exploratory horse race is prevalence vs lineage-mean only;
(b) freezing the mandatory-only matrix shows two systems with no mandatory cell
(HN, PE) — they are kept, and their emptiness is reported, as §4 requires. The
input matrix has not been read for analysis, and no test statistic has been
computed.

## 1. Study information

| field | value |
|---|---|
| title | From 25 systems to independent origins: does the document grammar survive a lineage-restricted re-derivation? |
| project | `05.4_universal_document_morphology` |
| claim under test | README headline findings 1–3; `morphology.md` §3 and §8; `analysis/findings.md` §1–2; `audit/RESULTS.md` (the fork regraded as one joint pattern) |
| population | the 25 slot-coded systems, explicitly as a convenience corpus — **not** a sample of the world's document regimes |
| design | deterministic lineage-level re-derivation of all 14 slots + permutation tests for descent structure + identification bounds + a compelled-requisites re-derivation + estimation |
| data | `analysis/slot_matrix.csv` and `requisites.csv`, both frozen by hash (§4); one new hand-coded table, `lineage_blocks.csv`, frozen before any statistic |
| registration | this file at git commit; no external registry |

Nothing human-subject; ethics: not applicable. No new sources are retrieved; the
study is CPU-only on data already in the repo.

## 2. Background and the problem this study exists to fix

The atlas treats 25 slot-coded systems as 25 observations. They are not
independent: the atlas itself says UA and SU share a Soviet ancestor, DE/UN/EU
inherit Western legal culture, VN is an heir of the Sinosphere, SN and BJ inherit
French administrative practice, and the Islamicate cases share a chancery tradition
(`diversity.md` §1–2, §12–13; `morphology.md` §8). Counting descendants as
independent observations is Galton's problem, and it inflates every "n of 25"
statement — including the registered audit's, whose tradition-blocked sensitivity
already showed the fork's evidence to be a between-tradition contrast
(`audit/RESULTS.md` §5.2).

The audit cannot settle this, because its primary null treats systems as
exchangeable. This study asks the de-duplication question directly, with a
deterministic primary analysis and no reliance on a test that the corpus cannot
power.

**A design fact that shapes everything below.** A lineage-blocked version of the
audit's joint-fork test is *incapable of rejecting at α* at this n: the normative
declension has two carrier systems, so within-lineage placement of those two
systems allows only a handful of distinct patterns, and the attainable p floor is
above 0.05. That test is therefore registered as an **identification bound**, not
as evidence (§6.4). The confirmatory weight sits on the deterministic
lineage-level re-derivation (§6.1), which needs no null to be informative.

## 3. Registered predictions

Fixed now, scored after the run whichever way they fall. Each is conceptual /
operational / statistical.

**R1 (stem survives de-duplication).** *Conceptual:* the universal-stem claim is not
an artefact of counting related systems. *Operational:* number of the six stem
slots (identity, origin, temporal, body, authentication, annex) that are present in
**every** lineage. *Statistical:* predicted 6 of 6.

**R2 (authentication).** *Conceptual:* authentication remains the most widespread
slot after de-duplication. *Operational:* rank of the authentication slot by the
number of lineages in which it is present. *Statistical:* predicted rank 1 (ties
reported, not broken).

**R3 (the fork is not lineage-universal).** *Conceptual:* the genre fork is a
division, so it should not be present in every lineage on both sides.
*Operational:* number of lineages containing at least one S9 (setting/preamble)
carrier. *Statistical:* predicted < the number of lineages, i.e. the normative
declension is absent from at least one lineage.

**R4 (descent structure exists).** *Conceptual:* document form clusters by
transmission. *Operational:* permutation p for the full-profile lineage-clustering
statistic (§6.2). *Statistical:* predicted p < 0.05.

**R5 (the fork's partners are less descent-bound than the surface).** *Conceptual:*
finding 3 — genre, not nation, drives the fork. *Operational:* BH-adjusted q for the
partner-slot clustering statistic (§6.3), against the same statistic on all 14 slots.
*Statistical:* predicted q ≥ 0.05 for the partner profile while R4 rejects — i.e.
overall form is lineage-structured but the fork's six partner slots are not.

**R6 (compulsion is narrower than observation).** *Conceptual:* the stem is what
standards *compel*, not everything they show. *Operational:* the joint-fork exact
test recomputed on a mandatory-only matrix (§6.5). *Statistical:* predicted **not to
reject** (p ≥ 0.05), because removing optional requisites strips the cells the test
needs; this is a prediction about power, and a rejection would be a stronger result
than expected.

**Registered disconfirmation.** If R1 fails — any stem slot absent from any lineage —
the "universal stem" language is regraded to "system-level majority, lineage-
conditional" in a later repo version, with the amendment logged. If R4 and R5 both
reject, finding 3 is regraded as lineage-confounded and the atlas stops describing
the fork as genre-driven without that caveat. Neither regrade is optional and
neither is softened in the write-up.

## 4. Data, freezing and effective n

- `analysis/slot_matrix.csv`, sha256
  `c29d0234ffb657e3c3bc580816c119bd2c439b721489892383cd671a2c74a6a3`
  (25 rows × S1–S14) — the sole matrix input.
- `requisites.csv`, sha256
  `ab501702a4e54bab151859d686bad752e61a3938b809b6b951d07b59990a82cd`
  — input for the mandatory-only matrix (§6.5), not otherwise re-coded.
- **New input, frozen at promotion:** `lineage_blocks.csv`, one row per system with
  its lineage label, the documented basis for the edge, and a confidence flag
  (`documented` / `inferred` / `singleton`). Coding rules in §5. It must be committed
  **before** any statistic is computed, and it must be produced without consulting
  slot values.
- **No exclusions and no re-coding.** Exactly the 25 rows of the frozen matrix. A
  system whose mandatory-only row is empty is kept and reported; it is never dropped
  after inspection. (At freezing, two systems have no mandatory cell: HN and PE.)
- **Effective n.** The number of lineage blocks is reported as the effective sample
  size next to every system-level n = 25. Singleton lineages count as one block each.

## 5. How lineage is coded (the contested part, fixed in advance)

**Definition.** Two systems share a lineage when the atlas documents transmission of
a document-format regime from a common ancestor: a standard, chancery practice or
administrative system adopted by the successor. Shared language, script, religion or
region is **not** enough on its own; it may support an `inferred` edge but never a
`documented` one.

**What a lineage block is not.** It is a **partition, not a tree**. The transmission
literature warns that traits also travel horizontally and that transplants are
modified (`brainstorm/raw/evidence_B3.md`, Q3–Q4), so the blocks are a coarse
stand-in for a graph. They are therefore called *transmission clusters* throughout,
never a phylogeny.

**Rules.**

1. Every system gets exactly one lineage. No system is split.
2. An edge is `documented` only if a case file, `diversity.md`, `morphology.md` or a
   retrieved source states the transmission. The table records the location of that
   statement; an edge without one is `inferred` and cannot be part of the primary
   variant.
3. Contested systems get a provisional singleton and a named alternative.
4. The table is coded slot-blind. If the coder has seen slot values, that is
   disclosed in the commit message.

**Three variants, all pre-registered, all reported** (the specification curve, §6.6).
Counts are the number of blocks, i.e. the effective n:

| variant | rule | blocks | use |
|---|---|---|---|
| **narrow** | documented edges only; the one contested membership (EE) as a singleton | 19 | maximal de-duplication scepticism |
| **base** | documented edges, contested membership included (EE with the Baltics) | 18 | **primary** |
| **broad** | base plus the inferred clusters: Western (DE/UN/EU), Anglophone (IN/NG/KE), Iberian (BR/PE), Sinosphere-Japan | 12 | maximal plausible clustering |

The primary verdict follows **base**. Narrow and broad are never used to rescue a
failing primary result; they are reported as a distribution and the disagreement is
the finding. Note that **base contains no inferred edge**: the atlas documents only
four clusters (Soviet-successor, Francophone-administrative, Islamicate-chancery,
Sinosphere), and everything else is a singleton until the broad variant merges it.

**The table (Appendix A)** is coded from the case files, one citation per documented
edge. It is frozen at promotion, not before; the owner should treat the contested
memberships (EE, Japan, the Western and Anglophone merges) as the review surface.

## 6. Analysis plan (locked)

### 6.1 Primary — deterministic lineage-level re-derivation (no null)

For each of the 14 slots, compute:

- **lineage presence**: number of lineages containing ≥ 1 carrier;
- **lineage universality**: number of lineages in which **every** member carries the
  slot;
- **lineage majority**: number of lineages in which > 50 % of members carry it.

No test, no p-value. The registered decision rule (§8) reads these counts directly.
This is deliberately the primary analysis: at n = 25 with 12–19 lineage blocks, it is
informative where a permutation test is not.

### 6.2 Full-profile lineage clustering (test, single confirmatory)

Statistic **T**: mean simple-matching agreement over within-lineage pairs minus the
same over between-lineage pairs, across all 14 slots.

- Null: lineage labels permuted across the 25 systems, block sizes fixed.
- 100,000 draws, seed `20261101`; p = (k + 1)/(M + 1), one-sided (T ≥ observed). The
  statistic is discrete-but-rich, so no α floor binds; the number of distinct
  label assignments is far larger than the draw count.
- Report T, p, and the null distribution's 2.5/50/97.5 percentiles.

### 6.3 Fork-partner clustering (secondary family, BH)

Same statistic restricted to the six partner slots (authority-mark, destination,
reference, subject, body, trace), and separately on the epistolary indicator
(destination present / absent). Both are tested against the same label-permutation
null, 100,000 draws, seed `20261101`. The family is {§6.3 partner profile, §6.3
epistolary indicator}; BH at α = 0.05, BY reported alongside.

The **normative** side of the fork carries two systems; no lineage-restricted
inference about it is possible at this n. That is reported as an identification
limit, not tested (§6.4).

### 6.4 Identification bounds (no verdict)

Recompute the audit's joint-fork and implication tests under a lineage-blocked null.
For each, report the **attainable p floor** — the smallest p the corpus can produce —
next to the observed p. Registered reading: if the floor exceeds α, the result is
"not identifiable at n = 25", never "not supported". This section exists to stop a
foregone non-rejection being read as evidence against the fork.

### 6.5 Compelled-requisites re-derivation

Build `mandatory_only.csv` by a frozen deterministic rule: cell (system, slot) = 1
iff at least one row of `requisites.csv` for that system and slot has
`obligation == "mandatory"`. Then repeat:

- the 14-slot lineage counts of §6.1;
- the joint-fork exact test and the six per-edge depletion tests, exactly as
  registered in `audit/PREREGISTRATION.md` §6 with that registration's corrections;
- system-level and lineage-level prevalence.

Report row sums; cells lost to the restriction are the finding, not a defect.

### 6.6 Specification curve (reporting, not a test)

Every combination of {base, narrow, broad} × {all requisites, mandatory only} is
reported for R1, R3, R4 and §6.5's joint test. No specification is selected after
the fact; the curve is the result.

### 6.7 Estimation (descriptive, pre-specified rule)

Clopper–Pearson 95 % intervals for each slot's system-level prevalence, and the
lineage-level proportion with its exact interval over blocks. **Rule fixed now:** a
census statement in the prose may be written as "most systems" only if the interval's
lower bound exceeds 0.5; otherwise it is written as "a plurality" / "just over half"
with the interval quoted. This rule is applied mechanically; it is not a test.

### 6.8 Exploratory (clearly labelled, no error-rate control)

A leave-one-system-out horse race on the 14-slot profile: **prevalence baseline vs
lineage-mean rule**, scored by Brier score, with a label-shuffle reference. This is
the "hold-out prediction" idea from the backlog. It carries **no confirmatory
claim**: n = 25, and the lineage rule's predictors are partly the coding itself, so
any win is descriptive. (A genre rule was drafted and dropped at code time: the
frozen data carry no system-level genre variable, and inventing one now would be a
new coding layer, not a robustness check.)

## 7. Multiple testing

- §6.2 is a single confirmatory test — no correction.
- {§6.3 partner, §6.3 epistolary} is one family — BH at α = 0.05, BY reported.
- §6.1, §6.4, §6.5, §6.6, §6.7 carry no p-value verdicts and are not corrected.
- §6.8 is exploratory and never enters a correction family.

## 8. Decision rules

| outcome | rule |
|---|---|
| R1: every stem slot present in every lineage | stem **survives de-duplication**; reported with the number of lineages as n_eff |
| R1: any stem slot absent from a lineage | stem **regraded** to lineage-conditional in a later version; amendment logged |
| R4 rejects (p < 0.05) | descent structure exists; n_eff becomes the headline n for every convergence claim |
| R4 does not reject | "no detectable descent structure at n = 25" — never "no descent" |
| R5 rejects after BH | the fork's partner slots are lineage-confounded; finding 3 regraded with that caveat |
| R5 does not reject | finding 3 **survives this challenge**; this removes one confound, it does not prove independence |
| §6.4 floor > α | "not identifiable at n = 25" for that claim; no inference either way |
| R6 not rejecting | the stem is compelled-but-narrower; report which slots survive |
| R6 rejecting | the fork holds under compulsion — a stronger result than predicted |
| variants disagree | all reported; the primary verdict follows base; disagreement discussed |

Verdicts are three-valued: **supported / regraded / not identified**. Nothing is
rounded into a verdict; a floor-bound result is reported as not identified.

## 9. Assertions before any test

1. Both input hashes match §4; mismatch stops the run.
2. Row count = 25; column set = S1…S14.
3. `lineage_blocks.csv` covers exactly the 25 systems, one lineage each, and every
   `documented` edge carries a citation string; a `documented` edge with no citation
   fails the run.
4. The mandatory-only matrix is regenerated from `requisites.csv` and asserted equal
   to the committed `mandatory_only.csv`.
5. The permutation script reproduces a stored check value on a synthetic frame
   (self-test), never on the real matrix.

## 10. Contingencies

| contingency | response |
|---|---|
| hash or row/column mismatch | stop; amendment before any test |
| a documented edge cannot be sourced | downgrade it to `inferred` **before** freezing, or drop it; never after a statistic is seen |
| base variant leaves < 6 lineages | report the effective n, proceed; the coarseness is the finding, not a reason to re-code |
| a slot has < 2 carriers anywhere on the mandatory-only matrix | report "not testable at these margins"; never impute |
| permutation script fails on the synthetic frame | stop; no real-data run until it passes |
| literature check finds a prior application to a comparable corpus | contribution framing narrowed to this corpus; logged, not hidden |

## 11. Open conditions before promotion

1. **Bounded literature check** — **done** (`brainstorm/raw/evidence_B3.md`;
   challenge-located: methods mature, application not located). It changed the
   variant rule, JP's placement and WA's status, all recorded as Revision 1.
2. **Lineage table coded and cited edge by edge**, slot-blind — **done and signed
   off** (`lineage/lineage_blocks.csv`).
3. **Analysis code self-tested** on a synthetic frame before the real matrix is read
   — **done**: `python3 lineage/lineage_audit.py --self-test` passes (block
   algebra, deterministic counts, clustering on strong vs random fixtures,
   Clopper–Pearson, fork machinery, floor behaviour, citation gate, mandatory-matrix
   rule, holdout, prevalence). The real matrix has not been read.
4. **Frozen derived inputs** — **done**: `python3 lineage/lineage_audit.py
   --freeze-inputs` wrote `lineage/mandatory_only.csv`; it computes no statistic.
5. **Owner approval of this text**, including whether §6.8 stays in scope — **given
   2026-10-27**; §6.8 stays, reduced to the two computable models (Revision 2).

## 12. Deviations and limitations

Deviations follow the house rule: what changed, why, effect on severity, effect on
validity; both analyses reported; the registered one is never replaced. Log created
at promotion (`DEVIATIONS.md` in the study directory).

1. **Convenience corpus.** Inference is conditional on the atlas's sampling frame,
   which was shaped by open-web retrievability.
2. **Lineage is hand-coded and contestable.** It is frozen before computation to
   prevent tuning, not because it is ground truth. The three variants exist because
   the coding is arguable — and the base variant has only four documented clusters,
   so most systems sit alone, which is itself a finding about the corpus.
3. **Small blocks, little power.** Singletons contribute no within-lineage pairs;
   base leaves ten within-lineage pairs at most, against hundreds between. Blomberg
   et al. report power ≈ 0.8 for phylogenetic signal at 20+ species, but that is per
   species, not per block, and cannot be transferred to 25 systems in 12–19 blocks
   (`brainstorm/raw/evidence_B3.md`). This is exactly why the deterministic analysis
   is primary and the permutation test is one confirmatory test, not the whole
   study. Coarseness is reported, never repaired by re-coding after inspection.
4. **The normative declension is untestable at this n.** Two carriers. Stated
   everywhere the fork is discussed.
5. **Coding treated as fixed.** A coding convention that correlates with lineage
   would masquerade as descent; that is a separate layer (P06-1) and is not modelled.
6. **Prior art.** Lineage-aware inference is established; novelty is claimed only for
   its application to this corpus and its specific claims. Absence of a located prior
   application is not evidence that none exists.
7. **No external registration; analyst = code author.** A git commit is auditable
   but not a third-party timestamp.
8. **Disclosure.** While verifying the matrix schema, the analyst viewed the header
   and two sample rows. The lineage table is derived from historical/transmission
   prose, not from slot values; if the owner wants stricter blindness, the table
   should be coded by someone who has not seen the matrix.
9. **A partition is not a transmission history.** Clusters are a coarse stand-in for
   a graph: traits travel horizontally, transplants are modified, and a successor can
   diverge by political choice (`cases/soviet_bloc.md:90`). The method literature
   says so explicitly (`brainstorm/raw/evidence_B3.md`, Q3–Q4). Results are therefore
   about *clustering by assigned lineage*, not about ancestry.
10. **Lineage by domain.** The legal-origin literature finds origins predict some
   legal substance and not others (`brainstorm/raw/evidence_B3.md`, Q4). Document
   *format* is not legal *substance*, so a null result here would not license a
   general claim that descent does not matter — only that it is not detectable in
   these 14 slots at this n.

---

## Appendix A — lineage table as coded (frozen at promotion)

`documented` = the atlas states the transmission, with the location given;
`documented-singleton` = the case says the tradition is its own; `unresolved` = no
statement in the corpus, so a singleton in base and a named merge in broad.
Machine-readable copy: `lineage/lineage_blocks.csv`.

| lineage (base) | systems | basis |
|---|---|---|
| soviet-successor | SU, UA, EE | `cases/soviet_bloc.md:5` (ancestor of ГОСТ Р 7.0.97 and ДСТУ 4163), `:90` (the Baltics inherited the same ancestor) |
| francophone-administrative | FR, SN, BJ | `cases/francophone_tradition.md:3`, `cases/sn.md:4`, `cases/bj.md:3` |
| islamicate-chancery | IS, SA, AE | `cases/islamic_chancery.md:1-16`, `cases/sa.md:5`, `cases/ae.md:31-37` (Saudi guide re-hosted as a regional template, same MD5) |
| sinosphere | CN, VN | `cases/vn.md:8` ("heir of the Sinosphere") |
| ethiopian-chancery | ET | `cases/et.md:25-26` (non-colonial state chancery) |
| thai-chancery | TH | `cases/th.md:44` (a bureaucracy standardising its own correspondence) |
| west-african-ajami | WA | `cases/west_african_ajami.md:3` ("neither European nor simply Islamic") |
| haudenosaunee | HN | `cases/wampum.md` (non-documentary record system; boundary case) |
| unresolved singletons | DE, UN, EU, IN, NG, KE, BR, PE, JP, ID | no transmission statement in the case file (see the CSV for the per-row note and the named broad-variant merge) |

Variant changes, fixed now: **narrow** moves EE to a singleton; **broad** merges
{DE, UN, EU} → western-legal, {IN, NG, KE} → anglophone-administrative, {BR, PE} →
iberian-notarial, and JP → sinosphere.

Three Appendix-A questions were settled by the evidence check and the case files,
and are recorded so they are not re-litigated after results: (a) IN/NG/KE and BR/PE
have **no** documented edge in the atlas, so they are singletons in base and merges
in broad only; (b) UN/EU are **not** a descent group on the atlas's own evidence —
`morphology.md:163` calls it shared legal culture, which the coding rule classes as
`inferred`; (c) West African Ajami is **not** Islamicate — the case says so
explicitly.

## Appendix B — promotion checklist

- [x] literature check run and recorded (`brainstorm/raw/evidence_B3.md`)
- [x] lineage table cited edge by edge, slot-blind (`lineage/lineage_blocks.csv`)
- [x] owner sign-off on contested memberships (EE, Japan, the broad merges)
- [x] analysis script self-tested on synthetic data; real matrix never read
- [x] `mandatory_only.csv` frozen from `requisites.csv` (no statistic computed)
- [x] `lineage_blocks.csv` and `mandatory_only.csv` in the study directory, committed with this file
- [x] this text amended where the owner requires
- [ ] registered by commit; then run once; deviations logged
