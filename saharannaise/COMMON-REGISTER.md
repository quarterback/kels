# The Common Register — the shared spine of Nelôxi's four standards

*The agreement that makes Metropolitan, Saharannaise, Congolaise, and Maré Nelôxi one language.*

Nelôxi is pluricentric. The coursebook is the **Metropolitan** standard; Saharannaise is
the **Atlantic** standard; Congolaise is the **River** standard; Maré is the **Oceanic**
standard. Their vocabularies diverge heavily and by design — that divergence is not a
failure of unity, it is what a real pluricentric language looks like
(Brazilian *ônibus* / European *autocarro*, both correct). What binds them into one
language is this document: a **shared grammar** and a **shared orthographic agreement**,
plus a **tag convention** for bridging the four lexicons. It is the Acordo Ortográfico of
this language — it standardizes the spine, not the word-list.

## 1 · The shared grammar (invariant across all four standards)

All four standards run the identical grammatical skeleton. No seat may alter it; a change
here is a change to the language itself, ruled by the Kēļs Kolēgi in consultation with the
other standard seats.

- No verb agreement. Strict SVO. Pre-verbal negation *äb*. Bare-stem imperative; hortative
  *-m*. Agglutinative case with vowel harmony.
- The productive derivational set, unchanged in all four: **-ôr/-õr** (agent), **-in, -mus/-mys,
  -ū, -stā, -ldā, -ām/-äm, -tū/-ty**, causative **-tā**, comparative **-mi**.
- Dozenal (base-12) numbers. 24-hour clock. Low German calendar.

A word from any standard declines by these rules. This is why a Saharan root such as
*žəml* can take *-ôr* and become *žəmlôr* and be, grammatically, an ordinary Nelôxi noun.
The grammar does not know or care which quarry a root came from — that is the whole point.

## 2 · The shared orthographic agreement

One archive script serves all four standards. The Metropolitan rules (ô [ɤ]; x = [ʃ], or [ks]
in proper nouns per §47; macrons for length; foreign scars worn openly, the *flœzī/dž*
class) are the base. Saharannaise, Congolaise, and Maré each add a **bounded extension** for their source phonetics —
and nothing beyond the ruled tables:

| Feature | Rule | Applies to |
|:---|:---|:---|
| **ô / ā flattening** | Vowels flatten to forward-stressed **ô** or long **ā**; *â/î/û → ā/ī/ū* or *ô* (mainland §63) | both, dominant in Saharannaise |
| **Final -a compression** | Hassaniya final *-a* drops or compresses to zero (*ḥamāda → xamād*, *nāga → nāg*) | Saharannaise |
| **Article agglutination** | Arabic *al-/el-* welds as a fixed prefix (*al-ʿuyūn → lāyūn*); Zenaga *a-* agglutinates (early) or drops (late) | Saharannaise |
| **ʿayn elision** | Arabic *ʿayn* (ʿ) drops **before a full vowel**, coloring/lengthening it (*ʿerg → erg*, *ʿaṭsh → aṭx*). **Retained before a glide**: when a short high vowel syncopates and brings ʿayn against *y/w*, it holds (*al-ʿuyūn → ʿyūn → **Ləʿyūn***). | Saharannaise |
| **§47 friction** | The back-fricative set **ḥ, š, kh** all → **x** ([ks] formal, [ʃ] in *š*-speech): *ḥamāda → xamād*, *šarg → xarg*, *khū → xū* | shared rule, heavy use in Saharannaise |
| **Qaf → g** | Hassaniya uvular *q* [g] is written **g** (*sūq → sūg*, *qamar → gamar*, *qāfila → gāfila*) | Saharannaise |
| **Emphatic scars** | The full emphatic series **ṭ ṣ ḍ ẓ** preserved, never mapped | Saharannaise |
| **Scar inventory** | Adds **ə** (schwa), **ž**, **ġ** (ghayn), **ṭ ṣ ḍ ẓ** to the mainland letters | Saharannaise |
| **No long ō** | A non-mainland long-o is written **ô**; the agent suffix stays exactly **-ôr** | all standards |
| **Congolaise scars** | Adds **ɓ ɗ ŋ** plus the shared **ə**; prenasal digraphs remain digraphs | Congolaise, by `../congolaise/CONFLUENCE-PRINCIPLE.md` |
| **Maré digraph scars** | Adds no single-letter diacritics; permits fixed Maré/Nengone digraphs **hm hn hng wh hy sh xh dr th tr ng** and apostrophe-marked **c' k' t'** | Maré, by `../mare/orthography.md` |

The extension is closed: a submission may not invent orthography outside this table or the
linked Congolaise and Maré amendment tables without a Register ruling.

## 3 · The tag convention (how the four lexicons bridge)

The standards keep **separate lexicons**, each counted on its own terms — the Metropolitan
word-list in the coursebook, the Atlantic word-list under `saharannaise/`, the River word-lists
under `congolaise/`, and the Oceanic word-list under `mare/`. They are bridged, not merged, by
a region tag on any entry whose standing is not universal:

- **(Metr.)** — Metropolitan-only form (the mainland member of a doublet).
- **(Sah.)** — Saharannaise-only form.
- **(Cong.)** — Congolaise-only form.
- **(Maré)** — Maré-only form.
- **(Sah.→Metr.)** — a back-flow loan: a Saharan word that has drifted into the metropolitan
  lexicon as a prestige maritime term. It becomes Metropolitan canon **only** when the Rector
  merges it into the coursebook; the tag marks candidacy, not automatic promotion.
- *(untagged)* — common across the standards that use it.

A **doublet** is one meaning carried by a tagged pair across standards — the Level-1
asymmetry of `saharannaise.md` §2. Example: "wadi/channel" is **kanā** (Metr.) ↔ **sāgī**
(Sah.). The clerk writes one; the worker says the other; all tagged forms are canon, in their own seat.

The tags produce a federated roll-up, the **Common Vocabulary (VOC)** in `VOC.md` — the
IILP's output for this language. Each standard keeps its own national list (the coursebook
= Metropolitan VON; the Saharannaise batches = Atlantic VON; Congolaise = River VON; Maré = Oceanic VON); the VOC aggregates them into
one view of every doublet, gap, and back-flow candidate. It is derived from the standard VONs,
never a source of truth itself.

## 4 · Governance — four seats, none supreme

- The **Kēļs Kolēgi** (the College of Language), headed by the **Rector**, governs the
  Metropolitan standard and the coursebook.
- The **Kēļs Dīwān** (the Saharan Register), headed by the **Amīn** (the Dean), governs
  Saharannaise and its lexicon files.
- The **Kēļs Penc** (the Forum), governs Congolaise and its lexicon files.
- The **Maré Register** governs Maré and its lexicon files.
- **The shared spine (§1–§2) is joint.** No seat changes the grammar or the
  orthographic agreement alone; those amendments are logged in the common register and in the
  affected standard's doctrine.
- Vocabulary is **each seat's own business.** Each seat may coin, reroot, and archive
  words in its own standard without the other seats' approval, provided every standard obeys
  the shared spine.

This is the Lisbon/Brasília settlement: four academies, one orthographic agreement, divergent
dictionaries, one language.
