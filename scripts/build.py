#!/usr/bin/env python3
"""
ColdCaseIndex site generator.

Reads data/cases.json and data/us-homicide-stats.json and writes:
  cases/{id}/index.html       one page per case
  states/                     directory + one page per US state / country
  types/, decades/            hub pages
  index.html                  generated blocks between <!-- NAME:START/END --> markers
  data/cases-index.json       slim search index used by the homepage
  site.css                    style.css + base.css + components.css
  sitemap.xml                 indexable pages only, real lastmod dates

Run from the project root:  python3 scripts/build.py
Then:                       python3 scripts/check.py
See scripts/BUILD.md.
"""

import datetime
import hashlib
import html
import json
import math
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import viz  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT, 'data', 'cases.json')
STATS_FILE = os.path.join(ROOT, 'data', 'us-homicide-stats.json')
STATE_FILE = os.path.join(ROOT, 'data', 'build-state.json')

BASE_URL = 'https://coldcaseindex.com'
SITE = 'ColdCaseIndex'
OG_IMAGE = f'{BASE_URL}/og-image.png'
CONTACT = 'info@coldcaseindex.com'
ADSENSE_CLIENT = 'ca-pub-5861928596436289'
TODAY = datetime.date.today()
BUILD_YEAR = TODAY.year

e = html.escape

# ── Head scripts. Order is load-bearing: Consent Mode v2 defaults first (denied
# for the EEA/UK/CH region list, granted elsewhere), then AdSense (which carries
# Google's CMP), then gtag. ──
CONSENT = ('<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
           "gtag('consent','default',{'analytics_storage':'denied','ad_storage':'denied',"
           "'ad_user_data':'denied','ad_personalization':'denied','wait_for_update':500,"
           "'region':['BE','BG','CZ','DK','DE','EE','IE','GR','ES','FR','HR','IT','CY','LV','LT','LU',"
           "'HU','MT','NL','AT','PL','PT','RO','SI','SK','FI','SE','GB','CH','IS','LI','NO']});"
           "gtag('consent','default',{'analytics_storage':'granted','ad_storage':'granted',"
           "'ad_user_data':'granted','ad_personalization':'granted'});</script>")
ADSENSE = ('<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
           f'?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>')
GA = ('<script async src="https://www.googletagmanager.com/gtag/js?id=G-9D333CYZNN"></script>'
      '<script>gtag("js",new Date());gtag("config","G-9D333CYZNN");</script>')
AHREFS = ('<script src="https://analytics.ahrefs.com/analytics.js" '
          'data-key="rHBSdf2qb23/3ZsFUBTcuQ" async></script>')
THEME_BOOT = ("<script>try{var _t=localStorage.getItem('cci-theme');"
              "if(_t)document.documentElement.setAttribute('data-theme',_t)}catch(e){}</script>")
HEAD_SCRIPTS = '\n'.join([CONSENT, ADSENSE, GA, AHREFS, THEME_BOOT])

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700'
         '&family=IBM+Plex+Serif:wght@600;700&display=swap" rel="stylesheet">')

LOGO = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect x="3" y="6" width="18" height="22" rx="2" stroke="currentColor" stroke-width="1.5"/>
        <path d="M7 6V4a2 2 0 012-2h10l4 4v0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="7" y1="13" x2="17" y2="13" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
        <line x1="7" y1="17" x2="14" y2="17" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
        <line x1="7" y1="21" x2="12" y2="21" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
        <circle cx="23" cy="20" r="5" stroke="var(--color-primary)" stroke-width="1.8"/>
        <line x1="26.5" y1="23.5" x2="30" y2="27" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round"/>
      </svg>'''

SITE_JS = '''(function(){
  var toggle=document.querySelector('[data-theme-toggle]'),root=document.documentElement;
  var sun='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>';
  var moon='<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  var theme=window.matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light';
  try{theme=localStorage.getItem('cci-theme')||theme}catch(e){}
  function apply(t){root.setAttribute('data-theme',t);if(toggle){toggle.setAttribute('aria-label','Switch to '+(t==='dark'?'light':'dark')+' mode');toggle.innerHTML=t==='dark'?sun:moon}}
  apply(theme);
  if(toggle)toggle.addEventListener('click',function(){theme=theme==='dark'?'light':'dark';try{localStorage.setItem('cci-theme',theme)}catch(e){}apply(theme)});
  var btn=document.getElementById('mobileMenuBtn'),nav=document.getElementById('headerNav');
  if(btn&&nav)btn.addEventListener('click',function(){var open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',open);btn.setAttribute('aria-label',open?'Close menu':'Open menu')});
})();'''

US_STATES = set(viz.STATE_ABBR)

# ── Status model ──
# group key -> (label, badge class, chart class, resolution-scale step)
STATUS_GROUPS = {
    'unsolved':    ('Unsolved', 'badge-unsolved', 'v1', 0),
    'partial':     ('Partly resolved', 'badge-partial', 'v2', 1),
    'proceedings': ('Charges or trial pending', 'badge-arrest', 'v3', 2),
    'resolved':    ('Solved or convicted', 'badge-conviction', 'v4', 3),
    'other':       ('Closed without conviction', 'badge-neutral', 'v5', 3),
}
STATUS_TO_GROUP = {
    'Unsolved': 'unsolved',
    'Partially Solved': 'partial', 'Identified': 'partial',
    'Arrest Made': 'proceedings', 'Pending Trial': 'proceedings', 'Wanted': 'proceedings',
    'Solved': 'resolved', 'Conviction': 'resolved',
    'No Conviction': 'other', 'Ruled Suicide': 'other',
}
STATUS_EXPLAIN = {
    'Unsolved': 'No one has been charged and the case remains open.',
    'Partially Solved': 'Part of the case has been resolved; significant questions remain open.',
    'Identified': 'The victim has been identified. This does not mean anyone has been charged.',
    'Arrest Made': 'A person has been arrested or charged. They are presumed innocent unless convicted.',
    'Pending Trial': 'A defendant is awaiting trial and is presumed innocent unless convicted.',
    'Wanted': 'A named suspect has been charged and is a fugitive.',
    'Solved': 'The case was resolved, for example through a posthumous DNA identification of the perpetrator or the person being found.',
    'Conviction': 'At least one person was convicted in connection with the case.',
    'No Conviction': 'The case was closed or tried without a conviction for the death or disappearance.',
    'Ruled Suicide': 'Authorities ruled the death a suicide. The ruling has been publicly questioned.',
}
OPEN_GROUPS = {'unsolved', 'partial', 'proceedings'}

TYPE_NOUN = {
    'Homicide': 'homicide', 'Multiple Homicide': 'multiple homicide',
    'Serial Killer Victims': 'serial murders', 'Missing Person': 'missing person case',
    'Unidentified Person': 'unidentified person case', 'Suspicious Death': 'suspicious death',
    'Abduction': 'abduction', 'Historic Injustice': 'historic injustice case',
    'Fraud': 'fraud case', 'Fugitive': 'fugitive case', 'Sexual Violence': 'sexual violence case',
    'Mass Shooting': 'mass shooting', 'Sex Trafficking': 'sex trafficking case',
    'Espionage': 'espionage case', 'Arson': 'arson case',
}
TYPE_PLURAL = {
    'Homicide': 'Homicides', 'Multiple Homicide': 'Multiple Homicides',
    'Serial Killer Victims': 'Serial Killer Cases', 'Missing Person': 'Missing Persons',
    'Unidentified Person': 'Unidentified Persons', 'Suspicious Death': 'Suspicious Deaths',
    'Abduction': 'Abductions', 'Historic Injustice': 'Historic Injustice Cases',
    'Fraud': 'Fraud Cases', 'Fugitive': 'Fugitive Cases', 'Sexual Violence': 'Sexual Violence Cases',
    'Mass Shooting': 'Mass Shootings', 'Sex Trafficking': 'Sex Trafficking Cases',
    'Espionage': 'Espionage Cases', 'Arson': 'Arson Cases',
}
TYPE_INTRO = {
    'Homicide': 'Killings of a single victim, from unsolved murders to cases that ended in a conviction decades later.',
    'Multiple Homicide': 'Incidents in which more than one person was killed.',
    'Serial Killer Cases': '',
    'Serial Killer Victims': 'Series of killings attributed to one confirmed or suspected offender.',
    'Missing Person': 'People who disappeared and, in most of these cases, have never been found.',
    'Unidentified Person': 'Recovered remains that were, or still are, without a name. Several have since been identified through forensic genetic genealogy.',
    'Suspicious Death': 'Deaths whose cause or manner is disputed, including some officially ruled accidental or self-inflicted.',
    'Abduction': 'Kidnappings, including cases where the victim was recovered alive.',
    'Historic Injustice': 'Cases where the justice system failed, such as wrongful convictions and killings that went unprosecuted for decades.',
    'Fraud': 'Major fraud and financial crime cases.',
    'Fugitive': 'Cases centred on a named suspect who fled.',
    'Sexual Violence': 'Sexual assault cases and serial offenders.',
    'Mass Shooting': 'Shootings with multiple victims.',
    'Sex Trafficking': 'Trafficking prosecutions and investigations.',
    'Espionage': 'Espionage and wrongful-detention cases.',
    'Arson': 'Fatal or major arson cases.',
}

TIP_LINES = {
    'United States': [
        ('<a href="https://tips.fbi.gov/" target="_blank" rel="noopener noreferrer">FBI Tips (tips.fbi.gov)</a>', 'submit a tip online to the Federal Bureau of Investigation'),
        ('FBI tip line: 1-800-CALL-FBI (1-800-225-5324)', ''),
    ],
    'United Kingdom': [
        ('<a href="https://crimestoppers-uk.org/" target="_blank" rel="noopener noreferrer">Crimestoppers UK</a>', 'anonymous reporting online or on 0800 555 111'),
        ('Police non-emergency number: 101', ''),
    ],
    'Australia': [
        ('<a href="https://www.crimestoppers.com.au/" target="_blank" rel="noopener noreferrer">Crime Stoppers Australia</a>', 'report online or on 1800 333 000'),
    ],
    'Canada': [
        ('<a href="https://www.canadiancrimestoppers.org/" target="_blank" rel="noopener noreferrer">Canadian Crime Stoppers</a>', 'anonymous tips on 1-800-222-8477'),
    ],
}


def slugify(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def known(v):
    return v is not None and str(v).strip() not in ('', 'Unknown', 'N/A')


def plural(n, one, many=None):
    return f'{n} {one if n == 1 else (many or one + "s")}'


def status_group(status):
    return STATUS_TO_GROUP.get(status, 'unsolved')


def badge(status, small=False):
    cls = STATUS_GROUPS[status_group(status)][1]
    style = ' style="font-size:11px;"' if small else ''
    return f'<span class="badge {cls}"{style}>{e(status or "Unsolved")}</span>'


def fit(text, limit):
    """Trim to `limit` chars at a sentence end if possible, else at a word, with an ellipsis."""
    text = ' '.join(str(text).split())
    if len(text) <= limit:
        return text
    cut = text[:limit + 1]
    end = max(cut.rfind('. '), cut.rfind('? '), cut.rfind('! '))
    if end >= limit * 0.55:
        return cut[:end + 1]
    return text[:limit - 1].rsplit(' ', 1)[0].rstrip(',;:—-') + '…'


# ─────────────────────────── data ───────────────────────────

def load_cases():
    with open(DATA_FILE, encoding='utf-8') as f:
        cases = json.load(f)
    for c in cases:
        c['_country'] = c.get('country') or 'United States'
        us = c['_country'] == 'United States'
        c['_us'] = us
        # directory page: US state, or the country for everything else
        c['_region'] = c.get('state') if us else c['_country']
        c['_region_slug'] = slugify(c['_region'])
        c['_group'] = status_group(c.get('status'))
        c['_decade'] = (c['year'] // 10) * 10 if c.get('year') else None
        c['_type_slug'] = slugify(TYPE_PLURAL.get(c['type'], c['type']))
        parts = [c.get('city')]
        if us:
            parts.append(c.get('state'))
        else:
            if c.get('state') and c['state'] != c['_country'] and c['state'] != c.get('city'):
                parts.append(c['state'])
            parts.append(c['_country'])
        c['_place'] = ', '.join(p for p in parts if known(p))
        c['_sources'] = [s for s in c.get('sources', [])
                         if s.get('url') and s.get('title')
                         and urllib.parse.urlparse(s['url']).path.strip('/') != '']
    return cases


def first_published():
    """Date each generated page first appeared in git, so datePublished is stable."""
    try:
        out = subprocess.run(
            ['git', 'log', '--diff-filter=A', '--name-only', '--format=@%as', '--', '*.html'],
            cwd=ROOT, capture_output=True, text=True, check=True).stdout
    except Exception:
        return {}
    dates, cur = {}, None
    for line in out.splitlines():
        if line.startswith('@'):
            cur = line[1:]
        elif line.strip():
            dates[line.strip()] = cur  # log is newest-first, so the oldest add wins
    return dates


class Pages:
    """Collects rendered pages, tracks content hashes so lastmod only moves when
    a page's content actually changes."""

    def __init__(self):
        self.state = {}
        if os.path.exists(STATE_FILE):
            with open(STATE_FILE, encoding='utf-8') as f:
                self.state = json.load(f)
        self.git_dates = first_published()
        self.pages = []  # (path, indexable, priority)
        self.today = TODAY.isoformat()

    def dates(self, path, content_key):
        """Return (published, modified) for a page and record them."""
        h = hashlib.sha1(content_key.encode('utf-8')).hexdigest()[:16]
        st = self.state.get(path, {})
        published = st.get('published') or self.git_dates.get(path) or self.today
        modified = st.get('modified', self.today) if st.get('hash') == h else self.today
        if modified < published:
            modified = published
        self.state[path] = {'hash': h, 'published': published, 'modified': modified}
        return published, modified

    def write(self, path, render, indexable=True, priority='0.6'):
        """`render(published, modified)` returns the HTML. The hash is taken over a
        render with fixed dates so that dates do not feed back into it."""
        probe = render('0000-00-00', '0000-00-00')
        published, modified = self.dates(path, probe)
        full = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'w', encoding='utf-8') as f:
            f.write(render(published, modified))
        self.pages.append((path, indexable, priority, modified))

    def save(self):
        live = {p for p, *_ in self.pages}
        self.state = {k: v for k, v in sorted(self.state.items()) if k in live}
        with open(STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.state, f, indent=0, sort_keys=True)
            f.write('\n')


# ─────────────────────────── page shell ───────────────────────────

NAV = [('#statistics', 'Statistics'), ('states/', 'By State'), ('types/', 'By Type'),
       ('decades/', 'By Decade'), ('about/', 'About')]


def header(prefix, active=None):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if label == active else ''
        links.append(f'<a href="{prefix}{href}"{cur}>{label}</a>')
    return f'''<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="header-inner">
    <a href="{prefix}" class="header-logo" aria-label="ColdCaseIndex home">
      {LOGO}
      <span class="header-logo-text">ColdCaseIndex</span>
    </a>
    <nav class="header-nav" id="headerNav" aria-label="Main navigation">
      {''.join(links)}
    </nav>
    <div class="header-actions">
      <button class="theme-toggle" data-theme-toggle aria-label="Toggle color theme"></button>
      <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="headerNav">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </div>
</header>'''


def footer(prefix):
    return f'''<footer class="site-footer">
  <div class="footer-inner">
    <div>
      <div class="footer-brand">
        {LOGO}
        <span>ColdCaseIndex</span>
      </div>
      <p class="footer-text">A searchable database of documented cold cases and historic crimes, compiled from public records and cited reporting.</p>
    </div>
    <div class="footer-links">
      <div class="footer-link-group">
        <h2 class="footer-heading">Browse</h2>
        <a href="{prefix}#cases">All cases</a>
        <a href="{prefix}states/">By state</a>
        <a href="{prefix}types/">By type</a>
        <a href="{prefix}decades/">By decade</a>
      </div>
      <div class="footer-link-group">
        <h2 class="footer-heading">Site</h2>
        <a href="{prefix}about/">About &amp; methodology</a>
        <a href="{prefix}privacy/">Privacy</a>
        <a href="mailto:{CONTACT}">Report a correction</a>
      </div>
      <div class="footer-link-group">
        <h2 class="footer-heading">Data sources</h2>
        <a href="https://www.murderdata.org/" target="_blank" rel="noopener noreferrer">Murder Accountability Project</a>
        <a href="https://namus.nij.ojp.gov/" target="_blank" rel="noopener noreferrer">NamUs</a>
        <a href="https://charleyproject.org/" target="_blank" rel="noopener noreferrer">The Charley Project</a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; {BUILD_YEAR} ColdCaseIndex. A research resource for public interest.</p>
    <p>Contact: <a href="mailto:{CONTACT}">{CONTACT}</a></p>
  </div>
</footer>

<script>
{SITE_JS}
</script>'''


def page(*, title, desc, canonical, prefix, body, schema, active=None, og_type='website',
         robots=None, extra_head='', published=None, modified=None, extra_js=''):
    ld = '\n'.join(
        '<script type="application/ld+json">\n'
        + json.dumps(s, indent=1, ensure_ascii=False).replace('</', '<\\/')
        + '\n</script>' for s in schema)
    art = ''
    if og_type == 'article' and published:
        art = (f'\n<meta property="article:published_time" content="{published}">'
               f'\n<meta property="article:modified_time" content="{modified}">')
    robots_tag = f'\n<meta name="robots" content="{robots}">' if robots else ''
    js = f'\n<script>\n{extra_js}\n</script>' if extra_js else ''
    canonical_tag = '' if robots == 'noindex' else f'<link rel="canonical" href="{canonical}">'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{HEAD_SCRIPTS}

<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">{robots_tag}
{canonical_tag}

<meta property="og:site_name" content="{SITE}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:alt" content="ColdCaseIndex: cold case and historic crime database">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">{art}
<meta name="twitter:card" content="summary_large_image">

{FONTS}

<meta name="theme-color" content="#0d0d0f">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="manifest" href="/manifest.json">

<link rel="stylesheet" href="{prefix}site.css">{extra_head}
{ld}
</head>
<body>

{header(prefix, active)}

<main id="main">
{body}
</main>

{footer(prefix)}{js}

</body>
</html>
'''


def breadcrumb_ld(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": name, "item": url}
            for i, (name, url) in enumerate(items)],
    }


def breadcrumb_html(items, prefix):
    """items: [(label, site-relative path or None for the current page)]"""
    out = []
    for label, path in items:
        if path is None:
            out.append(f'<span aria-current="page">{e(label)}</span>')
        else:
            out.append(f'<a href="{prefix}{path}">{e(label)}</a>')
    sep = '<span class="case-breadcrumb-sep" aria-hidden="true">›</span>'
    return f'<nav class="case-breadcrumb" aria-label="Breadcrumb">{sep.join(out)}</nav>'


def item_list_ld(cases):
    return {
        "@type": "ItemList",
        "numberOfItems": len(cases),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": c['name'],
             "url": f"{BASE_URL}/cases/{c['id']}/"}
            for i, c in enumerate(cases)],
    }


def case_card(c, prefix, place='city'):
    where = c.get('city') if place == 'city' else c['_region']
    age = f'<span class="case-tag">Age {c["age"]}</span>' if known(c.get('age')) else ''
    return f'''<a href="{prefix}cases/{c['id']}/" class="case-card">
        <div class="case-card-header">
          {badge(c.get('status'))}
          <span class="case-card-year">{c.get('year') or ''}</span>
        </div>
        <h3 class="case-card-name">{e(c['name'])}</h3>
        <p class="case-card-summary">{e(fit(c.get('summary') or '', 230))}</p>
        <div class="case-card-tags">
          <span class="case-tag">{e(where or '')}</span>
          <span class="case-tag">{e(c.get('type') or '')}</span>
          {age}
        </div>
      </a>'''


def status_figure(cases, title):
    counts = Counter(c['_group'] for c in cases)
    groups = [(STATUS_GROUPS[g][0], counts.get(g, 0), STATUS_GROUPS[g][2])
              for g in ('unsolved', 'partial', 'proceedings', 'resolved', 'other')]
    return (f'<figure class="viz"><div class="viz-title">{e(title)}</div>'
            f'{viz.stacked_bar(groups)}</figure>')


def decade_figure(cases, prefix, title, min_cases=4):
    decs = Counter(c['_decade'] for c in cases if c['_decade'])
    if len(cases) < min_cases or len(decs) < 2:
        return ''
    lo, hi = min(decs), max(decs)
    data = [(f'{d}s', decs.get(d, 0)) for d in range(lo, hi + 10, 10)]
    links = {f'{d}s': f'{prefix}decades/{d}s/' for d in decs}
    rows = ''.join(f'<tr><th scope="row"><a href="{prefix}decades/{d}s/">{d}s</a></th><td>{decs[d]}</td></tr>'
                   for d in sorted(decs))
    return f'''<figure class="viz">
        <div class="viz-title">{e(title)}</div>
        <div class="viz-sub">Decade of the incident or disappearance. Select a column to see every case from that decade.</div>
        {viz.columns(data, links=links)}
        <details class="table-view"><summary>Show as table</summary>
          <div class="table-wrap" tabindex="0"><table class="data-table"><thead><tr><th scope="col">Decade</th><th scope="col">Cases</th></tr></thead><tbody>{rows}</tbody></table></div>
        </details>
      </figure>'''


# ─────────────────────────── case pages ───────────────────────────

def case_title(c):
    name, year, status = c['name'], c.get('year'), c.get('status') or 'Unsolved'
    noun = TYPE_NOUN.get(c['type'], 'case')
    lead = {'Unsolved': 'Unsolved', 'Conviction': 'Solved', 'Solved': 'Solved',
            'Identified': 'Identified', 'Partially Solved': 'Partly Solved'}.get(status)
    has_year = bool(year) and str(year) in name
    yr = '' if has_year or not year else f' ({year})'
    options = []
    if lead:
        options.append(f'{name}: {lead} {noun.title()}{yr} | {SITE}')
        options.append(f'{name}: {lead} {noun.title()}{yr}')
    options += [f'{name}{yr} | {SITE}', f'{name}{yr}', f'{name} | {SITE}', name]
    for o in options:
        o = o[0].upper() + o[1:]
        if len(o) <= 60:
            return o
    return fit(name, 60)


def case_desc(c):
    """Answer first: status, what, where, when; then the lead of the summary."""
    status = c.get('status') or 'Unsolved'
    noun = TYPE_NOUN.get(c['type'], 'case')
    where = c['_place']
    head = f'{status}: {noun}'
    if where:
        head += f', {where}'
    if c.get('year'):
        head += f', {c["year"]}'
    head += '. '
    body = fit(c.get('summary') or '', 158 - len(head))
    if len(body) < 40:
        # location too long to leave room for a useful lead: drop it
        head = f'{status} {noun}' + (f', {c["year"]}' if c.get('year') else '') + '. '
        body = fit(c.get('summary') or '', 158 - len(head))
    return head + body


def related_sets(cases):
    """For each case: nearest-in-time cases from the same region, plus similar
    cases elsewhere scored on shared distinctive tags, type and era."""
    by_region = defaultdict(list)
    for c in cases:
        by_region[c['_region']].append(c)
    generic = set()
    for c in cases:
        generic.update({str(c.get('year')), c.get('state', '').lower(), c['_country'].lower(),
                        c['type'].lower(), (c.get('status') or '').lower(), (c.get('city') or '').lower()})
    tag_cases = defaultdict(set)
    for i, c in enumerate(cases):
        for t in c.get('tags', []):
            t = str(t).strip().lower()
            if t and t not in generic and not t.isdigit():
                tag_cases[t].add(i)
    n = len(cases)
    idf = {t: math.log(n / len(s)) for t, s in tag_cases.items() if 2 <= len(s) <= 60}
    out = {}
    for i, c in enumerate(cases):
        year = c.get('year') or 0
        same = sorted((o for o in by_region[c['_region']] if o is not c),
                      key=lambda o: (abs((o.get('year') or 0) - year), o['name']))[:6]
        same_ids = {o['id'] for o in same}
        score = Counter()
        for t in c.get('tags', []):
            t = str(t).strip().lower()
            if t in idf:
                for j in tag_cases[t]:
                    if j != i:
                        score[j] += idf[t]
        for j, o in enumerate(cases):
            if j == i:
                continue
            s = 0.0
            if o['type'] == c['type']:
                s += 1.5
                gap = abs((o.get('year') or 0) - year)
                if gap <= 3:
                    s += 1.5
                elif gap <= 10:
                    s += 0.75
            if s:
                score[j] += s
        ranked = sorted(score.items(), key=lambda kv: (-kv[1], cases[kv[0]]['name']))
        similar = [cases[j] for j, _ in ranked if cases[j]['id'] not in same_ids][:6]
        out[c['id']] = (same, similar)
    return out


def related_cards(items, prefix, show='place'):
    cards = []
    for rc in items:
        meta = rc['_place'] if show == 'place' else (rc.get('city') or '')
        cards.append(f'''<a href="{prefix}cases/{rc['id']}/" class="related-case-card">
            <div class="related-case-header">
              {badge(rc.get('status'), small=True)}
              <span class="case-card-year">{rc.get('year') or ''}</span>
            </div>
            <div class="related-case-name">{e(rc['name'])}</div>
            <div class="related-case-meta">{e(meta)}</div>
          </a>''')
    return f'<div class="related-grid">{"".join(cards)}</div>'


def narrative_html(c):
    if c.get('enriched') and c.get('narrative'):
        body = '\n'.join(f'        <p class="case-narrative">{e(p)}</p>'
                         for p in c['narrative'] if p.strip())
        return f'''<div class="case-narrative-section">
        <h2 class="section-label">Case background and investigation</h2>
{body}
      </div>'''
    # Not yet researched: state only what the record holds, no filler.
    facts = []
    noun = TYPE_NOUN.get(c['type'], 'case')
    facts.append(f"This record documents a {noun} in {c['_place'] or 'an unrecorded location'}"
                 + (f", dated {c['date']}." if known(c.get('date')) else '.'))
    if known(c.get('lastSeen')):
        facts.append(f"Last known information: {c['lastSeen']}.")
    facts.append(STATUS_EXPLAIN.get(c.get('status'), ''))
    facts.append('A fully sourced account of this case has not been compiled yet; the summary '
                 'above reflects the information currently on record.')
    return f'''<div class="case-narrative-section">
        <h2 class="section-label">Case details</h2>
        <p class="case-narrative">{e(' '.join(f for f in facts if f))}</p>
      </div>'''


def case_events(c):
    if c.get('enriched') and c.get('timeline'):
        return [(str(ev.get('date', '')).strip(), str(ev.get('event', '')).strip())
                for ev in c['timeline'] if str(ev.get('event', '')).strip()]
    return []


def sources_html(c):
    items = [f'<li><a href="{e(s["url"])}" target="_blank" rel="noopener noreferrer nofollow">'
             f'{e(s["title"])}</a></li>' for s in c['_sources']]
    if len(items) < 3:
        q = urllib.parse.quote(' '.join(p for p in (c['name'], c.get('city'), c['_region']) if known(p)))
        items.append(f'<li><a href="https://news.google.com/search?q={q}" target="_blank" '
                     f'rel="noopener noreferrer nofollow">Search news coverage of this case</a></li>')
    return f'''<div class="case-sources">
        <h2 class="section-label">Sources</h2>
        <p class="case-sources-note">References used for this entry. ColdCaseIndex is an index of public information. To report an error, email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
        <ul class="case-sources-list">
          {''.join(items)}
        </ul>
      </div>'''


def help_html(c):
    if c['_group'] not in OPEN_GROUPS:
        return f'''<div class="how-to-help">
        <h2 class="how-to-help-heading">About this entry</h2>
        <p class="how-to-help-text">This case is recorded as {e((c.get('status') or '').lower())} and is kept in the index for its historical and investigative significance. {e(STATUS_EXPLAIN.get(c.get('status'), ''))}</p>
        <p class="how-to-help-note">To report an error on this page, email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
      </div>'''
    lines = []
    for label, note in TIP_LINES.get(c['_country'], []):
        lines.append(f'<li>{label}' + (f': {note}' if note else '') + '</li>')
    if c['_us'] and c['type'] in ('Missing Person', 'Unidentified Person'):
        lines.append('<li><a href="https://namus.nij.ojp.gov/" target="_blank" rel="noopener noreferrer">NamUs</a>: the National Missing and Unidentified Persons System</li>')
    if c['_us'] and c['type'] == 'Missing Person' and known(c.get('age')) and c['age'] < 18:
        lines.append('<li>National Center for Missing &amp; Exploited Children: 1-800-THE-LOST (1-800-843-5678)</li>')
    place = c.get('city') if known(c.get('city')) else c['_region']
    lines.append(f'<li>The police force or sheriff\'s office responsible for {e(place)}</li>')
    return f'''<div class="how-to-help">
        <h2 class="how-to-help-heading">Have information about this case?</h2>
        <p class="how-to-help-text">Cold cases are solved when someone comes forward. Even a detail that seems minor can matter. Contact law enforcement through one of these channels:</p>
        <ul class="how-to-help-list">
          {''.join(lines)}
        </ul>
        <p class="how-to-help-note">Tips can usually be given anonymously. ColdCaseIndex does not collect tips. To report an error on this page, email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
      </div>'''


def progress_html(c):
    status = c.get('status') or 'Unsolved'
    step = STATUS_GROUPS[c['_group']][3]
    labels = ['Open', 'Partly resolved', 'Charges or trial', 'Closed']
    lis = []
    for i, lab in enumerate(labels):
        cls = 'current' if i == step else ('done' if i < step else '')
        cur = ' aria-current="step"' if i == step else ''
        inner = f'{lab}<span>{e(status)}</span>' if i == step else lab
        lis.append(f'<li class="{cls}"{cur}>{inner}</li>')
    return f'''<figure class="viz">
          <div class="viz-title">Where the case stands</div>
          <ol class="progress">{''.join(lis)}</ol>
          <p class="viz-sub" style="margin-top:var(--space-3)">{e(STATUS_EXPLAIN.get(status, ''))}</p>
        </figure>'''


def render_case(c, related, state_links, region_counts):
    slug = c['id']
    prefix = '../../'
    canonical = f'{BASE_URL}/cases/{slug}/'
    title, desc = case_title(c), case_desc(c)
    same, similar = related
    region, rslug = c['_region'], c['_region_slug']
    events = case_events(c)

    # details grid
    details = [('Status', badge(c.get('status'), small=True)),
               ('Type', f'<a href="{prefix}types/{c["_type_slug"]}/">{e(c["type"])}</a>'),
               ('Date', e(str(c.get('date') or c.get('year') or 'Unknown')))]
    loc_bits = [e(p) for p in (c.get('city'),) if known(p)]
    loc_bits.append(f'<a href="{prefix}states/{rslug}/">{e(region)}</a>')
    details.append(('Location', ', '.join(loc_bits)))
    multi = c.get('gender') in ('Multiple', 'Mixed') or c['type'] in ('Multiple Homicide', 'Serial Killer Victims', 'Mass Shooting')
    if known(c.get('age')) and not multi:
        details.append(('Age', e(str(c['age']))))
    if known(c.get('gender')):
        details.append(('Victims' if multi else 'Gender',
                        'Multiple' if c['gender'] in ('Multiple', 'Mixed') else e(c['gender'])))
    if c['_decade']:
        details.append(('Decade', f'<a href="{prefix}decades/{c["_decade"]}s/">{c["_decade"]}s</a>'))
    grid = ''.join(f'''<div class="case-detail-item">
          <dt class="case-detail-label">{k}</dt>
          <dd class="case-detail-value">{v}</dd>
        </div>''' for k, v in details)

    # visuals
    strip = viz.timeline_strip(events, c.get('year'), c['_group'] in OPEN_GROUPS, BUILD_YEAR)
    strip_html = ''
    if strip:
        strip_html = f'''<figure class="viz">
          <div class="viz-title">Timeline to scale</div>
          <div class="viz-sub">Each dot is a dated event below; the distance between dots is elapsed time. The darker dot marks the incident.</div>
          {strip}
        </figure>'''
    locator = viz.locator_map(c.get('state'), state_links) if c['_us'] else ''
    locator_html = ''
    if locator:
        n_region = region_counts[region]
        locator_html = f'''<figure class="viz locator">
          <div class="viz-title">{e(region)}</div>
          <div class="viz-sub"><a class="prose-link" href="{prefix}states/{rslug}/">{plural(n_region, 'case')} in {e(region)}</a>. Select any state to browse its cases.</div>
          {locator}
        </figure>'''
    left = progress_html(c) + strip_html
    visuals = (f'<div class="case-visuals"><div>{left}</div>{locator_html}</div>'
               if locator_html else f'<div class="case-visuals" style="grid-template-columns:1fr"><div>{left}</div></div>')

    timeline_html = ''
    if len(events) >= 2:
        items = '\n'.join(f'''<li class="timeline-item">
            <div class="timeline-marker" aria-hidden="true"></div>
            <div>
              <div class="timeline-label">{e(viz.human_date(d) or '—')}</div>
              <div class="timeline-value">{e(ev)}</div>
            </div>
          </li>''' for d, ev in events)
        timeline_html = f'''<div style="margin-top: var(--space-8);">
        <h2 class="section-label">Timeline</h2>
        <ol class="timeline">{items}</ol>
      </div>'''

    last_seen = ''
    if known(c.get('lastSeen')):
        lab = 'Last seen' if c['type'] == 'Missing Person' else 'Last known information'
        last_seen = f'''<div class="modal-last-seen" style="margin-bottom: var(--space-5);">
        <div class="modal-last-seen-label">{lab}</div>
        <div class="modal-last-seen-value">{e(c['lastSeen'])}</div>
      </div>'''

    tags = ''.join(f'<span class="case-tag">{e(str(t))}</span>' for t in c.get('tags', []) if str(t).strip())
    tags_html = (f'<div class="case-tags-section" style="display:flex;gap:var(--space-2);flex-wrap:wrap;'
                 f'margin-top:var(--space-5);">{tags}</div>') if tags else ''

    related_html = ''
    if same:
        related_html += f'''
  <section class="section" style="background: var(--color-surface);">
    <div class="section-inner">
      <h2 class="section-heading">Other cases in {e(region)}</h2>
      {related_cards(same, prefix, show='city')}
      <a href="{prefix}states/{rslug}/" class="all-state-link">All {region_counts[region]} {e(region)} cases &rarr;</a>
    </div>
  </section>'''
    if similar:
        tp = TYPE_PLURAL.get(c['type'], c['type']).lower()
        dec = (f'<a href="{prefix}decades/{c["_decade"]}s/">All cases from the {c["_decade"]}s</a>'
               if c['_decade'] else '')
        related_html += f'''
  <section class="section">
    <div class="section-inner">
      <h2 class="section-heading">Similar cases</h2>
      <p class="section-subtext">Cases of the same type and era, or sharing a distinctive theme with this one.</p>
      {related_cards(similar, prefix)}
      <div class="hub-links">
        <a href="{prefix}types/{c['_type_slug']}/">All {e(tp)}</a>
        {dec}
        <a href="{prefix}states/">Cases by state</a>
      </div>
    </div>
  </section>'''

    crumbs_ld = breadcrumb_ld([('Home', f'{BASE_URL}/'),
                               (f'{region} cases', f'{BASE_URL}/states/{rslug}/'),
                               (c['name'], canonical)])

    def render(published, modified):
        article = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": fit(c['name'], 110),
            "description": desc,
            "url": canonical,
            "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
            "image": OG_IMAGE,
            "inLanguage": "en-US",
            "articleSection": c['type'],
            "datePublished": published,
            "dateModified": modified,
            "author": {"@type": "Organization", "name": SITE, "url": f'{BASE_URL}/about/'},
            "publisher": {"@type": "Organization", "name": SITE, "url": BASE_URL,
                          "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/logos/logo-icon-512x512.png"}},
        }
        addr = {"@type": "PostalAddress", "addressCountry": c['_country']}
        if c['_us'] or c.get('state') != c['_country']:
            addr["addressRegion"] = c.get('state')
        if known(c.get('city')):
            addr["addressLocality"] = c['city']
        article["contentLocation"] = {"@type": "Place", "name": c['_place'], "address": addr}
        if c['_sources']:
            article["citation"] = [{"@type": "CreativeWork", "name": s['title'], "url": s['url']}
                                   for s in c['_sources']]
        mod_h = viz.human_date(modified) if modified != '0000-00-00' else ''
        body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), (f'{region} cases', f'states/{rslug}/'), (c['name'], None)], prefix)}

      <div class="case-page-header">
        <div class="case-page-meta-row">
          {badge(c.get('status'))}
          <span class="case-year-label">{e(str(c.get('date') or c.get('year') or ''))}</span>
          <span class="case-type-label">{e(c['type'])}</span>
        </div>
        <h1 class="case-page-title">{e(c['name'])}</h1>
      </div>

      <p class="case-summary">{e(c.get('summary') or '')}</p>

      <dl id="data-table-zone" class="case-details-grid">
        {grid}
      </dl>

      {visuals}

      {narrative_html(c)}

      {last_seen}
      {tags_html}
      {timeline_html}

      {sources_html(c)}

      {help_html(c)}

      <p class="case-updated">Entry last updated {mod_h}.</p>
    </div>
  </section>
{related_html}
'''
        return page(title=title, desc=desc, canonical=canonical, prefix=prefix, body=body,
                    schema=[article, crumbs_ld], og_type='article',
                    published=published, modified=modified)
    return render


# ─────────────────────────── directory pages ───────────────────────────

def region_stats_html(region, stats):
    row = next((s for s in stats['states'] if s['state'] == region), None)
    if not row:
        return ''
    nat = stats['national']['since1980']
    src = stats['source']
    est = (' Illinois and New York report only partial clearance data, so their figures are estimates.'
           if region in ('Illinois', 'New York') else '')
    return f'''<h2 class="sub-heading">Homicide clearance in {e(region)}, 1965 to 2024</h2>
      <div id="data-table-zone" class="stat-row">
        <div class="stat"><span class="stat-value">{row['homicides']:,}</span><span class="stat-label">Homicides reported</span></div>
        <div class="stat"><span class="stat-value">{row['unsolved']:,}</span><span class="stat-label">Not cleared</span></div>
        <div class="stat"><span class="stat-value">{row['clearancePct']}%</span><span class="stat-label">Clearance rate</span></div>
        <div class="stat"><span class="stat-value">{nat['clearancePct']}%</span><span class="stat-label">US clearance rate, 1980 to 2024</span></div>
      </div>
      <p class="source-note">A homicide is "cleared" when police make an arrest or close it by exceptional means, so an uncleared case is not always an unsolved one. Source: Murder Accountability Project analysis of FBI Uniform Crime Report data, as published by <a href="{src['url']}" target="_blank" rel="noopener noreferrer">Project: Cold Case</a>.{est} These are statewide totals and are separate from the {SITE} entries listed below.</p>'''


def render_region(region, cases, all_regions, stats, state_links):
    slug = slugify(region)
    prefix = '../../'
    url = f'{BASE_URL}/states/{slug}/'
    n = len(cases)
    us = region in US_STATES
    unsolved = sum(1 for c in cases if c['_group'] == 'unsolved')
    years = sorted(c['year'] for c in cases if c.get('year'))
    yr = str(years[0]) if years[0] == years[-1] else f'{years[0]} to {years[-1]}'
    types = Counter(c['type'] for c in cases)
    ordered = sorted(cases, key=lambda c: (-(c.get('year') or 0), c['name']))
    indexable = us or n >= 2

    top_types = ', '.join(f'{v} {TYPE_PLURAL.get(t, t).lower() if v != 1 else TYPE_NOUN.get(t, t).replace(" case", "")}'
                          for t, v in types.most_common(3))
    title = f'{region} Cold Cases: {n} Documented Cases'
    if len(title) > 60 or n == 1:
        title = f'{region} Cold Cases | {SITE}'
    if len(title) > 60:
        title = f'{region} Cold Cases'
    desc = fit(f'{plural(n, "documented case")} in {region}, {yr}: {unsolved} still unsolved. '
               f'Includes {top_types}. Status, timeline and sources for each case.', 158)

    oldest = ordered[-1]
    newest = ordered[0]
    intro = (f'{SITE} documents {plural(n, "case")} in {e(region)}, dated {yr}. '
             f'{unsolved} {"is" if unsolved == 1 else "are"} recorded as unsolved. ')
    if n > 1:
        intro += (f'The earliest is <a href="{prefix}cases/{oldest["id"]}/">{e(oldest["name"])}</a> ({oldest.get("year")}) '
                  f'and the most recent is <a href="{prefix}cases/{newest["id"]}/">{e(newest["name"])}</a> ({newest.get("year")}).')

    type_chips = ''.join(
        f'<a class="breakdown-chip" href="{prefix}types/{slugify(TYPE_PLURAL.get(t, t))}/"><strong>{v}</strong> '
        f'{e(TYPE_PLURAL.get(t, t) if v != 1 else t)}</a>' for t, v in types.most_common())

    cities = Counter(c['city'] for c in cases if known(c.get('city')))
    city_note = ''
    if not us:
        regions_in = Counter(c['state'] for c in cases if c.get('state') and c['state'] != region)
        if regions_in:
            city_note = ('<p class="section-subtext" style="margin-top:var(--space-3)">Regions covered: '
                         + ', '.join(f'{e(r)} ({v})' for r, v in regions_in.most_common()) + '.</p>')

    locator = ''
    if us:
        svg = viz.locator_map(region, state_links)
        locator = f'''<figure class="viz locator">
        <div class="viz-title">{e(region)} on the map</div>
        <div class="viz-sub">Select another state to see its cases.</div>
        {svg}
      </figure>'''

    idx = [r for r, _ in all_regions].index(region)
    prev_r = all_regions[idx - 1][0]
    next_r = all_regions[(idx + 1) % len(all_regions)][0]
    cards = '\n      '.join(case_card(c, prefix) for c in ordered)

    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Cases by state', 'states/'), (region, None)], prefix)}

      <h1 class="section-heading">Cold Cases in {e(region)}</h1>
      <p class="section-subtext">{intro}</p>
      {city_note}

      <div class="case-visuals" style="margin-top:var(--space-8)">
        <div>
          {status_figure(cases, f'Status of the {plural(n, "case")} in this index')}
          {decade_figure(cases, prefix, f'{region} cases by decade')}
        </div>
        {locator}
      </div>

      {region_stats_html(region, stats) if us else ''}

      <h2 class="sub-heading">By type</h2>
      <div class="breakdown-row">{type_chips}</div>

      <h2 class="sub-heading">All {e(region)} cases</h2>
      <div class="cases-grid">
      {cards}
      </div>

      <nav class="state-nav-links" aria-label="More regions">
        <a href="../{slugify(prev_r)}/">&larr; {e(prev_r)}</a>
        <a href="../">All states and countries</a>
        <a href="../{slugify(next_r)}/">{e(next_r)} &rarr;</a>
      </nav>
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Cases by state', f'{BASE_URL}/states/'), (region, url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": f"Cold cases in {region}",
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"},
         "mainEntity": item_list_ld(ordered)},
    ]

    def render(published, modified):
        return page(title=title, desc=desc, canonical=url, prefix=prefix, body=body, schema=schema,
                    active='By State', robots=None if indexable else 'noindex,follow')
    return render, indexable


def render_states_index(by_region, stats, state_links):
    prefix = '../'
    url = f'{BASE_URL}/states/'
    total = sum(len(v) for v in by_region.values())
    us = sorted(r for r in by_region if r in US_STATES)
    intl = sorted(r for r in by_region if r not in US_STATES)
    mx = max(len(v) for v in by_region.values())

    def card(r):
        n = len(by_region[r])
        uns = sum(1 for c in by_region[r] if c['_group'] == 'unsolved')
        return f'''<a href="./{slugify(r)}/" class="state-card" data-state="{e(r.lower())}">
            <div class="state-card-header">
              <span class="state-name">{e(r)}</span>
              <span class="state-count-badge">{n}</span>
            </div>
            <div class="state-bar-wrapper"><div class="state-bar" style="width:{n / mx * 100:.1f}%"></div></div>
            <div class="state-card-meta">{plural(n, 'case')}, {uns} unsolved</div>
          </a>'''

    counts = {viz.STATE_ABBR[r]: len(by_region[r]) for r in us}
    fills = {}
    bins = [5, 10, 20, 40, 10 ** 6]
    for ab, v in counts.items():
        i = next(k for k, b in enumerate(bins) if v <= b)
        fills[ab] = (viz.SEQ_RAMP[i], viz.SEQ_INK[i])
    tips = {ab: f'{viz.ABBR_STATE[ab]}: {plural(v, "case")}' for ab, v in counts.items()}
    W, H, tiles = viz.tile_map(fills=fills, links={ab: f'./{slugify(viz.ABBR_STATE[ab])}/' for ab in counts}, tips=tips)
    legend = ''.join(f'<li><span class="swatch" style="background:{viz.SEQ_RAMP[i]}"></span>{lab}</li>'
                     for i, lab in enumerate(['1 to 5', '6 to 10', '11 to 20', '21 to 40', 'More than 40']))
    desc = (f'Browse {total} documented cold cases by US state and country: {len(us)} states and DC, '
            f'plus {len(intl)} other countries. Counts, status and case lists for each.')
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Cases by state', None)], prefix)}
      <h1 class="section-heading">Cold Cases by State and Country</h1>
      <p class="section-subtext">{total} documented cases across all 50 US states, the District of Columbia and {len(intl)} other countries. Each page lists every case with its status, a breakdown by decade and type, and for US states the statewide homicide clearance figures.</p>

      <figure class="viz" style="margin-top:var(--space-8)">
        <div class="viz-title">Cases in this index, by state</div>
        <div class="viz-sub">Darker tiles hold more documented cases. This reflects what the index covers, not crime rates. Select a state to open its page.</div>
        <svg viewBox="0 0 {W} {H}" role="img" aria-label="Tile map of US states shaded by number of documented cases" xmlns="http://www.w3.org/2000/svg">{tiles}</svg>
        <ul class="viz-legend">{legend}</ul>
      </figure>

      <label class="sr-only" for="stateSearch">Filter states and countries</label>
      <input type="search" class="states-search" id="stateSearch" placeholder="Filter states and countries" autocomplete="off">

      <div id="statesContainer">
        <div class="state-section">
          <h2 class="state-section-heading">United States</h2>
          <div class="states-grid">{''.join(card(r) for r in us)}</div>
        </div>
        <div class="state-section">
          <h2 class="state-section-heading">Other countries</h2>
          <div class="states-grid">{''.join(card(r) for r in intl)}</div>
        </div>
      </div>
      <p id="noStates" role="status" style="display:none;color:var(--color-text-muted);font-size:var(--text-sm)">No states or countries match.</p>
    </div>
  </section>
'''
    js = '''document.getElementById('stateSearch').addEventListener('input',function(){
  var q=this.value.trim().toLowerCase(),visible=0;
  document.querySelectorAll('.state-card').forEach(function(c){var s=c.dataset.state.indexOf(q)>-1;c.style.display=s?'':'none';if(s)visible++});
  document.querySelectorAll('.state-section').forEach(function(sec){var any=[].some.call(sec.querySelectorAll('.state-card'),function(c){return c.style.display!=='none'});sec.style.display=any?'':'none'});
  document.getElementById('noStates').style.display=visible?'none':'block';
});'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Cases by state', url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Cold cases by state and country",
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"}},
    ]
    return lambda p, m: page(title=f'Cold Cases by State and Country | {SITE}', desc=desc, canonical=url,
                             prefix=prefix, body=body, schema=schema, active='By State', extra_js=js)


def render_hub(kind, key, label, cases, siblings, intro, heading):
    """kind: 'types' or 'decades'. siblings: [(slug, label, count)] for cross links."""
    prefix = '../../'
    slug = key
    url = f'{BASE_URL}/{kind}/{slug}/'
    n = len(cases)
    unsolved = sum(1 for c in cases if c['_group'] == 'unsolved')
    ordered = sorted(cases, key=lambda c: (-(c.get('year') or 0), c['name']))
    parent = 'Cases by type' if kind == 'types' else 'Cases by decade'
    regions = Counter(c['_region'] for c in cases)
    top_regions = ', '.join(f'{r} ({v})' for r, v in regions.most_common(3))
    if kind == 'types':
        title = f'{label}: {n} Cold Cases'
        years = sorted(c['year'] for c in cases if c.get('year'))
        desc = fit(f'{plural(n, "documented case")} of this type, {years[0]} to {years[-1]}: {unsolved} unsolved. '
                   f'Most entries: {top_regions}. Status, timeline and sources for each.', 158)
        second = decade_figure(cases, prefix, f'{label} by decade')
        chips_title = 'By state or country'
        chips = ''.join(f'<a class="breakdown-chip" href="{prefix}states/{slugify(r)}/"><strong>{v}</strong> {e(r)}</a>'
                        for r, v in regions.most_common(12))
    else:
        title = f'Cold Cases of the {label}: {n} Cases'
        types = Counter(c['type'] for c in cases)
        top_types = ', '.join(f'{v} {TYPE_PLURAL.get(t, t).lower()}' for t, v in types.most_common(3))
        desc = fit(f'{plural(n, "documented case")} from the {label}: {unsolved} still unsolved. '
                   f'Includes {top_types}. Most entries: {top_regions}.', 158)
        yrs = Counter(c['year'] for c in cases)
        base = int(label[:4])
        data = [(str(y), yrs.get(y, 0)) for y in range(base, base + 10)]
        second = ''
        if n >= 4:
            second = f'''<figure class="viz">
        <div class="viz-title">Cases by year, {label}</div>
        {viz.columns(data, label=f"Cases by year in the {label}")}
      </figure>'''
        chips_title = 'By type'
        chips = ''.join(f'<a class="breakdown-chip" href="{prefix}types/{slugify(TYPE_PLURAL.get(t, t))}/"><strong>{v}</strong> '
                        f'{e(TYPE_PLURAL.get(t, t))}</a>' for t, v in types.most_common())
    if len(title) > 60:
        title = f'{label} | {SITE}' if kind == 'types' else f'{label} Cold Cases'
    sib = ''.join(
        (f'<a href="../{s}/"><strong>{c}</strong> {e(l)}</a>' if s != slug
         else f'<a href="../{s}/" aria-current="page"><strong>{c}</strong> {e(l)}</a>')
        for s, l, c in siblings)
    cards = '\n      '.join(case_card(c, prefix, place='region') for c in ordered)
    indexable = n >= 3
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), (parent, f'{kind}/'), (label, None)], prefix)}
      <h1 class="section-heading">{e(heading)}</h1>
      <p class="section-subtext">{intro}</p>

      {status_figure(cases, f'Status of the {plural(n, "case")}')}
      {second}

      <h2 class="sub-heading">{chips_title}</h2>
      <div class="breakdown-row">{chips}</div>

      <h2 class="sub-heading">All {plural(n, 'case')}</h2>
      <div class="cases-grid">
      {cards}
      </div>

      <h2 class="sub-heading">{'Other case types' if kind == 'types' else 'Other decades'}</h2>
      <div class="hub-links">{sib}</div>
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), (parent, f'{BASE_URL}/{kind}/'), (label, url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": heading,
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"},
         "mainEntity": item_list_ld(ordered)},
    ]
    active = 'By Type' if kind == 'types' else 'By Decade'
    return (lambda p, m: page(title=title, desc=desc, canonical=url, prefix=prefix, body=body,
                              schema=schema, active=active,
                              robots=None if indexable else 'noindex,follow')), indexable


def render_hub_index(kind, entries, total):
    """entries: [(slug, label, count, unsolved, blurb)]"""
    prefix = '../'
    url = f'{BASE_URL}/{kind}/'
    if kind == 'types':
        h1, title = 'Cold Cases by Type', f'Cold Cases by Type | {SITE}'
        desc = (f'{total} documented cases grouped into {len(entries)} types, from homicides and missing '
                f'persons to unidentified remains. Counts and unsolved totals for each.')
        lead = 'Every case in the index is assigned one type. Choose a type to see all of its cases, how many remain unsolved and how they spread across decades.'
        chart = viz.columns([(l.replace(' Cases', '').replace('Persons', 'pers.'), c) for _, l, c, _, _ in entries[:8]],
                            label='Cases by type') if False else ''
    else:
        h1, title = 'Cold Cases by Decade', f'Cold Cases by Decade | {SITE}'
        desc = (f'{total} documented cases from the {entries[0][1]} to the {entries[-1][1]}, grouped by the '
                f'decade of the incident. Counts and unsolved totals for each decade.')
        lead = 'Cases are grouped by the decade in which the crime or disappearance happened, not when it was solved.'
        chart = viz.columns([(l, c) for _, l, c, _, _ in entries],
                            links={l: f'./{s}/' for s, l, _, _, _ in entries}, label='Cases by decade')
    mx = max(c for _, _, c, _, _ in entries)
    cards = ''.join(f'''<a href="./{s}/" class="state-card">
            <div class="state-card-header"><span class="state-name">{e(l)}</span><span class="state-count-badge">{c}</span></div>
            <div class="state-bar-wrapper"><div class="state-bar" style="width:{c / mx * 100:.1f}%"></div></div>
            <div class="state-card-meta">{plural(c, 'case')}, {u} unsolved{('. ' + e(b)) if b else ''}</div>
          </a>''' for s, l, c, u, b in entries)
    fig = ''
    if chart:
        fig = f'''<figure class="viz"><div class="viz-title">Cases in the index by decade</div>
        <div class="viz-sub">Select a column to open that decade.</div>{chart}</figure>'''
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), (h1.replace('Cold Cases', 'Cases'), None)], prefix)}
      <h1 class="section-heading">{h1}</h1>
      <p class="section-subtext">{lead}</p>
      {fig}
      <div class="states-grid" style="margin-top:var(--space-8)">{cards}</div>
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), (h1.replace('Cold Cases', 'Cases'), url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": h1, "description": desc,
         "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"}},
    ]
    active = 'By Type' if kind == 'types' else 'By Decade'
    return lambda p, m: page(title=title, desc=desc, canonical=url, prefix=prefix, body=body,
                             schema=schema, active=active)


def redirect_stub(target_url):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Page moved | {SITE}</title>
<meta name="robots" content="noindex,follow">
<link rel="canonical" href="{target_url}">
<meta http-equiv="refresh" content="0; url={target_url}">
</head>
<body>
<p>This page has moved to <a href="{target_url}">{target_url}</a>.</p>
</body>
</html>
'''


# ─────────────────────────── homepage blocks ───────────────────────────

def home_card(c):
    age = f'<span class="case-tag">Age {e(str(c["age"]))}</span>' if known(c.get('age')) else ''
    return (f'<a href="./cases/{e(c["id"])}/" class="case-card">'
            f'<div class="case-card-header">{badge(c.get("status"))}'
            f'<span class="case-card-year">{e(str(c.get("year") or ""))}</span></div>'
            f'<h3 class="case-card-name">{e(c["name"])}</h3>'
            f'<p class="case-card-summary">{e(fit(c.get("summary") or "", 230))}</p>'
            f'<div class="case-card-tags"><span class="case-tag">{e(c["_region"])}</span>'
            f'<span class="case-tag">{e(c["type"])}</span>{age}</div></a>')


def home_blocks(cases, stats, by_region):
    years = stats['years']
    nat = stats['national']
    src = stats['source']
    latest = years[-1]
    low = min(years, key=lambda y: (y['clearancePct'], y['year']))
    high = max(years, key=lambda y: y['clearancePct'])
    worst = sorted(stats['states'], key=lambda s: (s['clearancePct'], -s['homicides']))[:2]
    src_link = (f'<a href="{src["url"]}" target="_blank" rel="noopener noreferrer">Project: Cold Case</a>')

    data = [(str(y['year']), y['clearancePct']) for y in years]
    idx = {y['year']: i for i, y in enumerate(years)}
    chart = viz.line_chart(data, 40, 80, 10, annotate=[(idx[high['year']], 'above'),
                                                       (idx[low['year']], 'below'),
                                                       (len(years) - 1, 'end')])
    year_rows = ''.join(
        f'<tr><th scope="row">{y["year"]}</th><td>{y["homicides"]:,}</td><td>{y["clearancePct"]}%</td>'
        f'<td>{y["unsolved"]:,}</td></tr>' for y in reversed(years))

    stats_html = f'''<div class="stats-grid">
      <div class="stat-card">
        <div class="stat-card-label">Homicides not cleared</div>
        <div class="stat-card-value">{nat['unsolved']:,}</div>
        <div class="stat-card-meta">United States, 1965 to 2024</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-label">Clearance rate, {latest['year']}</div>
        <div class="stat-card-value">{latest['clearancePct']}%</div>
        <div class="stat-card-meta">Up from {low['clearancePct']}% in {low['year']}</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-label">Not cleared in {latest['year']}</div>
        <div class="stat-card-value">{latest['unsolved']:,}</div>
        <div class="stat-card-meta">Of {latest['homicides']:,} reported homicides</div>
      </div>
      <div class="stat-card">
        <div class="stat-card-label">Lowest long-run clearance</div>
        <div class="stat-card-value">{worst[0]['clearancePct']}%</div>
        <div class="stat-card-meta">{worst[0]['state']} and {worst[1]['state']}, 1965 to 2024</div>
      </div>
    </div>

    <figure class="viz viz-wide" style="max-width:860px;margin-top:var(--space-10)">
      <div class="viz-title">Share of US homicides cleared, {years[0]['year']} to {latest['year']}</div>
      <div class="viz-sub">The clearance rate fell from {high['clearancePct']}% in {high['year']} to {low['clearancePct']}% in {low['year']} and has since recovered to {latest['clearancePct']}%. Hover or tap a year for its value.</div>
      {chart}
      <details class="table-view"><summary>Show as table</summary>
        <div id="data-table-zone" class="table-wrap" tabindex="0"><table class="data-table">
          <thead><tr><th scope="col">Year</th><th scope="col">Homicides</th><th scope="col">Cleared</th><th scope="col">Not cleared</th></tr></thead>
          <tbody>{year_rows}</tbody></table></div>
      </details>
    </figure>
    <p class="source-note">A homicide is "cleared" when police make an arrest or close the case by exceptional means, such as the death of the offender. Source: Murder Accountability Project analysis of FBI Uniform Crime Report data, as published by {src_link} (retrieved {viz.human_date(src['retrieved'])}). Annual figures cover reporting agencies only.</p>'''

    # state map + table
    vals = {viz.STATE_ABBR[s['state']]: s['clearancePct'] for s in stats['states']}
    links = {viz.STATE_ABBR[s['state']]: f'./states/{slugify(s["state"])}/' for s in stats['states']
             if s['state'] in by_region}
    cmap = viz.choropleth(vals, links, lambda v: f'{v}% of homicides cleared',
                          'Tile map of US states shaded by homicide clearance rate, 1965 to 2024',
                          bins=[59, 64, 69, 74, 100])
    legend = viz.ramp_legend(['Under 60%', '60 to 64%', '65 to 69%', '70 to 74%', '75% and over'])
    rows = ''
    for s in sorted(stats['states'], key=lambda s: -s['unsolved']):
        name = s['state']
        cell = (f'<a href="./states/{slugify(name)}/">{e(name)}</a>' if name in by_region else e(name))
        est = '*' if name in ('Illinois', 'New York') else ''
        n_idx = len(by_region.get(name, []))
        rows += (f'<tr><th scope="row" data-v="{e(name)}">{cell}{est}</th>'
                 f'<td data-v="{s["homicides"]}">{s["homicides"]:,}</td>'
                 f'<td data-v="{s["clearancePct"]}">{s["clearancePct"]}%</td>'
                 f'<td data-v="{s["unsolved"]}">{s["unsolved"]:,}</td>'
                 f'<td data-v="{n_idx}">{n_idx}</td></tr>')
    state_html = f'''<figure class="viz" style="max-width:720px">
      <div class="viz-title">Homicide clearance rate by state, 1965 to 2024</div>
      <div class="viz-sub">Darker tiles cleared a smaller share of their homicides. Select a state to see its cases.</div>
      {cmap}
      {legend}
    </figure>

    <div id="data-table-zone" class="table-wrap" tabindex="0" role="region" aria-label="Homicides by state, scrollable table">
      <table class="data-table" id="stateTable">
        <caption>*Illinois and New York report only partial clearance data; their figures are estimates. Source: Murder Accountability Project analysis of FBI data, via {src_link}.</caption>
        <thead><tr>
          <th scope="col" aria-sort="none"><button class="sort-btn" data-col="0" data-type="text">State</button></th>
          <th scope="col" aria-sort="none"><button class="sort-btn" data-col="1">Homicides</button></th>
          <th scope="col" aria-sort="none"><button class="sort-btn" data-col="2">Cleared</button></th>
          <th scope="col" aria-sort="descending"><button class="sort-btn" data-col="3">Not cleared</button></th>
          <th scope="col" aria-sort="none"><button class="sort-btn" data-col="4">Cases in this index</button></th>
        </tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>'''

    # browse chips (static, crawlable)
    decs = Counter(c['_decade'] for c in cases if c['_decade'])
    types = Counter(c['type'] for c in cases)
    dec_chips = ''.join(f'<a class="browse-chip" href="./decades/{d}s/">{d}s<strong>{decs[d]}</strong></a>'
                        for d in sorted(decs))
    type_chips = ''.join(
        f'<a class="browse-chip" href="./types/{slugify(TYPE_PLURAL.get(t, t))}/">{e(TYPE_PLURAL.get(t, t))}<strong>{v}</strong></a>'
        for t, v in types.most_common())
    status_fig = status_figure(cases, f'Status of the {len(cases)} cases in the index')

    unsolved_recent = sorted((c for c in cases if c['_group'] == 'unsolved' and c.get('enriched')),
                             key=lambda c: (-(c.get('year') or 0), c['name']))
    featured = (unsolved_recent[:12] + [c for c in cases if c.get('enriched') and c['_group'] != 'unsolved'][:12])[:24]
    return {
        'HOME_STATS': stats_html,
        'HOME_STATE_DATA': state_html,
        'HOME_DECADES': dec_chips,
        'HOME_TYPES': type_chips,
        'HOME_STATUS': status_fig,
        'HOME_CARDS': '\n'.join(home_card(c) for c in cases[:24]),
        'HOME_RECENT': '\n'.join(home_card(c) for c in list(reversed(cases[-6:]))),
        'HOME_COUNT': f'{len(cases):,}',
        'HOME_UNSOLVED_TOTAL': f'{nat["unsolved"]:,}',
        'HOME_CLEARANCE': f'{latest["clearancePct"]}%',
    }


HOME_JS = r"""
var CASES=[],filtered=[],PAGE=24,shown=0;
var GROUP={'Unsolved':'unsolved','Partially Solved':'partial','Identified':'partial','Arrest Made':'arrest','Pending Trial':'arrest','Wanted':'arrest','Solved':'conviction','Conviction':'conviction','No Conviction':'neutral','Ruled Suicide':'neutral'};
function esc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})}
function card(c){return '<a href="./cases/'+encodeURIComponent(c.id)+'/" class="case-card"><div class="case-card-header"><span class="badge badge-'+(GROUP[c.status]||'unsolved')+'">'+esc(c.status)+'</span><span class="case-card-year">'+esc(c.year||'')+'</span></div><h3 class="case-card-name">'+esc(c.name)+'</h3><p class="case-card-summary">'+esc(c.summary)+'</p><div class="case-card-tags"><span class="case-tag">'+esc(c.state)+'</span><span class="case-tag">'+esc(c.type)+'</span>'+(c.age!=null?'<span class="case-tag">Age '+esc(c.age)+'</span>':'')+'</div></a>'}
var $=function(id){return document.getElementById(id)};
function draw(){
  $('casesGrid').innerHTML=filtered.slice(0,shown).map(card).join('');
  var left=filtered.length-shown,btn=$('loadMore');
  btn.hidden=left<=0;btn.textContent='Load more cases ('+left+' remaining)';
  $('filterCount').textContent=filtered.length+(filtered.length===1?' case':' cases');
  $('noResults').hidden=filtered.length>0;
}
function apply(){
  var t=$('filterType').value,s=$('filterState').value,d=$('filterDecade').value,st=$('filterStatus').value,q=$('filterSearch').value.trim().toLowerCase();
  filtered=CASES.filter(function(c){
    if(t&&c.type!==t)return false;if(s&&c.state!==s)return false;
    if(d&&Math.floor((c.year||0)/10)*10!==+d)return false;if(st&&c.status!==st)return false;
    if(q&&(c.name+' '+c.state+' '+(c.city||'')+' '+c.summary+' '+c.type+' '+(c.year||'')).toLowerCase().indexOf(q)<0)return false;
    return true});
  shown=PAGE;draw();
}
function fill(id,vals,fmt){var el=$(id);vals.forEach(function(v){var o=document.createElement('option');o.value=v;o.textContent=fmt?fmt(v):v;el.appendChild(o)})}
function uniq(a){return a.filter(function(v,i){return v!==''&&v!=null&&a.indexOf(v)===i}).sort()}
function start(){
  fill('filterType',uniq(CASES.map(function(c){return c.type})));
  fill('filterState',uniq(CASES.map(function(c){return c.state})));
  fill('filterDecade',uniq(CASES.map(function(c){return c.year?Math.floor(c.year/10)*10:null})).sort(function(a,b){return a-b}),function(v){return v+'s'});
  fill('filterStatus',uniq(CASES.map(function(c){return c.status})));
  var p=new URLSearchParams(location.search),map={state:'filterState',type:'filterType',decade:'filterDecade',status:'filterStatus',q:'filterSearch'},hit=false;
  Object.keys(map).forEach(function(k){var v=p.get(k);if(!v)return;var el=$(map[k]);if(el.tagName==='SELECT'&&![].some.call(el.options,function(o){return o.value===v}))return;el.value=v;hit=true});
  ['filterType','filterState','filterDecade','filterStatus'].forEach(function(id){$(id).addEventListener('change',apply)});
  $('filterSearch').addEventListener('input',apply);
  $('loadMore').addEventListener('click',function(){shown+=PAGE;draw()});
  $('filtersBar').hidden=false;
  if(hit){apply();$('cases').scrollIntoView()}else{filtered=CASES;shown=PAGE;draw()}
}
var loading=null;
function load(){if(!loading)loading=fetch('./data/cases-index.json').then(function(r){return r.json()}).then(function(d){CASES=d;start()}).catch(function(){});return loading}
if('requestIdleCallback' in window)requestIdleCallback(load,{timeout:2500});else setTimeout(load,1200);
var hero=$('heroSearch'),box=$('searchResults');
hero.addEventListener('focus',load);
hero.addEventListener('input',function(){
  var q=this.value.trim().toLowerCase();
  if(q.length<2){box.classList.remove('active');return}
  var m=CASES.filter(function(c){return (c.name+' '+c.state+' '+c.type+' '+(c.year||'')).toLowerCase().indexOf(q)>-1}).slice(0,8);
  box.innerHTML=m.length?m.map(function(c){return '<a href="./cases/'+encodeURIComponent(c.id)+'/" class="search-result-item"><div class="search-result-info"><div class="search-result-name">'+esc(c.name)+'</div><div class="search-result-meta">'+esc(c.state)+' · '+esc(c.year||'')+' · '+esc(c.type)+'</div></div></a>'}).join(''):'<div class="search-no-results">No cases found</div>';
  box.classList.add('active')});
$('heroForm').addEventListener('submit',function(ev){ev.preventDefault();load().then(function(){$('filterSearch').value=hero.value;box.classList.remove('active');apply();$('cases').scrollIntoView({behavior:'smooth'})})});
document.addEventListener('click',function(ev){if(!ev.target.closest('.hero-search-wrapper'))box.classList.remove('active')});
document.addEventListener('keydown',function(ev){if(ev.key==='Escape')box.classList.remove('active')});
// sortable state table
[].forEach.call(document.querySelectorAll('#stateTable .sort-btn'),function(b){b.addEventListener('click',function(){
  var th=b.parentNode,col=+b.dataset.col,text=b.dataset.type==='text',cur=th.getAttribute('aria-sort');
  var dir=cur==='none'?(text?'ascending':'descending'):(cur==='ascending'?'descending':'ascending');
  [].forEach.call(th.parentNode.children,function(h){h.setAttribute('aria-sort','none')});th.setAttribute('aria-sort',dir);
  var tb=document.querySelector('#stateTable tbody'),rows=[].slice.call(tb.rows);
  rows.sort(function(x,y){var a=x.cells[col].dataset.v,c=y.cells[col].dataset.v,r=text?a.localeCompare(c):a-c;return dir==='ascending'?r:-r});
  rows.forEach(function(r){tb.appendChild(r)})})});
"""


def render_home(cases, stats, by_region):
    b = home_blocks(cases, stats, by_region)
    n = len(cases)
    nat = stats['national']
    latest = stats['years'][-1]
    low = min(stats['years'], key=lambda y: (y['clearancePct'], y['year']))
    countries = len({c['_country'] for c in cases}) - 1
    years = [c['year'] for c in cases if c.get('year')]
    unsolved = sum(1 for c in cases if c['_group'] == 'unsolved')
    url = f'{BASE_URL}/'
    title = f'{SITE}: Cold Case and Unsolved Crime Database'
    desc = (f'{n} documented cold cases and historic crimes with status, timeline and sources: '
            f'{unsolved} unsolved. Search by name, state, type or decade.')
    body = f"""
<section class="hero" id="hero">
  <div class="hero-inner">
    <h1 class="hero-headline"><span class="highlight">{nat['unsolved']:,}</span> US homicides have gone uncleared since 1965.</h1>
    <p class="hero-subtext">In {latest['year']}, police cleared {latest['clearancePct']}% of reported homicides, up from a low of {low['clearancePct']}% in {low['year']}. {SITE} documents {n} individual cases, {unsolved} of them still unsolved, each with its status, a dated timeline and the sources behind it.</p>
    <div class="hero-search-wrapper">
      <form class="hero-search" id="heroForm" role="search">
        <label class="sr-only" for="heroSearch">Search cases</label>
        <input type="search" id="heroSearch" placeholder="Search cases by name, state or keyword" autocomplete="off">
        <button type="submit">Search</button>
      </form>
      <div class="search-results" id="searchResults" aria-live="polite"></div>
    </div>
    <div class="hero-stats">
      <div class="hero-stat"><span class="hero-stat-value" id="heroStatCases">{n}</span><span class="hero-stat-label">Documented cases</span></div>
      <div class="hero-stat"><span class="hero-stat-value">{unsolved}</span><span class="hero-stat-label">Still unsolved</span></div>
      <div class="hero-stat"><span class="hero-stat-value">50 states + DC</span><span class="hero-stat-label">and {countries} other countries</span></div>
      <div class="hero-stat"><span class="hero-stat-value">{min(years)} to {max(years)}</span><span class="hero-stat-label">Years covered</span></div>
    </div>
  </div>
</section>

<section class="section" id="statistics">
  <div class="section-inner">
    <div class="section-label">National statistics</div>
    <h2 class="section-heading">How Many US Homicides Go Unsolved</h2>
    <p class="section-subtext" style="margin-bottom: var(--space-8);">Figures for the United States as a whole, from FBI data analysed by the Murder Accountability Project. They describe all reported homicides, not only the cases documented on this site.</p>
    {b['HOME_STATS']}
  </div>
</section>

<section class="section" id="cases" style="background: var(--color-surface);">
  <div class="section-inner">
    <div class="section-label">Case database</div>
    <h2 class="section-heading">Browse Cases</h2>
    <p class="section-subtext" style="margin-bottom: var(--space-6);">Filter the {n} documented cases by type, state or country, decade and status, or browse by <a href="./states/">state</a>, <a href="./types/">type</a> or <a href="./decades/">decade</a>.</p>

    <div class="filters-bar" id="filtersBar" hidden>
      <div class="filter-group"><label for="filterType">Type</label><select class="filter-select" id="filterType"><option value="">All types</option></select></div>
      <div class="filter-group"><label for="filterState">State or country</label><select class="filter-select" id="filterState"><option value="">All</option></select></div>
      <div class="filter-group"><label for="filterDecade">Decade</label><select class="filter-select" id="filterDecade"><option value="">All decades</option></select></div>
      <div class="filter-group"><label for="filterStatus">Status</label><select class="filter-select" id="filterStatus"><option value="">All statuses</option></select></div>
      <div class="filter-group" style="flex: 1; min-width: 180px;"><label for="filterSearch">Search</label><input class="filter-search" type="search" id="filterSearch" placeholder="Name, place or keyword"></div>
      <span class="filter-count" id="filterCount" role="status"></span>
    </div>

    <div class="cases-grid" id="casesGrid">
{b['HOME_CARDS']}
    </div>
    <div class="no-results" id="noResults" hidden>
      <h3>No cases found</h3>
      <p style="font-size: var(--text-sm);">Try adjusting your filters or search terms.</p>
    </div>
    <div style="text-align:center;margin-top:var(--space-8)"><button class="load-more" id="loadMore" hidden>Load more cases</button></div>
  </div>
</section>

<section class="section" id="browse">
  <div class="section-inner">
    <div class="section-label">Browse</div>
    <h2 class="section-heading">Explore the Database</h2>
    {b['HOME_STATUS']}

    <h3 class="browse-subheading">By decade</h3>
    <div class="browse-chips">{b['HOME_DECADES']}</div>

    <h3 class="browse-subheading">By type</h3>
    <div class="browse-chips">{b['HOME_TYPES']}</div>

    <h3 class="browse-subheading">Recently added</h3>
    <div class="cases-grid">
{b['HOME_RECENT']}
    </div>
  </div>
</section>

<section class="section" id="states" style="background: var(--color-surface);">
  <div class="section-inner">
    <div class="section-label">State by state</div>
    <h2 class="section-heading">Homicide Clearance by State</h2>
    <p class="section-subtext" style="margin-bottom: var(--space-8);">Reported homicides, the share cleared and the number left uncleared in each state and the District of Columbia, 1965 to 2024. Select a column heading to sort.</p>
    {b['HOME_STATE_DATA']}
  </div>
</section>

<section class="section" id="about">
  <div class="section-inner">
    <div class="section-label">About</div>
    <h2 class="section-heading">About ColdCaseIndex</h2>
    <div class="about-content">
      <p>{SITE} is a structured index of cold cases and historically significant crimes. Most entries are unsolved. Others were solved, sometimes decades later, and are kept because the investigation, the forensic method or the outcome matters to understanding how cases are resolved.</p>
      <p>Each entry is compiled from public sources: law enforcement releases, court records, NamUs, the Charley Project, the DNA Doe Project and established news reporting. Sources are listed on every case page. People who have not been convicted are presumed innocent and are described that way.</p>
      <p>This is a research resource, not a tip line. If you have information about a case, contact the responsible police force or the FBI on 1-800-CALL-FBI. To report an error, email <a href="mailto:{CONTACT}">{CONTACT}</a>. Read more <a href="./about/">about the index and its methodology</a>.</p>
    </div>
  </div>
</section>
"""
    schema = [
        {"@context": "https://schema.org", "@type": "WebSite", "@id": f"{BASE_URL}/#website",
         "name": SITE, "alternateName": "Cold Case Index", "url": url, "inLanguage": "en-US",
         "description": desc, "publisher": {"@id": f"{BASE_URL}/#organization"}},
        {"@context": "https://schema.org", "@type": "Organization", "@id": f"{BASE_URL}/#organization",
         "name": SITE, "url": url,
         "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/logos/logo-icon-512x512.png"},
         "contactPoint": {"@type": "ContactPoint", "email": CONTACT, "contactType": "corrections"}},
        {"@context": "https://schema.org", "@type": "Dataset", "name": f"{SITE} case database",
         "description": (f"{n} documented cold cases and historic crimes with type, status, date, location, "
                         "summary, timeline and sources."),
         "url": url, "creator": {"@id": f"{BASE_URL}/#organization"},
         "temporalCoverage": f"{min(years)}/{max(years)}",
         "keywords": ["cold cases", "unsolved homicides", "missing persons", "unidentified persons"],
         "distribution": [{"@type": "DataDownload", "encodingFormat": "application/json",
                           "contentUrl": f"{BASE_URL}/data/cases.json"}]},
    ]
    extra = ('\n<link rel="stylesheet" href="./home.css">\n'
             '<meta name="google-site-verification" content="PnQaWQNHws_WTbo90jGB6meg8bYUQTFNwPb3DeO4XjM">')
    return lambda p, m: page(title=title, desc=desc, canonical=url, prefix='./', body=body,
                             schema=schema, extra_head=extra, extra_js=HOME_JS)


def render_static(cases, stats):
    """About, privacy and 404 are written from body fragments in scripts/content/."""
    def content(name):
        with open(os.path.join(ROOT, 'scripts', 'content', name), encoding='utf-8') as f:
            return f.read()
    years = [c['year'] for c in cases if c.get('year')]
    regions = len({c['_region'] for c in cases})
    fill = {
        '{{CASES}}': str(len(cases)),
        '{{UNSOLVED}}': str(sum(1 for c in cases if c['_group'] == 'unsolved')),
        '{{REGIONS}}': str(regions),
        '{{YEARS}}': f'{min(years)} to {max(years)}',
        '{{US_UNSOLVED}}': f"{stats['national']['unsolved']:,}",
    }
    out = {}
    about = content('about.html').replace(
        '{{BREADCRUMB}}', breadcrumb_html([('Home', ''), ('About', None)], '../'))
    for k, v in fill.items():
        about = about.replace(k, v)
    about_url = f'{BASE_URL}/about/'
    about_schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('About', about_url)]),
        {"@context": "https://schema.org", "@type": "AboutPage", "name": f"About {SITE}",
         "url": about_url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"}},
    ]
    out['about/index.html'] = (lambda p, m: page(
        title=f'About {SITE}: Sources and Methodology',
        desc=(f'How {SITE} compiles its {len(cases)} case entries: the sources used, what each '
              'status means, how unconvicted people are described, and how to report an error.'),
        canonical=about_url, prefix='../', body=about, schema=about_schema, active='About'), True)

    privacy = content('privacy.html').replace(
        '{{BREADCRUMB}}', breadcrumb_html([('Home', ''), ('Privacy', None)], '../'))
    out['privacy/index.html'] = (lambda p, m: page(
        title=f'Privacy Policy | {SITE}',
        desc=(f'What {SITE} collects: no accounts or forms; Google Analytics and AdSense cookies with '
              'consent controls; how to contact us about case information.'),
        canonical=f'{BASE_URL}/privacy/', prefix='../', body=privacy, schema=[],
        robots='noindex,follow'), False)

    nf = f'<div class="notfound-wrap" style="min-height:60vh">{content("404.html")}</div>'
    out['404.html'] = (lambda p, m: page(
        title=f'Page Not Found | {SITE}', desc='The page you were looking for could not be found.',
        canonical=f'{BASE_URL}/', prefix='/', body=nf, schema=[], robots='noindex'), False)
    return out



# ─────────────────────────── outputs ───────────────────────────

def write_css():
    out = []
    for name in ('style.css', 'base.css', 'components.css'):
        with open(os.path.join(ROOT, name), encoding='utf-8') as f:
            out.append(f.read())
    css = '\n'.join(out)
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    css = re.sub(r'\n\s*\n+', '\n', css)
    css = re.sub(r'^[ \t]+', '', css, flags=re.M)
    with open(os.path.join(ROOT, 'site.css'), 'w', encoding='utf-8') as f:
        f.write('/* Generated by scripts/build.py from style.css, base.css and components.css */\n' + css)


def write_search_index(cases):
    rows = [{'id': c['id'], 'name': c['name'], 'type': c['type'], 'status': c.get('status'),
             'year': c.get('year'), 'state': c['_region'], 'city': c.get('city'),
             'age': c.get('age'), 'summary': fit(c.get('summary') or '', 230)} for c in cases]
    with open(os.path.join(ROOT, 'data', 'cases-index.json'), 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, separators=(',', ':'))
    return rows


def write_sitemap(pages, static):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    rows = list(static)
    for path, indexable, _prio, modified in pages.pages:
        if indexable:
            rows.append((f'{BASE_URL}/' + re.sub(r'index\.html$', '', path), modified))
    rows.sort(key=lambda r: (r[0].count('/'), r[0]))
    for loc, mod in rows:
        lines += ['  <url>', f'    <loc>{loc}</loc>', f'    <lastmod>{mod}</lastmod>', '  </url>']
    lines.append('</urlset>')
    with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    return len(rows)


def update_counts(n):
    subs = {
        'manifest.json': [(r'("description": "Database of )[\d,]+', rf'\g<1>{n}')],
        'llms.txt': [(r'(database of )[\d,]+( documented)', rf'\g<1>{n}\g<2>')],
    }
    for path, pairs in subs.items():
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            continue
        with open(full, encoding='utf-8') as f:
            s = f.read()
        for pat, rep in pairs:
            s = re.sub(pat, rep, s)
        with open(full, 'w', encoding='utf-8') as f:
            f.write(s)


def main():
    cases = load_cases()
    with open(STATS_FILE, encoding='utf-8') as f:
        stats = json.load(f)
    pages = Pages()
    print(f'Loaded {len(cases)} cases')

    by_region = defaultdict(list)
    for c in cases:
        by_region[c['_region']].append(c)
    region_counts = {r: len(v) for r, v in by_region.items()}
    all_regions = sorted(((r, len(v)) for r, v in by_region.items()), key=lambda rv: rv[0])
    state_links = {viz.STATE_ABBR[r]: f'../../states/{slugify(r)}/' for r in by_region if r in US_STATES}

    write_css()

    # case pages
    related = related_sets(cases)
    live_cases = set()
    for c in cases:
        path = f'cases/{c["id"]}/index.html'
        pages.write(path, render_case(c, related[c['id']], state_links, region_counts), True, '0.7')
        live_cases.add(c['id'])
    # merged duplicates redirect to the surviving record; anything else not in the data is removed
    red_file = os.path.join(ROOT, 'data', 'redirects.json')
    redirects = {}
    if os.path.exists(red_file):
        with open(red_file, encoding='utf-8') as f:
            redirects = json.load(f)
    cdir = os.path.join(ROOT, 'cases')
    stubs = removed = 0
    for d in sorted(os.listdir(cdir)):
        full = os.path.join(cdir, d)
        if not os.path.isdir(full) or d in live_cases:
            continue
        target = redirects.get(d)
        if target and target.startswith('/'):
            # removed from the index: send visitors to a browse page
            with open(os.path.join(full, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(redirect_stub(f'{BASE_URL}{target}'))
            stubs += 1
            continue
        hops = 0
        while target and target not in live_cases and hops < 5:
            target, hops = redirects.get(target), hops + 1
        if target in live_cases:
            with open(os.path.join(full, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(redirect_stub(f'{BASE_URL}/cases/{target}/'))
            stubs += 1
        else:
            shutil.rmtree(full)
            removed += 1
    print(f'Wrote {len(cases)} case pages, {stubs} redirect stubs, removed {removed}')

    # region pages
    live_regions = set()
    for region, _ in all_regions:
        render, indexable = render_region(region, by_region[region], all_regions, stats, state_links)
        pages.write(f'states/{slugify(region)}/index.html', render, indexable)
        live_regions.add(slugify(region))
    pages.write('states/index.html', render_states_index(by_region, stats, state_links), True)
    # region pages that no longer exist become redirect stubs to their new home
    moved = {slugify(c['state']): c['_region_slug'] for c in cases
             if c.get('state') and slugify(c['state']) not in live_regions}
    moved['new-hampshire-vermont'] = 'new-hampshire'
    sdir = os.path.join(ROOT, 'states')
    stubs = 0
    for d in sorted(os.listdir(sdir)):
        if os.path.isdir(os.path.join(sdir, d)) and d not in live_regions:
            target = moved.get(d)
            url = f'{BASE_URL}/states/{target}/' if target else f'{BASE_URL}/states/'
            with open(os.path.join(sdir, d, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(redirect_stub(url))
            stubs += 1
    print(f'Wrote {len(all_regions)} region pages, {stubs} redirect stubs')

    # type hubs
    by_type = defaultdict(list)
    for c in cases:
        by_type[c['type']].append(c)
    t_entries = sorted(((slugify(TYPE_PLURAL.get(t, t)), TYPE_PLURAL.get(t, t), len(v),
                         sum(1 for c in v if c['_group'] == 'unsolved'), '') for t, v in by_type.items()),
                       key=lambda x: -x[2])
    sib_t = [(s, l, n) for s, l, n, _, _ in t_entries]
    for t, v in by_type.items():
        label = TYPE_PLURAL.get(t, t)
        intro = (f'{TYPE_INTRO.get(t, "")} {SITE} documents {plural(len(v), "case")} of this type, of which '
                 f'{sum(1 for c in v if c["_group"] == "unsolved")} are recorded as unsolved.').strip()
        render, indexable = render_hub('types', slugify(label), label, v, sib_t, e(intro), label)
        pages.write(f'types/{slugify(label)}/index.html', render, indexable)
    pages.write('types/index.html', render_hub_index('types', t_entries, len(cases)), True)

    # decade hubs
    by_dec = defaultdict(list)
    for c in cases:
        if c['_decade']:
            by_dec[c['_decade']].append(c)
    d_entries = [(f'{d}s', f'{d}s', len(by_dec[d]),
                  sum(1 for c in by_dec[d] if c['_group'] == 'unsolved'), '') for d in sorted(by_dec)]
    sib_d = [(s, l, n) for s, l, n, _, _ in d_entries]
    for d, v in by_dec.items():
        label = f'{d}s'
        uns = sum(1 for c in v if c['_group'] == 'unsolved')
        intro = (f'{plural(len(v), "documented case")} in which the crime or disappearance took place between '
                 f'{d} and {d + 9}. {uns} {"is" if uns == 1 else "are"} recorded as unsolved.')
        render, indexable = render_hub('decades', label, label, v, sib_d, e(intro), f'Cold Cases of the {label}')
        pages.write(f'decades/{label}/index.html', render, indexable)
    pages.write('decades/index.html', render_hub_index('decades', d_entries, len(cases)), True)
    print(f'Wrote {len(by_type)} type hubs and {len(by_dec)} decade hubs')

    # homepage + data
    write_search_index(cases)
    pages.write('index.html', render_home(cases, stats, by_region), True)
    update_counts(len(cases))

    for path, (render, indexable) in render_static(cases, stats).items():
        pages.write(path, render, indexable)
    n = write_sitemap(pages, [])
    pages.save()
    print(f'Sitemap: {n} URLs')


if __name__ == '__main__':
    main()
