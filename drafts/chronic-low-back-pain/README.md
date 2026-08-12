# Chronic Low Back Pain Evidence

**Status:** Step 0 owner-approved · Phase 0 library **frozen** (17 sources) · 12-object index **accepted** · Phase 1–2 **frozen** · object freeze **complete** · Phase 3 landscape **approved and frozen** · Phase 4 charter/outline **frozen** · public copy **frozen** · accent color **locked** (C) · hub + 12 topic HTML **live** (2026-08-11)  
**Campaign brief:** [`chronic-low-back-pain-campaign-brief-v0.1.md`](chronic-low-back-pain-campaign-brief-v0.1.md) (owner-approved August 11, 2026)  
**Methodology:** [`../adhd/condition-evidence-methodology-v1.0.md`](../adhd/condition-evidence-methodology-v1.0.md) adopted as-is (Pain batch)  
**Product philosophy:** [`../../evidence/evidence-product-charter.md`](../../evidence/evidence-product-charter.md)  
**Freeze register:** [`freeze-register-v1.0.md`](freeze-register-v1.0.md) (twelve objects frozen; Phase 3–4 charter frozen; public copy frozen; HTML frozen)

This folder holds two layers:

1. A permanent, versioned scientific reference collection.  
2. A claim-calibration synthesis layer (objects → freeze register → Phase 3 landscape).

The goal is to understand chronic low back pain as an **intervention landscape**, not reproduce a source library. Research begins with the broad clinical population appropriate to CLBP. Phenotype rails, object boundaries, and reader architecture are findings, not scaffold assumptions. Education, remaining active, exercise and rehabilitation, psychological therapies, medicines, injections, surgery, manual therapies, acupuncture, devices, supplements, and popular home remedies are all in scope for investigation; seats are earned by evidence.

---

## Files

### Campaign and library layer

| File | Role | Status |
|---|---|---|
| [`chronic-low-back-pain-campaign-brief-v0.1.md`](chronic-low-back-pain-campaign-brief-v0.1.md) | Step 0 decision problem and research object | Owner-approved |
| [`chronic-low-back-pain-evidence-library-v0.1.md`](chronic-low-back-pain-evidence-library-v0.1.md) | Canonical membership, roles, rationale, controversies | **Frozen v0.1 · 17 sources** |
| [`citation-log-v0.1.md`](citation-log-v0.1.md) | Verified citations and primary identifiers | Locked to frozen membership |
| [`CHANGELOG.md`](CHANGELOG.md) | Library and campaign version history | Started |
| [`proposals/`](proposals/) | Proposed membership changes and decision notes | Ready |

### Synthesis layer

| File | Role | Status |
|---|---|---|
| [`chronic-low-back-pain-thinking-artifact-workflow-v0.1.md`](chronic-low-back-pain-thinking-artifact-workflow-v0.1.md) | Phase status, object index, merge/split decisions | Phase 3 frozen · Phase 4 charter/outline frozen · public copy drafted |
| [`objects/`](objects/) | Per-object Stability Checks and Thinking Artifacts | Twelve check + artifact pairs **frozen** |
| [`freeze-register-v1.0.md`](freeze-register-v1.0.md) | Frozen §12 claims, shapes, and Phase 3 architecture | Object freeze complete · Phase 3 frozen |
| [`chronic-low-back-pain-evidence-landscape-phase3-v0.1.md`](chronic-low-back-pain-evidence-landscape-phase3-v0.1.md) | Comparative claim ladder and reader architecture | **Approved and frozen** |
| [`chronic-low-back-pain-page-reader-charter-phase4-v0.1.md`](chronic-low-back-pain-page-reader-charter-phase4-v0.1.md) | Phase 4 reader/product charter | **Frozen** |
| [`chronic-low-back-pain-page-outline-phase4-v0.1.md`](chronic-low-back-pain-page-outline-phase4-v0.1.md) | Phase 4 hub + topic outline | **Frozen** |
| [`public-copy/`](public-copy/) | Reader-facing copy drafts before HTML | **Frozen** |
| [`../../intervention-maps/chronic-low-back-pain.html`](../../intervention-maps/chronic-low-back-pain.html) + `chronic-low-back-pain-*.html` | Public hub + twelve topic pages | **Live · 2026-08-11** |

Accent color locked as design identity C (`#1a6b78` / ink `#134e58` in `sketch.css` as `ev--chronic-low-back-pain`). Not an official CLBP ribbon claim. In sitemap and on the Intervention Maps index.

---

## How to maintain the library

1. **Do not silently change membership.** Open a proposal in `proposals/` first.  
2. **Prefer primary versions.** Publisher / guideline organization / PubMed / PMC / Cochrane over mirrors.  
3. **Preserve rationale.** Every source keeps its role label, phenotype/duration metadata, claim-type note, and “why it belongs” note.  
4. **Bump versions deliberately.**  
   - Patch (v0.1 → v0.1.1): bibliographic correction; same membership  
   - Minor (v0.1 → v0.2): membership change after approved proposal  
   - Major (v1.0): library frozen enough for first full synthesis campaign  
5. **Add a source only if it** replaces a domain winner, creates a new trial-backed domain, materially changes a controversy, or is a landmark RCT reviews will keep depending on.

---

## Source ID scheme

- **A** Standard-of-care / guideline anchors  
- **B** Landscape syntheses that preserve guideline disagreement or a SOC the A set does not fully carry  
- **C** Domain-defining syntheses  
- **D** Landmark trials (only when needed)  
- **E** Not used as a separate “comparator-only” shelf in this campaign; medicines, injections, and surgery sit in A/B/C/D because they are on the map

Exact counts lock with Phase 0 membership.

---

## Parallel condition libraries

[`../adhd/`](../adhd/) · [`../depression/`](../depression/) · [`../anxiety/`](../anxiety/) · [`../rheumatoid-arthritis/`](../rheumatoid-arthritis/) · [`../osteoarthritis/`](../osteoarthritis/)
