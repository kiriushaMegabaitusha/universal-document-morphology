#!/usr/bin/env python3
"""Headless end-to-end test of human_survey.html (development harness, not data).

Drives the generated instrument in a real Chromium and checks the things that have
broken or could break:

  1. the language switch on the intro re-renders the page in the chosen language
     (it did not: the radio toggled and the text stayed Ukrainian);
  2. the skip control is a working toggle - it visibly marks the question, clears a
     chosen answer, and reverts when an answer is chosen again (it used to be a
     no-op that could not be undone);
  3. a full session: 12 screens, 3 questions each, both registers of every
     obligation, and the two registers of an obligation never adjacent;
  4. the export parses and carries every field the scorer needs.

The participant record it writes is a MACHINE-GENERATED FIXTURE, not a human
response: results/TEST_participant_NOT_DATA.json. It must never be pooled into an
analysis - score_human.py --fixture exists to keep that promise.

Requires playwright (pip --user) with a chromium browser:
  PLAYWRIGHT_BROWSERS_PATH=~/.cache/ms-playwright python3 experiment/test_survey_headless.py
"""
import json
import os
import sys

try:
    from playwright.sync_api import sync_playwright
except ImportError:  # pragma: no cover
    print("playwright not installed - skipping (this is a dev harness)")
    sys.exit(0)

HERE = os.path.dirname(os.path.abspath(__file__))
SURVEY = "file://" + os.path.join(HERE, "human_survey.html")
FIXTURE = os.path.join(HERE, "results", "TEST_participant_NOT_DATA.json")
MIN_SEPARATION = 4


def main():
    stim = json.load(open(os.path.join(HERE, "stimuli.json"), encoding="utf-8"))
    n_screens = len(stim["documents"]) * 2
    items_per_doc = len(stim["documents"][0]["items"])
    n_trials = n_screens * items_per_doc

    errors, console, checks = [], [], []

    def check(label, ok):
        checks.append((label, bool(ok)))
        if not ok:
            errors.append(label)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.on("console", lambda m: console.append("%s: %s" % (m.type, m.text)))
        page.on("pageerror", lambda e: errors.append("pageerror: %s" % e))
        page.goto(SURVEY)

        # --- 1. language switch re-renders ---------------------------------
        uk_h1 = page.inner_text("h1")
        page.check("#lang_en")
        page.wait_for_timeout(120)
        en_h1 = page.inner_text("h1")
        check("language switch re-renders the intro (uk -> en)",
              "Understanding official documents" in en_h1 and en_h1 != uk_h1)
        check("exactly one language radio is checked",
              page.locator("input[name=lang]:checked").count() == 1)
        page.check("#lang_uk")
        page.wait_for_timeout(120)
        check("language switch back to uk", "Розуміння офіційних документів" in page.inner_text("h1"))

        page.click("#start")
        check("start shows a document screen", page.locator("#next").count() == 1)

        # --- 2. skip control behaves as a toggle ---------------------------
        first_fs = page.locator("fieldset").first
        first_fs.locator("input[type=radio]").first.check()          # choose an answer
        skip_btn = first_fs.locator("button.skip")
        check("skip starts unarmed", "пропустити" in skip_btn.inner_text())
        skip_btn.click()
        page.wait_for_timeout(60)
        check("skip clears the chosen answer", first_fs.locator("input[type=radio]:checked").count() == 0)
        check("skip relabels itself", "повернутися" in skip_btn.inner_text())
        first_fs.locator("input[type=radio]").first.check()          # answer again
        page.wait_for_timeout(60)
        check("choosing an answer disarms skip", "пропустити" in skip_btn.inner_text())

        # --- 3. full session ----------------------------------------------
        screens = 0
        bad_screens = []
        while page.locator("#next").count() == 1:
            screens += 1
            if page.locator("fieldset").count() != items_per_doc:
                bad_screens.append(screens)
            assert len(page.locator("div.doc").inner_text().strip()) > 40, "empty document text"
            for fs in page.locator("fieldset").all():
                fs.locator("input[type=radio]").first.check()
            page.locator("input[name^=conf_]").first.check()
            page.click("#next")
            assert screens <= n_screens, "more than %d screens: loop is not terminating" % n_screens
        check("every screen shows %d questions (bad: %s)" % (items_per_doc, bad_screens or "none"),
              not bad_screens)

        page.wait_for_selector("#dl")
        blob = page.locator("textarea").input_value()
        data = json.loads(blob)
        page.screenshot(path=os.path.join(HERE, "results", "survey_test_done.png"), full_page=True)
        browser.close()

    # --- 4. the export -----------------------------------------------------
    check("%d screens" % n_screens, screens == n_screens)
    check("%d trials" % n_trials, len(data["trials"]) == n_trials)
    check("%d attempted" % n_trials, data["n_attempted"] == n_trials)
    check("language recorded", data["lang"] in ("uk", "en"))
    regs = {t["register"] for t in data["trials"]}
    docs = {t["document"] for t in data["trials"]}
    check("both registers present", regs == {"formal", "plain"})
    check("all 6 obligations present", len(docs) == 6)
    need = {"item", "document", "register", "lang", "kind", "response", "correct",
            "keyed", "skipped", "position", "pair_pos", "rt_ms", "confidence"}
    missing = [t["item"] for t in data["trials"] if not need <= set(t)]
    check("every trial carries all fields (missing: %s)" % (missing or "none"), not missing)
    # every obligation appears exactly twice, once per register
    per = {}
    for t in data["trials"]:
        per.setdefault(t["document"], set()).add(t["register"])
    check("each obligation read in both registers",
          all(v == {"formal", "plain"} for v in per.values()))
    # the pair is never adjacent
    pos = {}
    for t in data["trials"]:
        pos[(t["document"], t["register"])] = t["position"]
    gaps = [abs(pos[(d, "formal")] - pos[(d, "plain")]) for d in per]
    check("registers of an obligation are >= %d screens apart (min gap %d)"
          % (MIN_SEPARATION, min(gaps)), min(gaps) >= MIN_SEPARATION)
    check("positions are 1..%d" % n_screens, sorted({t["position"] for t in data["trials"]}) == list(range(1, n_screens + 1)))

    os.makedirs(os.path.dirname(FIXTURE), exist_ok=True)
    with open(FIXTURE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    print("instrument checks (%d):" % len(checks))
    for label, ok in checks:
        print("  %-58s %s" % (label, "ok" if ok else "FAIL"))
    print("wrote fixture (NOT DATA): %s" % os.path.relpath(FIXTURE, os.path.dirname(HERE)))
    if console:
        print("console:", console[:5])
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
