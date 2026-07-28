#!/usr/bin/env python3
"""Generate numbers.html — the Nelôxi dozenal number page.

Everything on the page comes from grammar/12-numbers.md (charter §37, §74–§75,
§77, §80). The page is self-contained and works from a file:// path.

Two things it does that the prose module cannot: it composes ANY number into its
Nelôxi form, and it reads a Nelôxi number back to a value. The reader is
self-verifying — it re-composes whatever it parsed and refuses the answer if the
two do not match, so it can never report a wrong value quietly.

Usage: python3 tools/build_numbers.py
"""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nelôxi — numbers</title>
<meta name="description" content="The Nelôxi dozenal number system: the digits, the powers of twelve, the fused teens, and a converter that composes any number into its Nelôxi form.">
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
html{background:var(--bg);-webkit-text-size-adjust:100%}
body{background:var(--bg);color:var(--ink);font-family:"General Sans",system-ui,-apple-system,sans-serif;font-size:14.5px;line-height:1.45;-webkit-font-smoothing:antialiased}
.wrap{max-width:1120px;margin:0 auto;padding:0 24px 120px}
.mast{padding:34px 0 14px}
.brandrow{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}
.title{font-family:"Cabinet Grotesk","General Sans",sans-serif;font-weight:800;font-size:clamp(28px,4.2vw,46px);letter-spacing:-.032em;line-height:1}
.title .o{color:var(--accent)}
.kicker{font-weight:600;font-size:13px;letter-spacing:.02em;color:var(--ink3);text-transform:uppercase}
.tagline{margin-top:10px;color:var(--ink2);font-size:15px;max-width:76ch}
.tagline b{color:var(--ink);font-weight:600}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow)}
h2{font-family:"Cabinet Grotesk","General Sans",sans-serif;font-weight:800;font-size:19px;letter-spacing:-.02em;margin:34px 0 12px}
h2 .sub{font-family:"General Sans";font-weight:500;font-size:13px;color:var(--ink3);margin-left:9px;letter-spacing:0}

/* converter */
.conv{padding:20px;margin-top:20px}
.inrow{display:flex;gap:10px;flex-wrap:wrap}
.inrow .f{position:relative;flex:1 1 320px}
#q{width:100%;height:56px;padding:0 16px;font-family:"Zodiak",Georgia,serif;font-size:22px;font-weight:500;color:var(--ink);background:var(--surface);border:1px solid var(--line);border-radius:10px}
#q::placeholder{font-family:"General Sans";font-size:16px;font-weight:400;color:var(--ink4)}
#q:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-weak)}
.seg{display:flex;gap:4px;align-items:center;background:var(--chip);border-radius:999px;padding:4px}
.seg button{font-family:ui-monospace,Menlo,monospace;font-size:14px;font-weight:600;padding:6px 13px;border:none;border-radius:999px;background:transparent;color:var(--ink2);cursor:pointer;display:flex;flex-direction:column;align-items:center;line-height:1.25;letter-spacing:.08em}
.seg button .gl{font-family:"General Sans";font-size:9.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--ink4);margin-top:1px}
.seg button[aria-pressed="true"]{background:var(--ink);color:#fff}
.seg button[aria-pressed="true"] .gl{color:rgba(255,255,255,.6)}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-top:12px}
.chips button{font-family:inherit;font-size:12.5px;font-weight:500;padding:6px 11px;border:1px solid transparent;border-radius:999px;background:var(--chip);color:var(--ink2);cursor:pointer}
.chips button:hover{background:var(--chip-hover);color:var(--ink)}
.read{margin-top:14px;font-size:12.5px;color:var(--ink3)}
.read b{color:var(--ink2);font-weight:600}
.bad{color:var(--accent2);font-weight:600}

.out{margin-top:16px;border-top:1px solid var(--line2);padding-top:18px}
.hero{font-family:"Zodiak",Georgia,serif;font-weight:500;font-size:clamp(24px,4.4vw,40px);line-height:1.15;letter-spacing:-.01em}
.heroline{margin-top:8px;color:var(--ink3);font-size:13px}
.heroline code{font-family:ui-monospace,Menlo,monospace;font-size:12.5px;background:var(--chip);padding:2px 6px;border-radius:5px;color:var(--ink2)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(215px,1fr));gap:1px;margin-top:20px;background:var(--line2);border:1px solid var(--line2);border-radius:10px;overflow:hidden}
.cell{background:var(--surface);padding:13px 15px}
.cell .l{font-size:10.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--ink3)}
.cell .v{font-family:"Zodiak",Georgia,serif;font-size:18px;margin-top:5px;word-break:break-word}
.cell .n{font-size:12px;color:var(--ink3);margin-top:3px}
.cell.mono .v{font-family:ui-monospace,Menlo,monospace;font-size:19px;font-weight:500;letter-spacing:.04em}
.cell.off .v{color:var(--ink4);font-family:"General Sans";font-size:14px}

/* tables */
table{width:100%;border-collapse:collapse}
.tcard{overflow:hidden}
.tscroll{overflow-x:auto}
th{font-size:11px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--ink3);text-align:left;padding:11px 15px;border-bottom:1px solid var(--line);background:var(--raise);white-space:nowrap}
td{padding:10px 15px;border-bottom:1px solid var(--line2);vertical-align:baseline}
tr:last-child td{border-bottom:none}
td.fig{font-family:ui-monospace,Menlo,monospace;font-weight:500;color:var(--ink2);white-space:nowrap}
td.nx{font-family:"Zodiak",Georgia,serif;font-size:17px;white-space:nowrap}
td.en{color:var(--ink2)}
td.note{color:var(--ink3);font-size:13px}

/* the 144 grid */
.dozgrid{display:grid;grid-template-columns:repeat(12,1fr);gap:1px;background:var(--line2);border:1px solid var(--line2);border-radius:10px;overflow:hidden;min-width:840px}
.dz{background:var(--surface);padding:7px 6px 8px;text-align:center;cursor:pointer}
.dz:hover{background:var(--accent-weak)}
.dz .f{font-family:ui-monospace,Menlo,monospace;font-size:11px;color:var(--ink4)}
.dz .w{font-family:"Zodiak",Georgia,serif;font-size:12.5px;margin-top:2px;line-height:1.2;word-break:break-word}
.dz.zero{background:var(--raise)}
.dz.roll .f{color:var(--accent);font-weight:700}
.hint{margin-top:9px;font-size:12.5px;color:var(--ink3)}
.hint code{font-family:ui-monospace,Menlo,monospace;background:var(--chip);padding:1px 5px;border-radius:4px}
.foot{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);color:var(--ink3);font-size:12.5px}
.foot a{color:var(--accent2);font-weight:600;text-decoration:none}
.foot a:hover{text-decoration:underline}
.open{margin-top:14px;padding:13px 16px;background:#fff8ec;border:1px solid #f0dfc0;border-radius:10px;font-size:13px;color:#6b5326}
.open b{color:#4c3a15}
@media (max-width:640px){.wrap{padding:0 16px 90px}.conv{padding:16px}}
</style>
</head>
<body>
<div class="wrap">

<header class="mast">
  <div class="brandrow">
    <h1 class="title">Nel<span class="o">ô</span>xi &middot; numbers</h1>
    <span class="kicker">base twelve</span>
  </div>
  <p class="tagline">Nelôxi counts in <b>twelves</b>. Twelve is the round number the way ten is in
  English, the digits are Slavic, and the powers of twelve each have their own word. Type any
  number below &mdash; decimal, a dozenal figure, or Nelôxi words.</p>
</header>

<section class="card conv">
  <div class="inrow">
    <div class="f"><input id="q" value="144" autocomplete="off" spellcheck="false"
      placeholder="a number, a dozenal figure, or Nelôxi words"></div>
    <div class="seg" id="glyphseg" title="Ten and eleven"></div>
  </div>
  <div class="read" id="glyphnote"></div>
  <div class="chips" id="chips"></div>
  <div class="read" id="read"></div>
  <div class="out" id="out"></div>
</section>

<h2>The digits<span class="sub">0&ndash;11</span></h2>
<div class="card tcard"><div class="tscroll"><table id="tdig"></table></div></div>

<h2>Where counting rolls over<span class="sub">the powers of twelve</span></h2>
<div class="card tcard"><div class="tscroll"><table id="tpow"></table></div></div>

<h2>The dozens are packets<span class="sub">each a thing that came in that quantity &mdash; no two share a root</span></h2>
<div class="card tcard"><div class="tscroll"><table id="tpack"></table></div></div>
<p class="hint"><b>langhunt</b> is 120, not 144 &mdash; the Germanic long hundred really was ten
dozen (charter &sect;37, adopted for divisibility). So the word that looks like &ldquo;hundred&rdquo;
is not the round number of the system. The round number is <b>gros&ocirc;</b>.</p>

<h2>The fused teens<span class="sub">13&ndash;23 &middot; one word each, <i>düna</i> erodes to <i>dün-</i></span></h2>
<div class="card tcard"><div class="tscroll"><table id="tteen"></table></div></div>

<h2>Round figures, and the misreading they cause<span class="sub">a Nel&ocirc;xian round number looks foreign and is worth more</span></h2>
<div class="card tcard"><div class="tscroll"><table id="tround"></table></div></div>
<p class="hint">The error is not random &mdash; it is <b>exactly a fifth per place</b>. A figure
misread as decimal comes out short by 1.2&#8319;. Six places and the outside world has under-read
you by a factor of three. A figure with a <code>D</code> or an <code>E</code> in it at least
announces itself; <code>1000</code> does not.</p>

<h2>Nought to a gross<span class="sub">0&ndash;143 &middot; each row is a dozen; click any cell</span></h2>
<div class="tscroll"><div class="dozgrid" id="dozgrid"></div></div>
<p class="hint">Twelve rows of twelve. The left column is where the figure gains a place
(<code>10</code>, <code>20</code>, <code>30</code>&hellip;), and the last cell is
<code>EE</code> &mdash; 143, the number before a gross.</p>

<h2>Building past twenty-three<span class="sub">bare juxtaposition, largest unit first</span></h2>
<div class="card tcard"><div class="tscroll"><table id="tex"></table></div></div>

<h2>What you do with a number once you have it</h2>
<div class="card tcard"><div class="tscroll"><table id="tuse"></table></div></div>

<h2>Percent is per <i>gross</i><span class="sub">100 = 12² = 144, so the figures do not match decimal ones</span></h2>
<div class="card tcard"><div class="tscroll"><table id="tpct"></table></div></div>

<h2>The clock<span class="sub">24-hour, dozenal, with <i>klôk</i> &mdash; no a.m./p.m.</span></h2>
<div class="card tcard"><div class="tscroll"><table id="tclk"></table></div></div>

<div class="open" id="openq"></div>

<p class="foot">Every form on this page comes from <b>grammar/12-numbers.md</b> (charter §37,
§74&ndash;§75, §77, §80). The withdrawn Finnic (<i>üks, kaks, kolm&hellip;</i>) and Germanic
(<i>ēn, twē, drē&hellip;</i>) numerals are not used here and are not canon.
&nbsp;·&nbsp; <a href="index.html#/numbers">the grammar module</a></p>

</div>
<script>
"use strict";
/* ── canon ─────────────────────────────────────────────────────────────────── */
/* Latin, inherited through Habsburg chancery Latin and re-based from ten to twelve. */
const DIG  = ["nul","ūn","duô","trē","kvatôr","kvīnk","sex","septôm","oktô","novôm","deçôm","undeçôm"];
const EN   = ["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven"];
const LAT  = ["nullus","unus","duo","tres","quattuor","quinque","sex","septem","octo","novem","decem","undecim"];
/* no fused teens: 13–23 are duodeç + digit, two words */
const DUNA="duodeç", GROSO="çent", MIRO="mīl", MILJON="milj";
/* The Latin -ginta series re-pointed from ten to twelve: viginti is no longer
   2x10 but 2x12. Latin had no *decaginta* — it jumped to centum, because in
   base ten 10x10 IS the square. Base twelve needs 10x and 11x, so those two are
   regularised onto the same series. deçāgint is the long hundred. */
const PACK={ 2:["vigint","viginti"], 3:["trigint","triginta"], 4:["kvadrāgint","quadraginta"],
             5:["kvīnkvāgint","quinquaginta"], 6:["sexāgint","sexaginta"],
             7:["septvāgint","septuaginta"], 8:["oktōgint","octoginta"],
             9:["nonāgint","nonaginta"],
            10:["deçāgint","regularised — the long hundred; Latin had no *decaginta*"],
            11:["undeçāgint","regularised on the -ginta series"] };
/* centum is the square of the base and mille the cube — the words keep their
   POSITION and change their value: çent is 144, mīl is 1,728. */
const SCALE=["", MIRO, MILJON, "bilj", "trilj"];
const TRIAD=1728, MAXN=Math.pow(1728,5)-1;

/* Ten and eleven are D and E, from deseñç and elva — the only pair that is on
   every machine that has to print a tariff. The others are registers, not
   rivals: turned digits for inscriptions, Cyrillic for the Sarmatian fork. */
const GLYPHS={ "Printed":["D","E"], "Ceremonial":["↊","↋"], "Sarmatian":["Д","Е"] };
const GLYPHNOTE={
  "Printed":"the standard — <b>D</b> from <i>deseñç</i>, <b>E</b> from <i>elva</i>; sets in any type, punches on any card",
  "Ceremonial":"the turned digits, cut for foundation stones and the Bourse frieze. Never in a document that must be reproduced.",
  "Sarmatian":"the eastern fork writes in full Cyrillic, so its two extra digits are <b>Д</b> and <b>Е</b>"
};
let glyph="Printed";

/* ── composing a number ────────────────────────────────────────────────────── */
/* 0–1727: the grosô digit, then the dozens-and-units remainder */
function triad(n){
  const g=Math.floor(n/144), r=n%144, out=[];
  if(g) out.push(g>1 ? DIG[g]+" "+GROSO : GROSO);
  if(r){
    if(r<12)       out.push(DIG[r]);
    else if(r===12)out.push(DUNA);
    else if(r<24){ out.push(DUNA); out.push(DIG[r-12]); }   /* two words, never glued */
    else { const d=Math.floor(r/12), u=r%12;
           out.push(PACK[d][0]); if(u) out.push(DIG[u]); }   /* packet, then remainder */
  }
  return out.join(" ");
}
function cardinal(n){
  if(n===0) return DIG[0];
  const groups=[]; let x=n;
  while(x>0){ groups.push(x%TRIAD); x=Math.floor(x/TRIAD); }
  const parts=[];
  for(let i=groups.length-1;i>=0;i--){
    if(!groups[i]) continue;
    if(i===0) parts.push(triad(groups[i]));
    /* a coefficient of one is left bare, the way 144 is grosô and 12 is düna */
    else parts.push(groups[i]===1 ? SCALE[i] : triad(groups[i])+" "+SCALE[i]);
  }
  return parts.join(" ");
}
function digitsOf(n){
  if(n===0) return [0];
  const d=[]; let x=n;
  while(x>0){ d.unshift(x%12); x=Math.floor(x/12); }
  return d;
}
/* the written figure */
function figure(n){
  const [t,e]=GLYPHS[glyph];
  return digitsOf(n).map(d=>d<10?String(d):(d===10?t:e)).join("");
}
/* how a figure is read aloud — digit by digit, hyphenated: 100 → jedôn-nolô-nolô */
function readFigure(n){ return digitsOf(n).map(d=>DIG[d]).join("-"); }
/* the arithmetic behind the words */
function breakdown(n){
  if(n<12) return "";
  const d=digitsOf(n), P=[];
  d.forEach((v,i)=>{ const p=d.length-1-i; if(v) P.push(p?`${v}×12${sup(p)}`:`${v}`); });
  return P.join(" + ")+" = "+n.toLocaleString("en-US");
}
const sup=p=>["","","²","³","⁴","⁵","⁶","⁷","⁸","⁹","¹⁰","¹¹","¹²"][p]||("^"+p);

/* -tô on the cardinal: jedôntô, dvatô, dünatô — the suffix lands on the last word */
function ordinal(n){ return cardinal(n)+"tô"; }
/* canon has half as its own word; everything else is number + dēl */
function fraction(n){ return n===2 ? "half" : cardinal(n)+"-dēl"; }

/* ── reading a number back ─────────────────────────────────────────────────── */
const DIGIDX={}, TEENIDX={};
DIG.forEach((w,i)=>DIGIDX[fold(w)]=i);
/* no teens to index */
function fold(s){
  return String(s).toLowerCase()
    .replace(/ô/g,"o").replace(/ā/g,"a").replace(/ē/g,"e").replace(/ī/g,"i")
    .replace(/ō/g,"o").replace(/ū/g,"u").replace(/ñ/g,"n").replace(/ç/g,"c")
    .replace(/ä/g,"a").replace(/ö/g,"o").replace(/ü/g,"u").replace(/õ/g,"o");
}
const UNITW={ [fold(DUNA)]:12, [fold(GROSO)]:144 };
const SCALEW={ [fold(MIRO)]:1728, [fold(MILJON)]:Math.pow(12,6),
               [fold("bilj")]:Math.pow(12,9), [fold("trilj")]:Math.pow(12,12),
               [fold("milly")]:Math.pow(12,6), [fold("billy")]:Math.pow(12,9),
               [fold("trilly")]:Math.pow(12,12) };
/* each packet is a bare value, not a coefficient — kvādôr IS 24 */
const PACKW={}; Object.keys(PACK).forEach(k=>PACKW[fold(PACK[k][0])]=k*12);

/* Parses Nelôxi words, then RE-COMPOSES the result and compares. A mismatch is
   reported as unreadable rather than answered wrongly. */
/* milly/billy/trilly are the street forms of milj/bilj/trilj — accepted on
   input, normalised to the formal word before the round-trip check runs. */
const STREET={ milly:"milj", billy:"bilj", trilly:"trilj" };
function deStreet(s){
  return String(s).split(/(\s+)/).map(w=>STREET[fold(w)]||w).join("");
}
function parseWords(raw){
  const str=deStreet(raw);
  const toks=fold(str).split(/[\s\-·,]+/).filter(Boolean);
  if(!toks.length) return null;
  let total=0, group=0, pend=null;
  const flush=()=>{ if(pend!==null){ group+=pend; pend=null; } };
  for(let i=0;i<toks.length;i++){
    const t=toks[i];
    if(DIGIDX[t]!==undefined){ flush(); pend=DIGIDX[t]; continue; }
    if(PACKW[t]!==undefined){ flush(); group+=PACKW[t]; continue; }
    if(UNITW[t]!==undefined){ group += (pend===null?1:pend)*UNITW[t]; pend=null; continue; }
    if(SCALEW[t]!==undefined){
      let mult=SCALEW[t];
      flush();
      total += (group===0?1:group)*mult;
      group=0; continue;
    }
    return null;                                   /* not a numeral word */
  }
  flush();
  total+=group;
  if(!Number.isFinite(total) || total<0 || total>MAXN) return null;
  return fold(cardinal(total))===fold(str.trim().replace(/[·,]+/g," ")) ? total : null;
}
function parseFigure(str){
  const [t,e]=["de","xe","↊↋"];                    /* accept any glyph set */
  const s=String(str).trim().toUpperCase().replace(/^0Z/,"").replace(/[\s_]/g,"");
  if(!s || !/^[0-9DEX↊↋]+$/.test(s)) return null;
  let n=0;
  for(const c of s){
    let d;
    if(/[0-9]/.test(c)) d=+c;
    else if(c==="D"||c==="X"||c==="↊") d=10;
    else if(c==="E"||c==="↋") d=11;
    else return null;
    n=n*12+d;
    if(n>MAXN) return null;
  }
  return n;
}
/* one input, three notations — work out which was meant */
function interpret(raw){
  const s=raw.trim();
  if(!s) return null;
  if(/^-?[\d,\s]+$/.test(s)){
    const n=parseInt(s.replace(/[,\s]/g,""),10);
    if(Number.isFinite(n)&&n>=0) return {n, how:"a decimal number"};
    return null;
  }
  if(/^(0z|0Z)/.test(s)||/^[0-9DEXde x↊↋]+$/.test(s)){
    const n=parseFigure(s);
    if(n!==null) return {n, how:"a dozenal figure"};
  }
  const w=parseWords(s);
  if(w!==null) return {n:w, how:"Nelôxi words"};
  const n2=parseFigure(s);
  if(n2!==null) return {n:n2, how:"a dozenal figure"};
  return null;
}

/* ── render ────────────────────────────────────────────────────────────────── */
const $=id=>document.getElementById(id);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const cell=(l,v,n,cls)=>`<div class="cell ${cls||""}"><div class="l">${l}</div>`+
  `<div class="v">${v}</div>${n?`<div class="n">${n}</div>`:""}</div>`;

const NOUNS=[["kalāt","fish"],["pǟvôt","days"],["kūt","months"],["līnāt","towns"]];

function draw(){
  const raw=$("q").value, got=interpret(raw);
  if(!got){
    $("read").innerHTML=raw.trim()
      ? `<span class="bad">Not a number I can read.</span> Try <b>144</b>, <b>100</b> as a figure, or <b>grosô</b>.`
      : "";
    $("out").innerHTML=""; markGrid(null); return;
  }
  const n=got.n;
  $("read").innerHTML=`Read as <b>${got.how}</b>.`;

  const bits=[];
  bits.push(`<div class="hero">${esc(cardinal(n))}</div>`);
  const bd=breakdown(n);
  bits.push(`<div class="heroline">${n.toLocaleString("en-US")} in decimal &middot; `+
            `figure <code>${esc(figure(n))}</code>${bd?" &middot; "+esc(bd):""}</div>`);

  const g=[];
  g.push(cell("Figure", esc(figure(n)),
    "positional, base 12", "mono"));
  g.push(cell("Figure read aloud", esc(readFigure(n)),
    "digit by digit, hyphenated"));
  g.push(cell("Ordinal", esc(ordinal(n)), "&minus;tô on the cardinal"));
  g.push(cell("How many times", esc(cardinal(n))+" māl",
    n===1?"once":(n===2?"twice":"")));
  g.push(n<2 ? cell("Fraction","—","no share below a half","off")
             : cell("Fraction", esc(fraction(n)),
                    n===2?"its own word, not dva-dēl":"number + dēl"));
  const noun=NOUNS[n%NOUNS.length];
  g.push(n===1
    ? cell("Counted noun", "jedôn "+esc(noun[0].replace(/t$/,"d")),
           "one takes no partitive")
    : cell("Counted noun", esc(cardinal(n)+" "+noun[0]),
           "partitive singular &mdash; "+esc(n+" "+noun[1])));
  g.push(n<24
    ? cell("Clock", "klôk "+esc(cardinal(n)),
           String(n).padStart(2,"0")+":00 &mdash; 24-hour, no a.m./p.m.")
    : cell("Clock","—","hours only run 0&ndash;23","off"));
  const pctOf=(n/144*100);
  g.push(n<=144
    ? cell("As a share of the gross", esc(figure(n))+"%",
           esc(n+"/144 = "+(pctOf).toFixed(pctOf%1?2:0)+"% decimal"))
    : cell("As a share of the gross","—","over a full gross","off"));
  bits.push(`<div class="grid">${g.join("")}</div>`);
  $("out").innerHTML=bits.join("");
  markGrid(n);
}

function tbl(id, head, rows){
  $(id).innerHTML=`<thead><tr>${head.map(h=>`<th>${h}</th>`).join("")}</tr></thead>`+
    `<tbody>${rows.map(r=>`<tr>${r.join("")}</tr>`).join("")}</tbody>`;
}
const c=(cls,v)=>`<td class="${cls}">${v}</td>`;

function tables(){
  tbl("tdig",["Value","Figure","Nelôxi","English"],
    DIG.map((w,i)=>[c("en",i), c("fig",figure(i)), c("nx",esc(w)), c("en",EN[i])]));

  tbl("tpow",["Word","Value","Figure","What it is"],
    [[c("nx",DUNA), c("en","12"), c("fig",figure(12)), c("note","one dozen — where counting rolls over")],
     [c("nx",GROSO), c("en","144"), c("fig",figure(144)), c("note","12² — a dozen dozens, the gross. This is what “100” means.")],
     [c("nx",MIRO), c("en","1,728"), c("fig",figure(1728)), c("note","12³")],
     [c("nx",DUNA+" "+MIRO), c("en","20,736"), c("fig",figure(20736)), c("note","12⁴ — rides as a coefficient, like “ten thousand”")],
     [c("nx",MILJON), c("en","2,985,984"), c("fig",figure(Math.pow(12,6))), c("note","12⁶ — a late loan · street <i>milly</i>")],
     [c("nx","bilj"), c("en","5,159,780,352"), c("fig",figure(Math.pow(12,9))), c("note","12⁹ — a late loan · street <i>billy</i>")],
     [c("nx","trilj"), c("en","8,916,100,448,256"), c("fig",figure(Math.pow(12,12))), c("note","12¹² — a late loan · street <i>trilly</i>")]]);

  /* the ten packets — each a thing that came in that quantity */
  tbl("tpack",["Dozens","Value","Figure","Word","What it is"],
    Object.keys(PACK).map(k=>[c("en",k+"×"), c("en",k*12), c("fig",figure(k*12)),
      c("nx",esc(PACK[k][0])), c("note",esc(PACK[k][1]))]));

  const teen=[];
  teen.push([c("en","12"), c("fig",figure(12)), c("nx",DUNA), c("note","bare — the teens start at 13")]);
  for(let i=13;i<=23;i++) teen.push([c("en",i), c("fig",figure(i)), c("nx",esc(cardinal(i))),
    c("note","dün- + "+esc(DIG[i-12])+(i-12>=7?" (clipped)":""))]);
  tbl("tteen",["Value","Figure","Nelôxi","Made from"],teen);

  /* the same digit string, read two ways — the drift is exactly 1.2ⁿ */
  const LOOKS=["ten","a hundred","a thousand","ten thousand","a hundred thousand","a million",
               "ten million"];
  tbl("tround",["Figure","Looks like","Actually is","Read aloud","Short by"],
    LOOKS.map((looks,k)=>{
      const places=k+1, v=Math.pow(12,places), dec=Math.pow(10,places);
      return [c("fig","1"+"0".repeat(places)), c("en",looks),
              c("nx",v.toLocaleString("en-US")),
              c("note",places<=3?esc(readFigure(v)):"<i>&mdash;</i>"),
              c("note","&times;"+(v/dec).toFixed(4).replace(/0+$/,"").replace(/\.$/,"")+
                       " &nbsp;<span style='color:var(--ink4)'>("+
                       Math.round((1-dec/v)*100)+"% under)</span>")];
    }));

  const EXAMPLES=[24,27,41,168,351,1728,2000,5000,144000];
  tbl("tex",["Value","Figure","Nelôxi","Arithmetic"],
    EXAMPLES.map(n=>[c("en",n.toLocaleString("en-US")), c("fig",figure(n)),
      c("nx",esc(cardinal(n))), c("note",esc(breakdown(n)))]));

  tbl("tuse",["Job","Form","Example"],
   [[c("en","Counting a noun"), c("nx","number + partitive singular"),
     c("note","<i>tri kalāt</i> “three fish” — never the plural <i>kalād</i>")],
    [c("en","Ordinal"), c("nx","cardinal + −tô"),
     c("note","<i>jedôntô pǟvôl</i> “on the first day” · <i>dünatô</i> twelfth")],
    [c("en","How many times"), c("nx","bare cardinal + māl"),
     c("note","<i>dva māl</i> twice · <i>düna māl</i> a dozen times. <i>māl</i> never inflects.")],
    [c("en","Fraction"), c("nx","half, or number + dēl"),
     c("note","<i>tri-dēl</i> a third · <i>xtiri-dēl</i> a quarter · <i>dünas half</i> half a dozen")],
    [c("en","Reading a figure"), c("nx","digit by digit, hyphenated"),
     c("note","<i>100</i> is <i>jedôn-nolô-nolô</i> — not <i>grosô</i>, which is the value’s own name")],
    [c("en","Percent, formally"), c("nx","pôkrosa"),
     c("note","government documents, official metrics, technical readouts")],
    [c("en","Percent, casually"), c("nx","krossi"),
     c("note","<i>jedôn-nolô-nolô krossi</i> — “100 krossi sure”")]]);

  const SHARES=[[1,"the whole",144],[0.5,"half",72],[1/3,"a third",48],[0.25,"a quarter",36],
                [1/6,"a sixth",24],[1/12,"a twelfth",12],[1/144,"one part in a gross",1]];
  tbl("tpct",["Share","Nelôxi figure","Read aloud","Decimal equivalent"],
    SHARES.map(([f,label,v])=>[c("en",label), c("fig",figure(v)+"%"),
      c("nx",esc(readFigure(v))), c("note",(f*100).toFixed(f*100%1?2:0)+"%"+
        (label==="half"?" — so half is written <b>60%</b>, not 50%":""))]));

  const clk=[];
  for(let h=0;h<24;h++) clk.push([c("en",String(h).padStart(2,"0")+":00"),
    c("nx","klôk "+esc(cardinal(h))),
    c("note", h===0?"midnight":(h===12?"noon":(h<12?"morning":"afternoon and evening")))]);
  tbl("tclk",["Written","Spoken","&nbsp;"],clk);

  $("openq").innerHTML=`<b>Retired:</b> charter §37–§39 ruled a nested tally on the long hundred `+
    `— <i>dūtô</i> 12, <i>drētig</i> 30, <i>fērtig</i> 40 — before the base was settled. It was `+
    `orphaned when this module was written and never reached the lexicon. It is now formally `+
    `superseded; <b>langhunt</b> (120) and <b>xokô</b> (60) survive because base twelve has room `+
    `for them as packets rather than places. &nbsp;<b>Still yours:</b> the currency has no name — `+
    `canon has only <i>rā</i>, “money.”`;
}

function dozGrid(){
  let h="";
  for(let n=0;n<144;n++){
    const cls=["dz"]; if(n===0) cls.push("zero"); if(n%12===0&&n) cls.push("roll");
    h+=`<button class="${cls.join(" ")}" data-n="${n}"><div class="f">${esc(figure(n))}</div>`+
       `<div class="w">${esc(cardinal(n))}</div></button>`;
  }
  $("dozgrid").innerHTML=h;
  $("dozgrid").addEventListener("click",e=>{
    const b=e.target.closest(".dz"); if(!b) return;
    $("q").value=b.dataset.n; draw(); $("q").scrollIntoView({block:"center",behavior:"smooth"});
  });
}
function markGrid(n){
  document.querySelectorAll(".dz").forEach(b=>{
    b.style.background = (n!==null&&+b.dataset.n===n) ? "var(--accent)" : "";
    b.style.color      = (n!==null&&+b.dataset.n===n) ? "#fff" : "";
  });
}

function glyphSeg(){
  $("glyphseg").innerHTML=Object.keys(GLYPHS)
    .map(k=>`<button data-g="${k}" aria-pressed="${k===glyph}">${GLYPHS[k].join(" ")}`+
            `<span class="gl">${k}</span></button>`).join("");
  $("glyphseg").addEventListener("click",e=>{
    const b=e.target.closest("button"); if(!b) return;
    glyph=b.dataset.g; glyphSeg(); tables(); dozGrid(); draw();
  });
  $("glyphnote").innerHTML=GLYPHNOTE[glyph];
}
function chips(){
  const QUICK=[["12","a dozen"],["144","a gross"],["1728","12³"],["18","the clock at 18:00"],
               ["351",""],["2026",""],["grosô kvādôr","the quire packet"],["dva grosô xokô tri",""]];
  $("chips").innerHTML=QUICK.map(([v,t])=>
    `<button data-v="${esc(v)}"${t?` title="${esc(t)}"`:""}>${esc(v)}</button>`).join("");
  $("chips").addEventListener("click",e=>{
    const b=e.target.closest("button"); if(!b) return;
    $("q").value=b.dataset.v; draw();
  });
}

glyphSeg(); chips(); tables(); dozGrid(); draw();
$("q").addEventListener("input",draw);

/* ── self-check: the canon examples must come out exactly as written ───────── */
(function(){
  const MUST=[[0,"nul"],[1,"ūn"],[11,"undeçôm"],[12,"duodeç"],[13,"duodeç ūn"],
    [18,"duodeç sex"],[23,"duodeç undeçôm"],[24,"vigint"],[27,"vigint trē"],
    [41,"trigint kvīnk"],[60,"kvīnkvāgint"],[120,"deçāgint"],[132,"undeçāgint"],
    [143,"undeçāgint undeçôm"],[144,"çent"],[168,"çent vigint"],
    [351,"duô çent kvīnkvāgint trē"],[1728,"mīl"],
    [Math.pow(12,6),"milj"],[Math.pow(12,9),"bilj"],[Math.pow(12,12),"trilj"]];
  const bad=MUST.filter(([n,w])=>cardinal(n)!==w)
                .map(([n,w])=>`${n}: got "${cardinal(n)}", canon "${w}"`);
  /* every value must also read back to itself */
  for(let n=0;n<2000;n++) if(parseWords(cardinal(n))!==n) bad.push("round-trip "+n);
  window.__CHECK__ = bad;
  if(bad.length) console.error("CANON CHECK FAILED", bad);
})();
</script>
</body>
</html>
"""


def main():
    out = ROOT / "numbers.html"
    out.write_text(TEMPLATE, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")
    print("digits nul–undeçôm · base duodeç · -ginta dozens · çent 144 · mīl 1728")
    print("milj/bilj/trilj are late loans; milly/billy/trilly on the street")
    print("converter reads decimal, dozenal figures and Nelôxi words "
          "(round-trip verified in-page)")


if __name__ == "__main__":
    main()
