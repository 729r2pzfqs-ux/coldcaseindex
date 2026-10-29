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
import changelog  # noqa: E402
import geo  # noqa: E402
import analysis  # noqa: E402
import serial_killers  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT, 'data', 'cases.json')
STATS_FILE = os.path.join(ROOT, 'data', 'us-homicide-stats.json')
STATE_FILE = os.path.join(ROOT, 'data', 'build-state.json')

BASE_URL = 'https://coldcaseindex.com'
SITE = 'ColdCaseIndex'
OG_IMAGE = f'{BASE_URL}/og-image.png'
CONTACT = 'info@coldcaseindex.com'
TODAY = datetime.date.today()
BUILD_YEAR = TODAY.year

e = html.escape

# ── Head scripts. Mediavine first (it carries its own consent management for the
# EEA/UK and US state laws), then GA4, then Ahrefs. Mediavine requires exclusivity for
# display, video and native ads: no other ad network code may be added here. ──
MEDIAVINE = ('<script type="text/javascript" async="async" data-noptimize="1" data-cfasync="false" '
             'src="//scripts.scriptwrapper.com/tags/07246c68-4098-4276-b4dd-3605803c5564.js"></script>')
# Mediavine ad settings, read by the script wrapper from the first element in <body>:
# blocks the recipe unit, the auto-inserted sticky unit and interstitials.
MEDIAVINE_CONFIG = ('<div id="ad-management-config-settings" data-blocklist-recipe="1" '
                    'data-blocklist-auto-insert-sticky="1" data-blocklist-interstitial-mobile="1" '
                    'data-blocklist-interstitial-desktop="1" ></div>')
GA = ('<script async src="https://www.googletagmanager.com/gtag/js?id=G-9D333CYZNN"></script>'
      '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
      'gtag("js",new Date());gtag("config","G-9D333CYZNN");</script>')
AHREFS = ('<script src="https://analytics.ahrefs.com/analytics.js" '
          'data-key="rHBSdf2qb23/3ZsFUBTcuQ" async></script>')
THEME_BOOT = ("<script>try{var _t=localStorage.getItem('cci-theme');"
              "if(_t)document.documentElement.setAttribute('data-theme',_t)}catch(e){}</script>")
HEAD_SCRIPTS = '\n'.join([MEDIAVINE, GA, AHREFS, THEME_BOOT])

# Fonts are self-hosted in /fonts/ (declared in style.css). Preload the body face so text
# does not wait on the stylesheet; the display face is only needed below the fold.
FONTS = ('<link rel="preload" href="/fonts/IBMPlexSans-latin.woff2" as="font" type="font/woff2" crossorigin>')

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
  // header search: same index and matching as the homepage search
  var sf=document.getElementById('siteSearchForm'),si=document.getElementById('siteSearch'),sr=document.getElementById('siteSearchResults');
  if(sf&&si&&sr){
    var base=sf.getAttribute('data-root')||'./',idx=null,data=[],act=-1;
    var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
    var loadIdx=function(){if(!idx)idx=Promise.all([fetch(base+'data/cases-index.json').then(function(r){return r.json()}),fetch(base+'data/serial-killers-index.json').then(function(r){return r.json()}).catch(function(){return []})]).then(function(d){data=d[0].concat(d[1])}).catch(function(){});return idx};
    var close=function(){sr.classList.remove('active');si.setAttribute('aria-expanded','false');si.removeAttribute('aria-activedescendant');act=-1};
    var render=function(){var q=si.value.trim().toLowerCase();if(q.length<2){close();return}
      var m=data.filter(function(c){return (c.name+' '+c.state+' '+c.type+' '+(c.year||'')).toLowerCase().indexOf(q)>-1}).slice(0,8);
      sr.innerHTML=m.length?m.map(function(c,i){return '<a href="'+base+(c.url||'cases/'+encodeURIComponent(c.id)+'/')+'" class="search-result-item" role="option" id="siteSearchOpt'+i+'" aria-selected="false"><div class="search-result-info"><div class="search-result-name">'+esc(c.name)+'</div><div class="search-result-meta">'+esc(c.state)+' · '+esc(c.year||'')+' · '+esc(c.type)+'</div></div></a>'}).join(''):'<div class="search-no-results">No cases found</div>';
      act=-1;sr.classList.add('active');si.setAttribute('aria-expanded','true')};
    si.addEventListener('focus',loadIdx);
    si.addEventListener('input',function(){loadIdx().then(render)});
    si.addEventListener('keydown',function(ev){var opts=sr.querySelectorAll('[role="option"]');
      if(ev.key==='ArrowDown'||ev.key==='ArrowUp'){if(!opts.length)return;ev.preventDefault();act=ev.key==='ArrowDown'?(act+1)%opts.length:(act-1+opts.length)%opts.length;
        [].forEach.call(opts,function(o,i){o.setAttribute('aria-selected',i===act?'true':'false')});si.setAttribute('aria-activedescendant',opts[act].id);opts[act].scrollIntoView({block:'nearest'})}
      else if(ev.key==='Enter'&&act>-1&&opts[act]){ev.preventDefault();location.href=opts[act].href}
      else if(ev.key==='Escape')close()});
    document.addEventListener('click',function(ev){if(!sf.contains(ev.target))close()});
  }
  // "Copy" buttons in the citation box
  [].forEach.call(document.querySelectorAll('[data-copy]'),function(b){b.addEventListener('click',function(){
    var t=document.getElementById(b.getAttribute('data-copy'));if(!t||!navigator.clipboard)return;
    navigator.clipboard.writeText(t.textContent).then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1500)})})});
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

# Tag synonyms, merged at load time. Keys and values are lower case.
TAG_ALIASES = {
    'children': 'child', 'child victim': 'child', 'child victims': 'child', 'missing child': 'child',
    'teen': 'teenager', 'teens': 'teenager', 'teenagers': 'teenager',
    'college students': 'college student',
    'forensic genealogy': 'genetic genealogy', 'dna genealogy': 'genetic genealogy',
    'missing persons': 'missing person',
    'no body': 'body never found', 'no bodies found': 'body never found',
    'no remains found': 'body never found', 'no-body homicide': 'body never found',
    'dna': 'dna evidence',
    'fbi': 'fbi case', 'fbi investigation': 'fbi case',
    'domestic': 'domestic violence',
    'serial murder': 'serial killer',
    'confessions': 'confession',
    'reward offered': 'reward',
    'overturned conviction': 'conviction overturned', 'conviction vacated': 'conviction overturned',
    'vacated conviction': 'conviction overturned',
    'murder-for-hire': 'murder for hire',
    'surveillance video': 'surveillance footage',
    'historic': 'historical',
    'axe murders': 'axe murder',
    'milk carton kids': 'milk carton', 'milk cartons': 'milk carton',
    'btk killer': 'btk',
    'undetermined manner': 'undetermined', 'undetermined death': 'undetermined',
    'undetermined cause': 'undetermined',
    'suspected foul play': 'foul play suspected',
    'unidentified victim': 'unidentified victims',
}
DECADE_TAG = re.compile(r'^(\d{4}s(-\d{4}s)?( cold case)?|19th century)$')


def normalize_tags(c):
    """Merge synonyms, drop decade tags (the decade hubs cover them) and tags that only
    repeat the case's own city, state, country, type, status or year. Order is kept."""
    own = {str(c.get(k) or '').strip().lower() for k in ('city', 'state', 'country', 'type', 'status', 'year')}
    if c.get('state') == 'District of Columbia':
        own |= {'washington dc', 'washington d.c.'}
    if 'Homicide' in str(c.get('type') or ''):
        own.add('homicide')
    out, seen = [], set()
    for t in c.get('tags') or []:
        t = ' '.join(str(t).split())
        low = t.lower()
        if low in TAG_ALIASES:
            t = low = TAG_ALIASES[low]
        if not low or low in own or low in seen or DECADE_TAG.match(low):
            continue
        seen.add(low)
        out.append(t)
    return out


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
        c['tags'] = normalize_tags(c)
        c['_tags'] = {t.lower() for t in c['tags']}
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
       ('serial-killers/', 'Serial Killers'), ('decades/', 'By Decade'), ('map/', 'Map'), ('analysis/', 'Analysis'), ('about/', 'About')]


def header_search(prefix):
    """Site search for every page except the homepage, which has the hero search.
    Submitting without JS lands on the homepage with ?q=, which its filter JS honours."""
    return f'''<form class="header-search" id="siteSearchForm" role="search" data-mediavine-no-ads action="{prefix}" method="get" data-root="{prefix}">
        <label class="sr-only" for="siteSearch">Search cases</label>
        <input type="search" id="siteSearch" name="q" placeholder="Search cases" autocomplete="off" role="combobox" aria-expanded="false" aria-controls="siteSearchResults" aria-autocomplete="list">
        <div class="search-results" id="siteSearchResults" role="listbox" aria-label="Matching cases"></div>
      </form>'''


def header(prefix, active=None):
    links = []
    for href, label in NAV:
        cur = ' aria-current="page"' if label == active else ''
        links.append(f'<a href="{prefix}{href}"{cur}>{label}</a>')
    search = '' if prefix == './' else header_search(prefix)
    return f'''<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="header-inner">
    <a href="{prefix}" class="header-logo" aria-label="ColdCaseIndex home">
      {LOGO}
      <span class="header-logo-text">ColdCaseIndex</span>
    </a>
    <nav class="header-nav" id="headerNav" aria-label="Main navigation">
      {''.join(links)}
      {search}
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
        <a href="{prefix}themes/">By theme</a>
        <a href="{prefix}cities/">By city</a>
        <a href="{prefix}serial-killers/">Serial killers</a>
        <a href="{prefix}map/">Case map</a>
        <a href="{prefix}analysis/">Analysis</a>
        <a href="{prefix}updates/">Recent updates</a>
        <a href="{prefix}watch/">Cases to watch</a>
        <a href="{prefix}today/">On this day</a>
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
<link rel="alternate" type="application/atom+xml" title="{SITE} updates" href="/feed.xml">

<link rel="stylesheet" href="{prefix}site.css">{extra_head}
{ld}
</head>
<body>
{MEDIAVINE_CONFIG}

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
    return (f'<figure class="viz" data-mediavine-no-ads><div class="viz-title">{e(title)}</div>'
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
    return f'''<figure class="viz" data-mediavine-no-ads>
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
    return f'''<figure class="viz" data-mediavine-no-ads>
          <div class="viz-title">Where the case stands</div>
          <ol class="progress">{''.join(lis)}</ol>
          <p class="viz-sub" style="margin-top:var(--space-3)">{e(STATUS_EXPLAIN.get(status, ''))}</p>
        </figure>'''


MLA_MONTHS = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.']


def cite_html(name, canonical, modified):
    """Ready-made APA, MLA and Wikipedia citations with the permalink and last-updated date."""
    m = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', modified)
    if m and 1 <= int(m.group(2)) <= 12:
        y, mo, d = m.group(1), int(m.group(2)), int(m.group(3))
        apa_date = f'{y}, {viz.MONTHS[mo - 1]} {d}'
        mla_date = f'{d} {MLA_MONTHS[mo - 1]} {y}'
    else:
        y, apa_date, mla_date = modified[:4], modified, modified
    name = e(name)
    bare = canonical.replace('https://', '')
    return f'''<details class="cite-box" id="cite">
        <summary>Cite this entry</summary>
        <p class="cite-note">Permalink: <a href="{canonical}">{canonical}</a>. This entry was last updated on {viz.human_date(modified)}; cite that date as the publication date. The primary sources listed above should be cited for the underlying facts.</p>
        <dl class="cite-list">
          <div class="cite-item"><dt>APA</dt><dd><span id="cite-apa">{SITE}. ({apa_date}). <i>{name}</i>. {canonical}</span> <button type="button" class="cite-copy" data-copy="cite-apa">Copy</button></dd></div>
          <div class="cite-item"><dt>MLA</dt><dd><span id="cite-mla">\u201c{name}.\u201d <i>{SITE}</i>, {mla_date}, {bare}.</span> <button type="button" class="cite-copy" data-copy="cite-mla">Copy</button></dd></div>
          <div class="cite-item"><dt>Wikipedia</dt><dd><code id="cite-wiki">{{{{cite web |url={canonical} |title={name} |website={SITE} |date={modified} |access-date=}}}}</code> <button type="button" class="cite-copy" data-copy="cite-wiki">Copy</button></dd></div>
        </dl>
      </details>'''


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
    profs = serial_killers.BY_CASE.get(slug, [])
    if profs:
        details.append(('Offender profile', ', '.join(
            f'<a href="{prefix}serial-killers/{p["id"]}/">{e(p["name"])}</a>' for p in profs)))
    ck = city_key(c)
    if ck in CITY_HUBS:
        loc_bits = [f'<a href="{prefix}cities/{CITY_HUBS[ck]}/">{e(ck[0])}</a>']
    else:
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
        strip_html = f'''<figure class="viz" data-mediavine-no-ads>
          <div class="viz-title">Timeline to scale</div>
          <div class="viz-sub">Each dot is a dated event below; the distance between dots is elapsed time. The darker dot marks the incident.</div>
          {strip}
        </figure>'''
    locator = viz.locator_map(c.get('state'), state_links) if c['_us'] else ''
    locator_html = ''
    if locator:
        n_region = region_counts[region]
        locator_html = f'''<figure class="viz locator" data-mediavine-no-ads>
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

    tags = ''.join(
        (f'<a class="case-tag case-tag-link" href="{prefix}themes/{TAG_THEME[str(t).lower()]}/">{e(str(t))}</a>'
         if str(t).lower() in TAG_THEME else f'<span class="case-tag">{e(str(t))}</span>')
        for t in c.get('tags', []) if str(t).strip())
    tags_html = (f'<div class="case-tags-section" style="display:flex;gap:var(--space-2);flex-wrap:wrap;'
                 f'margin-top:var(--space-5);">{tags}</div>') if tags else ''

    related_html = ''
    if profs:
        related_html += f'''
  <section class="section" style="background: var(--color-surface);">
    <div class="section-inner">
      <h2 class="section-heading">Offender profile{'s' if len(profs) > 1 else ''}</h2>
      <p class="section-subtext">The person or people linked to this case have a profile with years active, victim counts, capture method, legal outcome and sources.</p>
      <div class="related-grid">{''.join(serial_killers.small_card(p, prefix) for p in profs)}</div>
      <a href="{prefix}serial-killers/{serial_killers.state_slug(profs[0]['primaryState'])}/" class="all-state-link">{e(serial_killers.state_name(profs[0]['primaryState']))} &rarr;</a>
    </div>
  </section>'''
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
        dec += ''.join(f'<a href="{prefix}themes/{s}/">{e(l)} cases</a>'
                       for s, l, _h, tg, _i in THEMES if c['_tags'] & tg)
        if ck in CITY_HUBS:
            dec += f'<a href="{prefix}cities/{CITY_HUBS[ck]}/">All {e(ck[0])} cases</a>'
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

      <dl class="case-details-grid" data-mediavine-no-ads>
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

      {cite_html(c['name'], canonical, modified)}
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
      <div class="stat-row" data-mediavine-no-ads>
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
        locator = f'''<figure class="viz locator" data-mediavine-no-ads>
        <div class="viz-title">{e(region)} on the map</div>
        <div class="viz-sub">Select another state to see its cases.</div>
        {svg}
      </figure>'''

    city_chips = ''.join(
        f'<a class="breakdown-chip" href="{prefix}cities/{CITY_HUBS[k]}/"><strong>{v}</strong> {e(k[0])}</a>'
        for k, v in sorted(((k, len(v)) for k, v in city_groups(cases).items() if k in CITY_HUBS),
                           key=lambda kv: (-kv[1], kv[0])))
    cities_html = (f'<h2 class="sub-heading">By city</h2><div class="breakdown-row">{city_chips}</div>'
                   if city_chips else '')
    n_sk = len(serial_killers.BY_STATE.get(region, []))
    if n_sk:
        cities_html += (f'<h2 class="sub-heading">Serial killers</h2><div class="hub-links">'
                        f'<a href="{prefix}serial-killers/{slug}/"><strong>{n_sk}</strong> '
                        f'{"profile" if n_sk == 1 else "profiles"}: {e(serial_killers.state_name(region))}</a></div>')
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
      {cities_html}

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

      <figure class="viz" data-mediavine-no-ads style="margin-top:var(--space-8)">
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


def render_hub(kind, slug, label, cases, siblings, intro, heading, *, links='', min_index=3):
    """kind: 'types', 'decades', 'themes' or 'cities'. siblings: [(slug, label, count)] for
    cross links. links: extra HTML placed under the intro. Returns (render, indexable)."""
    prefix = '../../'
    url = f'{BASE_URL}/{kind}/{slug}/'
    n = len(cases)
    unsolved = sum(1 for c in cases if c['_group'] == 'unsolved')
    ordered = sorted(cases, key=lambda c: (-(c.get('year') or 0), c['name']))
    parent, active = HUB_PARENT[kind]
    regions = Counter(c['_region'] for c in cases)
    types = Counter(c['type'] for c in cases)
    top_regions = ', '.join(f'{r} ({v})' for r, v in regions.most_common(3))
    top_types = ', '.join(f'{v} {TYPE_PLURAL.get(t, t).lower()}' for t, v in types.most_common(3))
    years = sorted(c['year'] for c in cases if c.get('year'))
    span = str(years[0]) if years[0] == years[-1] else f'{years[0]} to {years[-1]}'
    region_chips = ''.join(f'<a class="breakdown-chip" href="{prefix}states/{slugify(r)}/"><strong>{v}</strong> {e(r)}</a>'
                           for r, v in regions.most_common(12))
    type_chips = ''.join(f'<a class="breakdown-chip" href="{prefix}types/{slugify(TYPE_PLURAL.get(t, t))}/"><strong>{v}</strong> '
                         f'{e(TYPE_PLURAL.get(t, t))}</a>' for t, v in types.most_common())
    second = ''
    if kind == 'types':
        title = f'{label}: {n} Cold Cases'
        desc = fit(f'{plural(n, "documented case")} of this type, {span}: {unsolved} unsolved. '
                   f'Most entries: {top_regions}. Status, timeline and sources for each.', 158)
        second = decade_figure(cases, prefix, f'{label} by decade')
        chips = [('By state or country', region_chips)]
    elif kind == 'decades':
        title = f'Cold Cases of the {label}: {n} Cases'
        desc = fit(f'{plural(n, "documented case")} from the {label}: {unsolved} still unsolved. '
                   f'Includes {top_types}. Most entries: {top_regions}.', 158)
        yrs = Counter(c['year'] for c in cases)
        base = int(label[:4])
        data = [(str(y), yrs.get(y, 0)) for y in range(base, base + 10)]
        if n >= 4:
            second = f'''<figure class="viz" data-mediavine-no-ads>
        <div class="viz-title">Cases by year, {label}</div>
        {viz.columns(data, label=f"Cases by year in the {label}")}
      </figure>'''
        chips = [('By type', type_chips)]
    elif kind == 'themes':
        title = f'{label}: {n} Cold Cases'
        desc = fit(f'{plural(n, "documented case")} on this theme, {span}: {unsolved} unsolved. '
                   f'Includes {top_types}. Most entries: {top_regions}.', 158)
        second = decade_figure(cases, prefix, f'{label} cases by decade')
        chips = [('By type', type_chips), ('By state or country', region_chips)]
    else:
        region = cases[0]['_region']
        short = viz.STATE_ABBR.get(region, region)
        title = next(t for t in (f'Cold Cases in {label}, {short}: {n} Documented Cases',
                                 f'{label}, {short} Cold Cases: {n} Cases',
                                 f'{label} Cold Cases | {SITE}', f'{label}, {short} Cold Cases')
                     if len(t) <= 60)
        desc = fit(f'{plural(n, "documented case")} in {label}, {region}, {span}: {unsolved} still unsolved. '
                   f'Includes {top_types}. Status, timeline and sources for each case.', 158)
        second = decade_figure(cases, prefix, f'{label} cases by decade')
        chips = [('By type', type_chips)]
    if len(title) > 60:
        title = f'{label} | {SITE}' if kind != 'decades' else f'{label} Cold Cases'
    sib = ''.join(
        (f'<a href="../{s}/"><strong>{c}</strong> {e(l)}</a>' if s != slug
         else f'<a href="../{s}/" aria-current="page"><strong>{c}</strong> {e(l)}</a>')
        for s, l, c in siblings)
    chips_html = ''.join(f'<h2 class="sub-heading">{t}</h2><div class="breakdown-row">{h}</div>' for t, h in chips if h)
    cards = '\n      '.join(case_card(c, prefix, place='region' if kind != 'cities' else 'city') for c in ordered)
    indexable = n >= min_index
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), (parent, f'{kind}/'), (label, None)], prefix)}
      <h1 class="section-heading">{e(heading)}</h1>
      <p class="section-subtext">{intro}</p>
      {links}

      {status_figure(cases, f'Status of the {plural(n, "case")}')}
      {second}

      {chips_html}

      <h2 class="sub-heading">All {plural(n, 'case')}</h2>
      <div class="cases-grid">
      {cards}
      </div>

      <h2 class="sub-heading">{HUB_OTHERS[kind]}</h2>
      <div class="hub-links">{sib}<a href="../">{e(parent)}</a></div>
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
    return (lambda p, m: page(title=title, desc=desc, canonical=url, prefix=prefix, body=body,
                              schema=schema, active=active,
                              robots=None if indexable else 'noindex,follow')), indexable


def render_hub_index(kind, entries, total):
    """entries: [(slug, label, count, unsolved, blurb)]"""
    prefix = '../'
    url = f'{BASE_URL}/{kind}/'
    chart, crumb = '', None
    if kind == 'types':
        h1, title = 'Cold Cases by Type', f'Cold Cases by Type | {SITE}'
        desc = (f'{total} documented cases grouped into {len(entries)} types, from homicides and missing '
                f'persons to unidentified remains. Counts and unsolved totals for each.')
        lead = 'Every case in the index is assigned one type. Choose a type to see all of its cases, how many remain unsolved and how they spread across decades.'
    elif kind == 'decades':
        h1, title = 'Cold Cases by Decade', f'Cold Cases by Decade | {SITE}'
        desc = (f'{total} documented cases from the {entries[0][1]} to the {entries[-1][1]}, grouped by the '
                f'decade of the incident. Counts and unsolved totals for each decade.')
        lead = 'Cases are grouped by the decade in which the crime or disappearance happened, not when it was solved.'
        chart = viz.columns([(l, c) for _, l, c, _, _ in entries],
                            links={l: f'./{s}/' for s, l, _, _, _ in entries}, label='Cases by decade')
    elif kind == 'themes':
        h1, title = 'Cold Cases by Theme', f'Cold Cases by Theme | {SITE}'
        desc = (f'{total} documented cases across {len(entries)} themes: genetic genealogy, college students, '
                f'civil rights era killings, disputed convictions, Doe cases and bodies never found.')
        lead = ('Themes cut across type, place and decade, and a case can belong to more than one. Each hub lists '
                'every case carrying the theme\'s tags, how many remain unsolved and how they spread across decades.')
    else:
        h1, title = 'Cold Cases by City', f'Cold Cases by City | {SITE}'
        desc = (f'{total} documented cases in the {len(entries)} cities with two or more cases, '
                f'from {entries[0][1]} and {entries[1][1]} down. Counts and unsolved totals for each.')
        lead = ('Cities and towns with at least two documented cases. Select one for its cases, their status and '
                'how they spread across decades. The <a href="../map/">case map</a> plots every US case by city.')
        chart = viz.columns([(l, c) for _, l, c, _, _ in entries[:12]],
                            links={l: f'./{s}/' for s, l, _, _, _ in entries[:12]}, label='Cities with the most cases')
    mx = max(c for _, _, c, _, _ in entries)
    cards = ''.join(f'''<a href="./{s}/" class="state-card">
            <div class="state-card-header"><span class="state-name">{e(l)}</span><span class="state-count-badge">{c}</span></div>
            <div class="state-bar-wrapper"><div class="state-bar" style="width:{c / mx * 100:.1f}%"></div></div>
            <div class="state-card-meta">{plural(c, 'case')}, {u} unsolved{('. ' + e(b)) if b else ''}</div>
          </a>''' for s, l, c, u, b in entries)
    fig = ''
    if chart:
        cap = {'decades': ('Cases in the index by decade', 'Select a column to open that decade.'),
               'cities': ('Cities with the most documented cases', 'Select a column to open that city.')}[kind]
        fig = f'''<figure class="viz" data-mediavine-no-ads><div class="viz-title">{cap[0]}</div>
        <div class="viz-sub">{cap[1]}</div>{chart}</figure>'''
    crumb = h1.replace('Cold Cases', 'Cases')
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), (crumb, None)], prefix)}
      <h1 class="section-heading">{h1}</h1>
      <p class="section-subtext">{lead}</p>
      {fig}
      <div class="states-grid" style="margin-top:var(--space-8)">{cards}</div>
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), (crumb, url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": h1, "description": desc,
         "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"}},
    ]
    active = HUB_PARENT[kind][1]
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


# ─────────────────────────── themes and cities ───────────────────────────

# slug, label, heading, member tags (normalised, lower case), intro
THEMES = [
    ('genetic-genealogy', 'Genetic Genealogy', 'Cold Cases and Forensic Genetic Genealogy',
     {'genetic genealogy', 'dna doe project', 'othram', 'parabon nanolabs'},
     'Cases in which investigators used forensic genetic genealogy: comparing DNA from a crime scene or from '
     'unidentified remains against public genealogy databases to build a family tree that points to a name. '
     'The list includes victims and suspects identified this way and unidentified-remains cases where the work '
     'is still under way.'),
    ('college-students', 'College Students', 'Cold Cases Involving College Students',
     {'college student', 'college', 'university', 'sorority', 'college campus', 'campus disappearance',
      'law student', 'nursing students', 'exchange student'},
     'Homicides and disappearances of college and university students, on campus and off. Several of these '
     'cases led to changes in campus safety law and practice.'),
    ('civil-rights', 'Civil Rights Era', 'Civil Rights Era Cold Cases',
     {'civil rights', 'civil rights era', 'freedom summer', 'ku klux klan', 'kkk', 'selma', 'naacp'},
     'Killings connected to the civil rights movement and to racial terror in the United States, many of them '
     'left unprosecuted for decades. Some were reopened under the Emmett Till Unsolved Civil Rights Crime Act '
     'and ended in convictions forty years or more after the crime.'),
    ('wrongful-conviction', 'Wrongful and Disputed Convictions', 'Wrongful and Disputed Convictions',
     {'wrongful conviction', 'exoneration', 'conviction overturned', 'wrongful conviction concerns',
      'wrongful conviction possible', 'coerced confession', 'recanted confession', 'disputed conviction',
      'controversial conviction'},
     'Cases in which a conviction was overturned or the convicted person was exonerated, and cases in which a '
     'conviction has been publicly disputed. Listing a case here does not mean the conviction was wrong: each '
     'entry states precisely what a court has and has not found.'),
    ('jane-john-doe', 'Jane and John Doe Cases', 'Jane Doe and John Doe Cases',
     {'jane doe', 'john doe', 'doe case', 'princess doe', 'buckskin girl', 'jane doe identified'},
     'People who were known for years only by a placeholder name because their remains could not be '
     'identified. Some have since been given their names back, usually through DNA; the rest are still '
     'waiting. The type hub for unidentified persons lists every case of that type, named or not.'),
    ('body-never-found', 'Body Never Found', 'Cases Where the Body Was Never Found',
     {'body never found'},
     'Disappearances and presumed homicides in which no remains have ever been recovered, including several '
     'that ended in a conviction without a body.'),
]
TAG_THEME = {t: slug for slug, _l, _h, tags, _i in THEMES for t in tags}

HUB_PARENT = {'types': ('Cases by type', 'By Type'), 'decades': ('Cases by decade', 'By Decade'),
              'themes': ('Cases by theme', None), 'cities': ('Cases by city', None)}
HUB_OTHERS = {'types': 'Other case types', 'decades': 'Other decades', 'themes': 'Other themes',
              'cities': 'Other cities with several cases'}

CITY_SKIP = re.compile(r'^(multiple|various|unknown|several|statewide)\b', re.I)
CITY_HUBS = {}   # (city, region) -> slug, filled in main() before case pages render


def city_key(c):
    city = c.get('city')
    if known(city) and not CITY_SKIP.match(str(city)):
        return (str(city).strip(), c['_region'])
    return None


def city_slug(city, region):
    return slugify(f'{city} {viz.STATE_ABBR.get(region, region)}')


def city_groups(cases, min_cases=2):
    groups = defaultdict(list)
    for c in cases:
        k = city_key(c)
        if k:
            groups[k].append(c)
    return {k: v for k, v in groups.items() if len(v) >= min_cases}


# ─────────────────────────── map explorer ───────────────────────────

CITY_COORDS_FILE = os.path.join(ROOT, 'data', 'city-coords.json')


def map_points(cases):
    """{'City|State': [x, y, hub_slug]} for every US city with cached coordinates."""
    coords = {}
    if os.path.exists(CITY_COORDS_FILE):
        with open(CITY_COORDS_FILE, encoding='utf-8') as f:
            coords = json.load(f)
    points, missing = {}, Counter()
    for c in cases:
        if not c['_us']:
            continue
        k = city_key(c)
        if not k:
            missing['unplaceable'] += 1
            continue
        key = f'{k[0]}|{k[1]}'
        if key in points:
            continue
        hit = coords.get(key)
        pt = geo.project(hit['lon'], hit['lat']) if hit else None
        if not pt:
            missing['no coordinates'] += 1
            continue
        points[key] = [pt[0], pt[1], CITY_HUBS.get(k, '')]
    return points, missing


MAP_JS = r"""
(function(){
var P=MAP_POINTS,data=[],groups={},sel=null;
var GROUP={'Unsolved':'unsolved','Partially Solved':'partial','Identified':'partial','Arrest Made':'proceedings','Pending Trial':'proceedings','Wanted':'proceedings','Solved':'resolved','Conviction':'resolved','No Conviction':'other','Ruled Suicide':'other'};
var BADGE={unsolved:'badge-unsolved',partial:'badge-partial',proceedings:'badge-arrest',resolved:'badge-conviction',other:'badge-neutral'};
var $=function(id){return document.getElementById(id)};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]})};
var dots=$('mapDots'),panel=$('mapPanel'),count=$('mapCount');
var slugKey={};Object.keys(P).forEach(function(k){if(P[k][2])slugKey[P[k][2]]=k});
function key(c){return c.city+'|'+c.state}
function n(x,one,many){return x+' '+(x===1?one:many)}
function fill(id,vals,fmt){var el=$(id);vals.forEach(function(v){var o=document.createElement('option');o.value=v;o.textContent=fmt?fmt(v):v;el.appendChild(o)})}
function uniq(a){return a.filter(function(v,i){return v!==''&&v!=null&&a.indexOf(v)===i}).sort()}
function filtered(){var st=$('mapStatus').value,t=$('mapType').value,d=$('mapDecade').value;
  return data.filter(function(c){if(!P[key(c)])return false;if(st&&GROUP[c.status]!==st)return false;if(t&&c.type!==t)return false;if(d&&Math.floor((c.year||0)/10)*10!==+d)return false;return true})}
function place(k){return k.split('|')[0]+', '+k.split('|')[1]}
function draw(){
  var rows=filtered();groups={};
  rows.forEach(function(c){var k=key(c);(groups[k]=groups[k]||[]).push(c)});
  var keys=Object.keys(groups).sort(function(a,b){return groups[b].length-groups[a].length});
  dots.innerHTML=keys.map(function(k){var p=P[k],m=groups[k].length,r=(3+1.7*Math.sqrt(m)).toFixed(1);
    return '<circle class="map-dot'+(k===sel?' on':'')+'" cx="'+p[0]+'" cy="'+p[1]+'" r="'+r+'" data-k="'+esc(k)+'" tabindex="0" role="button" aria-label="'+esc(place(k)+': '+n(m,'case','cases'))+'"><title>'+esc(place(k)+': '+n(m,'case','cases'))+'</title></circle>'}).join('');
  count.textContent=n(rows.length,'case','cases')+' in '+n(keys.length,'city','cities');
  if(sel&&!groups[sel])sel=null;
  show();
  var q=new URLSearchParams();
  [['status','mapStatus'],['type','mapType'],['decade','mapDecade']].forEach(function(p){if($(p[1]).value)q.set(p[0],$(p[1]).value)});
  if(sel&&P[sel][2])q.set('city',P[sel][2]);
  var qs=q.toString();try{history.replaceState(null,'',location.pathname+(qs?'?'+qs:''))}catch(e){}
}
function show(){
  if(!sel){panel.innerHTML='<p class="map-panel-hint">Select a dot to list the cases recorded in that city. Larger dots hold more cases. Dots mark the city, not an address.</p>';return}
  var cs=groups[sel].slice().sort(function(a,b){return (b.year||0)-(a.year||0)||a.name.localeCompare(b.name)});
  var city=sel.split('|')[0],state=sel.split('|')[1],p=P[sel];
  var hub=p[2]?'<a class="all-state-link" href="../cities/'+p[2]+'/">All '+esc(city)+' cases &rarr;</a>':'';
  panel.innerHTML='<h2 class="map-panel-title">'+esc(city)+', '+esc(state)+'</h2><p class="map-panel-sub">'+n(cs.length,'case','cases')+' matching the current filters</p><ol class="map-panel-list">'+cs.map(function(c){return '<li><a href="../cases/'+encodeURIComponent(c.id)+'/"><span class="badge '+BADGE[GROUP[c.status]||'unsolved']+'">'+esc(c.status)+'</span><span class="map-panel-name">'+esc(c.name)+'</span><span class="map-panel-year">'+esc(c.year||'')+'</span></a></li>'}).join('')+'</ol>'+hub;
}
function select(k){sel=(sel===k)?null:k;[].forEach.call(dots.querySelectorAll('.map-dot'),function(d){d.classList.toggle('on',d.dataset.k===sel)});show();
  var q=new URLSearchParams(location.search);if(sel&&P[sel][2])q.set('city',P[sel][2]);else q.delete('city');var qs=q.toString();try{history.replaceState(null,'',location.pathname+(qs?'?'+qs:''))}catch(e){}}
dots.addEventListener('click',function(ev){var t=ev.target.closest('.map-dot');if(t)select(t.dataset.k)});
dots.addEventListener('keydown',function(ev){if(ev.key!=='Enter'&&ev.key!==' ')return;var t=ev.target.closest('.map-dot');if(!t)return;ev.preventDefault();select(t.dataset.k)});
['mapStatus','mapType','mapDecade'].forEach(function(id){$(id).addEventListener('change',draw)});
$('mapReset').addEventListener('click',function(){['mapStatus','mapType','mapDecade'].forEach(function(id){$(id).value=''});sel=null;draw()});
fetch('../data/cases-index.json').then(function(r){return r.json()}).then(function(d){
  data=d;
  fill('mapType',uniq(data.filter(function(c){return P[key(c)]}).map(function(c){return c.type})));
  fill('mapDecade',uniq(data.map(function(c){return c.year?Math.floor(c.year/10)*10:null})).sort(function(a,b){return a-b}),function(v){return v+'s'});
  var q=new URLSearchParams(location.search),map={status:'mapStatus',type:'mapType',decade:'mapDecade'};
  Object.keys(map).forEach(function(k){var v=q.get(k);if(!v)return;var el=$(map[k]);if([].some.call(el.options,function(o){return o.value===v}))el.value=v});
  var city=q.get('city');if(city&&slugKey[city])sel=slugKey[city];
  $('mapFilters').hidden=false;draw();
  if(sel)$('mapPanel').scrollIntoView({block:'nearest'});
}).catch(function(){count.textContent='The case index could not be loaded.'});
})();
"""


def render_map(cases, city_hubs_count):
    prefix = '../'
    url = f'{BASE_URL}/map/'
    points, missing = map_points(cases)
    states = geo.load_states()
    us = [c for c in cases if c['_us']]
    plotted = [c for c in us if city_key(c) and f'{city_key(c)[0]}|{city_key(c)[1]}' in points]
    intl = len(cases) - len(us)
    by_state = Counter(c['state'] for c in plotted)
    n_states = len(by_state)
    unplaced = len(us) - len(plotted)
    groups = city_groups(cases, 1)
    top = sorted(((k, len(v)) for k, v in groups.items() if k in CITY_HUBS), key=lambda kv: (-kv[1], kv[0]))[:24]
    top_chips = ''.join(
        f'<a class="breakdown-chip" href="{prefix}cities/{CITY_HUBS[k]}/"><strong>{n}</strong> {e(k[0])}, {e(viz.STATE_ABBR.get(k[1], k[1]))}</a>'
        for k, n in top)
    state_paths = ''.join(
        f'<path class="map-state" d="{d}"><title>{e(viz.ABBR_STATE[ab])}: {plural(by_state.get(viz.ABBR_STATE[ab], 0), "case")}</title></path>'
        for ab, d in states.items())
    status_opts = ''.join(f'<option value="{g}">{e(lab)}</option>' for g, (lab, *_rest) in STATUS_GROUPS.items())
    title = f'Cold Case Map: {len(plotted)} US Cases by City'
    desc = (f'Interactive map of {len(plotted)} documented cold cases across {len(points)} US cities and '
            f'{n_states} states. Filter by status, type and decade; select a city to see its cases.')
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Map', None)], prefix)}
      <h1 class="section-heading">Cold Case Map</h1>
      <p class="section-subtext">{len(plotted)} of the {len(us)} US cases in the index are placed on the map below, at the city level, across {len(points)} cities in {n_states} states and the District of Columbia. Dots mark a city, never an address. Filter by status, type or decade, then select a dot to list that city's cases. {unplaced} US {"case spans" if unplaced == 1 else "cases span"} several places or {"has" if unplaced == 1 else "have"} no mappable city and {"is" if unplaced == 1 else "are"} not plotted; the {intl} cases outside the United States are listed <a href="{prefix}states/">by country</a>.</p>

      <div class="map-filters" id="mapFilters" hidden data-mediavine-no-ads>
        <div><label for="mapStatus">Status</label><select id="mapStatus"><option value="">All statuses</option>{status_opts}</select></div>
        <div><label for="mapType">Type</label><select id="mapType"><option value="">All types</option></select></div>
        <div><label for="mapDecade">Decade</label><select id="mapDecade"><option value="">All decades</option></select></div>
        <button type="button" class="map-reset" id="mapReset">Reset</button>
        <span class="map-count" id="mapCount" role="status" aria-live="polite"></span>
      </div>

      <div class="map-explorer" data-mediavine-no-ads>
        <figure class="viz viz-wide map-stage" data-mediavine-no-ads>
          <svg viewBox="0 0 {geo.W} {geo.H}" role="img" aria-label="Map of the United States with a dot for every city that has documented cases" xmlns="http://www.w3.org/2000/svg">
            <g class="map-states">{state_paths}</g>
            <g id="mapDots"></g>
          </svg>
          <figcaption class="viz-sub">Base map: US Atlas (Census Bureau cartographic boundaries), Albers USA projection. City positions from OpenStreetMap.</figcaption>
        </figure>
        <aside class="map-panel" id="mapPanel" aria-live="polite"><p class="map-panel-hint">Loading the case index…</p></aside>
      </div>

      <h2 class="sub-heading">Cities with the most documented cases</h2>
      <div class="breakdown-row">{top_chips}</div>
      <div class="hub-links">
        <a href="{prefix}cities/">All cities with several cases ({city_hubs_count})</a>
        <a href="{prefix}states/">Cases by state and country</a>
        <a href="{prefix}types/">Cases by type</a>
      </div>
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Map', url)]),
        {"@context": "https://schema.org", "@type": "WebPage", "name": "Cold case map",
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"}},
    ]
    js = 'var MAP_POINTS=' + json.dumps(points, separators=(',', ':')) + ';' + MAP_JS
    print(f'Map: {len(points)} cities plotted, {len(plotted)} cases; not placed: {dict(missing)}')
    return lambda p, m: page(title=title, desc=desc, canonical=url, prefix=prefix, body=body,
                             schema=schema, active='Map', extra_js=js)


# ─────────────────────────── analysis pages ───────────────────────────

ANALYSIS = [
    ('how-long-cold-cases-take-to-solve', 'How long do cold cases take to solve?'),
    ('cold-case-resolution-methods', 'How cold cases get solved'),
]


METHOD_SHORT = {'initial': 'Initial', 'genealogy': 'Genealogy', 'dna': 'DNA match', 'confession': 'Confession',
                'witness': 'Witness or tip', 'other-crime': 'Other arrest', 'fingerprint': 'Fingerprint',
                'other': 'Not stated'}


def stat_row(items):
    return ('<div class="stat-row" data-mediavine-no-ads>'
            + ''.join(f'<div class="stat"><span class="stat-value">{v}</span><span class="stat-label">{e(l)}</span></div>'
                      for v, l in items) + '</div>')


def data_table(headers, rows, caption=''):
    th = ''.join(f'<th scope="col">{e(h)}</th>' for h in headers)
    body = ''.join('<tr>' + ''.join((f'<th scope="row">{cells[0]}</th>' if i == 0 else f'<td>{v}</td>')
                                    for i, v in enumerate(cells)) + '</tr>' for cells in rows)
    cap = f'<caption>{caption}</caption>' if caption else ''
    return (f'<div class="table-wrap" data-mediavine-no-ads tabindex="0"><table class="data-table">{cap}'
            f'<thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>')


def rec_link(r, prefix):
    return f'<a href="{prefix}cases/{r["id"]}/">{e(r["name"])}</a>'


def fmt_years(y):
    if y is None:
        return '—'
    return f'{y:g}'


def analysis_page(slug, title, h1, desc, lead, sections, method_notes, recs_n):
    """Shared shell for the analysis reports."""
    prefix = '../../'
    url = f'{BASE_URL}/analysis/{slug}/'
    others = ''.join(f'<a href="../{s}/">{e(l)}</a>' for s, l in ANALYSIS if s != slug)
    notes = ''.join(f'<li>{n}</li>' for n in method_notes)

    def render(published, modified):
        mod_h = viz.human_date(modified) if modified != '0000-00-00' else ''
        body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Analysis', 'analysis/'), (title, None)], prefix)}
      <div class="case-page-header">
        <div class="case-page-meta-row"><span class="case-type-label">Analysis</span><span class="case-year-label">Based on {recs_n} resolved cases, computed {mod_h}</span></div>
        <h1 class="case-page-title">{e(h1)}</h1>
      </div>
      <p class="case-summary">{lead}</p>
      {sections}
      <div class="case-narrative-section">
        <h2 class="section-label">Method and caveats</h2>
        <ul class="how-to-help-list">{notes}</ul>
        <p class="case-narrative">The figures are recomputed from <a href="{prefix}data/cases.json">the published dataset</a> on every build, so they change as cases are added or their status changes. The rules live in <code>scripts/analysis.py</code> in the site's source. To report an error, email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
      </div>
      <p class="case-updated">Last recomputed {mod_h}.</p>
      {cite_html(h1, url, modified)}
      <h2 class="sub-heading">More analysis</h2>
      <div class="hub-links">{others}<a href="../">All analysis</a><a href="{prefix}map/">Case map</a><a href="{prefix}themes/genetic-genealogy/">Genetic genealogy cases</a></div>
    </div>
  </section>
'''
        article = {
            "@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc,
            "url": url, "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "image": OG_IMAGE,
            "inLanguage": "en-US", "articleSection": "Analysis",
            "datePublished": published, "dateModified": modified,
            "author": {"@type": "Organization", "name": SITE, "url": f'{BASE_URL}/about/'},
            "publisher": {"@type": "Organization", "name": SITE, "url": BASE_URL,
                          "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/logos/logo-icon-512x512.png"}},
            "isBasedOn": {"@type": "Dataset", "name": f"{SITE} case database", "url": f"{BASE_URL}/data/cases.json"},
        }
        crumbs = breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Analysis', f'{BASE_URL}/analysis/'), (title, url)])
        return page(title=f'{title} | {SITE}', desc=desc, canonical=url, prefix=prefix, body=body, schema=[article, crumbs],
                    active='Analysis', og_type='article', published=published, modified=modified)
    return render


def render_analysis_time(recs, skipped):
    prefix = '../../'
    n = len(recs)
    fast = [r for r in recs if r['years'] <= 1]
    cold = [r for r in recs if r['years'] >= 2]
    cold_years = [r['years'] for r in cold]
    med_cold = analysis.median(cold_years)
    over10 = sum(1 for y in cold_years if y >= 10)
    over20 = sum(1 for y in cold_years if y >= 20)
    over30 = sum(1 for r in recs if r['years'] >= 30)
    longest = sorted(recs, key=lambda r: (-r['years'], r['name']))
    top = longest[0]
    conv = [r for r in recs if r['closed'] is not None]
    conv_gap = [r['closed'] - r['broke'] for r in conv]
    bk = analysis.buckets(recs)
    decs = analysis.by_decade(recs)
    types = defaultdict(list)
    for r in recs:
        types[r['type']].append(r['years'])

    sec = []
    sec.append(stat_row([
        (n, 'resolved cases with a dated break in the timeline'),
        (f'{round(len(fast) / n * 100)}%', 'broken within a year of the crime'),
        (f'{fmt_years(med_cold)} yrs', f'median wait for the {len(cold)} cases that went cold'),
        (over30, 'cases that took 30 years or more'),
    ]))
    sec.append(f'''<div class="case-narrative-section">
        <h2 class="section-label">The two kinds of resolved case</h2>
        <p class="case-narrative">Of the {n} cases, {len(fast)} ({round(len(fast) / n * 100)}%) were broken within a year of the crime or disappearance: an arrest, charge or identification followed the initial investigation. The other {len(cold)} went cold first. Among those, the median wait between the crime and the break was {fmt_years(med_cold)} years; {over10} waited ten years or more and {over20} waited twenty years or more. The longest wait in the index is {rec_link(top, prefix)}, broken {top['years']} years after the event, in {top['broke']}.</p>
        <p class="case-narrative">For the {len(conv)} cases that ended in a conviction, the median gap between the break and the conviction was {fmt_years(analysis.median(conv_gap))} {"year" if analysis.median(conv_gap) == 1 else "years"}; {sum(1 for g in conv_gap if g >= 3)} took three years or more from arrest to verdict.</p>
      </div>''')
    # Chart and its data table share one no-ads block so an in-content ad cannot land between them.
    bk_table = data_table(['Years from crime to break', 'Cases', 'Share'],
                          [(e(lab), v, f'{round(v / n * 100)}%') for lab, v in bk])
    sec.append(f'''<div class="viz-group" data-mediavine-no-ads>
      <figure class="viz" data-mediavine-no-ads>
        <div class="viz-title">Years from the crime to the break, all {n} resolved cases</div>
        <div class="viz-sub">The break is the first dated arrest, charge, identification, DNA match or confession in the case timeline.</div>
        {viz.columns(bk, label='Years to resolution')}
      </figure>
      {bk_table}
    </div>''')

    dec_rows = []
    for d, cnt, med, mean, over, within in decs:
        if cnt < 5:
            continue
        dec_rows.append((f'<a href="{prefix}decades/{d}s/">{d}s</a>', cnt, fmt_years(med), fmt_years(mean),
                         f'{round(within / cnt * 100)}%', f'{round(over / cnt * 100)}%'))
    small = sum(cnt for d, cnt, *_ in decs if cnt < 5)
    sec.append(f'''<h2 class="sub-heading">By decade of the crime</h2>
      <p class="section-subtext">Recent decades can only hold cases that were resolved quickly, because the slow ones have not been resolved yet. Read the 2010s and 2020s rows as a floor, not a trend. Decades with fewer than five resolved cases ({small} cases in total) are left out.</p>
      {data_table(['Decade', 'Resolved cases', 'Median years', 'Mean years', 'Broken within a year', 'Took 10+ years'], dec_rows)}''')

    bm = analysis.by_method(recs)
    m_rows = [(f'<a href="../cold-case-resolution-methods/#{k}">{e(lab)}</a>', cnt, fmt_years(med),
               sum(1 for r in rs if r['years'] >= 2))
              for k, lab, cnt, med, rs in bm]
    sec.append(f'''<h2 class="sub-heading">By what broke the case</h2>
      <p class="section-subtext">Genetic genealogy and DNA database matches are the methods that resolve the oldest cases. Confessions and tips arrive at every age. The <a href="../cold-case-resolution-methods/">resolution methods report</a> has the detail.</p>
      {data_table(['Method', 'Cases', 'Median years to break', 'Of which went cold (2+ years)'], m_rows)}''')

    t_rows = sorted(((t, len(ys), analysis.median(ys), sum(1 for y in ys if y >= 10)) for t, ys in types.items() if len(ys) >= 5),
                    key=lambda x: -x[1])
    sec.append(f'''<h2 class="sub-heading">By case type</h2>
      {data_table(['Type', 'Resolved cases', 'Median years', 'Took 10+ years'],
                  [(f'<a href="{prefix}types/{slugify(TYPE_PLURAL.get(t, t))}/">{e(TYPE_PLURAL.get(t, t))}</a>', cnt, fmt_years(med), over) for t, cnt, med, over in t_rows],
                  'Types with fewer than five resolved cases are left out.')}''')

    l_rows = [(rec_link(r, prefix), r['inc'], r['broke'], r['years'], e(analysis.METHOD_LABEL[r['method']]))
              for r in longest[:20]]
    sec.append(f'''<h2 class="sub-heading">The twenty longest waits</h2>
      {data_table(['Case', 'Crime', 'Break', 'Years', 'What broke it'], l_rows)}''')

    notes = [
        f'<strong>Which cases.</strong> Every case whose status is Conviction, Solved or Identified: {n + len(skipped)} cases. {len(skipped)} of them have no dated event in their timeline that matches the break rules (for example the suspect died before any arrest, or the victim was found alive) and are left out. Cases with the status Partially Solved, Arrest Made, Pending Trial, Wanted, No Conviction or Ruled Suicide are not counted as resolved.',
        '<strong>The break.</strong> The first timeline event, dated in or after the year of the crime, whose text records an arrest, charge, indictment, identification, DNA or fingerprint match, confession or guilty plea. Years are counted as whole calendar years between the year of the crime and the year of that event, so a case broken the next January counts as one year.',
        '<strong>Selection.</strong> ColdCaseIndex is a curated index of notable cases, not a random sample of all homicides and disappearances. Famous cases that were solved quickly and famous cases that took decades are both over-represented compared with routine investigations. The figures describe the index, and should be cited that way.',
        '<strong>Dates.</strong> Timeline dates are taken from the sources listed on each case page. Where a source gives only a year, that year is used.',
    ]
    lead = (f'Among the {n} resolved cases in this index whose timelines record when the case broke, '
            f'{round(len(fast) / n * 100)}% were broken within a year. For the {len(cold)} that went cold first, '
            f'the median wait was {fmt_years(med_cold)} years and {over20} waited twenty years or more, '
            f'most of them until a DNA match or genetic genealogy named a suspect or a victim.')
    desc = fit(f'Resolution times for {n} solved cold cases: {round(len(fast) / n * 100)}% broken within a year; '
               f'for cases that went cold the median wait was {fmt_years(med_cold)} years. Breakdowns by decade, '
               f'method and type.', 158)
    return analysis_page('how-long-cold-cases-take-to-solve', 'How long do cold cases take to solve?',
                         'How Long Do Cold Cases Take to Solve?', desc, lead, '\n'.join(sec), notes, n)


def render_analysis_methods(recs, skipped, genealogy_cases):
    prefix = '../../'
    n = len(recs)
    bm = analysis.by_method(recs)
    counts = {k: cnt for k, _l, cnt, _m, _rs in bm}
    cold = [r for r in recs if r['years'] >= 2]
    cold_methods = Counter(r['method'] for r in cold)
    gen = next(((cnt, med, rs) for k, _l, cnt, med, rs in bm if k == 'genealogy'), (0, None, []))
    dna = next(((cnt, med, rs) for k, _l, cnt, med, rs in bm if k == 'dna'), (0, None, []))
    conf = next(((cnt, med, rs) for k, _l, cnt, med, rs in bm if k == 'confession'), (0, None, []))
    gen_years = sorted(r['broke'] for r in gen[2])
    gen_first = gen_years[0] if gen_years else None
    gen_recent = sum(1 for y in gen_years if y >= 2018)
    over20 = [r for r in recs if r['years'] >= 20]
    over20_lab = Counter(r['method'] for r in over20)
    lab_share = ', '.join(f'{analysis.METHOD_LABEL[k].lower()} ({v})' for k, v in over20_lab.most_common(3))
    conf_fast = sum(1 for r in conf[2] if r['years'] <= 1)
    conf_late = sum(1 for r in conf[2] if r['years'] >= 5)
    w20, f20 = over20_lab.get('witness', 0), over20_lab.get('fingerprint', 0)
    over20_tail = (f'{"None" if f20 == 0 else f20} of them {"was" if f20 == 1 else "were"} resolved by a fingerprint and '
                   f'{"none" if w20 == 0 else w20} by a witness or tip.')
    dna_first = min((r['broke'] for r in dna[2]), default=None)

    sec = []
    sec.append(stat_row([
        (n, 'resolved cases classified'),
        (gen[0], 'broken by genetic genealogy'),
        (dna[0], 'broken by a DNA match'),
        (conf[0], 'broken by a confession'),
    ]))
    sec.append(f'''<div class="case-narrative-section">
        <h2 class="section-label">What breaks a cold case</h2>
        <p class="case-narrative">For {counts.get('initial', 0)} of the {n} resolved cases ({round(counts.get('initial', 0) / n * 100)}%) the break came in the initial investigation, within a year of the crime, and the timeline records nothing more specific than the arrest. The remaining {n - counts.get('initial', 0)} cases are where the methods separate. Genetic genealogy accounts for {gen[0]} cases, all broken in {gen_first} or later, with a median wait of {fmt_years(gen[1])} years. A DNA database or direct DNA match accounts for {dna[0]} (median {fmt_years(dna[1])} years). Confessions account for {conf[0]}: {conf_fast} of them came within a year of the crime and {conf_late} came five years or more later.</p>
        <p class="case-narrative">Among the {len(over20)} cases that waited twenty years or more, the breaks came from {lab_share}. {over20_tail}</p>
      </div>''')
    m_rows = []
    for k, lab, cnt, med, rs in bm:
        m_rows.append((f'<span id="{k}">{e(lab)}</span>', cnt, f'{round(cnt / n * 100)}%', fmt_years(med),
                       cold_methods.get(k, 0)))
    sec.append(f'''<h2 class="sub-heading">Resolution methods, all {n} resolved cases</h2>
      {data_table(['Method', 'Cases', 'Share', 'Median years to break', 'Of which went cold (2+ years)'], m_rows)}''')
    chart = viz.columns([(METHOD_SHORT.get(k, lab), cnt) for k, lab, cnt, _m, _rs in bm], label='Resolved cases by method')
    sec.append(f'<figure class="viz" data-mediavine-no-ads><div class="viz-title">Resolved cases by what broke them</div>{chart}</figure>')

    bd = analysis.by_break_decade(recs)
    cols = [k for k in analysis.METHOD_ORDER if counts.get(k)]
    d_rows = []
    for d, cnt in bd:
        tot = sum(cnt.values())
        if tot < 5:
            continue
        d_rows.append((f'{d}s', tot, *[cnt.get(k, 0) or '' for k in cols]))
    sec.append(f'''<h2 class="sub-heading">By the decade the case broke</h2>
      <p class="section-subtext">Counted by the year of the break, not the year of the crime. The first DNA match in the index came in {dna_first}, the first genetic genealogy identification in {gen_first}. Decades with fewer than five breaks are left out.</p>
      {data_table(['Decade', 'Cases'] + [METHOD_SHORT.get(k, analysis.METHOD_LABEL[k]) for k in cols], d_rows)}''')

    g_rows = [(rec_link(r, prefix), r['inc'], r['broke'], r['years'], e(r['status']))
              for r in sorted(gen[2], key=lambda r: (r['broke'], r['name']))]
    sec.append(f'''<h2 class="sub-heading" id="genealogy-cases">The {gen[0]} genetic genealogy resolutions</h2>
      <p class="section-subtext">{len(genealogy_cases)} cases in the index involve forensic genetic genealogy. {gen[0]} of them are resolved with the technique credited in the timeline; the rest are unidentified-remains cases where it has produced leads but not yet a name, or cases where it identified a victim but not the person responsible. {gen_recent} of the {gen[0]} resolutions came in 2018 or later. See the <a href="{prefix}themes/genetic-genealogy/">genetic genealogy theme hub</a> for all {len(genealogy_cases)}.</p>
      {data_table(['Case', 'Crime', 'Identified', 'Years', 'Status'], g_rows)}''')

    for k, lab, cnt, med, rs in bm:
        if k in ('genealogy', 'initial', 'other'):
            continue
        rows = [(rec_link(r, prefix), r['inc'], r['broke'], r['years'], e(fit(r['event'], 140))) for r in rs[:8]]
        sec.append(f'''<h2 class="sub-heading">{e(lab)}: {cnt} cases, longest waits</h2>
      {data_table(['Case', 'Crime', 'Break', 'Years', 'Timeline entry'], rows)}''')

    notes = [
        f'<strong>Which cases.</strong> The {n} cases with status Conviction, Solved or Identified whose timeline holds a dated break event; {len(skipped)} resolved cases without one are left out. See the <a href="../how-long-cold-cases-take-to-solve/">resolution times report</a> for the definition of the break.',
        '<strong>Classification.</strong> The break event and the two timeline entries that follow it are matched against keyword rules, in this order: genetic genealogy (also matched on the case tags), DNA match, fingerprint, confession or surrender, witness, tip or informant, arrest in another case, and reinvestigation. A case broken within a year that matches none of them is counted as the initial investigation; one broken later that matches none is counted as not stated. Each case gets one method, the first that matches, even where several contributed.',
        '<strong>What the categories mean.</strong> "DNA match" covers direct comparisons and database (CODIS) hits, including familial searches of offender databases; "genetic genealogy" covers family-tree work from public genealogy databases. "Arrest in another case" means the suspect was identified after being arrested or caught for a different crime, or after a victim escaped.',
        '<strong>Selection.</strong> The index favours notable cases, and cases solved by new forensic techniques are notable. The share of genealogy resolutions here is far higher than in homicide clearances generally.',
    ]
    lead = (f'Of the {n} resolved cases in this index, {counts.get("initial", 0)} were broken in the initial '
            f'investigation. Among the rest, genetic genealogy ({gen[0]} cases, median wait {fmt_years(gen[1])} years) '
            f'and DNA matches ({dna[0]} cases) resolved the oldest cases, while confessions ({conf[0]}) and '
            f'witnesses or tips ({counts.get("witness", 0)}) arrived at every age.')
    desc = fit(f'What broke {n} solved cold cases: genetic genealogy {gen[0]}, DNA match {dna[0]}, confession {conf[0]}, '
               f'witness or tip {counts.get("witness", 0)}. Counts, median waits and the cases behind each method.', 158)
    return analysis_page('cold-case-resolution-methods', 'How cold cases get solved',
                         'How Cold Cases Get Solved: Resolution Methods', desc, lead, '\n'.join(sec), notes, n)


def render_analysis_index(recs, skipped):
    prefix = '../'
    url = f'{BASE_URL}/analysis/'
    n = len(recs)
    cold = [r for r in recs if r['years'] >= 2]
    med = analysis.median([r['years'] for r in cold])
    gen = sum(1 for r in recs if r['method'] == 'genealogy')
    fast = sum(1 for r in recs if r['years'] <= 1)
    cards = f'''<div class="states-grid" style="margin-top:var(--space-8)">
        <a href="./how-long-cold-cases-take-to-solve/" class="state-card">
          <div class="state-card-header"><span class="state-name">How long do cold cases take to solve?</span></div>
          <div class="state-card-meta">Years from the crime to the break for {n} resolved cases, by decade, method and type. {round(fast / n * 100)}% were broken within a year; the cases that went cold waited a median of {fmt_years(med)} years.</div>
        </a>
        <a href="./cold-case-resolution-methods/" class="state-card">
          <div class="state-card-header"><span class="state-name">How cold cases get solved</span></div>
          <div class="state-card-meta">What broke each of the {n} resolved cases: genetic genealogy ({gen}), DNA matches, confessions, witnesses and tips, with the cases behind each method.</div>
        </a>
      </div>'''
    desc = (f'How long {n} solved cold cases took and what broke them, from genetic genealogy to '
            f'confessions: original analysis computed from the case timelines.')
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Analysis', None)], prefix)}
      <h1 class="section-heading">Cold Case Analysis</h1>
      <p class="section-subtext">Findings computed from the dated timelines of the cases in this index. Each report states its rules and its limits, links every case it counts, and is recomputed whenever the data changes. Cite the page and the date shown on it.</p>
      {cards}
      <h2 class="sub-heading">Related</h2>
      <div class="hub-links"><a href="{prefix}map/">Case map</a><a href="{prefix}#statistics">US homicide clearance statistics</a><a href="{prefix}themes/">Cases by theme</a><a href="{prefix}data/cases.json">Download the dataset (JSON)</a></div>
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Analysis', url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Cold case analysis",
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"}},
    ]
    return lambda p, m: page(title=f'Cold Case Analysis: Resolution Times and Methods', desc=desc, canonical=url,
                             prefix=prefix, body=body, schema=schema, active='Analysis')


# ─────────────────────────── homepage blocks ───────────────────────────

def home_card(c):
    age = f'<span class="case-tag">Age {e(str(c["age"]))}</span>' if known(c.get('age')) else ''
    return (f'<a href="./cases/{e(c["id"])}/" class="case-card">'
            f'<div class="case-card-header">{badge(c.get("status"))}'
            f'<span class="case-card-year">{e(str(c.get("year") or ""))}</span></div>'
            f'<h3 class="case-card-name">{e(c["name"])}</h3>'
            f'<p class="case-card-summary">{e(fit(c.get("summary") or "", 120))}</p>'
            f'<div class="case-card-tags"><span class="case-tag">{e(c["_region"])}</span>'
            f'<span class="case-tag">{e(c["type"])}</span>{age}</div></a>')


def home_blocks(cases, stats, by_region, log):
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

    <figure class="viz viz-wide" data-mediavine-no-ads style="max-width:860px;margin-top:var(--space-10)">
      <div class="viz-title">Share of US homicides cleared, {years[0]['year']} to {latest['year']}</div>
      <div class="viz-sub">The clearance rate fell from {high['clearancePct']}% in {high['year']} to {low['clearancePct']}% in {low['year']} and has since recovered to {latest['clearancePct']}%. Hover or tap a year for its value.</div>
      {chart}
      <details class="table-view"><summary>Show as table</summary>
        <div class="table-wrap" data-mediavine-no-ads tabindex="0"><table class="data-table">
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
    state_html = f'''<div class="viz-group" data-mediavine-no-ads>
    <figure class="viz" data-mediavine-no-ads style="max-width:720px">
      <div class="viz-title">Homicide clearance rate by state, 1965 to 2024</div>
      <div class="viz-sub">Darker tiles cleared a smaller share of their homicides. Select a state to see its cases.</div>
      {cmap}
      {legend}
    </figure>

    <div class="table-wrap" data-mediavine-no-ads tabindex="0" role="region" aria-label="Homicides by state, scrollable table">
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
    </div>
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
    theme_chips = ''.join(
        f'<a class="browse-chip" href="./themes/{slug}/">{e(label)}<strong>{sum(1 for c in cases if c["_tags"] & tags)}</strong></a>'
        for slug, label, _h, tags, _i in THEMES)

    unsolved_recent = sorted((c for c in cases if c['_group'] == 'unsolved' and c.get('enriched')),
                             key=lambda c: (-(c.get('year') or 0), c['name']))
    featured = (unsolved_recent[:12] + [c for c in cases if c.get('enriched') and c['_group'] != 'unsolved'][:12])[:24]
    return {
        'HOME_STATS': stats_html,
        'HOME_STATE_DATA': state_html,
        'HOME_DECADES': dec_chips,
        'HOME_TYPES': type_chips,
        'HOME_THEMES': theme_chips,
        'HOME_STATUS': status_fig,
        'HOME_CARDS': '\n'.join(home_card(c) for c in sorted(cases, key=lambda c: (-(c.get('year') or 0), c['name']))[:24]),
        'HOME_FRESH': fresh_strip(log, {c['id']: c for c in cases}),
        'HOME_WATCH': str(sum(1 for c in cases if c.get('status') in WATCH_STATUSES)),
        'HOME_COUNT': f'{len(cases):,}',
        'HOME_UNSOLVED_TOTAL': f'{nat["unsolved"]:,}',
        'HOME_CLEARANCE': f'{latest["clearancePct"]}%',
    }


HOME_JS = r"""
var CASES=[],filtered=[],PAGE=24,shown=0;
var SORT={newest:function(a,b){return (b.year||0)-(a.year||0)||a.name.localeCompare(b.name)},oldest:function(a,b){return (a.year||0)-(b.year||0)||a.name.localeCompare(b.name)},name:function(a,b){return a.name.localeCompare(b.name)},added:function(a,b){return b._i-a._i}};
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
  filtered.sort(SORT[$('sortOrder').value]||SORT.newest);
  shown=PAGE;draw();
}
function fill(id,vals,fmt){var el=$(id);vals.forEach(function(v){var o=document.createElement('option');o.value=v;o.textContent=fmt?fmt(v):v;el.appendChild(o)})}
function uniq(a){return a.filter(function(v,i){return v!==''&&v!=null&&a.indexOf(v)===i}).sort()}
function start(){
  CASES.forEach(function(c,i){c._i=i});
  fill('filterType',uniq(CASES.map(function(c){return c.type})));
  fill('filterState',uniq(CASES.map(function(c){return c.state})));
  fill('filterDecade',uniq(CASES.map(function(c){return c.year?Math.floor(c.year/10)*10:null})).sort(function(a,b){return a-b}),function(v){return v+'s'});
  fill('filterStatus',uniq(CASES.map(function(c){return c.status})));
  var p=new URLSearchParams(location.search),map={state:'filterState',type:'filterType',decade:'filterDecade',status:'filterStatus',sort:'sortOrder',q:'filterSearch'},hit=false;
  Object.keys(map).forEach(function(k){var v=p.get(k);if(!v)return;var el=$(map[k]);if(el.tagName==='SELECT'&&![].some.call(el.options,function(o){return o.value===v}))return;el.value=v;hit=true});
  ['filterType','filterState','filterDecade','filterStatus','sortOrder'].forEach(function(id){$(id).addEventListener('change',apply)});
  $('filterSearch').addEventListener('input',apply);
  $('loadMore').addEventListener('click',function(){shown+=PAGE;draw()});
  $('filtersBar').hidden=false;
  apply();if(hit)$('cases').scrollIntoView();
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


def render_home(cases, stats, by_region, log):
    b = home_blocks(cases, stats, by_region, log)
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
    <div class="hero-search-wrapper" data-mediavine-no-ads>
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

<section class="fresh" aria-labelledby="freshTitle">
  <div class="fresh-box">
    <div class="fresh-head">
      <h2 class="fresh-title" id="freshTitle">Recently updated</h2>
      <nav class="fresh-links" aria-label="Updates and anniversaries">
        <a href="./updates/">All updates</a>
        <a href="./watch/">Cases to watch</a>
        <a href="./today/">On this day</a>
        <a href="./feed.xml">Atom feed</a>
      </nav>
    </div>
    <ul class="fresh-list">{b['HOME_FRESH']}</ul>
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
    <p class="section-subtext" style="margin-bottom: var(--space-6);">The most recent cases are listed first. Filter the {n} documented cases by type, state or country, decade and status, change the sort order, or browse by <a href="./states/">state</a>, <a href="./types/">type</a> or <a href="./decades/">decade</a>.</p>

    <div class="filters-bar" id="filtersBar" hidden data-mediavine-no-ads>
      <div class="filter-group"><label for="filterType">Type</label><select class="filter-select" id="filterType"><option value="">All types</option></select></div>
      <div class="filter-group"><label for="filterState">State or country</label><select class="filter-select" id="filterState"><option value="">All</option></select></div>
      <div class="filter-group"><label for="filterDecade">Decade</label><select class="filter-select" id="filterDecade"><option value="">All decades</option></select></div>
      <div class="filter-group"><label for="filterStatus">Status</label><select class="filter-select" id="filterStatus"><option value="">All statuses</option></select></div>
      <div class="filter-group"><label for="sortOrder">Sort</label><select class="filter-select" id="sortOrder"><option value="newest">Newest first</option><option value="oldest">Oldest first</option><option value="name">Name A to Z</option><option value="added">Recently added</option></select></div>
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

    <h3 class="browse-subheading">By theme</h3>
    <div class="browse-chips">{b['HOME_THEMES']}</div>

    <h3 class="browse-subheading">Explore</h3>
    <div class="browse-chips"><a class="browse-chip" href="./map/">Case map</a><a class="browse-chip" href="./cities/">Cases by city</a><a class="browse-chip" href="./analysis/">Analysis: how long cold cases take and what solves them</a></div>

    <h3 class="browse-subheading">Keep up to date</h3>
    <div class="browse-chips"><a class="browse-chip" href="./updates/">Recent changes</a><a class="browse-chip" href="./watch/">Cases to watch<strong>{b['HOME_WATCH']}</strong></a><a class="browse-chip" href="./today/">On this day</a><a class="browse-chip" href="./month/">Anniversaries by month</a><a class="browse-chip" href="./feed.xml">Atom feed</a></div>
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
         "license": "https://creativecommons.org/licenses/by-nc/4.0/",
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
        desc=(f'What {SITE} collects: no accounts or forms; Google Analytics and Mediavine advertising '
              'cookies, with opt-out links; how to contact us about case information.'),
        canonical=f'{BASE_URL}/privacy/', prefix='../', body=privacy, schema=[],
        robots='noindex,follow'), False)

    nf = f'<div class="notfound-wrap" style="min-height:60vh">{content("404.html")}</div>'
    out['404.html'] = (lambda p, m: page(
        title=f'Page Not Found | {SITE}', desc='The page you were looking for could not be found.',
        canonical=f'{BASE_URL}/', prefix='/', body=nf, schema=[], robots='noindex'), False)
    return out



# ─────────────────────────── freshness: updates, watch list, anniversaries ───────────────────────────

CHANGELOG_FILE = os.path.join(ROOT, 'data', 'changelog.json')
CASE_STATE_FILE = os.path.join(ROOT, 'data', 'case-state.json')
WATCH_STATUSES = ('Pending Trial', 'Arrest Made', 'Wanted')
KIND_LABEL = {'added': 'New case', 'status': 'Status change', 'extended': 'Timeline',
              'revised': 'Revised', 'removed': 'Removed'}
MONTHS = changelog.MONTHS


def short_date(iso):
    """'2026-10-27' -> 'Oct 27, 2026'."""
    y, m, d = iso.split('-')
    return f'{MONTHS[int(m) - 1][:3]} {int(d)}, {y}'


def count_label(kind, n):
    return {'added': plural(n, 'case added', 'cases added'),
            'status': plural(n, 'status change'),
            'extended': plural(n, 'timeline extended', 'timelines extended'),
            'revised': plural(n, 'entry revised', 'entries revised'),
            'removed': plural(n, 'entry removed', 'entries removed')}[kind]


def change_text(x, by_id, limit=150):
    """One line saying what changed, as HTML."""
    c = by_id.get(x['id'])
    kind = x['kind']
    if kind == 'added':
        return e(fit(c.get('summary') or '', limit)) if c else ''
    if kind == 'status':
        return (f'{e(x["from"])}<span class="change-arrow" aria-hidden="true">→</span>'
                f'<span class="sr-only"> to </span>{e(x["to"])}')
    if kind == 'extended':
        n = x.get('count', 1)
        when = changelog.human(changelog.parse_date(x.get('when'))) or x.get('when') or ''
        lead = f'{plural(n, "new event")}, latest ' if n > 1 else ''
        return e(f'{lead}{when}: {fit(x.get("event") or "", limit)}')
    if kind == 'revised':
        return e('Revised: ' + ', '.join(x.get('fields') or []))
    return ''


def case_link(x, by_id, prefix):
    if x['id'] in by_id:
        return f'<a href="{prefix}cases/{e(x["id"])}/">{e(x["name"])}</a>'
    return e(x['name'])


def change_item(x, by_id, prefix):
    c = by_id.get(x['id'])
    meta = (f' <span class="change-meta">{e(str(c.get("year") or ""))}, {e(c["_region"])}</span>'
            if c else '')
    text = change_text(x, by_id)
    text = f'<div class="change-text">{text}</div>' if text else ''
    return (f'<li class="change change-{x["kind"]}"><span class="change-kind">{KIND_LABEL[x["kind"]]}</span>'
            f'<div><div class="change-head">{case_link(x, by_id, prefix)}{meta}</div>{text}</div></li>')


def render_updates(cases, log):
    prefix = '../'
    url = f'{BASE_URL}/updates/'
    by_id = {c['id']: c for c in cases}
    by_date = defaultdict(list)
    for x in log:
        by_date[x['date']].append(x)
    dates = sorted(by_date, reverse=True)
    cutoff = (TODAY - datetime.timedelta(days=90)).isoformat()
    shown = [d for i, d in enumerate(dates) if d >= cutoff or i < 3]
    limit, names_limit = 25, 100
    sections, totals = [], Counter()
    for d in shown:
        kinds = defaultdict(list)
        for x in by_date[d]:
            kinds[x['kind']].append(x)
        counts, parts = [], []
        for kind in changelog.KINDS:
            items = kinds.get(kind)
            if not items:
                continue
            totals[kind] += len(items)
            counts.append(count_label(kind, len(items)))
            if kind in ('revised', 'removed'):
                names = ', '.join(case_link(x, by_id, prefix) for x in items[:names_limit])
                if len(items) > names_limit:
                    names += f' and {len(items) - names_limit} more'
                what = ('re-checked against their sources and revised' if kind == 'revised'
                        else 'removed from the index, as duplicates of another entry or as out of scope')
                parts.append(f'<details class="change-fold"><summary>{count_label(kind, len(items))}: '
                             f'show which</summary><p class="change-names">{plural(len(items), "entry", "entries")} '
                             f'{what}: {names}.</p></details>')
            else:
                lis = ''.join(change_item(x, by_id, prefix) for x in items[:limit])
                more = ''
                if len(items) > limit:
                    rest = ', '.join(case_link(x, by_id, prefix) for x in items[limit:names_limit])
                    if len(items) > names_limit:
                        rest += f' and {len(items) - names_limit} more'
                    more = f'<li class="change-more">And {len(items) - limit} more that day: {rest}.</li>'
                parts.append(f'<ul class="change-list">{lis}{more}</ul>')
        sections.append(f'''<section class="change-day" aria-labelledby="d-{d}">
        <h2 class="sub-heading" id="d-{d}">{changelog.human(changelog.parse_date(d))}</h2>
        <p class="change-summary">{", ".join(counts)}.</p>
        {''.join(parts)}
      </section>''')
    title = 'Case Updates: Recent Changes to the Index'
    desc = fit(f'What changed on {SITE} in the last three months: {totals["added"]} cases added, '
               f'{totals["status"]} status changes and {totals["extended"]} timelines extended, '
               f'listed by day. Also available as an Atom feed.', 158)
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Updates', None)], prefix)}
      <h1 class="section-heading">Recent Changes to the Index</h1>
      <p class="section-subtext">Every build compares each case with its previous version and records what changed: cases added or removed, status changes, timelines that gained events, and entries revised after a check against their sources. Wording fixes and site-wide template changes are not listed. A status changes only when a cited source reports the development, and people who have not been convicted remain presumed innocent.</p>
      <p class="section-subtext" style="margin-top:var(--space-3)">Follow the <a href="{prefix}feed.xml">Atom feed</a> for new cases, status changes and timeline updates. See also <a href="{prefix}watch/">cases to watch</a>, whose status is expected to change, and <a href="{prefix}today/">on this day</a>.</p>
      {''.join(sections)}
      <p class="section-subtext" style="margin-top:var(--space-8)">This page shows the most recent changes. The full record since launch is published as <a href="{prefix}data/changelog.json">changelog.json</a>.</p>
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Updates', url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Recent changes to the index",
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"}},
    ]
    return lambda p, m: page(title=title, desc=desc, canonical=url, prefix=prefix, body=body, schema=schema)


def write_feed(log, cases):
    """Atom feed of the latest additions, status changes and timeline updates."""
    by_id = {c['id']: c for c in cases}
    items = [x for x in reversed(log) if x['kind'] in changelog.FEED_KINDS and x['id'] in by_id][:50]

    def stamp(d):
        return f'{d}T00:00:00Z'
    entries = []
    for x in items:
        c = by_id[x['id']]
        link = f'{BASE_URL}/cases/{x["id"]}/'
        summary = f'<p>{e(fit(c.get("summary") or "", 300))}</p>'
        if x['kind'] == 'added':
            title = f'New case: {x["name"]} ({c.get("year")}, {c["_region"]})'
            body = summary
        elif x['kind'] == 'status':
            title = f'Status change: {x["name"]}, {x["from"]} to {x["to"]}'
            body = (f'<p>Status changed from {e(x["from"])} to {e(x["to"])}. '
                    f'{e(STATUS_EXPLAIN.get(x["to"], ""))}</p>{summary}')
        else:
            title = f'Timeline updated: {x["name"]}'
            body = f'<p>{change_text(x, by_id, 300)}</p>{summary}'
        entries.append(f'''  <entry>
    <title>{e(title)}</title>
    <link rel="alternate" type="text/html" href="{link}"/>
    <id>tag:coldcaseindex.com,{x['date']}:{x['id']}/{x['kind']}</id>
    <published>{stamp(x['date'])}</published>
    <updated>{stamp(x['date'])}</updated>
    <category term="{x['kind']}"/>
    <content type="html">{e(body)}</content>
  </entry>''')
    updated = stamp(items[0]['date']) if items else stamp(TODAY.isoformat())
    xml = f'''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>{SITE} updates</title>
  <subtitle>New cases, status changes and timeline updates in the cold case index</subtitle>
  <link rel="self" type="application/atom+xml" href="{BASE_URL}/feed.xml"/>
  <link rel="alternate" type="text/html" href="{BASE_URL}/updates/"/>
  <id>{BASE_URL}/feed.xml</id>
  <updated>{updated}</updated>
  <author><name>{SITE}</name><uri>{BASE_URL}/</uri></author>
  <rights>CC BY-NC 4.0</rights>
{chr(10).join(entries)}
</feed>
'''
    with open(os.path.join(ROOT, 'feed.xml'), 'w', encoding='utf-8') as f:
        f.write(xml)
    return len(items)


def render_watch(cases):
    prefix = '../'
    url = f'{BASE_URL}/watch/'
    rows = []
    for c in cases:
        if c.get('status') not in WATCH_STATUSES:
            continue
        evs = case_events(c)
        rows.append((c, evs[-1] if evs else ('', ''), changelog.next_date(evs, TODAY)))

    def last_day(r):
        return changelog.to_date(changelog.parse_date(r[1][0])) or datetime.date.min
    upcoming = sorted((r for r in rows if r[2] and not r[2]['past']),
                      key=lambda r: changelog.to_date(r[2]['when']))
    passed = sorted((r for r in rows if r[2] and r[2]['past']),
                    key=lambda r: changelog.to_date(r[2]['when']))
    nodate = sorted((r for r in rows if not r[2]), key=lambda r: (-last_day(r).toordinal(), r[0]['name']))

    def table(group, caption, empty):
        if not group:
            return f'<p class="section-subtext">{empty}</p>'
        trs = []
        for c, (ld, lt), nd in group:
            when = changelog.human(changelog.parse_date(ld)) or ld
            if nd:
                nxt = f'<span class="watch-date">{e(changelog.human(nd["when"]))}</span>'
                if nd['past']:
                    nxt += '<span class="watch-flag">Date has passed; outcome not yet recorded</span>'
                elif nd['source'] == 'mention':
                    nxt += '<span class="watch-note">As given in the latest entry</span>'
            else:
                nxt = '<span class="watch-note">No date recorded</span>'
            trs.append(f'''<tr>
            <td class="watch-case"><a href="{prefix}cases/{e(c["id"])}/">{e(c["name"])}</a>
              <span class="watch-sub">{e(c["_place"] or c["_region"])}, {e(str(c.get("year") or ""))} · {e(c["type"])}</span>
              <span class="watch-sub">{badge(c.get("status"), small=True)}</span></td>
            <td><span class="watch-when">{e(when)}</span>{e(fit(lt, 170))}</td>
            <td>{nxt}</td>
          </tr>''')
        return f'''<div class="table-wrap" data-mediavine-no-ads tabindex="0" role="region" aria-label="{e(caption)}">
        <table class="data-table watch-table">
          <caption>{e(caption)}</caption>
          <thead><tr><th scope="col">Case</th><th scope="col">Last recorded development</th><th scope="col">Next date</th></tr></thead>
          <tbody>{''.join(trs)}</tbody>
        </table>
      </div>'''

    by_status = Counter(c['status'] for c, _, _ in rows)
    n = len(rows)
    pt, w, a = by_status['Pending Trial'], by_status['Wanted'], by_status['Arrest Made']
    title = 'Cases to Watch: Pending Trials and Wanted Suspects'
    desc = fit(f'{n} cases whose status can still change: {pt} awaiting trial, {w} with a wanted suspect '
               f'and {a} with an arrest made. Last recorded development and next court date for each.', 158)
    explain = ''.join(f'<dt>{e(s)}</dt><dd>{e(STATUS_EXPLAIN[s])}</dd>' for s in WATCH_STATUSES)
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Cases to watch', None)], prefix)}
      <h1 class="section-heading">Cases to Watch</h1>
      <p class="section-subtext">{plural(n, 'case')} in the index with a status that is expected to change: a trial or hearing is pending, a suspect has been charged and arrested, or a charged suspect is a fugitive. Each row shows the last development recorded here and, where the entry gives one, the next scheduled date. Dates that have passed are flagged until the outcome is recorded. Changes appear in <a href="{prefix}updates/">recent updates</a> and the <a href="{prefix}feed.xml">Atom feed</a>.</p>
      <dl class="status-dl">{explain}</dl>

      <h2 class="sub-heading">Upcoming dates</h2>
      {table(upcoming, 'Cases with a scheduled date still ahead, soonest first.', 'No upcoming dates are recorded.')}

      <h2 class="sub-heading">Dates that have passed</h2>
      {table(passed, 'The last scheduled date is in the past and the outcome has not yet been recorded here.', 'Every recorded date is still ahead.')}

      <h2 class="sub-heading">No date recorded</h2>
      {table(nodate, 'Mostly fugitive cases, where there is no court date to wait for. Most recently updated first.', 'Every case has a date.')}

      <p class="section-subtext" style="margin-top:var(--space-8)">Nothing here states or implies that an accused person is guilty. A conviction is recorded only when a court has entered one; an acquittal, dismissal or overturned conviction is recorded as precisely as the sources allow.</p>
    </div>
  </section>
'''
    ordered = [r[0] for r in upcoming + passed + nodate]
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Cases to watch', url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Cases to watch",
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"},
         "mainEntity": item_list_ld(ordered)},
    ]
    return lambda p, m: page(title=title, desc=desc, canonical=url, prefix=prefix, body=body, schema=schema)


def anniversary_index(cases):
    """(month, day) -> cases whose incident began that day, and
    (month, day) -> [(year, case, event)] for other day-precise timeline events."""
    inc, evs = defaultdict(list), defaultdict(list)
    for c in cases:
        own = changelog.parse_date(c.get('date'))
        if own and own[1] and own[2]:
            inc[(own[1], own[2])].append(c)
        for d, text in case_events(c):
            q = changelog.parse_date(d)
            if not q or not q[1] or not q[2] or q == own:
                continue
            day = changelog.to_date(q)
            if not day or day > TODAY:
                continue
            evs[(q[1], q[2])].append((q[0], c, text))
    for v in inc.values():
        v.sort(key=lambda c: (c.get('year') or 0, c['name']))
    for v in evs.values():
        v.sort(key=lambda t: (t[0], t[1]['name']))
    return inc, evs


def anniv_case_row(c, prefix):
    return (f'<li class="anniv-item"><span class="anniv-year">{e(str(c.get("year") or ""))}</span>'
            f'<div><a href="{prefix}cases/{e(c["id"])}/">{e(c["name"])}</a>'
            f'<span class="anniv-meta">{e(c["_place"] or c["_region"])} · {e(c["type"])}</span>'
            f'{badge(c.get("status"), small=True)}'
            f'<div class="anniv-text">{e(fit(c.get("summary") or "", 130))}</div></div></li>')


def anniv_event_row(year, c, text, prefix, compact=False):
    meta = '' if compact else f'<span class="anniv-meta">{e(c["_place"] or c["_region"])}</span>'
    return (f'<li class="anniv-item"><span class="anniv-year">{year}</span>'
            f'<div><a href="{prefix}cases/{e(c["id"])}/">{e(c["name"])}</a>{meta}'
            f'<div class="anniv-text">{e(fit(text, 110 if compact else 170))}</div></div></li>')


def render_today(inc, evs):
    prefix = '../'
    url = f'{BASE_URL}/today/'
    m, d = TODAY.month, TODAY.day
    month, label = MONTHS[m - 1], f'{MONTHS[m - 1]} {TODAY.day}'
    today_cases, today_events = inc.get((m, d), []), evs.get((m, d), [])
    n, k = len(today_cases), len(today_events)
    title = f'On This Day, {label}: Cold Case Anniversaries'
    if n:
        desc = (f'{plural(n, "documented case")} began on {label}, and {k} dated developments in other '
                f'cases fell on this date. Rebuilt every day from the {SITE} database.')
    else:
        desc = (f'No documented case in the index began on {label}, but {k} dated developments in other '
                f'cases fell on this date. Rebuilt every day from the {SITE} database.')
    desc = fit(desc, 158)
    if today_cases:
        cases_html = f'<div class="cases-grid">{"".join(case_card(c, prefix, place="region") for c in today_cases)}</div>'
    else:
        cases_html = (f'<p class="anniv-empty">No case in the index has an incident date of {label}. '
                      f'Browse <a href="{prefix}month/{month.lower()}/">every {month} anniversary</a> instead.</p>')
    events_html = (f'<ul class="anniv-list">{"".join(anniv_event_row(y, c, t, prefix) for y, c, t in today_events)}</ul>'
                   if today_events else '<p class="section-subtext">No other dated developments fall on this date.</p>')
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Anniversaries', 'month/'), (label, None)], prefix)}
      <h1 class="section-heading">On This Day: {label}</h1>
      <p class="section-subtext">Cases in the index whose incident or disappearance happened on {label}, in any year, followed by other dated developments recorded on this date: arrests, verdicts, identifications and discoveries. This page is rebuilt daily. See all of <a href="{prefix}month/{month.lower()}/">{month}</a>, browse <a href="{prefix}month/">by month</a>, or follow <a href="{prefix}updates/">recent updates</a>.</p>

      <h2 class="sub-heading">Cases that began on {label}</h2>
      {cases_html}

      <h2 class="sub-heading">Also on this date</h2>
      {events_html}
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Anniversaries', f'{BASE_URL}/month/'), (label, url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": f'On this day: {label}',
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"},
         "mainEntity": item_list_ld(today_cases)},
    ]
    return lambda p, m: page(title=title, desc=desc, canonical=url, prefix=prefix, body=body, schema=schema)


def render_month(month, inc, evs, month_counts):
    prefix = '../../'
    name = MONTHS[month - 1]
    url = f'{BASE_URL}/month/{name.lower()}/'
    days = sorted(d for (mo, d) in inc if mo == month)
    month_cases = [c for d in days for c in inc[(month, d)]]
    ev_days = sorted(d for (mo, d) in evs if mo == month)
    n_ev = sum(len(evs[(month, d)]) for d in ev_days)
    n = len(month_cases)
    unsolved = sum(1 for c in month_cases if c['_group'] == 'unsolved')
    title = f'{name} Cold Case Anniversaries: {n} Cases'
    desc = fit(f'{plural(n, "documented case")} began in {name}, listed day by day, {unsolved} of them still '
               f'unsolved, plus {n_ev} dated developments in other cases that month. Status, place and year for each.', 158)
    day_html = ''.join(
        f'<h2 class="anniv-day" id="d{d}">{name} {d}</h2><ul class="anniv-list">'
        + ''.join(anniv_case_row(c, prefix) for c in inc[(month, d)]) + '</ul>' for d in days)
    ev_html = ''.join(
        f'<h3 class="anniv-day">{name} {d}</h3><ul class="anniv-list">'
        + ''.join(anniv_event_row(y, c, t, prefix, compact=True) for y, c, t in evs[(month, d)]) + '</ul>' for d in ev_days)
    sib = []
    for i, mname in enumerate(MONTHS):
        cur = ' aria-current="page"' if i + 1 == month else ''
        sib.append(f'<a href="../{mname.lower()}/"{cur}><strong>{month_counts[i + 1]}</strong> {mname}</a>')
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Anniversaries', 'month/'), (name, None)], prefix)}
      <h1 class="section-heading">{name} in Cold Case History</h1>
      <p class="section-subtext">{plural(n, 'documented case')} began in {name}, listed by the day of the incident or disappearance (for a series, the first incident). {unsolved} {'is' if unsolved == 1 else 'are'} still unsolved. Further down, {n_ev} other dated developments recorded in {name}: arrests, verdicts, identifications and discoveries. For today's date, see <a href="{prefix}today/">on this day</a>.</p>
      {day_html or '<p class="anniv-empty">No case in the index has a full incident date in this month.</p>'}

      <h2 class="sub-heading">Other developments recorded in {name}</h2>
      <details class="change-fold"><summary>Show {plural(n_ev, 'dated development')}</summary>{ev_html}</details>

      <h2 class="sub-heading">Other months</h2>
      <div class="hub-links">{''.join(sib)}</div>
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Anniversaries', f'{BASE_URL}/month/'), (name, url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": f'{name} in cold case history',
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"},
         "mainEntity": item_list_ld(month_cases)},
    ]
    return lambda p, m: page(title=title, desc=desc, canonical=url, prefix=prefix, body=body, schema=schema)


def render_month_index(month_counts, unsolved_counts):
    prefix = '../'
    url = f'{BASE_URL}/month/'
    total = sum(month_counts.values())
    data = [(m[:3], month_counts[i + 1]) for i, m in enumerate(MONTHS)]
    links = {m[:3]: f'./{m.lower()}/' for m in MONTHS}
    chart = viz.columns(data, links=links, label='Cases by month of incident')
    mx = max(month_counts.values()) or 1
    cards = ''.join(f'''<a href="./{m.lower()}/" class="state-card">
            <div class="state-card-header"><span class="state-name">{m}</span><span class="state-count-badge">{month_counts[i + 1]}</span></div>
            <div class="state-bar-wrapper"><div class="state-bar" style="width:{month_counts[i + 1] / mx * 100:.1f}%"></div></div>
            <div class="state-card-meta">{plural(month_counts[i + 1], 'case')}, {unsolved_counts[i + 1]} unsolved</div>
          </a>''' for i, m in enumerate(MONTHS))
    title = f'Cold Case Anniversaries by Month | {SITE}'
    desc = fit(f'{total} documented cases with a known incident date, grouped by the month they began. '
               f'Pick a month for a day-by-day list, or see which cases began on today\'s date.', 158)
    body = f'''
  <section class="section">
    <div class="section-inner">
      {breadcrumb_html([('Home', ''), ('Anniversaries', None)], prefix)}
      <h1 class="section-heading">Cold Case Anniversaries by Month</h1>
      <p class="section-subtext">{total} of the cases in the index have a full incident date. They are grouped here by the month in which the crime or disappearance began, with a day-by-day list for each month and the other dated developments recorded that month. <a href="{prefix}today/">On this day</a> shows the cases and developments that fall on today's date; it is rebuilt daily.</p>
      <figure class="viz" data-mediavine-no-ads><div class="viz-title">Cases by month of incident</div>
        <div class="viz-sub">Select a column to open that month.</div>{chart}</figure>
      <div class="states-grid" style="margin-top:var(--space-8)">{cards}</div>
    </div>
  </section>
'''
    schema = [
        breadcrumb_ld([('Home', f'{BASE_URL}/'), ('Anniversaries', url)]),
        {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Cold case anniversaries by month",
         "description": desc, "url": url, "inLanguage": "en-US",
         "isPartOf": {"@type": "WebSite", "name": SITE, "url": f"{BASE_URL}/"}},
    ]
    return lambda p, m: page(title=title, desc=desc, canonical=url, prefix=prefix, body=body, schema=schema)


def fresh_items(log, by_id, limit=6):
    """Newest additions, status changes and timeline updates, one per case."""
    seen, items = set(), []
    for x in reversed(log):
        if x['kind'] not in changelog.FEED_KINDS or x['id'] not in by_id or x['id'] in seen:
            continue
        seen.add(x['id'])
        items.append(x)
        if len(items) == limit:
            break
    return items


def fresh_strip(log, by_id):
    lis = []
    for x in fresh_items(log, by_id):
        c = by_id[x['id']]
        if x['kind'] == 'added':
            detail = f'{e(str(c.get("year") or ""))}, {e(c["_region"])}. {e(fit(c.get("summary") or "", 90))}'
        elif x['kind'] == 'status':
            detail = change_text(x, by_id)
        else:
            detail = e(fit(x.get('event') or '', 110))
        lis.append(f'<li class="fresh-item"><span class="fresh-kind kind-{x["kind"]}">{KIND_LABEL[x["kind"]]}</span>'
                   f'<a href="./cases/{e(x["id"])}/">{e(x["name"])}</a>'
                   f'<time datetime="{x["date"]}">{short_date(x["date"])}</time>'
                   f'<span class="fresh-detail">{detail}</span></li>')
    return ''.join(lis)


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
             'age': c.get('age'), 'summary': fit(c.get('summary') or '', 120)} for c in cases]
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
    serial_killers.init(sys.modules[__name__])
    serial_killers.load(cases)
    with open(STATS_FILE, encoding='utf-8') as f:
        stats = json.load(f)
    pages = Pages()
    log = changelog.track(cases, TODAY.isoformat(), CASE_STATE_FILE, CHANGELOG_FILE)
    print(f'Loaded {len(cases)} cases, {len(log)} changelog entries')

    by_region = defaultdict(list)
    for c in cases:
        by_region[c['_region']].append(c)
    region_counts = {r: len(v) for r, v in by_region.items()}
    all_regions = sorted(((r, len(v)) for r, v in by_region.items()), key=lambda rv: rv[0])
    state_links = {viz.STATE_ABBR[r]: f'../../states/{slugify(r)}/' for r in by_region if r in US_STATES}
    CITY_HUBS.clear()
    CITY_HUBS.update({k: city_slug(*k) for k in city_groups(cases)})
    assert len(set(CITY_HUBS.values())) == len(CITY_HUBS), 'city slugs collide'

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
    # also create redirect stubs for redirects.json entries with no on-disk directory yet
    for slug, target in sorted(redirects.items()):
        if slug in live_cases:
            continue
        full = os.path.join(cdir, slug)
        if os.path.isdir(full):
            continue                     # already handled above
        if target and target.startswith('/'):
            os.makedirs(full, exist_ok=True)
            with open(os.path.join(full, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(redirect_stub(f'{BASE_URL}{target}'))
            stubs += 1
            continue
        dest, hops = target, 0
        while dest and dest not in live_cases and hops < 5:
            dest, hops = redirects.get(dest), hops + 1
        if dest in live_cases:
            os.makedirs(full, exist_ok=True)
            with open(os.path.join(full, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(redirect_stub(f'{BASE_URL}/cases/{dest}/'))
            stubs += 1
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
    moved['washington-dc'] = 'district-of-columbia'
    moved['chiriquí-province'] = 'chiriqui-province'    # earlier builds kept accents in slugs
    moved['isère'] = 'isere'
    sdir = os.path.join(ROOT, 'states')
    # region pages that were deleted outright: recreate them as stubs so old links don't 404
    for d in ('washington-dc', 'multiple', 'chiriquí-province', 'isère'):
        if d not in live_regions:
            os.makedirs(os.path.join(sdir, d), exist_ok=True)
    stubs = 0
    for d in sorted(os.listdir(sdir)):
        if os.path.isdir(os.path.join(sdir, d)) and d not in live_regions:
            target = moved.get(d)
            url = f'{BASE_URL}/states/{target}/' if target else f'{BASE_URL}/states/'
            with open(os.path.join(sdir, d, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(redirect_stub(url))
            stubs += 1
    print(f'Wrote {len(all_regions)} region pages, {stubs} redirect stubs')

    # serial killer profiles, state pages, lists, timeline, statistics and answer pages
    print(serial_killers.write_all(pages, cases, state_links))

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
        links = ''
        if t == 'Serial Killer Victims' and serial_killers.PROFILES:
            links = (f'<div class="hub-links"><a href="../../serial-killers/">Serial killer profiles '
                     f'({len(serial_killers.PROFILES)})</a><a href="../../serial-killers/lists/">Serial killer lists</a></div>')
        render, indexable = render_hub('types', slugify(label), label, v, sib_t, e(intro), label, links=links)
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
        links = ''
        if any(p['_decade'] == d for p in serial_killers.PROFILES):
            links = f'<div class="hub-links"><a href="../../serial-killers/timeline/#{label}">Serial killers of the {label}</a></div>'
        render, indexable = render_hub('decades', label, label, v, sib_d, e(intro), f'Cold Cases of the {label}', links=links)
        pages.write(f'decades/{label}/index.html', render, indexable)
    pages.write('decades/index.html', render_hub_index('decades', d_entries, len(cases)), True)

    # theme hubs
    th = [(slug, label, heading, tags, intro, [c for c in cases if c['_tags'] & tags])
          for slug, label, heading, tags, intro in THEMES]
    th_entries = sorted(((slug, label, len(v), sum(1 for c in v if c['_group'] == 'unsolved'), fit(intro, 110))
                         for slug, label, _h, _t, intro, v in th), key=lambda x: -x[2])
    sib_th = [(s, l, n) for s, l, n, _, _ in th_entries]
    for slug, label, heading, tags, intro, v in th:
        uns = sum(1 for c in v if c['_group'] == 'unsolved')
        full = (f'{intro} {SITE} lists {plural(len(v), "case")} on this theme, of which {uns} '
                f'{"is" if uns == 1 else "are"} recorded as unsolved.')
        render, indexable = render_hub('themes', slug, label, v, sib_th, e(full), heading)
        pages.write(f'themes/{slug}/index.html', render, indexable)
    in_theme = len({c['id'] for *_rest, v in th for c in v})
    pages.write('themes/index.html', render_hub_index('themes', th_entries, in_theme), True)

    # city hubs: every city with two or more cases, indexable from five
    groups = city_groups(cases)
    ct_entries = sorted(((CITY_HUBS[k], f'{k[0]}, {viz.STATE_ABBR.get(k[1], k[1])}', len(v),
                          sum(1 for c in v if c['_group'] == 'unsolved'), '') for k, v in groups.items()),
                        key=lambda x: (-x[2], x[1]))
    sib_ct = [(s, l, n) for s, l, n, _, _ in ct_entries if n >= 5]
    for k, v in groups.items():
        city, region = k
        slug = CITY_HUBS[k]
        uns = sum(1 for c in v if c['_group'] == 'unsolved')
        ordered = sorted(v, key=lambda c: (-(c.get('year') or 0), c['name']))
        yrs = sorted(c['year'] for c in v if c.get('year'))
        span = str(yrs[0]) if yrs[0] == yrs[-1] else f'{yrs[0]} to {yrs[-1]}'
        intro = (f'{SITE} documents {plural(len(v), "case")} in {e(city)}, {e(region)}, dated {span}. '
                 f'{uns} {"is" if uns == 1 else "are"} recorded as unsolved. The earliest is '
                 f'<a href="../../cases/{ordered[-1]["id"]}/">{e(ordered[-1]["name"])}</a> ({ordered[-1].get("year")}) '
                 f'and the most recent is <a href="../../cases/{ordered[0]["id"]}/">{e(ordered[0]["name"])}</a> ({ordered[0].get("year")}).')
        links = (f'<div class="hub-links"><a href="../../states/{slugify(region)}/">All {e(region)} cases</a>'
                 + (f'<a href="../../map/?city={slug}">Show on the map</a>' if region in US_STATES else '')
                 + '</div>')
        sib = sib_ct if any(s == slug for s, *_ in sib_ct) else sib_ct + [(slug, f'{city}, {viz.STATE_ABBR.get(region, region)}', len(v))]
        render, indexable = render_hub('cities', slug, city, v, sib, intro, f'Cold Cases in {city}, {region}',
                                       links=links, min_index=5)
        pages.write(f'cities/{slug}/index.html', render, indexable)
    pages.write('cities/index.html', render_hub_index('cities', ct_entries, sum(len(v) for v in groups.values())), True)
    print(f'Wrote {len(th)} theme hubs and {len(groups)} city hubs ({len(sib_ct)} indexable)')

    # hubs whose type, decade, theme or city no longer has any cases: redirect to the hub index
    hub_stubs = 0
    for kind, live in (('types', {s for s, *_ in t_entries}), ('decades', {s for s, *_ in d_entries}),
                       ('themes', {s for s, *_ in th_entries}), ('cities', {s for s, *_ in ct_entries})):
        hdir = os.path.join(ROOT, kind)
        for d in sorted(os.listdir(hdir)):
            if os.path.isdir(os.path.join(hdir, d)) and d not in live:
                with open(os.path.join(hdir, d, 'index.html'), 'w', encoding='utf-8') as f:
                    f.write(redirect_stub(f'{BASE_URL}/{kind}/'))
                hub_stubs += 1
    print(f'Wrote {len(by_type)} type hubs and {len(by_dec)} decade hubs, {hub_stubs} redirect stubs')

    # short URLs that were never generated but are requested anyway (/1990s/, /cases/):
    # redirect them to the real hub so they stop returning 404
    short_stubs = 0
    for label, *_ in d_entries:
        ldir = os.path.join(ROOT, label)
        os.makedirs(ldir, exist_ok=True)
        with open(os.path.join(ldir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(redirect_stub(f'{BASE_URL}/decades/{label}/'))
        short_stubs += 1
    with open(os.path.join(ROOT, 'cases', 'index.html'), 'w', encoding='utf-8') as f:
        f.write(redirect_stub(f'{BASE_URL}/'))
    short_stubs += 1
    print(f'Wrote {short_stubs} short-URL redirect stubs')

    # updates, watch list, anniversaries, feed
    inc, evs = anniversary_index(cases)
    month_counts, unsolved_counts = Counter(), Counter()
    for (mo, _d), v in inc.items():
        month_counts[mo] += len(v)
        unsolved_counts[mo] += sum(1 for c in v if c['_group'] == 'unsolved')
    pages.write('updates/index.html', render_updates(cases, log), True)
    pages.write('watch/index.html', render_watch(cases), True)
    pages.write('today/index.html', render_today(inc, evs), True)
    for mo in range(1, 13):
        pages.write(f'month/{MONTHS[mo - 1].lower()}/index.html', render_month(mo, inc, evs, month_counts), True)
    pages.write('month/index.html', render_month_index(month_counts, unsolved_counts), True)
    n_feed = write_feed(log, cases)
    print(f'Wrote updates, watch, today and 12 month pages; feed.xml with {n_feed} entries')

    # map and analysis
    pages.write('map/index.html', render_map(cases, len(CITY_HUBS)), True)
    recs, skipped = analysis.compute(cases)
    gen_cases = [c for c in cases if c['_tags'] & THEMES[0][3]]
    pages.write('analysis/index.html', render_analysis_index(recs, skipped), True)
    pages.write('analysis/how-long-cold-cases-take-to-solve/index.html', render_analysis_time(recs, skipped), True)
    pages.write('analysis/cold-case-resolution-methods/index.html',
                render_analysis_methods(recs, skipped, gen_cases), True)
    print(f'Analysis: {len(recs)} resolved cases classified, {len(skipped)} without a dated break')

    # homepage + data
    write_search_index(cases)
    with open(os.path.join(ROOT, 'data', 'serial-killers-index.json'), 'w', encoding='utf-8') as f:
        json.dump(serial_killers.search_rows(serial_killers.PROFILES), f, ensure_ascii=False, separators=(',', ':'))
    pages.write('index.html', render_home(cases, stats, by_region, log), True)
    update_counts(len(cases))

    for path, (render, indexable) in render_static(cases, stats).items():
        pages.write(path, render, indexable)
    n = write_sitemap(pages, [])
    pages.save()
    print(f'Sitemap: {n} URLs')


if __name__ == '__main__':
    main()
