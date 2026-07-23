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
| 267 | **East Neloxia**⁴ | ENX | Caffa | 21,000,000 | 1 | Europe | Crimea + the north-Caucasus/Caspian span |

¹ Skaria's capital is founder-open in the lore; Göteborg is a placeholder (biggest
city in its territory).
² The lore-ratified sport code (`saharannaise/toponymy.md`).
³ OOTP requires one continent per nation; the legislative capital Esperanza puts it
in South America.
⁴ Name provisional per `east/east.md` (candidates: Colchia/Kôlxônô, Sarmatia,
Alania, Šaraya, Kervania) — a one-line rename in the NATION record when the founder
rules. Its extent here is the conservative core (Crimea → Caucasus gates → Caspian
shore); the Herat road is left unmodeled.

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
  Futuna and New Caledonia, plus the Canary Islands (from Spain) and Corsica
  (from France). A **Magau** state was added new — the existing Macau nation
  record was left alone because it carries your custom Far-East content (see
  below); if you want the lore version pure, delete that nation's Aomen state
  or the whole record.
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

- Your **Zephyria Oblast** (in the custom Macau/Far-East nation) was a clone of
  Jewish Oblast that still carried the same state id (2590) and the same 18 city
  ids — exactly the duplicate-id crash risk. It now has fresh unique ids. If
  Zephyria was meant to *replace* Jewish Oblast, delete the Jewish Oblast block.
- **French Guiana's** state/city blocks existed twice (the original nation +
  your Montequinto's copies). Esperanza was built with fresh ids and the original
  nation removed, so those ids are now unique to Montequinto.
- Still pre-existing (harmless so far, untouched): ~23 duplicate city ids wholly
  inside the stock United States record (the Appalachia region duplication),
  Montequinto's Road Town copy, Bristol (GB/US), and four empty
  `REGION_NATION id=""` entries.
- **Cameroon and Bolivia had broken capital references in the stock file**
  (capids pointing at cities that don't exist). Repaired to Yaoundé and La Paz.
