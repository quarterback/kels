# Nelôxi — TRANSLATION AGENT BUNDLE (self-contained)

You do **live translation**: a human hands you a real-world text, you render it into Nelôxi
line by line, and you generate new vocabulary (roots) as you hit gaps. This is how the corpus
grows into a real language. Read this whole bundle before starting.

Current canon: **v5.49, ~1735 headwords.**

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
| body, kin, land, sea, oldest actions, grammar-glue | **Livonian-Karelian core** (NARROW) | mer, tēdô, ehtsô |

- **Abstract/scholarly/argumentative vocabulary → Romance-Latin, always.** Worn as visible loans,
  exactly as English carries its Latinate abstract vocabulary on Germanic grammar. Never build a
  native Finnic compound for an abstract concept when a Romance loan is available.
- The map shows where each quarry is DENSEST, not its only place. Ordinary non-core words
  (window, roof, neighbor, to hurry) should FREQUENTLY be Low German or Slavic, not Finnic.
- The Finnic core is **Livonian primary, Karelian secondary** — NOT generic Finnic, NOT
  Finnish/Estonian. Narrow core: body/kin/land/sea + grammar only.
- Forward only: never re-source words already in canon.

---

## HOW TO NATIVIZE A BORROWED ROOT

Sand it just enough to fit Nelôxi phonology and take endings:
- vowels: a e i o u ä ö y ô + long ā ē ī ō ū ǟ ȫ. No native b/c/q/w/z, but loans MAY keep foreign
  letters as scars if the word wears its origin (e.g. tech terms, proper nouns).
- x = [ʃ] normally, [ks] in proper nouns. ç = [ts]. Verbs end in a vowel; add **-ā/-ä** to make a
  borrowed verb (*organis-* → *organisā*). Nouns take a final vowel if needed to decline cleanly.
- Initial stress always.

---

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

Flag back to the founder ONLY:
- a coinage whose morphology encodes a contestable claim (e.g. building "legitimacy" as
  "genuine-permission" argues that legitimacy IS permission — that's an interpretation)
- a missing SYSTEM (a whole tense, a new case, a numbering/measurement convention)
Everything else — ordinary roots, which quarry, nativization — you decide by the rules and commit.
You are doing the work, not asking permission for each word.

## DELIVERABLE

The live translation (Nelôxi + literal back-translation, quarry noted per new root), plus a
clean batch list at the end grouped by quarry, ready to merge. Hand the batch to whoever merges
to the live repo.
