# Idea catalogue — session udm-ideation-01 (57 ideas, 11 AI participants)

The first 48 ideas came from the independent round (blind, no cross-talk, no literature search, 2026-10-15); the last 9 from the post-check re-open after the evidence wave (skill step 8). Full fields (assumptions, predictions, disconfirmation, feasibility risk, repo connections) live in `raw/P*.md` and in `session.json`. `rk/score` appears only for the 23 rated ideas — see `RESULTS.md`. Reserves and post-check ideas were not rated, not rejected.

Participants: P01 historian/diplomatics · P02 computational linguist · P03 psycholinguist · P04 standards/metrology · P05 bureaucracy/digital government · P06 statistician/methodologist · P07 archival science · P08 anthropology of knowledge systems · P09-P11 post-check re-open (novelty pivot / synthesis & sequencing / kill-criteria).


## C1 — The epistolary/normative fork and 'genre, not nation' under test — same headline claim put at risk


### P01-1 — **rk 6, score 72.7**; evidence: support-located; adv: revise

Test the atlas's strongest structural claim — the perfect complementary distribution of destination (S6) and preamble (S9) — against pre-modern and early-modern chancery instruments in which a named addressee and a recital coexist (royal letters patent, chancery mandates, farmans addressed to named governors), to determine whether the epistolary/normative fork is universal or an artefact of modern codification.

  _origin: P01, independent, AI-generated_

### P02-2 — **rk 9, score 68.2**; evidence: mixed; adv: revise

Test the perfect complementarity of destination (S6) and preamble (S9) on a corpus of thousands of actual official documents tagged automatically for those two slots, rather than 25 hand-coded systems.

  _origin: P02, independent, AI-generated_

### P05-3 — *reserve (not rated this round)*

Test whether the epistolary/normative complementarity (destination never co-occurs with preamble) survives at the level of individual documents in a held-out corpus coded by an automated slot detector, rather than only as an aggregated property of 25 hand-coded systems.

  _origin: P05, independent, AI-generated_

### P05-4 — *reserve (not rated this round)*

Formally test the headline claim "genre, not nation, is the main axis of variation" by partitioning document-level slot-vector variation between genre, country/tradition and their interaction in a small crossed corpus (the same two genres observed in four to six countries).

  _origin: P05, independent, AI-generated_

### P02-3 — *reserve (not rated this round)*

Train epistolary-vs-normative classifiers on surface (lexical/layout) features in one tradition and on structural (slot-presence) features in another, then measure zero-shot cross-script transfer to decompose "genre, not nation" into deep-grammar versus ritual-surface signal.

  _origin: P02, independent, AI-generated_

### P08-6 — **rk 7, score 70.5**; evidence: mixed; adv: retain

Test whether the atlas's two declensions conceal a third genre class — the deliberative/argumentative *note* (Indian secretariat note, French/Bénin note de service, U.O. note) — with its own exclusion profile, by functionally coding note-type documents across the corpus and checking them against the S6⊥S9 fork.

  _origin: P08, independent, AI-generated_

### P06-3 — **rk 3, score 79.5**; evidence: mixed; adv: retain

Quantify headline finding 3 as an effect size: build a system × genre slot matrix (each system's epistolary exemplar and normative exemplar, coded from existing case files), partition cross-system variation in slot presence between genre, tradition family and residual — permutation-based variance partition (PERMANOVA on Jaccard distances) plus a hierarchical logistic model with tradition as a grouping factor — and report R² with bootstrap confidence intervals.

  _origin: P06, independent, AI-generated_

## C2 — Reliability of the hand-coded layers — measurement error of requisites.csv / case coding


### P01-6 — *reserve (not rated this round)*

Apply diplomatics' own internal/external criticism to the atlas itself: write a CPU-only extractor that reads the retrieved primary texts in `sources/` (60 sources with extracted `.txt`) and independently re-derives slot presence per system, then adjudicate every disagreement against the originals as a formal audit of the hand-coded `requisites.csv`.

  _origin: P01, independent, AI-generated_

### P02-1 — **rk 8, score 68.2**; evidence: challenge-located; adv: revise

Build an automatic tagger that assigns the 14 canonical slots (and, secondarily, the 10 theme codes) to each requisite row and to raw document text, and run it as an independent second coder against the hand-coded `requisites.csv`, reporting agreement instead of trust.

  _origin: P02, independent, AI-generated_

### P04-4 — *reserve (not rated this round)*

Run a blinded re-coding study of a stratified subsample of case files — a second human coder and/or independent LLM coders — and propagate the observed disagreement through `analysis/recompute.py` so that every headline finding carries a measurement-uncertainty interval instead of a point value.

  _origin: P04, independent, AI-generated_

### P06-1 — **rk 12, score 68.2**; evidence: challenge-located; adv: retain

Blindly re-code a stratified random subsample of all four hand-coded layers of the atlas — slot mappings in `requisites.csv`, keyword themes, era anchors, regime classes — with a frozen codebook, quantify agreement (κ / exact agreement), and then propagate the measured error rates through a `recompute.py`-style resimulation to report which headline findings survive plausible mis-coding.

  _origin: P06, independent, AI-generated_

### P06-6 — *reserve (not rated this round)*

Add an explicit codability code (present / absent / not-applicable-not-a-page-document) to the 225-row mapping so that structural zeros are separated from undefined cells, then re-derive the slot census, Jaccard similarity and clustering under opportunity-corrected denominators, explicitly dissolving the JP = KE = HN = 1.0 sparsity artifact.

  _origin: P06, independent, AI-generated_

### P07-5 — **rk 4, score 79.5**; evidence: challenge-located; adv: retain

Freeze the per-case grounding tiers the README already discloses into a machine-readable column, then recompute the headline structural claims (universal-stem membership, the S6⊥S9 fork, S12 as the modal slot) on the strong-primary subset alone, to test whether the universality claim is robust to — or dependent on — the corpus's thin secondary-grounded cases.

  _origin: P07, independent, AI-generated_

## C3 — Formal statistical audit of the structural claims — are the 'perfect' patterns real?


### P06-2 — **rk 1, score 90.9**; evidence: challenge-located; adv: retain

Convert the atlas's perfect structural rules (S9 ⊥ S4/S6/S7/S8/S10/S14 and the 1.00 implication rules S6⇒S12, S8⇒S12) from census statements into population inferences, using exact enumeration/permutation nulls on the 25-system slot matrix with FDR control, plus a sample-size target for how many further systems each per-edge claim needs before it is informative.

  _origin: P06, independent, AI-generated_

### P06-3 — **rk 3, score 79.5**; evidence: mixed; adv: retain *(also listed under an earlier cluster)*

Quantify headline finding 3 as an effect size: build a system × genre slot matrix (each system's epistolary exemplar and normative exemplar, coded from existing case files), partition cross-system variation in slot presence between genre, tradition family and residual — permutation-based variance partition (PERMANOVA on Jaccard distances) plus a hierarchical logistic model with tradition as a grouping factor — and report R² with bootstrap confidence intervals.

  _origin: P06, independent, AI-generated_

### P06-4 — **rk 2, score 88.6**; evidence: challenge-located; adv: retain

Recast the scoped universality claim as an estimate over an explicitly stated sampling frame of written official-document regimes: attach Wilson/beta-binomial intervals to each slot's prevalence, run leave-one-tranche-out and leave-one-tradition-out sensitivity to show which findings are carried by which subset, and commit — before coding — the model's predicted slot vector for the next system added (or for the provisional RU/GOST column once a non-blocked source appears), then score it.

  _origin: P06, independent, AI-generated_

### P04-6 — *reserve (not rated this round)*

Operationalise the kinds of document law (layout, formulas, naming, function, plus the trace / access / persistence regime dimensions) as rule-based per-system indicators over all 28 systems, build the resulting feature matrix inside `analysis/`, and test whether the typology is an exclusive partition or a continuous mixture.

  _origin: P04, independent, AI-generated_

### P05-4 — *reserve (not rated this round)* *(also listed under an earlier cluster)*

Formally test the headline claim "genre, not nation, is the main axis of variation" by partitioning document-level slot-vector variation between genre, country/tradition and their interaction in a small crossed corpus (the same two genres observed in four to six countries).

  _origin: P05, independent, AI-generated_

## C4 — The document as an information channel — operationalising morphology.md §6 efficiency


### P04-1 — **rk 11, score 68.2**; evidence: mixed; adv: revise

Compute an information-theoretic efficiency profile for each of the 25 slot-coded systems — slot-wise entropy, conditional entropy given genre, and each slot's share of total redundancy — to convert the repo's unmeasured claim that official formats spend their bits on validity rather than comprehension into a number.

  _origin: P04, independent, AI-generated_

### P02-6 — **rk 10, score 68.2**; evidence: challenge-located; adv: revise

Remove one canonical slot at a time from full official documents (real or template-instantiated) and measure the drop in a machine reader's ability to answer who-did-what-to-whom questions, yielding a per-slot functional-value profile that tests whether the "universal stem" is also the load-bearing core.

  _origin: P02, independent, AI-generated_

### P04-5 — *reserve (not rated this round)*

Quantify S2 as an information channel: encode each corpus identifier grammar (UN symbol, ОКУД/НК 010 eight-digit codes, GB/T 版头 fields, DIN reference line, UAE naming discipline) in a fixed field dictionary, then measure metadata bits carried per character and the error rate of decoding document metadata from the identifier string alone.

  _origin: P04, independent, AI-generated_

### P04-2 — *reserve (not rated this round)*

Extend the existing machine arm from a register contrast to a morphology contrast: render one identical obligation in six corpus formats (DIN-5008 letter, ДСТУ наказ, GB/T 9704 公文, UN resolution, EU regulation, Francophone lettre administrative) and measure extraction accuracy, prompt-token cost and latency per format.

  _origin: P04, independent, AI-generated_

### P05-5 — *reserve (not rated this round)*

Move the machine arm from constructed register stimuli to real public documents and test whether requisite completeness — how many of a system's expected slots an individual document actually carries — predicts how accurately reader models extract its key facts, with register entered as a competing predictor.

  _origin: P05, independent, AI-generated_

## C5 — Comprehension experiment (finding 5) extensions — same instrument/outcome family


### P03-1 — **rk 18, score 61.4**; evidence: mixed; adv: pause; ethics: review-required

Add a pre-registered processing-cost outcome — per-question response time, plus a time-bounded fact-location ("findability") version of the hardest items — as a co-primary outcome beside accuracy in the finding-5 comprehension test, so the register question can be answered on *cost of understanding* even if accuracy stays at ceiling.

  _origin: P03, independent, AI-generated_

### P03-2 — *reserve (not rated this round)*

Re-render the six experimental obligations in both declensions — as a letter (destination + reference, no preamble) and as a normative act (preamble, no addressee) — holding register, language and fact tuples fixed, and measure whether the fork's furniture (S6 ⊥ S9) helps or hinders readers finding and acting on the same obligation.

  _origin: P03, independent, AI-generated_

### P03-3 — *reserve (not rated this round)*

Present identical document content once in the atlas's canonical slot order (identity → origin → date → body → authentication → annex) and once with the self-contained blocks shuffled, then probe memory for and source-location of slot-specific facts (identifier, date, authentication) — testing whether "the ordering is the *syntax* of the document" (`morphology.md` §2) is a cognitive asset or only a legal one.

  _origin: P03, independent, AI-generated_

### P03-4 — *reserve (not rated this round)*

Pre-specify, before any human data, a stress condition — bounded display time or a light concurrent memory load — and register a register × load interaction, so the human arm cannot fail merely by being too easy, and so a null at leisure is not over-read as equivalence under load.

  _origin: P03, independent, AI-generated_

### P03-5 — *reserve (not rated this round)*

Manipulate the authentication block (signed-and-sealed vs "signature withheld" vs absent) on otherwise identical obligations and measure three separable outcomes — trust in the document, willingness to comply, and fact comprehension — to test whether the atlas's most universal slot does any work in a reader's head.

  _origin: P03, independent, AI-generated_

### P02-5 — *reserve (not rated this round)*

Replace the two-level formal/plain label with a continuous, automatically computed register index over the stimulus texts (and any content-gated paraphrase ladder), reanalyse the existing machine-arm accuracy as a dose–response, and use the same index plus machine item difficulty to select a harder item pool that breaks the ceiling — logged as a pre-registration revision before any human data.

  _origin: P02, independent, AI-generated_

### P06-5 — **rk 13, score 68.2**; evidence: challenge-located; adv: retain; ethics: not-assessed

Quantify how much of the registered 10 pp SESOI is attainable as a function of baseline accuracy (at baseline b the largest possible plain advantage is 1−b), re-derive the design's power surface over (baseline, effect) rather than at the single assumed baseline, and calibrate all 18 items' difficulty and discrimination on an expanded machine reader panel (the 12-model arm cost $0.0314, so a 60–100 model panel is dollars) so the human instrument is retargeted before recruitment starts.

  _origin: P06, independent, AI-generated_

### P08-2 — **rk 17, score 63.6**; evidence: mixed; adv: external review; ethics: review-required

Test whether Indigenous and community data-sovereignty frameworks constitute a fourth regime dimension of "document law" — **stewardship** (who may use a record, for what purpose, under whose interpretation) — distinct from the atlas's trace, access and persistence/appraisal dimensions.

  _origin: P08, independent, AI-generated_

## C6 — Diachrony: standards editions and regime trajectories — within-object change over time


### P01-2 — *reserve (not rated this round)*

Build a small longitudinal panel by sampling the same chancery lineage at four or more dates (e.g. French royal chancery → ancien régime → modern French administrative letter; or the Soviet ЄДСД line → post-Soviet RU/UA/EE) and re-coding the same slots at each date, so that the published "modernity = identifier" trend can be separated from a corpus-composition effect.

  _origin: P01, independent, AI-generated_

### P01-4 — *reserve (not rated this round)*

Convert the atlas's static finding that authentication (S12) is the most variable slot into a dated transition analysis, asking whether authentication forms follow a restricted, non-random order of succession (witnessed attestation → registered seal → hand signature → registered stamp → cryptographic) and whether regulatory change leads or lags the material change.

  _origin: P01, independent, AI-generated_

### P04-3 — **rk 19, score 61.4**; evidence: challenge-located; adv: pause

Treat the layer-1 standards as versioned artefacts (DIN 5008 across its post-1949 revisions, ДСТУ 4163:2003 → 4163:2020, ГОСТ 6.38-90 → ГОСТ Р 7.0.97-2016, GB/T 9704 editions) and diff their requisite inventories across editions to measure per-decade slot accretion and deletion rates.

  _origin: P04, independent, AI-generated_

### P05-2 — **rk 21, score 56.8**; evidence: mixed; adv: revise

Reconstruct the pre- and post-digitisation slot profiles of one Ukrainian document flow (the ГОСТ 6.38 → ДСТУ 4163 official-documentation lineage plus the electronic document-management rules) to test `diversity.md` §7's claim that "the medium moves the slots into infrastructure" on an observed reform trajectory instead of a single endpoint comparison.

  _origin: P05, independent, AI-generated_

### P08-4 — *reserve (not rated this round)*

Type the atlas's most variable slot by *where the binding force resides* — object-bound (signature, registered seal, tughra), event/performance-bound (witness attestation, belt recitation), system-bound (cryptographic signature, automatic log) — and test the compensation prediction that when authentication leaves the page, trace (S14) or authority-mark (S4) thickens in its place.

  _origin: P08, independent, AI-generated_

## C7 — The record above the page (file, retention, migration) — next-level unit of the record-keeping system


### P01-5 — *reserve (not rated this round)*

Generalise the atlas's single observation that India's CSMOP makes the *file*, not the document, the accountable unit into a comparative test across bureaucracies that visibly keep dossiers (Russian/post-Soviet дело practice, Ottoman register practice, Chinese 卷, Ethiopian imperial custody), asking whether a second, higher-level grammar of assembly exists and whether it converges as strongly as the document's.

  _origin: P01, independent, AI-generated_

### P07-1 — **rk 20, score 61.4**; evidence: challenge-located; adv: revise

Code a fourth, page-independent "record-life" layer (retention schedule · appraisal criteria · disposal / transfer rule · legal-hold or permanent-value class) for all 28 systems, so the persistence/appraisal dimension announced in finding 5 stops being a one-case illustration (Nigeria) and becomes a variable that can be cross-tabulated against the slot data and the regime classes.

  _origin: P07, independent, AI-generated_

### P07-2 — *reserve (not rated this round)*

Systematically hash and near-duplicate-detect every retrieved source text in `sources/` to measure how many nominally independent systems' evidence is actually the same or a derivative of the same template document, then re-run the slot-similarity analysis with shared-template pairs flagged as a sensitivity check on the convergence claim.

  _origin: P07, independent, AI-generated_

### P07-3 — **rk 16, score 63.6**; evidence: mixed; adv: revise

Classify all 225 requisites in `requisites.csv` by migration behaviour — content-invariant, structure- dependent, substrate-bound, wording-bound — and compute per-system and per-slot fragility rates to test the repo's qualitative claim that "the morphology survives; its carriers do not".

  _origin: P07, independent, AI-generated_

### P07-4 — *reserve (not rated this round)*

Code all 28 systems on the level of their accountable record unit (page document / file / series-fonds / automatic log) and test whether that level predicts which of the three regime dimensions — trace, access, persistence/appraisal — the system's legal order legislates.

  _origin: P07, independent, AI-generated_

## C8 — Non-documentary boundaries and de-centring the corpus — what/who is outside the atlas frame, and corpus-construction bias


### P01-3 — *reserve (not rated this round)*

Extend the atlas's chronology from c. 1412 back to antiquity by coding a small sample of early administrative record objects (cuneiform accounts, Egyptian hieratic dockets, Chinese bronze/bamboo administrative texts, Roman tabulae) on the 14 slots, and use the result to convert the currently qualitative khipu/wampum boundary into an explicit slot-count threshold for what counts as a "document regime".

  _origin: P01, independent, AI-generated_

### P08-1 — **rk 5, score 77.3**; evidence: mixed; adv: external review; ethics: review-required

Replace the "n/a" slot profiles currently assigned to the khipu and the wampum with a second, medium-neutral *record* grammar (abstract slots: provenance, custody, temporal reference, content encoding, authentication/validation, transmission-of-authority), and re-code both boundary systems — plus one further non-documentary record system chosen for source availability — to test whether the atlas's deep grammar is a property of *authoritative records* or specifically of *writing*.

  _origin: P08, independent, AI-generated_

### P08-3 — **rk 14, score 68.2**; evidence: mixed; adv: revise

Code each system's colonial administrative heritage as a categorical variable and test, by permutation, whether metropole–successor slot-profile similarity exceeds successor–same-region similarity — turning the repo's narrative "imperial/colonial continuity" theme into a measurable claim.

  _origin: P08, independent, AI-generated_

### P08-5 — **rk 22, score 54.5**; evidence: mixed; adv: revise

Build a coverage-gap index against an external universe (states that maintain a documentation/records standard) and test whether the atlas's inclusion decisions and grounding tiers track *source retrievability* — how far a state publishes its standards on an open web — rather than a principled coverage frame.

  _origin: P08, independent, AI-generated_

### P07-6 — *reserve (not rated this round)*

Ask of the two non-documentary boundary systems the *archival* question rather than the morphological one — did their record systems govern custody (trace), who may hear/see them (access), and what is kept, repaired, retired or destroyed (persistence/appraisal)? — to test whether the atlas's three regime dimensions are document-independent while its 14-slot grammar is document-bound.

  _origin: P07, independent, AI-generated_

### P08-2 — **rk 17, score 63.6**; evidence: mixed; adv: external review; ethics: review-required *(also listed under an earlier cluster)*

Test whether Indigenous and community data-sovereignty frameworks constitute a fourth regime dimension of "document law" — **stewardship** (who may use a record, for what purpose, under whose interpretation) — distinct from the atlas's trace, access and persistence/appraisal dimensions.

  _origin: P08, independent, AI-generated_

## C9 — Policy-facing payoff — converts the atlas into a measurable citizen-facing quantity


### P05-1 — *reserve (not rated this round)*

Convert the atlas's qualitative claim that trace/audit density (S14) tracks the strength of the central recordkeeping regime into a quantitative per-system index derived from `requisites.csv`, and test whether it covaries with an externally compiled cross-national indicator of digital-government or public-administration capacity.

  _origin: P05, independent, AI-generated_

### P05-6 — **rk 23, score 47.7**; evidence: mixed; adv: revise

Add a new column over `requisites.csv` — *who supplies this requisite, the citizen or the administration* — and use it to compute, for one common public service in two or three atlas systems (Ukraine, Estonia, Germany), a slot-level "citizen-supplied requisites" count as a grammar-based pilot measure of administrative burden.

  _origin: P05, independent, AI-generated_

### P03-6 — *reserve (not rated this round)*

Build a CPU-only, regenerable surface-formality index (sentence length, subordination depth, nominalisation and passive rates, direct-address and directive markers) over the 69 extracted source texts in `sources/`, join it to system and tradition via `ledger.json`, and use it to (a) validate that the experiment's constructed `en-formal`/`uk-formal` renderings sit inside the corpus's actual formal range and (b) ask whether formality differs across the five kinds of document law while slot structure converges.

  _origin: P03, independent, AI-generated_

## C10 — Integrity tooling for the ledger — strengthens the verification gate itself


### P02-4 — **rk 15, score 63.6**; evidence: challenge-located; adv: retain

Extend `check_claims.py` from structural citation resolution to semantic verification: an LLM entailment pass that checks each of the 92 ledger claims against its retrieved source text, requires a verbatim quote, string-matches the quote into the source, and flags unsupported claims for researcher review.

  _origin: P02, independent, AI-generated_

## C11 — Post-check re-open round (after the evidence wave, skill step 8): novelty pivots, synthesis/sequencing, and kill-criteria responses — unrated by design


### P09-1 — *post-check re-open round; not rated*

Freeze the slot vocabulary and all text preprocessing, cluster the 225 requisites' own descriptions (`local_term` + `gloss_en` in `requisites.csv`) unsupervised over a pre-registered range of k, align the recovered clusters to S1–S14, and report ARI/NMI against a fixed-margin permutation null — asking whether the atlas's deep grammar re-emerges from the data or exists only in the analyst's codebook.

  _origin: P09, post-check, AI-generated_

### P09-2 — *post-check re-open round; not rated*

Build a frozen descent/citation edge set over the atlas's own standards and administrations from documents already on disk (`STANDARDS.md`, `diversity.md`, `cases/`, `ledger.json` — no new retrieval), and re-test the convergence claims (universal stem, S6⊥S9, "genre, not nation") under lineage-blocked nulls plus a profile-similarity regression on descent distance, partitioning the "deep grammar" into convergent structure versus common descent.

  _origin: P09, post-check, AI-generated_

### P09-3 — *post-check re-open round; not rated*

Use the obligation coding already frozen in `requisites.csv` (150 mandatory / 66 optional / 9 other tokens) as the *explanatory* variable for cross-system slot presence — pre-registered leave-one-system-out prediction of each system's slot vector from the other systems' mandate shares, scored against a prevalence-only baseline — testing whether the universal stem is essentially what every standard compels and whether the epistolary/normative fork is a conflict of genre-conditional mandates.

  _origin: P09, post-check, AI-generated_

### P10-1 — *post-check re-open round; not rated*

Merge P06-2's perfect rules, P06-1's error propagation and P02-1's second-coder idea into one week-long study that computes, for each headline "perfect" rule, the exact set of matrix cells whose single flip would break it, re-adjudicates *only* those cells against the retrieved primary texts in `sources/` under a frozen codebook (LLM used solely to triage disagreements, never to set a cell), and reports each rule as decidable/undecidable at the measured cell-error rate — the outcome fixing the scope of P10-2.

  _origin: P10, post-check, AI-generated_

### P10-2 — *post-check re-open round; not rated*

Run P06-2 (exact nulls), P06-3 (variance partition), P06-4 (prevalence intervals) and P07-5 (tier restriction) as a *single* pre-registered specification curve over the frozen matrices — the set of defensible specifications (denominator/codability rule × evidence-tier cut × distance metric × tradition-blocking scheme) enumerated by a written rule before any computation — reporting one robustness-mass per headline claim plus one pre-committed leave-one-tranche-out prediction scored at the end, instead of four analyses with four p-values.

  _origin: P10, post-check, AI-generated_

### P10-3 — *post-check re-open round; not rated*

Combine P01-1 (pre-modern instruments), P08-6 (deliberative notes) and P02-2 (document-level scale) into one frozen S6/S9 coding protocol applied *sequentially* to three out-of-sample bins — bin A: public-domain pre-modern chancery specimens; bin B: openly posted French/Indian deliberative notes; bin C: ordinary unsorted modern documents — running each bin only if all cheaper previous bins failed to break the fork, and stopping the study at the first bin whose co-occurrence rate exceeds a threshold fixed before any coding.

  _origin: P10, post-check, AI-generated_

### P11-1 — *post-check re-open round; not rated*

Pre-register two stages before any further statistics on `requisites.csv` — (i) a worst/best-case bounds analysis in which the 24 rows already tagged outside the canonical 14 slots (`rank-modifier`, `meta-structure`, `infrastructure`, `access`, `mixed`, `structural`; 10.7% of the 225) may take any canonical value their notes plausibly bear, and (ii) an open-vocabulary re-extraction over a stratified subsample of `sources/*.txt` with the slot list withheld — and declare in advance that any absence-flavoured headline ("rank is a scalar, not a slot", "nothing in the standards is optimised for comprehension", "the stem exhausts the document") that moves inside those bounds, or any unmappable-element rate above a frozen threshold, will be reported as **vocabulary-conditional**, not as a finding.

  _origin: P11, post-check, AI-generated_

### P11-2 — *post-check re-open round; not rated*

Pre-register, as a pre-data revision with the same standing as v1→v2, a sensitivity gate for the finding-5 instrument — a positive control with a guaranteed ≥SESOI effect (answer-bearing content corrupted vs size-matched intact sham) plus a document-absent floor, run on the frozen machine panel before any recruitment — under the rule that no equivalence/null verdict about register, *including the "no detectable register effect" already printed in README v1.1/v1.2*, may be reported unless the instrument demonstrates ≥10 pp dynamic range on the same items, failing which the machine null is downgraded to an instrument-insensitivity note and the human arm stays paused.

  _origin: P11, post-check, AI-generated_

### P11-3 — *post-check re-open round; not rated*

Pre-register a lineage graph and a threshold k from evidence already on disk, then re-derive the atlas's convergence claims (universal stem, perfect fork, "17/25 authentication") under a lineage-restricted permutation null in which systems are exchangeable only within documented descent lines — with a frozen rule that any pattern failing to recur in ≥k independently rooted lineages is reported as **inheritance-plus-diffusion with the effective sample size equal to the number of independent origins**, not as convergence.

  _origin: P11, post-check, AI-generated_
