# -*- coding: utf-8 -*-
"""Page chrome: <head>, top bar, header/nav, footer, and small components."""

from sitedata import SITE, CITIES, PRODUCTS, RESOURCES

# ---------------------------------------------------------------- inline icons
ICON = {
    "drop": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.7s6.2 6.6 6.2 11a6.2 6.2 0 1 1-12.4 0c0-4.4 6.2-11 6.2-11z"/></svg>',
    "phone": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/></svg>',
    "mail": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>',
    "pin": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "clock": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "shield": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.5 4.5 5.6v5.9c0 4.7 3.2 9 7.5 10 4.3-1 7.5-5.3 7.5-10V5.6z"/><path d="m9 12 2 2 4-4"/></svg>',
    "badge": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="5.5"/><path d="m8.5 13.5-1.5 8 5-2.5 5 2.5-1.5-8"/></svg>',
    "star": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/></svg>',
    "tag": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 13.5 13 21a2 2 0 0 1-2.8 0l-7-7A2 2 0 0 1 2.6 12l.5-7A2 2 0 0 1 5 3.1l7-.5a2 2 0 0 1 1.5.6l7 7a2 2 0 0 1 0 3.3z"/><circle cx="7.5" cy="7.5" r="1.4"/></svg>',
    "wrench": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M14.5 6.5a4.5 4.5 0 0 0 5.9 5.9L21 13l-8 8a2.8 2.8 0 0 1-4-4l8-8z"/></svg>',
    "home": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="m3 10 9-7 9 7v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 21v-7h6v7"/></svg>',
    "beaker": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M9.5 3v6L4 19a2 2 0 0 0 1.8 3h12.4A2 2 0 0 0 20 19l-5.5-10V3"/><path d="M8 3h8M6.6 15h10.8"/></svg>',
    "leaf": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M20 4C10 4 4 9 4 16c0 2 .7 3.4.7 3.4S8 12 20 4z"/><path d="M4.7 19.4C7 20.6 17 21 20 4"/></svg>',
    # benefit icons
    "shower": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M4 21V6a3 3 0 0 1 6 0v1"/><path d="M9.5 8.5 18 4l2 2-4.5 8.5z"/><path d="M7 14v.01M11 16v.01M9 19v.01M14 18v.01"/></svg>',
    "sparkle": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M8 3.5 9.4 7 13 8.4 9.4 9.8 8 13.4 6.6 9.8 3 8.4 6.6 7z"/><path d="M17 13.5 17.9 16 20.5 16.9 17.9 17.8 17 20.4 16.1 17.8 13.5 16.9 16.1 16z"/></svg>',
    "laundry": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2.5" width="16" height="19" rx="2.5"/><circle cx="12" cy="14" r="4.5"/><path d="M7.5 6h.01M11 6h.01"/></svg>',
    "faucet": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round"><path d="M12 2.5 15.5 8 12 13.5 8.5 8z"/><path d="M6 12.5 8.5 16.5 6 20.5 3.5 16.5z"/><path d="M18 12.5 20.5 16.5 18 20.5 15.5 16.5z"/></svg>',
    "stain": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3.5s5 5.4 5 9a5 5 0 0 1-10 0c0-3.6 5-9 5-9z"/><path d="M9.5 13.5c.4 1.4 1.4 2.2 2.7 2.4"/></svg>',
    "chev": '<svg class="chev" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>',
    "arrow": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "prev": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m15 6-6 6 6 6"/></svg>',
    "next": '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg>',
    "fb": '<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M14 9V7.2c0-.8.2-1.2 1.4-1.2H17V3h-2.6C11.3 3 10.3 4.5 10.3 7v2H8v3h2.3v9H14v-9h2.6l.4-3z"/></svg>',
    "ig": '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none"/></svg>',
    "in": '<svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M6.9 8.5H3.7V21h3.2zM5.3 3a1.9 1.9 0 1 0 0 3.8 1.9 1.9 0 0 0 0-3.8M21 13.9c0-3.4-1.8-5-4.2-5-1.9 0-2.8 1.1-3.3 1.8V8.5H10.3V21h3.2v-6.8c0-1.5.9-2.3 2-2.3s2.3.8 2.3 2.4V21H21z"/></svg>',
}


def head(title, desc, depth=0, extra=""):
    up = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#1b3a6b">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Orlando Water Pros">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="icon" href="{up}assets/img/logo/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{up}assets/img/logo/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{up}assets/img/logo/favicon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{up}assets/css/style.css">
{extra}</head>
<body>
"""


def _nav_link(label, href, active, key, up):
    cls = ' class="is-active"' if active == key else ""
    return f'<a href="{up}{href}"{cls}>{label}</a>'


def header(active="", depth=0):
    up = "../" * depth
    sol_items = "".join(
        f'<a href="{up}solutions/{p["slug"]}.html">{p["name"]}</a>' for p in PRODUCTS[:12]
    )
    city_items = "".join(
        f'<a href="{up}service-areas/{c["slug"]}.html">{c["name"]}</a>' for c in CITIES
    )
    res_items = "".join(
        f'<a href="{up}resources/{r["slug"]}.html">{r["title"]}</a>' for r in RESOURCES
    )
    return f"""<div class="topbar">
  <div class="wrap">
    <div class="topbar-note">{ICON['pin']}&nbsp;Serving Orange, Seminole, Osceola, Lake &amp; Volusia counties</div>
    <div class="topbar-links">
      <a href="{up}quote.html">Free quote</a>
      <a href="mailto:{SITE['email']}">{SITE['email']}</a>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{up}index.html" aria-label="Orlando Water Pros — home">
      <img class="brand-logo" src="{up}assets/img/logo/horizontal.svg"
           alt="Orlando Water Pros" width="483" height="176">
    </a>

    <nav class="nav" id="primary-nav" aria-label="Main">
      {_nav_link("Products", "solutions.html", active, "solutions", up)}
      <div class="has-menu">
        <button type="button" aria-expanded="false">Service Areas {ICON['chev']}</button>
        <div class="menu cols">
          {city_items}
          <a href="{up}service-areas.html"><strong>All areas →</strong></a>
        </div>
      </div>
      <div class="has-menu">
        <button type="button" aria-expanded="false">Resources {ICON['chev']}</button>
        <div class="menu">
          {res_items}
          <a href="{up}resources.html"><strong>All articles →</strong></a>
        </div>
      </div>
      {_nav_link("About", "about.html", active, "about", up)}
      {_nav_link("Contact", "contact.html", active, "contact", up)}
    </nav>

    <div class="header-cta">
      <a class="header-phone" href="mailto:{SITE['email']}">{ICON['mail']}<span class="lbl">{SITE['email']}</span></a>
      <a class="btn btn-primary btn-sm" href="{up}quote.html">Get a Free Quote</a>
      <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false" aria-controls="primary-nav"><span></span></button>
    </div>
  </div>
</header>
"""


def cta_band(depth=0, heading=None, text=None):
    up = "../" * depth
    heading = heading or "Get a free quote on your system"
    text = text or ("Tell us about your home and we'll give you a flat installed price in writing. "
                    "No charge for the quote, and no pressure.")
    return f"""<section class="section">
  <div class="wrap">
    <div class="cta-band">
      <div>
        <h2>{heading}</h2>
        <p>{text}</p>
      </div>
      <div class="btn-row">
        <a class="btn btn-primary" href="{up}quote.html">Get a Free Quote</a>
        <a class="btn btn-ghost" href="mailto:{SITE['email']}">{ICON['mail']} Email Us</a>
      </div>
    </div>
  </div>
</section>
"""


def footer(depth=0):
    up = "../" * depth
    top_products = "".join(
        f'<li><a href="{up}solutions/{p["slug"]}.html">{p["name"]}</a></li>' for p in PRODUCTS[:6]
    )
    top_cities = "".join(
        f'<li><a href="{up}service-areas/{c["slug"]}.html">{c["name"]}</a></li>' for c in CITIES[:7]
    )
    top_res = "".join(
        f'<li><a href="{up}resources/{r["slug"]}.html">{r["title"]}</a></li>' for r in RESOURCES[:5]
    )
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="{up}index.html" aria-label="Orlando Water Pros — home">
          <img class="brand-logo brand-logo-footer" src="{up}assets/img/logo/horizontal-dark.svg"
               alt="Orlando Water Pros" width="483" height="176">
        </a>
        <p>Water filtration and softening for homes across Orange, Seminole, Osceola, Lake and Volusia counties.</p>
        <p class="footer-contact">
          <a href="mailto:{SITE['email']}">{SITE['email']}</a>
        </p>
        <div class="socials">
          <a href="#" aria-label="Facebook">{ICON['fb']}</a>
          <a href="#" aria-label="Instagram">{ICON['ig']}</a>
          <a href="#" aria-label="LinkedIn">{ICON['in']}</a>
        </div>
      </div>
      <div>
        <h4>Solutions</h4>
        <ul>{top_products}<li><a href="{up}solutions.html">All solutions</a></li></ul>
      </div>
      <div>
        <h4>Service Areas</h4>
        <ul>{top_cities}<li><a href="{up}service-areas.html">All areas</a></li></ul>
      </div>
      <div>
        <h4>Resources</h4>
        <ul>{top_res}<li><a href="{up}resources.html">All articles</a></li></ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="{up}about.html">About us</a></li>
          <li><a href="{up}index.html#faq">FAQ</a></li>
          <li><a href="{up}warranty.html">Warranty</a></li>
          <li><a href="{up}quote.html">Get a free quote</a></li>
          <li><a href="{up}contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>© <span data-year></span> {SITE['legal']}. All rights reserved.</div>
      <ul>
        <li><a href="{up}privacy.html">Privacy Policy</a></li>
        <li><a href="{up}terms.html">Terms of Service</a></li>
        <li><a href="{up}warranty.html">Warranty</a></li>
      </ul>
    </div>
  </div>
</footer>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{SITE['brand']}",
  "description": "Water filtration and softening installation across Orange, Seminole, Osceola, Lake and Volusia counties in Central Florida.",
  "url": "https://{SITE['domain']}/",
  "email": "{SITE['email']}",
  "areaServed": [{", ".join(f'{{"@type": "City", "name": "{c["name"]}"}}' for c in CITIES)}],
  "priceRange": "$$"
}}
</script>
<script src="{up}assets/js/main.js"></script>
</body>
</html>
"""


def page_hero(title, sub, crumbs_html=""):
    return f"""<section class="page-hero">
  <div class="wrap">
    {f'<div class="crumbs">{crumbs_html}</div>' if crumbs_html else ''}
    <h1>{title}</h1>
    <p class="lede" style="color:#b9c9de">{sub}</p>
  </div>
</section>
"""


def quote_form(depth=0):
    """First/last name, phone, email, zip, best time to call, optional message."""
    return """<form class="form-card" data-quote-form>
  <h3>Get your free quote</h3>
  <p class="muted" style="margin-bottom:20px">Tell us how to reach you and we'll come back with a price. Usually the same business day.</p>
  <div class="field-row">
    <div class="field"><label for="fn">First name</label><input id="fn" name="first_name" autocomplete="given-name" required></div>
    <div class="field"><label for="ln">Last name</label><input id="ln" name="last_name" autocomplete="family-name" required></div>
  </div>
  <div class="field-row">
    <div class="field"><label for="ph">Phone number</label><input id="ph" type="tel" name="phone" autocomplete="tel" required></div>
    <div class="field"><label for="em">Email</label><input id="em" type="email" name="email" autocomplete="email" required></div>
  </div>
  <div class="field-row">
    <div class="field"><label for="zp">ZIP code</label><input id="zp" name="zip" inputmode="numeric" pattern="[0-9]{5}" maxlength="5" autocomplete="postal-code" required></div>
    <div class="field">
      <label for="bt">Best time to call</label>
      <select id="bt" name="best_time">
        <option>Morning (8am–12pm)</option>
        <option>Afternoon (12pm–4pm)</option>
        <option>Evening (4pm–7pm)</option>
        <option>Weekends</option>
        <option>Anytime</option>
      </select>
    </div>
  </div>
  <div class="field">
    <label for="ms">Message <span class="opt">optional</span></label>
    <textarea id="ms" name="message" placeholder="Spotting on glassware, chlorine smell, stiff laundry, sulfur odor on a well&hellip;"></textarea>
  </div>
  <button class="btn btn-primary btn-block" type="submit">Get My Free Quote</button>
  <p class="form-note" data-form-msg>We usually respond the same business day.</p>
</form>
"""


def contact_panel(depth=0):
    return f"""<div class="contact-panel">
  <h3>Prefer to talk it through?</h3>
  <p style="color:#b9c9de;margin-bottom:22px">Send us a message and you'll hear back from someone local who knows Central Florida water. Not a national call center.</p>
  <ul class="contact-list">
    <li><span class="ci">{ICON['mail']}</span><div><strong>Email</strong><a href="mailto:{SITE['email']}">{SITE['email']}</a></div></li>
    <li><span class="ci">{ICON['pin']}</span><div><strong>Service area</strong><span>Orange, Seminole, Osceola, Lake &amp; Volusia counties</span></div></li>
    <li><span class="ci">{ICON['clock']}</span><div><strong>Hours</strong><span>{SITE['hours']}</span></div></li>
  </ul>
  <div class="area-panel">
    <h4>We come to you</h4>
    <p>We're a mobile service. Every quote and installation happens at your home, anywhere in our Central Florida service area.</p>
    <a class="area-link" href="{"../" * depth}service-areas.html">See all cities we serve {ICON['arrow']}</a>
  </div>
</div>
"""
