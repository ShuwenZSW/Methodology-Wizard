# Methodology List in Social Sciences

Interactive methodology atlas for internal team audits — 3 paradigms, 16 categories, 72 methods with newcomer-friendly profiles.

**Author:** Shuwen Zhang, Ph.D. (shuwenzhang@um.edu.mo) · ReGovNet Research Group

## Project structure

| File | Purpose | Edit by hand? |
|---|---|---|
| `data_methods.py` | All content: TREE (method hierarchy) + PROFILES (detail cards) | Yes — content lives here |
| `build_site.py` | Generator: validates data and builds the page | No |
| `template.html` | Page template (styling and interactions) | Only for design changes |
| `logo.png` | Research group logo | Replace the file to update |
| `index.html` | The generated website | No — auto-generated |

## Day-to-day workflow (expanding the site)

1. Open `data_methods.py`: add/edit nodes in `TREE`, and add a profile with the same name in `PROFILES`.
2. Run the generator (zero dependencies, any Python 3):

   ```bash
   python build_site.py
   ```

   It runs a pre-flight check first — missing profiles, empty fields, or an
   out-of-range `adopt` value will abort the build with a clear error, so a
   broken page can never be published by accident.
3. Double-click `index.html` to preview locally, then publish:

   ```bash
   git add .
   git commit -m "Add new methods"
   git push
   ```

## First-time publishing on GitHub Pages

```bash
git init
git add .
git commit -m "Initial release"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

Then go to the repository's **Settings → Pages → Deploy from a branch → main / (root)**.
The site goes live at `https://<your-username>.github.io/<repo-name>/` in about a minute.
