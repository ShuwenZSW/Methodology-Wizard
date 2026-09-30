# -*- coding: utf-8 -*-
"""
============================================================
SITE GENERATOR — PA Theories & Research Topics
============================================================
Usage:
    python build_pa.py

What it does:
  1. Reads TREE (theory hierarchy) and PROFILES (theory cards)
     from data_pa.py
  2. Validates: every leaf theory must have a profile, all required
     fields must be filled (use / explain / concepts / founders /
     classics / frameworks / apply)
  3. Injects the data into template_pa.html and writes index.html
  4. index.html + logo.png is the complete site, ready for GitHub Pages

Note: never edit index.html by hand (it is overwritten on every build).
      Edit data_pa.py for content, template_pa.html for design.
============================================================
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

# Short aliases: text mentions in "Applying It" that should link to a
# canonical method card (plurals, common abbreviations, spelling variants).
METHOD_ALIASES = {
    "fsQCA": "QCA (csQCA / fsQCA)",
    "csQCA": "QCA (csQCA / fsQCA)",
    "QCA": "QCA (csQCA / fsQCA)",
    "structural equation model": "Structural Equation Modelling",
    "field experiments": "Field Experiments & RCTs",
    "lab-in-field": "Field Experiments & RCTs",
    "survey experiments": "Survey Experiments & Conjoint",
    "online experiments": "Survey Experiments & Conjoint",
    "vignette": "Survey Experiments & Conjoint",
    "lab experiments": "Lab Experiments",
    "RCTs": "Randomized Controlled Trials",
    "event history analysis": "Survival & Event History Analysis",
    "agent-based": "Agent-Based Modeling",
    "synthetic control": "Synthetic Control Method",
    "deliberative poll": "Citizen Juries & Deliberative Polling",
    "panel econometrics": "Panel & Fixed-Effects Models",
    "elite interviews": "Expert & Elite Interviews",
    "ethnography": "Ethnography & Participant Observation",
    "surveys": "Survey Design & Sampling",
    "survey": "Survey Design & Sampling",
    "meta-analysis": "Systematic Review & Meta-Analysis",
    "multilevel": "Multilevel / Hierarchical Models",
}
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "methods"))   # the sister site's method tree
from data_pa import TREE, PROFILES
from data_methods import TREE as METHOD_TREE


def iter_leaves(node):
    """Recursively yield all leaf nodes (nodes without children)."""
    if not node.get("children"):
        yield node
    else:
        for c in node["children"]:
            yield from iter_leaves(c)


def validate():
    """Pre-flight check: refuse to build a broken page."""
    errors, warnings = [], []
    leaves = list(iter_leaves(TREE))

    for leaf in leaves:
        name = leaf["name"]
        if name not in PROFILES:
            errors.append(f"missing profile: {name}")
            continue
        p = PROFILES[name]
        for field in ("use", "explain", "concepts", "founders", "classics", "frameworks", "apply"):
            if not p.get(field):
                errors.append(f"profile field missing [{name}] -> {field}")

    leaf_names = {l["name"] for l in leaves}
    for key in PROFILES:
        if key not in leaf_names:
            warnings.append(f"unused profile (no such theory in TREE): {key}")

    return leaves, errors, warnings


def main():
    leaves, errors, warnings = validate()
    for w in warnings:
        print("  [warn]", w)
    if errors:
        print(f"Build aborted — {len(errors)} problem(s) found:")
        for e in errors:
            print("  [error]", e)
        sys.exit(1)

    template = (HERE / "template_pa.html").read_text(encoding="utf-8")
    html = template.replace("__DATA_JSON__",
                            json.dumps(TREE, ensure_ascii=False))
    html = html.replace("__PROFILES_JSON__",
                        json.dumps(PROFILES, ensure_ascii=False))

    # inject the sister site's method names so "Applying It" texts can be
    # auto-linked to the corresponding method cards
    method_names = [n["name"] for n in iter_leaves(METHOD_TREE)]
    html = html.replace("__METHODS_JSON__",
                        json.dumps(method_names, ensure_ascii=False))
    html = html.replace("__ALIASES_JSON__",
                        json.dumps(METHOD_ALIASES, ensure_ascii=False))

    for ph in ("__DATA_JSON__", "__PROFILES_JSON__", "__METHODS_JSON__", "__ALIASES_JSON__"):
        if ph in html:
            print(f"[error] placeholder not fully replaced: {ph} — check template_pa.html")
            sys.exit(1)

    out = HERE / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"[OK] validation passed: {len(leaves)} theories, {len(PROFILES)} profiles")
    print(f"[OK] generated -> {out}")
    print('Next: git add . && git commit -m "update" && git push')


if __name__ == "__main__":
    main()
