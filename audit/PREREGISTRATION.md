# Pre-registration — P06-2: exact-null audit of the atlas's perfect structural rules

**Status: LOCKED before run.** Owner approval: Kyrylo Yasuda, 2026-10-15
(session udm-ideation-01, decision log D002). Promoted from the session draft
`brainstorm/P06-2_PREREGISTRATION_DRAFT.md` with two pre-registration edits, both
recorded here: (a) this status header; (b) §5.2's block source, widened from
"`diversity.md` §1–§2 alone" to the root README's §Coverage grouping — the §1 table
covers only the extended set and cannot label the base systems (DE, CN, UA, EU, UN),
while the README §Coverage list was written at v1.1 on 2026-10-06, before this
session, and is equally slot-value-blind. This file, `tradition_blocks.csv`,
`null_audit.py` and `DEVIATIONS.md` are committed together; that commit hash and
date are the registration timestamp, the same pattern as
`experiment/PREREGISTRATION.md`. No test statistic on the registered matrix has been
computed at registration. There is no external registry entry; that limitation is
stated in §10 (an OSF registration is the obvious follow-up).

Selection of this study: Kyrylo Yasuda, 2026-10-15 (session udm-ideation-01,
decision log D002). Pre-registration drafted by the project's Hermes agent; the
same agent is the analyst (§10).

Two working numbers in §2 are **hand-derived from published prose**
(`analysis/findings.md` §1–§2) purely to fix expectations; they are re-derived in
code at run time from the frozen matrix, and an assertion failure stops the run
(§6.1, §8).

## 1. Study information

| field | value |
|---|---|
| title | From census to inference: are the atlas's "perfect" structural rules surprising under exact nulls? |
| project | `05.4_universal_document_morphology` (comparative atlas of official-document standards) |
| claim under test | README headline findings 1–2; `morphology.md` §3 and §5.2; `analysis/findings.md` §2 (fork); `analysis/qualitative_analysis.md` §1 (implication rules, negative rule) |
| population | the 25 slot-coded systems of the atlas corpus, explicitly as a convenience corpus (§10.1) — not a random sample of the world's document regimes |
| design | exact enumeration / Fisher-type tests of three pre-enumerated claim families on one frozen matrix, plus a tradition-blocked secondary null and deterministic informativeness thresholds |
| data | `analysis/slot_matrix.csv` (25 × 14 slots), frozen by hash (§4) |
| registration | this file at git commit; no external registry |
| contribution framing | prior art for permutation/exact nulls in typological co-occurrence exists (evidence check E02, status challenge-located); the claimed contribution is the **application to this atlas's specific rules and corpus**, stated so in any write-up |

Nothing human-subject; ethics: not applicable.

## 2. Background and hypotheses

The atlas states its structural regularities as census facts about 25 systems:
"S9 never co-occurs with …" and implication rules at confidence 1.00. "Never in our
data" is a fact about 25 systems; whether it would hold in the 26th is a sampling
question, and with the printed marginals some perfect patterns are exactly what
independence would produce. Hand-worked illustration (fixed expectations only;
re-derived in code): with S6 = 8/25 and S9 = 2/25, P(both S9 systems fall outside
the eight S6 systems) = C(17,2)/C(25,2) = 136/300 ≈ 0.45 — the single edge the
prose calls the clearest structural finding is, alone, not unlikely. The testable
object is therefore the *joint* fork pattern and the *implications*, not each
negation edge in isolation.

**Registered predictions** (fixed now, scored after the run regardless of direction;
each labelled conceptual / operational / statistical):

**R1 (fork, per-edge).** *Conceptual:* each negation edge is individually
unsurprising at current margins. *Operational:* count of family-A edges with
BH-adjusted q < 0.05. *Statistical:* predicted = 0 rejections after BH-FDR
(one-sided depletion tests, §5).

**R2 (fork, joint).** *Conceptual:* the fork is supported as one joint pattern,
not as six independent pieces of evidence. *Operational:* exact p of statistic T =
number of S9 systems carrying ≥1 partner slot (observed 0) under fixed-margin
enumeration of all C(25,2) = 300 placements of the S9 pair. *Statistical:*
predicted p < 0.05 (single declared test, §6.4).

**R3 (implications).** *Conceptual:* at least one confidence-1.00 implication rule
survives as a population-level inference. *Operational:* count of family-B rules
with BH q < 0.05 (one-sided enrichment tests). *Statistical:* predicted ≥ 1
rejection.

**R4 (informativeness).** *Conceptual:* some per-edge claims are currently
untestable rather than confirmed. *Operational:* n* = smallest total corpus size
N ≥ 25 at which continued perfect pattern would reject at per-edge α = 0.05 (§6.6).
*Statistical:* predicted ≥ 1 family-A edge with n* > 100 systems (4× the corpus).

**Disconfirmation is registered too:** if R2 fails to reject, the fork loses its
inferential base and must be regraded descriptive-only in a later repo version, with
that amendment logged. If the tradition-blocked null makes the pattern *more*
surprising than the unblocked one, the per-edge ranking reported is the blocked one
and the reversal is discussed (§5.2).

## 3. Claims under test (frozen enumeration)

**Family A — negation edges (6):** S9 ⊥ S4, S9 ⊥ S6, S9 ⊥ S7, S9 ⊥ S8,
S9 ⊥ S10, S9 ⊥ S14 (source: `analysis/qualitative_analysis.md` §1 "negative rule";
`findings.md` §2).

**Family B — implication rules at confidence 1.00 (4):** S6 ⇒ S12 (support 8),
S6 ⇒ S8 (8), S6 ⇒ S10 (8), S8 ⇒ S12 (10) (source: `analysis/qualitative_analysis.md`
§1 table). The "Consistent (0.88–0.90)" rules are **out of scope** — testing them
was not registered here; any run-time look at them is exploratory and labelled.

**Family C — joint fork (1):** no S9 system carries any of the six partner slots.

Any rule discovered at run time outside this list → exploratory, no confirmatory
claim, reported only in a clearly marked section.

## 4. Data and freezing

- `analysis/slot_matrix.csv`, sha256
  `c29d0234ffb657e3c3bc580816c119bd2c439b721489892383cd671a2c74a6a3`
  — the sole analysis input (25 rows × S1–S14).
- `requisites.csv`, sha256
  `ab501702a4e54bab151859d686bad752e61a3938b809b6b951d07b59990a82cd`
  — context only (marginal sanity check), not an analysis input.
- **Exclusions:** exactly the rows present in the frozen file (n = 25). No system is
  added, dropped, or re-coded. Coding error is out of scope — it is P06-1's separate
  layer, and conclusions here are conditional on the coding as fixed (§10.2).
- **Source of truth:** the matrix. Hand-quoted marginals used as assertions only:
  S9 = 2, S4 = 9, S6 = 8, S7 = 9, S8 = 10, S10 = 14, S12 = 17, S14 = 11.
- Any hash mismatch at run time, or any re-coding of the matrix between registration
  and run, requires an amendment **before** the analysis executes (§8, §9).

## 5. Null models (pre-specified)

**5.1 Primary — independent placement, fixed margins.**

- Family A: one-sided Fisher exact test of depletion (alternative: fewer S9∩partner
  systems than independence predicts); the two-sided p is also reported, descriptive.
- Family B: one-sided Fisher exact test of enrichment (alternative: the antecedent
  slot appears with the consequent more often than independence predicts).
- Family C: exact enumeration over all C(25,2) = 300 placements of the S9 pair;
  statistic T (§2, R2); p = fraction of placements with T = 0. **The p floor is
  1/300 ≈ 0.0033** — results are reported as "p = k/300", never as "p < 0.001".

**5.2 Secondary — tradition-blocked permutation.**

Blocks are the root README's §Coverage grouping of the systems (list written at
v1.1, 2026-10-06, before this session), restricted to the 25 slot-coded systems,
**without consulting any slot value**, frozen in `tradition_blocks.csv` (committed
with this registration) *before* any statistic is computed: Europe & EU {DE, FR,
EU} · North America {UN, HN} · Latin America {BR} · Africa {SN, BJ, NG, KE, ET, WA} ·
Middle East {IS, SA, AE} · South & East Asia {IN, CN, JP, VN, TH, ID} · Post-Soviet
{UA, SU} · Baltic-digital {EE} · Andean {PE}. (HN = Haudenosaunee wampum and
PE = Inka khipu, per `requisites.csv` — both sit in the frozen matrix as boundary
rows.) Slots are permuted within blocks: exact enumeration where block sizes
permit, otherwise Monte Carlo with 100,000 draws, seed 20261015. Same tests, same
corrections, same families, clearly labelled secondary.

**Verdicts follow the primary null.** If primary and secondary disagree, the
disagreement *is* the reported result — no choosing between them, no silent
substitution.

## 6. Analysis plan (locked)

1. **Assertions first.** Load the frozen matrix, re-derive every margin, assert
   equality with §4's eight quoted counts; assert row count = 25 and column set =
   S1…S14. Failure → stop, drift report, amendment (never a silent fix).
2. **Family A:** per-edge one-sided depletion p; Benjamini–Hochberg at α = 0.05
   across the 6 edges; two-sided p and Haldane-corrected odds ratio (observed vs
   expected overlap) reported beside each.
3. **Family B:** per-rule one-sided enrichment p; BH at α = 0.05 across the 4 rules;
   support proportions and corrected OR reported.
4. **Family C:** single exact test at α = 0.05, declared its own family of one —
   no correction across families A/B/C.
5. **Secondary null:** §5.2 repeated for all families, labelled secondary, same
   corrections. **Dependence sensitivity:** Benjamini–Yekutieli q-values reported
   alongside BH for families A and B (the edges share the S9 vector; the rules share
   S6/S8), since BH's guarantee assumes independence or positive dependence.
6. **Informativeness thresholds n* (deterministic, no simulation):** for each
   family-A edge, the smallest N ≥ 25 at which continued zero overlap, with margins
   scaled at the current proportions (S9 at 2/25, partner at its marginal), yields
   one-sided exact p < 0.05; for each family-B rule, the smallest N at which
   continued full support at scaled margins yields one-sided enrichment p < 0.05.
   These are per-edge α = 0.05 thresholds, **not** multiplicity-adjusted — stated as
   such wherever quoted.
7. **Reporting:** every claim in §3 gets a row: observed statistic, primary p, BH q,
   BY q, blocked p, n*, and the §7 label — regardless of how it looks.
8. **No model selection, no alternative marginals, no dropped edges.** The plan
   above is the whole confirmatory analysis.

## 7. Decision rules

| outcome | rule |
|---|---|
| Family C rejects (p < 0.05) | fork **regraded**: "supported as one joint population-level pattern", replacing the six-census-facts framing in a later repo version (amendment logged) |
| Family C fails to reject | fork reported **descriptive only**; R2 disconfirmed; headline findings 1–2 amended (amendment logged); no inferential language kept |
| Family A edge, BH q < 0.05 | edge "individually surprising (depletion)" — R1 loses by one edge per rejection |
| Family A edge, BH q ≥ 0.05 | edge "individually unsurprising" at current n; n* carries the informativeness statement |
| Family B rule, BH q < 0.05 | rule **regraded inference-supported**; else **census-only** |
| R1–R4 | scored supported/not-supported exactly as registered in §2, printed in the results header whichever way they fall |
| blocked vs primary disagreement | both reported, verdicts follow primary, disagreement discussed as the finding (§5.2) |

Verdicts are three-valued: supported / regraded / inconclusive. An inconclusive
outcome is reported as inconclusive; nothing is rounded into a verdict.

## 8. Contingencies (pre-specified responses)

| contingency | response |
|---|---|
| margin assertion fails (§6.1) | stop; report prose-vs-data drift; amendment before any test |
| file hash mismatch at run time | stop; amendment before any test |
| tradition blocks cannot be built from `diversity.md` without consulting slot values | secondary null reported as **not run**, reason logged; primary unaffected; no substitute blocks invented after seeing data |
| joint-test p floor binds (k/300 = smallest attainable) | quote as "p = k/300"; floor stated next to every family-C number |
| BH dependence concern | BY q-values already in §6.5 — reported, not a post-hoc rescue |
| a family-B rule's consequent margin makes exact p impossible at α after BH | rule reported "not testable at current margins" with n*; never reported as confirmed |
| P06-1 later shows non-trivial coding error | conclusions re-issued as provisional on fixed coding; this audit is never silently re-run on re-coded data |

## 9. Deviations

Same four elements as the house rule (`experiment/PREREGISTRATION.md` §9): what
changed, why, effect on severity of the test, effect on validity. Registered and
deviated analyses reported side by side; the registered one is never replaced.
Deviation log created at promotion (e.g. `audit/DEVIATIONS.md`). Deviations so far:
none — this document has not yet been registered or run.

## 10. Limitations declared in advance

1. **Convenience corpus.** 25 systems selected by the atlas's own sampling frame,
   itself shaped by open-web retrievability (P08-5's concern). Inference is
   conditional on that frame; "the population of written official-document regimes"
   is a working scope, not a sampling frame. Population language in any write-up is
   scoped accordingly (the reviewer's condition on P06-2).
2. **Coding treated as fixed.** The audit cannot distinguish a real pattern from a
   systematic coding convention; that is P06-1's layer, and the two interact.
3. **Hand-assigned tradition blocks** (secondary null only) come from prose
   groupings, not from an independent taxonomy; they are frozen before computation
   to prevent tuning, not to become ground truth.
4. **Dependence among tests** within families (shared S9 vector, shared S6/S8);
   BH plus BY both reported.
5. **p floor at n = 25** limits how surprising anything can look (family C:
   granularity 1/300).
6. **Exchangeability under the primary null is a working fiction** — traditions
   cluster, which is exactly why the blocked null exists. Disagreement between nulls
   is expected to be informative.
7. **Prior art.** Exact/permutation nulls for typological co-occurrence are
   established (E02, challenge-located); novelty is claimed at application level
   only. Absence of a located prior application is not evidence that none exists —
   the bounded search is recorded in `raw/evidence_E02.md`.
8. **No external registry; analyst = code author.** A git commit is auditable but
   not a third-party timestamp. Anyone rerunning the scripts has everything needed
   to check the analysis independently.
9. **Statistical surprise is not mechanism.** A rejecting result says the pattern is
   unlikely under a null, not why chanceries converged; historical explanation stays
   in the prose layer of the atlas.