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
(root / 'data' / 'dictionary.tsv').write_text(
    "headword\tgloss\n" + "".join(f"{h}\t{g}\n" for h, g in items))
(root / 'data' / 'headwords.txt').write_text("".join(h + "\n" for h, _ in items))
print(f"regenerated: {len(items)} headwords")
