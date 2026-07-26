#!/usr/bin/env python3
"""Bring an already-built Nelôxi OOTP world up to the transoceanic expansion.

Stage 2 on top of build_world.py's output. Where build_world.py carves the
nine-region corridor state from a pristine base world_default.xml, this script
edits the ALREADY-BUILT file in place — no base file needed — applying the
twelve-region founder ratification in world/boundaries.md:

  Region 10  Western Alpine & Riviera Arc  — FR Provence-Alpes-Côte-d'Azur ·
             IT Piedmont, Lombardy, Veneto, Valle d'Aosta · CH Ticino, Valais,
             Graubünden
  Region 11  Thracian–Macedonian Corridor  — BG Burgas, Jambol, Haskovo,
             Kardzali, Smoljan, Blagoevgrad · TR Edirne · AL Vlorë, Gjirokastër,
             Korçë, Sarandë, Tepelenë, Përmet, Pogradec · MK Bitola, Prilep,
             Krusevo, Resen, Veles, Kavadarci, Negotino, Strumica, Radovis,
             Sveti Nikole, Gevgelija
  Region 12  Yemeni Commonwealth           — the whole of nation 214 (Yemen),
             absorbed as a constituent transoceanic state; nation removed and
             its baseball name-pool REGION_NATION refs repointed at Nelôxia
  Federal    Sevastopol                    — state 9174 taken from Sarmatia
             (267) as a Nelôxian naval enclave; Sarmatia keeps the rest of Crimea

Also: marquee city renames per world/gazetteer.md (Marsēl, Nissô, Torīnô,
Milān, Venēsiô, Monastir, Valonô, …), Nelôxia's population set to the ratified
≈148,000,000, and the source nations' populations reduced by what they lost.

Idempotent: re-running detects the expansion is already applied and stops.

Usage: python3 expand_transoceanic.py <world.xml>   (edits in place)
"""

import sys
import xml.etree.ElementTree as ET

NELOXIA = "260"
SARMATIA = "267"
YEMEN = "214"

# ---------------------------------------------------------------- region plan
# (region name, abbr, ratified pop, [(source nation id, state id), ...])
REGIONS = [
    ("The Western Alpine & Riviera Arc", "WAR", 22000000, [
        ("70", "1162"),                                     # Provence-Alpes-Côte-d'Azur
        ("95", "1586"), ("95", "1584"), ("95", "1592"),      # Piedmont, Lombardy, Veneto
        ("95", "1602"),                                     # Valle d'Aosta
        ("186", "2883"), ("186", "2882"), ("186", "2881"),   # Ticino, Valais, Graubünden
    ]),
    ("The Thracian-Macedonian Corridor", "THM", 7000000, [
        ("31", "546"), ("31", "556"), ("31", "554"),          # Burgas, Jambol, Haskovo
        ("31", "563"), ("31", "567"), ("31", "557"),          # Kardzali, Smoljan, Blagoevgrad
        ("199", "3127"),                                     # Edirne (Eastern Thrace)
        ("2", "36"), ("2", "45"), ("2", "39"), ("2", "52"),   # Vlorë, Gjirokastër, Korçë, Sarandë
        ("2", "55"), ("2", "58"), ("2", "43"),                # Tepelenë, Përmet, Pogradec
        ("66", "1880"), ("66", "1881"), ("66", "1905"),       # Bitola, Prilep, Krusevo
        ("66", "1900"), ("66", "1883"), ("66", "1888"),       # Resen, Veles, Kavadarci
        ("66", "1895"), ("66", "1887"), ("66", "1892"),       # Negotino, Strumica, Radovis
        ("66", "1896"), ("66", "1894"),                       # Sveti Nikole, Gevgelija
    ]),
]

# The Yemeni Commonwealth: every state of nation 214, kept as its own region.
YEMEN_REGION = ("The Yemeni Commonwealth", "YEM", 38000000)

# The federal city, carved out of Sarmatia's Crimea.
FEDERAL_CITY = (SARMATIA, "9174", "Sevastopol - Federal City", "SVP", 1000000)

# Marquee city renames (gazetteer.md naming layers). id -> Nelôxi name.
RENAMES = {
    # Region 10 — Occitan/Provençal + Italian/Venetian
    "Marseille": "Marsēl", "Nice": "Nissô", "Toulon": "Tolon",
    "Avignon": "Avinjon", "Aix-en-Provence": "Ais", "Cannes": "Kanô",
    "Antibes": "Antibô",
    "Torino": "Torīnô", "Turin": "Torīnô",
    "Milano": "Milān", "Milan": "Milān",
    "Venezia": "Venēsiô", "Venice": "Venēsiô",
    "Como": "Kômô",
    # Region 11 — Ottoman/Greek/Albanian route-names
    "Bitola": "Monastir", "Vlorë": "Valonô", "Vlore": "Valonô",
    "Gjirokastër": "Argirokastrô", "Gjirokaster": "Argirokastrô",
    "Korçë": "Korça", "Korce": "Korça",
    "Nesebar": "Mesembriô", "Nesebár": "Mesembriô",
    "Sozopol": "Sozôpôl",
    # Federal city
    "Sevastopol": "Sevastôpôl",
}

NEW_STATE_ID = 9210          # above the file's max (9202)
RATIFIED_POP = 148000000

# Canon city populations (settlements.html / the working model). The base file
# carries real-world figures; the federation's alternate history is much larger,
# and Aden in particular is the federal gateway, not a 550K colonial port.
POP_OVERRIDES = {
    # Yemeni Commonwealth
    "Aden": 6500000, "Sana": 3600000, "Taizz": 1300000,
    "al-Hudaydah": 1300000, "Ibb": 700000, "al-Mukalla": 500000,
    "Ðamar": 320000,
    # Region 10 marquee (post-rename names)
    "Milān": 3500000, "Torīnô": 1700000, "Marsēl": 1800000,
    "Nissô": 700000, "Venēsiô": 600000, "Tolon": 420000,
    # Region 11 / federal city
    "Monastir": 110000, "Valonô": 180000, "Sevastôpôl": 800000,
}


def abbr_for(name):
    a = "".join(c for c in name.upper() if c.isalpha())[:3]
    return a or "XXX"


def main(path):
    ET.register_namespace("", "")
    tree = ET.parse(path)
    root = tree.getroot()

    nations = {n.get("id"): n for n in root.iter("NATION")}
    parent_of_nation = {}
    for holder in root.iter("NATIONS"):
        for n in holder.findall("NATION"):
            parent_of_nation[n.get("id")] = holder

    nx = nations.get(NELOXIA)
    if nx is None:
        sys.exit("nation 260 (Nelôxia) not found — run build_world.py first")
    nx_states = nx.find("STATES")

    existing = {s.get("name") for s in nx_states.findall("STATE")}
    if "The Yemeni Commonwealth" in existing:
        print("already expanded (Yemeni Commonwealth present) — nothing to do")
        return

    global NEW_STATE_ID
    renamed = 0
    repopped = 0
    moved_states = 0

    def apply_renames(state_el):
        """Rename marquee cities, then apply canon populations (post-rename)."""
        nonlocal renamed, repopped
        for city in state_el.iter("CITY"):
            new = RENAMES.get(city.get("name"))
            if new:
                city.set("name", new)
                city.set("abbr", abbr_for(new))
                for k in ("name_korean", "abbr_korean"):
                    city.attrib.pop(k, None)
                renamed += 1
            pop = POP_OVERRIDES.get(city.get("name"))
            if pop:
                city.set("pop", str(pop))
                repopped += 1

    def take(nid, sid):
        """Detach state sid from nation nid; return (element, pop)."""
        nonlocal moved_states
        src = nations.get(nid)
        if src is None:
            print(f"  ! nation {nid} missing, skipping {sid}")
            return None, 0
        holder = src.find("STATES")
        for st in holder.findall("STATE"):
            if st.get("id") == sid:
                holder.remove(st)
                pop = int(st.get("pop") or 0)
                src.set("pop", str(max(0, int(src.get("pop") or 0) - pop)))
                moved_states += 1
                return st, pop
        print(f"  ! state {sid} not found in nation {nid}")
        return None, 0

    def merged_region(name, abbr, pop, takes):
        """One Nelôxian region built from the cities of several source states."""
        cities = []
        for nid, sid in takes:
            st, _ = take(nid, sid)
            if st is None:
                continue
            apply_renames(st)
            wrap = st.find("CITIES")
            cities += list(wrap.findall("CITY")) if wrap is not None else []
        st_el = ET.SubElement(nx_states, "STATE")
        st_el.set("id", str(NEW_STATE_ID))
        st_el.set("name", name)
        st_el.set("pop", str(pop))
        st_el.set("abbr", abbr)
        wrap = ET.SubElement(st_el, "CITIES")
        for c in cities:
            wrap.append(c)
        print(f"  + {name}: {len(cities)} cities, pop {pop:,}")
        return st_el

    print(f"expanding {path} to the transoceanic canon")

    # --- Regions 10 and 11 -------------------------------------------------
    for name, abbr, pop, takes in REGIONS:
        merged_region(name, abbr, pop, takes)
        NEW_STATE_ID += 1

    # --- Region 12: absorb Yemen entirely ----------------------------------
    ye = nations.get(YEMEN)
    if ye is not None:
        cities = []
        holder = ye.find("STATES")
        for st in list(holder.findall("STATE")):
            apply_renames(st)
            wrap = st.find("CITIES")
            cities += list(wrap.findall("CITY")) if wrap is not None else []
            holder.remove(st)
            moved_states += 1
        name, abbr, pop = YEMEN_REGION
        st_el = ET.SubElement(nx_states, "STATE")
        st_el.set("id", str(NEW_STATE_ID)); NEW_STATE_ID += 1
        st_el.set("name", name); st_el.set("pop", str(pop))
        st_el.set("abbr", abbr)
        wrap = ET.SubElement(st_el, "CITIES")
        for c in cities:
            wrap.append(c)
        print(f"  + {name}: {len(cities)} cities, pop {pop:,} (nation 214 absorbed)")
        # remove the now-empty Yemen nation
        parent_of_nation[YEMEN].remove(ye)
        # repoint its baseball name-pool region refs at Nelôxia
        repointed = 0
        for reg in root.iter("REGION_NATIONS"):
            for rn in reg.findall("REGION_NATION"):
                if rn.get("id") == YEMEN:
                    rn.set("id", NELOXIA)
                    repointed += 1
        print(f"    repointed {repointed} REGION_NATION refs 214 -> 260")
    else:
        print("  ! nation 214 (Yemen) already absent")

    # --- The federal city --------------------------------------------------
    nid, sid, fname, fabbr, fpop = FEDERAL_CITY
    st, _ = take(nid, sid)
    if st is not None:
        apply_renames(st)
        st.set("name", fname)
        st.set("abbr", fabbr)
        st.set("pop", str(fpop))
        for k in ("name_korean", "abbr_korean"):
            st.attrib.pop(k, None)
        nx_states.append(st)
        print(f"  + {fname}: taken from nation {nid} as a Nelôxian enclave")

    # --- National population ----------------------------------------------
    nx.set("pop", str(RATIFIED_POP))

    total_states = len(nx_states.findall("STATE"))
    print(f"  Nelôxia: {total_states} states, pop {RATIFIED_POP:,}")
    print(f"  moved {moved_states} source states, renamed {renamed} cities, "
          f"set {repopped} canon populations")

    ET.indent(tree, space="  ")
    tree.write(path, encoding="UTF-8", xml_declaration=True)
    print(f"wrote {path}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "world_default_neloxi.xml")
