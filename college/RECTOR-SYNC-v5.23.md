# Rector Sync — canon state and rulings through §90 (v5.23)

*From the merge-and-review Rector to the batch Rector. Read fully before producing or merging
anything. This supersedes any snapshot you are holding.*

## 1. The authoritative state

**Canon is v5.23, 1213 headwords, ruling log through §90**, on the branch
`claude/new-session-cnscqk` of github.com/quarterback/kels. `main` is STALE (pre-§79) until the
open PR merges — pull canon from the branch, not from main and not from memory. `data/version.json`
always states the version, headword count, and last ruling of whatever checkout you are reading;
check it first.

## 2. The ruling-number map (your numbers moved)

Your batches were merged and renumbered around rulings you did not have. Cite these numbers from
now on, and before self-assigning a §-number, always read the last `## N.` in the charter at HEAD:

| You called it | Canon § | Content |
|---|---|---|
| §79 | **§79** | The Creole Principle (unchanged) |
| — | **§80–§82** | numbers audit · percent semantics · eventive addendum (merge-Rector rulings you lacked) |
| §83 | **§83** | Cat Hicks batch |
| — | **§84** | post-merge corrections to §83 |
| §84 | **§85** | Yle weather/farming batch |
| §85 | **§86** | Yle IOC/politics batch |
| §86 | **§87** | exonym system + defence/finance batch |
| §87 | **§88** | exonyms made tiered (founder correction) |
| — | **§89** | post-merge corrections to §85–§87 |
| — | **§90** | the complete nation list, settled, with overrules |

**Next free ruling number: §91.**

## 3. Corrections applied to your merges, and why (§84, §89)

These are settled canon. Do not re-propose the removed forms; use the reshaped ones.

**Removed — duplicate of a word already in canon** (cause: batch not checked against HEAD
`data/headwords.txt`; this is STEP 0 of the delegate brief):
kuivô (=kuiv) · jôgô (=jôg) · järv (=jǟrv) · marjô (=mārjā) · sesōn (=sesôn) · visô (=vīzô) ·
pehmü (=pehmē) · võtā (=votā, twice) · kōpô (=inkôp — the same Low German *inkōp* proposed twice
in one batch) · mõjutā (Estonian *mõjutama* leak; the same batch already supplied virkā "to
affect") · viljôlusô (undeclared -lusô suffix; the same batch already supplied kultivômus).

**Reshaped — orthography and morphology rules:**
- teoríä → **teorī** — í is not in the vowel inventory; the batch's own anomalī/psükolōgī set the shape.
- mašīn → **maxīn** — [ʃ] is written **x**, never š.
- kogõ → **kogē** — "to experience" sat one letter from the function word kôgõ "everything"
  (the äb/ǟbū collision class, charter §5c).
- sōl → **suô** — "marsh" sat one letter from BOTH sōla "salt" and sol "sun".
- tagasi → **tagān** — raw Estonian function word (the §23 auto-return class); Livonian *tagān*.
- harvôstā → **viljôstā** — parsed as harvõ "rarely" + -stā ("engage in rarity"); the declared
  -stā denominative on viljô follows the kalāstā "to fish" pattern.
- klimô-muutôs → **klimô-muutômus** — the result-noun suffix is -mus (from muutô); -s is not a
  Nelôxi nominalizer.

**Ruled doublets (kept, with cf-notes in the dictionary):** riig ↔ rīgô (riig is load-bearing in
the founder's calque Ühüriigôd) · mäng ↔ pēlô · andā ↔ donā · kaunõ ↔ bel. Cross-quarry or
register doublets are fine (the pôlū/gribô pattern); silent same-meaning re-coinages are not.

**Phantom-canon warning renewed:** your §86 notes claimed *korsô* "race" "already existed from
early canon." No such headword has ever existed. Never cite canon you have not verified in
`data/headwords.txt` (charter §32).

## 4. The exonym decision (§90) — settled, with reasons

The founder's complete nation list is canon in `world/exonyms.md`. It is FINAL — do not
re-derive, extend it only via the tier rule when a new country actually comes up.

Overrules applied to the draft, and the standing rules they came from:
- **Length is a macron, never a doubled vowel.** Leetô→Lētô, Gruusiô→Grūsiô,
  Austraaliô→Austrāliô, Aasiô→Āsiô, Indoneesiô→Indonēsiô. Double vowels are Estonian
  orthography leaking in.
- **Pôhôlô-mōd → Pôjā-mōd.** Canon deliberately split the Estonian *põhja* homonymy: pôjā is
  north, pôhô is bottom/base. Check the actual canon root, not the Estonian one.
- **Sūd-Afrikô → Sud-Afrikô.** Canon already had sud "south" — the compass is complete and
  already creole (pôjā/idā/lǟn Finnic, sud Low German). Check HEAD before coining.
- **kuning "king" canonized** (+1 headword) to carry Ühükuningôd "United Kingdom".

**Quarry-balance question, decided:** the list stays as-is. Tier-1 names look Finnic because deep
names are the oldest layer and the oldest layer IS the Finnic substrate — that is stratigraphy,
not purebred drift, and it is how real languages behave (Finnish Venäjä/Ruotsi/Saksa are ancient;
Espanja is a plain loan). The other families already have their shine: kuning is itself a
Proto-Germanic loan into Finnic; sud and Legmō are Low German; Polskô/Belôrus/Ukrainô are Slavic
self-names; Danô/Nôrô/Grekô came via the Scandinavian and merchant sea-runs; Txekô uses the
Catalan-style tx digraph. Route-name variants (Frankrīk, Ingland) were considered and NOT
adopted — optional future flavor only if the founder asks. The -ô endings are phonology, not
Finnic sourcing.

## 5. Recurring failure checklist (run this before submitting any future batch)

1. Pull `data/headwords.txt` from the branch HEAD and check EVERY candidate — exact match and
   near-collision (§5). Eight of your last ~110 words duplicated existing canon exactly.
2. Within the batch, one concept one word — you proposed the same meaning twice in one batch
   three times (inkôp/kōpô, mõjutā/virkā, sadô/urôžai; sadô and urôžai survived on split glosses).
3. No doubled vowels; length is a macron. No š — [ʃ] is x. No í. No raw Estonian function words.
4. Derive only with declared suffixes (-ji, -ôr, -in, -mus/-mys, -ū, -stā, -ldā, -ām, -tū;
   causative -tā). One attestation is not a suffix.
5. Never cite canon you have not verified. Never use a word in an example that is neither canon
   nor in your batch.
6. Read the charter's last ruling number at HEAD before numbering your own report.

Everything above is logged in full in the charter (§84, §89, §90). Current canon files, the
creole doctrine, and the exonym list are the only sources of truth. Sync your snapshot before
the next run.
