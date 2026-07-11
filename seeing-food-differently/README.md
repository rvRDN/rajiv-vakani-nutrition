# Seeing Food Differently

**Status:** Soft launch / Early Edition. Live at its permanent URL. Not announced. Not in main site navigation. Pages stay `noindex` until a public launch decision.

## Purpose

A kitchen guide inside rajivvakani.com: five ways of seeing, one path.

## Pages

| # | File | Source draft |
|---|------|----------------|
| — | `index.html` | Guide entrance |
| 1 | `starting-state.html` | `drafts/starting-state-chapter-v0.2.md` |
| 2 | `flavor.html` | `drafts/flavor-chapter-v0.2.md` |
| 3 | `knife-cuts.html` | `drafts/knife-cuts-chapter-v0.1.md` |
| 4 | `heat.html` | `drafts/heat-chapter-v0.1.md` |
| 5 | `steering.html` | `drafts/steering-chapter-v0.2.md` |

**Sequence:** Starting State → Flavor → Knife Cuts → Heat → Steering

## Regenerate chapter HTML

After markdown draft edits:

```bash
python scripts/build-sfd-prototype.py
```

Styles: `guide-prototype.css` (guide-family register, not Insights essay mode).

**Evidence library seed:** `media/seeing-food-differently/`
