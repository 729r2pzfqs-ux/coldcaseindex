#!/usr/bin/env python3
"""
ColdCaseIndex QA. Run after scripts/build.py:  python3 scripts/check.py
Exits non-zero if any check fails.
"""
import html
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://coldcaseindex.com'
SKIP_DIRS = {'.git', 'scripts', 'node_modules', '.claude'}
ALLOWED_STATUS = {'Unsolved', 'Arrest Made', 'Pending Trial', 'Conviction', 'No Conviction',
                  'Partially Solved', 'Solved', 'Identified', 'Ruled Suicide', 'Wanted'}


def pages():
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for f in files:
            if f.endswith('.html'):
                yield os.path.relpath(os.path.join(d, f), ROOT)


def main():
    errors, warnings = [], []
    titles, descs = defaultdict(list), defaultdict(list)
    info = {}
    for path in sorted(pages()):
        with open(os.path.join(ROOT, path), encoding='utf-8') as f:
            s = f.read()
        head = s.split('</head>')[0]
        robots = re.search(r'<meta name="robots" content="([^"]+)"', head)
        noindex = bool(robots and 'noindex' in robots.group(1))
        stub = 'http-equiv="refresh"' in head
        info[path] = {'noindex': noindex, 'stub': stub}
        if stub:
            continue
        t = re.search(r'<title>(.*?)</title>', head, re.S)
        d = re.search(r'<meta name="description" content="([^"]*)"', head)
        title = html.unescape(t.group(1)) if t else ''
        desc = html.unescape(d.group(1)) if d else ''
        if not title:
            errors.append(f'{path}: no title')
        if not noindex:
            if len(title) > 60:
                errors.append(f'{path}: title {len(title)} chars: {title}')
            if not 70 <= len(desc) <= 160:
                errors.append(f'{path}: description {len(desc)} chars')
            titles[title].append(path)
            descs[desc].append(path)
            if not re.search(r'<link rel="canonical" href="' + re.escape(BASE), head):
                errors.append(f'{path}: no canonical')
        if len(re.findall(r'<h1[\s>]', s)) != 1:
            errors.append(f'{path}: expected exactly one h1')
        if 'hreflang' in head:
            errors.append(f'{path}: hreflang present')
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            try:
                ld = json.loads(m.group(1))
            except ValueError as ex:
                errors.append(f'{path}: invalid JSON-LD ({ex})')
                continue
            if ld.get('@type') == 'FAQPage':
                errors.append(f'{path}: FAQPage markup present')
            if ld.get('@type') == 'BreadcrumbList':
                for item in ld['itemListElement']:
                    target = item['item'].replace(BASE, '').lstrip('/')
                    target = os.path.join(target, 'index.html') if not target.endswith('.html') else target
                    if not os.path.exists(os.path.join(ROOT, target)):
                        errors.append(f'{path}: breadcrumb target missing: {item["item"]}')
        for tag in ('juhaporraskorpi', '/Users/'):
            if tag in s:
                errors.append(f'{path}: contains "{tag}"')
        if 'fonts.googleapis.com' in head or 'fonts.gstatic.com' in head:
            errors.append(f'{path}: loads fonts from Google instead of /fonts/')
        # Mediavine requires exclusivity: no AdSense or other ad-network code may remain.
        if 'scripts.scriptwrapper.com/tags/07246c68-4098-4276-b4dd-3605803c5564.js' not in head:
            errors.append(f'{path}: Mediavine script missing from head')
        if 'id="ad-management-config-settings"' not in s.split('</head>', 1)[-1][:400]:
            errors.append(f'{path}: Mediavine ad config div missing from the top of body')
        for tag in ('adsbygoogle', 'pagead2.googlesyndication.com', 'ca-pub-', 'gtag(\'consent\''):
            if tag in s:
                errors.append(f'{path}: contains ad-network or consent code "{tag}"')
        # internal links
        base_dir = os.path.dirname(path)
        markup = re.sub(r'<script\b.*?</script>', '', s, flags=re.S)
        dup_ids = [i for i, n in Counter(re.findall(r'\sid="([^"]+)"', markup)).items() if n > 1]
        if dup_ids:
            errors.append(f'{path}: duplicate id {dup_ids[:3]}')
        for href in set(re.findall(r'<a[^>]+href="([^"#?]+)[^"]*"', markup)):
            if re.match(r'^(https?:|mailto:|tel:|//)', href):
                if href.startswith(BASE):
                    href = href[len(BASE):] or '/'
                else:
                    continue
            target = href.lstrip('/') if href.startswith('/') else os.path.normpath(os.path.join(base_dir, href))
            target = '' if target == '.' else target
            full = os.path.join(ROOT, target)
            if os.path.isdir(full):
                full = os.path.join(full, 'index.html')
            if not os.path.exists(full):
                errors.append(f'{path}: broken link {href}')
            else:
                rel = os.path.relpath(full, ROOT)
                if info.get(rel, {}).get('stub'):
                    warnings.append(f'{path}: links to redirect stub {href}')

    for t, ps in titles.items():
        if len(ps) > 1:
            errors.append(f'duplicate title "{t}": {ps[:3]}')
    for d, ps in descs.items():
        if len(ps) > 1:
            errors.append(f'duplicate description: {ps[:3]}')

    # links to stubs can only be judged once every page has been classified
    # (second pass, cheap)
    # ads.txt is static and owned by Mediavine; the build must never remove it
    ads_path = os.path.join(ROOT, 'ads.txt')
    if not os.path.exists(ads_path):
        errors.append('ads.txt is missing from the site root')
    elif 'pub-5861928596436289' in open(ads_path, encoding='utf-8').read():
        errors.append('ads.txt still lists the old AdSense publisher id')

    # sitemap
    with open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8') as f:
        locs = re.findall(r'<loc>(.*?)</loc>', f.read())
    seen = set()
    for loc in locs:
        rel = loc.replace(BASE, '').lstrip('/')
        rel = os.path.join(rel, 'index.html') if not rel.endswith('.html') else rel
        rel = os.path.normpath(rel)
        seen.add(rel)
        if rel not in info:
            errors.append(f'sitemap: {loc} does not exist')
        elif info[rel]['noindex'] or info[rel]['stub']:
            errors.append(f'sitemap: {loc} is noindex or a redirect')
    for path, i in info.items():
        if not i['noindex'] and not i['stub'] and path not in seen:
            errors.append(f'sitemap: indexable page missing: {path}')

    # data
    with open(os.path.join(ROOT, 'data', 'cases.json'), encoding='utf-8') as f:
        cases = json.load(f)
    ids = Counter(c['id'] for c in cases)
    for c in cases:
        cid = c['id']
        if ids[cid] > 1:
            errors.append(f'data: duplicate id {cid}')
        if c.get('status') not in ALLOWED_STATUS:
            errors.append(f'data: {cid} has status {c.get("status")!r}')
        years = re.findall(r'\b(1[5-9]\d\d|20\d\d)\b', str(c.get('date')))
        if years and str(c.get('year')) not in years:
            errors.append(f'data: {cid} year {c.get("year")} not in date {c.get("date")!r}')
        if not c.get('summary') or len(c['summary']) < 120:
            errors.append(f'data: {cid} summary too short')
        if not c.get('enriched'):
            warnings.append(f'data: {cid} has no researched narrative')
        srcs = [s for s in c.get('sources', []) if s.get('url')]
        if len(srcs) < 2:
            warnings.append(f'data: {cid} has {len(srcs)} source(s)')
        if not os.path.exists(os.path.join(ROOT, 'cases', cid, 'index.html')):
            errors.append(f'data: no page for {cid}')
        for t in c.get('tags') or []:
            if re.match(r'^\d{4}s', str(t)):
                errors.append(f'data: {cid} has decade tag {t!r}; decade hubs cover that')
    # the map needs cached coordinates for every mappable US city
    coords_path = os.path.join(ROOT, 'data', 'city-coords.json')
    coords = json.load(open(coords_path, encoding='utf-8')) if os.path.exists(coords_path) else {}
    for c in cases:
        if c.get('country') and c['country'] != 'United States':
            continue
        city = str(c.get('city') or '').strip()
        if not city or re.match(r'^(multiple|various|unknown|several|statewide)\b', city, re.I):
            continue
        key = f'{city}|{c.get("state")}'
        if key not in coords:
            warnings.append(f'map: no cached coordinates for {key}; run scripts/geocode.py')
        elif coords[key] is None:
            warnings.append(f'map: {key} could not be geocoded')
    cdir = os.path.join(ROOT, 'cases')
    on_disk = {d for d in os.listdir(cdir) if os.path.isdir(os.path.join(cdir, d))}
    for d in sorted(on_disk - set(ids)):
        p = f'cases/{d}/index.html'
        if not info.get(p, {}).get('stub'):
            errors.append(f'orphan case page: {p}')

    # serial killer profiles: data rules, one page per profile, section pages present
    sk_path = os.path.join(ROOT, 'data', 'serial-killers.json')
    sk_dir = os.path.join(ROOT, 'serial-killers')
    sk_states = {'alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware',
                 'district-of-columbia', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa',
                 'kansas', 'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota',
                 'mississippi', 'missouri', 'montana', 'nebraska', 'nevada', 'new-hampshire', 'new-jersey',
                 'new-mexico', 'new-york', 'north-carolina', 'north-dakota', 'ohio', 'oklahoma', 'oregon',
                 'pennsylvania', 'rhode-island', 'south-carolina', 'south-dakota', 'tennessee', 'texas', 'utah',
                 'vermont', 'virginia', 'washington', 'west-virginia', 'wisconsin', 'wyoming'}
    sk_reserved = {'lists', 'timeline', 'statistics', 'how-many-are-active-in-the-us', 'which-state-has-the-most'}
    sk_legal = {'Convicted', 'Convicted (overturned)', 'Charged', 'Died before trial', 'Confessed, never tried',
                'Suspected, never charged', 'Unidentified'}
    sk_fate = {'Imprisoned', 'Executed', 'Died in prison', 'Died (other)', 'Suicide', 'Killed', 'Released',
               'At large', 'Unknown'}
    sk_ids = set()
    if os.path.exists(sk_path):
        with open(sk_path, encoding='utf-8') as f:
            profiles = json.load(f)
        for p in profiles:
            pid = p.get('id', '?')
            if pid in sk_ids:
                errors.append(f'serial-killers: duplicate id {pid}')
            sk_ids.add(pid)
            if pid in sk_states or pid in sk_reserved:
                errors.append(f'serial-killers: id {pid} collides with a state or reserved path')
            if p.get('legalStatus') not in sk_legal:
                errors.append(f'serial-killers: {pid} legalStatus {p.get("legalStatus")!r}')
            if p.get('fate') not in sk_fate:
                errors.append(f'serial-killers: {pid} fate {p.get("fate")!r}')
            for cid in p.get('cases', []):
                if cid not in ids:
                    errors.append(f'serial-killers: {pid} links to missing case {cid}')
            if len([x for x in p.get('sources', []) if x.get('url')]) < 3:
                errors.append(f'serial-killers: {pid} has fewer than 3 sources')
            if not os.path.exists(os.path.join(sk_dir, pid, 'index.html')):
                errors.append(f'serial-killers: no page for {pid}')
            for key in ('juhaporraskorpi', 'Murderpedia', 'murderpedia.org'):
                if key in json.dumps(p):
                    errors.append(f'serial-killers: {pid} contains {key!r}')
        for st in sk_states:
            if not os.path.exists(os.path.join(sk_dir, st, 'index.html')):
                errors.append(f'serial-killers: state page missing for {st}')
        for rel in ('serial-killers/index.html', 'serial-killers/lists/index.html', 'serial-killers/timeline/index.html',
                    'serial-killers/statistics/index.html', 'serial-killers/how-many-are-active-in-the-us/index.html',
                    'serial-killers/which-state-has-the-most/index.html'):
            if rel not in info:
                errors.append(f'missing page {rel}')
            elif info[rel]['noindex'] or info[rel]['stub']:
                errors.append(f'{rel}: should be indexable')
        if os.path.isdir(sk_dir):
            for d in sorted(os.listdir(sk_dir)):
                if not os.path.isdir(os.path.join(sk_dir, d)):
                    continue
                if d in sk_ids or d in sk_states or d in sk_reserved:
                    continue
                if not info.get(f'serial-killers/{d}/index.html', {}).get('stub'):
                    errors.append(f'orphan serial killer page: serial-killers/{d}/')

    # freshness pages, feed and change tracking
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
              'september', 'october', 'november', 'december']
    for p in (['updates/index.html', 'watch/index.html', 'today/index.html', 'month/index.html',
               'map/index.html', 'analysis/index.html', 'themes/index.html', 'cities/index.html',
               'analysis/how-long-cold-cases-take-to-solve/index.html',
               'analysis/cold-case-resolution-methods/index.html']
              + [f'month/{m}/index.html' for m in months]):
        if p not in info:
            errors.append(f'missing page {p}')
        elif info[p]['noindex'] or info[p]['stub']:
            errors.append(f'{p}: should be indexable')
    feed_path = os.path.join(ROOT, 'feed.xml')
    if not os.path.exists(feed_path):
        errors.append('feed.xml missing')
    else:
        try:
            root = ET.parse(feed_path).getroot()
            ns = {'a': 'http://www.w3.org/2005/Atom'}
            entries = root.findall('a:entry', ns)
            if not entries:
                errors.append('feed.xml: no entries')
            feed_ids = []
            for en in entries:
                feed_ids.append(en.findtext('a:id', '', ns))
                href = en.find('a:link', ns).get('href', '')
                rel = href.replace(BASE, '').lstrip('/')
                if not os.path.exists(os.path.join(ROOT, rel, 'index.html')):
                    errors.append(f'feed.xml: link target missing {href}')
                for tag in ('title', 'updated', 'content'):
                    if not en.findtext(f'a:{tag}', '', ns):
                        errors.append(f'feed.xml: entry without {tag}')
            if len(feed_ids) != len(set(feed_ids)):
                errors.append('feed.xml: duplicate entry ids')
        except ET.ParseError as ex:
            errors.append(f'feed.xml: not well-formed ({ex})')
    state_path = os.path.join(ROOT, 'data', 'case-state.json')
    log_path = os.path.join(ROOT, 'data', 'changelog.json')
    if not os.path.exists(state_path) or not os.path.exists(log_path):
        errors.append('data/case-state.json or data/changelog.json missing: run scripts/build.py '
                      '(or scripts/seed_changelog.py to rebuild them from git history)')
    else:
        with open(state_path, encoding='utf-8') as f:
            if set(json.load(f)) != set(ids):
                errors.append('data/case-state.json does not match cases.json: run scripts/build.py')
        with open(log_path, encoding='utf-8') as f:
            log = json.load(f)
        allowed_kinds = {'added', 'status', 'extended', 'revised', 'removed'}
        for x in log:
            if not {'date', 'id', 'kind', 'name'} <= set(x) or x['kind'] not in allowed_kinds:
                errors.append(f'changelog.json: malformed entry {x}')
                break
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', x['date']):
                errors.append(f'changelog.json: bad date {x["date"]!r}')
                break

    size = os.path.getsize(os.path.join(ROOT, 'index.html'))
    if size > 120_000:
        errors.append(f'homepage is {size:,} bytes')

    kinds = Counter(w.split(':')[0] + ':' + w.split(':')[1].strip().split(' ')[0] if w.startswith('data') else 'link' for w in warnings)
    print(f'{len(info)} pages, {len(locs)} sitemap URLs, {len(cases)} cases, homepage {size:,} bytes')
    print(f'{len(warnings)} warnings')
    for w in warnings[:15]:
        print('  warn:', w)
    if errors:
        print(f'{len(errors)} ERRORS')
        for x in errors[:60]:
            print('  ', x)
        sys.exit(1)
    print('OK')


if __name__ == '__main__':
    main()
