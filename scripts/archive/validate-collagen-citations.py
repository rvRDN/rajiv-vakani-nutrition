from pathlib import Path
import re

html = Path("insights/collagen-compared-to-what.html").read_text(encoding="utf-8")
assert html.count("<html") == 1
assert html.count("</html>") == 1
assert html.count('class="post-sources"') == 1
assert html.count('class="post-next"') == 1
refs = re.findall(r'href="#src-(\d+)"', html)
print("unique source refs cited:", len(set(refs)))
print("total superscript links:", len(refs))
print("uncited sources:", sorted(set(str(i) for i in range(1, 23)) - set(refs)))
