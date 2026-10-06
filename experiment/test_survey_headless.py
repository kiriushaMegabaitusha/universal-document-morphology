#!/usr/bin/env python3
"""Headless end-to-end test of human_survey.html (development harness, not data).

Drives the generated instrument in a real Chromium: starts a session, reads all 12
documents, answers every question, finishes, and parses the export the participant
would send back. Proves the instrument works, and gives score_human.py a fixture to
run against.

The participant record this writes is a MACHINE-GENERATED FIXTURE, not a human
response. It is written to results/TEST_participant_NOT_DATA.json and must never be
pooled into an analysis.

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


def main():
    errors, console = [], []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page()
        page.on("console", lambda m: console.append("%s: %s" % (m.type, m.text)))
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.goto(SURVEY)

        assert "Розуміння офіційних документів" in page.inner_text("h1"), "intro missing"
        assert page.locator("#start").count() == 1, "no start button"
        page.click("#start")

        n_docs = 0
        while page.locator("#next").count() == 1:
            n_docs += 1
            assert page.locator("fieldset").count() == 2, "expected 2 questions per document"
            assert len(page.locator("div.doc").inner_text().strip()) > 40, "empty document text"
            # answer both questions (option A) and rate confidence
            for fs in page.locator("fieldset").all():
                fs.locator("input[type=radio]").first.check()
            page.locator("input[name^=conf_]").first.check()
            page.click("#next")
            assert n_docs <= 12, "more than 12 documents: loop is not terminating"

        # export screen
        page.wait_for_selector("#dl")
        blob = page.locator("textarea").input_value()
        data = json.loads(blob)
        page.screenshot(path=os.path.join(HERE, "results", "survey_test_done.png"), full_page=True)
        browser.close()

    assert n_docs == 12, "expected 12 documents, saw %d" % n_docs
    assert len(data["trials"]) == 24, "expected 24 trials, got %d" % len(data["trials"])
    assert data["n_attempted"] == 24, "expected 24 attempted, got %d" % data["n_attempted"]
    assert data["lang"] in ("uk", "en"), "language not recorded"
    regs = {t["register"] for t in data["trials"]}
    docs = {t["document"] for t in data["trials"]}
    assert regs == {"formal", "plain"}, "both registers must appear: %s" % regs
    assert len(docs) == 6, "expected all 6 obligations, got %d" % len(docs)
    for t in data["trials"]:
        assert set(t) >= {"item", "document", "register", "lang", "kind", "response",
                          "correct", "rt_ms", "confidence"}, "trial fields incomplete"
    os.makedirs(os.path.dirname(FIXTURE), exist_ok=True)
    with open(FIXTURE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    print("instrument OK: %d documents, %d trials, both registers, language %s"
          % (n_docs, len(data["trials"]), data["lang"]))
    print("export keys: %s" % sorted(data))
    print("wrote fixture (NOT DATA): %s" % os.path.relpath(FIXTURE, os.path.dirname(HERE)))
    if errors:
        print("PAGE ERRORS:", errors)
        return 1
    if console:
        print("console:", console[:5])
    return 0


if __name__ == "__main__":
    sys.exit(main())
