# Nelôxi — Multi-Agent Coordination (for the founder)

Canon: **v4.8, 889 headwords.** You have Agent A (on rung 4 now), Agent B ready, and ~20
more incoming. Here is how to run them without collisions.

## The rule that prevents clashes

Two axes of work, and no two agents share a cell:

**Axis 1 — Corpus (text) agents** work the GENRE LADDER. Each agent owns a genre; genres
don't overlap in vocabulary demand. Rungs:
1. Recipe/how-to — DONE
2. Haggling dialogue — DONE
3. Folktale (past narrative) — DONE (Agent A)
4. Letter / lament (irrealis, emotion) — ASSIGNED to Agent A
5. Proverb / notice / law (generic statements, idiom)
6. Standard comparison texts (Babel; North Wind and the Sun; UDHR Article 1)
7. Children's rhyme / song (meter, repetition, numbers)
8. Riddle / joke (wordplay, double meaning)
9. Weather report / almanac (time, seasons, prediction)
10. Personal insult match / flyting (the profanity register in use)

**Axis 1b — The Daily-Life / Connective-Speech agent** is a standing role (not a rung): it
writes sustained everyday prose and harvests the connective glue — particles, hedges, light
verbs, connectives — that no domain owns. See `DAILY-LIFE-BRIEF.md`. One agent holds this lane
continuously, working through "a day in the life" in stretches. It does not collide with genre
or domain work because its target (structure words) is disjoint from theirs (content words).

**Axis 2 — Domain (vocabulary) agents** claim a DOMAIN in `college/ASSIGNMENTS.md` before
coining. Open domains include: U23, U27+ (medicine/the body, plants/trees, weather/seasons,
music/instruments, religion/ritual, clothing/textiles, tools/trades, animals/wildlife,
time/calendar, law/court procedure, warfare, seafaring-deep, emotion-fine, abstract/philosophy).

An agent does EITHER a genre text OR a domain batch — never both in one pass. Give each new
agent the DELEGATE-BRIEF (for domain work) or CORPUS-BRIEF (for text work), plus one
assignment from the lists above. They pull current canon, work, flag gaps, submit.

## Immediate assignments

- **Agent A:** rung 4 (letter/lament). Already briefed.
- **Agent B:** rung 5 (proverb/notice/law) OR a domain batch — recommend **domain: weather &
  seasons**, since three later genres (almanac, rhyme, lament) will lean on it and it's
  currently thin. Give B the DELEGATE-BRIEF and tell it to claim "U27 Weather & seasons" in
  the ledger.
- **Incoming agents:** hand each the next unclaimed genre rung or domain, in order. Never
  two agents on the same rung or domain at once.

## The one hard rule for all of them

Pull `data/headwords.txt` at current HEAD before working. Flag gaps; never borrow a
source-language word (no raw Estonian/Finnish/Polish forms in text — shape proposals to
Nelôxi or flag them). Submit text/batch + gap-list. The Rector (you, or a Code-instance
Rector agent) reviews against canon, nativizes anything source-shaped, merges, regenerates
data, logs the ruling, commits.

## What you (or the Code Rector) do each cycle

1. Receive batch + gap-list.
2. Check against `data/headwords.txt` HEAD (catch stale work, duplicates, leaks).
3. Rule on grammar gaps; nativize/shape any source-language proposals; fill approved lexical gaps.
4. Merge into the coursebook; run `regen_data.py` + `regen_reverse.py`; sync charter §7.
5. Log the ruling as the next §-number; commit.
6. Return a short rulings doc + next assignment to that agent.

The genre ladder and the domain ledger together guarantee 20 agents can run in parallel with
zero collisions, because every agent owns a distinct cell and the Rector serializes the merges
through git.
