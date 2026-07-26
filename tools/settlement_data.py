#!/usr/bin/env python3
"""Canonical settlement table for Nelôxia — the single source for the
settlements gazetteer page and the toponym generator.

READ THIS FIRST — what the `site` column is and is not.

`site` is a **real-world reference key**, not an in-world name. It is the label
the place carries on a present-day map, inherited from the subdivision lists in
world/boundaries.md purely so the founder can tell which place is meant. No
names pass has ever been run on this world, so the in-world name of almost every
settlement — its LOCAL name as well as its Nelôxi one — is undetermined.

Treating `site` as the local name is a category error, and in 24 cases it is a
flat impossibility: those names are Soviet-era or Russian-imperial coinages
(Petrozavodsk 1703, Belomorsk 1938, Kaliningrad 1946, Priozersk 1948,
Blagoevgrad 1950, Kostomuksha 1977 …) that could not exist in a timeline where
Nelôxia has held these places for five centuries. See ANACHRONISM below.

So a settlement has up to four name slots, three of them usually open:

  site     — the real-world reference key (known; NOT in-world, NEVER a name)
  nelox    — the Nelôxi endonym (open docket unless in CANON)
  local    — what people there call it. DEFAULTS TO `nelox`: after five centuries
             the local form IS the Nelôxi name. Only set separately where a living
             local-language community keeps its own form alongside.
  former   — the pre-Nelôxian / substrate name (Gumbinnen, Akhtiar, Petroskoi).
             A former name, NOT a current local one.
  exonym   — what the outside world calls it (open docket)

Three separate concerns, deliberately kept apart:

  CITIES  — the physical facts: reference key, region, country, terrain,
            a one-clause note, and the canonical fictional population.
  CANON   — ONLY the Nelôxi names that are actually canon, i.e. attested in
            world/gazetteer.md, each with its gazetteer layer tag. Everything
            not in this dict has NO Nelôxi name yet; it is an open docket for
            the founder (charter §63/§64) and the toponym generator's worklist.
  EXONYM  — the international / historical form outsiders use. Canon requires
            this be a SEPARATE field from the endonym: gazetteer.md records
            "Odessa survives only as the outsiders' exonym" for Uusatôm.
  HINT    — where a genuine historical or trade-route name exists (Danzig,
            Memel, Fiume, Monastir), it is offered to the generator as strong
            raw-loan material. A hint is a candidate, never a decision.

The layer tags are the five canon ones (gazetteer.md): native · nativized ·
raw loan · archaic-x · hybrid.
"""

# --- regions: name, per-capita GDP (USD, fictional), status --------------------
REGIONS = [
    ("Karelia & the North",          42000, "core"),
    ("Livonian Core",                44000, "core"),
    ("Lithuanian Spine",             41000, "core"),
    ("Prussian–Pomeranian Coast",    58000, "core"),
    ("Eastern Corridor",             34000, "core"),
    ("Moldavian Arc & Black Sea",    33000, "core"),
    ("Pannonian Bridge",             38000, "core"),
    ("Alpine–Adriatic Arm",          56000, "core"),
    ("Dalmatian Coast",              40000, "core"),
    ("Western Alpine & Riviera Arc", 60000, "core"),
    ("Thracian–Macedonian Corridor", 24000, "core"),
    ("Sevastopol · Federal City",    40000, "federal"),
    ("Yemeni Commonwealth",          19000, "commonwealth"),
]

# Regions the toponym generator must NOT offer. The Yemeni Commonwealth keeps
# its Arabic toponymy by ruling: "a Nelôxi civic overlay sits beside — never
# over — the Arabic name" (world/yemeni-commonwealth.md).
NO_RENAME_REGIONS = {"Yemeni Commonwealth"}

# --- (site, region, cc, terrain, notes, pop) -----------------------------------
CITIES = [
 # Region 1 · Karelia & the North
 ("Belomorsk","Karelia & the North","RU","Sea","White Sea coast; canal outlet to the Arctic",26000),
 ("Kem","Karelia & the North","RU","Sea","White Sea harbour; the Solovki crossing",22000),
 ("Petrozavodsk","Karelia & the North","RU","Lake","Lake Onega west shore; the lake capital",480000),
 ("Kondopoga","Karelia & the North","RU","Lake","Onega rapids; water-power and locks",62000),
 ("Sortavala","Karelia & the North","RU","Lake","Ladoga north shore; skerry harbour",42000),
 ("Olonets","Karelia & the North","RU","Lake","Ladoga lake-plain; river confluence",30000),
 ("Segezha","Karelia & the North","RU","Forest","Timber belt; canal-side mill site",58000),
 ("Kostomuksha","Karelia & the North","RU","Forest","Iron-ore field near the Finnish line",46000),
 ("Vyborg","Karelia & the North","RU","Sea","The isthmus gate; deep granite bay",165000),
 ("Priozersk","Karelia & the North","RU","Lake","Ladoga west shore; fortress on the Vuoksi",26000),
 # Region 2 · Livonian Core
 ("Kuressaare","Livonian Core","EE","Island","Saaremaa's harbour and castle",24000),
 ("Kärdla","Livonian Core","EE","Island","Hiiumaa's north-coast landing",6000),
 ("Valga","Livonian Core","EE","Plain","Rail crossing on the Estonian–Latvian seam",24000),
 ("Võru","Livonian Core","EE","Lake","Upland lake country; the Tamula shore",22000),
 ("Põlva","Livonian Core","EE","Upland","Devonian upland; a small river valley",12000),
 ("Madona","Livonian Core","LV","Upland","Vidzeme highland; the estate belt",14000),
 ("Gulbene","Livonian Core","LV","Upland","Highland rail junction",15000),
 ("Aizkraukle","Livonian Core","LV","River","Daugava bank; hydro site",16000),
 ("Smiltene","Livonian Core","LV","Upland","Gauja headwater country",10000),
 # Region 3 · Lithuanian Spine
 ("Klaipėda","Lithuanian Spine","LT","Sea","The only deep sea port; Curonian Lagoon mouth",460000),
 ("Neringa","Lithuanian Spine","LT","Spit","The Curonian Spit; dunes and pilot station",8000),
 ("Palanga","Lithuanian Spine","LT","Sea","Open amber coast; sand beach",40000),
 ("Kaunas","Lithuanian Spine","LT","River","Nemunas–Neris confluence; the river hinge",820000),
 ("Jonava","Lithuanian Spine","LT","River","Neris crossing; chemical works",62000),
 ("Kėdainiai","Lithuanian Spine","LT","Plain","Nevėžis valley; the estate town",48000),
 ("Šiauliai","Lithuanian Spine","LT","Plain","Inland rail junction; the northern crossroads",210000),
 ("Radviliškis","Lithuanian Spine","LT","Plain","Rail marshalling yards",30000),
 ("Raseiniai","Lithuanian Spine","LT","Plain","Dubysa valley; Samogitian upland edge",18000),
 ("Tauragė","Lithuanian Spine","LT","River","Jūra crossing on the Prussian road",42000),
 ("Marijampolė","Lithuanian Spine","LT","Plain","Šešupė valley; the Suvalkija plain",72000),
 ("Alytus","Lithuanian Spine","LT","River","Nemunas bend; pine country",96000),
 ("Kelmė","Lithuanian Spine","LT","Plain","A small estate town, Samogitia",16000),
 # Region 4 · Prussian–Pomeranian Coast
 ("Kaliningrad","Prussian–Pomeranian Coast","RU","River","Pregolya mouth on the Vistula Lagoon; the capital basin",5800000),
 ("Baltiysk","Prussian–Pomeranian Coast","RU","Strait","The lagoon's only sea gate; naval deepwater",66000),
 ("Primorsk","Prussian–Pomeranian Coast","RU","Lagoon","Lagoon fishing shore",12000),
 ("Svetlogorsk","Prussian–Pomeranian Coast","RU","Sea","Cliff coast; amber baths",30000),
 ("Sovetsk","Prussian–Pomeranian Coast","RU","River","Nemunas crossing; the river border town",76000),
 ("Chernyakhovsk","Prussian–Pomeranian Coast","RU","River","Angrapa–Instruch confluence",72000),
 ("Gusev","Prussian–Pomeranian Coast","RU","Plain","Eastern Prussian plain; road town",56000),
 ("Gdańsk","Prussian–Pomeranian Coast","PL","Delta","Vistula delta; the great grain port",1400000),
 ("Gdynia","Prussian–Pomeranian Coast","PL","Sea","Purpose-built deepwater harbour",480000),
 ("Sopot","Prussian–Pomeranian Coast","PL","Sea","Sand-beach shore between the two ports",40000),
 ("Puck","Prussian–Pomeranian Coast","PL","Bay","Sheltered inner bay behind the Hel spit",14000),
 ("Wejherowo","Prussian–Pomeranian Coast","PL","Upland","Kashubian lake upland; inland of the bay",68000),
 ("Elbląg","Prussian–Pomeranian Coast","PL","Lagoon","Vistula Lagoon head; canal to the lakes",150000),
 ("Malbork","Prussian–Pomeranian Coast","PL","River","Nogat crossing; the castle river-anchor",48000),
 ("Tczew","Prussian–Pomeranian Coast","PL","River","Vistula bridge crossing",76000),
 ("Olsztyn","Prussian–Pomeranian Coast","PL","Lake","Masurian lake plateau; the inland seat",220000),
 ("Ełk","Prussian–Pomeranian Coast","PL","Lake","Eastern Masurian lakes",78000),
 ("Giżycko","Prussian–Pomeranian Coast","PL","Lake","The isthmus between the great Masurian lakes",38000),
 ("Gołdap","Prussian–Pomeranian Coast","PL","Upland","Romincka forest edge; lake basin",18000),
 ("Szczecin","Prussian–Pomeranian Coast","PL","River","Oder mouth; the western gate to the interior",900000),
 ("Świnoujście","Prussian–Pomeranian Coast","PL","Strait","The Oder lagoon's sea channel",52000),
 ("Kołobrzeg","Prussian–Pomeranian Coast","PL","Sea","River-mouth harbour; salt springs",70000),
 ("Koszalin","Prussian–Pomeranian Coast","PL","Plain","Coastal plain behind the dune belt",140000),
 ("Słupsk","Prussian–Pomeranian Coast","PL","River","Słupia valley; inland of the coast",110000),
 ("Stargard","Prussian–Pomeranian Coast","PL","River","Ina crossing; inland Oder hinterland",90000),
 # Region 5 · Eastern Corridor
 ("Hrodna","Eastern Corridor","BY","River","Neman high bank; the border-bend fortress",780000),
 ("Lida","Eastern Corridor","BY","Plain","Portage country between river systems",180000),
 ("Vawkavysk","Eastern Corridor","BY","Plain","Rail-gauge transfer point",80000),
 ("Slonim","Eastern Corridor","BY","River","Shchara valley; canal to the Pripyat",90000),
 ("Baranavichy","Eastern Corridor","BY","Plain","The great rail crossroads of the corridor",320000),
 ("Brest","Eastern Corridor","BY","River","Bug–Mukhavets confluence; the gauge frontier",620000),
 ("Kobryn","Eastern Corridor","BY","Canal","Dnieper–Bug canal town",96000),
 ("Pinsk","Eastern Corridor","BY","Marsh","Pripyat marshes; the marsh capital and river port",230000),
 ("Mazyr","Eastern Corridor","BY","River","Pripyat high bank; refinery site",200000),
 ("Homel","Eastern Corridor","BY","River","Sozh river port; the corridor's eastern anchor",1050000),
 ("Rechytsa","Eastern Corridor","BY","River","Dnieper bank; oil-field edge",120000),
 ("Svetlahorsk","Eastern Corridor","BY","River","Berezina crossing",130000),
 ("Zhlobin","Eastern Corridor","BY","River","Dnieper crossing; steelworks",150000),
 ("Lublin","Eastern Corridor","PL","Upland","Loess upland; the corridor's western seat",720000),
 ("Zamość","Eastern Corridor","PL","Plain","Planned fortress town on the Roztocze edge",110000),
 ("Chełm","Eastern Corridor","PL","Upland","Chalk hills above the Bug plain",96000),
 ("Puławy","Eastern Corridor","PL","River","Vistula bank; chemical works",84000),
 ("Biała Podlaska","Eastern Corridor","PL","Plain","Road town on the Brest highway",96000),
 ("Rzeszów","Eastern Corridor","PL","River","Wisłok valley; the Subcarpathian seat",340000),
 ("Stalowa Wola","Eastern Corridor","PL","Forest","Purpose-built steel and forest-industry town",110000),
 ("Mielec","Eastern Corridor","PL","Plain","Wisłoka valley; aviation works",100000),
 ("Tarnobrzeg","Eastern Corridor","PL","River","Vistula bank; sulphur basin",80000),
 ("Przemyśl","Eastern Corridor","PL","River","San gorge; the fortress gate to the passes",110000),
 ("Krosno","Eastern Corridor","PL","Upland","Carpathian foothills; the oil cradle",84000),
 ("Sanok","Eastern Corridor","PL","Mountain","San valley at the Bieszczady gate",66000),
 ("Prešov","Eastern Corridor","SK","Mountain","Torysa valley; salt workings under the Carpathians",150000),
 ("Poprad","Eastern Corridor","SK","Mountain","Under the High Tatras; the mountain junction",92000),
 ("Humenné","Eastern Corridor","SK","River","Laborec valley; eastern Carpathian approach",58000),
 ("Bardejov","Eastern Corridor","SK","Mountain","Pass town on the Polish frontier; spa springs",56000),
 # Region 6 · Moldavian Arc & Black Sea
 ("Odesa","Moldavian Arc & Black Sea","UA","Sea","Liman coast; the founding harbour",2200000),
 ("Chornomorsk","Moldavian Arc & Black Sea","UA","Sea","Deepwater container roads south of the liman",120000),
 ("Bilhorod-Dnistrovskyi","Moldavian Arc & Black Sea","UA","Liman","Dniester liman fortress",96000),
 ("Izmail","Moldavian Arc & Black Sea","UA","River","Danube river port above the delta",140000),
 ("Uzhhorod","Moldavian Arc & Black Sea","UA","Mountain","Uzh valley at the Carpathian pass mouth",230000),
 ("Mukachevo","Moldavian Arc & Black Sea","UA","Mountain","Latorica valley; castle on the plain edge",170000),
 ("Suceava","Moldavian Arc & Black Sea","RO","Upland","Bukovina plateau; the old princely seat",168000),
 ("Botoșani","Moldavian Arc & Black Sea","RO","Plain","Moldavian plain; market town",210000),
 ("Iași","Moldavian Arc & Black Sea","RO","Hill","Bahlui valley hills; the Moldavian capital site",800000),
 ("Vaslui","Moldavian Arc & Black Sea","RO","Plain","Bârlad valley; central Moldavia",110000),
 ("Bârlad","Moldavian Arc & Black Sea","RO","Plain","Bârlad river market town",110000),
 ("Roman","Moldavian Arc & Black Sea","RO","River","Siret–Moldova confluence",100000),
 ("Galați","Moldavian Arc & Black Sea","RO","River","Danube maritime port; the seagoing head of the river",430000),
 ("Tulcea","Moldavian Arc & Black Sea","RO","Delta","The Danube delta gateway",130000),
 ("Constanța","Moldavian Arc & Black Sea","RO","Sea","The great Black Sea port; Dobruja headland",700000),
 ("Mangalia","Moldavian Arc & Black Sea","RO","Sea","Southern Dobruja coast; shipyard",72000),
 ("Medgidia","Moldavian Arc & Black Sea","RO","Canal","On the Danube–Black Sea canal",78000),
 ("Bistrița","Moldavian Arc & Black Sea","RO","Mountain","Under the Bârgău pass into Moldavia",150000),
 ("Oradea","Moldavian Arc & Black Sea","RO","Plain","Criș river; the Pannonian gate",390000),
 ("Dobrich","Moldavian Arc & Black Sea","BG","Plain","Southern Dobruja grain plateau",150000),
 ("Balchik","Moldavian Arc & Black Sea","BG","Sea","Chalk-cliff coast; sheltered anchorage",24000),
 ("Slobozia","Moldavian Arc & Black Sea","MD","River","Dniester left bank",28000),
 ("Ștefan Vodă","Moldavian Arc & Black Sea","MD","Plain","Dniester lowland; vineyard country",14000),
 # Region 7 · Pannonian Bridge
 ("Szeged","Pannonian Bridge","HU","River","Tisza–Maros confluence; the plain's southern seat",320000),
 ("Hódmezővásárhely","Pannonian Bridge","HU","Plain","Tisza flood-plain market town",88000),
 ("Szentes","Pannonian Bridge","HU","River","Tisza bank; thermal water",54000),
 ("Békéscsaba","Pannonian Bridge","HU","Plain","Körös plain; rail crossroads",110000),
 ("Gyula","Pannonian Bridge","HU","Plain","Körös marsh castle; thermal springs",58000),
 ("Orosháza","Pannonian Bridge","HU","Plain","Deep plain; gas field",54000),
 ("Kecskemét","Pannonian Bridge","HU","Sand","Danube–Tisza sand ridge; orchard country",220000),
 ("Baja","Pannonian Bridge","HU","River","Danube crossing on the southern plain",68000),
 ("Szekszárd","Pannonian Bridge","HU","Hill","Loess wine hills above the Danube",62000),
 ("Pécs","Pannonian Bridge","HU","Mountain","Under the Mecsek; coal and the southern seat",280000),
 ("Kaposvár","Pannonian Bridge","HU","Hill","Kapos valley in the Somogy hills",122000),
 ("Siófok","Pannonian Bridge","HU","Lake","Balaton's south shore at the Sió outlet",50000),
 ("Nagykanizsa","Pannonian Bridge","HU","Plain","Southwest gate; oil field and rail",92000),
 ("Zalaegerszeg","Pannonian Bridge","HU","Hill","Zala valley in the western hills",112000),
 ("Szombathely","Pannonian Bridge","HU","Plain","The old Roman road seat; Alpine foreland",156000),
 ("Sopron","Pannonian Bridge","HU","Hill","The gate between the Alps and Lake Fertő",124000),
 ("Mosonmagyaróvár","Pannonian Bridge","HU","River","Danube branch crossing at the Little Plain",66000),
 ("Győr","Pannonian Bridge","HU","River","Danube–Rába–Rábca confluence; the Little Plain seat",260000),
 # Region 8 · Alpine–Adriatic Arm
 ("Eisenstadt","Alpine–Adriatic Arm","AT","Hill","Leitha hills above the Fertő basin",30000),
 ("Graz","Alpine–Adriatic Arm","AT","River","Mur valley basin; the Alpine engineering seat",700000),
 ("Leoben","Alpine–Adriatic Arm","AT","Mountain","Mur valley narrows; the iron road",50000),
 ("Kapfenberg","Alpine–Adriatic Arm","AT","Mountain","Mürz valley steel works",46000),
 ("Klagenfurt","Alpine–Adriatic Arm","AT","Lake","Wörthersee basin; the Carinthian seat",210000),
 ("Villach","Alpine–Adriatic Arm","AT","River","Drava valley at the three-pass junction",130000),
 ("Wolfsberg","Alpine–Adriatic Arm","AT","Valley","Lavant valley; the eastern Carinthian road",50000),
 ("Trieste","Alpine–Adriatic Arm","IT","Sea","The head of the Adriatic; karst escarpment harbour",400000),
 ("Gorizia","Alpine–Adriatic Arm","IT","River","Isonzo valley mouth; the border town",68000),
 ("Monfalcone","Alpine–Adriatic Arm","IT","Sea","Shipyard bay at the Isonzo mouth",60000),
 ("Udine","Alpine–Adriatic Arm","IT","Plain","Friulian plain; the inland Friuli seat",200000),
 ("Pordenone","Alpine–Adriatic Arm","IT","Plain","Western Friulian plain; Noncello river",100000),
 ("Koper","Alpine–Adriatic Arm","SI","Sea","Istrian bay; the container port",70000),
 ("Ilirska Bistrica","Alpine–Adriatic Arm","SI","Karst","Reka valley at the karst threshold",9000),
 ("Piran","Alpine–Adriatic Arm","SI","Cape","A walled point between two bays; the salt pans",10000),
 ("Izola","Alpine–Adriatic Arm","SI","Sea","Fishing harbour on the Slovene coast",20000),
 ("Ankaran","Alpine–Adriatic Arm","SI","Sea","The bay's northern shore below the Karst edge",6000),
 ("Sežana","Alpine–Adriatic Arm","SI","Karst","The Karst plateau; the rail line to the sea",12000),
 ("Divača","Alpine–Adriatic Arm","SI","Karst","Cave country; the junction above the Škocjan chasms",3000),
 ("Nova Gorica","Alpine–Adriatic Arm","SI","River","Soča valley at the Italian line; the twin of Gorizia",26000),
 ("Ajdovščina","Alpine–Adriatic Arm","SI","Valley","Vipava valley; the bora wind gate",14000),
 ("Idrija","Alpine–Adriatic Arm","SI","Mountain","The mercury mine in a deep mountain fold",12000),
 ("Tolmin","Alpine–Adriatic Arm","SI","Valley","Upper Soča; the Julian Alps approach",8000),
 # Region 9 · Dalmatian Coast (incl. Istria & the Kvarner)
 ("Pula","Dalmatian Coast","HR","Bay","A deep sheltered gulf at the peninsula's tip; the great naval harbour",120000),
 ("Rovinj","Dalmatian Coast","HR","Sea","Rock peninsula town among the west-coast islets",28000),
 ("Poreč","Dalmatian Coast","HR","Sea","Low limestone west coast; shallow harbour",32000),
 ("Umag","Dalmatian Coast","HR","Sea","The northwest cape facing the Venetian lagoon",26000),
 ("Pazin","Dalmatian Coast","HR","Gorge","The peninsula's interior; a castle above a swallow-hole chasm",18000),
 ("Labin","Dalmatian Coast","HR","Hill","Hill town above the Kvarner; the Istrian coal field",22000),
 ("Buzet","Dalmatian Coast","HR","Karst","Upper Mirna valley; the truffle woods",12000),
 ("Rijeka","Dalmatian Coast","HR","Bay","Where the Kvarner gulf meets the pass road; the deepwater terminal",350000),
 ("Opatija","Dalmatian Coast","HR","Sea","Sheltered shore under Učka; the winter coast",22000),
 ("Krk","Dalmatian Coast","HR","Island","The great Kvarner island; bridged to the mainland",13000),
 ("Mali Lošinj","Dalmatian Coast","HR","Island","Deep island harbour in the outer Kvarner",16000),
 ("Senj","Dalmatian Coast","HR","Sea","Velebit channel; the bora gate",14000),
 ("Gospić","Dalmatian Coast","HR","Karst","Lika polje behind the Velebit wall",24000),
 ("Zadar","Dalmatian Coast","HR","Sea","Peninsula harbour among the islands",150000),
 ("Šibenik","Dalmatian Coast","HR","Estuary","Krka river gorge mouth; a hidden deepwater bay",90000),
 ("Knin","Dalmatian Coast","HR","Karst","Krka headwaters; the inland fortress crossroads",30000),
 ("Split","Dalmatian Coast","HR","Sea","Sheltered bay under the Mosor; the coast's seat",450000),
 ("Ploče","Dalmatian Coast","HR","Delta","Neretva delta port",18000),
 ("Metković","Dalmatian Coast","HR","River","Head of Neretva navigation",30000),
 ("Dubrovnik","Dalmatian Coast","HR","Sea","Walled rock harbour on the open sea",84000),
 ("Bihać","Dalmatian Coast","BA","River","Una valley; the Bosnian Krajina gate",110000),
 ("Livno","Dalmatian Coast","BA","Karst","Livno polje; a great karst basin",34000),
 ("Široki Brijeg","Dalmatian Coast","BA","Karst","Herzegovinian karst plateau",30000),
 # Region 10 · Western Alpine & Riviera Arc
 ("Marseille","Western Alpine & Riviera Arc","FR","Sea","Calanque coast; the great Mediterranean harbour",1800000),
 ("Toulon","Western Alpine & Riviera Arc","FR","Bay","A deep natural roadstead; the naval anchorage",420000),
 ("Aix-en-Provence","Western Alpine & Riviera Arc","FR","Hill","Thermal springs below the Sainte-Victoire",220000),
 ("Avignon","Western Alpine & Riviera Arc","FR","River","Rhône crossing; the bridge city",190000),
 ("Nice","Western Alpine & Riviera Arc","FR","Sea","Where the Alps meet the sea; the bay of angels",700000),
 ("Cannes","Western Alpine & Riviera Arc","FR","Sea","Sheltered Riviera bay; the Lérins roads",150000),
 ("Antibes","Western Alpine & Riviera Arc","FR","Cape","Cape harbour between two bays",150000),
 ("Aosta","Western Alpine & Riviera Arc","IT","Valley","The junction of the Great and Little St Bernard passes",68000),
 ("Turin","Western Alpine & Riviera Arc","IT","River","Po headwaters under the Alpine wall; the Savoy seat",1700000),
 ("Cuneo","Western Alpine & Riviera Arc","IT","Plateau","The wedge between two rivers; the Ligurian pass approach",110000),
 ("Asti","Western Alpine & Riviera Arc","IT","Hill","Monferrato wine hills",150000),
 ("Alessandria","Western Alpine & Riviera Arc","IT","Plain","Tanaro–Bormida confluence; the fortress plain",180000),
 ("Novara","Western Alpine & Riviera Arc","IT","Plain","Rice plain between Ticino and Sesia",200000),
 ("Milan","Western Alpine & Riviera Arc","IT","Plain","The central Po plain; the canal and road hub",3500000),
 ("Monza","Western Alpine & Riviera Arc","IT","River","Lambro valley at the Brianza edge",250000),
 ("Como","Western Alpine & Riviera Arc","IT","Lake","The lake's south horn; the Splügen road",170000),
 ("Varese","Western Alpine & Riviera Arc","IT","Lake","Prealpine lake basin",160000),
 ("Bergamo","Western Alpine & Riviera Arc","IT","Hill","Walled hill above the plain; Brembana valley mouth",240000),
 ("Brescia","Western Alpine & Riviera Arc","IT","Hill","Between Garda and the Val Trompia iron",400000),
 ("Cremona","Western Alpine & Riviera Arc","IT","River","Po bank; the river crossing",140000),
 ("Pavia","Western Alpine & Riviera Arc","IT","River","Ticino–Po confluence; the covered bridge",140000),
 ("Mantua","Western Alpine & Riviera Arc","IT","Lake","Mincio lakes; a city on water",100000),
 ("Verona","Western Alpine & Riviera Arc","IT","River","Adige bend at the Brenner road mouth",520000),
 ("Vicenza","Western Alpine & Riviera Arc","IT","Plain","Bacchiglione plain under the Berici hills",220000),
 ("Padua","Western Alpine & Riviera Arc","IT","Plain","Brenta plain; the lagoon's mainland seat",440000),
 ("Venice","Western Alpine & Riviera Arc","IT","Lagoon","The lagoon islands; the sea's own city",600000),
 ("Treviso","Western Alpine & Riviera Arc","IT","River","Sile springs; the walled water town",170000),
 ("Rovigo","Western Alpine & Riviera Arc","IT","Delta","Polesine, between Adige and Po",100000),
 ("Lugano","Western Alpine & Riviera Arc","CH","Lake","Lake basin below the Ceneri; the southern valleys",130000),
 ("Bellinzona","Western Alpine & Riviera Arc","CH","Valley","The castle gate of the Ticino valley; the St Gotthard road",90000),
 ("Sion","Western Alpine & Riviera Arc","CH","Valley","Rhône valley floor between rock hills",70000),
 ("Chur","Western Alpine & Riviera Arc","CH","Valley","Rhine valley at the fan of Alpine passes",74000),
 # Region 11 · Thracian–Macedonian Corridor
 ("Burgas","Thracian–Macedonian Corridor","BG","Bay","A great shallow bay and salt lakes; the southern port",300000),
 ("Nesebar","Thracian–Macedonian Corridor","BG","Island","Rock peninsula harbour",16000),
 ("Sozopol","Thracian–Macedonian Corridor","BG","Sea","Old Greek colony headland",7000),
 ("Yambol","Thracian–Macedonian Corridor","BG","River","Tundzha valley; the Thracian plain",110000),
 ("Elhovo","Thracian–Macedonian Corridor","BG","River","Lower Tundzha; the Turkish frontier road",14000),
 ("Haskovo","Thracian–Macedonian Corridor","BG","Hill","Between the Rhodope foot and the Maritsa plain",110000),
 ("Dimitrovgrad","Thracian–Macedonian Corridor","BG","River","Maritsa crossing; planned industry town",58000),
 ("Svilengrad","Thracian–Macedonian Corridor","BG","River","Maritsa bridge at the three-border point",28000),
 ("Kardzhali","Thracian–Macedonian Corridor","BG","Mountain","Arda gorges; the eastern Rhodope reservoirs",68000),
 ("Smolyan","Thracian–Macedonian Corridor","BG","Mountain","High Rhodope valley",42000),
 ("Blagoevgrad","Thracian–Macedonian Corridor","BG","Valley","Struma valley under Rila",110000),
 ("Sandanski","Thracian–Macedonian Corridor","BG","Valley","Lower Struma; hot springs, Pirin foot",40000),
 ("Petrich","Thracian–Macedonian Corridor","BG","Valley","The Struma gate to the Aegean",44000),
 ("Gotse Delchev","Thracian–Macedonian Corridor","BG","Valley","Mesta valley between Pirin and the Rhodope",30000),
 ("Razlog","Thracian–Macedonian Corridor","BG","Basin","High basin between Rila and Pirin",18000),
 ("Edirne","Thracian–Macedonian Corridor","TR","River","Maritsa–Tundzha–Arda confluence; the Thracian crossroads",260000),
 ("Keşan","Thracian–Macedonian Corridor","TR","Hill","Between the Gulf of Saros and the Maritsa plain",70000),
 ("Uzunköprü","Thracian–Macedonian Corridor","TR","River","The long bridge over the Ergene",50000),
 ("Vlorë","Thracian–Macedonian Corridor","AL","Bay","The bay at the Otranto narrows; Karaburun shelter",180000),
 ("Sarandë","Thracian–Macedonian Corridor","AL","Sea","Channel coast facing Corfu",40000),
 ("Himarë","Thracian–Macedonian Corridor","AL","Sea","The Riviera under the Ceraunian mountains",8000),
 ("Gjirokastër","Thracian–Macedonian Corridor","AL","Mountain","Drino valley; the stone hill town",30000),
 ("Tepelenë","Thracian–Macedonian Corridor","AL","River","Vjosa gorge junction",6000),
 ("Përmet","Thracian–Macedonian Corridor","AL","Valley","Upper Vjosa; thermal springs",9000),
 ("Korçë","Thracian–Macedonian Corridor","AL","Basin","A high plain basin near the lakes",80000),
 ("Pogradec","Thracian–Macedonian Corridor","AL","Lake","Lake Ohrid's southwest shore",30000),
 ("Bitola","Thracian–Macedonian Corridor","MK","Plain","Pelagonia plain under Baba mountain",110000),
 ("Prilep","Thracian–Macedonian Corridor","MK","Plain","Northern Pelagonia; tobacco and marble",96000),
 ("Kruševo","Thracian–Macedonian Corridor","MK","Mountain","The high mountain town above the plain",8000),
 ("Resen","Thracian–Macedonian Corridor","MK","Lake","Prespa basin between the two lakes",12000),
 ("Veles","Thracian–Macedonian Corridor","MK","River","Vardar gorge crossing; the central hinge",70000),
 ("Kavadarci","Thracian–Macedonian Corridor","MK","Valley","Tikveš wine basin",50000),
 ("Negotino","Thracian–Macedonian Corridor","MK","River","Vardar valley floor",20000),
 ("Demir Kapija","Thracian–Macedonian Corridor","MK","Gorge","The Iron Gate of the Vardar",5000),
 ("Gevgelija","Thracian–Macedonian Corridor","MK","River","The Vardar's exit to the Aegean plain",22000),
 ("Strumica","Thracian–Macedonian Corridor","MK","Basin","A warm sheltered basin; market gardens",55000),
 ("Radoviš","Thracian–Macedonian Corridor","MK","Valley","Under Plachkovica; copper workings",25000),
 ("Sveti Nikole","Thracian–Macedonian Corridor","MK","Plain","Ovče Pole, the sheep plain",20000),
 # Sevastopol · Federal City
 ("Sevastopol","Sevastopol · Federal City","UA","Bay","The great drowned-valley naval harbour; federal city and Fleet seat",800000),
 # Region 12 · Yemeni Commonwealth — Arabic toponymy, NOT subject to renaming
 ("Aden","Yemeni Commonwealth","YE","Crater","A volcanic crater harbour at the strait; the federal gateway",6500000),
 ("Sanaa","Yemeni Commonwealth","YE","Highland","High plateau basin ringed by mountains; the commonwealth capital",3600000),
 ("Taiz","Yemeni Commonwealth","YE","Mountain","Under Jabal Sabir; the southern highland seat",1300000),
 ("Al Hudaydah","Yemeni Commonwealth","YE","Sea","Red Sea shallow-water port",1300000),
 ("Ibb","Yemeni Commonwealth","YE","Highland","The green highland; monsoon terraces",700000),
 ("Mukalla","Yemeni Commonwealth","YE","Sea","Cliff-backed harbour on the Hadhramaut coast",500000),
 ("Dhamar","Yemeni Commonwealth","YE","Highland","High plain south of the capital basin",320000),
 ("Say'un","Yemeni Commonwealth","YE","Wadi","Wadi Hadhramaut; the mudbrick oasis towns",130000),
 ("Ataq","Yemeni Commonwealth","YE","Desert","Desert-edge road town; oil fields",90000),
 ("Zinjibar","Yemeni Commonwealth","YE","Coast","Abyan delta; the coastal farm belt",90000),
 ("Hadibu","Yemeni Commonwealth","YE","Island","Socotra; the island under the monsoon",20000),
]

# --- CANON: only names attested in world/gazetteer.md -------------------------
# site -> (nelôxi endonym, layer, gloss)
CANON = {
 "Belomorsk":   ("Korbitô",     "native",    "backwoods-settlement (korpi + -itô)"),
 "Petrozavodsk":("Petrôsô",     "hybrid",    "Peter's river-bend (Slavic Petro- + -sô)"),
 "Sortavala":   ("Sôrtô",       "nativized", "Karelian, clipped and harmonized"),
 "Kondopoga":   ("Koskenbôrk",  "hybrid",    "rapids-fortress (koski + -bôrk)"),
 "Olonets":     ("Järvemō",     "native",    "lake-land (järve + -mō)"),
 "Vyborg":      ("Vīpôri",      "nativized", "Norse Viborg 'holy castle', harmonized"),
 "Kuressaare":  ("Sārô",        "native",    "island-land"),
 "Kärdla":      ("Hiumō",       "native",    "Hiiu-land (-mō)"),
 "Klaipėda":    ("Māmeli",      "nativized", "Hanseatic river-name; sea-mouth Māmelinsô"),
 "Šiauliai":    ("Xauli",       "archaic-x", "š- → x read [ks]: KSAU-li"),
 "Neringa":     ("Neikūri",     "nativized", "Curonian Neukuhr 'new croft'"),
 "Raseiniai":   ("Rosēni",      "nativized", "Lithuanian, stripped of the Baltic plural"),
 "Kėdainiai":   ("Keidani",     "raw loan",  "Polish/Radziwiłł estate name Kiejdany, kept raw"),
 "Kaliningrad": ("Kunislinnô",  "hybrid",    "king's-fortress (kunis- + -linnô); ceremonial Kunixa"),
 "Baltiysk":    ("Pillô",       "nativized", "Pillau; the naval deepwater port"),
 "Svetlogorsk": ("Rauschenbôrk","raw loan",  "German Rauschenburg, keeps sch; -bôrk from -burg"),
 "Primorsk":    ("Fischūsô",    "raw loan",  "LG Fischhausen 'fish-houses'; keeps f and sch"),
 "Sovetsk":     ("Tilsit",      "raw loan",  "the German river-border town on the Nemunas"),
 "Gdańsk":      ("Tantsika",    "archaic-x", "Danzig via x=[ks]: tant-SEE-ka"),
 "Elbląg":      ("Elbinki",     "nativized", "LG Elbing kept, Baltic -i"),
 "Malbork":     ("Marianbôrk",  "raw loan",  "Marienburg; German -bôrk from -burg"),
 "Puck":        ("Puka",        "nativized", "Putzig, clipped to a clean Finnic shape"),
 "Gołdap":      ("Goldap",      "raw loan",  "Old Prussian galda 'lake-basin', left raw"),
 "Szczecin":    ("Stetīn",      "nativized", "German Stettin → Stetīn"),
 "Hrodna":      ("Marīsô",      "native",    "border-bend (marī- 'march' + -sô)"),
 "Lida":        ("Līda",        "raw loan",  "Slavic, adopted completely raw"),
 "Vawkavysk":   ("Volkovixi",   "archaic-x", "Slavic 'wolf's-mouth' + administrative [ks]"),
 "Odesa":       ("Uusatôm",     "native",    "new-harbour (uus + satām), named by its founders"),
 "Constanța":   ("Kôstônç",     "nativized", "Ottoman trade-name Köstence → Kôstônç"),
 "Graz":        ("Gräts",       "nativized", "German Graz → Gräts"),
 "Trieste":     ("Triest",      "raw loan",  "the Adriatic legal-financial port; Italian kept"),
 "Split":       ("Spalôt",      "nativized", "Venetian Spalato → Spalôt, not Slavic Split"),
 "Dubrovnik":   ("Ragūz",       "nativized", "Venetian Ragusa → Ragūz"),
 # Sevastopol is deliberately NOT here. "Sevastôpôl" is Sevastopol with
 # diacritics — the exact failure this table exists to prevent — and it was
 # never founder canon. The Fleet seat is an open docket: a federal naval city
 # is strong ground for a patron or functional name, not a respelling.
}

# --- EXONYM: the international / historical form outsiders use -----------------
# Only where it differs from the site name. Canon requires the endonym and the
# exonym be separate fields (Uusatôm ↔ Odessa).
EXONYM = {
 "Belomorsk":"Belomorsk","Vyborg":"Viborg","Priozersk":"Kexholm","Kondopoga":"Kondopoga",
 "Klaipėda":"Memel","Neringa":"Nidden","Palanga":"Polangen","Kaunas":"Kovno",
 "Kėdainiai":"Keidany","Šiauliai":"Shavli","Raseiniai":"Rossieny","Tauragė":"Tauroggen",
 "Marijampolė":"Mariampol","Alytus":"Olita","Radviliškis":"Radziwiliszki",
 "Kaliningrad":"Königsberg","Baltiysk":"Pillau","Primorsk":"Fischhausen",
 "Svetlogorsk":"Rauschen","Sovetsk":"Tilsit","Chernyakhovsk":"Insterburg","Gusev":"Gumbinnen",
 "Gdańsk":"Danzig","Gdynia":"Gdynia","Sopot":"Zoppot","Puck":"Putzig","Wejherowo":"Neustadt",
 "Elbląg":"Elbing","Malbork":"Marienburg","Tczew":"Dirschau","Olsztyn":"Allenstein",
 "Ełk":"Lyck","Giżycko":"Lötzen","Szczecin":"Stettin","Świnoujście":"Swinemünde",
 "Kołobrzeg":"Kolberg","Koszalin":"Köslin","Słupsk":"Stolp",
 "Hrodna":"Grodno","Vawkavysk":"Volkovysk","Brest":"Brest-Litovsk","Homel":"Gomel",
 "Mazyr":"Mozyr","Kobryn":"Kobrin","Baranavichy":"Baranovichi","Svetlahorsk":"Svetlogorsk",
 "Odesa":"Odessa","Chornomorsk":"Illichivsk","Bilhorod-Dnistrovskyi":"Akkerman",
 "Izmail":"Ismail","Uzhhorod":"Ungvár","Mukachevo":"Munkács",
 "Iași":"Jassy","Galați":"Galatz","Tulcea":"Tultcha","Constanța":"Kustendje",
 "Bistrița":"Bistritz","Oradea":"Grosswardein","Suceava":"Suczawa",
 "Pécs":"Fünfkirchen","Szombathely":"Steinamanger","Sopron":"Ödenburg","Győr":"Raab",
 "Szekszárd":"Sechshard","Nagykanizsa":"Grosskanizsa","Mosonmagyaróvár":"Ungarisch-Altenburg",
 "Graz":"Graz","Gorizia":"Görz","Pordenone":"Portenau","Koper":"Capodistria",
 "Piran":"Pirano","Izola":"Isola","Ankaran":"Ancarano","Idrija":"Idria","Tolmin":"Tolmein",
 "Ajdovščina":"Haidenschaft","Sežana":"Sesana","Divača":"Divaccia",
 "Pula":"Pola","Rovinj":"Rovigno","Poreč":"Parenzo","Umag":"Umago","Pazin":"Pisino",
 "Labin":"Albona","Buzet":"Pinguente","Rijeka":"Fiume","Opatija":"Abbazia","Krk":"Veglia",
 "Mali Lošinj":"Lussin","Senj":"Zengg","Zadar":"Zara","Šibenik":"Sebenico",
 "Split":"Spalato","Dubrovnik":"Ragusa",
 "Marseille":"Marseilles","Turin":"Turin","Milan":"Milan","Venice":"Venice","Padua":"Padua",
 "Mantua":"Mantua","Cuneo":"Coni","Aix-en-Provence":"Aix","Sion":"Sitten","Chur":"Coire",
 "Nesebar":"Mesembria","Sozopol":"Sozopolis","Edirne":"Adrianople",
 "Gotse Delchev":"Nevrokop","Blagoevgrad":"Gorna Dzhumaya","Kardzhali":"Kirdjali",
 "Vlorë":"Valona","Sarandë":"Santi Quaranta","Gjirokastër":"Argyrokastro","Korçë":"Koritza",
 "Përmet":"Premeti","Bitola":"Monastir","Kruševo":"Krushevo","Gevgelija":"Gevgeli",
 "Strumica":"Strumitsa","Radoviš":"Radovish",
 "Sevastopol":"Sevastopol",
 "Al Hudaydah":"Hodeidah","Sanaa":"Sana'a","Say'un":"Seiyun","Mukalla":"Al Mukalla",
}

# --- HINT: genuine historical / trade-route names offered to the generator ----
# as strong (raw loan) candidates. A hint is a candidate, never a decision.
HINT = {
 "Priozersk":"Kexhôlm","Chernyakhovsk":"Insterbôrk","Tczew":"Dirschau","Olsztyn":"Allenstein",
 "Świnoujście":"Svīnamündõ","Kołobrzeg":"Kôlbôrk","Bilhorod-Dnistrovskyi":"Akerman",
 "Koper":"Capodistria","Rijeka":"Fiume","Zadar":"Zara","Pula":"Pola","Šibenik":"Sebenico",
 "Krk":"Veglia","Bitola":"Monastir","Vlorë":"Valona","Nesebar":"Mesembria",
 "Gotse Delchev":"Nevrokop","Gjirokastër":"Argirocastro","Edirne":"Edirne",
 "Venice":"Venesia","Turin":"Torino","Milan":"Milano","Marseille":"Marselha","Nice":"Niça",
 "Toulon":"Tolon","Avignon":"Avinhon","Aix-en-Provence":"Ais",
}


# --- ANACHRONISM: real-world NAMES that cannot exist in this timeline ---------
# Soviet-era and Russian-imperial coinages. Nelôxia has held these places for
# ~500 years, so the renaming event never happened.
#
# IMPORTANT — this constrains the NAME, never the PLACE. The site is still there:
# the harbour, the confluence, the ore field, the isthmus. Even where the
# real-world settlement is a 20th-century purpose-built town, Nelôxia founds its
# own version — the state has always built new towns (Uusatôm is a founding,
# Gdynia is purpose-built). So a "would not exist" reference is not a dead end;
# it is a FOUNDING to be dated and attributed. See FOUNDING below.
#
# site -> (substrate candidate, why the real-world name is impossible)
ANACHRONISM = {
 "Petrozavodsk":("Petroskoi","Russian foundation 1703 — Peter the Great's ironworks ('Peter's factory'). Karelian form Petroskoi."),
 "Belomorsk":("Soroka","Soviet 1938 ('White-Sea-town'); the town was Soroka."),
 "Priozersk":("Käkisalmi","Soviet 1948; Karelian/Finnish Käkisalmi, Swedish Kexholm."),
 "Segezha":("Segeža","Soviet industrial foundation; Karelian form."),
 "Kostomuksha":("Kostamus","Soviet mining town, 1977; Karelian Kostamus."),
 "Kondopoga":("Kondupohja","Russified spelling; Karelian Kondupohja."),
 "Olonets":("Aunus","Russified; Karelian/Finnish Aunus."),
 "Kem":("Kemi","Russified; Karelian Kemi."),
 "Kaliningrad":("Königsberg","Soviet 1946, after Kalinin. The city was Königsberg."),
 "Baltiysk":("Pillau","Soviet 1946; the port was Pillau."),
 "Sovetsk":("Tilsit","Soviet 1946; the town was Tilsit."),
 "Svetlogorsk":("Rauschen","Soviet 1947; the resort was Rauschen."),
 "Primorsk":("Fischhausen","Soviet 1947; the town was Fischhausen."),
 "Chernyakhovsk":("Insterburg","Soviet 1946; the town was Insterburg."),
 "Gusev":("Gumbinnen","Soviet 1946; the town was Gumbinnen."),
 "Svetlahorsk":("Shatilki","Soviet 1961; the village was Shatilki."),
 "Chornomorsk":("Buhas","2016 rename of Illichivsk, itself a 1973 Soviet foundation."),
 "Dimitrovgrad":("Rakovski","Bulgarian 1947, after Georgi Dimitrov."),
 "Blagoevgrad":("Gorna Dzhumaya","Bulgarian 1950, after Dimitar Blagoev."),
 "Gotse Delchev":("Nevrokop","Bulgarian 1951; the town was Nevrokop."),
 "Sandanski":("Sveti Vrach","Bulgarian 1949; the town was Sveti Vrach."),
 "Stalowa Wola":("","Polish 1938 purpose-built steel town, so the name is not inherited — but the site is: San valley, forest, and the ore road. Nelôxia founds its own works town here; date it and name the founder."),
 "Bilhorod-Dnistrovskyi":("Akkerman","Soviet/Ukrainian rename; the fortress was Akkerman."),
 "Sevastopol":("Akhtiar","Russian foundation 1783; the Tatar village was Akhtiar."),
}

# --- SUBSTRATE: the in-world local name where a genuine one is on record ------
# Offered as a candidate for the `local` slot, never as a decision.
SUBSTRATE = {
 "Vyborg":"Viipuri", "Sortavala":"Sortavala", "Kuressaare":"Kuressaare",
 "Klaipėda":"Memel", "Gdańsk":"Danzig", "Szczecin":"Stettin",
 "Elbląg":"Elbing", "Malbork":"Marienburg", "Tczew":"Dirschau",
 "Olsztyn":"Allenstein", "Ełk":"Lyck", "Giżycko":"Lötzen",
 "Świnoujście":"Swinemünde", "Kołobrzeg":"Kolberg", "Koszalin":"Köslin",
 "Słupsk":"Stolp", "Gdynia":"Gdingen", "Sopot":"Zoppot", "Puck":"Putzig",
 "Hrodna":"Grodno", "Brest":"Brest-Litovsk", "Homel":"Homiel",
 "Kaunas":"Kaunas", "Trieste":"Trieste", "Koper":"Capodistria",
 "Rijeka":"Fiume", "Zadar":"Zara", "Pula":"Pola", "Šibenik":"Sebenico",
 "Split":"Spalato", "Dubrovnik":"Ragusa", "Krk":"Veglia",
 "Marseille":"Marselha", "Nice":"Niça", "Toulon":"Tolon",
 "Turin":"Torino", "Milan":"Milano", "Venice":"Venesia", "Padua":"Padova",
 "Bitola":"Monastir", "Vlorë":"Valona", "Gjirokastër":"Argirocastro",
 "Nesebar":"Mesembria", "Sozopol":"Sozopolis", "Edirne":"Edirne",
 "Iași":"Iași", "Constanța":"Köstence", "Uzhhorod":"Ungvár",
 "Mukachevo":"Munkács", "Pécs":"Fünfkirchen", "Sopron":"Ödenburg",
 "Győr":"Raab", "Szombathely":"Steinamanger",
}


# --- FOUNDING: is the in-world settlement inherited, or a Nelôxian foundation? -
# "inherited"  — an older settlement continues; it has a substrate name to keep
#                or digest, and the naming layers apply as normal.
# "foundation" — the real-world town is purpose-built (steel works, rail town,
#                canal town, planned port), so there is no inherited name. In
#                this timeline NELÔXIA founds it instead: pick the era, the
#                founder, and the reason. These sites want patron, event and
#                functional-descriptive names, not retained ones.
FOUNDING = {
 "Stalowa Wola": ("foundation", "steel and forest-industry works town"),
 "Segezha":      ("foundation", "canal-side timber and mill town"),
 "Kostomuksha":  ("foundation", "iron-ore field town at the frontier"),
 "Gdynia":       ("foundation", "purpose-built deepwater harbour beside an older rival port"),
 "Chornomorsk":  ("foundation", "planned deepwater container roads south of the liman"),
 "Svetlahorsk":  ("foundation", "chemical and power town at the Berezina crossing"),
 "Dimitrovgrad": ("foundation", "planned industrial town at the Maritsa crossing"),
 "Zhlobin":      ("foundation", "steelworks at the Dnieper crossing"),
 "Mielec":       ("foundation", "aviation works on the Wisłoka"),
 "Medgidia":     ("foundation", "town on the Danube–Black Sea canal"),
 "Nova Gorica":  ("foundation", "planned twin town at the border, facing Gorizia"),
 "Tarnobrzeg":   ("foundation", "sulphur-basin works town"),
 "Neringa":      ("foundation", "pilot station and dune-service settlement on the Spit"),
 "Sevastopol":   ("foundation", "naval station and Fleet seat, built for the purpose"),
}

# Eras a Nelôxian foundation can be dated to, with the flavour each implies.
FOUNDING_ERAS = [
 ("Hanseatic", "1300–1600", "a charter granted to a trading company; the works came before the town"),
 ("charter",   "1600–1800", "a crown or company foundation, laid out on a surveyor's grid"),
 ("rail",      "1800–1900", "a rail-and-industry foundation — the state built the line, then the town"),
 ("federal",   "1900–",     "a federal new town: planned housing, a technical school, and one industry"),
]


def rows():
    """CITIES joined with the name slots. Nothing here is settled: `site` is a
    real-world reference key, and local / nelox / exonym are open dockets unless
    explicitly on record."""
    out = []
    for site, region, cc, terrain, notes, pop in CITIES:
        nelox, layer, gloss = CANON.get(site, ("", "", ""))
        sub, why = ANACHRONISM.get(site, ("", ""))
        fkind, fwhat = FOUNDING.get(site, ("inherited", ""))
        out.append({
            "site": site, "region": region, "cc": cc, "terrain": terrain,
            "notes": notes, "pop": pop,
            # the Nelôxi endonym: on record (gazetteer.md) or open
            "nelox": nelox, "layer": layer, "gloss": gloss,
            "on_record": bool(nelox),
            "source": "gazetteer" if nelox else "",
            # The in-world local name. After five centuries of Nelôxian rule the
            # people there call the place by its Nelôxi name — so `local` FOLLOWS
            # `nelox` and is only distinct where a living local-language community
            # keeps its own form. The pre-Nelôxian name is `former`, not `local`.
            "local": nelox,
            "former": sub or SUBSTRATE.get(site, ""),
            # the outward-facing exonym: open; a historical form may be on record
            "exonym": "",
            "exonym_hint": EXONYM.get(site, ""),
            "hint": HINT.get(site, ""),
            # the real-world reference key cannot be the in-world name
            "anachronism": why,
            # inherited settlement, or a Nelôxian foundation to be dated?
            "founding": fkind, "founds_what": fwhat,
            "norename": region in NO_RENAME_REGIONS,
        })
    return out
