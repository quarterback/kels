#!/usr/bin/env python3
"""Regenerate data/reverse-index.md (English → Nelôxi) from data/dictionary.tsv.
Run after regen_data.py, after every merge. Derived artifact — never hand-edit."""
import re, collections, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
entries = []
with open(root/'data'/'dictionary.tsv') as f:
    next(f)
    for line in f:
        hw, _, gloss = line.rstrip('\n').partition('\t')
        entries.append((hw, gloss))

reverse = collections.defaultdict(list)
for hw, gloss in entries:
    tag = 'late' if '(late-stratum)' in gloss else ''
    g = re.sub(r'\s*\(late-stratum\)', '', gloss).strip()
    for sense in (s.strip() for s in g.split(';') if s.strip()):
        for p in (x.strip() for x in re.split(r',(?![^()]*\))', sense)):
            if not p or not p[0].isalpha():
                continue  # skip pure-annotation glosses like "(question particle)"
            key, marker = (p[3:], ' (v.)') if p.startswith('to ') and len(p) > 3 else (p, '')
            reverse[key.lower()].append((key + marker if marker else p, hw, tag))

out = ["# Nelô kēļ — English → Nelôxi Reverse Index", "",
       f"*Generated from the coursebook master dictionary ({len(entries)} headwords). "
       "Find your English word, take the Nelôxi headword, inflect per the reference grammar. "
       "⁺ marks late-stratum (technical/recent register). Derived artifact — "
       "regenerate with tools/regen_reverse.py after every merge.*", ""]
cur = ''
for k in sorted(reverse):
    if k[0].upper() != cur:
        cur = k[0].upper()
        out.append(f"\n## {cur}\n")
    seen, shown = set(), []
    for _, hw, tag in reverse[k]:
        if hw in seen: continue
        seen.add(hw)
        shown.append(f"**{hw}**" + ("⁺" if tag == 'late' else ""))
    out.append(f"{reverse[k][0][0]} → {' · '.join(shown)}  ")
(root/'data'/'reverse-index.md').write_text('\n'.join(out) + '\n')
print("reverse index:", len(reverse), "English keys")
