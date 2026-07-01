# AI Stack Guide

A static affiliate content site about AI/productivity tools for freelancers and small teams, with a weekly automated content pipeline.

- `content/` — markdown source articles and pages
- `templates/` — Jinja2 HTML templates
- `static/` — CSS and other assets
- `docs/` — generated static site (this is what gets deployed — see SETUP.md for GitHub Pages)
- `generator.py` — build script: `python3 generator.py` regenerates `docs/` from `content/`
- `affiliate-links.json` — placeholder affiliate links per tool; replace with real ones once approved
- `topic-queue.md` — queue of future article topics for the automation to work through
- `AUTOPILOT.md` — how the weekly automated article generation works
- `SETUP.md` — **start here** — the one-time setup only you can do (GitHub, domain, affiliate program applications)
- `PLAN.md` — the original content/niche plan this site was built from

## Quick start

```
pip install jinja2 markdown --break-system-packages
python3 generator.py
```

Then open `docs/index.html` in a browser, or push this repo to GitHub and enable Pages on `/docs` (see SETUP.md).
