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
     [data-library-map]        -- Library page: the Map (Layer 1)
     [data-library-archive]    -- Library page: Everything (Layer 3)
     [data-topic-page]         -- topic page (anchor + framing +
                                  inquiries + article listings)
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
  function renderTopicPage(root, topic, articles, library, options) {
    if (!root) return;
    var includeDrafts = options && options.includeDrafts;

    /* Anchor + title + framing. */
    var anchor = root.querySelector('[data-topic-anchor]');
    if (anchor) {
      var insightsHref = resolveSiteUrl('insights.html');
      anchor.innerHTML = 'in <a href="' + escapeHTML(insightsHref) + '">Insights</a>';
    }
    var titleEl = root.querySelector('[data-topic-title]');
    if (titleEl) titleEl.textContent = topic.name;

    var framingEl = root.querySelector('[data-topic-framing]');
    if (framingEl) framingEl.textContent = topic.framing || '';

    if (topic.name && document.title.indexOf('|') !== -1) {
      document.title = topic.name + ' | Rajiv Vakani';
    }

    /* Inquiries  --  one per cluster with articles. Empty clusters
       are omitted on the public topic page. */
    var threadsHost = root.querySelector('[data-topic-threads]');
    if (threadsHost) {
      var clusters = topic.clusters || [];
      threadsHost.innerHTML = clusters.map(function (cluster) {
        var pieces = getArticlesInCluster(articles, topic.id, cluster.id, { includeDrafts: includeDrafts });
        if (pieces.length === 0) {
          return '';
        }
        var listHtml = '<ul class="thread__list">' + pieces.map(function (a) {
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


  /* E5. Library page  --  Layer 1: The Map.

     Six topic rows. Each row is the topic name (linked) and an
     article count. The count uses drafts when drafts are visible
     so it matches what shows up in Everything below. Empty topics
     read as "opening" -- still listed (the territory exists). */
  function renderLibraryMap(container, library, articles, options) {
    var includeDrafts = options && options.includeDrafts;
    if (!container || !library || !library.topics) {
      setState(container, 'empty', 'No topics yet.');
      return;
    }
    container.removeAttribute('data-render-state');
    container.innerHTML = library.topics.map(function (topic) {
      var visible = includeDrafts
        ? countArticlesInTopic(articles, topic.id, { includeDrafts: true })
        : countArticlesInTopic(articles, topic.id, { includeDrafts: false });
      var url = resolveSiteUrl(topic.url);
      var titleHtml = '<a href="' + escapeHTML(url) + '">' + escapeHTML(topic.name) + '</a>';
      var countText;
      if (visible === 0) countText = 'opening';
      else if (visible === 1) countText = '1 piece';
      else countText = visible + ' pieces';
      return [
        '<li class="library-map__item">',
          '<h3 class="library-map__title">', titleHtml, '</h3>',
          '<span class="library-map__count">', escapeHTML(countText), '</span>',
        '</li>'
      ].join('');
    }).join('');
  }

  /* E6. Library page  --  Layer 3: Everything.

     For each topic that has any articles, render the topic name
     (linked) and a flat list of article titles. Title only.
     Drafts get a small muted "Draft" tag inline. Articles are
     sorted by title alphabetically.

     Topics with zero articles are omitted entirely. The Map above
     already declares the full inventory; this section is for
     retrieval. Empty topics have nothing to retrieve. */
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
        return [
          '<li class="library-archive__item">',
            '<a href="', escapeHTML(href), '">', escapeHTML(a.title), '</a>',
            draftTag,
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
    var attentionEl      = document.querySelector('[data-library-attention]');
    var homeAttentionEl  = document.querySelector('[data-home-attention]');
    var topicsEl         = document.querySelector('[data-library-topics]');
    var homeTopicsEl     = document.querySelector('[data-home-topics]');
    var libraryMapEl     = document.querySelector('[data-library-map]');
    var libraryArchiveEl = document.querySelector('[data-library-archive]');
    var topicBody        = document.body && document.body.hasAttribute('data-topic-page')
      ? document.body
      : null;
    var articleSlug      = document.body && document.body.getAttribute('data-article-slug');
    var nextEl           = document.querySelector('[data-post-next]');

    var anyTarget = attentionEl || homeAttentionEl || topicsEl || homeTopicsEl || libraryMapEl || libraryArchiveEl ||
                    topicBody || (articleSlug && nextEl);
    if (!anyTarget) return;

    var data = getData();
    if (!data.library) {
      var msg = 'Library data could not load. Make sure insights/data.js is included before insights/library.js.';
      console.error('[Library]', msg);
      [attentionEl, topicsEl, libraryMapEl, libraryArchiveEl, nextEl].forEach(function (el) {
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
    if (libraryMapEl)     renderLibraryMap(libraryMapEl, library, articles, { includeDrafts: includeDrafts });
    if (libraryArchiveEl) renderLibraryArchive(libraryArchiveEl, library, articles, { includeDrafts: includeDrafts });

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
    renderLibraryMap:        renderLibraryMap,
    renderLibraryArchive:    renderLibraryArchive,
    formatDate:              formatDate,
    formatArticleDate:       formatArticleDate,
    articleListingDate:      articleListingDate,
    resolveSiteUrl:          resolveSiteUrl
  };
})();
