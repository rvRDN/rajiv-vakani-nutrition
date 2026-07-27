/* Contents Thread — sync open state + aria with existing menu toggles.
   Reserves classic scrollbar width so the two-line / X control does not shift. */
(function () {
  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  ready(function () {
    var toggle = document.querySelector(".menu-toggle");
    var links = document.querySelector(".nav-links");
    if (!toggle || !links) return;

    var sbw = 0;

    function measureScrollbar() {
      sbw = Math.max(0, window.innerWidth - document.documentElement.clientWidth);
    }

    function applyCompensation(open) {
      document.documentElement.style.setProperty("--thread-sbw", open ? sbw + "px" : "0px");
    }

    function sync() {
      var open = links.classList.contains("active");
      applyCompensation(open);
      document.body.classList.toggle("contents-open", open);
      toggle.classList.toggle("active", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      if (!open) measureScrollbar();
    }

    if (!toggle.hasAttribute("aria-controls")) {
      if (!links.id) links.id = "site-nav-links";
      toggle.setAttribute("aria-controls", links.id);
    }
    toggle.setAttribute("aria-expanded", "false");
    if (!toggle.getAttribute("aria-label") || toggle.getAttribute("aria-label") === "Toggle navigation") {
      toggle.setAttribute("aria-label", "Open menu");
    }

    measureScrollbar();
    window.addEventListener("resize", function () {
      if (!links.classList.contains("active")) measureScrollbar();
    }, { passive: true });

    /* Capture before page scripts toggle .active — measure while scrollbar still exists */
    toggle.addEventListener("click", function () {
      if (!links.classList.contains("active")) {
        measureScrollbar();
        applyCompensation(true);
      }
    }, true);

    new MutationObserver(sync).observe(links, {
      attributes: true,
      attributeFilter: ["class"]
    });
    sync();
  });
})();
