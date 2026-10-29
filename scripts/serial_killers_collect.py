#!/usr/bin/env python3
"""Collect, verify and merge serial killer profiles. Run by hand; the build never calls the network.

  python3 scripts/serial_killers_collect.py verify <dir>   check every draft JSON in <dir>: schema, word
                                                           counts, HTTP status of every source URL; dead
                                                           links are removed, blocked ones are kept and flagged
  python3 scripts/serial_killers_collect.py merge <dir>    merge the drafts that passed into
                                                           data/serial-killers.json (sorted, indent=1)
  python3 scripts/serial_killers_collect.py volumes        apply SEARCH_VOLUME to data/serial-killers.json

candidates / infobox / select (Wikipedia list and infobox harvest, Radford cross-check) are phase 2
and not implemented yet; see docs/serial-killers-plan.md section 4.2.
"""
import json
import os
import re
import socket
import ssl
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT, 'data', 'serial-killers.json')
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ColdCaseIndex-linkcheck/1.0'

# Monthly search volume from the keyword review (2026-10). Drives the "famous" list and the hub's
# featured cards. Add a line when a profile's volume is known.
SEARCH_VOLUME = {
    'jerry-brudos': 82000, 'israel-keyes': 76000, 'albert-fish': 71000, 'edmund-kemper': 29000,
    'richard-cottingham': 22000, 'charles-cullen': 19000, 'bobby-joe-long': 18000, 'dean-corll': 18000,
    'gary-heidnik': 13000, 'joel-rifkin': 12000, 'joseph-deangelo': 11000, 'todd-kohlhepp': 11000,
    'danny-rolling': 10000, 'randy-kraft': 9700, 'shawn-grate': 9600, 'nannie-doss': 9400,
    'robert-berdella': 9100, 'carl-panzram': 8700, 'shelly-knotek': 8400, 'anthony-sowell': 8300,
    'gary-ridgway': 40000, 'herb-baumeister': 13000,
    # Ahrefs Keywords Explorer, US, 2026-10-29 (phase 4). Read from the per-term clusters of an 82-keyword
    # list, so only names whose surname or alias term is unique to one keyword are recorded.
    'jeffrey-dahmer': 990000, 'ted-bundy': 364000, 'john-wayne-gacy': 275000, 'aileen-wuornos': 255000,
    'zodiac-killer': 174000, 'rex-heuermann': 145000, 'richard-ramirez': 112000, 'rodney-alcala': 79000,
    'dennis-rader': 70000, 'david-berkowitz': 42000, 'samuel-little': 38000, 'wayne-williams': 26000,
    'dorothea-puente': 20000, 'robert-hansen': 19000, 'henry-lee-lucas': 12000, 'h-h-holmes': 11000,
    'henry-louis-wallace': 7500, 'ottis-toole': 7400, 'albert-desalvo': 6900, 'richard-chase': 6600,
    'keith-jesperson': 6500, 'derrick-todd-lee': 6400, 'tommy-lynn-sells': 6200, 'robert-ben-rhoades': 6100,
    'belle-gunness': 5200, 'christopher-wilder': 4800, 'robert-yates': 4800, 'william-bonin': 4600,
    'donald-gaskins': 4100, 'charles-ng': 3900, 'jane-toppan': 3900, 'herbert-mullin': 3700,
    'gary-michael-hilton': 3500, 'kenneth-bianchi': 3200, 'kristen-gilbert': 3200, 'scott-kimball': 3100,
    'kenneth-mcduff': 3100, 'paul-john-knowles': 3000, 'velma-barfield': 2900, 'edward-wayne-edwards': 2700,
    'arthur-shawcross': 2700, 'lawrence-bittaker': 2600, 'lonnie-franklin': 2600, 'khalil-wheeler-weaver': 2500,
    'axeman-of-new-orleans': 2400, 'juan-corona': 2400, 'genene-jones': 2400, 'westley-allan-dodd': 2200,
    'judy-buenoano': 2100,
}

LEGAL = {'Convicted', 'Convicted (overturned)', 'Charged', 'Died before trial', 'Confessed, never tried',
         'Not guilty by reason of insanity', 'Suspected, never charged', 'Unidentified'}
FATE = {'Imprisoned', 'Executed', 'Died in prison', 'Died (other)', 'Suicide', 'Killed', 'Released',
        'At large', 'Unknown'}
REQUIRED = ['id', 'name', 'aliases', 'born', 'died', 'gender', 'country', 'states', 'primaryState',
            'cities', 'activeFrom', 'activeTo', 'victims', 'victimProfile', 'method', 'apprehended',
            'captureMethod', 'legalStatus', 'sentence', 'fate', 'fateDetail', 'summary', 'narrative',
            'timeline', 'cases', 'tags', 'sources', 'wikipedia', 'enriched', 'verified']
BANNED_HOSTS = ('murderpedia.org', 'fandom.com', 'reddit.com', 'medium.com', 'quora.com', 'pinterest.')
DEAD = 'dead'
LIVE = 'live'
BLOCKED = 'blocked'


def http_status(url):
    """LIVE for 2xx/3xx, DEAD for 404/410/DNS failure, BLOCKED for 403/429/5xx/timeouts."""
    ctx = ssl.create_default_context()
    for method in ('HEAD', 'GET'):
        req = urllib.request.Request(url, method=method, headers={'User-Agent': UA, 'Accept': '*/*'})
        try:
            with urllib.request.urlopen(req, timeout=20, context=ctx) as r:
                if 200 <= r.status < 400:
                    return LIVE, r.status
        except urllib.error.HTTPError as ex:
            if ex.code in (404, 410):
                return DEAD, ex.code
            if method == 'GET':
                return BLOCKED, ex.code
        except (urllib.error.URLError, socket.timeout, ssl.SSLError, ConnectionError, OSError) as ex:
            reason = str(getattr(ex, 'reason', ex))
            if 'nodename' in reason or 'Name or service' in reason or 'getaddrinfo' in reason:
                return DEAD, reason[:40]
            if method == 'GET':
                return BLOCKED, reason[:40]
    return BLOCKED, '?'


def schema_errors(p, case_ids):
    errs = []
    miss = [k for k in REQUIRED if k not in p]
    if miss:
        return [f'missing keys {miss}']
    if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', p['id']):
        errs.append('id is not a slug')
    if p['legalStatus'] not in LEGAL:
        errs.append(f'legalStatus {p["legalStatus"]!r}')
    if p['fate'] not in FATE:
        errs.append(f'fate {p["fate"]!r}')
    if p['country'] != 'United States':
        errs.append('country must be United States at this stage')
    if not p['states'] or p['primaryState'] not in p['states']:
        errs.append('primaryState must be one of states')
    if not isinstance(p['activeFrom'], int) or not isinstance(p['activeTo'], int) or p['activeFrom'] > p['activeTo']:
        errs.append('activeFrom/activeTo')
    v = p['victims']
    for k in ('convicted', 'confessed'):
        if v.get(k) is not None and not isinstance(v[k], int):
            errs.append(f'victims.{k} must be int or null')
    if not (120 <= len(p['summary']) <= 300):
        errs.append(f'summary {len(p["summary"])} chars')
    words = sum(len(x.split()) for x in p['narrative'])
    if not (400 <= words <= 950):
        errs.append(f'narrative {words} words')
    if not (5 <= len(p['timeline']) <= 20):
        errs.append(f'timeline {len(p["timeline"])} events')
    for ev in p['timeline']:
        if not re.match(r'^\d{4}(-\d{2})?(-\d{2})?$', str(ev.get('date', ''))):
            errs.append(f'timeline date {ev.get("date")!r}')
            break
    for cid in p['cases']:
        if cid not in case_ids:
            errs.append(f'unknown case id {cid}')
    for key in ('<', '>', 'juhaporraskorpi'):
        if key in json.dumps(p['narrative']) + p['summary']:
            errs.append(f'narrative contains {key!r}')
    return errs


def verify(d):
    with open(os.path.join(ROOT, 'data', 'cases.json'), encoding='utf-8') as f:
        case_ids = {c['id'] for c in json.load(f)}
    out_dir = os.path.join(d, 'verified')
    os.makedirs(out_dir, exist_ok=True)
    passed = failed = 0
    for name in sorted(os.listdir(d)):
        if not name.endswith('.json') or name == 'facts.json':
            continue
        path = os.path.join(d, name)
        try:
            with open(path, encoding='utf-8') as f:
                p = json.load(f)
        except json.JSONDecodeError as ex:
            print(f'FAIL {name}: not JSON ({ex})')
            failed += 1
            continue
        errs = schema_errors(p, case_ids)
        kept, report = [], []
        for s in p.get('sources', []):
            url = s.get('url', '')
            if any(h in url for h in BANNED_HOSTS):
                report.append(f'    banned  {url}')
                continue
            status, code = http_status(url)
            report.append(f'    {status:7} {code!s:5} {url}')
            if status != DEAD:
                s['_status'] = status
                kept.append(s)
        live = sum(1 for s in kept if s['_status'] == LIVE)
        if len(kept) < 3:
            errs.append(f'{len(kept)} sources after link check')
        for s in kept:
            s.pop('_status', None)
        p['sources'] = kept
        print(f'{"FAIL" if errs else "ok  "} {p.get("id", name)}: {live} live, {len(kept) - live} blocked, {len(p.get("sources", []))} kept'
              + (f'; {"; ".join(errs)}' if errs else ''))
        for line in report:
            print(line)
        if errs:
            failed += 1
            continue
        with open(os.path.join(out_dir, name), 'w', encoding='utf-8') as f:
            json.dump(p, f, ensure_ascii=False, indent=1)
            f.write('\n')
        passed += 1
    print(f'{passed} passed, {failed} failed; verified drafts in {out_dir}')
    return failed == 0


def merge(d):
    src = os.path.join(d, 'verified') if os.path.isdir(os.path.join(d, 'verified')) else d
    existing = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, encoding='utf-8') as f:
            existing = json.load(f)
    by_id = {p['id']: p for p in existing}
    added = updated = 0
    for name in sorted(os.listdir(src)):
        if not name.endswith('.json') or name == 'facts.json':
            continue
        with open(os.path.join(src, name), encoding='utf-8') as f:
            p = json.load(f)
        if p['id'] in SEARCH_VOLUME:
            p['searchVolume'] = SEARCH_VOLUME[p['id']]
        if p['id'] in by_id:
            updated += 1
        else:
            added += 1
        by_id[p['id']] = p
    rows = [by_id[k] for k in sorted(by_id)]
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'{added} added, {updated} updated, {len(rows)} profiles in {DATA_FILE}')


def volumes():
    with open(DATA_FILE, encoding='utf-8') as f:
        rows = json.load(f)
    n = 0
    for p in rows:
        if p['id'] in SEARCH_VOLUME and p.get('searchVolume') != SEARCH_VOLUME[p['id']]:
            p['searchVolume'] = SEARCH_VOLUME[p['id']]
            n += 1
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print(f'{n} volumes updated')


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    if cmd == 'verify' and len(sys.argv) == 3:
        sys.exit(0 if verify(sys.argv[2]) else 1)
    elif cmd == 'merge' and len(sys.argv) == 3:
        merge(sys.argv[2])
    elif cmd == 'volumes':
        volumes()
    elif cmd in ('candidates', 'infobox', 'select'):
        sys.exit(f'{cmd}: planned for phase 2, see docs/serial-killers-plan.md section 4.2')
    else:
        sys.exit(__doc__)
