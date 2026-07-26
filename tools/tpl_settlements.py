#!/usr/bin/env python3
"""HTML template for settlements.html — the Nelôxia settlements gazetteer."""

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nelôxia — settlements</title>
<meta name="description" content="A searchable gazetteer of the settlements of Nelôxia: Nelôxi endonym, international exonym, terrain, population, and output across the twelve regions.">
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link href="https://api.fontshare.com/v2/css?f[]=general-sans@400,500,600,700&f[]=zodiak@400,500&f[]=cabinet-grotesk@700,800&display=swap" rel="stylesheet">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>ô</text></svg>">
<style>
:root{
  --bg:#f4f5f8;--surface:#fff;--raise:#fbfcfd;
  --ink:#151823;--ink2:#565f70;--ink3:#8b93a4;--ink4:#aeb5c2;
  --line:#e4e7ee;--line2:#eef1f5;
  --accent:#d6274b;--accent2:#b71d3e;--accent-weak:#fdeaef;
  --chip:#eef1f6;--chip-hover:#e5e9f0;
  --bar:#eaeef4;--bar-fill:#a9b6cd;--bar-fill2:#c7d0e0;
  --shadow:0 1px 2px rgba(20,24,35,.04),0 6px 24px rgba(20,24,35,.06);
  --radius:12px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--bg);-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--ink);font-family:"General Sans",system-ui,-apple-system,sans-serif;font-size:14.5px;line-height:1.45;-webkit-font-smoothing:antialiased}
.wrap{max-width:1400px;margin:0 auto;padding:0 24px 120px}
.mast{padding:34px 0 18px}
.brandrow{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
.title{font-family:"Cabinet Grotesk","General Sans",sans-serif;font-weight:800;font-size:clamp(28px,4.2vw,46px);letter-spacing:-.032em;line-height:1}
.title .o{color:var(--accent)}
.kicker{font-weight:600;font-size:13px;letter-spacing:.02em;color:var(--ink3)}
.tagline{margin-top:10px;color:var(--ink2);font-size:15px;max-width:78ch}
.tagline b{color:var(--ink);font-weight:600}
.tagline a{color:var(--accent2);font-weight:600;text-decoration:none}
.tagline a:hover{text-decoration:underline}
.nat{display:flex;flex-wrap:wrap;gap:10px;margin-top:20px}
.natcard{flex:1 1 150px;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:14px 16px;box-shadow:var(--shadow)}
.natcard .n{font-family:"Cabinet Grotesk","General Sans";font-weight:800;font-size:24px;letter-spacing:-.02em;line-height:1}
.natcard .l{margin-top:6px;color:var(--ink3);font-size:12px;font-weight:500;letter-spacing:.02em;text-transform:uppercase}
.natcard.accent .n{color:var(--accent)}
.controls{position:sticky;top:0;z-index:40;background:var(--bg);padding:16px 0 12px;margin-top:6px}
.controls:before{content:"";position:absolute;left:-40px;right:-40px;top:0;bottom:0;background:var(--bg);z-index:-1}
.searchrow{display:flex;gap:10px;flex-wrap:wrap;align-items:stretch}
.field{position:relative;flex:1 1 360px}
.field input{width:100%;height:50px;padding:0 44px 0 46px;font-family:inherit;font-size:16px;font-weight:500;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:10px;box-shadow:var(--shadow)}
.field input::placeholder{color:var(--ink4);font-weight:400}
.field input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-weak)}
.field .mag{position:absolute;left:16px;top:16px;color:var(--ink3);pointer-events:none}
.field .clr{position:absolute;right:10px;top:9px;width:32px;height:32px;border:none;background:transparent;color:var(--ink3);font-size:18px;border-radius:8px;cursor:pointer;display:none}
.field input:not(:placeholder-shown)+.clr{display:block}
.field .clr:hover{background:var(--chip);color:var(--ink)}
.summary{display:flex;align-items:center;gap:16px;padding:0 20px;height:50px;background:var(--surface);border:1px solid var(--line);border-radius:10px;box-shadow:var(--shadow);white-space:nowrap}
.summary .s b{font-family:"Cabinet Grotesk","General Sans";font-weight:800;font-size:17px;color:var(--ink)}
.summary .s span{color:var(--ink3);font-size:12px;font-weight:500;margin-left:5px;text-transform:uppercase;letter-spacing:.02em}
.summary .div{width:1px;height:24px;background:var(--line)}
.filters{margin-top:12px}
.frow{display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.frow+.frow{margin-top:8px}
.flabel{font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3);margin-right:6px;min-width:58px}
.f{font-family:inherit;font-size:13px;font-weight:500;padding:6px 12px;border-radius:999px;cursor:pointer;background:var(--chip);border:1px solid transparent;color:var(--ink2)}
.f:hover{background:var(--chip-hover);color:var(--ink)}
.f:focus-visible{outline:2px solid var(--accent);outline-offset:1px}
.f[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
.f.all[aria-pressed="true"]{background:var(--accent);border-color:var(--accent)}
.f .fc{color:var(--ink4);font-weight:500;margin-left:5px}
.f[aria-pressed="true"] .fc{color:rgba(255,255,255,.65)}
.tablecard{margin-top:14px;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);overflow:hidden}
.tscroll{overflow-x:auto}
table{width:100%;border-collapse:collapse;min-width:1000px}
thead th{position:sticky;top:0;z-index:2;background:var(--raise);font-size:11.5px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--ink3);text-align:left;padding:13px 16px;border-bottom:1px solid var(--line);cursor:pointer;user-select:none;white-space:nowrap}
thead th:hover{color:var(--ink)}
thead th[data-on]{color:var(--accent)}
thead th:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
thead th.num{text-align:right}
.car{font-size:8px;margin-left:4px}
tbody tr{border-bottom:1px solid var(--line2)}
tbody tr:last-child{border-bottom:none}
tbody tr:hover{background:var(--raise)}
td{padding:12px 16px;vertical-align:middle}
.c-site .name{font-weight:600;font-size:15px;color:var(--ink);letter-spacing:-.01em}
.c-site .notes{color:var(--ink3);font-size:12.5px;margin-top:2px;max-width:44ch}
.nlx{font-family:"Zodiak",Georgia,serif;font-weight:500;font-size:19px;color:var(--ink)}
.gloss{color:var(--ink3);font-size:12px;margin-top:3px;max-width:34ch;font-style:italic}
.pending{color:var(--ink4);font-size:13px}
.pending b{display:block;font-size:10.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#b06a10;margin-top:3px}
.exo{font-size:14px;color:var(--ink2);white-space:nowrap}
.c-pop{text-align:right;white-space:nowrap}
.popn{font-weight:600;font-variant-numeric:tabular-nums}
.popbar{margin-top:5px;margin-left:auto;height:4px;width:110px;background:var(--bar);border-radius:3px;overflow:hidden}
.popbar i{display:block;height:100%;background:linear-gradient(90deg,var(--bar-fill2),var(--bar-fill));border-radius:3px}
.c-gdp{text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums;font-weight:600}
.c-gdp .per{display:block;margin-top:3px;font-weight:500;font-size:11.5px;color:var(--ink4)}
.pill{display:inline-flex;align-items:center;font-size:12px;font-weight:600;color:var(--ink2);background:var(--chip);padding:4px 10px;border-radius:6px;white-space:nowrap}
.lay{font-size:10.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;padding:3px 8px;border-radius:5px;background:#eaf1ff;color:#2b52c4;white-space:nowrap}
.region{color:var(--ink2);font-size:13px;white-space:nowrap}
.region .dot{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:7px;vertical-align:middle}
.badge{display:inline-block;font-size:10px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;padding:2px 7px;border-radius:5px;margin-left:7px;vertical-align:middle}
.badge.fed{background:#eaf1ff;color:#2b52c4}
.badge.com{background:#fff2e2;color:#b06a10}
.loc{white-space:nowrap;color:var(--ink2);font-size:13px}
.loc .flag{font-size:16px;margin-right:7px;vertical-align:-2px}
.empty{padding:80px 24px;text-align:center;color:var(--ink3)}
.empty .big{font-size:17px;font-weight:600;color:var(--ink2)}
.foot{margin-top:22px;color:var(--ink3);font-size:12.5px;line-height:1.65}
.foot b{color:var(--ink2);font-weight:600}
.foot a{color:var(--accent2);text-decoration:none}
.foot a:hover{text-decoration:underline}
@media(max-width:1180px){.hide-lg{display:none!important}table{min-width:700px}}
@media(max-width:760px){.hide-md{display:none!important}table{min-width:460px}.c-site .notes,.gloss{display:none}.summary{width:100%;justify-content:space-between;padding:0 14px;gap:8px}.natcard .n{font-size:20px}}
</style>
</head>
<body><div class="wrap">
  <header class="mast">
    <div class="brandrow">
      <h1 class="title">Nel<span class="o">ô</span>xia <span style="color:var(--ink3);font-weight:700">·</span> settlements</h1>
      <span class="kicker">FEDERAL GAZETTEER</span>
    </div>
    <p class="tagline">First column is a real-world map reference, not an in-world name. Local, Nelôxi and exonym are separate open decisions. <a href="toponyms.html">Roller ↗</a></p>
    <div class="nat" id="nat"></div>
  </header>

  <div class="controls">
    <div class="searchrow">
      <div class="field">
        <svg class="mag" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4.4-4.4"/></svg>
        <input id="q" type="search" placeholder="Search settlements, Nelôxi names, exonyms, terrain…" aria-label="Search settlements">
        <button class="clr" id="clr" aria-label="Clear search">×</button>
      </div>
      <div class="summary">
        <div class="s"><b id="ct">0</b><span>shown</span></div><div class="div"></div>
        <div class="s"><b id="cn">0</b><span>on record</span></div><div class="div"></div>
        <div class="s"><b id="sp">0</b><span>people</span></div><div class="div"></div>
        <div class="s"><b id="sg">0</b><span>output</span></div>
      </div>
    </div>
    <div class="filters">
      <div class="frow" id="fr"><span class="flabel">Region</span></div>
      <div class="frow" id="fl"><span class="flabel">Naming</span></div>
      <div class="frow" id="ft"><span class="flabel">Terrain</span></div>
    </div>
  </div>

  <div class="tablecard">
    <div class="tscroll">
      <table><thead><tr>
        <th data-k="site" tabindex="0">Real-world ref<span class="car"></span></th>
        <th data-k="local" tabindex="0" class="hide-md">Local name<span class="car"></span></th>
        <th data-k="nelox" tabindex="0">Nelôxi name<span class="car"></span></th>
        <th data-k="exonym" tabindex="0" class="hide-md">Exonym<span class="car"></span></th>
        <th data-k="pop" class="num" tabindex="0">Population<span class="car"></span></th>
        <th data-k="gdp" class="num hide-md" tabindex="0">Output<span class="car"></span></th>
        <th data-k="terrain" tabindex="0" class="hide-md">Terrain<span class="car"></span></th>
        <th data-k="region" tabindex="0" class="hide-lg">Region<span class="car"></span></th>
        <th data-k="cc" tabindex="0" class="hide-lg">Locale<span class="car"></span></th>
      </tr></thead><tbody id="tb"></tbody></table>
    </div>
    <div class="empty" id="empty" hidden><div class="big">No settlements match.</div><div>Try a different term or clear the filters.</div></div>
  </div>

</div>

<script>
const D = __DATA__;
const REGIONS = __REGIONS__;
const PERCAP = __PERCAP__;
const NAT = __NAT__;

const RCOLORS=["#5b8ff9","#61c0bf","#65789b","#f6bd16","#7262fd","#78d3f8","#9661bc","#f6903d","#008685","#ff99c3","#e8684a","#6dc8ec","#c2a36b"];
const RMETA={}; REGIONS.forEach((r,i)=>{RMETA[r.name]={...r,color:RCOLORS[i%RCOLORS.length]};});
D.forEach(d=>{d.gdp=d.pop*(PERCAP[d.region]||0);});
const MAXPOP=Math.max.apply(null,D.map(d=>d.pop));
const $=id=>document.getElementById(id);
const fmt=n=>n.toLocaleString("en-US");
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
function flag(cc){if(!cc||cc.length!==2)return"🏳️";return String.fromCodePoint(...[...cc.toUpperCase()].map(c=>0x1F1E6+c.charCodeAt(0)-65));}
const CCNAME={RU:"Russia",EE:"Estonia",LV:"Latvia",LT:"Lithuania",PL:"Poland",BY:"Belarus",SK:"Slovakia",UA:"Ukraine",RO:"Romania",BG:"Bulgaria",MD:"Moldova",HU:"Hungary",AT:"Austria",IT:"Italy",SI:"Slovenia",HR:"Croatia",BA:"Bosnia & Herzegovina",FR:"France",CH:"Switzerland",TR:"Türkiye",AL:"Albania",MK:"North Macedonia",YE:"Yemen"};
function money(v){if(v>=1e12)return"$"+(v/1e12).toFixed(2)+"T";if(v>=1e9)return"$"+(v/1e9).toFixed(v>=1e11?0:1)+"B";if(v>=1e6)return"$"+(v/1e6).toFixed(0)+"M";return"$"+fmt(v);}
function people(v){if(v>=1e6)return(v/1e6).toFixed(v>=1e7?0:1)+"M";if(v>=1e3)return(v/1e3).toFixed(0)+"K";return fmt(v);}

$("nat").innerHTML=NAT.map(c=>`<div class="natcard${c[2]?" accent":""}"><div class="n">${c[0]}</div><div class="l">${c[1]}</div></div>`).join("");

let aR=null,aT=null,aL=null,sk="pop",sd="desc",q="";
const TERRAINS=[...new Set(D.map(d=>d.terrain))].sort();
const LAYERS=[...new Set(D.filter(d=>d.layer).map(d=>d.layer))].sort();

function chip(label,active,cls,count){
  const b=document.createElement("button");
  b.className="f"+(cls?" "+cls:"");
  b.setAttribute("aria-pressed",active?"true":"false");
  b.innerHTML=label+(count!=null?` <span class="fc">${count}</span>`:"");
  return b;
}
function buildFilters(){
  const fr=$("fr"); fr.querySelectorAll(".f").forEach(e=>e.remove());
  const all=chip("All regions",aR===null,"all"); all.onclick=()=>{aR=null;render();}; fr.appendChild(all);
  REGIONS.forEach(r=>{
    const c=D.filter(d=>d.region===r.name).length;
    const b=chip(esc(r.name.replace(" · Federal City","")),aR===r.name,null,c);
    b.onclick=()=>{aR=(aR===r.name?null:r.name);render();}; fr.appendChild(b);
  });
  const fl=$("fl"); fl.querySelectorAll(".f").forEach(e=>e.remove());
  const alll=chip("All",aL===null,"all"); alll.onclick=()=>{aL=null;render();}; fl.appendChild(alll);
  const nc=D.filter(d=>d.nelox).length, pc=D.length-nc;
  const bc=chip("On record",aL==="__canon",null,nc); bc.onclick=()=>{aL=(aL==="__canon"?null:"__canon");render();}; fl.appendChild(bc);
  const bp=chip("Open",aL==="__pending",null,pc); bp.onclick=()=>{aL=(aL==="__pending"?null:"__pending");render();}; fl.appendChild(bp);
  const ac=D.filter(d=>d.anachronism).length;
  const ba=chip("⚠ Anachronistic ref",aL==="__anach",null,ac); ba.onclick=()=>{aL=(aL==="__anach"?null:"__anach");render();}; fl.appendChild(ba);
  LAYERS.forEach(l=>{
    const c=D.filter(d=>d.layer===l).length;
    const b=chip(esc(l),aL===l,null,c);
    b.onclick=()=>{aL=(aL===l?null:l);render();}; fl.appendChild(b);
  });
  const ft=$("ft"); ft.querySelectorAll(".f").forEach(e=>e.remove());
  const allt=chip("All terrain",aT===null,"all"); allt.onclick=()=>{aT=null;render();}; ft.appendChild(allt);
  TERRAINS.forEach(t=>{
    const b=chip(t,aT===t); b.onclick=()=>{aT=(aT===t?null:t);render();}; ft.appendChild(b);
  });
}
function sortHeads(){
  document.querySelectorAll("thead th[data-k]").forEach(th=>{
    const on=th.dataset.k===sk;
    if(on){th.dataset.on="1";th.querySelector(".car").textContent=sd==="asc"?"▲":"▼";}
    else{th.removeAttribute("data-on");th.querySelector(".car").textContent="";}
  });
}
function render(){
  buildFilters(); sortHeads();
  let r=D.filter(d=>{
    if(aR&&d.region!==aR)return false;
    if(aT&&d.terrain!==aT)return false;
    if(aL==="__canon"&&!d.nelox)return false;
    if(aL==="__pending"&&d.nelox)return false;
    if(aL==="__anach"&&!d.anachronism)return false;
    if(aL&&aL[0]!=="_"&&d.layer!==aL)return false;
    if(!q)return true;
    return (d.site+" "+d.nelox+" "+d.local+" "+d.local_hint+" "+d.exonym+" "+d.exonym_hint+" "+d.terrain+" "+d.notes+" "+d.region+" "+(CCNAME[d.cc]||d.cc)).toLowerCase().includes(q);
  });
  const num=sk==="pop"||sk==="gdp";
  r.sort((a,b)=>{
    let A=a[sk],B=b[sk];
    if(num)return sd==="asc"?A-B:B-A;
    A=(A||"zzzz").toString();B=(B||"zzzz").toString();
    return sd==="asc"?A.localeCompare(B):B.localeCompare(A);
  });
  $("ct").textContent=fmt(r.length);
  $("cn").textContent=fmt(r.filter(d=>d.nelox).length);
  $("sp").textContent=people(r.reduce((s,d)=>s+d.pop,0));
  $("sg").textContent=money(r.reduce((s,d)=>s+d.gdp,0));
  $("empty").hidden=r.length>0;
  document.querySelector(".tscroll").style.display=r.length?"":"none";
  $("tb").innerHTML=r.map(d=>{
    const m=RMETA[d.region]||{};
    let badge="";
    if(m.status==="federal")badge=`<span class="badge fed">Federal city</span>`;
    else if(m.status==="commonwealth")badge=`<span class="badge com">Commonwealth</span>`;
    const per=(PERCAP[d.region]/1000).toFixed(0);
    const nameCell=d.nelox
      ? `<span class="nlx">${esc(d.nelox)}</span>${d.gloss?`<div class="gloss">${esc(d.gloss)}</div>`:""}${d.layer?`<div style="margin-top:5px"><span class="lay">${esc(d.layer)}</span></div>`:""}`
      : `<span class="pending">—<b>${d.norename?"Arabic — not renamed":"open"}</b></span>${d.hint?`<div class="gloss">route form on record: ${esc(d.hint)}</div>`:""}`;
    const localCell=d.local
      ? `<span class="exo">${esc(d.local)}</span>`
      : `<span class="pending">—<b>open</b></span>${d.local_hint?`<div class="gloss">candidate: ${esc(d.local_hint)}</div>`:""}`;
    const exoCell=d.exonym
      ? `<span class="exo">${esc(d.exonym)}</span>`
      : `<span class="pending">—<b>open</b></span>${d.exonym_hint?`<div class="gloss">candidate: ${esc(d.exonym_hint)}</div>`:""}`;
    const anach=d.anachronism
      ? `<div class="gloss" style="color:#b71d3e;font-style:normal">⚠ cannot be the in-world name: ${esc(d.anachronism)}</div>` : "";
    return `<tr>
      <td class="c-site"><div class="name">${esc(d.site)}${badge}</div><div class="notes">${esc(d.notes)}</div>${anach}</td>
      <td class="hide-md">${localCell}</td>
      <td>${nameCell}</td>
      <td class="hide-md">${exoCell}</td>
      <td class="c-pop"><div class="popn">${fmt(d.pop)}</div><div class="popbar"><i style="width:${Math.max(2,d.pop/MAXPOP*100).toFixed(1)}%"></i></div></td>
      <td class="c-gdp hide-md">${money(d.gdp)}<span class="per">$${per}k/cap</span></td>
      <td class="hide-md"><span class="pill">${esc(d.terrain)}</span></td>
      <td class="hide-lg"><span class="region"><span class="dot" style="background:${m.color}"></span>${esc(d.region.replace(" · Federal City",""))}</span></td>
      <td class="hide-lg"><span class="loc"><span class="flag">${flag(d.cc)}</span>${esc(CCNAME[d.cc]||d.cc)}</span></td>
    </tr>`;
  }).join("");
}
$("q").addEventListener("input",e=>{q=e.target.value.toLowerCase().trim();render();});
$("clr").addEventListener("click",()=>{$("q").value="";q="";$("q").focus();render();});
document.querySelectorAll("thead th[data-k]").forEach(th=>{
  const go=()=>{const k=th.dataset.k;
    if(sk===k){sd=sd==="asc"?"desc":"asc";}else{sk=k;sd=(k==="pop"||k==="gdp")?"desc":"asc";}
    render();};
  th.onclick=go;
  th.onkeydown=e=>{if(e.key==="Enter"||e.key===" "){e.preventDefault();go();}};
});
render();
</script>
</body>
</html>
"""
