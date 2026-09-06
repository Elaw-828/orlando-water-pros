# -*- coding: utf-8 -*-
"""Generate the static site into ../ (the site root)."""

import datetime
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, ".."))

from sitedata import SITE, PRODUCTS, CITIES, RESOURCES     # noqa: E402
import pages_home                                          # noqa: E402
import pages_rest as R                                     # noqa: E402

# pages from the previous (Honest Water) structure that no longer exist
STALE = ["products.html", "gallery.html", "products", "solutions"]

DOMAIN = f"https://{SITE['domain']}"
DEFAULT_OG_IMAGE = f"{DOMAIN}/assets/img/complete-home-system.webp"


def _canonical_url(relpath):
    """Map a written relpath to its public URL. index.html maps to the domain root."""
    if relpath == "index.html":
        return f"{DOMAIN}/"
    return f"{DOMAIN}/{relpath}"


def _inject_seo_tags(relpath, html):
    """Add a canonical link, og:url and og:image — these need the full public
    URL, which isn't known inside head() itself, so they're added here where
    the page's relpath is available."""
    url = _canonical_url(relpath)
    tags = (f'<link rel="canonical" href="{url}">\n'
            f'<meta property="og:url" content="{url}">\n'
            f'<meta property="og:image" content="{DEFAULT_OG_IMAGE}">\n'
            f'<meta name="twitter:image" content="{DEFAULT_OG_IMAGE}">\n')
    return html.replace("</head>", tags + "</head>", 1)


def write(relpath, html):
    html = _inject_seo_tags(relpath, html)
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return relpath


def write_sitemap(relpaths):
    today = datetime.date.today().isoformat()
    urls = "".join(
        f"  <url><loc>{_canonical_url(r)}</loc><lastmod>{today}</lastmod></url>\n"
        for r in relpaths
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{urls}</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(xml)


def write_robots():
    txt = f"User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n"
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(txt)


def clean():
    for s in STALE:
        p = os.path.join(ROOT, s)
        if os.path.isdir(p):
            shutil.rmtree(p)
        elif os.path.exists(p):
            os.remove(p)


def main():
    clean()
    written = []
    written.append(write("index.html", pages_home.build()))
    written.append(write("solutions.html", R.solutions_index()))
    written.append(write("about.html", R.about()))
    written.append(write("quote.html", R.quote_page()))
    written.append(write("contact.html", R.contact()))
    written.append(write("service-areas.html", R.areas_index()))
    written.append(write("resources.html", R.resources_index()))
    written.append(write("warranty.html", R.warranty_page()))

    for p in PRODUCTS:
        written.append(write(f"solutions/{p['slug']}.html", R.solution_page(p)))
    for c in CITIES:
        written.append(write(f"service-areas/{c['slug']}.html", R.city_page(c)))
    for r in RESOURCES:
        written.append(write(f"resources/{r['slug']}.html", R.article_page(r)))
    for key in ("privacy", "terms"):
        written.append(write(f"{key}.html", R.legal_page(key)))

    write_sitemap(written)
    write_robots()

    print(f"{len(written)} pages written to {ROOT}, plus sitemap.xml and robots.txt")


if __name__ == "__main__":
    main()
