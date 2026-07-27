/* Contents Thread — sync open state + aria with existing menu toggles */
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

    function sync() {
      var open = links.classList.contains("active");
      document.body.classList.toggle("contents-open", open);
      document.documentElement.classList.toggle("contents-open", open);
      toggle.classList.toggle("active", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    }

    if (!toggle.hasAttribute("aria-controls")) {
      if (!links.id) links.id = "site-nav-links";
      toggle.setAttribute("aria-controls", links.id);
    }
    toggle.setAttribute("aria-expanded", "false");
    if (!toggle.getAttribute("aria-label") || toggle.getAttribute("aria-label") === "Toggle navigation") {
      toggle.setAttribute("aria-label", "Open menu");
    }

    new MutationObserver(sync).observe(links, {
      attributes: true,
      attributeFilter: ["class"]
    });
    sync();
  });
})();
