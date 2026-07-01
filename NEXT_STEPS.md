# Next Steps: Getting AI Stack Guide Live

Follow these in order. Total time: roughly 1-2 hours spread over a few sessions, plus ongoing affiliate approvals that can take days to weeks.

## Step 1: Create a GitHub account (skip if you have one)

1. Go to github.com and sign up with your email.
2. Verify your email address.

## Step 2: Create the repository

1. Click the "+" in the top right → "New repository."
2. Name it something like `ai-stack-guide`.
3. Set it to **Public** (required for free GitHub Pages).
4. Don't initialize with a README, .gitignore, or license — leave it empty.
5. Click "Create repository." Keep the page open; it shows the commands you'll need.

## Step 3: Generate a personal access token

1. Click your profile photo (top right) → Settings.
2. Scroll to "Developer settings" (bottom of left sidebar).
3. "Personal access tokens" → "Fine-grained tokens" → "Generate new token."
4. Give it a name like `ai-stack-guide-push`, set expiration (90 days is fine, you can regenerate later), and under "Repository access" select "Only select repositories" → pick the repo you just made.
5. Under permissions, set "Contents" to Read and write.
6. Generate it and **copy the token immediately** — GitHub only shows it once.

## Step 4: Give me the repo and token so I can connect it

Send me:
- The repo URL (looks like `https://github.com/yourusername/ai-stack-guide`)
- The token from Step 3

I'll add it as the `origin` remote and push the site. After that, the weekly autopilot will push new articles automatically without you doing anything.

*(If you'd rather not hand me a token, you can instead unzip the site I sent you, run `git remote add origin <repo-url>` and `git push -u origin main` yourself from a terminal — then tell me it's done so I know to stop treating the remote as unset.)*

## Step 5: Turn on GitHub Pages

1. In the repo, go to Settings → Pages.
2. Under "Build and deployment," set Source to "Deploy from a branch."
3. Set Branch to `main` and folder to `/docs`. Save.
4. Wait 1-2 minutes, then refresh — GitHub will show your live URL, something like `https://yourusername.github.io/ai-stack-guide/`.
5. Open that URL and click through a couple of articles to confirm it looks right.

## Step 6 (optional but recommended): Buy a domain

1. Pick a registrar (Cloudflare Registrar and Namecheap are both reasonable, typically $10-15/year for a `.com`).
2. Search for something close to "AI Stack Guide" or a name of your own choosing, and buy it.
3. Tell me the domain name — I'll add a `CNAME` file to the repo and update the site's canonical URL for you.
4. In your registrar's DNS settings, add the records GitHub's custom domain docs specify (an `A` record set or a `CNAME` record pointing at your github.io address, depending on whether you use the root domain or a subdomain).
5. Back in Settings → Pages, enter your custom domain in the "Custom domain" field and enable "Enforce HTTPS" once it's available.

## Step 7: Apply to affiliate programs

Do this only after Steps 5 (and ideally 6) are done, since most programs want a live URL to review.

1. Open `affiliate-links.json` in the site — it lists 13 placeholder tools (Jasper, Copy.ai, Grammarly, ClickUp, Notion, Asana, Surfer SEO, Semrush, Ahrefs, Synthesia, Descript, Pictory, Canva).
2. For each one you want to monetize, search "`[tool name]` affiliate program," find their official page, and apply using your live site URL.
3. Applications typically take anywhere from instant to a couple of weeks to get approved — apply to several at once rather than one at a time so you're not waiting serially.
4. As each gets approved, send me the real tracking link (or edit `affiliate-links.json` yourself) and I'll rebuild the site with it live.

## Step 8 (optional): Add analytics

Tell me if you want Plausible, Fathom, or Google Analytics added, and I'll wire the tracking snippet into the site template and update the privacy policy to match — or do it yourself by editing `templates/base.html`.

## Step 9: Settle into the weekly rhythm

- Every Monday, the autopilot adds a new article and (once Step 4 is done) pushes it live on its own.
- Spend 10-15 minutes a week: skim the new article for anything off, check on pending affiliate applications, and glance at analytics if you've added them.
- Every couple of months, skim a few older articles for anything stale (tool renamed, feature changed) and let me know if something needs a refresh.

## Quick status check anytime

Ask me "what's the status of the affiliate site" and I'll check the repo connection, the trigger, and how many articles have published.
