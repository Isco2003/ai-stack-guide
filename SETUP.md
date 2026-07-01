# One-time setup checklist (things only you can do)

I built the whole site and the weekly auto-content pipeline. What's left requires your identity, payment info, or account logins — none of which I can create or hold on your behalf. Roughly 1-2 hours total, one time.

## 1. Create a GitHub repo and connect it (~15 min)

1. Create a free account at github.com if you don't have one.
2. Create a new **public** repo, e.g. `ai-stack-guide`.
3. Generate a personal access token (Settings -> Developer settings -> Personal access tokens -> generate one scoped to just that repo, "contents: read/write").
4. Come back and tell me the repo URL and give me the token (or add the remote yourself). Once `origin` is configured, the weekly autopilot will push automatically.
5. In the repo's Settings -> Pages, set source to "Deploy from a branch," branch `main`, folder `/docs`. This makes the site live at `https://<yourusername>.github.io/ai-stack-guide/` within a few minutes, no build step needed since `docs/` is already fully built static HTML.

## 2. Buy a domain (optional but recommended) (~10 min)

A real domain (e.g. from Namecheap, Cloudflare, Google Domains successor, or similar registrar) costs roughly $10-15/year and looks far more credible than a github.io subdomain to both readers and affiliate program reviewers. Point it at GitHub Pages via their custom domain instructions. Once you have one, tell me the domain and I'll update `SITE_URL` in `generator.py` and add a `CNAME` file.

## 3. Apply to affiliate programs (~30-60 min, ongoing)

`affiliate-links.json` has placeholder entries for: Jasper, Copy.ai, Grammarly, ClickUp, Notion, Asana, Surfer SEO, Semrush, Ahrefs, Synthesia, Descript, Pictory, Canva. For each one you actually want to monetize:

1. Find their official affiliate/partner program page (search "[tool name] affiliate program").
2. Apply with your own details — most require your site URL, so do this after step 1.
3. Some programs want to see live content before approving; that's normal, and it's part of why the site already has 8 articles ready.
4. Once approved, replace the matching `affiliate_url` placeholder in `affiliate-links.json` with your real tracking link, then run `python3 generator.py` to rebuild — or just tell me the real links and I'll do it.

**Important:** verify each program's current commission rate and terms yourself — they change, and I generated this list from general knowledge of well-known programs, not a live lookup of every current term.

## 4. Add analytics (optional) (~10 min)

Add a privacy-friendly analytics snippet (e.g. Plausible, Fathom, or Google Analytics) to `templates/base.html` in the `<head>` block, and update `content/page-privacy.md` to accurately describe what it collects. Skip this if you'd rather not track visitors at all.

## 5. Check in weekly (~10-15 min)

The scheduled task adds one new article every Monday. Once a week:
- Skim the new article for accuracy before it goes live if you haven't connected the repo for auto-push, or after if you have.
- Check whether any affiliate applications need follow-up.
- Glance at GitHub Pages / your analytics to see if anything's obviously broken.

## What "done" looks like

Site live at a real URL, `origin` connected so autopilot auto-publishes, at least a few affiliate programs approved and live-linked, and a Monday habit of a quick skim. Income after that depends on search traffic and affiliate approvals building over weeks to months — there's no shortcut around that part.
