# -*- coding: utf-8 -*-
"""Generate the static site into ../ (the site root)."""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, ".."))

from sitedata import PRODUCTS, CITIES, RESOURCES          # noqa: E402
import pages_home                                          # noqa: E402
import pages_rest as R                                     # noqa: E402

# pages from the previous (Honest Water) structure that no longer exist
STALE = ["products.html", "gallery.html", "products", "solutions"]


def write(relpath, html):
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return relpath


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

    print(f"{len(written)} pages written to {ROOT}")


if __name__ == "__main__":
    main()
