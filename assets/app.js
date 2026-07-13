/* Nelô kēļ — static site for the Nelôxi language repository.
   Reads the canonical repo files live and renders them; the coursebook and
   other sources remain the single source of truth (nothing is duplicated here). */

(function () {
  "use strict";

  // --- Page manifest ------------------------------------------------------
  // Each entry is either a rendered-markdown page (`file`) or a custom view
  // (`view`). Grouped for the sidebar.
  var PAGES = {
    home:        { title: "Home",              view: "home",    group: null },
    coursebook:  { title: "Coursebook",        sub: "Grammar & master dictionary", file: "coursebook/nelo-kel-coursebook.md", group: "Learn", toc: true },
    verbs:       { title: "Verb reference",    sub: "The verb system, digested",    file: "coursebook/VERB-REFERENCE.md",     group: "Learn", toc: true },
    dictionary:  { title: "Dictionary",        sub: "Nelôxi → English, searchable", view: "dictionary", group: "Reference" },
    reverse:     { title: "Reverse index",     sub: "English → Nelôxi",             file: "data/reverse-index.md",            group: "Reference", toc: false },
    functions:   { title: "Function words",    sub: "High-frequency glue",          file: "college/FUNCTION-WORDS.md",        group: "Reference", toc: true },
    reader:      { title: "Register showcase", sub: "One scene, two registers",     file: "reader/parallel-showcase.md",      group: "Reader" },
    haggling:    { title: "Haggling dialogue", sub: "Bargaining at the market",     file: "reader/dialogue-haggling.md",      group: "Reader" },
    recipe:      { title: "Mushroom soup",     sub: "A recipe / how-to text",       file: "reader/recipe-mushroom-soup.md",   group: "Reader" },
    folktale:    { title: "The fisher & the sea", sub: "Folktale (past tense)",         file: "reader/folktale-fisher-sea.md",    group: "Reader" },
    calibration: { title: "Calibration texts",  sub: "North Wind · UDHR Art. 1",       file: "reader/calibration-texts.md",      group: "Reader" },
    merchant:    { title: "The merchant & daughter", sub: "Dialogue + simultaneous action", file: "reader/folktale-merchant-daughter.md", group: "Reader" },
    idioms:      { title: "Idioms & sayings",   sub: "Freedom, fate, and other pictures", file: "reader/idioms.md",                 group: "Reader" },
    fisherwife:  { title: "The angler & hearth-mate", sub: "Grimm, translated (Low German)", file: "reader/fisher-and-wife.md",     group: "Reader" },
    ordinance:   { title: "Harbor ordinance",   sub: "A port by-law (civic-legal)",    file: "reader/harbor-ordinance.md",       group: "Reader" },
    ecclesiastes:{ title: "Ecclesiastes 1",     sub: "Wisdom register (translated)",   file: "reader/ecclesiastes-1.md",         group: "Reader" },
    dialects:    { title: "Dialects",          sub: "Overview",                     file: "dialects/README.md",               group: "Dialects" },
    metrolect:   { title: "Metrolect",         sub: "Metroplex standard",           file: "dialects/metrolect/metrolect.md",  group: "Dialects" },
    inland:      { title: "Inland",            sub: "Conservative rural",           file: "dialects/inland/inland.md",        group: "Dialects" },
    tristine:    { title: "Tristine",          sub: "Adriatic Venetian-tilt register", file: "dialects/tristine/tristine.md",   group: "Dialects" },
    pluricentric:{ title: "Pluricentric Nelôxi", sub: "The Atlantic second center (essay)", file: "saharannaise/pluricentric.md", group: "Saharannaise" },
    saharannaise:{ title: "Saharannaise",      sub: "The Atlantic standard",         file: "saharannaise/saharannaise.md",     group: "Saharannaise" },
    commonregister:{ title: "Common Register", sub: "The shared spine of both standards", file: "saharannaise/COMMON-REGISTER.md", group: "Saharannaise" },
    voc:         { title: "Common Vocabulary (VOC)", sub: "Federated index of both standards", file: "saharannaise/VOC.md", group: "Saharannaise" },
    saharannaiseB:{ title: "Domain B lexicon", sub: "Terrain·water·weather·livestock", file: "saharannaise/lexicon-B-terrain-water-weather-livestock.md", group: "Saharannaise" },
    saharannaiseC:{ title: "Domain C lexicon", sub: "Food·kin·market·the day", file: "saharannaise/lexicon-C-food-kin-market-day.md", group: "Saharannaise" },
    saharannaiseA:{ title: "Domain A lexicon", sub: "Admin·documents·port·sea-trade", file: "saharannaise/lexicon-A-admin-maritime.md", group: "Saharannaise" },
    saharcompose:{ title: "Saharannaise composition", sub: "How to write connected prose", file: "saharannaise/composition.md", group: "Saharannaise" },
    saharcaravan:{ title: "The Caravan & the Well", sub: "Desert narrative (corpus text)", file: "saharannaise/reader-caravan.md", group: "Saharannaise" },
    saharshowcase:{ title: "Showcase · asymmetry", sub: "One scene, two standards", file: "saharannaise/showcase-asymmetry.md", group: "Saharannaise" },
    sahartopo:   { title: "Atlanta · toponymy", sub: "Place-names, Nelôxian | Saharannaise", file: "saharannaise/toponymy.md", group: "Saharannaise" },
    charter:     { title: "Charter",           sub: "Protocol & ruling log",        file: "college/kels-kolegi-charter.md",   group: "College", toc: true },
    creole:      { title: "Creole principle",  sub: "The standing vocabulary doctrine", file: "college/CREOLE-PRINCIPLE.md",  group: "College", toc: true },
    texture:     { title: "Metaphor fields",   sub: "Coining with culture, not relex", file: "college/METAPHOR-FIELDS.md",   group: "College", toc: true },
    worklist:    { title: "Translation worklist", sub: "Claimable texts to translate",  file: "college/TEXT-WORKLIST.md",    group: "College", toc: true },
    coordination:{ title: "Coordination",      sub: "Running multiple agents",      file: "college/COORDINATION.md",          group: "College" },
    onboarding:  { title: "Rector onboarding", sub: "For a new Rector",             file: "college/NEW-RECTOR-ONBOARDING.md", group: "College" },
    assignments: { title: "Assignments",       sub: "Domain-claim ledger",          file: "college/ASSIGNMENTS.md",           group: "College" },
    contributing:{ title: "Contributing",      sub: "How the language grows",       file: "CONTRIBUTING.md",                  group: "College" },
    delegate:    { title: "Delegate brief",    sub: "Contributor protocol",         file: "college/DELEGATE-BRIEF.md",        group: "Briefs", toc: true },
    corpus:      { title: "Corpus brief",      sub: "Writing genre texts",          file: "college/CORPUS-BRIEF.md",          group: "Briefs", toc: true },
    dailylife:   { title: "Daily-life brief",  sub: "Connective speech",            file: "college/DAILY-LIFE-BRIEF.md",      group: "Briefs" },
    numbers:     { title: "Numbers",           sub: "Dozenal counting, clock, percent", file: "grammar/12-numbers.md",           group: "Reference", toc: true },
    neloxialore: { title: "Nelôxia — the country", sub: "Geography, scale, posture (lore)", file: "world/neloxia-lore.md",         group: "World" },
    atlantalore: { title: "Atlanta — founding history", sub: "Nelôxia & the Atlantic Sahara (lore)", file: "world/atlanta-lore.md",   group: "World" },
    modernmodel: { title: "Modern Nelôxia — working model", sub: "The expanded ~56M state (draft)", file: "world/modern-neloxia-working-lore-model.md", group: "World" },
    expandedlore:{ title: "The Expanded Nelôxia", sub: "Accession history & framing (lore)", file: "world/neloxia-expanded-lore.md", group: "World" },
    geography:   { title: "Geography",         sub: "The shape of Nelôxia",         file: "world/geography.md",               group: "World" },
    gazetteer:   { title: "Gazetteer",         sub: "Cities & place-names",         file: "world/gazetteer.md",               group: "World", toc: true },
    boundaries:  { title: "Boundaries",        sub: "Canonical borders & units",    file: "world/boundaries.md",              group: "World", toc: true },
    governance:  { title: "Governance",        sub: "The Voice & the Service (polity)", file: "world/governance.md",           group: "World", toc: true },
    names:       { title: "Civil names",        sub: "Local · civil · short-civic forms", file: "world/names.md",              group: "World" },
    namegen:     { title: "Name generator",      sub: "Roll a civil name by region", view: "namegen",                          group: "World" },
    toponymy:    { title: "Toponymy",          sub: "How places get named",         file: "world/toponymy.md",                group: "World", toc: true },
    exonyms:     { title: "Exonyms",           sub: "What Nelôxi calls other lands", file: "world/exonyms.md",                 group: "World", toc: true },
    gr_index:    { title: "Grammar modules",   sub: "Foundation index",             file: "grammar/00-INDEX.md",              group: "Grammar" },
    gr_part:     { title: "The partitive",     sub: "Module 01",                    file: "grammar/01-partitive-case.md",     group: "Grammar", toc: true },
    gr_verb:     { title: "Verb derivation",   sub: "Module 02",                    file: "grammar/02-verb-derivation.md",    group: "Grammar", toc: true },
    gr_grad:     { title: "Gradation",         sub: "Module 03",                    file: "grammar/03-consonant-gradation.md",group: "Grammar", toc: true },
    gr_comp:     { title: "Compounding",       sub: "Module 04",                    file: "grammar/04-compounding.md",        group: "Grammar", toc: true },
    gr_decl:     { title: "Noun declension",   sub: "Module 06 — full case table",  file: "grammar/06-declension.md",         group: "Grammar", toc: true },
    gr_pron:     { title: "Pronouns",          sub: "Module 07 — full paradigm",    file: "grammar/07-pronouns.md",           group: "Grammar", toc: true },
    gr_rel:      { title: "Relations",         sub: "Module 08 — space & time",     file: "grammar/08-relations.md",          group: "Grammar", toc: true },
    gr_tense:    { title: "Tense & aspect",    sub: "Module 09 — saying when",      file: "grammar/09-tense-aspect.md",       group: "Grammar", toc: true },
    gr_adj:      { title: "Adjectives",        sub: "Module 10 — invariance",       file: "grammar/10-adjectives.md",         group: "Grammar", toc: true },
    gr_cmd:      { title: "Commands",          sub: "Module 11 — imperative & hortative", file: "grammar/11-commands.md",       group: "Grammar", toc: true },
    gr_compose:  { title: "Composition",       sub: "Module 14 — sentences & paragraphs", file: "grammar/14-composition.md",    group: "Grammar", toc: true },
    gr_apics:    { title: "Structural profile", sub: "APiCS typological parameters",  file: "grammar/structural-profile-apics.md", group: "Grammar", toc: true },
    bnd_grammar: { title: "Grammar reference", sub: "Complete grammar, one file",   file: "bundles/BUNDLE-grammar-reference.md", group: "Bundles", toc: true },
    bnd_domain:  { title: "Domain agent kit",  sub: "For coining vocabulary",       file: "bundles/BUNDLE-domain-agent.md",   group: "Bundles", toc: true },
    bnd_corpus:  { title: "Corpus agent kit",  sub: "For writing genre texts",      file: "bundles/BUNDLE-corpus-agent.md",   group: "Bundles", toc: true }
  };

  var GROUP_ORDER = ["Learn", "Grammar", "Reference", "Reader", "World", "Dialects", "Saharannaise", "College", "Briefs", "Bundles"];

  var content = document.getElementById("content");
  var sidebar = document.getElementById("sidebar");
  var dictCache = null;      // parsed dictionary rows
  var markedReady = null;    // promise resolving when marked is loaded

  // --- Markdown loader (marked via CDN, graceful fallback) ----------------
  function loadMarked() {
    if (markedReady) return markedReady;
    markedReady = new Promise(function (resolve) {
      if (window.marked) return resolve(true);
      var s = document.createElement("script");
      s.src = "assets/vendor/marked.min.js"; // vendored — self-contained, no CDN needed
      s.onload = function () { resolve(true); };
      s.onerror = function () { resolve(false); };
      document.head.appendChild(s);
    });
    return markedReady;
  }

  function renderMarkdown(text) {
    if (window.marked) {
      window.marked.setOptions({ gfm: true, breaks: false, headerIds: true, mangle: false });
      return window.marked.parse(text);
    }
    // Fallback: show raw text readably.
    var esc = text.replace(/[&<>]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;" }[c];
    });
    return "<pre>" + esc + "</pre>";
  }

  function fetchText(path) {
    return fetch(path, { cache: "no-cache" }).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status + " for " + path);
      return r.text();
    });
  }

  // --- Heading IDs + table of contents ------------------------------------
  function slugify(s) {
    return s.toLowerCase().trim()
      .replace(/[^\w\sÀ-ɏ-]/g, "")
      .replace(/\s+/g, "-")
      .replace(/-+/g, "-");
  }

  function buildToc(container) {
    var heads = container.querySelectorAll("h2, h3");
    if (heads.length < 3) return null;
    var seen = {};
    var items = [];
    heads.forEach(function (h) {
      var base = slugify(h.textContent) || "sec";
      var id = base;
      var n = 1;
      while (seen[id]) { id = base + "-" + (++n); }
      seen[id] = true;
      h.id = id;
      items.push({ id: id, text: h.textContent, level: h.tagName === "H2" ? 2 : 3 });
    });
    var toc = document.createElement("nav");
    toc.className = "toc";
    var html = '<div class="toc-title">On this page</div><ul>';
    items.forEach(function (it) {
      html += '<li class="lvl-' + it.level + '"><a href="#' + it.id + '">' +
        escapeHtml(it.text) + "</a></li>";
    });
    html += "</ul>";
    toc.innerHTML = html;
    return toc;
  }

  function escapeHtml(s) {
    return s.replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  // --- Views --------------------------------------------------------------
  function showLoading() {
    content.innerHTML = '<div class="loading">Loading…</div>';
  }

  function showError(msg) {
    content.innerHTML = '<div class="error"><strong>Could not load this page.</strong><br>' +
      escapeHtml(msg) + "<br><br>If you are viewing locally, serve the folder over HTTP " +
      '(e.g. <code>python3 -m http.server</code>) — opening the file directly blocks fetches.</div>';
  }

  function renderMarkdownPage(page) {
    showLoading();
    Promise.all([loadMarked(), fetchText(page.file)]).then(function (res) {
      var text = res[1];
      var article = document.createElement("article");
      article.className = "prose";
      article.innerHTML = renderMarkdown(text);
      interceptLinks(article);
      content.innerHTML = "";
      if (page.toc) {
        var toc = buildToc(article);
        if (toc) content.appendChild(toc);
      }
      content.appendChild(article);
      focusContent();
    }).catch(function (e) { showError(e.message); });
  }

  // Rewrite links to repo .md files so they route within the site.
  var FILE_TO_ROUTE = {};
  Object.keys(PAGES).forEach(function (k) {
    if (PAGES[k].file) FILE_TO_ROUTE[PAGES[k].file] = k;
  });

  function interceptLinks(root) {
    root.querySelectorAll("a[href]").forEach(function (a) {
      var href = a.getAttribute("href");
      if (!href || href.charAt(0) === "#") return;
      if (/^https?:\/\//.test(href) || href.charAt(0) === "/") {
        if (/^https?:\/\//.test(href)) a.setAttribute("rel", "noopener");
        return;
      }
      var clean = href.split("#")[0].replace(/^\.\//, "").replace(/^(\.\.\/)+/, "");
      if (FILE_TO_ROUTE[clean]) {
        a.setAttribute("href", "#/" + FILE_TO_ROUTE[clean]);
      }
    });
  }

  // --- Dictionary view ----------------------------------------------------
  function parseTsv(text) {
    var lines = text.split(/\r?\n/);
    var rows = [];
    for (var i = 1; i < lines.length; i++) { // skip header
      var line = lines[i];
      if (!line.trim()) continue;
      var tab = line.indexOf("\t");
      if (tab === -1) continue;
      rows.push({ hw: line.slice(0, tab), gl: line.slice(tab + 1) });
    }
    return rows;
  }

  function loadDict() {
    if (dictCache) return Promise.resolve(dictCache);
    return fetchText("data/dictionary.tsv").then(function (t) {
      dictCache = parseTsv(t);
      return dictCache;
    });
  }

  function renderDictionaryPage(initialQuery) {
    showLoading();
    loadDict().then(function (rows) {
      content.innerHTML =
        '<div class="dict-head"><h1>Dictionary</h1>' +
        '<span class="dict-count" id="dict-count"></span></div>' +
        '<p style="color:var(--ink-soft);margin:.2em 0 0;font-family:var(--sans);font-size:15px">' +
        'Headword → gloss, generated from the canonical coursebook. ' +
        'Search matches Nelôxi headwords and English glosses.</p>' +
        '<div class="dict-controls">' +
        '<input id="dict-search" type="search" placeholder="Search headword or meaning…" autocomplete="off" spellcheck="false" />' +
        '</div>' +
        '<table class="dict"><thead><tr><th style="width:26%">Headword</th><th>Gloss</th></tr></thead>' +
        '<tbody id="dict-body"></tbody></table>';

      var input = document.getElementById("dict-search");
      var body = document.getElementById("dict-body");
      var countEl = document.getElementById("dict-count");

      function draw(q) {
        q = (q || "").trim().toLowerCase();
        var frag = "";
        var shown = 0;
        for (var i = 0; i < rows.length; i++) {
          var r = rows[i];
          if (q && r.hw.toLowerCase().indexOf(q) === -1 && r.gl.toLowerCase().indexOf(q) === -1) continue;
          frag += "<tr><td class=\"hw\">" + hl(r.hw, q) + "</td><td class=\"gl\">" + hl(r.gl, q) + "</td></tr>";
          shown++;
        }
        body.innerHTML = frag || '<tr><td colspan="2" class="dict-empty">No entries match “' + escapeHtml(q) + "”.</td></tr>";
        countEl.textContent = q ? (shown + " of " + rows.length + " entries") : (rows.length + " entries");
      }

      var t;
      input.addEventListener("input", function () {
        clearTimeout(t);
        var v = input.value;
        t = setTimeout(function () { draw(v); }, 90);
      });

      if (initialQuery) input.value = initialQuery;
      draw(input.value);
      focusContent();
      if (!initialQuery) input.focus();
    }).catch(function (e) { showError(e.message); });
  }

  function hl(text, q) {
    var safe = escapeHtml(text);
    if (!q) return safe;
    var idx = text.toLowerCase().indexOf(q);
    if (idx === -1) return safe;
    // Highlight on the escaped string by re-finding (query has no HTML-special chars typically).
    var before = escapeHtml(text.slice(0, idx));
    var match = escapeHtml(text.slice(idx, idx + q.length));
    var after = escapeHtml(text.slice(idx + q.length));
    return before + "<mark>" + match + "</mark>" + after;
  }

  // --- Civil-name generator view ------------------------------------------
  // Modern civil MEANING-NAMES (world/names.md): a registered name chosen
  // because it matters to the family — it need not describe birth, place, or
  // origin. The long form may be an image, joke, blessing, complaint, memory,
  // object, or absurd civic artifact; the short civic form is a socially usable
  // compression. This is the proper-name register (charter §63/§73): it is
  // built from canon roots but assembles them freely, and a family name does
  // not have to decode from the outside. Word banks below are [Nelôxi, English]
  // pairs drawn from the master dictionary so the pieces are real words.
  var NAMEGEN = {
    banks: {
      obj:  [["klokkô","bell"],["lampô","lamp"],["lepôl","spoon"],["nugā","knife"],["vôtī","key"],["taul","table"],["kadīr","chair"],["spēgôl","mirror"],["köis","rope"],["nôglô","needle"],["padā","pot"],["livrô","book"],["kandelô","candle"],["pühkin","broom"],["finest","window"],["durô","door"],["taç","cup"],["vôrk","net"],["rūnô","letter"],["knēpô","button"],["küüs","nail"]],
      nat:  [["talv","winter"],["suvi","summer"],["kevä","spring"],["sügü","autumn"],["nēu","snow"],["pakā","frost"],["tormô","storm"],["tūļ","wind"],["pilv","cloud"],["lain","wave"],["lūdô","tide"],["sol","sun"],["kū","moon"],["estēl","star"],["jǟ","ice"],["sōla","salt"],["kivī","stone"],["tuhk","ash"],["suitô","smoke"],["tolmô","dust"],["mudā","mud"],["läte","spring-source"],["müristü","thunder"],["kōit","dawn"]],
      anim: [["kajak","gull"],["kat","cat"],["gos","dog"],["kalā","fish"],["hering","herring"],["hīr","mouse"],["imô","bee"],["mottô","moth"],["krā","crow"],["voss","fox"],["volk","wolf"],["rob","seal"],["obūn","horse"],["lammô","sheep"],["kitsô","goat"],["sigô","pig"],["bēr","bear"],["rēô","roe-deer"],["pakalā","flounder"]],
      emo:  [["lōtū","hope"],["iglū","longing"],["häbū","shame"],["ilo","joy"],["ūpū","pride"],["pōr","fear"],["amōr","love"],["rahu","calm"],["lohū","comfort"],["mūrô","worry"],["mēl","memory"],["unī","dream"],["skuld","debt"],["tôsī","truth"],["mentīd","lie"],["merjagô","fate"],["vaik","calm"]],
      adj:  [["jôvā","good"],["sūr","big"],["petīt","small"],["uus","new"],["vana","old"],["must","black"],["pūn","red"],["sinī","blue"],["rôhī","green"],["grīs","grey"],["nīrô","bright"],["pehmē","soft"],["kôv","hard"],["lent","slow"],["nobē","fast"],["tyhjā","empty"],["tǟs","full"],["rik","rich"],["krōm","crooked"],["blin","blind"],["kerg","light"],["helē","pale"]],
      kin:  [["mǟr","mother"],["pǟr","father"],["poig","son"],["tytār","daughter"],["läpx","child"],["veļ","brother"],["sisār","sister"],["vanamǟr","grandmother"],["vanapǟr","grandfather"],["leskô","widow"],["orvô","orphan"],["nabôr","neighbor"],["amīk","friend"],["vôrô","stranger"],["külalü","guest"],["bebē","baby"],["onkô","uncle"],["tantô","aunt"]],
      work: [["kalā","fish"],["pa","bread"],["sōla","salt"],["olūt","beer"],["melī","honey"],["jôu","flour"],["purjē","sail"],["akôr","anchor"],["bōt","boat"],["dek","deck"],["last","cargo"],["turg","market"],["tōl","toll"],["raud","iron"],["köis","rope"],["vôrk","net"]],
      civic:[["aktô","file"],["registrô","register"],["rūnô","letter"],["sīgel","seal"],["mustlivrô","black-book"],["klokkôtōl","bell-fee"],["manifest","cargo manifest"],["maksômus","tax"],["mytnik","toll-taker"],["kvitô","receipt"]],
      day:  [["matī","morning"],["vespôr","evening"],["nīt","night"],["kesknahtô","midnight"],["pǟvô","day"],["kōit","dawn"],["tīsdag","Tuesday"],["frīdag","Friday"],["setmān","week"],["sôndag","Sunday"]],
      // Attested eventive participles / eventive adjectives (§96 forms).
      evt:  [["syndänü","born"],["kasvanü","raised"],["ärkänü","awakened"],["kirjôtū","written"],["väsinü","grown tired"],["jättänü","spent"]],
      // Dozenal digits, for bureaucratic codes.
      num:  [["jedôn","1"],["dva","2"],["tri","3"],["xtiri","4"],["sedôm","7"]]
    },
    // Given-name pools by cultural quarry (proper-name register: kept as-is).
    given: {
      livonian:  ["Mārta", "Pēter", "Līna", "Jāns", "Märt", "Anna", "Ilze", "Baiba", "Jānis", "Mārtiņš", "Artūrs", "Dace", "Līga", "Edgars", "Andris", "Andres"],
      lowgerman: ["Hans", "Grete", "Klaus", "Trīne", "Jürgen", "Gesche", "Tönnies", "Margrete"],
      slavic:    ["Ivan", "Olga", "Dmitri", "Natālija", "Pavel", "Irina", "Nikolaj", "Marek", "Tomāš", "Katerina"],
      romance:   ["Marc", "Clara", "Ferran", "Carles", "Rosa", "Jordi", "Lluís", "Pau", "Margarida", "Caterina", "Elisa", "António", "João", "Maria", "José", "Ana", "Teresa", "Andrē"],
      saharan:   ["Amādū", "Zāra", "Azīz", "Nūra", "Samīr", "Laila"]
    },
    // Family-name pools (kept phonetically, per world/names.md).
    family: {
      maritime:  ["Kivi", "Rānd", "Sār", "Jorg", "Raud", "Kolk", "Kur", "Dūna", "Mēm", "Gauj", "Neik", "Keid", "Põder", "Kosken", "Vīp", "Jārv", "Petr", "Sten", "Hav"],
      lowgerman: ["Smit", "Bôrk", "Pill", "Turm", "Strāl", "Brün", "Müllôr", "Torr"],
      slavic:    ["Kova", "Volk", "Lis", "Grod", "Lid", "Volkov", "Beogrôd", "Skôpi", "Saraj"],
      romance:   ["Ponte", "Ros", "Cort", "Mar", "Pedr", "Angra", "Roch", "Ilh"],
      place:     ["Stet", "Rosēn", "Grīp", "Grāts", "Laib", "Prag", "Vīn", "Brand", "Triest", "Kors", "Kotôr", "Dürôs", "Split", "Ragūz", "Filipôl", "Sofi", "Odes", "Kônstanç", "Atlant", "Trist"]
    }
  };
  function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
  function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }
  // Naive locative: vowel-final words take -l (kamī → kamīl, klokkô → klokkôl),
  // consonant-final take -ôl (rānd → rāndôl) — matches the canon name forms.
  function loc(w) { return /[aeiouäöüõôāēīōūǟȫî]$/.test(w) ? w + "l" : w + "ôl"; }

  // Each shape builds one registered meaning-name: {nx, en, tag}.
  // nx = the Nelôxi long form; en = English sense; tag = how it reads.
  // The naming register composes canon words freely — a name does not
  // have to explain itself, and some of these deliberately don't.
  var B = NAMEGEN.banks;
  NAMEGEN.shapes = {
    // Plain: one word, no ornament. "Spoon." "Grey."
    plain: function () {
      var w = pick([pick(B.obj), pick(B.nat), pick(B.anim), pick(B.adj)]);
      return { nx: cap(w[0]), en: cap(w[1]), short: cap(w[0]) };
    },
    // Old: the classic origin-descriptor, still on the books.
    old: function () {
      var n = pick(B.nat.concat(B.work)), e = pick(B.evt);
      return { nx: cap(loc(n[0])) + " " + e[0], en: e[1] + " at the " + n[1],
               short: cap(n[0]) };
    },
    // Image: adjective + noun. Sometimes beautiful, sometimes flat.
    image: function () {
      var a = pick(B.adj), n = pick([pick(B.obj), pick(B.nat), pick(B.anim)]);
      return { nx: cap(a[0]) + " " + cap(n[0]), en: "The " + a[1] + " " + n[1],
               short: cap(n[0]) };
    },
    // Pair: two nouns joined with ja "and". Reads old or reads random.
    pair: function () {
      var a = pick(B.nat.concat(B.obj)), b = pick(B.nat.concat(B.emo));
      if (a[0] === b[0]) b = pick(B.emo);
      return { nx: cap(a[0]) + " ja " + cap(b[0]), en: cap(a[1]) + " and " + b[1],
               short: cap(a[0]) };
    },
    // Praise: an abstract lifted whole. "Great Joy." "Full Calm."
    praise: function () {
      var a = pick([["sūr","great"],["nīrô","bright"],["tǟs","full"],["vaik","still"],["jôvā","good"]]);
      var n = pick(B.emo);
      return { nx: cap(a[0]) + " " + cap(n[0]), en: cap(a[1]) + " " + n[1],
               short: cap(n[0]) };
    },
    // Protection: something guards someone. Chosen at hard births.
    guard: function () {
      var n = pick(B.nat), k = pick(B.kin);
      return { nx: cap(n[0]) + " valvā se " + k[0], en: "The " + n[1] + " guards the " + k[1],
               short: "Valvā " + cap(n[0]) };
    },
    // Story: a clause the family kept. Overlong on purpose.
    story: function () {
      var k = pick(B.kin), o = pick(B.obj), d = pick(B.day);
      var v = pick([["kaotā","lost"],["leidā","found"],["unôstā","forgot"],["parandā","mended"],["kandā","carried"]]);
      return { nx: "Se " + k[0] + ", ken " + v[0] + " se " + o[0] + " " + loc(d[0]),
               en: "The " + k[1] + " who " + v[1] + " the " + o[1] + " on a " + d[1],
               short: cap(o[0]) };
    },
    // Event: weather pinned to a day. Sincere or trivial; no way to tell.
    event: function () {
      var n = pick(B.nat), d = pick(B.day);
      return { nx: cap(n[0]) + " " + loc(d[0]), en: cap(n[1]) + " on a " + d[1],
               short: cap(n[0]) };
    },
    // Opaque: two words that share no obvious sense. The family knows.
    opaque: function () {
      var a = pick(B.obj.concat(B.anim)), b = pick(B.day.concat(B.emo).concat(B.work));
      if (a[0] === b[0]) b = pick(B.day);
      return { nx: cap(b[0]) + "-" + a[0], en: cap(b[1]) + " " + a[1],
               short: cap(a[0]) };
    },
    // Clerk: a registry artifact that hardened into a name.
    clerk: function () {
      var c = pick(B.civic), n1 = pick(B.num), n2 = pick(B.num);
      var withCode = Math.random() < 0.6;
      if (withCode) return { nx: cap(c[0]) + " " + n1[0] + "-" + n2[0],
        en: cap(c[1]) + " " + n1[1] + "-" + n2[1], short: cap(c[0]) };
      var a = pick(B.adj);
      return { nx: cap(a[0]) + " " + c[0], en: "The " + a[1] + " " + c[1] + ", as filed",
               short: cap(c[0]) };
    },
    // Grievance: a complaint or a refusal, registered forever.
    spite: function () {
      var pickFrom = Math.random() < 0.5;
      if (pickFrom) {
        var o = pick(B.obj);
        return { nx: "Äb se " + o[0], en: "Not the " + o[1], short: cap(o[0]) };
      }
      var k = pick(B.kin), e = pick([["mentīd","lie"],["skuld","debt"],["tōl","toll"]]);
      return { nx: "Se " + k[0] + " " + e[0], en: "The " + k[1] + "'s " + e[1],
               short: cap(e[0]) };
    },
    // Memory: someone stayed somewhere, or something is still owed.
    memory: function () {
      var k = pick(B.kin), n = pick(B.nat.concat(B.work));
      return { nx: "Se " + k[0] + ", ken jǟmä " + loc(n[0]),
               en: "The " + k[1] + " who stayed at the " + n[1],
               short: cap(n[0]) };
    },
    // Contradiction: it cannot be both. It is both.
    contra: function () {
      var pairs = [[["tyhjā","empty"],["tǟs","full"]],[["vana","old"],["uus","new"]],[["petīt","small"],["sūr","big"]],[["lent","slow"],["nobē","fast"]]];
      var p = pick(pairs), n = pick(B.obj.concat(B.nat));
      return { nx: cap(p[0][0]) + " " + p[1][0] + " " + n[0],
               en: "The " + p[0][1] + " " + p[1][1] + " " + n[1],
               short: cap(n[0]) };
    },
    // Luck at work: the one good day that named a child.
    luck: function () {
      var w = pick(B.work);
      return { nx: cap(w[0]) + " tǟs", en: "The " + w[1] + " came in full",
               short: cap(w[0]) };
    }
  };
  // Tone groups for the picker. "any" samples the lot.
  NAMEGEN.tones = [
    { key: "any",    name: "Any register",        shapes: null },
    { key: "old",    name: "Old forms",            shapes: ["old", "pair", "guard"] },
    { key: "plain",  name: "Plain",                shapes: ["plain", "image", "event"] },
    { key: "story",  name: "Family stories",       shapes: ["story", "memory", "luck"] },
    { key: "joke",   name: "Jokes & opaque",       shapes: ["opaque", "contra", "spite"] },
    { key: "clerk",  name: "Bureaucratic",         shapes: ["clerk"] },
    { key: "grand",  name: "Praise & protection",  shapes: ["praise", "guard", "image"] }
  ];

  function makeName(toneKey) {
    var tone = null;
    for (var i = 0; i < NAMEGEN.tones.length; i++) if (NAMEGEN.tones[i].key === toneKey) tone = NAMEGEN.tones[i];
    var keys = (tone && tone.shapes) ? tone.shapes : Object.keys(NAMEGEN.shapes);
    var m = NAMEGEN.shapes[pick(keys)]();
    var given = pick(NAMEGEN.given[pick(Object.keys(NAMEGEN.given))]);
    var family = pick(NAMEGEN.family[pick(Object.keys(NAMEGEN.family))]);
    return {
      full:  m.nx + " — " + given + " " + family,
      short: m.short + " " + given + " " + family,
      gloss: m.en
    };
  }

  function renderNameGenerator() {
    var toneOptions = "";
    NAMEGEN.tones.forEach(function (t) {
      toneOptions += '<option value="' + t.key + '">' + escapeHtml(t.name) + "</option>";
    });

    content.innerHTML =
      '<div class="dict-head"><h1>Civil-name generator</h1></div>' +
      '<p style="color:var(--ink-soft);margin:.2em 0 0;font-family:var(--sans);font-size:15px">' +
      'Modern civil meaning-names: a registered name chosen because it matters to the family — ' +
      'it does not have to explain itself. The short civic form keeps whatever would stick in ' +
      'public memory. See <a href="#/names">Civil names</a> for the system.</p>' +
      '<div class="ng-controls">' +
      '<select id="ng-tone" aria-label="Register">' + toneOptions + "</select>" +
      '<button id="ng-go" class="ng-go" type="button">Generate names</button>' +
      "</div>" +
      '<div id="ng-results" class="ng-results" aria-live="polite"></div>';

    var toneSel = document.getElementById("ng-tone");
    var results = document.getElementById("ng-results");

    function draw() {
      var frag = "";
      for (var i = 0; i < 8; i++) {
        var n = makeName(toneSel.value);
        frag +=
          '<div class="ng-card">' +
          '<div class="ng-label">Full civil name</div>' +
          '<div class="ng-full">' + escapeHtml(n.full) + "</div>" +
          '<div class="ng-label">Short civic name</div>' +
          '<div class="ng-short">' + escapeHtml(n.short) + "</div>" +
          '<div class="ng-gloss">&ldquo;' + escapeHtml(n.gloss) + '&rdquo;</div>' +
          "</div>";
      }
      results.innerHTML = frag;
    }

    document.getElementById("ng-go").addEventListener("click", draw);
    draw();
    focusContent();
  }

  // --- Home view ----------------------------------------------------------
  function renderHome() {
    var cards = [
      ["#/coursebook", "Coursebook", "The grammar and the master dictionary."],
      ["#/dictionary", "Dictionary", "Search a Nelôxi headword for its gloss."],
      ["#/reverse", "Reverse index", "Start from English, reach the Nelôxi word."],
      ["#/reader", "Reader", "Corpus texts: a market scene, a haggling, a recipe."],
      ["#/namegen", "Name generator", "Roll a civil name in the registry pattern."],
      ["#/verbs", "Verb reference", "The verb system in one page."],
      ["#/charter", "Charter", "The College's protocol and ruling log."]
    ];
    var html =
      '<section class="hero">' +
      '<div class="hero-mark">ô</div>' +
      "<h1>Nelô kēļ</h1>" +
      '<div class="pron">the Nelôxi language · <em>nel-OX-ee</em></div>' +
      '<p class="lede">Reference grammar, course, and dictionary, kept by the Kēļs Kolēgi.</p>' +
      "</section>" +
      '<div class="cards">';
    cards.forEach(function (c) {
      html += '<a class="card" href="' + c[0] + '"><h3>' + c[1] + "</h3><p>" + c[2] + "</p></a>";
    });
    html += "</div>";
    content.innerHTML = html;
    focusContent();
  }

  // --- Sidebar ------------------------------------------------------------
  function buildSidebar() {
    var html = '<a class="nav-link" href="#/home" data-route="home">Home</a>';
    GROUP_ORDER.forEach(function (group) {
      var keys = Object.keys(PAGES).filter(function (k) { return PAGES[k].group === group; });
      if (!keys.length) return;
      html += '<div class="nav-group"><div class="nav-group-title">' + group + "</div>";
      keys.forEach(function (k) {
        var p = PAGES[k];
        html += '<a class="nav-link" href="#/' + k + '" data-route="' + k + '">' +
          escapeHtml(p.title) +
          (p.sub ? '<span class="nl-sub">' + escapeHtml(p.sub) + "</span>" : "") +
          "</a>";
      });
      html += "</div>";
    });
    sidebar.innerHTML = html;
  }

  function markActive(route) {
    sidebar.querySelectorAll(".nav-link").forEach(function (a) {
      a.classList.toggle("active", a.getAttribute("data-route") === route);
    });
  }

  // --- Version stamp --------------------------------------------------------
  // Two independent signals so the reader can always tell they have the latest:
  //  1. data/version.json — GENERATED from the charter alongside the data files,
  //     fetched relatively, so it is always in lockstep with the deployed canon.
  //  2. The repository's latest commit (GitHub API) — when the site last changed.
  function loadVersionStamp() {
    var badge = document.createElement("div");
    badge.className = "version-badge";
    sidebar.insertBefore(badge, sidebar.firstChild);
    var foot = document.getElementById("version-stamp");

    function setText(el, text) { if (el) el.textContent = text; }

    fetch("data/version.json", { cache: "no-cache" })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (v) {
        if (!v) return;
        var canon = "Canon " + v.version + " · " + v.headwords + " headwords · through §" + v.ruling;
        setText(badge, canon);
        setText(foot, canon);
        badge.setAttribute("title", "Generated from the charter with the data files — always matches the content you are reading.");
      })
      .catch(function () {});

    fetch("https://api.github.com/repos/quarterback/kels/commits?per_page=1", { cache: "no-cache" })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (list) {
        if (!list || !list.length) return;
        var c = list[0];
        var when = new Date(c.commit.committer.date);
        var stamp = "updated " + when.toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" }) +
          " " + when.toLocaleTimeString(undefined, { hour: "2-digit", minute: "2-digit" }) +
          " (" + c.sha.slice(0, 7) + ")";
        var line = document.createElement("div");
        line.className = "version-badge-when";
        line.textContent = stamp;
        line.setAttribute("title", (c.commit.message || "").split("\n")[0]);
        badge.appendChild(line);
        if (foot) foot.textContent += " · " + stamp;
      })
      .catch(function () {});
  }

  // --- Router -------------------------------------------------------------
  function parseHash() {
    var h = location.hash.replace(/^#\/?/, "");
    return h || "home";
  }

  function route() {
    var raw = parseHash();
    // Support #/dictionary?q=word
    var qIdx = raw.indexOf("?");
    var query = null;
    if (qIdx !== -1) {
      var qs = raw.slice(qIdx + 1);
      raw = raw.slice(0, qIdx);
      var m = /(?:^|&)q=([^&]*)/.exec(qs);
      if (m) query = decodeURIComponent(m[1].replace(/\+/g, " "));
    }
    var page = PAGES[raw] || PAGES.home;
    markActive(PAGES[raw] ? raw : "home");
    document.body.classList.remove("nav-open");
    window.scrollTo(0, 0);

    if (page.view === "home") renderHome();
    else if (page.view === "namegen") renderNameGenerator();
    else if (page.view === "dictionary") renderDictionaryPage(query);
    else if (page.file) renderMarkdownPage(page);
    else renderHome();

    var t = page.title ? page.title + " · Nelô kēļ" : "Nelô kēļ";
    document.title = t;
  }

  function focusContent() {
    // Accessibility: move focus to content region on navigation without scrolling.
    try { content.focus({ preventScroll: true }); } catch (e) { /* older browsers */ }
  }

  function onHashChange() {
    // Route hashes look like "#/name"; a bare "#id" is an in-page anchor
    // (e.g. a table-of-contents link) — let the browser scroll, keep the view.
    var h = location.hash;
    if (h && h.indexOf("#/") !== 0) return;
    route();
  }

  // --- Wire up ------------------------------------------------------------
  buildSidebar();
  loadVersionStamp();
  window.addEventListener("hashchange", onHashChange);

  document.getElementById("nav-toggle").addEventListener("click", function () {
    document.body.classList.toggle("nav-open");
  });
  document.body.addEventListener("click", function (e) {
    // Close mobile nav when a sidebar link is tapped.
    if (e.target.closest(".nav-link")) document.body.classList.remove("nav-open");
  });

  var quick = document.getElementById("quick-dict");
  if (quick) {
    quick.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        var v = quick.value.trim();
        location.hash = "#/dictionary" + (v ? "?q=" + encodeURIComponent(v) : "");
        quick.value = "";
      }
    });
  }

  route();
})();
