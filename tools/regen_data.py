#!/usr/bin/env python3
"""Regenerate data/dictionary.tsv and data/headwords.txt from the coursebook.
Run after every merge. The coursebook is the single source of truth."""
import re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
text = (root / 'coursebook' / 'nelo-kel-coursebook.md').read_text()
dict_text = text[text.find('Master Dictionary'):]
entries = {}
for line in dict_text.splitlines():
    line = line.strip()
    if not line.startswith('**') or '—' not in line:
        continue
    line = re.sub(r'^\*\*[^*]+\*\*\s*—\s*', '', line)
    line = line.replace('famīl·la', 'famīlINTERPUNCTla')
    for p in line.split('·'):
        p = p.strip().replace('famīlINTERPUNCTla', 'famīl·la')
        if not p:
            continue
        hw, _, gloss = p.partition(' ')
        entries.setdefault(hw.strip(), gloss.strip())
items = sorted(entries.items(), key=lambda kv: kv[0].lower())

# ---- lint gate (§112/§113): drift fails the merge, loudly ----
# 1. Retired graphemes may not appear in NEW headwords (legacy forms are frozen in
#    data/legacy-orthography.txt — grandfathered, not a license).
# 2. No gloss may cite Estonian or Finnish as a source — the base is Livonian/Karelian,
#    and "(Estonian X)" in an etymology is the tell that a coinage reached the wrong way.
# 3. "Finnic" is retired as a stratum label (§113) — the native pole is tagged (Livonian).
# NOTE — peer-standard scars are OUT OF SCOPE here, and legal in their own namespaces. This
# gate reads only the coursebook (Metropolitan canon); it never touches the Saharannaise or
# Congolaise lexicons, which live under saharannaise/ and congolaise/ and are counted on their
# own terms. Their stratum graphemes are sanctioned by their own orthographic agreements, NOT
# retired: Saharannaise ə ž ġ ṭ ṣ ḍ ẓ (COMMON-REGISTER §2), Congolaise ɓ ɗ ŋ + shared ə
# (CONFLUENCE-PRINCIPLE §2). None of these is in RETIRED, so even a stray peer-standard form in
# the coursebook would not false-positive; the real guarantee is that peer scars are legal by
# design and must never be "sanded" to plain letters (ɓiɗo→biɗo, žəml→zeml) on the theory that
# they are drift. They are the opposite of drift — they are the fingerprint of the stratum.
legacy_path = root / 'data' / 'legacy-orthography.txt'
legacy = set(legacy_path.read_text().split()) if legacy_path.exists() else set()
RETIRED = set('õêîûâšč')
errors = []
for h, g in items:
    # The native grammatical -õ ENDING (adjective/adverb: kaunõ, harvõ, sagõ, rôimõ) is a LIVING
    # morpheme — not the retired stem-õ the v4.0 reform replaced with ô in body-part roots
    # (nõsô→nôsô, §104/§126). A single word-final õ is therefore legal in new coinage; if a word
    # makes grammatical sense on this ending, it exists. õ elsewhere (stems/loans) and êîûâšč
    # anywhere still fail — those are real drift.
    stem = h[:-1] if h.endswith('õ') else h
    if (RETIRED & set(stem)) and h not in legacy:
        errors.append(f"retired grapheme in new headword: {h!r} (stem õ/ê/î/û/â/š/č left the "
                      f"inventory — use ô/ē/ī/ū/ā/x/ç; §104/§109; the native -õ ending is exempt, §126)")
    if re.search(r'\b(Estonian|Finnish)\b', g):
        errors.append(f"{h!r}: gloss cites Estonian/Finnish — source the native pole from "
                      f"Livonian/Karelian instead (§112)")
    if '(Finnic' in g or 'Finnic)' in g:
        errors.append(f"{h!r}: 'Finnic' is retired as a stratum label — tag (Livonian) (§113)")
if errors:
    for e in errors:
        print("LINT:", e)
    raise SystemExit(f"regen_data: {len(errors)} lint error(s) — merge blocked. "
                     f"Fix the entries above; do not bypass.")

(root / 'data' / 'dictionary.tsv').write_text(
    "headword\tgloss\n" + "".join(f"{h}\t{g}\n" for h, g in items))
(root / 'data' / 'headwords.txt').write_text("".join(h + "\n" for h, _ in items))
print(f"regenerated: {len(items)} headwords (lint clean)")
