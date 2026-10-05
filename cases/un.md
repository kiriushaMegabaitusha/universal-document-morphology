# Case: United Nations

Two mechanisms: the **document symbol** (identification) and the
**resolution grammar** (the act).

## The document symbol

Every UN document carries a unique symbol; all language versions share it. The
symbol's components are *meaningful*: the first indicates the organ (A/- General
Assembly, S/- Security Council, E/- ECOSOC, ST/- Secretariat), later components
indicate subsidiary bodies, series and number; some bodies have special symbols
(CRC/C/-, DP/-, UNEP/-). The symbol generally does **not** encode the topic
[S-UNSYM, C11]. This is a fully decomposed identifier grammar — the opposite
design from DIN 5008's indifference.

## The resolution grammar

The UN Editorial Manual fixes the order of a resolution's component elements
exactly [S-UNRES, C12]:

> (a) the name of the organ; (b) the preamble, if any; (c) the operative part.

- Each **preambular** paragraph begins with a present, past or perfect
  participle or participial phrase or an adjective.
- Each **operative** paragraph begins with an operative verb (or phrase) in
  the present indicative tense; operative paragraphs are numbered, preambular
  ones are not.
- The text is followed by the meeting and the date of adoption (e.g. "82nd
  plenary meeting, 29 November 1979").

So the *morphology is enforced grammatically*: the part-of-speech of a
paragraph's first word tells you whether it justifies (S9) or commands (S11).
That is the sharpest formalisation of the preamble/dispositif distinction in
the sample.

## Slot profile

S1 ● · S2 ● (symbol) · S3 ● (name of organ) · S4 ● (masthead) · S5 ● (date of
adoption) · S6 — (resolutions are erga omnes) · S7 ○ · S8 ● (title; SC
resolutions have none) · S9 ● (preamble) · S10 ○ · S11 ● (operative part) ·
S12 ● (signature) · S13 ● (annexes) · S14 ● (meeting + date of adoption)
