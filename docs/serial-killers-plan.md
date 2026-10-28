# Serial killers category: implementation plan

Status: phase 1 shipped 2026-10-28 (commits 8abaafa6, 2b64d141 and the one carrying this
line). Decisions taken: US only at launch, 3-plus victim threshold, build biggest to smallest
by search volume. Live: 20 profiles, the hub, 51 state pages (6 indexable), 7 lists, timeline,
statistics and both answer pages; 133 checked sources; 9 profiles linked to existing case
files, plus Shelly Knotek under a recorded exception (section 3.4). Next: phase 2, starting with the collect
script's `candidates`, `infobox` and `select` stages and the high-volume states in 2.1.

Target: a new `/serial-killers/` section of coldcaseindex.com aimed at the "serial killers"
keyword cluster (75K/mo head term at KD 17; "california serial killers" 2K at KD 1;
"serial killers by state" 600 with 41K traffic potential), built on the existing generator,
design system and QA rules, and cross-linked with the 96 serial-murder case pages the site
already has.

## 1. What the repo looks like today

### 1.1 Build pipeline

- **There is no Jinja2.** `scripts/build.py` (about 3,150 lines) renders every page with Python
  f-strings. Each page type is a `render_*` function that returns a closure
  `lambda published, modified: page(...)`; the `page()` shell adds head scripts (Mediavine, GA4,
  Ahrefs), meta tags, JSON-LD, header, footer and the Mediavine config div. The plan below
  follows that pattern rather than introducing a template engine.
- `python3 scripts/build.py` writes everything; `python3 scripts/check.py` is the QA gate.
  `.github/workflows/daily-rebuild.yml` runs both daily at 06:20 UTC and commits to `main`.
- `Pages` (build.py line 346) tracks a content hash per page in `data/build-state.json` so
  `lastmod` and `dateModified` only move when content changes. New pages must go through
  `pages.write(path, render, indexable, priority)` to get this and to land in the sitemap.
- Helper modules: `viz.py` (SVG charts: `tile_map`, `locator_map`, `choropleth`, `columns`,
  `stacked_bar`, `line_chart`, `timeline_strip`), `analysis.py` (resolution-time stats),
  `changelog.py` (per-case change tracking), `geo.py` (Albers map).
- CSS: `style.css` (tokens), `base.css` (reset), `components.css` (components), concatenated
  into `site.css` by the build; `home.css` is homepage-only. Fonts are self-hosted.
- Ads: Mediavine, exclusive. Interactive and data containers carry `data-mediavine-no-ads`
  and are single elements so in-content ads land between them, never inside.

### 1.2 URL structure and page types

| Path | Renderer | Notes |
|---|---|---|
| `/` | `render_home` | hero search, stats, filters, newest-first grid, changelog strip |
| `/cases/<id>/` | `render_case` | 780 pages, priority 0.7, `Article` JSON-LD |
| `/states/<slug>/`, `/states/` | `render_region`, `render_states_index` | 50 states + DC + countries; locator map, clearance stats, city chips |
| `/types/<slug>/`, `/decades/<d>s/`, `/themes/<slug>/`, `/cities/<slug>/` | `render_hub` | one generic hub renderer with per-kind title/desc rules; noindex below 3 cases (cities: 5) |
| `/map/`, `/analysis/...`, `/updates/`, `/watch/`, `/today/`, `/month/<m>/` | dedicated renderers | |
| `/about/`, `/privacy/`, `404.html` | `render_static` from `scripts/content/*.html` | |
| short URLs (`/1990s/`, `/cases/`) and removed pages | `redirect_stub` | meta-refresh stubs, noindex |

### 1.3 Case data

`data/cases.json` is a list of 780 objects with a fixed key set: `id, name, type, status, year,
date, state, city, age, gender, summary, lastSeen, tags, sources, narrative, timeline, enriched`
(+ `country` on 99 non-US cases). Status is one of ten values enforced by `check.py`. Tags are
normalised at load time (`TAG_ALIASES`, `normalize_tags`). Derived fields (`_region`,
`_region_slug`, `_group`, `_decade`, `_tags`, `_type_slug`) are added in `load_cases()`.

Existing serial-murder coverage:

| Measure | Count |
|---|---|
| Cases with type `Serial Killer Victims` | 65 |
| Cases tagged `serial killer` (any type) | 96 |
| US states with at least one such case | 26, plus DC and 8 countries |
| Existing hub | `/types/serial-killer-cases/` ("Serial Killer Cases: 65 Cold Cases") |

The existing entries are victim-centred series pages (`green-river-killer`, `btk-victims`,
`golden-state-killer`, `zodiac-killer`). They are the natural targets for profile-to-case links,
but they are not killer profiles and they do not carry victim counts, aliases, birth/death
dates or criminal status.

### 1.4 check.py

Walks every HTML file and enforces: title at most 60 chars, description present and in range,
no Google Fonts, Mediavine tag and config div present, no AdSense or consent-mode code, no
`juhaporraskorpi` or `/Users/` strings, no duplicate ids, every internal link resolves, no
duplicate titles or descriptions site-wide, sitemap lists exactly the indexable non-stub pages,
required freshness pages exist and are indexable, data rules (allowed statuses, year in date,
summary at least 120 chars, no decade tags, 2+ sources warning), map coordinates cached,
changelog and case-state integrity, homepage under 120 KB, `ads.txt` present.

### 1.5 Navigation, sitemap, internal links

- `NAV` has seven entries (Statistics, By State, By Type, By Decade, Map, Analysis, About).
  The footer "Browse" group has eleven links. `llms.txt` lists the URL families.
- Case pages link to: type hub, state page, city hub, decade hub, 6 nearest-in-time cases from
  the same region and 6 tag-similar cases (`related_sets`).
- State pages link to: type chips, city chips, the locator map (every other state), the
  states index.
- Sitemap: every indexable page, sorted by depth, `lastmod` from build-state.
- Site search (`SITE_JS`) fetches `data/cases-index.json` and links every hit to `cases/<id>/`,
  so profiles cannot be added to it without a `url` field (section 7.5).

## 2. Keyword to page mapping

| Query cluster | Page | Primary H1 / title angle |
|---|---|---|
| serial killers, famous serial killers, list of serial killers, american serial killers | `/serial-killers/` | "Serial Killers: Profiles, Lists and Cases by State" |
| serial killers by state, serial killers in [state], [state] serial killers | `/serial-killers/<state>/` | "[State] Serial Killers: N Documented Killers" |
| [name], [name] victims, was [name] caught | `/serial-killers/<name-slug>/` | "[Name]: [alias], N victims, [years]" |
| most prolific serial killers, serial killers with most victims | `/serial-killers/lists/most-victims/` | |
| female serial killers, women serial killers | `/serial-killers/lists/female/` | |
| serial killers never caught, unidentified serial killers, uncaught | `/serial-killers/lists/never-caught/` | |
| serial killers still alive, serial killers on death row | `/serial-killers/lists/still-alive/`, `/serial-killers/lists/executed/` | |
| serial killers of the 1970s/80s, serial killer timeline | `/serial-killers/timeline/` (one page, decade anchors) | |
| serial killer statistics | `/serial-killers/statistics/` | |
| how many serial killers are active in the us (4,300/mo, KD 1) | `/serial-killers/how-many-are-active-in-the-us/` | answer page, section 5.7 |
| what state has the most serial killers (2,600+/mo across variants) | `/serial-killers/which-state-has-the-most/` | answer page, section 5.7 |
| famous serial killers (18,000/mo, KD 0) | `/serial-killers/lists/famous/` | answer-style list |
| female serial killers (11,000/mo) | `/serial-killers/lists/female/` | answer-style list |
| serial killers that were never caught (1,600+/mo, KD 0) | `/serial-killers/lists/never-caught/` | answer-style list |
| serial killers still alive (500/mo, KD 1) | `/serial-killers/lists/still-alive/` | answer-style list |
| child serial killers, truck stop / highway killers, nurse / medical killers | later: `/serial-killers/lists/<topic>/` once data supports 8+ entries each | |

The head term is won by the hub plus the depth behind it, not by the hub alone. The state
pages are the cheapest wins (KD 1 to 5) and ship first together with the profiles they link to.

### 2.1 State priority by monthly search volume

| State | Volume | State | Volume |
|---|---|---|---|
| Wisconsin | 2,000 | Washington | 350 |
| California | 2,000 | Michigan | 300 |
| Texas | 600 | Oregon | 250 |
| Virginia | 600 | New York | 250 |
| Florida | 450 | Colorado | 200 |
| Illinois | 450 | | |
| Ohio | 400 | | |
| Indiana | 350 | | |

About 25 states are under 100 searches a month and stay `noindex` until they have real
depth. Profiles are researched in this order: the 20 priority names in section 3.4 first,
then whatever fills the states above from the top down.

State title phrasing follows each state's higher-volume variant rather than one template:
"Wisconsin Serial Killers" where the "[state] serial killers" form wins, "Serial Killers in
Texas" where the "serial killers in [state]" form wins. The variant lives in a `STATE_PHRASE`
table in the build module; the default is the "[State] Serial Killers" form and known
exceptions (Texas) are listed there.

### 2.2 Competitive position

The incumbent for name queries is Murderpedia: last updated in 2017, no structured data, not
usable on a phone. The profiles here win on what Murderpedia cannot do: a data table on every
page with convicted, confessed and suspected counts kept separate, years active, fate and the
capture method; per-state statistics computed from the dataset; a "last verified" date on
every profile; schema.org markup; a layout that works on a phone.

## 3. Data model

### 3.1 New file: `data/serial-killers.json`

A list of profile objects. The schema mirrors `cases.json` conventions (snake-free camelCase
keys, `sources` as `{title, url}`, `timeline` as dated events, `enriched` flag) so the existing
enrichment tooling and QA habits carry over.

```json
{
  "id": "gary-ridgway",
  "name": "Gary Ridgway",
  "aliases": ["The Green River Killer"],
  "born": "1949-02-18",
  "died": null,
  "gender": "Male",
  "country": "United States",
  "states": ["Washington"],
  "primaryState": "Washington",
  "cities": ["Seattle", "Kent", "SeaTac"],
  "activeFrom": 1982,
  "activeTo": 1998,
  "victims": {"convicted": 49, "confessed": 71, "suspected": "71 to 90+"},
  "victimProfile": "Women and girls, many of them sex workers, aged 15 to 38",
  "method": ["strangulation"],
  "apprehended": "2001-11-30",
  "legalStatus": "Convicted",
  "sentence": "48 consecutive life sentences without parole (2003), one further life sentence (2011)",
  "fate": "Imprisoned",
  "fateDetail": "Washington State Penitentiary, Walla Walla",
  "identificationMethod": "DNA (2001)",
  "summary": "120 to 300 character neutral summary used on cards, meta description and the hub.",
  "narrative": ["Paragraph 1", "Paragraph 2", "..."],
  "timeline": [{"date": "1982-07-15", "text": "Wendy Coffield, 16, found in the Green River."}],
  "cases": ["green-river-killer"],
  "relatedKillers": [],
  "tags": ["sex workers", "dna evidence", "task force"],
  "sources": [{"title": "King County Prosecutor - Ridgway plea statement", "url": "https://..."}],
  "wikipedia": "https://en.wikipedia.org/wiki/Gary_Ridgway",
  "enriched": true,
  "verified": "2026-11-05"
}
```

Field rules (enforced by `check.py`, section 7.4):

- `id`: slug, unique across profiles **and** must not equal any state slug or the reserved
  words `lists`, `timeline`, `statistics`, because all three live under `/serial-killers/`.
- `legalStatus` enum: `Convicted`, `Convicted (overturned)`, `Died before trial`,
  `Killed during arrest`, `Confessed, never tried`, `Charged`, `Suspected, never charged`,
  `Unidentified`. Nothing in the profile may go further than this field. A person with
  `Suspected, never charged` is only included when an official body publicly named them
  (coroner, prosecutor, police) and the profile says so in its first paragraph.
- `fate` enum: `Imprisoned`, `Executed`, `Died in prison`, `Died (other)`, `Suicide`,
  `Killed`, `Released`, `At large`, `Unknown`.
- `victims.convicted` is an integer or null; `confessed` integer or null; `suspected` a
  string because sources give ranges. Counts are always attributed in the narrative.
- `states`: full state names as in `cases.json` so the same `slugify` and `viz.STATE_ABBR`
  work. `primaryState` picks the state page the profile is listed first on; a profile is
  listed on every state in `states`.
- `cases`: ids that must exist in `cases.json`. The build fails otherwise.
- `summary` 120 to 300 chars; `narrative` 400 to 800 words; `timeline` 5 to 20 events;
  `sources` at least 3, every URL HTTP-checked at collection time; Wikipedia counts as one
  source only and never as the sole source for a conviction, sentence or victim count.
- Victims' names appear only when they are already public in cited reporting or court
  records, and never for living survivors unless they have spoken publicly.

### 3.2 Reverse link from cases

No change to `cases.json`. The build derives `case id -> [profile ids]` from the `cases`
arrays, so a case page can show "Offender profile: Gary Ridgway" without editing 780 records.
If a case later needs an explicit link the natural place is a new optional `offenders` key,
but that is not required for phase 1.

### 3.3 Scope of the first dataset (decided)

- **US only at launch.** `country` is always "United States" in phase 1 and 2; the 23
  non-US serial cases on the site are not profiled until a later phase.
- **Inclusion bar: 3 or more victims** in the convicted, confessed or officially attributed
  count, or an unidentified series the site already documents.
- **Order: biggest to smallest by search volume.** The priority names in 3.4 first, then
  profiles that fill the high-volume states in section 2.1.
- Target 150 profiles for launch of phase 3, 200 by the end of phase 4.

### 3.4 Priority profiles (phase 1)

Monthly search volume and keyword difficulty from the keyword review. All have KD under 10.

| Profile | Volume | Profile | Volume |
|---|---|---|---|
| Jerry Brudos | 82,000 | Joseph DeAngelo | 11,000 (KD 2) |
| Israel Keyes | 76,000 | Todd Kohlhepp | 11,000 |
| Albert Fish | 71,000 | Danny Rolling | 10,000 (KD 1) |
| Edmund Kemper | 29,000 (KD 3) | Randy Kraft | 9,700 |
| Richard Cottingham | 22,000 | Shawn Grate | 9,600 |
| Charles Cullen | 19,000 (KD 3) | Nannie Doss | 9,400 (KD 0) |
| Bobby Joe Long | 18,000 (KD 0) | Robert Berdella | 9,100 |
| Dean Corll | 18,000 | Carl Panzram | 8,700 (KD 0) |
| Gary Heidnik | 13,000 (KD 1) | Shelly Knotek | 8,400 (see note) |
| Joel Rifkin | 12,000 (KD 3) | Anthony Sowell | 8,300 |

Note on Shelly Knotek: she was convicted of two killings (second-degree murder of Kathy
Loreno, manslaughter of Ron Woodworth); the third death in the household, Shane Watson, was
her husband's conviction. She does not meet the 3-victim bar as the data model counts it.
Decision 2026-10-28: included under a recorded exception (`THRESHOLD_EXCEPTIONS` in the
build module) for search volume and notoriety; the profile states the counts exactly. Gary
Ridgway was added as well because the site already has the Green River case page.

Existing case pages that these profiles link to: `israel-keyes-victims`, `dean-corll`,
`gary-heidnik`, `golden-state-killer`, `todd-kohlhepp`, `gainesville-ripper`,
`anthony-sowell`, `green-river-killer`.

## 4. Data collection

### 4.1 Sources, in order of trust

1. **Court and government records** for status, sentence and counts: state DOC inmate
   lookups, state supreme court opinions (Justia, CourtListener), DOJ and FBI press releases,
   state AG releases. These settle `legalStatus`, `sentence`, `fate`.
2. **Established reporting**: AP, Reuters, major regional papers, the same outlets the case
   pages already cite. Needed for narrative claims and victim counts that courts never
   adjudicated.
3. **Wikipedia** as the candidate list and as a cross-check, not as the final citation:
   - `List of serial killers in the United States`: columns Name, Years active, Proven
     victims, Possible victims, Fate, Notes (state is only inside Notes), roughly 500 rows plus
     a separate "Unidentified serial killers" section.
   - `List of serial killers by number of victims`: Name, Country, Years active, Proven,
     Possible, Notes; useful for the most-victims list and for the international bucket.
   - Each killer's article uses `Template:Infobox serial killer` with structured fields
     (`victims`, `beginyear`, `endyear`, `country`, `states`, `apprehended`,
     `criminal_status`, `conviction`, `penalty`). The MediaWiki API returns wikitext, which
     is far easier to parse than the rendered tables.
   - Wikipedia text is CC BY-SA. Facts are reused; prose is never copied. Each profile cites
     the article as one source.
4. **Radford/FGCU Serial Killer Database** (Aamodt, 4,700+ offenders compiled from court and
   prison records). Used two ways: as a candidate and cross-check list for the `select`
   stage (name, state, years, counts, fate), and as the cited source for national and
   per-state figures on the statistics and answer pages. The raw database is not
   redistributed; its published reports are cited.
5. **Murder Accountability Project** (murderdata.org, 638,000 homicide records, free
   download; already linked in the footer). Used for the answer pages: clearance context,
   the MAP algorithm's cluster estimates of uncaught serial offenders, and per-state
   unsolved counts that put the site's own numbers in proportion.

Not used: Murderpedia, fan wikis, true-crime podcasts, Reddit.

### 4.2 Script: `scripts/serial_killers_collect.py`

Runs by hand, never from the daily build (the build never calls the network). Stages are
separate subcommands so each can be rerun and reviewed:

```
python3 scripts/serial_killers_collect.py candidates   # Wikipedia lists -> data/work/sk-candidates.json
python3 scripts/serial_killers_collect.py infobox      # per-article infobox -> sk-candidates.json (merged)
python3 scripts/serial_killers_collect.py select       # apply inclusion rules, map to states, print gaps
python3 scripts/serial_killers_collect.py draft ID...  # write data/work/sk-drafts/<id>.json skeletons
python3 scripts/serial_killers_collect.py verify       # HTTP-check every source URL in drafts
python3 scripts/serial_killers_collect.py merge        # validated drafts -> data/serial-killers.json
```

- `candidates`: fetch the two list pages through the MediaWiki API (`action=parse`,
  `prop=wikitext`), parse the table rows, keep Name, article title, years, proven, possible,
  fate, notes. Extract state names from Notes with the `viz.STATE_ABBR` vocabulary; rows with
  no state become "needs state" for the infobox stage.
- `infobox`: for each candidate fetch the article wikitext, parse the serial-killer infobox
  into the schema fields, record the article revision id and the fetch date.
- `select`: inclusion rules from 3.3, plus a hand-maintained `data/work/sk-include.txt`
  (ids to force in or out) so editorial decisions survive reruns. Prints per-state coverage
  so the gap list drives the next research batch.
- `draft`: skeleton JSON with the structured fields filled and `narrative`, `timeline`,
  `summary` empty. Writing those is the research step from the existing enrichment pipeline:
  one agent per profile, batches of 10 to 30, every claim attributed, every URL opened and
  checked. Keep batches small and merge as they finish (see memory: research control).
- `verify`: HEAD/GET every URL, drop dead links, fail any draft that ends with fewer than 3
  live sources, check the word counts and enums, check `cases` ids exist, check slug
  collisions.
- `merge`: deterministic write of `data/serial-killers.json` with `indent=1` like
  `cases.json`, sorted by id.

Network fetches land in `data/work/` (gitignored except `sk-include.txt`). The daily build
only reads `data/serial-killers.json`.

### 4.3 Editorial rules carried over

The site's existing bar applies in full (BUILD.md "Editorial bar", about page "Standards we
hold to", the audit rulings): never imply guilt without a conviction, state acquittals and
overturned convictions precisely, never name uncharged persons of interest, no invented
sources. For this category add:

- A profile exists for a named living person only with a conviction, a formal charge, or an
  official public attribution. Suspects named by journalists or by other inmates are out.
- Counts are stated as what a court found, what the person confessed to, and what police
  attribute, as three separate numbers, never blended into one.
- No crime-scene detail beyond what is needed to describe the method and identification.
  Mediavine sells against this content; keep it documentary, not lurid.
- Victims are the subject of the `cases` pages; the profile's victims table lists names only
  where the case page or cited reporting already does.
- Nothing is ever ranked or described by attractiveness, charm or notoriety. Lists sort by
  counts, dates and names only.
- Victims are named only from the public record (court documents, official releases,
  established reporting). Never from social media or forums.
- Every profile leads with facts: who, where, when, counts, legal outcome. Biography comes
  last and stays short.
- Every profile carries a corrections and family contact line pointing at
  `info@coldcaseindex.com`, and a "last verified" date.
- Pending cases use "accused" or "charged" throughout, badge and text (Kohberger-type
  cases), and the `Charged` status is the only claim the page makes.

## 5. Page types

All pages use `prefix` relative links like the rest of the site (`../` from a state or
profile, `../../` from a list). Breadcrumbs: Home > Serial Killers > [State | Name | Lists > List].

### 5.1 `/serial-killers/` hub

Sections, top to bottom:

1. Heading, intro (what the section is, the inclusion bar, counts: N profiles, N states,
   N linked case pages, N still unidentified).
2. Stat row: profiles, convicted, unidentified, executed, still imprisoned (reuse
   `stat_row`, `data-mediavine-no-ads`).
3. **By state**: `viz.tile_map` shaded by profile count, each tile linking to
   `/serial-killers/<state>/`, with a text list of all 50 states and DC and their counts
   underneath (the text list is what ranks; the map is navigation).
4. **Most searched / famous**: 12 profile cards chosen by a hand-ordered `featured` list in
   the data (Bundy, Gacy, Dahmer, Ridgway, Ramirez, BTK, Zodiac, Golden State Killer...).
5. **Lists**: cards linking to each list page with its count.
6. **Timeline and statistics**: two cards.
7. **Linked cold cases**: the 65 `Serial Killer Victims` cases as a compact grid link to the
   existing type hub ("All 65 serial killer case files").
8. Methodology note and correction contact (`info@coldcaseindex.com`).

JSON-LD: `CollectionPage` + `ItemList` of state pages + `BreadcrumbList`.

### 5.2 `/serial-killers/<state>/` (50 + DC)

1. H1 "[State] Serial Killers", intro sentence with count, active-year span, earliest and
   latest profile, how many have linked case files, how many unidentified.
2. Locator map (reuse `viz.locator_map`, links to every other state's serial-killers page).
3. Profile cards sorted by first active year (name, alias, years active, victims, status
   badge, one-line summary).
4. "Cold case files from [State]": the serial-murder case cards from `cases.json` for that
   state (links to `/cases/<id>/`), plus "All [State] cold cases" link to `/states/<slug>/`.
5. Neighbouring and other states: hub-links row (same pattern as `HUB_OTHERS`).
6. Short state note (2 to 4 sentences, hand-written in `data/serial-killers-states.json`,
   optional) on patterns worth stating: the Highway Serial Killings Initiative for I-40
   states, Washington's Green River task force, California's volume. Only where a source
   supports it.

Indexing rule: a state page is indexable when it has 2 or more profiles and the state is
not in the under-100-a-month tier (section 2.1); the `STATE_VOLUME` table in the build
module holds the known volumes and the tier. With 1 profile the page is built but
`noindex,follow`; with 0 it is a short "no documented profiles yet" page linking to the
state's cold cases, `noindex,follow`. The 51 URLs stay stable while the dataset grows.
Title uses the state's phrasing variant: "[State] Serial Killers: N Documented Profiles" or
"Serial Killers in [State]: N Profiles" (fallback drops the count if over 60 chars).

JSON-LD: `CollectionPage` + `ItemList` of profiles.

### 5.3 `/serial-killers/<name-slug>/` profile (150 to 200)

1. Header: name, alias line, status badge (reuse `.badge` classes: Convicted = conviction,
   Unidentified = unsolved, Charged = arrest, Suspected = partial, others = neutral).
2. Details grid (reuse `case-details-grid`): Active years, States (links), Victims
   (convicted / confessed / suspected on separate lines), Method, Apprehended,
   Identification, Legal status, Sentence, Fate, Born / Died.
3. Summary paragraph.
4. Timeline to scale (`viz.timeline_strip`) and the dated timeline list (reuse `.timeline`).
5. Narrative, 400 to 800 words, each paragraph attributed as on case pages.
6. **Case files**: cards for every linked case (`/cases/<id>/`), heading "Victims and case
   files on ColdCaseIndex".
7. Related profiles: same state (up to 4) and same era or method (up to 4), computed like
   `related_sets`.
8. Sources list, cite box (`cite_html`), correction note with `info@coldcaseindex.com`.

Title formula, tried in order until one fits 60 chars: "[Name], the [Alias]: [N] Victims,
[years]"; "[Name]: Serial Killer, [State], [years]"; "[Name] | ColdCaseIndex". Description:
status-first like `case_desc` ("Convicted. Gary Ridgway, the Green River Killer, pleaded
guilty to 49 murders in Washington, 1982 to 1998. Timeline, victims, sources."), fitted to
158.

JSON-LD: `Article` (headline, description, datePublished, dateModified, publisher) with
`about: {"@type": "Person", "name": ..., "alternateName": [...]}` and `BreadcrumbList`. No
`Person` as the top-level entity: the page is an article about the person, and Google's
profile-page markup is for the subject's own page.

### 5.4 `/serial-killers/lists/` and `/serial-killers/lists/<list>/`

Lists are computed from the data, not curated by hand, so they stay correct as profiles are
added. Each list page: intro (how the list is defined, in one sentence), a sortable
`data-table` (rank, name, alias, state, years, count, status) inside `table-wrap`, then
profile cards. Launch lists:

| Slug | Definition | Sort |
|---|---|---|
| `most-victims` | US profiles by convicted count, with confessed and suspected columns | convicted desc |
| `female` | `gender == "Female"` | first active year |
| `never-caught` | `legalStatus == "Unidentified"` or `fate == "At large"` | first active year |
| `still-alive` | `died == null` and fate in Imprisoned, Released, At large | name |
| `executed` | `fate == "Executed"` | execution date from timeline |
| `died-in-prison` | `fate == "Died in prison"` | name |
| `by-decade` | one page, H2 per decade of first activity, anchors `#1970s` | decade |

A list is only indexable with 8 or more entries; the lists index shows every list with its
count. JSON-LD `ItemList` with `itemListOrder`.

### 5.5 `/serial-killers/timeline/`

One long page: a `viz.columns` chart of profiles by decade of first known murder, then a
chronological list grouped by decade with year, name, state, count. Each decade heading is an
anchor so `/serial-killers/timeline/#1980s` can be linked from decade hubs.

### 5.6 `/serial-killers/statistics/`

Built like the analysis pages (`analysis_page` shell, computed every build): profiles by
state (choropleth), by decade, victims by method, time from first murder to arrest
(`timeline_strip` logic reused), share identified by DNA or genealogy, share unidentified.
Every figure has a "Show as table" details block as on the decade figures. Cite the
Radford/FGCU reports and MAP for the national context sentences; everything else is
computed from the site's own dataset and says so.

### 5.7 Answer pages

Two question pages are generated from the dataset plus a small hand-maintained
`data/serial-killers-facts.json` of cited national figures (FBI definition and estimates,
Radford/FGCU counts by decade and state, MAP cluster estimates), each fact with its source
URL so the page can cite it inline:

- `/serial-killers/how-many-are-active-in-the-us/`: H1 "How Many Serial Killers Are Active
  in the US?" Opens with the direct answer (the cited estimates and why they differ), then
  the site's own counts: profiles by decade of activity, how many profiles have `fate`
  `At large` or `legalStatus` `Unidentified`, how many were caught within a year, a decade,
  never. Links to the never-caught list and the statistics page.
- `/serial-killers/which-state-has-the-most/`: H1 "Which State Has the Most Serial
  Killers?" Direct answer first (Radford/FGCU ranking, with the per-capita caveat), a
  choropleth and a ranked table of the site's profiles by state, with each row linking to
  the state page. Links to the hub's by-state section.

The four list pages with answer-style demand (famous, female, never caught, still alive)
open with a two-sentence direct answer and a definition of the list before the table.

## 6. Template and design

- Reuse first: `section`, `section-inner`, `section-heading`, `section-subtext`,
  `breadcrumb_html`, `badge`, `stat_row`, `case-details-grid`, `cases-grid`, `case-card`,
  `related-grid`, `hub-links`, `breakdown-row` / `breakdown-chip`, `figure.viz`,
  `table-wrap` / `data-table`, `timeline`, `cite-box`, `how-to-help`.
- New CSS, appended to `components.css` under one `/* ── Serial killers ── */` block:
  `.profile-card` (a `case-card` variant with an alias line and a victims figure),
  `.victims-row` (three labelled numbers), `.sk-status` modifiers if the badge colours need
  one extra state. Use only `--color-*`, `--space-*`, `--text-*` tokens. No new colours:
  the five status colours were checked for colour-blind separation and the plan maps every
  legal status onto one of them.
- Every chart, table, map and the details grid is a single element with
  `data-mediavine-no-ads`. Narrative paragraphs are plain `<p>` siblings so Mediavine can
  place in-content units between them.
- No images of offenders. The site has none for cases and adding portraits raises rights
  and taste problems for no ranking gain.
- Dark mode works automatically through the tokens; verify the tile map fills in both themes.

## 7. Build system integration

### 7.1 New module `scripts/serial_killers.py`

Keeps build.py from growing by another thousand lines. Exposes:

```
load(path) -> list[profile]        # validate, derive _slug, _states, _decade, _group
index(profiles, cases) -> dict     # by_state, by_case, featured, lists
render_hub(...), render_state(...), render_profile(...), render_list(...),
render_lists_index(...), render_timeline(...), render_statistics(...)
```

Each render function returns `(render_closure, indexable)` exactly like `render_hub`, and
imports `page`, `breadcrumb_html`, `badge`, `stat_row`, `case_card`, `fit`, `slugify`,
`plural` from build.py (circular import avoided by passing them in through an `init(build)`
call, the way `analysis.py` is already structured as a pure computation module).

### 7.2 Changes to `build.py`

- `main()`: after case pages and before region pages, `profiles = serial_killers.load(...)`,
  build the index, write hub, 51 state pages, profiles, lists, timeline, statistics through
  `pages.write`. Priority 0.7 for profiles and state pages, 0.8 for the hub.
- `render_case`: when a case id has linked profiles, add an "Offender profile" row to the
  details grid and a "Profiles" card block above related cases.
- `render_region`: when a US state has 1+ profiles, add a hub-link "Serial killers in
  [State] (N)" next to the type chips.
- `render_hub` for `types/serial-killer-cases`: add a `links` block pointing at
  `/serial-killers/` (the hub renderer already accepts `links`).
- Decade hubs: link to `/serial-killers/timeline/#<decade>` when that decade has profiles.
- `NAV`: add `('serial-killers/', 'Serial Killers')`. Seven entries become eight; check the
  header at 768 to 1024 px, where the nav already wraps into the mobile menu. If it does not
  fit, replace `Statistics` (an anchor to the homepage) with the new entry.
- Footer "Browse": add "Serial killers".
- Homepage: one card in the browse chips row ("Serial killers by state").
- `write_search_index`: add profiles as rows with `type: "Serial Killer"` and a `url` field;
  change `SITE_JS` and `HOME_JS` to use `c.url || 'cases/' + c.id + '/'`.
- `llms.txt`: add the dataset and URL family.
- Redirects: `data/redirects.json` only covers `/cases/`; add the same stub logic for
  `/serial-killers/` so renamed profile slugs never 404 (a `serial-killers-redirects.json`
  or a `redirects` section keyed by path).
- Stale-directory cleanup under `/serial-killers/`: same pattern as `cases/` (stub or
  remove), so the daily build is idempotent.

### 7.3 Changelog and feed

Phase 1 leaves `changelog.json` and the feed untouched: they are keyed by case id and
`check.py` validates that. Phase 3 can add `kind: "profile-added"` entries once the profile
set is stable, so `/updates/` and the feed announce new profiles.

### 7.4 `check.py` additions

- `data/serial-killers.json` parses; ids unique; ids do not collide with state slugs or
  reserved words; enums valid; `cases` ids exist; summary length; at least 3 sources;
  `states` are known state names; `activeFrom <= activeTo`; `born < activeFrom`.
- A page exists for every profile; no orphan directories under `/serial-killers/` that are
  not stubs.
- `/serial-killers/`, `/serial-killers/lists/`, `/serial-killers/timeline/`,
  `/serial-killers/statistics/` exist and are indexable; 51 state pages exist.
- Every state page with 2+ profiles is indexable and in the sitemap; with fewer it is
  `noindex`.
- Existing global checks (title length, unique descriptions, link resolution, Mediavine tag)
  cover the new pages automatically. Unique descriptions matter: the formulas in section 5
  include name, state and count so 200 profiles and 51 states cannot collide.

### 7.5 Search

`cases-index.json` grows by about 200 rows (roughly 30 KB). Acceptable. The profile row
carries `url: "serial-killers/<id>/"` and the search meta line shows "Serial killer ·
[State] · [years]".

## 8. Internal linking

| From | To | Mechanism |
|---|---|---|
| Profile | linked case pages, state serial-killers page, state cold-cases page, related profiles, lists it appears on, hub | sections 5.3 |
| Case page (serial type) | offender profile(s) | details row + card block |
| State cold-cases page | state serial-killers page | hub-link when count > 0 |
| State serial-killers page | profiles, state cold-cases page, serial case cards, all other states | sections 5.2 |
| Type hub `/types/serial-killer-cases/` | `/serial-killers/` | `links` block |
| Decade hubs | timeline anchor | hub-link |
| Homepage, nav, footer, llms.txt | hub | one link each |
| Lists | profiles | table and cards |
| Analysis index | statistics page | card |

Every profile is reachable within two clicks from the hub (hub > state > profile) and from
at least one case page, so nothing depends on the lists for discovery.

## 9. SEO

- Titles 60 chars max and descriptions 158 max through `fit`, with the fallbacks above;
  `check.py` already fails anything longer or duplicated.
- Canonicals, Open Graph and Twitter card come from `page()`. The shared `og-image.png` is
  fine for launch; per-state OG images are not worth the build time.
- JSON-LD per page type as in section 5; all pages get `BreadcrumbList`. Add a `Dataset`
  entry for `data/serial-killers.json` on the hub, mirroring the homepage `Dataset` block
  (same CC BY-NC 4.0 licence field that GSC asked for).
- Sitemap: automatic through `pages.write`. State pages with fewer than 2 profiles stay out.
- Content depth: profiles under 400 words are not published (the `verify` stage refuses
  them). Thin profiles would compete with Wikipedia on nothing.
- The existing type hub keeps its URL and title; the new hub does not cannibalise it because
  the type hub is about case files and says so in its first line, and each links to the other.
- `robots.txt` gets `Disallow: /docs/` so this plan and later docs are not indexed (they are
  served by GitHub Pages like everything else in the repo). That line is added in the same
  commit as this document.

## 10. Phasing

| Phase | Deliverable | Pages | Size |
|---|---|---|---|
| 0 | Review this plan; decide open questions below | 0 | |
| 1 | Schema, `serial_killers.py` renderers for every page type, `check.py` rules, CSS, nav and back-links, the 20 priority profiles of section 3.4, answer pages and lists live with that data | about 85 | in progress |
| 2 | Collect script (`candidates`, `infobox`, `select` against Wikipedia and Radford); profiles for the high-volume states of 2.1 until each has 5+; the 60 profiles tied to existing series cases | about 100 | research in batches of 10, merged and pushed as they finish |
| 3 | Profiles to 150 by state gaps and volume; changelog entries for profiles; remaining lists | about 70 | same cadence |
| 4 | Topic lists (highway, medical, child victims), international bucket, per-state notes | 10 to 20 | |

Phase 2 ships only when every published profile passes `verify` and `check.py` is clean.
The daily rebuild then keeps `lastmod`, lists and statistics current without any network
access.

## 11. Risks and how the plan handles them

- **Invented facts and dead URLs** (the September 2026 audit found both in batch-added
  cases): the `verify` stage HTTP-checks every URL and refuses drafts under 3 live sources;
  narratives attribute every claim; the structured fields are cross-checked against the
  infobox and at least one court or government source.
- **Defamation and living people**: the inclusion rule in 4.3; the `legalStatus` enum is the
  strongest statement the page makes; disputed convictions use `Convicted (overturned)` and
  say what the court found.
- **Ad policy**: documentary tone, no gore, no images. Mediavine's config div already blocks
  interstitials and the sticky unit site-wide.
- **Duplicate titles or descriptions** across 250 new pages: formulas carry name, state and
  count; `check.py` fails the build on any duplicate.
- **Slug namespace** under `/serial-killers/`: collision check in `check.py` and in the
  collect script; profile slugs are always `first-last` or `first-last-year`.
- **Build time**: the current build takes well under a minute; 250 more pages adds seconds.
- **Scope creep in research**: fixed batch sizes, plain progress counts, merge and push after
  every batch (memory: research control).

## 12. Decisions and remaining questions

Decided 2026-10-28: US only at launch; 3-victim threshold; build order by search volume;
victims named only from the public record; pending cases use "accused" or "charged".

Still open:

1. Nav: "Serial Killers" is added as an eighth item in phase 1; if the header wraps badly at
   tablet widths it replaces the "Statistics" anchor.
2. `Suspected, never charged` profiles: allowed with an official attribution, or excluded?
3. Should profiles enter `/updates/` and the Atom feed in phase 2 rather than phase 3?

## Appendix A. Existing serial-murder cases by state

Counts of cases typed `Serial Killer Victims` or tagged `serial killer`, which seed the
profile-to-case links and the first 60 profiles.

| Region | Cases | Example ids |
|---|---|---|
| California | 16 | zodiac-killer, golden-state-killer, night-stalker, hillside-strangler, grim-sleeper |
| Texas | 7 | dean-corll, henry-lee-lucas-victims, texas-killing-fields, the-texarkana-moonlight |
| New York | 7 | son-of-sam-victims, long-island-serial-killer, alphabet-murders-1970s |
| Florida | 6 | ted-bundy-victims, aileen-wuornos, gainesville-ripper, christopher-wilder-1984 |
| Louisiana | 4 | new-orleans-ax-man, jeff-davis-8, derrick-todd-lee-2003 |
| Alaska | 3 | robert-hansen-victims, israel-keyes-victims, eklutna-annie-1980 |
| Washington | 3 | green-river-killer, robert-yates-victims, ted-bundy-washington |
| Ohio, Massachusetts, Kansas, Michigan, Virginia, Pennsylvania, New Hampshire | 2 each | torso-murders, boston-strangler, btk-victims, oakland-county-child-killer, colonial-pkwy-murders, gary-heidnik, bear-brook-murders |
| Illinois, Wisconsin, Georgia, Indiana, Maryland, South Carolina, Wyoming, Nevada, DC, New Mexico, New Jersey, Hawaii, Montana | 1 each | john-wayne-gacy, jeffrey-dahmer, wayne-williams-victims, i-70-killer, todd-kohlhepp, freeway-phantom-1971, west-mesa-murders-2009, honolulu-strangler-1985 |
| Non-US (UK, Canada, Australia, Italy, Russia, Japan, Ecuador) | 23 | peter-sutcliffe-yorkshire-2020, robert-pickton-victims, ivan-milat-backpacker-1996, andre-chikatilo-1992 |

24 states have no serial-murder case on the site today: those state pages depend entirely on
new profiles, which is why the phase 3 selection is driven by state gaps.
