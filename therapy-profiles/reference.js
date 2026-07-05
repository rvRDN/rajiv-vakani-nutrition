(function () {
  'use strict';

  function normalize(str) {
    return (str || '').toLowerCase().replace(/[.\s]+/g, ' ').trim();
  }

  function scoreEntry(entry, query) {
    var q = normalize(query);
    if (!q) return 0;
    var title = normalize(entry.title);
    var aliases = (entry.aliases || []).map(normalize);
    if (title === q) return 100;
    if (title.indexOf(q) === 0) return 90;
    if (title.indexOf(q) !== -1) return 70;
    for (var i = 0; i < aliases.length; i++) {
      if (aliases[i] === q) return 85;
      if (aliases[i].indexOf(q) === 0) return 75;
      if (aliases[i].indexOf(q) !== -1) return 55;
    }
    return 0;
  }

  function initSearch() {
    var form = document.querySelector('[data-ref-search-form]');
    var input = document.querySelector('[data-ref-search-input]');
    var results = document.querySelector('[data-ref-search-results]');
    if (!form || !input || !results || !window.RVReference) return;

    var entries = window.RVReference.entries;

    function renderResults(matches) {
      results.innerHTML = '';
      matches.slice(0, 6).forEach(function (entry) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = entry.url;
        a.innerHTML =
          '<span class="ref-search-results__name">' + entry.title + '</span>' +
          '<span class="ref-search-results__meta">' + entry.typeLabel + '</span>';
        li.appendChild(a);
        results.appendChild(li);
      });
    }

    function findMatches(query) {
      return entries
        .map(function (entry) {
          return { entry: entry, score: scoreEntry(entry, query) };
        })
        .filter(function (item) {
          return item.score > 0;
        })
        .sort(function (a, b) {
          return b.score - a.score;
        })
        .map(function (item) {
          return item.entry;
        });
    }

    input.addEventListener('input', function () {
      var matches = findMatches(input.value);
      renderResults(matches);
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var matches = findMatches(input.value);
      if (matches.length) {
        window.location.href = matches[0].url;
      }
    });
  }

  function initNav() {
    var menuToggle = document.querySelector('.menu-toggle');
    var navLinks = document.querySelector('.nav-links');
    var overlay = document.querySelector('.mobile-menu-overlay');
    if (!menuToggle || !navLinks) return;

    menuToggle.addEventListener('click', function () {
      navLinks.classList.toggle('active');
      menuToggle.classList.toggle('active');
      if (overlay) overlay.classList.toggle('active');
      document.body.classList.toggle('menu-open');
    });

    if (overlay) {
      overlay.addEventListener('click', function () {
        navLinks.classList.remove('active');
        menuToggle.classList.remove('active');
        overlay.classList.remove('active');
        document.body.classList.remove('menu-open');
      });
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    initSearch();
    initNav();
  });
})();
