#!/usr/bin/env python3
"""Update an OOTP weather.txt to match the Nelôxi world_default.

Two changes:

1. Reference fixes — weather rows for cities the world build moved to a
   different nation, or whose nation was absorbed:
     151 San Juan  -> 206 (Puerto Rico is now a US state)
      23 Town Hill -> 266 (Bermuda -> Meridian States)
      71 Cayenne   -> 266 Esperanza (French Guiana -> Meridian, renamed)
      42 Urumqi    -> 269 (Xinjiang -> Tarun)

2. New-nation capitals — the ten new nations that had no weather station get
   one, using the real-world climate of the city each capital is (Kaliningrad
   for Kunislinnô, Feodosia for Caffa, Yuzhno-Sakhalinsk for Gannibal, …).
   Meridian's Esperanza comes from the Cayenne fix above. Temps are °F monthly
   Jan–Dec, then precipitation (in) Jan–Dec — approximations to tweak freely.

Usage: python3 update_weather.py <weather.txt in> <weather.txt out>
"""

import sys

# (old_nid, city) -> (new_nid, new_city_or_None)
FIXES = {
    ("151", "San Juan"): ("206", None),
    ("23", "Town Hill"): ("266", None),
    ("71", "Cayenne"): ("266", "Esperanza"),
    ("42", "Urumqi"): ("269", None),
}

# nid, city, wind, [12 monthly avg temp °F], [12 monthly precip in]
NEW_CAPITALS = [
    (260, "Kunislinnô", 9, [30, 30, 36, 45, 55, 61, 64, 63, 57, 48, 39, 33],
     [3, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 3]),                 # Kaliningrad
    (261, "Göteborg", 10, [32, 32, 37, 44, 54, 60, 63, 62, 55, 47, 40, 35],
     [3, 2, 3, 2, 2, 3, 3, 4, 4, 4, 4, 3]),                 # Skaria
    (262, "Fôntāna", 10, [61, 63, 66, 68, 70, 73, 75, 77, 77, 74, 68, 63],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]),                 # Laayoune
    (263, "Atar", 8, [71, 75, 80, 84, 90, 95, 96, 95, 93, 88, 79, 72],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0]),                 # Adrāra
    (264, "Ndar", 9, [71, 72, 73, 74, 77, 81, 83, 82, 83, 82, 79, 74],
     [0, 0, 0, 0, 0, 1, 2, 5, 5, 2, 0, 0]),                 # Saint-Louis
    (265, "Portô Venla", 8, [77, 77, 74, 68, 61, 56, 55, 58, 62, 67, 72, 76],
     [4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 4, 4]),                 # Porto Alegre
    (267, "Caffa", 10, [36, 37, 42, 50, 61, 70, 76, 76, 67, 57, 47, 40],
     [2, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 2]),                 # Feodosia
    (268, "Gannibal", 9, [18, 21, 30, 40, 49, 57, 63, 66, 59, 47, 34, 22],
     [2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 3, 3]),                 # Yuzhno-Sakhalinsk
    (269, "Tashkent", 6, [37, 41, 51, 62, 72, 81, 86, 84, 74, 61, 49, 40],
     [2, 2, 2, 2, 1, 0, 0, 0, 0, 1, 2, 2]),                 # Tarun
    (270, "Kazan", 8, [12, 16, 27, 42, 58, 66, 70, 66, 55, 40, 26, 16],
     [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1]),                 # Qazania
]


def main(src, dst):
    lines = open(src, encoding="utf-8").read().splitlines()
    out = []
    for l in lines:
        f = l.split(",")
        if len(f) > 2 and (f[0], f[1]) in FIXES:
            new_nid, new_city = FIXES[(f[0], f[1])]
            f[0] = new_nid
            if new_city:
                f[1] = new_city
            l = ",".join(f)
        out.append(l)
    for nid, city, wind, temp, precip in NEW_CAPITALS:
        vals = [str(nid), city, "", str(wind)] + [str(x) for x in temp] + \
               [str(x) for x in precip]
        out.append(",".join(vals) + ",")   # trailing comma, as in the file
    open(dst, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"wrote {dst}: {len(FIXES)} fixes, +{len(NEW_CAPITALS)} capitals")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
