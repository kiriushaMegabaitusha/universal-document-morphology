# Evidence check E02 — bounded post-ideation literature search

Checker: evidence-checker E02 (session udm-ideation-01) · Date of all searches: **2026-10-15**
Scope: 6 assigned ideas — P06-2, P06-3, P06-4, P02-6, P04-1, P02-4.
Method: 1–3 `web_search` queries per idea (18 total), translated from each idea's statement into
searchable concepts + alternative terminology; at least one query per idea aimed at prior/adjacent
work that would CHALLENGE novelty or the premise. Judgments rest on search-result **snippets only**
— no paywalled page was opened or guessed at; every URL below appeared in an actual result.

Status vocabulary: `support-located` | `challenge-located` | `mixed` | `search-incomplete` | `not-checked`.
How I applied it: **challenge-located** = the yield is prior/adjacent art that materially undercuts
novelty or the premise, with no source found bearing on the idea's specific empirical claim;
**mixed** = a novelty challenge AND at least one source bearing on the idea's core premise/prediction
(supporting or undercutting it); **support-located** = only supportive evidence found.

Evidence is separated per idea into: **direct** (same objects/claims: official-document slot systems),
**indirect** (analogous domain, transferable method or finding), **no direct evidence located**.

> **Standing limit for every section: absence from this bounded 3-query search does NOT establish
> novelty.** Nothing here should be read as "no prior work exists" — only as "not found in these
> queries on this date."

---

## P06-2 — Exact null-model test: structural law or sparse-sample absence?

**Search questions.** (Q1) How are exact/permutation nulls run on co-occurrence patterns in small
binary feature matrices? (Q2) What is known about spurious "perfect" associations in sparse 2×2
tables / rule discovery? (Q3) [challenge] Has anyone already tested typological-style feature
co-occurrence for significance by chance, with multiple-testing control?

**Queries run (2026-10-15), exact strings.**
1. `permutation test co-occurrence binary matrix typological features chance null model`
2. `Fisher exact test spurious perfect association sparse contingency table small sample rule discovery`
3. `challenge: co-occurrence patterns in linguistic typology databases significant by chance multiple testing`

**Sources seen (titles + URLs, all real results).**
- Co-occurrence permutation test — https://stamatios.nicolis.web.ulb.be/apps/permutations.html
- Species co-occurrence null models in R – Tidy Ecology — https://tidyecology.com/posts/co-occurrence-null-models/
- Null model algorithms — SESraster (CRAN vignette) — https://cran.r-project.org/web/packages/SESraster/vignettes/null-models.html
- The use of Fisher's exact test in contingency table analysis in palaeopathology — https://pubmed.ncbi.nlm.nih.gov/41653486/
- Sensitivity of Fisher's exact test to minor perturbations in 2×2 contingency tables — https://pubmed.ncbi.nlm.nih.gov/3823670/
- Elucidating the Foundations of Statistical Inference with 2 × 2 Tables (PLOS ONE) — https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0121263
- Problems testing typological correlations with the online WALS (Dryer) — https://www.acsu.buffalo.edu/~dryer/DryerTestingWALS2009.pdf
- A statistical methodology for analyzing cooccurrence data from a large sample — https://pmc.ncbi.nlm.nih.gov/articles/PMC2041889/
- Randomization tests in language typology — https://exa.ai/library/publication/dcc8qlcy24c
- Quantitative Methods in Typology: Hypothesis testing (Leipzig slides, Bickel group) — https://www.isle.uzh.ch/bickel-files/Leipzig2010/le2010-2.pdf
- Beyond Binary Dependencies In Language Structure — https://exa.ai/library/publication/3926msz1jh0
- Replication and methodological robustness in quantitative typology — https://exa.ai/library/publication/m65w3rkwwj1
- Fitting a hypothesis too well: Real or manipulated data? (Significance, Oxford) — https://academic.oup.com/jrssig/article/22/2/24/7998829

**Evidence for.**
- Method is feasible and cheap: co-occurrence null models with fixed-fixed randomization and
  standardized effect sizes are packaged and routine (Tidy Ecology, SESraster, EcoSimR sim2/sim8,
  ecospat C-score) — *indirect* (ecology: sites × species, not systems × slots).
- The idea's premise is well attested in analogous data: "Beyond Binary Dependencies…" describes
  co-occurrence inflation from shared history/contact (Galton's problem) and notes that any
  reasonable sampling model produces proportion differences even with no effect (Cysouw 2010);
  Dryer shows raw language counts from WALS give misleading typological "correlations" —
  *indirect* support that a census rule ≠ a structural law.
- Small-n p-value behaviour matches the idea's stated risk: Fisher exact p-values are heavily
  discretized/conservative at small n, and 2×2 p-values are "extremely sensitive to small
  perturbations" (PubMed 3823670) — *indirect* support for the enumeration floor caveat.

**Evidence against / novelty challenge.**
- Randomization/exact tests for typological feature data are already an established, published
  method: "Randomization tests in language typology" proposes randomization tests precisely because
  typological data violate random-sampling assumptions, with a routine for checking whether a
  conclusion depends on a few sample languages (https://exa.ai/library/publication/dcc8qlcy24c).
- The Bickel Leipzig slides describe conditional (Monte-Carlo permutation) inference as the standard
  answer for non-random typological samples, citing Janssen, Bickel & Zúñiga 2006, plus family/area
  blocking — the same "tradition-blocked null" move the idea proposes (le2010-2.pdf, snippet text).
- Large-scale co-occurrence testing already has an FDR-adjacent machinery story (volume test +
  p-value plot for thousands of χ² co-occurrence tests, PMC2041889) — "per-edge tests + multiple
  testing on a co-occurrence matrix" is not a new combination.
- Dryer's paper is essentially a published warning that naive per-edge testing of feature pairs in
  exactly this kind of 25-ish-unit curated matrix produces misleading positives unless area/genera
  blocking is used — i.e. the methodological problem and its fix are prior art in the nearest domain.

**Status: challenge-located.**
**Direct vs indirect:** no direct evidence located (no source evaluates these document-slot rules);
indirect analogy only (typology/ecology co-occurrence nulls).
**Limits:** 3 queries, snippets only; English-language results dominated; the exa.ai library URLs are
mirror pages, not publisher pages; nothing here establishes that anyone has applied such a null to
official-document formats — and, equally, this search does NOT establish that nobody has.

---

## P06-3 — "Genre, not nation" as a variance partition with uncertainty

**Search questions.** (Q1) How is variance partitioned over binary presence/absence matrices with
two factors (PERMANOVA + Jaccard)? (Q2) [challenge] Has corpus research apportioned variation
between genre/register and geography/national variety? (Q3) [challenge] How much variance do genre
versus language/variety factors explain in multidimensional analyses?

**Queries run (2026-10-15), exact strings.**
1. `PERMANOVA Jaccard distance variance partitioning binary presence absence two factors effect size`
2. `corpus linguistics partitioning variance explained genre versus language family register dialect confounded`
3. `multidimensional analysis Biber genre register variation how much variance explained by genre vs language`

**Sources seen (titles + URLs, all real results).**
- PERMANOVA-S: association test for microbial community composition (Bioinformatics) — https://academic.oup.com/bioinformatics/article/32/17/2618/2450751
- Rarefaction-without-resampling extension of PERMANOVA for presence–absence associations (Bioinformatics) — https://academic.oup.com/bioinformatics/article/38/15/3689/6611716
- Multifactorial analysis of distance in studies of ecological community structure (JABES) — https://link.springer.com/article/10.1198/10857110260141256
- PERMANOVA (Wiley StatsRef entry) — https://onlinelibrary.wiley.com/doi/10.1002/9781118445112.stat07841
- ANOSIM for 2-way layouts … with comparative notes on PERMANOVA (Austral Ecology) — https://onlinelibrary.wiley.com/doi/10.1111/aec.13059
- Exploring variability within and between corpora (Gries) — https://www.stgries.info/research/2006_STG_ExploringVariability_Corpora.pdf
- A semi-supervised multivariate approach to the study of language variation (Diwersy, Evert, Neumann) — https://www.stephanie-evert.de/PUB/DiwersyEvertNeumann2012.pdf
- Variation in English world-wide: varieties and genres in a quantitative perspective (dissertation) — https://exa.ai/library/publication/swscm8h3p19
- Comparing Approaches to (Sub-)Register Variation — https://exa.ai/library/publication/nphw11sgbhv
- Issues of corpus comparability and register variation in the International Corpus of English — https://exa.ai/library/publication/0tswmtyql9l
- Using Register-Diversified Corpora for General Language Studies (Biber, Computational Linguistics) — https://aclanthology.org/J93-2001.pdf
- The Multi-Dimensional Approach to Linguistic Analyses of Genre Variation (Biber, Springer) — https://link.springer.com/article/10.1007/BF00136979
- Register, Genre and Style, ch. 9 Multi-Dimensional Patterns of Register Variation (Cambridge) — https://www.cambridge.org/core/books/register-genre-and-style/multidimensional-patterns-of-register-variation/F385D0F5EFED6DE86A63A7C0A8BC536D

**Evidence for.**
- **Directly relevant direction of effect (indirect domain):** the World Englishes dissertation
  (7,309 texts, 10 national varieties, 236 variables, EFA) "gives a unified account of different
  determinants of variation — the geographic and the generic-situational — and systematically
  compares their effects… the former [generic-situational] are established as significantly more
  powerful predictors of variation than the latter." That is exactly the idea's predicted ordering
  (genre > nation), already obtained once in an analogous design — *indirect* but on-point support.
- Feasibility: PERMANOVA with Jaccard on presence–absence data, partitioning variation across
  factors with permutation inference, is standard and documented (StatsRef entry; JABES distance-
  partitioning framework; two-way comparisons) — *indirect* (ecology/microbiome), the machinery the
  idea proposes exists out of the box.
- Corpus-linguistic framing matches: Gries's "Exploring variability within and between corpora"
  explicitly asks "are the variables A, B, C responsible for a significant proportion of P's
  variability?" — the partition-with-uncertainty move is established practice in corpus work.

**Evidence against / novelty challenge.**
- The genre-vs-geography variance comparison has, in substance, already been carried out at scale in
  World Englishes (dissertation above) — the idea's headline ("quantify genre-not-nation as an
  effect size") is not new as a research move, only as applied to this atlas's 25 slot systems.
- Register/genre labels are shown to be corpus-construction artifacts that can manufacture the very
  between-group differences being partitioned ("Comparing Approaches to (Sub-)Register Variation";
  "Issues of corpus comparability and register variation in ICE") — a challenge to the idea's
  assumption that its genre and tradition labels are clean partition terms.
- Unsupervised factor/PCA approaches are reported to let between-language/genre variation "completely
  obscure" subtler effects (Diwersy/Evert/Neumann) — a caution that a two-term partition may not
  behave as hoped with ~28 units.

**Status: mixed.**
**Direct vs indirect:** no direct evidence located on official-document slot systems; strong indirect
analogy (World Englishes, corpus register literature, PERMANOVA tooling).
**Limits:** snippets only; the two most on-point items are repository/mirror pages (exa.ai) whose
underlying dissertation I did not open; 3 queries; no search was run on "tradition family" as a
variance term per se (the term "national variety / geography" was used instead).

---

## P06-4 — Universality as a prevalence estimate: frame, intervals, leave-one-out, hold-out

**Search questions.** (Q1) What is known about generalizing prevalence/universality claims from
non-random typological-style samples? (Q2) Interval estimation for a proportion at small n plus
sensitivity/hold-out practice. (Q3) [challenge] Explicit critique of purposive/convenience
"sampling frames" behind universality claims.

**Queries run (2026-10-15), exact strings.**
1. `typological universals sampling bias non-random sample prevalence estimate confidence interval generalization`
2. `Wilson interval proportion small sample leave-one-cluster-out sensitivity pre-registered holdout prediction cross-linguistic`
3. `"sampling frame" purposive sample selection bias claims of universality linguistics WALS curated sample critique`

**Sources seen (titles + URLs, all real results).**
- A Principled Framework for Evaluating on Typologically Diverse Languages (ACL Anthology) — https://aclanthology.org/2026.cl-1.7.pdf
- A Principled Framework for Evaluating on Typologically Diverse Languages (arXiv HTML) — https://arxiv.org/html/2407.05022v2
- Ploeger et al., language-sampling framework paper (AAU PDF) — https://vbn.aau.dk/ws/portalfiles/portal/856610872/coli.a.577.pdf
- Sampling matters: commentary on "Replication and methodological robustness in quantitative typology" — https://exa.ai/library/publication/w0byqlgskk8
- Replication and methodological robustness in quantitative typology — https://exa.ai/library/publication/m65w3rkwwj1
- Sampling bias (Wikipedia) — https://en.wikipedia.org/wiki/Sampling_bias
- An Interval Estimation Approach to Sample Selection Bias (arXiv) — https://arxiv.org/pdf/1906.10159v2
- Correcting prevalence estimation for biased sampling with… (Statistics in Medicine) — https://onlinelibrary.wiley.com/doi/10.1002/sim.9885
- CI for a Proportion: Wald vs Wilson vs Exact (CASRAI guide) — https://casrai.org/guides/confidence-interval-for-a-proportion
- A Comprehensive Comparison of the Wald, Wilson, and adjusted Wilson… (arXiv) — https://arxiv.org/pdf/2508.10223
- A Critical Assessment of Bias in Survey Studies Using… location-based sampling (PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC5062950/

**Evidence for.**
- The idea's core recommendation — declare universe / frame / sample before generalizing — is spelled
  out and endorsed in current work: Bell (1978) universe-frame-sample notions are re-used verbatim in
  Ploeger et al., which stresses that "typologically diverse" samples in NLP are "mostly flawed and
  inconsistent" and that selection is usually post-hoc (*indirect*, same argumentative shape as the
  idea's "the 28 systems are a purposive sample selected by retrievability").
- The sampling commentary supports the premise that a sample must represent population variation for
  any population-level claim ("convenience samples are always suspect"; variety sampling married to
  statistical modelling) — *indirect* support for recasting 17/25 as an estimate over a stated frame.
- Wilson-interval guidance confirms the specific technical choice (Wald fails near 0/1 and small n;
  Wilson is the fix) — *direct* methodological support for the hand-computed [0.48, 0.83] idea
  (arithmetic itself not verified by me here).

**Evidence against / novelty challenge.**
- The whole apparatus the idea proposes (explicit frame, principled sampling, bias assessment via
  modelling, sensitivity to which units are included) is an established program in typology and its
  NLP offshoot — Bell 1978 / Rijkhoff & Bakker 1998 taxonomy, Dahl 2008, Stoll & Bickel 2013,
  Ploeger et al. 2024/2026 — so "recast a universality claim as a frame-bound prevalence estimate"
  is prior art as a method, even if not yet done for document-format slots.
- A sharper premise challenge: the sampling commentary argues the opposite of one of the idea's
  mitigations — "No statistical method could remedy such deficiencies in a convenience sample,"
  i.e. intervals and leave-one-out cannot repair a purposively retrieved frame; only a better sample
  can. The idea's fallback ("report the estimate under two or three pre-stated frames") is therefore
  weaker than the literature thinks.
- Prevalence estimation under biased/oversampled designs already has dedicated correction methods
  (Statistics in Medicine; interval-estimation approach to selection bias) — so "intervals under a
  biased frame" is not an untouched problem.

**Status: challenge-located.**
**Direct vs indirect:** no direct evidence located (no source estimates slot prevalence or tests a
document-format universality claim with intervals/hold-outs); indirect analogy only.
**Limits:** 3 queries, snippets only; no source was found on *pre-registered hold-out predictions in
typology* specifically (query 2 returned general Wilson-interval material instead — that sub-question
is effectively `search-incomplete` within this bounded run); absence ≠ novelty established.

---

## P02-6 — Slot ablation: per-slot functional value profile

**Search questions.** (Q1) [challenge] Has anyone removed document fields and measured the effect on
model answers/extraction? (Q2) Which document fields carry extraction performance (missing-field /
field-importance studies)? (Q3) [challenge] Sensitivity of readers to document content position/order
perturbation (would confound an ablation).

**Queries run (2026-10-15), exact strings.**
1. `ablation study removing document fields impact LLM question answering accuracy`
2. `information extraction forms which fields matter perturbation missing metadata document understanding ablation`
3. `LLM sensitivity to position order of document content in context "lost in the middle" field ordering prompt perturbation`

**Sources seen (titles + URLs, all real results).**
- AbGen: Evaluating Large Language Models in Ablation Study Design and Evaluation for Scientific Research — https://arxiv.org/html/2507.13300v1
- Robustness Evaluation of Transformer-based Form Field Extractors via Form Attacks — https://arxiv.org/html/2110.04413
- PM3-KIE: A Probabilistic Multi-Task Meta-Model for Document Key Information Extraction (Findings of ACL 2025) — https://aclanthology.org/2025.findings-acl.1075.pdf
- Data-Efficient Information Extraction from Form-Like Documents — https://ar5iv.labs.arxiv.org/html/2201.02647
- Few-Shot Learning for Structured Information Extraction From Form-Like Documents Using a Diff Algorithm (DI-2021) — https://document-intelligence.github.io/DI-2021/files/di-2021_final_3.pdf
- Extracting Zero-shot Structured Information from Form-like Documents: Pretraining with Keys and Triggers (AAAI) — https://ojs.aaai.org/index.php/AAAI/article/download/17494/17301
- Characterizing Positional Bias in Large Language Models: A Multi-Model Evaluation of Prompt Order Effects — https://aclanthology.org/2025.findings-emnlp.1124.pdf
- Can We Instruct LLMs to Compensate for Position Bias? — https://aclanthology.org/2024.findings-emnlp.732.pdf
- Found in the Middle: Permutation Self-Consistency Improves Listwise Ranking in LLMs — https://aclanthology.org/2024.naacl-long.129.pdf
- Lost in the Evidence? Reproducing Document Position and Context Size Effects in RAG (SIGIR) — https://dl.acm.org/doi/10.1145/3805712.3808569
- Attention Instruction: Amplifying Attention in the Middle via Prompting — https://arxiv.org/html/2406.17095
- Semantic Needles in Document Haystacks: Sensitivity Testing of LLM-as-a-Judge Similarity Scoring — https://arxiv.org/html/2604.18835v1
- Automatic Error Analysis for Document-level Information Extraction — https://arxiv.org/pdf/2209.07442v1.pdf

**Evidence for.**
- **Premise supported by direct-in-kind prior art (different domain):** the form-attacks paper already
  runs field-drop and field-perturbation ablations on invoices/receipts and quantifies the damage —
  a **Key Drop** transformation (keys/field labels removed "if accidentally missed by OCR") causes
  significant F1 loss; neighbor/background drops cost ~10% F1; text-order shuffle costs ~15–38% F1;
  the authors conclude "keys and neighbors are essential for value extractions" — *indirect* but
  strongly analogous: removal → measurable degradation, i.e. some fields are load-bearing.
- Obligatory-vs-optional framing has an engineering parallel: PM3-KIE encodes which fields are
  **mandatory** vs optional per schema and enforces them, explicitly noting models omit required
  elements — *indirect* support for using `obligation` as a dose prediction.
- Positional/ordering confounds are well documented (lost-in-the-middle; permutation self-consistency;
  SIGIR reproducibility study), which supports the idea's worry about removal artefacts and its need
  for a sham-deletion control — *indirect*.

**Evidence against / novelty challenge.**
- "Delete a field from a document and measure the extraction/performance drop" already exists as a
  published evaluation framework (Form Attacks, 14 form transformations incl. Key Drop, Global
  Shuffle, Value Location Augment) — the novelty of a per-field ablation profile is undercut at the
  method level, even though nobody has done it over a morphology-style canonical slot set.
- Field-level performance decomposition is also routine in KIE error analysis (mandatory/optional
  constraints, per-field F1 reporting in PM3-KIE; automatic error analysis for template filling) —
  "per-field value profile" is not a new artifact type.
- AbGen shows "ablation study design" itself is now a studied/benchmarked object in NLP, i.e. the
  vocabulary is crowded.

**Status: challenge-located.**
**Direct vs indirect:** no direct evidence located on official-document canonical slots (S1–S14) or
on who-did-what QA after slot removal; indirect analogy is strong (form-field ablation, KIE schemas,
positional bias).
**Limits:** 3 queries, snippets only; query 1 returned mostly "ablation study design" material rather
than content-ablation (that sub-angle is thin — treat as `search-incomplete` for the QA-with-ablated-
text variant); no source found using real/template-instantiated official documents with a sham
control — absence here does NOT establish that none exists.

---

## P04-1 — Slot-alphabet redundancy budget: entropy metric for document channels

**Search questions.** (Q1) [challenge] Any information-theoretic entropy/redundancy analysis of
document or message formats as channels? (Q2) Small-sample bias of mutual information/entropy
estimators and how it is corrected (the idea's stated feasibility risk). (Q3) [challenge] Shannon
entropy applied to bureaucratic/legal/document templates and their structure.

**Queries run (2026-10-15), exact strings.**
1. `information theoretic analysis document format redundancy entropy administrative forms channel capacity`
2. `mutual information small sample bias correction permutation null binary matrix contingency table estimator comparison`
3. `Shannon entropy applied to bureaucratic document templates structure corpus information content of a form`

**Sources seen (titles + URLs, all real results).**
- Influence of Format on Message Information Entropy and Loading of Communication Channels — https://exa.ai/library/publication/vfr59hqj8rg
- Exploring Whether Data Can be Represented as a Composite Unit in Form Processing Using the Manufacturing of Information Approach — https://espace2.etsmtl.ca/id/eprint/18860/1/Glaus%20M%202019%2018860.pdf
- Contextual information quality assessment methodology in data processing… (MSc thesis, form-as-channel) — https://espace.etsmtl.ca/id/eprint/2419/
- The Entropy of Digital Texts — The Mathematical Background of Correctness — https://pmc.ncbi.nlm.nih.gov/articles/PMC9955509/
- Simplify Your Law: Using Information Theory to Deduplicate Legal Documents — https://ar5iv.labs.arxiv.org/html/2110.00735
- Balisage: XML Entropy Study — https://www.balisage.net/Proceedings/vol8/html/Ruellan01/BalisageVol8-Ruellan01.html
- A bias correction for the mutual information sample estimator (Statistics & Probability Letters) — https://www.sciencedirect.com/science/article/pii/S0167715226001665
- Bias-Corrected Estimators for Joint Entropy, Conditional Entropy, and Mutual Information — https://arxiv.org/abs/2610.02558
- Mutual Information for Discrete Variables with Miller-Madow — https://metricgate.com/docs/mutual-information-discrete/
- Mutual information and the encoding of contingency tables — https://arxiv.org/html/2405.05393v1
- Entropy (information theory) (Wikipedia) — https://en.wikipedia.org/wiki/Entropy_(information_theory)
- Multi-scale information content measurement method based on… (arXiv) — https://arxiv.org/pdf/2305.12559

**Evidence for.**
- The idea's feasibility risk is confirmed by current method literature: plug-in estimators of joint
  entropy, conditional entropy and mutual information are biased at finite n, with explicit first-
  order bias formulas and published bias corrections (arXiv 2610.02558; "A bias correction for the
  mutual information sample estimator"; Miller-Madow tooling) — *direct* support for the requirement
  "bias-corrected estimators + permutation nulls are mandatory at n = 25".
- The premise that forms/formats carry measurable redundancy is supported: the manufacturing-of-
  information line treats **the form as the communication channel** and detects redundant fields
  (student ID vs employee ID), reporting that a redesigned form cut input data 50% while raising
  information quality 15% — *indirect but same object class (administrative forms)*.
- Legal-text work measures redundancy information-theoretically (MDL/duplicated-phrase detection in
  the U.S. Code) — *indirect* support that "structure spent on something other than comprehension"
  is measurable.

**Evidence against / novelty challenge.**
- **Strongest challenge:** an earlier report already did the format-as-channel entropy budget for a
  class of formatted messages: "Influence of Format on Message Information Entropy and Loading of
  Communication Channels" concludes that in Navy formatted messages "the format carries about 66
  percent of the text, but only 6.5 percent of its information content" and that the language has
  ">85-percent redundancy compared with asymptotic information content" — i.e. "formal format bits go
  to structure/overhead, not content" has been quantified before, in a directly comparable framing.
- Structure-vs-content entropy decomposition of documents also exists (XML Entropy Study splits
  entropy by event type/structure vs content and shows structure entropy dominating certain
  encodings) — the "per-slot share of total redundancy" decomposition has a close precedent.
- Entropy-of-documents work already exists for correctness/formatting/modification of digital texts
  (PMC9955509) — "apply Shannon entropy to documents and call it a quality metric" is occupied ground,
  albeit measuring different things.

**Status: mixed.**
**Direct vs indirect:** no direct evidence located for the atlas's 14-slot codewords; near-direct
analogy for the Navy formatted-message result and the form-as-channel IQ work; method-level direct
support from MI/entropy bias-correction literature.
**Limits:** 3 queries, snippets only; the Navy report and exa.ai item are mirror/library pages — I did
not verify the underlying report's provenance or date; two 2026-dated arXiv/Elsevier items were read
from snippets only; absence of a search hit on "redundancy budget of official document requisites"
does NOT establish novelty.

---

## P02-4 — Semantic gate: entailment check of ledger claims against retrieved sources

**Search questions.** (Q1) LLM/NLI verification of claims against their source text. (Q2) [challenge]
Established pipelines requiring verbatim quotes / atomic-fact support (FActScore, ALCE-style,
attribution verification). (Q3) [challenge] Automated detection that a citation's claim is
unsupported/overstated by the cited source.

**Queries run (2026-10-15), exact strings.**
1. `LLM claim verification against source text NLI citation entailment supported quote attributed generation`
2. `FActScore ALCE atomic fact verification retrieval evidence quote support free-form claim checking benchmark`
3. `automatic detection of citation claim mismatch overstatement source paper reference checking LLM entailment pipeline`

**Sources seen (titles + URLs, all real results).**
- Claim Verification in the Age of Large Language Models: A Survey — https://arxiv.org/html/2408.14317v1
- Cited but Not Verified: Parsing and Evaluating Source Attribution in… — https://arxiv.org/html/2605.06635
- Citation and Grounding: Attributing Answers (Neel Mishra blog) — https://neelmishra.github.io/blog/mlops/rag/citation-grounding.html
- LLM-Cite: Cheap Fact Verification with Attribution via URL Generation (OpenReview) — https://openreview.net/forum?id=qb2QRoE4W3
- FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation — https://arxiv.org/abs/2305.14251 (also https://aclanthology.org/2023.emnlp-main.741/ and https://github.com/shmsw25/FActScore)
- CiteCheck: Retrieval-Grounded Detection of LLM Citation Hallucinations in Scientific Text — https://arxiv.org/abs/2605.27700
- awesome-citation-claim-verification (curated paper list) — https://github.com/get-tushar-iiita/awesome-citation-claim-verificatation
- SourceCheckup: An automated framework for assessing how well LLMs cite sources (Nature Communications) — https://www.nature.com/articles/s41467-025-58551-6
- Attribution and Citation: Sourcing LLM Outputs (blog) — https://mbrenndoerfer.com/writing/attribution-and-citation
- How to Build Output Grounding and Fact-Checking for LLM Apps (blog) — https://agentbus.sh/posts/how-to-build-output-grounding-and-fact-checking-for-llms/

**Evidence for.**
- The proposed mechanics are known-good: "A robust citation verification pipeline uses Natural
  Language Inference (NLI) to check whether each cited claim is actually entailed by its source"
  (Neel Mishra blog) — the claim → source → entailment → supported/partial/not-supported pattern the
  idea describes is documented as working practice — *direct* methodological support (implementation
  genre, not this repo).
- "Cited but Not Verification" frames exactly the idea's evaluator task: "the evaluator must assess
  whether a claim is supported by retrieved source content" — confirming the problem framing is live
  and that partial/not-found outputs plus review queues are the accepted output shape.
- Cost assumption is consistent with FActScore-style reporting: FActScore states ~$1 of API cost per
  100 sentences — *indirect* support that ~92–200 calls is trivially affordable.

**Evidence against / novelty challenge.**
- **This is the most crowded space of the six.** Atomic-fact decomposition + support checking against
  a knowledge source (FActScore, EMNLP 2023), claim-verification surveys (arXiv 2408.14317),
  source-attribution verification ("Cited but Not Verified"), agent pipelines scoring relevance and
  **supportiveness** of sources (SourceCheckup, Nature Communications 2025), citation-hallucination
  detection (CiteCheck), and entailment-checked URL citation (LLM-Cite) all predate the idea; a
  curated "citation-claim-verification" literature list exists on GitHub.
- Verbatim-quote string-matching as a hallucination guard is already standard advice in the
  attribution/grounding write-ups seen (quote must appear in source; exact-quote matching mitigates
  false entailment) — so the idea's distinctive "mechanical quote match" component is prior art too.
- Nothing found addresses the repo's specific situation (a local `ledger.json` over 60 on-disk
  sources with 4 blocked-host provisional claims); the novelty, if any, is only the application
  context, not the method.

**Status: challenge-located.**
**Direct vs indirect:** direct methodological prior art located (same pipeline shape: claim →
retrieved source → entailment + quote verification → review queue); no evidence located about this
repository's ledger specifically.
**Limits:** 3 queries, snippets only; several hits are blogs/READMEs rather than peer-reviewed pages
(used only to illustrate that the pattern is documented practice, not as authority); ALCE was named in
my query but no ALCE result actually appeared in the results — I therefore do **not** cite ALCE as a
seen source. Absence of a hit on "ledger claim verification for curated research repos" does NOT
establish novelty of that narrower variant.

---

## Cross-cutting notes

- 18 queries total, all run 2026-10-15, all `web_search`; no page was opened beyond the search
  results themselves, so every claim above rests on snippet text.
- Repeated pattern across ideas: **methods are almost never new; the domain application is.** For
  P06-2/P06-4/P04-1/P02-4 the methodological moves have close prior art in typology, ecology,
  communications and NLP respectively; for P06-3 the substantive genre-vs-geography comparison has
  been published in World Englishes; for P02-6 field-drop ablation exists in form-extraction robustness
  work. What none of these searches located is prior work on **official-document slot morphology
  itself** — and per the standing limit above, that is a bounded-search observation, not evidence of
  novelty.
- Backend note: several searches were auto-rescued by an alternate search backend after the default
  one failed; results were still real and recorded verbatim.