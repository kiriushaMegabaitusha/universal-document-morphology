# Results — B1 wave 2: the nine post-check ideas

**Date 2026-10-28.** Protocol frozen before any score (`PROTOCOL.md`). Four
independent raters, separate sessions, blind to each other and to wave 1.
Seven ideas rated; two excluded as already executed. **Decision: null** — the
matrix is a decision aid, the owner selects.

## Scores

Formula as wave 1: `100 · Σ wᵢ(cᵢ − 1) / (4 · Σ wᵢ)`, weights 3/3/2/2/1. Median
central per criterion, lower-middle for the even rater count.

| rank | idea | score | info | feas | rigor | syn | cover | rater spread | rank range under ±10 % weight perturbation |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | **P09-1** vocabulary re-induction | **79.5** | 4 | 5 | 4 | 5 | 1 | 1 | **1–1** |
| 2 | P10-1 load-bearing-cell adjudication | 72.7 | 4 | 4 | 4 | 5 | 1 | 1 | 2–3 |
| 3 | P10-3 cheapest-bin-first fork falsification | 72.7 | 5 | 2 | 4 | 5 | 4 | 1 | 2–4 |
| 4 | P11-2 sensitivity gate before register nulls | 72.7 | 3 | 5 | 4 | 5 | 1 | 1 | 2–4 |
| 5 | P11-1 vocabulary bounds + open extraction | 68.2 | 4 | 3 | 4 | 5 | 2 | 1 | 5–5 |
| 6 | P10-2 one registered specification curve | 65.9 | 3 | 4 | 4 | 5 | 1 | 1 | 6–6 |
| 7 | P09-3 universality as compulsion | 63.6 | 3 | 5 | 3 | 4 | 1 | 1 | 7–7 |

**Ranks 2–4 are a tie class, not an ordering.** All three score 72.7 and two of
them (P10-3, P11-2) move between ranks 2 and 4 under a single-weight perturbation.
Only rank 1 is stable under every one-at-a-time perturbation, and ranks 5–7 are
stable in place.

**Rater agreement.** No criterion on any idea had a central spread of more than 1
point. Individual top picks split: R01 and R02 put P09-1 first; R03 put P10-3
first; R04 put P11-2 first. The aggregate rank 1 is therefore not a consensus
preference but a weighted consequence of four similar profiles — the same caveat
as wave 1, and the reason scores are aids, not evidence.

## What the raters converged on

- **P09-1** is the cheapest idea that attacks the assumption every other audit
  conditions on — whether the 14 slots are recovered from the requisites or
  imposed by the codebook. All four raters liked the S6/S9 by-product; all four
  flagged the same weakness: glosses and labels were written by the same analyst.
- **P10-1** was rated among the most rigorous in the set (median 4, one rater 5)
  and the most directly decision-relevant: it returns per-claim
  decidable/undecidable verdicts before any null. Its cost was judged higher than
  the idea assumes (three to four weeks, not one).
- **P10-3** was the only idea rated 5 on information gain by three of four raters,
  and the only one that generates evidence the frozen corpus cannot produce. Its
  feasibility (2) is what holds it to the tie class: three sourcing campaigns.
- **P11-2** is the cheapest item in the wave and the only one that supplies a
  failure condition for an equivalence verdict already printed. Its gain is capped
  because a corruption control is not a register-shaped control, and because the
  human arm is paused.

## Evidence check (top three only, bounded)

`P09-1` — **challenge-located.** Unsupervised clustering used to validate an
existing typology, scored with the corrected Rand index, is published prior art
(Despeyroux et al., *Experiments in Clustering Homogeneous XML Documents to
Validate an Existing Typology*, arXiv cs/0507024, 2005; ARI stability as model
selection is standard in a 2026 *Phil. Trans. R. Soc. A* review). The contribution
would be the application — a document-slot ontology — not the instrument.

`P10-1` — **not located.** A bounded search found the adjacent qualitative-coding
reliability literature (inter-coder agreement, single-coder limits) but no direct
prior art for enumerating a claim's load-bearing cells and adjudicating only
those. Absence in a four-query search is not evidence of absence.

`P10-3` — **support-located.** Diplomatics supports the directional prediction:
letters patent carry a general address together with arenga/narratio/dispositio,
and in Iranian farmāns "at least as early as the Timurids, the mention of the
addressee and the beneficiaries were integrated into the arenga" (Encyclopaedia
Iranica, *Farmān*). The predicted S6+S9 co-occurrence in pre-modern instruments is
documented, so the test is a real falsification attempt rather than a fishing trip.
`P11-1`, `P10-2`, `P09-3`, `P11-2` — **not-checked** (protocol §5 limits the check
to the top three).

Sources: arXiv cs/0507024; Royal Society *Phil. Trans. A* (2026) unsupervised-ML
review; Encyclopaedia Iranica "Farmān"; *Diplomatics* (Duranti) and the Britannica
diplomatics entry for letters patent. Queries and limits are recorded in this file;
no full texts beyond abstracts/excerpts were read.

## Decision-relevant reading (not a selection)

The wave does not pick a winner; it makes the trade-off visible:

- **P09-1** is the only stable rank 1 and the cheapest high-synergy test, but its
  method is prior art and its positive result is partly uninterpretable because of
  the gloss/label circularity. Its value is asymmetric: a null is very informative,
  a positive is weak.
- **P10-3** is the only idea that adds new evidence and the only one whose
  prediction the literature already supports, which makes a survival genuinely
  surprising. It is also the only one that costs a retrieval campaign.
- **P10-1** is the strongest governance move: it decides which existing claims are
  decidable at all, before any further statistics.
- **P11-2** is nearly free but its payoff is currently moot while the human arm is
  paused.

If the owner wants a sequence rather than a single choice, the evidence supports
P10-1 (which claims are decidable) → P09-1 (is the vocabulary recoverable) →
P10-3 (out-of-sample, if retrieval capacity exists). That is a reading of the
matrix, not a decision, and the decision is recorded in `DECISION_LOG.md` only if
the owner makes one.

## Gates and limitations

- No ethics gate applies to any rated idea; none uses human, community or
  Indigenous data, and none clears the P03-1 / P08-1 / P08-2 / P04-3 gates.
- Four AI raters, no human expertise: consensus is not evidence.
- Seven items, two resolved ideas excluded; status was frozen by the facilitator
  before rating and is auditable in `PROTOCOL.md` §1.
- No adversarial review was run in this wave. If an idea is selected, the wave-1
  practice (non-originator adversarial review before any registration) should be
  applied to it.
