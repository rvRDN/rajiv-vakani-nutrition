(function () {
  'use strict';

  var targets = document.querySelectorAll('.guide-lens-wrap, .guide-reveal');
  if (!targets.length) return;

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function show(el) {
    el.classList.add('is-visible');
  }

  if (reduced) {
    targets.forEach(show);
    return;
  }

  if (!('IntersectionObserver' in window)) {
    targets.forEach(show);
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          show(entry.target);
          observer.unobserve(entry.target);
        }
      });
    },
    { root: null, rootMargin: '0px 0px -6% 0px', threshold: 0.1 }
  );

  targets.forEach(function (el) {
    observer.observe(el);
  });
})();
