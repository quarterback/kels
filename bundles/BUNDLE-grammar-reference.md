# Nelôxi — COMPLETE GRAMMAR REFERENCE (self-contained)

> The full structural core of Nelôxi in one file. Hand this to a grammar agent, or to any
> agent that has started drifting (using Estonian, guessing forms) to re-ground it.
> Canon v5.56. Every module assumes no prior knowledge.

---

# Nelôxi Foundation Grammar — Module Index

These modules teach the structural core of Nelôxi. **Each is self-contained and assumes no
prior knowledge** — an agent with an empty context can read any one and apply it correctly,
without relying on conversation history. Hand an agent the module(s) relevant to its task.

Reading order for a full onboarding:

- **00** — this index
- **01 — The Partitive Case** — partial/counted/negated/ongoing objects (-t / -tô)
- **02 — The Verb Derivation Engine** — building verbs from verbs (causative, frequentative,
  momentane, reflexive)
- **03 — Consonant Gradation** — the double-stop → single-stop stem alternation
- **04 — Compounding** — joining existing roots into new words (head-final)
- **06 — Noun Declension** — the full case table; how any noun runs through every case
- **07 — Pronouns** — personal, possessive, demonstrative, interrogative, relative, indefinite
- **08 — Relations** — spatial & temporal: which cases do the job, the full postposition inventory, known gaps
- **09 — Tense & Aspect** — how to say when: the complete time system (no future/perfect by design)
- **10 — Adjectives** — invariance plus eventive adjectives
- **11 — Commands & Suggestions** — the imperative (bare stem) and hortative (-m)
- **12 — Numbers** — dozenal digits, fused teens, counted nouns, fractions, clock time, and percent
- **13 — Loan Endings & Surface Balance** — how a borrowed word enters and declines; -ô is one landing form, not the default (§109)
- **14 — Sentence & Text Composition** — the capstone: building a clause, joining clauses into complex sentences, and chaining sentences into a paragraph; a writer's checklist and the syntactic gaps that block prose

Reference (not a teaching module):
- **structural-profile-apics** — Nelôxi's full typological profile answered against the APiCS
  (Atlas of Pidgin & Creole Language Structures) parameter framework: word order, nominal
  categories, TMA, negation, questions, sound systems, lexicon, sociolinguistics — with
  daughter-lect divergences and open slots flagged.

Planned / forthcoming modules:
- **05 — Contact History** — the historical story of who brought which words (Hanseatic Low
  German, the Marīsô Slavic border, Scandinavian coast, Finnic substrate), so contributors reach
  for the right source organically rather than by rule. (To be written from the worldbuilding.)

Each module corresponds to a charter ruling (§59, §60, §61, …) where the change is logged.
The authoritative source is always `coursebook/nelo-kel-coursebook.md`; these modules are the
teachable presentation of what the coursebook encodes.

---

# Nelôxi Grammar — The Partitive Case
*Foundation module 01 · charter §59*

> **Read this even if you have never seen Nelôxi before.** It teaches one case of the language
> from scratch. You need no other file to apply it. Terms are defined as they appear.

## Background you need first

**Nelôxi** is a constructed language whose nouns take **endings** to show their role in a
sentence. The base form of a noun is its **stem** (e.g. *lēte* "milk," *pan* "bread," *kalā*
"fish"). One such ending marks the **direct object** — the thing an action is done to — with
**-n**: *Mä juô lēten* "I drink the milk." This document teaches a *different* object ending,
the **partitive**, and when to use it instead of -n.

## What the partitive means

The **partitive** marks a noun as **partial, unbounded, or indefinite** — "some of it," "an
unspecified amount," "not the whole thing." It contrasts directly with the **-n** object case,
which marks a **whole, complete, bounded** thing.

- *Mä juô lēte**n*** — "I drink **the** milk" (all of it; the glass is emptied)
- *Mä juô lēte**t*** — "I drink milk / **some** milk" (part of it; unbounded)

## Form

- Stem ending in a **vowel** → add **-t**: *lēte* → *lētet*; *kalā* → *kalāt*
- Stem ending in a **consonant** → add a linking vowel + **-tô** or **-tä** (chosen by vowel
  harmony — back vowels take -tô, front vowels take -tä): *pan* → *pant*; *sōl* → *sōlat*

## When you MUST use the partitive (four situations)

### 1. Partial or uncountable objects
Things you can't count as whole units, or take only part of:
*votā vetet* "take some water" · *anda rāt* "give some money."

### 2. After a number greater than one, and after quantity words
The counted noun goes in the **partitive singular** (not a plural):
*tri kalāt* "three fish" · *mult pant* "much bread" · *vehä sōlat* "a little salt."

### 3. Whenever the object is negated
A negated object is **always** partitive — never -n:
*Mä äb juô lētet* "I don't drink milk" · *tä äb nǟ kalāt* "he doesn't see any fish."

### 4. When the action is ongoing / incomplete
The case on the object shows whether the action is finished. This is how Nelôxi expresses
aspect — there is no separate tense for it:
- *Mä lugē livrô**t*** "I am reading a book" (ongoing, not finished)
- *Mä lugē livrô**n*** "I read the book (through)" (finished, whole)

## Rule of thumb for contributors

Ask of every object: **whole and finished?** → use **-n**. **Partial, uncountable, counted,
negated, or still ongoing?** → use the partitive **-t / -tô**. Counted things and negated
objects always take the partitive.

---

# Nelôxi Grammar — The Verb Derivation Engine
*Foundation module 02 · charter §60*

> **Read this even if you have never seen Nelôxi before.** It teaches how the language builds
> verbs from other verbs, from scratch. You need no other file to apply it.

## Background you need first

**Nelôxi** is a constructed language. A **verb** names an action; its base form (the
**dictionary form**) is also the present tense — e.g. *sȫ* "to eat / eats," *nǟgô* "to see /
sees," *avā* "to open." This document shows how to turn one such verb into a whole family of
related verbs by adding a **derivational ending** to the stem. The point: **when you need a
verb that is a variant of one that already exists, you build it with these endings — you do
not invent a new word or borrow one.**

## The four derivation chains

### 1. Causative — ending *-tā / -tä* — "make/cause X to happen"
Adds a doer who causes the action.
- *kūlô* "hear" → *kūlôtā* "announce" (make someone hear)
- *sȫ* "eat" → *sȫtä* "feed" (make someone eat)
- *kadô* "vanish" → *kadôtā* "get rid of" (make something vanish)

### 2. Frequentative — ending *-ilā / -elä* — "keep doing X, do X repeatedly"
Marks repeated, habitual, or drawn-out action.
- *lôigā* "cut" → *lôigilā* "keep cutting"
- *nǟgô* "see" → *nǟgilä* "keep looking, gaze"
- *koput* "knock" → *koputelä* "keep knocking"

### 3. Momentane — ending *-ahtā / -ähtä* — "do X once, suddenly"
A single instant of the action — the opposite of the frequentative.
- *naurô* "laugh" → *naurahtā* "give a (single) laugh"
- *nǟgô* "see" → *nǟgahtā* "glance"
- *līkô* "move" → *līkahtā* "give a start, twitch"

### 4. Reflexive / automative — ending *-u / -y* — "X happens of itself, or to oneself"
Removes the outside doer; the action happens on its own or turns back on the subject.
- *avā* "open (something)" → *avau* "come open (by itself)"
- *kôrdā* "fix" → *kôrdau* "get fixed, come right"
- *pesô* "wash" → *pesu* "wash oneself"

## The chains stack

You can apply one ending to an already-derived verb:
- *sȫ* eat → *sȫtä* feed → *sȫtätä* "have (someone) fed"
- *avā* open → *avau* come open → *avautelä* "keep coming open"

## How to apply it as a contributor

Need a verb meaning a caused, repeated, momentary, or self-happening version of an existing
verb? **Add the matching ending to the existing stem.** Only coin or borrow a brand-new root
when there is no existing verb to build from. This is the main way the language grows verbs
without borrowing.

---

# Nelôxi Grammar — Consonant Gradation
*Foundation module 03 · charter §61*

> **Read this even if you have never seen Nelôxi before.** This document teaches one rule of
> the language from scratch. You do not need any other file to apply it. Terms are defined as
> they appear.

## Background you need first (30 seconds)

**Nelôxi** is a constructed language. Its nouns and verbs change form by adding endings to a
**stem** (the base form of a word). For example, the noun stem *kōt* "house" adds **-l** to
mean "at the house" (*kōtôl*) and **-n** to mark it as a direct object (*kōtôn*). The bare stem
with no ending is also the **dictionary form** — the form you look up.

Some stems end in a **double stop**: a doubled *k*, *p*, or *t*, written **kk**, **pp**, **tt**
(e.g. *tappô* "deed," *noppô* "a choice," *jättô* "a leaving"). This document is about what
happens to those double stops when you add an ending.

## The rule

> **A stem-final double stop (kk, pp, tt) weakens to a single stop (k, p, t) when an ending is
> added.**

The doubled form is called the **strong grade**; the single form is the **weak grade**.

- **Strong grade** = the bare dictionary form, no ending: *tappô*, *noppô*, *jättô*.
- **Weak grade** = the form with almost any ending attached: *tapô-*, *nopô-*, *jätô-*.

## Worked examples

Noun *tappô* "deed" (stem ends in **-pp-** … wait: the doubling is **pp**):

| Meaning | Form | Grade |
|---|---|---|
| a deed (dictionary form) | **tappô** | strong (pp) |
| the deed — as object (-n) | **tapôn** | weak (p) |
| of the deed (-s) | **tapôs** | weak (p) |
| at the deed (-l) | **tapôl** | weak (p) |

Noun *jättô* "a leaving" (ends in **-tt-**):

| Meaning | Form |
|---|---|
| a leaving (dictionary) | **jättô** |
| the leaving — object | **jätôn** |
| at the leaving | **jätôl** |

Verb *jättā* "to leave" (ends in **-tt-**) — gradation also happens in the **past tense**
(past adds **-i** to the stem):

| Meaning | Form |
|---|---|
| to leave / leaves (present) | **jättā** |
| left (past) | **jäti** |

Verb *noppā* "to pick" (ends in **-pp-**):

| present | **noppā** |
| past | **nopi** |

## The limits of the rule (important — do not over-apply)

This is the **only** consonant change in Nelôxi. Specifically:

1. It applies **only** to a **double stop (kk, pp, tt)** at the **end of a stem**.
2. It weakens to the **single** version of the same stop: kk→k, pp→p, tt→t. Nothing else.
3. **Every other consonant is stable.** Single stops, *s, l, r, m, n, v, j, ç, x, ñ*, etc.
   never change.
4. **Vowel-final stems never change** — and these are the large majority of the language, so
   most words are completely unaffected.

There is no other mutation, softening, or alternation anywhere in the language. If a stem does
not end in kk, pp, or tt, it does not gradate. Do not invent gradations for other consonants.

## How to apply it as a contributor

1. Look at the stem's ending.
2. If it ends in **kk, pp, or tt** → use the single stop (k, p, t) before any case ending or in
   the past tense. Keep the double stop only in the bare dictionary form.
3. If it ends in anything else → do nothing; the stem is stable.

That is the entire rule.

---

# Nelôxi Grammar — Compounding
*Foundation module 04 · charter §62*

> **Read this even if you have never seen Nelôxi before.** It teaches how the language builds
> new words by joining existing ones, from scratch. You need no other file to apply it.

## Background you need first

**Nelôxi** is a constructed language. Words have a base form called the **stem** (e.g. *livrô*
"book," *kōt* "house"). Like English and the Finnic and Germanic languages, Nelôxi can join two
stems into a single new word — a **compound** (English does this in "bookhouse," "rainstorm,"
"nightwatch"). This document teaches how Nelôxi does it, so you can **build a needed word from
roots that already exist instead of borrowing or inventing one.**

## The core rule: compounds are head-final

The **last** element is the **head** — it carries the core meaning. Everything before it
**modifies** the head. The whole compound is "a kind of [head]."

- *livrô* "book" + *kōt* "house" → **livrôkōt** "library" — a kind of *house* (for books)
- *petīt* "small" + *vim* "rain" → **petītvim** "drizzle" — a kind of *rain* (small)
- *sesôn* "season" + *kôrd* "order, cycle" → **sesônkôrd** "the seasonal cycle" — a kind of
  *order*

If you reverse the elements you change the meaning: a "house-book" (*kōtlivrô*) would be a book
about houses, not a library. **The head always comes last.**

## How to join the pieces

1. **The modifier keeps its bare stem** — no ending: *sesôn* + *kôrd* → *sesônkôrd* (not
   *sesônôs kôrd*).
2. **Add a linking vowel only if needed for pronunciation** — *-ô-* with back-vowel words,
   *-e-* with front-vowel words: *pildô-livrô* "picture book," *lǟmi-mēdôr* "thermometer." If the
   two stems already join cleanly, add nothing.
3. **Stress stays on the first element** (Nelôxi always stresses the first syllable of a word),
   so the compound is pronounced as one word: *LIVrôkōt*.
4. **Only the head takes endings.** To inflect a compound, put the case ending on the **last**
   element: "in the library" = **livrôkōtôl** (the -l "at/in" attaches to *kōt*). Never inflect
   the modifier.

## Interaction with consonant gradation

If the head ends in a double stop (**kk, pp, tt**), it still weakens to a single stop when
inflected (this is the general gradation rule — see module 03). A compound ending in *-jättô*
would inflect as *-jätô-*. If the head has no double stop, nothing changes.

## Chaining

Compounds can themselves be built from compounds, always head-final:
- *matī* "morning" + *veç* "water" → **matīveç** "dew"
- *tems* "weather" + *livrô* "book" → **temslivrô** "almanac"

## How to apply it as a contributor

Need a word for a compound concept — "harbor-master," "fish-market," "night-watch"? Find the
two roots already in the lexicon, put the **modifier first and the head (the core thing) last**,
join them (with a linking vowel only if needed), and inflect only the head. Build before you
borrow.

---

# Nelôxi Grammar — Noun Declension (The Full Case Table)
*Foundation module 06 · charter §66*

> **Read this even if you have never seen Nelôxi before.** It shows how any noun changes form
> for every case, from scratch. You need no other file to inflect a noun correctly.

## Background you need first

**Nelôxi** nouns do the work English does with word order and prepositions by adding **case
endings** to the **stem** (base form). "In the house," "of the house," "into the house" are all
one word: *kōt* + an ending. This module lists every case and shows model nouns run all the way
through, so you never have to guess a form.

## The two rules that govern every ending

1. **Linking vowel.** When an ending begins with a consonant and the stem ends in a consonant,
   a helping vowel joins them: **-ô-** after the back vowels *a o u ô*, and **-e-** after the
   front vowels *ä ö y e i*. (This is vowel harmony — the helper matches the stem's vowel type.)
   Vowel-final stems usually need no helper.
2. **Consonant gradation.** If the stem ends in a double stop **kk, pp, tt**, it weakens to a
   single **k, p, t** before an ending (see module 03). Most stems are unaffected.

## The cases

| Case | Ending | Meaning |
|---|---|---|
| plain (nominative) | — | the subject |
| object (accusative) | **-n** | whole/completed direct object |
| partitive | **-t / -tô / -tä** | partial, counted, negated, or ongoing object |
| linking (genitive) | **-s** | of, 's, possession |
| place (locative) | **-l** | in, at, on |
| goal (lative) | **-lô / -lä** | into, onto, to |
| source (ablative) | **-lt** | from |
| together (comitative) | **-k** | with, using |
| plural marker | **-d** | (added before case endings for plural) |

## Model noun 1 — *kōt* "house" (consonant-final, back-harmony, no gradation)

| Case | Singular | Plural (insert -d-) |
|---|---|---|
| plain | **kōt** | **kōtôd** |
| object | **kōtôn** | **kōtôdôn** |
| partitive | **kōtôt** | **kōtôdôt** |
| linking | **kōtôs** | **kōtôdôs** |
| place | **kōtôl** | **kōtôdôl** |
| goal | **kōtôlô** | **kōtôdôlô** |
| source | **kōtôlt** | **kōtôdôlt** |
| together | **kōtôk** | **kōtôdôk** |

## Model noun 2 — *mer* "sea" (consonant-final, front-harmony)

| Case | Singular | Plural |
|---|---|---|
| plain | **mer** | **mered** |
| object | **meren** | **mereden** |
| partitive | **meret** | **meredet** |
| linking | **meres** | **meredes** |
| place | **merel** | **meredel** |
| goal | **merelä** | **meredelä** |
| source | **merelt** | **meredelt** |
| together | **merek** | **meredek** |

(Front-harmony stems take **-e-** helpers and the **-lä** goal ending, mirroring *kōt*'s back
**-ô-** and **-lô**.)

## Model noun 3 — *kalā* "fish" (vowel-final — no helper vowel needed)

| Case | Singular | Plural |
|---|---|---|
| plain | **kalā** | **kalād** |
| object | **kalān** | **kalādôn** |
| partitive | **kalāt** | **kalādôt** |
| linking | **kalās** | **kalādôs** |
| place | **kalāl** | **kalādôl** |
| goal | **kalālô** | **kalādôlô** |
| source | **kalālt** | **kalādôlt** |
| together | **kalāk** | **kalādôk** |

## Model noun 4 — *tappô* "deed" (ends in double stop — gradation fires)

The **-pp-** weakens to **-p-** before every ending; the strong grade survives only in the bare
plain form:

| Case | Singular |
|---|---|
| plain | **tappô** |
| object | **tapôn** |
| partitive | **tapôt** |
| linking | **tapôs** |
| place | **tapôl** |
| goal | **tapôlô** |
| source | **tapôlt** |

## How to inflect any noun (procedure)

1. Find the stem's final sound.
2. **Vowel-final** (*kalā*)? Add the ending directly (no helper).
3. **Consonant-final** (*kōt*, *mer*)? Insert the harmony helper (**-ô-** back / **-e-** front),
   then the ending.
4. **Ends in kk/pp/tt** (*tappô*)? Weaken to single stop before adding anything.
5. **Plural?** Insert **-d-** after the stem, before the case ending.

Follow the model noun that matches your stem's shape. Every noun in the language declines by one
of these four patterns.

---

# Nelôxi Grammar — Pronouns (The Full Paradigm)
*Foundation module 07 · charter §67*

> **Read this even if you have never seen Nelôxi before.** It gives every pronoun in every form,
> from scratch. You need no other file. Pronouns are among the most frequent words in any
> language — get these right and most sentences fall into place.

## Background you need first

**Nelôxi** pronouns **decline like nouns** — they take the same case endings (see module 06). So
"me / to me / with me / from me" are the pronoun *mä* "I" carrying the object, goal, comitative,
and source endings. This module runs every pronoun through its forms so nothing is guessed.

## 1. Personal pronouns

Base forms:
- **mä** I · **sä** you (sg.) · **tä** he/she/it · **mēg** we · **tēg** you (pl.) · **ne** they

Declined (same endings as nouns — object -n, linking/possessive -s, place -l, goal -lô/-lä,
source -lt, comitative -k):

| | I | you sg | he/she/it | we | you pl | they |
|---|---|---|---|---|---|---|
| plain (subject) | mä | sä | tä | mēg | tēg | ne |
| object (me/you…) | män | sän | tän | mēgen | tēgen | nen |
| possessive (my…) | **mäs** | **säs** | **täs** | **mēgs** | **tēgs** | **nes** |
| to (to me…) | **mäle** | **säle** | **täle** | mēgele | tēgele | nele |
| at/on (place) | mäl | säl | täl | mēgel | tēgel | nel |
| from (source) | mält | sält | tält | mēgelt | tēgelt | nelt |
| with (comitative) | mäk | säk | täk | mēgek | tēgek | nek |

Note: the "to" form uses the goal case and is the everyday **dative** ("give it to me" =
*donā sen mäle*). Nelôxi has **no gender** — *tä* is he, she, or it alike.

Pronouns are dropped once the subject is clear (Nelôxi is pro-drop): *Ka sä volē pan? — Jā, volē*
"Do you want bread? — Yes, (I) want."

## 2. Possessive (just the -s form, used before the noun)

**mäs** my · **säs** your · **täs** his/her/its · **mēgs** our · **tēgs** your (pl.) · **nes** their.
*Mäs nim um Ron* "My name is Ron." *Ka säs gos um jūn?* "Is your dog young?"

## 3. Demonstratives

- **se** this / that (the general one; also "it")
- **sedä** this-here (near the speaker) · **tuo** that-there (far)

They decline like nouns: *sen* (obj.), *ses* (of this), *sel* (at this), *selô* (to this).
*Anda sen mäle* "give me that." Plural: **ned** "these/those."

## 4. Interrogatives (question words)

- **ken** who · **mis** what/which · **kus** where · **kun** when · **miks** why · **kui** how ·
  **kui mult** how much/many
- These decline too: *kenen* "whom (obj.)," *kens* "whose," *kusel*… but most appear in the
  plain form fronted in the question: *Ken tulē?* "Who is coming?" *Mis um säs nim?* "What is
  your name?" *Kus sä lǟdô?* "Where are you going?"

## 5. Relatives (linking clauses)

- **ken** "who" (for people), **mis** "which/what" (for things) — the same words as the
  interrogatives, used to head a relative clause: *mēs, ken kantāi* "the man who sang"; *livrô,
  mis vanamǟr donai* "the book that grandmother gave."
- **et** "that" introduces a reported/complement clause: *Mä tēdô, et sä tulī* "I know that you
  came."

## 6. Indefinite & universal

- **kekõ** someone / anyone · **miskü** something / anything · **kôgõ** everything · **kôg** all,
  every · **mõnü** some, a few · **midagü** nothing · **isü** self, oneself · **teinütõ** each
  other, one another
- These decline like nouns as needed: *kekõle* "to someone," *miskün* "something (obj.)."

## How to use this as a contributor

Need a pronoun in a role you haven't seen? **Take the base pronoun and add the case ending from
module 06**, exactly as you would to a noun. "with them" = *ne* + comitative *-k* = *nek*. Do not
reach for another language's pronoun — every form is derivable from the base plus a case ending.

---

# Nelôxi Grammar — Spatial & Temporal Relations (Postpositions and Cases)
*Foundation module 08 · charter §68*

> **Read this even if you have never seen Nelôxi before.** It teaches how the language says
> where and when things are — every relation, in one place. You need no other file.

## Background you need first

English uses **prepositions** before a noun ("under the house"). **Nelôxi** does two things
instead, and knowing WHICH to use is the whole trick:

1. **Cases** — endings on the noun itself — handle the most basic relations (in/at, into, from,
   with). See module 06.
2. **Postpositions** — little words placed **after** the noun — handle everything finer (under,
   behind, through, between). The noun before a postposition takes the **linking -s** case:
   *kōtôs al* "under the house" (literally "the-house's under").

**Rule one: check whether a case already does the job before reaching for a postposition.**

## Part 1 — Relations handled by CASE (no postposition needed)

| Relation | Case | Example |
|---|---|---|
| in / at / on | place **-l** | *kōtôl* "in the house" |
| into / onto / to | goal **-lô/-lä** | *kōtôlô* "into the house" |
| from | source **-lt** | *kōtôlt* "from the house" |
| with / using | comitative **-k** | *aerôk* "with an oar" |
| of / possession | linking **-s** | *kōtôs port* "the house's door" |
| to (a person) — dative | goal on pronoun/person | *mäle* "to me," *täle* "to him" |
| becoming / turning (a state) | goal on the state-word | *mer jǟi vaiklô* "the sea went calm" |

Do NOT build a postposition for these; the ending is the whole answer.

## Part 2 — The postposition inventory (noun takes -s, word follows)

### Spatial
- **al** — under: *kōtôs al* "under the house" *(nominal cousin: alū "the underside")*
- **tāga** — behind: *pūs tāga* "behind the tree"
- **jeds** — in front of: *portôs jeds* "in front of the door"
- **kesk** — in the middle of: *pǟvôs kesk* "at midday"
- **sisü** — inside: *kōtôs sisü* "inside the house"
- **ümbär** — around: *linnôs ümbär* "around the town"
- **läbi** — through: *meçās läbi* "through the forest"
- **üle** — over, across: *jôgôs üle* "across the river"
- **vahel** — between (two things): *kōtôs ja merôs vahel* "between the house and the sea"
- **pitkin** — along: *rāndôs pitkin* "along the shore"
- **pōl** — toward: *satāmôs pōl* "toward the harbor"
- **vällô** — outside, beyond: *līnôs vällô* "outside the town"

### Temporal
- **enne** — before (in time): *pulmôs enne* "before the wedding" (also bare adverb "earlier")
- **pǟrast** — after (in time): *mult tīt pǟrast* "after much time"
- **kesk** — in the middle of (a time): *ȫs kesk* "in the middle of the night"

### Abstract / transactional
- **pǟl** — about, concerning: *merôs pǟl* "about the sea"
- **ilma** — without: *rās ilma* "without money"
- **eest** — for, in exchange for: *kolm kalād dva rās eest* "three fish for two money"
- **vastü** — against; in reply to: *tūlôs vastü* "against the wind"

## Part 3 — Known gaps (flag these; do not invent)

Relations with **no form yet** (a delegate who needs one flags it as a gap for the Rector):
- "beside / next to" (currently approximated with *kesk*/*jeds* phrases) ·
  "instead of" as a spatial frame (*hoopõs* covers the adverb "instead") · "since (a time)" ·
  "until" as a postposition (*kuni* exists but is a conjunction: *kuni sup um paks* "until the
  soup is thick" — there is no noun-governing "until Tuesday" form yet).

## How to say it (procedure)

1. Is the relation basic (in/to/from/with/of)? → **use the case ending** (Part 1).
2. Finer relation? → noun in **-s**, then the **postposition** (Part 2).
3. Not in either list? → **it is a gap. Flag it.** Do not borrow a word from another language
   and do not repurpose a case.

---

# Nelôxi Grammar — Tense & Aspect (How to Say When)
*Foundation module 09 · charter §69*

> **Read this even if you have never seen Nelôxi before.** It teaches the complete system for
> expressing time — including every English tense Nelôxi does NOT have, and exactly what to say
> instead. You need no other file.

## Background you need first

**Nelôxi** verbs have only **two inflected tenses** — present (the bare dictionary form) and
past (**-i**) — plus a conditional (**-ks**). There is **no future tense, no perfect ("have
done"), no pluperfect, and no progressive ("is doing") as verb forms.** This is deliberate:
the language pushes time onto **time-words** and **the object's case**, not onto the verb.
This module shows how every English time-meaning is actually expressed. Do not invent tenses.

## The two verb tenses

| Tense | Form | Example |
|---|---|---|
| Present (also habitual & future) | bare stem | *mä lugē* "I read / I am reading / I will read" |
| Past | stem + **-i** | *mä lugī* "I read (yesterday) / was reading" |

Copula: **um** (present, all persons) / **ūli** (past). Conditional: **-ks** (*voleks* "would
want," *pidāks* "should").

### Building the past — two classes (§120)

The marker is always **-i**; how it surfaces depends on the verb's class:

- **Class I — basic (root) verbs.** Drop the final stem vowel, add **-i**. After root **-a-/-ā**
  the *-i* fuses into the diphthong **-ai**: *donā→donai*, *votā→votai*, *ootā→ootai*,
  *vōigā→vōigai*, *kantā→kantāi*. After other root vowels it is plain **-i**: *lǟdô→lǟdi*,
  *pelgô→pelgi*, *sōudô→sōudi*, *itkô→itki*.
- **Class II — derived verbs** (a derivational suffix on the stem — frequentative *-ldā/-tā*,
  continuative/inchoative *-stā/-stō*). The suffix's consonant blocks the diphthong, so the past is
  long **-ī**: *kalāstā→kalāstī*, *môtôldā→môtôldī*, *armôldā→armôldī*.
- **Strong basic verbs** — the three highest-frequency roots lexicalize a long **-ī**:
  *tulē→tulī*, *elā→elī*, *nǟgô→nǟgī*. Learn these as irregulars.
- **Monosyllabic vowel-roots** take a **-si** past to stay distinct from the present:
  *dī→dīsi* "said."

## How each English tense is expressed

### Future — present + a time-word
No future tense exists. The bare present with a time-word does all future work:
- *Demā mä lǟdô markôtôlô* "Tomorrow I('ll) go to the market."
- *Varsü tä tulē* "He'll come soon." · *Nūlô mä vastā* "I'll answer in a bit."
The time-word can be dropped when context is clear: *Ka sä tulē?* "Are you coming / will you come?"

### Ongoing action ("is doing") — the PARTITIVE object
Aspect lives on the **object's case**, not the verb (module 01):
- *Mä lugē livrô**t*** "I **am reading** a book" (ongoing — partitive object)
- *Mä lugē livrô**n*** "I read the book **through**" (completed — object case)
With no object, the plain verb is ambiguous and context or a time-word disambiguates:
*Mä kirôtā nū* "I'm writing right now."

### Perfect ("have done") — the plain past, with jubā "already" when needed
There is no perfect. The simple past covers it:
- "I have seen it" → *Mä nǟgī sen* (I saw it) or *Mä jubā nǟgī sen* "I've already seen it."
- "I haven't seen him in a long time" → *Mä äb nǟgī tän ammū* "I didn't see him (in) long."

### Pluperfect ("had done") — past + enne or jubā
- "She had already left when I arrived" → *Tä jubā lǟdī, kun mä tulī* "She already left when I came."

### Used to / habitual past — past + a frequency word
- *Mä kalāstī sagõ* "I used to fish often." · *Enne mä elī sāl* "I used to live there (before)."

### Was about to / on the point of — conditional + nūlô/varsü
- *Mä tuleks nūlô* "I was just about to come."

### Still / not yet / no longer — veel and the negation
- *Tä veel magā* "He's still sleeping." · *Tä äb veel tulī* "He hasn't come yet."
- *Tä äb magā amplü* "He no longer sleeps / doesn't sleep anymore." **amplü** (§120) is the
  negative-polarity "no longer / anymore"; it pairs with preverbal *äb*. (Estonian *enäm* stays
  off-limits, §112.)

## The time-word toolkit (all canon)

**Points:** *nū* now · *nūlô* just now/soon · *äsjü* a moment ago · *varsü* soon · *demā*
tomorrow · *avuī* today · *ajēr* yesterday · *hetk* a moment · *ammū* long ago.
**Sequence:** *enne* before/earlier · *pǟrast* after · *tôl* then/next · *seejärõl* after that ·
*esmõks* first · *lopõks* finally · *selēks* by then · *alõs* not until · *kuni* until (clause).
**Frequency:** *alatü* always · *sagõ* often · *vahel* sometimes · *harvõ* rarely · *jällü*
again · *jubā* already · *veel* still · *amplü* (with *äb*) no longer, anymore.
**Distributive:** *elkü* every, each (*elkü matī* "every morning").

## Rules for contributors

1. **Never coin a future, perfect, or progressive form.** The system above is complete by design.
2. Time goes in a **time-word**; completion goes in the **object's case**; everything else is
   the plain present or past.
3. Build the past by **class** (§120): basic *-a-/-ā* roots → **-ai**, other basic roots → **-i**,
   derived *-stā/-ldā/-tā/-stō* stems → long **-ī**; strong *tulī/elī/nǟgī*, monosyllabic *dīsi*.
4. "No longer / anymore" is **amplü** (§120), with *äb*. Add the frequency word **amplü** to the
   toolkit below.

---

# Nelôxi Grammar — Adjectives (Invariance and Eventive Use)
*Foundation module 10 · charter §70 (invariance), §78 and §82 (eventive adjectives)*

> **Read this even if you have never seen Nelôxi before.** It teaches how adjectives behave —
> first the invariance rule, then the eventive pattern. You need no other file.

## Background you need first

In many languages (Finnish, Russian, Latin), an adjective **agrees** with its noun — it copies
the noun's case and number endings ("in the big houses" puts endings on "big" too). **Nelôxi
does not do this.**

## The rule

> **Adjectives are invariant.** An adjective before its noun takes no case ending and no plural
> ending — ever. Only the noun (the head) inflects.

| English | Nelôxi | What inflects |
|---|---|---|
| the old book | *vana livrô* | nothing (plain) |
| the old books | *vana livrôd* | noun takes -d; *vana* unchanged |
| in the old books | *vana livrôdôl* | noun takes -d-l; *vana* unchanged |
| these old red books (obj.) | *se vana pūn livrôdôn* | only the noun |

Adjectives stack freely before the noun with no linking element: *vana pūn livrôd* "old red
books." The demonstrative comes first: *se vana pūn livrôd* "these old red books."

## When an adjective stands alone (predicate position)

After the copula, the adjective is still bare: *Livrô um vana* "the book is old." *Livrôd um
vana* "the books are old" — the adjective does not pluralize even here.

## Eventive adjectives

Some adjectives can sit in the ordinary adjective slot before an object noun while describing the
event carried by the verb. This is an **eventive adjective**. The noun still takes its normal case;
the adjective does not inflect.

**The template:**

```
Subject + verb + adjective + object noun-[object -n / partitive -t/-tô]
```

- The adjective stays **bare**.
- The **noun** carries the case.
- The adjective describes the **action/event** when the adjective plausibly applies to *how* the
  action is done.
- **Boundedness still comes from the object case, not the adjective** (object -n = bounded/done,
  partitive -t/-tô = ongoing/unbounded).

- *Tä donā kylm vastômusôn* — "She gives a cold answer / answers coldly."
- *Tä küpsā nobē kōkôn* — "She bakes a quick cake / bakes the cake quickly."

The object's case still does its ordinary aspect work — the eventive adjective does not replace
it. Object **-n** marks the action as bounded or completed; partitive **-t / -tô** marks it as
partial, ongoing, or unbounded:

- *Tä küpsā nobē kōkôn* — "She quickly bakes the cake" (bounded/completed).
- *Tä küpsā nobē kōkôt* — "She is quickly baking cake / baking at the cake" (ongoing/unbounded).
- *Tä votā nobē fȫrôn* — "He takes the lead quickly" (bounded: the lead is taken).
- *Tä votā nobē fȫrôt* — "He is quickly moving into the lead" (ongoing/unbounded).

The construction is normal grammar, not slang. It is also not fully free: an eventive reading is
conventional rather than freely productive, and strongest with adjectives whose meanings
naturally apply to actions or events — quick, sudden, cold, sharp, quiet, careful, rough, and
similar manner-like qualities. Ordinary descriptive adjectives keep their ordinary noun meaning
unless context makes an eventive reading natural.

- *Tä lugē vana livrôn* — "She reads an old book," not "she reads oldly."
- *Tä küpsā bel kōkôn* — "She bakes a beautiful cake," not usually "she bakes beautifully."

## Two apparent exceptions (which are not exceptions)

1. **Comparative -mi** (*raskmi* "heavier") and the **kui** "than" frame are DERIVATION, not
   agreement — they change the adjective's meaning, not its case: *raskmi kui ne nǟdô* "heavier
   than they seem."
2. **An adjective used AS a noun** ("the old (one)") declines like a noun, because it has become
   one: *vanan* "the old one (obj.)." This is conversion, not agreement.

## Why (for the curious)

The invariance matches the language's design: rich case morphology concentrated on the noun
head, analytic everywhere else (verbs don't agree with subjects either). One word per phrase
carries the grammar.

## Rule for contributors

Never put a case or plural ending on an attributive adjective. If you catch yourself writing
*vanad livrôd* or *vanal kōtôl* for "old" — stop; it is *vana livrôd*, *vana kōtôl*.

When using an eventive adjective, put it in the same adjective slot before the object noun and let
the noun carry the case: *kylm vastômusôn*, *nobē kōkôt*. Do not add an adverbial ending.

---

# Nelôxi Grammar — Commands & Suggestions (Imperative and Hortative)
*Foundation module 11 · charter §71*

> **Read this even if you have never seen Nelôxi before.** It teaches how to give a command and
> how to say "let's," from scratch. You need no other file. (These rules exist in canon but were
> previously only in the main coursebook; this module makes them a standalone reference.)

## Background you need first

**Nelôxi** verbs use the bare dictionary form for the present tense and add **-i** for the past
(see module 09). Giving an order and making a suggestion each have their own simple pattern,
shown here.

## The imperative — a command

> **The imperative IS the bare verb stem.** No ending, no marker. Usually no pronoun.

- *Votā!* "Take!" · *Segā!* "Stir!" · *Lôigā!* "Cut!" · *Tulē!* "Come!" · *Lǟdô!* "Go!"

You may keep the pronoun *sä* "you" for emphasis or clarity, especially in instructions:
*Sä votā veçet* "You take (some) water" — this is how recipes and directions are written, and it
is still an imperative, not a statement.

**Negative command** — put **äb** before the bare stem (the same negator used for statements):
- *Äb votā!* "Don't take!" · *Äb tulē!* "Don't come!"

Plural or polite "you" giving a command works the same way — the verb does not change; add *tēg*
"you (pl.)" if you need to make the addressee explicit.

## The hortative — "let's"

> **"Let's do X" = the verb + -m.**

- *Lǟkõm!* "Let's go!" (from *lǟdô*) · *Sȫkôm!* "Let's eat!" (from *sȫ*) · *Segākôm* "Let's stir."

The linking vowel (**-ô-** back / **-e-** front) joins the *-m* to a consonant-heavy stem, as
elsewhere. There are also two fixed hortative expressions already in the lexicon: **minõm**
"let's go / we should go" and **lasõkäi** "go on, go ahead, let's do it."

## Quick contrast

| Function | Form | Example |
|---|---|---|
| statement | bare stem + pronoun | *sä votā* "you take" |
| command | bare stem (pronoun optional) | *votā!* "take!" |
| negative command | *äb* + bare stem | *äb votā!* "don't take!" |
| let's (hortative) | stem + **-m** | *votākôm* "let's take" |

## Rule for contributors

To give an order, use the **plain verb** — do not invent an imperative ending. To say "let's,"
add **-m**. To forbid, use **äb** + plain verb. These three patterns cover all commands and
suggestions; nothing else is needed.

---

# Nelôxi Grammar — Numbers (Dozenal Counting, Clock Time, and Percent)
*Foundation module 12 · charter §37, §74–§75, §77, §80*

> **Read this even if you have never seen Nelôxi before.** It teaches the whole number system
> from scratch — counting, ordinals, fractions, the clock, and percent. You need no other file.

## Background you need first

Nelôxi counts in **twelves** (base-12, dozenal). The digits are of Slavic origin — the count of
the market and the metroplex. Twelve is the round number of the system, the way ten is in
English; a written figure like *18:00* or *61%* is read with dozenal words. Older Finnic and
Germanic numeral sets existed historically and are **withdrawn from canon** — if you see *üks,
kaks, kolm…* or *ēn, twē, drē…* in an old document, do not use them; they survive only as inland
dialect color.

## The digits (0–11)

0 **nolô** · 1 **jedôn** · 2 **dva** · 3 **tri** · 4 **xtiri** · 5 **peñç** · 6 **xeç** ·
7 **sedôm** · 8 **osôm** · 9 **deveñç** · 10 **deseñç** · 11 **elva**

Zero, **nolô**, is the placeholder and the empty count: *Mäl um nolô kalād* "I have zero fish."

Twelve — **düna** — is where counting rolls over. The powers of twelve are each their own word:

- **düna** = 12 (one dozen)
- **grosô** = 144 (a dozen dozens, the gross)
- **mīrô** = 1728 (12³)
- **miljôn** = 12⁶ (~2.99 million)

## Counting past twelve

Thirteen through twenty-three are **fused single words** — *düna* erodes to *dün-* — the way
Romance teens are opaque:

13 **dünjôn** · 14 **dünva** · 15 **düntri** · 16 **dünxtir** · 17 **dünpeñç** · 18 **dünxeç** ·
19 **dünsedm** · 20 **dünosm** · 21 **dündevç** · 22 **dündesç** · 23 **dünelva**

Everything between breakpoints is **bare juxtaposition** — largest unit first, no connector,
no hyphen:

- *dva düna* 24 · *dva düna tri* 27 · *tri düna peñç* 41
- *grosô dva düna* 168 · *dva grosô peñç düna tri* 351

The fixed largest-first order keeps it unambiguous.

## Counted nouns take the partitive singular

After any number greater than one (and after quantity words), the counted noun goes in the
**partitive singular** (-t / -tô), never a plural:

- *tri kalāt* — "three fish"
- *sedôm pǟvôt* — "seven days"
- *düna kūt* — "twelve months"

This is the partitive's counting job; module 01 covers the case in full.

## Ordinals

Add **-tô** to the cardinal: *jedôntô* first, *dvatô* second, *tritô* third, *dünatô* twelfth.
*Jedôntô pǟvôl* "on the first day." (The old *-nd* ordinal rule and the suppletive *esmī/tôin*
belong to the withdrawn numerals; do not use them.)

## Fractions and shares

Fractions come from the trade quarry (Low German, the Hanseatic counting-house layer):

- **half** — "half"
- **dēl** — "part, share"; a fraction is *number + dēl*: *tri-dēl* "a third," *xtiri-dēl*
  "a quarter," *deseñç-dēl* "a tenth"

Because twelve divides cleanly (by 2, 3, 4, 6), bulk goods sell in whole shares: half a *düna*
is *xeç* (6), a third is *xtiri* (4), a quarter is *tri* (3). The thing divided takes the
linking case: *dünas half* "half a dozen," *rās tri-dēl* "a third of the money."

## Clock time

Clock time uses **klôk** (hour, o'clock) with the **24-hour clock** — hours count 0–23 in the
dozenal numbers:

- *klôk xeç* — "at 06:00"
- *klôk dünxeç* — "at 18:00" (6 p.m. — one word, the fused teen)
- *klôk düna* — "at noon (12:00)"
- *klôk nolô* — "at midnight"

Written *18:00*. A full date-time reads *Mōndag, 13. jūli, klôk dünxeç* "Monday, July 13,
18:00." Casual speech may add the time of day (*klôk xeç ôhtôl* "six in the evening"), but the
standard is the plain 24-hour number — there is no a.m./p.m. The months (*janôr…detsembôr*) and
weekdays (*mōndag…sôndag*) are Low German trade-calendar loans; the week is **vekk**.

## Percent

Nelôxia keeps the international **%** symbol unchanged, and it means what it means everywhere:
**per hundred**. The difference is what "100" is: in a base-12 count, *100* (*jedôn-nolô-nolô*)
is 12² — **a full gross, 144**. A percentage is a fraction of the gross, so the figures do not
map one-to-one onto decimal ones:

- *100%* = the whole (144/144) — same as decimal
- half = **60%** (60 in base-12 is 72, and 72/144 = ½), not 50%

The formal term is **pôkrosa** (government documents, official metrics, civic and technical
readouts): *61%* is a pôkrosa figure in a report. The casual term is **krossi** — full certainty
is *jedôn-nolô-nolô krossi*, a full gross of certainty: "I'm 100 krossi sure" is the street
idiom. (The "two circles = a dozen of dozens" gloss is a schoolroom mnemonic for the gross, not
the mechanism.)

## Rule for contributors

Count only with the dozenal Slavic digits above. Put the counted noun in the partitive singular
(*tri kalāt*, never *tri kalād*). Form ordinals with -tô and fractions with *half / number+dēl*.
Give clock times as plain 24-hour dozenal numbers with *klôk*. Never reach for the withdrawn
Finnic (*üks…*) or Germanic (*ēn…*) numerals — a batch or text that uses them is working from
dead canon.

---

# Nelôxi Grammar — Loan Endings & Surface Balance
*Foundation module 13 · charter §109*

> **Read this before coining any borrowed word.** It teaches *how much* to sand a loan when it
> enters the language, and how the result declines. You need no other file.

How a borrowed word enters the language. The creole doctrine (§79) says borrow freely from the
owning quarry and sand the form only enough to fit Nelôxi. This module fixes *how much* sanding,
because one ending — **-ô** — had quietly become the automatic coat of paint on every loan noun,
and hundreds of words through the same machine flatten the texture. Borrowing harder does not mean
adding -ô harder. -ô is one landing form, not the default.

## The core rule

A loan noun enters in the form that best carries its source-history, chosen from six landings —
NOT defaulted to -ô because it is a noun. Before assigning -ô, test in this order:

1. **Final-consonant (zero ending)** — the borrowed stem stands as-is: *adres, postkōd, folk, rap,
   trumpet, kanôn, templ*. This is the default for stable international and learned loans. The
   language already tolerates consonant-final nouns — *kōt, mer, dek, pont, port, flag, risk,
   struktūr* — so a consonant-final loan is native-legal, not foreign.
2. **Source-final long vowel preserved** — where the final vowel IS the word's felt identity:
   *džezô, çellô, pianô, sōlô, kantelô*. Keep it; removing it makes the word less itself.
3. **Learned suffix preserved** — Greek/Latin/Romance abstractions keep their scholarly tail:
   *-ī* (liturgī, homilī, herēsī, blasfemī, anatomī), *-ēt* (identitēt, kapasitēt), *-ūr*
   (struktūr, dressūr, kultūr), *-iôn* (akūzatsiôn, procesiôn, edukatsiôn).
4. **True derived Nelôxi form** — when the word is genuinely built inside the language with a
   declared suffix: *-ômus/-mys* (result/event nouns off verbs), *-ôr/-ji* (agents), *-in, -ām*.
   A derivation, not a paint job.
5. **Raw international scar** — the deliberate un-nativized loan whose foreign shape is the point:
   *džezô*'s dž, *flœzī*'s œ, and the fossil/polemic compounds where ugliness carries social
   history: *fānkellô, düvēlmarkôt, drōksektô, hūrkirīk*. The sediment doctrine (§97) protects
   these — do not sand them.
6. **-ô** — the domesticated count-noun ending, used ONLY when it is the cleanest Nelôxi landing,
   not because the word is a noun. Keep it where it is doing real work (§below).

## Endings as register, not decoration

The ending should tell you a word's history. Allocation:

| ending | carries |
|---|---|
| **zero** (consonant-final) | raw/stable international & learned loans: adres, postkōd, folk, rap, trumpet, kanôn, violīn |
| **-ô** | common domesticated count nouns, where -ô is the best landing — one option among six, not the default |
| **long vowel** (-ō/-ā/-ē/-ī final) | loans whose final vowel is their identity: džezô, çellô, pianô |
| **-ī** | learned Greek/Latin abstractions: liturgī, herēsī, blasfemī |
| **-ēt** | abstract learned nouns: identitēt, kapasitēt |
| **-ūr** | learned/technical nouns: struktūr, dressūr |
| **-iôn** | formal institutional/action nouns: akūzatsiôn, procesiôn |
| **-ômus** | true Nelôxi event/result nouns derived from verbs |
| **-ôr / -ji** | people, roles, agents |
| **-ā** | verbs; source-final -a nouns when warranted |

## How zero-final loans decline (the wrinkle that makes this safe)

A consonant-final loan is **not** a new declension class. It inherits the existing consonant-final
pattern — **Model 1 *kōt* (back-harmony) or Model 2 *mer* (front-harmony)** from module 06. Two
rules from that module govern every case, and both must be applied so a bare-looking loan does not
decline wrong:

**(a) The harmony helper is obligatory in oblique cases.** A zero-final loan is never bare-stem
before a consonant-initial ending. It takes the harmony helper — **-ô-** after a back final vowel,
**-e-** after a front one — exactly as *kōt → kōtôs* and *mer → meres*. This is what saves the
sibilant- and cluster-final loans: *adres* does not form a genitive *adres-s* (illegal); it forms
**adres + helper + -s**. So:

- *plats* "square" (back) → object **platsôn**, genitive **platsôs**, place **platsôl**, goal **platsôlô**
- *adres* "address" (front) → object **adresen**, genitive **adreses**, place **adresel**, goal **adreselä**
- *violīn* (back) → **violīnôn, violīnôs, violīnôl**; *trumpet* (front) → **trumpeten, trumpetes, trumpetel**
- *kanôn* (back) → **kanônôn, kanônôs**; *templ* (front) → **templen, temples**

**(b) Harmony is read from each word's OWN last vowel, never regularized by ending shape.** Two
loans that look like they rhyme can decline with different helpers, and that is correct:

- The last vowel rules, not an earlier one and not the ending's look. *altār* and *breviār* both
  end in *ā* (back), so both take **-ô-**: **altārôs, breviārôs** — the *i* earlier in *breviār*
  does not pull it front. Where a loan's final vowel is back (*a o u ô ā ō ū*) it takes **-ô-/-lô**;
  where front (*ä ö y e i ē ī*) it takes **-e-/-lä**.
- *bulvār* (back) → **bulvārôl**; *avenīd* (front, final *ī*→*i*) → **avenīdel**.

The agent does not choose harmony by taste or by analogy to a similar-looking word — it reads the
last vowel and applies module 06. State the harmony class in the dictionary entry when it is not
obvious from the spelling.

## Keep -ô where it earns its place

Do NOT strip -ô mechanically either — that is the same error inverted. Keep -ô when:
- the final vowel is part of the word's felt identity (*džezô, çellô, pianô, sakrô, violentô*);
- the shape is already canonical and used in the corpus (do not churn settled words);
- removing it would make the word *less* Nelôxi or create a collision;
- it is a fossil/polemic compound whose form carries social history (*fānkellô, babkô, bratkô, dēdkô*).

*barô* vs *bār*: -ô gives the domesticated urban form, zero gives the raw loan. Either is legal;
choose by the register you want, and rule it — do not leave both silently.

## The test to run before assigning any loan ending

> Do not use -ô as the automatic loan-noun ending. Before assigning -ô, test whether the borrowed
> form can enter as: (1) a final-consonant loan, (2) a source-final long-vowel loan, (3) a learned
> suffix form (-ī, -ēt, -ūr, -iôn), (4) a true derived Nelôxi form (-ômus, -ôr, -in, -ām), or (5) a
> raw international scar. Use -ô only when it is the best landing form. Then state the harmony class
> so the word declines by the right *kōt*/*mer* model.

The language stays dirty and loan-heavy. It just stops sounding like every foreign noun walked
through the same -ô machine.
