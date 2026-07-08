# Nelôxi — Change Brief for Contributors
### Numbers, fractions, letter-names (canon v3.3 → v3.7)

Hand this to any agent working from an older charter. It summarizes what changed;
the authoritative source remains `coursebook/nelo-kel-coursebook.md` and
`college/kels-kolegi-charter.md` (§36–§39). **Before batching, pull the current
`data/headwords.txt` — do not work from memory or a pasted list.**

---

## 1. The Finnic numerals are GONE. Do not use them.

**Withdrawn from canon** (rulings §37): *üks, kaks, kolm, nēļa, vīç, kūç, seis,
kōtôks, īdôks, kīm*, teens in *-teis*, tens in *-kīm*, *çent*, *mīl*, ordinals
*esmī / tôin*, and the *-nd* ordinal rule. If you use any of these, the batch is wrong.

(The word **üksū** "loneliness" survives — it is built on the *concept* of oneness,
not the numeral. It is not a number.)

## 2. Numbers are now Germanic, base-10

| # | word | # | word |
|---|---|---|---|
| 1 | **ēn** | 6 | **ses** |
| 2 | **twē** | 7 | **seven** |
| 3 | **drē** | 8 | **acht** |
| 4 | **fēr** | 9 | **nēgôn** |
| 5 | **fīf** | 10 | **tēn** |

- **Teens** add **-tein**: *ēntein* 11, *twētein* 12 … *nēgôntein* 19
- **Tens** add **-tig**: *twētig* 20, *drētig* 30, *fērtig* 40, *fīftig* 50, *sestig* 60,
  *seventig* 70, *achttig* 80, *nēgôntig* 90
- **Compounds** hyphenate tens-unit: *twētig-ēn* 21, *fīftig-ses* 56
- **hunt** 100, **dūsônd** 1000: *twē hunt fīftig* 250, *ēn dūsônd nēgôn hunt* 1900
- **Ordinals** add **-tô**: *ēntô* first, *twētô* second, *drētô* third, *tēntô* tenth

## 3. The long hundred (Hanseatic trade tally)

Bulk goods count in dozens, not tens — 120 divides cleanly, which is the point.

- **dūtô** = a dozen (12)
- **xok** = a schock (60 = five dozen)
- **langhunt** = a long hundred (120 = ten dozen)
- plain **hunt** (100) remains for ordinary counting

Count **largest grouping first, remainder in units, joined by *ja***:
*drē dūtô* 36 · *twē langhunt ja tēn* 250.

Use for money, weight, cargo, market tally: *Kalāji vendai drē dūtô kalād* "the
fisher sold three dozen fish (36)." *Xip kannā twē langhunt tônn* "the ship carries
two long-hundred tons (240)."

## 4. Fractions & shares (Low German trade quarry — NOT Finnic)

- **half** — half
- **dēl** — part, share (a merchant's cut)
- Fractions = **number + dēl**: **drēdēl** third, **fērdēl** quarter, **tēndēl** tenth
- **Trade rule:** in a tally, name the sub-unit, don't say the fraction — half a
  *langhunt* is a **xok** (60); a tenth is a **dūtô** (12). Fractions are for general
  (non-tally) use.
- **Partitive** uses the existing linking case *-s* ("of"): *langhuntôs half* "half of
  a long-hundred," *rās drēdēl* "a third of the money," *pas dēl* "a share of the bread"

Do **not** re-coin fraction words from Finnic roots. (*osô* was tried and withdrawn, §39.)

## 5. Letter-names & acronyms (§36)

- Consonants take **-ē**: *bē, dē, fē, gē, hē, jē, kē, lē, mē, nē, pē, rē, sē, tē, vē*;
  special letters by sound + -ē: *çē* [tsē], *xē* [ʃē]
- Vowels are named as themselves (*a, e, i, o, u, ä, ö, y, ô*); a long vowel is
  *pikk* + the vowel (*pikk ā*)
- Acronyms spoken as letter-names, written as the run when lexicalized:
  **tēvē** "TV" (*Mä nǟgô tēvēn*) — the fully-eroded end of *taikfinest → taikô → taiki → tēvē*

---

## What did NOT change

- All grammar (5+ cases, vowel harmony, participles, the derivational suffixes
  -ji/-ôr/-mus/-ū/-stā/-ldā/-ām/-in/-tū, negation, questions) is unchanged.
- The four loan quarries (Finnic core, Low German, Scandinavian, Slavic) are unchanged.
- Nelôxi still has Finnic *grammar* — it simply no longer *counts* in Finnic.

**Current canon: v3.7, 845 headwords.** Regenerate `data/` with
`tools/regen_data.py` && `tools/regen_reverse.py` after any merge; the coursebook is
the single source of truth.
