# Adversarial review B — P09-1 (vocabulary re-induction)

**Reviewer: B (non-originator) | Lens: measurement and decision value | Date 2026-10-28**
**Idea under review:** P09-1, "Validity, not reliability: can the 14-slot deep grammar be re-induced from the requisites themselves?" (`brainstorm/raw/P09.md`).
**Status per PROTOCOL:** open. Evidence status: `not-checked` — no literature search was run for this review.

Method note: everything numeric below comes from a read-only stdlib probe I ran on the frozen
`requisites.csv` (average-linkage agglomerative clustering on cosine distance over TF–IDF
features; ARI/NMI recomputed from contingency tables; permutation nulls with 200–2000 draws).
The probe is a feasibility check, not a result, and it is not committed to the repo.

---

## 1. Strongest version of the idea

Strip the reliability framing and state the claim P09-1 is actually testing. The atlas asserts
a 14-slot deep grammar of official documents. Every existing warrant for it is internal: the
slots were defined by the analyst, then applied by the analyst, and the B3 re-derivation re-reads
the same coded rows. So the strongest version is:

> If S1–S14 are functional kinds rather than filing labels, then the *descriptions* of requisites
> — the field terms and their short renderings, recorded across 25 systems and many languages
> before any cluster was computed — should carry recoverable cluster structure, and the recovered
> structure should approximate the codebook without being given it. If it does not, the 14 slots are an analyst's filing system and every
> prevalence figure in the atlas is a statement about that filing system, not about documents.

That is a real question, and it is the only question in this wave that can embarrass the atlas
from the inside. Two design choices make the strongest version sharper than the text in P09:

- **The estimand should be granularity, not agreement.** The live decision after B3 is not
  "is the grammar real" (that has been moved to system level) but "is 14 the right number of
  slots, and are the boundaries where we say they are". A clustering study can answer that.
  An ARI-against-the-codebook study cannot, because ARI answers "did you recover my labels",
  which is the wrong question.
- **The design should be a pre-registered multiverse, not a protocol.** The defensible version
  fixes the *entire* preprocessing grid in advance and reports the distribution of outcomes.
  This is the only version in which the researcher's degrees of freedom (tokenisation,
  n-gram range, weighting, linkage, distance) are neutralised by disclosure rather than by a
  promise. My probe shows why this is not optional: see §4.

With those two changes the idea becomes a cheap, honest, publishable methods result: *the
lexical evidence supports a coarser and partly different partition than the codebook, and here
is the whole grid*. That is worth having.

## 2. Observation that would count against it

Two distinct observations, and P09-1 currently names only the weaker one.

**(a) The stated disconfirmation is nearly unreachable.** P09 says the idea dies if ARI/NMI is
"statistically indistinguishable from the fixed-margin null at every frozen k". On this data
that null has a standard deviation of 0.004–0.008 in ARI, because a 14-way partition of 201
rows with sizes 3–31 has almost no permutation variance. Anything that clusters at all clears
it. In my probe the *word* feature gave ARI = 0.008 and still returned p = 0.030 against the
free slot-margin null; the *char-4* feature gave ARI = 0.152, p = 0.005. A criterion that is
satisfied by ARI = 0.008 is not a criterion.

**(b) The observation that should count against it is instability of the recovered partition
itself.** If the 14-cluster solution is not reproducible under resampling, then ARI against the
codebook is a draw from a distribution centred near zero, and no value of it — high or low —
supports a claim about the grammar. In my probe the bootstrap ARI of the recovered 14-way
partition against itself is **0.32, 0.42, 0.54, 0.52, 0.37** across five resamples. The usual
consensus bar for "these clusters exist" is ~0.75. So the solution the study would align to
S1–S14 is itself about half noise. That is the disconfirming observation the pre-registration
must name: *recovered-cluster stability below the pre-set threshold, at every k in the grid,
with ARI-vs-codebook reported but uninterpretable*.

## 3. Alternative explanations

At least four, and the design as written separates none of them.

**A1 — The codebook is a paraphrase of the glosses.** The same analyst wrote `gloss_en` and
assigned `slot`, and the glosses frequently reuse the slot's own vocabulary: "Addressee" (S6),
"Signature"/"Seal" (S12), "Date" (S5), "Body" (S10). Recovering clusters from those strings is
recovering the analyst's word choices, not the documents' functional structure. This is
circularity, and P09 acknowledges it only as "an explicit sensitivity". It is not a sensitivity;
it is the whole mechanism. Any positive ARI is compatible with A1, and any negative ARI is
compatible with "the analyst paraphrased inconsistently". The study cannot distinguish
"slots are real" from "glosses are slot-flavoured".

**A2 — Lexical coherence is local, not global (the granularity alternative).** My probe finds
strong local signal and weak global structure at the same time: nearest-neighbour same-slot
purity across *different systems* is **68%** against 9.4% chance, yet ARI at k = 14 is 0.15 and
the recovered 14-cluster solution contains a 1-row and a 2-row cluster, spreads S12 across at least four
clusters (15/8/4/3) and S14 across four, and merges S1 with S13 at 5/5. Read plainly: the
requisites cluster into a *coarser* set of lexical families (header/marks, date-place, addressee,
subject, body, signature, annex), and the 14-way split subdivides some of those families by
vocabulary that has nothing to do with function ("Digital document container (ASiC-E)" sits in
S12 next to "Complimentary close"). The deep grammar may be ~6–8 kinds, not 14. This is a
finding the study should be able to return, and the current design treats it as failure.

**A3 — Script and template, not slot.** 123 of 201 canonical rows have non-Latin `local_term`
(52 Cyrillic, 19 Arabic, 16 CJK). "local_term + gloss_en" is therefore not a common feature
space: a word tokeniser silently drops 60% of the local terms, while a character-n-gram
tokeniser turns script into a near-perfect proxy for system. Under the system-preserving null
(permute slot labels only *within* each system), the word-feature result collapses to p = 0.303
while char-4 survives at p = 0.005 — i.e. one defensible feature set is largely measuring
within-system template repetition. A study that reports one configuration cannot tell A3 from
a slot effect.

**A4 — Genre, not slot.** S12 is 31 rows and is mostly "signature/seal/close"; correspondence is
30 rows of the corpus and is where salutations and closings live. A cluster of closing formulae
is equally explained by genre. Because genre is a column in the same CSV and is never held
constant or modelled, every cluster can be re-described as a genre cluster.

## 4. Measurement or analysis failure

This is where the idea fails hardest, and the failures are specific.

**4.1 The headline number is decided by an arbitrary preprocessing choice.** Same data, same k,
same algorithm, two defensible feature sets:

| features | ARI(14) | NMI(14) | reading |
|---|---|---|---|
| word tokens, TF–IDF | **0.008** | 0.212 | "null-level" — the stated disconfirmation is met |
| char 4-grams, TF–IDF | **0.152** | 0.422 | "clearly above null" — the prediction is met |

The gap between these two numbers is larger than either effect. Pre-registering one of them
converts a coin flip into a finding. This is the cheapest possible kill and the cheapest
possible fix (pre-register the grid and report the median and range). Without it the study has
no measurement model, only a preference.

**4.2 The k-curve has no peak at 14, so k = 14 is not identified.** Char-4 ARI rises
monotonically: 0.059 (k=8), 0.112 (10), 0.120 (12), 0.152 (14), 0.157 (18), 0.196 (20), 0.206
(25). Word ARI rises 0.000 → 0.105 over the same range. There is no elbow, no maximum at 14,
and no penalised criterion in the design. Under P09's own prediction this is "graded
recoverability"; under any selection rule it is "the number of clusters is unidentified". Both
cannot be true, and the pre-registration must decide in advance which reading governs. As it
stands, the design has 20 k-values × N preprocessing configs and no multiplicity control: the
analyst will find a cell with ARI 0.4 and call it confirmation.

**4.3 The wrong null, and the wrong use of NMI.** The fixed-slot-margin permutation null is
degenerate here (sd 0.004–0.008) and rejects everything, so "p < 0.05" carries no information.
The informative null is partition-size-matched: draw random partitions with the observed
cluster-size profile. I ran it — ARI mean 0.000, sd 0.008, so the observed 0.152 is z ≈ 20.
Significance is trivially achieved; *magnitude* is the question, and the design never sets a
magnitude threshold. For NMI the same null gives mean **0.178**, sd 0.014 — so the reportable
NMI of 0.42 is 0.24 above a null that already looks substantial. Reporting "NMI = 0.42,
p < 0.01" without the size-matched null would overstate the result by roughly a factor of two
in the reader's mind.

**4.4 The n is wrong in the statement and the fix prejudges another idea.** P09-1 says "cluster
the 225 requisites". 225 is the whole file; **201** rows are in canonical slots and **24** are
off-vocabulary (`meta-structure` 10, `rank-modifier` 4, `mixed` 3, `infrastructure` 3,
`structural` 2, `access` 2). If the 24 are included, the target partition has 20 labels and
"14" is undefined; if silently dropped, the study discards 11% of the corpus — precisely the
rows where the vocabulary strains, and precisely the rows P11-1 is rated to analyse. These two
ideas are in direct conflict, and P09-1 must not resolve it by deleting the evidence.

**4.5 The data are too thin for the objects being claimed, in three specific places.**
S9 has **3** rows ("Justification/recitals", "Legal-basis citations", "Recitals"), S11 has 4,
S7 has 9. A 3-row cluster can contribute at most 3/201 to ARI; no statement about "S9 floating
between clusters" is evidence — it is arithmetic. The predicted "S6-group vs S9-group separate
as branches without being seeded" is therefore untestable, and the claim that this "re-tests
finding 2 out of sample for free" is false: all 11 S6 rows and all 3 S9 rows were coded
by the same hand from the same glosses. That is in-sample, not out of sample.

**4.6 Interpretive cost is unbounded and unfalsifiable.** The compute is trivial (my whole probe
ran in minutes). The expensive step is "align the recovered clusters to S1–S14", which requires
a human to name 14 clusters per configuration; at 30–45 min each over a grid of 14 configs that
is 10–15 analyst-hours, and the naming is exactly where researcher degrees of freedom re-enter
after the "frozen vocabulary" promise. If the project instead drops interpretation (label-invariant
indices only), the study becomes ~2 days of work — but it also loses the only part a reader can
act on. That tension is the real cost, and P09-1 does not price it.

## 5. Prior evidence (not-checked)

`not-checked`. No search was run for this review, and nothing below is asserted as located
evidence — it is what a search would have to address before any novelty or absence claim:

- Whether unsupervised re-induction of a document-structure ontology from field labels has been
  published in document/genre studies, diplomatic editing, or records management (the claim
  "first recoverability test of an official-document slot ontology" is exactly the kind of
  absence claim a bounded search can fail to support).
- Whether cluster-stability thresholds (the ~0.75 consensus figure I use above) are the ones a
  reviewer would accept, and what the standard practice is for reporting ARI under unbalanced
  partitions.
- Whether short-string multilingual clustering has documented failure modes at n ≈ 200 that
  would make the whole exercise a known negative result.

The design does not depend on novelty, so `not-checked` does not block the idea — but the
"first" language in P09.md should not survive into a pre-registration.

## 6. Disposition

**Revise — and re-scope from "validity of the deep grammar" to "granularity and lexical
grounding of the slot vocabulary", a codebook-diagnostics study with a pre-registered
multiverse.**

Reasons, in order of weight:

1. The estimand no longer matches the claim. After B3 the stem is a system-level prevalence
   statement; a row-level clustering of 201 glosses cannot confirm or refute it. A null result
   would show that the *glosses* do not encode the slots lexically — a coding-manual finding,
   not a finding about documents. A positive result would show that the analyst's paraphrases
   resemble the analyst's labels. Neither moves a headline.
2. What decision value remains is real but different: whether to keep 14 slots or collapse to
   ~6–8 in the next version. My probe suggests the data support a coarser partition, which
   makes the study worth doing *if and only if* the pre-registration states in advance which
   vocabulary change each outcome licenses.
3. As specified, the outcome is decided by an unstated preprocessing choice (0.008 vs 0.152) and
   the k-curve is monotone, so the design has no measurement model and no selection rule.

It does not need external review. The data are frozen, no humans are involved, the compute is
minutes, and the failure modes are all fixable by writing things down before running. But it
should not be pre-registered in its current form, and it should not be described as a validity
test of the deep grammar.

## 7. Required conditions before any pre-registration could be accepted

1. **Restate the estimand as granularity.** The pre-registration must say that the object is the
   number and boundaries of slots, not "is the grammar valid", and must name the vocabulary
   decision each outcome licenses (retain 14 / merge to a specified coarser set / split a named
   slot). A study whose every outcome leaves the codebook unchanged has no decision value.
2. **Pre-register the full multiverse, not one configuration.** Enumerate every cell of
   {word tokens, char 3/4/5-grams} × {binary, sublinear TF} × {cosine, jaccard} × {average,
   complete, ward linkage}, state the aggregation rule (median and range of ARI across cells),
   and report all cells. One config is a coin flip; the grid is the measurement.
3. **Pre-register the k-selection rule and the flat-curve reading.** Name the penalised criterion
   (silhouette, gap, or a bootstrap-stability maximum) and fix the conclusion for each shape in
   advance: monotone increasing ⇒ "14 is not identified"; peaked away from 14 ⇒ the vocabulary is
   mis-specified and the peak is reported; flat ⇒ power failure, no claim. State the multiple-
   comparison correction over k × configs, or declare the study descriptive and forbid a
   "significant cell" claim.
4. **Replace the primary null.** Use a partition-size-matched null for both ARI and NMI, report
   NMI's null mean (≈0.18 here) alongside the observed value, and demote the free slot-margin
   permutation to a footnote. Add the within-system null and report it: if the result does not
   survive it, the finding is template repetition, not slot structure.
5. **Make cluster stability co-primary with a veto.** Pre-register bootstrap and split-half ARI
   of the recovered partition, and state that a solution below the chosen stability threshold
   (justify the number) cannot support any claim about k or about slot recovery, regardless of
   its ARI against the codebook.
6. **Fix n and the off-vocabulary rows explicitly.** 201 canonical rows are the primary corpus;
   the 24 off-vocabulary rows are analysed as a separate block, not deleted and not folded into
   a 20-label target. Coordinate with P11-1 rather than pre-empting it.
7. **Fix the feature space across scripts.** Either drop `local_term` from the primary features
   (gloss-only) or pre-register a script-stratified analysis, and report how much of the result
   is carried by the 78 Latin-script rows. "local_term + gloss_en" as a single string is not
   comparable across 123 non-Latin rows.
8. **Retire the two claims the data cannot support.** Delete "re-tests finding 2 out of sample"
   (S6/S9 were coded from the same glosses by the same hand; S9 has 3 rows) and delete "first
   recoverability test" until a bounded search supports it.
9. **Cap and price the interpretive step.** Either (a) no semantic naming of clusters at all —
   label-invariant indices only, ~2 days of work; or (b) pre-register a naming protocol, a
   time budget, two blind namers and their agreement, and report the cost. Unbounded
   post-hoc interpretation is where the frozen-vocabulary promise dies.
10. **State the too-thin stop rule in advance.** Define what outcome is reported as "the data are
    too thin to identify k" and commit to publishing that as a methods note with no claim about
    the grammar. My probe suggests this is a live outcome (ARI 0.008 under word features), and
    the project should decide now that it will not be buried.
11. **Disclose prior contact.** A reviewer-side probe has already observed ARI ≈ 0.008 (word) and
    0.152 (char-4) on these data. Analytic blindness is gone. The only remedy is the full-grid
    disclosure in condition 2 plus a pre-registration date before any confirmatory run.
