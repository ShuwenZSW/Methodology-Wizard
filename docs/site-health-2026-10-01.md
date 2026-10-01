# Site Health Report — 2026-10-01

Full internal-audit pass over Tiny Atlas (9 pages, 113 static links, 14 deep-link targets).
Method: static link extraction + resolution against the filesystem, deep-link targets checked
against `methods/data_methods.py` TREE node names, every page rendered headless (Chrome)
with console-message capture.

## Verdict: healthy — one defect found and fixed

| Check | Scope | Result |
|---|---|---|
| Static links exist | 113 hrefs across 9 pages | 113 / 113 OK |
| Anchor fragments | all `#id` links | OK (0 broken) |
| `?m=` deep-link targets | 14 distinct targets vs 92 tree nodes | 14 / 14 match real nodes |
| Console errors | 9 pages, headless render | 0 errors, 0 warnings |
| JS labs produce metrics | SNA playground, Confounding Lab, Evidence Lab, ICA Dilemma Lab | all render computed values |

## Defect found & fixed

**Category deep links landed as dead ends.** The four Field Guides link to the methodology
map with `?m=Social Network Analysis` and `?m=Case-Oriented Comparison` — both are
*category* nodes, which carry no profile card. The map zoomed to the category but opened
nothing, leaving visitors without feedback.

Fix in `methods/template.html` (deep-link handler): when the target is a category
(`children.length > 0`), expand it and mark it `selected` after the fly-in instead of
calling `showMethodPanel` (which early-returns for nodes without profiles). Method nodes
keep the existing open-the-card behavior.

Verified after regeneration (`methods/index.html`):

- `?m=Social Network Analysis` → category expanded, 5 children visible, node selected
- `?m=Case-Oriented Comparison` → category expanded + selected
- `?m=ERGM`, `?m=Process Tracing` → profile panel opens as before

## Page inventory (all render clean)

| Page | Live URL | Interactive surface |
|---|---|---|
| Home | `/` | Expedition banner, feedback box |
| Team | `/team/` | — |
| Field Guides overview | `/guides/` | The Expedition SVG trail map |
| Guide No. 1 Networks | `/guides/sna/` | Network playground |
| Guide No. 2 Causes | `/guides/causal-inference/` | Confounding laboratory |
| Guide No. 3 Cases | `/guides/cases/` | Evidence Lab |
| Guide No. 4 Policy Networks | `/guides/policy-networks/` | ICA Dilemma Lab |
| Methodology map | `/methods/` | 92-node tree, 72 method cards, `?m=` deep links |
| PA map | `/pa/` | 36 theory canon cards |

## Maintenance notes

- `methods/index.html` and `pa/index.html` are generated — edit the matching
  `template*.html` + `data_*.py`, then run `python3 methods/build_site.py` or
  `python3 pa/build_pa.py` (validation: 72 methods / 72 profiles; 36 theories / 36 profiles).
- Deep links strip a trailing `★` before matching, so `?m=Centrality Measures` resolves
  to the node `Centrality Measures ★`. The methodology map takes `?m=<method>`; the PA
  map takes `?t=<theory or branch>`. Category/branch targets expand and highlight;
  leaf targets open their card.
- Field Guides cross-link both maps: method references deep-link into the methodology
  map, discipline references (e.g. Governance & Network Theory) deep-link into the PA map.
