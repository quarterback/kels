# The Common Vocabulary (VOC)
### *Vocabulário Ortográfico Comum* — the federated index of Nelôxi's two standards

The federation layer. Each standard keeps its own national list — the **Metropolitan VON**
(the coursebook) and the **Atlantic VON** (the Saharannaise batches). This VOC does not
replace them; it **rolls them up** into one view so the state of the federation is legible
at a glance: where the two standards agree, where they diverge into doublets, where one has
a word the other lacks, and which Saharan terms are drifting back toward the mainland.

This is the IILP's job in the Lusophone world, done here. It is **hand-maintained** while
Saharannaise is small; once it grows it should be script-generated from the two VONs, like
`data/*`. Governance and the tag convention live in `COMMON-REGISTER.md`; this file is the
output that convention produces.

*Status tags: **doublet** = both standards, different roots · **shared** = one form serves
both (usually a borrowed Saharan referent) · **Metr-gap** = mainland has no word; Saharan
fills it · **Sah-internal** = two Saharannaise words split one concept · **back-flow** =
Saharan term drifting toward metropolitan canon (enters by Rector merge only).*

---

## 1 · Doublets — one concept, a root in each standard

The core of the asymmetry: the clerk writes the left column, the dockworker says the right.

| Concept | Metropolitan (VON) | Saharannaise (VON) | Domain |
|:---|:---|:---|:---|
| tea | tē | **atāy** | food |
| milk | juht | **ləbn** | food |
| water | veç | **aman / lma** | food |
| bread | pa | **ġrum** | food |
| meat | karn | **lxam** | food |
| salt | sōla | **məlx** | food |
| mother | mǟr | **umm** | kin |
| father | pǟr | **bā** | kin |
| son, boy | poig | **wəld** | kin |
| daughter, girl | tytār | **bənt** | kin |
| brother | veļ | **xū** | kin |
| sister | sisār | **əxt** | kin |
| man, husband | mēs | **rāžəl** | kin |
| woman, wife | nān | **mra** | kin |
| child | läpx | **žāhəl** | kin |
| house | barô | **axam** | dwelling |
| market | markôt | **sūg** | market |
| money | rā | **flūs** | market |
| to buy | komprā | **xrā** | market |
| sun | päikü | **xəms** | day |
| moon | kū | **gamar** | day |
| star | estēl | **nəžma** | day |
| night | nahtô | **līl** | day |
| day, daytime | pǟvô | **nhār** | day |
| morning | matī | **ṣbāx** | day |
| evening, sunset | vespôr | **məġrəb** | day |
| thirst | jān | **aṭx** | day |
| shade / shadow | çeñ | **ẓəl** | day |
| cloud | pilv | **ṣxāb** | weather |
| cold (weather) | kylm | **barād** | weather |
| wadi / channel | kanā | **sāgī** | terrain |

## 2 · Metropolitan gaps — Saharannaise fills a missing referent

The mainland has no native word because it has no such thing. The Saharan term is the only
one available, so it functions across both standards — and this is the channel through
which back-flow begins.

| Concept | Saharannaise | Status | Domain |
|:---|:---|:---|:---|
| caravan, trade convoy | **gāfila** | Metr-gap · back-flow | market |
| tent (mobile home) | **xəyma** | Metr-gap | dwelling |
| waterskin | **girba** | Metr-gap · back-flow | market |
| tribe, extended kin | **gabīla** | Metr-gap | kin |
| dates (palm fruit) | **tamar** | Metr-gap | food |
| couscous | **səksū** | Metr-gap | food |
| sweetened camel milk | **zrīg** | Metr-gap | food |
| sandstorm, haboob | **ṭāyf** | Metr-gap · back-flow | weather |
| flash flood | **sayl** | Metr-gap · back-flow | weather |
| coastal / Atlantic fog | **ġabīn** | Metr-gap · back-flow | weather |
| erg, sand sea | **erg** | Metr-gap · back-flow | terrain |
| hamada, rock plateau | **xamād** | Metr-gap | terrain |
| sebkha, salt pan | **sabx** | Metr-gap | terrain |
| guelta, rock pool | **galt** | Metr-gap | terrain |

*(and the rest of the Batch-1 terrain/livestock inventory — the desert's own referents,
all effectively Metr-gaps until a mainland need pulls them across.)*

## 3 · Saharannaise-internal doublets

Where the Atlantic standard splits one concept across its own two source strata — the
substrate/superstrate contrast that mirrors the mainland's Livonian-under-loans shape.

| Concept | Substrate (Zenaga) | Superstrate (Hassaniya) | Note |
|:---|:---|:---|:---|
| water | **aman** (deep, ritual, the substance) | **lma** (everyday, drinking) | Berber vs Arabic |
| dwelling | **axam** (settled house) | **xəyma** (mobile tent) | sedentary vs nomad |

## 4 · Back-flow register — merged & queued

Saharan terms drifting into metropolitan maritime vocabulary. Each enters coursebook canon
only by an explicit Rector merge, at which point it leaves the queue, **nativizes** (sheds
its Saharan scars), and gains a `(Sah.→Metr.)` tag in the mainland VON.

**Proposed to the Kēļs Kolēgi** (nativized forms the loans would take on entry; adoption is
the mainland's call, per `COMMON-REGISTER.md` §4 — Saharannaise does not edit the coursebook):

| Saharannaise | Proposed Metropolitan | Gloss |
|:---|:---|:---|
| **ġabīn** | *gabīn* | sea-fog, coastal fog-bank (ġ→g) |
| **gāfila** | *gāfila* | convoy, caravan (would fill a mainland gap) |
| **ṭāyf** | *tāyf* | sea-haze, dust-fog (ṭ→t) |

**Also queued:** **sayl** (flash flood) · **erg** (sand sea) · **girba** (waterskin) ·
**nəžma** (star, for navigation).

---

*Sources: Metropolitan forms are coursebook canon; Saharannaise forms are archived in
`lexicon-B-*` (Batch 1, terrain), `lexicon-C-*` (Batch 2, domestic core), `lexicon-A-*`
(Batch 3, admin & maritime — a further ~30 doublets: durô↔marsā, xip↔markab, kalā↔xūt,
handlôji↔tāžər, sīgel↔xātam, aktô↔warga, rīgô↔dawla, …), `lexicon-D-*` (Batch 4,
material-culture / heat-craft — dress, shelter, and evaporative cooling: dərrāʿ, tāgəlmust, gaṣba,
tazəqqa, zīr, …), and `lexicon-E-*` (Batch 5, caravan / faith / the guest-law: gāfla, dlīl, əddīn,
mrābəṭ, ḍiyāfa, əl-ḥagg, …). 149 Saharannaise headwords across five batches, federated here against
their mainland counterparts.*
