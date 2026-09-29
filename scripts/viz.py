"""
ColdCaseIndex: inline SVG / HTML figures.

Every figure is static markup themed through the CSS custom properties in
style.css (so light and dark mode both work) and sized by viewBox, so it scales
down to a 375px viewport without horizontal scrolling. Each figure that encodes
values also ships a table or legend carrying the same numbers as text.
"""

import html
import re

e = html.escape

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
MONTH_LOOKUP = {m.lower(): i + 1 for i, m in enumerate(MONTHS)}
MONTH_LOOKUP.update({m[:3].lower(): i + 1 for i, m in enumerate(MONTHS)})
SEASONS = {'winter': 1, 'spring': 4, 'summer': 7, 'fall': 10, 'autumn': 10}

# NPR-style tile grid: (column, row) per state
TILE_GRID = {
    'AK': (0, 0), 'ME': (11, 0),
    'WI': (6, 1), 'VT': (10, 1), 'NH': (11, 1),
    'WA': (1, 2), 'ID': (2, 2), 'MT': (3, 2), 'ND': (4, 2), 'MN': (5, 2), 'IL': (6, 2),
    'MI': (7, 2), 'NY': (9, 2), 'MA': (10, 2),
    'OR': (1, 3), 'NV': (2, 3), 'WY': (3, 3), 'SD': (4, 3), 'IA': (5, 3), 'IN': (6, 3),
    'OH': (7, 3), 'PA': (8, 3), 'NJ': (9, 3), 'CT': (10, 3), 'RI': (11, 3),
    'CA': (1, 4), 'UT': (2, 4), 'CO': (3, 4), 'NE': (4, 4), 'MO': (5, 4), 'KY': (6, 4),
    'WV': (7, 4), 'VA': (8, 4), 'MD': (9, 4), 'DE': (10, 4),
    'AZ': (2, 5), 'NM': (3, 5), 'KS': (4, 5), 'AR': (5, 5), 'TN': (6, 5), 'NC': (7, 5),
    'SC': (8, 5), 'DC': (9, 5),
    'OK': (4, 6), 'LA': (5, 6), 'MS': (6, 6), 'AL': (7, 6), 'GA': (8, 6),
    'HI': (0, 7), 'TX': (4, 7), 'FL': (9, 7),
}

STATE_ABBR = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
    'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI',
    'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
    'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND',
    'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
    'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
}
ABBR_STATE = {v: k for k, v in STATE_ABBR.items()}

# One-hue sequential ramp (amber), light -> dark, with the label ink that clears
# contrast on each step.
SEQ_RAMP = ['#f1e2b4', '#dfc070', '#c29a3c', '#94742a', '#614b17']
SEQ_INK = ['dark', 'dark', 'dark', 'light', 'light']


def parse_when(text):
    """Best-effort fractional year from an ISO or prose date. None if no year."""
    if text is None:
        return None
    s = str(text).strip()
    m = re.match(r'^(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?$', s)
    if m:
        y = int(m.group(1))
        mo = int(m.group(2) or 1)
        d = int(m.group(3) or 1)
        return y + (min(max(mo, 1), 12) - 1) / 12 + (min(max(d, 1), 31) - 1) / 372
    ym = re.search(r'\b(1[5-9]\d\d|20\d\d)\b', s)
    if not ym:
        return None
    y = int(ym.group(1))
    low = s.lower()
    mo = 1
    for word in re.findall(r'[a-z]+', low):
        if word in MONTH_LOOKUP:
            mo = MONTH_LOOKUP[word]
            break
        if word in SEASONS:
            mo = SEASONS[word]
            break
    dm = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?,', s)
    d = int(dm.group(1)) if dm else 1
    return y + (mo - 1) / 12 + (min(d, 31) - 1) / 372


def human_date(text):
    """'1987-03-05' -> 'March 5, 1987'; '1987-03' -> 'March 1987'; prose passes through."""
    s = str(text or '').strip()
    m = re.match(r'^(\d{4})(?:-(\d{1,2}))?(?:-(\d{1,2}))?$', s)
    if not m:
        return s
    y, mo, d = m.group(1), m.group(2), m.group(3)
    if mo and 1 <= int(mo) <= 12:
        if d:
            return f'{MONTHS[int(mo) - 1]} {int(d)}, {y}'
        return f'{MONTHS[int(mo) - 1]} {y}'
    return y


def _plural(n, word):
    return f'{n} {word}' + ('' if n == 1 else 's')


def timeline_strip(events, incident_year, still_open, build_year):
    """Events on a true time axis. `events` is [(date_text, event_text)].

    Returns '' when there is nothing a proportional axis would add (fewer than
    two dated events, or everything inside a single year for a closed case).
    """
    pts = []
    for d, ev in events:
        t = parse_when(d)
        if t is not None:
            pts.append((t, d, ev))
    if len(pts) < 2:
        return ''
    pts.sort(key=lambda p: p[0])
    t0, t_last = pts[0][0], pts[-1][0]
    t1 = max(t_last, build_year + 0.75) if still_open else t_last
    if t1 - t0 < 1:
        return ''

    W, H, x0, x1, y = 720, 104, 16, 704, 50

    def X(t):
        return x0 + (t - t0) / (t1 - t0) * (x1 - x0)

    # incident = first event in the recorded incident year, else the first event
    inc = next((p for p in pts if int(p[0]) == incident_year), pts[0])

    parts = [f'<line class="track" x1="{x0}" y1="{y}" x2="{X(t_last):.1f}" y2="{y}"/>']
    if still_open and t1 > t_last:
        parts.append(f'<line class="track-open" x1="{X(t_last):.1f}" y1="{y}" x2="{x1}" y2="{y}"/>')

    # decade ticks, only when they are far enough apart to read
    span = t1 - t0
    step = 10 if span > 25 else (5 if span > 10 else (1 if span <= 6 else 2))
    first_tick = (int(t0) // step + 1) * step
    labels = []  # (x, text, css)
    tick_years = range(first_tick, int(t1) + 1, step)
    for ty in tick_years:
        parts.append(f'<line class="grid" x1="{X(ty):.1f}" y1="{y - 6}" x2="{X(ty):.1f}" y2="{y + 6}"/>')

    for t, d, ev in pts:
        cls = 'dot-key' if (t, d, ev) == inc else 'dot'
        tip = e(f'{human_date(d)}: {ev}')
        parts.append(
            f'<g class="pt"><circle class="hit" cx="{X(t):.1f}" cy="{y}" r="14"/>'
            f'<circle class="{cls}" cx="{X(t):.1f}" cy="{y}" r="6"><title>{tip}</title></circle></g>')

    # year labels under the axis: first, incident, last, and "today" for open cases
    wanted = [(X(pts[0][0]), str(int(pts[0][0])), 't-strong'),
              (X(inc[0]), str(int(inc[0])), 't-strong'),
              (X(t_last), str(int(t_last)), 't-strong')]
    if still_open and t1 > t_last:
        wanted.append((x1, str(build_year), 't-faint'))
    placed = []
    for x, txt, css in wanted:
        if any(abs(x - px) < 58 for px, _, _ in placed) or any(txt == pt for _, pt, _ in placed):
            continue
        placed.append((x, txt, css))
    for x, txt, css in placed:
        anchor = 'start' if x < 60 else ('end' if x > W - 60 else 'middle')
        parts.append(f'<text class="{css}" x="{x:.1f}" y="{y + 34}" font-size="19" text-anchor="{anchor}">{txt}</text>')

    # one annotation above the axis: elapsed time
    end_t = t1 if still_open else t_last
    years = int(round(end_t - inc[0]))
    if years >= 2:
        if still_open:
            note = f'{years} years since the incident'
        else:
            note = f'{years} years from incident to latest development'
        mid = (X(inc[0]) + X(end_t)) / 2
        mid = min(max(mid, 150), W - 150)
        parts.append(f'<text x="{mid:.1f}" y="22" font-size="18" text-anchor="middle">{note}</text>')

    desc = (f'Timeline from {int(t0)} to {int(t1)} with {len(pts)} dated events. '
            + (f'{years} years have passed since the incident.' if still_open and years >= 2 else ''))
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{e(desc.strip())}" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>')


def tile_map(highlight=None, fills=None, links=None, tips=None, label_all=True):
    """US tile-grid map.

    highlight: state abbreviation drawn in the accent colour (locator use)
    fills:     {abbr: (hex, 'dark'|'light')} for a choropleth
    links:     {abbr: href}; tiles without a link are not clickable
    tips:      {abbr: tooltip text}
    """
    T, G = 44, 4
    W, H = 12 * (T + G) - G, 8 * (T + G) - G
    out = []
    for ab, (cx, cy) in sorted(TILE_GRID.items(), key=lambda kv: (kv[1][1], kv[1][0])):
        x, y = cx * (T + G), cy * (T + G)
        on = ab == highlight
        style = ''
        lab_cls = 'map-label'
        if fills and ab in fills:
            style = f' style="fill:{fills[ab][0]}"'
            lab_cls += ' map-label-dark' if fills[ab][1] == 'dark' else ' map-label-light'
        if on:
            lab_cls += ' map-label-on'
        tip = (tips or {}).get(ab, ABBR_STATE[ab])
        tile = (f'<rect class="map-tile{" map-tile-on" if on else ""}" x="{x}" y="{y}" width="{T}" '
                f'height="{T}" rx="4"{style}><title>{e(tip)}</title></rect>')
        label = (f'<text class="{lab_cls}" x="{x + T / 2}" y="{y + T / 2 + 5.5}">{ab}</text>'
                 if (label_all or on) else '')
        href = (links or {}).get(ab)
        if href:
            out.append(f'<a href="{e(href)}" aria-label="{e(tip)}">{tile}{label}</a>')
        else:
            out.append(f'<g>{tile}{label}</g>')
    return W, H, ''.join(out)


def locator_map(state, links):
    ab = STATE_ABBR.get(state)
    if not ab:
        return ''
    W, H, body = tile_map(highlight=ab, links=links)
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Map of the United States with '
            f'{e(state)} highlighted" xmlns="http://www.w3.org/2000/svg">{body}</svg>')


def choropleth(values, links, fmt, title_attr, bins):
    """values: {abbr: number}. bins: ascending upper bounds, one per ramp step
    (darkest step = lowest value, because a low clearance rate is the finding)."""
    fills, tips = {}, {}
    for ab, v in values.items():
        idx = next((i for i, b in enumerate(bins) if v <= b), len(bins) - 1)
        step = len(SEQ_RAMP) - 1 - idx
        fills[ab] = (SEQ_RAMP[step], SEQ_INK[step])
        tips[ab] = f'{ABBR_STATE[ab]}: {fmt(v)}'
    W, H, body = tile_map(fills=fills, links=links, tips=tips)
    svg = (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{e(title_attr)}" '
           f'xmlns="http://www.w3.org/2000/svg">{body}</svg>')
    return svg


def ramp_legend(labels):
    """Legend for the choropleth; labels run from lowest bin to highest."""
    items = []
    for i, lab in enumerate(labels):
        step = len(SEQ_RAMP) - 1 - i
        items.append(f'<li><span class="swatch" style="background:{SEQ_RAMP[step]}"></span>{e(lab)}</li>')
    return f'<ul class="viz-legend">{"".join(items)}</ul>'


def _nice_max(v):
    for m in (4, 5, 8, 10, 20, 40, 50, 80, 100, 150, 200, 250, 400, 500, 1000):
        if v <= m:
            return m
    return v


def columns(data, links=None, unit='case', label='Cases by decade'):
    """Column chart. data: [(label, value)]. One series, so no legend box."""
    if not data:
        return ''
    n = len(data)
    W, H = 720, 250
    left, right, top, bottom = 44, 12, 24, 40
    pw, ph = W - left - right, H - top - bottom
    vmax = _nice_max(max(v for _, v in data))
    band = pw / n
    bw = min(24, band * 0.6)
    peak = max(v for _, v in data)
    parts = []
    for i in range(0, 5):
        gv = vmax * i / 4
        gy = top + ph - ph * i / 4
        cls = 'axis' if i == 0 else 'grid'
        parts.append(f'<line class="{cls}" x1="{left}" y1="{gy:.1f}" x2="{W - right}" y2="{gy:.1f}"/>')
        txt = f'{gv:g}'
        parts.append(f'<text class="t-faint" x="{left - 8}" y="{gy + 5:.1f}" font-size="15" text-anchor="end">{txt}</text>')
    # thin out x labels when columns are narrow
    every = 1 if band >= 56 else (2 if band >= 30 else 3)
    labelled_peak = False
    for i, (lab, v) in enumerate(data):
        cx = left + band * i + band / 2
        h = ph * v / vmax
        x, y = cx - bw / 2, top + ph - h
        r = min(4, h, bw / 2)
        if v > 0:
            path = (f'M{x:.1f},{top + ph:.1f} V{y + r:.1f} Q{x:.1f},{y:.1f} {x + r:.1f},{y:.1f} '
                    f'H{x + bw - r:.1f} Q{x + bw:.1f},{y:.1f} {x + bw:.1f},{y + r:.1f} V{top + ph:.1f} Z')
            tip = f'{lab}: {_plural(v, unit)}'
            mark = (f'<rect class="hit" x="{cx - band / 2:.1f}" y="{top}" width="{band:.1f}" height="{ph}"/>'
                    f'<path class="series" d="{path}"><title>{e(tip)}</title></path>')
            href = (links or {}).get(lab)
            if href:
                mark = f'<a href="{e(href)}" aria-label="{e(tip)}">{mark}</a>'
            parts.append(mark)
        if v == peak and not labelled_peak:
            labelled_peak = True
            parts.append(f'<text class="t-strong" x="{cx:.1f}" y="{y - 7:.1f}" font-size="16" text-anchor="middle">{v}</text>')
        if i % every == 0:
            parts.append(f'<text x="{cx:.1f}" y="{H - 14}" font-size="15" text-anchor="middle">{e(str(lab))}</text>')
    desc = f'{label}. ' + ', '.join(f'{lab}: {v}' for lab, v in data)
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{e(desc)}" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>')


def line_chart(data, ymin, ymax, ystep, suffix='%', annotate=None):
    """Single-series line chart. data: [(x_label, value)] evenly spaced."""
    n = len(data)
    W, H = 720, 320
    left, right, top, bottom = 48, 56, 20, 40
    pw, ph = W - left - right, H - top - bottom

    def X(i):
        return left + pw * i / (n - 1)

    def Y(v):
        return top + ph - ph * (v - ymin) / (ymax - ymin)

    parts = []
    v = ymin
    while v <= ymax + 1e-9:
        cls = 'axis' if v == ymin else 'grid'
        parts.append(f'<line class="{cls}" x1="{left}" y1="{Y(v):.1f}" x2="{W - right}" y2="{Y(v):.1f}"/>')
        parts.append(f'<text class="t-faint" x="{left - 8}" y="{Y(v) + 5:.1f}" font-size="15" text-anchor="end">{v:g}{suffix}</text>')
        v += ystep
    for i, (lab, _) in enumerate(data):
        if int(lab) % 10 == 0:
            parts.append(f'<text x="{X(i):.1f}" y="{H - 14}" font-size="15" text-anchor="middle">{lab}</text>')
    pts = ' '.join(f'{X(i):.1f},{Y(val):.1f}' for i, (_, val) in enumerate(data))
    area = f'{left},{Y(ymin):.1f} {pts} {X(n - 1):.1f},{Y(ymin):.1f}'
    parts.append(f'<polygon class="series-area" points="{area}"/>')
    parts.append(f'<polyline class="series-line" points="{pts}"/>')
    # hover layer: a hit column per point; the dot and value show on hover
    band = pw / (n - 1)
    for i, (lab, val) in enumerate(data):
        parts.append(
            f'<g class="pt"><rect class="hit" x="{X(i) - band / 2:.1f}" y="{top}" width="{band:.1f}" '
            f'height="{ph}"><title>{lab}: {val:g}{suffix}</title></rect>'
            f'<circle class="dot hover-mark" cx="{X(i):.1f}" cy="{Y(val):.1f}" r="5"/></g>')
    # selective direct labels
    for idx, place in (annotate or []):
        lab, val = data[idx]
        cx, cy = X(idx), Y(val)
        parts.append(f'<circle class="dot" cx="{cx:.1f}" cy="{cy:.1f}" r="5"/>')
        if place == 'end':
            parts.append(f'<text class="t-strong" x="{cx + 10:.1f}" y="{cy + 5:.1f}" font-size="17">{val:g}{suffix}</text>')
        else:
            dy = -12 if place == 'above' else 24
            parts.append(f'<text class="t-strong" x="{cx:.1f}" y="{cy + dy:.1f}" font-size="16" '
                         f'text-anchor="middle">{val:g}{suffix} ({lab})</text>')
    desc = (f'Line chart, {data[0][0]} to {data[-1][0]}. Starts at {data[0][1]:g}{suffix}, '
            f'ends at {data[-1][1]:g}{suffix}.')
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{e(desc)}" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(parts)}</svg>')


def stacked_bar(groups):
    """groups: [(label, count, css_class)]. HTML bar + legend carrying every number."""
    total = sum(c for _, c, _ in groups)
    if not total:
        return ''
    segs = ''.join(
        f'<span class="{cls}" style="flex:{c} 1 0" title="{e(lab)}: {c}"></span>'
        for lab, c, cls in groups if c)
    legend = ''.join(
        f'<li><span class="swatch {cls}"></span>{e(lab)} <strong>{c}</strong> '
        f'({round(c / total * 100)}%)</li>'
        for lab, c, cls in groups if c)
    desc = ', '.join(f'{lab}: {c}' for lab, c, _ in groups if c)
    return (f'<div class="stackbar" role="img" aria-label="{e(desc)}">{segs}</div>'
            f'<ul class="viz-legend">{legend}</ul>')
