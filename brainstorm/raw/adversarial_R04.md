# Adversarial review — reviewer R04 (session udm-ideation-01)

Reviewer: R04, independent AI reviewer, disclosed. I originated none of the ideas
reviewed here. No literature search was performed this round; every
prior-evidence item below is a *what to look for* statement labelled
`not-checked — no search this round`. I did not rank ideas or pick a winner.
Order: P06-1, P07-5, P05-2, P08-3, P08-2.

---

## P06-1

**Idea ID.** P06-1 — Measure coding reliability once, then propagate the measured
error into every headline figure.

**Reviewer.** R04 (independent AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** Freeze a codebook, run an LLM second coder at
temperature 0 blind to `requisites.csv` (plus researcher adjudication of every
disagreement), re-code all four hand-coded layers (slots, keyword themes, era
anchors, regime classes), report κ/exact agreement per layer and per slot family,
then propagate the *measured* error rates through a `recompute.py`-style
resimulation so every headline figure (17/25, the fork, the diachronic shares)
carries an interval instead of a point value — with pre-stated predictions that
stem slots agree best, themes/era anchors worst, and at least one
`EXECUTIVE_SUMMARY.md` figure moves outside the current tolerance. Either outcome
is informative: survival upgrades the caveat, movement bounds the claim.

**Observation that would count against it.** Agreement is high on all four layers
*and* no headline figure moves under simulated error at the measured κ — the
deliverable collapses into a documented "coding error threatens no finding" note
plus the two-coder thematic pass the repo already lists under "What remains", so
no new analysis program is opened.

**Alternative explanations (three).**
1. High κ may reflect shared bias rather than validity: a codebook written by the
   same researcher, an LLM trained on similar descriptive conventions, and the
   original coding can all agree while being wrong together. Agreement ≠ correctness.
2. Instability in the diachronic bins may be driven by bin size (n = 6–10) rather
   than by coding error — the propagation would attribute small-n sampling
   instability to the instrument.
3. An `EXECUTIVE_SUMMARY.md` figure leaving "tolerance" may be an artefact of
   `recompute.py`'s tolerance being calibrated for arithmetic/figure drift, not
   for measurement error — a threshold-mismatch, not a finding.

**Measurement or analysis failure.** κ is inflated/deflated under the severe
marginal imbalance of sparse slots (the κ prevalence paradox), so κ alone
misstates reliability — raw agreement and a prevalence-robust statistic are
needed. Row-level perturbation assumes errors independent conditional on slot,
but coding errors plausibly cluster by tradition and script, which would make
propagated intervals too narrow. Era anchors and regime classes are analyst
judgments, not row-level items: κ may be undefined or meaningless for two of the
four layers, forcing a different statistic mid-analysis. A single pooled error
rate also discards the slot-specific rates the design itself predicts.

**Sampling or generalizability failure.** One model family at one temperature is
one coder, not a sample of coders; machine–human agreement bounds human–human κ
only under an explicitly untested assumption. The single researcher adjudicating
every disagreement re-introduces the sole-coder bottleneck at exactly the step
where disagreements are resolved. Re-coding from case files alone restricts both
coders to the same prose, so thin-grounding systems (PE, HN, ET, WA) will tend to
agree for lack of evidence to disagree about — inflating κ where it matters most.

**Prior evidence that challenges it.** Look for: published LLM-vs-human versus
human-vs-human agreement comparisons on structured content coding (does the
machine proxy inflate or deflate κ?); the κ prevalence-pariance/paradox literature
and recommendations for imbalanced binary coding; evidence that error propagation
assuming row-level independence understates intervals under clustered coding;
whether any comparative-coding project propagates measured coder error into
headline typological counts. — **not-checked — no search this round**.

**Potential harm, inequity, or misuse.** A high machine–human κ could be over-sold
as "the coding is validated", licensing complacency about a matrix whose validity
was never tested; a low κ could be used to dismiss genuinely real findings (e.g.
the fork) that a fairer reliability estimate would support. Either number will be
quoted beyond what agreement can support. A machine coder also imports
anglophone/descriptivist bias into an instrument whose whole point is
cross-tradition neutrality, with the bias invisible in a single pooled κ.

**Mitigation.** Pre-specify the statistics (raw agreement plus a
prevalence-robust index alongside κ) and the stratification (slot, tradition,
script); cluster the perturbation by tradition rather than by row; separate
"reliability" from "validity" language in every reported figure; add a
source-level spot-check of disputed cells against the retrieved primary texts so
agreement is anchored to something outside the coding; declare the two
non-row-level layers (era anchors, regime classes) out of κ's scope and treat them
separately.

**Residual uncertainty.** Whether machine–human agreement bounds human–human
agreement at all, and whether propagated intervals at n = 25 with clustered
errors are honest — both remain untested without a genuine second human rater,
and the optional human-coder variant is itself an ethics-review trigger.

**Disposition: retain** — pre-specified, dual-outcome, cheap, and null-informative;
carry the validity-versus-reliability caveat into any write-up.

---

## P07-5

**Idea ID.** P07-5 — Evidence-tier stress test: does the universal stem survive on
primary-anchored systems only?

**Reviewer.** R04 (independent AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** Freeze the README's disclosed grounding tiers
into a machine-readable column *before* any recomputation, then re-run the three
headline structural claims (universal-stem membership, S6⊥S9, S12 as modal slot)
on the strong-primary subset alone with exact-count decision rules and
dual-direction predictions: replication upgrades "grounding tiers differ" from an
honest gap to a measured robustness result; loss of a stem member shows some
universality was carried by secondary evidence. It is a small, fully
ledger-compatible branch of `recompute.py`, minutes of compute, in the project's
own method style.

**Observation that would count against it.** After excluding page-slotless regimes
and boundary cases, only ~6–8 systems remain, so every verdict becomes an exact
count table with almost no discriminating power — and any full-versus-restricted
difference cannot be attributed to evidence *quality* because the subset also
changed *composition* (regimes, boundary cases and non-page systems left at the
same time).

**Alternative explanations (three).**
1. Tier and system type are confounded: any change between the full and restricted
   results may be driven by which systems left (regimes/boundary cases), not by
   their evidential thinness.
2. A fork that holds perfectly on the primary subset may hold by construction —
   both S9-bearing systems (UN, EU) are strongly anchored, so "robust on strong
   evidence" is a property of where the support sits, not of evidence quality.
3. The tier labels are the same researcher's prose judgments frozen into a column;
   freezing them can canonise the original coding decision rather than test it.

**Measurement or analysis failure.** "Strong primary anchor" is a narrative
disclosure coerced into one ordinal/binary column with no calibration rule per
case; the README's tier list mixes source *type* (encyclopedic vs primary) with
retrieval *status* (57/60 fetched), two different constructs in one column. With
n ≈ 8–10, exact tests have essentially no power and leave-one-out is dominated by
single systems — the honest failure mode the idea itself names ("informative but
underpowered") is the likeliest output, and must not be sold as confirmation.

**Sampling or generalizability failure.** The primary-anchored subset is not a
random subsample: it skews to states whose standards are openly digitised and
published — the very retrievability bias P08-5 names. Robustness on that subset
generalises only to the open-web-generous core; it cannot speak to the thin cases
or to traditions never represented. Conversely, dropping thin cases removes
exactly the underrepresented African/pre-modern systems whose inclusion earned
the coverage claim, so a "robust" verdict could quietly narrow the atlas's scope.

**Prior evidence that challenges it.** Look for: whether comparative typological
or area-study databases report prevalence sensitivity after excluding
low-confidence cases (and whether exclusions correlate with region); prior repo
statements that tier correlates with regime class, region or standard type
(`README.md` honest gaps, `analysis/findings.md` §5, `analysis/evidence_base.csv`);
any earlier claim in this repo that the fork's support is concentrated in UN/EU.
— **not-checked — no search this round**.

**Potential harm, inequity, or misuse.** A clean "all headline claims survive on
primary-only data" could be used to close the honest-gaps item and stop investing
in thin cases (PE, HN, ET, WA), entrenching an open-web-centred, Euro-American
core as the "verified" atlas; a failing result could be over-read as "the atlas is
wrong" when it may only show the subset shrank and changed shape.

**Mitigation.** Pre-freeze both the tier rule *and* the exclusion rule for
regimes/boundary cases; report under at least two subset definitions and state
openly that tier and system type are confounded; publish the subset composition
beside every number; pair any robustness verdict with a commitment to strengthen
rather than drop thin cases.

**Residual uncertainty.** Whether enough usable primary-anchored page-document
systems exist at all after exclusions (A2 estimates 8–10 *before* excluding
regimes and boundaries); and whether tier-as-column can be defended given it was
produced by the coder whose reliability is in question.

**Disposition: retain** — cheapest robustness check on the slate and
dual-direction; report it as a composition-confounded sensitivity, not as
validation.

---

## P05-2

**Idea ID.** P05-2 — A within-system digitisation trajectory: do slots migrate
into infrastructure?

**Reviewer.** R04 (independent AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** Use one dated Ukrainian lineage
(ГОСТ 6.38 → ДСТУ 4163:2003 → 4163:2020 → electronic document-flow rules) as its
own control: code each successive standard on the closed 14 slots and test three
pre-stated predictions — stem slots never drop from the requisites list, S14
carriers shift from paper marks (registration stamps, execution lines) to system
logs, and S12 changes form (hand → qualified electronic signature) while staying
present. This converts `diversity.md` §7's cross-sectional inference ("the medium
moves the slots into infrastructure", drawn from Estonia vs Brazil endpoints) into
an observed before/after inside a single system.

**Observation that would count against it.** The requisites list is carried forward
essentially unchanged across editions — no carrier shift at all — or stem slots
drop from the post-digitisation list. The first makes §7's mechanism look wrong
(standard inert to medium), the second breaks stem universality under digitisation;
in a single lineage both are equally consistent with "this standard is a
conservative legal text" rather than with the medium hypothesis.

**Alternative explanations (three).**
1. Policy era and medium are bundled: any change between 2003/2020/e-flow tracks
   Ukraine's wider e-governance and decentralisation reform package, not
   digitisation of the medium as such.
2. A carrier shift may be a *wording* change in the standard (the log is described
   instead of the stamp) with no change in documentary practice — standards record
   doctrine, not behaviour.
3. Persistence of inherited ГОСТ requisites may reflect textual borrowing from the
   Soviet standard rather than invariance of the deep grammar — the null result
   would then be path dependence, not universality.

**Measurement or analysis failure.** The design codes *standards texts* before and
after, while §7's claim is about *documents*; a before/after difference may
therefore be instrument change (normative list vs artefact) rather than regime
change — no practice-level specimen check is specified to anchor either side. The
coding is single-coder with no reliability estimate, and the "sharp reform date"
assumption conflicts with the repo's own admission that era anchors are
approximate. There is also no pre-specified effect size: "some requisites moved
carrier" is unfalsifiably elastic unless the exact slot-by-slot mapping is fixed
before coding.

**Sampling or generalizability failure.** One country, one flow, one lineage — the
idea concedes it cannot support a general claim, yet §7 is a general claim about
medium, so the case can only illustrate. Ukraine is also among the densest,
best-represented, S14-heavy systems in the atlas (the case file is a strong
primary anchor), i.e. the atypical case for any "slots migrate to infrastructure"
story; the trajectory says nothing about traditions whose digitisation was not
post-Soviet reform-driven.

**Prior evidence that challenges it.** Look for: whether successive ГОСТ 6.38 /
ДСТУ 4163 editions actually differ in their requisite lists at all (a diff of
editions would show whether there is any signal to explain); whether the Ukrainian
e-document-flow rules restate requisites or merely cross-reference the standard;
any repo statement already documenting carrier shift for UA or EE as an endpoint
(`diversity.md` §7, `cases/ua.md`, `cases/ee.md`). — **not-checked — no search this
round**.

**Potential harm, inequity, or misuse.** Over-reading one national trajectory as
*the* digitisation mechanism risks essentialising a post-Soviet reform model as
universal; narrating Ukrainian standards mainly as a Soviet-inheritance→EU-association
arc, without the state's own framing of its documentation policy, flattens national
agency — a modest equity concern in how a Ukrainian reform is represented, given
the project is explicitly about de-centring single-axis stories.

**Mitigation.** Add one mechanism-distinguishing observation (does the e-flow rule
re-specify requisites, or only reference the standard?); pre-fix the slot-by-slot
carrier mapping before coding; if time allows add one non-UA comparison lineage
(e.g. the DIN or GB/T revision line) as a control; label output explicitly as a
mechanism-revealing case, never an effect estimate; keep the retrieval attempt log
so blocked Soviet-era sources are visible.

**Residual uncertainty.** Retrieval of older Soviet-era and pre-2020 Ukrainian
texts (the RU/GOST precedent shows this can fail), and the possibility that
editions are near-identical — yielding a null that cannot separate medium
invariance from legal inertia.

**Disposition: revise** — keep the trajectory, but add a comparison lineage and a
practice-level specimen check so medium effect and legal-document conservatism are
separable.

---

## P08-3

**Idea ID.** P08-3 — The colonial genealogy test: does documentary form follow the
metropole?

**Reviewer.** R04 (independent AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** Add a colonial-heritage column to the existing
28-system slot matrix and pre-register a permutation test of
Jaccard(metropole, successor) > Jaccard(successor, same-region non-successor), with
Ethiopia (no metropole) as a negative control and two pre-stated refinements:
stronger affinity for Francophone successors (formula/naming traditions are cheap
to carry) than for successors of layout-fixing traditions, and no affinity for
Ethiopia. This converts `diversity.md` §11d's narrative continuity — Senegal
holding the AOF fonds beside the post-1960 state's — into a falsifiable structural
claim the similarity analysis (`findings.md` §4) never tested, using one added
column on frozen data plus bounded new case files.

**Observation that would count against it.** Metropole–successor affinity
indistinguishable from the permutation null, or a pre-specified model comparison
showing geography or legal family explains profile similarity better than colonial
heritage — the continuity claim fails as structure; equivalently, the effect
vanishes once the sparsity-artefact systems (JP = KE = HN = 1.0) are handled by
the declared exclusion/down-weighting rule.

**Alternative explanations (three).**
1. Shared language and legal family: Francophone successors reuse
   French-derived requisites vocabulary and often literally inherit
   French-model rules, so apparent metropole affinity may be linguistic/legal-family
   affinity — heritage, language and legal family are nearly collinear here.
2. Descriptive-source kinship: successors and metropole may be coded similarly
   because both rest on the same secondary literature that echoes the metropole's
   own administrative writing, not because their documents converge.
3. Standard-template diffusion (GOST-line texts, Francophone guide families) can
   generate profile similarity through copying of a template — a documented
   failure mode (`diversity.md` §12b) that mimics genealogy.

**Measurement or analysis failure.** Jaccard on binary slot presence weights all
slots equally, so the fork's S6/S9 and dense-regime slot counts can dominate
distances irrespective of genealogy; distance choice and sparse-system handling
must be pre-specified or the test becomes degrees-of-freedom. The heritage coding
is categorical and partly contested (Belgian, Italian, mandate cases), decided by
one researcher. Critically, the metropole profiles (GB, PT, BE) do not exist in
the corpus — newly authored case files, written by the same coder in the same
session as the successors, risk inflating similarity through shared coding style,
exactly the correlation the test is meant to detect in the data.

**Sampling or generalizability failure.** n ≈ 25 gives a coarse permutation
distribution, and the African successors in the corpus are thin/secondary-grounded
and Francophone-heavy — the design over-samples precisely the colonial
relationship predicted to be strongest, so a positive result may not survive an
Anglophone/Portuguese expansion. Successor and metropole systems are not
independent observations (one tradition generates the other), violating the
exchangeability the permutation null assumes unless blocks are declared in
advance. Results would not transfer to non-colonial or settler contexts absent
from the 28.

**Prior evidence that challenges it.** Look for: quantitative work on legal
transplants/administrative transfer showing how much successor-system convergence
is attributable to language and legal family rather than colonial administration;
any prior measurement of documentary-form inheritance in post-colonial
bureaucracies; repo-internal assertions of continuity that are already data-free
(`diversity.md` §11d, §10e, §12c, `cases/sn.md`, `cases/et.md`,
`theme_matrix.csv` "imperial/colonial continuity = 6"). — **not-checked — no search
this round**.

**Potential harm, inequity, or misuse.** Reducing successor states' document regimes
to "inherited from the metropole" can reproduce a colonial narrative in which
African and Asian administrative lineages have no indigenous history — the output
could be misused as evidence that post-colonial administrations are derivative
rather than autonomous; framing Ethiopia only as a "negative control" risks
tokenising the one non-colonial case. This is a representational/equity risk in how
the finding is stated, not a risk to participants.

**Mitigation.** Pre-register a three-predictor comparison (heritage vs legal family
vs region) and report the collinearity honestly rather than claiming causal
separation; frame conclusions as properties of *document form* only, explicitly
not of administrative capacity, legitimacy or statehood; keep the Ethiopian
control in the write-up as a substantive case, not a null; disclose single-coder
authorship of any new metropole case files and, where possible, code metropole
files before successors to reduce style leakage.

**Residual uncertainty.** Whether heritage can be statistically separated from
language/legal family at n ≈ 25 at all; and whether GB/PT/BE profiles can be built
to the repo's evidential standard inside a 1–3 month window without weakening the
frozen-coding discipline.

**Disposition: revise** — proceed only as the pre-registered three-predictor
comparison with the Ethiopia control and a bounded metropole-coding plan; if
collinearity proves unresolvable, report a scoped descriptive instead of a
genealogy claim.

---

## P08-2

**Idea ID.** P08-2 — Sovereignty/stewardship as a fourth regime dimension of
document law.

**Reviewer.** R04 (independent AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** Desk-code published Indigenous/community
data-governance framework texts clause-by-clause using the repo's own
clause→dimension mapping method (the way `requisites.csv` maps requisites), and
test three pre-stated predictions: a non-empty residual category of obligations
that fit neither trace, access nor persistence/appraisal; governance attaching to
record systems/fonds rather than to documents (unit one level up, echoing the
Indian file); and at least one documented case where a state open-government
access regime and a community stewardship regime constrain the same records in
opposite directions. If any of these hold, the "kinds of document law" catalogue
gains a dimension whose legislator is not the state — a genuine de-centring move
that neither the atlas nor its regime catalogue currently allows.

**Observation that would count against it.** Every coded clause maps cleanly onto
access or appraisal (dimension redundant), or the frameworks turn out to govern
licences and persons rather than records (wrong object). Either result kills the
fourth dimension — and, worse, a desk-only coding cannot distinguish "no residual
exists" from "a state-document-derived codebook cannot see the residual".

**Alternative explanations (three).**
1. A residual category may be an artefact of applying a state-derived codebook to
   community texts — the instrument generates the novelty; an independent
   inductive pass over the same clauses might dissolve it.
2. Apparent stewardship clauses may be access conditions with purpose limits
   (access *with qualifiers*), i.e. a difference of degree on the existing access
   dimension rather than a new dimension.
3. Apparent state-vs-community tensions may reflect jurisdiction over different
   records or different legal authority, not competing governance of the same
   records — a scope mismatch rather than a structural conflict.

**Measurement or analysis failure.** The clause→dimension mapping is hand-mapping,
and the repo has never measured hand-mapping reliability (the very gap P06-1 and
P02-1 target) — here with no inter-rater check and no community member among
coders. "Residual > 0" is a trivially satisfiable threshold: any coding scheme
produces a residual, so the test as specified cannot fail on quantity, only on
interpretation. No minimum residual size or proportion is pre-declared, and no
manipulation check exists for the access/stewardship distinction itself.
Community framework texts are living, versioned documents, so the corpus is
unstable unless version-pinned at coding time.

**Sampling or generalizability failure.** Which frameworks are selected determines
the answer: OCAP-style and CARE-type frameworks are concentrated in Anglo
settler-colonial contexts, so a handful of published national frameworks cannot
represent Indigenous governance diversity; coding only openly published texts
systematically excludes community-held and unpublished governance practice —
the same open-web selection bias P08-5 identifies, now applied to the communities
the idea intends to centre. The idea also concedes its third assumption (solo
non-community coding without validation) is its weakest point.

**Prior evidence that challenges it.** Look for: prior scholarship analysing
whether Indigenous data-governance principles (OCAP®-style principles, CARE
principles and non-Anglophone equivalents) are treated as distinct from access,
consent or licensing frameworks — and whether the distinctness claim is
substantiated or asserted; critiques of extractive coding of community governance
texts; the derivation of the atlas's own three regime dimensions
(`diversity.md` §10b, `EXECUTIVE_SUMMARY.md`) to check whether a fourth was
already considered and rejected. — **not-checked — no search this round**.

**Potential harm, inequity, or misuse.** Extractive use of community governance
texts without engagement reproduces precisely the inequity the idea claims to
correct, and may breach custodial norms about how such frameworks should be used;
re-characterising a community's model as "access with conditions" would be a
substantive representational harm; the catalogue could then be used to fold
community sovereignty into a state-centred taxonomy, diluting the de-centring
claim — and publishing a desk-only coding without community review risks being
read as the project speaking for those communities.

**Mitigation.** Run only the desk version in this cycle: version-pin every text,
record provenance and custody notes, and pre-register both the residual threshold
*and* a second inductive coding pass to test whether the residual survives a
fresh frame; never contact or identify community members in this session; route
any community-engaged version, and any output intended to characterise a living
community's governance, to an authorized ethics/consultation body for review
before work begins; invite community review of the coding frame before any
publication of results.

**Residual uncertainty.** Whether a residual exists at all under a state-derived
codebook; whether the desk-only version can be defended as non-extractive; and
whether meaningful community review is feasible at all within the solo-researcher
constraint — none of which this session can resolve or approve.

**Disposition: external review** — the desk version may be prepared as a
specification, but any community-engaged work, and arguably publication of coding
community governance texts, requires an authorized ethics/consultation body
outside this session; this session cannot issue that approval.

---

*End of adversarial round — R04. Five ideas reviewed: P06-1, P07-5, P05-2, P08-3,
P08-2. No rankings, no winner selection, no literature search.*
