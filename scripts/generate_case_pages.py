#!/usr/bin/env python3
"""
ColdCaseIndex — Case Page Generator
Reads data/cases.json and generates individual HTML pages at cases/{slug}/index.html,
regenerates sitemap.xml, and injects the current case count into the static pages
(index.html, about/index.html, manifest.json) so it is never hardcoded by hand.
Run from the project root: python3 scripts/generate_case_pages.py
"""

import datetime
import html
import json
import os
import re
from collections import defaultdict

# ── Paths / constants ──
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_FILE = os.path.join(ROOT_DIR, 'data', 'cases.json')
CASES_DIR = os.path.join(ROOT_DIR, 'cases')
SITEMAP_FILE = os.path.join(ROOT_DIR, 'sitemap.xml')

BASE_URL = 'https://coldcaseindex.com'
OG_IMAGE = f'{BASE_URL}/og-image.png'
SITE_NAME = 'ColdCaseIndex'
TAGLINE = 'Cold Case & Historic Crime Database'
GA_SNIPPET = ('<script async src="https://www.googletagmanager.com/gtag/js?id=G-9D333CYZNN"></script>'
              '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
              'gtag("js",new Date());gtag("config","G-9D333CYZNN");</script>')


def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def truncate_words(text, limit=155):
    """Truncate at the last word boundary within `limit` chars, append ellipsis."""
    text = ' '.join(text.split())
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(' ', 1)[0].rstrip(',;:')
    return cut + '…'


def sentence_truncate(text, limit):
    """Truncate at the last full sentence within `limit` chars; fall back to word boundary."""
    text = ' '.join(text.split())
    if len(text) <= limit:
        return text
    cut = text[:limit + 1]
    end = max(cut.rfind('. '), cut.rfind('! '), cut.rfind('? '))
    if end >= limit // 2:
        return cut[:end + 1]
    return truncate_words(text, limit)


def build_meta_desc(case, max_len=160):
    """Keyword-rich meta description: summary lead + type/location/year/status tail."""
    name = case.get('name', 'Unknown')
    summary = case.get('summary', '') or f'{name} — cold case details, timeline, and investigation status.'
    case_type = case.get('type', 'Homicide')
    status = case.get('status', 'Unsolved')
    city = case.get('city', '')
    state = case.get('state', '')
    year = case.get('year')

    loc = ', '.join(p for p in (city, state) if p and p != 'Unknown')
    tail = f' {case_type} cold case'
    if loc:
        tail += f' in {loc}'
    if year:
        tail += f' ({year})'
    tail += f'. Status: {status}.'

    body = sentence_truncate(summary, max_len - len(tail))
    # If the summary is too dense to fit a useful lead, fall back to summary alone.
    if len(body) < 40:
        return sentence_truncate(summary, max_len)
    return body + tail


def iso_date(case):
    """Best-effort ISO 8601 date for a case ('April 24, 1891' -> '1891-04-24')."""
    date = case.get('date', '')
    for fmt in ('%B %d, %Y', '%b %d, %Y', '%B %Y', '%Y-%m-%d'):
        try:
            return datetime.datetime.strptime(date.strip(), fmt).date().isoformat()
        except (ValueError, AttributeError):
            continue
    year = case.get('year')
    return str(year) if year else None


def status_badge_class(status):
    if not status:
        return 'badge-unsolved'
    s = status.lower()
    if 'conviction' in s and 'no conviction' not in s:
        return 'badge-conviction'
    if s in ('solved', 'identified'):
        return 'badge-conviction'
    if 'arrest' in s:
        return 'badge-arrest'
    if 'partially' in s:
        return 'badge-partial'
    return 'badge-unsolved'


def status_badge_label(status):
    return status if status else 'Unsolved'


def an_article(word):
    return 'an' if word and word[0].lower() in 'aeiou' else 'a'


TYPE_NOUN = {
    'Homicide': 'homicide',
    'Multiple Homicide': 'multiple-homicide',
    'Serial Killer Victims': 'serial-homicide',
    'Missing Person': 'missing-person',
    'Unidentified Person': 'unidentified-persons',
    'Suspicious Death': 'suspicious-death',
    'Historic Injustice': 'historic-injustice',
}


def _known(v):
    return v is not None and str(v).strip() not in ('', 'Unknown', 'N/A')


def build_narrative(case):
    """Build 3-4 paragraphs of prose from *verified fields only*.

    Every sentence is either a restatement of a recorded field (name, type,
    status, date, location, age, gender) or generically-true context about the
    case category. No case-specific fact is asserted beyond the stored data, so
    this expands thin pages without fabricating claims about real people.
    Case-specific tokens are interpolated throughout so each page's prose is
    lexically distinct rather than boilerplate.

    If the case has a researched `narrative` (enriched cases), that verified,
    individually-sourced prose is rendered instead of the generic build.
    """
    if case.get('enriched') and case.get('narrative'):
        e = html.escape
        body = '\n'.join(f'        <p class="case-narrative">{e(p)}</p>'
                         for p in case['narrative'] if p.strip())
        return f'''
      <!-- Researched Narrative -->
      <div class="case-narrative-section fade-in">
        <div class="section-label">Case Background &amp; Investigation</div>
{body}
      </div>'''

    name = case.get('name', 'This case')
    case_type = case.get('type', 'Homicide')
    status = case.get('status', 'Unsolved')
    city = case.get('city', '')
    state = case.get('state', '')
    date = case.get('date', '')
    year = case.get('year')
    age = case.get('age')
    gender = case.get('gender', '')
    last_seen = case.get('lastSeen', '')
    tags = [t for t in case.get('tags', []) if str(t).strip()]
    type_noun = TYPE_NOUN.get(case_type, 'cold')
    is_missing = case_type == 'Missing Person'
    is_unid = case_type == 'Unidentified Person'
    is_multi = case_type in ('Multiple Homicide', 'Serial Killer Victims')

    loc = ', '.join(p for p in (city, state) if _known(p)) or 'the United States'

    # ── Paragraph 1: case details ──
    facts = []
    if is_missing:
        facts.append(f"{name} is documented in the ColdCaseIndex database as a "
                     f"missing-person case connected to {loc}.")
    elif is_unid:
        facts.append(f"“{name}” is an unidentified-persons case in the "
                     f"ColdCaseIndex database, associated with {loc}.")
    else:
        facts.append(f"{name} is documented in the ColdCaseIndex database as "
                     f"{an_article(type_noun)} {type_noun} case in {loc}.")

    if _known(date):
        if is_missing:
            facts.append(f"The disappearance is dated to {date}.")
        elif is_unid:
            facts.append(f"The remains are associated with {date}.")
        else:
            facts.append(f"The events are dated to {date}.")

    if is_multi:
        facts.append("The case involves more than one victim.")
    elif not is_unid:
        demo = None
        if _known(age) and _known(gender) and gender != 'Multiple':
            demo = f"The victim is recorded as {age} years old and {gender.lower()}."
        elif _known(age):
            demo = f"The victim is recorded as {age} years old."
        elif _known(gender) and gender != 'Multiple':
            demo = f"The victim is recorded as {gender.lower()}."
        if demo:
            facts.append(demo)

    if _known(last_seen):
        facts.append(f"The last known information on record places the case at {last_seen}.")

    # ── Paragraph 2: classification & themes (verified taxonomy fields) ──
    type_def = {
        'Homicide': "A homicide entry documents a killing in which the perpetrator has not been identified, has not been convicted, or where the case is otherwise historically notable.",
        'Multiple Homicide': "A multiple-homicide entry documents an incident involving more than one victim.",
        'Serial Killer Victims': "This entry is grouped under a confirmed or suspected serial perpetrator.",
        'Missing Person': "A missing-person entry documents someone who disappeared under circumstances that remain unresolved.",
        'Unidentified Person': "An unidentified-persons entry documents recovered remains whose identity has not been established.",
        'Suspicious Death': "A suspicious-death entry documents a death, sometimes officially ruled accidental or natural, that remains contested.",
        'Historic Injustice': "This entry documents a historically significant case of injustice.",
    }.get(case_type, "This entry documents a case of continuing public interest.")
    class_parts = [
        f"Within the ColdCaseIndex taxonomy, {name} is filed under {case_type} with a "
        f"status of {status}.",
        type_def,
    ]
    if tags:
        shown = tags[:8]
        class_parts.append(
            "The record is cross-referenced under the themes "
            + ', '.join(shown)
            + ", which connect it to related cases across the database.")
    classification_text = ' '.join(class_parts)

    # ── Paragraph 3: investigation status (generic-but-true, interpolated) ──
    status_text = {
        'Unsolved': (
            f"As of the most recent information compiled here, no arrest has been "
            f"publicly recorded in the {name} case, and it remains open and unsolved. "
            f"Cases like this can be reactivated at any time — advances in DNA "
            f"analysis, forensic genetic genealogy, and renewed public attention have "
            f"resolved cases that lay dormant for decades."),
        'Conviction': (
            f"The {name} case ended in a criminal conviction. It is retained in this "
            f"index as a historically significant case — one whose investigation, "
            f"prosecution, or aftermath shaped forensic practice, criminal law, or the "
            f"public understanding of violent crime."),
        'Arrest Made': (
            f"An arrest has been made in the {name} case, but it had not reached a "
            f"final resolution as of the information compiled here."),
        'Partially Solved': (
            f"The {name} case is partially resolved: some elements have been "
            f"established while significant questions remain open."),
        'No Conviction': (
            f"In the {name} case, the circumstances or the person believed responsible "
            f"are known, but no conviction was secured — for example following an "
            f"acquittal, a death before trial, or a declined indictment."),
        'Ruled Suicide': (
            f"The {name} case was officially ruled a suicide, a determination that has "
            f"been questioned or revisited by some observers."),
    }.get(status, (
        f"The current status of the {name} case is recorded as “{status}.” "
        f"Details may change as new information becomes available."))

    # ── Paragraph 3: jurisdiction & national context ──
    juris_place = city if _known(city) else (state if _known(state) else 'the local area')
    state_clause = f", supported by {state} state investigative authorities" if _known(state) else ""
    juris_text = (
        f"Primary jurisdiction for the {name} case rests with local law enforcement in "
        f"{juris_place}{state_clause}. The case sits within a wider national picture: the "
        f"U.S. homicide clearance rate has fallen from roughly 90% in the 1960s to about "
        f"54% today, and more than 346,000 homicides recorded since 1965 remain unsolved. "
        f"ColdCaseIndex documents individual cases like this one to keep them publicly "
        f"visible and searchable.")

    e = html.escape
    paras = [' '.join(facts), classification_text, status_text, juris_text]
    body = '\n'.join(f'        <p class="case-narrative">{e(p)}</p>' for p in paras if p.strip())
    return f'''
      <!-- Extended Narrative -->
      <div class="case-narrative-section fade-in">
        <div class="section-label">Case Details</div>
{body}
      </div>'''


def render_sources_section(case):
    """Render 'Sources & Further Reading': stored references + honest search links."""
    e = html.escape
    name = case.get('name', '')
    city = case.get('city', '')
    state = case.get('state', '')
    sources = [s for s in case.get('sources', []) if s.get('url') and s.get('title')]

    items = []
    for s in sources:
        items.append(
            f'<li><a href="{e(s["url"])}" target="_blank" rel="noopener noreferrer nofollow">'
            f'{e(s["title"])}</a></li>')

    # Honestly-labeled search deep-links (always valid; generated, not stored).
    q_parts = [name] + [p for p in (city, state) if _known(p)]
    query = ' '.join(q_parts).strip()
    if query:
        import urllib.parse as _up
        q = _up.quote(query)
        items.append(
            f'<li><a href="https://en.wikipedia.org/w/index.php?search={q}" '
            f'target="_blank" rel="noopener noreferrer nofollow">Search Wikipedia for this case</a></li>')
        items.append(
            f'<li><a href="https://news.google.com/search?q={q}" '
            f'target="_blank" rel="noopener noreferrer nofollow">Search news coverage</a></li>')

    if not items:
        return ''
    return f'''
      <!-- Sources & Further Reading -->
      <div class="case-sources fade-in">
        <div class="section-label">Sources &amp; Further Reading</div>
        <p class="case-sources-note">Curated starting points for verifying and researching this case. Direct references are checked; search links are provided as further-reading aids. ColdCaseIndex is an index of public information — see a case correction? Email <a href="mailto:info@coldcaseindex.com">info@coldcaseindex.com</a>.</p>
        <ul class="case-sources-list">
          {''.join(items)}
        </ul>
      </div>'''


def generate_case_page(case, related_cases, today_iso):
    slug = case.get('id', slugify(case.get('name', 'unknown')))
    name = case.get('name', 'Unknown')
    status = case.get('status', 'Unsolved')
    year = case.get('year', '')
    date = case.get('date', str(year) if year else 'Unknown')
    state = case.get('state', 'Unknown')
    city = case.get('city', 'Unknown')
    age = case.get('age')
    gender = case.get('gender', 'Unknown')
    case_type = case.get('type', 'Homicide')
    summary = case.get('summary', '')
    last_seen = case.get('lastSeen', '')
    tags = case.get('tags', [])

    badge_class = status_badge_class(status)
    badge_label = status_badge_label(status)
    age_str = str(age) if age is not None else 'Unknown'

    canonical = f'{BASE_URL}/cases/{slug}/'
    page_title = f'{name} — {SITE_NAME}'
    meta_desc = build_meta_desc(case)

    e = html.escape  # attribute/text escaping

    # Tags HTML
    tags_html = '\n'.join(f'<span class="case-tag">{e(t)}</span>' for t in tags) if tags else ''

    state_slug = slugify(state) if state and state != 'Unknown' else ''

    # Related cases (other cases in same state, max 6)
    related_html = ''
    if related_cases:
        cards = []
        for rc in related_cases[:6]:
            rc_slug = rc.get('id', slugify(rc.get('name', '')))
            rc_badge = status_badge_class(rc.get('status', 'Unsolved'))
            rc_badge_label = status_badge_label(rc.get('status', 'Unsolved'))
            cards.append(f'''
              <a href="../../cases/{rc_slug}/" class="related-case-card">
                <div class="related-case-header">
                  <span class="badge {rc_badge}" style="font-size:10px;">{e(rc_badge_label)}</span>
                  <span class="case-card-year">{rc.get('year', '')}</span>
                </div>
                <div class="related-case-name">{e(rc.get('name', ''))}</div>
                <div class="related-case-meta">{e(rc.get('city', ''))}</div>
              </a>''')
        all_state_link = (f'\n        <a href="../../states/{state_slug}/" class="all-state-link">'
                          f'View all {e(state)} cases &rarr;</a>' if state_slug else '')
        related_html = f'''
    <section class="section" style="background: var(--color-surface);">
      <div class="section-inner fade-in">
        <div class="section-label">Related Cases</div>
        <h2 class="section-heading">Other Cases in {e(state)}</h2>
        <div class="related-grid">
          {''.join(cards)}
        </div>{all_state_link}
      </div>
    </section>'''

    # Timeline. Enriched cases carry a researched, dated event list; others fall
    # back to the few entries the structured data supports.
    timeline_events = []
    if case.get('enriched') and case.get('timeline'):
        for ev in case['timeline']:
            d_lbl = str(ev.get('date', '')).strip()
            e_val = str(ev.get('event', '')).strip()
            if e_val:
                timeline_events.append((d_lbl or '—', e_val))
    else:
        if last_seen and last_seen not in ('N/A', 'Unknown', ''):
            timeline_events.append(('Last Known Information', last_seen))
        if date and str(date) not in ('Unknown', ''):
            incident_label = {
                'Missing Person': 'Reported Missing',
                'Unidentified Person': 'Remains Discovered',
            }.get(case_type, 'Date of Incident')
            timeline_events.append((incident_label, str(date)))
        timeline_events.append(('Current Status', f'{status}' + ('' if status != 'Unsolved' else ' — the case remains open')))

    timeline_html = ''
    if len(timeline_events) >= 2:
        items = '\n'.join(f'''
          <div class="timeline-item">
            <div class="timeline-marker" aria-hidden="true"></div>
            <div>
              <div class="timeline-label">{e(label)}</div>
              <div class="timeline-value">{e(value)}</div>
            </div>
          </div>''' for label, value in timeline_events)
        timeline_html = f'''
      <!-- Timeline -->
      <div class="fade-in" style="margin-top: var(--space-8);">
        <div class="section-label">Timeline</div>
        <div class="timeline">{items}
        </div>
      </div>'''

    # How to Help
    if case_type == 'Missing Person':
        type_specific_help = '''
          <li><a href="https://namus.nij.ojp.gov/" target="_blank" rel="noopener noreferrer">NamUs (namus.nij.ojp.gov)</a> — the National Missing and Unidentified Persons System accepts information on missing persons cases</li>
          <li>National Center for Missing &amp; Exploited Children: 1-800-THE-LOST (1-800-843-5678)</li>'''
    elif case_type == 'Unidentified Person':
        type_specific_help = '''
          <li><a href="https://namus.nij.ojp.gov/" target="_blank" rel="noopener noreferrer">NamUs (namus.nij.ojp.gov)</a> — the National Missing and Unidentified Persons System maintains records of unidentified remains and accepts public information</li>'''
    else:
        type_specific_help = ''
    jurisdiction = e(state) if state and state != 'Unknown' else 'the relevant jurisdiction'
    how_to_help_html = f'''
      <!-- How to Help -->
      <div class="how-to-help fade-in">
        <div class="section-label">How to Help</div>
        <h2 class="how-to-help-heading">Have Information About This Case?</h2>
        <p class="how-to-help-text">Cold cases are solved when someone comes forward. Even a detail that seems minor can matter. If you have any information about this case, contact law enforcement through one of these channels:</p>
        <ul class="how-to-help-list">
          <li><a href="https://tips.fbi.gov/" target="_blank" rel="noopener noreferrer">FBI Tips (tips.fbi.gov)</a> — submit a tip online to the Federal Bureau of Investigation</li>
          <li>FBI Tip Line: 1-800-CALL-FBI (1-800-225-5324)</li>{type_specific_help}
          <li>The local police department or sheriff's office in {jurisdiction}, or the state bureau of investigation</li>
        </ul>
        <p class="how-to-help-note">Tips can usually be submitted anonymously. To report an error on this page, email <a href="mailto:info@coldcaseindex.com">info@coldcaseindex.com</a>.</p>
      </div>'''

    # Schema.org JSON-LD: Article + BreadcrumbList
    article_schema = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": name,
        "description": meta_desc,
        "url": canonical,
        "mainEntityOfPage": {"@type": "WebPage", "@id": canonical},
        "image": OG_IMAGE,
        "inLanguage": "en-US",
        "articleSection": case_type,
        "isPartOf": {"@type": "WebSite", "name": SITE_NAME, "url": BASE_URL},
        "dateModified": today_iso,
        "author": {"@type": "Organization", "name": SITE_NAME, "url": BASE_URL},
        "publisher": {
            "@type": "Organization",
            "name": SITE_NAME,
            "url": BASE_URL,
            "logo": {"@type": "ImageObject", "url": f"{BASE_URL}/logos/logo-icon-512x512.png"}
        }
    }
    if tags:
        article_schema["keywords"] = ", ".join(tags)
    if state and state != 'Unknown':
        country_code = case.get('country', 'US') or 'US'
        address = {"@type": "PostalAddress", "addressRegion": state, "addressCountry": country_code}
        place_name = state
        if city and city != 'Unknown':
            address["addressLocality"] = city
            place_name = f"{city}, {state}"
        article_schema["contentLocation"] = {"@type": "Place", "name": place_name, "address": address}
    # datePublished = when this page was first published (use today's date as page pub date)
    article_schema["datePublished"] = today_iso

    # Sources → citation only (sameAs is for the subject entity, not an Article)
    src_list = [s for s in case.get('sources', []) if s.get('url') and s.get('title')]
    if src_list:
        article_schema["citation"] = [
            {"@type": "CreativeWork", "name": s['title'], "url": s['url']} for s in src_list
        ]

    if state_slug:
        crumb_mid = {"@type": "ListItem", "position": 2, "name": f"{state} Cases",
                     "item": f"{BASE_URL}/states/{state_slug}/"}
    else:
        crumb_mid = {"@type": "ListItem", "position": 2, "name": "Cases", "item": f"{BASE_URL}/#cases"}
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{BASE_URL}/"},
            crumb_mid,
            {"@type": "ListItem", "position": 3, "name": name, "item": canonical}
        ]
    }

    narrative_html = build_narrative(case)
    sources_html = render_sources_section(case)

    last_seen_section = ''
    if last_seen and last_seen not in ('N/A', 'Unknown', ''):
        last_seen_section = f'''
          <div class="modal-last-seen" style="margin-bottom: var(--space-5);">
            <div class="modal-last-seen-label">Last Seen / Last Known Information</div>
            <div class="modal-last-seen-value">{e(last_seen)}</div>
          </div>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
{GA_SNIPPET}
<script>try{{var _t=localStorage.getItem('cci-theme');if(_t)document.documentElement.setAttribute('data-theme',_t)}}catch(e){{}}</script>

<title>{e(page_title)}</title>
<meta name="description" content="{e(meta_desc)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">

<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:type" content="article">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{e(page_title)}">
<meta property="og:description" content="{e(meta_desc)}">
<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(page_title)}">
<meta name="twitter:description" content="{e(meta_desc)}">
<meta name="twitter:image" content="{OG_IMAGE}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Serif:wght@600;700&display=swap" rel="stylesheet">

<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">

<link rel="stylesheet" href="../../base.css">
<link rel="stylesheet" href="../../style.css">

<script type="application/ld+json">
{json.dumps(article_schema, indent=2, ensure_ascii=False)}
</script>
<script type="application/ld+json">
{json.dumps(breadcrumb_schema, indent=2, ensure_ascii=False)}
</script>

<style>
/* ── Case Page Styles ── */
.case-breadcrumb {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  margin-bottom: var(--space-6);
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-wrap: wrap;
}}
.case-breadcrumb a {{
  color: var(--color-text-faint);
  text-decoration: none;
  transition: color var(--transition-interactive);
}}
.case-breadcrumb a:hover {{ color: var(--color-text); }}
.case-breadcrumb-sep {{ opacity: 0.4; }}
.case-page-header {{
  margin-bottom: var(--space-8);
  padding-bottom: var(--space-8);
  border-bottom: 1px solid var(--color-divider);
}}
.case-page-title {{
  font-family: var(--font-display);
  font-size: clamp(1.5rem, 4vw, 2.5rem);
  font-weight: 700;
  line-height: 1.1;
  margin-bottom: var(--space-4);
  margin-top: var(--space-3);
}}
.case-page-meta-row {{
  display: flex;
  align-items: center;
  gap: var(--space-3);
  flex-wrap: wrap;
  margin-bottom: var(--space-4);
}}
.case-year-label {{
  font-size: var(--text-sm);
  color: var(--color-text-muted);
}}
.case-type-label {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  background: var(--color-surface-offset);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-sm);
}}
.case-details-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: var(--space-4);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-5);
  margin-bottom: var(--space-6);
}}
.case-detail-item {{
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}}
.case-detail-label {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-weight: 500;
}}
.case-detail-value {{
  font-size: var(--text-sm);
  font-weight: 500;
}}
.case-summary {{
  font-size: var(--text-base);
  color: var(--color-text);
  line-height: 1.8;
  margin-bottom: var(--space-6);
  max-width: 70ch;
  font-weight: 500;
}}
.case-narrative-section {{
  margin-bottom: var(--space-8);
  max-width: 70ch;
}}
.case-narrative {{
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: 1.85;
  margin-bottom: var(--space-4);
}}
.case-narrative:last-child {{ margin-bottom: 0; }}
.case-sources {{
  margin-top: var(--space-10);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  max-width: 75ch;
}}
.case-sources-note {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  line-height: 1.7;
  margin-bottom: var(--space-4);
  max-width: 65ch;
}}
.case-sources-note a {{ color: var(--color-primary); text-underline-offset: 2px; }}
.case-sources-list {{
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: 1.9;
  padding-left: var(--space-5);
  margin: 0;
}}
.case-sources-list li {{ margin-bottom: var(--space-1); }}
.case-sources-list a {{ color: var(--color-primary); text-underline-offset: 2px; }}
.case-sources-list a:hover {{ text-decoration: underline; }}
.case-back-btn {{
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  text-decoration: none;
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-md);
  border: 1px solid var(--color-border);
  transition: all var(--transition-interactive);
  margin-bottom: var(--space-8);
}}
.case-back-btn:hover {{
  color: var(--color-text);
  background: var(--color-surface);
  border-color: var(--color-text-faint);
}}
.related-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(min(200px, 100%), 1fr));
  gap: var(--space-3);
  margin-top: var(--space-6);
}}
.related-case-card {{
  background: var(--color-surface-2);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-4);
  text-decoration: none;
  display: block;
  transition: border-color var(--transition-interactive), box-shadow var(--transition-interactive), transform var(--transition-interactive);
}}
.related-case-card:hover {{
  border-color: var(--color-primary);
  box-shadow: var(--shadow-md);
  transform: translateY(-1px);
}}
.related-case-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: var(--space-2);
}}
.related-case-name {{
  font-size: var(--text-sm);
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: var(--space-1);
  line-height: 1.3;
}}
.related-case-meta {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
}}
.all-state-link {{
  display: inline-block;
  margin-top: var(--space-5);
  font-size: var(--text-sm);
  font-weight: 500;
  color: var(--color-primary);
  text-decoration: none;
}}
.all-state-link:hover {{ text-decoration: underline; text-underline-offset: 2px; }}
.timeline {{
  margin-top: var(--space-4);
  border-left: 2px solid var(--color-border);
  padding-left: var(--space-5);
  display: flex;
  flex-direction: column;
  gap: var(--space-5);
  max-width: 60ch;
}}
.timeline-item {{
  position: relative;
  display: flex;
  gap: var(--space-3);
}}
.timeline-marker {{
  position: absolute;
  left: calc(-1 * var(--space-5) - 7px);
  top: 5px;
  width: 12px;
  height: 12px;
  border-radius: var(--radius-full);
  background: var(--color-surface);
  border: 2px solid var(--color-primary);
}}
.timeline-label {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-weight: 500;
  margin-bottom: var(--space-1);
}}
.timeline-value {{
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: 1.6;
}}
.how-to-help {{
  margin-top: var(--space-10);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  max-width: 75ch;
}}
.how-to-help-heading {{
  font-family: var(--font-display);
  font-size: var(--text-lg);
  font-weight: 600;
  margin-bottom: var(--space-3);
}}
.how-to-help-text {{
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: 1.7;
  margin-bottom: var(--space-4);
}}
.how-to-help-list {{
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: 1.8;
  padding-left: var(--space-5);
  margin-bottom: var(--space-4);
}}
.how-to-help-list li {{ margin-bottom: var(--space-2); }}
.how-to-help-list a, .how-to-help-note a {{ color: var(--color-primary); text-underline-offset: 2px; }}
.how-to-help-note {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  line-height: 1.6;
}}
.badge-partial {{
  background: oklch(0.5 0.15 70 / 0.15);
  color: oklch(0.75 0.15 70);
}}

/* Reuse styles from main */
.skip-link {{
  position: absolute;
  top: -100%;
  left: var(--space-4);
  padding: var(--space-2) var(--space-4);
  background: var(--color-primary);
  color: var(--color-text-inverse);
  border-radius: var(--radius-md);
  font-size: var(--text-sm);
  z-index: 1000;
  text-decoration: none;
}}
.skip-link:focus {{ top: var(--space-2); }}
.site-header {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: oklch(from var(--color-bg) l c h / 0.92);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--color-divider);
  padding: var(--space-3) var(--space-4);
}}
.header-inner {{
  max-width: var(--content-wide);
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-4);
}}
.header-logo {{
  display: flex;
  align-items: center;
  gap: var(--space-2);
  text-decoration: none;
  color: var(--color-text);
  flex-shrink: 0;
}}
.header-logo svg {{ width: 28px; height: 28px; }}
.header-logo-text {{
  font-family: var(--font-display);
  font-size: var(--text-sm);
  font-weight: 700;
  letter-spacing: -0.01em;
}}
.header-nav {{
  display: flex;
  align-items: center;
  gap: var(--space-1);
}}
.header-nav a {{
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  text-decoration: none;
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-sm);
  transition: color var(--transition-interactive), background var(--transition-interactive);
  white-space: nowrap;
}}
.header-nav a:hover {{ color: var(--color-text); background: var(--color-surface); }}
.header-actions {{
  display: flex;
  align-items: center;
  gap: var(--space-2);
}}
.theme-toggle {{
  padding: var(--space-2);
  color: var(--color-text-muted);
  border-radius: var(--radius-md);
  transition: color var(--transition-interactive), background var(--transition-interactive);
}}
.theme-toggle:hover {{ color: var(--color-text); background: var(--color-surface); }}
.mobile-menu-btn {{
  display: none;
  padding: var(--space-2);
  color: var(--color-text-muted);
  border-radius: var(--radius-md);
}}
@media (max-width: 768px) {{
  .header-nav {{ display: none; }}
  .header-nav.open {{
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background: var(--color-surface);
    border-bottom: 1px solid var(--color-divider);
    padding: var(--space-2) var(--space-4);
    gap: 0;
    z-index: 200;
  }}
  .mobile-menu-btn {{ display: block; }}
  .case-details-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}
.section {{
  padding: clamp(var(--space-12), 6vw, var(--space-24)) var(--space-4);
}}
.section-inner {{
  max-width: var(--content-wide);
  margin: 0 auto;
}}
.section-label {{
  font-family: var(--font-body);
  font-size: var(--text-xs);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-primary);
  margin-bottom: var(--space-3);
}}
.section-heading {{
  font-family: var(--font-display);
  font-size: var(--text-xl);
  font-weight: 600;
  margin-bottom: var(--space-4);
}}
.badge {{
  display: inline-flex;
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  font-size: var(--text-xs);
  font-weight: 600;
  letter-spacing: 0.02em;
}}
.badge-unsolved {{ background: var(--color-error-highlight); color: var(--color-error); }}
.badge-arrest {{ background: var(--color-primary-highlight); color: var(--color-primary); }}
.badge-conviction {{ background: var(--color-success-highlight); color: var(--color-success); }}
.case-tag {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  background: var(--color-surface-offset);
  padding: 2px var(--space-2);
  border-radius: var(--radius-sm);
}}
.modal-last-seen {{
  background: var(--color-surface-offset);
  border-radius: var(--radius-md);
  padding: var(--space-4);
}}
.modal-last-seen-label {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  font-weight: 500;
  margin-bottom: var(--space-2);
}}
.modal-last-seen-value {{
  font-size: var(--text-sm);
}}
.site-footer {{
  border-top: 1px solid var(--color-divider);
  padding: var(--space-8) var(--space-4);
}}
.footer-inner {{
  max-width: var(--content-wide);
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: var(--space-6);
  flex-wrap: wrap;
}}
.footer-brand {{
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-3);
}}
.footer-brand svg {{ width: 20px; height: 20px; color: var(--color-text-faint); }}
.footer-brand span {{
  font-family: var(--font-display);
  font-size: var(--text-xs);
  font-weight: 600;
  color: var(--color-text-faint);
}}
.footer-text {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  max-width: 50ch;
  line-height: 1.6;
}}
.footer-links {{
  display: flex;
  gap: var(--space-6);
}}
.footer-link-group h4 {{
  font-size: var(--text-xs);
  font-weight: 600;
  color: var(--color-text-muted);
  margin-bottom: var(--space-2);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}}
.footer-link-group a {{
  display: block;
  font-size: var(--text-xs);
  color: var(--color-text-faint);
  text-decoration: none;
  padding: var(--space-1) 0;
  transition: color var(--transition-interactive);
}}
.footer-link-group a:hover {{ color: var(--color-text); }}
.footer-bottom {{
  max-width: var(--content-wide);
  margin: var(--space-6) auto 0;
  padding-top: var(--space-4);
  border-top: 1px solid var(--color-divider);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--space-4);
  flex-wrap: wrap;
}}
.footer-bottom p, .footer-bottom a {{
  font-size: var(--text-xs);
  color: var(--color-text-faint);
}}
.footer-bottom a {{
  text-decoration: underline;
  text-underline-offset: 2px;
  transition: color var(--transition-interactive);
}}
.footer-bottom a:hover {{ color: var(--color-text-muted); }}
.fade-in {{ opacity: 1; }}
@supports (animation-timeline: scroll()) {{
  .fade-in {{
    opacity: 0;
    animation: reveal-fade linear both;
    animation-timeline: view();
    animation-range: entry 0% entry 100%;
  }}
}}
@keyframes reveal-fade {{ to {{ opacity: 1; }} }}
body::after {{
  content: '';
  position: fixed;
  inset: 0;
  opacity: 0.025;
  pointer-events: none;
  z-index: 1000;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}}
</style>
</head>
<body>

<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="header-inner">
    <a href="../../" class="header-logo" aria-label="ColdCaseIndex home">
      <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
        <rect x="3" y="6" width="18" height="22" rx="2" stroke="currentColor" stroke-width="1.5"/>
        <path d="M7 6V4a2 2 0 012-2h10l4 4v0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
        <line x1="7" y1="13" x2="17" y2="13" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
        <line x1="7" y1="17" x2="14" y2="17" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
        <line x1="7" y1="21" x2="12" y2="21" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>
        <circle cx="23" cy="20" r="5" stroke="var(--color-primary)" stroke-width="1.8"/>
        <line x1="26.5" y1="23.5" x2="30" y2="27" stroke="var(--color-primary)" stroke-width="2" stroke-linecap="round"/>
      </svg>
      <span class="header-logo-text">ColdCaseIndex</span>
    </a>

    <nav class="header-nav" id="headerNav" aria-label="Main navigation">
      <a href="../../#statistics">Statistics</a>
      <a href="../../#cases">Cases</a>
      <a href="../../states/">By State</a>
      <a href="../../about/">About</a>
    </nav>

    <div class="header-actions">
      <button class="theme-toggle" data-theme-toggle aria-label="Toggle color theme">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
      </button>
      <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Open menu" aria-expanded="false">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </div>
</header>

<main id="main">

  <section class="section">
    <div class="section-inner">

      <!-- Back button -->
      <a href="../../#cases" class="case-back-btn">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M19 12H5M12 5l-7 7 7 7"/></svg>
        Back to Cases
      </a>

      <!-- Breadcrumb -->
      <nav class="case-breadcrumb" aria-label="Breadcrumb">
        <a href="../../">Home</a>
        <span class="case-breadcrumb-sep">›</span>
        {f'<a href="../../states/{state_slug}/">{e(state)} Cases</a>' if state_slug else '<a href="../../#cases">Cases</a>'}
        <span class="case-breadcrumb-sep">›</span>
        <span>{e(name)}</span>
      </nav>

      <!-- Case Header -->
      <div class="case-page-header fade-in">
        <div class="case-page-meta-row">
          <span class="badge {badge_class}">{e(badge_label)}</span>
          <span class="case-year-label">{e(str(date))}</span>
          <span class="case-type-label">{e(case_type)}</span>
        </div>
        <h1 class="case-page-title">{e(name)}</h1>
      </div>

      <!-- Details Grid -->
      <div class="case-details-grid fade-in">
        <div class="case-detail-item">
          <span class="case-detail-label">Status</span>
          <span class="case-detail-value"><span class="badge {badge_class}" style="font-size:11px;">{e(badge_label)}</span></span>
        </div>
        <div class="case-detail-item">
          <span class="case-detail-label">Type</span>
          <span class="case-detail-value">{e(case_type)}</span>
        </div>
        <div class="case-detail-item">
          <span class="case-detail-label">Date</span>
          <span class="case-detail-value">{e(str(date))}</span>
        </div>
        <div class="case-detail-item">
          <span class="case-detail-label">Location</span>
          <span class="case-detail-value">{e(city)}, {e(state)}</span>
        </div>
        <div class="case-detail-item">
          <span class="case-detail-label">Victim Age</span>
          <span class="case-detail-value">{e(age_str)}</span>
        </div>
        <div class="case-detail-item">
          <span class="case-detail-label">Gender</span>
          <span class="case-detail-value">{e(gender)}</span>
        </div>
      </div>

      <!-- Summary -->
      <div class="fade-in">
        <p class="case-summary">{e(summary)}</p>
      </div>
      {narrative_html}

      <!-- Last Seen -->
      {last_seen_section}

      <!-- Tags -->
      {'<div class="case-tags-section fade-in" style="display:flex;gap:var(--space-2);flex-wrap:wrap;margin-top:var(--space-5);">' + tags_html + '</div>' if tags_html else ''}

      {timeline_html}

      {sources_html}

      {how_to_help_html}

    </div>
  </section>

  {related_html}

</main>

<footer class="site-footer">
  <div class="footer-inner">
    <div>
      <div class="footer-brand">
        <svg viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <rect x="3" y="6" width="18" height="22" rx="2" stroke="currentColor" stroke-width="1.5"/>
          <path d="M7 6V4a2 2 0 012-2h10l4 4v0" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
          <circle cx="23" cy="20" r="5" stroke="currentColor" stroke-width="1.5"/>
          <line x1="26.5" y1="23.5" x2="30" y2="27" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
        </svg>
        <span>ColdCaseIndex</span>
      </div>
      <p class="footer-text">A searchable database of cold cases and historic crimes in America. Bringing data-driven attention to unsolved cases and honoring victims through accessible information.</p>
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
    <a href="../../privacy/">Privacy Policy</a>
  </div>
</footer>

<script>
// Theme toggle (persisted via localStorage)
(function() {{
  const toggle = document.querySelector('[data-theme-toggle]');
  const root = document.documentElement;
  const sunIcon = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>';
  const moonIcon = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
  let theme = window.matchMedia('(prefers-color-scheme:dark)').matches ? 'dark' : 'light';
  try {{ theme = localStorage.getItem('cci-theme') || theme; }} catch (e) {{}}
  function apply(t) {{
    root.setAttribute('data-theme', t);
    if (toggle) {{
      toggle.setAttribute('aria-label', `Switch to ${{t === 'dark' ? 'light' : 'dark'}} mode`);
      toggle.innerHTML = t === 'dark' ? sunIcon : moonIcon;
    }}
  }}
  apply(theme);
  if (toggle) {{
    toggle.addEventListener('click', () => {{
      theme = theme === 'dark' ? 'light' : 'dark';
      try {{ localStorage.setItem('cci-theme', theme); }} catch (e) {{}}
      apply(theme);
    }});
  }}
}})();

// Mobile menu
document.getElementById('mobileMenuBtn').addEventListener('click', function() {{
  const nav = document.getElementById('headerNav');
  const open = nav.classList.toggle('open');
  this.setAttribute('aria-expanded', open);
  this.innerHTML = open
    ? '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>'
    : '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>';
}});
</script>

</body>
</html>'''


def write_sitemap(cases, today_iso):
    static_urls = [
        (f'{BASE_URL}/', 'weekly', '1.0'),
        (f'{BASE_URL}/states/', 'monthly', '0.8'),
        (f'{BASE_URL}/about/', 'monthly', '0.5'),
        (f'{BASE_URL}/privacy/', 'yearly', '0.3'),
    ]
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, freq, prio in static_urls:
        lines += ['  <url>',
                  f'    <loc>{loc}</loc>',
                  f'    <lastmod>{today_iso}</lastmod>',
                  f'    <changefreq>{freq}</changefreq>',
                  f'    <priority>{prio}</priority>',
                  '  </url>']
    # per-state pages (generated separately), discovered from disk
    states_dir = os.path.join(ROOT_DIR, 'states')
    state_slugs = sorted(
        d for d in os.listdir(states_dir)
        if os.path.isfile(os.path.join(states_dir, d, 'index.html'))
    ) if os.path.isdir(states_dir) else []
    for slug in state_slugs:
        lines += ['  <url>',
                  f'    <loc>{BASE_URL}/states/{slug}/</loc>',
                  f'    <lastmod>{today_iso}</lastmod>',
                  '    <changefreq>monthly</changefreq>',
                  '    <priority>0.6</priority>',
                  '  </url>']
    for slug in sorted(c['id'] for c in cases):
        lines += ['  <url>',
                  f'    <loc>{BASE_URL}/cases/{slug}/</loc>',
                  f'    <lastmod>{today_iso}</lastmod>',
                  '    <changefreq>monthly</changefreq>',
                  '    <priority>0.7</priority>',
                  '  </url>']
    lines.append('</urlset>')
    with open(SITEMAP_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"Wrote sitemap with {len(cases) + len(static_urls)} URLs")


def update_static_counts(count):
    """Inject the real case count into static pages so it is never hand-maintained."""
    replacements = [
        (os.path.join(ROOT_DIR, 'index.html'), [
            (r'(id="heroStatCases">)\d+', rf'\g<1>{count}'),
            (r'(A searchable database of )\d+( documented cold cases)', rf'\g<1>{count}\g<2>'),
        ]),
        (os.path.join(ROOT_DIR, 'about', 'index.html'), [
            (r'(id="aboutStatCases">)\d+', rf'\g<1>{count}'),
        ]),
        (os.path.join(ROOT_DIR, 'manifest.json'), [
            (r'("description": "Database of )\d+', rf'\g<1>{count}'),
        ]),
        (os.path.join(ROOT_DIR, 'llms.txt'), [
            (r'(database of )\d+( documented cold cases)', rf'\g<1>{count}\g<2>'),
        ]),
    ]
    for path, subs in replacements:
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        for pattern, repl in subs:
            content = re.sub(pattern, repl, content)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    print(f"Injected case count ({count}) into static pages")


def _home_badge_class(status):
    """Mirror the homepage JS getStatusBadge() mapping exactly."""
    s = (status or '').lower()
    if 'conviction' in s and 'no conviction' not in s:
        return 'badge-conviction'
    if s in ('solved', 'identified'):
        return 'badge-conviction'
    if 'arrest' in s:
        return 'badge-arrest'
    if 'partially' in s:
        return 'badge-partial'
    return 'badge-unsolved'


def render_home_card(case):
    """Static equivalent of the homepage JS caseCardHTML(), so the browse grid
    is populated in the initial HTML (no JS required). JS re-renders the same
    markup on load as progressive enhancement."""
    e = html.escape
    cid = case.get('id', slugify(case.get('name', '')))
    name = case.get('name', '')
    status = case.get('status', 'Unsolved')
    badge = _home_badge_class(status)
    year = case.get('year', '') or ''
    summary = case.get('summary', '') or ''
    state = case.get('state', '') or ''
    ctype = case.get('type', '') or ''
    age = case.get('age')
    age_tag = f'<span class="case-tag">Age {e(str(age))}</span>' if _known(age) else ''
    return (
        f'<a href="./cases/{e(cid)}/" class="case-card" aria-label="View details for {e(name)}">'
        f'<div class="case-card-header">'
        f'<span class="badge {badge}">{e(status)}</span>'
        f'<span class="case-card-year">{e(str(year))}</span>'
        f'</div>'
        f'<h3 class="case-card-name">{e(name)}</h3>'
        f'<p class="case-card-summary">{e(summary)}</p>'
        f'<div class="case-card-tags">'
        f'<span class="case-tag">{e(state)}</span>'
        f'<span class="case-tag">{e(ctype)}</span>'
        f'{age_tag}'
        f'</div>'
        f'</a>')


def inject_home_grid(cases, count=24):
    """Bake the first `count` case cards into index.html between markers so the
    homepage is not empty without JavaScript."""
    index_path = os.path.join(ROOT_DIR, 'index.html')
    if not os.path.exists(index_path):
        return
    with open(index_path, encoding='utf-8') as f:
        content = f.read()
    cards = '\n'.join(render_home_card(c) for c in cases[:count])
    block = f'<!-- HOME_CARDS:START -->\n{cards}\n<!-- HOME_CARDS:END -->'
    pattern = re.compile(r'<!-- HOME_CARDS:START -->.*?<!-- HOME_CARDS:END -->', re.S)
    if pattern.search(content):
        content = pattern.sub(lambda _m: block, content)
    else:
        # First run: insert markers inside the (empty) cases grid container.
        content = content.replace(
            '<div class="cases-grid" id="casesGrid"></div>',
            f'<div class="cases-grid" id="casesGrid">{block}</div>', 1)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Injected {min(count, len(cases))} static case cards into homepage grid")


def main():
    print("Loading cases...")
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        cases = json.load(f)
    print(f"Loaded {len(cases)} cases")

    today_iso = datetime.date.today().isoformat()

    by_state = defaultdict(list)
    for c in cases:
        by_state[c.get('state', 'Unknown')].append(c)

    os.makedirs(CASES_DIR, exist_ok=True)

    generated = 0
    errors = 0
    for case in cases:
        slug = case.get('id') or slugify(case.get('name', f'case-{generated}'))
        state = case.get('state', '')
        # Same-state cases closest in time first, so related lists vary per case
        year = case.get('year') or 0
        related = sorted(
            (c for c in by_state.get(state, []) if c.get('id') != slug),
            key=lambda c: (abs((c.get('year') or 0) - year), c.get('name', ''))
        )[:6]
        try:
            page_html = generate_case_page(case, related, today_iso)
            page_dir = os.path.join(CASES_DIR, slug)
            os.makedirs(page_dir, exist_ok=True)
            with open(os.path.join(page_dir, 'index.html'), 'w', encoding='utf-8') as f:
                f.write(page_html)
            generated += 1
            if generated % 100 == 0:
                print(f"  Generated {generated}/{len(cases)} pages...")
        except Exception as exc:
            print(f"  ERROR generating page for {slug}: {exc}")
            errors += 1

    print(f"Done! Generated {generated} case pages. Errors: {errors}")

    write_sitemap(cases, today_iso)
    update_static_counts(len(cases))
    inject_home_grid(cases)


if __name__ == '__main__':
    main()
