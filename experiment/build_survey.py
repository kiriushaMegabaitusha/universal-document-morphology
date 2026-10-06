#!/usr/bin/env python3
"""Generate the self-contained human instrument (human_survey.html) from stimuli.json.

Generating rather than hand-writing the survey means the participant-facing texts
cannot drift from the registered stimuli: the same JSON is inlined verbatim.

The generated file needs no network, no server and no dependencies. A participant
opens it, picks a language, reads 12 documents (each obligation in both registers)
and answers 24 four-option questions plus a confidence rating per document. Results
stay in the participant's browser until they download them and send them back.

Order control: document order and, within each document, the order of the two
registers are permuted per participant from a seed derived from the participant id.
Condition labels are never shown.

Run:  python3 experiment/build_survey.py   ->  experiment/human_survey.html
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

HTML = r"""<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Розуміння офіційних документів / Understanding official documents</title>
<style>
  :root { --fg:#111; --bg:#fbfbf9; --muted:#555; --line:#bbb; --accent:#1a4f8a; }
  html { font-size: 18px; }
  body { margin:0; background:var(--bg); color:var(--fg);
         font-family: "DejaVu Serif", Georgia, "Times New Roman", serif;
         line-height:1.65; }
  main { max-width: 46rem; margin: 0 auto; padding: 1.5rem 1.25rem 5rem; }
  h1 { font-size:1.5rem; line-height:1.3; margin:0 0 .5rem; }
  h2 { font-size:1.15rem; margin:1.6rem 0 .4rem; }
  .muted { color:var(--muted); font-size:.92rem; }
  .doc { border:1px solid var(--line); background:#fff; padding:1rem 1.1rem;
         margin:.9rem 0 1.2rem; white-space:pre-wrap; font-size:1.02rem; }
  fieldset { border:0; padding:0; margin:1.1rem 0 0; }
  legend { font-weight:bold; padding:0 0 .35rem; }
  label.opt { display:block; padding:.5rem .6rem; border:1px solid var(--line);
              border-radius:.25rem; margin:.35rem 0; background:#fff; cursor:pointer; }
  label.opt:hover { border-color:var(--accent); }
  label.opt input { margin-right:.55rem; }
  button { font:inherit; padding:.6rem 1.1rem; border:1px solid var(--accent);
           background:var(--accent); color:#fff; border-radius:.25rem; cursor:pointer; }
  button.secondary { background:#fff; color:var(--accent); }
  button:focus, label.opt:focus-within, input:focus { outline:3px solid #ffbf47; outline-offset:2px; }
  .bar { height:.4rem; background:#e3e3e0; border-radius:.2rem; overflow:hidden; margin:.6rem 0 1.4rem; }
  .bar > i { display:block; height:100%; background:var(--accent); width:0; }
  .conf { display:flex; gap:.6rem; flex-wrap:wrap; margin-top:.4rem; }
  .conf label { border:1px solid var(--line); border-radius:.25rem; padding:.35rem .6rem; background:#fff; cursor:pointer; }
  textarea { width:100%; height:9rem; font-family:ui-monospace, monospace; font-size:.85rem; }
  .skip { background:none; border:0; color:var(--accent); text-decoration:underline; padding:.2rem 0; cursor:pointer; }
  details { margin-top:1rem; }
  .big { font-size:1.2rem; }
</style>
</head>
<body>
<main id="app" aria-live="polite"></main>
<script>
const STIM = @@STIMULI@@;
const KEY = "udm_comp_test_v1";
const S = { step: "intro", i: 0, order: [], regOrder: {}, started: null, finished: null,
            pid: null, lang: "uk", answers: {}, conf: {} };

/* ---------- deterministic per-participant permutation ---------- */
function hash(str){ let h=2166136261; for(let i=0;i<str.length;i++){ h^=str.charCodeAt(i); h=Math.imul(h,16777619);} return h>>>0; }
function mulberry(a){ return function(){ a|=0; a=a+0x6D2B79F5|0; let t=Math.imul(a^a>>>15,1|a); t=t+Math.imul(t^t>>>7,61|t)^t; return ((t^t>>>14)>>>0)/4294967296; }; }
function shuffled(arr, rnd){ const a=arr.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(rnd()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; }
function buildOrder(){
  const rnd = mulberry(hash(S.pid));
  S.order = shuffled(STIM.documents.map(d=>d.id), rnd);
  S.regOrder = {};
  for(const id of S.order){
    const first = rnd() < 0.5 ? ["formal","plain"] : ["plain","formal"];
    S.regOrder[id] = first;
  }
}

/* ---------- persistence ---------- */
function save(){ try{ localStorage.setItem(KEY, JSON.stringify(S)); }catch(e){} }
function load(){
  let raw=null; try{ raw=localStorage.getItem(KEY); }catch(e){}
  if(!raw) return false;
  try{ const o=JSON.parse(raw); Object.assign(S,o); return S.step!=="intro"; }catch(e){ return false; }
}
function resetAll(){ try{ localStorage.removeItem(KEY); }catch(e){}
  location.reload(); }

/* ---------- helpers ---------- */
const el = (t,a={},...kids)=>{ const n=document.createElement(t); for(const k in a){ if(k==="class"){n.className=a[k];} else {n.setAttribute(k,a[k]);} } kids.forEach(k=>n.append(k)); return n; };
const t = (txt)=>document.createTextNode(txt);
function T(uk, en){ return S.lang==="uk" ? uk : en; }
function trialKey(docId, reg, itemId){ return docId+"|"+reg+"|"+itemId; }
function answeredCount(){ return Object.keys(S.answers).filter(k=>S.answers[k]).length; }
function totalTrials(){ return STIM.documents.length*2*STIM.meta.items_per_document; }

/* ---------- screens ---------- */
function render(){
  const app = document.getElementById("app");
  app.innerHTML = "";
  window.scrollTo(0,0);
  if(S.step==="intro") return renderIntro(app);
  if(S.step==="task")  return renderTask(app);
  if(S.step==="done")  return renderDone(app);
}

function renderIntro(app){
  app.append(el("h1",{}, t(T("Розуміння офіційних документів",
                             "Understanding official documents"))));
  app.append(el("p",{class:"muted"}, t(T(
    "Дослідження до атласу стандартів оформлення документів (проєкт 05.4). Ви прочитаєте 12 коротких фрагментів офіційних документів і відповісте на 24 запитання. Це займе приблизно 10–15 хвилин.",
    "A study for the official-document standards atlas (project 05.4). You will read 12 short passages of official documents and answer 24 questions. This takes about 10–15 minutes."))));
  app.append(el("h2",{}, t(T("Що важливо знати","What you should know"))));
  const ul = el("ul",{});
  [
    T("Участь добровільна, ім'я не потрібне. Нічого не надсилається автоматично: відповіді зберігаються лише у вашому браузері, і наприкінці ви завантажуєте файл із результатами.",
      "Participation is voluntary and anonymous. Nothing is sent anywhere: your answers stay in this browser, and at the end you download a results file."),
    T("Прочитайте фрагмент уважно, але не повертайтеся назад: кожен документ показується один раз.",
      "Read each passage carefully, but you cannot go back: each document is shown once."),
    T("Запитання мають 4 варіанти відповіді; правильна лише одна. Якщо не знаєте — оберіть найближчий варіант або натисніть «пропустити».",
      "Each question has 4 options and exactly one correct answer. If unsure, pick the closest option or press skip."),
    T("Немає обмеження часу і немає «правильної швидкості».",
      "There is no time limit and no \"right\" speed.")
  ].forEach(x=>ul.append(el("li",{},t(x))));
  app.append(ul);
  app.append(el("h2",{}, t(T("Мова","Language"))));
  const langs = el("div",{class:"conf",role:"radiogroup","aria-label":T("Мова","Language")});
  [["uk","Українська"],["en","English"]].forEach(([code,label])=>{
    const id="lang_"+code;
    const l=el("label",{for:id}, el("input",{type:"radio",name:"lang",id:id,value:code,checked:S.lang===code?"checked":null}), t(label));
    l.querySelector("input").addEventListener("change",()=>{S.lang=code; save();});
    langs.append(l);
  });
  app.append(langs);
  app.append(el("p",{}, el("button",{id:"start"}, t(T("Почати","Start")))));
  app.append(el("p",{class:"muted small"}, t(T(
    "Продовжуючи, ви погоджуєтеся взяти участь. Ви можете закрити сторінку будь-коли; щоб почати заново, натисніть «Скинути».",
    "By continuing you agree to take part. You can close the page at any time; to start over, press reset."))));
  document.getElementById("start").addEventListener("click", ()=>{
    if(!S.pid){ S.pid = (new URLSearchParams(location.search)).get("pid") || "p"+Math.random().toString(36).slice(2,10); }
    buildOrder(); S.started = new Date().toISOString(); S.step="task"; S.i=0; save(); render();
  });
  app.append(el("p",{}, el("button",{class:"skip",id:"reset"}, t(T("Скинути збережений прогрес","Reset saved progress")))));
  document.getElementById("reset").addEventListener("click", resetAll);
}

function renderTask(app){
  const docId = S.order[S.i];
  const doc = STIM.documents.find(d=>d.id===docId);
  const regs = S.regOrder[docId];
  const reg = regs[S.regCursor||0];
  const shown = new Date();
  const pct = Math.round(100*answeredCount()/totalTrials());
  app.append(el("h1",{}, t(T("Документ","Document")) + " " + (S.i+1) + "/" + S.order.length));
  app.append(el("div",{class:"bar",role:"progressbar","aria-valuenow":pct,"aria-valuemin":"0","aria-valuemax":"100"},
    el("i",{style:"width:"+pct+"%"})));
  app.append(el("div",{class:"doc",lang:S.lang==="uk"?"uk":"en"}, t(doc.registers[S.lang+"-"+reg])));
  doc.items.forEach((it, qi)=>{
    const fs = el("fieldset",{});
    fs.append(el("legend",{}, t(it["q_"+S.lang])));
    const opts = it["options_"+S.lang];
    opts.forEach((o, oi)=>{
      const letter="ABCD"[oi], id=trialKey(docId,reg,it.id)+"_"+letter;
      const l = el("label",{class:"opt",for:id});
      const input = el("input",{type:"radio",name:trialKey(docId,reg,it.id),id:id,value:letter});
      const prev = S.answers[trialKey(docId,reg,it.id)];
      if(prev===letter) input.setAttribute("checked","checked");
      input.addEventListener("change",()=>{ S.answers[trialKey(docId,reg,it.id)]=letter; save(); updateProgress(); });
      l.append(input, t(letter + ". " + o));
      fs.append(l);
    });
    const skip = el("button",{class:"skip",type:"button"}, t(T("пропустити це запитання","skip this question")));
    skip.addEventListener("click", ()=>{ S.answers[trialKey(docId,reg,it.id)]="SKIP"; save(); updateProgress(); });
    fs.append(skip);
    app.append(fs);
  });
  app.append(el("h2",{}, t(T("Наскільки впевнено ви відповіли?","How confident are you in your answers?"))));
  const conf = el("div",{class:"conf",role:"radiogroup","aria-label":T("Впевненість","Confidence")});
  [["1",T("1 — зовсім не впевнено","1 — not at all")],["2","2"],["3","3"],["4","4"],
   ["5",T("5 — цілком впевнено","5 — completely")]].forEach(([v,lbl])=>{
    const id="conf_"+v;
    const l=el("label",{for:id});
    const input=el("input",{type:"radio",name:"conf_"+(docId+reg),id:id,value:v});
    if(S.conf[docId+"|"+reg]===v) input.setAttribute("checked","checked");
    input.addEventListener("change",()=>{ S.conf[docId+"|"+reg]=v; save(); });
    l.append(input, t(lbl));
    conf.append(l);
  });
  app.append(conf);
  const next = el("p",{}, el("button",{id:"next"}, t(
    (S.i===S.order.length-1 && (S.regCursor||0)===regs.length-1)
      ? T("Завершити","Finish") : T("Далі","Next"))));
  app.append(next);
  const rt = ()=> Math.round(performance.now() - shown.getTime());
  document.getElementById("next").addEventListener("click", ()=>{
    const key = docId+"|"+reg;
    const now = new Date().getTime();
    doc.items.forEach(it=>{
      const k = trialKey(docId,reg,it.id);
      const rec = S.answers[k];
      S.answers[k] = rec || "SKIP";
      S.answers["rt_"+key] = now - shown.getTime();
    });
    save();
    if((S.regCursor||0) === regs.length-1){ S.regCursor = 0; S.i += 1; } else { S.regCursor = (S.regCursor||0)+1; }
    if(S.i >= S.order.length){ S.step="done"; S.finished=new Date().toISOString(); }
    save(); render();
  });
}

function updateProgress(){
  const pct = Math.round(100*answeredCount()/totalTrials());
  const bar=document.querySelector(".bar");
  if(bar){ bar.setAttribute("aria-valuenow",pct); bar.querySelector("i").style.width=pct+"%"; }
}

function exportObject(){
  const trials=[];
  for(const docId of STIM.documents.map(d=>d.id)){
    const doc = STIM.documents.find(d=>d.id===docId);
    ["formal","plain"].forEach(reg=>{
      doc.items.forEach(it=>{
        const k = trialKey(docId,reg,it.id);
        const resp = S.answers[k];
        const idx = "ABCD".indexOf(resp);
        trials.push({
          item: it.id, document: docId, register: reg, lang: S.lang, kind: it.kind,
          response: (resp==="SKIP"||resp===undefined) ? null : resp,
          correct: (idx>=0 && resp===it.answer) ? 1 : 0,
          keyed: it.answer,
          rt_ms: S.answers["rt_"+docId+"|"+reg] || null,
          confidence: S.conf[docId+"|"+reg] || null
        });
      });
    });
  }
  trials.sort((a,b)=> (a.document+a.register+a.item).localeCompare(b.document+b.register+b.item));
  const attempted = trials.filter(t=>t.response!==null).length;
  return { participant: S.pid, lang: S.lang, started: S.started, finished: S.finished,
           n_trials: trials.length, n_attempted: attempted,
           duration_min: S.started ? Math.round((new Date(S.finished||Date.now()) - new Date(S.started))/6000)/10 : null,
           design: "within: both registers of every obligation",
           stimuli_version: STIM.meta.created, trials: trials };
}

function renderDone(app){
  const obj = exportObject();
  const json = JSON.stringify(obj, null, 1);
  app.append(el("h1",{}, t(T("Дякую! Це все.","Thank you — that is everything."))));
  app.append(el("p",{class:"big"}, t(T("Завантажте файл із результатами й надішліть його досліднику.",
                                       "Download the results file and send it back to the researcher."))));
  const dl = el("button",{id:"dl"}, t(T("Завантажити результати (JSON)","Download results (JSON)")));
  dl.addEventListener("click", ()=>{
    const blob = new Blob([json], {type:"application/json"});
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "comprehension_"+S.pid+".json";
    document.body.append(a); a.click(); a.remove();
  });
  app.append(el("p",{}, dl));
  app.append(el("details",{}, el("summary",{}, t(T("Або скопіюйте вміст файлу вручну","Or copy the file contents manually"))),
    el("textarea",{readonly:"readonly","aria-label":"results json"}, t(json))));
  app.append(el("p",{class:"muted"}, t(T("Відповідей: ","Answered: ") + obj.n_attempted + "/" + obj.n_trials +
      " · " + T("ідентифікатор учасника","participant id") + ": " + S.pid)));
  app.append(el("p",{}, el("button",{class:"secondary",id:"again"}, t(T("Почати заново (скидання)","Start over (reset)")))));
  document.getElementById("again").addEventListener("click", resetAll);
}

/* ---------- boot ---------- */
(function(){
  const resumed = load();
  if(resumed && S.step==="task" && (!S.order || !S.order.length)) buildOrder();
  if(resumed && S.step==="task" && !S.regOrder) buildOrder();
  render();
})();
</script>
</body>
</html>
"""


def main():
    stim = json.load(open(os.path.join(HERE, "stimuli.json"), encoding="utf-8"))
    # ship only what the instrument needs (and never the register labels to the eye)
    payload = {
        "meta": stim["meta"],
        "documents": [
            {"id": d["id"], "registers": d["registers"],
             "items": [{"id": i["id"], "kind": i["kind"], "answer": i["answer"],
                        "q_uk": i["q_uk"], "q_en": i["q_en"],
                        "options_uk": i["options_uk"], "options_en": i["options_en"]}
                       for i in d["items"]]}
            for d in stim["documents"]
        ],
    }
    html = HTML.replace("@@STIMULI@@", json.dumps(payload, ensure_ascii=False, indent=1))
    assert "@@STIMULI@@" not in html
    out = os.path.join(HERE, "human_survey.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    n_trials = len(payload["documents"]) * 2 * payload["meta"]["items_per_document"]
    print("wrote %s (%d KB) — %d documents, %d trials per participant"
          % (os.path.relpath(out, os.path.dirname(HERE)), len(html) // 1024,
             len(payload["documents"]), n_trials))


if __name__ == "__main__":
    main()
