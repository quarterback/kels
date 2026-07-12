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
  // Builds names in the documented registry pattern (world/names.md):
  //   descriptor · given · family   +   short civic form.
  // The descriptor is  [place] [feature-locative] [eventive participle];
  // the short civic form clips the descriptor to the feature's anchor word.
  // Nothing here is canon lexicon — this is the proper-name register
  // (charter §63/§73), so foreign given/family names keep their scars.
  var NAMEGEN = {
    // Eventive participles that close every descriptor.
    participles: [
      { form: "syndänü", gloss: "born" },
      { form: "kasvanü", gloss: "raised" },
      { form: "ärkänü",  gloss: "awakened" },
      { form: "kirjôtū", gloss: "written" }
    ],
    // Landscape / civic features. `loc` is the locative form used in the full
    // descriptor; `anchor` is the clipped word the short civic form keeps.
    features: {
      rand:   { loc: "rāndôl",  anchor: "Rānd",   gloss: "shore" },
      laht:   { loc: "lahtôl",  anchor: "Laht",   gloss: "bay" },
      sar:    { loc: "sārôl",   anchor: "Sār",    gloss: "island" },
      jog:    { loc: "jōgôl",   anchor: "Jōg",    gloss: "river" },
      kot:    { loc: "kōtôl",   anchor: "Kōt",    gloss: "house" },
      borg:   { loc: "bôrgôl",  anchor: "Bôrk",   gloss: "fortress" },
      torn:   { loc: "tornôl",  anchor: "Torn",   gloss: "tower" },
      merd:   { loc: "merdôl",  anchor: "Merd",   gloss: "sea" },
      kirik:  { loc: "kirīkôl", anchor: "Kirīk",  gloss: "church" },
      pont:   { loc: "pontôl",  anchor: "Pont",   gloss: "bridge" },
      lod:    { loc: "lōdôl",   anchor: "Lōd",    gloss: "quay" },
      vec:    { loc: "veçôl",   anchor: "Veç",    gloss: "water" },
      pold:   { loc: "põldôl",  anchor: "Põld",   gloss: "field" },
      kor:    { loc: "kôrôl",   anchor: "Kôr",    gloss: "valley" },
      mets:   { loc: "metsôl",  anchor: "Mets",   gloss: "forest" },
      kald:   { loc: "kaldôl",  anchor: "Kald",   gloss: "bank" },
      jarv:   { loc: "jārvôl",  anchor: "Jārv",   gloss: "lake" },
      spit:   { loc: "spitôl",  anchor: "Spit",   gloss: "spit" },
      targ:   { loc: "tārgôl",  anchor: "Tārg",   gloss: "market" },
      kaj:    { loc: "kājôl",   anchor: "Kāj",    gloss: "quay" },
      mal:    { loc: "māldôl",  anchor: "Māl",    gloss: "ground" },
      sep:    { loc: "sepôl",   anchor: "Sep",    gloss: "smithy" },
      satam:  { loc: "satâmôl", anchor: "Satām",  gloss: "harbor" },
      dun:    { loc: "dunôl",   anchor: "Dun",    gloss: "Danube" },
      raj:    { loc: "rājôl",   anchor: "Rāj",    gloss: "road" },
      munt:   { loc: "muntôl",  anchor: "Munt",   gloss: "mountain" },
      pass:   { loc: "passôl",  anchor: "Pass",   gloss: "pass" },
      maj:    { loc: "mājôl",   anchor: "Māj",    gloss: "house" },
      port:   { loc: "portôl",  anchor: "Port",   gloss: "port" },
      bir:    { loc: "bīrôs",   anchor: "Bīr",    gloss: "well" },
      ilh:    { loc: "ilhôl",   anchor: "Ilh",    gloss: "island" },
      sild:   { loc: "sildôl",  anchor: "Sild",   gloss: "bridge" },
      raudte: { loc: "raudtēôl",anchor: "Raudtē", gloss: "rail line" },
      amt:    { loc: "amtôl",   anchor: "Amt",    gloss: "office" },
      kort:   { loc: "kōrtôl",  anchor: "Kōrt",   gloss: "court" },
      tunn:   { loc: "tunnôl",  anchor: "Tunn",   gloss: "tunnel" },
      karst:  { loc: "karstôl", anchor: "Karst",  gloss: "karst" },
      most:   { loc: "mostôl",  anchor: "Most",   gloss: "bridge" }
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
  // Each region: places that lead the descriptor, the features that fit its
  // terrain, and which given/family pools its people draw from.
  NAMEGEN.regions = [
    { key: "maritime",  name: "Maritime Core",        places: ["Jorg", "Salac", "Muhu", "Vīp", "Rīk", "Andres"],        feats: ["rand", "laht", "sar", "jog", "kot", "kald"],        given: ["livonian", "lowgerman"], family: ["maritime"] },
    { key: "prussian",  name: "Prussian Anchor",      places: ["Kunix", "Pill", "Rausch", "Fisch", "Grīs"],             feats: ["borg", "torn", "merd", "kald", "kirik"],            given: ["lowgerman", "livonian"], family: ["lowgerman"] },
    { key: "vistula",   name: "Vistula Delta",        places: ["Tant", "Elb", "Marian", "Puk", "Stet"],                 feats: ["pont", "lod", "laht", "rand", "vec"],               given: ["slavic", "romance", "livonian"], family: ["slavic", "lowgerman"] },
    { key: "inland",    name: "Baltic Inland",        places: ["Mitau", "Gauj", "Vend", "Tils", "Gold"],                feats: ["pold", "kor", "mets", "kald", "jarv"],              given: ["livonian"], family: ["maritime"] },
    { key: "curonian",  name: "Curonian Land Bridge", places: ["Mēm", "Xaul", "Neik", "Rosēn", "Keid"],                 feats: ["spit", "targ", "kaj", "mal", "pont"],               given: ["livonian"], family: ["maritime"] },
    { key: "slavfront", name: "Slavic Frontier",      places: ["Grod", "Lid", "Volk", "Marīsô", "Kova"],                feats: ["targ", "merd", "mets", "satam", "sep"],             given: ["slavic", "romance"], family: ["slavic"] },
    { key: "karelia",   name: "Karelia",              places: ["Vīp", "Petr", "Sôrt", "Korb", "Järv"],                  feats: ["jarv", "mets", "jog", "laht", "kald"],              given: ["livonian", "slavic"], family: ["maritime", "slavic"] },
    { key: "westrim",   name: "Western Baltic Rim",   places: ["Rostok", "Vism", "Strāl", "Grīp", "Stet"],              feats: ["kaj", "laht", "torn", "rand", "pont"],              given: ["lowgerman"], family: ["lowgerman"] },
    { key: "amber",     name: "Amber Road Corridor",  places: ["Brand", "Prag", "Brün", "Vīn", "Grāts", "Laib"],        feats: ["sild", "raudte", "amt", "kort", "tunn", "karst"],    given: ["romance", "lowgerman"], family: ["romance", "slavic"] },
    { key: "adriatic",  name: "Adriatic Terminals",   places: ["Triest", "Krk", "Cort", "Ponte", "Ros"],                feats: ["satam", "kort", "laht", "maj", "port"],             given: ["romance"], family: ["romance"] },
    { key: "corsica",   name: "Corsican Relay",       places: ["Kors", "Torr", "Mar", "Cort", "Bast"],                  feats: ["torn", "merd", "kirik", "port", "kaj"],             given: ["romance"], family: ["romance"] },
    { key: "dalmatia",  name: "Dalmatian Coast",      places: ["Split", "Ragūz", "Kotôr", "Dürôs", "Shib"],             feats: ["merd", "pont", "laht", "satam", "kald"],            given: ["slavic", "romance"], family: ["romance", "slavic"] },
    { key: "balkan",    name: "Balkan Interior",      places: ["Saraj", "Beogrôd", "Skôpi", "Prixtīn", "Most"],         feats: ["most", "dun", "raj", "mal", "maj"],                 given: ["slavic"], family: ["slavic"] },
    { key: "thrace",    name: "Thracian & Aegean",    places: ["Sofi", "Filipôl", "Balk", "Mar", "Aeg"],                feats: ["pass", "mal", "munt", "merd", "laht"],              given: ["romance", "slavic"], family: ["place"] },
    { key: "blacksea",  name: "Black Sea Littoral",   places: ["Kônstanç", "Odes", "Pont", "Dun", "Mar"],               feats: ["dun", "kaj", "merd", "satam", "laht"],              given: ["romance", "slavic"], family: ["place", "slavic"] },
    { key: "saharan",   name: "Saharan Diaspora (Atlanta)", places: ["Atlant", "Sahar", "Tīr", "Oasi", "Mer", "Mel"],   feats: ["port", "dun", "mal", "bir", "kaj"],                 given: ["saharan"], family: ["place"] },
    { key: "tristense", name: "Tristense Diaspora",   places: ["Trist", "Ilh", "Pedr", "Angra", "Roch", "Mar"],         feats: ["ilh", "rand", "laht", "kald", "port"],              given: ["romance"], family: ["romance"] }
  ];

  function pick(arr) { return arr[Math.floor(Math.random() * arr.length)]; }
  function poolNames(map, keys) {
    var out = [];
    keys.forEach(function (k) { out = out.concat(map[k]); });
    return out;
  }

  // Build one name. `region` is a region object; if `creole` is true, the
  // given and family are drawn from pools other than the descriptor's region.
  function makeName(region, creole) {
    var place = pick(region.places);
    var feat = NAMEGEN.features[pick(region.feats)];
    var ptcp = pick(NAMEGEN.participles);

    var givenKeys = region.given, familyKeys = region.family, mix = null;
    if (creole) {
      var gKey = pick(Object.keys(NAMEGEN.given));
      var fKey = pick(Object.keys(NAMEGEN.family));
      givenKeys = [gKey];
      familyKeys = [fKey];
      mix = region.name + " descriptor · " + gKey + " given · " + fKey + " family";
    }
    var given = pick(poolNames(NAMEGEN.given, givenKeys));
    var family = pick(poolNames(NAMEGEN.family, familyKeys));

    return {
      full:  place + " " + feat.loc + " " + ptcp.form + " " + given + " " + family,
      short: feat.anchor + " " + given + " " + family,
      gloss: ptcp.gloss + " at the " + place + " " + feat.gloss,
      mix:   mix
    };
  }

  function renderNameGenerator() {
    var regionOptions = '<option value="__any">Any region</option>' +
      '<option value="__creole">Creole / mixed</option>';
    NAMEGEN.regions.forEach(function (r) {
      regionOptions += '<option value="' + r.key + '">' + escapeHtml(r.name) + "</option>";
    });

    content.innerHTML =
      '<div class="dict-head"><h1>Civil-name generator</h1></div>' +
      '<p style="color:var(--ink-soft);margin:.2em 0 0;font-family:var(--sans);font-size:15px">' +
      'Names in the registry pattern — <strong>descriptor · given · family</strong>, with the short civic form. ' +
      'See <a href="#/names">Civil names</a> for how the system works.</p>' +
      '<div class="ng-controls">' +
      '<select id="ng-region" aria-label="Region">' + regionOptions + "</select>" +
      '<button id="ng-go" class="ng-go" type="button">Generate names</button>' +
      "</div>" +
      '<div id="ng-results" class="ng-results" aria-live="polite"></div>';

    var regionSel = document.getElementById("ng-region");
    var results = document.getElementById("ng-results");

    function draw() {
      var val = regionSel.value;
      var frag = "";
      for (var i = 0; i < 6; i++) {
        var creole = false, region;
        if (val === "__creole") {
          creole = true;
          region = pick(NAMEGEN.regions);
        } else if (val === "__any") {
          region = pick(NAMEGEN.regions);
        } else {
          region = NAMEGEN.regions.filter(function (r) { return r.key === val; })[0] || NAMEGEN.regions[0];
        }
        var n = makeName(region, creole);
        frag +=
          '<div class="ng-card">' +
          '<div class="ng-full">' + escapeHtml(n.full) + "</div>" +
          '<div class="ng-short">' + escapeHtml(n.short) + "</div>" +
          '<div class="ng-gloss">' + escapeHtml(n.gloss) +
          (n.mix ? ' <span class="ng-mix">· ' + escapeHtml(n.mix) + "</span>" : "") +
          "</div>" +
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
