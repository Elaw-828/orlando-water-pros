# Orlando Water Pros — website repo

26-page static site. All HTML is **generated** by a small Python build system and
committed to the repo; Vercel serves the committed files directly.
Repo: `github.com/Elaw-828/orlando-water-pros`, branch `main`.

---

## 1. Never hand-edit the generated HTML

Every `.html`, plus `sitemap.xml` and `robots.txt`, is output. Editing them is
always wrong — the next build silently overwrites your work. Edit these instead:

| File | Holds |
|---|---|
| `build/sitedata.py` | All content: `SITE` config, products, 14 cities, SPECS, FAQs, warranty, certs, comparison table, maintenance table |
| `build/layout.py` | Page chrome: `<head>`, top bar, nav, footer, quote form, contact panel, inline icons |
| `build/pages_home.py` | Home page + shared `product_card` / table helpers. **`FEATURED` on line 8 is a hardcoded slug list** |
| `build/pages_rest.py` | Every interior page (solutions index, product pages, cities, about, quote, contact, warranty, legal) |
| `build/build.py` | Orchestrator; injects canonical/OG tags, writes sitemap + robots, runs `clean()` |
| `build/bundle_preview.py` | Bundles the whole site into single-file `preview.html` (gitignored) |

Styling lives in `assets/css/style.css`; form behaviour in `assets/js/main.js`.

---

## 2. Building

```
cd build && python3 build.py
```

### Environment facts that matter

- **Python is NOT installed on Everett's Windows machine.** He cannot run the
  build himself in cmd. Don't hand him a command that starts with `python`.
- **Python 3.10 IS available in the `device_bash` VM**, which mounts the repo at
  `$HOME/mnt/Website/hwcfl`. Build there — it's far cheaper than rebuilding in the
  cloud container and shuttling files back.
- **`build.py`'s `clean()` does `shutil.rmtree` on `solutions/`.** `device_bash`
  blocks deletes by default, so the build dies with
  `PermissionError: Operation not permitted`. Call
  `device_request_delete_permission` on `C:\Users\evere\Documents\Website` **first**.
  That same `rmtree` is why removed product pages disappear on their own —
  `git add -A` stages the deletions and no `git rm` is needed.
- The mounted repo often leaves a stale `.git/index.lock`. `rm -f .git/index.lock`
  before git commands. `core.fileMode false` is already set.
- If you do build in the cloud container, `device_commit_files` caps at **50 files
  per call**; a full rebuild is ~28 files plus sitemap and robots.

---

## 3. Shipping

**Neither sandbox can reach github.com** (403 at the egress proxy). Claude can
commit locally; **Everett runs the push.**

Commit message is exactly:

```
a few changes
```

One line. No body, no trailers, no co-author lines. He has objected to long
messages twice, pointedly.

---

## 4. Current state (Nov 2026)

**3 products**, 2 categories:

| Slug | Category | Note |
|---|---|---|
| `softener-carbon-filtration` | Whole Home | main seller, carries the "Most Popular" badge |
| `city-water-dual-tank` | Whole Home | |
| `well-water-dual-tank` | Well Water | |

Removed Oct 2026 and **not to be reinstated without asking**: Complete Home System,
whole-home carbon filter, premium well water system, salt-free conditioner, and both
RO units (`hw800-alkapro`, `5-stage-reverse-osmosis`). The pre-sediment filter was
removed earlier.

`SITE` config: phone `(689) 210-3180`, email `hello@orlandowaterpros.com`,
domain `www.orlandowaterpros.com`, `show_forms: True`, `chat_widget: False`.

---

## 5. Hard rules

### Data provenance — read this before touching any number

The 14 per-city hardness ranges in `sitedata.py` are **NOT sourced**, despite the
code comment claiming they come from the EWG Tap Water Database. EWG tracks
contaminants, not hardness. An audit in Oct 2026 found:

- **13 of the 14 utilities publish no hardness figure at all.** Hardness has no
  federal MCL and isn't on Florida's secondary standards list, so the FDEP CCR
  template omits it. Clermont's own site search for "hardness" returns zero results.
- **The only real published number is OUC's**: "129 ppm or 7 gpg" on ouc.com.
  The site currently says Orlando is 6–15. That contradicts the utility.
- Every competitor hardness map is invented, because there's nothing to cite.

Everett chose to leave the figures in place for now. **Treat them as known-bad.**
Do not add new city figures, do not cite them as sourced, and do not build
marketing claims on them. Full audit with every source URL and the utility phone
numbers: `Claude outputs/hardness-audit.md`.

The general rule this came from: **never publish a figure without a primary source
and never describe a number as sourced when it isn't.**

### No licensing or insurance claims

All "licensed and insured" / "licensed Florida plumber" language was deliberately
stripped. Everett works with a plumber licensed through a company but not
individually. The site leans on the Florida **489.103(15) water-conditioning
exemption**. Do not add a license number, do not add "insured", and do not
reinstate either in copy, ads or apparel. An older version of the site skill
wrongly advised adding a license number — ignore that.

### Banned sentence

Never write, in any copy: *"We can run a line to the refrigerator and ice maker
while we're there."*

### Brand

Navy + aqua only; amber was removed deliberately.
`--navy-900 #0d1f3f` · `--aqua-500 #16a6c9` · `--aqua-600 #0f8fae`
Fonts: Plus Jakarta Sans (headings), Inter (body).
Logos in `assets/img/logo/` — light and dark of each lockup. WQA Gold Seal applies
to the **resin**, not to the company or the system; never claim otherwise.

---

## 6. The quote form

Posts JSON to a GoHighLevel inbound webhook (`SITE['form_endpoint']`).

Three non-obvious behaviours in `assets/js/main.js`, all of which were real bugs:

1. **GHL returns HTTP 200 with `{"status":"Error: ..."}` when it rejects a payload.**
   Checking `r.ok` alone reports success while silently dropping the lead. The
   handler inspects the response body. Don't "simplify" that away.
2. A capture-phase `invalid` listener is required — the browser blocks the submit
   event entirely when a required field fails, so the handler never runs and the
   user sees no message at all.
3. The honeypot field is `b_ref_7`, not `company`. Password managers autofill
   anything named "company" and silently killed real submissions. It sets a
   `spam_suspected` flag rather than dropping the lead.

`leadconnectorhq.com` is **blocked by the egress proxy** from both the cloud
container and `device_bash`. The only way to test the webhook is the built-in
browser running from the live site, which also gives the true production origin
for CORS.

---

## 7. Verification before shipping

These have each caught a real bug:

- Grep generated HTML for owner-facing leftovers: `needs-edit`, `add your`,
  `placeholder`, `Before publishing`.
- Walk every `href`/`src` in the output and confirm it resolves on disk.
- Grep for CSS tokens referenced by inline SVGs (`var(--aqua-500)` etc.) — renaming
  a token in `style.css` breaks them silently.
- Screenshot at 1280px and 390px with Playwright (`/opt/pw-browsers/chromium`).
  Check the header doesn't wrap and mobile has no horizontal overflow. **Lazy-loaded
  images report broken until scrolled into view** — scroll first.
- Colour changes need WCAG math, not eyeballing: ≥4.5:1 text, ≥3:1 large UI. An
  aqua-on-aqua swap once put the primary button at 1.32:1.
- Removing a product? Check `pages_home.py` `FEATURED` (hardcoded slugs → `KeyError`),
  `PRODUCT_CATS` for now-empty categories, grid column counts, `SPECS` keys, the
  MAINTENANCE table, FAQs, warranty copy, and the OG image in `build.py`.

---

## 8. Supplier

Equipment comes from **Honest Water Co** (Fort Worth, TX). Published spec sheet:
`honestwaterco.com/specs/standard-softener-filtration`.

The main unit (Standard Whole-Home Softener + Filtration): 10"×54" Enpress tank,
15"×35" brine tank, ResinTech CG10 10%-crosslinked resin + Jacobi coconut carbon,
1.5 cu ft combined, 48,000 grains, Honest ProValve (Hankscraft ceramic disc),
120V/60Hz via 12V 650mA transformer, 28 GPM valve / 27 GPM service at 15 PSI drop,
3.0 GPM backwash, 1" ports, 30–125 PSI, NSF/ANSI 44/42/61.

**Unresolved:** 48,000 grains from 1.5 cu ft of *combined* resin and carbon doesn't
reconcile — standard cation resin yields ~30,000 grains/cu ft. Either the 1.5 is
resin-only or the rating is optimistic. Salt dose per regeneration is unpublished.
Don't quote either number to a customer until Honest Water confirms.

Their warranty terms, installer claims and PFAS/VOC reduction claims are **theirs**,
not Orlando Water Pros'. Don't copy them across without substantiation.

---

## 9. Still open

- Quote form live, but confirm the GHL workflow is published and field-mapped.
- No real reviews yet — that section was removed rather than filled with fakes.
- Permit requirements unconfirmed with Orange/Seminole/Osceola/Lake/Volusia counties.
- Windermere's water provider is unverified; the site claims Orange County
  Utilities, and OCU doesn't list Windermere in three years of reports.
- Apopka: a local outlet reported in Aug 2026 that the state is investigating 11
  possible water system violations. Unverified against FDEP. Check before naming
  Apopka in paid advertising.
