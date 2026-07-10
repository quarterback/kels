# Nelôxi — Rector Handoff / Succession Doc

You are taking over as **Rector** of the Kēļs Kolēgi (College of Language), steward of the
constructed language **Nelôxi** (*nelô kēļ*, said *nel-OX-ee* — x=[ks] in the name, §47). A
previous session held this role; you pick up cleanly from the current state and do not need its
conversation history. Everything that matters is in the repository.

**Current state: v5.33, 1,533 headwords, ruling log through §100.**

---

## What this project is

A multi-agent conlang. The **founder** (the human) sets all direction and rules. **Delegate
agents** propose vocabulary batches and short texts; you, the **Rector**, review each against
canon, rule on gaps, nativize anything source-shaped, merge accepted material into the
coursebook, regenerate derived files, log the ruling, and commit. You implement the founder's
decisions exactly — you do not substitute your own aesthetic (an early logged mistake, §32/§33).

## The five things you must know

1. **The coursebook is the only source of truth.** `coursebook/nelo-kel-coursebook.md` is canon.
   Everything else — the charter's §7 headword list, `data/*.tsv`, `data/*.txt`,
   `data/reverse-index.md` — is GENERATED from it. After every merge run
   `python3 tools/regen_data.py` then `python3 tools/regen_reverse.py`, then sync the charter's
   §7 header count and word list.

2. **Never write a file from its own just-read contents in one expression.** This has emptied
   the charter twice (recovered from git both times). Read into a variable, modify, write once,
   verify with `wc -l`.

3. **DECIDE, don't defer.** When a batch or translation hits a missing word or a missing
   proper-noun system (months, a unit, an institution), the founder's standing instruction is to
   RULE it then and there — propose forms from the quarries, the founder vetoes what they dislike
   — not to flag-and-move-on. Deferring key nouns defeats the purpose (§74).

4. **The recurring delegate failure is source-language leak** — raw Estonian/Finnish/Polish words
   (esp. Estonian `-ma` infinitives) proposed as headwords or used in examples. It happens in
   nearly every batch and is caught by checking `data/headwords.txt` at HEAD and by
   `college/FUNCTION-WORDS.md` (the high-frequency glue that already exists). Nativize or reject.
   Also watch for **phantom headwords** — words used in coursebook examples but never actually in
   the lexicon (sȫ, markôt were both caught this way); grep the dictionary before trusting a form.

5. **The four quarries each have a home** (this is how loanword-sourcing stays organic, not
   guesswork): **Finnic** = the deep core + the water/heartland; **Low German** = trade,
   seafaring, the counting-house, the calendar; **Scandinavian** = colloquial/street/deck;
   **Slavic** = the Marīsô border, market, familiar-kin; **Romance/Catalan** = the register of
   cultivation — law, learning, documents, sentiment, cuisine, formal speech (§76; Romance had
   been neglected — give it first look for those domains).

## The language in one breath

Finnic grammar (agglutinative cases, vowel harmony, NO verb agreement, pre-verbal negation *äb*,
bare-stem imperative, hortative *-m*) under four-quarry loan contact. **Base-12 (dozenal)
numbers** with Slavic digits (nolô, jedôn, dva, tri…), fused teens (dünjôn 13…), Low German
fractions (half, dēl). Orthography uses **ô** [ɤ] (not õ, retired v4.0). x = [ʃ] normally, [ks]
in proper nouns. **24-hour clock**, Low German calendar (jūli, augôst; mōndag…sôndag). Percent: % still
means per-hundred, but 100 in base-12 is a full gross (144), so half = 60% — formal **pôkrosa**,
slang **krossi**. Two dialects: the metroplex
metrolect (standard) and conservative inland; the Finnic layer belongs to the water, the interior
is Baltic-German/Slavic (§64).

## The repository map

```
coursebook/nelo-kel-coursebook.md   CANON — grammar (Part One) + master dictionary
coursebook/VERB-REFERENCE.md        verb-system digest
grammar/00-INDEX.md + 01–11         FOUNDATION teaching modules, each self-contained:
   01 partitive · 02 verb-derivation · 03 gradation · 04 compounding · 06 declension ·
   07 pronouns · 08 relations · 09 tense&aspect · 10 adjectives · 11 commands
   (05 = contact history, RESERVED for the founder's worldbuilding)
college/kels-kolegi-charter.md      protocol + full ruling log §1–§76 + §7 headword list
college/FUNCTION-WORDS.md           cheat-sheet: high-frequency glue already in canon (anti-leak)
college/CREOLE-PRINCIPLE.md         THE standing vocabulary doctrine (§79): borrow first, five co-primary quarries
college/ASSIGNMENTS.md              domain-claim ledger
college/COORDINATION.md             multi-agent scheme (genre ladder + domain ledger + daily-life lane)
college/DELEGATE-BRIEF.md           brief for vocabulary agents
college/CORPUS-BRIEF.md             brief for text agents
college/DAILY-LIFE-BRIEF.md         brief for the standing connective-glue agent
world/geography.md, boundaries.md, gazetteer.md, toponymy.md
                                    the settled world: 7-region map, 30 cities, naming system
bundles/BUNDLE-domain-agent.md      SELF-CONTAINED bundle: hand to a word-coining agent
bundles/BUNDLE-corpus-agent.md      SELF-CONTAINED bundle: hand to a text-writing agent
bundles/BUNDLE-grammar-reference.md SELF-CONTAINED bundle: full grammar; also re-grounds a drifting agent
data/*                              GENERATED — never hand-edit
tools/regen_data.py, regen_reverse.py   the regenerators
reader/                             finished corpus texts (recipe, dialogue, showcase)
index.html, assets/                 the website (github.com/quarterback/kels) — fetches repo md live
```

## How to delegate (the bundles)

Hand an agent ONE self-contained bundle matching its task — never the repo, never the charter:
- coining vocabulary → `bundles/BUNDLE-domain-agent.md`
- writing a text → `bundles/BUNDLE-corpus-agent.md`
- grammar work, OR re-grounding an agent that has started drifting into Estonian →
  `bundles/BUNDLE-grammar-reference.md`

Bundles embed a headword snapshot, so **regenerate them after canon changes** (the build step
concatenates the briefs + FUNCTION-WORDS + relevant grammar modules + current headword list).
Cold agents on a bundle also serve as a TEST INSTRUMENT — if one flags a rule as "missing" that
actually exists, the bundle/module docs are incomplete there (this is how the imperative gap and
the sȫ/markôt phantoms were found).

## The merge cycle (each batch)

1. Check the delegate worked from HEAD `data/headwords.txt` (stale batch = #1 failure).
2. Verify vs the headword list — no duplicates, no phantom-canon, no source-language leaks.
3. Rule on gaps; **decide missing proper-noun systems now**; nativize source-shaped proposals;
   fill approved lexical gaps; reject undeclared suffixes.
4. Merge into the coursebook (correct dictionary letter-section, keep sorted; protect the
   `famīl·la` interpunct so it doesn't split on `·`).
5. `regen_data.py` && `regen_reverse.py`; sync charter §7 count + word list.
6. Log the ruling as the next §-number.
7. Commit. Regenerate bundles if the change is material.
8. Return a short rulings doc + next assignment to that agent.

## Standing founder principles (do not relitigate)

- Loan generosity: modern/urban/colloquial domains borrow FREELY; hacker-type tech terms are
  loans, not coinages (§27/§33).
- Doublets draw from a DIFFERENT quarry than the native word, never a second Finnic form (§52).
- Place-names keep foreign scars; fix only characters in no language (î/û/â → ô/macrons) (§63).
- The Finnic layer belongs to the water; do not Finnicise the interior (§64).
- Names are composed from culture-specific toponymic elements, not defaulted to Finnic (§73).
- Romance is the cultivation register; give it first look for law/learning/sentiment/cuisine (§76).

## Document discipline

State what things are, plainly. No process narration, apologies, or records of your own mistakes
inside repository documents — the founder and other agents read them. Corrections happen in
conversation; documents carry the settled result. Keep contributor-facing docs self-contained.

## What is open (by design)

- **History & politics** of Nelôxia — founder-controlled, deliberately not canonized.
- **Module 05, the contact history** — reserved for when the founder's worldbuilding lands.
- **Translation as a delegation type** — being practiced now; a translation bundle will follow.
