# Adversarial review — reviewer R02 (session udm-ideation-01)

Reviewer: **R02** — AI reviewer, disclosed; originated none of these ideas.
Method: each idea is reviewed in its **strongest version** before any attack.
No literature search this round — prior-evidence items are stated as what to
look for, flagged `not-checked — no search this round`.
No ranking or winner-picking; dispositions concern only the six ideas below.

---

## P08-6

**Reviewer.** R02 (AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** The two-declension model is a claim about a
closed paradigm, and the corpus itself already names a genre that fits neither
pole: the Indian secretariat note "argues toward a decision" (`cases/in.md`)
and Bénin's note drops S6 *and* S12 by rule (`cases/bj.md`). If a functional
definition (internal, deliberative, argues toward a decision) finds that
profile in ≥5 systems across ≥3 traditions, then the perfect S6⊥S9
complementary distribution is a special case of a three-or-more-profile
paradigm — a genuine structural challenge to `morphology.md` §3 and
`analysis/findings.md` §2, not a footnote. The idea pre-states the expected
profile (no S9, no S12, S7/S8 filled) and offers a permutation/cluster check,
so a failed challenge strengthens the fork either way.

**Observation that would count against it.** Note-type documents, once located,
scatter onto the existing epistolary and normative profiles with no residual
cluster (permutation check fails to separate a third group); or the genre is
found in only 2 systems — the two already described — so the hypothesis dies on
coverage rather than structure.

**Alternative explanations (≥2).**
1. Any apparent third cluster could be an artefact of the analyst's own
   functional definition plus one coder's classification — different plausible
   definitions of "deliberative note" could redistribute the same documents
   back onto the two poles.
2. A "no S12" sub-profile may track *internal vs issued* status (a working
   document is unauthenticated because it is not yet an act), not a third
   declension — i.e. the profile marks document lifecycle stage, not a genre
   class competing with the fork.
3. Thin or translated sources may simply fail to record S6/S9 cues in
   note-type documents, producing an apparent empty pole from missing data
   rather than from structure.

**Measurement or analysis failure.** Single-coder, cross-linguistic genre
identification with no inter-rater check — the repo's own declared caveat for
keyword coding recurs here at higher stakes. The `genre` column extension to
`requisites.csv` is a schema-gate change: if `recompute.py`'s checked figures
drift, the challenge can be mistaken for a data error. Slot coding of notes in
thin-sourced systems may inherit gloss-only `local_term` cells, so "S9 absent"
may mean "recital cue untranslated". Finally, the sample is selected *because*
these documents were noticed in case prose — a look-elsewhere effect that
inflates the apparent cluster.

**Sampling or generalizability failure.** The coverage gate (≥5 systems,
≥3 traditions) is both the idea's admission ticket and its weakest point: the
two known instances are Indian and Francophone, i.e. the same traditions that
already carry the richest case files, so the "third declension" could turn out
to be a feature of Anglophone/Francophone secretariat practice rather than a
paradigm-level class. Soviet, Chinese and Islamicate chancery naming logics
are explicitly documented as non-shared (`qualitative_analysis.md` §3), so
absence of "notes" there may reflect vocabulary, not genre structure.

**Prior evidence that challenges it.** Look for: (a) genre taxonomies in
diplomatics/records-management literature that classify the deliberative note
as a sub-genre of the normative act rather than a third class; (b) any prior
corpus study of internal government "notes" showing they inherit the
surrounding regime's slot profile; (c) evidence that Bénin's note drops S6/S12
by an idiosyncratic national rule rather than a recurrent type.
**not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low direct harm. Risks are
reputational and inferential: a weak, single-coder "third declension" published
against the atlas's own gate would invite the criticism that the project
dismantles its headline finding on ad hoc genre definitions. Indirectly,
privileging the Indian/Francophone note as "universal class" while other
traditions' equivalent internal documents go unnamed over-represents
metropolitan secretariat vocabulary — the exact bias the session tries to
de-centre.

**Mitigation.** Freeze the functional definition and the expected slot profile
*before* coding; require the profile to be demonstrated in ≥2 traditions with
retrievable sources, not just case-file prose; run the cluster check blind to
system identity; register the `genre` schema change as a declared deviation
before `recompute.py` runs; report a "coverage failed" outcome as a legitimate
endpoint, not a silent drop.

**Residual uncertainty.** Whether any cross-linguistically stable definition of
"deliberative note" exists at all — if not, the idea cannot be falsified as
specified, only abandoned, and the falsifier "genre cannot be located outside
two cases" is indistinguishable from "the definition was wrong".

**Disposition:** **retain** — sharp, pre-stateable challenge to a headline
finding with a symmetric, publishable failure mode; proceed only behind the
coverage gate and a frozen definition.

---

## P06-4

**Reviewer.** R02 (AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** The atlas's 28 systems are a purposive
sample selected partly by retrievability of a standard — correlated with the
very property claimed (a codified document regime) — yet every prevalence
(17/25, 4/10 → 7/9) is quoted without an interval. Wilson intervals, clustered
intervals, leave-one-tranche-out sensitivity, and — the strongest element — a
*committed, pre-coded prediction for the next system added* turn post-hoc
description into a genuine out-of-sample test. The committed prediction is the
part nothing else in the session can substitute: it is scoreable, it is
pre-registered by construction, and a miss by >4 slots would directly bound
the scoped universality claim in `EXECUTIVE_SUMMARY.md`.

**Observation that would count against it.** The committed hold-out scores
poorly (miss by >4 slots), or authentication's clustered interval collapses
toward the codability base rate, or leave-one-tradition-out drops a "universal"
stem slot below half — each shows the grammar does not generalise beyond the
sample that produced it.

**Alternative explanations (≥2).**
1. A poor hold-out score may reflect *retrieval and coding quality* on the new
   system rather than failure of the grammar — the provisional RU column is
   blocked precisely where evidence is thinnest, so a miss could be a
   measurement failure wearing a theoretical costume.
2. Wide intervals may reflect tradition clustering (systems are not
   independent draws) rather than genuine prevalence uncertainty — under a
   clustered frame the "estimate" describes a handful of tradition families,
   not a population of regimes; the same numbers then support a defensible
   claim under one frame and a weak one under another.
3. The frame is chosen by the analyst after knowing which systems exist; a
   contestable frame can be tuned (accidentally or not) until intervals look
   good — "disclosed and varied" mitigates but does not remove the
   researcher-degrees-of-freedom problem.

**Measurement or analysis failure.** Interval choice (Wilson vs beta-binomial
vs clustered) changes widths materially at n≈25 and the choices must be
pre-specified or the exercise looks like an analyst-degrees-of-freedom
demonstration. Scoring the hold-out needs a frozen coding rule for the new
system — but coding is single-coder, so the "prediction" and its scoring share
one coder's judgement. Leave-one-tranche-out with ~3 tranches produces
coarse, unstable sensitivity swings that can be narrated either way. The
predicted Wilson interval for 17/25 (≈ [0.48, 0.83]) is hand-computed in the
register and must be re-derived in code (its own note says so).

**Sampling or generalizability failure.** The sampling frame is the load-bearing
weakness and the idea admits it: no census of "all official-document regimes"
exists, so any frame (retrievable in-force standard; UN member states) selects
on observability — the same retrievability bias that P08-5 exists to audit.
Tradition clustering means the effective n is closer to the number of tradition
families (~7) than to 25, which the naive intervals will understate until the
clustered version is reported. A hold-out drawn from an already-represented
tradition tests interpolation, not universality; only an unrepresented-tradition
hold-out tests the claim, and retrieval there is exactly what has failed so far.

**Prior evidence that challenges it.** Look for: (a) methodological literature
on convenience/purposive samples of institutional regimes showing prevalence
estimates biased toward codified systems; (b) prior work quoting intervals on
comparative-type samples and how clustered designs were handled; (c) whether
any existing typology already attempted an out-of-sample prediction of document
requisite profiles and how it scored.
**not-checked — no search this round.**

**Potential harm, inequity, or misuse.** A committed prediction that fails
badly could be weaponised as "the atlas is wrong" when the honest reading may
be "the frame was wrong" — reputational harm to a careful project if the frame
caveat is buried. Conversely, publishing narrow naive intervals invites
over-claiming precision. No participant or community risk; the equity angle is
that frames built on open-web retrievability systematically under-represent
Central Asia, Pacific and small states — the framing must not re-certify that
gap as a population fact.

**Mitigation.** Pre-register two or three frames and the interval family before
computing; report naive and clustered intervals side by side; freeze the coding
rule and the scoring key for the hold-out before any new system is coded;
commit to scoring the hold-out regardless of outcome (no second look, no
recoding after seeing the prediction); treat a retrieval failure as
"instrument not run", never as a miss.

**Residual uncertainty.** Whether a defensible population statement is even
available for "written official-document regimes" — if frames cannot be
defended against each other, the deliverable degrades to a sensitivity table
whose interpretation stays contested, though the committed prediction remains
valuable regardless of frame.

**Disposition:** **retain** — the committed out-of-sample prediction is
unmatched in the pool and cheap; run it behind a pre-registered frame and
interval specification.

---

## P04-1

**Reviewer.** R02 (AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** `README.md` says "Efficiency is measured
nowhere" and `morphology.md` §6 says a metric is needed; `requisites.csv` plus
`slot_matrix.csv` already hold 14-bit codewords for 25 systems. Entropy,
conditional entropy given genre, and a per-slot redundancy decomposition turn
"the corpus spends its bits on forgery-resistance and audit, not comprehension"
into a number, and H(slots|genre) < H(slots) would give finding 3 an
information-theoretic form. It is days of CPU on frozen data, fully compatible
with `recompute.py`, and the permutation-null design means a null result
("swallowed by sparsity") is itself an honest, reportable outcome.

**Observation that would count against it.** Redundancy distributes uniformly
across slots, or the whole structure is reproduced by coding density and
sparsity under a permutation null, or H(slots|genre) ≥ H(slots) — any of these
means the metric re-derives the existing caveats rather than measuring
efficiency.

**Alternative explanations (≥2).**
1. A concentration of "redundancy" in S12/S14 could be a mechanical
   consequence of their high marginal frequencies — high-prevalence slots
   dominate any entropy budget by construction, so "the corpus spends bits on
   validity" may be arithmetic, not a finding about design priorities.
2. Genre conditioning effects may reflect how genre *labels* were assigned per
   system (hand-coded, one label each) rather than a real channel property —
   mislabelling moves conditional entropy directly.
3. The whole profile may be an artefact of the hand-coded binary matrix: cells
   where the coder was unsure tend toward 0/1 patterns that inflate apparent
   structure.

**Measurement or analysis failure.** Mutual-information estimators are biased
upward at n = 25 (the register says so); if the bias correction or the
permutation null is chosen after seeing results, the analyst decides the
outcome. "Redundancy share" has no unique definition at 14 binary positions
with a 225-row matrix — plug-in vs bias-corrected vs Bayesian answers differ.
Genre conditioning uses a single genre label per system while systems produce
multiple genres, so H(slots|genre) is computed on a coarse proxy. Finally,
binary slot presence discards obligatory/optional and form information, so
"bits" are a very loose channel metaphor — the mapping from entropy to
"spent on validity not comprehension" is interpretive, not derivable.

**Sampling or generalizability failure.** 25 systems with documented sparsity
artefacts (JP = KE = HN = 1.0) and heterogeneous denominators (regimes vs
page standards, P06-6's codability problem) mean the "channel" sample mixes
non-comparable codeword alphabets; leave-one-system-out stability for S12's
share is stated as a prediction but with n=25 a single dense system (SU, UA)
can dominate. Nothing generalises beyond this purposive corpus — fine for a
metrological description of the atlas, not for claims about official documents
as a class.

**Prior evidence that challenges it.** Look for: (a) information-theoretic
analyses of small categorical codebooks showing what n is needed for stable
entropy/mutual-information estimates; (b) prior "efficiency of document
format" measurements and whether any used slot-presence entropy (vs actual
token/compression measures); (c) critiques equating marginal frequency with
"redundancy" in coding schemes.
**not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low. Main risk is over-claiming: a
clean-looking "redundancy budget" figure could be cited as if it measured
citizen-facing comprehension cost, which it does not — it measures hand-coded
slot distributions. A wrong-signed or null result published without the
estimator caveats would hand sceptics a "the metric was broken" argument.

**Mitigation.** Pre-specify the estimator family, the null (independent and
tradition-blocked) and the primary statistic in a short analysis plan before
running; report redundancy alongside raw marginal frequencies so arithmetic
confounds are visible; state the "binary presence is a loose channel metaphor"
limitation in the figure caption; keep permutation results, not point estimates,
as the headline output.

**Residual uncertainty.** Whether any information-theoretic signal survives the
sparsity at n = 25 at all — the idea says it "dies honestly" if not, but that
outcome leaves the efficiency claim exactly where it was (unmeasured), so the
idea may deliver rigour without delivering the metric the project wants.

**Disposition:** **revise** — keep the idea, but freeze estimator, null and
primary statistic pre-computation, and add the marginal-frequency control so
the redundancy ranking cannot be arithmetic in disguise.

---

## P03-1

**Reviewer.** R02 (AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** Accuracy in the finding-5 instrument sits at
or near ceiling for 6/12 machine readers and is suspected of ceiling for
humans; `morphology.md` §6 names parsing cost/time as the missing efficiency
metric; `PREREGISTRATION.md` §5 already timestamps trials (`rt_ms`). Adding a
pre-registered processing-cost co-primary outcome means the register question
stays answerable even under a null accuracy result: "same answers, more work"
would be the first positive comprehension signal in the project, and a precise
cost null (CI excluding ≥10% of median RT) would upgrade the current
equivalence claim. It reuses the existing instrument, existing power tooling,
and the `DEVIATIONS.md` pre-data revision precedent.

**Observation that would count against it.** Plain slower than formal on
correct trials with a CI excluding zero in the opposite direction; or every RT
gap explained by fast errors (no cost on correct trials); or equivalence CIs
narrow around zero under both the open and the time-bounded version — all
would push the register effect from "undetected" to "credibly absent".

**Alternative explanations (≥2).**
1. An RT gap could reflect *decision and distraction* time in a browser
   (reading, verifying, tab-switching) rather than comprehension cost — browser
   RT at per-question granularity still bundles several processes.
2. Formal renderings may simply be longer texts; any raw-RT difference then
   measures length, not register — unless word count is controlled, which the
   current design does not specify.
3. The time-bounded findability block changes task demands (speeded vs
   unspeeded), so a block difference could be an instruction effect rather than
   a register effect.

**Measurement or analysis failure.** `rt_ms` granularity is explicitly
"to be verified" — if timing is per-document rather than per-answer, the
pre-data revision changes the instrument after the fact and the change must be
logged before any human data or the pre-registration's credibility is
compromised. RT distributions are skewed: trimming rules, log-transform and
the treatment of errors must be pre-specified or the outcome becomes
researcher-degrees-of-freedom. Power was computed for accuracy, not RT; the
register's own plan to re-run `simulate_data.py` for the RT outcome must happen
before collection, and RT effects at N=36 may be underpowered regardless.

**Sampling or generalizability failure.** The same participant pool as the
registered experiment — likely a convenience sample; RT is notoriously
population-sensitive (fatigue, device, language dominance), so a browser-based
RT effect generalises poorly beyond the recruited sample, and bilingual
(EN/UK) conditions add language-order effects. Six obligations across two
languages give few items per cell once RT variance is added.

**Prior evidence that challenges it.** Look for: (a) register/formality effects
on reading time in official or legal texts, and whether effects survive
length-matched controls; (b) methodological work on browser-based RT
measurement reliability (latency noise, device effects); (c) whether existing
comprehension experiments on plain-language rewrites found cost (RT) effects
when accuracy was null.
**not-checked — no search this round.**

**Potential harm, inequity, or misuse.** New human participants ⇒ ethics gate
applies and cannot be cleared by this session. Beyond process harm, a
speeded-or-timed design could disadvantage participants with lower literacy,
non-native speakers or disability — the very populations plain-language
research aims to serve — if the time-bounded block is introduced without
accessibility safeguards. Inference harm: publishing RT as a co-primary
outcome after seeing accuracy nulls would look like outcome-switching unless
registered pre-collection.

**Mitigation.** Machine-only and timing-code work proceeds now; the human
version waits for authorized ethics review. Register the RT outcome, the
findability block, trimming/transform rules and a length-matched analysis
*before* any human data as a `DEVIATIONS.md` Revision 2. Keep accuracy
co-primary (no switch). Drop or soften speeded deadlines, offer unspeeded
analyses as primary, exclude speed-accuracy-confounded trials by pre-set rule,
and report device/language covariates.

**Residual uncertainty.** Whether browser RT at this item count can resolve a
plausible register effect at all — if the CI at N=36 cannot exclude a 10% gap,
the cost outcome replicates the accuracy ceiling problem in a new currency.

**Disposition:** **pause** — sound and worth keeping, but gated on external
ethics review before any human-facing step; only the timing-code and
machine-side preparations may proceed meanwhile.

---

## P07-3

**Reviewer.** R02 (AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** `diversity.md` §7 claims "the morphology
survives; its carriers do not" from exactly two cases (Estonia, Brazil) and
never measures it — yet this is the claim digital archives care about. A
four-way rubric (content-invariant / structure-dependent / substrate-bound /
wording-bound) applied to all 225 requisites yields per-slot and per-system
fragility rates, tests stem-vs-surface separation directly, and produces a
preservation-risk profile no page-format standard offers. It is CPU-trivial,
weeks of solo work, uses the frozen CSV, and pre-states quantitative
predictions (stem ≥90% content-invariant; substrate marks ≥70% fragile; S12 the
most fragile stem slot — a universality-vs-portability tension).

**Observation that would count against it.** Fragility rates fail to separate
stem from surface (small or reversed gap); S12 scores no more fragile than
other stem slots; or the delayed re-code shows low agreement — the last would
disconfirm the rubric itself and reduce the idea to a qualitative essay.

**Alternative explanations (≥2).**
1. Any stem/surface fragility gap could be *definitional*: the rubric will be
   written by someone who already believes stem slots carry content and surface
   slots carry substrate, so the coded gap may recapitulate the codebook rather
   than measure migration behaviour.
2. A high fragility rate for S12 may reflect that authentication *forms* are
   already documented as variable (`diversity.md` §3) — i.e. fragility tracks
   known form-variation, not migration risk specifically.
3. Rows whose `local_term` holds only an English gloss may be coded fragile
   because the substrate cue is missing from the data, not because the requisite
   is substrate-bound — a data-completeness effect.

**Measurement or analysis failure.** The only reliability check available to a
sole researcher is a delayed self-recode of 50 rows — self-agreement is
optimistic by construction and provides no inter-rater bound, so P1–P3 could be
artefacts of stable individual bias. "Would survive a migration" is a
counterfactual judgement about an undefined event: the register does define
migration as paper → structured digital, but later format changes
(print→PDF→XML→JSON) may flip categories, and rows judged from glosses rather
than source documents inherit the repo's English-gloss caveat
(`findings.md` §6). There is no external criterion validating the four classes,
and no sham or positive-control coding to show the rubric discriminates when it
should.

**Sampling or generalizability failure.** The 225 rows are the requisites of
25 systems with wildly unequal coding depth — thin, secondary-grounded cases
(PE, HN, ET, WA) contribute more uncertain judgments while dense cases (UA, SU)
dominate rates; per-system fragility profiles for thin systems are therefore
mostly the coder's inference from encyclopedia prose. "Migration" cases are
drawn mainly from two traditions (Estonia, Brazil) plus narrative hints
(Garuda stamp, hanko, tughra) — a rubric tuned on those cues may not transfer
to systems with no documented digitisation episode at all.

**Prior evidence that challenges it.** Look for: (a) records-migration and
digital-preservation literature on which document features actually survive
format migration (does content/structure separation match practice?); (b)
whether empirical migration studies find authentication features more or less
durable than content fields; (c) prior inter-rater reliability for analogous
"migration-behaviour" coding schemes, to know what self-agreement is worth.
**not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low direct harm; the misuse risk is
downstream — a single-coder "fragility rate" could be cited by archives or
standards bodies as a preservation risk assessment when it rests on one
researcher's counterfactual judgement. Equity angle: systems with thin
(non-Western, encyclopedia-grade) sources will appear more fragile simply
because their substrate cues were never captured in the data, penalising
already under-evidenced traditions.

**Mitigation.** Freeze the rubric with positive and negative control rows
before coding; add an independent second pass (blind LLM coder at temperature
0, documented — no participants needed) and report agreement alongside the
self-recode; code `uncodable` explicitly rather than guessing; report fragility
rates with the grounding tier as a covariate so thin-source systems are visibly
separated; pre-register the three predictions and the low-agreement abort
condition.

**Residual uncertainty.** Whether any solo-observable reliability check can
establish that "would survive a migration" is a property of the requisite
rather than of the coder — if not, the output is a structured expert opinion
and must be labelled as such, not as a measurement.

**Disposition:** **revise** — the question is worth answering and the data are
in hand, but the single-coder self-recode must be replaced/augmented by an
independent second coding pass and control rows before any figure is published.

---

## P02-4

**Reviewer.** R02 (AI reviewer, disclosed; non-originator).

**Strongest version of the idea.** `check_claims.py` proves that every claim-id
and source-id *resolves*; it cannot detect a claim that overstates, drifts from
or contradicts its source — the failure mode a citation graph is most exposed
to. With 57 of 60 sources already on disk as plain text, a cheap LLM
entailment pass returning supported / partially supported / not-found **plus a
verbatim quote that is string-matched into the source** mechanically defeats
hallucinated evidence; the output is a ranked review queue, never an automatic
edit. Cost is ~92–200 model calls at the repo's demonstrated dollar scale, and
the 4 provisional claims correctly returning "not found" is an informative
expected result rather than a failure.

**Observation that would count against it.** More than 10–15% of verified
claims are unmatchable (the ledger's prose overstates its sources and "88
verified" needs redefinition); or the pass agrees with manual reading no better
than chance on a hand-checked subsample (the tool is noise).

**Alternative explanations (≥2).**
1. "Not found" may indicate *quote-location* failure (boilerplate-heavy HTML,
   encoding, segmentation) rather than unsupported claims — a retrieval/layout
   artefact would be misread as a ledger defect unless false-negative rates are
   measured.
2. Supported verdicts may be inflated by *shared bias*: claims were written
   (possibly agent-assisted) from the same sources the entailment model reads,
   so agreement can reflect common provenance rather than independent
   verification — the same circularity P01-6 warns about.
3. Interpretive/cross-file claims (e.g. ancestor or causal statements in
   `diversity.md` §13) legitimately span multiple sources; their "partial"
   verdicts could be counted as failures, distorting the headline mismatch
   rate.

**Measurement or analysis failure.** Entailment over English claims and
UA/RU/AR/ZH/FR sources depends on cross-lingual capability of a cheap model —
unverified, and weakest exactly where grounding is thinnest (Arabic, Thai,
Ge'ez material). String-matching the quote is strong for hallucination but
weak against *misleading* quotes: a verbatim span can be torn from context and
still "support" an overstated claim — the pass catches missing evidence, not
scope or polarity drift beyond the span. Thresholds (what counts as
"partially supported", what mismatch rate triggers redefinition) must be
fixed before running or the review queue becomes a dial. The 15-claim
hand-check is itself single-coder.

**Sampling or generalizability failure.** 92 claims from 60 sources is the
whole ledger, so there is no sampling issue within the project — but the
generalisability question is whether a verdict calibrated on this ledger
transfers to new claims added later; the tool's error rates are unmeasurable
beyond a small hand-check. Boilerplate-heavy wiki dumps and re-hosted mirrors
(known from `diversity.md` §12b) concentrate in some source classes, so error
rates are heterogeneous across the very sources carrying the most claims.

**Prior evidence that challenges it.** Look for: (a) benchmarks of LLM
entailment/claim-verification against human judgement, especially
cross-lingual and on long documents — expect non-trivial false-positive rates;
(b) studies on quote-matching-based fact verification and known failure modes
(context stripping, granularity mismatch); (c) whether NLP-based literature-
review tools have been audited for false "supported" verdicts on interpretive
claims.
**not-checked — no search this round.**

**Potential harm, inequity, or misuse.** Low direct harm; misuse risks are
(a) false confidence — wiring the pass into the gate as if it were a verifier
when it measures model agreement, not truth; (b) false accusation — flagging
carefully scoped claims as overstated because a cheap model cannot follow
qualification; (c) over-trust of monolingual-English claims vs translated
sources, which could systematically flag non-English-sourced work as weaker —
an equity problem for a corpus deliberately built on UA/AR/ZH material.

**Mitigation.** Keep the pass advisory (queue, never auto-edit) exactly as
specified; validate on a stratified hand-check spanning script families and
source types *before* wiring in; report false-positive and false-negative
rates per script family, not one global rate; require quote + surrounding
sentence (window match) rather than bare span; pre-register the flag thresholds
and the interpretation of "partially supported"; treat the 4 provisional claims
as a pre-declared expected class.

**Residual uncertainty.** Whether cross-lingual entailment at dollar-level cost
is accurate enough on Arabic/Thai/Ge'ez sources to avoid systematically
flagging non-English evidence — until the stratified hand-check says, the
tool's fairness across the corpus's script families is unknown.

**Disposition:** **retain** — cheap, mechanically verifiable, advisory-only,
and its failure modes are checkable in advance; proceed behind the stratified
hand-check gate.

---

*End of adversarial review — R02, 6 of 6 assigned ideas covered.*
