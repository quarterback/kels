# Nelôxi — TRANSLATION AGENT BUNDLE (self-contained)

You do **live translation**: a human hands you a real-world text, you render it into Nelôxi
line by line, and you generate new vocabulary (roots) as you hit gaps. This is how the corpus
grows into a real language. Read this whole bundle before starting.

Current canon: **v5.75, ~2002 headwords.**

---

## STEP 0 — PULL LIVE CANON FIRST (mandatory, anti-drift)

Before translating anything, get the current language from the live repository:
**https://github.com/quarterback/kels**

Pull at minimum:
- `data/headwords.txt` — the complete current word list (check every word against this)
- `coursebook/nelo-kel-coursebook.md` — grammar + full dictionary (the source of truth)
- `college/CREOLE-PRINCIPLE.md` — the vocabulary doctrine (governs every root you make)
- the `grammar/` modules — how derivation and declension work

Do this **at the start of every session.** The #1 failure mode of translation agents is working
from memory or a stale snapshot and drifting — especially defaulting to Estonian. Working against
live canon is the cure. If you cannot access GitHub, say so and stop; do not translate blind.

---

## THE MOST IMPORTANT RULE: you invent ROOTS, not words

Real languages have two layers, and only one of them takes judgment:

1. **Roots** — irreducible cores (*tēdô* "know", *mer* "sea", *legitīm* "legitimate"). These
   either come from the Finnic core or are BORROWED from a quarry. **This is the only creative
   decision you make.** Every gap you hit is a root decision: which bucket does it come from?

2. **Derivation & inflection** — everything else falls out of the rules automatically, no
   invention:
   - agent noun: **-ji** or **-ôr** (*tēdô* → *tēdôr* "expert")
   - result noun: **-mus/-mys** (*solvā* → *solvômus* "solution")
   - noun→verb: **-stā / -ldā**; verb→verb chains: causative **-tā**, frequentative **-ilā**,
     momentane **-ahtā**, reflexive **-u** (see grammar module 02)
   - declension: every case form is fixed by the table (grammar module 06) — never "invent" a
     declined form, look up the pattern
   - compounding: head-final, only the head inflects (module 04)

**So your job is: decide roots by the doctrine below, then let the rules generate the rest.**
Do not agonize over derived forms or declensions — those are mechanical. Do not invent a
declension. Focus your judgment entirely on where each new ROOT comes from.

---

## THE CREOLE DOCTRINE (how to source every root)

Nelôxi is a **polyglot maritime creole**: Livonian-Karelian Baltic-Finnic GRAMMAR carrying a
FIVE-WAY loan VOCABULARY. It must stay dirty. Do NOT default to Finnic — that is the constant
drift, and it makes the language read as "just Finnish/Estonian."

**When you hit a gap, ask which of the five quarries would have owned that word, then borrow it
and add a Nelôxi ending. Borrowing is the DEFAULT, not the fallback.** This is the Finnish move:
*pankki, posti, presidentti* — take the word, add an ending, done. Why invent when borrowing
will do?

The five quarries are **co-primary** (the territory is demographically mostly non-Finnic, so the
loan quarries do broad everyday work, not niches):

| The gap is about… | Reach for… | Example |
|---|---|---|
| trade, tools, ledgers, shipping, bureaucracy, + ordinary port/city life | **Low German** | rabat, laadā |
| market, food, frontier, + interior domestic/social/emotional life | **Slavic** | gribô, pirôg |
| rough/casual/colloquial, the street, everyday informal speech | **Scandinavian** | snē, vanlü, līkgōd |
| **law, learning, documents, abstract & scholarly, sentiment, cuisine, formal register** | **Romance/Latin** | legitīm, struktūr, psükolōg |
| body, kin, **the land**, oldest actions, grammar-glue | **Livonian-Karelian core** (NARROW) | mer, tēdô, ehtsô |
| **the DECK — fish, coast, seamanship** (maritime = whoever crewed the boats: LG traders, Scand deckhands, Saharan mariners) | **Low German / Scandinavian / Saharan back-flow**, NOT Finnic | hering, lax, xūt, klippô (§142) |

- **Technical / institutional / scholarly vocabulary that genuinely ARRIVED from outside → borrow**
  (Romance-Latin for law/learning/documents; international for tech/sport; Low German for the wharf).
  Worn as visible loans. ⚠️ **BUT this no longer applies to *lived* abstractions — see the TEXTURE
  DOCTRINE below, which is the single most important update to this bundle.**
- The map shows where each quarry is DENSEST, not its only place. Ordinary non-core words
  (window, roof, neighbor, to hurry) should FREQUENTLY be Low German or Slavic, not Finnic.
- The Finnic core is **Livonian primary, Karelian secondary** — NOT generic Finnic, NOT
  Finnish/Estonian. Narrow core: body/kin/**land** + grammar only. **The SEA is NOT hearth
  vocabulary — it is DECK vocabulary** (§142): fish, coast, and seamanship come from the mixed
  crews (Low German, Scandinavian, Saharan), never Finnicised. Only *inland freshwater* fish
  (haug, ahvôn, särg) and the *dry land* are native.
- Forward only: never re-source words already in canon.
- **The nursery stratum is quarry-independent (§144).** Baby-talk words — *mama, papa* and the wider
  babble family (*baba, tata, nana, dada*) — are NOT a quarry decision. Baby-mouth mechanics make every
  people on this mixed coast babble the same open-vowel + labial/nasal, so the intimate address words are
  shared identically across all five quarries — the one universal layer. A nursery/hypocoristic gap is
  answered by the reduplicated babble form, not by borrowing. The *formal* kin words (**mǟr** mother,
  **pǟr** father) stay Finnic-core; the babble forms (**mama, papa**) belong to no one and everyone, and
  underlie the formal word ("daddy" older than "dad").

---

## HOW TO NATIVIZE A BORROWED ROOT

Sand it just enough to fit Nelôxi phonology and take endings:
- vowels: a e i o u ä ö y ô + long ā ē ī ō ū ǟ ȫ. No native b/c/q/w/z, but loans MAY keep foreign
  letters as scars if the word wears its origin (e.g. tech terms, proper nouns).
- x = [ʃ] normally, [ks] in proper nouns. ç = [ts]. Verbs end in a vowel; add **-ā/-ä** to make a
  borrowed verb (*organis-* → *organisā*). Nouns take a final vowel if needed to decline cleanly.
- Initial stress always.

---

## ⭐ THE TEXTURE DOCTRINE (§122–§128) — READ THIS; it overrides "borrow for abstractions"

Borrowing is right for **concrete things and genuinely imported institutions**. It is *wrong* for
concepts the culture already **lives** — emotions, virtues, kinship, fate, freedom. Coining those as
loan+`-ô` (*dignitā*, *egāl*) makes a cipher, not a language. Read `college/METAPHOR-FIELDS.md` in full.

**The test for every gap: *would a fisher-trader on this cold trading coast reach for a foreign word,
or did this concept genuinely arrive from outside?*** If they'd already have it, BUILD it from native
material — the sea, the salt & scale, the black-book, the net, the hearth, the parish, the pitch —
by compound or extension, and write the gloss as *an image with a stance*, not a dictionary equivalent.

- ✅ fate → **merjagô** "the share the sea deals you" (not Latin *fatum*)
- ✅ dignity → **nimpundô** "the weight a name carries" · conscience → **isülivrô** "the inner black-book"
- ✅ equal → **ühüvāgô** "of one weight on the scale" · brotherhood → **ühüvôrk** "one net"
- ✅ flounder → **pakalā** "loaf-fish" · hovel → **hīrlôukkōt** "a house full of mousetraps"
- ❌ **do not default to `-ô`.** An `-ô` ending on a lived concept is the tell you got lazy. Compound.

**Kinship is not possession, and not gendered (§127).** Never render "his wife / her husband / their
children." Name people and bond them — *ja* "and", apposition, comitative `-k` — never a possessive,
never a gendered kin-word. *"Sergei, his wife Misha, and their kids"* → *Sergei ja ühüfôk Misha, ja
läpxôd…*. Use **ühüfôk** "spouse" (shared-hearth), **läpx** "child" (genderless). Possessives are fine
for *things* (*täs līnô* "his line"), never for people.

**Idioms & formulas (§124).** When a concept wants a *scene*, give it one and register it in
`reader/idioms.md` with its edge (freedom = *säs eläji kōrrô karrēl…* "your animals in the street
eating ham"). A recurring refrain in a tale is a **formula** — fix it and register it.

**The lint gate flags, it does not veto (§126).** `tools/regen_data.py` blocks retired graphemes
(`õêîûâšč` in stems) and Estonian citations — real drift. But the native `-õ` *ending* is legal
(*kaunõ, rôimõ*), and a grammatically sound form the founder wants stands. The gate is a guardrail,
not a court.

## THE TRANSLATION METHOD (do this live, line by line)

1. Take one sentence. Render it into Nelôxi using words that already exist (check headwords.txt).
2. Every gap = a root decision. Source it by quarry (doctrine above), nativize, use it.
   **DECIDE it now — do not defer, do not flag-and-skip.** Propose and commit the root.
3. Show your work: give the Nelôxi line, a literal back-translation, and note the source quarry
   for each new root (e.g. "*legitīm* — Romance").
4. Never reach for the source language of the text. If you're translating English and hit
   "legitimate," you do NOT write an English or Estonian word — you borrow from the correct
   quarry (here Romance) and nativize.
5. **Phantom check:** before using any word as if it exists, confirm it's actually in
   headwords.txt. Words used in examples but never canonized (past cases: sȫ, markôt) are bugs —
   don't trust memory, grep the list.
6. Keep a running batch of every new root with its gloss and source quarry.

## WHAT NEEDS THE HUMAN (a thin slice — everything else you just decide)

You decide: ordinary concrete/institutional roots (which quarry, nativization), all derivation and
inflection, idiom construction, the kinship phrasing. **Flag to the founder ONLY:**
- **Culturally-loaded lived concepts** where the *image itself is a design choice* — happy, freedom,
  fate, honor, love, grief, a curse, a blessing. The founder often wants to *carve the sense* (happy =
  glee/celebration/pride; freedom = animals loose in the street). Propose your best image, but mark it
  ⟨founder-image⟩ so it can be reshaped. This is where the language's soul is set.
- A coinage whose morphology encodes a contestable claim (e.g. "legitimacy" as "genuine-permission").
- A missing **SYSTEM** (a whole tense, a new case, a measurement convention).

Everything else you decide by the rules and commit. You are doing the work, not asking per word.

## THE MERGE PIPELINE (how a finding becomes canon — run it yourself)

A gap-list isn't enough; land the words. In order:
1. **Add each headword** to the right per-letter line in `coursebook/nelo-kel-coursebook.md`
   (format: `hw gloss (source/etymology)` joined by ` · `). Gloss lived concepts as *images*.
2. `python3 tools/regen_data.py` — regenerates `data/{dictionary.tsv,headwords.txt}` and runs the
   **lint gate**. Fix real drift; the `-õ` ending is exempt.
3. `python3 tools/regen_reverse.py` — rebuilds the English→Nelôxi index.
4. **Charter** `college/kels-kolegi-charter.md`: bump the §7 header (`vX — N entries`), regenerate the
   §7 headword line from `data/headwords.txt`, and append a **ruling §NNN** describing the batch.
5. `python3 tools/build_bundles.py` — validates count == charter, stamps `data/version.json` + all
   bundles/briefs. It **fails loudly** if anything is inconsistent — that's your proof of a clean merge.
6. Register any new reader text in `assets/app.js` (ROUTES; run `node --check assets/app.js`).
7. Commit + push. Minor-version bump when headwords change; ruling number always advances.

## DELIVERABLE

1. **The translation** as a `reader/*.md` file — Nelôxi + line-by-line English, register-exempt names.
2. **New words merged** through the pipeline above (not just listed) — each an image or a justified loan.
3. **A gap-list** of what's still missing (⟨word gap⟩ / ⟨grammar gap⟩ / ⟨founder-image⟩) — the seam for
   the next agent.
4. **Idioms/formulas** registered in `reader/idioms.md`.

Pick your next text from `college/TEXT-WORKLIST.md` — claim it, translate it, land the words, mark it done.
