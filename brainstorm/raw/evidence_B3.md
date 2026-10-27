# Evidence check — B3 lineage-restricted inference

**Date:** 2026-10-27 · **Status of the idea before this check:** unrated and
unchecked (post-check idea from `brainstorm/RESULTS.md`, P09-2 / P11-3 / P09-3) ·
**Method:** bounded web search, four queries, snippets first; no full texts read
beyond abstracts and search excerpts · **Purpose:** satisfy the promotion
precondition in `brainstorm/B3_PREREGISTRATION_DRAFT.md` §11.1.

**Overall verdict: challenge-located.** The *methods* are mature and easy to find;
no prior application to a document-morphology codebook was located. As with P06-2,
novelty can be claimed only for the application, and this file records that the
search was bounded.

## Queries run

1. `Galton's problem comparative law legal institutions observations not independent`
2. `phylogenetic signal legal origins comparative law cultural traits`
3. `clustered permutation test cultural traits lineages exchangeability`
4. `de-duplication cross-national legal coding descendants independent observations`

## What was located

### Q1 — the independence problem is old and named

- **"Galton's Problem in Cross-National Research"**, *World Politics* (Cambridge
  Core). States the problem exactly as B3 frames it: cases in comparative research
  are not independent because of historical diffusion.
  <https://www.cambridge.org/core/journals/world-politics/article/galtons-problem-in-crossnational-research/3919C49D626707821ABAB3E10CC65158>
- **"Institutional Lineages and Galton's Problem in Comparative Politics"**, APSA
  preprint (2026). Treats regime types as historically related lineages rather than
  independent observations and embeds relatedness in a Bayesian phylogenetic model.
  This is the closest prior *application* located, in a neighbouring field.
  <https://preprints.apsanet.org/engage/api-gateway/apsa/assets/orp/resource/item/69be6936d1922e37d5b3b94f/original/modernization-without-the-end-of-history-institutional-lineages-and-galton-s-problem-in-comparative-politics.pdf>
- JSTOR, **"Galton's Problem: The Logic of Cross-Cultural Analysis"** — the
  cross-cultural-survey statement of the problem.
  <https://www.jstor.org/stable/pdf/40969817.pdf>

### Q2 — signal tests exist, with a power result that matters here

- **Blomberg, Garland & Ives, "Testing for phylogenetic signal in comparative
  data"** (*Evolution*, 2003). A randomization procedure with correct Type I error
  and **power ≈ 0.8 for simulated data with 20 or more species**, plus the K
  statistic for comparing signal across traits.
  <https://pubmed.ncbi.nlm.nih.gov/12778543/>
  *Relevance:* our n = 25 systems, but only ~8–17 lineage blocks. The power result
  is stated per species, not per block, so it cannot be borrowed directly; it is
  grounds for expecting the clustering test to be weak, which is why the
  deterministic analysis is primary.
- **"Permutation tests for comparative data"** (bioRxiv, 2020) — restricted
  permutation as the standard solution to relatedness.
  <https://doi.org/10.1101/2020.10.24.325472>

### Q3 — clustered permutation is standard, with named constraints

- **Winkler et al., "Multi-level block permutation"** (*NeuroImage*; PMC4644991).
  Exchangeability blocks, within-block vs whole-block shuffling, nested designs.
  This is the scheme B3 uses and the reason a naive system-level shuffle is wrong.
  <https://pmc.ncbi.nlm.nih.gov/articles/PMC4644991/>
- **"The Exchangeability Assumption for Permutation Tests"** (arXiv, 2024) — works
  through clustered examples and the permutation counts they imply.
  <https://arxiv.org/html/2406.07756v1>
- **"Comparative Methods for Studying Cultural Trait Evolution: A Simulation
  Study"** (*Cross-Cultural Research*, 2006) — warns that cultural traits travel
  horizontally as well as vertically, so a branching tree is a working fiction.
  <https://doi.org/10.1177/1069397105283401>

### Q4 — legal-family coding is contested, and that bears on Appendix A

- **"Drawing the Legal Family Tree"** (*Journal of Legal Analysis*, 2021; 129
  jurisdictions, 170 binary property-law variables, unsupervised clustering). Finds
  that **East Asian jurisdictions do not form a category of their own**, that
  formerly socialist countries cluster, and that legal-origin labels are a poor
  guide to legal substance. <https://doi.org/10.1093/jla/laaa004>
- **"Do Legal Origins Predict Legal Substance?"** (*JLA*, 2021) — origins predict
  property-law similarity but **do little to predict antitrust**; lineage matters
  by domain, not uniformly. <https://doi.org/10.1086/712420>
- **"Global Legal History, Legal Systemology, and the Genealogy of Law"** (*AJCL*,
  2018) — argues for replacing static legal families with genealogies.
  <https://doi.org/10.1093/ajcl/avy047>
- **Guerriero (2016), dataset of 155 legal transplants** — documents that
  transplanted institutions are frequently modified, so "descendant" does not mean
  "copy". <https://doi.org/10.1016/j.dib.2016.05.049>

## Status by claim

| claim B3 relies on | status | note |
|---|---|---|
| systems are not independent observations | **support-located** | Galton's problem; institutional-lineage work |
| restricted/clustered permutation is the right null | **support-located** | Winkler et al.; exchangeability literature |
| lineage blocks can be coded from transmission evidence | **mixed** | legal-family coding is contested; origins ≠ substance |
| this application is novel | **not located, not established** | bounded search only; nearest neighbour is the APSA preprint |
| a branching tree is an adequate model of transmission | **challenge-located** | horizontal transmission; transplants are modified |

## What the check changed in the draft

1. **Transmission clusters, not a tree.** The method literature says cultural traits
   travel horizontally and transplants get modified. The draft now says "lineage
   block / transmission cluster", never "phylogeny", and §12 states that a partition
   is a coarse stand-in for a graph.
2. **Sinosphere restricted.** `cases/jp.md` says only that seals are used "in the
   Sinosphere"; it does not document Japan adopting a Chinese document format. Japan
   therefore moves out of the base lineage and into the broad variant.
3. **West African Ajami is not Islamicate.** `cases/west_african_ajami.md` says the
   tradition is "neither European nor simply Islamic", which settles the Appendix A
   question against merging it.
4. **Variant rule revised.** The original base/narrow split collapsed once the
   documented edges were actually listed (base would have contained no inferred
   edges). The rule is now: *narrow* = documented edges, contested member as
   singleton; *base* = documented edges with the contested member included;
   *broad* = base plus inferred clusters. All three are reported; the primary
   verdict still follows base.
5. **A citation for expected weakness.** Blomberg et al.'s power result (n ≈ 20
   species) is cited in §12 to justify why the deterministic analysis is primary —
   not borrowed as if it applied to 25 systems in 8–17 blocks.

## Limits of this check

- Snippets and abstracts only; no paywalled full text was read.
- Four queries, one language; non-English scholarship is not covered.
- Absence of a located prior application to a document-morphology codebook is **not**
  evidence that none exists.
- Search date 2026-10-27; sources are cited as URLs, not archived locally.
- No claim here is used to *support* a substantive result. This file exists to keep
  the novelty framing honest and to record that the design changed before
  registration, not after seeing data.
