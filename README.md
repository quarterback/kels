# Nelô kēļ — the Nelôxi language

The working repository of the Nelôxi language (*nelô kēļ*): reference grammar, course, dictionary, and the governance materials of the Kēļs Kolēgi (College of Language).

## Website

Browse the whole repository as a site: **https://quarterback.github.io/kels/**

It reads the canonical files directly (never a stale copy) — the coursebook and verb reference as formatted pages, a live-searchable dictionary (Nelôxi → English) and the English → Nelôxi reverse index, the reader texts, the dialect overlays, and the College's charter and briefs. Static, no build step: `index.html` plus `assets/`. To serve it, point GitHub Pages at the branch root (Settings → Pages). To preview locally, run `python3 -m http.server` in the repo root — opening `index.html` as a `file://` path blocks the fetches the site relies on.

## Repository structure

```
coursebook/nelo-kel-coursebook.md   ← CANON. The single source of truth.
college/kels-kolegi-charter.md      ← Contributor protocol + ruling log + collision list
archive/neloxi-language-spec.md     ← Design archive (internal; not reference material)
dialects/                           ← Regional overlays on the standard (metrolect, inland)
data/dictionary.tsv                 ← Machine-readable headword → gloss (generated)
data/headwords.txt                  ← Flat headword list (generated)
```

## The one rule that matters

**The coursebook is the single merge target.** All canonized vocabulary and grammar lives there and only there. The charter's collision list (§7) and the `data/` files are *generated from* the coursebook after each merge — they are derived artifacts, never edited by hand. If any file disagrees with the coursebook, the coursebook wins and the other file gets regenerated.

## How the language grows

1. A contributor takes a domain batch under the charter's rules (`college/kels-kolegi-charter.md`).
2. The batch is submitted with collision notes in the charter's format.
3. The Rector reviews, rules, and merges accepted words into the coursebook.
4. The charter's ruling log records the decision; §7 and `data/` are regenerated.

Nothing is canon until merged.

## Current state

- **542 headwords** across the ten core units plus law & governance, colors & qualities, sport & play, craft & tools, extended kinship, learning & writing, deep maritime, and abstract thought.
- Full reference grammar: 5+2 cases (with temporal use), pronoun-driven verbs, conditional, participles, and eight productive derivational affixes (-ji, -mus/-mys, -ū, -stā, -ldā, -ām, -ôr, -mi).
- A first reader text (*Kalāji ja mer*) and course dialogues throughout.
- Open domains: U18 (emotion nuance), U19 (food, deep).

## Register

Reference materials treat Nelôxi as a language, full stop. Design history and source discussion live only in `archive/` and the charter's backstage sections, never in the coursebook.
