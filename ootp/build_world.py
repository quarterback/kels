#!/usr/bin/env python3
"""Build the Nelôxi-world OOTP world file from a base world_default XML.

Adds the eight sovereign nations of the settled world layer (world/*.md) and
removes/carves the real-world places they are based on:

  260 Nelôxia          — the nine ratified regions (boundaries.md)
  261 Skaria           — the Nordic breakaway republic (skaria-lore.md)
  262 Atlanta          — Atlantic Sahara, replaces Western Sahara (atlanta-lore.md)
  263 Adrāra           — the Bidhan north of old Mauritania (african-bloc.md)
  264 Soninka & Toro   — the river south of old Mauritania + North Senegal
  265 Valdória         — the southern-cone settler republic (valdoria-lore.md)
  266 Meridian States  — the transoceanic federation (meridian-states.md)
  267 East Neloxia     — provisional name; Crimea–Caucasus–Caspian span (east/east.md)

  268 Zaryanova        — the Black-majority Pacific great power (zaryanova.md)
  269 Tarun            — the unified Turkic bloc (neighbor-states.md)
  270 Qazania          — Idel-Ural realised: Tatarstan+Bashkortostan

Also: Puerto Rico, the Northern Marianas, Guam, and the US Virgin Islands are
folded into The United States as states; Macau joins the Meridian States (Magau);
West Virginia is renamed Appalachia and gains its border towns. Kuwait and
Morocco stay sovereign (aligned, not absorbed).

Built for the "Enhanced Complete World Names" base (Korean-localized, richer
Latino ethnicity table, ships with names.xml/namescustom.xml). Name generation
is driven by each nation's ethnicity (etid) mix, chosen to read culturally.

ID policy: new nation ids 260–270, new state ids 9101+, new city ids 150001+ —
all above the base file's maxima (252 / 3400 / 95477), so nothing collides.

Usage: python3 build_world.py <input.xml> <output.xml>
"""

import re
import sys

# ---------------------------------------------------------------- id counters
NEW_STATE_ID = 9101
NEW_CITY_ID = 150001


def next_state_id():
    global NEW_STATE_ID
    NEW_STATE_ID += 1
    return NEW_STATE_ID - 1


def next_city_id():
    global NEW_CITY_ID
    NEW_CITY_ID += 1
    return NEW_CITY_ID - 1


# ------------------------------------------------------------------- parsing
def parse(lines):
    """Index continents, nations, and states by scanning the line list."""
    continents = {}   # name -> {"nations_end": line index of </NATIONS>}
    nations = {}      # id -> dict
    cur_cont = None
    cur_nat = None
    cur_state = None
    for i, l in enumerate(lines):
        m = re.search(r'<CONTINENT id="(\d+)" name="([^"]+)"', l)
        if m:
            cur_cont = m.group(2)
            continents[cur_cont] = {}
            continue
        if "</NATIONS>" in l and cur_cont:
            continents[cur_cont]["nations_end"] = i
        m = re.search(r'<NATION id="(\d+)" name="([^"]+)"', l)
        if m:
            cur_nat = int(m.group(1))
            nations[cur_nat] = {
                "name": m.group(2), "start": i, "end": None,
                "continent": cur_cont, "states": {}, "pop_line": i,
            }
            continue
        if cur_nat is not None and re.search(r"^\s*</NATION>\s*$", l):
            nations[cur_nat]["end"] = i
            cur_nat = None
            continue
        m = re.search(r'<STATE id="(\d+)" name="([^"]+)".*? pop="(\d+)"', l)
        if m and cur_nat is not None:
            cur_state = (int(m.group(1)), i)
            continue
        if cur_state and "</STATE>" in l and cur_nat is not None:
            sid, s_start = cur_state
            sm = re.search(r'<STATE id="\d+" name="([^"]+)".*? pop="(\d+)"',
                           lines[s_start])
            # first occurrence wins (dup ids exist in user customizations)
            nations[cur_nat]["states"].setdefault(sid, {
                "name": sm.group(1), "pop": int(sm.group(2)),
                "start": s_start, "end": i,
            })
            cur_state = None
    return continents, nations


def city_lines(lines, st):
    """The raw <CITY .../> lines of a state block."""
    return [lines[i] for i in range(st["start"], st["end"] + 1)
            if "<CITY " in lines[i]]


def strip_korean(l):
    return re.sub(r' (?:name|abbr|dem|short)_korean="[^"]*"', "", l)


def set_attr(line, attr, value):
    if re.search(rf'{attr}="[^"]*"', line):
        return re.sub(rf'{attr}="[^"]*"', f'{attr}="{value}"', line, count=1)
    return line


def rename_city(l, new_name):
    l = strip_korean(l)
    l = re.sub(r'name="[^"]*"', f'name="{new_name}"', l, count=1)
    abbr = re.sub(r"[^A-Za-z]", "", new_name.upper())[:3] or "XXX"
    l = re.sub(r'abbr="[^"]*"', f'abbr="{abbr}"', l, count=1)
    return l


def make_city(name, pop, lat, lon, cid=None):
    cid = cid or next_city_id()
    abbr = re.sub(r"[^A-Za-z]", "", name.upper())[:3] or "XXX"
    return (f'                <CITY id="{cid}" name="{name}" pop="{pop}" '
            f'lat="{lat}" long="{lon}" abbr="{abbr}" />\n')


def indent_city(l):
    return "                " + l.lstrip()


def xml_escape(name):
    return re.sub(r"&(?!amp;)", "&amp;", name)


def state_block(sid, name, pop, cities, abbr=None, tz=None):
    abbr = abbr or re.sub(r"[^A-Za-z]", "", name.upper())[:3]
    name = xml_escape(name)
    tzs = f' time_zone="{tz}"' if tz is not None else ""
    out = [f'            <STATE id="{sid}" name="{name}" pop="{pop}" '
           f'abbr="{abbr}"{tzs}>\n', "              <CITIES>\n"]
    out += [indent_city(c) for c in cities]
    out += ["              </CITIES>\n", "            </STATE>\n"]
    return out


def nation_block(nid, name, pop, etid, capid, gender, bbqual, abbr, dem, tz,
                 ethn, states, second=None, dst=False, short=None):
    dsts = ' observes_dst="1"' if dst else ""
    shorts = f' short="{short}"' if short else ""
    out = [f'        <NATION id="{nid}" name="{name}" pop="{pop}" '
           f'etid="{etid}" capid="{capid}" gender="{gender}" '
           f'bbqual="{bbqual}" abbr="{abbr}" dem="{dem}" '
           f'time_zone="{tz}"{dsts}{shorts}>\n']
    if second:
        out.append("          <SECOND_NATIONS>\n")
        for sid_, pct in second:
            out.append(f'            <SECOND_NATIONS id="{sid_}" pct="{pct}" '
                       f'use_name="0" />\n')
        out.append("          </SECOND_NATIONS>\n")
    else:
        out.append("          <SECOND_NATIONS />\n")
    out.append("          <ETHN_PCTS>\n")
    for e, p in ethn:
        out.append(f'            <ETHN_PCT etid="{e}" pct="{p}" />\n')
    out.append("          </ETHN_PCTS>\n          <STATES>\n")
    for s in states:
        out += s
    out.append(f"          </STATES>\n          <CAPITAL id=\"{capid}\" />\n"
               "        </NATION>\n")
    return out


def main(src, dst):
    lines = open(src, encoding="utf-8").readlines()
    continents, nations = parse(lines)

    def nat_by_name(name, continent=None):
        for nid, n in nations.items():
            if n["name"] == name and (continent is None
                                      or n["continent"] == continent):
                return nid, n
        raise KeyError(name)

    delete = set()          # line indices to drop
    pop_deltas = {}         # nation id -> pop to subtract
    renames = {}            # city id -> new name (applied to extracted lines)
    pop_overrides = {}      # city id -> new pop  (applied to extracted lines)

    def take_state(nid, sid):
        """Remove a state from its nation; return its city lines + pop."""
        st = nations[nid]["states"][sid]
        for i in range(st["start"], st["end"] + 1):
            delete.add(i)
        pop_deltas[nid] = pop_deltas.get(nid, 0) + st["pop"]
        return city_lines(lines, st), st["pop"]

    def take_city(nid, sid, cid):
        """Remove one city line from a state that otherwise stays."""
        st = nations[nid]["states"][sid]
        for i in range(st["start"], st["end"] + 1):
            m = re.search(r'<CITY id="(\d+)"', lines[i])
            if m and int(m.group(1)) == cid:
                delete.add(i)
                pm = re.search(r'pop="(\d+)"', lines[i])
                pop = int(pm.group(1))
                pop_deltas[nid] = pop_deltas.get(nid, 0) + pop
                # shrink the host state's pop attribute
                lines[st["start"]] = set_attr(
                    lines[st["start"]], "pop",
                    max(0, int(re.search(r'pop="(\d+)"',
                                         lines[st["start"]]).group(1)) - pop))
                return lines[i]
        raise KeyError((nid, sid, cid))

    def remove_nation(nid):
        n = nations[nid]
        for i in range(n["start"], n["end"] + 1):
            delete.add(i)
        return n

    def finish_cities(cls, fresh_ids=False):
        """Strip Korean attrs, apply renames/pop overrides, optionally re-id."""
        out = []
        for l in cls:
            l = strip_korean(l)
            m = re.search(r'<CITY id="(\d+)"', l)
            cid = int(m.group(1))
            if cid in renames:
                l = rename_city(l, renames[cid])
            if cid in pop_overrides:
                l = set_attr(l, "pop", pop_overrides[cid])
            if fresh_ids:
                l = re.sub(r'<CITY id="\d+"', f'<CITY id="{next_city_id()}"',
                           l, count=1)
            out.append(l)
        return out

    RU, _ = nat_by_name("Russia")
    EE, _ = nat_by_name("Estonia"); LV, _ = nat_by_name("Latvia")
    LT, _ = nat_by_name("Lithuania"); PL, _ = nat_by_name("Poland")
    BY, _ = nat_by_name("Belarus"); SK, _ = nat_by_name("Slovakia")
    UA, _ = nat_by_name("Ukraine"); RO, _ = nat_by_name("Romania")
    BG, _ = nat_by_name("Bulgaria"); HU, _ = nat_by_name("Hungary")
    AT, _ = nat_by_name("Austria"); IT, _ = nat_by_name("Italy")
    SI, _ = nat_by_name("Slovenia"); HR, _ = nat_by_name("Croatia")
    DK, _ = nat_by_name("Denmark"); NO, _ = nat_by_name("Norway")
    SE, _ = nat_by_name("Sweden"); FI, _ = nat_by_name("Finland")
    ES, _ = nat_by_name("Spain"); FR, _ = nat_by_name("France")
    DZ, _ = nat_by_name("Algeria"); SN, _ = nat_by_name("Senegal")
    BR, _ = nat_by_name("Brazil"); AR, _ = nat_by_name("Argentina")
    PY, _ = nat_by_name("Paraguay"); BO, _ = nat_by_name("Bolivia")
    CL, _ = nat_by_name("Chile"); UY, _ = nat_by_name("Uruguay")
    KZ, _ = nat_by_name("Kazakhstan"); UZ, _ = nat_by_name("Uzbekistan")
    TM, _ = nat_by_name("Turkmenistan"); KG, _ = nat_by_name("Kyrgyzstan")
    CN, _ = nat_by_name("China")

    # ============================================== 260 NELÔXIA (Europe)
    # marquee renames from world/gazetteer.md
    renames.update({
        58601: "Petrôsô", 84818: "Vīpôri", 75183: "Sôrtô", 8438: "Korbitô",
        57247: "Järvemō", 39437: "Koskenbōrk",
        38968: "Māmeli", 77516: "Xauli", 54745: "Neikūri", 65099: "Rosēni",
        35985: "Keidani",
        36558: "Kunislinnô", 6651: "Pillô", 75491: "Tilsit",
        60996: "Fischūsô", 65959: "Rauschenbôrk",
        27996: "Tantsika", 47214: "Marianbôrk", 61257: "Puka",
        77335: "Stetīn", 23313: "Elbinki",
        32756: "Marīsô", 84299: "Volkovixi",
        56811: "Uusatôm", 14885: "Kôstônç",
        29632: "Gräts", 81119: "Triest", 75636: "Spalôt", 19791: "Ragūz",
    })
    pop_overrides[36558] = 1500000  # the capital basin (lore: metro 5-6M)

    def merged_state(name, abbr, pop, takes):
        cls = []
        for nid, sid in takes:
            c, _ = take_state(nid, sid)
            cls += c
        return state_block(next_state_id(), name, pop,
                           finish_cities(cls), abbr=abbr)

    nx_states = [
        merged_state("Karelia & the North", "KAR", 6500000,
                     [(RU, 2570), (RU, 2589)]),
        merged_state("The Livonian Core", "LIV", 1750000,
                     [(EE, 1095), (EE, 1103), (EE, 1096), (EE, 1097),
                      (EE, 1100), (LV, 1781), (LV, 1779), (LV, 1778),
                      (LV, 1783)]),
        merged_state("The Lithuanian Spine", "LIT", 3500000,
                     [(LT, 1858), (LT, 1865), (LT, 1859), (LT, 1857),
                      (LT, 1861)]),
        merged_state("The Prussian-Pomeranian Coast", "PRU", 17000000,
                     [(RU, 2547), (PL, 2423), (PL, 2424), (PL, 2430)]),
        merged_state("The Eastern Corridor", "COR", 17000000,
                     [(BY, 425), (BY, 426), (BY, 422), (PL, 2426),
                      (PL, 2431), (SK, 2673)]),
        merged_state("The Moldavian Arc & the Black Sea", "MOL", 15000000,
                     [(UA, 3203), (UA, 3180), (RO, 2490), (RO, 2487),
                      (RO, 2470), (RO, 2500), (RO, 2475), (RO, 2497),
                      (RO, 2479), (RO, 2495), (RO, 2474), (RO, 2510),
                      (BG, 551)]),
        merged_state("The Pannonian Bridge", "PAN", 5500000,
                     [(HU, 1420), (HU, 1410), (HU, 1414), (HU, 1426),
                      (HU, 1411), (HU, 1419), (HU, 1421), (HU, 1416),
                      (HU, 1412)]),
        merged_state("The Alpine-Adriatic Arm", "ALP", 7500000,
                     [(AT, 257), (AT, 250), (AT, 254), (IT, 1593),
                      (SI, 2684), (SI, 2689)]),
        merged_state("The Dalmatian Coast", "DAL", 2750000,
                     [(HR, 862), (HR, 847), (HR, 852), (HR, 844),
                      (HR, 856)]),
    ]
    neloxia = nation_block(
        260, "Nelôxia", 76000000, 50, 36558, 1, 2, "NEL", "Nelôxian", 2,
        [(50, 14), (51, 8), (52, 10), (15, 14), (13, 10), (49, 8), (48, 6),
         (7, 7), (28, 8), (35, 6), (183, 4), (11, 3), (25, 2)],
        nx_states, dst=True, short="Nelôxia")

    # ============================================== 261 SKARIA (Europe)
    sk_takes = [(DK, s) for s in (902, 900, 908, 899, 903, 904, 911, 901)]
    sk_takes += [(NO, s) for s in (2313, 2314, 2304)]
    sk_takes += [(SE, s) for s in (2851, 2861, 2850, 2868, 2867, 2869)]
    sk_takes += [(FI, s) for s in (1148, 1150, 1159, 1156)]
    sk_states = []
    for nid, sid in sk_takes:
        st = nations[nid]["states"][sid]
        cls, pop = take_state(nid, sid)
        sk_states.append(state_block(next_state_id(), st["name"], pop,
                                     finish_cities(cls)))
    skaria = nation_block(
        261, "Skaria", 9300000, 12, 27329, 1, 1, "SKA", "Skarian", 1,
        [(12, 35), (25, 30), (11, 20), (10, 15)],
        sk_states, dst=True, short="Skaria")

    # ============================================== 262 ATLANTA (Africa)
    ws = remove_nation(nat_by_name("Western Sahara")[0])
    ws_cities = {}
    for sid, st in ws["states"].items():
        for l in city_lines(lines, st):
            cid = int(re.search(r'<CITY id="(\d+)"', l).group(1))
            ws_cities[cid] = l
    renames.update({964: "Fôntāna", 2186: "Daxla", 4322: "Santsmāra",
                    5431: "Buždūr", 78629: "Ṭarfāya"})
    pop_overrides.update({964: 520000, 2186: 260000})
    north = finish_cities([ws_cities[964], ws_cities[23143], ws_cities[78629],
                           ws_cities[4322], ws_cities[5431]])
    north += [make_city("Xawza", 12000, "27.15", "-11.15"),
              make_city("Maxbəs", 8000, "27.10", "-9.10"),
              make_city("Fərsīya", 6000, "26.90", "-10.55")]
    south = finish_cities([ws_cities[2186]])
    south += [make_city("Awsərd", 15000, "22.55", "-14.33"),
              make_city("Tixla", 7000, "21.60", "-14.85"),
              make_city("Zūg", 5000, "21.35", "-14.19"),
              make_city("Mīžək", 6000, "23.50", "-13.05"),
              make_city("Bīr Anzarān", 10000, "23.90", "-14.53"),
              make_city("Bīr Gandūs", 5000, "21.50", "-16.45"),
              make_city("Galt Zəmmūr", 9000, "25.13", "-12.37")]
    atlanta = nation_block(
        262, "Atlanta", 2800000, 53, 964, 0, 2, "ATL", "Atlantan", 0,
        [(53, 70), (17, 15), (87, 10), (50, 5)],
        [state_block(next_state_id(), "Pūnkanā", 1600000, north, abbr="PUN"),
         state_block(next_state_id(), "Kuldjôg", 1200000, south, abbr="KUL")],
        second=[(260, 10)])

    # ============================================== 263/264 old Mauritania
    MR, _ = nat_by_name("Mauritania")
    mr_states = dict(nations[MR]["states"])  # copy before removal
    remove_nation(MR)

    def mr_state(sid, rename=None):
        st = mr_states[sid]
        cls = finish_cities(city_lines(lines, st))
        return state_block(next_state_id(), rename or st["name"], st["pop"],
                           cls)

    # Adrāra — the Bidhan north; Atar + Chinguetti are misfiled in Algeria's
    # Adrar state in the base file (Mauritanian coordinates) — reclaim them.
    atar = take_city(DZ, 101, 116)
    singati = take_city(DZ, 101, 77524)
    renames[77524] = "Chinguetti"
    adrar_cities = finish_cities([atar, singati])
    adrar_cities += [make_city("Ouadane", 4000, "20.93", "-11.62"),
                     make_city("Choum", 3000, "21.30", "-13.02")]
    ad_states = [mr_state(s) for s in (1997, 1998, 2002, 2008, 2007, 1999,
                                       2003, 2006)]
    ad_states.append(state_block(next_state_id(), "Adrār", 90000,
                                 adrar_cities, abbr="ADR"))
    adrara = nation_block(
        263, "Adrāra", 1900000, 119, 116, 0, 1, "ADR", "Adrāri", 0,
        [(119, 85), (53, 10), (132, 5)],
        ad_states, second=[(262, 5)])

    # Soninka & Toro — the river state
    renames[68511] = "Ndar"
    pop_overrides[68511] = 220000
    renames[6323] = "Bakəl"
    walo_c, _ = take_state(SN, 2658)          # Saint-Louis region
    trarza = mr_states[2000]
    walo_cities = finish_cities(city_lines(lines, trarza) + walo_c)
    for i in range(trarza["start"], trarza["end"] + 1):
        delete.add(i)
    walo_cities.append(make_city("Lumo-Wālo", 5000, "16.20", "-14.40"))
    futa_cities = []
    for sid in (2005, 2001):
        st = mr_states[sid]
        futa_cities += city_lines(lines, st)
        for i in range(st["start"], st["end"] + 1):
            delete.add(i)
    matam_c, _ = take_state(SN, 2665)
    futa_cities = finish_cities(futa_cities + matam_c)
    gaj = mr_states[2004]
    gaj_cities = city_lines(lines, gaj)
    for i in range(gaj["start"], gaj["end"] + 1):
        delete.add(i)
    gaj_cities = finish_cities(gaj_cities + [take_city(SN, 2662, 6323)])
    gaj_cities += [make_city("Sanudugu", 18000, "13.10", "-11.75"),
                   make_city("Kolon-Sira", 4000, "15.25", "-12.17")]
    sotoro = nation_block(
        264, "Soninka &amp; Toro", 4200000, 132, 68511, 0, 1, "SOT",
        "Sotoran", 0,
        [(132, 70), (119, 15), (130, 15)],
        [state_block(next_state_id(), "Wālo", 1600000, walo_cities,
                     abbr="WAL"),
         state_block(next_state_id(), "Futa", 1500000, futa_cities,
                     abbr="FUT"),
         state_block(next_state_id(), "Gajāga", 1100000, gaj_cities,
                     abbr="GAJ")],
        second=[(SN, 10)])

    # ============================================== 265 VALDÓRIA (S. America)
    renames.update({60516: "Portô Venla", 63518: "Santa Laura"})
    pop_overrides[60516] = 1650000
    vd_map = [
        (BR, 520, "Rīu Grandē"), (BR, 530, "Santa Katarīna"),
        (UY, 3217, "Roçā"), (AR, 214, "Korentē"), (AR, 215, "Misjôn"),
        (AR, 219, "Formôsa"), (AR, 210, "Salta"), (AR, 216, "Huhūi"),
        (PY, 2381, "Itapūa"), (PY, 2387, "Ñeʼembukū"),
        (BO, 481, "Tariha"), (BO, 482, "Potosī"), (CL, 734, "Litorāl"),
    ]
    vd_states = []
    for nid, sid, newname in vd_map:
        st = nations[nid]["states"][sid]
        cls, pop = take_state(nid, sid)
        cls = finish_cities(cls)
        if newname == "Rīu Grandē":
            cls.append(make_city("Koinīnia", 42000, "-29.68", "-53.80"))
        vd_states.append(state_block(next_state_id(), newname, pop, cls))
    valdoria = nation_block(
        265, "Valdória", 34000000, 75, 60516, 0, 2, "VAL", "Valdórian", -3,
        [(75, 25), (80, 18), (70, 12), (5, 8), (7, 8), (15, 5), (48, 4),
         (9, 2), (38, 14), (67, 4)],
        vd_states, second=[(260, 3)], short="Valdória")

    # ============================================== 266 MERIDIAN STATES
    me_states = []
    # Canary Islands (from Spain) and Corsica (from France), states kept
    for nid, sid in ((ES, 2746), (ES, 2754), (FR, 1181)):
        st = nations[nid]["states"][sid]
        cls, pop = take_state(nid, sid)
        me_states.append(state_block(next_state_id(), st["name"], pop,
                                     finish_cities(cls)))

    def absorb(nation_name, state_name, fresh=False, extra=None,
               rename_pairs=None, abbr=None):
        nid, n = nat_by_name(nation_name)
        remove_nation(nid)
        cls = []
        for st in n["states"].values():
            cls += city_lines(lines, st)
        if rename_pairs:
            renames.update(rename_pairs)
        cls = finish_cities(cls, fresh_ids=fresh)
        if extra:
            cls += extra
        pop = sum(int(re.search(r'pop="(\d+)"', c).group(1)) for c in cls)
        me_states.append(state_block(next_state_id(), state_name, pop, cls,
                                     abbr=abbr))
        return nid

    # Esperanza gets FRESH city ids: the user's custom nation Montequinto
    # already carries copies of French Guiana's blocks under the original ids,
    # so re-idding here removes that duplication instead of adding to it.
    esperanza_renames = {18057: "Esperanza"}
    pop_overrides[18057] = 85000
    absorb("French Guiana", "Esperanza", fresh=True,
           rename_pairs=esperanza_renames, abbr="ESP")
    # find the fresh id Cayenne/Esperanza received (last state added)
    esp_cap = None
    for l in me_states[-1]:
        if 'name="Esperanza"' in l and "<CITY" in l:
            esp_cap = int(re.search(r'<CITY id="(\d+)"', l).group(1))
    absorb("Bermuda", "Bermuda",
           extra=[make_city("Hamilton", 54000, "32.29", "-64.78")],
           abbr="BER")
    absorb("São Tomé &amp; Principe", "São Tomé e Príncipe", abbr="STP")
    absorb("Saint-Pierre &amp; Miquelon", "Saint Pierre &amp; Miquelon",
           abbr="SPM")
    absorb("St. Helena", "Saint Helena", abbr="STH")
    absorb("Mayotte", "Mayotte", abbr="MAY")
    absorb("Wallis &amp; Futuna", "Wallis &amp; Futuna", abbr="WAF")
    absorb("New Caledonia", "New Caledonia", abbr="NCL")
    # Macau joins the Meridian States (user directive): its Aomen state
    # becomes Magau. Macau has only the one state in this base.
    MC, mc = nat_by_name("Macau")
    remove_nation(MC)
    renames[3496] = "Magau"
    aomen = mc["states"][776]
    me_states.append(state_block(776, "Magau", aomen["pop"],
                                 finish_cities(city_lines(lines, aomen)),
                                 abbr="MAG", tz=8))
    # ZARYANOVA — the Black-majority Pacific great power (world/zaryanova.md):
    # ONE country spanning the whole Russian Far East, carved from the real
    # oblasts: Primorsky, Khabarovsk, Kamchatka, Sakhalin & the Kurils,
    # Magadan, the Jewish AO, and Chukotka (the doc's UTC+9..+13 /
    # 180°-meridian span). Capital Gannibal (the purpose-built city, here the
    # renamed Yuzhno-Sakhalinsk); largest city Pushkin (renamed Vladivostok);
    # Vorota, the DPRK gateway town, added on the Khasan border point.
    renames[80861] = "Gannibal"     # Yuzhno-Sakhalinsk → the built capital
    renames[85048] = "Pushkin"      # Vladivostok → the commercial capital
    pop_overrides[85048] = 1900000
    zy_states = []
    for sid, tz in ((2532, 10), (2534, 10), (2578, 12), (2579, 11),
                    (2588, 11), (2590, 10), (2597, 12)):
        st = nations[RU]["states"][sid]
        cls, pop = take_state(RU, sid)
        cls = finish_cities(cls)
        if sid == 2532:   # Primorsky — the DPRK gateway
            cls.append(make_city("Vorota", 85000, "42.43", "130.64"))
        zy_states.append(state_block(sid, st["name"], pop, cls, tz=tz))
    zaryanova = nation_block(
        268, "Zaryanova", 29863010, 38, 80861, 1, 4, "ZAR", "Zaryan", 10,
        [(38, 55), (13, 20), (3, 10), (4, 10), (2, 3), (47, 2)],
        zy_states, second=[(206, 8), (265, 2)], short="Zaryanova")

    # APPALACHIA — a canonical US state in this universe (West Virginia
    # renamed, expanded with the NC/KY/VA/TN/GA border country). The base
    # models it as state 167 "West Virginia"; rename it and pull in the 44
    # border towns (moved by id from their real states, so no city is
    # duplicated). The one bad Bristol-England id from the old data is left
    # in England.
    US, us = nat_by_name("The United States")
    APP_BORDER = {1974, 3585, 4411, 4431, 7906, 9388, 9880, 10727, 11612,
                  11771, 11773, 12073, 13272, 13615, 14135, 14310, 15034,
                  16002, 19029, 21804, 23389, 23391, 23413, 25736, 27492,
                  27914, 27922, 28621, 29762, 30709, 31132, 31405, 35189,
                  35558, 38596, 39092, 44834, 48295, 51837, 52665, 56311,
                  58957, 75739, 85549}
    app = us["states"][167]                       # base "West Virginia"
    lines[app["start"]] = set_attr(set_attr(lines[app["start"]],
                                            "name", "Appalachia"),
                                   "abbr", "AP")
    app_extra = []
    app_gain = 0
    for n2 in nations.values():
        for sid2, st2 in n2["states"].items():
            if sid2 == 167:
                continue
            for i in range(st2["start"], st2["end"] + 1):
                m = re.search(r'<CITY id="(\d+)".*? pop="(\d+)"', lines[i])
                if m and int(m.group(1)) in APP_BORDER:
                    delete.add(i)
                    app_extra.append(strip_korean(lines[i]))
                    app_gain += int(m.group(2))
                    lines[st2["start"]] = set_attr(
                        lines[st2["start"]], "pop",
                        max(0, int(re.search(r'pop="(\d+)"',
                                             lines[st2["start"]]).group(1))
                            - int(m.group(2))))
    # splice the border cities in just before the state's </CITIES>
    app_close = next(i for i in range(app["start"], app["end"] + 1)
                     if "</CITIES>" in lines[i])
    extra_ins = {app_close: [indent_city(c) for c in app_extra]}
    lines[app["start"]] = set_attr(
        lines[app["start"]], "pop",
        int(re.search(r'pop="(\d+)"', lines[app["start"]]).group(1))
        + app_gain)

    # US STATEHOOD FOR THE FOUR TERRITORIES (user directive). In this base
    # Puerto Rico (151), the Northern Marianas (229), Guam (79), and the US
    # Virgin Islands (202) are all separate nations. Each is dissolved into a
    # single new US state carrying all its cities; the US population grows by
    # what it gains, and each territory's "US TERRITORY" region is repointed
    # to the new state (below).
    us_new_states = []
    us_pop_add = 0
    us_annex_state = {}   # old nation id -> new US state id

    def annex_to_us(nation_name, state_name, abbr):
        nonlocal us_pop_add
        nid, n = nat_by_name(nation_name)
        cls = []
        state_pop = 0
        for st in n["states"].values():
            cls += city_lines(lines, st)
            state_pop += st["pop"]
        sid = next_state_id()
        us_new_states.extend(state_block(sid, state_name, state_pop,
                                         finish_cities(cls), abbr=abbr,
                                         tz=-4))
        us_pop_add += int(re.search(r'pop="(\d+)"',
                                    lines[n["pop_line"]]).group(1))
        us_annex_state[nid] = sid
        remove_nation(nid)

    annex_to_us("Puerto Rico", "Puerto Rico", "PR")
    annex_to_us("Northern Marianas", "Northern Mariana Islands", "MP")
    annex_to_us("Guam", "Guam", "GU")
    annex_to_us("Virgin Islands", "U.S. Virgin Islands", "VI")
    us_states_end = next(i for i in range(us["start"], us["end"] + 1)
                         if re.search(r"^\s*</STATES>\s*$", lines[i]))

    meridian = nation_block(
        266, "Meridian States", 4300000, 70, esp_cap, 0, 3, "MER",
        "Meridian", -3,
        [(70, 25), (8, 12), (42, 12), (217, 5), (144, 8), (96, 10),
         (159, 8), (101, 8), (112, 4), (20, 4), (46, 4)],
        me_states, second=[(260, 5)], short="Meridian States")

    # ============================================== 267 EAST NELOXIA
    # The Corridor State (world/east-neloxia.md, founder-ratified): the
    # northern/Caspian Silk Road held end to end — Caffa/Crimea with the
    # Kherson–Zaporizhzhia land bridge, the Caucasus gate (NO Ingushetia),
    # western Georgia, Astrakhan and the Volga hinge, Orenburg, the Caspian
    # east shore (west Kazakh oblasts, Balkan/Ahal), and the Herat–Makran
    # reach (Herat, Farah, Nimruz, Sistan-Baluchestan, Baluchistan).
    GE, _ = nat_by_name("Georgia")
    AF, _ = nat_by_name("Afghanistan")
    IR, _ = nat_by_name("Iran")
    PK, _ = nat_by_name("Pakistan")
    renames[25441] = "Caffa"
    pop_overrides[25441] = 180000
    en_takes = [(UA, s, None) for s in (3187, 3188, 3189, 3182)]
    en_takes += [(RU, s, None) for s in (2527, 2583, 2584, 2568, 2561,
                                         2577, 2542, 2552, 2586, 2541)]
    en_takes += [(RU, 2535, 5)]
    en_takes += [(GE, s, 3) for s in (1207, 1208, 1211, 1213)]
    en_takes += [(KZ, s, 5) for s in (1701, 1705, 1704)]
    en_takes += [(TM, s, 5) for s in (3172, 3173, 3168)]
    en_takes += [(AF, s, 4) for s in (4, 21, 23)]
    en_takes += [(IR, 1513, 4), (PK, 2329, 5)]
    en_states = []
    for nid, sid, tz in en_takes:
        st = nations[nid]["states"][sid]
        cls, pop = take_state(nid, sid)
        en_states.append(state_block(next_state_id(), st["name"], pop,
                                     finish_cities(cls), tz=tz))
    eastneloxia = nation_block(
        267, "East Neloxia", 29000000, 29, 25441, 1, 1, "ENX",
        "East Neloxian", 3,
        [(29, 15), (13, 14), (24, 12), (48, 10), (26, 5), (50, 6),
         (79, 8), (56, 5), (31, 8), (89, 9), (37, 8)],
        en_states, second=[(260, 15)], short="East Neloxia")

    # ==================== 269 TARUN & 270 QAZANIA (neighbor-states.md)
    # Tarun — the unified Turkic bloc: Kazakhstan (less the East Neloxian
    # west), all of Uzbekistan and Kyrgyzstan, Turkmenistan (less Balkan and
    # Ahal), and Xinjiang. Tajikistan stays independent. Capital: Tashkent
    # (largest city — the doc names no capital; placeholder).
    tr_takes = [(KZ, s) for s in (1692, 1693, 1694, 1695, 1696, 1697, 1698,
                                  1699, 1700, 1702, 1703)]
    tr_takes += [(UZ, s) for s in sorted(nations[UZ]["states"])]
    tr_takes += [(TM, s) for s in (3169, 3170, 3171, 3174)]
    tr_takes += [(KG, s) for s in sorted(nations[KG]["states"])]
    tr_takes += [(CN, 766)]
    tr_states = []
    for nid, sid in tr_takes:
        st = nations[nid]["states"][sid]
        cls, pop = take_state(nid, sid)
        tr_states.append(state_block(sid, st["name"], pop,
                                     finish_cities(cls)))
    tarun = nation_block(
        269, "Tarun", 68000000, 56, 78705, 0, 1, "TAR", "Taruni", 5,
        [(56, 35), (78, 20), (24, 20), (79, 15), (13, 10)],
        tr_states, short="Tarun")
    for nid in (KZ, UZ, TM, KG):
        remove_nation(nid)   # fully partitioned: Tarun + East Neloxia

    # Qazania — Idel-Ural realised: Tatarstan + Bashkortostan united.
    # Capital Kazan, demonym Qazani, ~8M, Turkic, Muslim, oil-rich.
    qz_states = []
    for sid, tz in ((2518, 3), (2521, 5)):
        st = nations[RU]["states"][sid]
        cls, pop = take_state(RU, sid)
        qz_states.append(state_block(sid, st["name"], pop,
                                     finish_cities(cls), tz=tz))
    qazania = nation_block(
        270, "Qazania", 8000000, 24, 37581, 1, 1, "QAZ", "Qazani", 3,
        [(24, 45), (13, 30), (73, 15), (79, 5), (56, 5)],
        qz_states, second=[(156, 10)], short="Qazania")

    # ============================== fix the duplicated Zephyria Oblast ids
    zeph_state_id = next_state_id()
    zeph_fix = {}
    in_zeph = False
    for i, l in enumerate(lines):
        if 'name="Zephyria Oblast"' in l:
            in_zeph = True
            lines[i] = re.sub(r'<STATE id="\d+"',
                              f'<STATE id="{zeph_state_id}"', l, count=1)
            continue
        if in_zeph:
            if "</STATE>" in l:
                break
            m = re.search(r'<CITY id="(\d+)"', l)
            if m:
                nc = next_city_id()
                zeph_fix[int(m.group(1))] = nc
                lines[i] = re.sub(r'<CITY id="\d+"', f'<CITY id="{nc}"', l,
                                  count=1)

    # ============================================== assemble output
    inserts = {
        continents["Europe"]["nations_end"]: neloxia + skaria + eastneloxia
                                            + qazania,
        continents["Africa"]["nations_end"]: atlanta + adrara + sotoro,
        continents["South America"]["nations_end"]: valdoria + meridian,
        mc["start"]: zaryanova + tarun,   # where Macau stood (Asia)
        us_states_end: us_new_states,     # the four territories as US states
    }
    inserts.update(extra_ins)             # Appalachia border cities
    # nation pop reductions
    for nid, delta in pop_deltas.items():
        if nations[nid]["end"] is None or nations[nid]["start"] in delete:
            continue
        i = nations[nid]["pop_line"]
        cur = int(re.search(r'pop="(\d+)"', lines[i]).group(1))
        lines[i] = set_attr(lines[i], "pop", max(0, cur - delta))
    # US gains the annexed-territory population
    up = us["pop_line"]
    lines[up] = set_attr(lines[up], "pop",
                         int(re.search(r'pop="(\d+)"',
                                       lines[up]).group(1)) + us_pop_add)

    # REGION_NATION remap: absorbed nation -> successor
    successor = {121: 263, 218: 262, 23: 266, 71: 266, 123: 266, 134: 266,
                 160: 266, 173: 266, 213: 266, 249: 266, 238: 266,
                 100: 269, 208: 269, 200: 269, 103: 269}
    # The four territories (Puerto Rico 151, Northern Marianas 229, Guam 79,
    # US Virgin Islands 202) became US states — drop their old nation-pool
    # refs (the US, already in the core USA regions, now carries them; each
    # territory region is repointed to its new state below). 29 is the old
    # Montequinto id (absent in this base; harmless).
    drop_refs = {29, 151, 229, 79, 202}
    # new nations join the sensible geographic regions (by REGION id)
    region_adds = {44: [260, 261, 267], 48: [260, 261], 46: [260, 267],
                   56: [262, 263, 264], 57: [262, 263], 58: [264],
                   41: [265, 266], 42: [265],
                   50: [268, 269], 51: [268], 61: [268],
                   45: [269, 270], 142: [267, 268, 269, 270]}

    out = []
    seen_region_nations = set()
    cur_region = None
    for i, l in enumerate(lines):
        if i in inserts:
            out += inserts[i]
        if i in delete:
            continue
        m = re.search(r'<REGION id="(\d+)"', l)
        if m:
            cur_region = int(m.group(1))
            seen_region_nations = set()
        m = re.search(r'<SECOND_NATIONS id="(\d+)"', l)
        if m:
            rid = int(m.group(1))
            if rid in drop_refs:
                continue
            if rid in successor:
                l = re.sub(r'<SECOND_NATIONS id="\d+"',
                           f'<SECOND_NATIONS id="{successor[rid]}"', l,
                           count=1)
        m = re.search(r'<REGION_NATION id="(\d+)"', l)
        if m:
            rid = int(m.group(1))
            if rid in drop_refs:
                continue
            rid = successor.get(rid, rid)
            if rid in seen_region_nations:
                continue
            seen_region_nations.add(rid)
            l = re.sub(r'<REGION_NATION id="\d+"',
                       f'<REGION_NATION id="{rid}"', l, count=1)
        if "</REGION_NATIONS>" in l and cur_region in region_adds:
            for add in region_adds[cur_region]:
                if add not in seen_region_nations:
                    seen_region_nations.add(add)
                    out.append(f'        <REGION_NATION id="{add}" />\n')
        out.append(l)

    text = "".join(out)

    # repair capids broken in this base (nation capid / CAPITAL tag point at a
    # city that isn't in the nation): Cameroon→Yaoundé, Gambia→Banjul,
    # Bolivia→La Paz. Scoped to capid=/CAPITAL attrs, never <CITY id=.
    for old, new in (("21371", "88603"), ("1196", "6925"),
                     ("71061", "42537")):
        text = text.replace(f'capid="{old}"', f'capid="{new}"')
        text = text.replace(f'<CAPITAL id="{old}"', f'<CAPITAL id="{new}"')

    # Each annexed territory's "US TERRITORY: X" region lost its nation ref
    # (dropped above); repoint it at the territory's new US state so the pool
    # still resolves.
    terr_region = {"Puerto Rico": "US TERRITORY: Puerto Rico",
                   "Northern Marianas": "US TERRITORY: Northern Mariana "
                                        "Islands",
                   "Guam": "US TERRITORY: Guam",
                   "Virgin Islands": "US TERRITORY: Virgin Islands"}
    for nid, sid in us_annex_state.items():
        rn = re.escape(terr_region[nations[nid]["name"]])
        text = re.sub(
            rf'(name="{rn}"[^>]*>\s*)<REGION_NATIONS>\s*</REGION_NATIONS>',
            rf'\1<REGION_STATES>\n        <REGION_STATE id="{sid}" />\n'
            r'      </REGION_STATES>', text)
    open(dst, "w", encoding="utf-8").write(text)
    out = text.splitlines(keepends=True)
    print(f"wrote {dst}: {len(out)} lines "
          f"(was {len(lines)}; removed {len(delete)}, "
          f"inserted {sum(len(v) for v in inserts.values())})")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
