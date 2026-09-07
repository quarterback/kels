#!/usr/bin/env python3
"""Render canonical Metropolitan Nelôxi in Modern Anbur rev. 2.

This is intentionally NOT a lossless cipher:
- long vowels are doubled;
- ô and final õ merge;
- y/ü, ö/œ, x/legacy š merge;
- ñ and ļ use 𐍲 as an Anbur palatalizer;
- l·l becomes ordinary doubled l.

Latin remains the lexical/archive spelling.
"""

from __future__ import annotations
import argparse, sys, unicodedata

MAP = {
    "a":"𐍐","b":"𐍑","d":"𐍓","e":"𐍔","f":"𐍫","g":"𐍒","h":"𐍬",
    "i":"𐍙","j":"𐍵","k":"𐍚","l":"𐍛","m":"𐍜","n":"𐍝","o":"𐍩",
    "p":"𐍟","r":"𐍠","s":"𐍡","t":"𐍢","u":"𐍣","v":"𐍞","x":"𐍥",
    "y":"𐍧","ä":"𐍱","ö":"𐍪","ô":"𐍨","õ":"𐍨","ç":"𐍭",
    "ñ":"𐍝𐍲","ļ":"𐍛𐍲",
    "ž":"𐍕","dž":"𐍖","z":"𐍗","w":"𐍮",
    "ü":"𐍧","œ":"𐍪","š":"𐍥",
}
LONG = {"ā":"a","ē":"e","ī":"i","ō":"o","ū":"u","ǟ":"ä","ȫ":"ö"}

def to_anbur(text: str, strict: bool = True) -> str:
    text = unicodedata.normalize("NFC", text)
    out = []
    i = 0
    while i < len(text):
        if text[i:i+3].lower() == "l·l":
            out.append(MAP["l"] + MAP["l"])
            i += 3
            continue
        if text[i:i+2].lower() == "dž":
            out.append(MAP["dž"])
            i += 2
            continue
        ch = text[i]
        low = ch.lower()
        if low in LONG:
            glyph = MAP[LONG[low]]
            out.append(glyph + glyph)
        elif low in MAP:
            out.append(MAP[low])
        elif ch.isalpha() and strict:
            raise ValueError(f"Unmapped alphabetic character at {i}: {ch!r}")
        else:
            out.append(ch)
        i += 1
    return "".join(out)

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--no-strict", action="store_true")
    p.add_argument("text", nargs="*")
    a = p.parse_args()
    src = " ".join(a.text) if a.text else sys.stdin.read()
    try:
        out = to_anbur(src, strict=not a.no_strict)
    except ValueError as e:
        print(f"anbur: {e}", file=sys.stderr)
        return 2
    sys.stdout.write(out + ("\n" if a.text else ""))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
