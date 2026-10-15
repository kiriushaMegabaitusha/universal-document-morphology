# Evidence check E03 — bounded post-ideation literature search

Session: udm-ideation-01 · Checker: E03 · Search date for ALL queries below: **2026-10-15**
Scope: 6 assigned ideas (P06-5, P03-1, P08-2, P04-3, P05-2, P07-1), 1–3 web_search queries each (3 run each).
Evidence rules: snippets relied on unless page content was returned in full by the search result; only titles/URLs actually seen in results are listed; no paywalled content was guessed; nothing cited that did not appear in a real result.
**Global limit: this is a bounded search (18 queries total). Absence of a hit does NOT establish novelty — it only means this search did not find it.**

---

## P06-5 — Ceiling-constrained power + item calibration on an expanded machine panel

**Search questions.** (a) Does prior work derive power/attainable-effect surfaces that depend on baseline accuracy (ceiling-constrained SESOI)? (b) Has item calibration (difficulty/discrimination) already been done on panels of LLMs instead of human respondents, and does machine difficulty predict human difficulty?

**Queries run + date (2026-10-15).**
1. `ceiling effect baseline accuracy maximum possible effect size equivalence test TOST power`
2. `LLM item calibration difficulty discrimination predict human test performance IRT`
3. `smallest effect size of interest baseline-dependent power analysis comprehension accuracy`

**Sources seen (titles + URLs).**
- Power for Equivalence (TOST) — https://cttir.github.io/tutorials/tutorials/sample-size/power-equivalence-tost.html
- PowerTOST: Power and Sample Size for (Bio)Equivalence Studies — https://cran.r-project.org/web/packages/PowerTOST/PowerTOST.pdf
- Simulation-Based Power Analyses for the Smallest Effect Size of Interest — https://journals.sagepub.com/doi/10.1177/25152459241240722
- Chapter 5: Power in TOST | Bioequivalence for Biosimilar — https://gccllab.github.io/TOST/chapter-5-power-in-tost.html
- Can LLMs Estimate Student Struggles? Human-AI Difficulty Alignment with Proficiency Simulation for Item Difficulty Prediction — https://aclanthology.org/2026.findings-acl.1270.pdf
- Synthetic Student Responses: LLM-Extracted Features for IRT Difficulty Parameter Estimation — https://arxiv.org/html/2602.00034v1
- Consensus without Accuracy: Investigating LLM's Ability to Recover Item Difficulty Using Paired Comparisons — https://aclanthology.org/2026.aimecon-wip.4.pdf
- SMART: Simulated Students Aligned with Item Response Theory for Question Difficulty Prediction — https://aclanthology.org/2025.emnlp-main.1274.pdf
- LLMs Struggle to Measure What Distinguishes Students of Different Proficiency Levels: A Study of Item Discrimination in Reading Comprehension Assessment — https://arxiv.org/html/2606.18709

**Evidence for (directly relevant).** None located for the ceiling-constrained attainable-effect derivation itself — queries 1 and 3 returned only generic TOST/SESOI power methodology (margins, variance, sample size), nothing conditioning power on baseline accuracy or deriving a maximum attainable effect 1−b. Feasibility of cheap machine-panel calibration is indirectly supported: prior studies run IRT/CTT calibration on 20–42 LLMs treating the model pool as synthetic respondents (ACL 2026 findings; arXiv 2606.18709; AIMEcon WIP), i.e., large model panels are an established, inexpensive instrument.

**Evidence against / novelty challenge.** Direct and substantial for the calibration half of the idea: machine/LLM item calibration against human-calibrated IRT difficulty is an active, published literature (sources above). It also attacks the load-bearing assumption: (i) ACL 2026 findings paper — IRT difficulty derived from models' correctness correlates *worse* with humans than models' explicit perceptions, "Curse of Knowledge", 75.6% item saturation, model consensus diverges from human reality; (ii) arXiv 2606.18709 — LLM-derived item discrimination aligns weakly (best Spearman 0.152 direct; 0.241 response-based); (iii) AIMEcon WIP — pooled LLM pairwise rankings ρ = 0.400 with respondent-calibrated 1PL difficulty, explicitly "not a substitute for respondent-based calibration". So the idea's premise (machine difficulty ordering transfers to item selection for humans) is empirically contested in prior work.

**Status:** challenge-located.
**Direct/indirect split:** direct challenge on machine-panel calibration (novelty + premise); indirect analogy only for power methodology (TOST/SESOI general, ceiling-constrained version not found); no direct evidence located for the attainable-effect (1−b) derivation.
**Limits.** 3 queries, English only, snippet-level; no repo-internal check here (novelty claim inside the project not verified by this search); machine-calibration papers are educational-item domains, not document-comprehension tests; no hit ≠ no prior work.

---

## P03-1 — Pre-registered processing-cost (RT) outcome beside accuracy in the comprehension test

**Search questions.** (a) Is RT already used as a registered/co-outcome beside accuracy in reading-comprehension testing (precedent)? (b) Is there prior experimental work on processing time/reading time for plain vs formal legal text? (c) Do register/formality manipulations produce reading-time effects (premise: cost shows before error)?

**Queries run + date (2026-10-15).**
1. `response time outcome alongside accuracy reading comprehension ceiling effect plain language study`
2. `plain language legal documents reading time processing cost experiment`
3. `register formality text comprehension reaction time speed accuracy dissociation`

**Sources seen (titles + URLs).**
- Improving the Predictive Validity of Reading Comprehension … (response times as ancillary information) — https://files.eric.ed.gov/fulltext/ED614299.pdf (same work: https://www.tandfonline.com/doi/full/10.1080/08957347.2019.1577247)
- Accuracy and response-time effects of structured input on the … — https://journals.sagepub.com/doi/10.1177/13621688251329670
- Using Response Time and Accuracy Data to Inform the Measurement of Fluency — https://www.researchgate.net/publication/301265259_Using_Response_Time_and_Accuracy_Data_to_Inform_the_Measurement_of_Fluency
- Using Response Times and Response Accuracy to … (Springer) — https://link.springer.com/article/10.1007/s11336-020-09717-2
- The Role of Plain Language in Legal Documents — https://www.researchgate.net/publication/388919042_The_Role_of_Plain_Language_in_Legal_Documents
- Plain Language in the Written Law (Georgetown) — https://www.law.georgetown.edu/legal-ethics-journal/wp-content/uploads/sites/24/2024/03/GT-GJLE230044.pdf
- Eye-tracking context formality effects in German and Japanese sentence processing (Sci Rep) — https://www.nature.com/articles/s41598-025-23609-4
- The interplay of situation-formality register congruence and verb-argument relations (SFB 1412) — https://vivo.sfb1412.hu-berlin.de/display/n33
- Register and standard language knowledge in interaction (REALIS) — https://realis.linguistik.hu-berlin.de/index.php/REALIS/article/download/25/3/6
- (How) Do Register and Morphosyntactic Congruence Effects Interact during Sentence Reading? Two Eye-Tracking Pilot Studies — https://escholarship.org/uc/item/05q9v8cv
- Impact of Respectfulness on Semantic Integration During Discourse Processing — https://pmc.ncbi.nlm.nih.gov/articles/PMC12024179/

**Evidence for (directly relevant).** RT alongside accuracy in comprehension testing is established practice: ERIC ED614299 / J. Educational Measurement article uses response times as ancillary information to improve parameter estimation in reading-comprehension tests ("a fast, correct response is an indicator of effective automatic processing"); fluency-measurement papers jointly model RT + accuracy (Springer, ResearchGate hits). Indirect support for the premise: multiple sentence-processing studies find formality/register manipulations produce measurable reading-time/eye-tracking effects (Nature Sci Rep; SFB 1412; escholarship pilots).

**Evidence against / novelty challenge.** (1) Novelty: RT-as-outcome in comprehension/psychometrics is standard, not a new instrument class — the idea's distinctiveness rests on pre-registering it *for this project*, which is repo-specific and not assessable from search. (2) Premise challenge: the SFB 1412 self-paced-reading study reports **null main effect of register congruence on reading times** (accuracy differences n.s.), explicitly noting sensitivity limits — register may not move RT first. Plain-language query 2 returned only prose essays/guides (Scribd, ResearchGate, Georgetown, LinkedIn) with **no reading-time experiment** — the "plain vs formal legal text, cost measured" experiment was not located.

**Status:** mixed.
**Direct/indirect split:** direct evidence that RT is used beside accuracy in comprehension testing (precedent for feasibility, mild novelty challenge); indirect analogy from register/formality processing studies (supportive of mechanism but with a documented null); no direct evidence located for a plain-vs-formal legal-document RT experiment.
**Limits.** 3 queries; snippets only; query 2's results were poor-quality grey literature; domain (legal/official documents) may differ from the psycholinguistic register studies; absence of a legal-RT experiment in this search is not proof none exists.

---

## P08-2 — Sovereignty/stewardship as a fourth regime dimension of document law

**Search questions.** (a) Do the candidate frameworks exist as retrievable public texts (CARE, OCAP)? (b) Do their clauses regulate *use/interpretation* rather than merely access (the distinctness assumption)? (c) Challenge: is "an additional governance dimension beyond access/openness" already articulated in prior data-governance literature?

**Queries run + date (2026-10-15).**
1. `CARE Principles Indigenous data governance framework collective benefit authority control responsibility`
2. `OCAP First Nations principles ownership control access possession data governance`
3. `Indigenous data sovereignty CARE FAIR principles tension open government data access critique`

**Sources seen (titles + URLs).**
- CARE Principles for Indigenous Data Governance — Wikipedia — https://en.wikipedia.org/wiki/CARE_Principles_for_Indigenous_Data_Governance
- The CARE Principles (GIDA-global) — https://www.gida-global.org/careprinciples
- The CARE Principles for Indigenous Data Governance (Data Science Journal) — https://datascience.codata.org/articles/10.5334/dsj-2020-043
- CARE Data Maturity Model (Collaboratory for Indigenous Data Governance) — https://indigenousdatalab.org/care-data-maturity-model/
- The CARE Principles for Indigenous Data Governance (ResearchGate) — https://www.researchgate.net/publication/346665037_The_CARE_Principles_for_Indigenous_Data_Governance
- The First Nations Principles of OCAP® (FNIGC) — https://fnigc.ca/ocap-training/
- OCAP® FAQs (Alberta FNIGC) — https://afnigc.ca/wp-content/uploads/2024/06/OCAP%C2%AE-FAQs-compressed.pdf
- OCAP® — afnigc — https://afnigc.ca/ocap/
- First Nations principles of OCAP — Wikipedia — https://en.wikipedia.org/wiki/First_Nations_principles_of_OCAP
- Principles of OCAP (FNIGC brochure) — https://fnigc.ca/wp-content/uploads/2022/10/OCAP_Brochure_20220927_web.pdf
- Operationalizing the CARE and FAIR Principles for Indigenous … (Scientific Data) — https://www.nature.com/articles/s41597-021-00892-0

**Evidence for (directly relevant).** The idea's explicit feasibility assumption ("frameworks exist as retrievable public texts, unverified this round") is now **verified**: CARE (GIDA, CODATA-DSJ 2020, CARE Data Maturity Model) and OCAP® (FNIGC, Alberta FNIGC, brochure, Wikipedia) are public, versioned web texts. Direct support for the access-vs-stewardship distinction: FNIGC's own text says First Nations "own and control how this information can be stored, **interpreted**, used, or shared" and defines Possession/stewardship as physical control — use/interpretation clauses sit inside OCAP beyond the "Access" principle; the OCAP FAQ describes community privacy laws, data-sharing agreements and standards (operative conditions on use). CARE's own description (GIDA) names a **tension between data-sharing/openness and collective control** — i.e., a documented friction with state open-data regimes (matches the idea's Prediction 3 direction).

**Evidence against / novelty challenge.** Direct: the "additional dimension" framing already exists in the prior art — CARE is explicitly positioned as a people/purpose-oriented complement to FAIR (CODATA-DSJ: "Be FAIR and CARE"), and the Scientific Data paper operationalizes CARE *in the context of* FAIR/ open scientific data, i.e., stewardship-as-distinct-layer is a published construct in data governance, not an open question there. Indirect risk-flag (not a source): OCAP is trademarked/governed by FNIGC and the texts are described as living, community-interpreted — supporting the idea's own extractive-coding risk. Note also: nothing found codes these frameworks as *document-law* clauses or tests them against a trace/access/persistence scheme.

**Status:** mixed.
**Direct/indirect split:** direct evidence for feasibility (frameworks exist publicly) and for the distinctness assumption (use/interpretation clauses present); direct novelty challenge to the "new fourth dimension" framing (CARE-vs-FAIR complementarity already published); no direct evidence located on coding these as a document-law dimension or on the redundancy-vs-distinctness question.
**Limits.** 3 queries, English; snippets only; searched frameworks' existence/distinctness, not the atlas-specific coding claim; no community-authored critique literature specifically about external coding was retrieved; search does not establish that no one has made the document-law move.

---

## P04-3 — Within-standard revision diffing (DIN 5008, ДСТУ 4163, ГОСТ 6.38, GB/T 9704)

**Search questions.** (a) Are superseded editions and their dates retrievable? (b) Challenge: has anyone already diffed editions of these standards' requisite inventories? (c) Challenge: does longitudinal version-evolution analysis of standards already exist as a method?

**Queries run + date (2026-10-15).**
1. `DIN 5008 revision history changes since 1949 editions letter writing formatting rules`
2. `longitudinal analysis of changes across editions of technical standards requirements evolution study`
3. `DSTU 4163:2003 vs 4163:2020 changes GOST 6.38 requirements comparison revisions`

**Sources seen (titles + URLs).**
- DIN 5008 — Wikipedia — https://en.wikipedia.org/wiki/DIN_5008
- DIN 5008 – Wikipedia (DE) — https://de.wikipedia.org/wiki/DIN_5008
- DIN 5008 — Grokipedia — https://grokipedia.com/page/din_5008
- DIN 5008 - 2011-04 - DIN Media (editions 1949, 1951, 1963, 1975, 1986, 1996, 2001) — https://www.dinmedia.de/en/standard/din-5008/137578108
- DIN 5008: Geschichte und Regeln der Geschäftsbrief-Norm — https://awerka.de/en/blog/din-5008-geschaeftsbrief-norm/
- Review Evolution of Safety Requirements in Industrial … (arXiv) — https://arxiv.org/pdf/2602.17822
- The Evolution and Specialization of IETF Standards (IGI Global) — https://www.igi-global.com/chapter/the-evolution-and-specialization-of-ietf-standards/115269
- A longitudinal analysis of published clinical practice guidelines (Nature Comms) — https://www.nature.com/articles/s41467-026-75668-4
- Changing standards for drug approval: A longitudinal analysis … / Understanding the Evolution of Standards (ScienceDirect result bundle) — https://www.sciencedirect.com/science/article/pii/S0277953618307081
- Understanding the Evolution of Standards: Alignment and Reconfiguration in Standards Development and Implementation Arenas (ResearchGate) — https://www.researchgate.net/publication/264999771_Understanding_the_Evolution_of_Standards_Alignment_and_Reconfiguration_in_Standards_Development_and_Implementation_Arenas
- [Ukrainian teaching text] quantitative changes of requisites in ДСТУ 4163-2003 vs ГОСТ 6.38-90 (31 → 32, new registration requisite) — https://files.library.nung.edu.ua/chytalnya/4330/files/basic-html/page35.html
- [Zagorecka] Новий національний стандарт України …: історія розроблення, аналіз основних змін (ДСТУ 4163-2003 → 4163:2020, "було/стало" requisite table, 32 → 32, requisite 03 removed / 28 added) — https://nbuviap.gov.ua/images/e_biblioteka/naukovi_resursi/dokumentoznavstvo/Zagorecka%20O.%20Novij%20nacionalnij%20standart%20Ukraini.pdf
- State Standard of Ukraine DSTU 4163: 2020: Innovations and Problems (comparative analysis of requisite composition, counts) — https://unz.univer.km.ua/article/view/82_108-124
- ДСТУ 4163-2003 catalogue entry (scope; notes non-application to electronic document flow) — https://online.budstandart.com/ua/catalog/doc-page.html?id_doc=24770
- (ResearchGate version of the Zagorecka paper: https://www.researchgate.net/publication/369471194_The_New_National_Standard_of_Ukraine_for_the_Formation_of_Organizational_and_Administrative_Documentation_History_of_Development_Analysis_of_Main_Changes_and_Issues_of_Implementation_of_The_Standard)

**Evidence for (directly relevant).** Feasibility: DIN Media lists DIN 5008 editions 1949/1951/1963/1975/1986/1996/2001; German Wikipedia notes the 1996 Neufassung added PC word processing — dated editions are publicly traceable. The Ukrainian/GOST lineage is publicly diffable: an open PDF gives a "was in ДСТУ 4163-2003 / became in ДСТУ 4163:2020" requisite table with counts and specific add/delete (03 out, 28 in), and an open teaching text gives ГОСТ 6.38-90 → ДСТУ 4163-2003 counts (31 → 32, registration requisite added).

**Evidence against / novelty challenge.** Direct: edition-to-edition requisite diffing for two of the four named standards **has already been published** — Zagorecka's comparative "було/стало" analysis (via nbuviap.gov.ua and ResearchGate), the unz.univer.km.ua "Innovations and Problems" comparative analysis, and the nung.edu.ua material comparing ГОСТ 6.38-90 to ДСТУ 4163-2003 (including the exact "requisite count changed 31 → 32" move). So "diff their requisite inventories across editions" is not itself new for this lineage. Indirect: longitudinal/version-evolution studies of standards exist as a recognized method (IETF standards evolution chapter; ScienceDirect "Understanding the Evolution of Standards: … versions of a particular standard, and the displacement of one standard by another"; drug-approval longitudinal analysis; safety-requirements evolution arXiv). Not found: any multi-standard, per-decade accretion/deletion *rate* analysis over ≥3 of these standards using a closed slot vocabulary (the idea's added value) — no hit either way.

**Status:** challenge-located.
**Direct/indirect split:** direct prior requisite-diff for ДСТУ/ГОСТ (novelty challenge, operation already done); direct support for edition retrievability (DIN edition list); indirect method precedent (standards version-evolution studies); no direct evidence located on the per-decade rate/time-series framing.
**Limits.** 3 queries; snippets only; did not verify whether the prior Ukrainian papers code to anything like a closed slot vocabulary; GB/T 9704 editions and ГОСТ Р 7.0.97 revisions not separately searched; superseded-edition paywall risk (idea's stated feasibility risk) not tested by these queries.

---

## P05-2 — Within-system digitisation trajectory: do slots migrate into infrastructure?

**Search questions.** (a) Is the Ukrainian sequence (GOST/Soviet inheritance → ДСТУ 4163:2020 → electronic document flow) publicly documented with dates? (b) Challenge: is "document features/requisites move into system metadata/logs under digitisation" already an empirically described phenomenon? (c) Any prior paper–digital migration/coding studies on requisites?

**Queries run + date (2026-10-15).**
1. `Ukraine electronic document management reform transition paper documents electronic flow DSTU rules`
2. `digitization paper document features absorbed into information system metadata logs study`
3. `"electronic document" replaces paper form requisites migration standard medium change research`

**Sources seen (titles + URLs).**
- The New National Standard of Ukraine for the Formation of Organizational and Administrative Documentation: History of Development, Analysis of Main Changes … — https://www.researchgate.net/publication/369471194_The_New_National_Standard_of_Ukraine_for_the_Formation_of_Organizational_and_Administrative_Documentation_History_of_Development_Analysis_of_Main_Changes_and_Issues_of_Implementation_of_The_Standard
- DSTU 4163:2020: document formatting rules (ТОРГСОФТ) — https://torgsoft.ua/en/articles/law/4163/
- Ukraine's Electronic Document Flow: Changes and Prospects — https://intecracy.com/en/electronic-document-management/ukraines-electronic-document-flow-changes-and-prospects/
- Electronic Document Management: Reform Must Continue (Pravo-Justice) — https://www.pravojustice.eu/en/post/elektronnij-dokumentoobig-reforma-maye-prodovzhuvatisya-nezvazhayuchi-na-vijnu-en
- State Standard of Ukraine DSTU 4163: 2020: Innovations and Problems — https://unz.univer.km.ua/article/view/82_108-124
- Paper 'Work' And Electronic Files: defending professional practice (UCD repository, ethnography of paper vs electronic case files) — https://researchrepository.ucd.ie/bitstreams/ac9cae60-b5aa-4a80-86c2-aecfe4c22ece/download
- Data Model and Architecture of a Paper-Digital Document Management System (ACM) — https://dl.acm.org/doi/pdf/10.1145/1284420.1284429
- A Model for Mapping between Printed and Digital Document Instances — https://beatsigner.com/publications/a-model-for-mapping-between-printed-and-digital-document-instances.pdf
- Metadata use in document management systems, which support business processes (Öberg) — https://archivo.cartagena.es/doc/Archivos_Social_Studies/Vol2_n1/09-oberg_metadata.pdf
- Digital Traces of Information Systems: Sociomateriality made Researchable (ICIS) — https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1069&context=icis2013
- Transitional strategies migrating legacy paper archives to digital repositories — https://www.fdaguidelines.com/transitional-strategies-migrating-legacy-paper-archives-to-digital-repositories/
- Electronic Systems, Electronic Records, and Electronic Signatures … (FDA guidance) — https://www.fda.gov/regulatory-information/search-fda-guidance-documents/electronic-systems-electronic-records-and-electronic-signatures-clinical-investigations-questions
- Digital Records Conversion and Migration Guideline (City of Toronto) — https://www.toronto.ca/wp-content/uploads/2023/10/9114-Digital-Records-Conversion-and-Migration-Guideline.pdf
- Electronic document management systems implementation across industries: systematic analysis (ResearchGate) — https://www.researchgate.net/publication/384511242_Electronic_document_management_systems_implementation_across_industries_systematic_analysis

**Evidence for (directly relevant).** The Ukrainian trajectory is documented and dated in public sources: the DSTU 4163:2020 history/changes paper (2022), Pravo-Justice and Intecracy accounts of the electronic-document-flow reform, and the standard's own scope note that it does not cover electronic document flow (budstandart, from query 3 of P04-3 and here via torgsoft/Zagorecka) — a sharp, citable boundary between the paper-era standard and the electronic regime. The Zagorecka text also states ДСТУ 4163:2020 incorporated requirements of Resolution №55 on paper *and* electronic documents — i.e., a reform moment where requisites are re-described across media.

**Evidence against / novelty challenge.** Indirect but close: the *mechanism* the idea wants to demonstrate ("medium moves the slots into infrastructure") is already empirically described in adjacent literatures — Öberg compares metadata actually captured in live EDMS against recordkeeping metadata sets (which requisites survive the move into systems); the UCD ethnography documents exactly the loss of paper meta-information (order, annotations, "document of record") when case files move to a system, and that electronic entries are "stripped of their uniqueness"; ICIS paper covers digital traces as the infrastructural residue of activity; migration guidelines (FDA, Toronto, fdaguidelines) treat paper→digital conversion as regulated practice. None of these is a coded pre/post slot analysis of one document flow — no direct prior test of *this* claim located.

**Status:** mixed.
**Direct/indirect split:** direct evidence for feasibility (dated Ukrainian reform + standard-scope boundary); indirect analogy/mechanism evidence from records/IS studies (mild novelty challenge: phenomenon well described qualitatively); no direct evidence located for a 14-slot-coded before/after trajectory within one system.
**Limits.** 3 queries; snippets; Ukrainian-language sources surfaced only via English queries — a Ukrainian/Russian query set might find prior slot-level comparison; single-country search; retrieval risk for Soviet-era texts untested here; absence ≠ novelty.

---

## P07-1 — Turn persistence/appraisal from a named dimension into a coded layer (28 systems)

**Search questions.** (a) Challenge: do cross-national coded comparisons of retention/appraisal/disposal provisions already exist? (b) Is there a standards-level conceptual separation between records-life rules and document-format rules? (c) Are country-level retention compendia available as data?

**Queries run + date (2026-10-15).**
1. `comparative analysis records retention legislation across countries archives act disposal`
2. `ISO 15489 retention appraisal disposal records management requirements versus document format standards`
3. `comparative study national records management legislation retention schedules countries dataset`

**Sources seen (titles + URLs).**
- Archives and Records Management Legislation: A RAMP Study with Guidelines (UNESCO RAMP, ~120 countries) — https://policycommons.net/artifacts/10664832/legislation-et-reglementation-en-matiere-darchives-et-de-gestion-des-documents/11572194/
- A comparative study of laws and procedures … retention of medical records (USA, UK, Australia, Iran) — https://pmc.ncbi.nlm.nih.gov/articles/PMC3508852/
- Impact of archival legislation on national archives policies: a comparative study (Archives, 1994) — https://liverpooluniversitypress.co.uk/doi/10.3828/archives.1994.1
- Provisions for managing and preserving records created in networked environments (SADC, qualitative content analysis of archival legislation, 9 countries) — https://www.tandfonline.com/doi/full/10.1080/01576895.2015.1136225
- Council of Europe Access Info Group (AIG) draft thematic evaluation report (retention periods, retention-schedule validation, appraisal/disposal procedures by country incl. Ukraine, Sweden, Estonia, Latvia…) — https://rm.coe.int/council-of-europe-access-info-group-aig-draft-thematic-evaluation-repo/48802bd0e2
- ISO 15489-1:2016 Information and documentation — Records management — https://www.iso.org/standard/62542.html
- ISO 15489 Records management (TC 46/SC 11) — https://committee.iso.org/sites/tc46sc11/home/projects/published/iso-15489-records-management.html
- ISO 15489-1:2016 (ISO OBP) — https://www.iso.org/obp/ui/en/#!iso:std:62542:en
- ISO 15489: Records Mgmt Concepts (CASRAI) — https://casrai.org/guides/iso-15489-records-management-concepts-principles
- ISO 15489-1:2016 (SIS) — https://www.sis.se/en/produkter/standardization/information-sciences-publishing/information-sciences/iso1548912016/
- Data Retention Laws by Country (2026) — https://www.recordinglaw.com/world-laws/world-data-privacy-laws/data-retention-laws-by-country/
- Your Record Retention cheat sheet: a comparative look (Crown RMS) — https://www.crownrms.com/insights/your-record-retention-cheat-sheet-a-comparative-look-from-healthcare-to-government/
- Global Records Retention Toolkit (Thomson Reuters Practical Law) — https://anzlaw.thomsonreuters.com/w-025-5854
- PI's briefing on national data retention laws (Privacy International) — https://privacyinternational.org/report/5267/pis-briefing-national-data-retention-laws
- filerskeepers — your global data retention schedule — https://www.filerskeepers.co/

**Evidence for (directly relevant).** Feasibility and format: comparable cross-national coding of exactly these variables already exists as a method — the Council of Europe AIG report tabulates retention-period ranges, retention-schedule validation, appraisal and disposal procedures per country (with Ukraine's "three to seventy-five years depending on retention value" explicitly listed); UNESCO's RAMP study analyses archives/records legislation from ~120 countries; the SADC study is a qualitative content analysis of retention/preservation provisions across 9 national archives acts. So the layer is codable and has published coding schemes to borrow. Indirect support for the orthogonality premise: ISO 15489 (records creation/capture/management over time) sits in a different standards family (TC 46/SC 11) from page/format standards; CASRAI explicitly distinguishes ISO 15489 records-management/retention concepts from other documentation standards.

**Evidence against / novelty challenge.** Direct: "a variable that can be cross-tabulated across systems" for retention/appraisal/disposal is already a published comparative object (CoE AIG report; UNESCO RAMP ~120 countries; SADC content analysis; medical-record retention comparison across 4 countries; Impact-of-archival-legislation comparative study). The idea's claim to novelty therefore narrows to *joining this layer to the atlas's own slot data / testing orthogonality with page-format law* — that specific test was **not found either way**. Also flag: three of the query-3 hits (recordinglaw, Privacy International, filerskeepers) are *data/privacy* retention, not archival records retention — adjacent but not the same construct (the CoE and SADC sources are the on-topic ones).

**Status:** challenge-located.
**Direct/indirect split:** direct prior cross-national coded retention/appraisal/disposal comparisons (novelty challenge to "coded layer" itself); direct feasibility support (CoE/RAMP coding schemes demonstrably work, incl. Ukraine and Sweden); indirect conceptual support for layer-separation (ISO 15489 vs format standards); no direct evidence located for the orthogonality test (page-format standards carrying retention clauses, or not).
**Limits.** 3 queries; snippets only; sources overlap in coverage with the atlas's 28 systems only partly (CoE parties ≠ atlas systems); no search was run on whether any *page-format* standard specifies retention (the idea's falsifier P1) — that question is open after this round; absence ≠ novelty.

---

## Summary table

| Idea | Status | Direct evidence | Indirect evidence | No direct evidence located |
|---|---|---|---|---|
| P06-5 | challenge-located | LLM-panel item calibration literature (ACL/EMNLP/AIMEcon/arXiv) + evidence machine difficulty ≠ human difficulty | generic TOST/SESOI power methodology | ceiling-constrained attainable-effect (1−b) derivation |
| P03-1 | mixed | RT as co-outcome in comprehension testing (ERIC/tandfonline, fluency models) | register/formality reading-time studies (incl. one null) | plain-vs-formal legal-document RT experiment |
| P08-2 | mixed | CARE/OCAP texts verified public; use/interpretation clauses present; CARE–FAIR "extra layer" already published | GIDA note on sharing-vs-control tension | coding these as document-law clauses / distinctness test |
| P04-3 | challenge-located | published ДСТУ 4163-2003→2020 and ГОСТ 6.38→ДСТУ requisite diffs; DIN edition list | standards version-evolution studies (IETF, ScienceDirect) | multi-standard per-decade accretion-rate time series |
| P05-2 | mixed | dated Ukrainian reform sequence + standard scope boundary (paper vs electronic) | EDMS metadata/ethnography studies of features moving into systems | coded before/after slot trajectory in one flow |
| P07-1 | challenge-located | CoE AIG / UNESCO RAMP / SADC cross-national retention-appraisal-disposal comparisons | ISO 15489 vs format-standard separation (CASRAI) | orthogonality test (format standards vs archives acts) |

**Caveat repeated:** 18 queries, snippet-level, English-dominant, one date (2026-10-15). A "challenge-located" or "mixed" status here reflects what these queries surfaced; "no direct evidence located" is a statement about this bounded search only, never proof of novelty.
