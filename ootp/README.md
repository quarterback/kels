# OOTP world file — the Nelôxi world

`world_default_neloxi.xml` is an OOTP `world_default.xml` with the eight sovereign
nations of the settled world layer (`../world/*.md`) built in, and the real-world
places they are based on removed or carved. `build_world.py` is the script that
generated it from the base copy of the file (so the whole edit is reproducible —
rerun it against a fresh base if you ever want to tweak the mapping).

**To install:** back up the `world_default.xml` your OOTP loads when creating a new
game, then replace it with this file (renamed to `world_default.xml`). It only
takes effect for newly created games.

## The eight nations

| id | Nation | Abbr | Capital | Pop | bbqual | Continent | States |
|---|---|---|---|---|---|---|---|
| 260 | **Nelôxia** | NEL | Kunislinnô | 76,000,000 | 2 | Europe | the nine ratified regions of `boundaries.md` |
| 261 | **Skaria** | SKA | Göteborg¹ | 9,300,000 | 1 | Europe | the 21 seceded Nordic subdivisions |
| 262 | **Atlanta** | ATL² | Fôntāna | 2,800,000 | 2 | Africa | Pūnkanā, Kuldjôg |
| 263 | **Adrāra** | ADR | Atar | 1,900,000 | 1 | Africa | the Bidhan north of old Mauritania + Adrār |
| 264 | **Soninka & Toro** | SOT | Ndar | 4,200,000 | 1 | Africa | Wālo, Futa, Gajāga |
| 265 | **Valdória** | VAL | Portô Venla | 34,000,000 | 2 | South America | the 13 provinces of `verdenese/toponymy.md` |
| 266 | **Meridian States** | MER | Esperanza | 4,300,000 | 3 | South America³ | one state per member territory |
| 267 | **East Neloxia**⁴ | ENX | Caffa | 29,000,000 | 1 | Europe | the Black Sea→Makran corridor of `world/east-neloxia.md` (30 states) |
| 268 | **Zaryanova**⁵ | ZAR | Gannibal | 29,863,010 | 4 | Asia | Gannibal (Sakhalin & Kurils), Zephyria Oblast, Primorsky, Khabarovsk, Kamchatka, Magadan, Chukotka |
| 269 | **Tarun**⁶ | TAR | Tashkent | 68,000,000 | 1 | Asia | Kazakhstan (less the East Neloxian west), Uzbekistan, Turkmenistan (less Balkan/Ahal), Kyrgyzstan, Xinjiang |
| 270 | **Qazania**⁶ | QAZ | Kazan | 8,000,000 | 1 | Europe | Tatarstan + Bashkortostan (Idel-Ural realised) |

¹ Skaria's capital is founder-open in the lore; Göteborg is a placeholder (biggest
city in its territory).
² The lore-ratified sport code (`saharannaise/toponymy.md`).
³ OOTP requires one continent per nation; the legislative capital Esperanza puts it
in South America.
⁴ Name provisional per `../world/east-neloxia.md` (candidates: Šaraya, Kervania,
Colchia/Kôlxônô, Sarmatia, Alania) — a one-line rename when the founder rules.
Built to the ratified corridor territory: Crimea + Kherson/Zaporizhzhia land
bridge, the Caucasus gate (Ingushetia stays Russian per the doc), western Georgia
(Abkhazia, Samegrelo & Zemo Svaneti, Guria, Racha-Lechkhumi & Kvemo Svaneti),
Astrakhan/Kalmykia/Orenburg, the west Kazakh oblasts, Balkan/Ahal (with the
Asgabat city-state), and the Herat–Makran reach (Herat, Farah, Nimruz, Sistan-e
Baluchestan, Baluchistan). The population figure is a working number — the doc
gives none.
⁵ Per `../world/zaryanova.md` (founder-ratified): the Black-majority Pacific great
power spanning the whole Russian Far East. Capital **Gannibal** (the purpose-built
city, on Sakhalin); largest city **Pushkin** (renamed Vladivostok, pop boosted);
**Vorota**, the DPRK gateway town, added at the Khasan border point. Jewish Oblast
is carried by its renamed successor **Zephyria Oblast** (the doc's "provincial
cities are being renamed from their Russian counterparts"), which resolves the
duplicate-id problem those two blocks had. Chukotka is included because the doc's
UTC+9–+13 / 180°-meridian span requires it, though the territory list doesn't name
it — drop state 2597 back to Russia if that's wrong. bbqual 4 reflects the
African-American founding culture.
⁶ Per `../world/neighbor-states.md`. Tarun's capital is a Tashkent placeholder
(the doc names none) and its population a working number; Tajikistan stays
independent and untouched. Qazania is Tatarstan + Bashkortostan with capital
Kazan, demonym Qazani, ~8M per the doc. Kazakhstan, Uzbekistan, Turkmenistan and
Kyrgyzstan are fully partitioned between Tarun and East Neloxia and their nation
records removed; China loses Xinjiang.

`bbqual` (0–5 baseball quality) values are judgment calls — edit the NATION lines
to taste.

## What was carved or removed

- **Nelôxia** takes its nine regions from Russia (Karelia, Leningrad, Kaliningrad),
  Estonia (Saare, Hiiu, Võru, Valga, Põlva), Latvia (Aizkraukle, Madona, Gulbene,
  Valka as the Smiltene stand-in), Lithuania (Klaipėda, Tauragė, Šiauliai, Kaunas,
  Alytus), Poland (Pomorskie, Zachodniopomorskie, Warmińsko-Mazurskie, Lubelskie,
  Podkarpackie), Belarus (Grodno, Brest, Gomel), Slovakia (Prešov), Ukraine
  (Zakarpattia, Odessa), Romania (the nine arc counties incl. both duplicate
  Constanța records), Bulgaria (Dobrich), Hungary (the nine bridge counties),
  Austria (Burgenland, Styria, Carinthia), Italy (Friuli-Venezia Giulia), Slovenia
  (Obalno-kraška, Notranjsko-kraška) and Croatia (the five Dalmatian counties).
  Marquee cities renamed per the gazetteer (Kunislinnô, Tantsika, Stetīn, Uusatôm,
  Kôstônç, Māmeli, Vīpôri, Petrôsô, Gräts, Triest, Spalôt, Ragūz, Marīsô, …).
  The Bosnian cantons of Region 9 could not be carved — the base file models
  Bosnia only as its two entities.
- **Skaria** takes the ratified Danish, Norwegian, Swedish and Finnish
  subdivisions (Innlandet modeled as Hedmark + Oppland; Åland does not exist in
  the base file and is omitted).
- **Atlanta** replaces Western Sahara outright (its duplicate zero-coordinate
  city records dropped; canon waypoint towns added).
- **Adrāra + Soninka & Toro** replace Mauritania (north/south split per
  `african-bloc.md`); Soninka & Toro also takes Senegal's Saint-Louis and Matam
  regions and the town of Bakel (→ Bakəl). Atar and Chinguetti, misfiled inside
  Algeria in the base file with Mauritanian coordinates, were reclaimed into
  Adrāra.
- **Valdória** takes Rio Grande do Sul + Santa Catarina (Brazil), Rocha
  (Uruguay), Corrientes, Misiones, Formosa, Salta, Jujuy (Argentina), Itapúa,
  Ñeembucú (Paraguay), Tarija, Potosí (Bolivia) and Antofagasta (Chile, as
  Litorāl). Porto Alegre → Portô Venla, Pelotas → Santa Laura; Koinīnia added.
- **Meridian States** absorbs the nations Bermuda, French Guiana (→ Esperanza),
  Saint-Pierre & Miquelon, St. Helena, São Tomé & Príncipe, Mayotte, Wallis &
  Futuna and New Caledonia, plus the Canary Islands (from Spain), Corsica
  (from France), and **Magau** (the old Macau record's Aomen state, renamed).
- **Montequinto** was removed from the file entirely, and the **Macau** nation
  record is gone: Aomen joined the Meridian States as Magau, and the Far-East
  states parked inside it became Zaryanova's core (see note ⁵ above), joined by
  Primorsky, Magadan, and Chukotka carved from Russia. All league-pool and
  second-nation references were remapped or dropped accordingly.
- **Kuwait** is untouched — per `kuwait-condominium.md` it keeps its own name,
  flag and national teams. **Morocco** is untouched (aligned, never absorbed).
- Donor nations keep their capitals and remaining states; their `pop` attributes
  were reduced by what moved.

## ID policy

New nation ids 260–267, new state ids 9101+, new city ids 150001+ — all above the
base file's maxima (253 / 9000 / 99991), so every new id is unique. Moved states
and cities keep their original ids (their old owners are gone, so no collisions).
All `REGION_NATION` league-pool references to absorbed nations were remapped to
their successors and deduplicated, and the new nations were added to the
appropriate geographic regions (Europe at-Large, Africa at-Large, South America,
etc.).

## Base-file quirks found along the way

- Your **Zephyria Oblast** was a clone of Jewish Oblast carrying the same state
  id (2590) and the same 18 city ids — exactly the duplicate-id crash risk.
  Resolved by dropping Jewish Oblast (Zephyria is its built replacement and now
  owns those ids uniquely, as Qazania's territory).
- **French Guiana's** state/city blocks existed twice (the original nation +
  Montequinto's copies). Both duplication sources are gone: Esperanza was built
  with fresh ids and Montequinto was removed.
- **Appalachia** (the canonical US state of this universe — West Virginia
  renamed and expanded with the KY/VA/TN border country) had a half-finished
  migration: 21 towns copied into it still existed in Kentucky, Virginia, and
  Tennessee under the same city ids, and **Wilder** carried Bristol England's
  city id and coordinates. Finished here: the towns now live in Appalachia
  only (an internal move — US national population unchanged), and Wilder has
  its own id at the Bristol TN/VA location, population kept at 430,713.
  **The output file now has zero duplicate ids of any kind.**
- Still pre-existing (harmless, untouched): four empty `REGION_NATION id=""`
  entries and six phantom nation ids (61, 79, 140, 202, 212, 375) that stock
  regions/second-nation lists reference without the nations existing — exactly
  as in the base file.
- **Cameroon and Bolivia had broken capital references in the stock file**
  (capids pointing at cities that don't exist). Repaired to Yaoundé and La Paz.
