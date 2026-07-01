#!/usr/bin/env python3
"""
Static site generator for the affiliate site.

Reads markdown files from content/, renders them through Jinja2 templates,
and writes a fully static site to dist/. Also emits sitemap.xml, rss.xml,
robots.txt.

Frontmatter format (simple, hand-rolled — no external frontmatter lib needed):

    ---
    title: My Article Title
    slug: my-article-title
    description: One sentence for meta description and homepage card.
    date: 2026-07-01
    type: article        # article | page
    tools: jasper, copyai, grammarly   # keys into affiliate-links.json (article only)
    ---
    Markdown body starts here.
"""
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

import markdown as md
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).parent
CONTENT_DIR = ROOT / "content"
# Named "docs" (not "dist") so GitHub Pages can serve straight from this
# folder via Settings -> Pages -> Deploy from branch -> /docs, no build step needed.
DIST_DIR = ROOT / "docs"
STATIC_DIR = ROOT / "static"
TEMPLATES_DIR = ROOT / "templates"
AFFILIATE_JSON = ROOT / "affiliate-links.json"

SITE_NAME = "AI Stack Guide"
SITE_TAGLINE = "Straight-talking reviews and comparisons of AI tools for freelancers and small teams."
SITE_URL = "https://REPLACE-WITH-YOUR-DOMAIN"  # update once domain is live


def parse_frontmatter(text: str):
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError("Missing frontmatter block (--- ... ---) at top of file")
    raw_fm, body = match.groups()
    meta = {}
    for line in raw_fm.splitlines():
        if not line.strip():
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        meta[key.strip()] = value
    return meta, body


def load_articles():
    affiliate_data = json.loads(AFFILIATE_JSON.read_text())
    articles, pages = [], []
    for path in sorted(CONTENT_DIR.glob("*.md")):
        raw = path.read_text()
        meta, body_md = parse_frontmatter(raw)
        html_body = md.markdown(body_md, extensions=["extra", "tables"])
        entry_type = meta.get("type", "article")
        tool_keys = [t.strip() for t in meta.get("tools", "").split(",") if t.strip()]
        tools = [affiliate_data[k] for k in tool_keys if k in affiliate_data]
        entry = {
            "title": meta["title"],
            "slug": meta["slug"],
            "description": meta.get("description", ""),
            "date": meta.get("date", ""),
            "body": html_body,
            "tools": tools,
        }
        if entry_type == "page":
            pages.append(entry)
        else:
            articles.append(entry)
    articles.sort(key=lambda a: a["date"], reverse=True)
    return articles, pages


def build():
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)))
    articles, pages = load_articles()
    year = datetime.now().year

    common = {
        "site_name": SITE_NAME,
        "site_tagline": SITE_TAGLINE,
        "site_url": SITE_URL,
        "year": year,
    }

    # Home page
    index_tpl = env.get_template("index.html")
    (DIST_DIR / "index.html").write_text(index_tpl.render(
        **common,
        root="",
        canonical_path="/",
        page_title=f"{SITE_NAME} — {SITE_TAGLINE}",
        page_description=SITE_TAGLINE,
        articles=articles,
    ))

    # Articles
    article_tpl = env.get_template("article.html")
    for a in articles:
        out = DIST_DIR / f"{a['slug']}.html"
        out.write_text(article_tpl.render(
            **common,
            root="",
            canonical_path=f"/{a['slug']}.html",
            page_title=f"{a['title']} | {SITE_NAME}",
            page_description=a["description"],
            title=a["title"],
            date=a["date"],
            body=a["body"],
            tools=a["tools"],
        ))

    # Static pages (about, disclosure, privacy)
    page_tpl = env.get_template("simple_page.html")
    for p in pages:
        out = DIST_DIR / f"{p['slug']}.html"
        out.write_text(page_tpl.render(
            **common,
            root="",
            canonical_path=f"/{p['slug']}.html",
            page_title=f"{p['title']} | {SITE_NAME}",
            page_description=p["description"],
            title=p["title"],
            body=p["body"],
        ))

    # Static assets
    shutil.copytree(STATIC_DIR, DIST_DIR / "static", dirs_exist_ok=True)

    # robots.txt
    (DIST_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
    )

    # sitemap.xml
    urls = ["", "about.html", "disclosure.html", "privacy.html"] + [f"{a['slug']}.html" for a in articles]
    sitemap_items = "\n".join(
        f"  <url><loc>{SITE_URL}/{u}</loc></url>" for u in urls
    )
    (DIST_DIR / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap_items}\n</urlset>\n'
    )

    # rss.xml
    rss_items = "\n".join(
        f"    <item><title>{a['title']}</title><link>{SITE_URL}/{a['slug']}.html</link>"
        f"<description>{a['description']}</description><pubDate>{a['date']}</pubDate></item>"
        for a in articles
    )
    (DIST_DIR / "rss.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel>'
        f"<title>{SITE_NAME}</title><link>{SITE_URL}</link><description>{SITE_TAGLINE}</description>"
        f"\n{rss_items}\n</channel></rss>\n"
    )

    print(f"Built {len(articles)} articles + {len(pages)} pages -> {DIST_DIR}")


if __name__ == "__main__":
    build()
