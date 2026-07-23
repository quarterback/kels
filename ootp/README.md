# OOTP world file — the Nelôxi world

`world_default_neloxi.xml` is an OOTP `world_default.xml` with the **eleven sovereign
nations** of the settled world layer (`../world/*.md`) built in, and the real-world
places they are based on removed or carved. `build_world.py` regenerates it from a
base file, so the whole edit is reproducible — rerun it against a fresh base to tweak
the mapping.

**Built for the "Enhanced Complete World Names" base** (Korean-localized, a richer
Latino ethnicity table, and it ships with `names.xml` + `namescustom.xml`). Player
**name generation is driven by each nation's ethnicity (`etid`) mix** — there is no
separate "language" field in OOTP; the name files key every name by `lid`, and `lid`
= the ethnicity id. So each new nation's ethnicity blend was chosen to read
culturally (see the naming table below). Use this world file **together with** that
pack's `names.xml`/`namescustom.xml` so the ethnicities resolve to the intended name
pools.

**To install:** back up the `world_default.xml` your OOTP loads when creating a new
game, then replace it with this file (renamed to `world_default.xml`), keeping the
`names.xml`/`namescustom.xml` alongside. It only takes effect for newly created games.

## The eleven nations

| id | Nation | Abbr (flag) | Capital | Pop | bbqual | Continent |
|---|---|---|---|---|---|---|
| 260 | **Nelôxia** | NEL | Kunislinnô | 76,000,000 | 2 | Europe |
| 261 | **Skaria** | SKA | Göteborg¹ | 9,300,000 | 1 | Europe |
| 262 | **Atlanta** | ATL² | Fôntāna | 2,800,000 | 2 | Africa |
| 263 | **Adrāra** | ADR | Atar | 1,900,000 | 1 | Africa |
| 264 | **Soninka & Toro** | SOT | Ndar | 4,200,000 | 1 | Africa |
| 265 | **Valdória** | VAL | Portô Venla | 34,000,000 | 2 | South America |
| 266 | **Meridian States** | MER | Esperanza | 4,300,000 | 3 | South America³ |
| 267 | **Sarmatia**⁴ | SAR | Caffa | 29,000,000 | 1 | Europe |
| 268 | **Zaryanova**⁵ | ZAR | Gannibal | 29,863,010 | 4 | Asia |
| 269 | **Tarun**⁶ | TAR | Tashkent | 68,000,000 | 1 | Asia |
| 270 | **Qazania**⁶ | QAZ | Kazan | 8,000,000 | 1 | Europe |

The **Abbr** column is the flag key — OOTP looks for a flag file per nation
abbreviation, so you can source one flag each for NEL, SKA, ATL, ADR, SOT, VAL, MER,
SAR, ZAR, TAR, QAZ.

¹ Skaria's capital is founder-open in the lore; Göteborg is a placeholder (largest
city in its territory).
² The lore-ratified sport code (`saharannaise/toponymy.md`).
³ OOTP requires one continent per nation; the legislative capital Esperanza puts it in
South America.
⁴ **Sarmatia** (the People's Republic of Sarmatia), founder-ratified — formerly East
Neloxia, the independence-era name; demonym Sarmat (`../world/sarmatia.md`). Built to
the ratified corridor: Crimea + Kherson/Zaporizhzhia land bridge, the Caucasus gate
(Ingushetia stays Russian per the doc), western Georgia, Astrakhan/Kalmykia/Orenburg,
the west Kazakh oblasts, Balkan/Ahal (with the Asgabat city-state), and the
Herat–Makran reach (Herat, Farah, Nimruz, Sistan-e Baluchestan, Baluchistan). The
population is a working number — the doc gives none.
⁵ Per `../world/zaryanova.md`: the Black-majority Pacific great power spanning the
whole Russian Far East — **Primorsky, Khabarovsk, Kamchatka, Sakhalin & the Kurils,
Magadan, the Jewish AO, and Chukotka** (the doc's UTC+9–+13 / 180°-meridian span).
Capital **Gannibal** (the purpose-built city — here the renamed Yuzhno-Sakhalinsk);
largest city **Pushkin** (renamed Vladivostok, pop boosted); **Vorota**, the DPRK
gateway town, added at the Khasan border point. The Jewish AO keeps its base name for
now (the doc's "provincial cities are being renamed" is open work). bbqual 4 reflects
the founding culture.
⁶ Per `../world/neighbor-states.md`. Tarun's capital is a Tashkent placeholder (the
doc names none) and its population a working number; Tajikistan stays independent.
Qazania = Tatarstan + Bashkortostan, capital Kazan, demonym Qazani, ~8M. Kazakhstan,
Uzbekistan, Turkmenistan and Kyrgyzstan are fully partitioned between Tarun and
Sarmatia; China loses Xinjiang.

`bbqual` (0–5 baseball quality) values are judgment calls — edit the NATION lines to
taste.

## Naming — how each nation generates player names

Ethnicity mix per nation (the `etid`s that drive `names.xml`), chosen to read
culturally. None require new name data; the enhanced pack's better Latino names reach
the Hispanic-blended nations automatically.

| Nation | Language (lore) | Ethnicity blend (dominant → minor) |
|---|---|---|
| Nelôxia | Metropolitan Nelôxi | Estonian/Latvian/Lithuanian + Polish/Russian/Belorussian/Ukrainian + German/Hungarian/Romanian/Finnish/Danish |
| Skaria | *(Nordic — not Nelôxi)* | Swedish/Danish/Finnish/Norwegian |
| Atlanta | Saharannaise | North-African + Pan-Arab + Islam-African + a Nelôxian-settler trace |
| Adrāra | Saharannaise | Mauretanian + North-African + Senegalese |
| Soninka & Toro | Congolaise | Senegalese + Mauretanian + Malian |
| Valdória | Verdenese | Arg-Italian + Brazilian + Spanish + Portuguese/German/Polish/Ukrainian/Italian + African-American (Ebony Pearl) + Native-American (Guaraní) |
| Meridian States | Maré | Spanish/French/French-Carib + Bermudan/Cape-Verdean/SEA-Chinese/IO-Muslim/New-Caledonian/Wallisian/English |
| Sarmatia | the East fork (Idā) | Georgian/Russian/Turkish/Ukrainian/Armenian + Persian/Afghani/Pakistani/Turkmen |
| Zaryanova | *(English + Russian creole)* | **Zaryan** (custom ethnicity 233) 74% + Russian/Korean/Chinese/Japanese/SE-Asian |
| Tarun | *(Turkic)* | Central-Asian + Uighur + Turkish + Turkmen + Russian |
| Qazania | *(Turkic/Tatar)* | Turkish + Russian + Pan-Islamic + Turkmen |

Seven of the eleven speak a Nelôxi standard (Atlanta and Adrāra share Saharannaise, so
that's all six standards/forks); the four that don't — Skaria, Zaryanova, Tarun,
Qazania — are exactly the four the lore marks as non-Nelôxi.

### Zaryanova's custom name pool (ethnicity 233)

No real ethnicity produces Zaryanova's Afro-Russian creole ("Marcus Volkov", "Pavel
Kuznetsov"), so it gets a **custom ethnicity, id 233 ("Zaryan")**, added to the world
file, and a matching **name pool under `lid` 233 injected into `names.xml`** by
`add_zaryan_names.py`. The names come from the founder's generator
(`quarterback/tennis-team-manager` `generators/zaryan_names.py`): the Russianized /
heritage given names it emits (Maks, Pavel, Mikhail, Isaiah, Solomon, Coretta, …) and
the Russified surnames from its meaning dictionary (Kuznetsov, Volkov, Chernov, Belov,
Melnikov, …) plus a few untranslated heritage surnames (Brooks, Jefferson, Washington)
for the modern/urban register. **This makes the modified `names.xml` a required
companion to the world file** — ship both together, or Zaryanova's players have no name
pool. Regenerate with `python3 ootp/add_zaryan_names.py <names.xml> <out.xml>`.

## What was carved or removed

- **Nelôxia** — nine regions carved from Russia (Karelia, Leningrad, Kaliningrad),
  Estonia, Latvia, Lithuania, Poland, Belarus, Slovakia (Prešov), Ukraine
  (Transcarpathia, Odessa), Romania (the arc counties), Bulgaria (Dobrich), Hungary,
  Austria, Italy (Friuli), Slovenia, Croatia (Dalmatia). Marquee cities renamed per the
  gazetteer (Kunislinnô, Tantsika, Stetīn, Uusatôm, Kôstônç, Māmeli, Vīpôri, Petrôsô,
  Gräts, Triest, Spalôt, Ragūz, Marīsô, …). Bosnia is modeled only as its two entities,
  so Region 9's Bosnian cantons couldn't be carved.
- **Skaria** — the ratified Danish/Norwegian/Swedish/Finnish subdivisions (Innlandet as
  Hedmark+Oppland; Åland absent from the base, omitted).
- **Atlanta** replaces Western Sahara; canon waypoint towns added.
- **Adrāra + Soninka & Toro** replace Mauritania (north/south split), plus Senegal's
  Saint-Louis and Matam and the town of Bakel (→ Bakəl); Atar and Chinguetti reclaimed
  from a misfiling inside Algeria.
- **Valdória** — Rio Grande do Sul + Santa Catarina (Brazil), Rocha (Uruguay),
  Corrientes/Misiones/Formosa/Salta/Jujuy (Argentina), Itapúa/Ñeembucú (Paraguay),
  Tarija/Potosí (Bolivia), Antofagasta (Chile, as Litorāl). Porto Alegre → Portô Venla,
  Pelotas → Santa Laura; Koinīnia added.
- **Sarmatia** — the corridor from Crimea to the Makran (see note ⁴).
- **Zaryanova** — the whole Russian Far East, carved from real oblasts (see note ⁵).
- **Tarun** — the unified Turkic bloc; **Qazania** — Tatarstan + Bashkortostan. The four
  Central-Asian donor nations are fully partitioned between Tarun and Sarmatia and
  their records removed; China loses Xinjiang.
- **Meridian States** absorbs Bermuda, French Guiana (→ Esperanza), Saint-Pierre &
  Miquelon, St. Helena, São Tomé & Príncipe, Mayotte, Wallis & Futuna and New Caledonia,
  plus the Canary Islands (Spain), Corsica (France), and **Magau** (Macau's Aomen state,
  renamed). The Macau nation record is removed.
- **US statehood for the four territories.** In this base Puerto Rico, the Northern
  Marianas, **Guam, and the US Virgin Islands are all separate nations** — each is
  dissolved into a single US state (abbrs PR, MP, GU, VI) inside The United States. US
  population +4.07M (~316M), now **55 states**, and each "US TERRITORY: X" region is
  repointed from the old nation to the new state.
- **Appalachia** — a canonical US state of this universe. The base models it as state
  167 "West Virginia"; it's renamed **Appalachia** (abbr AP) and gains its **44 border
  towns** (Asheville, Boone, Knoxville, Chattanooga, Bristol, Kingsdale, Hazard,
  Pikeville, Abingdon, …) moved in by city id from NC/KY/VA/TN/GA — moved, not copied,
  so no city is duplicated.
- **Kuwait** and **Morocco** untouched (sovereign, aligned, never absorbed).
- Donor nations keep their capitals and remaining states; their `pop` attributes were
  reduced by what moved.
- *Note:* The United States keeps `use_hardcoded_ml_player_origins="1"`, so OOTP
  generates US-born players from its built-in city distribution; the annexed territory
  cities exist on the map and any player explicitly from them is American, but they are
  not added to that hardcoded birth weighting.

## ID policy

New nation ids 260–270, new state ids 9101+, new city ids 150001+ — all above the base
file's maxima (252 / 3400 / 95477), so every new id is unique. Moved states and cities
keep their original ids (their old owners are gone, so no collisions). All
`REGION_NATION` league-pool references to absorbed nations were remapped to their
successors and deduplicated; the new nations were added to the appropriate geographic
pools (Europe/Africa/South America/Asia at-Large, Far East, Eurasia, Former Soviet
Union, etc.). **The output has zero duplicate ids of any kind, every capital resolves,
and no dangling region/second-nation references** beyond none.

## Base-file repairs

- **Cameroon, Gambia, and Bolivia** ship with broken capital references (capid / CAPITAL
  pointing at a city not in the nation). Repaired to Yaoundé, Banjul, and Bolivia's La
  Paz respectively.
