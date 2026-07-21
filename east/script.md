# The East Fork — the Script Decision

*The brief put the choice squarely: Circassian is really written in Cyrillic, so the East
fork either goes full Cyrillic (echoing the Uusatôm overlay and matching real Circassian
practice) or builds a purpose-built Latin romanization. The ruling below takes both horns
deliberately — and it costs zero new graphemes.*

---

## §1 · The ruling

1. **The archive and standard script of the East fork is Latin — the Metropolitan
   orthography, unextended.** The "purpose-built romanization" the brief asked for turns out
   to already exist: the shared orthography carries everything the fork needs (§2). The
   business register of a Neloxia-aligned commercial state writes the way the mainland
   ledger writes; that is half the point of the fork's existence.
2. **Full Cyrillic is licensed as the fork's second script, by wholesale adoption of the
   Uusatôm mapping** (`../dialects/uusatom/uusatom-cyrillic.md`) — not a new table, the
   existing one, unamended. The East fork's cities live inside the same Cyrillic-writing
   Black Sea–Caucasus world as Uusatôm and as real Circassian; a two-script standard
   (Cyrillic locally, Latin in the archive and abroad) is the realistic outcome, and the
   language already owns the machinery. What Dungan proved for Uusatôm holds here
   unchanged: Cyrillic can carry the whole phonology, so there is no mixing.

## §2 · Why zero new graphemes — the audit

Every sound the fork's three contact layers bring in lands on existing letters:

| Need | Solution | Already sanctioned by |
|---|---|---|
| Circassian-led grammar morphemes (*-r, -m, -p, me-, se-, sin-, tôl-*) | plain letters — the affix material is Nelôxi (`grammar-circassian.md` §4) | coursebook inventory |
| Turkic ç [tʃ] | **tx** (t + x [ʃ]), compositional | §47 (*x* = [ʃ]) |
| Turkic ş [ʃ] | **x** | §47 friction rule |
| Turkic c [dʒ] | **dž** | the *džezô/dīdžē* scar |
| Turkic ı [ɯ] | **ô** [ɤ] | the signature letter itself |
| Turkic ö, ü, long vowels; Persian ā | **ö, ü, macrons** | coursebook inventory |
| Seat-name fricative (Adyghe *хасэ*) | **x** (*Xasā*) | §47 (*kh → x*) |

Nothing enters the scar inventory; nothing touches the Common Register's orthographic
agreement; no East-fork form can even *approach* the retired set (*õ ê î û â š č*), which
stays retired in this namespace (`noun-cases.md` §5.3).

On the Cyrillic side the same audit holds: the Uusatôm table is closed and sufficient. The
digraph *tx* transliterates compositionally (*t → т, x → ш*: *txai → тшаі*) — deliberately
**not** Cyrillic ч, which the Uusatôm inventory does not contain and this standard does not
add. One grapheme per sound, no additions, both directions.

## §3 · The lint gate

The gate (`tools/regen_data.py`) reads only Metropolitan canon and is untouched in
substance; its namespace note now names `east/` alongside the other peer standards, recording
that the East fork sanctions **no additional graphemes at all** — the one peer standard with
an empty scar column. Concretely:

- **Nothing to add to any inventory.** No new letters Latin or Cyrillic; the gate has
  nothing new to permit and nothing new to catch.
- **The retired set binds here too.** An *õ/š/č*-bearing form in an East-fork file is drift,
  same as anywhere (the country-name candidate *Šaraya* is lore, a name under consideration
  in English text — if the founder chooses it, its Nelôxi form normalizes like every proper
  noun, *Xarajā*-shaped, before it enters any lexicon file).
- **The fork's real drift risks are not graphemic** and are enforced by Xasā review, not the
  gate: Caucasian roots leaking into core slots (`east.md`, the one rule) and Estonian
  citation-shapes leaking into coinage (`noun-cases.md` §5) — the same review-beats-gate
  division of labor the charter already records for every branch.

## §4 · Worked sample, both scripts

> **Latin:** Kalāji-r kalā bazarôle tôl-vendāi. Rā mult m-um-p — agā merjagô jôvā um.
> **Cyrillic:** Кала̄йі-р кала̄ базаръле тъл-венда̄і. Ра̄ мулт м-ум-п — ага̄ мерйагъ йъва̄ ум.
> "The fisher sold the fish off at the bazar. I don't have much money — but the sea's share
> is good."

*(The mapping is the Uusatôm table applied mechanically: ô → ъ, j → й, ā → а̄. The Latin page
remains the etymological record and the archive form, exactly as ruled for Uusatôm.)*
