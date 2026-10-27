# Project plan — single source of truth

**Updated: 2026-10-27 · Owner: Kyrylo Yasuda · Atlas version: 1.3.**

This file is the **plan**: what the project is trying to establish, what is
finished, what is live, what comes next, and what is waiting on a decision. It is
deliberately short on quoted numbers — those live in the data, the gates and the
results files, and are not repeated here where they could drift.

It does **not** replace the evidence, the pre-registrations or the results. It
tells you which of those is authoritative when they disagree.

---

## 1. Precedence — which document wins

Read from the top down; a lower tier never overrides a higher one.

| tier | what it settles | authoritative files |
|---|---|---|
| 1 | **the corpus and the claims** | `requisites.csv`, `ledger.json`, `sources/`, `analysis/*.csv` |
| 2 | **what a study promised** | `experiment/PREREGISTRATION.md`, `audit/PREREGISTRATION.md`, both `DEVIATIONS.md` |
| 3 | **what actually happened** | `experiment/results/`, `audit/RESULTS.md`, `audit/results.json` |
| 4 | **status, order of work, open decisions** | this file |
| 5 | **interpretation and narrative** | `README.md`, `morphology.md`, `diversity.md`, `STANDARDS.md`, `EXECUTIVE_SUMMARY.md`, `cases/` |

If tier 5 contradicts tier 1–4, the prose is wrong and gets corrected; if tier 2
is contradicted by tier 3, the departure must already be in a `DEVIATIONS.md`,
and both analyses are reported side by side. The registered analysis is never
replaced. A change to a registered study is an amendment, not an edit.

**Verification is a command, not an opinion:**

```bash
python3 check_claims.py                  # corpus + ledger + citations in *.md
python3 analysis/recompute.py --check    # derived figures vs prose
python3 experiment/check_stimuli.py      # stimuli + answer key + manipulation
python3 audit/null_audit.py --self-test  # audit pipeline on synthetic data only
```

`python3 audit/null_audit.py` (no flag) is the **registered one-shot analysis**.
It rewrites `audit/results.json`; run it only to re-run the registered study, and
only under a logged amendment.

---

## 2. What the programme is

One question, stated at `README.md` §Question: is there a structure that official
documents share because it is *required*, or is their form just accumulated
tradition — and is any of it demonstrably the more efficient carrier of official
information?

The working answer is a scoped one: a convergent deep grammar of identity, origin,
date, body, authentication and annex; divergence concentrated in the surface and
driven more by **genre** than by nation; universality explained by legal validity,
attribution and procedure — **not** by measured comprehension efficiency; and the
claim bounded to the written official document (the khipu and wampum cases mark
the boundary). The narrative is in `morphology.md`; the evidence is in the tier-1
files.

Two things would move the project's position: a **better inference about the
structural regularities** (the audit track) and a **measurement of comprehension**
(the experiment track). Both have been designed; one has been run. That is the
whole plan.

---

## 3. Current state

| id | workstream | state | pointer | next action |
|---|---|---|---|---|
| W0 | Comparative atlas, v1.4 | **frozen** | `README.md` | maintenance only (see §5) |
| W1 | P06-2 exact-null audit of the structural rules | **closed** | `audit/RESULTS.md` | none — do not re-run |
| W2 | Finding-5 comprehension test, human arm | **paused — owner decision, 2026-10-27** | `experiment/PREREGISTRATION.md` | none; runbook retained in §4, no collection |
| W3 | Forward agenda from the ideation session | **parked** | `brainstorm/DECISION_LOG.md` | on trigger only (§5) |

Closed means: registered before data, run once, deviations logged, results
committed, and the atlas prose amended where the registered decision rule required
it (README v1.3–v1.4). Nothing in W0 or W1 is reopened without a new registration.

**Consequence of pausing W2 (recorded, not softened).** Finding 5 stays
**unmeasured**. There are no human data and none are being collected; the machine
arm is registered as exploratory and cannot stand in for comprehension
(`experiment/PREREGISTRATION.md` §7, §10.6). The atlas's claim therefore remains
the negative, evidence-based one it already states — no standard optimises for
comprehension — rather than an empirical comparison of registers. Any future
write-up must say "untested in people", not "tested and found equivalent".

---

## 4. Dormant workstream — W2, the human arm (paused)

**Status: paused by owner decision, 2026-10-27. No participant will be recruited
and no collection will run for now.** The design, instrument and recruitment pack
are complete and stay as they are, so the arm can restart without redesign; this
section is the runbook, not an active task list.

Reopening requires only an owner decision to collect — no new registration, because
the existing one is unchanged and has never been used to collect data.

**Objective (if reopened).** Test finding 5 empirically: does the *same* obligation,
rendered in formal versus plain register, yield different comprehension? The machine
arm is exploratory only and can never answer this (a language model has no
comprehension to measure); the human arm is the confirmatory test.

**Definition of done** — all six, in this order:

1. **N ≥ 20 complete sessions** scored; target N = 36. Below 20 the arm is reported
   as exploratory by the registered rule, and H1 is not tested confirmatorily.
2. All pre-registered exclusions applied before analysis (completeness, duration,
   attempted-the-questions, language match), and the count of excluded sessions
   reported.
3. `experiment/score_human.py` run on `experiment/exports/`; correctness recomputed
   from `stimuli.json`, never trusted from the client.
4. `experiment/results/HUMAN_RESULTS.md` written with the pre-registered verdict —
   **supported / falsified / inconclusive** — plus the estimate and CI, the TOST
   result, the exposure-robustness check and the secondary family.
5. Any departure from `experiment/PREREGISTRATION.md` §3–§7 entered in
   `experiment/DEVIATIONS.md` with the four house elements (what, why, severity,
   validity).
6. Tier-5 prose updated to match the verdict, or explicitly left unchanged with
   the reason stated.

**Steps.**

- [ ] Confirm whether the institution requires ethics review for this use; if so,
      obtain it before the first participant (the prereg declares no approval).
- [ ] Send the invitation and `experiment/human_survey.html` — **never** name the
      formal-vs-plain manipulation (see `experiment/recruitment/README.md`).
- [ ] Collect returned JSON into `experiment/exports/`; log each session in
      `experiment/exports/MANIFEST.csv`.
- [ ] Send the debrief only after the file comes back.
- [ ] Open a two-week collection window; stop at N = 36 or at the window's end.
- [ ] Score with `python3 experiment/score_human.py --dir experiment/exports/ --min-n 20`.
- [ ] Write the results, log deviations, update this file's status table.

**Do not, during collection:** edit `stimuli.json` or `human_survey.html` (both are
registration material; regenerate the instrument from the stimuli if it must
change, and log it), reveal the manipulation, or discuss the task content between
participants.

**Risks and registered responses.**

| risk | response (pre-specified) |
|---|---|
| under-recruitment (< 20) | report as exploratory, do not test H1 confirmatorily, report achieved MDE |
| manipulation check fails in one language | report the failure, restrict the claim to the language where it held, no mechanism claim |
| > 15 % of sessions excluded for one reason | report the exclusion analysis and both analyses, with and without |
| item set also near ceiling for people | the registered MDE is the limit; report inconclusive rather than over-reading |
| experimenter wrote the stimuli | cross-arm agreement reported as mitigation, never as confirmatory for H1 |
| register is visible to participants | bounded by unlabelled conditions and answerable-from-document items; declared as limitation |

The full list is `experiment/PREREGISTRATION.md` §10 and must be repeated in any
write-up.

---

## 5. Backlog — parked, each with a trigger

Nothing here starts without its trigger. Order is a recommendation, not a queue.

| item | what | trigger |
|---|---|---|
| B6 | Documentation corrections: stale item counts in `experiment/PREREGISTRATION.md` §3; stale status line in `brainstorm/RESULTS.md`; `EXECUTIVE_SUMMARY.md` version header | **done 2026-10-27** — logged as Erratum 2 in `experiment/DEVIATIONS.md`; gates pass |
| B3 | Inference follow-ons on frozen data: lineage-restricted re-derivation, prevalence bounds, compelled-requisites robustness, spec curve | **closed 2026-10-27** — `lineage/RESULTS.md`. Stem not lineage-universal (0/6), no descent clustering (p = 0.52), authentication rank 1, mandatory-only fork p = 0.24. Regrade done in v1.4 (D6) |
| B1 | Rating wave for the 9 unrated post-check ideas (`brainstorm/RESULTS.md`, `P09`–`P11`) | owner requests the wave; criteria frozen first |
| B2 | Human-arm follow-up: wider item sample, or a design without double exposure | blocked while W2 is paused; after W2 reports, and only as a new registration |
| B4 | P03-1 (human subjects), P04-3 (licence/retrieval probe) | gate cleared: ethics determination, licence probe |
| B5 | P08-1, P08-2 (community/Indigenous record heritage) | external community/subject-matter authorisation |

**With W2 paused, the project has no active confirmatory workstream.** The next
substantive step is B3, which exists as a drafted pre-registration awaiting the
owner's approval; it becomes active only when registered. B1 (rating wave) remains
the alternative and is still unfrozen.

**Documentation-only maintenance to W0** is always allowed and needs no
registration: fixing a wrong cross-reference, a stale filename, a header that
misstates the version. It must not touch data, claims, figures, the slot
vocabulary, or a registered document's substance. B6 is that class of work.

---

## 6. Standing rules (non-negotiable)

1. **Register before you look.** Any confirmatory analysis is written down, with
   its null, decision rule and SESOI, before a statistic is computed.
2. **Run once, report both.** A registered analysis runs once; every departure is
   logged with what/why/severity/validity, and the registered result is never
   replaced.
3. **Never invent evidence.** No source, URL, claim, citation or requisite is
   created to satisfy a gate. Unretrieved material stays labelled provisional.
4. **Generated files are not hand-edited** — `analysis/slot_matrix.csv`,
   `slot_similarity.csv`, `evidence_base.csv`, `experiment/human_survey.html`,
   `posters/*`. Change the input and regenerate.
5. **Pinned inputs stay pinned.** The audit's hashes and margins change only under
   a logged amendment, never a hash refresh.
6. **Scope the claim.** The corpus is a convenience frame, not a random sample;
   machine results are exploratory; "efficiency" is measured nowhere in the
   standards.
7. **The gate decides.** If `check_claims.py` or `recompute.py --check` fails, the
   work is not done — fix the data or the prose, never the test.

---

## 7. Open decisions for the owner

| id | decision | state / default |
|---|---|---|
| D1 | Human arm: collect or not | **DECIDED 2026-10-27 — do not collect; W2 paused.** No participants recruited; the runbook stays ready if reopened |
| D2 | Request the rating wave for the 9 unrated ideas (B1) | open; they stay candidates and the rating round stays frozen until you ask |
| D3 | Pursue the three gate clearances (B4, B5) | open; those ideas stay paused, not rejected |
| D4 | Whether a future human study needs external registration (OSF) | open, and moot while W2 is paused |
| D5 | Next substantive track after B6: B3 (inference follow-ons) or B1 (rating wave) | **B3 registered and run** (`lineage/RESULTS.md`); B1 stays unfrozen |
| D6 | Regrade the atlas prose after B3: R1 failed, so §8 requires "universal stem" → "system-level majority, lineage-conditional", plus the S12 majority-claim wording | **done 2026-10-28** — atlas v1.4: stem regraded across `README.md`, `morphology.md`, `EXECUTIVE_SUMMARY.md`, `analysis/findings.md`, `diversity.md`; no data, claim or checked figure changed |

---

## 8. Plan maintenance

- Update this file **in the same commit** as the status change it describes. A
  status that exists only in a chat message does not exist.
- A row moves between states in §3 only with a pointer to the artifact that proves
  it (commit hash, results file, gate output).
- Do not paste derived figures here; link to the file that the gate checks.
- This file is independent of the atlas version. Documentation-only changes to it
  do not bump `README.md`'s version history.

**Plan changelog**

| date | change |
|---|---|
| 2026-10-27 | created: consolidated status, precedence, active workstream, backlog, rules and open decisions from `README.md`, both pre-registrations, `audit/RESULTS.md`, `experiment/README.md` and `brainstorm/DECISION_LOG.md`; no data, claim or registered document altered |
| 2026-10-27 | D1 recorded: human arm **paused by owner decision**, no collection. W2 moved out of active, its consequence (finding 5 stays unmeasured) stated, backlog re-prioritised (B6 actionable now, B3/B1 awaiting D5); experiment status doc and README honest-gap pointer aligned |
| 2026-10-27 | **B6 done**: stale v1 item counts corrected in the experiment preregistration (logged as Erratum 2, including the `max_exact` open condition), stale P06-2 status corrected in `brainstorm/RESULTS.md`, `EXECUTIVE_SUMMARY.md` header aligned to v1.3. **B3 drafted** (`brainstorm/B3_PREREGISTRATION_DRAFT.md`), awaiting approval; no statistic computed |
| 2026-10-27 | **B3 promotion, step 1–2**: bounded literature check run and recorded (`brainstorm/raw/evidence_B3.md`, challenge-located); lineage table coded with one citation per documented edge (`brainstorm/lineage_blocks_PROVISIONAL.csv`). Evidence check forced Revision 1 (transmission clusters not a tree; JP to broad; WA settled as non-Islamicate; variant rule rewritten: 19/18/12 blocks). No test statistic computed; nothing committed |
| 2026-10-27 | **B3 promotion, step 3–4**: analysis code written and self-tested (`lineage/lineage_audit.py --self-test`); derived input frozen (`lineage/mandatory_only.csv`, with HN and PE empty and kept); Revision 2 recorded (holdout reduced to prevalence vs lineage, genre rule not computable). Registration commit not made; real matrix never read for analysis |
| 2026-10-27 | **B3 registered** at the commit that adds `lineage/` together with `PREREGISTRATION.md` and `DEVIATIONS.md`; not yet run at the time of the commit. `PLAN.md` and the B6 corrections committed in the same session |
| 2026-10-27 | **B3 run once and closed** (`bfd6ffc` registration; no deviations): stem not lineage-universal (0/6 under both readings), no descent clustering (base p = 0.518, T = −0.062), authentication rank 1 (13/18 lineages), fork not lineage-universal (2/18), mandatory-only fork p = 6/25, lineage holdout worse than prevalence. **Regrade of the atlas prose now required (D6)** |
| 2026-10-28 | **D6 done — atlas v1.4**: stem regraded to system-level, lineage-conditional in `README.md`, `morphology.md`, `EXECUTIVE_SUMMARY.md`, `analysis/findings.md` and `diversity.md`; authentication becomes "highest-ranked", not "most universal", with its interval quoted. Claim language only: all 28 checked figures and the gate outputs unchanged |
