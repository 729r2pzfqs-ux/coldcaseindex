#!/usr/bin/env python3
"""
ColdCaseIndex — merge newly researched cases into data/cases.json.

Reads per-case JSON files from a directory (one case per file, produced by
research agents), validates them, HTTP-checks every source URL (dead links are
dropped; a case failing validation is skipped and reported), and appends the
survivors to data/cases.json with enriched:true.

Expected per-case JSON schema:
{
  "id": "kebab-slug", "name": "...", "type": "...", "status": "...",
  "year": 1990, "date": "Month D, YYYY", "state": "...", "city": "...",
  "age": 25 | null, "gender": "Female|Male|Multiple|Unknown",
  "summary": "1-3 sentences", "lastSeen": "...", "tags": [...],
  "sources": [{"title": ..., "url": ...}, ...],   # >=3 after link check
  "narrative": ["para", ...],                      # 400-600 words total
  "timeline": [{"date": ..., "event": ...}, ...]   # >=4 events
}

Usage: python3 scripts/add_cases.py <dir_of_case_jsons> [--dry-run]
"""

import concurrent.futures
import json
import os
import re
import sys
import urllib.request

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_FILE = os.path.join(ROOT_DIR, 'data', 'cases.json')

REQUIRED = ['id', 'name', 'type', 'status', 'year', 'state', 'city',
            'summary', 'sources', 'narrative', 'timeline']
VALID_STATUS = {'Unsolved', 'Conviction', 'No Conviction', 'Partially Solved',
                'Arrest Made', 'Solved', 'Exonerated', 'Identified'}
UA = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36'}


def check_url(url):
    try:
        req = urllib.request.Request(url, headers=UA, method='GET')
        with urllib.request.urlopen(req, timeout=15) as r:
            return 200 <= r.status < 400
    except Exception:
        return False


def word_count(narrative):
    return sum(len(p.split()) for p in narrative)


def validate(case, existing_ids, existing_names):
    errs = []
    for k in REQUIRED:
        if not case.get(k):
            errs.append(f'missing {k}')
    if errs:
        return errs
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', case['id']):
        errs.append(f"bad slug: {case['id']}")
    if case['id'] in existing_ids:
        errs.append(f"duplicate id: {case['id']}")
    key = (case['name'].lower(), case['year'])
    if key in existing_names:
        errs.append(f'duplicate name+year: {key}')
    if case['status'] not in VALID_STATUS:
        errs.append(f"bad status: {case['status']}")
    if not isinstance(case['narrative'], list):
        errs.append('narrative must be a list of paragraphs')
    else:
        wc = word_count(case['narrative'])
        if not 320 <= wc <= 700:
            errs.append(f'narrative {wc} words (want 400-600)')
    if len(case.get('timeline', [])) < 4:
        errs.append('timeline < 4 events')
    if not isinstance(case.get('year'), int) or not 1800 <= case['year'] <= 2026:
        errs.append(f"bad year: {case.get('year')}")
    return errs


def main():
    src_dir = sys.argv[1]
    dry = '--dry-run' in sys.argv
    cases = json.load(open(DATA_FILE))
    existing_ids = {c['id'] for c in cases}
    existing_names = {(c['name'].lower(), c['year']) for c in cases}

    files = sorted(f for f in os.listdir(src_dir) if f.endswith('.json'))
    accepted, skipped = [], []
    new_cases = []
    for fn in files:
        path = os.path.join(src_dir, fn)
        try:
            case = json.load(open(path))
        except Exception as e:
            skipped.append((fn, [f'bad json: {e}']))
            continue
        errs = validate(case, existing_ids, existing_names)
        if errs:
            skipped.append((fn, errs))
            continue
        new_cases.append(case)

    # HTTP-check all source URLs in parallel across all candidate cases.
    all_urls = {s['url'] for c in new_cases for s in c['sources']}
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
        ok = dict(zip(all_urls, ex.map(check_url, all_urls)))

    for case in new_cases:
        live = [s for s in case['sources'] if ok.get(s['url'])]
        dead = [s['url'] for s in case['sources'] if not ok.get(s['url'])]
        if len(live) < 3:
            skipped.append((case['id'], [f'only {len(live)} live sources (dead: {dead})']))
            continue
        case['sources'] = live
        case['enriched'] = True
        case.setdefault('age', None)
        case.setdefault('gender', 'Unknown')
        case.setdefault('date', str(case['year']))
        case.setdefault('lastSeen', f"{case['city']}, {case['state']}")
        case.setdefault('tags', [])
        existing_ids.add(case['id'])
        existing_names.add((case['name'].lower(), case['year']))
        accepted.append(case)
        if dead:
            print(f"  {case['id']}: dropped {len(dead)} dead link(s)")

    if not dry and accepted:
        cases.extend(accepted)
        with open(DATA_FILE, 'w') as f:
            json.dump(cases, f, indent=1, ensure_ascii=False)
            f.write('\n')

    print(f'accepted {len(accepted)}/{len(files)}; total cases now {len(cases) if not dry else len(cases) + len(accepted)}')
    for fn, errs in skipped:
        print(f'  SKIP {fn}: {"; ".join(errs)}')


if __name__ == '__main__':
    main()
