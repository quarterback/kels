#!/usr/bin/env python3
"""Generate settlements.html (the gazetteer) and toponyms.html (the name roller)
from the single canonical table in tools/settlement_data.py.

Both pages are self-contained — data is inlined, so they work from a file:// path
as well as over HTTP. Never hand-edit the generated HTML; edit the data module or
data/toponym-picks.tsv and re-run this.

Write-back loop: roll names in toponyms.html, copy the basket out as TSV, paste
it into data/toponym-picks.tsv, re-run this script. Picked names are then treated
as canon in settlements.html.

Usage: python3 tools/build_settlements.py
"""

import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import settlement_data as SD          # noqa: E402
from tpl_settlements import TEMPLATE as SETTLEMENTS_TMPL   # noqa: E402
from tpl_toponyms import TEMPLATE as TOPONYMS_TMPL         # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
PICKS = ROOT / "data" / "toponym-picks.tsv"

# National headline figures (boundaries.md, the transoceanic ratification).
NAT = [
    ["≈148M", "Population", False],
    ["≈$6.4T", "Nominal GDP", True],
    ["≈$43K", "GDP per capita", False],
    ["12 + 1", "Regions · federal city", False],
    ["≈79%", "Urban", False],
    ["≈1.35M km²", "Area", False],
]

# Characters that exist in neither a source language nor Nelôxi (gazetteer.md):
# errors, not fossils. Guard the data as well as the generator.
BANNED_CHARS = "îûâÎÛÂ"
BANNED_SENSES = ("merd", "lōd", "sildô")


def load_picks():
    """data/toponym-picks.tsv → {site: (nelox, exonym, layer, gloss)}.

    Columns: site, nelox, exonym, layer, strategy, gloss (the roller's TSV).
    """
    if not PICKS.exists():
        return {}
    picks = {}
    for i, line in enumerate(PICKS.read_text(encoding="utf-8").splitlines()):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        cols = line.split("\t")
        if i == 0 and cols[0].strip().lower() == "site":
            continue                                  # header
        if len(cols) < 2:
            continue
        site = cols[0].strip()
        nelox = cols[1].strip()
        if not site or not nelox:
            continue
        picks[site] = (
            nelox,
            cols[2].strip() if len(cols) > 2 else "",   # exonym
            cols[3].strip() if len(cols) > 3 else "",   # layer
            cols[5].strip() if len(cols) > 5 else "",   # gloss
            cols[6].strip() if len(cols) > 6 else "",   # local (in-world)
        )
    return picks


def main():
    rows = SD.rows()
    picks = load_picks()

    applied = 0
    for r in rows:
        p = picks.get(r["site"])
        if not p:
            continue
        if r["norename"]:
            print(f"  ! refusing pick for {r['site']}: {r['region']} keeps its "
                  f"local toponymy by ruling")
            continue
        nelox, exonym, layer, gloss, local = p
        r["nelox"], r["on_record"], r["source"] = nelox, True, "picked"
        if exonym:
            r["exonym"] = exonym
        if layer:
            r["layer"] = layer
        if gloss:
            r["gloss"] = gloss
        if local:
            r["local"] = local
        applied += 1

    # --- guards --------------------------------------------------------------
    problems = []
    for r in rows:
        if any(c in r["nelox"] for c in BANNED_CHARS):
            problems.append(f"{r['site']}: '{r['nelox']}' uses a forbidden "
                            f"diacritic (î/û/â are errors, not fossils)")
        low = r["nelox"].lower()
        for bad in BANNED_SENSES:
            if bad in low:
                problems.append(f"{r['site']}: '{r['nelox']}' uses the "
                                f"non-name sense '{bad}' (§146)")
        # The rule this whole rework exists to enforce. Exempt (raw loan):
        # keeping the local name IS that layer's definition, so a raw loan
        # differing only in Nelôxi length-marking (Lida → Līda) is correct.
        if r["nelox"] and r["nelox"] != r["site"] and r["layer"] != "raw loan":
            strip = str.maketrans("ôāēīōūäöüõçñǟȫ", "oaeiouaouocnao")
            if (r["nelox"].lower().translate(strip)
                    == r["site"].lower().translate(strip)):
                problems.append(
                    f"{r['site']}: '{r['nelox']}' is the local name with "
                    f"diacritics only — not a name (see world/toponymy.md)")
    if problems:
        print("VALIDATION FAILED:")
        for p in problems:
            print("  ×", p)
        sys.exit(1)

    sites = [r["site"] for r in rows]
    dupes = {s for s in sites if sites.count(s) > 1}
    if dupes:
        print("VALIDATION FAILED: duplicate sites:", ", ".join(sorted(dupes)))
        sys.exit(1)

    # --- emit ---------------------------------------------------------------
    percap = {name: pc for (name, pc, _st) in SD.REGIONS}
    region_meta = [{"name": n, "percap": pc, "status": st}
                   for (n, pc, st) in SD.REGIONS]

    def dump(o):
        return json.dumps(o, ensure_ascii=False)

    settle_keys = ("site", "region", "cc", "terrain", "notes", "pop",
                   "nelox", "layer", "gloss", "on_record",
                   "local", "local_hint", "exonym", "exonym_hint",
                   "anachronism", "hint", "norename", "founding", "founds_what", "source")
    data = [{k: r[k] for k in settle_keys} for r in rows]

    (ROOT / "settlements.html").write_text(
        SETTLEMENTS_TMPL
        .replace("__DATA__", dump(data))
        .replace("__REGIONS__", dump(region_meta))
        .replace("__PERCAP__", dump(percap))
        .replace("__NAT__", dump(NAT)),
        encoding="utf-8")

    # The roller needs less per city, and must never see the no-rename regions
    # as rollable (it filters on `norename` itself).
    top_keys = ("site", "region", "terrain", "notes", "pop", "nelox",
                "layer", "gloss", "on_record", "local", "local_hint",
                "exonym", "exonym_hint", "anachronism", "hint", "norename", "founding", "founds_what", "source")
    (ROOT / "toponyms.html").write_text(
        TOPONYMS_TMPL
        .replace("__CITIES__", dump([{k: r[k] for k in top_keys} for r in rows]))
        .replace("__REGIONS__", dump(region_meta)),
        encoding="utf-8")

    # --- report -------------------------------------------------------------
    anach = sum(1 for r in rows if r["anachronism"])
    canon = sum(1 for r in rows if r["nelox"])
    norename = sum(1 for r in rows if r["norename"])
    rollable = sum(1 for r in rows if not r["norename"] and not r["nelox"])
    print(f"settlements: {len(rows)}  ·  nelôxi name on record {canon}  ·  open "
          f"{rollable}  ·  no-rename {norename}")
    print(f"  ⚠ {anach} reference NAMES are Soviet/imperial coinages that cannot "
          f"be the in-world name (the places still exist)")
    founds = sum(1 for r in rows if r["founding"] == "foundation")
    print(f"  ⌂ {founds} sites are Nelôxian foundations rather than inherited "
          f"settlements — the roller dates and attributes them")
    if applied:
        print(f"applied {applied} pick(s) from {PICKS.relative_to(ROOT)}")
    elif PICKS.exists():
        print(f"{PICKS.relative_to(ROOT)} present but empty")
    else:
        print(f"no {PICKS.relative_to(ROOT)} yet — roll names in toponyms.html, "
              f"paste the TSV there, re-run")

    print()
    for name, pc, _st in SD.REGIONS:
        rs = [r for r in rows if r["region"] == name]
        if not rs:
            continue
        named = sum(1 for r in rs if r["nelox"])
        pop = sum(r["pop"] for r in rs)
        print(f"  {name:32s} {len(rs):3d} cities  {named:2d} named  {pop:>11,}")

    listed_pop = sum(r["pop"] for r in rows)
    listed_gdp = sum(r["pop"] * percap[r["region"]] for r in rows)
    print(f"\n  listed population {listed_pop:,}  ·  listed output ${listed_gdp:,}")
    print("wrote settlements.html, toponyms.html")


if __name__ == "__main__":
    main()
