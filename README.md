# Orlando Water Pros

A 44-page static site for a Central Florida water filtration and softening business.
Plain HTML, CSS and JavaScript — no build step needed to run it.

```bash
cd hwcfl && python3 -m http.server 8000    # then open http://localhost:8000
```

---

## Structure

```
index.html                Home
solutions.html            All solutions, grouped by category
solutions/*.html          14 "learn more" pages, one per system
service-areas.html        14 Central Florida cities
service-areas/*.html      Per-city pages with local hardness data
resources.html            Article index
resources/*.html          6 written articles
about.html                Story + 5-step process + credentials
quote.html                Free quote form
contact.html              Form + contact panel + map slot
warranty.html             Lifetime warranty terms
privacy.html / terms.html Placeholders — need a lawyer
assets/css/style.css      Design system, one file
assets/js/main.js         Nav, dropdowns, scroller, form handler
build/                    Python generator — edit content, re-run, all pages regenerate
```

Edit `build/sitedata.py`, then `cd build && python3 build.py`. Run
`python3 bundle_preview.py` afterward to refresh the single-file preview.

---

## Three things I built differently than asked

**1. Photos.** The product images on the North Carolina site belong to that
franchisee or to the manufacturer. Copying them onto a differently-branded site
is straight copyright infringement, so every image is still a labeled slot.
The legitimate route to the exact same photos: ask the manufacturer for the
dealer marketing asset pack. Dealers almost always get one, and it's licensed
for your use.

**2. The BBB card.** You asked for "BBB A+ Accredited" in the hero. The
accreditation on that BBB profile belongs to Honest Water Co in McKinney, Texas
— not to Orlando Water Pros. Claiming another company's accreditation as your
own is exactly the kind of thing BBB and the FTC act on, and it's easy for a
competitor to report. The hero says **NSF-Certified Systems** instead, which is
true of the equipment. Apply for your own BBB accreditation and it goes back in.

Related: you asked to drop the "Official Honest Water Co Dealer" card but keep
the NSF and WQA cards. Those certifications attach to the equipment, and the
dealer relationship is what entitles you to cite them. I'd put a version of that
card back — "Factory-backed equipment, factory-trained installation" is on the
page now as a softer stand-in, but naming the manufacturer is stronger, not
weaker. It's the difference between "we have certifications" and "here's why."

**3. "Best prices in Florida."** An unqualified superiority claim needs
substantiation you can produce on demand. Your price-match promise says the same
thing and is defensible, so the badge reads **Price-Match Promise**.

---

## Comparison table

Built with named columns as you asked. Cells say "Varies by dealer" where terms
genuinely differ between franchise locations, because asserting a specific
warranty length or contract term for a named national company without
documentation is a false-advertising exposure — and those companies have legal
departments that watch for it.

Fill in a specific claim only when you have the source saved. A screenshot of the
competitor's own published terms, dated, is the standard.

---

## Before launch

**Contact details** — all placeholders, in `build/sitedata.py`:

- [ ] Phone — currently `(407) 555-0142`, a reserved fictional number
- [ ] Email and business hours
- [ ] Review count on the trust strip

No street address appears anywhere on the site — it's set up as a service-area
business. When you register a Google Business Profile, choose the service-area
option so the address stays hidden there too.

**Legal**

- [ ] **Reviews.** Six placeholder cards on the home page. Paste in real Google
      reviews. Fabricated testimonials carry FTC penalties per violation.
- [ ] **Warranty page.** Coverage is stated, but the highlighted terms need your
      exact language — especially the definition of "lifetime." It must match
      your customer paperwork.
- [ ] **Privacy policy and terms.** Outlines only.
- [ ] **SMS consent** language must match how you actually text customers (TCPA).
- [ ] **Licensing.** The credentials section says installations are done by
      licensed Florida plumbers. Add the license number — yours or your
      installing partner's.
- [ ] **Franchise agreement.** If you're an Honest Water Co franchisee, operating
      under a different name is usually a breach. Check before spending on this
      brand.

**Functional**

- [ ] **Connect the quote form.** It shows an error on submit by design. Point it
      at Formspree, Netlify Forms or your CRM. Handler is at the bottom of
      `assets/js/main.js`.
- [ ] **Embed your Google Map** in the contact panel.
- [ ] **Add photos and your logo** — the header uses a generated water-drop mark.
- [ ] **Social links** in the footer point at `#`.
- [ ] **Verify hardness figures** against each utility's Consumer Confidence
      Report, especially Orlando — OUC's numbers vary by treatment plant.
