# Nelôxi — Delegate Brief (Kēļs Kolēgi contributor protocol)

> **READ `college/CREOLE-PRINCIPLE.md` FIRST.** Nelôxi is a five-way maritime creole, NOT a
> Finnic language with loanwords. When you hit a gap, ask which quarry (Low German / Slavic /
> Scandinavian / Romance-Latin / Finnic-core) would own that word and BORROW liberally — do not
> default to Finnic derivation. Abstract/legal/scholarly words come from Romance. Bias toward the
> visible loan. This is the most important rule in the project.

> **Before coining any function word, check `college/FUNCTION-WORDS.md`.** The high-frequency
> glue (pronouns, conjunctions, particles, light verbs, time words, interjections) is ALREADY
> canon. Never write the Estonian equivalent. If a function word isn't in that sheet or the
> headword list, flag it as a gap.


You are a delegate of the **Kēļs Kolēgi** (College of Language), coining vocabulary
for **Nelôxi** (*nelô kēļ*), a constructed language. The founder/Rector rules; you
propose, the Rector reviews and merges. **Nothing you submit is canon until merged.**
Read this whole brief before coining a single word.

Current canon: **v5.26, 1219 headwords.** Authoritative source: the repository —
`coursebook/nelo-kel-coursebook.md` (the language) and `college/kels-kolegi-charter.md`
(rules + full ruling log §1–§92).

---

## STEP 0 — Before you write anything (mandatory)

1. **Pull the current `data/headwords.txt` from the repo HEAD.** Do NOT work from
   memory, a pasted list, or a previous session. Stale batches are the #1 recurring
   failure; every one has been caught and sent back. Check the version tag matches
   the latest charter.
2. **Claim your domain in `college/ASSIGNMENTS.md` before coining.** Batches for
   already-canonized domains are rejected on arrival regardless of quality. Open
   slots are listed there.
3. **Read `college/CREOLE-PRINCIPLE.md` (§79) — the load-bearing vocabulary rule** — then
   skim the charter's recent rulings; the strata, the quarry system, numbers, and
   orthography are all logged there.

## STEP 1 — The hard rules (violating any = batch returned)

- **Check every candidate word against `data/headwords.txt`.** No duplicates. Do NOT
  invent a canon word to justify a collision clearance — that has happened and it
  corrupts the record (§32). If you think a word exists, verify it in the file.
- **Examples use ONLY canon vocabulary.** Every word in an example sentence must be a
  real headword. If you need a word that doesn't exist, that's a GAP — flag it, do
  not fill it. **Look up every verb in `data/reverse-index.md` before writing an
  example.** Reaching for a source-language word (Estonian *aitab*, *jääb*, *ainult*
  etc.) is an automatic batch return (§23). This has happened three times; do not be
  the fourth.
- **A missing word is a finding, not a hole to patch.** The best contributions have
  come from delegates who hit a gap and flagged it (this is how *pǟl*, *kesk*, *nīrā*,
  the device suffix *-in*, and the privative *-tū* all entered canon). Flag gaps
  explicitly in your collision notes.
- **Do not silently declare new suffixes or grammar.** If you notice a productive
  pattern, flag it for the Rector to rule on. One attestation is not a suffix.

## STEP 2 — Phonology & orthography (stay inside the inventory)

- Vowels: a e i o u ä ö y **ô** [ɤ], plus long macron vowels ā ē ī ō ū ǟ ȫ.
  (Note: the language uses **ô**, not õ — as of v4.0. Never write õ.)
- Consonants are soft/Romance-Finnic. **ç** = [ts], **x** = [ʃ], **ñ** = [ɲ],
  **j** = [j], **l·l** = geminate [lː]. No native **b, c (bare), q, w, z**.
- Old-stratum words: no initial consonant clusters, open or simple codas, vowel
  harmony in suffixes (back -ô- / front -e-).
- Late-stratum words MAY have initial clusters (st-, sk-, pr-, kr-, tr-, fl-, gl-, etc.,
  max two consonants).
- **Loanwords may keep a foreign mark** (grapheme or sound) to announce their origin —
  e.g. *flœzī* "donut" keeps œ and z, neither native. Contact loans that spread by ear
  may have loose/variant spelling; the sound is what's fixed. Do this sparingly and
  only for genuine cultural borrowings.

## STEP 3 — The quarries (know which you're drawing from)

Mark each late/loan word with its stratum. Grammar is Livonian-Karelian Baltic-Finnic;
vocabulary is a **five-way creole** (§79, `college/CREOLE-PRINCIPLE.md` — read it first). The
quarries are **CO-PRIMARY**: the map below shows where each is DENSEST, not the only place it
appears. For anything outside the deep Finnic core, borrow from the quarry that owns the domain
rather than defaulting to a Finnic derivation — that default is the drift the doctrine exists to stop.

- **Finnic core (Livonian primary, Karelian secondary)** — the deep core ONLY: body, kin, land,
  the sea, the oldest actions, and the grammar. A **narrow** core, not a broad default; abstract
  and scholarly words go to Romance, not here.
- **Low German** — trade, seafaring, the counting-house, the calendar — AND broad everyday work:
  rooms, buildings, tools, weather, daily verbs. Marked `(late-stratum)`.
- **Scandinavian** — colloquial/street/deck; casual register, spread widely through daily speech.
  Marked `(late-stratum)`; register: informal.
- **Slavic** (Polish/Masurian) — the interior and the Marīsô border: market, food, familiar-kin,
  courtyard, and everyday domestic/agricultural/social life. Marked `(Marīsô, slav)`.
  Adapt: sz/ż/rz → x, ć → ç, ę/ą → eñ/an, ń → ñ. No new phonemes.
- **Romance/Catalan-Latin** — the register of cultivation (§76): learning, law, documents and the
  written word (*livrô*, *eskōl*), the abstract and scholarly, sentiment, refined cuisine, and
  formal speech. Marked `(late-stratum)`. FIRST LOOK when a domain is learned, legal, refined,
  culinary-elevated, or affective-formal — and the home of abstract vocabulary generally.

**Register matters:** modern/urban/colloquial domains borrow FREELY — a high loan ratio
there is correct by design, not a defect (§27, §33). Profanity, tech, and border life
are loan-heavy on purpose. Core/native domains stay native. Do not force native calques
where a loan is natural, and do not force loans where a native word exists.

**Stratum doublets are allowed and encouraged:** a Slavic border word can sit beside a
native one for the same thing (native *pôlū* / Slavic *gribô* "mushroom") — they diverge
by register and dialect. This is a feature.

## STEP 4 — Derivation (use the productive suffixes; don't reinvent them)

- **-ji** — doer, from a VERB (*lugē* → *lugēji* "reader")
- **-õr / -ôr** — person associated with a NOUN/adj (*kēļ* → *kēļôr* "grammarian")
- **-in** — device/instrument that does a verb (*kūlô* → *kūlin* "speaker")
- **-mus / -mys** — result/abstract noun (harmonized; front roots take -mys)
- **-ū** — abstract noun from postposition/quality (*selg* → *selgū* "clarity")
- **-stā** — denominative "engage in X"
- **-ldā** — denominative mental-activity verb (*mõtô*→*mõtôldā* "to think")
- **-ām / -äm** — place/arena of the action (*pēlā* → *pēlām* "field")
- **-tū / -ty** — privative, "lacking X" (*klȫtô* → *klȫtôtū* "gutless")

## STEP 5 — Submit in this format

A table: **Headword | PoS | Stratum | Register (if any) | Gloss | Example sentence |
Translation**, followed by **collision notes** — for each word, what you checked it
against and why it's clear, which suffix/pattern it uses, and any gaps you're flagging.
Aim for 25–40 words per batch, one domain. State your late/loan ratio and justify it.

The Rector will review, rule (logged in the charter), merge into the coursebook, and
regenerate `data/`. Expect reshapes for collisions, register fixes, and gap-fills — that
is the process working, not criticism.

---

### Quick reference — numbers (v3.8+, in case your domain needs them)

Base-12, Slavic digits: **nolô** 0 · **jedôn** 1 · **dva** 2 · **tri** 3 · **xtiri** 4 ·
**peñç** 5 · **xeç** 6 · **sedôm** 7 · **osôm** 8 · **deveñç** 9 · **deseñç** 10 · **elva** 11 ·
**düna** 12. Teens 13–23 are fused single words (*dünjôn* 13…). Above: juxtaposition,
largest-first, no *ja*, no hyphen (*dva düna tri* = 27). Breakpoints: *düna* 12, *grosô* 144,
*mīrô* 1728. Fractions from the trade quarry: *half*, *dēl*, *number+dēl* (*tri-dēl* "third").
The old Finnic (üks…) and Germanic (ēn…) numerals are **extinct canon** — inland dialect only.
