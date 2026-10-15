# Adversarial review round — reviewer R03 (session udm-ideation-01)

Independent AI reviewer (disclosed: AI-generated review; originated none of the ideas).
No literature search this round — all "prior evidence" entries state what to look for
and are marked `not-checked — no search this round`. No ranking of ideas; dispositions
are per-idea process calls only. Strongest version reviewed first in every case.

Assigned ideas: P02-1, P06-2, P06-5, P04-3, P08-1, P08-5.

---

## P02-1

**Reviewer.** R03 (AI, independent).

**Strongest version of the idea.** Build a tagger whose prompt/feature set is derived
only from the slot definitions in `morphology.md` §2 (never from the hand labels), run
it gloss-blind against all 225 rows of `requisites.csv` and span-level over `sources/`,
and report per-slot and per-script Cohen's κ — substituting, at near-zero cost, for the
human second coder the repo lists as unavailable. High κ upgrades every atlas figure
from "one coder's judgement" to a measured quantity; low κ produces a ranked list of
which slot definitions cannot carry cross-system claims. Either way the project learns
something it currently cannot know, and the disagreement audit doubles as a
definition-quality review.

**Observation that would count against it.** Overall κ lands near 0.8 but is driven by
the overwhelming majority of *absent* cells (most slot × row combinations are 0), while
agreement on the *present* cells of exactly the load-bearing rare slots (S9 = 2/25,
S6 = 8/25) is poor — i.e., the second coder confirms the trivial part of the schema and
fails on the parts the headline findings rest on. A single aggregate κ would hide this.

**Alternative explanations.**
1. *Shared-definition artefact:* both coders read the same `morphology.md` §2
   definitions, so agreement measures internal consistency of the definition text, not
   correctness of the coding. Correlated errors between two readers of the same
   definition text yield high κ and low validity simultaneously.
2. *Model-coverage confound:* predicted lower κ on Arabic/Thai/Han rows may reflect
   weak cheap-model coverage of those scripts rather than genuinely fuzzier slot
   boundaries — the per-script pattern would then be a property of the model, not of
   the schema.
3. *Leakage:* residual `gloss_en`/`local_term` visibility inflates agreement; the idea
   names gloss-blindness as a condition but any accidental leakage in the row-level run
   would silently manufacture success.

**Measurement or analysis failure.** Cohen's κ is prevalence-sensitive: with skewed
binary marginals, high raw agreement can coexist with low κ (and vice versa), so κ
alone can misreport both directions. Span-level tagging of `sources/` has no gold
standard at all, making its "census differs from standards census" prediction
unfalsifiable as stated. The few-shot prompt, feature set and threshold are researcher
degrees of freedom that must be frozen before disagreements are seen. κ measures
agreement, not validity — the idea says this, but the headline use of the number
("second coder") quietly assumes validity.

**Sampling or generalizability failure.** 225 rows drawn from 28 purposively chosen
systems; per-script subsamples across ~5 script families are tiny, so per-script κ
intervals will be wide and any "Latin/Cyrillic high, Arabic/Thai/Han low" claim may be
one or two systems' worth of rows. Errors clustered by tradition are a prediction of
the idea itself, which breaks the independence assumptions behind a pooled κ. Nothing
here bounds human–human agreement unless the untested bridge assumption is granted.

**Prior evidence that challenges it.** Look for: (a) studies comparing LLM-vs-human
annotation agreement against human–human agreement in multilingual/low-resource schema
coding — does the machine proxy systematically over- or under-estimate human κ?
(b) the prevalence/bias literature on Cohen's κ and alternatives (Gwet's AC1, PABAK,
per-slot sensitivity); (c) whether comparative typology/archival studies accept an
automated second coder at all, or require a human. — *not-checked — no search this round*.

**Potential harm, inequity, or misuse.** A reported machine κ could be read as
"validated by a second coder", laundering the repo's single-coder caveat and hardening
figures that were never independently checked — an over-trust failure directed at
future readers of the atlas. Conversely an unfairly depressed κ (model weakness on
non-Latin scripts) could discredit correct coding and, by framing non-Latin systems as
"unreliable", reproduce a script-latitude inequity already latent in the corpus.
No human-participant harm.

**Mitigation.** Freeze and pre-register the tagger's prompt/feature set before any
label is shown; report κ *plus* raw agreement, Gwet's AC1, and per-slot
sensitivity/recall on present cells; run gloss-blind as a declared condition with a
gloss-visible arm for contrast; researcher-audit every disagreement (bounded) and
report the audited correction rate; state the machine→human bridge explicitly as an
untested assumption in any claim that cites the number as a "second coder".

**Residual uncertainty.** Whether machine–human agreement bounds human–human agreement
at all — two systems trained/derived from overlapping web text may share errors in ways
that make the proxy optimistic, and nothing internal to this design can detect that.

**Disposition:** revise — keep the idea, but add prevalence-robust agreement statistics
and present-cell sensitivity alongside κ, and mark the machine→human bridge as
untested before any figure cites it as a second coder.

---

## P06-2

**Reviewer.** R03 (AI, independent).

**Strongest version of the idea.** Turn the "perfect" census rules into stated
inference: enumerate exactly all C(25,2) = 300 placements of the S9 vector against the
fixed partner slots, compute per-edge hypergeometric p-values with FDR control across
the six negation edges plus the two 1.00 implication rules, add a tradition-blocked
null, and derive per-edge power curves. The worked example (the single most-quoted
edge, S9 ⊥ S6, is p ≈ 0.45 alone) shows why this matters: the current prose treats six
co-occurrence absences as six pieces of evidence when they are one joint pattern. The
result cleanly separates "structural law" from "sparse-sample absence", is fully
pre-registerable, runs on frozen data in minutes, and every outcome — including the
null — regrades the evidence honestly.

**Observation that would count against it.** The joint test rejects only because the
six partner slots jointly cover most of the 25 systems — so the "surprise" is a
statement about marginal densities rather than about any structural relation. If a null
built from the marginals alone (nothing more than "slots are common") reproduces the
joint pattern, the fork gains no evidential upgrade and the joint test's rejection is
an artefact of how the comparison was framed.

**Alternative explanations.**
1. *Coding/denominator artefact:* the complementary distribution may follow from how
   the two genres were defined operationally (a genre identified partly by which slots
   it lacks), so the pattern is baked into the coding scheme rather than observed in
   document practice.
2. *Null choice drives the verdict:* independent-placement vs tradition-blocked nulls
   can rank the same edges differently (the idea admits the blocked null may reverse
   conclusions); if so, the finding is a function of an analyst choice, not data.
3. *Selection on the sample:* the 25 systems were chosen partly for retrievability of
   codified standards — a selection correlated with having clean, pre-sorted genres —
   so the pattern may be a property of the sampling mechanism.

**Measurement or analysis failure.** Printed marginals in `findings.md` must reconcile
exactly with system rows in `requisites.csv`; any silent mismatch changes every
p-value (the idea flags this — it must be an automated precondition, not a note). With
300 placements the minimum attainable p ≈ 0.003, so several claims are structurally
unresolvable at this n. The six negation edges are not independent tests — FDR across
highly correlated edges is conservative but does not fix the underlying dependence.
Coding error is treated as fixed; interacts with P06-1 (a single recoded row can create
or destroy a "perfect" pattern).

**Sampling or generalizability failure.** n = 25 is purposive and tradition-clustered;
"population inference" needs a defined population of written official-document regimes
and exchangeability of systems within it — asserted, not established. Power curves
inherit the same frame: a curve saying "this edge needs 60 more systems" is meaningless
unless the population those systems are drawn from is specified. Effective n under
tradition blocking may be closer to ~7–8 tradition families than 25.

**Prior evidence that challenges it.** Look for: (a) whether perfect
co-occurrence/negation patterns of this marginal size are typical in small-n typological
feature databases (are such patterns usually sampling noise?); (b) permutation-test
practice for clustered, non-random samples — is a block-permuted null on a purposive
sample licensed as population inference anywhere?; (c) any prior statistical re-analysis
of document-requirement matrices or formulary studies. — *not-checked — no search this
round*.

**Potential harm, inequity, or misuse.** A quotable "the project's clearest finding was
never statistically significant" line could be lifted out of context to dismiss the
atlas (reputational harm, misuse by critics), while the idea's own framing — the joint
pattern survives — could equally be oversold as "the fork is proven". Either
headline-style reading distorts a result whose entire value is conditional on a stated
null and frame.

**Mitigation.** Pre-specify the null family (independent and tradition-blocked), the
edge set for FDR, and the primary statistic before any computation; run from the raw
matrix with an automated printed-marginal cross-check; report effect sizes (observed vs
expected co-occurrence) beside p-values; scope all inferential language to an explicit
sampling frame; deliver jointly with P06-1's coding-error sensitivity so rows and edges
are perturbed together.

**Residual uncertainty.** Which null is scientifically right for a purposive,
tradition-clustered corpus is a substantive judgement statistics cannot settle — the
pre-registration fixes the choice but does not make it true.

**Disposition:** retain.

---

## P06-5

**Reviewer.** R03 (AI, independent).

**Strongest version of the idea.** Before any human is seen, quantify the arithmetic
ceiling on the registered 10 pp SESOI (at baseline b the largest possible plain
advantage is 1−b), re-derive the power/verdict surface over baselines 0.70–0.95 instead
of `simulate_data.py`'s single fixed base, and calibrate all 18 items' difficulty and
discrimination on an expanded, family-clustered machine panel for a few dollars. If a
human baseline ≥0.90 makes the "supported" branch of the decision rule unreachable —
converting a real small advantage into a guaranteed "falsified" verdict — this idea is
the only thing standing between the project and a designed-in null, and it acts while
everything is still pre-data, absorbable as a documented pre-data revision.

**Observation that would count against it.** The power-surface half is closed-form
arithmetic given the decision rule — it will essentially certainly show verdict
instability above some baseline, so much of the deliverable is foreordained, while the
half that carries real information (item calibration) rests on a machine→human
invariance assumption the repo itself rejects when convenient (arm M measures machine
legibility, never human comprehension). The idea may therefore be a certain-to-confirm
calculation bolted to an unvalidatable proxy.

**Alternative explanations.**
1. *Ceiling may not apply to humans:* humans may find formal renderings genuinely
   harder, keeping human baselines well below machine baselines; if so, the whole
   retargeting is unnecessary and item selection driven by machine difficulty could
   discard items that discriminate perfectly well for humans.
2. *Model-family correlation, not item difficulty:* apparent item difficulty ordering
   may track correlated training data across model families; the predicted "ordering
   replication" on an expanded panel would then replicate family bias, not item
   properties — expansion adds models, not independent information.

**Measurement or analysis failure.** 18 items is a very small calibration sample for
Rasch/2PL-style estimation (wide item SEs); discrimination at ceiling is degenerate
(variance ≈ 0, estimates unstable); effective n after family clustering may be far
below 20, and the idea admits this. Re-derived power inherits `simulate_data.py`'s
structural assumptions (item independence, effect layout) rather than validating them —
a fragile power surface can be precisely wrong. The verdict-stability analysis is
conditioned on the SESOI and TOST rule staying as registered; any later revision
invalidates it again.

**Sampling or generalizability failure.** 60–100 released models are a convenience
sample of vendor releases at one point in time, not a sample from any defined
population — difficulty ordering generalizes to humans only through the untested bridge,
and to future models not at all. Effective-n collapse through family correlation means
the "panel" may be ~10–20 independent points. Any inference from machine panel to the
human recruitment population (N ≈ 24–36) is exactly the leap the repo's own limitations
section warns about.

**Prior evidence that challenges it.** Look for: (a) IRT parameter invariance
(DIF/anchoring) studies across machine vs human respondents — does item ordering
transfer at all?; (b) published work predicting human item difficulty from LLM-panel
performance; (c) attainable-effect/ceiling-robust power methods for bounded accuracy
outcomes and whether preregistered TOST rules under ceiling are known to inflate
"falsified" verdicts. — *not-checked — no search this round*.

**Potential harm, inequity, or misuse.** The human recruitment window is the project's
scarcest and least replaceable resource (one researcher, limited pool); a
mis-calibrated item set would spend that window on an instrument tuned to machine
readers — an opportunity-cost harm to the work itself. Over-trusting the calibration
could also produce an instrument blind to the very register effect it exists to detect,
and a "power recalibrated" note could later be cited as validation of the human results
without the invariance ever being tested. No direct participant harm beyond noisier
data.

**Mitigation.** Keep a mixed item set rather than purging all ceiling items (preserve
continuity with the registered instrument); make the idea's own hold-out check a hard
gate — calibration must predict a held-out machine subpanel before it influences any
selection; pre-register the baseline range used for the power surface and report
verdict-stability as the deliverable (not "corrected power"); state the machine→human
bridge as the load-bearing assumption in the preregistration revision; if any human
pilot is later used to validate the proxy, ethics review required first.

**Residual uncertainty.** The machine→human difficulty bridge is untestable before
recruitment and unfixable after it — if it fails, item selection will have been steered
in the wrong direction and the failure will only be visible in the human data itself.

**Disposition:** retain.

---

## P04-3

**Reviewer.** R03 (AI, independent).

**Strongest version of the idea.** The repo's diachrony is one approximate anchor year
per system in coarse era bins, which cannot separate "modern documents carry
identifiers" from "modern standard revisions add identifiers". Treating layer-1
standards as versioned artefacts (DIN 5008 post-1949 revisions, ДСТУ 4163:2003→2020,
ГОСТ 6.38-90 → ГОСТ Р 7.0.97-2016, GB/T 9704 editions) and diffing their requisite
inventories across editions gives a true longitudinal series with each standard as its
own control — pre-stated predictions (net S2/S14 accretion, S12 never deleted, the
four-addressee rule fossilised across ДСТУ editions, ~2 slot deltas per decade) and
sharp falsifiers (bidirectional churn; accretion fully explained by document-type
coverage change). It is the only shortlisted idea that measures change *decisions*
rather than states.

**Observation that would count against it.** A low/no-change series would be
indistinguishable from a retrieval artefact: the editions that survive online are
recent, digitised and open, so "standards are path-dependent" could simply be "old
editions are invisible" — and the systems with retrievable back-catalogues are exactly
the open-government regimes already overrepresented in the corpus.

**Alternative explanations.**
1. *Document-type coverage change:* new editions often extend scope to new document
   types; apparent slot accretion may be a scope change, not a change to existing
   requirements (named by the idea but not demonstrably separable in practice).
2. *Editorial churn vs regulatory change:* requisites renumbered, reordered or
   re-worded across editions register as deltas in a diff without any substantive
   change — inflating the per-decade rate the idea predicts to be low.
3. *Digitisation-era confound:* standards are revised partly when governments digitise
   paperwork, so accretion may co-occur with e-government pushes rather than accumulate
   smoothly; the "path dependence" reading would then misattribute a policy regime to
   gradualism.

**Measurement or analysis failure.** Mapping each edition's requisites onto the closed
14-slot vocabulary is manual, single-coder, and crosses languages/terminology shifts
(DIN German → ДСТУ Ukrainian → GB/T Chinese glosses), so inter-edition coding
consistency is itself unmeasured. "Slot delta per decade" needs a pre-declared rule for
editorial-only changes or the rate is a coding artefact. Counts are tiny (order 2 per
decade per standard), so rates are Poisson-noisy and any rank ordering of standards will
be dominated by single events. Disconfirmation by "coverage change explains it"
requires classifying every diffed requisite as within-scope or new-scope — a second
manual coding layer.

**Sampling or generalizability failure.** The design's own floor — ≥3 systems with ≥3
retrievable editions each — may not be met: superseded editions are frequently
paywalled, withdrawn or mirrored unreliably (the repo's RU blocked-source and
byte-identical-mirror precedents). Even if met, the four candidate standards are
European/post-Soviet/East-Asian codified traditions — no non-European, non-codified or
pre-state trajectory enters, so the series generalises only to ISO-lineage formatting
standards. Selection on retrievable editions biases toward open regimes again.

**Prior evidence that challenges it.** Look for: (a) standards-body archival and
purchase policies — which superseded editions of DIN 5008, ДСТУ 4163, ГОСТ 6.38/Р
7.0.97 and GB/T 9704 are actually obtainable in full text, and under what licence;
(b) existing revision-history or standard-accretion studies in metrology/standards
scholarship (is "low accretion" already documented?); (c) prior documentation of
post-Soviet standard transitions (ГОСТ → ДСТУ) that already narrates the diff.
— *not-checked — no search this round*.

**Potential harm, inequity, or misuse.** Paywalled superseded editions create a
practical pressure to use unlicensed copies — a legal/licensing exposure for a
single researcher with no institutional library assumed. Publishing a "time series"
from 3–4 sparse points could mislead policy readers into thinking standards bodies are
slow by nature when the observation window is a retrieval window. No participant harm.

**Mitigation.** Run a bounded, licence-clean retrieval probe first (system × edition
availability matrix, published before any coding) and pre-register a minimum viable
design (e.g., ≥3 systems × ≥3 editions) below which the idea is reported as not
feasible rather than answered; pre-declare the substantive-vs-editorial change rule and
the new-scope classification; code each edition twice with a delayed re-code;
scope claims explicitly to retrievable editions with the availability bias stated.

**Residual uncertainty.** Whether ≥3 systems with ≥3 accessible full-text editions
exist at all — the whole design rests on a retrieval assumption this session cannot
check without the literature/web round that is explicitly out of scope now; no
statistical fix can rescue a series that is anecdotal by availability.

**Disposition:** pause — contingent on a bounded, licence-clean retrieval probe
confirming at least three standards with three or more accessible editions each; if the
probe fails, log as deferred rather than running an anecdotal series.

---

## P08-1

**Reviewer.** R03 (AI, independent).

**Strongest version of the idea.** The atlas declares the khipu and wampum out of
domain *by definition* (n/a slot profiles) while `morphology.md` §1 defines the document
functionally — a definition that is medium-neutral. Recoding both boundary systems, plus
one further non-documentary record system chosen for source availability, against a
second abstract grammar (provenance, custody, temporal reference, content encoding,
authentication/validation, transmission-of-authority) converts "scoped by assertion"
into "scoped by test": ≥4 of 6 slots filling means universality extends past writing;
≤1 filling means the boundary was an analyst's choice; and applying the abstract grammar
back to the 25 written systems tests whether any core sits above the medium. Both
outcomes revise the scope of the central claim, and prediction 3 keeps the atlas's
scoped claim intact even under success — the highest-stakes scope test in the pool,
desk-based, with no recruitment.

**Observation that would count against it.** The disconfirmation thresholds are set by
the analyst's own slot definitions: a generous reading of "authentication/validation"
makes it fill for almost any record system, a strict reading makes it fail — so with
one coder and no inter-rater check, the ≥4/6 result measures the analyst's generosity
rather than a property of cords and belts. The test can be made to pass or fail at the
definitional stage, before any evidence is examined.

**Alternative explanations.**
1. *Source-depth confound:* both boundary systems rest on encyclopedia-grade sources
   with 3 rows each in `requisites.csv`; apparent missing slots may be missing
   ethnography, not missing functions — a "≤1 slot fills" verdict could be an evidence
   failure wearing the costume of a structural finding.
2. *Construct baked in:* the six abstract slots were distilled from the written
   grammar's own functions, so partial overlap is guaranteed by construction;
   prediction 3 ("overlap but not the same grammar") is unfalsifiable as worded because
   any degree of overlap is compatible with it.
3. *Intermediary bias:* what is documented about khipu administration and wampum
   diplomacy reaches the analyst through colonial-era, ethnographic and museum
   intermediaries with their own framing — slot presence coded from those texts may
   reflect the observers' categories.

**Measurement or analysis failure.** Presence/absence coding from prose by a single
researcher with no κ possible solo (the repo's declared caveat, inherited); the "fill"
threshold (≥4 of 6) is arbitrary and post-hoc-able; the third system is selected on
source availability, inviting selection-on-the-outcome for a universal claim;
"authentication migrates to recitation" (prediction 2) has no operational marker in the
data — it is interpretive, and the idea supplies no coding rule separating performance
from encoding; applying the abstract grammar to 25 written systems adds a second coding
layer whose consistency with the first is unmeasured.

**Sampling or generalizability failure.** Two boundary systems plus one convenience
third system cannot support any frequency claim about authoritative records generally;
both named cases are American (Andean, Haudenosaunee), so a "medium-neutral grammar"
validated there says nothing about African, Pacific, South Asian or Mesopotamian
non-documentary record traditions — the claim "grammar of records, not writing" would
rest on n ≈ 3 cases from two regions. Grounding is encyclopedia-tier throughout, and
each boundary system contributes only a handful of coded rows.

**Prior evidence that challenges it.** Look for: (a) the ethnographic/archaeological
khipu literature (Quipu studies, Ascher, Urton and successors) — what administrative
functions are independently documented, and do they map onto the six abstract slots
without forcing?; (b) Haudenosaunee wampum scholarship on diplomacy and record status
(including Indigenous-authored accounts); (c) archival-theory treatments of
"record-ness" outside writing — does any existing typology already settle or contradict
the abstract grammar?; (d) Indigenous data-sovereignty positions on secondary analysis
of cultural heritage. — *not-checked — no search this round*.

**Potential harm, inequity, or misuse.** The wampum is a governed cultural and political
artifact of living nations and khipu heritage carries living Andean knowledge claims;
publishing slot profiles of both, authored entirely without community input or
subject-matter review, is extractive in exactly the way P08-2's own text warns about —
and would sit awkwardly beside the same register's endorsement of OCAP/CARE-style
stewardship. Misuse risk: essentialist readings ("these records lack authentication")
lifted from a thin secondary-source coding and applied to the cultures concerned.
Inequity: interpretive authority stays entirely with the metropolitan analyst.

**Mitigation.** Pre-register the abstract-slot definitions and the fill threshold before
opening the boundary case files; upgrade sourcing beyond encyclopedia tier (published
ethnography/archaeology) and code `not found` separately from `absent`; frame all
output as provisional pending community/subject-matter review; offer the coding to
Andean- and Haudenosaunee-affiliated scholars for comment before any claim is led with
it; treat the ≥4/6 and ≤1/6 thresholds as pre-registered and forbid post-hoc
redefinition of "fill".

**Residual uncertainty.** Whether an abstract grammar can be judged at all from
secondary sources without the communities whose records they are — and whether the test
is falsifiable given that slot leniency is analyst-controlled; both are irreducible
inside a desk-only, single-coder design and cannot be cleared by this session.

**Disposition:** external review — community-affiliated/subject-matter review of the
abstract-grammar mapping and its sourcing is required before any boundary coding is
treated as evidence (ethics_status: review-required; this session cannot clear it).

---

## P08-5

**Reviewer.** R03 (AI, independent).

**Strongest version of the idea.** The README concedes heterogeneous grounding and two
structurally blocked sources, and `diversity.md` §9 lists whole missing regions — so
inclusion was partly decided by what could be fetched, and the open web's geography is
not neutral. Build an external universe (states maintaining a documentation/records
standard), freeze a retrievability proxy (open-web fetch success, JS-only/blocked
status, publication language), and test whether inclusion decisions and grounding tiers
track retrievability controlling for region and legal family. Either outcome publishes:
a retrievability effect documents an availability bias and *strengthens* the honesty of
the scoped claim; no effect empirically earns the coverage defence. It audits the very
sample on which every universality statement rests.

**Observation that would count against it.** "No association once region and legal
family are controlled" is offered as disconfirmation (design-driven coverage) — but
retrievability operates *through* region (open publication correlates with governance
and income, which correlate with region), so controlling for region can absorb the
effect by construction. The declared falsifier would then fire under a real bias still
present, and the "earned defence" verdict would be a modelling artefact.

**Alternative explanations.**
1. *Baseline constructed by the same filter:* the external universe of "states with a
   documentation standard" is itself assembled from open-web sources — the comparison
   group inherits the retrievability filter, attenuating any detected association
   toward zero by design.
2. *Temporal confound:* retrievability observed today ≠ retrievability when inclusion
   decisions were made; many administrations went online in the 2010s–2020s, so
   present-day fetch success can misclassify inclusion-time availability in either
   direction, and the test measures the web's current state, not the selection event.
3. *Post-hoc proxy tuning:* retrievability is coded after inclusion is known; even
   unconsciously, proxy variants (fetch success vs language vs JS-only) can be iterated
   toward or away from significance unless frozen in advance.

**Measurement or analysis failure.** "Retrievability" is a composite that must be
operationally frozen (endpoint, timeout, mirror rules, language credit) or it is a
researcher degree of freedom. With n = 28 inclusion decisions, logistic-style tests
have very low power — non-significance is the default and is explicitly framed here as
the *reassuring* result, which is a favourable-interpretation trap. Grounding tier is an
ordinal hand-coded judgement from `evidence_base.csv` plus prose notes; measurement
error in the outcome attenuates the association toward the "no bias" conclusion.

**Sampling or generalizability failure.** The external frame is contestable (UN
members vs states-with-standards vs ISO members) and the fallback (UN member states)
dilutes the construct — states with no documentation standard enter as "excluded, not
retrievable-or-absent", conflating three different states of the world. Small states
and non-English/non-web-publishing regimes will be systematically harder to classify,
exactly the population the index is meant to detect. Any per-region odds estimate from
28 binary decisions is unstable.

**Prior evidence that challenges it.** Look for: (a) literature on open-web/digital
availability bias in cross-national data collection (how others defined retrievability
proxies and sampling frames); (b) existing registries of national standards bodies
(ISO member bodies, UN/records-management listings) usable as retrieval-independent
universe lists; (c) evidence on national standards bodies' online publication practices
by region — is the open-web geography claim already documented?; (d) whether the atlas's
own inclusion chronology (which case was added when, and why) can reconstruct
inclusion-time retrievability. — *not-checked — no search this round*.

**Potential harm, inequity, or misuse.** A published "coverage is availability-driven"
verdict could be weaponised to dismiss the entire atlas as web-scraping artefact even
if the measured bias is small — asymmetric reputational harm. Conversely, burying a real
bias behind an underpowered null hides the continued absence of Central Asian, Pacific
and small-state traditions behind a principled-sounding frame, which harms exactly the
regions the index claims to surface. No participant harm.

**Mitigation.** Build the external universe from a retrieval-independent frame (e.g.,
UN member list or ISO/records-management body membership) and freeze it *before* any
inclusion data are examined; pre-register the retrievability proxy and one sensitivity
variant, and pre-register the primary model (region-control on/off) with effect sizes
and wide CIs reported rather than significance; reconstruct inclusion-time
retrievability from case-file dates where possible and label today's measure a lower
bound; publish the frame choice as a declared assumption, varied across ≥2 frames as
the idea already proposes.

**Residual uncertainty.** With ~28 inclusion decisions the study may be structurally
unable to distinguish availability-driven from design-driven coverage — the honest
result may be "underpowered in both directions", and the index then documents a
limitation of the method rather than a property of the atlas; neither outcome can be
known before the universe list exists.

**Disposition:** revise — rebuild the external universe from a retrieval-independent
frame, freeze the proxy and primary model pre-data, and demote the region-controlled
null from "disconfirmation" to a sensitivity analysis so the declared falsifier cannot
fire under a bias operating through region.
