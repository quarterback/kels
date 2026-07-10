#!/usr/bin/env python3
"""Regenerate the three self-contained agent bundles from current canon.

A bundle is a concatenation of contributor docs that already live in the repo —
the relevant brief, the function-word cheat-sheet, the relevant grammar modules,
and the current headword list — assembled so one agent can be handed exactly one
file. This script rebuilds them from those sources, so the bundles never drift
from canon.

It also normalizes the single current-state stamp (version + headword count) in
the site-facing briefs, so the version an agent reads is always the live one.
Historical version references (e.g. "õ retired in v4.0") are left untouched.

Run after every canon change, alongside regen_data.py and regen_reverse.py.
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel, text):
    (ROOT / rel).write_text(text, encoding="utf-8")


def sub1(text, pattern, repl, where):
    new, n = re.subn(pattern, repl, text)
    if n < 1:
        raise SystemExit(f"build_bundles: expected stamp not found in {where}: {pattern!r}")
    return new


# --- current canon facts (single source of truth) ---
charter = read("college/kels-kolegi-charter.md")
m = re.search(
    r"Canonical headword list \(collision reference, (v\d+\.\d+) — (\d+) entries", charter
)
if not m:
    raise SystemExit("build_bundles: could not read version/count from charter §7 header")
VERSION, COUNT = m.group(1), int(m.group(2))

words = [w for w in read("data/headwords.txt").splitlines() if w.strip()]
if len(words) != COUNT:
    raise SystemExit(f"build_bundles: charter says {COUNT} but headwords.txt has {len(words)}")
HWLIST = " · ".join(words)
LASTSEC = max(int(x) for x in re.findall(r"(?m)^## (\d+)\.", charter))

# --- normalize the current-state stamp in the site-facing briefs (narrow, anchored) ---
delegate = read("college/DELEGATE-BRIEF.md")
delegate = sub1(delegate,
                r"Current canon: \*\*v\d+\.\d+, \d+ headwords\.\*\*",
                f"Current canon: **{VERSION}, {COUNT} headwords.**", "DELEGATE-BRIEF")
delegate = sub1(delegate,
                r"full ruling log §1[–-]§\d+",
                f"full ruling log §1–§{LASTSEC}", "DELEGATE-BRIEF ruling-log ref")
write("college/DELEGATE-BRIEF.md", delegate)

functions = read("college/FUNCTION-WORDS.md")
functions = sub1(functions,
                 r"(?m)^Canon v\d+\.\d+\.",
                 f"Canon {VERSION}.", "FUNCTION-WORDS")
write("college/FUNCTION-WORDS.md", functions)

dailylife = read("college/DAILY-LIFE-BRIEF.md")
dailylife = sub1(dailylife,
                 r"Canon is \*\*v\d+\.\d+, \d+ headwords\.\*\*",
                 f"Canon is **{VERSION}, {COUNT} headwords.**", "DAILY-LIFE-BRIEF")
write("college/DAILY-LIFE-BRIEF.md", dailylife)

corpus_brief = read("college/CORPUS-BRIEF.md")
corpus_brief = sub1(corpus_brief,
                    r"Nelôxi is at version \d+\.\d+, \d+ headwords\.",
                    f"Nelôxi is at version {VERSION[1:]}, {COUNT} headwords.", "CORPUS-BRIEF")
corpus_brief = sub1(corpus_brief,
                    r"THE ATTESTED HEADWORD LIST \(\d+ words; use only these\)",
                    f"THE ATTESTED HEADWORD LIST ({COUNT} words; use only these)",
                    "CORPUS-BRIEF §6 header")
corpus_brief = sub1(corpus_brief,
                    r"(?m)^abī · abīstā .*$",
                    HWLIST, "CORPUS-BRIEF §6 list")
write("college/CORPUS-BRIEF.md", corpus_brief)

# --- assemble the bundles ---
SEP = "\n\n---\n\n"


def assemble(blocks):
    return SEP.join(b.rstrip("\n") for b in blocks) + "\n"


def part(label, body):
    return f"## {label}\n\n{body.strip()}\n"


def bundle_top(title, blurb, read_line, with_count=True):
    stamp = f"Canon {VERSION}, {COUNT} headwords." if with_count else f"Canon {VERSION}."
    return (
        f"# Nelôxi — {title} (self-contained)\n\n"
        f"> {blurb}\n"
        f"> {stamp} {read_line}\n"
    )


# Domain agent bundle
domain = assemble([
    bundle_top("DOMAIN AGENT BUNDLE",
               "Everything you need to coin vocabulary for one domain. You need no other file.",
               "Read top to bottom, then produce ONE domain batch."),
    part("THE CREOLE PRINCIPLE — the standing vocabulary doctrine (read before anything else)",
         read("college/CREOLE-PRINCIPLE.md")),
    part("PART A — Your brief", read("college/DELEGATE-BRIEF.md")),
    part("PART B — Function words that ALREADY EXIST (never re-propose, never write the Estonian)",
         read("college/FUNCTION-WORDS.md")),
    part("PART C — Verb-derivation (build verb variants instead of coining new roots)",
         read("grammar/02-verb-derivation.md")),
    part("PART D — Compounding (build words from existing roots instead of borrowing)",
         read("grammar/04-compounding.md")),
    part(f"PART E — The complete current headword list ({COUNT} words — use only these; "
         f"anything else is a gap to flag)", HWLIST),
])
write("bundles/BUNDLE-domain-agent.md", domain)

# Corpus agent bundle (its headword list lives inside PART A, section 6, already refreshed above)
corpus = assemble([
    bundle_top("CORPUS AGENT BUNDLE",
               "Everything you need to write a genre text and harvest gaps. You need no other file.",
               "Read top to bottom, then produce ONE text + gap-list."),
    part("THE CREOLE PRINCIPLE — the standing vocabulary doctrine (read before anything else)",
         read("college/CREOLE-PRINCIPLE.md")),
    part("PART A — Your brief (mission, genre ladder, method)", read("college/CORPUS-BRIEF.md")),
    part("PART B — Function words that ALREADY EXIST (never re-propose, never write the Estonian)",
         read("college/FUNCTION-WORDS.md")),
    part("PART C — Tense & aspect (how to say WHEN — no future/perfect by design)",
         read("grammar/09-tense-aspect.md")),
    part("PART D — Commands & suggestions (imperative = bare stem; hortative = -m)",
         read("grammar/11-commands.md")),
    part("PART E — Pronouns (full paradigm — high-frequency, get these right)",
         read("grammar/07-pronouns.md")),
    part("PART F — Adjectives (invariance rule)", read("grammar/10-adjectives.md")),
])
write("bundles/BUNDLE-corpus-agent.md", corpus)

# Grammar reference bundle (index + every module, no PART wrappers)
GRAMMAR_MODULES = [
    "grammar/00-INDEX.md",
    "grammar/01-partitive-case.md",
    "grammar/02-verb-derivation.md",
    "grammar/03-consonant-gradation.md",
    "grammar/04-compounding.md",
    "grammar/06-declension.md",
    "grammar/07-pronouns.md",
    "grammar/08-relations.md",
    "grammar/09-tense-aspect.md",
    "grammar/10-adjectives.md",
    "grammar/11-commands.md",
    "grammar/12-numbers.md",
]
grammar = assemble([
    bundle_top("COMPLETE GRAMMAR REFERENCE",
               "The full structural core of Nelôxi in one file. Hand this to a grammar agent, or "
               "to any\n> agent that has started drifting (using Estonian, guessing forms) to "
               "re-ground it.",
               "Every module assumes no prior knowledge.", with_count=False),
    *[read(mod).strip() + "\n" for mod in GRAMMAR_MODULES],
])
write("bundles/BUNDLE-grammar-reference.md", grammar)

# Version stamp for the website (data/version.json) — generated from the same
# charter facts as everything else, so the site badge always matches the deployed canon
import json
write("data/version.json", json.dumps(
    {"version": VERSION, "headwords": COUNT, "ruling": LASTSEC}, ensure_ascii=False) + "\n")

# Translation bundle is live-fetch by design (no embedded list) — sync only its canon stamp
trans = ROOT / "bundles/BUNDLE-translation-agent.md"
if trans.exists():
    t = trans.read_text(encoding="utf-8")
    t = sub1(t, r"Current canon: \*\*v\d+\.\d+, ~?[\d,]+ headwords\.\*\*",
             f"Current canon: **{VERSION}, ~{COUNT} headwords.**", "BUNDLE-translation-agent")
    trans.write_text(t, encoding="utf-8")

print(f"bundles rebuilt at {VERSION}, {COUNT} headwords (ruling log through §{LASTSEC})")
