# What does every official document have in common? {#official-documents}

Every operative official document carries a small structural grammar — **identity, origin, date, body, authentication, annex**. That grammar is a **system-level regularity, not a universal**: no stem slot appears in every documented lineage.

- Fourteen slots recur across 28 systems on six continents, c. 1412–2024.
- Genre, not nation, is the main axis of variation: letters and normative acts fill different slots.
- Authentication is the strongest slot: 17 of 25 systems, 13 of 18 lineages.
- A registered lineage audit found no stem slot in every lineage, so the atlas regraded the claim in 2026.

@answer scope="28 systems · 25 with page slots · written official documents · atlas v1.4, 2026-10-28"
@meta locale=en style=editorial
@source atlas title="Universal document morphology — atlas v1.4" url=https://github.com/kiriushaMegabaitusha/universal-document-morphology
@source audit title="P06-2 exact-null audit — results" url=https://github.com/kiriushaMegabaitusha/universal-document-morphology/blob/main/audit/RESULTS.md
@source b3 title="B3 lineage audit — results" url=https://github.com/kiriushaMegabaitusha/universal-document-morphology/blob/main/lineage/RESULTS.md

## What counts as an official document here? {#scope}

A document is a control record: it reconstitutes an action for a reader who was not present when the action happened. What makes it *official* is not the paper, the seal or the letterhead but the attribution chain — who may act, by what competence, in what form.[](source:atlas)

@callout level=note title="The boundary is the written document"
Two non-documentary record systems bound the claim: the Inka khipu (knotted cord) and Haudenosaunee wampum (shell beads). They carry authority without writing, so the atlas treats them as a boundary rather than as failures of the model.

The corpus is a convenience sample of 28 systems, not a random draw from the world's document regimes. Every claim is conditional on that frame, and the atlas says so wherever it makes one.

## What are the fourteen slots? {#slots}

Fourteen functional positions recur. They are not sections of a page: a slot can be carried by layout, by wording, by a stamp, or by a database field.[](source:atlas)

@tree id=slot-tree title="The fourteen slots, grouped by the question they answer"
| root | Official document | - |
| who | Who and where | root |
| when | When | root |
| route | Who it goes to | root |
| act | What it does | root |
| close | How it is guaranteed | root |
| s1 | S1 identity | who |
| s2 | S2 identifier | who |
| s3 | S3 origin | who |
| s4 | S4 authority mark | who |
| s5 | S5 temporal | when |
| s6 | S6 destination | route |
| s7 | S7 reference | route |
| s8 | S8 subject | route |
| s9 | S9 setting | act |
| s10 | S10 body | act |
| s11 | S11 dispositif | act |
| s12 | S12 authentication | close |
| s13 | S13 annex | close |
| s14 | S14 trace | close |

The distinction that matters most is inside "what it does". The **setting** (S9) explains why the act exists; the **dispositif** (S11) is the operative sentence that orders, grants or prohibits. A document can describe a decision without deciding anything, which is why the two are separate slots.

## How common is each slot? {#census}

- **S12 authentication** — 17 of 25
- **S10 body** — 14 of 25
- **S1 identity** — 11 of 25
- **S2 identifier** — 11 of 25
- **S14 trace** — 11 of 25
- **S8 subject** — 10 of 25
- **S4 authority mark** — 9 of 25
- **S7 reference** — 9 of 25
- **S13 annex** — 9 of 25
- **S3 origin** — 8 of 25
- **S5 temporal** — 8 of 25
- **S6 destination** — 8 of 25
- **S11 dispositif** — 4 of 25
- **S9 setting** — 2 of 25

No slot is universal even at this level: the best, authentication, reaches 17 of 25. The rarest are the setting (2 systems) and the dispositif (4) — the two slots that make an act normative.[](source:atlas)

## Why do a letter and a law look different? {#declensions}

The stem splits into two declensions by genre. A letter fills the routing slots and drops the preamble; a normative act does the reverse.[](source:atlas)

| | Letter (epistolary) | Normative act |
| --- | --- | --- |
| Destination (S6) | Filled {good:names a recipient} | Empty |
| Reference (S7) | Filled | Often empty |
| Setting (S9) | Empty | Filled {good:justifies the act} |
| Dispositif (S11) | Rare | Filled {good:orders or grants} |
| Examples | UA letter, DE DIN 5008, CN 信函格式 | UN resolution, EU regulation, UA наказ, CN 命令 |

@callout level=warning title="One joint pattern, not six separate rules"
The census fact is that the preamble never co-occurs with authority mark, addressee, reference, subject, body or trace. The registered audit showed that no individual "never" edge is surprising at 25 systems; each becomes informative only at 44–94 systems. The six together, however, reject independence at exact p = 10/300. Under a tradition-blocked null the joint pattern does not reject (p = 1/3 over six placements). Report it as one population-level pattern, not as six laws.[](source:audit)

## Is the grammar universal? {#universal span=12}

Not in the strict sense. The registered B3 audit re-derived the six stem slots at lineage level, using a table of documented transmission frozen before any statistic.[](source:b3)

| Stem slot | Systems (of 25) → lineages (of 18) |
| --- | --- |
| S1 identity | 11 → 8 |
| S3 origin | 8 → 7 |
| S5 temporal | 8 → 6 |
| S10 body | 14 → 11 |
| S12 authentication | 17 → 13 |
| S13 annex | 9 → 8 |

- **0 of 6** stem slots are present in every lineage, under both the "at least one carrier" and the "every member" reading.[](source:b3)
- **No lineage clustering**: p = 0.518, and within-lineage agreement is slightly *lower* than between-lineage (T = −0.062). Document form does not track the descent lines the atlas documents.
- **Authentication still ranks first** at 13 of 18 lineages, but its 95 % interval (0.465–0.903) does not license "most systems".
- **The preamble appears in 2 of 18 lineages**, consistent with a genre effect rather than a transmitted template.

@callout level=open-question title="So what drives the convergence?"
Not descent: there is no detectable lineage clustering. Not a universal: no stem slot survives de-duplication. Genre, function and instrument type remain candidates, and this study cannot separate them. That is the current frontier, stated as an open question rather than a conclusion.

## How was this established? {#method}

@workflow id=pipeline title="From documents to checked claims"
| corpus | Collect 28 systems | external |
| code | Map 225 requisites | backend |
| ledger | Tie each claim to a source | backend |
| gate | Run the checks | security |
| audit | Test the structural rules | backend |
| regrade | Correct the claim | backend |
| corpus > code | |
| code > ledger | |
| ledger > gate | |
| gate > audit | |
| audit > regrade | |

@facts
| Requisites mapped | 225 |
| Systems | 28 (25 with page slots) |
| Sources retrieved | 60 |
| Claims in the ledger | 92 (88 verified) |
| Registered studies | 2 audits, 1 comprehension test |

Two properties make the claims checkable rather than rhetorical. First, every claim in the ledger points to a retrieved source, and a gate fails the build if a citation does not resolve. Second, the audits were **pre-registered**: the hypotheses, nulls and decision rules were committed before the numbers were computed, and departures are logged.[](source:atlas)

The regrade in this page is the method working. The atlas previously called the stem "universal"; the lineage audit tested that, failed to support it, and the prose was corrected in version 1.4 rather than defended.

## What does this not tell you? {#limits}

- **No standard optimises for efficiency.** None claims its format is the most efficient carrier of official information, and the project has not tested that claim.
- **The machine comprehension test is exploratory.** It says nothing about how people read formal documents.
- **The corpus is a convenience frame.** "The world's documents" is a working scope, not a sample.
- **One system is provisional.** The Russian ГОСТ case rests on blocked primary hosts and is labelled as a placeholder.
- **The sources are not redistributed here.** The public repository omits third-party texts; the ledger keeps their URLs.

@callout level=warning title="Do not quote 17 of 25 as a majority"
The 95 % interval for authentication at system level is 0.465–0.851. The count may be quoted; "most systems" may not, because the lower bound falls below one half.[](source:b3)

## Try it: read a document in six passes {#practice}

Take any official letter, order or certificate you can legally inspect. Work through the passes, and write down what carries each one — a position on the page, a phrase, a stamp, a field.

@workflow id=reading title="Six passes over any official document"
| issuer | Who issued it | external |
| when | When and where | backend |
| to | Who it is for | backend |
| act | What it does | backend |
| auth | Who guarantees it | security |
| trace | Where it has been | backend |
| issuer > when | |
| when > to | |
| to > act | |
| act > auth | |
| auth > trace | |

@steps id=reading-steps
| issuer | Who issued it | Read the letterhead or signature block. Name the office, not just the person; competence is the point. | reading | issuer |
| when | When and where | Separate the date of the act from the date of receipt or registration. They can sit in different slots. | reading | when |
| to | Who it is for | A named addressee signals a letter. A general address signals an act that binds whoever it reaches. | reading | to |
| act | What it does | Find the operative verb: orders, grants, prohibits, records. If you cannot find one, the document may only describe. | reading | act |
| auth | Who guarantees it | Signature, seal, register entry, cryptographic signature: ask which person or office the mark binds. | reading | auth |
| trace | Where it has been | Registration numbers, stamps, filing marks. The trace is often the only evidence the document entered a system. | reading | trace |

## What should you check before quoting this page? {#checklist}

- [ ] The claim is scoped to written official documents, not to record-keeping in general.
- [ ] "Universal" is not used for the stem; the correct phrase is "system-level, lineage-conditional".
- [ ] Authentication is quoted with its interval, not as a majority.
- [ ] Any rule about the fork is described as one joint pattern, not six independent findings.
- [ ] The corpus is described as a convenience frame, and no population claim is made from it.
