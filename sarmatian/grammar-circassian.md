# The Sarmatian Standard — the Circassian-Led Grammar Spec

*The structural standard of the Sarmatian standard: the same Nelôxi words, run through a Caucasian
machine. The Metropolitan baseline this diverges from is the APiCS structural profile
(`../grammar/structural-profile-apics.md`); every divergence below is stated against it.
The noun-case half of the morphology is `noun-cases.md`; this file owns the clause and the
verb. Everything here is legal only under `sarmatian/` — in any other standard, all of it is error.*

**The design in one line:** Circassian supplies the *slots and their order*; Nelôxi supplies
everything that fills them.

---

## §1 · The divergence table

| Feature | Metropolitan | Sarmatian standard (Circassian-led) |
|---|---|---|
| Word order | SVO, fixed | **SOV** — verb-final, fixed |
| Alignment | Nominative–accusative (object takes *-n*) | **Ergative** — transitive agent takes *-r*; object unmarked. The signature difference. |
| Verb | Near-zero inflection, isolating | **Polysynthetic** — subject, object, direction, negation pack into the verb as affixes; the verb is the heavy word |
| Negation | Pre-verbal particle *äb* | **Verb-internal** — suffix *-p* folded into the verb complex; *äb* does not exist here |
| Postpositions | Yes (*kōtôs al*) | **Kept** (Circassian is also postpositional); ground noun in oblique *-m* (*kōtôm al*) |
| Adjective–noun | Adj–N | **Kept** (both languages are Adj–N) |
| Noun cases | Eight cases, harmonized alternants | **Kept but leaning Estonian** — leveled endings, goal *-le*; object *-n* retired (`noun-cases.md`) |
| Tense | Past *-i*, conditional *-ks*, no future | **Kept** — the Metropolitan suffixes ride inside the new verb complex |

## §2 · The clause — SOV and head-finality throughout

The verb stands **last**. Everything else lines up before it, dependents before heads,
consistently — the Sarmatian standard takes the head-final noun phrase Metropolitan already has and
extends the same logic to the whole clause:

- **Agent – object – verb:** *Kalāji-r kalā vendā.* "The fisher sells the fish."
  (Metropolitan: *Kalāji vendā kalān.*)
- **Time and place before the verb:** *Ajēr mä markôtôle me-lǟdi.* "Yesterday I went to the
  market."
- **Postpositions kept**, ground in oblique *-m*: *vana kōtôm al* "under the old house."
- **Adj–N, Num–N, Dem–N, Gen–N kept** exactly as Metropolitan: *vana kōt, tri kalā, se mēs,
  mäs nim.*
- **Complement clause precedes the matrix verb**, and the complementizer *et* goes
  clause-final — the head-final rendering of the same Metropolitan word:
  *[Sä tulī et] me-tēdô.* "I know that you came." (Metropolitan: *Mä tēdô, et sä tulī.*)
- **Relative clauses go prenominal.** The participle strategy Metropolitan already owns
  becomes the primary strategy (*kantāji mēs* "the man who sings"); the postnominal
  *ken/mis* clause recedes to formal-register use.
- **Question words** are not fronted; they sit in the preverbal focus slot:
  *Kus se-lǟdô?* "Where are you going?"
- **The polar particle *ka*** encliticizes to the verb — which, verb-final, puts it
  sentence-final: *Se-tulē-ka?* "Are you coming?"

## §3 · Alignment — the ergative

The Sarmatian standard is **ergative**. Three rules replace Metropolitan's *-n* object case:

1. **The transitive agent takes the ergative, *-r*** (vowel-final stems: *mä-r, kalāji-r*;
   consonant-final stems take the harmony helper: *kōtô-r, mēse-r* — full morphophonology in
   `noun-cases.md`).
2. **The intransitive subject and the direct object are unmarked** (absolutive = bare stem):
   *Mä tulē* "I come" · *Mä-r mer me-nǟgô* "I see the sea."
3. **The object case *-n* is retired.** Its disambiguating work is done by the ergative on
   the agent and by agreement inside the verb; its aspect work (completed vs. ongoing) is
   left to the time-word toolkit the language already has (*jubā, nū*), as futurity always
   was.

> The pair to memorize:
> **Metr.** *Mä nǟgô mern.* → **Sarm.** *Mä-r mer me-nǟgô.* — same three words, the marking
> swapped from the object to the agent, the pronoun echoed inside the verb.

## §4 · The verb complex — the polysynthetic template

The verb is the heavy word. Its shape, fixed:

> **ABS – DIR – ERG – ROOT – TENSE/MOOD – NEG – Q**

| Slot | What it carries | Forms |
|---|---|---|
| **ABS** | agreement with the absolutive (intransitive subject, or the object of a transitive) | *me-/mô-* 1sg · *se-/sô-* 2sg · **∅** 3sg · *mēg-* 1pl · *tēg-* 2pl · *ne-/nô-* 3pl |
| **DIR** | direction / orientation | *sin-* "hither" (< *sīn* here) · *tôl-* "onward, thither" (< *tôl* then, next) · *maha-* "down, off" (< *maha*) |
| **ERG** | agreement with the ergative agent — innermost, against the root | same person forms as ABS |
| **ROOT** | any Nelôxi verb, unchanged | *nǟgô, lǟdô, donā, komprā, tēdô…* |
| **TENSE/MOOD** | the Metropolitan machinery, kept | past *-i* · conditional *-ks* · (no future, as everywhere) |
| **NEG** | negation | *-p* (helper vowel per harmony after a consonant: *-ôp/-ep*) |
| **Q** | polar question | *-ka* |

**The affix material is Nelôxi.** The person prefixes are the pronouns *mä, sä, tä, mēg, tēg,
ne* ground down to their consonants; the directionals are the adverbs *sīn, tôl, maha*; the
tense suffixes are the coursebook's own. Circassian contributes the template — the fact of
packing, the slots, their order — and one piece of borrowed structure, the negative *-p*
(the Adyghe *-ep* pattern). Prefix vowels obey ordinary Nelôxi harmony (*me-nǟgô* front,
*mô-donā* back); before a vowel-initial root the vowel drops (*m-um*).

### Role is read from order

Outer prefix = absolutive, inner prefix = ergative. The same two morphs, swapped, swap the
meaning — the Sarmatian standard's favorite classroom minimal pair:

- *se-me-nǟgô* — ABS 2sg + ERG 1sg: "**I see you.**"
- *me-se-nǟgô* — ABS 1sg + ERG 2sg: "**you see me.**"

Third person singular is **∅** in both slots, so an all-third-person clause carries a bare
verb — *Kalāji-r kalā vendā* looks almost Metropolitan, and only the *-r* and the order give
it away. Third plural is *ne-*: *Mäs txai ne-tēdô* "they know my tea."

### Worked forms

| Sarmatian standard | Built as | Metropolitan | Gloss |
|---|---|---|---|
| *Mä-r mer me-nǟgô.* | mer(ABS) me-(ERG.1sg)-see | *Mä nǟgô mern.* | I see the sea. |
| *Mä turgôle me-lǟdô.* | market-to me-(ABS.1sg)-go | *Mä lǟdô turgôlô.* | I go to the market. |
| *Me-nǟgô-p.* | (ABS.3sg ∅)-ERG.1sg-see-NEG | *Mä äb nǟgô tä.* | I don't see him/her. |
| *Mēg-tēg-nǟgi-p.* | ABS.1pl-ERG.2pl-see-PST-NEG | *Tēg äb nǟgi mēg.* | You (pl.) didn't see us. |
| *Sin-tulē!* | hither-come | *Tulē sīn!* | Come here! |
| *Kalā sin-donā!* | fish(ABS) hither-give | *Donā kalān sīn!* | Hand the fish over here! |
| *Se-tulē-ka?* | ABS.2sg-come-Q | *Ka sä tulē?* | Are you coming? |
| *Mô-komprā-ks.* | ERG.1sg-buy-COND | *Mä kompraks.* | I would buy it. |

**Pro-drop, absorbed.** Because the verb carries its persons, the free pronouns drop unless
focused or contrasted; *Me-nǟgô-p* is a complete sentence. Written Sarmatian standard hyphenates the
verb-complex seams and the ergative in teaching texts (as throughout this section); running
prose writes them solid (*menǟgôp, mär*).

## §5 · Negation — verb-internal, no *äb*

The particle *äb* **does not exist in the Sarmatian standard**. Negation is the suffix *-p*, ordered
after tense, before *-ka*:

- *Mä-r tä me-nǟgô-p.* / packed: *Me-nǟgô-p.* — "I don't see him."
- *Rā m-um-p.* — "I have no money." (§7)
- Past: *me-nǟgi-p* "I didn't see"; conditional: *me-nǟgôksep* "I wouldn't see."
- **Negative imperative**: bare stem + *-p* — *Votā-p!* "Don't take it!" (Metr. *äb votā!*)
- Standalone "no" is still **nē**; negative concord with *midagü* holds: *Midagü me-nǟgô-p*
  "I see nothing."

## §6 · What is kept from the coursebook, deliberately

The fork diverges where Circassian leads and **nowhere else**. Kept exactly: the past *-i*
and its two classes, the conditional *-ks*, the no-future rule and the time-word toolkit,
the analytic modals *vôī* and *pidā* (they stand immediately before the verb complex:
*Mä pidā me-lǟdô* → *Pidā me-lǟdô* "I must go"), the copula pair *um/ūli*, the hortative
*-m* and bare-stem imperative, the participles *-ji/-dôt*, the whole derivational suffix set
(*-ôr, -in, -mus, -ām, -stā, -ldā, -tā, -mi*), the dozenal numbers, the 24-hour clock, the
calendar, vowel harmony, and consonant gradation. A Turkic loan-root takes *-ôr* the way a
Hassaniya root does: *bazarôr* "market trader" — the hybrid seam, sixth hand on the same
machine.

## §7 · Copula and possession

- **The copula goes final**, like every verb, invariant as ever: *Nahtô kylm um.* "The night
  is cold." (Same three words as Metropolitan *Nahtô um kylm* — order is the only change.)
- **Possession packs into an agreeing verb.** Metropolitan says *Mäl um rā* (at-me is
  money); the Sarmatian standard gives the possessor the ergative and echoes it on the copula:
  *Mä-r rā m-um*, or with the pronoun dropped, simply **Rā m-um** "I have money."
  Past *Rā m-ūli* "I had money"; negative *Rā m-um-p* "I'm broke"; second person *Rā s-um-ka?*
  "Do you have money?" The casual doublet slots straight in: *Para s-um-ka?*

## §8 · Writing connected Sarmatian standard — the composition rule

The Saharannaise rule inverted: **the words do the bridging, the structure does the
diverging.** Build the sentence from coursebook lexemes — reach for a Turkic doublet only in
casual register — and run it through the machine above: verb to the end, *-r* on the agent,
persons into the verb, *-p* for any negation. If a mainlander can gloss every word of your
sentence and still has to work for the proposition, you have written good Sarmatian standard.

A worked paragraph (every content word coursebook canon; the loans *bazar, txai, dost*
tagged (Sarm.)):

1. *Matīl kalāji-r kalā bazarôle tôl-vendāi.* — "In the morning the fisher sold the fish off
   at the bazar." *(SOV; ergative -r; directional tôl-; past -i inside the complex.)*
2. *Vespôrôl tä kōtôle tulī.* — "In the evening he came home." *(Intransitive: bare
   absolutive, ∅ 3sg agreement — the one line a mainlander reads cold.)*
3. *Dost-r txai kuinai, ja jôvā pǟvôt mēg-parlāi.* — "A friend made tea, and we talked of
   the good day." *(dost casual for amīk; the partitive surviving in its partial sense;
   "we" carried by the verb's own prefix.)*
4. *Rā mult m-um-p — agā merjagô jôvā um.* — "I don't have much money — but the sea's share
   is good." *(Possession packed; -p; the copula line, final.)*

**Run together:**

> *Matīl kalāji-r kalā bazarôle tôl-vendāi. Vespôrôl tä kōtôle tulī. Dost-r txai kuinai, ja
> jôvā pǟvôt mēg-parlāi. Rā mult m-um-p — agā merjagô jôvā um.*

Every root is legible from the mainland; not one clause parses by mainland rules. That is a
paragraph of Sarmatian standard: Nelôxi words, Caucasian house.

## §9 · What is NOT taken from Circassian — the guardrails

- **No vocabulary.** Not one Caucasian content-root in the core lexicon; the only Circassian
  words anywhere in the fork are the seat's own proposed name (*Xasā*) and title (*Tamadā*),
  learned-register institution-nouns exactly like *Dīwān* and *Penc*.
- **No phonology.** None of Adyghe's ejectives, none of its consonant inventory, no new
  graphemes (`script.md`). The template is borrowed; the sounds that fill it are Nelôxi's.
- **No further slots.** The template of §4 is **closed** — the Sarmatian standard does not grow
  applicatives, causative prefixes, valence machinery, or any additional slot without
  a Xasā ruling logged against this file. Adyghe has far more machinery than §4 takes;
  taking more is drift toward relexified-Circassian, the failure mode in the other
  direction.

---

*Companions: the noun half in `noun-cases.md`; the loan layer in `loans-turkic.md`; the
proof-by-lineup in `showcase-hexalect.md`; the machine in living use in `dialogue-bazar.md`.
The Metropolitan baseline diverged from is `../grammar/structural-profile-apics.md`.*
