# Adversarial synthesis — P09-1 (rank 1, B1 wave 2)

**Date 2026-10-28.** Two independent reviewers (A: construct validity; B: measurement
and decision value), neither an originator, no cross-talk, no literature search.
Both wrote full reviews (`adversarial_P09-1_A.md`, `adversarial_P09-1_B.md`) and both
ran **read-only design probes** on the frozen data. Those probes are indicative
design work, not registered analyses and not results; the reproducible facts among
them are verified below.

**Disposition: REVISE.** Not pause, not external review. The idea survives, but not
in the form that was rated, and it cannot be registered as written.

## Verified facts the reviews rest on

| fact | verified |
|---|---|
| analysis set is 201 canonical rows, not 225 (24 off-vocabulary rows excluded by `^(S\d+)-`) | yes |
| S9 has **3 rows**, S11 has 4; S12 has 31 | yes |
| 69.2 % of core glosses are ≤ 3 words | yes |
| 50 rows (24.9 %) sit in duplicated gloss strings | yes |
| RU, SE and ZA have no canonical rows (they are outside the 25-system matrix) | yes |

The ARI figures in the reviews are their own probes (word vs character n-gram
preprocessing, k grid). They are directionally consistent across both reviewers but
are not audited here; they should be reproduced by the registered code if the idea is
revised.

## What both reviewers found independently

1. **The estimand is mislabelled.** ARI against a partition the same analyst authored
   measures *reliability* of the coding, not *validity* of the grammar. The title
   ("validity, not reliability") is backwards as designed.
2. **The result flips on preprocessing.** Both probes found ARI at k = 14 ranging from
   roughly 0.01 (word TF–IDF) to roughly 0.15–0.19 (character n-grams). Freezing one
   config makes the choice blind, not harmless.
3. **The k-curve has no peak at 14.** One probe found ARI rising monotonically with k
   (0.06 at k = 8 to 0.21 at k = 25), so 14 is not identified by the data; the design
   has no rule for what a flat or monotone curve would mean.
4. **The proposed null is too weak.** Slot-margin permutation has a tiny SD, so an ARI
   of 0.07 is many SD "significant" while recovering about 7 % of the partition. A
   size-matched null gives a much higher chance level. As written, the confirmation bar
   fires on noise and the disconfirmation bar can almost never fire.
5. **The S6/S9 "out-of-sample corroboration" is a level-of-analysis error.** The
   declensions are defined *by* which of S6/S9 is filled, and the mutual exclusivity is
   a system × slot property. Row-level clustering cannot represent it; one probe found
   all three S9 rows landing in a single large mixed cluster.
6. **The 24 excluded rows are where the vocabulary visibly fails.** Dropping them
   removes the disconfirming evidence, and RU has no canonical rows at all.

## Where the reviewers differ

- **A** keeps the re-induction framing and makes a **blind re-gloss** the primary
  analysis, with the original glosses demoted to a reliability check.
- **B** re-scopes the estimand to **granularity and lexical grounding of the slot
  vocabulary** (is 14 right? are the boundaries lexical?), and treats the whole thing
  as a pre-registered multiverse codebook audit with full-grid disclosure.

These are compatible: B's estimand, A's blind coding, one design.

## Required conditions before any pre-registration

1. **Re-scope the estimand** to "granularity and lexical grounding of the slot
   vocabulary". Do not claim to test the validity of the deep grammar; after B3 the
   stem is already system-level and lineage-conditional.
2. **Blind re-gloss is the primary analysis**: ≥ 50 stratified rows re-glossed by a
   party blind to `slot` and to the existing glossary. Original-gloss results become a
   reliability check, not the headline.
3. **Pre-register the full preprocessing × linkage grid** and report median and range
   across it; never a single configuration as the result.
4. **One primary k = 14 with an absolute ARI floor**, plus a pre-registered selection
   rule and pre-committed interpretations for flat / monotone / peaked-away-from-14
   curves. Use a max-statistic null over the grid, not a per-config null.
5. **Stability is co-primary with a veto**: bootstrap or subsample stability of the
   14-cluster solution must clear a floor fixed in advance, or the recovered partition
   is reported as unstable regardless of ARI.
6. **Two nulls, correctly labelled**: size-matched permutation and a shuffled-gloss
   negative control. A null that cannot distinguish "no lexical signal" from "grammar
   imposed" must be reported as *uninformative*, never as disconfirmation.
7. **Fix the analysis set at n = 201 and analyse the 24 off-vocabulary rows as a
   separate block**, coordinated with P11-1. No silent deletion.
8. **Drop the S6/S9 corroboration claim**, or state it as a system-level comparison
   that this design cannot test.
9. **Pre-register the ARI triad** (slot vs system vs a coarse genre collapse) and commit
   in advance to how a genre win is interpreted.

## Consequence for the wave

- **P09-1 remains rank 1 on the frozen matrix** — the review does not re-score it — but
  it is **not registration-ready**, and its cost has risen (blind re-gloss, full grid,
  stability work).
- Its **decision value has moved**: after B3 it can justify keeping or collapsing the
  14-slot vocabulary. It can no longer speak to the stem claim.
- **P10-1, P10-3 and P11-2 are unreviewed.** If the owner prefers one of them, apply
  this same adversarial pass before registration; the review found enough in the
  top-ranked idea to make that non-optional.
- No idea was selected. `decision` remains null in `brainstorm/wave2/matrix.json`.
