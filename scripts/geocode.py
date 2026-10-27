#!/usr/bin/env python3
"""
Fill data/city-coords.json: one latitude/longitude per unique US (city, state) pair in
data/cases.json, looked up once on Nominatim (OpenStreetMap) and cached in the repo.

Run by hand whenever cases with new cities are added:   python3 scripts/geocode.py
The build never calls the network; it only reads the cached file. Cities that cannot be
geocoded are stored as null and left off the map. Coordinates are city centroids, never
addresses.
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES = os.path.join(ROOT, 'data', 'cases.json')
OUT = os.path.join(ROOT, 'data', 'city-coords.json')
UA = 'ColdCaseIndex-build/1.0 (info@coldcaseindex.com)'
SKIP = re.compile(r'^(multiple|various|unknown|several|statewide)\b', re.I)
DELAY = 1.1   # Nominatim usage policy: at most one request per second
# Places the geocoder cannot resolve, placed by hand at the named town or the centre of the area.
OVERRIDES = {
    'Lake Tahoe|Nevada': {'lat': 39.0, 'lon': -119.95, 'query': 'Lake Tahoe', 'match': 'manual: Nevada shore of Lake Tahoe'},
    'Connecticut River Valley (Claremont/Newport area)|New Hampshire': {'lat': 43.3767, 'lon': -72.3467, 'query': 'Claremont', 'match': 'manual: Claremont, NH'},
    'Sheep Mountains (near Las Vegas)|Nevada': {'lat': 36.55, 'lon': -115.2, 'query': 'Sheep Range', 'match': 'manual: Sheep Range, Clark County'},
}


def clean(city):
    """Turn a free-text place into something a geocoder can match."""
    c = re.sub(r'\s*\(.*?\)\s*', ' ', city)          # drop parenthetical notes
    c = c.split('/')[0]                               # "Santa Rosa / Sonoma County"
    c = re.sub(r'\b(metro area|metropolitan area|area|region|vicinity)$', '', c, flags=re.I)
    c = re.sub(r'^(near|rural|outside|greater)\s+', '', c, flags=re.I)
    return ' '.join(c.split()).strip(' ,')


def fetch(params):
    url = 'https://nominatim.openstreetmap.org/search?' + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def matches(result, state):
    addr = result.get('address', {})
    st = addr.get('state') or addr.get('territory') or ''
    if state == 'District of Columbia':
        return 'District of Columbia' in (st, addr.get('city', ''), result.get('display_name', ''))
    return st == state


def lookup(city, state):
    q = clean(city)
    if not q:
        return None
    attempts = [
        {'q': f'{q}, {state}, USA'},
        {'city': q, 'state': state, 'country': 'USA'},
        {'q': f'{q} County, {state}, USA'} if 'county' not in q.lower() else None,
    ]
    for p in attempts:
        if not p:
            continue
        p.update({'format': 'jsonv2', 'limit': 5, 'countrycodes': 'us', 'addressdetails': 1})
        try:
            res = fetch(p)
        except Exception as ex:  # network hiccup: give up on this city for now
            print(f'  ! {city}, {state}: {ex}', file=sys.stderr)
            time.sleep(DELAY * 3)
            continue
        time.sleep(DELAY)
        for r in res:
            if matches(r, state):
                return {'lat': round(float(r['lat']), 4), 'lon': round(float(r['lon']), 4),
                        'query': q, 'match': r.get('display_name', '')[:120]}
    return None


def main():
    with open(CASES, encoding='utf-8') as f:
        cases = json.load(f)
    coords = {}
    if os.path.exists(OUT):
        with open(OUT, encoding='utf-8') as f:
            coords = json.load(f)
    wanted = []
    for c in cases:
        if c.get('country') and c['country'] != 'United States':
            continue
        city, state = (c.get('city') or '').strip(), (c.get('state') or '').strip()
        if not city or not state or SKIP.match(city):
            continue
        key = f'{city}|{state}'
        if key not in coords and key not in wanted:
            wanted.append(key)
    retry = '--retry' in sys.argv
    if retry:
        wanted += [k for k, v in coords.items() if v is None and k not in wanted]
    print(f'{len(coords)} cached, {len(wanted)} to look up')
    for i, key in enumerate(wanted, 1):
        city, state = key.split('|', 1)
        hit = OVERRIDES.get(key) or lookup(city, state)
        coords[key] = hit
        print(f'[{i}/{len(wanted)}] {key}: ' + (f'{hit["lat"]}, {hit["lon"]}' if hit else 'NOT FOUND'), flush=True)
        with open(OUT, 'w', encoding='utf-8') as f:
            json.dump(dict(sorted(coords.items())), f, indent=0, ensure_ascii=False)
            f.write('\n')
    missing = [k for k, v in coords.items() if v is None]
    print(f'Done. {len(coords)} cities cached, {len(missing)} not found: {missing}')


if __name__ == '__main__':
    main()
