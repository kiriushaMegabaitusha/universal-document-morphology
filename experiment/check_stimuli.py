#!/usr/bin/env python3
"""Validate the comprehension-test stimuli and compute the manipulation check.

Three jobs:

1. STRUCTURE. Six obligations, four registers each ({en,uk} x {formal,plain}),
   two four-option items per obligation, answer key in A-D.
2. CONTENT PRESERVATION. The register manipulation must change style only, never
   the facts. Checked mechanically: within each language the formal and plain
   renderings must contain the same set of numeric tokens, and that set must
   equal the set the gold fact tuple declares. Across languages the numeric
   token sets must also agree. (Number form is held constant: digits everywhere.)
3. INDEPENDENT ANSWER KEY. EXPECTED_ANSWERS below is transcribed by hand from the
   gold facts, independently of the "answer" field in stimuli.json. Any later
   edit that breaks the key fails the gate.

Also writes results/manipulation_check.csv: surface complexity per rendering
(words, sentences, mean sentence length, long-word share, formal markers,
passive/reflexive markers). The register manipulation is only credible if these
move in the expected direction; the script prints an explicit verdict.

Run:  python3 experiment/check_stimuli.py
"""
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
REGISTERS = ["en-formal", "en-plain", "uk-formal", "uk-plain"]
LANGS = {"en": ["en-formal", "en-plain"], "uk": ["uk-formal", "uk-plain"]}

# Hand-transcribed answer key: the CONTENT of the correct answer, by item, in both
# languages, derived from the gold facts independently of the "answer" letter in
# stimuli.json. Letter-agnostic on purpose, so re-balancing option order cannot
# silently invalidate the key.
EXPECTED_ANSWER_TEXT = {
    "D1-Q1": ("On the next working day", "Наступного робочого дня"),
    "D1-Q2": ("The date of receipt, the correspondent's name and the registration index",
              "Дату надходження, назву кореспондента і реєстраційний індекс"),
    "D2-Q1": ("30 calendar days", "30 календарних днів"),
    "D2-Q2": ("Within 3 working days of that decision", "Протягом 3 робочих днів від дня цього рішення"),
    "D3-Q1": ("On the day after its publication", "Наступного дня після опублікування"),
    "D3-Q2": ("From 1 January 2027", "З 1 січня 2027 року"),
    "D4-Q1": ("10 working days from learning of the decision",
              "10 робочих днів від дня, коли дізналася про рішення"),
    "D4-Q2": ("It may still accept the appeal", "Може все одно прийняти скаргу до розгляду"),
    "D5-Q1": ("75 years", "75 років"),
    "D5-Q2": ("The expert commission, whose decision is recorded in an act",
              "Експертна комісія, рішення якої оформлюють актом"),
    "D6-Q1": ("If the head has issued a written order naming that deputy",
              "Якщо керівник видав письмове розпорядження і назвав цього заступника"),
    "D6-Q2": ("The deputy", "Заступник"),
}
EXPECTED_ANSWERS = EXPECTED_ANSWER_TEXT  # alias kept for readability below

FORMAL_MARKERS = {
    "en-formal": ["shall", "pursuant", "in accordance with", "not exceeding",
                  "the provisions", "provided that", "be permitted"],
    "uk-formal": ["у разі", "не перевищує", "відповідно до", "протягом",
                  "виключно", "зазначаються", "покладається", "є чинними",
                  "допускається", "підлягає"],
}
PASSIVE = {
    "en": r"\b(?:is|are|was|were|be|been|being|shall be)\s+\w+(?:ed|en)\b",
    "uk": r"\w+(?:ться|ються|ється|ається|ується)\b",
}
SENT_SPLIT = {"en": r"(?<=[.!?])\s+", "uk": r"(?<=[.!?])\s+"}

errors, warnings = [], []


def lang_of(reg):
    return reg.split("-")[0]


def register_of(reg):
    return reg.split("-")[1]


def sentences(text, lang):
    parts = [s for s in re.split(SENT_SPLIT[lang], text.strip()) if s.strip()]
    return parts


def words(text):
    return re.findall(r"[^\s]+", text)


def digits(text):
    return sorted(set(re.findall(r"\d+", text)))


def metrics(text, reg):
    lang = lang_of(reg)
    w = words(text)
    s = sentences(text, lang)
    longw = [x for x in w if len(re.sub(r"[^\w]", "", x)) >= 12]
    pas = len(re.findall(PASSIVE[lang], text))
    mark = sum(len(re.findall(re.escape(m), text, re.I)) for m in FORMAL_MARKERS.get(reg, []))
    return {
        "chars": len(text),
        "words": len(w),
        "sentences": len(s),
        "mean_sentence_len": round(len(w) / max(1, len(s)), 2),
        "long_word_share": round(len(longw) / max(1, len(w)), 3),
        "formal_markers": mark,
        "passive_markers": pas,
    }


def main():
    path = os.path.join(HERE, "stimuli.json")
    data = json.load(open(path, encoding="utf-8"))
    docs = data["documents"]

    if len(docs) != 6:
        errors.append("expected 6 obligations, found %d" % len(docs))

    rows, seen_items = [], []
    for doc in docs:
        did = doc["id"]
        regs = doc.get("registers", {})
        if sorted(regs) != sorted(REGISTERS):
            errors.append("%s: registers are %s, expected %s" % (did, sorted(regs), REGISTERS))
            continue
        if doc.get("verbatim") is not False:
            warnings.append("%s: verbatim is not explicitly false" % did)
        if not doc.get("modelled_on"):
            errors.append("%s: no modelled_on provenance" % did)

        # ---- content preservation ----
        for lang, pair in LANGS.items():
            f, p = pair  # formal, plain
            df, dp = digits(regs[f]), digits(regs[p])
            if df != dp:
                errors.append("%s/%s: numeric tokens differ formal=%s plain=%s" % (did, lang, df, dp))
            gold = sorted(set(doc["gold"]["digit_set"]))
            if df != gold:
                errors.append("%s/%s: numeric tokens %s != gold %s" % (did, lang, df, gold))
            if len(regs[f].split()) <= len(regs[p].split()):
                warnings.append("%s/%s: formal rendering is not longer than plain (%d vs %d words)"
                                % (did, lang, len(regs[f].split()), len(regs[p].split())))
        den, duk = digits(regs["en-formal"]), digits(regs["uk-formal"])
        if den != duk:
            errors.append("%s: numeric tokens differ across languages en=%s uk=%s" % (did, den, duk))

        # ---- items ----
        items = doc.get("items", [])
        if len(items) != data["meta"]["items_per_document"]:
            errors.append("%s: %d items, expected %d" % (did, len(items), data["meta"]["items_per_document"]))
        for it in items:
            seen_items.append(it["id"])
            for lang in LANGS:
                q, opts = it.get("q_" + lang, ""), it.get("options_" + lang, [])
                if not q.strip():
                    errors.append("%s (%s): empty question" % (it["id"], lang))
                if len(opts) != 4:
                    errors.append("%s (%s): %d options, expected 4" % (it["id"], lang, len(opts)))
                if any(not o.strip() for o in opts):
                    errors.append("%s (%s): empty option text" % (it["id"], lang))
                if len(set(opts)) != len(opts):
                    errors.append("%s (%s): duplicate option text" % (it["id"], lang))
            if it["answer"] not in "ABCD":
                errors.append("%s: answer %r not in A-D" % (it["id"], it["answer"]))
            exp = EXPECTED_ANSWER_TEXT.get(it["id"])
            if exp is None:
                errors.append("%s: not present in the independent answer key" % it["id"])
            elif it["answer"] in "ABCD":
                idx = "ABCD".index(it["answer"])
                exp_en, exp_uk = exp
                got_en = it["options_en"][idx] if idx < len(it["options_en"]) else None
                got_uk = it["options_uk"][idx] if idx < len(it["options_uk"]) else None
                if got_en != exp_en or got_uk != exp_uk:
                    errors.append("%s: letter %s points to %r / %r; independent key says %r / %r"
                                  % (it["id"], it["answer"], got_en, got_uk, exp_en, exp_uk))
            if it.get("kind") not in ("extraction", "inference"):
                warnings.append("%s: kind %r" % (it["id"], it.get("kind")))

        for reg in REGISTERS:
            m = metrics(regs[reg], reg)
            m = {"document": did, "register": reg, "lang": lang_of(reg), "form": register_of(reg), **m}
            rows.append(m)

    missing = set(EXPECTED_ANSWERS) - set(seen_items)
    if missing:
        errors.append("answer key lists items that do not exist: %s" % sorted(missing))
    letters = [it["answer"] for doc in docs for it in doc["items"]]
    dist = {k: letters.count(k) for k in "ABCD"}
    if max(dist.values()) >= 8:
        warnings.append("answer key is skewed: %s" % dist)

    os.makedirs(RESULTS, exist_ok=True)
    out = os.path.join(RESULTS, "manipulation_check.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    # ---- manipulation verdict ----
    print("manipulation check (mean over 6 obligations):")
    print("  %-10s %6s %6s %6s %8s %8s %8s" % ("register", "words", "sents", "msl", "longw", "formMk", "passMk"))
    by_reg = {}
    for reg in REGISTERS:
        sub = [r for r in rows if r["register"] == reg]
        agg = {k: round(sum(r[k] for r in sub) / len(sub), 2)
               for k in ("words", "sentences", "mean_sentence_len", "long_word_share", "formal_markers", "passive_markers")}
        by_reg[reg] = agg
        print("  %-10s %6.2f %6.2f %6.2f %8.2f %8.2f %8.2f"
              % (reg, agg["words"], agg["sentences"], agg["mean_sentence_len"],
                 agg["long_word_share"], agg["formal_markers"], agg["passive_markers"]))
    for lang, pair in LANGS.items():
        f, p = by_reg[pair[0]], by_reg[pair[1]]
        worse = (f["mean_sentence_len"] > p["mean_sentence_len"] and f["words"] > p["words"])
        print("  -> %s: formal is %s (msl %.2f vs %.2f, words %.1f vs %.1f, formal markers %.1f vs %.1f)"
              % (lang, "harder on every surface proxy" if worse else "NOT harder on every proxy",
                 f["mean_sentence_len"], p["mean_sentence_len"], f["words"], p["words"],
                 f["formal_markers"], p["formal_markers"]))
        if not worse:
            warnings.append("%s: manipulation did not raise every surface complexity proxy" % lang)

    print("\nwrote %s (%d rows)" % (os.path.relpath(out, os.path.dirname(HERE)), len(rows)))
    print("items: %d | answer distribution: %s" % (len(seen_items), dist))
    for w in warnings:
        print("WARNING:", w)
    if errors:
        print("\nERRORS:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print("\nOK - stimuli valid, content preserved across registers, answer key consistent")


if __name__ == "__main__":
    main()
