# Adversarial review round — reviewer R01 (session udm-ideation-01)

Reviewer: R01 — AI reviewer, disclosed; originated none of the ideas reviewed here.
Round rules observed: no literature search (evidence wave comes later), no reading of other
reviewers' outputs (`review_*`, `adversarial_*`, `evidence_*`), no ranking of ideas.
Each idea is reviewed in its strongest version before any attack is mounted.
Prior-evidence sections state what to look for only and are labelled
`not-checked — no search this round`.

---

## P01-1
**Idea ID:** P01-1
**Reviewer:** R01 (AI, disclosed; independent of the idea's originator)

**Strongest version of the idea.** The S6⊥S9 complementary distribution is the atlas's
"clearest single structural finding", derived from 25 modern systems whose genres were
pre-sorted by national page-format standards or modern legal taxonomy — precisely the
institutions that clean the two genres apart. Pre-modern chancery practice routinely
produced addressed instruments with full recitals (letters patent, chancery mandates,
farmans to named governors): exactly the S6+S9 cell that reads 0 today. The pre-modern bin
is n = 6 and rests on a handful of systems, so the negative rule has never met a genre that
was not pre-sorted. A dated sample of ≥30 instruments across ≥3 chancery traditions is a
cheap, decisive test of whether the fork is a deep-grammar universal or a modern
codification artefact — and the disconfirmation threshold (zero co-occurrence, recurrence
required in ≥2 traditions) is stated before any coding begins.

**Observation that would count against it.** A well-sampled pre-modern corpus
(≥30 instruments, ≥3 traditions, independent coding) in which S6 and S9 co-occur never or
only in single ambiguous cells: the fork survives its stress test and the challenge is
refuted on its own terms. Symmetrically, co-occurrence found only in one tradition's
idiosyncratic genre, or only in specimens whose published translations muddle recital and
addressee, would also count against the challenge (ambiguous-coding escape clause).

**Alternative explanations (two or more).**
1. *Translation artefact, not morphology:* the S6+S9 cells come from published
   translations that render a chancery address formula as a "whereas"-style recital (or
   vice versa) — the co-occurrence lives in the translator's conventions, not in the
   instrument. Independent translation of the same specimens into a common metalanguage
   would collapse the cell.
2. *Vocabulary drift, not a rule violation:* the modern slot definitions presuppose
   modern document types; what looks like "S9 present" in a farmān may be a doʿā /
   basmala / protocol opening with no normative-recital function, so the cell is a coding
   category error rather than a counterexample.
3. *Codification-side effect with a different cause:* even if modern systems show perfect
   negation, the cause need not be "modern standards clean the genres apart" — modern
   states may simply have inherited two mutually exclusive chancery templates. The
   historical test would then show coexistence pre-modern without establishing the
   proposed modern mechanism.

**Measurement or analysis failure.** Single-coder slot judgments with no inter-rater
check replicate the repo's own admitted gap (no kappa anywhere): an S6/S9 co-occurrence
pattern could be the coder's expectation in both directions. Mitigating thresholds are
stated (≥2 traditions, recurrence not single cells), but there is no blinded second coding
and no mechanical validity gate of the `check_stimuli.py` kind. Additionally, slot coding
on translations measures the translation layer; nothing in the design audits that layer.
Analysis failure mode: pooling all traditions into one co-occurrence count would let one
tradition's translation convention drive the headline; the pre-registered analysis must be
per-tradition as the idea itself implies.

**Sampling or generalizability failure.** The sample is convenience-bound to open,
citable transcriptions the single reader's languages cover (Latin/Old French, Ottoman
Turkish or Arabic, possibly Ge'ez) — i.e. exactly the best-published chanceries. Three
traditions chosen that way are not "pre-modern world"; failure to find co-occurrence in a
Turkish-Latin sample says little about Chinese, Indic, or East African chancery practice.
Surviving instruments are also biased toward the genres that were worth keeping and
translating (royal grants, not routine correspondence), and the n ≥ 30 threshold counts
instruments, not independent traditions — 30 specimens from one lineage would be pseudo-
replication.

**Prior evidence that challenges it.** What to look for in the coming evidence wave:
(da) scholarship showing the S6⊥S9 pattern holds in pre-modern corpora too, or that the
supposed pre-modern "hybrid" genres are in fact classifiable into the two declensions;
(b) evidence that the atlas's pre-modern thinness is a retrieval artefact rather than a
coding one; (c) translation-studies evidence that recital/addressee distinctions are
unstable across the specific translation traditions involved; (d) diplomatics literature
on whether addressed instruments with recitals were considered a separate genre rather
than a mixture. **not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low direct harm: no participants, public
documents. Misuse vectors: (i) a positive result could be oversold as "the atlas's
headline finding is an artefact" when it only scopes the fork's historical boundary —
damaging the project's claim strength beyond what the sample supports; (ii) asymmetric
burden: the traditions with the best European archival editions dominate the sample,
reproducing a metropolitan evidence bias under a de-centring headline; (iii) a null result
could be used to declare the pre-modern bin "settled" and block legitimate recoding.

**Mitigation.** Freeze a per-tradition reporting rule and a translation-provenance column
before coding (each specimen records translator/edition and whether the S6/S9 judgment
rests on the translator's wording); require ≥2 traditions with independent coding for any
positive claim; pre-register the exact disconfirmation threshold as written; blind the
coding of any specimen used as a threshold-anchor; report the sample's linguistic/
publishing bias explicitly in the write-up.

**Residual uncertainty.** Whether the 14-slot vocabulary is even applicable to addressed
pre-modern genres without distortion is assumed, not demonstrated (the idea admits this).
If the vocabulary cannot be applied without re-defining S9, the test degenerates into a
qualitative essay and the falsifier disappears — the largest single risk, unresolvable
before a small pilot coding of ~10 specimens.

**Disposition:** revise — keep the test, but add a translation-provenance column, a
per-tradition reporting rule, and a 10-specimen vocabulary-applicability pilot before the
full sample.

---

## P02-2
**Idea ID:** P02-2
**Reviewer:** R01 (AI, disclosed; independent of the idea's originator)

**Strongest version of the idea.** The fork's system-level support is 10 informative
cells (only-S6 = 8, only-S9 = 2, both = 0, neither = 15) — a strong pattern on a small
denominator. Public corpora of actual official documents (UN documents, EUR-Lex, national
gazettes; seeds already on disk in `sources/`) plus a slot tagger convert that census into
a co-occurrence *rate* with a real denominator across scripts and genres. Near-zero
co-occurrence at document scale hardens the universality claim from "true of 25 codified
systems" to "true of thousands of produced documents"; a structured nonzero cluster scoped
to subgenres would show the system-level negation was pooling artefact. The tagger's own
accuracy is audited on a hand-checked subsample, and the disconfirmation conditions are
two-sided (claim refuted *or* method falsified — declared in advance).

**Observation that would count against it.** Document-level co-occurrence rates
comparable to the marginals (S6 and S9 both frequent and jointly present across ordinary
genres) — the fork dissolves and the "clearest structural finding" is revealed as an
artefact of coding standards rather than documents. A weaker but still damaging
observation: co-occurrence concentrated in *any* routine subgenre (appointment/delegation
acts beyond a rare tail) would scope the fork far more narrowly than the atlas claims.

**Alternative explanations (two or more).**
1. *Detection failure masquering as confirmation:* address blocks and recital markers are
   layout-dependent; in HTML/OCR-extracted text the detector may systematically miss one
   slot class (e.g. recitals without an explicit "whereas"), producing near-zero
   co-occurrence for mechanical reasons — the observed rate would measure the detector,
   not the fork.
2. *Corpus-selection artefact:* UN/EUR-Lex/gazette corpora are themselves dominated by
   genres already pre-sorted into the two declensions; near-zero co-occurrence could
   simply reflect that the corpora sample the same codified populations as the 25 systems
   — apparent out-of-sample confirmation with no genuinely new population.
3. *Metadata leakage:* if genre or document type enters anywhere (even indirectly, via
   corpus choice, section headers, or the manual audit's expectations), the test
   re-derives the genre axis instead of testing slot co-occurrence.

**Measurement or analysis failure.** No gold labels exist at scale; accuracy is audited
only on a researcher-hand-checked subsample — single coder again, no kappa, so the same
subjectivity the audit is meant to check re-enters the validation set. Multi-script
detection has no stated per-script accuracy floor before the rate is reported (the idea
names detection failure in ≥2 of 5 script families as a falsifier, but the floor is not
pre-registered). Class imbalance (most documents are neither clean letter nor clean act)
means pooled rates will be dominated by the majority class; without a pre-declared
per-genre/per-script stratification the "real denominator" headline can be produced or
dissolved by corpus composition choices made after seeing results.

**Sampling or generalizability failure.** Thousands of documents from UN/EUR-Lex/one
gazette are thousands of draws from a handful of publishers, not from "official documents"
as a population — effective n is closer to the number of issuing bodies than the number
of documents, and clustering is not addressed. The corpora skew to supranational and
European open-data publishers; traditions in the atlas that publish little on the open web
(central Asia, parts of Africa — the same retrievability bias P08-5 worries about) are
absent, so "document scale" generalization would in fact be "open-web corpora
generalization". Documents are also not independent of the standards already coded: many
corpus documents are instances of the very page-format standards in `requisites.csv`.

**Prior evidence that challenges it.** What to look for: (a) prior document-level
corpora studies of addressed-vs-normative official texts showing non-zero hybrids at
routine rates; (b) evidence that recital conventions differ systematically by drafting
tradition (e.g. civil-law codes recite, common-law instruments do not) in ways that would
predict structure in the tagger output independent of the fork; (c) known OCR/layout
extraction failure rates for address blocks in the target corpora; (d) any existing
corpus-linguistics work on "whereas"-clause frequencies in legal texts. **not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low participant harm; main risks are
interpretive and resource-related: (i) a null could be weaponised as "the atlas's headline
finding is dead" when detector failure and population mismatch are live alternatives —
asymmetric reputational harm to the project from an under-validated negative; (ii) corpus
choice embeds a metropolitan/open-web bias while the result is framed as universality;
(iii) the tagger, once built, invites scope creep into auto-coding `requisites.csv`
itself, replacing the ledger's deliberate human discipline with an unaudited model.

**Mitigation.** Pre-register per-script and per-genre detection floors (reject rates
below floor rather than reporting them), freeze the corpus manifest with issuing-body
counts before running the rate, report cluster-robust intervals by issuing body, keep the
manual audit double-pass (re-code a random 10% after a delay), and state explicitly that
the tagger's output never writes to frozen repo files.

**Residual uncertainty.** Whether document-level tagging generalizes from standards rows
to produced documents is the very thing under test — so the validity gate and the test
share a failure mode: a detector validated on standards-flavoured samples may not be
validated for the corpus it is then run on. The design cannot fully break this circularity
without an independent gold sample drawn from the target corpora before the detector is
frozen; that step is implied but not specified.

**Disposition:** revise — add a pre-registered per-script/per-genre accuracy floor, a
corpus manifest with issuing-body clustering, and a gold sample drawn from the target
corpora before detector freeze.

---

## P06-3
**Idea ID:** P06-3
**Reviewer:** R01 (AI, disclosed; independent of the idea's originator)

**Strongest version of the idea.** "Genre, not nation, is the main axis of variation" is
currently a qualitative reading: `findings.md` §4 reports Jaccard pairs and a clustering
that "collapses to one trunk", and the headline cannot lose because any pairwise pattern
can be narrated either way. Building a system × genre matrix (each system's epistolary and
normative exemplar, coded from existing case files) and partitioning cross-system slot
variation between genre, tradition family and residual — PERMANOVA on Jaccard distances
plus a hierarchical logistic model — converts the headline into an effect size with a
confidence interval. The design is exactly the "genre-vs-nation" discrimination the frozen
criteria name as the top information-gain target: the two live explanations compete on the
same data under a pre-stated statistic, tradition labels and distance metric are declared
in advance, and either outcome (genre wins → headline earned; tradition wins → headline
rewritten) is informative. It is CPU-trivial and reuses frozen data plus existing case
files.

**Observation that would count against it.** Tradition family explains as much or more
variance than genre; or the genre term vanishes when the analysis is restricted to
within-system genre pairs — showing the current headline is an artefact of between-system
coding. The idea itself pre-commits that either would force a rewrite of README headline 3.

**Alternative explanations (two or more).**
1. *Coding-induced genre effect:* the genre exemplars are coded by the same researcher
   from prose case files; if exemplar choice is (consciously or not) steered toward
   documents that showcase the declension contrast, genre's share is inflated by
   selection, not discovered in the data.
2. *Density confound:* genre and slot-density co-vary (normative instruments tend to carry
   more requisites in the corpus's page-format systems); a Jaccard partition can load a
   density difference onto "genre" even when the identity of the slots, not their number,
   is the theoretical claim.
3. *Tradition-label granularity:* seven coarse tradition families (Anglophone, Soviet,
   Francophone…) are an analyst's bins; finer or different bins would move the tradition
   share, so the genre>tradition ordering may be a property of the binning, not of the
   systems.
4. *Sparsity artefact:* `findings.md` §4 already documents the JP = KE = HN = 1.0
   sparsity artifact; sparse systems contribute degenerate Jaccard distances that can
   masquerade as cross-genre similarity.

**Measurement or analysis failure.** The genre column does not yet exist at the required
grain — ~56 rows must be hand-coded from case-file prose, so the measurement instrument
for the *independent variable* is built by the same single coder whose reliability is
elsewhere (P06-1) an open question: no kappa is possible, and coder judgement re-enters
exactly where the headline lives. Method choices that remain open — Jaccard vs ordinal
coding of present/obligatory/optional, which distance, whether to include the `neither`
cells — are pre-declared as "must be fixed before results", but nothing forces the order:
with ~28 units the permutation distribution is coarse (p-value floor set by enumeration),
and a marginally non-significant genre share would be indistinguishable from low power
rather than from tradition parity. The two-term no-interaction model also cannot detect a
genre × tradition structure (e.g. genre matters only in codified systems), which is a live
substantive possibility.

**Sampling or generalizability failure.** n ≈ 28 systems, each contributing two exemplars
— the effective independent n for the tradition term is closer to 7 tradition families, so
the tradition share is estimated from a handful of clusters with no way to separate
within-tradition from between-tradition variance reliably. Both-genre exemplars are not
documented for every system (some traditions are coded for only one genre, some are
regimes rather than page documents), so complete-case restriction will drop exactly the
non-Western thin cases — biasing the partition toward the systems where genre distinctions
are best described by European document taxonomies. The result generalizes to "systems
with two well-documented exemplars", not to official documents generally.

**Prior evidence that challenges it.** What to look for: (a) prior variance-partition or
multilevel studies of document/register variation where nation, legal family or language
explains as much as register/genre; (b) evidence that the corpus's genre labels derive
from national taxonomies (which would make genre and nation partially the same variable —
the design's core contrast inoperative); (c) existing critique of Jaccard-based
similarity on sparse binary profiles; (d) any earlier project analysis already attempting
a genre × tradition split. **not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low direct harm. Misuse vectors: (i) a
tradition-share "win" could be read as cultural-essentialist evidence ("nations have
document DNA") when tradition family is itself a coarse analyst bin — framing harm,
particularly for thinly-coded traditions; (ii) complete-case dropping of thin non-Western
systems quietly re-centres the metropolitan axis under a formal method's prestige;
(iiii) the headline could be "confirmed" on data whose genre coding was shaped by the
headline (confirmation loop through exemplar choice).

**Mitigation.** Code the genre column blind to slot data (coder sees the document, not
the system's slot profile); pre-freeze exemplar selection rules with an inclusion log and
report which systems are dropped; pre-register the distance metric, coding scheme and
permutation scheme (including a tradition-blocked variant) in one declaration before any
result is computed; add a density-controlled sensitivity (partition on slot identity
conditional on slot count); report the coarse-bin sensitivity by re-running under two
alternative tradition binnings.

**Residual uncertainty.** Whether genre is measurable at the unit the partition needs
without importing national taxonomy assumptions is unresolvable inside this round: if the
genre labels come from the same national standards tradition as the slot coding, the
genre-vs-nation contrast may be partly circular at the measurement level even when the
statistics are clean. The single-coder genre coding also cannot be de-risked without a
second reader, which the sole-researcher constraint forbids.

**Disposition:** retain — with binding pre-registration of metric, coding rules and
exemplar-inclusion log before any computation, and a mandatory density-controlled
sensitivity.

---

## P02-6
**Idea ID:** P02-6
**Reviewer:** R01 (AI, disclosed; independent of the idea's originator)

**Strongest version of the idea.** `morphology.md` §6 admits the project has no
efficiency metric, and finding 5 asserts the slots exist for validity, not comprehension —
an unmeasured functional claim sitting under the atlas's central model. Ablation converts
the closed 14-slot vocabulary into an experimental factor: same document, minus one slot
at a time, identical who-did-what questions, accuracy/latency delta per slot with a
sham-deletion control. The `obligation` column supplies a ready-made dose prediction
(obligatory slots should hurt more than optional ones), stem-vs-surface ordering is
stated in advance, the experiment harness is reusable as-is, cost is dollars at the
repo's demonstrated $0.0314/864-call scale, and a flat profile or a surface-dominant
profile are both informative — the null is publishable under the project's own
decision-rule discipline. It is the first per-slot functional-value profile anywhere in
the repo.

**Observation that would count against it.** A flat ablation profile with a working sham
control (all slots equally dispensable — the deep grammar is descriptive baggage, or
machine readers bypass document structure entirely); or surface slots (S4, S8, S7)
hurting more than stem slots (S3, S5, S11, S12) — the divergent surface is what readers
rely on, directly challenging finding 5's reading.

**Alternative explanations (two or more).**
1. *Length/prompt-position artefact:* deleting a slot shortens the document; any delta
   may track prompt length or token position rather than the slot's function — the sham
   control must match deletion size, or "S12 matters" could be "removing 40 tokens from
   the header matters".
2. *Template unnaturalness:* template-instantiated documents with a slot surgically
   removed may read as defective, and the model may respond to the defect's detectability
   (a dangling reference where the identifier was) rather than to information loss —
   violations of well-formedness, not ablation of content.
3. *Question–slot alignment:* items that ask "who issued this?" obviously degrade when
   the issuing slot is removed; a slot's measured "value" may just reflect how often the
   question asks about it — an item-design artefact masquerading as functional value.
4. *Ceiling/difficulty regime:* if hard Q3-class items are not used from the start, all
   conditions sit at ceiling and the flat profile is a power failure, not a finding (the
   repo's documented v1 lesson).

**Measurement or analysis failure.** Layout/image-only slots (S4 emblem) degrade to
placeholder deletion — a different treatment class silently pooled with text deletions;
effect sizes are then not comparable across slots, and the design's own scope caveat
("declared out of scope rather than estimated") may be applied post hoc per slot after
results are seen. There is no stated rule for how many documents × slots × questions the
design needs, no power analysis for the per-slot contrasts (14 simultaneous comparisons —
multiplicity control is not mentioned), and the reader-panel choice (pre-selecting models
with headroom) is a post-hoc-able analytic decision that changes which deltas are
estimable. Single-authored question sets and single-authored documents mean question
quality and document quality are not independently verified.

**Sampling or generalizability failure.** Documents come from a handful of sources
(`sn_circulaire.txt`, `un_res.txt`, case-file examples, instantiated templates) — so a
per-slot profile estimated there generalizes to those document families, not to the 25
systems or to official documents broadly; slots rarely present in the chosen documents
(e.g. S6 in a UN resolution) cannot be ablated at all, so the profile is systematically
missing exactly the cross-cutting slots. Machine readers are an explicitly declared proxy
for machine legibility only: results say nothing about human comprehension, and the idea
must not leak into claims about finding 5's human arm. Model families on the panel are
correlated, so "N models" overstates effective n.

**Prior evidence that challenges it.** What to look for: (a) NLP deletion/occlusion
studies showing context lets models recover removed fields (implying ablation underestimates
slot value); (b) evidence that LLMs rely on document length/register cues rather than
structure (consistent with the arm's register null — the flat profile may be already
predicted); (c) prompt-sensitivity literature showing small layout perturbations move
accuracy by several points (making per-slot deltas indistinguishable from noise without
repeated sampling); (d) any prior finding that obligatory-slot coding in `requisites.csv`
correlates with slot frequency (collapsing the dose prediction). **not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low harm; misuse vectors: (i) a stem-dominant
profile could be oversold as "the deep grammar is functionally necessary" when it shows
only that models copy header fields — legitimising stronger universality claims than the
evidence carries; (ii) a flat profile could be weaponised against the whole morphology
model without the machine-only scope caveat traveling with the quote; (iii) building
auto-ablation tooling invites later misuse as a document-forgery pipeline (removing
authentication without detection) if the method section is read as a recipe.

**Mitigation.** Pre-register the document set, per-slot item counts, and a multiplicity
rule (e.g. Holm across 14 slot contrasts); make sham controls deletion-size-matched;
pre-specify that layout-only slots are excluded before results; run each ablation × item
cell with repeated sampling to separate prompt noise from slot effect; state in the output
file that the design measures machine legibility only and that text is researcher-authored;
freeze the reader panel (all 12 registered models plus a named expansion) before running.

**Residual uncertainty.** Ecological validity of ablated/instantiated texts is
unresolvable without a real-world counterpart (documents genuinely missing slots, i.e.
P05-5's completeness gradient) — the sham control tests deletion artefacts, not whether
natural omissions behave like experimental ones. Whether machine-reader deltas mean
anything for the project's comprehension claims at all remains open by the repo's own
scoping; the idea's information gain depends on accepting the machine-legibility reading.

**Disposition:** revise — retain the design but bind the document/item set, multiplicity
rule, size-matched shams and reader panel in a pre-registration addendum before any run.

---

## P07-1
**Idea ID:** P07-1
**Reviewer:** R01 (AI, disclosed; independent of the idea's originator)

**Strongest version of the idea.** The atlas announces three regime dimensions beyond the
page (`diversity.md` §10b) but only trace has quantitative teeth; persistence/appraisal
rests on one Nigerian case file plus an unstructured custody/archive keyword theme.
Coding a fourth, page-independent record-life layer (retention schedule · appraisal
criteria · disposal/transfer rule · legal-hold/permanent-value class) for all 28 systems
turns a narrative aside into a variable — and its sharpest pre-stated test is
orthogonality: page-format standards specify zero record-life variables while archives/records
regimes specify ≥3. That would demonstrate the "kinds of document law" catalogue as
disjoint layers rather than a list. Missing knowledge is coded `not found`, never
`absent`; the layer is declared non-derivable in `recompute.py` exactly like the existing
hand-assigned tables; the compute cost is a spreadsheet plus a gate extension, weeks at
most.

**Observation that would count against it.** Any page-format standard carrying an
explicit retention/disposal clause (falsifies orthogonality); no association between
archives-act regimes and the coded variables once genuine absence is separated from
`not found` (falsifies the layer's central prediction); or >1/3 of the 28 cells landing in
`not found` (falsifies feasibility of the layer as a quantitative instrument).

**Alternative explanations (two or more).**
1. *Retrieval depth, not layer structure:* page standards may code 0 retention variables
   simply because their sources are formatting manuals that were never going to mention
   disposal, while archives acts were selected because they do — apparent orthogonality
   would be an artefact of source genre, not of legal layers.
2. *Document-type confound:* the regimes that legislate retention (NG, KE, ZA, VN, UA) are
   also the full delovodstvo/statute systems with denser sources overall; any dimension
   coded from prose would correlate with them, so trace/access/persistence could all
   "associate" with the same source-density factor.
3. *Definition drift across traditions:* retention-like obligations in non-Western or
   non-English regimes may be expressed as archive-founding, waqf-like, or customary
   custodianship rules that the four-variable rubric reads as `not found` — apparent
   absence as a coding-window artefact.

**Measurement or analysis failure.** Hand-coding from prose with no second coder and no
kappa — the repo's standing caveat — re-enters on a new layer whose whole point is to
replace narrative with measurement. The `not found` vs `absent` distinction is the
layer's load-bearing measurement decision and is made by the same coder who is looking for
the predicted pattern; nothing in the design blinds the coder to a system's regime class
while coding its record-life variables, yet the prediction is *about* regime class — a
direct expectancy channel. The four variables are also not obviously commensurable (a
retention schedule is not the same kind of thing as a permanent-value class), so the
0–4 ordinal sum assumes an equal-interval structure the coding cannot justify.

**Sampling or generalizability failure.** The 28 systems were selected for document-law
coverage, not as a sample of record-keeping regimes; archives/records legislation exists
precisely in the jurisdictions whose sources the corpus happened to retrieve (the same
retrievability bias P08-5 targets). African archives-act cases (NG, KE, ZA) carry the
positive end of the orthogonality contrast almost alone — three systems, secondary
grounding, one coder: if they move together, the "layer" is a three-case regularity.
Systems with no retrievable records legislation (the encyclopedia-thin PE, HN, ET, WA)
will code `not found` by construction, so >1/3 `not found` may reflect the evidence base
rather than the layer's infeasibility — the disconfirmation threshold conflates the two.

**Prior evidence that challenges it.** What to look for: (a) records-management literature
showing page-format standards *do* sometimes specify retention (e.g. formats citing
retention requirements — would kill orthogonality at the source); (b) evidence that
"document law" typologies in the literature already include lifecycle/retention as a
dimension of formatting law rather than a separate layer; (c) studies of how reliably
retention rules can be coded from public sources (coding-yield expectations for `not
found` rates); (d) whether ISO 15489-style standards are cited by page-format standards,
which would already couple the layers in practice. **not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low direct harm; inequity risks: (i) coding
non-Western custodianship traditions through a Western records-management rubric can
render them `not found` and then be reported as "those regimes lack appraisal" — a
measured-looking erasure of traditions whose practice is oral or customary; (ii) the
layer's positive cases concentrate in a few post-colonial archives states, inviting
framing of African systems as "records-managed" through the very colonial administrative
heritage the project elsewhere treats critically; (iii) a published orthogonality claim
could be cited as standardisation guidance (retention is "not a formatting matter"),
which is a policy extrapolation the data cannot support.

**Mitigation.** Blind regime-class labels during record-life coding (code from sources
with the case file's regime class hidden); require a written source quote for every
non-`not found` cell and every `not found` cell (evidence of search, not just absence);
pre-register the ordinal treatment (report per-variable presence alongside the 0–4 sum);
report `not found` rates separately for page-standard and archives-act systems so the
disconfirmation threshold distinguishes instrument failure from layer structure; treat the
three African positive cases as a named fragility in the write-up.

**Residual uncertainty.** Whether the layer is codeable at all outside the best-documented
traditions is genuinely unknown until a pilot codes the four variables for ~8 contrasting
systems; the >1/3 `not found` disconfirmation may fire for reasons (source genre) the
design cannot distinguish from the substantive claim without that pilot. The orthogonality
test's purity also depends on "page-format standard" and "archives act" being clean source
categories — mixed instruments (codes that cover both) would need an exclusion rule fixed
in advance.

**Disposition:** revise — retain, but blind regime-class labels during coding, require
written evidence for every `not found`, and run an 8-system pilot before committing the
28-system layer and its disconfirmation threshold.

---

## P05-6
**Idea ID:** P05-6
**Reviewer:** R01 (AI, disclosed; independent of the idea's originator)

**Strongest version of the idea.** `morphology.md` §6 concedes efficiency is measured
nowhere and that the burden literature studies procedures, not document grammar: the atlas
codes what a document contains but never who produces each requisite — which is exactly
the burden question. Adding a "citizen-supplied vs administration-derived" column over
`requisites.csv` and computing a slot-level citizen-supplied count for one common public
service in Ukraine, Estonia and Germany turns the once-only narrative (`diversity.md` §7:
digitisation moves requisites from citizen to backend and dissolves shuttle genres) into a
countable, cross-nationally comparable quantity no existing burden measure provides. The
predictions are directional and pre-stated (Estonia fewest, Germany most; citizen-supplied
slots concentrate in S1, S3, S5, S6), equal counts or slot-shifting-without-net-reduction
are declared disconfirming, retrieval not analysis is the main uncertainty, and the pilot
is explicitly framed as illustrative rather than an estimate of national burden.

**Observation that would count against it.** Citizen-supplied counts equal across the
three systems; or digitisation merely changes *which* slot the citizen fills with no net
reduction — either outcome would show the grammar-level construct has no discriminatory
power and would challenge the once-only account rather than support it.

**Alternative explanations (two or more).**
1. *Service non-equivalence:* the "same class of service" in UA, EE and DE will not carry
   the same legal entitlement, identity-documentation basis, or register infrastructure;
   count differences could reflect what each service *is* rather than how each document
   grammar burdens citizens.
2. *Derivation infrastructure, not grammar:* Estonia's low count may follow from a single
   national population register (a backend fact), not from anything about the document's
   slot structure — the construct would be measuring e-government maturity in disguise,
   duplicating indicators the repo deliberately does not use.
3. *Form version and channel artefacts:* the retrieved form (web form vs PDF vs printable)
   determines how many fields the citizen types versus which are pre-filled; counts could
   track interface design choices of the sampled portal rather than the requisites regime.
4. *Researcher-coding expectancy:* the coder knows the once-only prediction; ambiguous
   identity fields can be coded citizen- or register-derived either way without a rule
   frozen in advance.

**Measurement or analysis failure.** The new column is single-coder with no kappa —
the repo's standing caveat applied to the construct the whole idea rests on — and
ambiguous cases are "declared rather than forced", but the declaration mechanism is not
specified (a per-row note? a count of ambiguities?). One service per country yields three
data points per prediction with no variance estimate: the ordered predictions (EE < UA <
DE) can be met or missed with n = 3 by chance ordering alone (1/6 probability of any exact
order), yet the idea's framing invites reading the order as evidence. No measurement of
uncertainty, no sensitivity to ambiguous-cell recoding (a single re-coded field can flip
the EE–UA ordering), and no independent check that the column's two categories are
mutually exclusive in practice (backend-derived fields still require citizen-supplied
identity anchors — the boundary is theoretically contested, not just noisy).

**Sampling or generalizability failure.** Three countries and one service each is
acknowledged as a pilot, but the country selection is the atlas's own convenience set —
all three are European/open-web jurisdictions with visible portals; the exact
retrievability bias P08-5 warns about determines the sample, while the once-only narrative
most at stake concerns digitising administrations outside that set. Services change
without notice and Estonian services may only be visible to authenticated users, so the
sampled form may be a snapshot of one portal state, not the service's requisites regime.
Generalization beyond "this service, this portal, this month" is explicitly deferred but
the predictions are written in register with national-level claims (Estonia *shows* the
fewest) that the design cannot carry.

**Prior evidence that challenges it.** What to look for: (a) administrative-burden
literature showing field-level burden measures already exist and behave differently from
document-grammar counts (would undercut the "no existing measure" rationale); (b) evidence
that once-only/once-only-*enough* implementations leave citizen-facing fields intact in
Estonia (would predict a null before we look); (c) prior UA/EE/DE comparative studies of
the same service class showing differing entitlements (service non-equivalence); (d)
register-derivation rules in DE that pre-fill most identity fields (would collapse the
predicted ordering). **not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low direct harm as designed (public forms only).
Misuse vectors: (i) a three-country pilot reported as a national burden ranking could be
cited in policy debate — Estonia-praising/Germany-critical framing from n = 3 services;
(ii) coding citizen-supplied fields implicitly blames citizens' inputs rather than
administration design, a framing that can be extracted from the paper and misused;
(iii) cross-national counts can essentialise "bureaucratic cultures" if the service
non-equivalence caveat does not travel with the number; (iv) any later variant involving
citizens or officials hits the ethics gate — as designed, none does.

**Mitigation.** Freeze a coding rulebook for citizen-supplied vs derived (with examples)
before coding any form and publish the ambiguous-cell count alongside the headline count;
pre-register the exact service-class definition and the inclusion/exclusion of each
country's specimen; report counts as ranges (ambiguous cells as ±) so the ordering's
robustness to a single re-code is visible; state per-country what the service's legal
basis is, so non-equivalence is documented rather than asserted; keep all outputs worded
as "one service, one portal, retrieval date" and forbid national-level burden language in
the write-up's own templates.

**Residual uncertainty.** Whether "the same class of service" exists in all three systems
is untestable before retrieval — if it does not, the comparative contrast (the idea's whole
cross-national payoff) is unavailable and the design degenerates to three unrelated
descriptions; the retrieval step is cheap but the equivalence judgment is not, and no
pilot is specified. Also unresolved: whether the construct adds anything beyond an
e-government-maturity indicator once backend derivation is entered — a construct-validity
question the design as specified cannot separate from its own predictions.

**Disposition:** revise — keep the pilot, but freeze a coding rulebook and service-class
definition pre-retrieval, report ambiguous-cell ranges, and word outputs at
service-not-country granularity; re-assess after an 8-form feasibility pilot (two systems
× four forms) before extending to the third country.

---

*End of adversarial review — R01, session udm-ideation-01. Six ideas reviewed:
P01-1, P02-2, P06-3, P02-6, P07-1, P05-6. No literature search performed; no other
reviewers' files read; no idea ranked.*