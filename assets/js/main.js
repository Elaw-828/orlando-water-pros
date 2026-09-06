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

    /* ---- quote form (front-end only until a backend is wired up) ---- */
    root.querySelectorAll("form[data-quote-form]").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var out = form.querySelector("[data-form-msg]");
        if (out) {
          out.textContent =
            "This form is not connected to an inbox yet. Hook it up to your form service " +
            "(Formspree, Netlify Forms, HubSpot, etc.) before the site goes live.";
          out.style.color = "#c0392b";
        }
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
