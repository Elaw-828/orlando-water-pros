# -*- coding: utf-8 -*-
"""Bundle the whole static site into one self-contained, click-through preview page."""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(ROOT, "preview.html")

BODY_RE = re.compile(r"<body>(.*)</body>", re.S)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S)
SCRIPT_RE = re.compile(r'<script src="[^"]*"></script>\s*', re.S)


def collect():
    pages = {}
    for dirpath, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in ("build", "assets", "__pycache__")]
        for f in sorted(files):
            if not f.endswith(".html") or f == "preview.html":
                continue
            full = os.path.join(dirpath, f)
            rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
            src = open(full, encoding="utf-8").read()
            body = BODY_RE.search(src)
            title = TITLE_RE.search(src)
            if not body:
                continue
            pages[rel] = {
                "t": title.group(1).strip() if title else rel,
                "h": SCRIPT_RE.sub("", body.group(1)).strip(),
            }
    return pages


def inline_images(pages):
    """Collect assets/img/** as data URIs once, and point pages at them by
    relative name. Only images a page actually references are embedded, so
    export-only files (large PNG logo exports) stay out of the bundle."""
    import base64
    import mimetypes
    img_dir = os.path.join(ROOT, "assets", "img")
    uris = {}
    if not os.path.isdir(img_dir):
        return uris
    for dirpath, _dirnames, filenames in os.walk(img_dir):
        for fn in sorted(filenames):
            path = os.path.join(dirpath, fn)
            name = os.path.relpath(path, img_dir).replace(os.sep, "/")
            mime = mimetypes.guess_type(fn)[0] or "application/octet-stream"
            if name.endswith(".svg"):
                mime = "image/svg+xml"
            with open(path, "rb") as fh:
                uris[name] = f"data:{mime};base64," + base64.b64encode(fh.read()).decode()

    used = set()
    for page in pages.values():
        for name in uris:
            for prefix in ("../", ""):
                token = f'src="{prefix}assets/img/{name}"'
                if token in page["h"]:
                    page["h"] = page["h"].replace(token, f'data-img="{name}"')
                    used.add(name)
    return {k: v for k, v in uris.items() if k in used}


def main():
    css = open(os.path.join(ROOT, "assets/css/style.css"), encoding="utf-8").read()
    js = open(os.path.join(ROOT, "assets/js/main.js"), encoding="utf-8").read()
    pages = collect()
    img_uris = inline_images(pages)
    print(f"inlined {len(img_uris)} images (deduped)")
    data = json.dumps(pages, ensure_ascii=False).replace("</", "<\\/")
    imgdata = json.dumps(img_uris, ensure_ascii=False)

    html = f"""<title>Orlando Water Pros</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Plus+Jakarta+Sans:wght@600;700;800&display=swap" rel="stylesheet">
<style>
{css}
</style>

<div id="app"></div>

<script>
{js}
</script>

<script>
(function () {{
  "use strict";
  var PAGES = {data};
  var IMG = {imgdata};
  var app = document.getElementById("app");
  var current = "index.html";

  function normalize(base, href) {{
    var parts = base.split("/").slice(0, -1).concat(href.split("/"));
    var out = [];
    parts.forEach(function (p) {{
      if (p === "" || p === ".") return;
      if (p === "..") {{ out.pop(); return; }}
      out.push(p);
    }});
    return out.join("/");
  }}

  function render(path, push) {{
    var page = PAGES[path];
    if (!page) return false;
    current = path;
    app.innerHTML = page.h;
    app.querySelectorAll("img[data-img]").forEach(function (el) {{
      var u = IMG[el.getAttribute("data-img")];
      if (u) el.src = u;
    }});
    document.title = page.t;
    if (window.HW_init) window.HW_init(app);
    window.scrollTo({{ top: 0, behavior: "instant" }});
    if (push) {{
      try {{ history.pushState({{ p: path }}, "", "#/" + path); }} catch (e) {{}}
    }}
    return true;
  }}

  app.addEventListener("click", function (e) {{
    var a = e.target.closest ? e.target.closest("a[href]") : null;
    if (!a) return;
    var href = a.getAttribute("href");
    if (!href || /^(https?:|tel:|mailto:|#)/.test(href)) return;
    var target = normalize(current, href.split("#")[0]);
    if (PAGES[target]) {{
      e.preventDefault();
      render(target, true);
    }}
  }});

  window.addEventListener("popstate", function (e) {{
    var p = (e.state && e.state.p) || (location.hash || "").replace(/^#\\//, "") || "index.html";
    render(p, false);
  }});

  var start = (location.hash || "").replace(/^#\\//, "");
  render(PAGES[start] ? start : "index.html", false);
}})();
</script>
"""
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", OUT, f"({len(html)/1024:.0f} KB, {len(pages)} pages)")


if __name__ == "__main__":
    main()
