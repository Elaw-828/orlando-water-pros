# -*- coding: utf-8 -*-
"""Generate the static site into ../ (the site root)."""

import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.abspath(os.path.join(HERE, ".."))

from sitedata import SITE, PRODUCTS, CITIES              # noqa: E402
import pages_home                                          # noqa: E402
import pages_rest as R                                     # noqa: E402

# pages from the previous (Honest Water) structure that no longer exist
STALE = ["products.html", "gallery.html", "products", "solutions",
         "resources.html", "resources",
         "solutions/pre-sediment-filter.html"]

DOMAIN = f"https://{SITE['domain']}"
DEFAULT_OG_IMAGE = f"{DOMAIN}/assets/img/softener-carbon-filtration.webp"


def _canonical_url(relpath):
    """Map a written relpath to its public URL. index.html maps to the domain root."""
    if relpath == "index.html":
        return f"{DOMAIN}/"
    return f"{DOMAIN}/{relpath}"


BIZ_ID = f"{DOMAIN}/#business"
LOGO_URL = f"{DOMAIN}/assets/img/logo/horizontal-1200.png"
SERVICE_TYPE = "Water softener and filtration installation"


def _areas():
    return [{"@type": "City", "name": f"{c['name']}, FL"} for c in CITIES]


def _business_node():
    """The one full LocalBusiness entity. No street address on purpose: this is a
    service-area business. No licence, insurance, rating or review properties
    either; those claims aren't made anywhere on the site."""
    hours = [{"@type": "OpeningHoursSpecification", "dayOfWeek": days,
              "opens": opens, "closes": closes}
             for days, opens, closes in SITE["hours_spec"]]
    return {
        "@type": "LocalBusiness", "@id": BIZ_ID,
        "name": SITE["brand"], "url": f"{DOMAIN}/",
        "description": ("Water filtration and softening installation across Orange, "
                        "Seminole, Osceola, Lake and Volusia counties in Central Florida."),
        "telephone": "+" + SITE["phone_href"].lstrip("+"), "email": SITE["email"],
        "logo": LOGO_URL, "image": DEFAULT_OG_IMAGE, "priceRange": "$$",
        "areaServed": _areas(), "openingHoursSpecification": hours,
    }


def _jsonld(relpath, crumbs, service):
    """Structured data per page. Home carries the business + WebSite entities;
    interior pages carry a BreadcrumbList; product and city pages add a Service."""
    graph = []
    if relpath == "index.html":
        graph.append(_business_node())
        graph.append({"@type": "WebSite", "@id": f"{DOMAIN}/#website",
                      "url": f"{DOMAIN}/", "name": SITE["brand"],
                      "publisher": {"@id": BIZ_ID}})
    if crumbs:
        items = [("Home", "index.html")] + list(crumbs)
        graph.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n,
             "item": _canonical_url(r)} for i, (n, r) in enumerate(items)]})
    if service:
        svc = {"@type": "Service", "serviceType": SERVICE_TYPE,
               "provider": {"@type": "LocalBusiness", "@id": BIZ_ID, "name": SITE["brand"]},
               "url": _canonical_url(relpath)}
        svc.update(service)
        graph.append(svc)
    if not graph:
        return ""
    blob = json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'<script type="application/ld+json">\n{blob}\n</script>\n'


def _inject_seo_tags(relpath, html, og_image=None, og_alt=None, crumbs=None, service=None):
    """Add canonical, og:url, og:image and JSON-LD. These need the full public
    URL, which isn't known inside head() itself, so they're added here where
    the page's relpath is available."""
    url = _canonical_url(relpath)
    img = og_image or DEFAULT_OG_IMAGE
    alt = og_alt or "Orlando Water Pros whole-home water softener and filtration system"
    tags = (f'<link rel="canonical" href="{url}">\n'
            f'<meta property="og:url" content="{url}">\n'
            f'<meta property="og:image" content="{img}">\n'
            f'<meta property="og:image:alt" content="{alt}">\n'
            f'<meta name="twitter:image" content="{img}">\n'
            f'<meta name="twitter:image:alt" content="{alt}">\n'
            + _jsonld(relpath, crumbs, service))
    return html.replace("</head>", tags + "</head>", 1)


PAGES = {}   # relpath -> final html, kept for the post-build audit


def write(relpath, html, **seo):
    html = _inject_seo_tags(relpath, html, **seo)
    PAGES[relpath] = html
    path = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)
    return relpath


def write_sitemap(relpaths):
    # No <lastmod>: stamping every URL with the build date is inaccurate, and
    # search engines discount lastmod once they catch a sitemap doing that.
    urls = "".join(f"  <url><loc>{_canonical_url(r)}</loc></url>\n" for r in relpaths)
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


def audit():
    """Print SEO warnings for the built pages. Never fails the build."""
    warns, titles, descs = [], {}, {}
    for rel, html in PAGES.items():
        t = re.search(r"<title>(.*?)</title>", html, re.S)
        d = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
        t, d = (t.group(1) if t else ""), (d.group(1) if d else "")
        if not t or len(t) > 65:
            warns.append(f"{rel}: title is {len(t)} chars (aim for 30-65)")
        if not 70 <= len(d) <= 160:
            warns.append(f"{rel}: meta description is {len(d)} chars (aim for 70-160)")
        if titles.setdefault(t, rel) != rel:
            warns.append(f"{rel}: title duplicates {titles[t]}")
        if descs.setdefault(d, rel) != rel:
            warns.append(f"{rel}: description duplicates {descs[d]}")
        n = len(re.findall(r"<h1[ >]", html))
        if n != 1:
            warns.append(f"{rel}: {n} <h1> tags (want exactly 1)")
        if "hardness" in d.lower():
            warns.append(f"{rel}: hardness in meta description (city hardness figures are unsourced)")
        for blob in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            try:
                json.loads(blob)
            except ValueError as e:
                warns.append(f"{rel}: invalid JSON-LD ({e})")
        for m in re.finditer(r'<img [^>]*?>', html):
            if "alt=" not in m.group(0):
                warns.append(f"{rel}: <img> without alt")
        base = os.path.dirname(os.path.join(ROOT, rel))
        for ref in set(re.findall(r'(?:href|src)="([^"#?:]+)"', html)):
            if ref.startswith(("http", "//", "tel", "mailto")):
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, ref))):
                warns.append(f"{rel}: broken local link {ref}")
    print("SEO audit: " + ("clean" if not warns else f"{len(warns)} warning(s)"))
    for w in warns:
        print("  - " + w)


def main():
    clean()
    written = []
    written.append(write("index.html", pages_home.build()))
    written.append(write("solutions.html", R.solutions_index(),
                         crumbs=[("Our Solutions", "solutions.html")]))
    written.append(write("about.html", R.about(), crumbs=[("About", "about.html")]))
    written.append(write("quote.html", R.quote_page(), crumbs=[("Get a Free Quote", "quote.html")]))
    written.append(write("contact.html", R.contact(), crumbs=[("Contact", "contact.html")]))
    written.append(write("service-areas.html", R.areas_index(),
                         crumbs=[("Service Areas", "service-areas.html")]))
    written.append(write("warranty.html", R.warranty_page(), crumbs=[("Warranty", "warranty.html")]))

    for p in PRODUCTS:
        rel = f"solutions/{p['slug']}.html"
        img = f"{DOMAIN}/assets/img/{p['img']}" if p.get("img") else None
        svc = {"name": p["name"], "description": p["short"], "areaServed": _areas()}
        if img:
            svc["image"] = img
        written.append(write(rel, R.solution_page(p), og_image=img,
                             og_alt=f"{p['name']} water treatment system",
                             crumbs=[("Our Solutions", "solutions.html"), (p["name"], rel)],
                             service=svc))
    for c in CITIES:
        rel = f"service-areas/{c['slug']}.html"
        svc = {"name": f"Water softening and filtration in {c['name']}, FL",
               "areaServed": {"@type": "City", "name": f"{c['name']}, FL"}}
        written.append(write(rel, R.city_page(c),
                             crumbs=[("Service Areas", "service-areas.html"), (c["name"], rel)],
                             service=svc))
    for key, name in (("privacy", "Privacy Policy"), ("terms", "Terms of Service")):
        written.append(write(f"{key}.html", R.legal_page(key), crumbs=[(name, f"{key}.html")]))

    write_sitemap(written)
    write_robots()

    print(f"{len(written)} pages written to {ROOT}, plus sitemap.xml and robots.txt")
    audit()


if __name__ == "__main__":
    main()
