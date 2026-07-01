# Autopilot: how the weekly automation works

A scheduled task fires weekly into this same session and does the following:

1. Open `topic-queue.md`, take the first unchecked topic.
2. Write a new article as `content/NN-slug.md`, following the frontmatter format used by every existing file in `content/` (title, slug, description, date, type: article, tools: comma-separated keys from `affiliate-links.json` that are actually relevant — leave blank if none apply).
3. Mark that topic checked in `topic-queue.md` and append 2-3 new topic ideas to the bottom of the list so it never runs dry.
4. Run `python3 generator.py` to rebuild `docs/`.
5. If a git remote named `origin` is configured (check with `git remote -v`), commit and push to the branch GitHub Pages / your host deploys from. If no remote is configured yet, just commit locally and note in the session that publishing is still pending your one-time GitHub setup (see SETUP.md).
6. Send a short summary of what was published.

## Content rules the automation must follow (same rules used for the initial batch)

- No fabricated first-hand experience claims ("I've used this for years") unless truly instructed to add real testimony later.
- No confident, specific pricing numbers — always tell the reader to check the vendor's current pricing page.
- Every article gets the standard affiliate disclosure line (handled automatically by `templates/article.html` — don't remove it).
- Only reference tools that plausibly still have public affiliate programs; when unsure, add the tool to `affiliate-links.json` with a `program_note` telling the site owner to verify before use, same pattern as the existing entries.
- Keep the tone practical and comparative, not hype-y or filled with superlatives that aren't backed by anything concrete.

## Where this can break

- If the git remote isn't set up yet, changes accumulate locally and need a first push once you've done the one-time GitHub setup in SETUP.md.
- If this session ever stops being reachable by the scheduled task (e.g. it's deleted), the trigger will fail silently until recreated. Check in on it occasionally — this is the "hour or two a week" of upkeep this system was designed around.
- Affiliate program terms and product details can drift out of date; a periodic manual pass to double-check older articles is worth doing every couple of months.
