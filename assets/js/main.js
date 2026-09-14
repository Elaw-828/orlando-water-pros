/* Honest Water Central Florida — site behavior */
(function () {
  "use strict";

  var docBound = false;

  function bindDocumentOnce(getMenus) {
    if (docBound) return;
    docBound = true;
    document.addEventListener("click", function () {
      getMenus().forEach(function (x) { x.classList.remove("open"); });
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") getMenus().forEach(function (x) { x.classList.remove("open"); });
    });
  }

  function init(root) {
    root = root || document;

    /* ---- mobile nav ---- */
    var toggle = root.querySelector(".nav-toggle");
    var nav = root.querySelector("#primary-nav");
    if (toggle && nav) {
      toggle.addEventListener("click", function () {
        var open = nav.classList.toggle("open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }

    /* ---- dropdown menus ---- */
    var menus = Array.prototype.slice.call(root.querySelectorAll(".has-menu"));
    menus.forEach(function (m) {
      var btn = m.querySelector("button");
      if (!btn) return;
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        var wasOpen = m.classList.contains("open");
        menus.forEach(function (x) { x.classList.remove("open"); });
        if (!wasOpen) m.classList.add("open");
        btn.setAttribute("aria-expanded", !wasOpen ? "true" : "false");
      });
    });
    bindDocumentOnce(function () {
      return Array.prototype.slice.call(document.querySelectorAll(".has-menu"));
    });

    /* ---- tabs ---- */
    root.querySelectorAll("[data-tabs]").forEach(function (group) {
      var tabs = group.querySelectorAll(".tab");
      var panels = group.querySelectorAll(".tabpanel");
      tabs.forEach(function (tab) {
        tab.addEventListener("click", function () {
          tabs.forEach(function (t) { t.setAttribute("aria-selected", "false"); });
          panels.forEach(function (p) { p.classList.remove("is-active"); });
          tab.setAttribute("aria-selected", "true");
          var panel = group.querySelector("#" + tab.getAttribute("aria-controls"));
          if (panel) panel.classList.add("is-active");
        });
      });
    });

    /* ---- testimonial scroller ---- */
    root.querySelectorAll("[data-scroller]").forEach(function (wrapEl) {
      var track = wrapEl.querySelector(".quote-track");
      var prev = wrapEl.querySelector("[data-prev]");
      var next = wrapEl.querySelector("[data-next]");
      if (!track) return;
      function step() {
        var first = track.querySelector(".quote");
        return first ? first.getBoundingClientRect().width + 22 : 340;
      }
      if (prev) prev.addEventListener("click", function () { track.scrollBy({ left: -step(), behavior: "smooth" }); });
      if (next) next.addEventListener("click", function () { track.scrollBy({ left: step(), behavior: "smooth" }); });
    });

    /* ---- quote form ----------------------------------------------------
       POSTs JSON to the endpoint in data-endpoint (a GoHighLevel Inbound
       Webhook URL, set via SITE["form_endpoint"] in build/sitedata.py).
       With no endpoint set it falls back to opening the visitor's mail app
       pre-filled, so a submission is never silently dropped.              */
    root.querySelectorAll("form[data-quote-form]").forEach(function (form) {
      var out = form.querySelector("[data-form-msg]");
      var btn = form.querySelector("[data-form-submit]");
      var btnText = btn ? btn.textContent : "";
      var endpoint = (form.getAttribute("data-endpoint") || "").trim();
      var email = form.getAttribute("data-email") || "";
      var phone = form.getAttribute("data-phone") || "";

      function say(msg, tone) {
        if (!out) return;
        out.textContent = msg;
        out.style.color = tone === "bad" ? "#c0392b" : (tone === "good" ? "#1d7a4c" : "");
      }
      function busy(on) {
        if (!btn) return;
        btn.disabled = on;
        btn.textContent = on ? "Sending\u2026" : btnText;
      }
      function values() {
        var d = {};
        new FormData(form).forEach(function (v, k) { d[k] = v; });
        d.page = location.pathname.replace(/^\//, "") || "index.html";
        d.submitted_at = new Date().toISOString();
        return d;
      }

      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (!form.reportValidity()) return;

        var data = values();
        if (data.company) return;          /* honeypot: silently drop bots */
        delete data.company;

        if (!endpoint) {
          var body =
            "Name: " + (data.first_name || "") + " " + (data.last_name || "") + "\n" +
            "Phone: " + (data.phone || "") + "\n" +
            "Email: " + (data.email || "") + "\n" +
            "ZIP: " + (data.zip || "") + "\n" +
            "Best time to call: " + (data.best_time || "") + "\n\n" +
            (data.message || "");
          say("Opening your email app so you can send this over \u2014 or just call " + phone + ".");
          window.location.href = "mailto:" + email +
            "?subject=" + encodeURIComponent("Quote request \u2014 " + (data.first_name || "") + " " + (data.last_name || "")) +
            "&body=" + encodeURIComponent(body);
          return;
        }

        busy(true);
        say("Sending\u2026");
        fetch(endpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(data)
        }).then(function (r) {
          if (!r.ok) throw new Error(r.status);
          form.reset();
          say("Thanks \u2014 we've got it. We'll call you back, usually the same business day.", "good");
          if (btn) { btn.disabled = true; btn.textContent = "Sent"; }
        }).catch(function () {
          busy(false);
          say("That didn't go through. Please call " + phone + " or email " + email + ".", "bad");
        });
      });
    });

    /* ---- current year ---- */
    root.querySelectorAll("[data-year]").forEach(function (el) {
      el.textContent = new Date().getFullYear();
    });
  }

  window.HW_init = init;
  init(document);
})();
