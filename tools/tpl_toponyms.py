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
  <p class="tagline">Name, then exonym. Weighted by region and era.</p>
</header>

<div class="panel">
  <div class="modes">
    <button class="mode" id="m-gaz" aria-pressed="true">Gazetteer — name a real city</button>
    <button class="mode" id="m-free" aria-pressed="false">Free roll — invent a place</button>
  </div>
  <div class="ctrls" id="ctrls"></div>
  <div class="ctx" id="ctx"></div>
</div>

<div class="sect"><h2>Candidates</h2><span id="cnt"></span><span id="prog" style="margin-left:auto"></span></div>
<div class="cards" id="cards"></div>

<div class="sect" id="pendsect" hidden><h2>Choose the exonym</h2><span>step 2 of 2</span></div>
<div id="pendwrap"></div>

<div class="basket">
  <div class="sect"><h2>Picked</h2><span id="bcnt"></span></div>
  <div id="bwrap"></div>
</div>

</div>

<script>
const CITIES = __CITIES__;
const REGIONS = __REGIONS__;

/* ── element banks, BY QUARRY ────────────────────────────────────────────────
   The creole doctrine has five co-primary quarries and the state spans Karelia
   to the Riviera to Thrace, so the naming vocabulary must too. Each quarry
   carries its own modifiers, settlement heads, and person names; a region draws
   only on the quarries that plausibly named its ground (the gravity principle).
   Glosses use the canon name-senses (§146): mer not merd, kājô not lōd.      */
const HEADS = {
  finnic:[["-sô","river-bend"],["-mō","land"],["-linnô","fortress"],["-itô","settlement"],
          ["-sār","island"],["-rānd","shore"],["-järv","lake"],["-koski","rapids"],
          ["-korbi","backwoods"],["-satām","harbour"],["-mündõ","river-mouth"],["-sū","river-mouth"],
          ["-lax","bay"],["-niemi","cape"],["-vesi","water"],["-kylä","village"],["-mäki","hill"],
          ["-suo","marsh"],["-salmi","sound"],["-vuori","fell"]],
  lowgerman:[["-bôrk","walled town"],["-hafõn","harbour"],["-hôlm","islet"],["-dôrp","village"],
             ["-markõt","market-town"],["-mündõ","river-mouth"],["-ūsô","works"],["-stedt","stead"],
             ["-wērder","river-isle"],["-brügg","bridge"],["-kōg","polder"],["-schans","redoubt"],
             ["-krōg","inn"],["-wik","inlet"],["-fēld","field"],["-hagen","enclosure"]],
  scand:[["-vīk","bay"],["-nes","cape"],["-ô","island"],["-fjôrd","sea-inlet"],["-sund","strait"],
         ["-bôd","booth, trading post"],["-hamn","haven"],["-berg","rock"],["-dal","dale"],
         ["-lund","grove"],["-tôrp","croft"],["-strand","strand"],["-ôyri","gravel-spit"]],
  slavic:[["-grôd","town"],["-ovô","place of"],["-sk","-town"],["-itsô","little settlement"],
          ["-pôl","field-town"],["-mīr","peace, world"],["-brôd","ford"],["-vôd","water"],
          ["-gôr","hill"],["-dôl","valley"],["-lug","meadow"],["-most","bridge"],["-slav","glory"]],
  baltic:[["-pils","castle"],["-ava","river-town"],["-upõ","stream"],["-kalns","hill"],
          ["-mestô","town"],["-mūiž","manor"],["-ezer","lake"],["-krôg","inn"],["-tilt","bridge"],
          ["-sala","island"],["-pēd","footing"]],
  romance:[["-vīla","chartered estate"],["-kolēgi","college"],["-kastel","castle"],
           ["-portô","port"],["-kampô","field"],["-vāl","vale"],["-bôrgô","borough"],
           ["-tôrre","tower"],["-pônte","bridge"],["-badīa","abbey"],["-mūr","wall"]],
  german:[["-stadt","town"],["-burg","fortress"],["-dorf","village"],["-berg","mount"],
          ["-tal","valley"],["-furt","ford"],["-brück","bridge"],["-au","water-meadow"],
          ["-kirchen","churches"],["-markt","market"],["-hôfen","farmsteads"],["-egg","spur"]],
  polish:[["-ôw","of"],["-itse","little"],["-vola","clearing-holding"],["-gura","hill"],
          ["-grud","stronghold"],["-brôd","ford"],["-mȫst","bridge"],["-pôle","field"],
          ["-lēs","wood"],["-stav","pond"]],
  belarusian:[["-avitxi","folk of"],["-in","of"],["-harôd","town"],["-slau","glory"],
              ["-bôr","pinewood"],["-brôd","ford"],["-hrad","fort"],["-ruçi","brook"]],
  ukrainian:[["-hrad","town"],["-pīl","town"],["-liman","liman"],["-slav","glory"],
             ["-kut","corner"],["-jar","ravine"],["-brīd","ford"],["-stepp","steppe"],
             ["-hāvan","haven"],["-sitx","stronghold-camp"]],
  yiddish:[["-shtôt","town"],["-shtetl","little town"],["-barg","hill"],["-brik","bridge"],
           ["-mark","market"],["-tôyer","gate"],["-gas","street-row"],["-hôyf","court"]],
  slovak:[["-ves","village"],["-hrad","castle"],["-brôd","ford"],["-nitsa","little"],
          ["-jar","spring"],["-pôtôk","brook"],["-lūka","meadow"]],
  slovene:[["-vas","village"],["-grād","castle"],["-itsa","little"],["-brôd","ford"],
           ["-pôlje","polje"],["-jama","cave"],["-most","bridge"],["-gôritsa","little hill"]],
  croatian:[["-grād","town"],["-itsa","little"],["-pôlje","polje"],["-luka","harbour"],
            ["-brôd","ford"],["-selô","village"],["-klanats","gorge"],["-vrh","summit"]],
  bulgarian:[["-grād","town"],["-tsi","folk of"],["-ovô","place of"],["-bānja","baths"],
             ["-mōgila","mound"],["-brôd","ford"],["-pôle","plain"]],
  macedonian:[["-grād","town"],["-anï","folk of"],["-dôl","valley"],["-vôden","watered"],
              ["-pôle","plain"],["-most","bridge"]],
  venetian:[["-nôvo","new"],["-vēkjô","old"],["-pôrtô","port"],["-kanāl","canal"],
            ["-lidô","barrier-shore"],["-riva","bank"],["-kāsa","house"],["-fôndakô","warehouse"],
            ["-tsitā","city"],["-mōlô","mole"],["-skala","landing"]],
  italian:[["-kastellô","castle"],["-bôrgô","borough"],["-vīla","estate"],["-mônte","mount"],
           ["-vālle","valley"],["-kampô","field"],["-pônte","bridge"],["-tôrre","tower"],
           ["-badīa","abbey"],["-pjeve","parish"],["-rôkka","crag-fort"]],
  occitan:[["-vīla","town"],["-kastēl","castle"],["-mônt","mount"],["-vāl","vale"],
           ["-pônt","bridge"],["-pōrt","port"],["-fōnt","spring"],["-rōka","rock"],
           ["-bastida","new-town"],["-mās","farmstead"]],
  friulian:[["-vīli","village"],["-kjastēl","castle"],["-mônt","mount"],["-riu","stream"],
            ["-pôrt","port"],["-glesie","church"],["-plan","plain"]],
  tatar:[["-saray","palace"],["-kerman","fortress"],["-baxçe","garden"],["-köz","eye, spring"],
         ["-jol","road"],["-tux","salt-flat"],["-liman","harbour"]],
  armenian:[["-akert","built-place"],["-avan","borough"],["-berd","fort"],["-tsor","valley"],
            ["-shēn","settlement"],["-kar","stone"]],
  ottoman:[["-köi","village"],["-hisār","fortress"],["-kale","castle"],["-pazār","market"],
           ["-limān","harbour"],["-burgāz","tower"],["-ovā","plain"],["-dere","valley"],
           ["-hān","caravanserai"],["-köprü","bridge"],["-tepe","hill"]],
  hellenic:[["-pôlis","city"],["-kastrô","fort"],["-hôri","village"],["-limni","lake"],
            ["-nesô","island"],["-vrisi","spring"],["-pirgô","tower"]],
  pannonian:[["-vār","castle"],["-falu","village"],["-hely","place"],["-rēv","ford"],
             ["-hīd","bridge"],["-vārôs","town"],["-halôm","mound"],["-telek","holding"],
             ["-sziget","island"],["-mezö","field"]],
  albanian:[["-gur","stone"],["-fushë","plain"],["-mal","mountain"],["-qafë","pass"],["-krôi","spring"]],
  danubian:[["-ești","folk of"],["-eni","people of"],["-tsetāte","citadel"],["-sat","village"],
            ["-vale","valley"],["-deal","hill"],["-pôd","bridge"],["-luncā","water-meadow"]],
  /* ── the eastern reach ──────────────────────────────────────────────────
     Nelôxia was joined to the corridor for centuries before Sarmatia — East
     Neloxia — went its own way, and the Nelosphere still clears through it.
     A name from Herat or the Kuban is not exotic here; it is a trade record. */
  circassian:[["-kuadje","village"],["-hable","hamlet"],["-psı","water"],["-bgı","mountain"],
              ["-xha","summit"],["-thı","ridge"],["-nepk","river-bank"],["-çıle","settlement"]],
  turkic:[["-orda","camp"],["-jurt","home-country"],["-kent","town"],["-tôbe","mound"],
          ["-kul","lake"],["-bulak","spring"],["-sai","dry-watercourse"],["-tax","stone"],
          ["-özek","valley"],["-aul","hamlet"],["-ata","forefather"]],
  georgian:[["-kalaki","city"],["-tsixe","fortress"],["-gôri","hill"],["-mta","mountain"],
            ["-tskali","water"],["-ubani","quarter"],["-djvari","cross"],["-sôpeli","village"],
            ["-veli","field"],["-hevi","gorge"]],
  persian:[["-ābād","settled-place"],["-xahr","city"],["-kôh","mountain"],["-deh","village"],
           ["-rūd","river"],["-band","dam"],["-gerd","round-town"],["-kart","town"],
           ["-çexme","spring"],["-bāg","garden"],["-kaleh","fort"],["-darvāze","gate"]]
};
/* modifiers, per quarry — a Slavic frontier town does not take a Finnic colour */
const QMODS = {
  finnic:[["uus","new"],["vana","old"],["sūr","great"],["petīt","little"],["must","black"],
    ["pūn","red"],["sinī","blue"],["rôhī","green"],["grīs","grey"],["nīrô","bright"],["helē","pale"],
    ["kivī","stone"],["sōla","salt"],["raud","iron"],["kuld","gold"],["tūļ","wind"],["nēu","snow"],
    ["jǟ","ice"],["pakā","frost"],["sol","sun"],["kū","moon"],["estēl","star"],["lain","wave"],
    ["tormô","storm"],["nôrd","north"],["sud","south"],["idā","east"],["lǟn","west"],["tyhjā","empty"],
    ["krōm","crooked"],["sügä","deep"],["külmä","cold"],["lāj","wide"],["kitsā","narrow"],
    ["pitkä","long"],["lyhü","short"],["hōp","silver"],["savi","clay"],["hiek","sand"]],
  lowgerman:[["nī","new"],["ōld","old"],["grōt","great"],["lütt","little"],["swart","black"],
    ["rōd","red"],["grön","green"],["witt","white"],["sand","sand"],["sōlt","salt"],["īsen","iron"],
    ["hōg","high"],["nedder","lower"],["vȫr","fore"],["achter","hind"],["ost","east"],["west","west"],
    ["nord","north"],["sūd","south"],["blank","shining"],["krumm","bent"],["dūv","dove"],
    ["stēn","stone"],["mȫl","mill"],["salz","salt"]],
  scand:[["ny","new"],["gamm","old"],["stōr","great"],["lit","little"],["svart","black"],
    ["raud","red"],["grön","green"],["hvīt","white"],["djūp","deep"],["brēd","broad"],["lang","long"],
    ["sand","sand"],["berg","rock"],["kald","cold"],["nôrd","north"],["sör","south"],["vest","west"],
    ["aust","east"],["mjôl","meal"],["sil","herring"]],
  slavic:[["nôv","new"],["star","old"],["vel","great"],["mal","little"],["çern","black"],
    ["kras","red, fair"],["zelen","green"],["bel","white"],["sol","salt"],["žel","iron"],
    ["gôr","upper"],["dôl","lower"],["krīv","crooked"],["sux","dry"],["mokr","wet"],
    ["kamen","stone"],["zlat","gold"],["srebr","silver"],["tix","quiet"],["dobr","good"],
    ["svjat","holy"],["glub","deep"],["xolôd","cold"]],
  baltic:[["nauj","new"],["sen","old"],["didz","great"],["maz","little"],["meln","black"],
    ["sarkan","red"],["zaļ","green"],["balt","white"],["akmen","stone"],["dzelz","iron"],
    ["kalnā","upper"],["lej","lower"],["saus","dry"],["slap","wet"],["liep","linden"],
    ["priede","pine"],["bērz","birch"],["auks","gold"]],
  romance:[["nova","new"],["vekjô","old"],["grand","great"],["petsôl","little"],["negrô","black"],
    ["rossô","red"],["verd","green"],["biankô","white"],["alt","high"],["bass","low"],
    ["bell","fair"],["mal","ill"],["sant","holy"],["mônt","mount"],["kampô","field"],
    ["frēd","cold"],["kald","warm"],["larg","broad"],["strett","narrow"],["dôr","gold"],
    ["arjent","silver"],["pētrô","stone"]],
  german:[["neu","new"],["alt","old"],["gros","great"],["klein","little"],["schwarts","black"],
    ["rōt","red"],["grün","green"],["weis","white"],["hōh","high"],["nieder","lower"],
    ["stein","stone"],["eisen","iron"],["salts","salt"],["kalt","cold"],["ober","upper"],
    ["unter","under"],["mitter","middle"],["breit","broad"],["lang","long"],["gold","gold"]],
  polish:[["nôvi","new"],["stari","old"],["velki","great"],["mali","little"],["tsarni","black"],
    ["biali","white"],["zelôni","green"],["tservôni","red"],["zlôti","gold"],["sôlni","salt"],
    ["dôlni","lower"],["gôrni","upper"],["sux","dry"],["krivi","crooked"],["kamen","stone"],
    ["jasni","bright"],["dlugi","long"],["shirôki","wide"]],
  belarusian:[["nôvi","new"],["stari","old"],["veliki","great"],["mali","little"],["çôrni","black"],
    ["beli","white"],["zeljôni","green"],["çirvôni","red"],["zalati","gold"],["sôlni","salt"],
    ["nižni","lower"],["višni","upper"],["kriva","crooked"],["mokri","wet"],["tixi","quiet"]],
  ukrainian:[["nôvi","new"],["stari","old"],["velikï","great"],["malï","little"],["çôrni","black"],
    ["bilï","white"],["zelenï","green"],["çervônï","red"],["zôlôtï","gold"],["sôljanï","salt"],
    ["nižnï","lower"],["veršnï","upper"],["sixï","dry"],["xolôdnï","cold"],["xirôkï","wide"],
    ["dôvhï","long"],["kaminnï","stony"],["vilnï","free"]],
  yiddish:[["nay","new"],["alt","old"],["grôys","great"],["kleyn","little"],["shvarts","black"],
    ["vays","white"],["grin","green"],["rôyt","red"],["gôldn","golden"],["zalts","salt"],
    ["kalt","cold"],["breyt","broad"],["hôyx","high"],["shtil","quiet"]],
  slovak:[["nôvi","new"],["stari","old"],["velki","great"],["mali","little"],["çierni","black"],
    ["bieli","white"],["zeleni","green"],["çerveni","red"],["slani","salt"],["suxi","dry"],
    ["hôrni","upper"],["dôlni","lower"],["dlhi","long"]],
  slovene:[["nôvi","new"],["stari","old"],["veliki","great"],["mali","little"],["çrni","black"],
    ["beli","white"],["zeleni","green"],["rdeçi","red"],["sôlni","salt"],["suxi","dry"],
    ["gôrni","upper"],["dôlni","lower"],["kamniti","stony"],["mrzli","cold"]],
  croatian:[["nôvi","new"],["stari","old"],["veliki","great"],["mali","little"],["tsrni","black"],
    ["bijeli","white"],["zeleni","green"],["tsrveni","red"],["slani","salt"],["suxi","dry"],
    ["gôrnji","upper"],["dônji","lower"],["kameni","stony"],["vjetrôvni","windy"],["dūgi","long"]],
  bulgarian:[["nôv","new"],["star","old"],["golem","great"],["malāk","little"],["çeren","black"],
    ["bjal","white"],["zelen","green"],["çerven","red"],["zlaten","gold"],["sôlen","salt"],
    ["gôren","upper"],["dôlen","lower"],["sux","dry"],["studen","cold"],["xirôk","wide"]],
  macedonian:[["nôv","new"],["star","old"],["golem","great"],["mal","little"],["tsrn","black"],
    ["bel","white"],["zelen","green"],["tsrven","red"],["zlaten","gold"],["sôlen","salt"],
    ["gôren","upper"],["dôlen","lower"],["suv","dry"],["studen","cold"]],
  venetian:[["nôvô","new"],["vēkjô","old"],["grandô","great"],["pikôlô","little"],["negrô","black"],
    ["biankô","white"],["verde","green"],["rôssô","red"],["dôrô","gold"],["salâ","salt"],
    ["alt","high"],["bass","low"],["bell","fair"],["longô","long"],["largô","broad"],
    ["frēdô","cold"],["sant","holy"],["pjērâ","stone"]],
  italian:[["nuôvô","new"],["vekjô","old"],["grande","great"],["pikkôlô","little"],["nerô","black"],
    ["biankô","white"],["verde","green"],["rôssô","red"],["ôrô","gold"],["sāle","salt"],
    ["altô","high"],["bassô","low"],["bellô","fair"],["lungô","long"],["largô","broad"],
    ["freddô","cold"],["santô","holy"],["pjētrâ","stone"],["forte","strong"]],
  occitan:[["nôu","new"],["vièlh","old"],["grand","great"],["petit","little"],["negre","black"],
    ["blanc","white"],["verd","green"],["rôge","red"],["aur","gold"],["sāl","salt"],
    ["aut","high"],["bas","low"],["bèl","fair"],["lông","long"],["larg","broad"],
    ["freid","cold"],["sant","holy"],["rôka","rock"],["ventôs","windy"]],
  friulian:[["gnûf","new"],["vieli","old"],["grant","great"],["pitsul","little"],["neri","black"],
    ["blank","white"],["vert","green"],["rôs","red"],["ôr","gold"],["sāl","salt"],
    ["alt","high"],["bas","low"],["frêt","cold"],["sant","holy"]],
  tatar:[["jañı","new"],["eski","old"],["ulu","great"],["kiçik","little"],["kara","black"],
    ["ak","white"],["kızıl","red"],["jexil","green"],["altın","gold"],["tuz","salt"],
    ["sôuk","cold"],["tax","stone"],["çôl","steppe"],["deñiz","sea"]],
  armenian:[["nôr","new"],["hin","old"],["mets","great"],["pôkr","little"],["sev","black"],
    ["spitak","white"],["kanaç","green"],["karmir","red"],["ôski","gold"],["ałt","salt"],
    ["bardzr","high"],["tsatsr","low"],["sur","sharp"],["kar","stone"]],
  albanian:[["i re","new"],["i vjetër","old"],["i madh","great"],["i vogël","little"],
    ["zi","black"],["bardh","white"],["kuq","red"],["gjelbër","green"],["ar","gold"],
    ["kripë","salt"],["ftôhtë","cold"],["gur","stone"],["lartë","high"],["gjatë","long"]],
  ottoman:[["jeni","new"],["eski","old"],["kara","black"],["ak","white"],["kızıl","red"],
    ["demīr","iron"],["tuz","salt"],["büjük","great"],["küçük","little"],["jexil","green"],
    ["altın","gold"],["gümüx","silver"],["sarı","yellow"],["sōuk","cold"],["dar","narrow"],
    ["gen","wide"],["taxlı","stony"],["su","water"]],
  hellenic:[["neô","new"],["palē","old"],["megā","great"],["mikrā","little"],["mavrô","black"],
    ["lefkô","white"],["kokinô","red"],["hlōrô","green"],["hrisô","gold"],["argirô","silver"],
    ["kalô","fair"],["āgiô","holy"],["patrô","stone"],["psihrô","cold"]],
  pannonian:[["ūj","new"],["ō","old"],["nagi","great"],["kix","little"],["feketē","black"],
    ["vörös","red"],["zöld","green"],["fehēr","white"],["vas","iron"],["sō","salt"],
    ["hedj","hill"],["völdj","valley"],["mezö","field"],["arani","gold"],["hidēg","cold"],
    ["sāraz","dry"],["nēdes","wet"],["kerek","round"]],
  danubian:[["nou","new"],["vekj","old"],["mare","great"],["mik","little"],["negru","black"],
    ["roxu","red"],["verde","green"],["alb","white"],["fier","iron"],["sare","salt"],
    ["deal","hill"],["vale","valley"],["kâmp","plain"],["aur","gold"],["rēçe","cold"],
    ["uskāt","dry"],["lung","long"],["lat","wide"]],
  circassian:[["kje","new"],["jı","old"],["ıne","great"],["tsıku","little"],["xuts","black"],
    ["fıj","white"],["plıj","red"],["utsı","green"],["gôj","yellow"],["dıxe","gold"],
    ["dıjın","silver"],["guçı","iron"],["xıgu","salt"],["mıjô","stone"],["psıne","spring"]],
  turkic:[["kôk","blue"],["kızıl","red"],["ak","white"],["kara","black"],["sarı","yellow"],
    ["temir","iron"],["altın","gold"],["kumıx","sandy"],["djetı","seven"],["bes","five"],
    ["uzun","long"],["tuzlu","salt"],["djasıl","green"],["muz","ice"],["djel","wind"],
    ["djañı","new"],["kôna","old"]],
  georgian:[["axali","new"],["dzveli","old"],["didi","great"],["patara","little"],["xavi","black"],
    ["tetri","white"],["tsiteli","red"],["mtsvane","green"],["ôkrô","gold"],["vertsxli","silver"],
    ["rkina","iron"],["kva","stone"],["marili","salt"],["magali","high"],["grdzeli","long"]],
  persian:[["nô","new"],["kôhne","old"],["bôzôrg","great"],["kūçek","little"],["siāh","black"],
    ["sefīd","white"],["sôrx","red"],["sabz","green"],["zar","gold"],["nôkre","silver"],
    ["āhan","iron"],["namak","salt"],["sang","stone"],["xôxk","dry"],["sard","cold"],
    ["bālā","upper"],["pājīn","lower"]]
};
/* terrain → LOCATABLE features only, per quarry-neutral canon senses. Resources
   and objects live in the modifier banks: you can be "at the shore" but not "at
   the fish". More features per terrain, or descriptive names collapse. */
const TERRFEAT = {
  Sea:[["mer","sea"],["rānd","shore"],["satām","harbour"],["kājô","quay"],["nēm","cape"],["lax","bay"],["mōl","mole"]],
  Bay:[["laht","bay"],["mer","sea"],["satām","harbour"],["rānd","shore"],["salmi","sound"],["akôrpaik","anchorage"]],
  Lagoon:[["laht","bay"],["rānd","shore"],["satām","harbour"],["mudā","flats"],["salmi","sound"]],
  Strait:[["sund","strait"],["mer","sea"],["pôrta","gate"],["salmi","sound"],["nēm","cape"]],
  Spit:[["rānd","shore"],["sār","island"],["nēm","cape"],["hiek","sand-bar"],["luidô","dune"]],
  Cape:[["nēm","cape"],["nes","cape"],["mer","sea"],["torn","tower"],["rānd","shore"]],
  Coast:[["rānd","shore"],["mer","sea"],["satām","harbour"],["kājô","quay"],["luidô","dune"]],
  Island:[["sār","island"],["hôlm","islet"],["rānd","shore"],["satām","harbour"],["kirīk","church"]],
  Delta:[["mündõ","river-mouth"],["jôg","river"],["rānd","shore"],["mudā","flats"],["hārô","branch"]],
  Estuary:[["mündõ","river-mouth"],["laht","bay"],["jôg","river"],["kājô","quay"],["salmi","sound"]],
  Liman:[["laht","bay"],["mündõ","river-mouth"],["rānd","shore"],["sōlajärv","salt-lake"]],
  River:[["jôg","river"],["pont","bridge"],["kājô","quay"],["koski","rapids"],["brôd","ford"],["saar","river-isle"]],
  Canal:[["kanā","channel"],["lukkô","lock"],["jôg","river"],["kājô","quay"],["pont","bridge"]],
  Lake:[["järv","lake"],["rānd","shore"],["satām","harbour"],["nēm","cape"],["sār","island"],["läte","spring"]],
  Marsh:[["sô","marsh"],["korbi","backwoods"],["jôg","river"],["läte","spring"],["kōg","polder"]],
  Forest:[["meçā","forest"],["korbi","backwoods"],["kamī","road"],["läte","spring"],["raiô","clearing"]],
  Hill:[["kalns","hill"],["kôrg","height"],["põld","field"],["mäki","rise"],["kirīk","church"]],
  Upland:[["kalns","hill"],["põld","field"],["meçā","forest"],["kôrg","height"],["mūiž","manor"]],
  Highland:[["munt","mountain"],["kalns","hill"],["põld","field"],["org","valley"],["läte","spring"]],
  Mountain:[["munt","mountain"],["kalns","hill"],["org","valley"],["pôrta","pass"],["kivī","crag"]],
  Valley:[["org","valley"],["jôg","river"],["kamī","road"],["põld","field"],["mūiž","manor"]],
  Gorge:[["org","valley"],["pôrta","gate"],["jôg","river"],["kivī","crag"],["pont","bridge"]],
  Karst:[["org","valley"],["bīr","well"],["põld","polje"],["kivī","crag"],["kōbas","cave"]],
  Plateau:[["põld","field"],["kamī","road"],["kalns","hill"],["bīr","well"],["kôrg","height"]],
  Basin:[["org","valley"],["põld","field"],["järv","lake"],["läte","spring"],["turg","market"]],
  Plain:[["põld","field"],["turg","market"],["kamī","road"],["brôd","ford"],["kylä","village"]],
  Sand:[["rānd","shore"],["põld","field"],["kamī","road"],["hiek","sand"],["luidô","dune"]],
  Desert:[["bīr","well"],["kamī","road"],["põld","waste"],["kivī","crag"],["kanā","wadi"]],
  Wadi:[["kanā","channel"],["bīr","well"],["org","valley"],["läte","spring"]],
  Crater:[["laht","bay"],["munt","mountain"],["satām","harbour"],["kivī","crag"]]
};
/* person names by quarry — expanded, and the missing quarries added */
const GIVEN = {
  finnic:["Mārta","Pēter","Līna","Jāns","Märt","Anna","Ilze","Jānis","Mārtiņš","Artūrs","Andres",
    "Aino","Väinö","Toivô","Helmi","Urhô","Kaisa","Eerô","Saimi","Tapiô","Kerttu"],
  lowgerman:["Hans","Grete","Klaus","Trīne","Jürgen","Gesche","Tönnies","Margrete","Hinrik","Wībke",
    "Detlev","Almut","Cord","Alheyd","Bartold","Metta"],
  scand:["Ragnar","Sigrid","Halvard","Ingebôrg","Torkel","Åsa","Gunnar","Bôrghild","Svein","Rannveig"],
  slavic:["Ivan","Olga","Dmitri","Natālija","Pavel","Irina","Nikolaj","Marek","Katerina","Bôgdan",
    "Zôra","Vlas","Milena","Radômir","Jadviga","Stanislav"],
  baltic:["Vytautas","Birutė","Kazimieras","Dainora","Algirdas","Rūta","Mindaugas","Guoda",
    "Ojārs","Zane","Valdis","Laima"],
  romance:["Marc","Clara","Ferran","Carles","Rosa","Jordi","Lluís","Pau","Caterina","Elisa",
    "Giacôm","Lucia","Bartôlô","Zuane","Nicolô","Orsôla","Marīn","Franceskô"],
  german:["Wôlfgang","Gertrud","Sigmund","Hildegard","Rupert","Notburga","Leôpôld","Adelheid"],
  polish:["Stanisław","Jadwiga","Kazimierz","Bôgusława","Wôjciech","Zôfia","Mieszkô","Halina"],
  belarusian:["Vasil","Halina","Aleś","Zôśka","Symôn","Uladzia","Jazep","Maryla"],
  ukrainian:["Ôstap","Oksana","Taras","Hanna","Bôhdan","Odarka","Danylô","Marusja","Hrytskô","Solomija"],
  yiddish:["Mendl","Beyle","Berl","Khaye","Zalman","Rivke","Shmuel","Gitl","Leybl","Sôre"],
  slovak:["Juraj","Anežka","Ondrej","Bôžena","Matúš","Vierka"],
  slovene:["Primôž","Neža","Jernej","Alenka","Blaž","Mojtsa"],
  croatian:["Ivô","Jelena","Frane","Mare","Nikô","Kate","Dujam","Vitsa"],
  bulgarian:["Todôr","Rada","Iliya","Nedelja","Petkô","Velika"],
  macedonian:["Kôle","Menka","Trajkô","Vasilka","Riste","Dôna"],
  venetian:["Zuane","Orsôla","Nicolô","Marīn","Piērô","Franceskīna","Marcô","Lucieta"],
  italian:["Giacômô","Lucia","Bartôlômeô","Caterina","Ambrôgiô","Bianca","Gianni","Rôsalia"],
  occitan:["Guilhem","Alienôr","Ramôn","Esclarmônda","Bertran","Azalais"],
  friulian:["Zuan","Rôsute","Tôni","Marie","Bepi","Nute"],
  tatar:["Qırım","Ayşe","Bekir","Zöhre","Seyit","Emine"],
  armenian:["Hakôb","Anahit","Grigôr","Sirarpi","Vahan","Nvard"],
  ottoman:["Mehmed","Emine","Hüsein","Fatma","Osmān","Ajxe","Ismāil","Zeineb","Murād","Hatidje"],
  hellenic:["Dimitri","Elenī","Stavrô","Maria","Panajôt","Sôfia","Kôsta","Despinā","Jôrgô","Vasilikī"],
  albanian:["Gjergj","Donikā","Lekë","Marā","Ndre","Fatimē","Zef","Drandē"],
  pannonian:["Istvān","Erzsēbet","Lāszlô","Katalin","Mātjās","Ilônā","Gergely","Zsôfiā","Bālint","Anikô"],
  danubian:["Ștefan","Ilinkā","Vasile","Marīa","Rādu","Ancā","Dumitru","Sāftā","Neagôe","Stankā"],
  circassian:["Nart","Adıif","Aslan","Guaxe","Bibars","Setenay","Timur","Dahenagô","Kazbek","Zerıfe"],
  turkic:["Aisulu","Batır","Gülnar","Kanat","Ainur","Tôktar","Zere","Erlan","Sarıbala","Ajgül"],
  georgian:["Giôrgi","Nīnô","Vaxtang","Tamar","Davit","Ketevan","Zurab","Mziā","Levan","Rusudan"],
  persian:["Rôstam","Gôharxād","Xīrīn","Dāriūx","Parvāne","Behzād","Nasrīn","Ferejdūn","Zarīn","Kūrôx"]
};
const FAMILY = {
  finnic:["Kivi","Rānd","Sār","Raud","Kolk","Kur","Põder","Jārv","Kosken","Lain","Nēm","Tūļ",
    "Kalā","Vôrk","Purjē","Sōla","Meçā","Läte"],
  lowgerman:["Smit","Bôrk","Pill","Turm","Strāl","Brün","Müllôr","Torr","Kōpman","Bôdeker",
    "Rēder","Schütt","Wulf","Lübke","Kruse","Hōlst"],
  scand:["Havstēn","Nôrdby","Sigurd","Strand","Bôdvar","Fjôrd","Lundgren","Vīkar"],
  slavic:["Kova","Volk","Lis","Grod","Volkov","Petr","Zubar","Mêlnik","Bôndar","Sôkôl",
    "Ždan","Kalina","Trav","Rîbak"],
  baltic:["Kalniņš","Bērziņš","Ozols","Liepa","Jankauskas","Petrauskas","Balčius","Vilkas",
    "Ģērmanis","Sīlis"],
  romance:["Ponte","Ros","Cort","Mar","Pedr","Roch","Zorzi","Contarīn","Morôsin","Dandôl",
    "Grimani","Vendramin","Bembô","Falēr","Loredan"],
  german:["Steiner","Hôfer","Grubēr","Wagnēr","Pichlēr","Ebnēr","Môsēr","Lechnēr"],
  polish:["Kôwalski","Nôwak","Wiśniewski","Zieliński","Lewandôwski","Dąbrôwski"],
  belarusian:["Bôndar","Kavalčuk","Kuźma","Hryb","Šuškevič","Sauka"],
  ukrainian:["Čôrnohuz","Melnyk","Kôvalenkô","Bôndarenkô","Hrytsenkô","Ševčenkô","Lymarenkô","Stepanenkô"],
  yiddish:["Rôytman","Fishbeyn","Zilbershteyn","Grinberg","Kôrnblum","Vaynshteyn","Tôyber","Mandlboym"],
  slovak:["Hôrvath","Kôváč","Baláž","Krajčír","Dubovský"],
  slovene:["Kraševec","Zupan","Kôvačič","Vidmar","Pôtôčnik"],
  croatian:["Marulić","Bôžić","Vlahôvić","Kôvačić","Perôjević","Šimunić"],
  bulgarian:["Bôtev","Kôlev","Ivanôv","Petkôv","Zlatev"],
  macedonian:["Trajkôvski","Kôčôv","Ristôvski","Dôneski"],
  venetian:["Contarīn","Morôsin","Dandôl","Grimani","Vendramin","Bembô","Falēr","Loredan","Zorzi"],
  italian:["Vissconti","Sfôrtsa","Gôntsaga","Bôrrômeô","Ôrsini","Kôlônna","Malatesta"],
  occitan:["Peirôl","Aimeric","Rôkafôrt","Ventadôrn","Belcaire"],
  friulian:["Della Tôr","Savôrgnan","Kôlôredô","Manin"],
  tatar:["Girai","Xôdja","Bôra","Karaman","Sarıbey"],
  armenian:["Ayvazian","Manukian","Sarkisian","Ôhanian","Bagratian"],
  ottoman:["Kôdjā","Demirdji","Tuzdju","Bôstandji","Karamān","Ak-Bey","Sarıoglu","Xahin"],
  hellenic:["Kômninô","Palēolôg","Vlastô","Kantakuzin","Trikupī","Andrônikô"],
  albanian:["Dukagjin","Kastriôt","Thôpiā","Zenebix","Muzakā","Arianit"],
  pannonian:["Kôvāç","Sabô","Tôth","Nemet","Farkas","Bīrô","Halāsz","Mēsāros","Rēvēsz","Vārhedji"],
  danubian:["Munteān","Popā","Kôjôkāru","Fierāru","Lupu","Barbu","Ursu","Dobre","Vlādut"],
  circassian:["Xhaguaj","Nexay","Kudaberd","Beslaney","Xhapaç","Tlebzu","Xerjes","Zeux"],
  turkic:["Aitbay","Djumabek","Nôgai","Kipçak","Kanglı","Baraq","Djanibek","Ürgençi"],
  georgian:["Dadiani","Gurieli","Çavçavadze","Abaxidze","Eristavi","Xervaxidze","Mikeladze"],
  persian:["Herātı","Sīstānı","Nīxāpūrı","Farrôx","Ansārı","Karīmı","Bāxtiārı","Marvazı"]
};
/* offices, with SEVERAL deeds each so the same title is not the same story */
const TITLES = [
  ["amirāl","admiral",["who broke the blockade off this coast","who lost half a squadron in the shoals and was pardoned anyway",
    "who charted the roads nobody else would enter","whose flag still hangs in the customs hall"]],
  ["generāl","general",["who held the line here through one winter","who never fought here but retired here",
    "who quartered eight thousand men on the town and was thanked for it","who paid the garrison out of his own purse"]],
  ["direktôr","company director",["who financed the first quay","who bought the whole valley and then died",
    "who moved the works here against every survey","whose signature is on the founding charter"]],
  ["rektôr","rector",["who chartered the school before the town","who taught forty years and refused a bishopric",
    "who left his library to the borough","who argued the town's case at court and won"]],
  ["posādnik","trade-city head",["who ran the counting-house for forty years","who kept the gauge honest when nobody was watching",
    "who was twice removed and twice reinstated","who wrote the by-laws the state later copied"]],
  ["batle","mayor",["the first to be elected, and the last to be forgiven","who drained the marsh at municipal expense",
    "who is remembered for a bridge and a scandal","who held the seat through three changes of flag"]],
  ["mytnik","toll-taker",["whose ledgers are the town's oldest paper","who undercounted for twenty years and was loved for it",
    "who built the weighhouse that still stands","who caught the great salt fraud"]],
  ["lōts","pilot",["who charted the approach nobody else would take","who took the first deep-draught ship over the bar",
    "who died on the bar and has a light named for him","who knew the channel by the sound of it"]],
  ["kapitān","captain",["who wintered here with a broken keel and never left","who brought the first cargo and the first plague",
    "whose crew founded half the parish","who is buried under the chapel floor"]],
  ["kanônik","canon",["who kept the register through the fire","who founded the almshouse",
    "who excommunicated the whole council once","who copied the charter by hand when the seal was lost"]],
  ["injenēr","engineer",["who cut the lock and drowned proving it","who moved a river fifty paces",
    "who built the mole against advice, and it held","whose survey stakes became the street plan"]],
  ["voivôd","voivode",["who granted the market right","who fortified it and then abandoned it",
    "who settled two hundred families here in one autumn","who is remembered for the tax and not the wall"]]
];
const EVENTS = [
  ["traktāt","treaty",["a treaty signed here","the peace conference nobody expected to hold"]],
  ["batāl","battle",["a battle fought here","a skirmish that got called a battle"]],
  ["vrak","wreck",["a ship lost on the approach","the wreck that closed the channel for a season"]],
  ["brand","fire",["the fire that took the old town","the fire that started in the rope-walk"]],
  ["ūv","flood",["the flood the dykes did not hold","the year the river changed its bed"]],
  ["pest","plague",["the plague year","the quarantine that lasted three winters"]],
  ["mirakôl","miracle",["a miracle attested in the parish book","the weeping ikon and the crowd it drew"]],
  ["turg","market",["the spring market that used to be held here","the fair that outgrew the town"]],
  ["vôrk","the catch",["the season the nets came in full","the run of herring that paid for the church"]],
  ["frid","peace",["the peace concluded at this crossing","the truce that held for ninety years"]],
  ["sīgel","the seal",["the charter sealed on this spot","the day the town got its own seal"]],
  ["mutin","the mutiny",["the mutiny of the salt-carters","the rising the garrison joined"]],
  ["kômet","the comet",["the comet the whole district saw","the star that stood over the harbour"]],
  ["jǟtalv","the hard winter",["the winter the lagoon froze to the bar","the ice-year the wolves came in"]],
  ["skuld","the debt",["the debt that ruined the founding house","the bankruptcy that transferred the charter"]]
];
const SAINTS = ["Amīk","Mārta","Pēter","Jāns","Anna","Klarā","Nikolaj","Katerinā","Laurēns","Mīkel",
  "Sīmôn","Elenī","Vīt","Barbarā","Dômnik","Ursulā","Blāsi","Margrete","Rôk","Panteleimôn",
  "Spiridôn","Genovēv","Kôsmā","Damiān"];
const MARGINALIA = [
  ["Äbtīd","not known","a surveyor's marginal 'not known' copied as the name"],
  ["Näekartô","see the chart","a cross-reference on the draft sheet, copied as the name"],
  ["Tyhjä","blank","the name-field was left blank, and 'blank' was filed as the name"],
  ["Samasô","the same","a clerk's ditto mark read as a word"],
  ["Kaksrūnô","two letters","a two-letter abbreviation nobody could expand"],
  ["Äbmērk","unmarked","the sheet said 'unmarked' where the name should have been"],
  ["Kolôn","the column","a column heading slipped down into the entry row"],
  ["Vīdesô","folio four","the folio number was read as the settlement's name"],
  ["Ütsluk","one gap","the gap left for a name was itself given a name"],
  ["Sammô","ditto","the ditto of a ditto, three towns down the page"],
  ["Provīs","provisional","the word stamped on the draft sheet outlived the draft"],
  ["Krôsdôr","crossed out","the crossed-out entry was the one that got copied"]
];
const FOUNDERS = [
 ["the Chamber","chartered the works and took the naming right with it"],
 ["a shipping house","put its own money in the quay and its own name on the gate"],
 ["the Service","planned it — a podestā's grid, drawn before anyone lived there"],
 ["a guild of masters","moved a whole trade here in one season"],
 ["the Fleet","needed the yard, and the town followed the yard"],
 ["the rail company","named it after its own junction number until the name stuck"],
 ["a salt monopoly","held the licence and built housing to keep its carters"],
 ["the College","put a technical school here first and the town grew round it"],
 ["a mining concession","sank the shafts and laid out four streets"],
 ["an insurance syndicate","underwrote the harbour and got the charter in return"],
 ["a religious house","held the land and let the market onto it"],
 ["the customs board","needed a post, and the post needed a town"]
];

/* What the place actually IS, read off its own notes — a HINT, not a rule.
   Used only to colour the modifier, and only sometimes. Applied to the head as
   well it became a formula: every harbour ends in -hafõn, every foundry says
   iron. Real places are named for a dead admiral, a saint, or a clerk's
   mistake, and the suffix does not have to agree with the freight manifest. */
const SENSEMAP = [
  [/\b(iron|ore|steel|smelt|foundr)/i, ["iron"]],
  [/\b(timber|forest|wood|mill|pine|sawn)/i, ["forest","backwoods","wood","pinewood","tree"]],
  [/\b(harbour|harbor|port|quay|deepwater|anchorage|roads|shipyard|landing)/i,
    ["harbour","quay","port","haven","mole","landing","anchorage"]],
  [/\b(salt|brine)/i, ["salt","salt-lake","salt-flat"]],
  [/\b(canal|lock)\b/i, ["channel","lock","canal"]],
  [/\b(rail|junction|marshalling|gauge)/i, ["road","market","ford"]],
  [/\b(grain|wheat|corn|granar)/i, ["field","market","plain"]],
  [/\b(fish|fishing|herring|nets)/i, ["fish","net","harbour","shore"]],
  [/\b(coal|mining|mine|copper|sulphur|marble|mercury)/i, ["stone","crag","iron","gold","silver"]],
  [/\b(naval|fleet|garrison|fortress|castle|citadel|redoubt)/i,
    ["fortress","castle","walled town","stronghold-camp","anchor","tower"]],
  [/\b(bridge|crossing|ford)/i, ["bridge","ford"]],
  [/\b(spa|springs?|thermal|baths)/i, ["spring","well","water"]],
  [/\b(vineyard|wine|orchard|garden|market gardens?)/i, ["field","garden","plain"]],
  [/\b(marsh|swamp|bog|flats)/i, ["marsh","flats","polder"]],
  [/\b(lake|lagoon|liman)/i, ["lake","bay","shore"]],
  [/\b(island|isle|spit|dune)/i, ["island","islet","sand","dune","shore"]],
  [/\b(pass|gorge|gate|isthmus|narrows|threshold)/i, ["gate","pass","valley","sound","strait"]],
  [/\b(estate|manor|rent)/i, ["manor","field","holding"]],
  [/\b(oil|refiner|chemical|works|aviation|industr)/i, ["works","field","market"]],
  [/\b(amber|gold)/i, ["gold","silver"]],
  [/\b(church|parish|monaster|abbey|shrine)/i, ["church","abbey","holy"]],
  [/\b(customs|toll|counting|bonded|financ|insuran)/i, ["market","market-town","gate","warehouse"]]
];
function senses(ctx){
  const src=((ctx&&ctx.notes)||"")+" "+((ctx&&ctx.founds_what)||"");
  const out=[];
  SENSEMAP.forEach(([re,gl])=>{ if(re.test(src)) gl.forEach(g=>out.push(g)); });
  return out;
}
/* nudge toward entries whose gloss matches what the place is — a minority of
   the time, so the trade is one possible reason among many, not the reason */
const SENSEBIAS = 0.3;
function biased(pool,want){
  if(!want||!want.length) return pool;
  const hit=pool.filter(x=>want.some(w=>String(x[1]).toLowerCase().includes(w)));
  return (hit.length && Math.random()<SENSEBIAS) ? hit : pool;
}

/* pick a modifier from a quarry the region actually draws on */
/* A purpose-built site has no inherited name — so Nelôxia founds it instead.
   The question is never "would it exist" but WHO founded it, WHEN, and WHY. */
const FOUNDING_ERAS = {
 hanseatic:["a charter granted to a trading company; the works came before the town"],
 charter:["a crown or company foundation, laid out on a surveyor's grid"],
 rail:["a rail-and-industry foundation — the state laid the line, then the town"],
 federal:["a federal new town: planned housing, a technical school, and one industry"]
};
function foundingNote(c,era){
  const e=FOUNDING_ERAS[era]||FOUNDING_ERAS.charter, f=pick(FOUNDERS);
  return `a Nelôxian foundation, not an inherited town${c.founds_what?" — "+c.founds_what:""}: ${e[0]}. ${up(f[0])} ${f[1]}.`;
}

/* not every quarry needs its own person-names; fall back to a near relative */
const NAMEKIN={venetian:"italian",friulian:"italian",occitan:"romance",romance:"italian",
  macedonian:"bulgarian",belarusian:"ukrainian",slovak:"polish",slovene:"croatian",
  albanian:"albanian",tatar:"tatar",armenian:"armenian",scand:"scand",german:"german"};
function poolFor(map,q){ return map[q]||map[NAMEKIN[q]]||map.finnic; }
function modOf(cults,ctx){
  /* the quarry is chosen by the region, never by the freight. Steering it to
     whichever quarry owns a word for "iron" made the ore towns all sound alike
     and pulled them off their own ground. */
  const q=pick(cults);
  return pick(biased(QMODS[q]||QMODS.finnic,senses(ctx)));
}
function headIn(q){ const h=HEADS[q]||HEADS.finnic; return pick(h); }

const REGPROF = {
 /* cult = the quarries that plausibly named this ground, in rough order of
    weight. The state runs White Sea → Riviera → Odessa → Aden, so the loan
    possibilities have to run that far too. */
 "Karelia & the North":{cult:["finnic","scand","ukrainian","yiddish"],ch:"reserve",
   w:{patron:6,event:8,desc:30,trans:6,folk:12,saint:2,acc:6,keep:30}},
 "Livonian Core":{cult:["finnic","baltic","german","lowgerman","yiddish"],ch:"interior",
   w:{patron:5,event:6,desc:16,trans:5,folk:16,saint:3,acc:7,keep:42}},
 "Lithuanian Spine":{cult:["baltic","polish","yiddish","lowgerman","finnic"],ch:"port",
   w:{patron:12,event:8,desc:14,trans:10,folk:12,saint:4,acc:6,keep:34}},
 "Prussian–Pomeranian Coast":{cult:["lowgerman","polish","german","scand","baltic","yiddish"],ch:"port",
   w:{patron:20,event:10,desc:18,trans:14,folk:8,saint:5,acc:6,keep:19}},
 "Eastern Corridor":{cult:["polish","belarusian","ukrainian","yiddish","slovak","baltic"],ch:"frontier",
   w:{patron:8,event:22,desc:12,trans:6,folk:14,saint:4,acc:8,keep:26}},
 /* Odessa was a polyglot free port: Ukrainian, Yiddish, Greek, Italian, French,
    Tatar and Armenian all named streets and suburbs there. */
 "Moldavian Arc & Black Sea":{cult:["ukrainian","danubian","yiddish","hellenic","italian","ottoman","bulgarian","armenian","tatar","circassian","georgian","persian","finnic"],ch:"frontier",
   w:{patron:12,event:18,desc:12,trans:12,folk:10,saint:8,acc:7,keep:21}},
 "Pannonian Bridge":{cult:["pannonian","german","slovak","croatian","yiddish"],ch:"interior",
   w:{patron:6,event:8,desc:10,trans:5,folk:18,saint:6,acc:8,keep:39}},
 "Alpine–Adriatic Arm":{cult:["german","slovene","friulian","venetian","italian"],ch:"romance",
   w:{patron:12,event:8,desc:14,trans:8,folk:10,saint:16,acc:6,keep:26}},
 "Dalmatian Coast":{cult:["venetian","croatian","italian","hellenic"],ch:"romance",
   w:{patron:14,event:8,desc:12,trans:12,folk:8,saint:20,acc:6,keep:20}},
 "Western Alpine & Riviera Arc":{cult:["occitan","italian","venetian","friulian","german"],ch:"romance",
   w:{patron:16,event:8,desc:10,trans:12,folk:8,saint:22,acc:6,keep:18}},
 "Thracian–Macedonian Corridor":{cult:["ottoman","bulgarian","macedonian","albanian","hellenic","turkic","persian"],ch:"frontier",
   w:{patron:8,event:18,desc:10,trans:6,folk:14,saint:10,acc:8,keep:26}},
 /* the Fleet enclave: a garrison town at the corridor's mouth, and every fleet
    town in history is named half by people who came ashore from somewhere else */
 "Sevastopol · Federal City":{cult:["tatar","ukrainian","hellenic","italian","armenian","circassian","georgian","turkic","persian","finnic"],ch:"port",
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
/* fold a name to bare letters, so "Kemô" and "Kem" compare equal */
const flat=s=>String(s).toLowerCase()
  .replace(/[ôöõō]/g,"o").replace(/[āäǟ]/g,"a").replace(/[ēë]/g,"e")
  .replace(/[īï]/g,"i").replace(/[ūü]/g,"u").replace(/[çćč]/g,"c")
  .replace(/[ñń]/g,"n").replace(/[šş]/g,"s").replace(/[žż]/g,"z")
  .replace(/[^a-z]/g,"");
const BANNED_CHARS=/[îûâÎÛÂ]/;
const BANNED_SENSE=/(merd|lōd|sildô)/i;
function valid(nx){ return !BANNED_CHARS.test(nx) && !BANNED_SENSE.test(nx); }

/* The head is FREE — of the town's trade AND of its coordinates. Towns are
   named for all manner of reasons: a dead admiral, a saint, a joke, a place
   eight hundred miles away. Landlocked Hafenberg exists; so does inland
   Newport. Nothing here filters a suffix by what is or is not outside. */
function headFrom(cults,ctx){
  return pick(HEADS[pick(cults)]||HEADS.finnic);
}
function headOf(cults,ctx){ return headFrom(cults,ctx); }
/* heads a plain description may take — landscape and settlement words only.
   Institution heads (-kolēgi, -vīla) are point-foundations: they need a founder
   or a patron saint behind them, not a colour. */
function plainHeadOf(cults,ctx){
  const c=cults.filter(k=>k!=="romance");
  return headFrom(c.length?c:["finnic"],ctx);
}
/* Terrain is a suggestion, not a licence check. Plenty of the world's names sit
   on ground that contradicts them, and the ones that don't were mostly named
   by someone who had just arrived from elsewhere. */
const ALLFEAT=[].concat.apply([],Object.keys(TERRFEAT).map(k=>TERRFEAT[k]));
function featOf(terrain,ctx){
  const t=TERRFEAT[terrain];
  return (t && Math.random()<0.45) ? pick(t) : pick(ALLFEAT);
}
/* join a modifier to a head-suffix, head-final like all Nelôxi compounds */
function joinHead(stem,head){ return up(stem)+head.replace(/^-/,""); }


/* ── how the outside world names it ─────────────────────────────────────────
   The exonym is its own decision, not a copy of the local name. Six real
   mechanisms; canon anchors: Uusatôm↔Odessa (old name persists),
   Kunislinnô↔Kunixa (ceremonial doublet), Dūnabôrk/Daugavpils (ledger vs
   street), Marīsô↔Marzeja (the other side's own form).                       */
function strip(s){
  return s.replace(/ô/g,"o").replace(/[āǟ]/g,"a").replace(/ē/g,"e").replace(/ī/g,"i")
          .replace(/[ōȫ]/g,"o").replace(/ū/g,"u").replace(/ä/g,"a").replace(/ö/g,"o")
          .replace(/ü/g,"u").replace(/õ/g,"o").replace(/ç/g,"ts").replace(/x/g,"ks");
}
const EXOSTRAT = [
 ["persists", (nx,ctx)=>ctx.anachronism ? (ctx.local_hint||ctx.exonym_hint||nx)
                                        : (ctx.exonym_hint||ctx.site),
   "the pre-Nelôxian name simply persisted abroad — the Uusatôm ↔ Odessa case: the state renamed it, the world did not follow."],
 ["anglicized", (nx)=>strip(nx),
   "the world took the Nelôxi name and stripped what it could not spell — the diacritics fall away in foreign print and timetables."],
 ["calque", (nx,ctx,gloss)=>{
     /* only a genuine quoted gloss can be calqued — the story is prose, and
        calquing prose produced nonsense like "Nobodyrenamed". No gloss, no
        calque: fall back to the anglicized form. */
     const m=/'([^']{2,40})'/.exec(gloss||"");
     if(!m) return strip(nx);
     const g=m[1].replace(/\(.*?\)/g,"").trim().toLowerCase();
     if(!g||/\b(at|the|who|and|homeland|pattern)\b/.test(g)||/[+\/]/.test(g))
       return strip(nx);
     const M={"new":"New","harbour":"haven","harbor":"haven","sea":"sea","fortress":"burgh",
       "lake":"lake","land":"land","river-bend":"reach","shore":"shore","island":"isle",
       "market-town":"market","walled":"wall","town":"ton","rapids":"falls","backwoods":"wood",
       "bay":"bay","hill":"hill","mountain":"mount","valley":"vale","field":"field","strait":"sound",
       "quay":"wharf","river":"water","cape":"ness","islet":"holm","village":"thorpe","works":"works",
       "gold":"Gold","iron":"Iron","salt":"Salt","stone":"Stan","great":"Great","little":"Little",
       "black":"Black","red":"Red","green":"Green","grey":"Grey","bright":"Bright","pale":"Pale",
       "north":"North","south":"South","east":"East","west":"West","empty":"Bare","crooked":"Crook",
       "old":"Old","snow":"Snow","ice":"Ice","frost":"Frost","sun":"Sun","moon":"Moon","wave":"Wave",
       "storm":"Storm","wind":"Wind","fish":"Fish","backwoods ":"wood"};
     const w=g.split(/[\s-]+/).filter(Boolean).slice(0,2).map(x=>M[x]||x);
     if(!w.length) return strip(nx);
     const out=w.join("");
     return out.charAt(0).toUpperCase()+out.slice(1).toLowerCase();
   },
   "the world translated the meaning rather than the sound — the way Finnish Tukholma renders Stockholm, or 'new harbour' comes out as Newhaven."],
 ["thirdparty", (nx,ctx)=>ctx.local_hint||ctx.exonym_hint||(ctx.anachronism?nx:ctx.site),
   "the world knows it by the name of whoever shipped there — the merchants' form, not the state's and not the locals'."],
 ["ceremonial", (nx)=>{
     const s=strip(nx);
     return s.replace(/^([A-Z][a-z]{2,4})/, m=>m)+ (/x/i.test(nx)?"":"ia");
   },
   "the formal register travelled instead of the everyday one — the Kunislinnô ↔ Kunixa split, with the charter name reaching foreign atlases first."],
 ["same", (nx)=>nx,
   "no divergence: the Nelôxi name is what the world uses, diacritics and all. Boring, and often what actually happens."]
];
/* every mechanism applied to the CHOSEN name, so the exonym is its own decision */
function exonymOptions(nx,ctx,gloss,keep){
  const out=[];
  EXOSTRAT.forEach(s=>{
    let ex;
    try{ ex=s[1](nx,ctx,gloss); }catch(e){ ex=null; }
    if(!ex) return;
    if(out.some(o=>o.ex===ex)) return;
    out.push({key:s[0],ex:ex,how:s[2]});
  });
  if(keep&&!out.some(o=>o.key==="same")) out.unshift({key:"same",ex:nx,
    how:"the local name is also the exonym — nothing was renamed, so nothing diverged."});
  return out;
}
function rollExonym(nx,ctx,gloss,keep){
  if(keep) return {ex:(ctx.anachronism?(ctx.local_hint||ctx.exonym_hint||ctx.site):(ctx.exonym_hint||ctx.site)),
    how:"the local name is also the exonym — nothing was renamed, so nothing diverged."};
  const w=[["persists",34],["anglicized",22],["calque",14],["thirdparty",12],["ceremonial",8],["same",10]];
  const tot=w.reduce((s,x)=>s+x[1],0); let r=Math.random()*tot, key="persists";
  for(const [k,v] of w){ if((r-=v)<=0){ key=k; break; } }
  const s=EXOSTRAT.find(x=>x[0]===key);
  let ex=s[1](nx,ctx,gloss)||strip(nx);
  return {ex:ex, how:s[2], exkey:key};
}

/* ── the seven strategies + retain ──────────────────────────────────────────
   Each returns {nx, layer, strategy, story}. The story is the point: it says
   WHY the name exists, which is what makes a candidate pickable.            */
const STRAT = {
 patron(c){
   const cult=pick(c.cults), t0=pick(TITLES), t=[t0[0],t0[1],pick(t0[2])];
   const fam=pick(poolFor(FAMILY,cult)), giv=pick(poolFor(GIVEN,cult));
   const r=Math.random();
   if(r<.45){ const h=headOf(c.cults,c);
     return {nx:joinHead(fam,h[0]),layer:"hybrid",strategy:"patron",head:h[0],
       story:`for ${t[1]} ${giv} ${fam}, ${t[2]}; the ${h[1]} took the family name.`}; }
   if(r<.7){ const h=headOf([cult==="slavic"?"slavic":"finnic"],c);
     return {nx:joinHead(t[0],h[0]),layer:"native",strategy:"patron",
       story:`named for the office, not the man — the ${t[1]}'s ${h[1]}. ${up(giv)} ${fam} held it first.`}; }
   if(r<.85) return {nx:fam+"ovô",layer:"hybrid",strategy:"patron",
     story:`Slavic possessive: '${fam}'s place'. ${t[1]} ${giv} ${fam} ${t[2]}.`};
   return {nx:"Kunis"+headOf(["finnic","lowgerman"],c)[0].replace(/^-/,""),layer:"hybrid",strategy:"patron",
     story:`a crown foundation — kunis- 'king's', the same element as Kunislinnô.`};
 },
 event(c){
   const e0=pick(EVENTS), e=[e0[0],e0[1],pick(e0[2])], r=Math.random();
   if(r<.4){ const h=headOf(c.cults,c);
     return {nx:joinHead(e[0],h[0]),layer:"native",strategy:"event",
       story:`${e[2]}; the ${h[1]} kept the word and lost the memory.`}; }
   if(r<.7){ const f=featOf(c.terrain,c);
     return {nx:up(e[0])+loc(f[0]),layer:"native",strategy:"event",
       story:`${e[2]} — literally '${e[1]} at the ${f[1]}'. Fossilized as one word.`}; }
   /* fossilization: clip the phrase until it stops meaning anything */
   /* fossilize by dropping the HEAD's tail at a vowel, not by truncating blind */
   const f=featOf(c.terrain,c), stem=up(e[0]);
   /* wear the ending off at a syllable boundary, but never down to a stump:
      a 2-letter remnant reads as a typo, not as erosion */
   let tail=f[0].replace(/^([^aeiouäöüõôāēīōū]*[aeiouäöüõôāēīōū][^aeiouäöüõôāēīōū]?).*/, "$1");
   if(tail.length<3) tail=f[0];
   const nx=stem+tail;
   return {nx:nx,layer:"native",strategy:"event",
     story:`${e[2]}. The full phrase was '${e[1]} ${f[1]}' — four centuries wore the ending off it, and nobody now hears the event in the name.`};
 },
 desc(c){
   const f=featOf(c.terrain,c), r=Math.random();
   const m=modOf(c.cults,c);
   const phrase=pick([
     "what the first surveyors wrote down","the entry in the oldest land-roll",
     "how the carters asked for it, and it stuck","the name on the earliest toll-list",
     "plain description, never improved on","what the place was called before anyone wrote it down"]);
   if(r<.5)
     return {nx:up(m[0])+f[0],layer:"native",strategy:"descriptive",head:f[0],
       story:`'${m[1]} ${f[1]}' — ${phrase}.`};
   const h=plainHeadOf(c.cults,c);
   return {nx:joinHead(m[0],h[0]),layer:c.cults[0]==="finnic"?"native":"hybrid",strategy:"descriptive",head:h[0],
     story:`'${m[1]} ${h[1]}' — ${phrase}.`};
 },
 trans(c){
   /* a transfer must carry a name that is actually Nelôxi. Donors whose name is
      just their own kept local form (a "keep local" pick) produced absurdities
      like "carried whole from Klaipėda (Klaipėda)" AND a duplicate city name. */
   const donors=CITIES.filter(d=>d.nelox && d.region!==c.region &&
     d.nelox.toLowerCase()!==d.site.toLowerCase());
   if(!donors.length) return STRAT.desc(c);
   const taken=new Set(CITIES.filter(d=>d.nelox&&d.site!==c.site)
                             .map(d=>d.nelox.toLowerCase()));
   const d=pick(donors), r=Math.random();
   const label=`${d.nelox} (${d.site})`;
   if(r<.45) return {nx:"Uus"+d.nelox.toLowerCase(),layer:"native",strategy:"transferred",
     story:`settlers out of ${label} named it for home — uus- 'new', the Uusatôm pattern.`};
   if(r<.7) return {nx:"Nova "+d.nelox,layer:"hybrid",strategy:"transferred",
     story:`the Romance settler-pattern 'Nova + homeland', as Nova Trentô. The founders came from ${label}.`};
   /* bare transfer only if it would not collide with a name already in use */
   if(taken.has(d.nelox.toLowerCase()))
     return {nx:"Uus"+d.nelox.toLowerCase(),layer:"native",strategy:"transferred",
       story:`settlers out of ${label} named it for home, distinguishing it with uus- 'new' because the old town still holds the bare name.`};
   return {nx:d.nelox,layer:"native",strategy:"transferred",
     story:`the name travelled and the meaning did not: carried whole from ${label} by its founders, `+
       pick(["and most people here have no idea it is a borrowed name",
         "who never explained it and were never asked",
         "and the two towns have been confused in the post ever since",
         "as a claim of continuity that nobody now remembers making"])+"."};
 },
 folk(c){
   /* the local name misheard and re-analysed as words it actually resembles.
      Scored across EVERY quarry the region draws on — matching on first letter
      alone locked every M-town onto the single M-modifier. */
   const src=((c.anachronism?c.local_hint:"")||c.site||"Nam").replace(/[^A-Za-zÀ-ɏ]/g,"");
   const low=src.toLowerCase();
   /* two pools kept apart: the first half may be re-heard as a modifier, but
      the second must land on a FEATURE, or you get "great green" with no noun */
   const modPool=[], featPool=(TERRFEAT[c.terrain]||[]).slice();
   c.cults.forEach(q=>{ (QMODS[q]||[]).forEach(m=>modPool.push(m));
                        (HEADS[q]||[]).forEach(h=>featPool.push([h[0].replace(/^-/,""),h[1]])); });
   if(!modPool.length) QMODS.finnic.forEach(m=>modPool.push(m));
   if(!featPool.length) HEADS.finnic.forEach(h=>featPool.push([h[0].replace(/^-/,""),h[1]]));
   const score=(w,chunk)=>{
     let n=0; const a=w.toLowerCase();
     while(n<a.length&&n<chunk.length&&a[n]===chunk[n]) n++;
     if(n===0&&a[0]===chunk[0]) n=1;
     return n;
   };
   /* split the source somewhere in the middle and re-analyse both halves */
   const cut=Math.max(2,Math.min(low.length-1,2+Math.floor(Math.random()*3)));
   const head=low.slice(0,cut), tail=low.slice(cut);
   const rank=(chunk,pool)=>{
     const scored=pool.map(w=>[w,score(w[0],chunk)]).filter(x=>x[1]>0)
                      .sort((a,b)=>b[1]-a[1]);
     if(!scored.length) return pick(pool)||pick(QMODS.finnic);
     const best=scored[0][1];
     const tier=scored.filter(x=>x[1]>=Math.max(1,best-1));
     /* a narrow tier re-elects the same word every roll — 'Nagykanizsa' kept
        landing on nôvi because nothing else scored as high. Widen to the best
        few so the echo stays audible without becoming a lookup. */
     const wide=tier.length>=5?tier:scored.slice(0,Math.max(7,tier.length));
     const hit=pick(wide);
     return (hit&&hit[0])||pick(pool)||pick(QMODS.finnic);
   };
   /* Re-analysis usually catches ONE element, not both: crayfish kept 'cray'
      whole and only heard "fish" in -visse. Deciding the suffix off the old
      spelling every time is what made these read as transliterations. */
   const ear=Math.random();
   let a = ear<.45 ? rank(head,modPool) : pick(modPool);
   let b = ear<.45 ? pick(featPool) : rank(tail,featPool);
   if(ear>=.9){ a=rank(head,modPool); b=rank(tail,featPool); }  /* both, rarely */
   if(!a||!a[0]) a=pick(QMODS.finnic);
   if(!b||!b[0]) b=featOf(c.terrain,c);
   const f=(a[0]===b[0])?featOf(c.terrain,c):b;
   const nx=up(a[0])+f[0];
   return {nx:nx,layer:"nativized",strategy:"folk-etymology",head:f[0],
     story:pick([
       `nobody renamed it — '${src}' was misheard as ${a[0]} '${a[1]}' + ${f[0]} '${f[1]}', and the wrong reading has been the official one so long that the false meaning is taught in the local school.`,
       `a re-analysis, not a renaming: '${src}' sounded enough like ${a[0]} '${a[1]}' + ${f[0]} '${f[1]}' that the clerks wrote what they heard, and the town has explained itself that way ever since.`,
       `the folk etymology won. '${src}' has nothing to do with ${a[1]} or ${f[1]}, but the arms show both, and arguing with the arms is a losing case.`,
       `the name was reinterpreted within a generation of the accession — '${src}' became ${a[0]} '${a[1]}' + ${f[0]} '${f[1]}', which is wrong, and is now the etymology on the town's own signage.`])};
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
   if(r<.7){ const src=((c.anachronism?c.local_hint:"")||c.site||"Nam").replace(/[^A-Za-zÀ-ɏ]/g,"");
     const cut=src.slice(0,Math.max(3,Math.ceil(src.length/2)));
     return {nx:up(cut)+"ô",layer:"nativized",strategy:"accident",
       story:`the copyist's hand ran off the edge of the sheet: '${src}' was entered as this, and the truncation was never queried.`}; }
   /* metathesis of an INTERIOR consonant cluster — how Xerez became sherry —
      not a first-letter swap, which just reads as a typo */
   const src=((c.anachronism?c.local_hint:"")||c.site||"Nam").replace(/[^A-Za-zÀ-ɏ]/g,"");
   let sw=src;
   const m2=/^(.{2,}?)([aeiouAEIOU])([bcdfgklmnprstvz])([aeiouAEIOU])/.exec(src);
   if(m2) sw=m2[1]+m2[3]+m2[2]+m2[4]+src.slice(m2[0].length);
   else if(src.length>4) sw=src.slice(0,2)+src[3]+src[2]+src.slice(4);
   if(sw===src) return STRAT.desc(c);
   return {nx:up(sw.toLowerCase()),layer:"nativized",strategy:"accident",
     story:pick([`two syllables changed places in the first printed atlas, and the atlas outsold its own correction.`,
       `the name was reversed in the mouth before it was reversed on the map — the way Xerez became sherry.`,
       `a compositor set the cluster backwards; nobody with authority read the proof.`])};
 },
 found(c){
   /* the state builds a town: name it for the works, the founder, or the year */
   const r=Math.random(), note=foundingNote(c,c.era||"charter");
   if(r<.4){ const m=modOf(c.cults,c), h=headOf(c.cults,c);
     return {nx:joinHead(m[0],h[0]),layer:"native",strategy:"founded",
       story:`${note} Named for the thing itself: '${m[1]} ${h[1]}'.`}; }
   if(r<.7){ const cult=pick(c.cults), fam=pick(poolFor(FAMILY,cult)), h=headOf(c.cults,c);
     return {nx:joinHead(fam,h[0]),layer:"hybrid",strategy:"founded",
       story:`${note} It carries the founding house's name — ${fam}.`}; }
   const f=featOf(c.terrain,c);
   return {nx:"Uus"+f[0],layer:"native",strategy:"founded",
     story:`${note} Called simply the new ${f[1]} while it was being built, and never renamed — the Uusatôm pattern.`};
 },
 keep(c){
   /* the reference name may be a Soviet/imperial coinage that never existed in
      this timeline — in that case "keeping the local name" keeps the substrate
      form, not the impossible one */
   if(c.founding==="foundation"){
     /* nothing to retain — but that is an opportunity, not an obstacle */
     const h=headOf(c.cults,c), m=modOf(c.cults,c);
     return {nx:joinHead(m[0],h[0]),layer:"native",strategy:"founded",key:"found",
       story:`no inherited name to keep — ${foundingNote(c,c.era||"charter")} Its first name is simply what it was for: '${m[1]} ${h[1]}'.`};
   }
   if(c.anachronism){
     const sub=c.local_hint;
     if(!sub) return {nx:"—",layer:"raw loan",strategy:"retained",keep:true,
       story:`nothing inherited to keep here, and no substrate name on record — treat it as a foundation and name it for what the state built.`};
     return {nx:sub,layer:"raw loan",strategy:"retained",keep:true,
       story:`keep the substrate name — NOT "${c.site}", which never existed in this timeline (${c.anachronism}) The locals went on calling it ${sub}, and the state saw no reason to change it.`};
   }
   const why = pick({
     interior:["the gravity principle: the Finnic layer belongs to the water, and this is estate-and-upland country — the state never had a reason to rename it.",
       "an estate name, and estates outlast administrations. The rent-roll kept the spelling and so did everyone else.",
       "too small to be worth a charter and too old to be worth changing; the parish register simply never updated.",
       "the landowners were here before the state and are still here; their name for it is the one on the deeds."],
     frontier:["an inland seam — the corridor's names stay raw by design; renaming here would read as erasure, not administration.",
       "a border town keeps its own name as a matter of pride, and the customs house found it easier to print than to argue.",
       "two languages already called it this, which made it the one thing nobody was fighting about.",
       "the gauge changed here but the name did not — the state's interest stopped at the rails."],
     romance:["the route already had a name in the language of whoever charted the coast, and the merchants kept using it.",
       "the notaries wrote it this way for four hundred years, and the notaries outlasted three flags.",
       "the shipping registers are the real authority here, and they never re-registered the town.",
       "the saint's day is named for it, not the other way round; you cannot rename a feast."],
     reserve:["the deep native layer already named it, and the name is older than the administration reading it.",
       "the Karelian form was the local form and the state's clerks were local; nothing needed translating.",
       "kept because it was already Finnic — this is the one region where the substrate and the state agree."],
     port:["a name on every manifest in the Baltic is not worth changing; the freight would not have followed.",
       "the harbour was known by this name in four counting-houses before the state held it.",
       "the pilots' charts said this, and you do not re-letter a chart lightly."]
   }[c.ch]||["held raw as a fossil: the spelling preserves whoever named the place, foreign scars and all."]);
   return {nx:c.site,layer:"raw loan",strategy:"retained",story:why,keep:true};
 }
};
const LABEL={patron:"Patron",event:"Event",desc:"Descriptive",trans:"Transferred",
  folk:"Folk-etymology",saint:"Saint",acc:"Accident",keep:"Keep local",
  found:"Foundation",hist:"Historical"};

function weights(prof,era){
  const m=ERAS[era].m, out=[];
  for(const k in prof.w){
    const key = k==="keep"?"keep":k;
    out.push([k, prof.w[k]*(m[key]!==undefined?m[key]:1)]);
  }
  return out;
}
function rollStrategy(prof,era,forceWild,isFoundation){
  if(forceWild) return pick(["patron","event","desc","trans","folk","saint","acc"]);
  let w=weights(prof,era);
  if(isFoundation){
    /* no inherited name exists: drop retain and folk-etymology, add foundation */
    w=w.filter(([k])=>k!=="keep"&&k!=="folk");
    w.push(["found",34]);
  }
  const tot=w.reduce((s,x)=>s+x[1],0);
  let r=Math.random()*tot;
  for(const [k,v] of w){ if((r-=v)<=0) return k; }
  return "desc";
}

/* one candidate; retries until it passes the orthographic + sense guards */
/* why a name from the far end of the sphere is standing here */
const WILDWHY = [
 "The vocabulary is from the other end of the sphere — a corridor family who settled out of the eastern trade and never went back.",
 "Out of register for this ground: the surveyor was a corridor man and named it in his own words, and nobody with authority objected.",
 "A garrison rotated home from the eastern stations and brought the word with them; it outlasted the regiment.",
 "The charter was drawn in a Nelosphere port a very long way from here, and the clerk used the vocabulary in front of him.",
 "A refugee community named its own quarter and the quarter outgrew the town.",
 "The naming came with the money — the concession-holders were easterners, and it is their word on the deed.",
 "Nobody local can parse it. That has never once stopped a name."
];

function roll(ctx,prof,era){
  for(let i=0;i<24;i++){
    /* The federation is enormous and the Nelosphere is larger still — White Sea
       to the Riviera to Odessa to Aden, and for centuries out through East
       Neloxia to Herat. People moved along all of it, and they named things
       where they landed. One name in seven comes from somewhere else entirely. */
    const wild = Math.random()<0.14;
    const key = rollStrategy(prof,era,wild,ctx.founding==="foundation");
    const cults = wild ? [pick(Object.keys(HEADS))] : prof.cult;
    const c = Object.assign({},ctx,{cults:cults,ch:prof.ch,era:era,
      anachronism:ctx.anachronism,local_hint:ctx.local_hint,site:ctx.site,
      founding:ctx.founding,founds_what:ctx.founds_what});
    const r = STRAT[key](c);
    if(!valid(r.nx)) continue;
    /* the failure this whole rework exists to prevent: Kem → "Kemô" is not a
       name, it is the same name wearing a hat. Compare folded, not literal. */
    if(!r.keep && ctx.site && flat(r.nx)===flat(ctx.site)) continue;
    r.key=key; r.wild=wild&&key!=="keep";
    const ex=rollExonym(r.nx,ctx,r.story,!!r.keep);
    r.exonym=ex.ex; r.exostory=ex.how; r.exokey=ex.exkey||"";
    return r;
  }
  return Object.assign(STRAT.keep(Object.assign({},ctx,{cults:prof.cult,ch:prof.ch})),{key:"keep"});
}

/* ── state ────────────────────────────────────────────────────────────────── */
let mode="gaz", basket=[], pending=null, currentOut=null, currentKey="", showDone=false;
const ROLLABLE = CITIES.filter(d=>!d.norename);

function controls(){
  const eraOpts=Object.keys(ERAS).map(k=>`<option value="${k}">${esc(ERAS[k].name)}</option>`).join("");
  if(mode==="gaz"){
    const groups={};
    ROLLABLE.filter(d=>showDone||!d.nelox).forEach(d=>{ (groups[d.region]=groups[d.region]||[]).push(d); });
    let opts="";
    Object.keys(groups).forEach(rg=>{
      opts+=`<optgroup label="${esc(rg)}">`;
      groups[rg].sort((a,b)=>b.pop-a.pop).forEach(d=>{
        const mark=(d.anachronism?" ⚠":"")+
          (d.nelox?(d.source==="picked"?"  ✔ "+d.nelox:"  ✓ "+d.nelox):"");
        opts+=`<option value="${esc(d.site)}">${esc(d.site)}${mark}</option>`;
      });
      opts+="</optgroup>";
    });
    $("ctrls").innerHTML=
      `<div class="fgrp"><label for="city">City (✓ = already canon)</label><select id="city">${opts}</select></div>`+
      `<div class="fgrp"><label for="era">Era</label><select id="era">${eraOpts}</select></div>`+
      `<button class="go" id="go">Roll 8 names</button>`+
      `<div class="fgrp" style="flex:0 0 auto"><label>&nbsp;</label>`+
      `<button class="mode" id="tdone" aria-pressed="${showDone}">${showDone?"showing all":"undecided only"}</button></div>`;
    $("city").addEventListener("change",()=>draw(true));
    $("tdone").addEventListener("click",()=>{showDone=!showDone;controls();draw(true);});
  } else {
    const rgOpts=Object.keys(REGPROF).map(k=>`<option value="${esc(k)}">${esc(k)}</option>`).join("");
    const tOpts=Object.keys(TERRFEAT).sort().map(t=>`<option value="${t}">${t}</option>`).join("");
    $("ctrls").innerHTML=
      `<div class="fgrp"><label for="rg">Region</label><select id="rg">${rgOpts}</select></div>`+
      `<div class="fgrp"><label for="tr">Terrain</label><select id="tr">${tOpts}</select></div>`+
      `<div class="fgrp"><label for="nm">Local name (optional)</label><input id="nm" placeholder="e.g. Vilkija" autocomplete="off"></div>`+
      `<div class="fgrp"><label for="era">Era</label><select id="era">${eraOpts}</select></div>`+
      `<button class="go" id="go">Roll 8 names</button>`;
    $("rg").addEventListener("change",()=>draw(true)); $("tr").addEventListener("change",()=>draw(true));
  }
  $("era").addEventListener("change",()=>draw(true));
  $("go").addEventListener("click",()=>draw(true));
}

function context(){
  if(mode==="gaz"){
    const d=ROLLABLE.find(x=>x.site===$("city").value)||ROLLABLE[0];
    return {site:d.site,region:d.region,terrain:d.terrain,notes:d.notes,
            exonym_hint:d.exonym_hint,former:d.former,local_hint:d.former,anachronism:d.anachronism,
            on_record:d.on_record,source:d.source,nelox:d.nelox,layer:d.layer,gloss:d.gloss,hint:d.hint,pop:d.pop,
            founding:d.founding,founds_what:d.founds_what};
  }
  const nm=($("nm").value||"").trim();
  return {site:nm,region:$("rg").value,terrain:$("tr").value,notes:"",
          exonym_hint:"",former:"",local_hint:"",anachronism:"",
          on_record:false,source:"",nelox:"",layer:"",gloss:"",hint:"",pop:0,
          founding:"inherited",founds_what:""};
}

function drawCtx(ctx,prof,era){
  const w=weights(prof,era).slice().sort((a,b)=>b[1]-a[1]);
  const tot=w.reduce((s,x)=>s+x[1],0);
  const mix=w.map(([k,v])=>`${LABEL[k]} ${Math.round(v/tot*100)}%`).join(" · ");
  let h="";
  if(mode==="gaz"){
    h+=`<b>${esc(ctx.site)}</b> — ${esc(ctx.terrain)}; ${esc(ctx.notes)}. `;
    h+=ctx.exonym_hint?`A historical outside form is on record: <b>${esc(ctx.exonym_hint)}</b> (a candidate, not a decision). `:"";
    if(ctx.founding==="foundation") h+=`<br><b>⌂ A Nelôxian foundation</b>${ctx.founds_what?" — "+esc(ctx.founds_what):""}: the real-world town is purpose-built, so no name is inherited. The state builds its own here — date it, attribute it, name it for what it does. `;
    if(ctx.anachronism) h+=`<br><span class="warn">⚠ "${esc(ctx.site)}" cannot be the in-world name:</span> ${esc(ctx.anachronism)} It is a real-world map reference only. `;
    if(ctx.nelox) h+=`<br><span style="color:${ctx.source==="picked"?"#1a7f4b":"var(--ink)"};font-weight:600">`+
      `${ctx.source==="picked"?"✔ You chose":"✓ On record as"} ${esc(ctx.nelox)}</span>`+
      ` (${esc(ctx.layer)}${ctx.gloss?" — "+esc(ctx.gloss):""})`+
      `${ctx.source==="picked"?" — recorded in data/toponym-picks.tsv":" — from world/gazetteer.md"}. Re-rolling replaces it. `;
    else h+=`<br>Nelôxi name: <b>open</b>. `;
    h+=`${ctx.former?"Former name: <b>"+esc(ctx.former)+"</b>. ":""}Exonym: <b>${ctx.exonym_hint?esc(ctx.exonym_hint)+" (candidate)":"open"}</b>. `;
  }
  h+=`<br><span style="color:var(--ink3)">Strategy mix for ${esc(prof.ch)} · ${esc(ERAS[era].name)}: ${mix}</span>`;
  $("ctx").innerHTML=h;
}

function draw(reroll){
  const ctx=context();
  if(pending&&pending.site!==(ctx.site||"(new)")){ pending=null; }
  const prof=REGPROF[ctx.region]||REGPROF["Livonian Core"];
  const era=$("era").value;
  drawCtx(ctx,prof,era);

  /* stable candidate set: only re-roll on demand or when the context changes */
  const key=(ctx.site||"(new)")+"|"+ctx.region+"|"+ctx.terrain+"|"+era;
  if(!reroll && currentOut && currentKey===key){
    renderCards(currentOut,ctx); return;
  }
  currentKey=key;
  const out=[];
  /* the hint, where one exists, is always offered as a real raw-loan candidate */
  if(ctx.hint) out.push({nx:ctx.hint,layer:"raw loan",strategy:"historical",key:"hist",
    exonym:ctx.exonym_hint||ctx.hint,exokey:"persists",
    exostory:"the same form abroad — a route name is already an international name.",
    story:`the genuine historical / trade-route form on record for this place — the name the routes actually carried.`});
  /* eight DISTINCT candidates — a repeated name wastes a card */
  /* eight DISTINCT candidates — and not three variations on the same head, which
     is what made a roll read as repetitive even when the names differed */
  for(let guard=0; out.length<8 && guard<160; guard++){
    const r=roll(ctx,prof,era);
    if(out.some(o=>o.nx===r.nx)) continue;
    if(r.head && out.filter(o=>o.head===r.head).length>=1 && guard<110) continue;
    /* nor three cards opening on the same stem — Nôvihalôm / Nôvigas /
       Nôvikirchen are three names only in the strictest sense */
    const pre=r.nx.slice(0,4).toLowerCase();
    if(out.some(o=>o.nx.slice(0,4).toLowerCase()===pre) && guard<120) continue;
    if(out.filter(o=>o.key===r.key).length>=3 && guard<130) continue;
    out.push(r);
  }
  /* guarantee the keep-local option is present */
  if(ctx.founding!=="foundation"&&!out.some(o=>o.key==="keep")&&ctx.site){
    out[out.length-1]=Object.assign(STRAT.keep(Object.assign({},ctx,{cults:prof.cult,ch:prof.ch})),
      {key:"keep",exonym:ctx.exonym});
  }

  /* say WHY an out-of-register name is standing here — and never say it twice
     in the same roll, which reads as boilerplate rather than as a reason */
  const why=WILDWHY.slice().sort(()=>Math.random()-.5);
  let wi=0;
  out.forEach(o=>{ if(o.wild) o.story+=" "+why[wi++%why.length]; });

  currentOut=out;
  renderCards(out,ctx);
}

function renderCards(out,ctx){
  const done=ROLLABLE.filter(d=>d.nelox).length;
  $("prog").textContent=`${done} named · ${ROLLABLE.length-done} open`;
  $("cnt").textContent=`${out.length} for ${ctx.site||"a new place"}`;
  $("cards").innerHTML=out.map((o,i)=>{
    const inB=basket.some(b=>b.nx===o.nx&&b.site===(ctx.site||""));
    return `<div class="card${o.key==="keep"?" keep":""}">
      <div class="nx">${esc(o.nx)}</div>
      <div class="story">${esc(o.story)}</div>
      <div class="tags">
        <span class="tag s">${esc(LABEL[o.key]||o.strategy)}</span>
        <span class="tag l">${esc(o.layer)}</span>
        ${o.wild?'<span class="tag">wildcard</span>':""}
      </div>
      <button class="take${inB?" on":""}" data-i="${i}">${inB?"✓ picked":"Pick this name →"}</button>
    </div>`;
  }).join("");

  $("cards").querySelectorAll(".take").forEach(b=>{
    b.addEventListener("click",()=>{
      const o=out[+b.dataset.i];
      if(!o) return;
      const key=o.nx+"|"+(ctx.site||"");
      const at=basket.findIndex(x=>x.nx+"|"+x.site===key);
      if(at>=0){ basket.splice(at,1); pending=null; }
      else {
        /* stage 2: the exonym is chosen FOR this name, not bundled with it */
        pending={site:ctx.site||"(new)",region:ctx.region,nx:o.nx,
          local:o.nx,
          layer:o.layer,strategy:LABEL[o.key]||o.strategy,story:o.story,
          opts:exonymOptions(o.nx,ctx,o.story,o.key==="keep")};
      }
      draw(); drawPending(); drawBasket();
    });
  });
}

function drawPending(){
  const w=$("pendwrap");
  if(!pending){ w.innerHTML=""; $("pendsect").hidden=true; return; }
  $("pendsect").hidden=false;
  w.innerHTML=
    `<div class="panel"><div style="margin-bottom:12px">You chose <span class="nx" style="font-size:22px">${esc(pending.nx)}</span> for <b>${esc(pending.site)}</b>.
     <div class="story" style="margin-top:6px">${esc(pending.story)}</div>
     <div style="margin-top:10px;font-size:11px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--ink3)">Exonym</div></div>
     <div class="cards">`+
    pending.opts.map((o,i)=>`<div class="card">
       <div class="nx" style="font-size:21px">${esc(o.ex)}</div>
       <div class="story">${esc(o.how)}</div>
       <div class="tags"><span class="tag s">${esc(o.key)}</span></div>
       <button class="take" data-x="${i}">Use this exonym</button>
     </div>`).join("")+
    `<div class="card keep">
       <div class="nx" style="font-size:21px;color:var(--ink4)">— open</div>
       <div class="tags"><span class="tag">defer</span></div>
       <button class="take" data-x="-1">Decide later</button>
     </div></div>
     <div class="bactions"><button class="take" id="pcancel">Cancel this pick</button></div>`;
  w.querySelectorAll(".take[data-x]").forEach(btn=>btn.addEventListener("click",()=>{
    const i=+btn.dataset.x;
    const chosen=i>=0?pending.opts[i]:{ex:"",how:""};
    basket.push({site:pending.site,region:pending.region,nx:pending.nx,local:pending.local,
      exonym:chosen.ex,layer:pending.layer,strategy:pending.strategy,
      story:pending.story,exostory:chosen.how,exokey:chosen.key||""});
    pending=null; draw(); drawPending(); drawBasket();
  }));
  const c=$("pcancel");
  if(c) c.addEventListener("click",()=>{ pending=null; draw(); drawPending(); });
}

function drawBasket(){
  $("bcnt").textContent=basket.length?`${basket.length} name${basket.length>1?"s":""}`:"";
  if(!basket.length){ $("bwrap").innerHTML=`<div class="bempty">Nothing picked yet. Pick candidates and they collect here as copyable rows.</div>`; return; }
  $("bwrap").innerHTML=
    `<table class="btable"><thead><tr><th>Ref</th><th>Nelôxi name</th><th>Exonym</th><th>Layer</th><th>Strategy</th><th></th></tr></thead><tbody>`+
    basket.map((b,i)=>`<tr><td>${esc(b.site)}</td><td class="bnx">${esc(b.nx)}</td><td>${b.exonym?esc(b.exonym):'<span class="pending" style="color:var(--ink4)">— open</span>'}</td><td>${esc(b.layer)}</td><td>${esc(b.strategy)}</td><td><button class="drop" data-i="${i}" aria-label="Remove">×</button></td></tr>`).join("")+
    `</tbody></table>
     <div class="bactions"><button class="go" id="copy">Copy as TSV</button>
     <button class="take" id="clear">Clear all</button></div>
     <textarea id="tsv" readonly spellcheck="false"></textarea>`;
  const tsv="site\tnelox\texonym\tlayer\tstrategy\tgloss\tlocal\n"+
    basket.map(b=>[b.site,b.nx,b.exonym,b.layer,b.strategy,b.story,b.local||""].join("\t")).join("\n");
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
  controls(); draw(true);
}
$("m-gaz").addEventListener("click",()=>setMode("gaz"));
$("m-free").addEventListener("click",()=>setMode("free"));
setMode("gaz"); drawPending(); drawBasket();
</script>
</body>
</html>
"""
