#!/usr/bin/env python3
"""
ColdCaseIndex — State Landing Page Generator
Reads data/cases.json and generates per-state pages at states/{slug}/index.html
Run from the project root: python3 scripts/generate_state_pages.py
"""

import json
import os
import re
from collections import Counter, defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_FILE = os.path.join(ROOT_DIR, 'data', 'cases.json')
STATES_DIR = os.path.join(ROOT_DIR, 'states')

BASE_URL = 'https://coldcaseindex.com'

GA_SNIPPET = '''<script async src="https://www.googletagmanager.com/gtag/js?id=G-9D333CYZNN"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag("js",new Date());gtag("config","G-9D333CYZNN");</script>
<script>try{document.documentElement.setAttribute('data-theme',localStorage.getItem('cci-theme')||'dark')}catch(e){}</script>'''

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@600;700&display=swap" rel="stylesheet">'''


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def status_badge_class(status):
    if not status:
        return 'badge-unsolved'
    s = status.lower()
    if 'conviction' in s and 'no conviction' not in s:
        return 'badge-conviction'
    if 'arrest' in s:
        return 'badge-arrest'
    if 'partially' in s:
        return 'badge-partial'
    return 'badge-unsolved'


SHARED_CSS = '''
.skip-link{position:absolute;top:-100%;left:var(--space-4);padding:var(--space-2) var(--space-4);background:var(--color-primary);color:var(--color-text-inverse);border-radius:var(--radius-md);font-size:var(--text-sm);z-index:1000;text-decoration:none}
.skip-link:focus{top:var(--space-2)}
.site-header{position:sticky;top:0;z-index:100;background:oklch(from var(--color-bg) l c h / 0.92);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border-bottom:1px solid var(--color-divider);padding:var(--space-3) var(--space-4)}
.header-inner{max-width:var(--content-wide);margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:var(--space-4)}
.header-logo{display:flex;align-items:center;gap:var(--space-2);text-decoration:none;color:var(--color-text);flex-shrink:0}
.header-logo svg{width:28px;height:28px}
.header-logo-text{font-family:var(--font-display);font-size:var(--text-sm);font-weight:700;letter-spacing:-0.01em}
.header-nav{display:flex;align-items:center;gap:var(--space-1)}
.header-nav a{font-size:var(--text-xs);color:var(--color-text-muted);text-decoration:none;padding:var(--space-1) var(--space-3);border-radius:var(--radius-sm);transition:color var(--transition-interactive),background var(--transition-interactive);white-space:nowrap}
.header-nav a:hover{color:var(--color-text);background:var(--color-surface)}
.header-nav a.active{color:var(--color-primary)}
.header-actions{display:flex;align-items:center;gap:var(--space-2)}
.theme-toggle{padding:var(--space-2);color:var(--color-text-muted);border-radius:var(--radius-md);transition:color var(--transition-interactive),background var(--transition-interactive)}
.theme-toggle:hover{color:var(--color-text);background:var(--color-surface)}
.mobile-menu-btn{display:none;padding:var(--space-2);color:var(--color-text-muted);border-radius:var(--radius-md)}
@media(max-width:768px){
  .header-nav{display:none}
  .header-nav.open{display:flex;flex-direction:column;position:absolute;top:100%;left:0;right:0;background:var(--color-surface);border-bottom:1px solid var(--color-divider);padding:var(--space-2) var(--space-4);gap:0;z-index:200}
  .mobile-menu-btn{display:block}
}
.section{padding:clamp(var(--space-12),6vw,var(--space-24)) var(--space-4)}
.section-inner{max-width:var(--content-wide);margin:0 auto}
.section-label{font-family:var(--font-body);font-size:var(--text-xs);font-weight:600;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-primary);margin-bottom:var(--space-3)}
.section-heading{font-family:var(--font-display);font-size:var(--text-xl);font-weight:600;margin-bottom:var(--space-4)}
.section-subtext{font-size:var(--text-sm);color:var(--color-text-muted);max-width:65ch;line-height:1.7}
.badge{display:inline-flex;padding:var(--space-1) var(--space-3);border-radius:var(--radius-full);font-size:var(--text-xs);font-weight:600;letter-spacing:0.02em}
.badge-unsolved{background:var(--color-error-highlight);color:var(--color-error)}
.badge-arrest{background:var(--color-primary-highlight);color:var(--color-primary)}
.badge-conviction{background:var(--color-success-highlight);color:var(--color-success)}
.badge-partial{background:oklch(0.5 0.15 70 / 0.15);color:oklch(0.75 0.15 70)}
.case-tag{font-size:var(--text-xs);color:var(--color-text-faint);background:var(--color-surface-offset);padding:2px var(--space-2);border-radius:var(--radius-sm)}
.site-footer{border-top:1px solid var(--color-divider);padding:var(--space-8) var(--space-4)}
.footer-inner{max-width:var(--content-wide);margin:0 auto;display:flex;justify-content:space-between;align-items:flex-start;gap:var(--space-6);flex-wrap:wrap}
.footer-brand{display:flex;align-items:center;gap:var(--space-2);margin-bottom:var(--space-3)}
.footer-brand svg{width:20px;height:20px;color:var(--color-text-faint)}
.footer-brand span{font-family:var(--font-display);font-size:var(--text-xs);font-weight:600;color:var(--color-text-faint)}
.footer-text{font-size:var(--text-xs);color:var(--color-text-faint);max-width:50ch;line-height:1.6}
.footer-links{display:flex;gap:var(--space-6)}
.footer-link-group h4{font-size:var(--text-xs);font-weight:600;color:var(--color-text-muted);margin-bottom:var(--space-2);text-transform:uppercase;letter-spacing:0.06em}
.footer-link-group a{display:block;font-size:var(--text-xs);color:var(--color-text-faint);text-decoration:none;padding:var(--space-1) 0;transition:color var(--transition-interactive)}
.footer-link-group a:hover{color:var(--color-text)}
.footer-bottom{max-width:var(--content-wide);margin:var(--space-6) auto 0;padding-top:var(--space-4);border-top:1px solid var(--color-divider);display:flex;justify-content:space-between;align-items:center;gap:var(--space-4);flex-wrap:wrap}
.footer-bottom p,.footer-bottom a{font-size:var(--text-xs);color:var(--color-text-faint)}
.footer-bottom a{text-decoration:underline;text-underline-offset:2px;transition:color var(--transition-interactive)}
.footer-bottom a:hover{color:var(--color-text-muted)}
.fade-in{opacity:1}
@supports(animation-timeline:scroll()){
  .fade-in{opacity:0;animation:reveal-fade linear both;animation-timeline:view();animation-range:entry 0% entry 100%}
}
@keyframes reveal-fade{to{opacity:1}}
body::after{content:'';position:fixed;inset:0;opacity:0.025;pointer-events:none;z-index:1000;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
'''

STATE_CSS = '''
.state-breadcrumb{font-size:var(--text-xs);color:var(--color-text-faint);margin-bottom:var(--space-6);display:flex;align-items:center;gap:var(--space-2);flex-wrap:wrap}
.state-breadcrumb a{color:var(--color-text-faint);text-decoration:none;transition:color var(--transition-interactive)}
.state-breadcrumb a:hover{color:var(--color-text)}
.state-breadcrumb-sep{opacity:0.4}
.state-stats-row{display:flex;gap:var(--space-6);flex-wrap:wrap;margin:var(--space-6) 0 var(--space-8);padding:var(--space-6);background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-lg)}
.state-stat{display:flex;flex-direction:column;gap:var(--space-1)}
.state-stat-value{font-family:var(--font-display);font-size:var(--text-lg);font-weight:700;color:var(--color-primary)}
.state-stat-label{font-size:var(--text-xs);color:var(--color-text-faint)}
.breakdown-row{display:flex;gap:var(--space-2);flex-wrap:wrap;margin-bottom:var(--space-8)}
.breakdown-chip{font-size:var(--text-xs);color:var(--color-text-muted);background:var(--color-surface-2);border:1px solid var(--color-border);padding:var(--space-1) var(--space-3);border-radius:var(--radius-full)}
.breakdown-chip strong{color:var(--color-text)}
.cases-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(320px,100%),1fr));gap:var(--space-4)}
.case-card{background:var(--color-surface-2);border:1px solid var(--color-border);border-radius:var(--radius-lg);padding:var(--space-5);text-decoration:none;display:block;transition:border-color var(--transition-interactive),box-shadow var(--transition-interactive),transform var(--transition-interactive)}
.case-card:hover{border-color:var(--color-primary);box-shadow:var(--shadow-md);transform:translateY(-2px)}
.case-card-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:var(--space-3)}
.case-card-year{font-size:var(--text-xs);color:var(--color-text-faint);font-variant-numeric:tabular-nums}
.case-card-name{font-family:var(--font-display);font-size:var(--text-lg);font-weight:600;margin-bottom:var(--space-2);line-height:1.25;color:var(--color-text)}
.case-card-summary{font-size:var(--text-sm);color:var(--color-text-muted);line-height:1.6;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.case-card-tags{display:flex;gap:var(--space-2);flex-wrap:wrap;margin-top:var(--space-3)}
.state-nav-links{display:flex;gap:var(--space-3);flex-wrap:wrap;margin-top:var(--space-10);padding-top:var(--space-6);border-top:1px solid var(--color-divider)}
.state-nav-links a{font-size:var(--text-xs);color:var(--color-text-muted);text-decoration:none;padding:var(--space-2) var(--space-3);border:1px solid var(--color-border);border-radius:var(--radius-md);transition:all var(--transition-interactive)}
.state-nav-links a:hover{color:var(--color-text);border-color:var(--color-text-faint);background:var(--color-surface)}
'''

LOGO_SVG = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect x="3" y="6" width="18" height="22" rx="2" stroke="currentColor" stroke-width="1.5"/>
        <path d="M7 6V4a2 2 0 012-2h10l4 4v0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="7" y1="13" x2="17" y2="13" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
        <line x1="7" y1="17" x2="14" y2="17" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
        <line x1="7" y1="21" x2="12" y2="21" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
        <circle cx="23" cy="20" r="5" stroke="var(--color-primary)" stroke-width="1.8"/>
        <line x1="26.5" y1="23.5" x2="30" y2="27" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round"/>
      </svg>'''

FOOTER_SVG = '''<svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="3" y="6" width="18" height="22" rx="2" stroke="currentColor" stroke-width="1.5"/>
          <path d="M7 6V4a2 2 0 012-2h10l4 4v0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          <circle cx="23" cy="20" r="5" stroke="currentColor" stroke-width="1.5"/>
          <line x1="26.5" y1="23.5" x2="30" y2="27" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
        </svg>'''

THEME_JS = '''// Theme toggle (persisted via localStorage)
(function() {
  const toggle = document.querySelector('[data-theme-toggle]');
  const root = document.documentElement;
  const sunIcon = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>';
  const moonIcon = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  let theme = 'dark';
  try { theme = localStorage.getItem('cci-theme') || 'dark'; } catch (e) {}
  function apply(t) {
    root.setAttribute('data-theme', t);
    if (toggle) {
      toggle.setAttribute('aria-label', `Switch to ${t === 'dark' ? 'light' : 'dark'} mode`);
      toggle.innerHTML = t === 'dark' ? sunIcon : moonIcon;
    }
  }
  apply(theme);
  if (toggle) {
    toggle.addEventListener('click', () => {
      theme = theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('cci-theme', theme); } catch (e) {}
      apply(theme);
    });
  }
})();
document.getElementById('mobileMenuBtn').addEventListener('click', function() {
  const nav = document.getElementById('headerNav');
  const open = nav.classList.toggle('open');
  this.setAttribute('aria-expanded', open);
  this.innerHTML = open
    ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
    : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
});'''

def build_header(active='states'):
    return f'''<header class="site-header">
  <div class="header-inner">
    <a href="../../" class="header-logo" aria-label="ColdCaseIndex home">
      {LOGO_SVG}
      <span class="header-logo-text">ColdCaseIndex</span>
    </a>
    <nav class="header-nav" id="headerNav" aria-label="Main navigation">
      <a href="../../#statistics">Statistics</a>
      <a href="../../#cases">Cases</a>
      <a href="../../states/" class="active">By State</a>
      <a href="../../about/">About</a>
    </nav>
    <div class="header-actions">
      <button class="theme-toggle" data-theme-toggle aria-label="Switch to light mode">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      </button>
      <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Open menu" aria-expanded="false">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </div>
</header>'''


def build_footer():
    return f'''<footer class="site-footer">
  <div class="footer-inner">
    <div>
      <div class="footer-brand">
        {FOOTER_SVG}
        <span>ColdCaseIndex</span>
      </div>
      <p class="footer-text">A searchable database of unsolved crimes in America. Bringing data-driven attention to cold cases and honoring victims through accessible information.</p>
    </div>
    <div class="footer-links">
      <div class="footer-link-group">
        <h4>Navigate</h4>
        <a href="../../#statistics">Statistics</a>
        <a href="../../#cases">Cases</a>
        <a href="../../states/">By State</a>
        <a href="../../about/">About</a>
        <a href="../../privacy/">Privacy</a>
      </div>
      <div class="footer-link-group">
        <h4>Data Sources</h4>
        <a href="https://www.murderdata.org/" target="_blank" rel="noopener noreferrer">Murder Accountability Project</a>
        <a href="https://ucr.fbi.gov/" target="_blank" rel="noopener noreferrer">FBI UCR Data</a>
        <a href="https://namus.nij.ojp.gov/" target="_blank" rel="noopener noreferrer">NamUs</a>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 ColdCaseIndex. A research resource for public interest.</p>
    <p><a href="../../privacy/">Privacy Policy</a> · Contact: <a href="mailto:info@coldcaseindex.com">info@coldcaseindex.com</a></p>
  </div>
</footer>'''


def esc(text):
    if text is None:
        return ''
    return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def case_card(c):
    slug = c.get('id', slugify(c.get('name', '')))
    badge = status_badge_class(c.get('status', 'Unsolved'))
    status = esc(c.get('status', 'Unsolved'))
    summary = esc((c.get('summary') or '')[:220])
    age_tag = f'<span class="case-tag">Age {c["age"]}</span>' if c.get('age') is not None else ''
    return f'''<a href="../../cases/{slug}/" class="case-card">
        <div class="case-card-header">
          <span class="badge {badge}">{status}</span>
          <span class="case-card-year">{c.get('year', '')}</span>
        </div>
        <h3 class="case-card-name">{esc(c.get('name', ''))}</h3>
        <p class="case-card-summary">{summary}</p>
        <div class="case-card-tags">
          <span class="case-tag">{esc(c.get('city', ''))}</span>
          <span class="case-tag">{esc(c.get('type', ''))}</span>
          {age_tag}
        </div>
      </a>'''


def generate_state_page(state, cases, all_state_slugs):
    slug = slugify(state)
    url = f'{BASE_URL}/states/{slug}/'
    n = len(cases)
    types = Counter(c.get('type', 'Unknown') for c in cases)
    statuses = Counter(c.get('status', 'Unsolved') for c in cases)
    unsolved = statuses.get('Unsolved', 0)
    years = sorted(c.get('year') for c in cases if c.get('year'))
    year_range = f'{years[0]}–{years[-1]}' if years else 'Unknown'
    if years and years[0] == years[-1]:
        year_range = str(years[0])

    cases_sorted = sorted(cases, key=lambda c: (-(c.get('year') or 0), c.get('name', '')))
    cards = '\n      '.join(case_card(c) for c in cases_sorted)

    type_chips = '\n      '.join(
        f'<span class="breakdown-chip"><strong>{types[t]}</strong> {esc(t)}{"s" if types[t] != 1 and not t.endswith("s") else ""}</span>'
        for t in sorted(types, key=lambda t: -types[t]))
    status_chips = '\n      '.join(
        f'<span class="breakdown-chip"><strong>{statuses[s]}</strong> {esc(s)}</span>'
        for s in sorted(statuses, key=lambda s: -statuses[s]))

    description = (f'{n} documented cold case{"s" if n != 1 else ""} in {state}: unsolved homicides, '
                   f'missing persons, and unidentified victims spanning {year_range}. '
                   f'Case details, status, and how to submit tips.')

    breadcrumb_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": "Cases by State", "item": f"{BASE_URL}/states/"},
            {"@type": "ListItem", "position": 3, "name": state, "item": url}
        ]
    }
    collection_ld = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": f"Cold Cases in {state}",
        "description": description,
        "url": url,
        "inLanguage": "en-US",
        "isPartOf": {"@type": "WebSite", "name": "ColdCaseIndex", "url": f"{BASE_URL}/"},
        "about": {"@type": "Thing", "name": f"Unsolved crimes in {state}"}
    }

    # Prev/next state links for internal crawl paths
    idx = all_state_slugs.index((state, slug))
    prev_state, prev_slug = all_state_slugs[idx - 1]
    next_state, next_slug = all_state_slugs[(idx + 1) % len(all_state_slugs)]

    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{GA_SNIPPET}
<title>Cold Cases in {state} — {n} Documented Cases | ColdCaseIndex</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:title" content="Cold Cases in {state} — ColdCaseIndex">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="ColdCaseIndex">

{FONTS}

<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">

<link rel="stylesheet" href="../../base.css">
<link rel="stylesheet" href="../../style.css">

<script type="application/ld+json">
{json.dumps(breadcrumb_ld, indent=1)}
</script>
<script type="application/ld+json">
{json.dumps(collection_ld, indent=1)}
</script>

<style>
{SHARED_CSS}
{STATE_CSS}
</style>
</head>
<body>

<a class="skip-link" href="#main">Skip to content</a>

{build_header()}

<main id="main">
  <section class="section">
    <div class="section-inner">

      <nav class="state-breadcrumb" aria-label="Breadcrumb">
        <a href="../../">Home</a>
        <span class="state-breadcrumb-sep">&rsaquo;</span>
        <a href="../">Cases by State</a>
        <span class="state-breadcrumb-sep">&rsaquo;</span>
        <span>{state}</span>
      </nav>

      <div class="section-label fade-in">State Directory</div>
      <h1 class="section-heading fade-in">Cold Cases in {state}</h1>
      <p class="section-subtext fade-in">ColdCaseIndex documents {n} cold case{'s' if n != 1 else ''} in {state}, spanning {year_range}. {unsolved} of these case{'s' if unsolved != 1 else ''} remain{'s' if unsolved == 1 else ''} fully unsolved. Each case page includes documented details, status, and information on how to submit a tip.</p>

      <div class="state-stats-row fade-in">
        <div class="state-stat">
          <span class="state-stat-value">{n}</span>
          <span class="state-stat-label">Documented Cases</span>
        </div>
        <div class="state-stat">
          <span class="state-stat-value">{unsolved}</span>
          <span class="state-stat-label">Still Unsolved</span>
        </div>
        <div class="state-stat">
          <span class="state-stat-value">{year_range}</span>
          <span class="state-stat-label">Year Range</span>
        </div>
        <div class="state-stat">
          <span class="state-stat-value">{len(types)}</span>
          <span class="state-stat-label">Case Types</span>
        </div>
      </div>

      <h2 class="section-heading" style="font-size:var(--text-base);">By Type</h2>
      <div class="breakdown-row fade-in">
      {type_chips}
      </div>

      <h2 class="section-heading" style="font-size:var(--text-base);">By Status</h2>
      <div class="breakdown-row fade-in">
      {status_chips}
      </div>

      <h2 class="section-heading" style="margin-top:var(--space-8);">All {state} Cases</h2>
      <div class="cases-grid">
      {cards}
      </div>

      <nav class="state-nav-links" aria-label="More states">
        <a href="../{prev_slug}/">&larr; {prev_state}</a>
        <a href="../">All States</a>
        <a href="../{next_slug}/">{next_state} &rarr;</a>
      </nav>

    </div>
  </section>
</main>

{build_footer()}

<script>
{THEME_JS}
</script>
</body>
</html>'''


INDEX_CSS = '''
.states-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(260px,100%),1fr));gap:var(--space-3)}
.state-card{background:var(--color-surface-2);border:1px solid var(--color-border);border-radius:var(--radius-lg);padding:var(--space-5);text-decoration:none;display:block;transition:border-color var(--transition-interactive),box-shadow var(--transition-interactive),transform var(--transition-interactive)}
.state-card:hover{border-color:var(--color-primary);box-shadow:var(--shadow-md);transform:translateY(-2px)}
.state-card-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:var(--space-3)}
.state-name{font-family:var(--font-display);font-size:var(--text-base);font-weight:600;color:var(--color-text)}
.state-count-badge{background:var(--color-primary-highlight);color:var(--color-primary);font-size:var(--text-xs);font-weight:700;padding:2px var(--space-2);border-radius:var(--radius-full)}
.state-bar-wrapper{height:4px;background:var(--color-border);border-radius:var(--radius-full);overflow:hidden;margin-bottom:var(--space-2)}
.state-bar{height:100%;background:var(--color-primary);border-radius:var(--radius-full);opacity:0.7;transition:opacity var(--transition-interactive)}
.state-card:hover .state-bar{opacity:1}
.state-card-meta{font-size:var(--text-xs);color:var(--color-text-faint)}
.states-search{width:100%;max-width:400px;padding:var(--space-3) var(--space-4);background:var(--color-surface);border:1px solid var(--color-border);border-radius:var(--radius-lg);font-size:var(--text-sm);color:var(--color-text);transition:border-color var(--transition-interactive);margin-bottom:var(--space-6)}
.states-search:focus{border-color:var(--color-primary);outline:none}
.states-search::placeholder{color:var(--color-text-faint)}
.state-section{margin-bottom:var(--space-8)}
.state-section-heading{font-size:var(--text-xs);font-weight:600;text-transform:uppercase;letter-spacing:0.1em;color:var(--color-text-faint);margin-bottom:var(--space-4);padding-bottom:var(--space-2);border-bottom:1px solid var(--color-divider)}
'''


def build_index_header():
    # Same header as state pages but with one-level-up relative paths
    return build_header().replace('../../', '../')


def build_index_footer():
    return build_footer().replace('../../', '../')


def generate_states_index(by_state):
    state_names = sorted(by_state.keys())
    max_count = max(len(v) for v in by_state.values())
    total = sum(len(v) for v in by_state.values())
    url = f'{BASE_URL}/states/'

    groups = defaultdict(list)
    for s in state_names:
        groups[s[0]].append(s)

    sections = []
    for letter in sorted(groups):
        cards = []
        for state in groups[letter]:
            n = len(by_state[state])
            slug = slugify(state)
            cards.append(f'''<a href="./{slug}/" class="state-card" data-state="{esc(state.lower())}" id="{slug}">
            <div class="state-card-header">
              <span class="state-name">{esc(state)}</span>
              <span class="state-count-badge">{n}</span>
            </div>
            <div class="state-bar-wrapper">
              <div class="state-bar" style="width:{n / max_count * 100:.1f}%"></div>
            </div>
            <div class="state-card-meta">{n} documented case{'s' if n != 1 else ''}</div>
          </a>''')
        sections.append(f'''<div class="state-section" data-letter="{letter}">
      <div class="state-section-heading">{letter}</div>
      <div class="states-grid">
        {''.join(cards)}
      </div>
    </div>''')

    description = (f'Browse {total} documented cold cases by US state and the District of Columbia. '
                   'Unsolved homicides, missing persons, and unidentified victims with per-state statistics.')

    breadcrumb_ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
            {"@type": "ListItem", "position": 2, "name": "Cases by State", "item": url}
        ]
    }
    collection_ld = {
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Cold Cases by State",
        "description": description,
        "url": url,
        "inLanguage": "en-US",
        "isPartOf": {"@type": "WebSite", "name": "ColdCaseIndex", "url": f"{BASE_URL}/"},
        "about": {"@type": "Thing", "name": "Cold cases and unsolved crimes by US state"}
    }

    search_js = '''
// Client-side filter over the static state grid
document.getElementById('stateSearch').addEventListener('input', function() {
  const q = this.value.trim().toLowerCase();
  let visible = 0;
  document.querySelectorAll('.state-card').forEach(card => {
    const show = card.dataset.state.includes(q);
    card.style.display = show ? '' : 'none';
    if (show) visible++;
  });
  document.querySelectorAll('.state-section').forEach(sec => {
    const any = [...sec.querySelectorAll('.state-card')].some(c => c.style.display !== 'none');
    sec.style.display = any ? '' : 'none';
  });
  document.getElementById('noStates').style.display = visible ? 'none' : 'block';
});'''

    return f'''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{GA_SNIPPET}
<title>Cold Cases by State — All 50 States and DC | ColdCaseIndex</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta property="og:title" content="Cold Cases by State — ColdCaseIndex">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="ColdCaseIndex">

{FONTS}

<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">

<link rel="stylesheet" href="../base.css">
<link rel="stylesheet" href="../style.css">

<script type="application/ld+json">
{json.dumps(breadcrumb_ld, indent=1)}
</script>
<script type="application/ld+json">
{json.dumps(collection_ld, indent=1)}
</script>

<style>
{SHARED_CSS}
{INDEX_CSS}
</style>
</head>
<body>

<a class="skip-link" href="#main">Skip to content</a>

{build_index_header()}

<main id="main">
<section class="section">
  <div class="section-inner">
    <div class="section-label fade-in">State Directory</div>
    <h1 class="section-heading fade-in">Cases by State</h1>
    <p class="section-subtext fade-in" style="margin-bottom:var(--space-6)">Browse {total} documented cold cases from all 50 states and the District of Columbia. Each state page lists every documented case with statistics on type, status, and time period.</p>

    <input type="text" class="states-search fade-in" id="stateSearch" placeholder="Search states..." aria-label="Search states">

    <div id="statesContainer" class="fade-in">
    {''.join(sections)}
    </div>
    <p id="noStates" style="display:none;color:var(--color-text-faint);font-size:var(--text-sm)">No states match your search.</p>
  </div>
</section>
</main>

{build_index_footer()}

<script>
{THEME_JS}
{search_js}
</script>
</body>
</html>'''


def main():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        cases = json.load(f)

    by_state = defaultdict(list)
    for c in cases:
        state = c.get('state')
        if state:
            by_state[state].append(c)

    state_names = sorted(by_state.keys())
    all_state_slugs = [(s, slugify(s)) for s in state_names]

    generated = 0
    for state in state_names:
        slug = slugify(state)
        page_dir = os.path.join(STATES_DIR, slug)
        os.makedirs(page_dir, exist_ok=True)
        html = generate_state_page(state, by_state[state], all_state_slugs)
        with open(os.path.join(page_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        generated += 1

    with open(os.path.join(STATES_DIR, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(generate_states_index(by_state))

    print(f'Generated {generated} state pages + states index in {STATES_DIR}')


if __name__ == '__main__':
    main()
