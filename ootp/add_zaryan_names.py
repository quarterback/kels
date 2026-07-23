#!/usr/bin/env python3
"""Inject a custom Zaryan name pool (lid 233) into an OOTP names.xml.

Zaryanova (world/zaryanova.md) has no real-world ethnicity that produces its
Afro-Russian creole names ("Marcus Volkov", "Pavel Kuznetsov"), so the world
file assigns it a custom ethnicity, id 233. This script gives that ethnicity a
name pool: it appends first names and surnames tagged with lid 233 to the
FIRST_NAMES and LAST_NAMES sections of names.xml.

Names are lifted from the founder's generator
(quarterback/tennis-team-manager generators/zaryan_names.py): the Russianized /
heritage given names it emits, and the Russified surnames from its meaning
dictionary, plus a handful of the untranslated heritage surnames the generator
keeps for the modern/urban register.

names.xml has no gender field on FIRST_NAMES, so male and female given names go
into one pool (as the base file does for every language).

Usage: python3 add_zaryan_names.py <names.xml in> <names.xml out>
"""

import re
import sys

LID = 233

FIRST = [
    # Russianized forms the converter emits
    "Aleksandr", "Andrey", "Antoniy", "Anya", "Avigail", "Avraam", "Daniil",
    "Danya", "Davyd", "Devora", "Eduard", "Elena", "Estera", "Evgeny",
    "Evvonna", "Feliks", "Filipp", "Foma", "Frants", "Garison", "Garold",
    "Garvey", "Genri", "Georgy", "Govard", "Iliya", "Iosif", "Irina",
    "Isayev", "Ivan", "Iyetan", "Katya", "Kira", "Kirill", "Klara",
    "Klaudiya", "Kodya", "Kolya", "Koretta", "Lev", "Liliya", "Liya", "Liza",
    "Luka", "Maks", "Maria", "Mark", "Matvey", "Mikhail", "Mila", "Miriam",
    "Misha", "Moisey", "Monika", "Nadya", "Naomi", "Nikolay", "Noy", "Oksana",
    "Pasha", "Pavel", "Petya", "Praskovya", "Pyotr", "Rakhil", "Ria",
    "Rikhard", "Rivka", "Roman", "Rostislav", "Rostya", "Roza", "Ruf",
    "Samuil", "Sasha", "Semyon", "Solomon", "Sonya", "Stefaniya", "Stepan",
    "Sterling", "Susanna", "Taisiya", "Tosha", "Tovy", "Valeriya", "Vanda",
    "Veronika", "Vika", "Vikenty", "Viktor", "Vilyam", "Yakov", "Yanna",
    "Yasha", "Yekaterina", "Yelizaveta", "Yosha", "Yudif", "Yulia", "Zakhar",
    "Zakhary", "Zara", "Ada", "Anna", "David", "Diana", "Booker",
    # heritage / Biblical given names the generator keeps bare
    "Isaiah", "Elijah", "Moses", "Abraham", "Marcus", "Coretta", "Ruth",
    "Esther", "Naomi", "Ezra", "Amos", "Malachi", "Delilah", "Cyrus",
]

SURNAMES = [
    # Russified surnames from the generator's meaning dictionary
    "Belov", "Bolotov", "Brodov", "Buryev", "Bystrov", "Chernov", "Dnyov",
    "Goncharov", "Gornov", "Kamenshchikov", "Kamnev", "Kolodtsev",
    "Kolokolov", "Korolyov", "Krepkov", "Krestov", "Kuznetsov", "Lesov",
    "Letov", "Lisin", "Melnikov", "Molodov", "Nosilov", "Okhotnikov",
    "Ozerov", "Pastukhov", "Pekarev", "Plotnikov", "Polev", "Povarov",
    "Ptitsyn", "Rechnov", "Rozin", "Rybakov", "Rytsarev", "Sadovnikov",
    "Skalov", "Snegov", "Surovov", "Svetlov", "Tkachev", "Trostnikov",
    "Volkov", "Volnov", "Zelyonov", "Zimin",
    # untranslated heritage surnames kept for the modern/urban register
    "Brooks", "Jefferson", "Washington", "Jackson", "Coleman", "Freeman",
    "Carter", "Robinson", "Booker", "Harrison", "Dawson", "Prince",
]


def main(src, dst):
    lines = open(src, encoding="utf-8").readlines()
    max_nid = max(int(m.group(1)) for l in lines
                  for m in [re.search(r'nid="(\d+)"', l)] if m)
    nid = max(max_nid, 1_500_000) + 1

    def entries(names):
        nonlocal nid
        out = []
        for nm in names:
            out.append(f'<N nid="{nid}"><EN>{nm}</EN>'
                       f'<NL><L lid="{LID}" dist="3"/></NL></N>\n')
            nid += 1
        return out

    out = []
    for l in lines:
        if l.startswith("</FIRST_NAMES>"):
            out += entries(FIRST)
        if l.startswith("</LAST_NAMES>"):
            out += entries(SURNAMES)
        out.append(l)
    open(dst, "w", encoding="utf-8").writelines(out)
    print(f"wrote {dst}: +{len(FIRST)} first names, +{len(SURNAMES)} "
          f"surnames under lid {LID}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
