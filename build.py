"""
Builds the static website into site/ from data/poems.py.

Only entries whose reveal_date is today or earlier are included.
Run this any time with:  python build.py
(The GitHub Actions workflow runs it automatically every day.)
"""

import html
import shutil
from datetime import date
from pathlib import Path

from data.poems import POEMS

ROOT = Path(__file__).parent
SITE = ROOT / "site"
ASSETS = ROOT / "build_assets"

# --- customize these ---
SITE_TITLE = "For You"
SITE_SUBTITLE = "A poem, once a month."
# ------------------------


def revealed_poems():
    today = date.today().isoformat()
    return sorted(
        [p for p in POEMS if p["reveal_date"] <= today],
        key=lambda p: p["reveal_date"],
        reverse=True,
    )


def next_locked_date():
    today = date.today().isoformat()
    upcoming = sorted(p["reveal_date"] for p in POEMS if p["reveal_date"] > today)
    return upcoming[0] if upcoming else None


def render_card(poem):
    imgs = "".join(
        f'<img src="{html.escape(img)}" alt="">' for img in poem.get("images", [])
    )
    gallery = f'<div class="gallery">{imgs}</div>' if imgs else ""
    return f"""
    <article class="month-card">
      <h2>{html.escape(poem['title'])}</h2>
      <div class="date">{poem['reveal_date']}</div>
      <p class="poem">{html.escape(poem['poem'])}</p>
      {gallery}
    </article>
    """


def build():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    (SITE / "images").mkdir()

    # copy images referenced by revealed poems
    for poem in revealed_poems():
        for img in poem.get("images", []):
            src = ROOT / img
            if src.exists():
                dest = SITE / img
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy(src, dest)

    # copy stylesheet
    shutil.copy(ASSETS / "style.css", SITE / "style.css")

    cards = "".join(render_card(p) for p in revealed_poems())

    locked_html = ""
    nxt = next_locked_date()
    if nxt:
        locked_html = f'<div class="locked">Next one unlocks {nxt} ✨</div>'

    if not cards:
        cards = '<div class="locked">Nothing revealed yet -- check back soon.</div>'

    html_out = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(SITE_TITLE)}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">
  <header class="site-header">
    <h1>{html.escape(SITE_TITLE)}</h1>
    <p>{html.escape(SITE_SUBTITLE)}</p>
  </header>
  {cards}
  {locked_html}
  <footer>updated automatically</footer>
</div>
</body>
</html>
"""
    (SITE / "index.html").write_text(html_out, encoding="utf-8")
    print(f"Built site with {len(revealed_poems())} revealed poem(s).")


if __name__ == "__main__":
    build()
