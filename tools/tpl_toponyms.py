#!/usr/bin/env python3
"""HTML template for toponyms.html — the Nelôxian city-name roller."""

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nelôxia — city-name roller</title>
<meta name="description" content="Rolls candidate Nelôxi city names on a weighted table of naming strategies — patron, event, descriptive, transferred, folk-etymology, saint, accident — by region and era.">
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
  --shadow:0 1px 2px rgba(20,24,35,.04),0 6px 24px rgba(20,24,35,.06);
  --radius:12px;
}
*{box-sizing:border-box;margin:0;padding:0}
html{background:var(--bg)}
body{background:var(--bg);color:var(--ink);font-family:"General Sans",system-ui,sans-serif;font-size:14.5px;line-height:1.45;-webkit-font-smoothing:antialiased}
.wrap{max-width:1240px;margin:0 auto;padding:0 24px 120px}
.mast{padding:34px 0 14px}
.brandrow{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
.title{font-family:"Cabinet Grotesk","General Sans",sans-serif;font-weight:800;font-size:clamp(26px,3.8vw,40px);letter-spacing:-.032em;line-height:1}
.title .o{color:var(--accent)}
.kicker{font-weight:600;font-size:13px;letter-spacing:.02em;color:var(--ink3)}
.tagline{margin-top:10px;color:var(--ink2);font-size:15px;max-width:78ch}
.tagline b{color:var(--ink);font-weight:600}
.rule{height:1px;background:var(--line);margin:18px 0}

.panel{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:16px 18px}
.modes{display:flex;gap:6px;margin-bottom:14px}
.mode{font-family:inherit;font-size:13.5px;font-weight:600;padding:8px 16px;border-radius:999px;cursor:pointer;background:var(--chip);border:1px solid transparent;color:var(--ink2)}
.mode[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
.mode:focus-visible{outline:2px solid var(--accent);outline-offset:1px}

.ctrls{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}
.fgrp{display:flex;flex-direction:column;gap:5px;flex:1 1 210px;min-width:0}
.fgrp label{font-size:11px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--ink3)}
select,.fgrp input{width:100%;height:42px;padding:0 12px;font-family:inherit;font-size:14.5px;font-weight:500;color:var(--ink);background:var(--raise);border:1px solid var(--line);border-radius:9px}
select:focus,.fgrp input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-weak)}
.go{height:42px;padding:0 22px;border:none;border-radius:9px;background:var(--accent);color:#fff;font-family:inherit;font-size:14.5px;font-weight:600;cursor:pointer;white-space:nowrap}
.go:hover{background:var(--accent2)}
.go:focus-visible{outline:2px solid var(--ink);outline-offset:2px}

.ctx{margin-top:12px;padding-top:12px;border-top:1px solid var(--line2);color:var(--ink2);font-size:13.5px}
.ctx b{color:var(--ink)}
.ctx .warn{color:var(--accent2);font-weight:600}

.sect{margin-top:22px;display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.sect h2{font-family:"Cabinet Grotesk","General Sans";font-weight:800;font-size:19px;letter-spacing:-.02em}
.sect span{color:var(--ink3);font-size:13px}

.cards{margin-top:12px;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:15px 16px;display:flex;flex-direction:column;gap:8px}
.card.keep{border-color:#c9d4e6;background:#f7f9fc}
.nx{font-family:"Zodiak",Georgia,serif;font-weight:500;font-size:25px;letter-spacing:-.01em;line-height:1.1}
.exo{font-size:12.5px;color:var(--ink3)}
.exo b{color:var(--ink2);font-weight:600}
.story{font-size:13.5px;color:var(--ink2);line-height:1.5}
.tags{display:flex;gap:5px;flex-wrap:wrap;margin-top:auto;padding-top:4px}
.tag{font-size:10.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;padding:3px 8px;border-radius:5px;background:var(--chip);color:var(--ink2)}
.tag.s{background:#eaf1ff;color:#2b52c4}
.tag.l{background:#fff2e2;color:#b06a10}
.take{align-self:flex-start;margin-top:4px;font-family:inherit;font-size:12.5px;font-weight:600;padding:6px 13px;border-radius:7px;border:1px solid var(--line);background:var(--raise);color:var(--ink2);cursor:pointer}
.take:hover{border-color:var(--accent);color:var(--accent2);background:var(--accent-weak)}
.take.on{background:var(--ink);border-color:var(--ink);color:#fff}

.basket{margin-top:24px}
.btable{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.btable th{background:var(--raise);font-size:11px;font-weight:600;letter-spacing:.04em;text-transform:uppercase;color:var(--ink3);text-align:left;padding:10px 13px;border-bottom:1px solid var(--line)}
.btable td{padding:10px 13px;border-bottom:1px solid var(--line2);font-size:13.5px;vertical-align:top}
.btable tr:last-child td{border-bottom:none}
.btable .bnx{font-family:"Zodiak",Georgia,serif;font-size:17px}
.drop{border:none;background:transparent;color:var(--ink4);cursor:pointer;font-size:16px;padding:0 4px}
.drop:hover{color:var(--accent)}
.bactions{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.bempty{color:var(--ink3);padding:22px 0;font-size:13.5px}
textarea{width:100%;margin-top:12px;min-height:130px;padding:12px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;line-height:1.6;color:var(--ink);background:var(--raise);border:1px solid var(--line);border-radius:9px;resize:vertical}
.foot{margin-top:26px;color:var(--ink3);font-size:12.5px;line-height:1.65}
.foot b{color:var(--ink2);font-weight:600}
@media(max-width:640px){.fgrp{flex:1 1 100%}}
</style>
</head>
<body><div class="wrap">
<header class="mast">
  <div class="brandrow">
    <h1 class="title">Nel<span class="o">ô</span>xia <span style="color:var(--ink3);font-weight:700">·</span> city-name roller</h1>
    <span class="kicker">TOPONYM GENERATOR</span>
  </div>
  <p class="tagline">Rolls candidate Nelôxi names on a weighted table of <b>seven naming strategies</b> — patron, event, descriptive, transferred, folk-etymology, saint, accident — plus <b>keeping the local name</b>. Weighted by region and era, because a coastal port and an inland estate town do not get named the same way. Every candidate carries the <b>story of why the name exists</b>; you pick, the generator only proposes.</p>
</header>

<div class="panel">
  <div class="modes">
    <button class="mode" id="m-gaz" aria-pressed="true">Gazetteer — name a real city</button>
    <button class="mode" id="m-free" aria-pressed="false">Free roll — invent a place</button>
  </div>
  <div class="ctrls" id="ctrls"></div>
  <div class="ctx" id="ctx"></div>
</div>

<div class="sect"><h2>Candidates</h2><span id="cnt"></span></div>
<div class="cards" id="cards"></div>

<div class="basket">
  <div class="sect"><h2>Picked</h2><span id="bcnt"></span></div>
  <div id="bwrap"></div>
</div>

<p class="foot">
  <b>The rule this tool exists to enforce.</b> A Nelôxi name must differ from the local name by
  <b>meaning or morphology, never by decoration</b> — <i>Milano → Milān</i> is not a name, it is the
  same name with diacritics. Every candidate here is either composed from canon elements, digested
  with a real sound change, a genuine historical/route name, or the local name deliberately kept.
  <b>Guards:</b> <i>î û â</i> are rejected outright (they exist in neither source nor Nelôxi —
  gazetteer.md); name-senses respect §146 (the sea is <i>mer</i> not <i>merd</i>, the quay
  <i>kājô</i> not <i>lōd</i>, the bridge <i>pont</i> not <i>sildô</i>).
  <b>Out of scope:</b> the Yemeni Commonwealth — its toponymy stays Arabic by ruling, a Nelôxi
  overlay sitting <i>beside, never over</i> the local name.
</p>
</div>

<script>
const CITIES = __CITIES__;
const REGIONS = __REGIONS__;

/* ── canon element banks ─────────────────────────────────────────────────────
   Heads are settlement-forming suffixes; feats are landscape words. Glosses are
   the canon name-senses (§146): mer not merd, kājô not lōd, pont not sildô.   */
const HEADS = {
  finnic:[["-sô","river-bend"],["-mō","land"],["-linnô","fortress"],["-itô","settlement"],
          ["-sār","island"],["-rānd","shore"],["-järv","lake"],["-koski","rapids"],
          ["-korbi","backwoods"],["-satām","harbour"],["-mündõ","river-mouth"],["-sū","river-mouth"]],
  lowgerman:[["-bôrk","walled town"],["-hafõn","harbour"],["-hôlm","islet"],["-dôrp","village"],
             ["-markõt","market-town"],["-mündõ","river-mouth"],["-ūsô","works"]],
  scand:[["-vīk","bay"],["-nes","cape"],["-ô","island"],["-fjôrd","sea-inlet"],["-sund","strait"]],
  slavic:[["-grôd","town"],["-ovô","place of"],["-sk","-town"],["-itsô","little settlement"],["-pôl","field-town"]],
  /* institution words: point-foundations, so they belong to patron and saint
     names, never to a colour-plus-feature description ("green college") */
  romance:[["-vīla","chartered estate"],["-kolēgi","college"]],
  baltic:[["-pils","castle"],["-ava","river-town"],["-upõ","stream"],["-kalns","hill"],["-mestô","town"]]
};
const MODS = [["uus","new"],["vana","old"],["sūr","great"],["petīt","little"],["must","black"],
  ["pūn","red"],["sinī","blue"],["rôhī","green"],["grīs","grey"],["nīrô","bright"],["helē","pale"],
  ["kivī","stone"],["sōla","salt"],["raud","iron"],["kuld","gold"],["kalā","fish"],["tūļ","wind"],
  ["nēu","snow"],["jǟ","ice"],["pakā","frost"],["sol","sun"],["kū","moon"],["estēl","star"],
  ["lain","wave"],["tormô","storm"],["nôrd","north"],["sud","south"],["idā","east"],["lǟn","west"],
  ["tyhjā","empty"],["krōm","crooked"]];
/* terrain → the feature-words that fit it, so descriptive names stay truthful */
/* terrain → LOCATABLE features only. Resources and objects (kalā fish, sōla
   salt, raud iron, sol sun, vôrk net, akôr anchor) live in MODS: you can be
   "at the shore" but not "at the fish", and the event strategy puts these in
   the locative. Keeping the two apart is what stops 'peace at the fish'. */
const TERRFEAT = {
  Sea:[["mer","sea"],["rānd","shore"],["satām","harbour"],["kājô","quay"]],
  Bay:[["laht","bay"],["mer","sea"],["satām","harbour"]],
  Lagoon:[["laht","bay"],["rānd","shore"],["satām","harbour"]],
  Strait:[["sund","strait"],["mer","sea"],["pôrta","gate"]],
  Spit:[["rānd","shore"],["sār","island"],["nēm","cape"]],
  Cape:[["nēm","cape"],["nes","cape"],["mer","sea"]],
  Coast:[["rānd","shore"],["mer","sea"],["satām","harbour"]],
  Island:[["sār","island"],["hôlm","islet"],["rānd","shore"]],
  Delta:[["mündõ","river-mouth"],["jôg","river"],["rānd","shore"]],
  Estuary:[["mündõ","river-mouth"],["laht","bay"],["jôg","river"]],
  Liman:[["laht","bay"],["mündõ","river-mouth"],["rānd","shore"]],
  River:[["jôg","river"],["pont","bridge"],["kājô","quay"],["koski","rapids"]],
  Canal:[["kanā","channel"],["lukkô","lock"],["jôg","river"]],
  Lake:[["järv","lake"],["rānd","shore"],["satām","harbour"]],
  Marsh:[["sô","marsh"],["korbi","backwoods"],["jôg","river"]],
  Forest:[["meçā","forest"],["korbi","backwoods"],["kamī","road"]],
  Hill:[["kalns","hill"],["kôrg","height"],["põld","field"]],
  Upland:[["kalns","hill"],["põld","field"],["meçā","forest"]],
  Highland:[["munt","mountain"],["kalns","hill"],["põld","field"]],
  Mountain:[["munt","mountain"],["kalns","hill"],["org","valley"]],
  Valley:[["org","valley"],["jôg","river"],["kamī","road"]],
  Gorge:[["org","valley"],["pôrta","gate"],["jôg","river"]],
  Karst:[["org","valley"],["bīr","well"],["põld","field"]],
  Plateau:[["põld","field"],["kamī","road"],["kalns","hill"]],
  Basin:[["org","valley"],["põld","field"],["järv","lake"]],
  Plain:[["põld","field"],["turg","market"],["kamī","road"]],
  Sand:[["rānd","shore"],["põld","field"],["kamī","road"]],
  Desert:[["bīr","well"],["kamī","road"],["põld","field"]],
  Wadi:[["kanā","channel"],["bīr","well"],["org","valley"]],
  Crater:[["laht","bay"],["munt","mountain"],["satām","harbour"]]
};
/* people: reused from the civil-name generator's pools (assets/app.js) */
const GIVEN = {
  livonian:["Mārta","Pēter","Līna","Jāns","Märt","Anna","Ilze","Jānis","Mārtiņš","Artūrs","Andres"],
  lowgerman:["Hans","Grete","Klaus","Trīne","Jürgen","Gesche","Tönnies","Margrete"],
  slavic:["Ivan","Olga","Dmitri","Natālija","Pavel","Irina","Nikolaj","Marek","Katerina"],
  romance:["Marc","Clara","Ferran","Carles","Rosa","Jordi","Lluís","Pau","Caterina","Elisa"]
};
const FAMILY = {
  livonian:["Kivi","Rānd","Sār","Raud","Kolk","Kur","Põder","Jārv","Kosken"],
  lowgerman:["Smit","Bôrk","Pill","Turm","Strāl","Brün","Müllôr","Torr"],
  slavic:["Kova","Volk","Lis","Grod","Volkov","Petr"],
  romance:["Ponte","Ros","Cort","Mar","Pedr","Roch"]
};
const TITLES = [["amirāl","admiral","who broke the blockade off this coast"],
  ["generāl","general","who held the line here through one winter"],
  ["direktôr","company director","who financed the first quay"],
  ["rektôr","rector","who chartered the school before the town"],
  ["posādnik","trade-city head","who ran the counting-house for forty years"],
  ["batle","mayor","the first to be elected, and the last to be forgiven"],
  ["mytnik","toll-taker","whose ledgers are the town's oldest paper"],
  ["lōts","pilot","who charted the approach nobody else would take"]];
const EVENTS = [["traktāt","treaty","a treaty signed here"],["batāl","battle","a battle fought here"],
  ["vrak","wreck","a ship lost on the approach"],["brand","fire","the fire that took the old town"],
  ["ūv","flood","the flood the dykes did not hold"],["pest","plague","the plague year"],
  ["mirakôl","miracle","a miracle attested in the parish book"],
  ["turg","market","the spring market that used to be held here"],
  ["vôrk","the catch","the season the nets came in full"],
  ["frid","peace","the peace concluded at this crossing"]];
const SAINTS = ["Amīk","Mārta","Pēter","Jāns","Anna","Klarā","Nikolaj","Katerinā","Laurēns","Mīkel"];
/* accidents: [name-fragment, gloss, story] */
const MARGINALIA = [["Äbtīd","not known","a surveyor's marginal 'not known' copied as the name"],
  ["Näekartô","see the chart","a cross-reference on the draft sheet, copied as the name"],
  ["Tyhjä","blank","the name-field was left blank, and 'blank' was filed as the name"],
  ["Samasô","the same","a clerk's ditto mark read as a word"],
  ["Kaksrūnô","two letters","a two-letter abbreviation nobody could expand"]];

const REGPROF = {
 "Karelia & the North":{cult:["finnic","scand"],ch:"reserve",
   w:{patron:6,event:8,desc:30,trans:6,folk:12,saint:2,acc:6,keep:30}},
 "Livonian Core":{cult:["finnic","baltic"],ch:"interior",
   w:{patron:5,event:6,desc:16,trans:5,folk:16,saint:3,acc:7,keep:42}},
 "Lithuanian Spine":{cult:["baltic","finnic","lowgerman"],ch:"port",
   w:{patron:12,event:8,desc:14,trans:10,folk:12,saint:4,acc:6,keep:34}},
 "Prussian–Pomeranian Coast":{cult:["lowgerman","finnic","scand"],ch:"port",
   w:{patron:20,event:10,desc:18,trans:14,folk:8,saint:5,acc:6,keep:19}},
 "Eastern Corridor":{cult:["slavic","baltic"],ch:"frontier",
   w:{patron:8,event:22,desc:12,trans:6,folk:14,saint:4,acc:8,keep:26}},
 "Moldavian Arc & Black Sea":{cult:["slavic","romance","finnic"],ch:"frontier",
   w:{patron:12,event:18,desc:12,trans:12,folk:10,saint:8,acc:7,keep:21}},
 "Pannonian Bridge":{cult:["slavic","baltic"],ch:"interior",
   w:{patron:6,event:8,desc:10,trans:5,folk:18,saint:6,acc:8,keep:39}},
 "Alpine–Adriatic Arm":{cult:["lowgerman","romance"],ch:"romance",
   w:{patron:12,event:8,desc:14,trans:8,folk:10,saint:16,acc:6,keep:26}},
 "Dalmatian Coast":{cult:["romance","slavic"],ch:"romance",
   w:{patron:14,event:8,desc:12,trans:12,folk:8,saint:20,acc:6,keep:20}},
 "Western Alpine & Riviera Arc":{cult:["romance"],ch:"romance",
   w:{patron:16,event:8,desc:10,trans:12,folk:8,saint:22,acc:6,keep:18}},
 "Thracian–Macedonian Corridor":{cult:["slavic","romance"],ch:"frontier",
   w:{patron:8,event:18,desc:10,trans:6,folk:14,saint:10,acc:8,keep:26}},
 "Sevastopol · Federal City":{cult:["finnic","romance"],ch:"port",
   w:{patron:24,event:14,desc:24,trans:8,folk:4,saint:4,acc:4,keep:18}}
};
const ERAS = {
 hanseatic:{name:"Hanseatic (1300–1600)",m:{desc:1.8,saint:1.6,folk:1.3,patron:.5,trans:.8,event:1,acc:1,keep:1.2}},
 charter:{name:"Charter era (1600–1800)",m:{patron:1.9,event:1.6,saint:1.2,desc:.9,trans:1.1,folk:1,acc:1,keep:.9}},
 rail:{name:"Rail & industry (1800–1900)",m:{patron:1.7,trans:1.7,desc:1.2,event:1,acc:1.2,folk:.7,saint:.6,keep:.7}},
 federal:{name:"Federal / modern (1900–)",m:{patron:1.5,event:1.2,desc:1.3,trans:1.2,acc:1,folk:.6,saint:.5,keep:.8}}
};

const $=id=>document.getElementById(id);
const pick=a=>a[Math.floor(Math.random()*a.length)];
const cap=s=>s.charAt(0)+s.slice(1);
const up=s=>s.charAt(0).toUpperCase()+s.slice(1);
/* canon locative: vowel-final +l, consonant-final +ôl (assets/app.js) */
const loc=w=>/[aeiouäöüõôāēīōūǟȫ]$/.test(w)?w+"l":w+"ôl";
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

/* ── guards ─────────────────────────────────────────────────────────────────
   1. î û â exist in neither source nor Nelôxi: errors, not fossils.
   2. §146 name-senses: merd / lōd / sildô must never appear in a name.       */
const BANNED_CHARS=/[îûâÎÛÂ]/;
const BANNED_SENSE=/(merd|lōd|sildô)/i;
function valid(nx){ return !BANNED_CHARS.test(nx) && !BANNED_SENSE.test(nx); }

function headOf(cults){ return pick(HEADS[pick(cults)]); }
/* heads a plain description may take — landscape and settlement words only.
   Institution heads (-kolēgi, -vīla) are point-foundations: they need a founder
   or a patron saint behind them, not a colour. */
function plainHeadOf(cults){
  const c=cults.filter(k=>k!=="romance");
  return pick(HEADS[pick(c.length?c:["finnic"])]);
}
function featOf(terrain){ return pick(TERRFEAT[terrain]||TERRFEAT.Plain); }
/* join a modifier to a head-suffix, head-final like all Nelôxi compounds */
function joinHead(stem,head){ return up(stem)+head.replace(/^-/,""); }

/* ── the seven strategies + retain ──────────────────────────────────────────
   Each returns {nx, layer, strategy, story}. The story is the point: it says
   WHY the name exists, which is what makes a candidate pickable.            */
const STRAT = {
 patron(c){
   const cult=pick(c.cults), t=pick(TITLES);
   const fam=pick(FAMILY[cult]||FAMILY.livonian), giv=pick(GIVEN[cult]||GIVEN.livonian);
   const r=Math.random();
   if(r<.45){ const h=headOf(c.cults);
     return {nx:joinHead(fam,h[0]),layer:"hybrid",strategy:"patron",
       story:`for ${t[1]} ${giv} ${fam}, ${t[2]}; the ${h[1]} took the family name.`}; }
   if(r<.7){ const h=headOf([cult==="slavic"?"slavic":"finnic"]);
     return {nx:joinHead(t[0],h[0]),layer:"native",strategy:"patron",
       story:`named for the office, not the man — the ${t[1]}'s ${h[1]}. ${up(giv)} ${fam} held it first.`}; }
   if(r<.85) return {nx:fam+"ovô",layer:"hybrid",strategy:"patron",
     story:`Slavic possessive: '${fam}'s place'. ${t[1]} ${giv} ${fam} ${t[2]}.`};
   return {nx:"Kunis"+headOf(["finnic","lowgerman"])[0].replace(/^-/,""),layer:"hybrid",strategy:"patron",
     story:`a crown foundation — kunis- 'king's', the same element as Kunislinnô.`};
 },
 event(c){
   const e=pick(EVENTS), r=Math.random();
   if(r<.4){ const h=headOf(c.cults);
     return {nx:joinHead(e[0],h[0]),layer:"native",strategy:"event",
       story:`${e[2]}; the ${h[1]} kept the word and lost the memory.`}; }
   if(r<.7){ const f=featOf(c.terrain);
     return {nx:up(e[0])+loc(f[0]),layer:"native",strategy:"event",
       story:`${e[2]} — literally '${e[1]} at the ${f[1]}'. Fossilized as one word.`}; }
   /* fossilization: clip the phrase until it stops meaning anything */
   const f=featOf(c.terrain), full=up(e[0])+f[0];
   return {nx:full.slice(0,Math.max(5,full.length-2)),layer:"native",strategy:"event",
     story:`${e[2]}. The full phrase was '${e[1]} ${f[1]}' — four centuries clipped it to this, and nobody now hears the event in it.`};
 },
 desc(c){
   const f=featOf(c.terrain), r=Math.random();
   if(r<.5){ const m=pick(MODS);
     return {nx:up(m[0])+f[0],layer:"native",strategy:"descriptive",
       story:`plain description: '${m[1]} ${f[1]}'. What the first surveyors wrote down.`}; }
   const h=plainHeadOf(c.cults), m=pick(MODS);
   return {nx:joinHead(m[0],h[0]),layer:c.cults[0]==="finnic"?"native":"hybrid",strategy:"descriptive",
     story:`'${m[1]} ${h[1]}' — the feature that mattered when the charter was drawn.`};
 },
 trans(c){
   const donors=CITIES.filter(d=>d.nelox&&d.region!==c.region);
   if(!donors.length) return STRAT.desc(c);
   const d=pick(donors), r=Math.random();
   /* don't build Uus-uusatôm: skip the prefix when the donor already carries it */
   if(r<.45 && !/^uus/i.test(d.nelox)) return {nx:"Uus"+d.nelox.toLowerCase(),layer:"native",strategy:"transferred",
     story:`settlers out of ${d.nelox} (${d.site}) named it for home — uus- 'new', the Uusatôm pattern.`};
   if(r<.7) return {nx:"Nova "+d.nelox,layer:"hybrid",strategy:"transferred",
     story:`the Romance settler-pattern 'Nova + homeland', as Nova Trentô. The founders came from ${d.nelox} (${d.site}).`};
   return {nx:d.nelox,layer:"native",strategy:"transferred",
     story:`the name travelled and the meaning did not: carried whole from ${d.nelox} (${d.site}) by its founders, ${Math.random()<.5?"and most people here have no idea it is a borrowed name":"who never explained it"}.`};
 },
 folk(c){
   /* the local name misheard and re-analysed as Nelôxi words it resembles,
      producing a confident WRONG meaning nobody questions */
   const src=(c.site||"").replace(/[^A-Za-zÀ-ɏ]/g," ").split(" ")[0]||"Nam";
   const a=src.slice(0,2).toLowerCase();
   let m=MODS.filter(x=>x[0][0]===a[0]); if(!m.length) m=MODS;
   const w=pick(m), f=featOf(c.terrain);
   const nx=up(w[0])+f[0];
   return {nx:nx,layer:"nativized",strategy:"folk-etymology",
     story:`nobody renamed it — '${src}' was simply misheard as ${w[0]} '${w[1]}' + ${f[0]} '${f[1]}', and the wrong reading has been the official one so long that the false meaning is taught in the local school.`};
 },
 saint(c){
   const s=pick(SAINTS), r=Math.random();
   if(r<.45) return {nx:"Sant"+s.toLowerCase(),layer:"hybrid",strategy:"saint",
     story:`a monastery foundation — sant- 'saint', the Santamīk pattern; the house of Saint ${s}.`};
   if(r<.7) return {nx:"Sent "+s,layer:"hybrid",strategy:"saint",
     story:`the parish predates the town: Saint ${s}'s, and the settlement took the church's name.`};
   if(r<.85) return {nx:"Sveti "+s,layer:"raw loan",strategy:"saint",
     story:`the Orthodox layer, kept in its own form — Sveti ${s}, as the local rite named it.`};
   return {nx:"Mônt"+s.toLowerCase(),layer:"hybrid",strategy:"saint",
     story:`mônt- 'hill-foundation' + the patron: the shrine on the height above the town.`};
 },
 acc(c){
   const r=Math.random();
   if(r<.4){ const m=pick(MARGINALIA);
     return {nx:m[0],layer:"native",strategy:"accident",
       story:`${m[2]} — it means '${m[1]}' and it has been the legal name since the survey was bound.`}; }
   if(r<.7){ const src=(c.site||"Nam").replace(/[^A-Za-zÀ-ɏ]/g,"");
     const cut=src.slice(0,Math.max(3,Math.ceil(src.length/2)));
     return {nx:up(cut)+"ô",layer:"nativized",strategy:"accident",
       story:`the copyist's hand ran off the edge of the sheet: '${src}' was entered as this, and the truncation was never queried.`}; }
   const src=(c.site||"Nam").replace(/[^A-Za-zÀ-ɏ]/g,"");
   const sw=src.length>3?src.slice(0,1)+src[2]+src[1]+src.slice(3):src;
   return {nx:up(sw.toLowerCase()),layer:"nativized",strategy:"accident",
     story:`two letters transposed in the first printed atlas. The atlas outsold the correction.`};
 },
 keep(c){
   const why = c.ch==="interior"
     ? "the gravity principle: the Finnic layer belongs to the water, and this is estate-and-upland country. The state never had a reason to rename it."
     : c.ch==="frontier"
     ? "an inland seam — the corridor's names stay raw and Slavic by design; renaming here would read as erasure, not administration."
     : c.ch==="romance"
     ? "the route already had a name in the language of whoever charted the coast, and the merchants kept using it."
     : "held raw as a fossil: the spelling preserves whoever named the place, foreign scars and all.";
   return {nx:c.site,layer:"raw loan",strategy:"retained",story:why,keep:true};
 }
};
const LABEL={patron:"Patron",event:"Event",desc:"Descriptive",trans:"Transferred",
  folk:"Folk-etymology",saint:"Saint",acc:"Accident",keep:"Keep local"};

function weights(prof,era){
  const m=ERAS[era].m, out=[];
  for(const k in prof.w){
    const key = k==="keep"?"keep":k;
    out.push([k, prof.w[k]*(m[key]!==undefined?m[key]:1)]);
  }
  return out;
}
function rollStrategy(prof,era,forceWild){
  if(forceWild) return pick(["patron","event","desc","trans","folk","saint","acc"]);
  const w=weights(prof,era), tot=w.reduce((s,x)=>s+x[1],0);
  let r=Math.random()*tot;
  for(const [k,v] of w){ if((r-=v)<=0) return k; }
  return "desc";
}

/* one candidate; retries until it passes the orthographic + sense guards */
function roll(ctx,prof,era){
  for(let i=0;i<24;i++){
    const wild = Math.random()<0.04;                 /* ~4% cross-culture wildcard */
    const key = rollStrategy(prof,era,wild);
    const cults = wild ? [pick(Object.keys(HEADS))] : prof.cult;
    const c = Object.assign({},ctx,{cults:cults,ch:prof.ch});
    const r = STRAT[key](c);
    if(!valid(r.nx)) continue;
    if(!r.keep && ctx.site && r.nx.toLowerCase()===ctx.site.toLowerCase()) continue;
    r.key=key; r.wild=wild&&key!=="keep";
    r.exonym = r.keep ? ctx.exonym : (ctx.exonym||ctx.site||"—");
    return r;
  }
  return Object.assign(STRAT.keep(Object.assign({},ctx,{cults:prof.cult,ch:prof.ch})),{key:"keep"});
}

/* ── state ────────────────────────────────────────────────────────────────── */
let mode="gaz", basket=[];
const ROLLABLE = CITIES.filter(d=>!d.norename);

function controls(){
  const eraOpts=Object.keys(ERAS).map(k=>`<option value="${k}">${esc(ERAS[k].name)}</option>`).join("");
  if(mode==="gaz"){
    const groups={};
    ROLLABLE.forEach(d=>{ (groups[d.region]=groups[d.region]||[]).push(d); });
    let opts="";
    Object.keys(groups).forEach(rg=>{
      opts+=`<optgroup label="${esc(rg)}">`;
      groups[rg].sort((a,b)=>b.pop-a.pop).forEach(d=>{
        const mark=d.canon?" ✓":"";
        opts+=`<option value="${esc(d.site)}">${esc(d.site)}${mark}</option>`;
      });
      opts+="</optgroup>";
    });
    $("ctrls").innerHTML=
      `<div class="fgrp"><label for="city">City (✓ = already canon)</label><select id="city">${opts}</select></div>`+
      `<div class="fgrp"><label for="era">Era</label><select id="era">${eraOpts}</select></div>`+
      `<button class="go" id="go">Roll 8 names</button>`;
    $("city").addEventListener("change",draw);
  } else {
    const rgOpts=Object.keys(REGPROF).map(k=>`<option value="${esc(k)}">${esc(k)}</option>`).join("");
    const tOpts=Object.keys(TERRFEAT).sort().map(t=>`<option value="${t}">${t}</option>`).join("");
    $("ctrls").innerHTML=
      `<div class="fgrp"><label for="rg">Region</label><select id="rg">${rgOpts}</select></div>`+
      `<div class="fgrp"><label for="tr">Terrain</label><select id="tr">${tOpts}</select></div>`+
      `<div class="fgrp"><label for="nm">Local name (optional)</label><input id="nm" placeholder="e.g. Vilkija" autocomplete="off"></div>`+
      `<div class="fgrp"><label for="era">Era</label><select id="era">${eraOpts}</select></div>`+
      `<button class="go" id="go">Roll 8 names</button>`;
    $("rg").addEventListener("change",draw); $("tr").addEventListener("change",draw);
  }
  $("era").addEventListener("change",draw);
  $("go").addEventListener("click",draw);
}

function context(){
  if(mode==="gaz"){
    const d=ROLLABLE.find(x=>x.site===$("city").value)||ROLLABLE[0];
    return {site:d.site,region:d.region,terrain:d.terrain,notes:d.notes,exonym:d.exonym,
            canon:d.canon,nelox:d.nelox,layer:d.layer,gloss:d.gloss,hint:d.hint,pop:d.pop};
  }
  const nm=($("nm").value||"").trim();
  return {site:nm,region:$("rg").value,terrain:$("tr").value,notes:"",exonym:nm,
          canon:false,nelox:"",layer:"",gloss:"",hint:"",pop:0};
}

function drawCtx(ctx,prof,era){
  const w=weights(prof,era).slice().sort((a,b)=>b[1]-a[1]);
  const tot=w.reduce((s,x)=>s+x[1],0);
  const mix=w.map(([k,v])=>`${LABEL[k]} ${Math.round(v/tot*100)}%`).join(" · ");
  let h="";
  if(mode==="gaz"){
    h+=`<b>${esc(ctx.site)}</b> — ${esc(ctx.terrain)}; ${esc(ctx.notes)}. `;
    h+=`Outsiders call it <b>${esc(ctx.exonym)}</b>. `;
    if(ctx.canon) h+=`<span class="warn">Already canon as ${esc(ctx.nelox)}</span> (${esc(ctx.layer)}${ctx.gloss?" — "+esc(ctx.gloss):""}) — from world/gazetteer.md; rolling here would replace a ratified name. `;
    else h+=`No Nelôxi name yet — an open docket. `;
    if(ctx.hint) h+=`Historical/route form on record: <b>${esc(ctx.hint)}</b>. `;
  }
  h+=`<br><span style="color:var(--ink3)">Strategy mix for ${esc(prof.ch)} · ${esc(ERAS[era].name)}: ${mix}</span>`;
  $("ctx").innerHTML=h;
}

function draw(){
  const ctx=context();
  const prof=REGPROF[ctx.region]||REGPROF["Livonian Core"];
  const era=$("era").value;
  drawCtx(ctx,prof,era);

  const out=[];
  /* the hint, where one exists, is always offered as a real raw-loan candidate */
  if(ctx.hint) out.push({nx:ctx.hint,layer:"raw loan",strategy:"historical",key:"hist",
    exonym:ctx.exonym,story:`the genuine historical / trade-route form already on record for this place — the name the routes actually carried.`});
  /* eight DISTINCT candidates — a repeated name wastes a card */
  for(let guard=0; out.length<8 && guard<80; guard++){
    const r=roll(ctx,prof,era);
    if(!out.some(o=>o.nx===r.nx)) out.push(r);
  }
  /* guarantee the keep-local option is present */
  if(!out.some(o=>o.key==="keep")&&ctx.site){
    out[out.length-1]=Object.assign(STRAT.keep(Object.assign({},ctx,{cults:prof.cult,ch:prof.ch})),
      {key:"keep",exonym:ctx.exonym});
  }

  $("cnt").textContent=`${out.length} for ${ctx.site||"a new place"}`;
  $("cards").innerHTML=out.map((o,i)=>{
    const inB=basket.some(b=>b.nx===o.nx&&b.site===(ctx.site||""));
    return `<div class="card${o.key==="keep"?" keep":""}">
      <div class="nx">${esc(o.nx)}</div>
      <div class="exo">exonym <b>${esc(o.exonym||"—")}</b></div>
      <div class="story">${esc(o.story)}</div>
      <div class="tags">
        <span class="tag s">${esc(LABEL[o.key]||o.strategy)}</span>
        <span class="tag l">${esc(o.layer)}</span>
        ${o.wild?'<span class="tag">wildcard</span>':""}
      </div>
      <button class="take${inB?" on":""}" data-i="${i}">${inB?"✓ picked":"Pick this"}</button>
    </div>`;
  }).join("");

  $("cards").querySelectorAll(".take").forEach(b=>{
    b.addEventListener("click",()=>{
      const o=out[+b.dataset.i];
      const key=o.nx+"|"+(ctx.site||"");
      const at=basket.findIndex(x=>x.nx+"|"+x.site===key);
      if(at>=0) basket.splice(at,1);
      else basket.push({site:ctx.site||"(new)",region:ctx.region,nx:o.nx,
        exonym:o.exonym||"",layer:o.layer,strategy:LABEL[o.key]||o.strategy,story:o.story});
      draw(); drawBasket();
    });
  });
}

function drawBasket(){
  $("bcnt").textContent=basket.length?`${basket.length} name${basket.length>1?"s":""}`:"";
  if(!basket.length){ $("bwrap").innerHTML=`<div class="bempty">Nothing picked yet. Pick candidates and they collect here as copyable rows.</div>`; return; }
  $("bwrap").innerHTML=
    `<table class="btable"><thead><tr><th>Settlement</th><th>Nelôxi name</th><th>Exonym</th><th>Layer</th><th>Strategy</th><th></th></tr></thead><tbody>`+
    basket.map((b,i)=>`<tr><td>${esc(b.site)}</td><td class="bnx">${esc(b.nx)}</td><td>${esc(b.exonym)}</td><td>${esc(b.layer)}</td><td>${esc(b.strategy)}</td><td><button class="drop" data-i="${i}" aria-label="Remove">×</button></td></tr>`).join("")+
    `</tbody></table>
     <div class="bactions"><button class="go" id="copy">Copy as TSV</button>
     <button class="take" id="clear">Clear all</button></div>
     <textarea id="tsv" readonly spellcheck="false"></textarea>`;
  const tsv="site\tnelox\texonym\tlayer\tstrategy\tgloss\n"+
    basket.map(b=>[b.site,b.nx,b.exonym,b.layer,b.strategy,b.story].join("\t")).join("\n");
  $("tsv").value=tsv;
  $("bwrap").querySelectorAll(".drop").forEach(x=>x.addEventListener("click",()=>{
    basket.splice(+x.dataset.i,1); draw(); drawBasket();
  }));
  $("copy").addEventListener("click",()=>{
    const t=$("tsv"); t.select();
    try{ navigator.clipboard.writeText(tsv); }catch(e){ document.execCommand("copy"); }
    $("copy").textContent="Copied ✓"; setTimeout(()=>$("copy").textContent="Copy as TSV",1400);
  });
  $("clear").addEventListener("click",()=>{ basket=[]; draw(); drawBasket(); });
}

function setMode(m){
  mode=m;
  $("m-gaz").setAttribute("aria-pressed",m==="gaz");
  $("m-free").setAttribute("aria-pressed",m==="free");
  controls(); draw();
}
$("m-gaz").addEventListener("click",()=>setMode("gaz"));
$("m-free").addEventListener("click",()=>setMode("free"));
setMode("gaz"); drawBasket();
</script>
</body>
</html>
"""
