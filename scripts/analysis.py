"""
Data behind the /analysis/ pages: how long resolved cases took, and what broke them.

Everything here is derived from the dated timelines in data/cases.json with keyword
rules, so the numbers are reproducible from the published data. The rules are
deliberately simple and are described on the pages themselves.

For each case whose status is Conviction, Solved or Identified:
  inc      year of the crime or disappearance (the case's `year`)
  broke    year of the first timeline event, on or after `inc`, that records the break
           in the case: an arrest, charge, indictment, identification, DNA match or
           confession (for Identified cases, the identification itself)
  closed   year of the first conviction, guilty plea or sentence (Conviction cases)
  method   what produced the break, by the first matching rule in METHODS
"""
import re
import statistics
from collections import Counter, defaultdict

RESOLVED = ('Conviction', 'Solved', 'Identified')

BREAK = re.compile(
    r'\b(is|are|was|were|being|gets|got)\s+(arrested|charged|indicted|detained|taken into custody)\b'
    r'|\b(arrests?|arrested|charges?|charged|indicts?|indicted)\b[^.;]{0,80}\b(suspect|him|her|them|with|for|in connection)\b'
    r'|\bidentif(y|ies|ied|ication)\b[^.;]{0,60}\b(as|through|via|using|by|remains|victim|suspect|killer|perpetrator|source)\b'
    r'|\b(DNA|profile|fingerprints?)\b[^.;]{0,60}\b(match|matched|matches|link|linked|links|identif)'
    r'|\b(match|matched|matches|link|linked|links)\b[^.;]{0,40}\b(DNA|profile|fingerprint)'
    r'|\bconfess(es|ed|ion)?\b'
    r'|\b(pleads?|pleaded|plead)\s+guilty\b|\bconvicted\b|\bfound guilty\b|\bsentenced\b'
    r'|\bnames?\s+[^.;]{0,60}\bas\s+(the|a)\s+(suspect|killer|perpetrator|gunman|shooter)\b'
    r'|\bturn(s|ed)?\s+(himself|herself|themselves)\s+in\b|\bsurrenders?\b',
    re.I)
CLOSED = re.compile(r'\b(convicted|found guilty|pleads? guilty|pleaded guilty|plead guilty|guilty plea|sentenced)\b', re.I)
# Events that look like a break but are not one: a failed or descriptive identification, or
# DNA that only links crimes to each other.
NOT_BREAK = re.compile(
    r"\b(not|cannot|can't|unable|could not|couldn't|fail\w*|without being|remain\w*|yet to be)\b[^.;]{0,25}\bidentif"
    r'|\bunidentified\b'
    r'|\bidentified as (a|an) (white|black|hispanic|latino|young|woman|man|female|male|girl|boy|likely|possible|probable|caucasian|native|asian|teen|child|infant|newborn|adult)'
    r'|\b(single|same) (offender|suspect|killer|perpetrator|person|man|weapon|gun|source)\b'
    r'|\blink(s|ed|ing)? the (crimes|murders|cases|killings|attacks|deaths|rapes)\b'
    r'|\b(no|not|without a|yields? no|yielded no|produces? no|fails? to) (match|hit)',
    re.I)
# For Identified cases only the identification itself counts as the break.
IDENT = re.compile(
    r'\bidentif(y|ies|ied|ication)\b[^.;]{0,80}\b(as|through|via|using|by|thanks)\b'
    r'|\bgenealog|\bgiven (back )?(her|his|their) name|\bconfirm(s|ed)? (the |her |his )?identity'
    r'|\bname(s|d)? (the|her|him|them|the victim|the remains)\b',
    re.I)

# (key, label, regex over the break event, the event before it and the two after it)
METHODS = [
    ('genealogy', 'Genetic genealogy', re.compile(r'genealog|dna doe project|othram|parabon', re.I)),
    ('dna', 'DNA match', re.compile(r'\bDNA\b|\bCODIS\b|genetic profile|\bprofile\b[^.;]{0,30}\bmatch', re.I)),
    ('fingerprint', 'Fingerprint match', re.compile(r'fingerprint|palm print', re.I)),
    ('confession', 'Confession', re.compile(r'confess|turn(s|ed)? (himself|herself|themselves) in|surrender|admits? (to )?(the )?(killing|murder|shooting|strangl)', re.I)),
    ('witness', 'Witness, tip or informant', re.compile(r'witness|came forward|comes forward|tip\b|tips\b|informant|cellmate|jailhouse|accomplice|co-?defendant|testif|cooperat|reward', re.I)),
    ('other-crime', 'Arrest in another case', re.compile(r'traffic stop|unrelated|another (crime|case|murder|attack|offen|assault|robbery|burglary)|separate (case|crime|charge|incident)|attempt(ed|ing)? (to )?(burglar|rob|kidnap|abduct)|escap|surviv', re.I)),
]
METHOD_LABEL = {k: l for k, l, _ in METHODS}
METHOD_LABEL.update({'initial': 'Arrest in the initial investigation', 'other': 'Other or not stated'})
METHOD_ORDER = ['initial', 'genealogy', 'dna', 'confession', 'witness', 'other-crime', 'fingerprint', 'other']


def year_of(text):
    m = re.search(r'\b(1[5-9]\d\d|20\d\d)\b', str(text or ''))
    return int(m.group(1)) if m else None


def classify(c):
    """Record for one resolved case, or None if its timeline holds no datable break."""
    inc = c.get('year')
    if not inc or c.get('status') not in RESOLVED:
        return None
    events = [(year_of(ev.get('date')), str(ev.get('event') or '')) for ev in c.get('timeline', [])]
    events = [(y, t) for y, t in events if y and y >= inc]
    events.sort(key=lambda yt: yt[0])
    rx = IDENT if c['status'] == 'Identified' else BREAK
    broke = next(((i, y) for i, (y, t) in enumerate(events) if rx.search(t) and not NOT_BREAK.search(t)), None)
    if not broke:
        return None
    bi, by = broke
    closed = next((y for y, t in events if y >= by and CLOSED.search(t)), None) if c['status'] == 'Conviction' else None
    # the break event, the one before it and the two after it, within two years of the break
    text = ' '.join(t for y, t in events[max(0, bi - 1):bi + 3] if abs(y - by) <= 2)
    method = 'other'
    for key, _label, mrx in METHODS:
        if mrx.search(text):
            method = key
            break
    if method == 'other' and by - inc <= 1:
        method = 'initial'
    return {'id': c['id'], 'name': c['name'], 'status': c['status'], 'type': c['type'],
            'inc': inc, 'broke': by, 'closed': closed, 'years': by - inc, 'method': method,
            'event': events[bi][1]}


def compute(cases):
    recs, skipped = [], []
    for c in cases:
        if c.get('status') not in RESOLVED:
            continue
        r = classify(c)
        (recs if r else skipped).append(r or c)
    return recs, skipped


def median(xs):
    return statistics.median(xs) if xs else None


def by_decade(recs):
    """[(decade, n, median_years, share_over_10)] by decade of the incident."""
    groups = defaultdict(list)
    for r in recs:
        groups[(r['inc'] // 10) * 10].append(r['years'])
    out = []
    for d in sorted(groups):
        ys = groups[d]
        out.append((d, len(ys), median(ys), round(statistics.mean(ys), 1),
                    sum(1 for y in ys if y >= 10), sum(1 for y in ys if y <= 1)))
    return out


def by_method(recs):
    groups = defaultdict(list)
    for r in recs:
        groups[r['method']].append(r)
    out = []
    for k in METHOD_ORDER:
        rs = groups.get(k, [])
        if rs:
            out.append((k, METHOD_LABEL[k], len(rs), median([r['years'] for r in rs]),
                        sorted(rs, key=lambda r: -r['years'])))
    return out


def buckets(recs):
    edges = [(0, 1, 'Under 2 years'), (2, 5, '2 to 5 years'), (6, 10, '6 to 10 years'),
             (11, 20, '11 to 20 years'), (21, 30, '21 to 30 years'), (31, 40, '31 to 40 years'),
             (41, 10 ** 4, 'More than 40 years')]
    return [(lab, sum(1 for r in recs if lo <= r['years'] <= hi)) for lo, hi, lab in edges]


def by_break_decade(recs):
    """Method mix by the decade in which the case broke."""
    groups = defaultdict(Counter)
    for r in recs:
        groups[(r['broke'] // 10) * 10][r['method']] += 1
    return sorted(groups.items())
