#!/usr/bin/env python3
"""
Rebuild data/changelog.json and data/case-state.json from the git history of
data/cases.json. Only needed once, or if those files are lost; the normal
build (scripts/build.py) keeps them up to date from then on.

    python3 scripts/seed_changelog.py
"""
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import changelog  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = 'data/cases.json'


def main():
    commits = subprocess.run(
        ['git', 'log', '--reverse', '--format=%H %as', '--', DATA],
        cwd=ROOT, capture_output=True, text=True, check=True).stdout.split('\n')
    log, prev = [], {}
    for line in commits:
        if not line.strip():
            continue
        sha, date = line.split()
        raw = subprocess.run(['git', 'show', f'{sha}:{DATA}'], cwd=ROOT,
                             capture_output=True, text=True).stdout
        try:
            cases = json.loads(raw)
        except ValueError:
            print(f'skip {sha[:8]} {date}: not valid JSON')
            continue
        if isinstance(cases, dict):
            cases = cases.get('cases') or []
        cur = {c['id']: changelog.snapshot(c) for c in cases if c.get('id')}
        if prev:
            entries = changelog.diff(prev, cur, date)
            log = changelog.merge(log, entries)
            print(f'{sha[:8]} {date}: {len(entries):4d} changes, {len(cur)} cases')
        else:
            # the first commit is the launch: record every case as added that day
            log = changelog.merge(log, [{'date': date, 'id': cid, 'name': s['name'], 'kind': 'added'}
                                        for cid, s in cur.items()])
            print(f'{sha[:8]} {date}: launch with {len(cur)} cases')
        prev = cur
    # the snapshot must describe the working tree, which is what the build compares against
    with open(os.path.join(ROOT, DATA), encoding='utf-8') as f:
        live = {c['id']: changelog.snapshot(c) for c in json.load(f)}
    if live != prev:
        log = changelog.merge(log, changelog.diff(prev, live, changelog.datetime.date.today().isoformat()))
    changelog.save_json(os.path.join(ROOT, 'data', 'changelog.json'), log)
    changelog.save_json(os.path.join(ROOT, 'data', 'case-state.json'), live)
    kinds = {}
    for x in log:
        kinds[x['kind']] = kinds.get(x['kind'], 0) + 1
    print(f'{len(log)} changelog entries: {kinds}')


if __name__ == '__main__':
    main()
