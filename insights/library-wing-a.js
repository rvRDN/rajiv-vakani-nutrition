/* ============================================================
   Knowledge Library  --  renderers + small data API
   ============================================================

   This file is the rendering layer for the Knowledge Library
   system. The data lives in insights/data.js as `window.RVData`
   (one canonical source). This file reads from it synchronously.

   Pages get auto-rendered by detecting these data-* attributes:

     [data-library-attention]  -- unused on Insights; Home uses [data-home-attention]
     [data-library-topics]     -- Knowledge Library topic doorways
                                  (Insights)
     [data-library-archive]    -- Library page: list archive (legacy)
     [data-library-mosaic]     -- Library page: packed mosaic shelf
     [data-library-subjects]   -- Library page: hero subject jump list
     [data-topic-page]         -- topic page (anchor + framing +
                                  inquiries + article listings)
                                  Wing redesign: body.topic-wing also
                                  fills [data-topic-line], [data-topic-map],
                                  [data-topic-start]
     [data-post-next]          -- article page Next block

   To add a topic:
     Edit `window.RVData.library.topics` in insights/data.js.
     Then create a topic-page shell at insights/topics/<id>.html
     (copy any existing topic page; set body[data-topic-page] to
     the new topic id).

   To add an article:
     Add an entry to `window.RVData.articles` in insights/data.js
     and create the article HTML by copying insights/_template.html.
     While drafting: keep date as the intended publication date; drafts
     auto-show the current month in listings. On publish: status published,
     keep date.
     The topic page picks it up automatically.

   Load order:
     <script defer src=".../insights/data.js?v=..."></script>
     <script defer src=".../insights/library.js?v=..."></script>

   `defer` preserves load order: data.js runs first, defines
   `window.RVData`, then library.js runs and reads it.
   ============================================================ */

(function () {
  'use strict';

  /* ---------- A. Tiny utilities ---------- */

  function escapeHTML(value) {
    var d = document.createElement('div');
    d.textContent = value == null ? '' : String(value);
    return d.innerHTML;
  }

  function formatDate(iso) {
    if (!iso) return '';
    var parts = String(iso).split('-');
    if (parts.length < 3) return iso;
    var months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December'];
    var m = parseInt(parts[1], 10) - 1;
    if (m < 0 || m > 11) return iso;
    return months[m] + ' ' + parseInt(parts[2], 10) + ', ' + parts[0];
  }

  function formatMonthYear(iso) {
    if (!iso) return '';
    var parts = String(iso).split('-');
    if (parts.length < 2) return iso;
    var months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December'];
    var m = parseInt(parts[1], 10) - 1;
    if (m < 0 || m > 11) return iso;
    return months[m] + ' ' + parts[0];
  }

  /* Drafts roll to the first of the current month for display and sort. */
  function draftMonthAnchor() {
    var now = new Date();
    var m = now.getMonth() + 1;
    var ms = m < 10 ? '0' + m : String(m);
    return now.getFullYear() + '-' + ms + '-01';
  }

  /* Publication date when live; current month anchor while draft. */
  function articleListingDate(article) {
    if (!article) return '';
    if (article.status === 'draft') return draftMonthAnchor();
    return article.date || '';
  }

  function formatArticleDate(article) {
    if (!article) return '';
    if (article.status === 'draft') return formatMonthYear(articleListingDate(article));
    return formatDate(article.date || '');
  }

  function renderPostMeta(article) {
    if (!article) return;
    var meta = document.querySelector('.post-meta');
    if (!meta) return;
    var spans = meta.querySelectorAll('span');
    if (spans.length < 2) return;
    spans[1].textContent = formatArticleDate(article);
  }

  /* Open a collapsed source list before an inline citation jumps to it.
     This also handles direct links such as article.html#src-4. */
  function revealSourceTarget(hash, shouldScroll) {
    if (!hash || hash.charAt(0) !== '#') return;

    var id;
    try {
      id = decodeURIComponent(hash.slice(1));
    } catch (error) {
      id = hash.slice(1);
    }
    if (!id) return;

    var target = document.getElementById(id);
    if (!target) return;

    var disclosure = target.closest('details.post-sources__disclosure');
    if (!disclosure) return;

    disclosure.open = true;
    if (shouldScroll) {
      window.requestAnimationFrame(function () {
        target.scrollIntoView({ block: 'start' });
      });
    }
  }

  function setupSourceDisclosures() {
    document.addEventListener('click', function (event) {
      var clicked = event.target;
      if (!clicked || typeof clicked.closest !== 'function') return;
      var link = clicked.closest('a[href^="#"]');
      if (!link) return;
      revealSourceTarget(link.getAttribute('href'), false);
    });

    window.addEventListener('hashchange', function () {
      revealSourceTarget(window.location.hash, true);
    });

    revealSourceTarget(window.location.hash, true);
  }

  function setState(el, state, message) {
    if (!el) return;
    el.setAttribute('data-render-state', state);
    if (message) el.textContent = message;
  }

  /* Resolve a site-relative URL (as stored in data.js) into a path
     that works from whatever depth the current page lives at. */
  function rootPrefix() {
    var path = location.pathname || '';
    if (path.indexOf('/insights/topics/') !== -1) return '../../';
    if (path.indexOf('/insights/') !== -1) return '../';
    return '';
  }
  function resolveSiteUrl(siteRelative) {
    if (!siteRelative) return '#';
    return rootPrefix() + siteRelative;
  }


  /* ---------- B. Data access ---------- */

  /* Sync read from the single source defined in insights/data.js.
     `defer` script ordering guarantees RVData exists by the time
     this runs. */
  function getData() {
    var data = (typeof window !== 'undefined' && window.RVData) || null;
    if (!data || !data.library) {
      return { library: null, articles: [] };
    }
    return {
      library: data.library,
      articles: data.articles || []
    };
  }

  /* Backward-compat shim. Old call sites (if any) used the async
     loadAll(). Resolving synchronously preserves that surface. */
  function loadAll() {
    return Promise.resolve(getData());
  }


  /* ---------- C. Small data API ---------- */

  function getTopic(library, topicId) {
    if (!library || !library.topics) return null;
    for (var i = 0; i < library.topics.length; i++) {
      if (library.topics[i].id === topicId) return library.topics[i];
    }
    return null;
  }

  function getArticlesInTopic(articles, topicId, options) {
    var includeDrafts = options && options.includeDrafts;
    return (articles || []).filter(function (a) {
      if (!a || a.topic !== topicId) return false;
      if (!includeDrafts && a.status !== 'published') return false;
      return true;
    });
  }

  function getArticlesInCluster(articles, topicId, clusterId, options) {
    return getArticlesInTopic(articles, topicId, options).filter(function (a) {
      return a.cluster === clusterId;
    });
  }

  function getArticleBySlug(articles, slug) {
    if (!articles) return null;
    for (var i = 0; i < articles.length; i++) {
      if (articles[i].slug === slug) return articles[i];
    }
    return null;
  }

  function countArticlesInTopic(articles, topicId, options) {
    return getArticlesInTopic(articles, topicId, options).length;
  }


  /* ---------- D. Recommendation engine ---------- */

  /* Build the Next-recommendations list for an article.

     Priority fill, in this order, up to maxResults total:
       1. Pinned slugs from article.next (in author order)
       2. Same-cluster siblings (auto)
       3. Same-topic, different cluster (auto)
       4. Cross-topic (auto)

     Within each automatic tier, published articles come before
     drafts; then newer dates before older. The pinned tier keeps
     author-specified order untouched. The current article is
     excluded; duplicates are de-duplicated.

     Authoring patterns this supports:
       next: []                 -> 3 fully automatic
       next: ["a"]              -> 1 pinned + 2 automatic
       next: ["a", "b", "c"]    -> 3 manual (legacy form)
  */
  function getNextRecommendations(article, articles, options) {
    if (!article) return [];
    options = options || {};
    var maxResults = typeof options.maxResults === 'number' ? options.maxResults : 3;
    var includeDrafts = options.includeDrafts !== false;

    var picks = [];
    var seen = {};
    seen[article.slug] = true;

    function tryAdd(candidate) {
      if (!candidate) return;
      if (picks.length >= maxResults) return;
      if (seen[candidate.slug]) return;
      if (!includeDrafts && candidate.status !== 'published') return;
      picks.push(candidate);
      seen[candidate.slug] = true;
    }

    /* Tier 1: pinned. */
    (article.next || []).forEach(function (slug) {
      tryAdd(getArticleBySlug(articles, slug));
    });

    if (picks.length >= maxResults) return picks;

    function rank(a, b) {
      var aPub = a.status === 'published' ? 0 : 1;
      var bPub = b.status === 'published' ? 0 : 1;
      if (aPub !== bPub) return aPub - bPub;
      var ad = articleListingDate(a);
      var bd = articleListingDate(b);
      if (ad === bd) return 0;
      return ad < bd ? 1 : -1;
    }

    /* Tier 2: same cluster, same topic. */
    (articles || [])
      .filter(function (a) { return a.topic === article.topic && a.cluster === article.cluster; })
      .slice()
      .sort(rank)
      .forEach(tryAdd);
    if (picks.length >= maxResults) return picks;

    /* Tier 3: same topic, different cluster. */
    (articles || [])
      .filter(function (a) { return a.topic === article.topic && a.cluster !== article.cluster; })
      .slice()
      .sort(rank)
      .forEach(tryAdd);
    if (picks.length >= maxResults) return picks;

    /* Tier 4: cross-topic. */
    (articles || [])
      .filter(function (a) { return a.topic !== article.topic; })
      .slice()
      .sort(rank)
      .forEach(tryAdd);

    return picks;
  }


  /* ---------- E. Renderers ---------- */

  /* E1. Library landing (Insights)  --  Current Attention list. */
  function renderAttention(container, library) {
    if (!container || !library || !library.currentAttention) {
      setState(container, 'empty', 'Nothing currently open.');
      return;
    }
    var items = library.currentAttention;
    if (!items.length) {
      setState(container, 'empty', 'Nothing currently open.');
      return;
    }
    container.removeAttribute('data-render-state');
    container.innerHTML = items.map(function (item) {
      return [
        '<li>',
          '<span class="attention__kind">', escapeHTML(item.kind || ''), '.</span>',
          '<span class="attention__what">', escapeHTML(item.what || ''), '</span>',
        '</li>'
      ].join('');
    }).join('');
  }

  /* E1b. Homepage composition beat  --  Current Attention list. */
  function renderHomeAttention(container, library) {
    if (!container || !library || !library.currentAttention) return;
    var items = library.currentAttention;
    if (!items.length) return;
    container.innerHTML = items.map(function (item) {
      var kind = item.kind || '';
      if (kind && kind.charAt(kind.length - 1) !== '.') kind += '.';
      return [
        '<li>',
          '<span class="beat__kind">', escapeHTML(kind), '</span>',
          '<span class="beat__what">', escapeHTML(item.what || ''), '</span>',
        '</li>'
      ].join('');
    }).join('');
  }

  /* E1c. Homepage composition beat  --  topic doorway links. */
  function renderHomeTopics(container, library) {
    if (!container || !library || !library.topics) return;
    var topicsHtml = library.topics.map(function (topic) {
      var url = resolveSiteUrl(topic.url);
      var name = topic.name || '';
      if (name && name.charAt(name.length - 1) !== '.') name += '.';
      return [
        '<li>',
          '<a href="', escapeHTML(url), '">', escapeHTML(name), '</a>',
          ' ', escapeHTML(topic.shortDescription || ''),
        '</li>'
      ].join('');
    }).join('');
    var profilesHtml = [
      '<li>',
        '<a href="', escapeHTML(resolveSiteUrl('therapy-profiles/index.html')), '">Traditional therapy profiles.</a>',
        ' When one name refers to a plant, a formulation, and a product at once,',
        ' each entry separates them again. Orientation, not recommendation.',
      '</li>'
    ].join('');
    container.innerHTML = topicsHtml + profilesHtml;
  }

  /* E2. Library landing (Insights)  --  Topic doorways.

     The topic name always links. Even if a topic has no articles
     yet, its topic page exists and is reachable. The doorway is
     not a dead-end.

     Count semantics: show published count; when drafts exist,
     append "N in progress" so drafts visibly participate in the
     architecture rather than being silently absent from the
     count visitors see on the way in. */
  function renderTopics(container, library, articles, options) {
    var includeDrafts = options && options.includeDrafts;
    if (!container || !library || !library.topics) {
      setState(container, 'empty', 'No topics yet.');
      return;
    }
    container.removeAttribute('data-render-state');
    container.innerHTML = library.topics.map(function (topic) {
      var published = countArticlesInTopic(articles, topic.id, { includeDrafts: false });
      var total = countArticlesInTopic(articles, topic.id, { includeDrafts: true });
      var drafts = includeDrafts ? (total - published) : 0;
      var url = resolveSiteUrl(topic.url);
      var titleHtml = '<a href="' + escapeHTML(url) + '">' + escapeHTML(topic.name) + '.</a>';

      var meta;
      if (published === 0 && drafts === 0) {
        meta = 'opening';
      } else if (published === 0) {
        meta = drafts === 1 ? '1 in progress' : drafts + ' in progress';
      } else if (drafts === 0) {
        meta = published === 1 ? '1 piece' : published + ' pieces';
      } else {
        var pieces = published === 1 ? '1 piece' : published + ' pieces';
        var inProg = drafts === 1 ? '1 in progress' : drafts + ' in progress';
        meta = pieces + ' \u00B7 ' + inProg;
      }

      return [
        '<li>',
          '<h3 class="topics__title">', titleHtml, '</h3>',
          '<p class="topics__desc">', escapeHTML(topic.shortDescription || ''), '</p>',
          '<p class="topics__meta">', escapeHTML(meta), '</p>',
        '</li>'
      ].join('');
    }).join('');
  }

  /* E3. Topic page  --  anchor, title, framing, and inquiries
     (clusters with published articles only). */
  /* Split a topic name for the wing title. Prefer a natural phrase
     break so multi-word subjects don't orphan a single first word. */
  function formatWingTitleHtml(name, mockItalic) {
    var raw = String(name || '').trim();
    if (!raw) return '';

    var presets = {
      'Reading the evidence': ['Reading', 'the evidence'],
      'South Asian food and nutrition': ['South Asian food', 'and nutrition'],
      'Practical nutrition': ['Practical', 'nutrition'],
      'Food culture and behavior': ['Food culture', 'and behavior'],
      'Food, growing, and systems': ['Food, growing,', 'and systems'],
      'Health and the body': ['Health', 'and the body']
    };

    var pair = presets[raw];
    if (!pair) {
      var parts = raw.split(/\s+/);
      if (parts.length === 1) {
        return mockItalic
          ? escapeHTML(parts[0])
          : '<span class="wing-title__lead">' + escapeHTML(parts[0]) + '</span>';
      }
      if (parts.length === 2) {
        pair = [parts[0], parts[1]];
      } else {
        var andAt = parts.indexOf('and');
        if (andAt > 0) {
          pair = [parts.slice(0, andAt).join(' '), parts.slice(andAt).join(' ')];
        } else {
          var mid = Math.ceil(parts.length / 2);
          pair = [parts.slice(0, mid).join(' '), parts.slice(mid).join(' ')];
        }
      }
    }

    /* Mockup A uses Reading<i>the evidence</i> */
    if (mockItalic) {
      return escapeHTML(pair[0]) + '<i>' + escapeHTML(pair[1]) + '</i>';
    }

    return [
      '<span class="wing-title__lead">', escapeHTML(pair[0]), '</span>',
      '<span class="wing-title__rest">', escapeHTML(pair[1]), '</span>'
    ].join('');
  }

  function padInquiryIndex(n) {
    return n < 10 ? '0' + String(n) : String(n);
  }

  function renderTopicPage(root, topic, articles, library, options) {
    if (!root) return;
    var includeDrafts = options && options.includeDrafts;
    var isWing = root.classList.contains('topic-wing');
    var isHeroA = !!root.querySelector('header.hero-a');

    /* Anchor + title + framing. */
    var anchor = root.querySelector('[data-topic-anchor]');
    if (anchor) {
      var insightsHref = resolveSiteUrl('insights.html');
      if (isHeroA) {
        anchor.innerHTML = 'in <b><a href="' + escapeHTML(insightsHref) + '">Insights</a></b>';
      } else {
        anchor.innerHTML = 'in <a href="' + escapeHTML(insightsHref) + '">Insights</a>';
      }
    }
    var titleEl = root.querySelector('[data-topic-title]');
    if (titleEl) {
      if (isHeroA) titleEl.innerHTML = formatWingTitleHtml(topic.name, true);
      else if (isWing) titleEl.innerHTML = formatWingTitleHtml(topic.name, false);
      else titleEl.textContent = topic.name;
    }

    var framingEl = root.querySelector('[data-topic-framing]');
    if (framingEl) {
      var framing = topic.framing || '';
      if (isHeroA && framing) {
        /* Full framing, mockup prose style — do not trim. */
        framingEl.innerHTML = '<p class="prose">' + escapeHTML(framing) + '</p>';
      } else if (isWing && framing) {
        var beats = framing.split(/(?<=\.)\s+/).filter(function (s) { return s && s.trim(); });
        if (beats.length > 1) {
          framingEl.innerHTML = beats.map(function (s) {
            return '<p>' + escapeHTML(s.trim()) + '</p>';
          }).join('');
        } else {
          framingEl.innerHTML = '<p>' + escapeHTML(framing) + '</p>';
        }
      } else {
        framingEl.textContent = framing;
      }
    }

    var lineEl = root.querySelector('[data-topic-line]');
    if (lineEl) lineEl.textContent = topic.shortDescription || '';

    if (topic.name && document.title.indexOf('|') !== -1) {
      document.title = topic.name + ' | Rajiv Vakani';
    }

    /* Build live clusters once (empty omitted). */
    var liveClusters = [];
    (topic.clusters || []).forEach(function (cluster) {
      var pieces = getArticlesInCluster(articles, topic.id, cluster.id, { includeDrafts: includeDrafts });
      if (pieces.length) liveClusters.push({ cluster: cluster, pieces: pieces });
    });

    var allPieces = getArticlesInTopic(articles, topic.id, { includeDrafts: includeDrafts });
    var totalPieces = allPieces.length;

    /* Hero rain — same scatter as mockups/topic-hero #a (around the well). */
    var rainHost = root.querySelector('[data-topic-rain]');
    if (rainHost) {
      if (!allPieces.length) {
        rainHost.innerHTML = '';
      } else {
        var rainPool = allPieces.slice();
        while (rainPool.length < 20) {
          rainPool = rainPool.concat(allPieces);
        }
        rainPool = rainPool.slice(0, 20);
        rainHost.innerHTML = rainPool.map(function (a) {
          return '<span>' + escapeHTML(a.title) + '</span>';
        }).join('');
        requestAnimationFrame(function () {
          positionWingRain(rainHost);
        });
      }
    }

    var metaEl = root.querySelector('[data-topic-meta]');
    if (metaEl) {
      if (!totalPieces) {
        metaEl.textContent = '';
      } else {
        var invLabel = totalPieces === 1 ? '1 investigation' : totalPieces + ' investigations';
        var inqLabel = liveClusters.length === 1 ? '1 inquiry' : liveClusters.length + ' inquiries';
        metaEl.textContent = invLabel + ' · ' + inqLabel;
      }
    }

    var heroMap = root.querySelector('[data-topic-hero-map]');
    if (heroMap) heroMap.innerHTML = '';

    var inquiriesLabel = root.querySelector('[data-topic-inquiries-label]');
    if (inquiriesLabel) {
      if (liveClusters.length === 1) inquiriesLabel.textContent = 'Inquiry';
      else if (liveClusters.length) inquiriesLabel.textContent = liveClusters.length + ' inquiries';
      else inquiriesLabel.textContent = 'Inquiries';
    }

    /* Start-here and map hosts unused. */
    var startHost = root.querySelector('[data-topic-start]');
    if (startHost) {
      startHost.hidden = true;
      startHost.innerHTML = '';
    }
    var mapHost = root.querySelector('[data-topic-map]');
    if (mapHost) mapHost.innerHTML = '';

    /* Inquiries. */
    var threadsHost = root.querySelector('[data-topic-threads]');
    if (threadsHost) {
      if (!liveClusters.length) {
        setState(threadsHost, 'empty', 'No investigations in this subject yet.');
        return;
      }
      threadsHost.removeAttribute('data-render-state');

      if (isWing) {
        threadsHost.innerHTML = liveClusters.map(function (row, i) {
          var cluster = row.cluster;
          var ribbon = buildWingRibbon(row.pieces);
          return [
            '<article class="wing-inquiry" id="inquiry-', escapeHTML(cluster.id), '">',
              '<p class="wing-inquiry__num" aria-hidden="true">', padInquiryIndex(i + 1), '</p>',
              '<div class="wing-inquiry__body">',
                '<h2 class="wing-inquiry__name">', escapeHTML(cluster.name), '</h2>',
                '<p class="wing-inquiry__framing">', escapeHTML(cluster.framing || ''), '</p>',
                ribbon,
              '</div>',
            '</article>'
          ].join('');
        }).join('');

        if (typeof IntersectionObserver !== 'undefined') {
          var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
              if (entry.isIntersecting) {
                entry.target.classList.add('is-in');
                io.unobserve(entry.target);
              }
            });
          }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
          Array.prototype.forEach.call(
            threadsHost.querySelectorAll('.wing-inquiry'),
            function (el) { io.observe(el); }
          );
        } else {
          Array.prototype.forEach.call(
            threadsHost.querySelectorAll('.wing-inquiry'),
            function (el) { el.classList.add('is-in'); }
          );
        }
      } else {
        threadsHost.innerHTML = liveClusters.map(function (row) {
          var cluster = row.cluster;
          var listHtml = '<ul class="thread__list">' + row.pieces.map(function (a) {
            var href = resolveSiteUrl(a.url);
            return [
              '<li>',
                '<a class="thread__article" href="', escapeHTML(href), '">',
                  '<p class="thread__article-title">', escapeHTML(a.title), '</p>',
                  '<p class="thread__article-lede">', escapeHTML(a.lede || ''), '</p>',
                '</a>',
              '</li>'
            ].join('');
          }).join('') + '</ul>';
          return [
            '<article class="thread">',
              '<div class="thread__opening">',
                '<h3 class="thread__title">', escapeHTML(cluster.name), '.</h3>',
                '<p class="thread__framing">', escapeHTML(cluster.framing || ''), '</p>',
              '</div>',
              listHtml,
            '</article>'
          ].join('');
        }).join('');
      }
    }
  }

  /* Title ribbon — loop so thin inquiries still feel full. */
  function buildWingRibbon(pieces) {
    if (!pieces || !pieces.length) return '';
    var loop = pieces.slice();
    while (loop.length < 8) {
      loop = loop.concat(pieces);
    }
    function half(list) {
      return list.map(function (a) {
        return '<a href="' + escapeHTML(resolveSiteUrl(a.url)) + '">' + escapeHTML(a.title) + '</a>';
      }).join('');
    }
    return [
      '<div class="wing-ribbon" aria-label="Investigations in this inquiry">',
        '<div class="wing-ribbon__track">',
          half(loop),
          half(loop),
        '</div>',
      '</div>'
    ].join('');
  }

  function positionWingRain(host) {
    if (!host) return;
    var spans = host.querySelectorAll('span');
    if (!spans.length) return;
    /* Exact mockup A scatter: mostly right + sparse left edge, around the well. */
    Array.prototype.forEach.call(spans, function (el, i) {
      var left = (i % 5 === 0)
        ? (6 + (i % 3) * 4)
        : (48 + ((i * 19) % 48));
      var top = 6 + ((i * 31) % 82);
      el.style.left = left + '%';
      el.style.top = top + '%';
      el.style.transform = 'rotate(' + (((i * 17) % 21) - 10) + 'deg)';
      el.style.fontSize = (1.05 + (i % 4) * 0.2) + 'rem';
      el.style.opacity = '';
    });
  }

  /* E4. Article page  --  the "Next" block. Uses the recommendation
     engine to fill up to 3 slots from pinned + auto. */
  function renderArticleNext(container, slug, articles, options) {
    if (!container) return;
    var article = getArticleBySlug(articles, slug);
    if (!article) {
      container.hidden = true;
      return;
    }
    var includeDrafts = options && options.includeDrafts !== false;
    var picks = getNextRecommendations(article, articles, {
      maxResults: 3,
      includeDrafts: includeDrafts
    });
    if (!picks.length) {
      container.hidden = true;
      return;
    }
    container.removeAttribute('data-render-state');
    container.innerHTML = '<p class="post-next__label">Next.</p>' +
      '<ul class="post-next__list">' + picks.map(function (a) {
        var href = resolveSiteUrl(a.url);
        var draftFlag = a.status === 'draft' ? '<span>Draft</span>' : '';
        return [
          '<li>',
            '<a href="', escapeHTML(href), '">',
              '<p class="post-next__title">', escapeHTML(a.title), '</p>',
              '<p class="post-next__why">', escapeHTML(a.lede || ''), '</p>',
              '<p class="post-next__meta">',
                '<span>', escapeHTML(a.type || ''), '</span>',
                '<span>', escapeHTML(formatArticleDate(a)), '</span>',
                draftFlag,
              '</p>',
            '</a>',
          '</li>'
        ].join('');
      }).join('') + '</ul>';
  }


  /* E5b. Library shelf mosaic (packed grid).

     Group heading cells mixed into the same grid as article cells.
     Default: published only (Library page uses data-hide-drafts).
     Article order follows data.js within each topic. Empty topics
     omitted so the mosaic reflows. */
  function renderLibraryMosaic(container, library, articles, options) {
    var includeDrafts = options && options.includeDrafts;
    if (!container || !library || !library.topics) {
      setState(container, 'empty', 'No topics yet.');
      return;
    }
    container.removeAttribute('data-render-state');

    var html = '';
    library.topics.forEach(function (topic) {
      var pieces = getArticlesInTopic(articles, topic.id, { includeDrafts: includeDrafts });
      if (!pieces.length) return;
      var topicUrl = resolveSiteUrl(topic.url);
      var countLabel = pieces.length === 1 ? '1 piece' : pieces.length + ' pieces';
      var groupId = 'g-' + topic.id;
      html += [
        '<div class="lib-cell lib-cell--group" id="', escapeHTML(groupId), '">',
          '<p class="lib-cell__kicker">Subject</p>',
          '<p class="lib-cell__title"><a href="', escapeHTML(topicUrl), '">', escapeHTML(topic.name), '</a></p>',
          '<p class="lib-cell__meta">', escapeHTML(countLabel), '</p>',
        '</div>'
      ].join('');
      pieces.forEach(function (a) {
        var href = resolveSiteUrl(a.url);
        var statusLabel = a.status === 'draft' ? 'Draft' : 'Published';
        var lede = a.lede
          ? '<p class="lib-cell__lede">' + escapeHTML(a.lede) + '</p>'
          : '';
        html += [
          '<a class="lib-cell lib-cell--article" href="', escapeHTML(href), '">',
            '<p class="lib-cell__meta">', escapeHTML(statusLabel), '</p>',
            '<p class="lib-cell__title">', escapeHTML(a.title), '</p>',
            lede,
          '</a>'
        ].join('');
      });
    });

    if (!html) {
      setState(container, 'empty', 'No published investigations yet.');
      return;
    }
    container.innerHTML = html;
  }

  /* E5c. Library hero subject jump list (published counts). */
  function renderLibrarySubjects(container, library, articles, options) {
    var includeDrafts = options && options.includeDrafts;
    if (!container || !library || !library.topics) {
      setState(container, 'empty', '');
      return;
    }
    container.removeAttribute('data-render-state');
    var items = library.topics.map(function (topic) {
      var n = countArticlesInTopic(articles, topic.id, { includeDrafts: includeDrafts });
      if (!n) return '';
      return [
        '<li><a href="#g-', escapeHTML(topic.id), '">',
          '<span></span>',
          escapeHTML(topic.name),
          '<span class="lib-map__n">', String(n), '</span>',
        '</a></li>'
      ].join('');
    }).join('');
    if (!items) {
      setState(container, 'empty', 'No subjects yet.');
      return;
    }
    container.innerHTML = items;
  }

  /* E5. Library shelf  --  Investigations (list archive; legacy).

     For each topic that has any articles, render the topic name
     (linked) and a list of articles with title + lede so readers
     know what they're opening. Drafts get a small muted "Draft"
     tag. Articles are sorted by title alphabetically.

     Topics with zero articles are omitted entirely. Empty topics
     have nothing to retrieve. */
  function renderLibraryArchive(container, library, articles, options) {
    var includeDrafts = options && options.includeDrafts;
    if (!container || !library || !library.topics) {
      setState(container, 'empty', 'No topics yet.');
      return;
    }
    container.removeAttribute('data-render-state');

    function alphaByTitle(a, b) {
      var at = (a.title || '').toLowerCase();
      var bt = (b.title || '').toLowerCase();
      if (at < bt) return -1;
      if (at > bt) return 1;
      return 0;
    }

    container.innerHTML = library.topics.map(function (topic) {
      var pieces = getArticlesInTopic(articles, topic.id, { includeDrafts: includeDrafts });
      if (!pieces.length) return '';
      pieces = pieces.slice().sort(alphaByTitle);
      var topicUrl = resolveSiteUrl(topic.url);
      var listHtml = '<ul class="library-archive__list">' + pieces.map(function (a) {
        var href = resolveSiteUrl(a.url);
        var draftTag = a.status === 'draft'
          ? '<span class="library-archive__draft">Draft</span>'
          : '';
        var lede = a.lede
          ? '<p class="library-archive__lede">' + escapeHTML(a.lede) + '</p>'
          : '';
        return [
          '<li class="library-archive__item">',
            '<p class="library-archive__title">',
              '<a href="', escapeHTML(href), '">', escapeHTML(a.title), '</a>',
              draftTag,
            '</p>',
            lede,
          '</li>'
        ].join('');
      }).join('') + '</ul>';
      return [
        '<section class="library-archive__group" aria-label="', escapeHTML(topic.name), '">',
          '<h2 class="library-archive__group-title">',
            '<a href="', escapeHTML(topicUrl), '">', escapeHTML(topic.name), '</a>',
          '</h2>',
          listHtml,
        '</section>'
      ].join('');
    }).join('');
  }


  /* ---------- F. Auto-render: detect page type and render ---------- */

  function autoRender() {
    setupSourceDisclosures();

    var attentionEl      = document.querySelector('[data-library-attention]');
    var homeAttentionEl  = document.querySelector('[data-home-attention]');
    var topicsEl         = document.querySelector('[data-library-topics]');
    var homeTopicsEl     = document.querySelector('[data-home-topics]');
    var libraryArchiveEl = document.querySelector('[data-library-archive]');
    var libraryMosaicEl  = document.querySelector('[data-library-mosaic]');
    var librarySubjectsEl = document.querySelector('[data-library-subjects]');
    var topicBody        = document.body && document.body.hasAttribute('data-topic-page')
      ? document.body
      : null;
    var articleSlug      = document.body && document.body.getAttribute('data-article-slug');
    var nextEl           = document.querySelector('[data-post-next]');

    var anyTarget = attentionEl || homeAttentionEl || topicsEl || homeTopicsEl || libraryArchiveEl ||
                    libraryMosaicEl || librarySubjectsEl ||
                    topicBody || (articleSlug && nextEl);
    if (!anyTarget) return;

    var data = getData();
    if (!data.library) {
      var msg = 'Library data could not load. Make sure insights/data.js is included before insights/library.js.';
      console.error('[Library]', msg);
      [attentionEl, topicsEl, libraryArchiveEl, libraryMosaicEl, librarySubjectsEl, nextEl].forEach(function (el) {
        if (el) setState(el, 'error', msg);
      });
      if (topicBody) {
        var threadsHost = topicBody.querySelector('[data-topic-threads]');
        if (threadsHost) setState(threadsHost, 'error', msg);
      }
      return;
    }

    var library = data.library;
    var articles = data.articles;

    /* Default: drafts visible so the visitor sees the real state of
       the body of work. Body[data-hide-drafts] flips to a
       "published only" view if ever needed (no UI for that yet). */
    var includeDrafts = !(document.body && document.body.hasAttribute('data-hide-drafts'));

    if (attentionEl)      renderAttention(attentionEl, library);
    if (homeAttentionEl)  renderHomeAttention(homeAttentionEl, library);
    if (topicsEl)         renderTopics(topicsEl, library, articles, { includeDrafts: includeDrafts });
    if (homeTopicsEl)     renderHomeTopics(homeTopicsEl, library);
    if (libraryArchiveEl) renderLibraryArchive(libraryArchiveEl, library, articles, { includeDrafts: includeDrafts });
    if (libraryMosaicEl)  renderLibraryMosaic(libraryMosaicEl, library, articles, { includeDrafts: includeDrafts });
    if (librarySubjectsEl) renderLibrarySubjects(librarySubjectsEl, library, articles, { includeDrafts: includeDrafts });

    if (topicBody) {
      var topicId = topicBody.getAttribute('data-topic-page');
      var topic = getTopic(library, topicId);
      if (!topic) {
        var titleEl = topicBody.querySelector('[data-topic-title]');
        if (titleEl) titleEl.textContent = 'Topic not found';
        var framingEl = topicBody.querySelector('[data-topic-framing]');
        if (framingEl) framingEl.textContent = 'The topic id "' + topicId + '" is not defined in data.js.';
      } else {
        renderTopicPage(topicBody, topic, articles, library, { includeDrafts: includeDrafts });
      }
    }

    if (articleSlug && nextEl) {
      renderArticleNext(nextEl, articleSlug, articles, { includeDrafts: includeDrafts });
    }

    if (articleSlug) {
      renderPostMeta(getArticleBySlug(articles, articleSlug));
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', autoRender);
  } else {
    autoRender();
  }

  /* Public API. */
  window.RVLibrary = {
    getData:                 getData,
    loadAll:                 loadAll,
    getTopic:                getTopic,
    getArticlesInTopic:      getArticlesInTopic,
    getArticlesInCluster:    getArticlesInCluster,
    getArticleBySlug:        getArticleBySlug,
    countArticlesInTopic:    countArticlesInTopic,
    getNextRecommendations:  getNextRecommendations,
    renderAttention:         renderAttention,
    renderTopics:            renderTopics,
    renderTopicPage:         renderTopicPage,
    renderArticleNext:       renderArticleNext,
    renderLibraryArchive:    renderLibraryArchive,
    renderLibraryMosaic:     renderLibraryMosaic,
    renderLibrarySubjects:   renderLibrarySubjects,
    formatDate:              formatDate,
    formatArticleDate:       formatArticleDate,
    articleListingDate:      articleListingDate,
    resolveSiteUrl:          resolveSiteUrl
  };
})();
