#!/usr/bin/env python3
"""
ColdCaseIndex — Source backfill.

Populates a `sources` array on every case in data/cases.json:

  1. VERIFIED Wikipedia article — only attached when the English Wikipedia has a
     matching, non-disambiguation article whose title contains a distinctive
     token of the case name AND whose intro mentions the case's year, city, or
     state. This guards against attaching the wrong same-named person's article.
  2. Type-appropriate authoritative resource(s) — NamUs / The Charley Project /
     The Doe Network for missing & unidentified cases, the Murder Accountability
     Project for homicides. Root portals only, so the links are always valid.

Only real, resolvable URLs are stored. Honestly-labeled *search* links (Wikipedia
search, news search) are generated at render time by generate_case_pages.py and
are deliberately NOT stored here, so `sources` stays a set of genuine references.

Run from the project root: python3 scripts/backfill_sources.py
"""

import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_FILE = os.path.join(ROOT_DIR, 'data', 'cases.json')

WIKI_API = 'https://en.wikipedia.org/w/api.php'
USER_AGENT = 'ColdCaseIndexBot/1.0 (https://coldcaseindex.com; info@coldcaseindex.com)'

STOPWORDS = {
    'the', 'and', 'of', 'a', 'an', 'in', 'on', 'at', 'to', 'for', 'victims',
    'victim', 'murders', 'murder', 'case', 'cases', 'killer', 'killings',
    'killing', 'jane', 'john', 'doe', 'unknown', 'family', 'three', 'four',
    'boys', 'girls', 'children', 'baby', 'bombing', 'massacre',
}


def significant_tokens(name):
    toks = re.findall(r"[A-Za-z][A-Za-z'\-]{2,}", name)
    return [t for t in toks if t.lower() not in STOPWORDS]


def type_resources(case_type):
    t = (case_type or '').lower()
    if 'missing' in t:
        return [
            {'title': 'NamUs — National Missing and Unidentified Persons System',
             'url': 'https://namus.nij.ojp.gov/'},
            {'title': 'The Charley Project — Missing Persons',
             'url': 'https://charleyproject.org/'},
        ]
    if 'unidentified' in t:
        return [
            {'title': 'NamUs — National Missing and Unidentified Persons System',
             'url': 'https://namus.nij.ojp.gov/'},
            {'title': 'The Doe Network — Unidentified & Missing',
             'url': 'https://www.doenetwork.org/'},
        ]
    # Homicide, Multiple Homicide, Serial Killer Victims, Suspicious Death, etc.
    return [
        {'title': 'Murder Accountability Project — Homicide Data',
         'url': 'https://www.murderdata.org/'},
    ]


def wiki_lookup(names):
    """Batch-query Wikipedia. Returns {queried_name: {title, extract, disambig}}."""
    out = {}
    params = {
        'action': 'query', 'format': 'json', 'redirects': 1,
        'prop': 'extracts|pageprops', 'exintro': 1, 'explaintext': 1,
        'exlimit': 'max', 'titles': '|'.join(names),
    }
    url = WIKI_API + '?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.load(resp)
    except Exception as exc:  # network hiccup — treat batch as unmatched
        print(f'  wiki batch error: {exc}', file=sys.stderr)
        return out

    query = data.get('query', {})
    # Map normalized/redirected titles back to the name we queried.
    norm = {n['from']: n['to'] for n in query.get('normalized', [])}
    redir = {r['from']: r['to'] for r in query.get('redirects', [])}

    def resolve(name):
        t = norm.get(name, name)
        seen = set()
        while t in redir and t not in seen:
            seen.add(t)
            t = redir[t]
        return t

    pages_by_title = {}
    for page in query.get('pages', {}).values():
        if 'missing' in page or page.get('pageid', 0) <= 0:
            continue
        pages_by_title[page['title']] = page

    for name in names:
        final_title = resolve(name)
        page = pages_by_title.get(final_title)
        if not page:
            continue
        out[name] = {
            'title': page['title'],
            'extract': page.get('extract', '') or '',
            'disambig': 'disambiguation' in (page.get('pageprops') or {}),
        }
    return out


def verified_wiki_source(case, hit):
    """Return a Wikipedia source dict only if the hit confidently matches."""
    if not hit or hit['disambig']:
        return None
    title = hit['title']
    extract = hit['extract'].lower()

    toks = significant_tokens(case.get('name', ''))
    title_l = title.lower()
    if toks and not any(tok.lower() in title_l for tok in toks):
        return None  # article is not about this named subject

    year = str(case.get('year') or '')
    city = (case.get('city') or '').strip().lower()
    state = (case.get('state') or '').strip().lower()
    anchor = False
    if year and year in extract:
        anchor = True
    elif city and city not in ('', 'unknown') and city in extract:
        anchor = True
    elif state and state not in ('', 'unknown') and state in extract:
        anchor = True
    if not anchor:
        return None  # can't tie the article to this case's time/place

    url = 'https://en.wikipedia.org/wiki/' + urllib.parse.quote(title.replace(' ', '_'))
    return {'title': f'{title} — Wikipedia', 'url': url}


def main():
    with open(DATA_FILE, encoding='utf-8') as f:
        cases = json.load(f)
    print(f'Loaded {len(cases)} cases')

    # Batch Wikipedia lookups (20 titles/request keeps exintro extracts full).
    hits = {}
    batch = []
    BATCH = 20
    for i, case in enumerate(cases):
        batch.append(case['name'])
        if len(batch) == BATCH or i == len(cases) - 1:
            hits.update(wiki_lookup(batch))
            batch = []
            time.sleep(0.3)  # be polite to the API

    verified = 0
    for case in cases:
        sources = []
        wiki = verified_wiki_source(case, hits.get(case['name']))
        if wiki:
            sources.append(wiki)
            verified += 1
        sources.extend(type_resources(case.get('type')))
        # de-dup by url, preserve order
        seen, deduped = set(), []
        for s in sources:
            if s['url'] not in seen:
                seen.add(s['url'])
                deduped.append(s)
        case['sources'] = deduped

    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(cases, f, ensure_ascii=False, indent=2)
        f.write('\n')

    print(f'Verified Wikipedia articles attached: {verified}/{len(cases)}')
    print(f'Wrote sources for all {len(cases)} cases -> {DATA_FILE}')


if __name__ == '__main__':
    main()
