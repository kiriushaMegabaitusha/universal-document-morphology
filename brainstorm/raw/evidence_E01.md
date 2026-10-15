# Evidence check E01 — bounded post-ideation literature check (step 8)

**Checker:** E01 | **Session:** udm-ideation-01 | **Date of all searches:** 2026-10-15
**Assigned ideas:** P01-1, P02-2, P08-6, P02-1, P06-1, P07-5
**Method:** 1–3 targeted web_search queries per idea (18 total), translated from each idea's statement into searchable concepts + alternative terminology; at least one challenge-oriented query per idea. Evidence taken from search-result snippets; pages not separately verified unless the snippet itself carried the content. Only sources that appeared in actual results are listed.
**Standing caveats:**
- This is a **bounded** search (18 queries, snippet-level). **Absence from this search does NOT establish novelty** for any idea — it only means nothing surfaced in these specific queries.
- Status vocabulary: support-located | challenge-located | mixed | search-incomplete | not-checked.
- Evidence classes per idea: **direct** (speaks to this idea's specific claim) / **indirect analogy** (same method or phenomenon in another domain) / **no direct evidence located**.

---

## P01-1 — Pre-modern stress test of the genre fork (S6 ⊥ S9 vs historical mixed genres)

**Search questions.** (Q1) Do pre-modern chancery instruments structurally combine a named addressee (destination) with a recital/preamble? (Q2) Do letters patent combine addressee + whereas-recital? (Q3) Do Ottoman firmans combine a formal address (inscriptio) with a recital (narratio/temhid)? Q3 aimed at adjacent diplomatics work that could show the co-occurrence is already well documented (novelty/premise challenge).

**Queries run (all 2026-10-15).**
1. `medieval charter structure arenga recital address diplomatics co-occurrence`
2. `letters patent recital addressee "whereas" structure addressed instrument`
3. `Ottoman ferman structure addressed governor preamble recital chancery`

**Sources seen (titles + URLs, real results only).**
- Diplomatics: The Science of Reading Medieval Documents — https://www.rmoa.unina.it/7518/1/Gallo-DEF-online.pdf
- Methods of Reading And Writing Ottoman Archival Documents … Registers of Important Affairs and Imperial Firmans — https://journals.univ-msila.dz/index.php/AHJ/article/download/10184/7838/14793
- FERMAN — DIPLOMATIČKI OSVRT (The ferman – a survey in diplomatics) — https://exa.ai/library/publication/2dn59jhpx5h
- An Analysis and Comparison of Berat and Ferman in Ottoman Diplomatics (Bulgarian Historical Review) — https://www.academia.edu/42202226/
- Letters patent — Wikipedia — https://en.wikipedia.org/wiki/Letters_patent
- Recitals Clause: Whereas Clauses & Interpretive Effect — https://www.contractken.com/glossary/recitals-clause
- Letters Patent (CBAI corpus item, "AND WHEREAS" incipit) — https://cbaionline.org/corpus/items/show/486
- (De Gruyter) chapter on composition of early medieval charters (arenga/inscriptio formulae by charter type) — https://www.degruyterbrill.com/document/doi/10.1515/9783110987126-008/pdf
- Parts of a Charter — After Empire (St Andrews) — https://arts.st-andrews.ac.uk/after-empire/2017/11/29/parts_of_a_charter/
- Ad fontes tutorial: Charters and Diplomatics (UZH) — https://www.adfontes.uzh.ch/en/tutorium/quellen-auswerten/urkunden-und-diplomatik/

**Evidence for (direct).**
- The Gallo diplomatics overview defines the standard medieval instrument as protocol (invo­catio, intitulatio, **inscriptio = address of the addressee**, salutatio) **plus textus** (arenga = **preamble/proem**, narratio, dispositio …) — i.e., address and preamble are structural parts of the *same* instrument, not mutually exclusive slots.
- The Ottoman ferman analyses describe exactly the disputed cell: an **INSCRIPTIO / "Imperial Address"** addressed to named officials ("Directives … addressed to its recipient … formulas depending on the rank of the addressee") **plus** preface/narration sections ("Nakil veya İblağ … explains the reason the ferman was written"). The academica.edu comparison states fermans "directly address officials or their offices" while both fermân and berât share standard components.
- Letters patent are by definition written orders "issued by a monarch … granting an office or right … to a person or corporation" (Wikipedia) and real letters-patent specimens in the CBAI corpus open with "AND WHEREAS" recitals — an addressed instrument with recitals.
- The De Gruyter chapter shows arenga usage varies systematically by charter type/transaction (frequency differences across donation/exchange/precaria charters) — heterogeneity, not exclusivity.

**Evidence against / novelty challenge (direct vs indirect).**
- *Direct:* none located — no source in these results claims addressee and preamble are complementary/exclusive in pre-modern instruments.
- *Indirect novelty challenge:* diplomatics has analyzed these formula inventories and their co-presence for centuries (Mabillon tradition, Fichtenau's *Arenga* 1957 referenced); the *components* are old scholarship. What no result showed is anyone testing a formal S6×S9 co-occurrence table across ≥3 chancery traditions — so the specific comparative test is **no direct evidence located** in this search.

**Status: support-located.**
**Evidence class:** directly relevant evidence for the premise (pre-modern addressed + recital instruments exist and are documented); no direct prior test of the fork located; method-level background is indirect.
**Limits.** Snippet-level only; no full text verified; Ottoman material in Turkish/French/English mix; no query specifically searched Ge'ez/Ethiopic or Sanskrit traditions; medieval sources describe parts, not co-occurrence *rates*; bounded search ≠ novelty established.

---

## P02-2 — Document-level scale test of the epistolary/normative fork (S6 ⊥ S9)

**Search questions.** (Q1) Can recital ("whereas") and address/preamble components be detected automatically in large official/legal document corpora? (Q2) Is there prior computational work classifying document components (recitals vs operative parts) at scale? (Q3) Prior work on automatic genre/structure classification of official documents that would challenge novelty of the tagging approach.

**Queries run (all 2026-10-15).**
1. `automated tagging "whereas" recitals address blocks corpus official documents NLP genre classification`
2. `computational corpus study legal documents recital clauses versus operative provisions classification`
3. `document genre classification large corpus official documents correspondence versus regulation NLP prior work`

**Sources seen.**
- LEDGAR: A Large-Scale Multi-label Corpus for Text Classification of Legal Provisions in Contracts (LREC 2020) — https://aclanthology.org/2020.lrec-1.155.pdf
- Annotated corpus of contract documents for recognizing rights/obligations (LREC 2020; describes English contract structure: premises/parties → **whereas clauses** → operative part → closing) — https://aclanthology.org/2020.lrec-1.251.pdf
- Annotation and Classification of Relevant Clauses in Terms-and-Conditions Contracts (LREC 2024; 14 categories, IAA 0.92) — https://aclanthology.org/2024.lrec-main.108/
- Corpus Based Classification of Text in Australian Contracts (*AUSNA?* ACL 2010; classes include RECITALHEAD, RECITALLINE, PARTIESHEAD, OPERATIVEPROVISIONLINE) — https://aclanthology.org/U10-1005.pdf
- Legal Whereas Clause Binary Classifier (md) (John Snow Labs, 2022) — https://nlp.johnsnowlabs.com/2022/11/25/legclf_whereas_md_en.html
- Legal Whereas Clause Binary Classifier (legclf_cuad_whereas_clause) (John Snow Labs, 2022) — https://nlp.johnsnowlabs.com/2022/09/20/legclf_cuad_whereas_clause_en.html
- The Form is the Substance: Classification of Genres in Text (ACL 2001) — https://aclanthology.org/W01-1007.pdf
- Long-length Legal Document Classification (arXiv 1912.06905) — https://arxiv.org/abs/1912.06905
- Squibs: Stable Classification of Text Genres (J11-2004) — https://aclanthology.org/J11-2004.pdf

**Evidence for (direct).**
- Automatic detection of **recital/whereas components** in legal documents is a shipped, published task: dedicated whereas-clause binary classifiers exist (John Snow Labs, CUAD-derived), and multiple annotated corpora label recitals/parties/operative parts as structural spans (LREC 2020 contract corpus explicitly documents the premises–whereas–operative structure; Australian contracts corpus has RECITALLINE as a class).
- Large-scale provision/genre classification of legal corpora is demonstrated (LEDGAR: ~100k provisions, 12k labels; genre classifiers at 9,705-document scale) — supports the feasibility assumption that taggers + open corpora give document-level rates with real denominators.

**Evidence against / novelty challenge (direct vs indirect).**
- *Direct novelty challenge (method):* component-level and genre-level automatic tagging of official/legal documents is well-trodden prior art (above). The idea's *tagging machinery* is not new; only its use to test destination×preamble co-occurrence could be new.
- *Direct premise evidence:* **no direct evidence located** in this search for or against the S6⊥S9 complementarity claim itself at document scale — no result reported co-occurrence rates of addressee and recital across corpora/scripts.
- *Indirect:* contract-domain corpora show recitals and parties co-occur routinely *within contracts* — a reminder that in some document populations both slots appear together (single-domain analogy, not the atlas's genres).

**Status: mixed.**
**Evidence class:** direct evidence for feasibility (tagging recitals/address at scale is established); indirect analogy only for the fork's behavior; no direct evidence on the fork located.
**Limits.** Snippets only; contract-domain results dominate — UN/EUR-Lex/gazette-scale tagging not directly confirmed in results; no multilingual/script evidence checked beyond English; queries in English may miss non-Anglophone legal-NLP work; bounded search ≠ novelty established.

---

## P08-6 — The third declension: does the deliberative note break the two-genre fork?

**Search questions.** (Q1) Is the French *note de service / note administrative* a documented, distinct internal genre and what is its function? (Q2) Is the Indian secretariat/Cabinet note a documented genre "arguing toward a decision"? (Q3) Challenge query: do existing administrative/organizational genre taxonomies already describe many-genre systems (memo/note families), undermining the framing of a novel "third class"?

**Queries run (all 2026-10-15).**
1. `"note de service" administrative genre fonction document interne argumentation France`
2. `Indian secretariat note decision-making administrative document genre argumentation`
3. `administrative document genre taxonomy internal notes memoranda deliberative working papers typology`

**Sources seen.**
- Note de service : rédaction, exemple et modèle (culture-rh.com, 2026-07-13) — https://culture-rh.com/note-de-service-utilite-contenu-exemples-modele/
- La Note de Service (Scribd) — https://fr.scribd.com/document/700538207/La-Note-de-Service
- Guide La Note Administrative (Scribd) — https://fr.scribd.com/document/369668820/Guide-La-Note-Administrative
- Modèle de Note de Service Administrative / La-note-de-service (Scribd) — https://www.scribd.com/document/470782495/La-note-de-service
- Government of India Cabinet Secretariat, Handbook on writing Cabinet Notes — https://cabsec.gov.in/writereaddata/handbook/english/1_Upload_3722.pdf (mirror: https://www.cabsec.nic.in/files/preperationofnotes/preperationofnotes.pdf)
- Genre Taxonomy: A Knowledge Repository of Communicative Actions (MIT CCS WP209) — http://ccs.mit.edu/papers/pdf/wp209.pdf ; ResearchGate record — https://www.researchgate.net/publication/220515773_Genre_taxonomy_A_knowledge_repository_of_communicative_actions
- Types of Administrative Documents (Scribd) — https://www.scribd.com/document/912419704/Models-of-Administrative-Documents
- Understanding Internal Correspondence (Scribd, Unit 13: memorandums, letters, office orders, circulars, notices, agendas, minutes) — https://www.scribd.com/document/559989003/Unit-13

**Evidence for (direct).**
- The French *note de service* is a documented, nameable internal genre ("document interne officiel … transmettre des consignes, annoncer des changements ou rappeler les règles"; "document interne par lequel un supérieur donne à ses subordonnés soit des informations, soit des instructions"), and *note administrative* has its own drafting guide with "différents types de notes administratives" — a stable functional genre exists across Francophone administration, supporting the assumption that a functional definition can locate the genre.
- The Indian Cabinet note is an official, handbooks-regulated genre ("Cabinet Notes as instruments of policy making"; "conceptually clear, lucid and well-organized" arguments placed before Cabinet) — directly supports the "argue toward a decision" functional definition (P08-6's core assumption and Prediction 1's Indian pole).

**Evidence against / novelty challenge (direct vs indirect).**
- *Direct, against Prediction 2's clean profile:* the French sources describe note de service as transmitting **instructions/rules** (and carrying regulation-like force when disciplinary) — i.e., a normative-flavored function. Notes may therefore not form a profile "empty of preamble/authentication" uniformly; they may scatter toward the normative pole, which the idea itself lists as its disconfirmation path.
- *Indirect novelty challenge:* organizational genre taxonomies already exist at fine granularity (MIT "Genre Taxonomy" prototype with memo and many specific genres; internal-correspondence teaching taxonomies list memos, circulars, notices, minutes as distinct classes) — multi-genre classification of administrative documents is established framing, so "a genre beyond two" is not conceptually new.
- *No direct evidence located* on whether notes occupy a distinct *slot profile* (S6⊥S9 residual cluster) — nobody in these results codes notes against destination/preamble slots.

**Status: mixed.**
**Evidence class:** direct evidence for genre identifiability (Feasibility/Assumption) in France and India; direct counterevidence (instruction function) against a uniformly deliberative profile; indirect only for the "third class vs binary fork" framing; no direct slot-profile evidence located.
**Limits.** Snippets only; many French results are template/Scribd pages, not peer-reviewed scholarship; no query covered Bénin's *note* specifically, nor Soviet протокол/Chinese 呈 traditions needed by Prediction 1; searches in English+French only; bounded search ≠ novelty established.

---

## P02-1 — Machine second coder for the slot and theme coding

**Search questions.** (Q1) Has LLM-as-second-coder with Cohen's κ against human coding been done? (Q2) Do LLMs substitute for human coders in social-science text coding — validity/reliability evidence? (Q3) Challenge query: does evidence show LLM agreement is unreliable/biased, undermining the premise that a machine coder measures what a human second coder would?

**Queries run (all 2026-10-15).**
1. `LLM second coder inter-rater reliability annotation Cohen kappa agreement study`
2. `large language models replace human annotators text coding reliability validity social science`
3. `LLM annotation agreement limitations shared bias human coders validity caution`

**Sources seen.**
- Investigation of the Inter-Rater Reliability between Large Language Models and Manual Coding (arXiv 2508.14764) — https://arxiv.org/html/2508.14764v1
- Multi-LLM Thematic Analysis with Dual Reliability Metrics (arXiv 2512.20352) — https://arxiv.org/pdf/2512.20352
- Navigating the Risks of Using Large Language Models for Text Annotation in Social Science Research (Lin & Zhang, SAGE, 2026) — https://journals.sagepub.com/doi/10.1177/08944393251366243
- Data Annotation with Large Language Models: Lessons from a Large Empirical Evaluation (eddieyang.net) — https://www.eddieyang.net/research/llm_annotation.pdf
- Best Practices for Text Annotation with Large Language Models (Sociologica) — https://sociologica.unibo.it/article/view/19461
- The Alternative Annotator Test for LLM-as-a-Judge (ACL 2025) — https://aclanthology.org/2025.acl-long.782.pdf
- Are chatbots reliable text annotators? Sometimes (PNAS-style empirical, PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC11954583/
- Observational Equivalence of LLM and Human Annotation (arXiv 2609.22133) — https://arxiv.org/pdf/2609.22133
- Evaluating how LLM annotations represent diverse views (arXiv 2503.23243) — https://arxiv.org/html/2503.23243

**Evidence for (direct).**
- The exact protocol proposed is established prior art and demonstrably runnable: an LLM prompted to replicate manual coding with Cohen's κ computed afterwards (arXiv 2508.14764: κ>0.6 for three themes, moderate for one after prompt/hyperparameter optimization); dual κ+semantic metrics for LLM thematic analysis (arXiv 2512.20352).
- Positive precedent exists that LLMs can match/beat human annotators in some settings (Gilardi et al. PNAS 2023 cited within results; "Observational Equivalence…" claims LLM–expert agreement comparable to expert–expert; ACL alt-test passes on 9/10 datasets) — supports feasibility of a machine second coder.

**Evidence against / novelty challenge (direct vs indirect).**
- *Direct novelty challenge:* LLM-as-coder/second-rater, κ reporting, and best-practice guidelines are a crowded, mature literature (Sociologica best-practices essay; SAGE risks framework; alt-test paper; multiple 2025–2026 reliability studies). The approach itself is plainly not new — only its application to `requisites.csv` could be.
- *Direct challenge to the idea's key assumption:* "Data Annotation with LLMs: Lessons from a Large Empirical Evaluation" reports LLM annotations have **low intercoder reliability with original human annotations (Krippendorff α 0.12–0.46)**, only moderate agreement among LLMs (α 0.14–0.69), and **downstream conclusions change in >1/3 of cases**; it also finds humans agree with each other more than with LLMs (α 0.62 vs 0.34) — directly contesting P02-1's stated assumption that "machine-coded agreement bounds human inter-rater agreement." "Are chatbots reliable text annotators? Sometimes" likewise advises caution (supervised DistilBERT often outperforms).

**Status: challenge-located.**
**Evidence class:** direct evidence both for feasibility (protocol exists) and against the premise (machine κ ≠ human κ bound) plus direct novelty challenge (mature prior art); no direct evidence about *this atlas's* 14-slot vocabulary located.
** Limits.** Snippets only, none of the papers opened in full; heterogeneous tasks (themes, sentiment, political text) — no result addresses a 14-slot cross-script morphology coding; results are conflicting by design (equivalence vs low-α papers both seen); bounded search ≠ novelty established.

---

## P06-1 — Measure coding reliability once, then propagate measured error into every headline figure

**Search questions.** (Q1) Is "quantify misclassification then propagate via simulation" an established method? (Q2) Is propagating coder uncertainty through content-analysis findings a known workflow? (Q3) Challenge query: is reliability-measure-then-robustness already standard practice (making the extension incremental)?

**Queries run (all 2026-10-15).**
1. `probabilistic bias analysis misclassification propagate measurement error simulation study results uncertainty`
2. `intercoder reliability propagate coding uncertainty through analysis sensitivity simulation content analysis`
3. `reliability-driven robustness analysis recode subsample kappa findings withstand misclassification established method`

**Sources seen.**
- Probabilistic Quantitative Bias Analysis for exposure/outcome misclassification (tutorial, ScienceDirect, 2026) — https://www.sciencedirect.com/science/article/pii/S0828282X25015776
- Probabilistic Sensitivity Analysis of Misclassification (Columbia Mailman, population-health methods) — https://www.publichealth.columbia.org/research/population-health-methods/probabilistic-sensitivity-analysis-misclassification
- SAS and R code for probabilistic quantitative bias analysis (Int J Epidemiol 52(5):1624) — https://academic.oup.com/ije/article/52/5/1624/7152433
- Probabilistic Bias Analysis for Simulation of Summary Level Data (Springer chapter, 2022) — https://link.springer.com/chapter/10.1007/978-3-030-82673-4_8
- Intercoder Reliability (Sage Encyclopedia of Communication Research Methods) — https://methods.sagepub.com/ency/edvol/the-sage-encyclopedia-of-communication-research-methods/chpt/intercoder-reliability
- Content Analysis: Coding Text Systematically (CASRAI guide) — https://casrai.org/guides/content-analysis
- Practical Resources for Assessing and Reporting Intercoder Reliability in Content Analysis (Bracken/Neuendorf PDF) — https://www.researchgate.net/profile/Cheryl-Bracken/publication/242785900_...
- Multi-LLM Thematic Analysis with Dual Reliability Metrics (arXiv 2512.20352) — https://arxiv.org/html/2512.20352v1

**Evidence for (direct).**
- The **propagation step has a validated playbook**: Monte Carlo Sensitivity Analysis / probabilistic quantitative bias analysis explicitly "translate[s] uncertainty about a study's bias parameters into a distribution of bias-adjusted estimates" by specifying distributions for sensitivity/specificity and re-simulating (Columbia; IJE code paper; Greenland 2005 & Lash et al. 2011 referenced there) — direct support that "measure error once, re-run analysis under perturbed codings" is executable and publishable methodology.
- The **measurement premise** is supported: intercoder reliability is described as an integral, expected part of content analysis used to "argue for the consistency … of findings" (Sage; CASRAI) — consistent with the repo's admission that κ is missing being a real gap.

**Evidence against / novelty challenge (direct vs indirect).**
- *Direct novelty challenge (method-level):* the whole chain — estimate misclassification, simulate, report which conclusions survive — is **decades-old established practice** in quantitative methods (probabilistic QBA, MCSA; systematic-error quantification is textbook). The idea's novelty is only the repo-specific four-layer application; a reviewer could call it an application of standard QBA to a small coded dataset.
- *Direct, mildly against:* Columbia's overview notes that in practice quantitative assessment of misclassification bias "is limited" and often qualitative — suggesting the workflow is standard *in principle* but not ubiquitous in applied work; and no result was found showing propagation from intercoder κ through *tabular/complementary-distribution* findings (the atlas's specific statistic class) — **no direct evidence located** on that transfer.
- *Indirect:* intercoder-reliability reporting guidance covers measurement but the searched guides did not describe propagate-into-headline-figures as a standard step — propagation beyond epidemiology appears less codified (indirect only).

**Status: challenge-located.**
**Evidence class:** direct support for feasibility (MCSA/QBA machinery) and for the reliability-gap premise; direct method-level novelty challenge (established bias-analysis practice); no direct evidence for the atlas-specific propagation targets located.
**Limits.** Snippets only; searches weighted to epidemiology/public-health terminology — communication-science or political-science "coding error propagation" work may use other vocabulary and was not exhaustively queried; no paywalled full texts opened; bounded search ≠ novelty established.

---

## P07-5 — Evidence-tier stress test: does the universal stem survive on primary-anchored systems only?

**Search questions.** (Q1) Is "restrict the analysis to the strongest-evidence subset and re-check conclusions" an established robustness technique? (Q2) Can evidence-tier/primary-source-only recomputation be grounded in documented method (challenge: standard practice)? (Q3) Cross-national/robustness-check precedent for recomputing universality claims on high-quality subsets.

**Queries run (all 2026-10-15).**
1. `sensitivity analysis restricting to studies low risk of bias evidence quality subset reanalysis robustness`
2. `primary source evidence tier grading recompute claims subset only thin documentation sensitivity`
3. `cross-national dataset robustness check subset high-quality cases only universality claim conditional analysis`

**Sources seen.**
- Incorporating 'risk of bias' assessments into meta-analyses (Cochrane Methods) — https://methods.cochrane.org/sites/methods.cochrane.org.bias/files/uploads/JH%20incorporating%20in%20meta-analyses.pdf
- Sensitivity Analysis in Meta-Analysis: A Tutorial (PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12767030/
- How do systematic reviews incorporate risk of bias assessments into the synthesis of evidence? (J Epidemiol Community Health 69(2):189) — https://jech.bmj.com/content/69/2/189
- Methodological tools and sensitivity analysis for assessing quality/risk of bias in systematic reviews (BMC Med Res Methodol) — https://link.springer.com/article/10.1186/s12874-020-00966-4
- Sensitivity and subgroup analysis in a meta-analysis – What we should know? (PMC) — https://pmc.ncbi.nlm.nih.gov/articles/PMC11498262/
- Chapter 5: Checking for Robustness (ACRE guide, Berkeley) — https://bitss.github.io/ACRE/robust.html
- RobuAI: Robustness Analysis AI (tool for alternative analysis paths to verify robustness of central claims) — https://lukasroeseler.github.io/robuai/
- Query 2 returned **no usable relevant results** (unrelated software/engineering docs about evidence tiers).

**Evidence for (direct, method-level).**
- Restricting the synthesis to the strongest-evidence stratum and re-running is *the* major recognized approach: "the major approach to incorporating risk of bias assessments in Cochrane reviews is to **restrict meta-analyses to studies at low risk of bias, or to stratify**" (Cochrane Methods); the JECH methodological study finds the common incorporation methods are "sensitivity analysis, narrative discussion and exclusion of studies at high RoB"; the BMC survey found quality/RoB-based sensitivity analysis was the most common sensitivity analysis (41% of those performed).
- The idea's own risk (small-n, "informative but underpowered") is corroborated as a known failure mode: in the JECH study, **half of the Cochrane reviews that planned a quality-restriction sensitivity analysis could not perform it due to too few studies** — direct support for P07-5's A2/A3 concern.
- Robustness-checking central claims across alternative specifications is a codified workflow in empirical social science (ACRE "Checking for Robustness"), and automated robustness tools exist (RobuAI).

**Evidence against / novelty challenge (direct vs indirect).**
- *Direct novelty challenge (method):* tier-restricted re-estimation is standard, long-established practice across evidence synthesis — the *technique* is not novel; only its application to this atlas's frozen ledger is repo-specific.
- *Direct challenge to clean execution:* quality thresholds used for such restrictions are "highly heterogeneous and inconsistent" across published reviews (BMC survey; only 52% even defined their threshold) — supports the idea's A1 (freeze tiers pre-hoc) as necessary but shows the tier-cut is conventionally arbitrary ("All thresholds are arbitrary" — Cochrane slide deck), which weakens any strong reading of a pass/fail result.
- *Indirect/against statistical force:* excluding studies narrows n and can flip results by chance (PMC tutorial warnings) — aligns with the idea's own "underpowered, must not be sold as confirmation."
- **No direct evidence located** on conditioning *morphological/universality* claims in document-typology corpora on source-grounding tiers — this specific combination did not surface.

**Status: challenge-located.**
**Evidence class:** direct method-level prior art (robustness via evidence-quality restriction is standard) with direct corroboration of the underpowering risk; no direct evidence about the atlas's stem/fork claims located; cross-domain analogy (meta-analysis) carries the bulk of the support.
**Limits.** One of three queries (Q2) returned nothing usable; heavy reliance on medical-review methodology as analogy — comparative politics/qualitative multi-case robustness work may use different vocabulary and was not exhaustively searched; snippet-level only; bounded search ≠ novelty established.

---

## Summary table

| Idea | Status | Direct evidence? |
|---|---|---|
| P01-1 | support-located | Direct: pre-modern instruments structurally combine addressee + recital/preamble (diplomatics, Ottoman, letters patent). No prior S6×S9 test located. |
| P02-2 | mixed | Direct for feasibility (recital/party component tagging exists at scale); direct method-novelty challenge; no direct fork evidence. |
| P08-6 | mixed | Direct for note-genre identifiability (France, India); direct counterevidence (instruction function); indirect taxonomy prior art; no direct slot-profile evidence. |
| P02-1 | challenge-located | Direct: mature LLM-coder prior art + direct evidence (low LLM–human α) against the machine-κ-bounds-human-κ assumption. |
| P06-1 | challenge-located | Direct: Monte Carlo QBA/MCSA is established practice; reliability measurement standard; no direct evidence for atlas-specific propagation. |
| P07-5 | challenge-located | Direct: evidence-quality-restricted reanalysis is standard (Cochrane/JECH/BMC); underpowering risk corroborated; no direct evidence on this corpus's claims. |

**Global limit:** 18 snippet-level queries in mostly English (plus French for P08-6), single day (2026-10-15), no full-text verification, no paywalled content accessed. **Nothing here establishes novelty for any idea; non-findings are not evidence of absence.**
