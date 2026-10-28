"""Serial killer profiles for /serial-killers/.

Data:   data/serial-killers.json        one object per offender (schema in docs/serial-killers-plan.md)
        data/serial-killers-facts.json  cited national figures for the answer pages
Pages:  /serial-killers/                       hub
        /serial-killers/<state>/               51 state pages (noindex below the thresholds)
        /serial-killers/<id>/                  one profile per offender
        /serial-killers/lists/, lists/<slug>/  computed lists
        /serial-killers/timeline/              profiles by decade
        /serial-killers/statistics/            figures computed from the dataset
        /serial-killers/how-many-are-active-in-the-us/
        /serial-killers/which-state-has-the-most/

build.py calls init(build) once, then load(cases) before case pages render (so case pages
can link to offender profiles) and write_all(...) to write the section. Everything here
renders with the helpers in build.py; nothing fetches the network.
"""
import json
import os
import re
from collections import Counter, defaultdict

B = None  # the build module, set by init()
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT, 'data', 'serial-killers.json')
FACTS_FILE = os.path.join(ROOT, 'data', 'serial-killers-facts.json')
SECTION = 'serial-killers'
SECTION_LABEL = 'Serial Killers'
NAV_LABEL = 'Serial Killers'

LEGAL = ['Convicted', 'Convicted (overturned)', 'Charged', 'Died before trial',
         'Confessed, never tried', 'Suspected, never charged', 'Unidentified']
FATE = ['Imprisoned', 'Executed', 'Died in prison', 'Died (other)', 'Suicide', 'Killed',
        'Released', 'At large', 'Unknown']
# Legal status -> badge class. The five badge colours are the site's checked set.
LEGAL_BADGE = {'Convicted': 'badge-conviction', 'Convicted (overturned)': 'badge-partial',
               'Charged': 'badge-arrest', 'Died before trial': 'badge-neutral',
               'Confessed, never tried': 'badge-neutral', 'Suspected, never charged': 'badge-partial',
               'Unidentified': 'badge-unsolved'}
LEGAL_EXPLAIN = {
    'Convicted': 'A court convicted this person of murder; the counts are stated in the sentence line.',
    'Convicted (overturned)': 'A conviction was recorded and later overturned; the page states what the courts found.',
    'Charged': 'This person has been charged and not convicted. They are presumed innocent until a court decides otherwise.',
    'Died before trial': 'This person died before any trial. The attribution rests on official findings, stated in the narrative.',
    'Confessed, never tried': 'This person confessed and was never tried for these killings. Confessions are stated as confessions.',
    'Suspected, never charged': 'An official body publicly named this person; no charge was ever brought.',
    'Unidentified': 'The offender has never been identified. The profile describes the series, not a person.',
}
ALIVE_FATES = {'Imprisoned', 'Released', 'At large', 'Unknown'}

# Monthly search volume for "[state] serial killers" style queries (keyword review, 2026-10).
# States not listed are treated as under 100 a month until a volume is recorded.
STATE_VOLUME = {'Wisconsin': 2000, 'California': 2000, 'Texas': 600, 'Virginia': 600, 'Florida': 450,
                'Illinois': 450, 'Ohio': 400, 'Indiana': 350, 'Washington': 350, 'Michigan': 300,
                'Oregon': 250, 'New York': 250, 'Colorado': 200}
# States whose higher-volume query is "serial killers in [state]" rather than "[state] serial killers".
STATE_PHRASE = {'Texas': 'in'}
# Profiles published below the 3-murder bar, each with the reason. Every entry here is an
# editorial decision recorded in docs/serial-killers-plan.md section 3.4.
THRESHOLD_EXCEPTIONS = {
    'gary-heidnik': 'two murder convictions; six women held captive in the same series',
}
MIN_PROFILES_HIGH = 2    # indexable from this many profiles when the state is in STATE_VOLUME
MIN_PROFILES_LOW = 3     # ... and from this many otherwise
MIN_LIST = 5             # a list is indexable from this many entries
FEATURED_N = 12

ANSWER_ACTIVE = 'how-many-are-active-in-the-us'
ANSWER_STATE = 'which-state-has-the-most'
RESERVED = {'lists', 'timeline', 'statistics', ANSWER_ACTIVE, ANSWER_STATE}

REQUIRED = ['id', 'name', 'aliases', 'born', 'died', 'gender', 'country', 'states', 'primaryState',
            'cities', 'activeFrom', 'activeTo', 'victims', 'victimProfile', 'method', 'apprehended',
            'captureMethod', 'legalStatus', 'sentence', 'fate', 'fateDetail', 'summary', 'narrative',
            'timeline', 'cases', 'tags', 'sources', 'wikipedia', 'enriched', 'verified']

PROFILES = []
BY_STATE = defaultdict(list)
BY_CASE = defaultdict(list)
FACTS = []


def init(build):
    global B
    B = build


def e(x):
    return B.e(x)


# ─────────────────────────── data ───────────────────────────

def state_slug(state):
    return B.slugify(state)


def _count_from_suspected(s):
    m = re.search(r'\d+', str(s or ''))
    return int(m.group()) if m else None


def load(cases):
    """Read, validate and derive. Fails the build on a schema error."""
    global PROFILES, FACTS
    if not os.path.exists(DATA_FILE):
        PROFILES = []
        return PROFILES
    with open(DATA_FILE, encoding='utf-8') as f:
        profiles = json.load(f)
    with open(FACTS_FILE, encoding='utf-8') as f:
        FACTS = json.load(f) if os.path.exists(FACTS_FILE) else []
    case_by_id = {c['id']: c for c in cases}
    state_names = set(B.viz.STATE_ABBR)
    state_slugs = {state_slug(s) for s in state_names}
    errors = []
    ids = Counter(p.get('id') for p in profiles)
    for p in profiles:
        pid = p.get('id') or '?'
        miss = [k for k in REQUIRED if k not in p]
        if miss:
            errors.append(f'{pid}: missing keys {miss}')
            continue
        if ids[pid] > 1:
            errors.append(f'{pid}: duplicate id')
        if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', pid):
            errors.append(f'{pid}: id is not a slug')
        if pid in RESERVED or pid in state_slugs:
            errors.append(f'{pid}: id collides with a reserved path or a state slug')
        if p['legalStatus'] not in LEGAL:
            errors.append(f'{pid}: legalStatus {p["legalStatus"]!r}')
        if p['fate'] not in FATE:
            errors.append(f'{pid}: fate {p["fate"]!r}')
        if p['country'] != 'United States':
            errors.append(f'{pid}: only United States profiles are published at this stage')
        if not p['states'] or any(s not in state_names for s in p['states']):
            errors.append(f'{pid}: states {p["states"]!r} must be US state names')
        if p['primaryState'] not in p['states']:
            errors.append(f'{pid}: primaryState not in states')
        if not isinstance(p['activeFrom'], int) or not isinstance(p['activeTo'], int) or p['activeFrom'] > p['activeTo']:
            errors.append(f'{pid}: activeFrom/activeTo {p["activeFrom"]!r}/{p["activeTo"]!r}')
        v = p['victims']
        if not isinstance(v, dict) or any(k not in v for k in ('convicted', 'confessed', 'suspected')):
            errors.append(f'{pid}: victims must have convicted, confessed, suspected')
        else:
            for k in ('convicted', 'confessed'):
                if v[k] is not None and not isinstance(v[k], int):
                    errors.append(f'{pid}: victims.{k} must be an integer or null')
            best = max([x for x in (v['convicted'], v['confessed'], _count_from_suspected(v['suspected'])) if x is not None] or [0])
            if best < 3 and p['legalStatus'] != 'Unidentified' and pid not in THRESHOLD_EXCEPTIONS:
                errors.append(f'{pid}: fewer than 3 attributed victims ({best})')
        if not (120 <= len(p['summary']) <= 300):
            errors.append(f'{pid}: summary is {len(p["summary"])} chars (120 to 300)')
        words = sum(len(x.split()) for x in p['narrative'])
        if not (380 <= words <= 900):
            errors.append(f'{pid}: narrative is {words} words (400 to 800)')
        if not (5 <= len(p['timeline']) <= 20):
            errors.append(f'{pid}: timeline has {len(p["timeline"])} events (5 to 20)')
        for ev in p['timeline']:
            if not re.match(r'^\d{4}(-\d{2})?(-\d{2})?$', str(ev.get('date', ''))) or not ev.get('text'):
                errors.append(f'{pid}: timeline event {ev!r} needs an ISO date and text')
                break
        live = [s for s in p['sources'] if s.get('url', '').startswith('http') and s.get('title')]
        if len(live) < 3:
            errors.append(f'{pid}: {len(live)} sources (at least 3)')
        for cid in p['cases']:
            if cid not in case_by_id:
                errors.append(f'{pid}: linked case {cid!r} does not exist')
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', str(p['verified'])):
            errors.append(f'{pid}: verified must be YYYY-MM-DD')
        if p['legalStatus'] == 'Charged' and p['fate'] not in ('Imprisoned', 'Unknown', 'At large'):
            errors.append(f'{pid}: a charged person cannot have fate {p["fate"]!r}')
    if errors:
        raise SystemExit('serial-killers.json:\n  ' + '\n  '.join(errors))

    for p in profiles:
        a, b = p['activeFrom'], p['activeTo']
        p['_years'] = str(a) if a == b else f'{a} to {b}'
        p['_decade'] = a // 10 * 10
        p['_cases'] = [case_by_id[c] for c in p['cases']]
        p['_alive'] = p['died'] is None and p['fate'] in ALIVE_FATES
        p['_caught'] = p['legalStatus'] != 'Unidentified' and p['fate'] != 'At large'
        v = p['victims']
        p['_count'] = next((x for x in (v['convicted'], v['confessed'], _count_from_suspected(v['suspected'])) if x), 0)
        p['_events'] = [(str(ev['date']), str(ev['text'])) for ev in p['timeline']]
        p['_alias'] = p['aliases'][0] if p['aliases'] else ''
        p['_sources'] = [s for s in p['sources'] if s.get('url', '').startswith('http')]
        p['_url'] = f'{B.BASE_URL}/{SECTION}/{p["id"]}/'
        p['_open'] = p['fate'] == 'At large' or p['legalStatus'] == 'Unidentified'
        ap = str(p['apprehended'] or '')
        p['_years_to_arrest'] = (int(ap[:4]) - a) if re.match(r'^\d{4}', ap) else None
    profiles.sort(key=lambda p: (p['name'].split()[-1].lower(), p['name'].lower()))
    PROFILES = profiles
    BY_STATE.clear()
    BY_CASE.clear()
    for p in profiles:
        for s in p['states']:
            BY_STATE[s].append(p)
        for c in p['cases']:
            BY_CASE[c].append(p)
    return profiles


def search_rows(profiles):
    return [{'id': p['id'], 'name': p['name'], 'type': 'Serial killer', 'status': p['legalStatus'],
             'year': p['activeFrom'], 'state': p['primaryState'], 'city': None, 'age': None,
             'summary': B.fit(p['summary'], 120), 'url': f'{SECTION}/{p["id"]}/'} for p in profiles]


# ─────────────────────────── shared markup ───────────────────────────

def badge(p, small=False):
    style = ' style="font-size:11px;"' if small else ''
    return f'<span class="badge {LEGAL_BADGE[p["legalStatus"]]}"{style}>{e(p["legalStatus"])}</span>'


def victims_text(p, short=False):
    v = p['victims']
    parts = []
    if v['convicted'] is not None:
        parts.append(f'{v["convicted"]} convicted')
    if v['confessed'] is not None:
        parts.append(f'{v["confessed"]} confessed')
    if v['suspected']:
        parts.append(f'{v["suspected"]} suspected')
    if short:
        return parts[0] if parts else 'count not established'
    return ', '.join(parts) if parts else 'count not established'


def state_name(state):
    """Heading form that matches the state's higher-volume query."""
    return f'Serial Killers in {state}' if STATE_PHRASE.get(state) == 'in' else f'{state} Serial Killers'


def state_href(prefix, state):
    return f'{prefix}{SECTION}/{state_slug(state)}/'


def profile_href(prefix, p):
    return f'{prefix}{SECTION}/{p["id"]}/'


def card(p, prefix):
    alias = f'<p class="case-card-alias">{e(p["_alias"])}</p>' if p['_alias'] else ''
    return f'''<a href="{profile_href(prefix, p)}" class="case-card">
        <div class="case-card-header">
          {badge(p)}
          <span class="case-card-year">{e(p['_years'])}</span>
        </div>
        <h3 class="case-card-name">{e(p['name'])}</h3>
        {alias}
        <p class="case-card-summary">{e(B.fit(p['summary'], 230))}</p>
        <div class="case-card-tags">
          <span class="case-tag">{e(p['primaryState'])}</span>
          <span class="case-tag">{e(victims_text(p, short=True))}</span>
          <span class="case-tag">{e(p['fate'])}</span>
        </div>
      </a>'''


def small_card(p, prefix):
    return f'''<a href="{profile_href(prefix, p)}" class="related-case-card">
            <div class="related-case-header">
              {badge(p, small=True)}
              <span class="case-card-year">{e(p['_years'])}</span>
            </div>
            <div class="related-case-name">{e(p['name'])}</div>
            <div class="related-case-meta">{e(p['_alias'] or p['primaryState'])} · {e(victims_text(p, short=True))}</div>
          </a>'''


def table(profiles, prefix, rank=True, caption=''):
    rows = []
    for i, p in enumerate(profiles, 1):
        v = p['victims']
        name = f'<a href="{profile_href(prefix, p)}">{e(p["name"])}</a>'
        cells = ([str(i)] if rank else []) + [
            name, e(p['_alias'] or '—'), e(', '.join(p['states'])), e(p['_years']),
            '—' if v['convicted'] is None else str(v['convicted']),
            '—' if v['confessed'] is None else str(v['confessed']),
            e(v['suspected'] or '—'), e(p['legalStatus']), e(p['fate'])]
        rows.append(cells)
    headers = (['#'] if rank else []) + ['Name', 'Alias', 'State', 'Active', 'Convicted', 'Confessed',
                                         'Suspected', 'Legal status', 'Fate']
    return B.data_table(headers, rows, caption)


def by_state_counts():
    return {s: len(BY_STATE.get(s, [])) for s in B.viz.STATE_ABBR}


def tile_figure(prefix, title, sub):
    counts = by_state_counts()
    bins = [2, 5, 10, 20, 10 ** 6]
    fills = {}
    for s, n in counts.items():
        if n:
            i = next(k for k, b in enumerate(bins) if n <= b)
            fills[B.viz.STATE_ABBR[s]] = (B.viz.SEQ_RAMP[i], B.viz.SEQ_INK[i])
    tips = {B.viz.STATE_ABBR[s]: f'{s}: {B.plural(n, "profile")}' for s, n in counts.items()}
    links = {B.viz.STATE_ABBR[s]: state_href(prefix, s) for s in counts}
    W, H, tiles = B.viz.tile_map(fills=fills, links=links, tips=tips)
    legend = ''.join(f'<li><span class="swatch" style="background:{B.viz.SEQ_RAMP[i]}"></span>{lab}</li>'
                     for i, lab in enumerate(['1 to 2', '3 to 5', '6 to 10', '11 to 20', 'More than 20']))
    return f'''<figure class="viz" data-mediavine-no-ads>
        <div class="viz-title">{e(title)}</div>
        <div class="viz-sub">{sub}</div>
        <svg viewBox="0 0 {W} {H}" role="img" aria-label="Tile map of US states shaded by number of serial killer profiles" xmlns="http://www.w3.org/2000/svg">{tiles}</svg>
        <ul class="viz-legend">{legend}</ul>
      </figure>'''


def state_chips(prefix, only_with=False):
    counts = by_state_counts()
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return ''.join(f'<a class="breakdown-chip" href="{state_href(prefix, s)}"><strong>{n}</strong> {e(s)}</a>'
                   for s, n in items if n or not only_with)


def sources_html(p):
    items = ''.join(f'<li><a href="{e(s["url"])}" target="_blank" rel="noopener noreferrer nofollow">{e(s["title"])}</a></li>'
                    for s in p['_sources'])
    return f'''<div class="case-sources">
        <h2 class="section-label">Sources</h2>
        <p class="case-sources-note">References used for this profile, checked on {B.viz.human_date(p['verified'])}. ColdCaseIndex is an index of public information; victims are named only where these sources name them.</p>
        <ul class="case-sources-list">{items}</ul>
      </div>'''


def corrections_html(p):
    return f'''<div class="how-to-help">
        <h2 class="how-to-help-heading">Corrections and family contact</h2>
        <p class="how-to-help-text">This profile states only what courts, official bodies and the cited reporting have recorded. {e(LEGAL_EXPLAIN[p['legalStatus']])}</p>
        <p class="how-to-help-note">If you are a relative of a victim named here and want a name corrected, updated or removed, or if you can show that a fact on this page is wrong, email <a href="mailto:{B.CONTACT}">{B.CONTACT}</a>. Requests from families are acted on first.</p>
      </div>'''


def section_links(prefix, current=None):
    links = [('', 'All serial killers'), ('lists/', 'Lists'), ('timeline/', 'Timeline'),
             ('statistics/', 'Statistics'), (f'{ANSWER_ACTIVE}/', 'How many are active?'),
             (f'{ANSWER_STATE}/', 'Which state has the most?')]
    return ''.join(f'<a href="{prefix}{SECTION}/{path}">{e(label)}</a>' for path, label in links if path != current)


def crumbs(prefix, trail):
    """trail: [(label, path under /serial-killers/ or None)]"""
    items = [('Home', ''), (SECTION_LABEL, f'{SECTION}/')] + [
        (label, None if path is None else f'{SECTION}/{path}') for label, path in trail]
    return B.breadcrumb_html(items, prefix)


def crumbs_ld(trail):
    items = [('Home', f'{B.BASE_URL}/'), (SECTION_LABEL, f'{B.BASE_URL}/{SECTION}/')] + [
        (label, f'{B.BASE_URL}/{SECTION}/{path}') for label, path in trail]
    return B.breadcrumb_ld(items)


def collection_ld(name, desc, url, profiles=None):
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": name,
          "description": desc, "url": url, "inLanguage": "en-US",
          "isPartOf": {"@type": "WebSite", "name": B.SITE, "url": f"{B.BASE_URL}/"}}
    if profiles:
        ld["mainEntity"] = {"@type": "ItemList", "numberOfItems": len(profiles),
                            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": p['name'],
                                                 "url": p['_url']} for i, p in enumerate(profiles)]}
    return ld


def article_ld(h1, desc, url, published, modified, about=None, section='Serial killers'):
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": B.fit(h1, 110),
          "description": desc, "url": url, "mainEntityOfPage": {"@type": "WebPage", "@id": url},
          "image": B.OG_IMAGE, "inLanguage": "en-US", "articleSection": section,
          "datePublished": published, "dateModified": modified,
          "author": {"@type": "Organization", "name": B.SITE, "url": f'{B.BASE_URL}/about/'},
          "publisher": {"@type": "Organization", "name": B.SITE, "url": B.BASE_URL,
                        "logo": {"@type": "ImageObject", "url": f"{B.BASE_URL}/logos/logo-icon-512x512.png"}},
          "isBasedOn": {"@type": "Dataset", "name": f"{B.SITE} serial killer profiles",
                        "url": f"{B.BASE_URL}/data/serial-killers.json"}}
    if about:
        ld["about"] = about
    return ld


def featured(profiles):
    ranked = sorted(profiles, key=lambda p: (-(p.get('searchVolume') or 0), -p['_count'], p['name']))
    return ranked[:FEATURED_N]


def facts_for(page):
    return [f for f in FACTS if f.get('page') in (page, 'both')]


def facts_html(items):
    if not items:
        return ''
    lis = ''.join(f'<li>{e(f["claim"])} <a href="{e(f["sourceUrl"])}" target="_blank" rel="noopener noreferrer nofollow">({e(f["sourceTitle"])})</a></li>'
                  for f in items)
    return f'<ul class="how-to-help-list">{lis}</ul>'


# ─────────────────────────── lists ───────────────────────────

LISTS = [
    ('famous', 'Famous Serial Killers', 'Famous Serial Killers: The Most Searched Names',
     'The most searched serial killers in the United States, ranked by how often people look them up, '
     'not by any judgement about the crimes. Each entry links to a profile with counts, dates, the '
     'capture method and sources.',
     lambda p: bool(p.get('searchVolume')), lambda p: (-(p.get('searchVolume') or 0), p['name'])),
    ('most-victims', 'Serial Killers With the Most Victims', 'Serial Killers With the Most Victims',
     'Ranked by the number of murders a court convicted the person of. Confessed and suspected counts '
     'are shown separately because they rest on weaker evidence than a conviction.',
     lambda p: True, lambda p: (-(p['victims']['convicted'] or 0), -(p['victims']['confessed'] or 0), p['name'])),
    ('female', 'Female Serial Killers', 'Female Serial Killers in the United States',
     'Women convicted of, or officially linked to, three or more murders. Poisoning and killings of '
     'family members or patients recur in this group far more than in the male profiles.',
     lambda p: p['gender'] == 'Female', lambda p: (p['activeFrom'], p['name'])),
    ('never-caught', 'Serial Killers Who Were Never Caught', 'Serial Killers Who Were Never Caught',
     'Series in which the offender was never identified, or was identified but never taken into '
     'custody. The linked case files hold the victims and the investigation.',
     lambda p: p['_open'], lambda p: (p['activeFrom'], p['name'])),
    ('still-alive', 'Serial Killers Still Alive', 'Serial Killers Who Are Still Alive',
     'Profiles with no recorded death: almost all are serving life sentences. Status is as of the '
     'verification date on each profile.',
     lambda p: p['_alive'], lambda p: (p['name'].split()[-1], p['name'])),
    ('executed', 'Executed Serial Killers', 'Serial Killers Who Were Executed',
     'Profiles ending in a state or federal execution, in date order.',
     lambda p: p['fate'] == 'Executed', lambda p: (str(p['died'] or ''), p['name'])),
    ('died-in-prison', 'Serial Killers Who Died in Prison', 'Serial Killers Who Died in Prison',
     'Profiles ending in death in custody, from natural causes, suicide or at the hands of other inmates, '
     'as recorded by the sources.',
     lambda p: p['fate'] in ('Died in prison', 'Suicide') and p['apprehended'], lambda p: (str(p['died'] or ''), p['name'])),
]


def list_entries(profiles):
    return {slug: sorted([p for p in profiles if keep(p)], key=key) for slug, _t, _h, _i, keep, key in LISTS}


# ─────────────────────────── renderers ───────────────────────────

def render_hub(profiles, serial_cases):
    prefix = '../'
    url = f'{B.BASE_URL}/{SECTION}/'
    n = len(profiles)
    counts = by_state_counts()
    states_with = sum(1 for v in counts.values() if v)
    convicted = sum(1 for p in profiles if p['legalStatus'].startswith('Convicted'))
    executed = sum(1 for p in profiles if p['fate'] == 'Executed')
    open_n = sum(1 for p in profiles if p['_open'])
    linked = sum(len(p['cases']) for p in profiles)
    lists = list_entries(profiles)
    feat = featured(profiles)
    list_cards = ''.join(f'''<a href="./lists/{slug}/" class="state-card">
          <div class="state-card-header"><span class="state-name">{e(title)}</span><span class="state-count-badge">{len(lists[slug])}</span></div>
          <div class="state-card-meta">{e(B.fit(intro, 120))}</div>
        </a>''' for slug, title, _h, intro, _k, _s in LISTS)
    more_cards = f'''<a href="./{ANSWER_ACTIVE}/" class="state-card">
          <div class="state-card-header"><span class="state-name">How many serial killers are active in the US?</span></div>
          <div class="state-card-meta">What the FBI and academic databases estimate, and what this dataset shows about how long offenders stayed active before capture.</div>
        </a>
        <a href="./{ANSWER_STATE}/" class="state-card">
          <div class="state-card-header"><span class="state-name">Which state has the most serial killers?</span></div>
          <div class="state-card-meta">The published rankings, the per-capita caveat, and this dataset's count for every state.</div>
        </a>
        <a href="./timeline/" class="state-card">
          <div class="state-card-header"><span class="state-name">Timeline by decade</span></div>
          <div class="state-card-meta">Every profile placed by the year of the first known murder, from the 1920s to today.</div>
        </a>
        <a href="./statistics/" class="state-card">
          <div class="state-card-header"><span class="state-name">Statistics</span></div>
          <div class="state-card-meta">Counts by state, decade, method, legal outcome and years to arrest, computed from the dataset on every build.</div>
        </a>'''
    desc = B.fit(f'{B.plural(n, "serial killer profile")} across {states_with} US states: names, years active, '
                 f'convicted and suspected victim counts, how each was caught, and linked case files. '
                 f'Browse by state or by list.', 158)
    body = f'''
  <section class="section">
    <div class="section-inner">
      {B.breadcrumb_html([('Home', ''), (SECTION_LABEL, None)], prefix)}
      <h1 class="section-heading">Serial Killers: Profiles, Lists and Cases by State</h1>
      <p class="section-subtext">Documented profiles of serial killers in the United States, each with the counts a court found, the counts the person confessed to and the counts police attribute, kept separate; years active; how the person was caught; the legal outcome; and the sources. The section covers offenders linked to three or more killings. It grows in order of public interest, so the best-known names come first.</p>
      {B.stat_row([(n, 'profiles'), (states_with, 'states covered'), (convicted, 'convicted'), (open_n, 'never caught'), (linked, 'linked case files')])}

      <h2 class="sub-heading">Serial killers by state</h2>
      {tile_figure(prefix, 'Profiles by state', 'Darker tiles hold more profiles. This reflects what the section covers so far, not where serial murder is most common. Select a state to open its page.')}
      <div class="breakdown-row">{state_chips(prefix)}</div>

      <h2 class="sub-heading">Most searched profiles</h2>
      <div class="cases-grid">{''.join(card(p, prefix) for p in feat)}</div>

      <h2 class="sub-heading">Lists</h2>
      <div class="states-grid">{list_cards}</div>

      <h2 class="sub-heading">Questions and analysis</h2>
      <div class="states-grid">{more_cards}</div>

      <h2 class="sub-heading">Case files</h2>
      <p class="section-subtext">The victims of these offenders are documented as cases, with their own timelines and sources. {B.plural(len(serial_cases), "serial murder case file")} are indexed under <a class="prose-link" href="{prefix}types/serial-killer-cases/">serial killer cases</a>; each profile links to the case files it is connected to.</p>

      <div class="how-to-help">
        <h2 class="how-to-help-heading">How these profiles are compiled</h2>
        <p class="how-to-help-text">Each profile is written from court opinions, corrections records, official releases and established reporting, with every claim attributed in the text and every source listed and checked on the date shown. Nobody is described as a killer without a conviction, a formal charge or an official attribution, and pending cases say "charged", not "guilty". Victims are named only where the public record names them.</p>
        <p class="how-to-help-note">Corrections, including requests from victims' families: <a href="mailto:{B.CONTACT}">{B.CONTACT}</a>.</p>
      </div>
    </div>
  </section>
'''
    schema = [
        B.breadcrumb_ld([('Home', f'{B.BASE_URL}/'), (SECTION_LABEL, url)]),
        collection_ld('Serial killers: profiles, lists and cases by state', desc, url, feat),
        {"@context": "https://schema.org", "@type": "Dataset", "name": f"{B.SITE} serial killer profiles",
         "description": "Structured profiles of US serial killers: names, aliases, states, years active, "
                        "convicted, confessed and suspected victim counts, capture method, legal status, "
                        "sentence, fate, timeline and sources.",
         "url": url, "license": "https://creativecommons.org/licenses/by-nc/4.0/",
         "creator": {"@type": "Organization", "name": B.SITE, "url": B.BASE_URL},
         "distribution": [{"@type": "DataDownload", "encodingFormat": "application/json",
                           "contentUrl": f"{B.BASE_URL}/data/serial-killers.json"}]},
    ]
    return lambda p, m: B.page(title='Serial Killers: Profiles, Lists and Cases by State', desc=desc,
                               canonical=url, prefix=prefix, body=body, schema=schema, active=NAV_LABEL)


def render_state(state, profs, serial_cases, all_states):
    prefix = '../../'
    slug = state_slug(state)
    url = f'{B.BASE_URL}/{SECTION}/{slug}/'
    n = len(profs)
    name = state_name(state)
    ordered = sorted(profs, key=lambda p: (p['activeFrom'], p['name']))
    known_vol = state in STATE_VOLUME
    indexable = n >= (MIN_PROFILES_HIGH if known_vol else MIN_PROFILES_LOW)
    ab = B.viz.STATE_ABBR[state]
    links = {B.viz.STATE_ABBR[s]: f'../{state_slug(s)}/' for s in all_states}
    locator = f'''<figure class="viz locator" data-mediavine-no-ads>
        <div class="viz-title">{e(state)}</div>
        <div class="viz-sub">Select another state to see its serial killers.</div>
        {B.viz.locator_map(state, links)}
      </figure>'''
    cases_html = ''
    if serial_cases:
        cases_html = f'''<h2 class="sub-heading">Serial murder case files from {e(state)}</h2>
      <p class="section-subtext">Victim-centred case pages from the cold case index, with their own timelines and sources.</p>
      <div class="cases-grid">{''.join(B.case_card(c, prefix) for c in serial_cases)}</div>'''
    others = ''.join(f'<a href="../{state_slug(s)}/"><strong>{len(BY_STATE[s])}</strong> {e(s)}</a>'
                     for s in sorted(BY_STATE, key=lambda s: (-len(BY_STATE[s]), s)) if s != state)
    if n:
        years = sorted(p['activeFrom'] for p in ordered)
        span = str(years[0]) if years[0] == years[-1] else f'{years[0]} to {years[-1]}'
        first, last = ordered[0], ordered[-1]
        caught = sum(1 for p in profs if p['_caught'])
        linked = sum(len(p['cases']) for p in profs)
        title = next(t for t in (f'{name}: {B.plural(n, "Documented Profile")}', f'{name} | {B.SITE}', name) if len(t) <= 60)
        desc = B.fit(f'{B.plural(n, "documented serial killer")} in {state}, active {span}: '
                     f'{", ".join(p["name"] for p in ordered[:3])}. Years active, victim counts, how each '
                     f'was caught, legal outcome and sources.', 158)
        intro = (f'{B.SITE} documents {B.plural(n, "serial killer")} whose murders took place in {e(state)}, '
                 f'with first known killings from {span}. {caught} of them {"was" if caught == 1 else "were"} '
                 f'caught; {B.plural(linked, "linked case file")} document their victims. The earliest series is '
                 f'<a href="../{first["id"]}/">{e(first["name"])}</a> ({first["activeFrom"]}) and the most recent is '
                 f'<a href="../{last["id"]}/">{e(last["name"])}</a> ({last["activeFrom"]}). Profiles are added in '
                 f'order of public interest, so this page is not a complete census of the state.')
        main = f'''<h2 class="sub-heading">All {B.plural(n, "profile")}</h2>
      <div class="cases-grid">{''.join(card(p, prefix) for p in ordered)}</div>
      <h2 class="sub-heading">At a glance</h2>
      {table(ordered, prefix, rank=False, caption=f'Serial killers in {state}, by first known murder')}'''
        stats = B.stat_row([(n, 'profiles'), (caught, 'caught'), (sum(1 for p in profs if p['fate'] == 'Executed'), 'executed'),
                            (sum(1 for p in profs if p['_alive']), 'still alive'), (linked, 'linked case files')])
    else:
        title = next(t for t in (f'{name} | {B.SITE}', name) if len(t) <= 60)
        desc = B.fit(f'No serial killer profiles for {state} have been published yet. '
                     f'{B.plural(len(serial_cases), "serial murder case file")} and '
                     f'the state cold case list are available while profiles are researched.', 158)
        intro = (f'{B.SITE} has not yet published a serial killer profile for {e(state)}. Profiles are '
                 f'researched in order of public interest and this page will list them as they are added. '
                 f'The <a href="{prefix}states/{slug}/">{e(state)} cold case list</a> is available now.')
        main = ''
        stats = ''
    body = f'''
  <section class="section">
    <div class="section-inner">
      {crumbs(prefix, [(state, None)])}
      <h1 class="section-heading">{e(name)}</h1>
      <p class="section-subtext">{intro}</p>
      {stats}
      <div class="case-visuals" style="margin-top:var(--space-6)"><div></div>{locator}</div>
      {main}
      {cases_html}
      <h2 class="sub-heading">More</h2>
      <div class="hub-links"><a href="{prefix}states/{slug}/">All {e(state)} cold cases</a>{section_links(prefix)}</div>
      <h2 class="sub-heading">Other states with profiles</h2>
      <div class="hub-links">{others}<a href="../">All states</a></div>
    </div>
  </section>
'''
    schema = [crumbs_ld([(state, f'{slug}/')]), collection_ld(name, desc, url, ordered)]
    return (lambda p, m: B.page(title=title, desc=desc, canonical=url, prefix=prefix, body=body, schema=schema,
                                active=NAV_LABEL, robots=None if indexable else 'noindex,follow')), indexable


def related(p, profiles):
    same = sorted((o for o in profiles if o is not p and set(o['states']) & set(p['states'])),
                  key=lambda o: (abs(o['activeFrom'] - p['activeFrom']), o['name']))[:4]
    same_ids = {o['id'] for o in same}
    score = Counter()
    for o in profiles:
        if o is p or o['id'] in same_ids:
            continue
        s = 0
        if set(o['method']) & set(p['method']):
            s += 2
        if abs(o['_decade'] - p['_decade']) <= 10:
            s += 1
        if o['fate'] == p['fate']:
            s += 0.5
        if set(o['tags']) & set(p['tags']):
            s += 1.5
        if s:
            score[o['id']] = s
    by_id = {o['id']: o for o in profiles}
    similar = [by_id[i] for i, _ in sorted(score.items(), key=lambda kv: (-kv[1], by_id[kv[0]]['name']))][:4]
    return same, similar


def render_profile(p, profiles, state_links):
    prefix = '../../'
    url = p['_url']
    alias = p['_alias']
    v = p['victims']
    nv = v['convicted'] if (v['convicted'] or 0) >= 3 else None
    title = next(t for t in (
        (f'{p["name"]}, the {alias.replace("The ", "")}: {nv} Victims, {p["_years"]}' if alias and nv else ''),
        (f'{p["name"]}: {nv} Victims, {p["primaryState"]}, {p["_years"]}' if nv else ''),
        f'{p["name"]}: Serial Killer, {p["primaryState"]}, {p["_years"]}',
        f'{p["name"]}: Serial Killer, {p["primaryState"]}', f'{p["name"]} | {B.SITE}', p['name']) if t and len(t) <= 60)
    desc = B.fit(f'{p["legalStatus"]}. {p["summary"]}', 158)
    same, similar = related(p, profiles)

    details = [('Also known as', e(', '.join(p['aliases']))) if p['aliases'] else None,
               ('Legal status', badge(p, small=True)),
               ('Active', e(p['_years'])),
               ('States', ', '.join(f'<a href="../{state_slug(s)}/">{e(s)}</a>' for s in p['states'])),
               ('Cities', e(', '.join(p['cities']))) if p['cities'] else None,
               ('Victims', e(victims_text(p))),
               ('Victim profile', e(p['victimProfile'])) if p['victimProfile'] else None,
               ('Method', e(', '.join(p['method']))) if p['method'] else None,
               ('Apprehended', e(B.viz.human_date(p['apprehended']))) if p['apprehended'] else None,
               ('How caught', e(p['captureMethod'])) if p['captureMethod'] else None,
               ('Sentence', e(p['sentence'])) if p['sentence'] else None,
               ('Fate', e(p['fate']) + (f': {e(p["fateDetail"])}' if p['fateDetail'] else '')),
               ('Born', e(B.viz.human_date(p['born']))) if p['born'] else None,
               ('Died', e(B.viz.human_date(p['died']))) if p['died'] else None]
    grid = ''.join(f'''<div class="case-detail-item">
          <dt class="case-detail-label">{k}</dt>
          <dd class="case-detail-value">{val}</dd>
        </div>''' for k, val in [d for d in details if d])

    strip = B.viz.timeline_strip(p['_events'], p['activeFrom'], p['_open'], B.BUILD_YEAR)
    strip_html = f'''<figure class="viz" data-mediavine-no-ads>
          <div class="viz-title">Timeline to scale</div>
          <div class="viz-sub">Each dot is a dated event below; the distance between dots is elapsed time. The darker dot marks the first known murder.</div>
          {strip}
        </figure>''' if strip else ''
    links = {B.viz.STATE_ABBR[s]: f'../{state_slug(s)}/' for s in B.viz.STATE_ABBR}
    n_state = len(BY_STATE[p['primaryState']])
    locator_html = f'''<figure class="viz locator" data-mediavine-no-ads>
          <div class="viz-title">{e(p['primaryState'])}</div>
          <div class="viz-sub"><a class="prose-link" href="../{state_slug(p['primaryState'])}/">{B.plural(n_state, 'serial killer profile')} in {e(p['primaryState'])}</a>. Select any state to browse its profiles.</div>
          {B.viz.locator_map(p['primaryState'], links)}
        </figure>'''
    visuals = (f'<div class="case-visuals"><div>{strip_html}</div>{locator_html}</div>' if strip_html
               else f'<div class="case-visuals"><div></div>{locator_html}</div>')
    narrative = '\n'.join(f'        <p class="case-narrative">{e(x)}</p>' for x in p['narrative'] if x.strip())
    items = '\n'.join(f'''<li class="timeline-item">
            <div class="timeline-marker" aria-hidden="true"></div>
            <div>
              <div class="timeline-label">{e(B.viz.human_date(d))}</div>
              <div class="timeline-value">{e(t)}</div>
            </div>
          </li>''' for d, t in p['_events'])
    cases_html = ''
    if p['_cases']:
        cases_html = f'''<div style="margin-top: var(--space-8);">
        <h2 class="section-label">Victims and case files</h2>
        <p class="case-sources-note">The victims are documented as cases in the cold case index, each with its own timeline and sources.</p>
        <div class="cases-grid">{''.join(B.case_card(c, prefix, place='city') for c in p['_cases'])}</div>
      </div>'''
    tags = ''.join(f'<span class="case-tag">{e(t)}</span>' for t in p['tags'])
    lists = [(slug, t) for slug, t, _h, _i, keep, _s in LISTS if keep(p)]
    list_links = ''.join(f'<a href="../lists/{slug}/">{e(t)}</a>' for slug, t in lists)
    related_html = ''
    if same:
        related_html += f'''
  <section class="section" style="background: var(--color-surface);">
    <div class="section-inner">
      <h2 class="section-heading">Other serial killers in {e(p['primaryState'])}</h2>
      <div class="related-grid">{''.join(small_card(o, prefix) for o in same)}</div>
      <a href="../{state_slug(p['primaryState'])}/" class="all-state-link">All {e(state_name(p['primaryState']).lower())} &rarr;</a>
    </div>
  </section>'''
    if similar:
        related_html += f'''
  <section class="section">
    <div class="section-inner">
      <h2 class="section-heading">Similar profiles</h2>
      <p class="section-subtext">Profiles sharing a method, era or theme with this one.</p>
      <div class="related-grid">{''.join(small_card(o, prefix) for o in similar)}</div>
      <div class="hub-links">{list_links}{section_links(prefix)}</div>
    </div>
  </section>'''
    about = {"@type": "Person", "name": p['name']}
    if p['aliases']:
        about["alternateName"] = p['aliases']
    if p['born']:
        about["birthDate"] = p['born']
    if p['died']:
        about["deathDate"] = p['died']
    ld_crumbs = crumbs_ld([(p['name'], f'{p["id"]}/')])

    def render(published, modified):
        mod_h = B.viz.human_date(modified) if modified != '0000-00-00' else ''
        article = article_ld(p['name'], desc, url, published, modified, about=about)
        article["citation"] = [{"@type": "CreativeWork", "name": s['title'], "url": s['url']} for s in p['_sources']]
        body = f'''
  <section class="section">
    <div class="section-inner">
      {crumbs(prefix, [(p['name'], None)])}

      <div class="case-page-header">
        <div class="case-page-meta-row">
          {badge(p)}
          <span class="case-year-label">{e(p['_years'])}</span>
          <span class="case-type-label">Serial killer profile</span>
        </div>
        <h1 class="case-page-title">{e(p['name'])}</h1>
        {f'<p class="case-alias">{e(alias)}</p>' if alias else ''}
      </div>

      <p class="case-summary">{e(p['summary'])}</p>

      <dl class="case-details-grid" data-mediavine-no-ads>
        {grid}
      </dl>

      {visuals}

      <div class="case-narrative-section">
        <h2 class="section-label">What the record shows</h2>
{narrative}
      </div>

      <div class="case-tags-section" style="display:flex;gap:var(--space-2);flex-wrap:wrap;margin-top:var(--space-5);">{tags}</div>

      <div style="margin-top: var(--space-8);">
        <h2 class="section-label">Timeline</h2>
        <ol class="timeline">{items}</ol>
      </div>

      {cases_html}

      {sources_html(p)}

      {corrections_html(p)}

      <p class="case-updated">Facts last verified {B.viz.human_date(p['verified'])}. Page last updated {mod_h}.</p>

      {B.cite_html(p['name'], url, modified)}
    </div>
  </section>
{related_html}
'''
        return B.page(title=title, desc=desc, canonical=url, prefix=prefix, body=body,
                      schema=[article, ld_crumbs], active=NAV_LABEL, og_type='article',
                      published=published, modified=modified)
    return render


def render_list(slug, title, h1, intro, entries):
    prefix = '../../../'
    url = f'{B.BASE_URL}/{SECTION}/lists/{slug}/'
    n = len(entries)
    indexable = n >= MIN_LIST
    names = ', '.join(p['name'] for p in entries[:3])
    desc = B.fit(f'{B.plural(n, "serial killer")} on this list: {names}. {intro}', 158) if n else B.fit(f'{title}: {intro}', 158)
    answer = (f'{B.SITE} currently lists {B.plural(n, "serial killer")} in this group, out of '
              f'{len(PROFILES)} profiles. The list is computed from the dataset on every build, so it changes as '
              f'profiles are added.' if n else
              f'No profile in the dataset meets this definition yet. The list is computed from the dataset on '
              f'every build and will fill as profiles are added.')
    others = ''.join(f'<a href="../{s}/">{e(t)}</a>' for s, t, *_ in LISTS if s != slug)
    main = (f'''{table(entries, prefix, rank=True, caption=h1)}
      <h2 class="sub-heading">Profiles</h2>
      <div class="cases-grid">{''.join(card(p, prefix) for p in entries)}</div>''' if n else '')
    body = f'''
  <section class="section">
    <div class="section-inner">
      {crumbs(prefix, [('Lists', 'lists/'), (title, None)])}
      <h1 class="section-heading">{e(h1)}</h1>
      <p class="section-subtext">{e(intro)}</p>
      <p class="case-summary">{e(answer)}</p>
      {main}
      <h2 class="sub-heading">Other lists</h2>
      <div class="hub-links">{others}<a href="../">All lists</a>{section_links(prefix)}</div>
    </div>
  </section>
'''
    schema = [crumbs_ld([('Lists', 'lists/'), (title, f'lists/{slug}/')]), collection_ld(h1, desc, url, entries)]
    if "mainEntity" in schema[1]:
        schema[1]["mainEntity"]["itemListOrder"] = "https://schema.org/ItemListOrderDescending" if slug in ('famous', 'most-victims') else "https://schema.org/ItemListOrderAscending"
    page_title = next(t for t in (f'{h1}', f'{title} | {B.SITE}', title) if len(t) <= 60)
    return (lambda p, m: B.page(title=page_title, desc=desc, canonical=url, prefix=prefix, body=body, schema=schema,
                                active=NAV_LABEL, robots=None if indexable else 'noindex,follow')), indexable


def render_lists_index(lists):
    prefix = '../../'
    url = f'{B.BASE_URL}/{SECTION}/lists/'
    cards = ''.join(f'''<a href="./{slug}/" class="state-card">
          <div class="state-card-header"><span class="state-name">{e(title)}</span><span class="state-count-badge">{len(lists[slug])}</span></div>
          <div class="state-card-meta">{e(B.fit(intro, 140))}</div>
        </a>''' for slug, title, _h, intro, _k, _s in LISTS)
    desc = B.fit(f'{len(LISTS)} lists of US serial killers computed from {len(PROFILES)} documented profiles: '
                 f'most victims, female, never caught, still alive, executed, died in prison, most searched.', 158)
    body = f'''
  <section class="section">
    <div class="section-inner">
      {crumbs(prefix, [('Lists', None)])}
      <h1 class="section-heading">Serial Killer Lists</h1>
      <p class="section-subtext">Each list is computed from the profile dataset on every build, using the definition stated at the top of the list. Rankings use counts and dates only.</p>
      <div class="states-grid" style="margin-top:var(--space-8)">{cards}</div>
      <h2 class="sub-heading">More</h2>
      <div class="hub-links">{section_links(prefix, 'lists/')}</div>
    </div>
  </section>
'''
    schema = [crumbs_ld([('Lists', 'lists/')]), collection_ld('Serial killer lists', desc, url)]
    return lambda p, m: B.page(title=f'Serial Killer Lists | {B.SITE}', desc=desc, canonical=url, prefix=prefix,
                               body=body, schema=schema, active=NAV_LABEL)


def render_timeline(profiles):
    prefix = '../../'
    url = f'{B.BASE_URL}/{SECTION}/timeline/'
    by_dec = defaultdict(list)
    for p in profiles:
        by_dec[p['_decade']].append(p)
    decades = sorted(by_dec)
    data = [(f'{d}s', len(by_dec.get(d, []))) for d in range(decades[0], decades[-1] + 10, 10)] if decades else []
    chart = B.viz.columns(data, links={f'{d}s': f'#{d}s' for d in by_dec}, unit='profile',
                          label='Profiles by decade of first known murder') if data else ''
    sections = ''
    for d in decades:
        rows = ''.join(f'<li class="anniv-item"><span class="anniv-year">{p["activeFrom"]}</span>'
                       f'<span class="anniv-text"><a href="../{p["id"]}/">{e(p["name"])}</a>'
                       f'{(" (" + e(p["_alias"]) + ")") if p["_alias"] else ""}, {e(", ".join(p["states"]))}, '
                       f'active {e(p["_years"])}, {e(victims_text(p, short=True))}, {e(p["fate"].lower())}.</span></li>'
                       for p in sorted(by_dec[d], key=lambda p: (p['activeFrom'], p['name'])))
        sections += f'<h2 class="sub-heading" id="{d}s">{d}s: {B.plural(len(by_dec[d]), "profile")}</h2><ol class="anniv-list">{rows}</ol>'
    desc = B.fit(f'{len(profiles)} US serial killers placed by the year of their first known murder, '
                 f'{decades[0]}s to {decades[-1]}s, with states, counts and outcomes for each.', 158) if decades else 'Timeline of US serial killers by decade.'
    body = f'''
  <section class="section">
    <div class="section-inner">
      {crumbs(prefix, [('Timeline', None)])}
      <h1 class="section-heading">Serial Killers Timeline, by Decade</h1>
      <p class="section-subtext">Every profile in the dataset placed by the year of the first known murder. Decades with more profiles reflect both the history of serial murder in the United States, which peaked in the 1970s and 1980s, and which profiles have been written so far.</p>
      <figure class="viz" data-mediavine-no-ads>
        <div class="viz-title">Profiles by decade of first known murder</div>
        <div class="viz-sub">Select a column to jump to that decade.</div>
        {chart}
      </figure>
      {sections}
      <h2 class="sub-heading">More</h2>
      <div class="hub-links">{section_links(prefix, 'timeline/')}<a href="{prefix}decades/">Cold cases by decade</a></div>
    </div>
  </section>
'''
    schema = [crumbs_ld([('Timeline', 'timeline/')]), collection_ld('Serial killers timeline by decade', desc, url, profiles)]
    return lambda p, m: B.page(title='Serial Killers Timeline by Decade', desc=desc, canonical=url, prefix=prefix,
                               body=body, schema=schema, active=NAV_LABEL)


def _report(slug, title, h1, desc, lead, sections, notes, active_label=None):
    prefix = '../../'
    url = f'{B.BASE_URL}/{SECTION}/{slug}/'
    notes_html = ''.join(f'<li>{n}</li>' for n in notes)

    def render(published, modified):
        mod_h = B.viz.human_date(modified) if modified != '0000-00-00' else ''
        body = f'''
  <section class="section">
    <div class="section-inner">
      {crumbs(prefix, [(title, None)])}
      <div class="case-page-header">
        <div class="case-page-meta-row"><span class="case-type-label">Serial killers</span><span class="case-year-label">Computed from {B.plural(len(PROFILES), 'profile')}, {mod_h}</span></div>
        <h1 class="case-page-title">{e(h1)}</h1>
      </div>
      <p class="case-summary">{lead}</p>
      {sections}
      <div class="case-narrative-section">
        <h2 class="section-label">Method and caveats</h2>
        <ul class="how-to-help-list">{notes_html}</ul>
        <p class="case-narrative">Figures from this site are recomputed from <a href="{prefix}data/serial-killers.json">the published profile dataset</a> on every build. The dataset grows in order of public interest and is not a census of serial murder; the national figures quoted above come from the sources named next to them. To report an error, email <a href="mailto:{B.CONTACT}">{B.CONTACT}</a>.</p>
      </div>
      <p class="case-updated">Last recomputed {mod_h}.</p>
      {B.cite_html(h1, url, modified)}
      <h2 class="sub-heading">More</h2>
      <div class="hub-links">{section_links(prefix, f'{slug}/')}</div>
    </div>
  </section>
'''
        return B.page(title=title if len(title) <= 60 else B.fit(title, 60), desc=desc, canonical=url, prefix=prefix,
                      body=body, schema=[article_ld(h1, desc, url, published, modified), crumbs_ld([(title, f'{slug}/')])],
                      active=NAV_LABEL, og_type='article', published=published, modified=modified)
    return render


def _fig(title, sub, inner):
    return f'''<figure class="viz" data-mediavine-no-ads>
        <div class="viz-title">{e(title)}</div>
        <div class="viz-sub">{sub}</div>
        {inner}
      </figure>'''


def render_statistics(profiles):
    prefix = '../../'
    n = len(profiles)
    by_dec = Counter(p['_decade'] for p in profiles)
    decs = sorted(by_dec)
    dec_data = [(f'{d}s', by_dec.get(d, 0)) for d in range(decs[0], decs[-1] + 10, 10)] if decs else []
    methods = Counter(m for p in profiles for m in p['method'])
    fates = Counter(p['fate'] for p in profiles)
    legal = Counter(p['legalStatus'] for p in profiles)
    yta = [p['_years_to_arrest'] for p in profiles if p['_years_to_arrest'] is not None]
    within_1 = sum(1 for y in yta if y <= 1)
    within_5 = sum(1 for y in yta if y <= 5)
    over_10 = sum(1 for y in yta if y > 10)
    med = sorted(yta)[len(yta) // 2] if yta else None
    counts = by_state_counts()
    state_rows = [[f'<a href="../{state_slug(s)}/">{e(s)}</a>', str(c),
                   str(sum(p['victims']['convicted'] or 0 for p in BY_STATE[s]))]
                  for s, c in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])) if c]
    victims_conv = sum(p['victims']['convicted'] or 0 for p in profiles)
    dna = sum(1 for p in profiles if re.search(r'\bDNA\b|genealog', p['captureMethod'] or '', re.I))
    female = sum(1 for p in profiles if p['gender'] == 'Female')
    sections = f'''
      {B.stat_row([(n, 'profiles'), (victims_conv, 'murder convictions in total'), (f'{med:g}' if med is not None else '—', 'median years to arrest'),
                   (dna, 'caught through DNA'), (female, 'women'), (fates.get('Executed', 0), 'executed')])}
      {_fig('Profiles by decade of first known murder', 'First known murder, by decade.', B.viz.columns(dec_data, unit='profile', label='Profiles by decade') if dec_data else '')}
      {_fig('Years from first murder to arrest', f'{len(yta)} profiles with an arrest date. {within_1} were arrested within a year of the first known murder, {within_5} within five years and {over_10} after more than ten.',
            B.viz.columns([('Under 1 year', within_1), ('1 to 5', within_5 - within_1), ('6 to 10', len(yta) - within_5 - over_10), ('Over 10', over_10)], unit='profile', label='Years to arrest') if yta else '')}
      <h2 class="sub-heading">By state</h2>
      {tile_figure(prefix, 'Profiles by state', 'Darker tiles hold more profiles. Select a state to open its page.')}
      {B.data_table(['State', 'Profiles', 'Murder convictions'], state_rows, 'Profiles and convictions by state')}
      <h2 class="sub-heading">Legal outcome and fate</h2>
      {B.data_table(['Legal status', 'Profiles'], [[e(k), str(v)] for k, v in legal.most_common()], 'Legal status')}
      {B.data_table(['Fate', 'Profiles'], [[e(k), str(v)] for k, v in fates.most_common()], 'What happened to the offender')}
      <h2 class="sub-heading">Method</h2>
      {B.data_table(['Method', 'Profiles'], [[e(k), str(v)] for k, v in methods.most_common()], 'Methods recorded in the profiles; a profile can list more than one')}
'''
    desc = B.fit(f'Serial killer statistics computed from {n} documented US profiles: counts by state and decade, '
                 f'years from first murder to arrest, legal outcomes, fates and methods.', 158)
    lead = (f'These figures are computed from the {n} serial killer profiles in this dataset. They describe the '
            f'profiles written so far, which are chosen by public interest, not a representative sample of serial '
            f'murder in the United States. For national estimates see '
            f'<a class="prose-link" href="../{ANSWER_ACTIVE}/">how many serial killers are active</a> and '
            f'<a class="prose-link" href="../{ANSWER_STATE}/">which state has the most</a>.')
    notes = ['Counts use the legal status, fate, states and dates recorded on each profile; see the schema in the site source.',
             'Years to arrest is the arrest year minus the year of the first known murder; profiles with no arrest are left out.',
             'A profile is counted under every state in which it records murders, so state totals can exceed the number of profiles.',
             'Murder convictions sum the convicted counts only; confessed and suspected numbers are not added.']
    return _report('statistics', 'Serial Killer Statistics', 'Serial Killer Statistics', desc, lead, sections, notes)


def render_answer_active(profiles):
    n = len(profiles)
    open_n = sum(1 for p in profiles if p['_open'])
    spans = [p['activeTo'] - p['activeFrom'] + 1 for p in profiles]
    med_span = sorted(spans)[len(spans) // 2] if spans else 0
    long_n = sum(1 for s in spans if s >= 10)
    recent = [p for p in profiles if p['activeTo'] >= 2000]
    facts = facts_for('active')
    by_dec = Counter(p['_decade'] for p in profiles)
    decs = sorted(by_dec)
    dec_data = [(f'{d}s', by_dec.get(d, 0)) for d in range(decs[0], decs[-1] + 10, 10)] if decs else []
    answer_lead = ('Nobody counts active serial killers directly, because an offender is only known to be one '
                   'after the murders are linked. The published estimates below come from the FBI, from the '
                   'Radford University and Florida Gulf Coast University database, and from the Murder '
                   'Accountability Project, and they measure different things: how many offenders are operating '
                   'at a given moment, how many have ever been documented, and how many unsolved murders look '
                   'like the work of a repeat killer.')
    sections = f'''
      <div class="case-narrative-section">
        <h2 class="section-label">What the published estimates say</h2>
        {facts_html(facts) or '<p class="case-narrative">National figures with their sources are added to this page as they are verified.</p>'}
      </div>
      <h2 class="sub-heading">What this dataset shows</h2>
      {B.stat_row([(n, 'profiles'), (open_n, 'never caught'), (f'{med_span}', 'median years active'), (long_n, 'active 10 years or more'), (len(recent), 'active since 2000')])}
      {_fig('Profiles by decade of first known murder', 'Profiles are added in order of public interest, so this reflects which names are documented so far as much as the history of serial murder.', B.viz.columns(dec_data, unit='profile', label='Profiles by decade') if dec_data else '')}
      <p class="case-narrative">Of the {n} offenders profiled here, {open_n} {"was" if open_n == 1 else "were"} never identified or never taken into custody. The median profile stayed active for {med_span} {"year" if med_span == 1 else "years"} between the first and last known murder, and {long_n} ran for ten years or more before the killings stopped or the offender was caught. Those spans are one reason estimates of "active" killers vary so widely: an offender can be active for years before anyone knows a series exists.</p>
      <h2 class="sub-heading">Related</h2>
      <div class="hub-links"><a href="../lists/never-caught/">Serial killers who were never caught</a><a href="../lists/still-alive/">Serial killers still alive</a><a href="../statistics/">Statistics</a></div>
'''
    desc = B.fit('How many serial killers are active in the US? The FBI, Radford/FGCU and Murder Accountability '
                 'Project estimates, what each one measures, and how long documented offenders stayed active.', 158)
    notes = ['Each national figure is quoted with its source and date; the sources use different definitions of serial murder and of "active".',
             'Years active is the span between the first and last known murder on each profile, inclusive.',
             '"Never caught" means the offender was never identified, or was identified but never taken into custody.']
    return _report(ANSWER_ACTIVE, 'How Many Serial Killers Are Active in the US?',
                   'How Many Serial Killers Are Active in the US?', desc, answer_lead, sections, notes)


def render_answer_state(profiles):
    prefix = '../../'
    counts = by_state_counts()
    ranked = sorted(((s, c) for s, c in counts.items() if c), key=lambda kv: (-kv[1], kv[0]))
    facts = facts_for('state')
    top = ', '.join(f'{s} ({c})' for s, c in ranked[:5])
    rows = [[f'<a href="../{state_slug(s)}/">{e(s)}</a>', str(c),
             str(sum(p['victims']['convicted'] or 0 for p in BY_STATE[s])),
             e(', '.join(p['name'] for p in sorted(BY_STATE[s], key=lambda p: -p['_count'])[:3]))]
            for s, c in ranked]
    lead = ('By raw count, California leads every published tally, whether it counts serial killers or their '
            'victims, followed by Texas, Florida, Illinois and New York, an order that tracks population more than '
            'anything else. Per head of population the picture changes, and Alaska ranks first. The published '
            'figures are quoted below with their sources and dates, followed by this dataset\'s own count.')
    sections = f'''
      <div class="case-narrative-section">
        <h2 class="section-label">What the published rankings say</h2>
        {facts_html(facts) or '<p class="case-narrative">Published state rankings with their sources are added to this page as they are verified.</p>'}
      </div>
      <h2 class="sub-heading">States in this dataset</h2>
      <p class="case-narrative">Profiles so far are concentrated in {top}. The dataset is built in order of public interest, so this ranking will shift as profiles are added, and it counts a profile under every state where it records murders.</p>
      {tile_figure(prefix, 'Profiles by state', 'Darker tiles hold more profiles. Select a state to open its page.')}
      {B.data_table(['State', 'Profiles', 'Murder convictions', 'Profiles'], rows, 'Profiles by state, ranked')}
      <h2 class="sub-heading">Related</h2>
      <div class="hub-links"><a href="../">Serial killers by state</a><a href="../statistics/">Statistics</a><a href="{prefix}states/">Cold cases by state</a></div>
'''
    desc = B.fit('Which state has the most serial killers? California leads every published count, with Texas, '
                 'Florida, Illinois and New York next; per capita the ranking changes. Sources and a state table.', 158)
    notes = ['Published rankings are quoted with their source and date. The Radford/FGCU database counts offenders by the state where they killed; some offenders killed in several states.',
             'This dataset counts a profile under every state in which it records murders.',
             'Raw counts track population; a per-capita view is needed before reading a ranking as a rate.']
    return _report(ANSWER_STATE, 'Which State Has the Most Serial Killers?',
                   'Which State Has the Most Serial Killers?', desc, lead, sections, notes)


# ─────────────────────────── orchestration ───────────────────────────

def write_all(pages, cases, state_links):
    """Write every page of the section. Returns a summary string."""
    profiles = PROFILES
    serial_cases = [c for c in cases if c['type'] == 'Serial Killer Victims' or 'serial killer' in c['_tags']]
    by_state_cases = defaultdict(list)
    for c in serial_cases:
        by_state_cases[c['_region']].append(c)
    all_states = sorted(B.viz.STATE_ABBR)

    pages.write(f'{SECTION}/index.html', render_hub(profiles, serial_cases), True, '0.8')
    live = set(RESERVED) | {'lists'}
    n_index = 0
    for s in all_states:
        slug = state_slug(s)
        render, indexable = render_state(s, BY_STATE.get(s, []), sorted(by_state_cases.get(s, []), key=lambda c: -(c.get('year') or 0)), all_states)
        pages.write(f'{SECTION}/{slug}/index.html', render, indexable, '0.7')
        live.add(slug)
        n_index += indexable
    for p in profiles:
        pages.write(f'{SECTION}/{p["id"]}/index.html', render_profile(p, profiles, state_links), True, '0.7')
        live.add(p['id'])
    lists = list_entries(profiles)
    live_lists = set()
    for slug, title, h1, intro, _k, _s in LISTS:
        render, indexable = render_list(slug, title, h1, intro, lists[slug])
        pages.write(f'{SECTION}/lists/{slug}/index.html', render, indexable, '0.6')
        live_lists.add(slug)
    pages.write(f'{SECTION}/lists/index.html', render_lists_index(lists), True, '0.6')
    pages.write(f'{SECTION}/timeline/index.html', render_timeline(profiles), True, '0.6')
    pages.write(f'{SECTION}/statistics/index.html', render_statistics(profiles), True, '0.6')
    pages.write(f'{SECTION}/{ANSWER_ACTIVE}/index.html', render_answer_active(profiles), True, '0.7')
    pages.write(f'{SECTION}/{ANSWER_STATE}/index.html', render_answer_state(profiles), True, '0.7')

    # stale directories (renamed or removed profiles, old lists) become redirect stubs
    stubs = 0
    sdir = os.path.join(ROOT, SECTION)
    for d in sorted(os.listdir(sdir)):
        if os.path.isdir(os.path.join(sdir, d)) and d not in live:
            with open(os.path.join(sdir, d, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(B.redirect_stub(f'{B.BASE_URL}/{SECTION}/'))
            stubs += 1
    ldir = os.path.join(sdir, 'lists')
    for d in sorted(os.listdir(ldir)):
        if os.path.isdir(os.path.join(ldir, d)) and d not in live_lists:
            with open(os.path.join(ldir, d, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(B.redirect_stub(f'{B.BASE_URL}/{SECTION}/lists/'))
            stubs += 1
    return (f'Serial killers: {len(profiles)} profiles, {len(all_states)} state pages ({n_index} indexable), '
            f'{len(LISTS)} lists, {stubs} redirect stubs')
