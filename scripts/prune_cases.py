#!/usr/bin/env python3
"""
ColdCaseIndex — prune unverifiable cases (2026-07-08 fabrication audit).

Reads a JSON file of {"id": ..., "note": ...} entries produced by the parallel
verification audit, removes those cases from data/cases.json, and deletes their
cases/<id>/ page directories. Regeneration is a separate step
(generate_case_pages.py + generate_state_pages.py).

Usage: python3 scripts/prune_cases.py <prune_list.json>
"""

import json
import os
import shutil
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_FILE = os.path.join(ROOT_DIR, 'data', 'cases.json')
CASES_DIR = os.path.join(ROOT_DIR, 'cases')


def main():
    if len(sys.argv) != 2:
        sys.exit('usage: prune_cases.py <prune_list.json>')
    prune = json.load(open(sys.argv[1]))
    ids = {p['id'] for p in prune}

    cases = json.load(open(DATA_FILE))
    before = len(cases)
    existing = {c['id'] for c in cases}
    missing = ids - existing
    if missing:
        print(f'WARNING: {len(missing)} prune ids not in cases.json: {sorted(missing)}')

    kept = [c for c in cases if c['id'] not in ids]
    removed = [c for c in cases if c['id'] in ids]
    # Safety: never prune an enriched case via this path.
    bad = [c['id'] for c in removed if c.get('enriched')]
    if bad:
        sys.exit(f'ABORT: prune list contains enriched cases: {bad}')

    with open(DATA_FILE, 'w') as f:
        json.dump(kept, f, indent=1, ensure_ascii=False)
        f.write('\n')

    deleted_dirs = 0
    for c in removed:
        d = os.path.join(CASES_DIR, c['id'])
        if os.path.isdir(d):
            shutil.rmtree(d)
            deleted_dirs += 1

    print(f'cases: {before} -> {len(kept)} (removed {len(removed)}, deleted {deleted_dirs} page dirs)')
    for c in removed:
        print(f"  - {c['id']}: {c['name']} ({c.get('city')}, {c.get('state')} {c.get('year')})")


if __name__ == '__main__':
    main()
