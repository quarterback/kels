# Modern Anbur — the formal Nelôxian orthography

*Proposed Foundation Module 17 · a full-script overlay on Metropolitan Nelôxi*

**Status:** proposed canon, ready for founder ratification.

Modern Anbur is the formal national orthography of Metropolitan Nelôxi, adapted from the historical Old Permic (Anbur/Abur) alphabet. It is a **script overlay only**: no grammar, vocabulary, pronunciation, morphology, or lexical spelling changes.

Latin remains the everyday, international, computational, and coursebook merge orthography. Modern Anbur is the high/formal written face of the same language: state seals, currency, passports, diplomas, constitutional editions, major monuments, ceremonial headings, formal invitations, public architecture, and selected literary publishing. It is taught nationally and is capable of carrying ordinary prose; it is not decorative pseudo-writing.

The adoption is explicitly an **adoption from the Komi/Permic Vesic tradition**, not a claim that medieval Old Permic was historically Nelôxian and not a claim that Anbur is the script of every Vesic language.

---

## 1 · Governing principles

1. **The Latin coursebook spelling remains the lexical source of truth.**
2. **Modern Anbur preserves Latin orthographic distinctions wherever practical.** It is deliberately less flattening than the Uusatôm Cyrillic overlay.
3. **Historical Old Permic values are retained where they fit Nelôxi cleanly.**
4. **Supplementary Old Permic letters are reassigned systematically for Nelôxi vowels and scar letters that Old Permic did not distinguish in the modern Nelôxian way.**
5. **Length remains visible.** Long vowels take U+0304 COMBINING MACRON.
6. **Palatality remains visible.** `ñ` and `ļ` use U+0300 COMBINING GRAVE on the corresponding Anbur consonant; the grave has historical Old Permic precedent as a palatalization mark.
7. **Modern Anbur is caseless.** Proper names have no uppercase forms.
8. **Dozenal figures remain `0–9 D E`.** Modern Anbur invents no pseudo-historical numeral set.
9. **§47 survives unchanged.** The Anbur sign corresponding to Latin `x` reads /ʃ/ ordinarily and /ks/ in the marked proper-name register, exactly as Latin `x` does.

---

## 2 · Core mapping

### Vowels

| Latin | IPA | Modern Anbur | Unicode source | Modern assignment |
|:---|:---|:---|:---|:---|
| a | /a/ | **𐍐** | U+10350 AN | historical core |
| e | /e/ | **𐍔** | U+10354 E | historical core |
| i | /i/ | **𐍙** | U+10359 I | historical core |
| o | /o/ | **𐍩** | U+10369 O | historical core |
| u | /u/ | **𐍣** | U+10363 U | historical core |
| ä | /æ/ | **𐍱** | U+10371 YAT | modern front-vowel assignment |
| ö | /ø/ | **𐍪** | U+1036A OO | modern front-rounded O assignment |
| y | /y/ | **𐍳** | U+10373 YU | modern front-rounded U assignment |
| ô | /ɤ/ | **𐍨** | U+10368 YERU | modern back-unrounded assignment |
| õ | /ɤ/, word-final | **𐍯** | U+1036F YER | preserves the Latin final-`õ` distinction |

### Long vowels

Length is written with **U+0304 COMBINING MACRON** on the Anbur vowel.

| Latin | Modern Anbur |
|:---|:---|
| ā | **𐍐̄** |
| ē | **𐍔̄** |
| ī | **𐍙̄** |
| ō | **𐍩̄** |
| ū | **𐍣̄** |
| ǟ | **𐍱̄** |
| ȫ | **𐍪̄** |

There is no long `y`, `ô`, or `õ` in the canonical inventory.

### Consonants

| Latin | IPA | Modern Anbur | Unicode source |
|:---|:---|:---|:---|
| b | /b/ | **𐍑** | U+10351 BUR |
| d | /d/ | **𐍓** | U+10353 DOI |
| f | /f/ | **𐍫** | U+1036B EF |
| g | /g/ | **𐍒** | U+10352 GAI |
| h | /h/ | **𐍬** | U+1036C HA |
| j | /j/ | **𐍵** | U+10375 IA |
| k | /k/ | **𐍚** | U+1035A KOKE |
| l | /l/ | **𐍛** | U+1035B LEI |
| m | /m/ | **𐍜** | U+1035C MENOE |
| n | /n/ | **𐍝** | U+1035D NENOE |
| p | /p/ | **𐍟** | U+1035F PEEI |
| r | /r/ | **𐍠** | U+10360 REI |
| s | /s/ | **𐍡** | U+10361 SII |
| t | /t/ | **𐍢** | U+10362 TAI |
| v | /v/ | **𐍞** | U+1035E VOOI |
| x | /ʃ/; /ks/ in §47 proper names | **𐍥** | U+10365 SHOOI |
| ç | /ts/ | **𐍭** | U+1036D TSIU |
| ñ | /ɲ/ | **𐍝̀** | NENOE + U+0300 |
| ļ | /lʲ/ | **𐍛̀** | LEI + U+0300 |

### Geminates

Ordinary doubled consonants remain doubled:

- `tt` → **𐍢𐍢**
- `kk` → **𐍚𐍚**
- `ss` → **𐍡𐍡**
- `nn` → **𐍝𐍝**
- `ll` → **𐍛𐍛**

The canonical interpunct geminate **`l·l`** remains visibly distinct:

- `l·l` → **𐍛·𐍛**

This preserves the Latin lexical distinction rather than flattening it.

---

## 3 · Scar and legacy letters

Modern Anbur preserves the principal Latin scar distinctions instead of collapsing them into the native letter with the same sound.

| Latin scar | Value | Modern Anbur | Unicode source |
|:---|:---|:---|:---|
| ž | /ʒ/ | **𐍕** | U+10355 ZHOI |
| dž | /dʒ/ | **𐍖** | U+10356 DZHOI |
| z | /z/ | **𐍗** | U+10357 ZATA |
| w | /w/ | **𐍮** | U+1036E VER |
| ü | /y/ | **𐍧** | U+10367 YRY |
| œ | /ø/ | **𐍰** | U+10370 YERI |
| legacy š | /ʃ/ | **𐍦** | U+10366 SHCHOOI |

Thus these distinctions survive in Anbur:

- `y` **𐍳** ≠ scar `ü` **𐍧**
- `ö` **𐍪** ≠ scar `œ` **𐍰**
- native `x` **𐍥** ≠ legacy `š` **𐍦**
- `ô` **𐍨** ≠ final `õ` **𐍯**

Rare multigraph scars (`sch`, `sz`) and any future diacritic scars remain **lexeme-ruling territory**; they do not enter the base alphabet automatically.

Reserved Old Permic characters remain available for future rulings rather than being filled merely because they exist. In particular U+10358 DZITA, U+10364 CHERY, U+10372 IE, and U+10374 YA are presently unassigned in core Modern Anbur.

---

## 4 · Capitalization

Old Permic is caseless, and Modern Anbur remains caseless.

Latin:

> **Nelôxia · Kunislinnô · Kēļs Kolēgi**

Modern Anbur:

> **𐍝𐍔𐍛𐍨𐍥𐍙𐍐 · 𐍚𐍣𐍝𐍙𐍡𐍛𐍙𐍝𐍝𐍨 · 𐍚𐍔̄𐍛̀𐍡 𐍚𐍩𐍛𐍔̄𐍒𐍙**

Properness is lexical and contextual, not marked by a special glyph shape. In bilingual documents the parallel Latin line retains normal capitalization.

---

## 5 · Punctuation

Modern prose may use the ordinary punctuation already used by Latin Nelôxi:

`. , ; : ? ! ( ) —`

Three older Anbur habits are retained as high-register options:

- **middle dot `·`** — division between short formal units, names, offices, or inscription clauses;
- **colon `:`** — formal division;
- **apostrophe `'`** — retained where the canonical Latin spelling requires it.

The middle dot is written **without surrounding spaces only inside `l·l`** (`𐍛·𐍛`). As phrase punctuation it is spaced: ` · `.

---

## 6 · Numerals

Modern Anbur uses the existing Nelôxian dozenal figures unchanged:

`0 1 2 3 4 5 6 7 8 9 D E`

Old Permic has no securely attested independent numeral system, so Modern Anbur does **not** invent one.

Examples:

- `10` = twelve
- `100` = 144
- `D` = *on*
- `E` = *jāz*
- `18:00` remains **18:00**

Number words themselves transliterate normally:

- `düzin` → **𐍓𐍧𐍗𐍙𐍝**
- `sôfôr` → **𐍡𐍨𐍫𐍨𐍠**
- `jāz` → **𐍵𐍐̄𐍗**

---

## 7 · Direction of transliteration and normalization

### Latin → Anbur

Transliteration is deterministic for canonical Metropolitan spelling.

Order of operations:

1. normalize the Latin input to Unicode NFC;
2. map `dž` before single letters;
3. map the special geminate `l·l`;
4. map precomposed long vowels to base Anbur vowel + U+0304;
5. map `ñ` and `ļ` to base consonant + U+0300;
6. map the remaining letters;
7. preserve spaces, punctuation, and dozenal figures.

### Anbur → Latin

Reverse transliteration is deterministic **except for capitalization**, because Anbur has no case.

The script deliberately preserves the Latin distinctions that Uusatôm Cyrillic flattens. A dictionary is therefore not normally required to recover `ô/õ`, `y/ü`, `ö/œ`, or `x/š`.

### §47 `x`

Anbur maps the **letter**, not a guessed pronunciation:

- ordinary `x` → **𐍥**, read /ʃ/
- proper-name `x` → **𐍥**, read /ks/ under the same §47 rule

Thus:

> `Nelôxi` → **𐍝𐍔𐍛𐍨𐍥𐍙**

The reader supplies /ks/ because *Nelôxi* belongs to the proper-name register, exactly as in Latin.

---

## 8 · National and institutional forms

| Latin | Modern Anbur |
|:---|:---|
| **Nelô kēļ** | **𐍝𐍔𐍛𐍨 𐍚𐍔̄𐍛̀** |
| **Nelôxia** | **𐍝𐍔𐍛𐍨𐍥𐍙𐍐** |
| **Kunislinnô** | **𐍚𐍣𐍝𐍙𐍡𐍛𐍙𐍝𐍝𐍨** |
| **Kēļs Kolēgi** | **𐍚𐍔̄𐍛̀𐍡 𐍚𐍩𐍛𐍔̄𐍒𐍙** |
| **Uusatôm** | **𐍣𐍣𐍡𐍐𐍢𐍨𐍜** |
| **Tantsika** | **𐍢𐍐𐍝𐍢𐍡𐍙𐍚𐍐** |
| **Māmeli** | **𐍜𐍐̄𐍜𐍔𐍛𐍙** |
| **Spalôt** | **𐍡𐍟𐍐𐍛𐍨𐍢** |
| **Ragūz** | **𐍠𐍐𐍒𐍣̄𐍗** |

---

## 9 · Corpus samples

These are existing Metropolitan Nelôxi forms and sentences from the coursebook and reader corpus, rendered through the mapping above.

### Daily language

**1. Nelô kēļ** — “the Nelôxi language”  
**𐍝𐍔𐍛𐍨 𐍚𐍔̄𐍛̀**

**2. Moin!** — “Hello!”  
**𐍜𐍩𐍙𐍝!**

**3. Kui sä?** — “How are you?”  
**𐍚𐍣𐍙 𐍡𐍱?**

**4. Mä äb saipā.** — “I don’t understand.”  
**𐍜𐍱 𐍱𐍑 𐍡𐍐𐍙𐍟𐍐̄.**

**5. Mis prēu?** — “How much?”  
**𐍜𐍙𐍡 𐍟𐍠𐍔̄𐍣?**

**6. Otelô, kus?** — “Where is the hotel?”  
**𐍩𐍢𐍔𐍛𐍨, 𐍚𐍣𐍡?**

**7. Mä sōv kafē.** — “I’d like coffee.”  
**𐍜𐍱 𐍡𐍩̄𐍞 𐍚𐍐𐍫𐍔̄.**

**8. Um jôvā sūr.** — “It’s very good.”  
**𐍣𐍜 𐍵𐍨𐍞𐍐̄ 𐍡𐍣̄𐍠.**

**9. Lǟdô jôvā.** — “Go well.”  
**𐍛𐍱̄𐍓𐍨 𐍵𐍨𐍞𐍐̄.**

**10. Demā!** — “See you tomorrow.”  
**𐍓𐍔𐍜𐍐̄!**

### Coursebook sentences

**11. Mä lugē livrôn.** — “I read the book.”  
**𐍜𐍱 𐍛𐍣𐍒𐍔̄ 𐍛𐍙𐍞𐍠𐍨𐍝.**

**12. Livrôn mä lugē.** — “The book I read.”  
**𐍛𐍙𐍞𐍠𐍨𐍝 𐍜𐍱 𐍛𐍣𐍒𐍔̄.**

**13. Demā mä lǟdô markôtôlô.** — “Tomorrow I go to the market.”  
**𐍓𐍔𐍜𐍐̄ 𐍜𐍱 𐍛𐍱̄𐍓𐍨 𐍜𐍐𐍠𐍚𐍨𐍢𐍨𐍛𐍨.**

**14. Mä juô lēten.** — “I drink the milk.”  
**𐍜𐍱 𐍵𐍣𐍨 𐍛𐍔̄𐍢𐍔𐍝.**

### Calibration corpus

**15. Pôjātūļ ja päikü diskutai, ken ūli fortmi.**  
“The North Wind and the Sun argued over which of them was the stronger.”  
**𐍟𐍨𐍵𐍐̄𐍢𐍣̄𐍛̀ 𐍵𐍐 𐍟𐍱𐍙𐍚𐍧 𐍓𐍙𐍡𐍚𐍣𐍢𐍐𐍙, 𐍚𐍔𐍝 𐍣̄𐍛𐍙 𐍫𐍩𐍠𐍢𐍜𐍙.**

**16. Pôjātūļ tūļāi fort, agā reisāji äb votai mäntlôn maha.**  
“The North Wind blew hard, but the traveler did not take the cloak off.”  
**𐍟𐍨𐍵𐍐̄𐍢𐍣̄𐍛̀ 𐍢𐍣̄𐍛̀𐍐̄𐍙 𐍫𐍩𐍠𐍢, 𐍐𐍒𐍐̄ 𐍠𐍔𐍙𐍡𐍐̄𐍵𐍙 𐍱𐍑 𐍞𐍩𐍢𐍐𐍙 𐍜𐍱𐍝𐍢𐍛𐍨𐍝 𐍜𐍐𐍬𐍐.**

**17. Päikü nīrai lǟmi, ja reisāji votai mäntlôn maha.**  
“The Sun shone warm, and the traveler took the cloak off.”  
**𐍟𐍱𐍙𐍚𐍧 𐍝𐍙̄𐍠𐍐𐍙 𐍛𐍱̄𐍜𐍙, 𐍵𐍐 𐍠𐍔𐍙𐍡𐍐̄𐍵𐍙 𐍞𐍩𐍢𐍐𐍙 𐍜𐍱𐍝𐍢𐍛𐍨𐍝 𐍜𐍐𐍬𐍐.**

**18. Niimôdõ päikü ūli fortmi kui pôjātūļ.**  
“So the Sun was the stronger of the two.”  
**𐍝𐍙𐍙𐍜𐍨𐍓𐍯 𐍟𐍱𐍙𐍚𐍧 𐍣̄𐍛𐍙 𐍫𐍩𐍠𐍢𐍜𐍙 𐍚𐍣𐍙 𐍟𐍨𐍵𐍐̄𐍢𐍣̄𐍛̀.**

**19. Kôg inim syndā līberü ja ühüvāgô nimpundôs ja rētôs.**  
“All human beings are born free and equal in dignity and rights.”  
**𐍚𐍨𐍒 𐍙𐍝𐍙𐍜 𐍡𐍳𐍝𐍓𐍐̄ 𐍛𐍙̄𐍑𐍔𐍠𐍧 𐍵𐍐 𐍧𐍬𐍧𐍞𐍐̄𐍒𐍨 𐍝𐍙𐍜𐍟𐍣𐍝𐍓𐍨𐍡 𐍵𐍐 𐍠𐍔̄𐍢𐍨𐍡.**

**20. Ne um pôhjôk ja isülivrôk, ja ne pidā elä teinütõk ühüvôrks.**  
“They are endowed with reason and conscience, and should live toward one another in brotherhood.”  
**𐍝𐍔 𐍣𐍜 𐍟𐍨𐍬𐍵𐍨𐍚 𐍵𐍐 𐍙𐍡𐍧𐍛𐍙𐍞𐍠𐍨𐍚, 𐍵𐍐 𐍝𐍔 𐍟𐍙𐍓𐍐̄ 𐍔𐍛𐍱 𐍢𐍔𐍙𐍝𐍧𐍢𐍯𐍚 𐍧𐍬𐍧𐍞𐍨𐍠𐍚𐍡.**

---

## 10 · Institutional usage

The standard division is:

### Latin Nelôxi
- everyday writing
- coursebook and dictionary headwords
- software source and machine-readable canon
- international trade
- ordinary newspapers and correspondence
- signage where maximum cross-border legibility is the priority

### Modern Anbur
- state seal and arms
- currency
- passports and citizenship documents
- constitutional and treaty presentation editions
- diplomas and university ceremonial documents
- courts and Diet chamber inscriptions
- monuments and memorials
- major railway, port, and government architecture
- formal book titles and literary editions
- national ceremonies

Parallel Latin + Anbur is normal on high-value public objects. Anbur-only prose is valid and readable, not merely ornamental.

---

## 11 · Governance

- This file governs **Metropolitan Nelôxi only**.
- It does not automatically impose Anbur on Saharannaise, Congolaise, Meralian, Verdenese, Sarmatian, Neloxian Arabic, or other Nelosphere languages and standards.
- Komi Old Permic remains Komi's own historical and modernized written tradition. Modern Nelôxian Anbur is a related but separately standardized adaptation.
- The **coursebook remains the merge target**. Anbur forms are generated from canonical Latin spelling and do not become separate dictionary headwords.
- The mapping table is closed after ratification. A new mapping requires a Kēļs Kolēgi ruling.
- No Anbur spelling may be used to justify a change in pronunciation or Latin canonical spelling.

---

## 12 · Implementation note

The repository should pair this module with a deterministic transliterator:

`tools/transliterate_anbur.py`

Recommended generated uses include:

- Anbur display field in the live dictionary;
- Anbur toggle on coursebook/reader pages;
- automatic rendering of state names and headings;
- corpus regression tests ensuring every canonical Metropolitan headword can be rendered.

The transliterator should fail loudly on an unmapped alphabetic character rather than silently inventing an Anbur spelling.

