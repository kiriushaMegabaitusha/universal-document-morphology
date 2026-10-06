# Recruitment pack

Everything needed to run the human arm, in Ukrainian and English.

    invitation.uk.txt / invitation.en.txt    send with human_survey.html
    debrief.uk.txt / debrief.en.txt          send after the results file comes back

## The one rule that matters

**Do not reveal what the study is about until the participant has finished.** The
invitation deliberately says only that it is about how people read official
documents. Naming the manipulation ("formal vs plain language") before the task
would let participants guess the hypothesis and bias the plain texts upward — the
exact demand-characteristic problem the pre-registration flags as limitation 2.

The debrief explains the design fully. Send it *after* they return their file, not
with the invitation.

## Order of contact

1. Send the invitation plus `experiment/human_survey.html` (one file; they
   double-click it).
2. They finish, press "Download results (JSON)" and send the file back.
3. Send the matching debrief.
4. Log the session in `experiment/exports/MANIFEST.csv` (participant id, date,
   language, usable or not, notes).

## Collection window

Target **N = 36** complete sessions (registered); the pre-registered minimum for a
confirmatory analysis is 20. Two weeks is a sensible window. Ask participants not to
discuss the task content during it — in a convenience sample of students they will
otherwise swap notes between sessions.

## Do not edit the instrument during collection

`human_survey.html` is generated from `stimuli.json` (`python3 experiment/build_survey.py`).
Changing either during collection would break the registration. If a change is
genuinely needed, make it, and record it in `experiment/DEVIATIONS.md` with the four
elements the pre-registration requires.

## Practical notes

- The instrument is keyboard-operable, has no timers, large text and no
  colour-only signals. If a participant needs a different format, tell me rather
  than hand-editing the file.
- If someone cannot open the file, check that they are double-clicking it and not
  opening it inside a code editor; any current browser works, offline.
- If a participant sends a screenshot instead of the file, ask for the file — the
  instrument also shows the JSON in a copyable text box at the end.
- Questions during the task: answer neutrally. Do not say which version they read,
  and do not comment on whether an answer was right.

## Before you collect

Check whether your institution expects ethics review for human-participant
research if this is intended to go beyond coursework. The pre-registration carries
no ethics approval number, and that absence is stated in its limitations; adding
one later is a normal amendment, not a problem.
