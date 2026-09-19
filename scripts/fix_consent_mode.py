#!/usr/bin/env python3
"""
ColdCaseIndex — Consent Mode v2 head-script ordering

Three things have to happen in this order, in every page's <head>:

  1. gtag('consent','default', …all denied…, wait_for_update:500)
     Declares the consent state before any Google tag reads it. This also
     defines window.dataLayer and the gtag() shim, so it must come first.
  2. The AdSense tag. Google's Privacy & Messaging CMP (googlefc, formerly
     Funding Choices) is delivered through it, so it has to be in flight
     before gtag if its consent update is to land inside the 500ms window.
  3. The gtag loader, then gtag('js') / gtag('config').

Previously gtag loaded first and AdSense last, so the CMP's update could not
reach the tag in time and GA had no declared default to wait on.

This script rewrites the hand-maintained pages; the generated pages get the
ordering from HEAD_SCRIPTS in generate_case_pages.py / generate_state_pages.py.
It then verifies the ordering across every HTML file in the repo.

Idempotent. Run from the project root:
    python3 scripts/fix_consent_mode.py
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)

GA_ID = 'G-9D333CYZNN'
ADSENSE_CLIENT = 'ca-pub-5861928596436289'

CONSENT = (
    '<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}'
    "gtag('consent','default',{'analytics_storage':'denied','ad_storage':'denied',"
    "'ad_user_data':'denied','ad_personalization':'denied','wait_for_update':500});</script>"
)
ADSENSE = (
    '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
    f'?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>'
)
GA_LOADER = f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>'
GA_CONFIG = f'<script>gtag("js",new Date());gtag("config","{GA_ID}");</script>'

ORDERED_BLOCK = '\n'.join([CONSENT, ADSENSE, GA_LOADER, GA_CONFIG])

# The old config script also defined dataLayer/gtag; that job moves to CONSENT.
OLD_GA_CONFIG = re.compile(
    r'<script>window\.dataLayer=window\.dataLayer\|\|\[\];'
    r'function gtag\(\)\{dataLayer\.push\(arguments\);\}'
    r'gtag\("js",new Date\(\)\);gtag\("config","' + re.escape(GA_ID) + r'"\);</script>\n?'
)

# Files that are not produced by a generator.
STATIC_PAGES = [
    'index.html',
    'about/index.html',
    'privacy/index.html',
    '404.html',
    'states/greece/index.html',
    'states/aruba/index.html',
]


def reorder(html):
    """Return (new_html, changed) with the head scripts in canonical order."""
    if CONSENT in html:
        return html, False

    for name, needle in (('gtag loader', GA_LOADER), ('adsense tag', ADSENSE)):
        if html.count(needle) != 1:
            raise SystemExit(f'expected exactly one {name}, found {html.count(needle)}')
    if len(OLD_GA_CONFIG.findall(html)) != 1:
        raise SystemExit('expected exactly one legacy gtag config script')

    # Drop the old config and the mis-ordered AdSense tag, then re-emit the
    # whole group in order at the point where the gtag loader used to sit.
    html = OLD_GA_CONFIG.sub('', html)
    html = html.replace(ADSENSE + '\n', '', 1)
    html = html.replace(ADSENSE, '', 1)
    html = html.replace(GA_LOADER, ORDERED_BLOCK, 1)

    # index.html labels the group; the label is now inaccurate.
    html = html.replace(
        '<!-- Google Analytics -->',
        '<!-- Consent Mode v2 defaults, then AdSense (carries the CMP), then GA — order matters -->',
        1,
    )
    return html, True


def verify(path):
    """Return an error string if `path` violates the ordering invariant."""
    with open(path, encoding='utf-8') as f:
        html = f.read()
    if GA_LOADER not in html and ADSENSE not in html:
        return None  # page carries no Google tags at all
    pos = {}
    for name, needle in (('consent', CONSENT), ('adsense', ADSENSE), ('gtag', GA_LOADER)):
        i = html.find(needle)
        if i < 0:
            return f'missing {name}'
        pos[name] = i
    if not pos['consent'] < pos['adsense'] < pos['gtag']:
        return f'out of order: {sorted(pos, key=pos.get)}'
    if OLD_GA_CONFIG.search(html):
        return 'legacy gtag config still redefines dataLayer after the consent block'
    return None


def main():
    changed = 0
    print('Patching hand-maintained pages:')
    for rel in STATIC_PAGES:
        path = os.path.join(ROOT_DIR, rel)
        if not os.path.exists(path):
            print(f'  ! {rel} — missing, skipped')
            continue
        with open(path, encoding='utf-8') as f:
            html = f.read()
        new_html, did = reorder(html)
        if did:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f'  + {rel}')
            changed += 1
        else:
            print(f'  = {rel} — already ordered')

    print(f'\n{changed} file(s) changed. Verifying every page:')
    checked = bad = 0
    for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
        dirnames[:] = [d for d in dirnames if d != '.git']
        for fn in filenames:
            if not fn.endswith('.html'):
                continue
            path = os.path.join(dirpath, fn)
            checked += 1
            err = verify(path)
            if err:
                bad += 1
                print(f'  FAIL {os.path.relpath(path, ROOT_DIR)}: {err}')

    print(f'  {checked - bad}/{checked} pages correctly ordered.')
    if bad:
        print('\nGenerated pages are stale — run generate_case_pages.py '
              'and generate_state_pages.py, then re-run this script.')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
