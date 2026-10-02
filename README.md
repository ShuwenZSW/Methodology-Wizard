# Tiny Atlas

**Small maps of big fields** — an open, growing atlas of research knowledge,
maintained by the ReGovNet Research Group as a small, beautiful scholarly
community. New maps join the atlas as new pages, so the name (and the URLs)
never go stale.

| Map | What's inside | Live URL |
|---|---|---|
| **Home** | Group introduction, map entries, community feedback box | https://shuwenzsw.github.io/Methodology-Wizard/ |
| **Methodology Map** | 3 paradigms · 16 categories · 72 methods, each with an adoption card (when to use, data, assumptions, skill, priority) | https://shuwenzsw.github.io/Methodology-Wizard/methods/ |
| **Public Administration Map** | 3 schools · 9 branches · 36 theories, each with a canon card (core proposition, key concepts, founders, classic readings, frameworks, research-design guide) — supports `?t=` deep links | https://shuwenzsw.github.io/Methodology-Wizard/pa/ |
| **Measurement Map** | 7 branches · 35 concepts — scales of measurement, validity, reliability, error & bias, data sources, sampling & coverage, comparability — each with a canon card (core proposition, key concepts, founders, classic readings, frameworks, research-design guide) — supports `?t=` deep links | https://shuwenzsw.github.io/Methodology-Wizard/measure/ |
| **Team** | The ReGovNet Research Group — regional governance, governance networks, interlocal management; methodological strengths in causal inference and social network analysis; led by Shuwen Zhang | https://shuwenzsw.github.io/Methodology-Wizard/team/ |
| **Field Guides overview** | "The Expedition" — the seven guides' model paths drawn as one interactive trail map, with a measurement base camp, cross-trail arcs, a frontier branch, and guide cards | https://shuwenzsw.github.io/Methodology-Wizard/guides/ |
| **Field Guide No. 0: Measurement** | Measurement & data collection as base camp — constructs and operationalization, Stevens's scale levels, validity and reliability, sampling and coverage, invariance, the model path (construct → indicators → collection → reliability & validity → invariance → documentation), an interactive Reliability Lab on attenuation, software, datasets, and the canon | https://shuwenzsw.github.io/Methodology-Wizard/guides/measurement/ |
| **Field Guide No. 1: Networks** | Social Network Analysis as a guided path — foundations, centrality measures, models (QAP → blockmodels → ERGM → latent space → SAOM), an interactive network playground, software, datasets, and the canon | https://shuwenzsw.github.io/Methodology-Wizard/guides/sna/ |
| **Field Guide No. 2: Causes** | Causal Inference as a guided path — potential outcomes and DAGs, six identification designs, the model path (backdoor → matching → DiD → RD → synthetic control → causal ML), an interactive confounding laboratory, software, datasets, and the canon | https://shuwenzsw.github.io/Methodology-Wizard/guides/causal-inference/ |
| **Field Guide No. 3: Cases** | Case study research as a guided path — case bounding and selection, six case designs, the model path (bounding → selection → process tracing → comparison → fsQCA → nested analysis), an interactive Evidence Lab on Van Evera's typology, software, datasets, and the canon | https://shuwenzsw.github.io/Methodology-Wizard/guides/cases/ |
| **Field Guide No. 4: Policy Networks** | Social Network Analysis in Public Administration — policy and governance networks, the hollow state, the ICA framework and six traditions, the model path (mapping → description → ERGM → SAOM → causal effects → network performance), an interactive ICA Dilemma Lab, software, datasets, and the canon | https://shuwenzsw.github.io/Methodology-Wizard/guides/policy-networks/ |
| **Field Guide No. 5: Network Intelligence** | Artificial Intelligence meets Social Network Analysis — computational social science, representation learning and GNNs, link prediction, ML community detection, synthetic networks, the model path (harvest → embed → predict → detect → simulate → explain & govern), an interactive Prediction Lab, software, datasets, and the canon | https://shuwenzsw.github.io/Methodology-Wizard/guides/ai-networks/ |
| **Field Guide No. 6: Regional Governance** | Public Administration's regional question — the Tiebout tradition, metropolitan reform, interlocal management, multilevel governance, and city-regions, the model path (delimit → map the institutional landscape → measure structure → explain network choice → evaluate performance → design a boundary reform), an interactive Polycentricity Lab on the scale–preference–coordination trade-off, software, datasets, and the canon | https://shuwenzsw.github.io/Methodology-Wizard/guides/regional-governance/ |

**Maintainer:** Shuwen Zhang, Ph.D. (shuwenzhang@um.edu.mo) · ReGovNet Research Group

---

## Project structure

| Path | Purpose | Edit by hand? |
|---|---|---|
| `index.html` | Home page (group intro + feedback box) | Yes — standalone static page |
| `team/index.html` | Team page (research areas, methods, principal) | Yes — standalone static page |
| `guides/index.html` | Field Guides overview — "The Expedition" interactive trail map (standalone static page) | Yes — standalone static page |
| `guides/measurement/index.html` | Field Guide No. 0 — Measurement & Data Collection (standalone static page with inline JS Reliability Lab) | Yes — standalone static page |
| `guides/sna/index.html` | Field Guide No. 1 — Social Network Analysis (standalone static page with inline JS playground) | Yes — standalone static page |
| `guides/causal-inference/index.html` | Field Guide No. 2 — Causal Inference (standalone static page with inline JS laboratory) | Yes — standalone static page |
| `guides/cases/index.html` | Field Guide No. 3 — Case Study Research (standalone static page with inline JS Evidence Lab) | Yes — standalone static page |
| `guides/policy-networks/index.html` | Field Guide No. 4 — SNA in Public Administration (standalone static page with inline JS ICA Dilemma Lab) | Yes — standalone static page |
| `guides/ai-networks/index.html` | Field Guide No. 5 — AI × SNA (standalone static page with inline JS Prediction Lab) | Yes — standalone static page |
| `guides/regional-governance/index.html` | Field Guide No. 6 — Regional Governance (standalone static page with inline JS Polycentricity Lab) | Yes — standalone static page |
| `methods/` | Methodology map site | |
| `methods/data_methods.py` | All content: `TREE` (method hierarchy) + `PROFILES` (method cards) | Yes — content lives here |
| `methods/build_site.py` | Generator: validates data, injects into template | No |
| `methods/template.html` | Map page template (design + interactions) | Only for design changes |
| `pa/` | Public Administration map site | |
| `pa/data_pa.py` | All content: `TREE` (theory hierarchy) + `PROFILES` (theory cards) | Yes — content lives here |
| `pa/build_pa.py` | Generator: validates data, injects both maps' data, emits method-name table for cross-links | No |
| `pa/template_pa.html` | Map page template (design + panel + linkifier) | Only for design changes |
| `measure/` | Measurement & Data Collection map site | |
| `measure/data_measure.py` | All content: `TREE` (concept hierarchy) + `PROFILES` (concept cards) | Yes — content lives here |
| `measure/build_measure.py` | Generator: validates data, injects both maps' data, emits method-name table for cross-links | No |
| `measure/template_me.html` | Map page template (design + panel + linkifier) | Only for design changes |
| `logo.png` | Research group logo, shared by all pages | Replace the file to update |
| `assets/` | Tiny Atlas brand assets: `favicon.svg` + PNG icons, `og-cover.png` share card, `gen_brand.py` generator | Regenerate with `python assets/gen_brand.py` |

Generated files `methods/index.html`, `pa/index.html`, and `measure/index.html` are
**never** edited by hand — they are rebuilt from the data files on every change.

---

## Content model

### Method cards (`methods/data_methods.py`)

One profile per leaf node in `TREE`, keyed by the exact node name (a trailing
` ★` marks a priority pick). Required fields: `use`, `data`, `n`, `assume`,
`skill`, `time`, `adopt` (1–5), `watch`.

### Theory cards (`pa/data_pa.py`)

One profile per leaf node in `TREE` (a trailing ` ★` marks core canon).
Required fields: `use` (core proposition), `explain`, `concepts` (list),
`founders`, `classics` (list), `frameworks` (list), `apply` (research-design
guide).

### Concept cards (`measure/data_measure.py`)

One profile per leaf node in `TREE`, same seven-field structure as theory
cards: `use`, `explain`, `concepts`, `founders`, `classics`, `frameworks`,
`apply`. The seven branch nodes carry a `color` key that maps into the
`COLORS` table in `measure/template_me.html`.

### Method cross-links

The `apply` text of theory and concept cards is auto-linkified: any mention of
a method node from the methodology map (plus the aliases in `METHOD_ALIASES`
inside `pa/build_pa.py` / `measure/build_measure.py`, e.g. `fsQCA`, `RCTs`,
`IRT`) becomes a clickable link that opens the methodology map at that
method's card (`methods/index.html?m=<name>`). To add or adjust aliases, edit
`METHOD_ALIASES` in the respective build script.

---

## Day-to-day workflow

### Add a method

1. Add a leaf under the right category in `methods/data_methods.py` → `TREE`.
2. Add a profile with the **same name** in `PROFILES` (copy an existing entry
   and edit).
3. Rebuild and preview:

   ```bash
   cd methods && python build_site.py
   ```

### Add a theory

1. Add a leaf under the right category in `pa/data_pa.py` → `TREE`.
2. Add a profile with the **same name** in `PROFILES`.
3. Rebuild (this also refreshes the cross-link table):

   ```bash
   cd pa && python build_pa.py
   ```

Both generators run a pre-flight check first — a leaf without a profile, an
empty field, or an out-of-range `adopt` value aborts the build with a clear
error, so a broken page can never be published by accident.

### Preview locally

```bash
python -m http.server 8000
# open http://localhost:8000/  (file:// also works for basic browsing,
# but deep links and some interactions behave best over http)
```

### Publish

```bash
git add .
git commit -m "Describe the change"
git push
```

GitHub Pages deploys automatically from `main` within a minute or two.

---

## Community feedback

The feedback box on the home page composes a pre-filled GitHub issue
(error correction / addition / deletion request / general suggestion).
Review incoming issues at:
https://github.com/ShuwenZSW/Methodology-Wizard/issues

Accepted changes are credited in the repository history.
