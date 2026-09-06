# -*- coding: utf-8 -*-
"""Interior pages: solutions, about, contact, quote, service areas, resources, legal."""

from sitedata import (SITE, CITIES, PRODUCTS, PRODUCT_CATS, RESOURCES,
                      FAQS, CERTS, WHY, WARRANTY, SPECS)
from layout import (head, header, footer, cta_band, quote_form, contact_panel,
                    page_hero, ICON)
from pages_home import product_card, product_media


# ------------------------------------------------------------------ solutions
def solutions_index():
    blocks = []
    for cat in PRODUCT_CATS:
        items = [p for p in PRODUCTS if p["cat"] == cat]
        if not items:
            continue
        cards = "".join(product_card(p) for p in items)
        blocks.append(f"""<div class="cat-block">
  <h2 class="cat-title">{cat}</h2>
  <div class="grid g3">{cards}</div>
</div>""")
    return head(
        "Our Solutions | Orlando Water Pros",
        "Whole-home water softening and filtration, well water iron and sulfur systems, reverse osmosis drinking water and smart add-ons installed across Central Florida.",
    ) + header("solutions") + page_hero(
        "Our Solutions",
        "Whole-home treatment, well water systems, drinking water and add-ons. Which one you need depends on what's coming into your house.",
        '<a href="index.html">Home</a> / Our Solutions',
    ) + f"""<section class="section"><div class="wrap">{''.join(blocks)}</div></section>""" + cta_band() + footer()


def solution_page(p):
    bullets = "".join(f'<li><span class="tick">✓</span><span>{b}</span></li>' for b in p["bullets"])
    long = "".join(f"<p>{para}</p>" for para in p["long"])
    others = [x for x in PRODUCTS if x["slug"] != p["slug"] and x["cat"] == p["cat"]][:3]
    if len(others) < 3:
        others += [x for x in PRODUCTS if x["slug"] != p["slug"] and x not in others][:3 - len(others)]
    rel = "".join(product_card(x, depth=1) for x in others)
    faqs = "".join(
        f'<details><summary>{q}</summary><div class="answer">{a}</div></details>'
        for q, a in FAQS[:4]
    )
    rows = [("Category", p["cat"])] + SPECS.get(p["slug"], [])
    if p["slug"] not in ("hw800-alkapro", "5-stage-reverse-osmosis"):
        rows.append(("Warranty", "Lifetime on tanks, valves, electronics and components; 1 year labor"))
    spec_rows = "".join(f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in rows)
    return head(
        f"{p['name']} | Orlando Water Pros",
        p["short"], depth=1,
    ) + header("solutions", depth=1) + page_hero(
        p["name"], p["short"],
        '<a href="../index.html">Home</a> / <a href="../solutions.html">Our Solutions</a> / ' + p["name"],
    ) + f"""
<section class="section">
  <div class="wrap split">
    <div class="split-media">{product_media(p, 1, "detail-media")}</div>
    <div>
      <span class="eyebrow">{p['cat']}</span>
      <h2>What it does</h2>
      {long}
      <p class="who-line"><strong>Best for:</strong> {p['who']}</p>
      <div class="btn-row mt-m">
        <a class="btn btn-primary" href="../quote.html">Get a Free Quote</a>
        <a class="btn btn-outline" href="mailto:{SITE['email']}">{ICON['mail']} Email Us</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap wrap-narrow">
    <div class="section-head center"><span class="eyebrow">Included</span><h2>What you get</h2></div>
    <ul class="symptom-list big-list">{bullets}</ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center"><h2>Specifications</h2>
    <p>Published manufacturer specifications.</p></div>
    <div class="table-scroll">
      <table class="compare spec">
        <thead><tr><th scope="col">Specification</th><th scope="col">Details</th></tr></thead>
        <tbody>{spec_rows}</tbody>
      </table>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap wrap-narrow">
    <div class="section-head center"><h2>Common questions</h2></div>
    <div class="faq">{faqs}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">Also consider</span><h2>Related solutions</h2></div>
    <div class="grid g3">{rel}</div>
  </div>
</section>
""" + cta_band(depth=1) + footer(depth=1)


# ------------------------------------------------------------------ about
def about():
    why = "".join(
        f'<div class="feature"><span class="feature-icon">{ICON[i]}</span><div><h4>{t}</h4><p>{d}</p></div></div>'
        for i, t, d in WHY
    )
    certs = "".join(
        f'<div class="cert"><span class="feature-icon">{ICON["shield"]}</span>'
        f'<div><h3>{t}</h3><p>{d}</p></div></div>'
        for t, d in CERTS
    )
    steps = [
        ("Tell us about your home",
         "Send the form or email us. We'll ask where your water comes from, how many people live there, and what you're noticing at the tap."),
        ("A recommendation, and the reasoning",
         "We tell you which system fits and why, including when a cheaper one would serve you just as well."),
        ("A flat installed price in writing",
         "One number, before anything is ordered. If your plumbing adds cost, you hear it then. Not on install day."),
        ("Installation by a licensed Florida plumber",
         "Two to four hours for most systems. We leave the space cleaner than we found it."),
        ("Service afterward",
         "We send filter reminders when they're due and handle warranty service ourselves. Just email us directly."),
    ]
    step_html = "".join(f"""<div class="card"><div class="card-body">
      <span class="card-tag">Step {n+1}</span><h3 style="font-size:1.08rem">{t}</h3><p>{d}</p>
    </div></div>""" for n, (t, d) in enumerate(steps))
    return head(
        "About | Orlando Water Pros",
        "Locally owned water filtration and softening for Orlando and Central Florida. How we quote, install and service.",
    ) + header("about") + page_hero(
        "About Orlando Water Pros",
        "Water filtration and softening for Central Florida homes. Installed by licensed Florida plumbers, backed by a lifetime warranty.",
        '<a href="index.html">Home</a> / About',
    ) + f"""

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">Process</span><h2>What working with us looks like</h2>
    <p>Five steps, no surprises in the middle of them.</p></div>
    <div class="grid g3">{step_html}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">Credentials</span><h2>Certified equipment, licensed installation</h2></div>
    <div class="cert-grid">{certs}</div>
  </div>
</section>

<section class="section section-navy">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">Why us</span><h2>What you actually get</h2></div>
    <div class="grid g3">{why}</div>
  </div>
</section>
""" + cta_band() + footer()


# ------------------------------------------------------------------ quote
def quote_page():
    return head(
        "Get a Free Quote | Orlando Water Pros",
        "Request a free quote on water filtration or softening for your Central Florida home. Usually a same-business-day response.",
    ) + header("quote") + page_hero(
        "Get a free quote",
        "A flat installed price, in writing, before anything is ordered. Serving Orange, Seminole, Osceola, Lake and Volusia counties.",
        '<a href="index.html">Home</a> / Get a Free Quote',
    ) + f"""
<section class="section">
  <div class="wrap split" style="align-items:start">
    {quote_form()}
    {contact_panel()}
  </div>
</section>

<section class="section section-alt">
  <div class="wrap wrap-narrow">
    <div class="section-head center"><h2>What happens next</h2></div>
    <div class="grid g3">
      <div class="card"><div class="card-body"><span class="card-tag">1</span><h3 style="font-size:1.02rem">We call you back</h3>
      <p>At the time you picked. Usually the same business day.</p></div></div>
      <div class="card"><div class="card-body"><span class="card-tag">2</span><h3 style="font-size:1.02rem">We talk through your water</h3>
      <p>Where it comes from, who's using it, and what you're noticing.</p></div></div>
      <div class="card"><div class="card-body"><span class="card-tag">3</span><h3 style="font-size:1.02rem">You get a price in writing</h3>
      <p>A flat installed price, with our price-match promise behind it.</p></div></div>
    </div>
  </div>
</section>
""" + footer()


# ------------------------------------------------------------------ contact
def contact():
    return head(
        "Contact | Orlando Water Pros",
        "Contact Orlando Water Pros for water filtration and softening across Central Florida — request a free quote online.",
    ) + header("contact") + page_hero(
        "Get in touch",
        "Serving Orange, Seminole, Osceola, Lake and Volusia counties. Same-day response on weekdays.",
        '<a href="index.html">Home</a> / Contact',
    ) + f"""
<section class="section">
  <div class="wrap split" style="align-items:start">
    {quote_form()}
    {contact_panel()}
  </div>
</section>

""" + footer()


# ------------------------------------------------------------------ areas
def areas_index():
    cards = "".join(f"""<a class="card" href="service-areas/{c['slug']}.html">
  <div class="card-body">
    <span class="card-tag">{c['county']}</span>
    <h3>{c['name']}</h3>
    <p>Typical hardness {c['hard']} gpg · {c['supply']}</p>
    <div class="card-foot"><span class="card-price">Local water info</span>{ICON['arrow']}</div>
  </div>
</a>""" for c in CITIES)
    return head(
        "Service Areas | Orlando Water Pros",
        "Water softening and filtration installation across Orange, Seminole, Osceola, Lake and Volusia counties in Central Florida.",
    ) + header("areas") + page_hero(
        "Where we work",
        "We cover Orange, Seminole, Osceola, Lake and Volusia counties. Pick your city for local water conditions.",
        '<a href="index.html">Home</a> / Service Areas',
    ) + f"""<section class="section"><div class="wrap"><div class="grid g3">{cards}</div>
  <p class="muted mt-l center">Not on the list? <a href="quote.html">Send us a quick message</a> — we cover more of Central Florida than we've listed here.</p>
</div></section>""" + cta_band() + footer()


def city_page(c):
    issues = "".join(f'<li><span class="tick">!</span><span>{x}</span></li>' for x in c["issues"])
    hi = int(c["hard"].split("–")[1])
    pct = min(100, int(hi / 25 * 100))
    recs = [p for p in PRODUCTS if p["cat"] in ("Whole Home", "Well Water", "Drinking Water")][:3]
    cards = "".join(product_card(p, depth=1) for p in recs)
    nearby = "".join(
        f'<a class="chip" href="{x["slug"]}.html">{x["name"]}</a>'
        for x in CITIES if x["slug"] != c["slug"]
    )
    faqs = "".join(
        f'<details><summary>{q}</summary><div class="answer">{a}</div></details>'
        for q, a in FAQS[:4]
    )
    return head(
        f"Water Softening & Filtration in {c['name']}, FL | Orlando Water Pros",
        f"Water filtration and softening in {c['name']}, {c['county']}. Typical hardness {c['hard']} grains per gallon. Free quotes, lifetime warranty.",
        depth=1,
    ) + header("areas", depth=1) + page_hero(
        f"Water filtration &amp; softening in {c['name']}, FL",
        f"{c['county']} · Typical hardness {c['hard']} grains per gallon · Supply: {c['supply']}",
        '<a href="../index.html">Home</a> / <a href="../service-areas.html">Service Areas</a> / ' + c["name"],
    ) + f"""
<section class="section">
  <div class="wrap">
    <div class="readout">
      <div class="stat"><div class="k">Typical hardness</div>
        <div class="v">{c['hard']} <span class="unit-lg">gpg</span></div>
        <div class="d">Above 7 gpg is considered hard water.</div>
        <div class="bar"><i style="width:{pct}%"></i></div></div>
      <div class="stat"><div class="k">Water supply</div>
        <div class="v" style="font-size:1.15rem">{c['supply']}</div>
        <div class="d">{c['county']}</div></div>
      <div class="stat"><div class="k">Common complaints</div>
        <ul class="symptom-list" style="margin-top:10px">{issues}</ul></div>
    </div>
    <div class="split mt-l">
      <div>
        <h2>What {c['name']} homeowners are dealing with</h2>
        <p class="lede">{c['note']}</p>
        <p>The hardness figures here are typical published ranges for the area's supply. They're a starting point, not a measurement of your house. Water changes between neighborhoods depending on which well field or plant serves you, and on a private well it changes from one property to the next.</p>
        <div class="btn-row mt-m">
          <a class="btn btn-primary" href="../quote.html">Get a Free Quote in {c['name']}</a>
          <a class="btn btn-outline" href="mailto:{SITE['email']}">{ICON['mail']} Email Us</a>
        </div>
      </div>
      <div class="split-media"><div class="ph" data-label="Photo: an install in {c['name']}"></div></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head center"><span class="eyebrow">Our Solutions</span><h2>Systems that suit {c['name']} water</h2>
    <p>Based on typical conditions in {c['county']}.</p></div>
    <div class="grid g3">{cards}</div>
  </div>
</section>

<section class="section">
  <div class="wrap wrap-narrow">
    <div class="section-head center"><h2>Common questions</h2></div>
    <div class="faq">{faqs}</div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap center">
    <h2 style="font-size:1.4rem">We also serve</h2>
    <div class="chips mt-m" style="justify-content:center">{nearby}</div>
  </div>
</section>
""" + cta_band(depth=1) + footer(depth=1)


# ------------------------------------------------------------------ resources
def resources_index():
    cards = "".join(f"""<a class="card" href="resources/{r['slug']}.html">
  <div class="ph ph-wide" data-label="Article image"></div>
  <div class="card-body"><h3 style="font-size:1.1rem">{r['title']}</h3><p>{r['blurb']}</p>
  <div class="card-foot"><span class="card-price">Read article</span>{ICON['arrow']}</div></div>
</a>""" for r in RESOURCES)
    return head(
        "Water Resources | Orlando Water Pros",
        "Plain-English guides to hard water, well water iron and sulfur, chloramine and softener sizing in Central Florida.",
    ) + header("resources") + page_hero(
        "Water, explained",
        "No sales pitch. Just what's in Central Florida water, why it's there, and what fixes it.",
        '<a href="index.html">Home</a> / Resources',
    ) + f"""<section class="section"><div class="wrap"><div class="grid g3">{cards}</div></div></section>""" + cta_band() + footer()


def article_page(r):
    body = "".join(f"<p>{para}</p>" for para in r["body"])
    others = [x for x in RESOURCES if x["slug"] != r["slug"]][:3]
    rel = "".join(
        f'<a class="card" href="{x["slug"]}.html"><div class="card-body">'
        f'<h3 style="font-size:1.02rem">{x["title"]}</h3><p>{x["blurb"]}</p></div></a>'
        for x in others
    )
    return head(
        f"{r['title']} | Orlando Water Pros",
        r["blurb"], depth=1,
    ) + header("resources", depth=1) + page_hero(
        r["title"], r["blurb"],
        '<a href="../index.html">Home</a> / <a href="../resources.html">Resources</a> / ' + r["title"],
    ) + f"""
<section class="section">
  <div class="wrap wrap-narrow">
    <div class="ph ph-wide" data-label="Article header image" style="border-radius:var(--radius-l);margin-bottom:34px"></div>
    <div class="article-body">{body}</div>
    <div class="cta-band mt-l">
      <div><h2 style="font-size:1.35rem">Ready for a price?</h2>
      <p>A flat installed price on the system your home needs, in writing.</p></div>
      <a class="btn btn-primary" href="../quote.html">Get a Free Quote</a>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <div class="section-head center"><h2>More reading</h2></div>
    <div class="grid g3">{rel}</div>
  </div>
</section>
""" + footer(depth=1)


# ------------------------------------------------------------------ warranty
def warranty_page():
    rows = "".join(
        f'<tr><th scope="row">{k}</th><td>{v}</td></tr>' for k, v in WARRANTY["covered"]
    )
    notes = "".join(f"<li>{n}</li>" for n in WARRANTY["notes"])
    return head(
        "Warranty | Orlando Water Pros",
        "Lifetime warranty on whole-home system tanks, valves, electronics and components, plus one year of labor.",
    ) + header("") + page_hero(
        "Warranty",
        WARRANTY["intro"],
        '<a href="index.html">Home</a> / Warranty',
    ) + f"""
<section class="section">
  <div class="wrap wrap-narrow">
    <h2>What's covered</h2>
    <div class="table-scroll mt-m">
      <table class="compare spec">
        <thead><tr><th scope="col">Item</th><th scope="col">Coverage</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>

    <h2 class="mt-l">Terms and conditions</h2>
    <ul class="term-list">{notes}</ul>

    <div class="notice mt-l">
      <strong>Before publishing:</strong> this page states the coverage as described to us, but the highlighted
      items still need your exact terms. Whatever appears here must match your customer paperwork and what your
      salespeople say — an advertised warranty that doesn't match the written one is a consumer protection problem,
      and "lifetime" in particular has to be defined. Have an attorney review this page.
    </div>

    <h2 class="mt-l">Making a claim</h2>
    <p>Email <a href="mailto:{SITE['email']}">{SITE['email']}</a> with your installation date handy.
    We handle warranty service directly rather than routing it through a national dispatch queue.</p>
  </div>
</section>
""" + cta_band() + footer()


# ------------------------------------------------------------------ legal
LEGAL = {
    "privacy": ("Privacy Policy", "How we handle information submitted through this site.", [
        f"{SITE['brand']} (\"we,\" \"us\") operates this website. This policy explains what information we collect when you use it and how we handle that information.",
        "<strong>Information we collect.</strong> When you submit our quote or contact form, we collect your first and last name, phone number, email address, ZIP code, best time to reach you, and anything you choose to tell us in the message field. We don't collect payment information through this site.",
        "<strong>How we use it.</strong> We use this information to contact you about your quote, schedule service, and respond to questions you send us. We don't sell your information, and we don't share it with third parties except the tools we use to run our business — such as scheduling or email software — and only as needed to provide our service to you.",
        "<strong>How long we keep it.</strong> We keep quote and contact information for as long as needed to follow up with you and, if you become a customer, for the life of your service relationship with us plus a reasonable period afterward for warranty and record-keeping purposes.",
        "<strong>Your choices.</strong> You can ask us to delete the information you've submitted, or to stop contacting you, at any time by emailing us at "
        f"<a href=\"mailto:{SITE['email']}\">{SITE['email']}</a>. We'll honor that request except where we need to keep limited records for legal or warranty purposes.",
        "<strong>Cookies and analytics.</strong> This site does not use advertising cookies or tracking pixels. If that changes in the future, this policy will be updated to disclose it.",
        "<strong>Contact.</strong> Questions about this policy can be sent to "
        f"<a href=\"mailto:{SITE['email']}\">{SITE['email']}</a>.",
    ]),
    "terms": ("Terms of Service", "The terms that govern use of this website.", [
        f"By using this website, you agree to these terms. If you don't agree, please don't use the site.",
        "<strong>Purpose of this site.</strong> This website provides general information about the water filtration and softening systems and services offered by "
        f"{SITE['brand']}. Content on this site — including water hardness figures, product descriptions, and comparisons — is general information, not a guarantee of results for any specific property. An in-home or phone consultation is required to determine what your home actually needs.",
        "<strong>No professional advice.</strong> Nothing on this site is engineering, plumbing, health, or legal advice. Always consult a licensed professional for advice specific to your property.",
        "<strong>Ownership.</strong> The text, layout, and design of this site belong to "
        f"{SITE['brand']}. Product names, images, and specifications belong to their respective manufacturers.",
        "<strong>Limitation of liability.</strong> This site is provided \"as is.\" To the fullest extent permitted by law, "
        f"{SITE['brand']} isn't liable for damages arising from your use of, or inability to use, this website.",
        "<strong>The actual sale and installation.</strong> Pricing, scheduling, payment, cancellation, and installation terms are governed by the written quote and service agreement you receive directly from us — not by this website.",
        "<strong>Governing law.</strong> These terms are governed by the laws of the State of Florida.",
        "<strong>Contact.</strong> Questions about these terms can be sent to "
        f"<a href=\"mailto:{SITE['email']}\">{SITE['email']}</a>.",
    ]),
}


def legal_page(key):
    title, sub, paras = LEGAL[key]
    body = "".join(f"<p>{p}</p>" for p in paras)
    return head(
        f"{title} | Orlando Water Pros", sub,
    ) + header("") + page_hero(title, sub, '<a href="index.html">Home</a> / ' + title) + f"""
<section class="section"><div class="wrap wrap-narrow">
  <div class="form-card article-body">{body}</div>
  <p class="muted mt-m">Last updated: September 6, 2026</p>
</div></section>
""" + footer()
