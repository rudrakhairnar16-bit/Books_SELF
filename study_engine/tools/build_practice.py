#!/usr/bin/env python3
"""
Build a self-contained interactive practice page for a subject:
flashcards (flip, know / don't-know) + MCQ quiz (score, per-topic weak areas, retry wrong).

Usage (repo root):  python3 study_engine/tools/build_practice.py DLD
Reads   study/<SUBJ>/*/05_mcqs.md  and  study/<SUBJ>/*/04_flashcards.csv
Writes  study/<SUBJ>/practice.html   (open in any browser / phone, works offline)
"""
import sys, os, re, csv, json, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def parse_mcqs(path, unit):
    txt = open(path, encoding="utf-8").read()
    out = []
    for block in re.split(r"\n### ", "\n" + txt)[1:]:
        lines = block.strip().splitlines()
        q = re.sub(r"^Q\d+\.\s*", "", lines[0]).strip()
        opts = [re.sub(r"^- [A-D]\)\s*", "", l).strip() for l in lines if re.match(r"^- [A-D]\)", l)]
        m = next((l for l in lines if l.startswith("**Ans:")), None)
        if not m or len(opts) != 4:
            continue
        ans = "ABCD".index(re.search(r"\*\*Ans:\s*([A-D])", m).group(1))
        why = re.sub(r"^\*\*Ans:\s*[A-D]\*\*\s*—?\s*", "", m)
        topic = (re.findall(r"`#([\w-]+)`", why) or ["general"])[0]
        src = (re.findall(r"`\[([^\]]+)\]`", why) or [""])[0]
        why = re.sub(r"`[^`]*`", "", why).strip()
        out.append({"u": unit, "q": q, "o": opts, "a": ans, "w": why, "t": topic, "s": src})
    return out


def main():
    subj = sys.argv[1]
    base = os.path.join(ROOT, "study", subj)
    mcqs, cards = [], []
    for d in sorted(glob.glob(os.path.join(base, "[0-9][0-9]_*"))):
        unit = os.path.basename(d)
        unit_label = "U" + str(int(unit[:2])) + " " + unit[3:].replace("_", " ")
        if os.path.exists(os.path.join(d, "05_mcqs.md")):
            mcqs += parse_mcqs(os.path.join(d, "05_mcqs.md"), unit_label)
        fc = os.path.join(d, "04_flashcards.csv")
        if os.path.exists(fc):
            for r in csv.DictReader(open(fc, encoding="utf-8"), delimiter=";"):
                cards.append({"u": unit_label, "f": r["front"], "b": r["back"], "t": r.get("tags", "").split("::")[-1]})
    data = json.dumps({"subject": subj, "mcqs": mcqs, "cards": cards}, ensure_ascii=False)
    page = TEMPLATE.replace("__DATA__", data).replace("__SUBJ__", html.escape(subj))
    out = os.path.join(base, "practice.html")
    open(out, "w", encoding="utf-8").write(page)
    print(f"wrote {out}: {len(mcqs)} MCQs, {len(cards)} flashcards")


TEMPLATE = r"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__SUBJ__ Practice — Mentor</title>
<style>
:root{--ink:#16266e;--red:#b2191e;--bg:#fbf8ee;--card:#fff;--ok:#1d7a3a}
*{box-sizing:border-box}body{margin:0;font-family:system-ui,Segoe UI,Roboto,sans-serif;background:var(--bg);color:#222}
header{background:var(--ink);color:#fff;padding:14px 18px}header h1{margin:0;font-size:20px}
nav{display:flex;gap:8px;flex-wrap:wrap;padding:10px 18px;background:#e9edf9}
button,select{font:inherit;padding:8px 14px;border-radius:8px;border:1px solid #9aa6d1;background:#fff;cursor:pointer}
button.on{background:var(--ink);color:#fff}main{max-width:820px;margin:18px auto;padding:0 14px}
.card{background:var(--card);border-radius:14px;box-shadow:0 2px 10px #0002;padding:22px;margin-bottom:14px}
.flip{min-height:200px;display:flex;align-items:center;justify-content:center;text-align:center;font-size:21px;cursor:pointer;white-space:pre-wrap}
.flip.back{background:#fff8d6}.meta{color:#667;font-size:13px;margin-bottom:8px}
.opt{display:block;width:100%;text-align:left;margin:7px 0;padding:11px 14px}
.opt.ok{background:#d9f3df;border-color:var(--ok)}.opt.bad{background:#fadcdc;border-color:var(--red)}
.why{margin-top:10px;padding:10px;border-left:4px solid var(--ink);background:#eef1fb;display:none}
.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;justify-content:space-between}
.bar{height:8px;background:#dde;border-radius:4px;overflow:hidden}.bar i{display:block;height:100%;background:var(--ok)}
table{border-collapse:collapse;width:100%}td,th{border-bottom:1px solid #ddd;padding:6px;text-align:left}
.weak{color:var(--red);font-weight:600}textarea{width:100%;height:90px}
</style></head><body>
<header><h1>📚 __SUBJ__ — Practice (Mentor)</h1><div style="font-size:13px;opacity:.85">Flashcards + MCQ quiz · works offline · progress saved in this browser</div></header>
<nav><button id="tF" class="on">🃏 Flashcards</button><button id="tQ">✅ MCQ Quiz</button><button id="tR">📊 Results</button>
<select id="unit"></select><select id="cnt"><option value="10">10 Qs</option><option value="20" selected>20 Qs</option><option value="9999">All</option></select>
<button id="wrongOnly">↻ Only my wrong ones</button></nav>
<main id="app"></main>
<script>
const D=__DATA__;const $=s=>document.querySelector(s);const LS="mentor_"+D.subject;
let st=JSON.parse(localStorage.getItem(LS)||'{"wrong":{},"hist":[],"known":{}}');const save=()=>localStorage.setItem(LS,JSON.stringify(st));
const units=[...new Set([...D.mcqs.map(m=>m.u),...D.cards.map(c=>c.u)])];
$("#unit").innerHTML='<option value="">All units</option>'+units.map(u=>`<option>${u}</option>`).join("");
const shuf=a=>{a=[...a];for(let i=a.length-1;i>0;i--){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]]}return a};
const esc=s=>s.replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));
let mode="F",onlyWrong=false;
function tab(m){mode=m;["F","Q","R"].forEach(x=>$("#t"+x).classList.toggle("on",x==m));render()}
$("#tF").onclick=()=>tab("F");$("#tQ").onclick=()=>tab("Q");$("#tR").onclick=()=>tab("R");
$("#unit").onchange=render;$("#cnt").onchange=render;$("#wrongOnly").onclick=()=>{onlyWrong=!onlyWrong;$("#wrongOnly").classList.toggle("on",onlyWrong);render()};
function pool(arr,key){let p=arr.filter(x=>!$("#unit").value||x.u==$("#unit").value);if(onlyWrong)p=p.filter(x=>st.wrong[key(x)]);return p}
function render(){mode=="F"?flash():mode=="Q"?quiz():results()}
function flash(){let cs=shuf(pool(D.cards,c=>"c:"+c.f)),i=0,back=false;
 const draw=()=>{if(!cs.length){$("#app").innerHTML='<div class="card">No cards here 🎉</div>';return}
  const c=cs[i];$("#app").innerHTML=`<div class="card"><div class="meta">${c.u} · #${c.t} · card ${i+1}/${cs.length}</div>
  <div class="flip ${back?"back":""}" id="fl">${esc(back?c.b:c.f)}</div><div class="meta" style="text-align:center">tap card to flip</div>
  <div class="row"><button id="no">❌ Didn't know</button><button id="yes">✔ Knew it</button></div></div>`;
  $("#fl").onclick=()=>{back=!back;draw()};
  const nx=k=>{if(k){delete st.wrong["c:"+c.f]}else{st.wrong["c:"+c.f]=1}save();i=(i+1)%cs.length;back=false;draw()};
  $("#yes").onclick=()=>nx(1);$("#no").onclick=()=>nx(0)};draw()}
function quiz(){let qs=shuf(pool(D.mcqs,m=>"q:"+m.q)).slice(0,+$("#cnt").value),i=0,score=0,log=[];
 const draw=()=>{if(!qs.length){$("#app").innerHTML='<div class="card">No questions here 🎉</div>';return}
  if(i>=qs.length)return finish();const m=qs[i];
  $("#app").innerHTML=`<div class="card"><div class="meta">${m.u} · #${m.t} · Q ${i+1}/${qs.length} · score ${score}</div>
  <div class="bar"><i style="width:${100*i/qs.length}%"></i></div><h3>${esc(m.q)}</h3>
  ${m.o.map((o,k)=>`<button class="opt" data-k="${k}">${"ABCD"[k]}) ${esc(o)}</button>`).join("")}
  <div class="why" id="why"><b>Answer ${"ABCD"[m.a]}</b> — ${esc(m.w)} <span class="meta">${esc(m.s)}</span></div>
  <div class="row" style="margin-top:10px"><span></span><button id="nx" style="display:none">Next →</button></div></div>`;
  document.querySelectorAll(".opt").forEach(b=>b.onclick=()=>{const k=+b.dataset.k,ok=k==m.a;
   document.querySelectorAll(".opt").forEach(x=>{x.disabled=true;if(+x.dataset.k==m.a)x.classList.add("ok")});
   if(!ok)b.classList.add("bad");if(ok){score++;delete st.wrong["q:"+m.q]}else st.wrong["q:"+m.q]=1;save();
   log.push({t:m.t,u:m.u,ok});$("#why").style.display="block";$("#nx").style.display="inline-block"});
  $("#nx").onclick=()=>{i++;draw()}};
 const finish=()=>{const by={};log.forEach(l=>{by[l.t]=by[l.t]||[0,0];by[l.t][1]++;if(l.ok)by[l.t][0]++});
  const pct=Math.round(100*score/qs.length);const weak=Object.entries(by).filter(([t,[a,n]])=>a/n<0.6).map(([t])=>t);
  st.hist.push({d:new Date().toISOString().slice(0,10),u:$("#unit").value||"All",s:score,n:qs.length,weak});save();
  const report=`${D.subject} quiz ${new Date().toISOString().slice(0,10)} (${$("#unit").value||"All units"}): ${score}/${qs.length} (${pct}%). Weak topics: ${weak.join(", ")||"none"}`;
  $("#app").innerHTML=`<div class="card"><h2>Score: ${score}/${qs.length} (${pct}%) ${pct>=80?"🟢 STRONG":pct>=60?"🟡 SHAKY":"🔴 WEAK"}</h2>
  <table><tr><th>Topic</th><th>Correct</th></tr>${Object.entries(by).map(([t,[a,n]])=>`<tr class="${a/n<0.6?"weak":""}"><td>#${t}</td><td>${a}/${n}</td></tr>`).join("")}</table>
  <p><b>Send this to your mentor:</b></p><textarea readonly>${report}</textarea>
  <div class="row"><button onclick="navigator.clipboard.writeText(document.querySelector('textarea').value)">📋 Copy</button><button onclick="render()">↻ New quiz</button></div></div>`};
 draw()}
function results(){const w=Object.keys(st.wrong);
 $("#app").innerHTML=`<div class="card"><h2>History</h2><table><tr><th>Date</th><th>Unit</th><th>Score</th><th>Weak</th></tr>
 ${st.hist.slice(-20).reverse().map(h=>`<tr><td>${h.d}</td><td>${h.u}</td><td>${h.s}/${h.n}</td><td class="weak">${h.weak.join(", ")}</td></tr>`).join("")||"<tr><td colspan=4>No quizzes yet</td></tr>"}</table>
 <p>Items currently marked wrong: <b>${w.length}</b> — use “Only my wrong ones” to drill them.</p>
 <button onclick="if(confirm('Reset all progress?')){localStorage.removeItem(LS);location.reload()}">Reset progress</button></div>`}
render();
</script></body></html>"""

if __name__ == "__main__":
    main()
