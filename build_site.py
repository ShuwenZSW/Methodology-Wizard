# -*- coding: utf-8 -*-
"""
============================================================
SITE GENERATOR — Methodology List in Social Sciences
============================================================
Usage:
    python build_site.py

What it does:
  1. Reads TREE (method hierarchy) and PROFILES (method cards)
     from data_methods.py
  2. Validates: every leaf method must have a profile, all required
     fields must be filled, and "adopt" must be within 1-5
  3. Injects the data into template.html and writes index.html
  4. index.html + logo.png is the complete site, ready for GitHub Pages

Note: never edit index.html by hand (it is overwritten on every build).
      Edit data_methods.py for content, template.html for design.
============================================================
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from data_methods import TREE, PROFILES

HERE = Path(__file__).parent


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
        for field in ("use", "data", "n", "assume", "skill", "time", "watch"):
            if not p.get(field):
                errors.append(f"profile field missing [{name}] -> {field}")
        if not (1 <= int(p.get("adopt", 0)) <= 5):
            errors.append(f"adopt must be 1-5: [{name}]")

    leaf_names = {l["name"] for l in leaves}
    for key in PROFILES:
        if key not in leaf_names:
            warnings.append(f"unused profile (no such method in TREE): {key}")

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

    template = (HERE / "template.html").read_text(encoding="utf-8")
    html = template.replace("__DATA_JSON__",
                            json.dumps(TREE, ensure_ascii=False))
    html = html.replace("__PROFILES_JSON__",
                        json.dumps(PROFILES, ensure_ascii=False))

    if "__DATA_JSON__" in html or "__PROFILES_JSON__" in html:
        print("[error] placeholders not fully replaced — check template.html")
        sys.exit(1)

    out = HERE / "index.html"
    out.write_text(html, encoding="utf-8")
    print(f"[OK] validation passed: {len(leaves)} methods, {len(PROFILES)} profiles")
    print(f"[OK] generated -> {out}")
    print('Next: git add . && git commit -m "update" && git push')


if __name__ == "__main__":
    main()
