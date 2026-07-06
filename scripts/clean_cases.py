#!/usr/bin/env python3
"""
ColdCaseIndex — one-off data cleanup (2026-07-06 audit).

Applies three kinds of fixes to data/cases.json:
  1. REMOVE   — entries that are fabricated, name real/living people as crime
                victims falsely, describe non-crimes, or duplicate another entry.
  2. RESLUG   — entries describing a real case whose URL slug referenced an
                unrelated person or case; the slug is changed to match content.
  3. FIX      — field-level factual corrections (wrong state/year/name/status,
                outdated statuses, misleading summaries).

Also deletes the cases/<slug>/ directories of removed and renamed entries.
Run from project root: python3 scripts/clean_cases.py
"""

import json
import os
import shutil

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_FILE = os.path.join(ROOT_DIR, 'data', 'cases.json')
CASES_DIR = os.path.join(ROOT_DIR, 'cases')

# ── 1. Removals ──────────────────────────────────────────────────────────
REMOVE = {
    # Falsely present real / living people as crime victims, or fabricated
    'patricia-hearst':        "names Steven Weed (never murdered) as homicide victim; duplicates patty-hearst-sla",
    'scottsboro-boys':        "lists the case's accusers as homicide victims — false",
    'mary-beth-tinker':       "fabricated victim 'Stephanie Nolen'; slug names a living activist",
    'sandy-hook-adam-lanza':  "fabricated, self-contradictory entry under an offensive slug",
    'arizona-unsolved-2008':  "names Lori Loughlin (living actress) as a murder victim",
    'karis-jagger':           "names Kori Cioca (living veteran) as a murder victim",
    'dan-quisenberry':        "names Carrie Ann Lucas (activist who died of illness) as murder victim",
    'dorothy-helen-scott':    "names Helen Grayco (singer, not murdered) as a murder victim",
    'ira-sorkin':             "fabricated 'Sharon Sorkin'; slug names a living attorney",
    'ann-burgess':            "fabricated; name matches living forensic-nursing pioneer",
    'alice-waters':           "fabricated; name matches living chef",
    'kim-porter':             "false: Kim Porter died of pneumonia in 2018, listed as 2007 homicide",
    'amber-hunt':             "fabricated; name matches living Cincinnati true-crime journalist",
    'lorraine-kelly':         "fabricated; name matches living TV presenter",
    'holly-jolly':            "fabricated entry, unverifiable",
    'taylor-thyfault':        "contradicts the real Taylor Thyfault case (2015 CO trooper cadet)",
    'patricia-meehan':        "contradicts the real Patricia Meehan case (1989 Montana)",
    'connie-smith-mn':        "boilerplate contradicting the well-known 1952 Connie Smith case",
    'alabama-missing-2003':   "boilerplate contradicting the well-known Cynthia Anderson case (Toledo 1981)",
    'michelle-la-toya-jackson': "Michael Jackson's death (solved manslaughter), misleading name",
    'michelle-mcnamara':      "fabricated 'James Benecke'; duplicates golden-state-killer",
    'william-greer-jr':       "garbled facts; slug names JFK's limousine driver",
    'henry-lee-lucas':        "garbled: 'Deborah Dudley' was a Heidnik victim, summary is Maine boilerplate",
    'ricky-brown':            "fabricated name; Central Park Jogger victim survived — no homicide",
    'gary-heidnik-2':         "profiles a living survivor as a case; duplicates gary-heidnik",
    'pike-county-massacre':   "fabricated 'Rowe Family Massacre'; slug suggests the 2016 Rhoden case",
    'houston-heights-killer': "fabricated 'William Dean Christiansen' conviction story",
    'jon-benet-updated':      "'Patsy Ramsey as Suspect' contradicts the 2008 DNA exoneration",
    'windwalker':             "garbled variant of the real Hanna Harris case (kept separately)",
    'dc-case-2010':           "fabricated; name matches a living federal prosecutor",
    # Not crimes
    'rodney-king':            "beating case; his 2012 death was ruled accidental — not a cold case",
    'chris-mccandles-context': "death by starvation, not a crime",
    'terri-schiavo':          "medical/right-to-die case, not a crime",
    'karen-ann-quinlan':      "medical/right-to-die case, not a crime",
    'george-zimmerman':       "killer known and acquitted; 'Unsolved homicide' framing is false",
    # Duplicates
    'sharon-richie':          "duplicates sharon-tate-murder",
    'james-byrd-killers':     "duplicates james-byrd; 'Shawn Berry Release' is misleading",
    'dc-unsolved-1999':       "duplicates chandra-levy",
    'd-b-cooper-detail':      "duplicates d-b-cooper",
    'gabby-petito-wyoming':   "duplicates gabby-petito",
    'scott-peterson-laci':    "duplicates laci-peterson",
    'jonbenet-suspect-2016':  "duplicates jonbenet-ramsey",
    'abby-hernandez-nh':      "duplicates abby-hernandez",
    'oj-simpson-double':      "duplicates ron-goldman-nicole-simpson",
    'robert-blake-bakley':    "duplicates bonny-lee-bakley",
    'amber-alert-1996':       "duplicates amber-hagerman",
    'tupac-las-vegas':        "duplicates tupac-shakur",
    'amber-geiger':           "duplicates botham-jean-detailed (kept as botham-jean)",
}

# ── 2. Re-slugs (old id → new id) ─────────────────────────────────────────
RESLUG = {
    'edgar-lee-masters':        'carrie-brown',
    'edgar-ray-killen':         'bucks-county-jane-doe',
    'helen-front':              'peggy-hettrick',
    'crystal-mangum':           'robert-wone',
    'zodiac-florida':           'danny-rolling-confession',
    'jennifer-cardy':           'kimberly-leach',
    'kim-leach-bundy':          'fsu-chi-omega-murders',
    'savanna-lafontaine-detail': 'hanna-harris',
    'theresa-halbach':          'teresa-halbach',
    'jessica-lundsford':        'jessica-lunsford',
    'valarie-mack':             'valerie-mack',
    'barbara-ann-mackle':       'barbara-jane-mackle',
    'tucson-victims':           'samantha-runnion',
    'phoenix-lights':           'michelle-martinez',
    'dillon-hull':              'paul-scagnetti',
    'ira-einhorn-holly':        'tom-donahue',
    'colt-bundy':               'linda-sobieraj',
    'angela-singleten':         'dorothy-sherrill',
    'claiborne-barnwell':       'amy-carney',
    'cathy-thomas-delaware':    'rebecca-williams',
    'mira-forman':              'sandy-forman',
    'sasha-mccrae':             'victoria-pham',
    'connecticut-grisly':       'juanita-williams',
    'michael-huston':           'james-riddle',
    'iowa-state-killings':      'lisa-doyle',
    'colorado-missing-2003':    'dru-sjodin',
    'illinois-missing-2000':    'brianna-maitland',
    'utah-missing-1997':        'cassie-jo-stoddart',
    'michigan-missing-2005':    'lauren-spierer',
    'vermont-unsolved-2001':    'melissa-jenkins',
    'washington-missing-2007':  'ingrid-lyne',
    'florida-missing-2014':     'denise-amber-lee',
    'sc-missing-2008':          'brittanee-drexel',
    'minnesota-missing-2011':   'paige-renkoski',
    'wyoming-missing-1994':     'amy-bechtel',
    'philando-castile-detail':  'laquan-mcdonald',
    'botham-jean-detailed':     'botham-jean',
    'selma-marching':           'jimmie-lee-jackson',
    'joseph-hilley':            'frank-hilley',
    'dorothy-puente':           'dorothea-puente',
}

# ── 3. Field fixes (applied after re-slug, keyed by NEW id) ───────────────
FIX = {
    'samantha-runnion': {
        'name': 'Samantha Runnion',
    },
    'shenandoah-murders': {
        'name': 'Julianne Williams & Lollie Winans',
        'status': 'Unsolved',
        'summary': ("Julianne Williams and Laura 'Lollie' Winans were found murdered at "
                    "their backcountry campsite in Shenandoah National Park in 1996. "
                    "Darrell Rice was indicted in 2002, but the charges were dropped in "
                    "2004 after DNA evidence did not match him. The murders remain "
                    "unsolved and the FBI continues to seek information."),
    },
    'brittanee-drexel': {
        'status': 'Conviction',
        'summary': ("Seventeen-year-old Brittanee Drexel disappeared from Myrtle Beach, "
                    "South Carolina during spring break in 2009. In 2022, Raymond Moody "
                    "pleaded guilty to her kidnapping, rape, and murder and was sentenced "
                    "to life in prison. Her remains were recovered in Georgetown County, "
                    "ending a thirteen-year search."),
    },
    'frank-hilley': {
        'name': 'Frank Hilley',
        'gender': 'Male',
        'age': 45,
        'year': 1975,
        'date': 'May 25, 1975',
        'summary': ("Frank Hilley died in Anniston, Alabama in 1975 of what was initially "
                    "diagnosed as infectious hepatitis. After his body was exhumed, his "
                    "death was attributed to arsenic poisoning, and his wife Audrey Marie "
                    "Hilley was convicted of his murder in 1983. She had also poisoned "
                    "their daughter Carol, who survived. Marie Hilley escaped custody in "
                    "1987 and died of exposure shortly after being recaptured."),
    },
    'dorothea-puente': {
        'name': 'Dorothea Puente Victims',
        'summary': ("Dorothea Puente was a Sacramento boardinghouse operator who poisoned "
                    "elderly tenants and continued cashing their Social Security checks. "
                    "Seven bodies were found buried in her yard in 1988. She was convicted "
                    "of three murders and died in prison in 2011. She remains one of "
                    "history's most notorious female serial killers."),
    },
    'hanna-harris': {
        'status': 'Conviction',
    },
    'kellie-poppleton': {
        'year': 1983, 'date': 'December 2, 1983', 'age': 14,
        'city': 'Fremont', 'state': 'California',
        'lastSeen': 'December 2, 1983, Fremont, California',
        'summary': ("Fourteen-year-old Kellie Poppleton disappeared in Fremont, California "
                    "on December 2, 1983 and was found murdered hours later. Despite an "
                    "extensive investigation and periodic reexamination of the evidence, "
                    "her killer has never been identified. The case remains open with "
                    "Alameda County investigators."),
        'tags': ['homicide', 'California', 'unsolved', '1983'],
    },
    'diane-suzuki': {
        'year': 1985, 'date': 'June 21, 1985', 'city': 'Aiea',
        'type': 'Missing Person',
        'lastSeen': 'June 21, 1985, dance studio in Aiea, Hawaii',
        'summary': ("Twenty-one-year-old Diane Suzuki disappeared after finishing a class "
                    "at the Aiea, Hawaii dance studio where she assisted in June 1985. She "
                    "was never found and was later declared legally dead. Investigators "
                    "treated the case as a homicide, but no one has ever been charged."),
        'tags': ['missing person', 'Hawaii', 'unsolved', '1985'],
    },
    'judy-chartier': {
        'year': 1982, 'date': 'June 5, 1982', 'age': 17,
        'city': 'Chelmsford', 'state': 'Massachusetts',
        'type': 'Missing Person',
        'lastSeen': 'June 5, 1982, leaving a party in Chelmsford, Massachusetts',
        'summary': ("Seventeen-year-old Judy Chartier disappeared after leaving a party in "
                    "Chelmsford, Massachusetts in June 1982. Neither she nor the car she "
                    "was driving has ever been found. Her case remains an open missing "
                    "persons investigation with Massachusetts authorities."),
        'tags': ['missing person', 'Massachusetts', 'unsolved', '1982'],
    },
    'janet-christman': {
        'year': 1950, 'date': 'March 18, 1950',
    },
    'tupac-shakur': {
        'state': 'Nevada',
    },
    'chandra-levy': {
        'state': 'District of Columbia', 'city': 'Washington',
    },
    'natalee-holloway': {
        'summary': ("Alabama teenager Natalee Holloway disappeared while on a graduation "
                    "trip to Aruba. She was last seen leaving a bar with Joran van der "
                    "Sloot, who was investigated repeatedly but not charged in her "
                    "disappearance. In 2023, van der Sloot admitted killing her as part of "
                    "a US federal plea agreement. Natalee was declared legally dead in 2012."),
    },
    'botham-jean': {
        'name': 'Botham Jean',
    },
    'recy-taylor': {
        'type': 'Historic Injustice',
        'status': 'No Conviction',
    },
    'virginia-christian': {
        'name': 'Virginia Christian Case',
    },
    # Police-involved and acquittal cases: perpetrator known, so "Unsolved" is
    # inaccurate — label the actual legal outcome instead.
    'eric-garner':              {'status': 'No Conviction'},
    'michael-brown':            {'status': 'No Conviction'},
    'tamir-rice':               {'status': 'No Conviction'},
    'freddie-gray':             {'status': 'No Conviction'},
    'philando-castile':         {'status': 'No Conviction'},
    'breonna-taylor':           {'status': 'No Conviction'},
    'caylee-anthony':           {'status': 'No Conviction'},
    'ron-goldman-nicole-simpson': {'status': 'No Conviction'},
    'sandra-bland':             {'status': 'Ruled Suicide'},
}

# Idaho student murders: Kohberger pleaded guilty in July 2025.
KOHBERGER_NOTE = (" Bryan Kohberger pleaded guilty to all charges in July 2025 and was "
                  "sentenced to life in prison without parole.")
for _id in ('moscow-murders', 'ethan-chapin', 'kaylee-goncalves', 'madison-mogen', 'xana-kernodle'):
    FIX.setdefault(_id, {})['status'] = 'Conviction'
    FIX[_id]['_append_summary'] = KOHBERGER_NOTE


def main():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        cases = json.load(f)
    print(f"Loaded {len(cases)} cases")

    ids = {c['id'] for c in cases}
    for old in list(REMOVE) + list(RESLUG):
        assert old in ids, f"unknown id: {old}"
    for new in RESLUG.values():
        assert new not in ids, f"re-slug target already exists: {new}"

    removed_dirs = []

    # 1. remove
    kept = []
    for c in cases:
        if c['id'] in REMOVE:
            print(f"  REMOVE {c['id']!r} ({c.get('name')!r}) — {REMOVE[c['id']]}")
            removed_dirs.append(c['id'])
        else:
            kept.append(c)
    cases = kept

    # 2. re-slug
    for c in cases:
        if c['id'] in RESLUG:
            new = RESLUG[c['id']]
            print(f"  RESLUG {c['id']!r} -> {new!r}")
            removed_dirs.append(c['id'])
            c['id'] = new

    # 3. field fixes
    for c in cases:
        fix = FIX.get(c['id'])
        if not fix:
            continue
        for k, v in fix.items():
            if k == '_append_summary':
                if v.strip() not in c.get('summary', ''):
                    c['summary'] = c.get('summary', '').rstrip() + v
            else:
                c[k] = v
        print(f"  FIX    {c['id']!r}: {', '.join(k for k in fix if k != '_append_summary')}"
              + (" +summary-note" if '_append_summary' in fix else ""))

    # sanity: unique ids
    final_ids = [c['id'] for c in cases]
    assert len(final_ids) == len(set(final_ids)), "duplicate ids after cleanup"

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(cases, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f"\nWrote {len(cases)} cases to {DATA_FILE}")

    # delete stale case page directories
    for slug in removed_dirs:
        path = os.path.join(CASES_DIR, slug)
        if os.path.isdir(path):
            shutil.rmtree(path)
    print(f"Deleted {len(removed_dirs)} stale case directories")


if __name__ == '__main__':
    main()
