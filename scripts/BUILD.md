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
| `data/redirects.json` | Old case ids that now point at another case (merged duplicates) or were removed. |
| `data/build-state.json` | Content hash, first-published and last-modified date per page. Written by the build. |
| `scripts/content/*.html` | Body of the about, privacy and 404 pages. |
| `style.css`, `base.css`, `components.css` | Design tokens, reset, components. Concatenated into `site.css`. |
| `home.css` | Homepage-only styles. |

## Generated

`index.html`, `about/`, `privacy/`, `404.html`, `cases/`, `states/`, `types/`, `decades/`,
`site.css`, `sitemap.xml`, `data/cases-index.json`.

## Rules the build enforces

- Titles are 60 characters or fewer; descriptions lead with status, type, place and year.
- `lastmod` and `dateModified` only change when a page's content changes.
- The sitemap lists indexable pages only. Privacy, 404, redirect stubs, single-case country
  pages and hubs with fewer than three cases are `noindex`.
- Cases outside the US are grouped under their country in `/states/`.
- Homepage sources that are not about the case itself (a site's front page) are not shown.
- Charts use the `--viz-*` tokens in `style.css`. The five status colours were checked for
  colour-blind separation in both themes; keep their order if you change them.

## Case status values

Unsolved, Partially Solved, Identified, Arrest Made, Pending Trial, Wanted, Conviction, Solved,
No Conviction, Ruled Suicide. `check.py` rejects anything else.

## Editorial bar

Never state or imply that someone who has not been convicted is guilty. Acquittals, dismissed
charges, overturned convictions and deaths before trial are stated precisely. People who were
questioned but never charged are left unnamed unless an official source named them.
