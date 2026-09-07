# -*- coding: utf-8 -*-
"""Home page."""

from sitedata import (SITE, CITIES, PRODUCTS, FAQS, CERTS, WHY,
                      COMPARE_COLS, COMPARE_ROWS)
from layout import head, header, footer, cta_band, quote_form, contact_panel, ICON

FEATURED = ["complete-home-system", "city-water-dual-tank",
            "premium-well-water-system", "hw800-alkapro"]

# Generated hero backdrop. Stands in until a real photo is dropped at
# assets/img/hero.jpg and --hero-photo is set in style.css.
HERO_ART = """<svg class="hero-art" viewBox="0 0 1440 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
  <defs>
    <linearGradient id="hgrad" x1="0" y1="0" x2="0.85" y2="1">
      <stop offset="0" stop-color="#06111f"/>
      <stop offset="52%" stop-color="#123356"/>
      <stop offset="100%" stop-color="#0e7794"/>
    </linearGradient>
    <radialGradient id="hglow" cx="74%" cy="24%" r="58%">
      <stop offset="0" stop-color="#4ad2ef" stop-opacity="0.50"/>
      <stop offset="100%" stop-color="#4ad2ef" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hglow2" cx="18%" cy="88%" r="46%">
      <stop offset="0" stop-color="#0b4f8a" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#0b4f8a" stop-opacity="0"/>
    </radialGradient>
    <filter id="caustics" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.0055 0.014" numOctaves="3" seed="11" result="noise"/>
      <feColorMatrix in="noise" type="matrix" result="light"
        values="0 0 0 0 0.36  0 0 0 0 0.80  0 0 0 0 0.92  0 0 0 -1.75 1.06"/>
      <feGaussianBlur in="light" stdDeviation="1.6"/>
    </filter>
    <filter id="caustics2" x="-15%" y="-15%" width="130%" height="130%" color-interpolation-filters="sRGB">
      <feTurbulence type="fractalNoise" baseFrequency="0.011 0.004" numOctaves="2" seed="4" result="noise"/>
      <feColorMatrix in="noise" type="matrix" result="light"
        values="0 0 0 0 0.62  0 0 0 0 0.90  0 0 0 0 1.00  0 0 0 -1.9 1.12"/>
      <feGaussianBlur in="light" stdDeviation="3"/>
    </filter>
  </defs>
  <rect width="1440" height="700" fill="url(#hgrad)"/>
  <rect width="1440" height="700" filter="url(#caustics)" opacity="0.62"/>
  <rect width="1440" height="700" filter="url(#caustics2)" opacity="0.34"/>
  <rect width="1440" height="700" fill="url(#hglow)"/>
  <rect width="1440" height="700" fill="url(#hglow2)"/>
  <g fill="#bff0fb" opacity="0.16">
    <circle cx="1180" cy="150" r="46"/><circle cx="1298" cy="286" r="22"/>
    <circle cx="1092" cy="336" r="13"/><circle cx="1340" cy="118" r="9"/>
    <circle cx="1236" cy="430" r="30"/><circle cx="1010" cy="196" r="7"/>
  </g>
  <g fill="none" stroke="#bff0fb" stroke-opacity="0.20" stroke-width="1.5">
    <circle cx="1180" cy="150" r="46"/><circle cx="1236" cy="430" r="30"/>
    <circle cx="1298" cy="286" r="22"/>
  </g>
</svg>"""

STEPS = [
    ("Tell us about your home",
     "Call, text, or send the form. We'll ask where your water comes from, how many people live there, and what you're noticing at the tap. Two minutes."),
    ("Get your price in writing",
     "One flat installed price, before anything is ordered. Our price-match promise stands behind it. No in-home pressure close, ever."),
    ("We install it",
     "Two to four hours. A licensed Florida plumber does the work. We leave the space cleaner than we found it."),
]

# The four symptoms people recognize instantly — these sit in the hero.
HERO_TILES = [
    ("\U0001F6BF", "Dry, itchy skin after a shower"),
    ("\U0001F37D\uFE0F", "Spotty dishes and glassware"),
    ("\U0001F455", "Stiff, faded laundry"),
    ("\U0001F6B0", "Chlorine taste and smell"),
]


# Duotone illustrations for the "damage you don't see" tiles.
def _art(paths):
    return ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + paths + '</svg>')

DAMAGE_ART = {
  # water heater: tall cylinder, inlet pipes, dial, scale settled in the base
  "heater": _art('<rect x="6.4" y="5" width="11.2" height="16" rx="2.6"/>'
                 '<path d="M9.4 5V2.9M14.6 5V2.9"/>'
                 '<circle cx="12" cy="11" r="1.7"/>'
                 '<path d="M6.4 16.4h11.2v2.1a2.5 2.5 0 0 1-2.5 2.5H8.9a2.5 2.5 0 0 1-2.5-2.5z" '
                 'fill="var(--aqua-500)" stroke="none"/>'),
  # washing machine: square body, large drum
  "washer": _art('<rect x="3.9" y="3" width="16.2" height="18" rx="3"/>'
                 '<circle cx="12" cy="14" r="4.7"/>'
                 '<circle cx="7.4" cy="6.4" r="1.05" fill="currentColor" stroke="none"/>'
                 '<path d="M12 9.3a4.7 4.7 0 0 1 4.7 4.7" stroke="var(--aqua-500)" stroke-width="2.3"/>'),
  # tapered tumbler with spots on the glass
  "glass":  _art('<path d="M6.9 3.4h10.2l-1.45 16.3a1.9 1.9 0 0 1-1.9 1.7h-3.5a1.9 1.9 0 0 1-1.9-1.7z"/>'
                 '<circle cx="10.6" cy="8.5" r="1.25" fill="var(--aqua-500)" stroke="none"/>'
                 '<circle cx="13.7" cy="12" r="1.05" fill="var(--aqua-500)" stroke="none"/>'
                 '<circle cx="11" cy="15.6" r="0.9" fill="var(--aqua-500)" stroke="none"/>'),
  # pump dispenser: spout arm makes the silhouette unmistakable
  "bottle": _art('<path d="M13.2 3.1h2.9v2.4h-2.6"/>'
                 '<path d="M11 5.5h2.2v2.1H11z"/>'
                 '<rect x="7.3" y="7.6" width="9.4" height="13.4" rx="2.5"/>'
                 '<path d="M7.3 14.4h9.4v4.1a2.5 2.5 0 0 1-2.5 2.5H9.8a2.5 2.5 0 0 1-2.5-2.5z" '
                 'fill="var(--aqua-500)" stroke="none"/>'),
  # droplet leaving a rust ring behind
  "rust":   _art('<path d="M12 2.9s3.9 4.4 3.9 7.3a3.9 3.9 0 0 1-7.8 0c0-2.9 3.9-7.3 3.9-7.3z"/>'
                 '<ellipse cx="12" cy="19.3" rx="6.1" ry="2.3" fill="var(--aqua-500)" stroke="none"/>'),
  # odor rising off the water line
  "odor":   _art('<path d="M3.4 19.4c2.1-1.5 4-.3 6.1 0 2.2.3 4.2-1.2 6.3-.6 1.8.5 3.5 1.2 5.2.5"/>'
                 '<path d="M7.9 13.9c0-2.5 2.5-2.5 2.5-5M13.6 12.6c0-2.5 2.5-2.5 2.5-5" '
                 'stroke="var(--aqua-500)" stroke-width="2.1"/>'),
}

# The damage that costs money but never announces itself.
SYMPTOMS = [
    ("heater", "Scale building inside your water heater"),
    ("washer", "Appliances wearing out years early"),
    ("glass",  "Chalky buildup on faucets and glass"),
    ("bottle", "Burning through soap, shampoo and detergent"),
    ("rust",   "Rust stains from iron in well water"),
    ("odor",   "Rotten-egg smell from sulfur"),
]


def product_media(p, depth=0, cls="card-media"):
    """Real product photo when we have one, labeled placeholder when we don't."""
    up = "../" * depth
    if p.get("img"):
        return (f'<div class="{cls}"><img src="{up}assets/img/{p["img"]}" '
                f'alt="{p["name"]}" loading="lazy" decoding="async"></div>')
    return f'<div class="ph" data-label="{p["photo"]}"></div>'


def product_card(p, depth=0):
    up = "../" * depth
    tag = f'<span class="card-tag">{p["tag"]}</span>' if p.get("tag") else ""
    return f"""<article class="card">
  {product_media(p, depth)}
  <div class="card-body">
    {tag}
    <h3>{p['name']}</h3>
    <p>{p['short']}</p>
    <div class="card-foot">
      <span class="card-price">Free quote</span>
      <a class="btn btn-outline btn-sm" href="{up}solutions/{p['slug']}.html">Learn more {ICON['arrow']}</a>
    </div>
  </div>
</article>"""


def _cell(v, is_us=False):
    cls = ' class="col-us"' if is_us else ""
    if v == "yes":
        return f'<td{cls}><span class="mark-yes" aria-label="Yes">✓</span></td>'
    if v == "no":
        return f'<td{cls}><span class="mark-no" aria-label="No">✗</span></td>'
    if v.startswith("no:"):
        return f'<td{cls}><span class="mark-no" aria-label="No">✗</span> <span class="cell-note">{v[3:]}</span></td>'
    return f'<td{cls}><span class="cell-note">{v}</span></td>'


def compare_table():
    heads = "".join(
        f'<th class="{"th-us" if i == 0 else ""}">{c}</th>'
        for i, c in enumerate(COMPARE_COLS)
    )
    rows = ""
    for row in COMPARE_ROWS:
        label, vals = row[0], row[1:]
        cells = "".join(_cell(v, i == 0) for i, v in enumerate(vals))
        rows += f"<tr><th scope='row'>{label}</th>{cells}</tr>"
    return f"""<div class="table-scroll">
  <table class="compare">
    <thead><tr><th scope="col">Feature</th>{heads}</tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>
<p class="table-note">Our own terms are shown in full. Competitor terms vary by dealer and location, so
we list them as "varies" rather than guess — confirm current terms directly with any company you're considering.</p>"""


def water_table():
    rows = ""
    for c in CITIES:
        lo = int(c["hard"].split("–")[0])
        hi = int(c["hard"].split("–")[1])
        pct = min(100, int(hi / 25 * 100))
        level = "Very hard" if lo >= 15 else ("Hard" if lo >= 10 else "Moderate–hard")
        rows += f"""<tr>
  <th scope="row"><a href="service-areas/{c['slug']}.html">{c['name']}</a><span class="row-sub">{c['county']}</span></th>
  <td class="num">{c['hard']}<span class="unit">gpg</span></td>
  <td class="hardcell"><span class="level">{level}</span><span class="bar"><i style="width:{pct}%"></i></span></td>
  <td class="issues">{' · '.join(c['issues'][:2])}</td>
</tr>"""
    return f"""<div class="table-scroll">
  <table class="watertable">
    <thead><tr>
      <th scope="col">City</th><th scope="col">Hardness</th>
      <th scope="col">Level</th><th scope="col">What we see most</th>
    </tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>
<p class="table-note">Figures are typical published ranges for each area's supply, not a measurement of your address.
Water differs between neighborhoods depending on which plant or well field serves you, and private wells vary property
to property. Above 7 gpg is considered hard.</p>"""



def build():
    by_slug = {p["slug"]: p for p in PRODUCTS}
    featured = "".join(product_card(by_slug[s]) for s in FEATURED)
    steps = "".join(
        f'<div class="step"><div class="step-n">{n+1}</div><h3>{t}</h3><p>{d}</p></div>'
        for n, (t, d) in enumerate(STEPS)
    )
    hero_tiles = "".join(
        f'<div class="hero-tile"><span class="hero-tile-icon" aria-hidden="true">{e}</span><span>{t}</span></div>'
        for e, t in HERO_TILES
    )
    symptoms = "".join(
        f'<li class="sym-tile"><span class="sym-icon">{DAMAGE_ART[k]}</span><span>{t}</span></li>'
        for k, t in SYMPTOMS
    )
    why = "".join(
        f'<div class="feature"><span class="feature-icon">{ICON[i]}</span><div><h4>{t}</h4><p>{d}</p></div></div>'
        for i, t, d in WHY
    )
    faqs = "".join(
        f'<details{" open" if n == 0 else ""}><summary>{q}</summary><div class="answer">{a}</div></details>'
        for n, (q, a) in enumerate(FAQS)
    )
    certs = "".join(
        f'<div class="cert"><span class="feature-icon">{ICON["shield"]}</span>'
        f'<div><h3>{t}</h3><p>{d}</p></div></div>'
        for t, d in CERTS
    )

    return head(
        "Water Filtration & Softening in the Orlando Area | Orlando Water Pros",
        "Whole-home water filtration and softening for Orlando and Central Florida. Softer showers, spot-free glassware, better laundry and chlorine removal. Free quotes, licensed installation, warranty in writing.",
    ) + header("home") + f"""
<section class="hero">
  {HERO_ART}
  <div class="hero-photo"></div>
  <div class="hero-scrim"></div>
  <div class="wrap">
    <div class="hero-inner">
      <span class="eyebrow" style="color:var(--aqua-500)">Orlando &amp; Central Florida</span>
      <h1>Water Filtration &amp; Softening in the Orlando Area</h1>
      <p class="hero-sub">Central Florida water is hard. Your house is paying for it.</p>
      <p class="hero-lede">Homes across Orange, Seminole, Osceola, Lake and Volusia counties test between 10 and 18 grains per gallon. That's scale in your water heater, film on your shower door, and laundry that never comes out soft. We fix it, usually in a single afternoon.</p>
      <div class="hero-badges">{hero_tiles}</div>
      <div class="btn-row">
        <a class="btn btn-primary" href="quote.html">Get a Free Quote</a>
        <a class="btn btn-ghost" href="solutions.html">See Solutions</a>
      </div>
      <p class="hero-note">Or call {SITE['phone_display']} — you'll reach someone local.</p>
    </div>
  </div>
</section>

<div class="badge-band">
  <div class="wrap">
    <div class="badge-row">
      <div class="badge-item">{ICON['shield']} Lifetime Limited Warranty</div>
      <div class="badge-item">{ICON['badge']} NSF-Certified Systems</div>
      <div class="badge-item">{ICON['tag']} Price-Match Promise</div>
      <div class="badge-item">{ICON['clock']} Same-Week Install</div>
    </div>
  </div>
</div>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">How it works</span>
      <h2>Three steps, no surprises</h2>
      <p>Professional-grade equipment. A price you see before you commit. A licensed Florida plumber doing the work.</p>
    </div>
    <div class="process">{steps}</div>
  </div>
</section>

<section class="section symptom-band">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">The expensive part</span>
      <h2>And the damage you don't see</h2>
    </div>
    <ul class="symptom-grid">{symptoms}</ul>
  </div>
</section>

<section class="section" id="solutions">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Our Solutions</span>
      <h2>The right system for your water</h2>
      <p>City water and well water are different problems with different answers. These four cover most Central Florida homes.</p>
    </div>
    <div class="grid g4">{featured}</div>
    <div class="center mt-l"><a class="btn btn-navy" href="solutions.html">See All Solutions {ICON['arrow']}</a></div>
  </div>
</section>


<section class="section section-alt">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">How we compare</span>
      <h2>What you're choosing between</h2>
      <p>There are a few ways to solve hard water in Central Florida. Here's how they compare.</p>
    </div>
    {compare_table()}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Water quality by city</span>
      <h2>What's in the water where you live</h2>
      <p>Hardness changes across Central Florida, and it changes inside Orlando too, depending on which plant serves your street.</p>
    </div>
    {water_table()}
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Credentials</span>
      <h2>Certified equipment, licensed installation</h2>
      <p>What our systems carry, and who puts them in your house.</p>
    </div>
    <div class="cert-grid">{certs}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Get started</span>
      <h2>Get a free quote</h2>
      <p>Tell us about your home. We'll come back with a flat installed price in writing.</p>
    </div>
    <div class="split" style="align-items:start">
      {quote_form()}
      {contact_panel()}
    </div>
  </div>
</section>


<section class="section section-navy">
  <div class="wrap">
    <div class="section-head center">
      <span class="eyebrow">Why us</span>
      <h2>What changes at your house</h2>
    </div>
    <div class="grid g3">{why}</div>
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap wrap-narrow">
    <div class="section-head center">
      <span class="eyebrow">FAQ</span>
      <h2>Questions we get a lot</h2>
    </div>
    <div class="faq">{faqs}</div>
  </div>
</section>

""" + cta_band() + footer()
