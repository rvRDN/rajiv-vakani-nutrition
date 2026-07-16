(function () {
  var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  document.querySelectorAll("a.et-invest[href]").forEach(function (link) {
    link.addEventListener("click", function (e) {
      if (prefersReduced || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      e.preventDefault();
      var href = link.getAttribute("href");
      link.classList.add("is-expanding");
      window.setTimeout(function () {
        window.location.href = href;
      }, 380);
    });
  });

  var sections = Array.prototype.slice.call(document.querySelectorAll(".et-sec[id]"));
  var links = Array.prototype.slice.call(document.querySelectorAll(".et-spine a[href^='#']"));
  if (!sections.length || !links.length) return;

  var currentId = null;

  function setCurrent(id) {
    if (id === currentId) return;
    currentId = id;
    links.forEach(function (a) {
      var on = a.getAttribute("href") === "#" + id;
      if (on) {
        a.setAttribute("aria-current", "true");
        if (a.scrollIntoView && window.matchMedia("(max-width: 979px)").matches) {
          a.scrollIntoView({ inline: "center", block: "nearest", behavior: "smooth" });
        }
      } else {
        a.removeAttribute("aria-current");
      }
    });
  }

  // Prefer the section whose top is nearest the upper third of the viewport
  function syncFromScroll() {
    var marker = window.innerHeight * 0.28;
    var best = sections[0];
    var bestDist = Infinity;
    sections.forEach(function (sec) {
      var top = sec.getBoundingClientRect().top;
      var dist = Math.abs(top - marker);
      if (top <= marker + 40 && dist < bestDist) {
        bestDist = dist;
        best = sec;
      }
    });
    if (best) setCurrent(best.id);
  }

  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function () { syncFromScroll(); },
      { rootMargin: "-20% 0px -55% 0px", threshold: [0, 0.25, 0.5, 1] }
    );
    sections.forEach(function (sec) { io.observe(sec); });
  }

  var ticking = false;
  window.addEventListener(
    "scroll",
    function () {
      if (ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        syncFromScroll();
        ticking = false;
      });
    },
    { passive: true }
  );

  syncFromScroll();
})();
