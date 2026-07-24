/* Insights appearance: Light / Dark. Persists across Insights pages. */
(function () {
  var root = document.documentElement;
  var key = "insights-skin";
  var opts = document.querySelectorAll(".skin__opt");

  function apply(skin) {
    skin = skin === "dark" ? "dark" : "light";
    root.setAttribute("data-skin", skin);
    opts.forEach(function (btn) {
      var on = btn.getAttribute("data-skin") === skin;
      btn.classList.toggle("is-active", on);
      btn.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  try {
    var saved = localStorage.getItem(key);
    if (saved === "dark" || saved === "light") apply(saved);
    else apply(root.getAttribute("data-skin") || "light");
  } catch (e) {
    apply(root.getAttribute("data-skin") || "light");
  }

  opts.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var next = btn.getAttribute("data-skin");
      if (next === root.getAttribute("data-skin")) return;
      apply(next);
      try {
        localStorage.setItem(key, next);
      } catch (e) {}
    });
  });
})();
