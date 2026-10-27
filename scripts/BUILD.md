# Building ColdCaseIndex

The site is generated. Do not edit the generated HTML by hand.

```
python3 scripts/build.py     # writes every page, site.css, sitemap.xml, data/cases-index.json
python3 scripts/check.py     # QA: titles, descriptions, links, schema, sitemap, data rules
```

## Sources of truth

| File | What it holds |
|---|---|
| `data/cases.json` | Every case. Edit this to change case content. |
| `data/us-homicide-stats.json` | State and yearly homicide clearance figures, with the source. |
| `data/redirects.json` | Old case id to new case id (merged duplicates, renamed URLs), to a path such as `/types/` (entries removed as out of scope), or `null` (removed, no redirect). |
| `data/build-state.json` | Content hash, first-published and last-modified date per page. Written by the build. |
| `data/case-state.json` | Snapshot of each case (status, timeline, last event, content hash). Written by the build; the next build diffs against it. |
| `data/changelog.json` | What changed per case and day: `added`, `removed`, `status`, `extended` (timeline gained events), `revised`. Appended by the build. Feeds `/updates/`, `/feed.xml` and the homepage strip. `scripts/seed_changelog.py` rebuilds it from git history if lost. |
| `scripts/content/*.html` | Body of the about, privacy and 404 pages. |
| `style.css`, `base.css`, `components.css` | Design tokens, reset, components. Concatenated into `site.css`. |
| `home.css` | Homepage-only styles. |

## Generated

`index.html`, `about/`, `privacy/`, `404.html`, `cases/`, `states/`, `types/`, `decades/`,
`updates/` (recent changes, from `changelog.json`), `feed.xml` (Atom, latest 50 additions,
status changes and timeline updates), `watch/` (cases whose status can still change, with the
next scheduled date read from the newest timeline entry), `today/` (cases and timeline events
whose month and day match the build date) and `month/<name>/` (anniversaries by month),
`site.css`, `sitemap.xml`, `data/cases-index.json`.
Redirect stubs for short URLs: `/<decade>s/` (for example `/1990s/`) to `/decades/<decade>s/`, and
`/cases/` to the homepage.

## Daily rebuild

`.github/workflows/daily-rebuild.yml` runs the build and the checks every day at 06:20 UTC and
commits the result when anything changed, so `/today/` follows the calendar and `/watch/` flags
dates that have passed. It commits to `main` as `github-actions[bot]`: pull before pushing local
work.

## Rules the build enforces

- Titles are 60 characters or fewer; descriptions lead with status, type, place and year.
- `lastmod` and `dateModified` only change when a page's content changes.
- The sitemap lists indexable pages only. Privacy, 404, redirect stubs, single-case country
  pages and hubs with fewer than three cases are `noindex`.
- Cases outside the US are grouped under their country in `/states/`.
- Homepage sources that are not about the case itself (a site's front page) are not shown.
- Changes are recorded per case, not per page: a template change moves every page's `lastmod`
  but adds nothing to `changelog.json`. Only a changed status, a longer timeline or edited
  content does.
- Charts use the `--viz-*` tokens in `style.css`. The five status colours were checked for
  colour-blind separation in both themes; keep their order if you change them.

## Case status values

Unsolved, Partially Solved, Identified, Arrest Made, Pending Trial, Wanted, Conviction, Solved,
No Conviction, Ruled Suicide. `check.py` rejects anything else.

## Editorial bar

Never state or imply that someone who has not been convicted is guilty. Acquittals, dismissed
charges, overturned convictions and deaths before trial are stated precisely. People who were
questioned but never charged are left unnamed unless an official source named them.
