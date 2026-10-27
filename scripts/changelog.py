"""
Case-level change tracking for /updates/, /feed.xml and the homepage strip.

data/build-state.json only knows that a page's HTML changed, and a template
change moves every page at once. This module keeps a compact snapshot of each
case in data/case-state.json and appends what actually changed to
data/changelog.json every time the build runs:

  added     a case entered the index
  removed   a case left the index (merged, redirected or dropped)
  status    the status field changed (from -> to)
  extended  the timeline gained events and the latest event is new
  revised   anything else changed (narrative, sources, dates, a re-checked timeline)

scripts/seed_changelog.py rebuilds both files from the git history of
data/cases.json if they are ever lost.

Also holds the date helpers shared by the anniversary pages and the
"cases to watch" page, because they have no dependency on the page shell.
"""

import datetime
import hashlib
import json
import os
import re

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
MONTH_NUM = {m: i + 1 for i, m in enumerate(MONTHS)}
KINDS = ('added', 'status', 'extended', 'revised', 'removed')
FEED_KINDS = ('added', 'status', 'extended')


# ─────────────────────────── dates ───────────────────────────

_TEXT_DATE = re.compile(r'^([A-Z][a-z]+)\.?\s+(\d{1,2})(?:\s*[-–]\s*\d{1,2})?,?\s+(\d{4})\b')
_TEXT_MONTH = re.compile(r'^([A-Z][a-z]+)\.?,?\s+(\d{4})\b')
_ISO = re.compile(r'^(\d{4})-(\d{1,2})(?:-(\d{1,2}))?\b')


def parse_date(text):
    """Return (year, month, day) with month/day None when not given, or None.

    Reads the *start* of the text, so a range or a parenthetical after the
    first date ("May 23, 1918 – October 27, 1919", "July 17, 1980 (body
    found)") yields the first date. Accepts "Month D, YYYY", "Month YYYY",
    "YYYY-MM-DD", "YYYY-MM" and "YYYY".
    """
    s = str(text or '').strip()
    m = _ISO.match(s)
    if m:
        y, mo, d = int(m.group(1)), int(m.group(2)), m.group(3)
        if 1 <= mo <= 12:
            d = int(d) if d else None
            if d is not None and not 1 <= d <= 31:
                d = None
            return y, mo, d
        return y, None, None
    m = _TEXT_DATE.match(s)
    if m and m.group(1) in MONTH_NUM:
        d = int(m.group(2))
        return int(m.group(3)), MONTH_NUM[m.group(1)], (d if 1 <= d <= 31 else None)
    m = _TEXT_MONTH.match(s)
    if m and m.group(1) in MONTH_NUM:
        return int(m.group(2)), MONTH_NUM[m.group(1)], None
    m = re.match(r'^(\d{4})\b', s)
    if m:
        return int(m.group(1)), None, None
    return None


def to_date(parsed, last=False):
    """(y, m, d) -> datetime.date. Missing parts become the first (or last)
    possible day so that comparisons are conservative."""
    if not parsed:
        return None
    y, mo, d = parsed
    if mo is None:
        mo = 12 if last else 1
    if d is None:
        if last:
            nxt = datetime.date(y + (mo == 12), (mo % 12) + 1, 1)
            d = (nxt - datetime.timedelta(days=1)).day
        else:
            d = 1
    try:
        return datetime.date(y, mo, d)
    except ValueError:
        return None


def human(parsed):
    if not parsed:
        return ''
    y, mo, d = parsed
    if mo and d:
        return f'{MONTHS[mo - 1]} {d}, {y}'
    if mo:
        return f'{MONTHS[mo - 1]} {y}'
    return str(y)


# Date mentions inside prose, for the "next scheduled date" heuristic.
_MENTION = re.compile(
    r'(?:(?:early|mid|late|mid-)\s+)?'
    r'([A-Z][a-z]+)\.?\s+(?:(\d{1,2})(?:\s*(?:[-–]|to|and)\s*(?:[A-Z][a-z]+\s+)?\d{1,2})?,?\s+)?(\d{4})\b')
_NEGATED = re.compile(r'\b(den(?:y|ies|ied)|vacat(?:e|es|ed)|reject(?:s|ed)?|refus(?:es|ed)|'
                      r'rather than|instead of|moved from|from|postpon(?:es|ed) (?:the|a)|'
                      r'originally|previously|had been|was set)\b', re.I)
_SCHEDULING = re.compile(r'\b(scheduled|is set|are set|set for|set to|due to|expected to|to begin|'
                         r'begins|will (?:begin|start|open|hear|be)|hearing|trial date|retrial|'
                         r'sentencing|arraign|next court)\b', re.I)


def date_mentions(text):
    """Dates written in prose, as [(parsed, start_offset)]."""
    out = []
    for m in _MENTION.finditer(text):
        if m.group(1) not in MONTH_NUM:
            continue
        d = int(m.group(2)) if m.group(2) else None
        if d is not None and not 1 <= d <= 31:
            d = None
        out.append(((int(m.group(3)), MONTH_NUM[m.group(1)], d), m.start()))
    return out


def next_date(events, today, lookback=3):
    """Best guess at the next scheduled date for a case from its newest events.

    events: [(date_text, event_text)] oldest first. Returns a dict with
    'when' (parsed), 'text' (the event the date came from), 'past' (bool)
    and 'source' ('event' when the event itself is dated in the future or is
    the scheduled hearing, 'mention' when the date was read from the prose),
    or None when nothing dated ahead is recorded.
    """
    for date_text, text in reversed(events[-lookback:]):
        own = parse_date(date_text)
        own_day = to_date(own)
        if own_day and own_day > today:
            return {'when': own, 'text': text, 'past': False, 'source': 'event'}
        # dates in the prose that lie after the event's own date and are not negated
        cands = []
        for parsed, pos in date_mentions(text):
            d = to_date(parsed, last=True)
            if not d or (own_day and d <= own_day):
                continue
            window = text[max(0, pos - 45):pos]
            if _NEGATED.search(window):
                continue
            cands.append((to_date(parsed), parsed))
        if cands:
            cands.sort()
            when = cands[0][1]
            return {'when': when, 'text': text, 'past': to_date(when, last=True) < today,
                    'source': 'mention'}
        # the event itself describes a scheduled hearing with no later date given
        if own_day and _SCHEDULING.search(text) and not re.search(
                r'\b(found guilty|convicted|acquitted|sentenced|ruled|pleaded|died|dismissed|concluded|'
                r'ended|verdict|jury finds|rests|announc)', text, re.I):
            return {'when': own, 'text': text, 'past': own_day < today, 'source': 'event'}
        break  # only look further back when the newest event is undated
    return None


# ─────────────────────────── snapshots and diffs ───────────────────────────

def _h(obj):
    return hashlib.sha1(json.dumps(obj, sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()[:12]


def _events(c):
    return [(str(ev.get('date', '')).strip(), str(ev.get('event', '')).strip())
            for ev in (c.get('timeline') or []) if str(ev.get('event', '')).strip()]


def snapshot(c):
    tl = _events(c)
    last = tl[-1] if tl else ('', '')
    return {
        'name': c.get('name') or c['id'],
        'status': c.get('status') or 'Unsolved',
        'events': len(tl),
        'timeline': _h(tl),
        'last_date': last[0],
        'last_event': last[1][:240],
        'text': _h([c.get('summary'), c.get('narrative'), c.get('sources'),
                    c.get('date'), c.get('lastSeen'), c.get('year'), c.get('type')]),
    }


def diff(prev, cur, date):
    """prev, cur: {id: snapshot}. Returns changelog entries dated `date`."""
    out = []
    for cid, s in cur.items():
        p = prev.get(cid)
        if p is None:
            out.append({'date': date, 'id': cid, 'name': s['name'], 'kind': 'added'})
            continue
        changed = False
        if s['status'] != p['status']:
            out.append({'date': date, 'id': cid, 'name': s['name'], 'kind': 'status',
                        'from': p['status'], 'to': s['status']})
            changed = True
        if s['timeline'] != p['timeline']:
            if (p['events'] and s['events'] > p['events']
                    and (s['last_date'], s['last_event']) != (p['last_date'], p['last_event'])):
                out.append({'date': date, 'id': cid, 'name': s['name'], 'kind': 'extended',
                            'count': s['events'] - p['events'],
                            'when': s['last_date'], 'event': s['last_event']})
                changed = True
        if not changed:
            fields = []
            if s['timeline'] != p['timeline']:
                fields.append('timeline')
            if s['text'] != p['text']:
                fields.append('details')
            if s['name'] != p['name']:
                fields.append('name')
            if fields:
                out.append({'date': date, 'id': cid, 'name': s['name'], 'kind': 'revised',
                            'fields': fields})
    for cid, p in prev.items():
        if cid not in cur:
            out.append({'date': date, 'id': cid, 'name': p['name'], 'kind': 'removed'})
    return out


def merge(log, entries):
    """Append entries, folding a repeat of the same (date, id, kind) into one."""
    index = {(x['date'], x['id'], x['kind']): x for x in log}
    for x in entries:
        key = (x['date'], x['id'], x['kind'])
        old = index.get(key)
        if old is None:
            log.append(x)
            index[key] = x
            continue
        if x['kind'] == 'status':
            old['to'] = x['to']                      # keep the original 'from'
            if old['to'] == old['from']:             # changed and changed back
                log.remove(old)
                del index[key]
        elif x['kind'] == 'extended':
            old['count'] = old.get('count', 0) + x.get('count', 0)
            old['when'], old['event'] = x['when'], x['event']
        elif x['kind'] == 'revised':
            old['fields'] = sorted(set(old.get('fields', [])) | set(x.get('fields', [])))
        old['name'] = x['name']
    # a case removed and re-added on the same day is no change at all
    for x in list(log):
        if x['kind'] == 'removed' and (x['date'], x['id'], 'added') in index:
            log.remove(x)
            log.remove(index[(x['date'], x['id'], 'added')])
    log.sort(key=lambda x: (x['date'], KINDS.index(x['kind']), x['name'].lower()))
    return log


def load_json(path, default):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    return default


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        if isinstance(data, list):
            f.write('[\n' + ',\n'.join(json.dumps(x, ensure_ascii=False, sort_keys=True) for x in data) + '\n]\n')
        else:
            json.dump(data, f, indent=0, sort_keys=True, ensure_ascii=False)
            f.write('\n')


def track(cases, today, state_file, log_file):
    """Compare the cases with the last snapshot, append the differences to the
    changelog and store the new snapshot. Returns the full changelog."""
    prev = load_json(state_file, {})
    cur = {c['id']: snapshot(c) for c in cases}
    log = load_json(log_file, [])
    if prev:                       # no snapshot yet: nothing to compare against
        log = merge(log, diff(prev, cur, today))
        if log != load_json(log_file, []):
            save_json(log_file, log)
    if cur != prev:
        save_json(state_file, cur)
    return log
