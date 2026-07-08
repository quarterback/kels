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
    dialects:    { title: "Dialects",          sub: "Overview",                     file: "dialects/README.md",               group: "Dialects" },
    metrolect:   { title: "Metrolect",         sub: "Metroplex standard",           file: "dialects/metrolect/metrolect.md",  group: "Dialects" },
    inland:      { title: "Inland",            sub: "Conservative rural",           file: "dialects/inland/inland.md",        group: "Dialects" },
    charter:     { title: "Charter",           sub: "Protocol & ruling log",        file: "college/kels-kolegi-charter.md",   group: "College", toc: true },
    coordination:{ title: "Coordination",      sub: "Running multiple agents",      file: "college/COORDINATION.md",          group: "College" },
    onboarding:  { title: "Rector onboarding", sub: "For a new Rector",             file: "college/NEW-RECTOR-ONBOARDING.md", group: "College" },
    assignments: { title: "Assignments",       sub: "Domain-claim ledger",          file: "college/ASSIGNMENTS.md",           group: "College" },
    contributing:{ title: "Contributing",      sub: "How the language grows",       file: "CONTRIBUTING.md",                  group: "College" },
    delegate:    { title: "Delegate brief",    sub: "Contributor protocol",         file: "college/DELEGATE-BRIEF.md",        group: "Briefs", toc: true },
    corpus:      { title: "Corpus brief",      sub: "Writing genre texts",          file: "college/CORPUS-BRIEF.md",          group: "Briefs", toc: true },
    dailylife:   { title: "Daily-life brief",  sub: "Connective speech",            file: "college/DAILY-LIFE-BRIEF.md",      group: "Briefs" },
    numbers:     { title: "Numbers change",    sub: "Numbers, fractions, letters",  file: "college/CHANGE-BRIEF-numbers.md",  group: "Briefs" }
  };

  var GROUP_ORDER = ["Learn", "Reference", "Reader", "Dialects", "College", "Briefs"];

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

  // --- Home view ----------------------------------------------------------
  function renderHome() {
    showLoading();
    loadDict().then(function (rows) { drawHome(rows.length); })
              .catch(function () { drawHome(null); });
  }

  function drawHome(count) {
    var cards = [
      ["#/coursebook", "Coursebook", "The full reference grammar and master dictionary — canon."],
      ["#/dictionary", "Dictionary", "Search every headword and its gloss, live."],
      ["#/reverse", "Reverse index", "Start from English, find the Nelôxi word."],
      ["#/reader", "Reader", "One scene in two registers, side by side."],
      ["#/verbs", "Verb reference", "The verb system in one digest."],
      ["#/charter", "Charter", "The College's protocol and full ruling log."]
    ];
    var html =
      '<section class="hero">' +
      '<div class="hero-mark">ô</div>' +
      "<h1>Nelô kēļ</h1>" +
      '<div class="pron">the Nelôxi language · <em>nel-OX-ee</em></div>' +
      '<p class="lede">A constructed language with Finnic grammar under multi-directional loan contact — ' +
      "Low German, Scandinavian, and Slavic — kept by the Kēļs Kolēgi, the College of Language.</p>" +
      "</section>" +
      '<div class="stat-row">' +
        '<div class="stat"><div class="num">' + (count != null ? count : "—") + '</div><div class="lbl">headwords</div></div>' +
        '<div class="stat"><div class="num">5+2</div><div class="lbl">noun cases</div></div>' +
        '<div class="stat"><div class="num">12</div><div class="lbl">number base</div></div>' +
        '<div class="stat"><div class="num">2</div><div class="lbl">dialects</div></div>' +
      "</div>" +
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
