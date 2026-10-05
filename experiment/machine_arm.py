#!/usr/bin/env python3
"""Machine arm of the finding-5 comprehension test (pre-registered, exploratory).

Each reader model answers both items of all 24 documents (6 obligations x 4
registers). One API call per (model, document, item) -> 48 item-administrations per
model. The model is never told which register it is reading: the prompt contains
the document text and the question, nothing else.

Credential handling: the OpenRouter key is read from ~/.hermes/.env at runtime and
never printed, logged or written into the results.

Outputs
  results/machine_raw.jsonl     one JSON object per item-administration (appended,
                                so the run is resumable; finished cells are skipped)
  results/machine_models.json   model ids, names and prices as of the run

Run
  python3 experiment/machine_arm.py                     # all registered models
  python3 experiment/machine_arm.py --limit 2           # smoke test: first 2 models
  python3 experiment/machine_arm.py --models a/b,c/d    # subset
"""
import argparse
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(HERE, "results")
RAW = os.path.join(RESULTS, "machine_raw.jsonl")
MODELS_OUT = os.path.join(RESULTS, "machine_models.json")
ENV_FILE = os.path.expanduser("~/.hermes/.env")
API = "https://openrouter.ai/api/v1/chat/completions"
MODELS_API = "https://openrouter.ai/api/v1/models"

# Fixed at registration (PREREGISTRATION.md §3): 12 readers spanning ~1B to ~30B+
# and six families. Cheap enough that the whole arm costs cents.
REGISTERED_MODELS = [
    "meta-llama/llama-3.2-1b-instruct",
    "meta-llama/llama-3.1-8b-instruct",
    "mistralai/mistral-nemo",
    "mistralai/mistral-small-24b-instruct-2501",
    "mistralai/ministral-8b-2512",
    "qwen/qwen-2.5-7b-instruct",
    "qwen/qwen3.5-9b",
    "qwen/qwen3-30b-a3b-instruct-2507",
    "google/gemini-2.5-flash-lite",
    "google/gemini-3.1-flash-lite",
    "deepseek/deepseek-v3.2",
    "deepseek/deepseek-chat-v3.1",
]

SYSTEM = ("You are a careful reader. Answer the question using ONLY the document "
          "provided. Do not explain. Reply with a single JSON object and nothing "
          'else: {"answer": "A"}')

_write_lock = threading.Lock()


def load_key():
    if not os.path.exists(ENV_FILE):
        sys.exit("no %s found" % ENV_FILE)
    for line in open(ENV_FILE, encoding="utf-8", errors="replace"):
        line = line.strip()
        if line.startswith("OPENROUTER_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("OPENROUTER_API_KEY not present in %s" % ENV_FILE)


def post(url, payload, key, timeout=90):
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8") if payload is not None else None,
        headers={"Authorization": "Bearer %s" % key,
                 "Content-Type": "application/json",
                 "HTTP-Referer": "https://localhost/atlas-comprehension-test",
                 "X-Title": "05.4 document morphology comprehension test"},
        method="POST" if payload is not None else "GET")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def models_meta():
    with urllib.request.urlopen(MODELS_API, timeout=60) as r:
        data = json.load(r)["data"]
    out = {}
    for m in data:
        pr = m.get("pricing", {}) or {}
        try:
            pin = float(pr.get("prompt") or 0) * 1e6
            pout = float(pr.get("completion") or 0) * 1e6
        except (TypeError, ValueError):
            pin = pout = None
        out[m["id"]] = {"name": m.get("name", ""), "prompt_usd_per_mtok": pin,
                        "completion_usd_per_mtok": pout}
    return out


def build_prompt(doc, item, lang):
    text = doc["registers"]["%s-%s" % (lang, item["register"])]
    q = item["q_" + lang]
    opts = item["options_" + lang]
    lines = ["DOCUMENT:", text, "", "QUESTION:", q, "", "OPTIONS:"]
    for i, o in enumerate(opts):
        lines.append("%s) %s" % ("ABCD"[i], o))
    lines += ["", 'Reply with JSON only: {"answer": "<A|B|C|D>"}']
    return "\n".join(lines)


def parse_answer(raw, options, lang):
    """Return (letter, ok_strict_json). Tolerant of the failure modes this model
    population actually shows: bare letters, JSON, or the option text echoed."""
    if raw is None:
        return None, False
    txt = raw.strip()
    letter, strict = None, False
    m = re.search(r'\{[^{}]*"answer"\s*:\s*"([A-Da-d])"', txt)
    if m:
        letter, strict = m.group(1).upper(), True
    else:
        m = re.search(r'\{[^{}]*"answer"\s*:\s*"?([^"}]{1,80})"?', txt)
        if m:
            cand = m.group(1).strip()
            if len(cand) == 1 and cand.upper() in "ABCD":
                letter, strict = cand.upper(), True
    if letter is None:
        # option text echoed back?
        for i, o in enumerate(options):
            if o.strip().lower() in txt.lower():
                letter = "ABCD"[i]
                break
    if letter is None:
        m = re.match(r'^\s*\(?([A-Da-d])\)?\s*[).:]?\s*$', txt)
        if m:
            letter = m.group(1).upper()
    if letter is None:
        m = re.search(r'\b([A-D])\b', txt)
        if m:
            letter = m.group(1)
    return letter, strict


def cells(data):
    """Every (document, register, item, lang) administration, in a fixed order."""
    out = []
    for doc in data["documents"]:
        for lang in ("en", "uk"):
            for reg in ("formal", "plain"):
                for it in doc["items"]:
                    item = dict(it, register=reg)
                    out.append({
                        "document": doc["id"], "lang": lang, "register": reg,
                        "item": it["id"], "kind": it["kind"], "answer_key": it["answer"],
                        "_doc": doc, "_item": item,
                    })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default=",".join(REGISTERED_MODELS))
    ap.add_argument("--limit", type=int, default=0, help="use only the first N models")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    models = [m.strip() for m in args.models.split(",") if m.strip()]
    if args.limit:
        models = models[:args.limit]

    data = json.load(open(os.path.join(HERE, "stimuli.json"), encoding="utf-8"))
    todo = cells(data)
    os.makedirs(RESULTS, exist_ok=True)

    meta = models_meta()
    unknown = [m for m in models if m not in meta]
    if unknown:
        print("WARNING: not in the OpenRouter catalogue, will skip:", unknown)
    models = [m for m in models if m in meta]
    with open(MODELS_OUT, "w", encoding="utf-8") as f:
        json.dump({m: meta[m] for m in models}, f, ensure_ascii=False, indent=2)

    # resume: skip cells already recorded
    done = set()
    if os.path.exists(RAW):
        for line in open(RAW, encoding="utf-8"):
            try:
                r = json.loads(line)
                done.add((r["model"], r["document"], r["item"], r["lang"], r["register"]))
            except Exception:
                pass
    jobs = [(m, c) for m in models for c in todo if (m, c["document"], c["item"], c["lang"], c["register"]) not in done]
    print("models=%d cells/model=%d total_cells=%d already_done=%d to_run=%d"
          % (len(models), len(todo), len(models) * len(todo), len(done), len(jobs)))
    if args.dry_run or not jobs:
        return 0

    key = load_key()

    def run_one(job):
        model, c = job
        prompt = build_prompt(c["_doc"], c["_item"], c["lang"])
        payload = {"model": model, "temperature": 0, "max_tokens": 40,
                   "messages": [{"role": "system", "content": SYSTEM},
                                {"role": "user", "content": prompt}]}
        rec = {"model": model, "document": c["document"], "item": c["item"],
               "register": c["register"], "lang": c["lang"], "kind": c["kind"],
               "answer_key": c["answer_key"], "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
        last_err = None
        for attempt in range(4):
            t0 = time.time()
            try:
                resp = post(API, payload, key)
                rec["latency_ms"] = int((time.time() - t0) * 1000)
                ch = resp.get("choices", [{}])[0]
                raw = (ch.get("message") or {}).get("content")
                rec["raw"] = raw
                u = resp.get("usage") or {}
                rec["prompt_tokens"] = u.get("prompt_tokens")
                rec["completion_tokens"] = u.get("completion_tokens")
                rec["served_model"] = resp.get("model")
                letter, strict = parse_answer(raw, c["_item"]["options_" + c["lang"]], c["lang"])
                rec["answer"] = letter
                rec["parse_ok"] = bool(letter is not None and strict)
                rec["correct"] = (None if letter is None else int(letter == c["answer_key"]))
                if letter is not None:
                    last_err = None
                    break
                last_err = "unparsable: %r" % (raw[:80] if raw else None)
            except urllib.error.HTTPError as e:
                last_err = "HTTP %s %s" % (e.code, e.read()[:120])
                if e.code in (429, 500, 502, 503, 504):
                    time.sleep(2 + 3 * attempt)
                    continue
                break
            except Exception as e:                       # noqa: BLE001 - record and retry
                last_err = "%s: %s" % (type(e).__name__, e)
                time.sleep(1.5 * (attempt + 1))
        if last_err:
            rec["error"] = str(last_err)
            if "correct" not in rec:
                rec["correct"] = None
        with _write_lock:
            with open(RAW, "a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        return rec

    t0 = time.time()
    n = 0
    errors = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for rec in ex.map(run_one, jobs):
            n += 1
            if rec.get("error"):
                errors += 1
            if n % 25 == 0 or n == len(jobs):
                print("  %d/%d  (%.0fs, errors=%d)" % (n, len(jobs), time.time() - t0, errors), flush=True)

    print("done: %d cells in %.0fs, %d with errors -> %s" % (n, time.time() - t0, errors, RAW))
    return 0


if __name__ == "__main__":
    sys.exit(main())
