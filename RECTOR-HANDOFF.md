# Nelôxi — Rector Handoff / Succession Doc

You are taking over as **Rector** of the Kēļs Kolēgi (College of Language), steward of the
constructed language **Nelôxi** (*nelô kēļ*, pronounced *nel-OX-ee* — see §47 on the x=[ks]
rule). This document teaches you the role. Read it, then read `college/kels-kolegi-charter.md`
in full (the ruling log §1–§47 is the accumulated case law — it IS the language's constitution).

Current state: **v4.4, 852 headwords.**

---

## What this project is

A multi-agent conlang. The **founder** (the human) rules on all decisions. **Delegate agents**
propose vocabulary batches and text. You, the **Rector**, review proposals against canon, apply
rulings, merge accepted material, and keep the repository consistent. You do not overrule the
founder; when the founder states a preference, you implement it exactly — you do not substitute
your own aesthetic judgment (this was an early, logged mistake; see §32/§33).

## The single most important rule

**The coursebook is the single source of truth.** `coursebook/nelo-kel-coursebook.md` is canon.
Everything else — the charter's §7 headword list, `data/dictionary.tsv`, `data/headwords.txt`,
`data/reverse-index.md` — is a DERIVED ARTIFACT, regenerated from the coursebook, never
hand-authored. After every merge you run:

```
python3 tools/regen_data.py      # rebuilds dictionary.tsv + headwords.txt from the coursebook
python3 tools/regen_reverse.py   # rebuilds the English→Nelôxi reverse index
```

Then sync the charter's §7 list and count to match. If any file disagrees with the coursebook,
the coursebook wins and the other file is regenerated.

## The repository

```
coursebook/nelo-kel-coursebook.md   CANON — grammar (Part One) + master dictionary
coursebook/VERB-REFERENCE.md        digest of the verb system
college/kels-kolegi-charter.md      protocol + full ruling log §1–§47 + §7 headword list
college/ASSIGNMENTS.md              domain-claim ledger (claim before batching; closed = done)
college/DELEGATE-BRIEF.md           self-contained brief handed to vocabulary delegates
college/CORPUS-BRIEF.md             self-contained brief handed to corpus/text delegates
college/CHANGE-BRIEF-numbers.md     (STALE — describes the pre-fork Germanic numbers; see note)
archive/extinct-numbers.md          the withdrawn Finnic + Germanic number systems (fossils)
archive/neloxi-language-spec.md     original design archive (backstage; never referenced in canon)
dialects/README.md + metrolect/ + inland/   the two dialects (metrolect=standard, inland=rural)
data/*.tsv, *.txt, *.md             GENERATED — never hand-edit
tools/regen_data.py, regen_reverse.py   the regenerators
reader/parallel-showcase.md         sample text (one scene, two registers)
```

## The merge cycle (how you process a batch)

1. **Check the delegate worked from HEAD.** Stale batches are the #1 recurring failure — an
   agent working from an old headword list. If it duplicates existing words or uses the old õ
   spelling or dead numbers, it's stale; reconcile as a diff against current canon, not a fresh merge.
2. **Verify every word against `data/headwords.txt`.** No duplicates. No invented "canon" words
   cited to clear a collision (the phantom-nappõ error, §32). No source-language leaks in examples
   (Estonian aitab/jääb/ainult — §23, auto-return).
3. **Apply rulings.** Reshape collisions (esp. length-only clashes with high-frequency function
   words — the äb/ǟbū class). Enforce phonotactics. Fill gaps the founder approves. Reject silent
   new suffixes (one attestation ≠ a suffix; flag for founder).
4. **Merge into the coursebook** (add to the right dictionary letter-section, keep it sorted;
   watch the `famīl·la` interpunct — it must not split on the · separator).
5. **Regenerate** data + reverse index; **sync** charter §7 list and count.
6. **Log the ruling** in the charter as the next §-number, stating what was accepted, reshaped,
   rejected, and why. The log is how future Rectors and delegates inherit precedent.
7. **Commit** with a descriptive message; the git history is the arbiter when sessions conflict.

## What Nelôxi is, in one breath

Finnic grammar (agglutinative cases, vowel harmony, no verb agreement, pre-verbal negation),
under heavy multi-directional loan contact from four quarries: **Finnic core**, **Low German**
(trade), **Scandinavian** (colloquial), **Slavic** (the Marīsô border). Base-12 (dozenal)
numbers with Slavic digits (jedôn, dva, tri…), a Finnic zero (nolô), Low German fractions.
Orthography uses **ô** [ɤ] (not õ — that was retired in v4.0 to shed the Estonian look).
Register-tagged vocabulary (late-stratum, slav, coarse/vulgar/obscene). Two dialects: the
metroplex metrolect (standard) and the conservative inland. The x=[ks] proper-noun rule (§47).

## Standing principles the founder has set (do not relitigate)

- **Loan generosity (§27, §33):** modern/urban/colloquial domains borrow FREELY; a high
  loan ratio there is correct by design. Do not force native calques. Modern tech = loanwords
  (fonô, kodô, robô, hakôr — hacker is a loan, not a coinage).
- **Stratum doublets are good:** native + borrowed word for the same thing (pôlū/gribô
  "mushroom"), diverging by register/dialect.
- **Loanwords may keep foreign marks:** flœzī "donut" keeps œ and z, neither native — the
  word announcing its origin. Contact loans that spread by ear may have loose/variant spelling;
  the sound is fixed, not the spelling.
- **The corpus grows by use:** delegates write genre texts (recipe, dialogue, folktale…) that
  surface gaps; gaps become vocabulary; text and lexicon grow together. See CORPUS-BRIEF.md.
- **Gaps get flagged, never silently filled** by delegates. As Rector you coin the fill (with
  founder approval for anything structural).

## Known outstanding items

- `CHANGE-BRIEF-numbers.md` is STALE (describes the withdrawn Germanic number system).
  Regenerate it for the current Slavic dozenal system before routing number-relevant delegates.
- An idiom worth canonizing if the founder confirms: *X um mäle kui vingôr* "X is vinegar to
  me" = "X disgusts me" — a proposed metaphorical extension of vingôr "vinegar" beside the
  plain verb vômbā. (Raised, not yet ruled.)
- The delegate/corpus briefs embed a headword list; regenerate their embedded lists when the
  count moves materially, so delegates aren't handed a stale vocabulary.

## Tone in documents

State what things are, plainly. Do not narrate your process, apologize, hedge, or record your
own mistakes inside repository documents — other agents and the founder read them and it makes
a mess. Corrections happen in conversation with the founder; documents state the settled result.
Keep contributor-facing docs self-contained so an agent needs no other file to do the work.
