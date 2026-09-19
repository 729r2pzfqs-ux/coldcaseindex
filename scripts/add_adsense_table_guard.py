#!/usr/bin/env python3
"""
ColdCaseIndex — AdSense data-table guard

Google Auto Ads injects <div class="google-auto-placed"> and <ins class="adsbygoogle">
into whatever container it judges to have room. Inside a table or a flex/grid data
strip that injected node becomes a layout child and shreds the alignment (and on the
homepage it lands inside a <tbody> that JS rebuilds on every sort).

This script fences those regions off:
  * adds id="data-table-zone" to the data-table wrapper on the hand-maintained pages
  * appends the suppression rule to base.css, which every page on the site loads

The generated pages (cases/, states/) carry the id from their generators
(generate_case_pages.py, generate_state_pages.py) — run those to refresh them.

Idempotent: re-running makes no further changes. Run from the project root:
    python3 scripts/add_adsense_table_guard.py
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)

ZONE_ID = 'data-table-zone'

CSS_MARKER = '/* ── AdSense: keep Auto Ads out of data tables ── */'
CSS_BLOCK = f"""
{CSS_MARKER}
#{ZONE_ID} .google-auto-placed,
#{ZONE_ID} ins.adsbygoogle {{ display: none !important; }}
"""

# (path relative to root, wrapper class to tag) — one zone per page keeps the id unique.
TARGETS = [
    ('index.html', 'state-table-wrapper'),
    ('states/greece/index.html', 'state-stats-row'),
    ('states/aruba/index.html', 'state-stats-row'),
]


def tag_wrapper(html, cls):
    """Add id="data-table-zone" to the single <div class="...cls..."> in `html`.

    Returns (new_html, changed). Raises if the wrapper is missing or ambiguous.
    """
    if f'id="{ZONE_ID}"' in html:
        return html, False

    # Match the opening div for `cls`, whether or not it carries other classes.
    pattern = re.compile(r'<div class="([^"]*\b' + re.escape(cls) + r'\b[^"]*)">')
    matches = pattern.findall(html)
    if len(matches) != 1:
        raise SystemExit(f'expected exactly one .{cls} wrapper, found {len(matches)}')

    return pattern.sub(
        lambda m: f'<div id="{ZONE_ID}" class="{m.group(1)}">', html, count=1
    ), True


def patch_css(path):
    with open(path, encoding='utf-8') as f:
        css = f.read()
    if CSS_MARKER in css:
        return False
    with open(path, 'w', encoding='utf-8') as f:
        f.write(css.rstrip('\n') + '\n' + CSS_BLOCK)
    return True


def main():
    changed = 0

    css_path = os.path.join(ROOT_DIR, 'base.css')
    if patch_css(css_path):
        print('  + base.css — added Auto Ads suppression rule')
        changed += 1
    else:
        print('  = base.css — rule already present')

    for rel, cls in TARGETS:
        path = os.path.join(ROOT_DIR, rel)
        if not os.path.exists(path):
            print(f'  ! {rel} — missing, skipped')
            continue
        with open(path, encoding='utf-8') as f:
            html = f.read()
        new_html, did = tag_wrapper(html, cls)
        if did:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f'  + {rel} — tagged .{cls}')
            changed += 1
        else:
            print(f'  = {rel} — already tagged')

    print(f'\nDone. {changed} file(s) changed.')
    print('Generated pages: run generate_case_pages.py and generate_state_pages.py.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
