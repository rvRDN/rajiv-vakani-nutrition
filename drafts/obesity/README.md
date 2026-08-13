# Obesity Evidence

**Status:** Object freeze **complete** · Phase 0 library **frozen** (8 sources) · object index **accepted** (6) · Phase 1+2 **Frozen v1.0 (6/6)** · Phase 3 **approved and frozen** · Phase 4 charter + outline **Frozen v1.0** · public-copy **Frozen v1.0** · HTML **live**  
**Campaign brief:** [`obesity-campaign-brief-v0.1.md`](obesity-campaign-brief-v0.1.md) (owner-approved August 13, 2026)  
**Methodology:** [`../adhd/condition-evidence-methodology-v1.0.md`](../adhd/condition-evidence-methodology-v1.0.md) adopted as-is (post-Metabolic batch; v1.0 carried forward)  
**Product philosophy:** [`../../evidence/evidence-product-charter.md`](../../evidence/evidence-product-charter.md)  
**Freeze register:** [`freeze-register-v1.0.md`](freeze-register-v1.0.md) (object freeze complete · Phase 3 architecture locked · Phase 4 charter/outline/public-copy frozen · HTML live)

This folder holds two layers:

1. A permanent, versioned scientific reference collection.  
2. A claim-calibration synthesis layer (objects → freeze register → Phase 3 landscape).

The goal is to understand obesity as an **intervention landscape**, not reproduce a source library. Research begins with the broad clinical population appropriate to obesity as people search it. BMI-class rails, pediatric architecture, and reader architecture are findings, not scaffold assumptions. Lifestyle foundations, anti-obesity medicines, behavioral programs, surgery, devices, supplements, herbs, and popular home remedies are all in scope for investigation; seats are earned by evidence. Plant-based analogues are checked when appropriate ([`.cursor/rules/plant-based-analogue-check.mdc`](../../.cursor/rules/plant-based-analogue-check.mdc)). Owner nutrition curiosity does not lower the membership bar.

Type 2 diabetes, hypertension, and hyperlipidemia remain sibling campaigns. The Emerging Therapies peptide studio is a different product (overlapping molecules, no merge).

---

## Files

### Campaign and library layer

| File | Role | Status |
|---|---|---|
| [`obesity-campaign-brief-v0.1.md`](obesity-campaign-brief-v0.1.md) | Step 0 decision problem and research object | Owner-approved |
| [`obesity-evidence-library-v0.1.md`](obesity-evidence-library-v0.1.md) | Canonical membership, roles, rationale, controversies | **Frozen v0.1 · 8 sources** |
| [`citation-log-v0.1.md`](citation-log-v0.1.md) | Verified citations and primary identifiers | Locked to frozen membership |
| [`CHANGELOG.md`](CHANGELOG.md) | Library and campaign version history | Updated |
| [`proposals/`](proposals/) | Proposed membership changes and decision notes | Object index accepted |

### Synthesis layer

| File | Role | Status |
|---|---|---|
| [`obesity-thinking-artifact-workflow-v0.1.md`](obesity-thinking-artifact-workflow-v0.1.md) | Phase status, object index, merge/split decisions | Object freeze complete · Phase 3 frozen · Phase 4 public-copy frozen · HTML drafted `noindex` |
| [`objects/`](objects/) | Per-object Stability Checks and Thinking Artifacts | Frozen v1.0 (6/6 Phase 1 + 2 pairs) |
| [`freeze-register-v1.0.md`](freeze-register-v1.0.md) | Frozen §12 claims, shapes, and Phase 3 architecture | Object freeze complete · Phase 3 architecture locked |
| [`obesity-evidence-landscape-phase3-v0.1.md`](obesity-evidence-landscape-phase3-v0.1.md) | Comparative claim ladder and reader architecture | **Approved and frozen** |
| [`obesity-page-reader-charter-phase4-v0.1.md`](obesity-page-reader-charter-phase4-v0.1.md) | Phase 4 reader and product charter | **Frozen v1.0** |
| [`obesity-page-outline-phase4-v0.1.md`](obesity-page-outline-phase4-v0.1.md) | Phase 4 hub/topic outline | **Frozen v1.0** |
| [`public-copy/`](public-copy/) | Hub + six topic pages, reader-facing | **Frozen v1.0** |

---

## How to maintain the library

1. **Do not silently change membership.** Open a proposal in `proposals/` first.  
2. **Prefer primary versions.** Publisher / guideline organization / PubMed / PMC / Cochrane over mirrors.  
3. **Preserve rationale.** Every source keeps its role label, population/measurement metadata, claim-type note, and “why it belongs” note.  
4. **Bump versions deliberately.**  
   - Patch (v0.1 → v0.1.1): bibliographic correction; same membership  
   - Minor (v0.1 → v0.2): membership change after approved proposal  
   - Major (v1.0): library frozen enough for first full synthesis campaign  
5. **Add a source only if it** replaces a domain winner, creates a new trial-backed domain, materially changes a controversy, or is a landmark RCT reviews will keep depending on.

---

## Source ID scheme

- **A** Standard-of-care / guideline anchors  
- **B** Landscape syntheses that preserve comparative medicine placement the A set does not fully quantify  
- **C** Domain-defining syntheses  
- **D** Landmark trials (only when needed)  
- **E** Not used as a separate “comparator-only” shelf in this campaign; lifestyle and medicines sit in A/B/C/D because they are on the map

Exact counts lock with Phase 0 membership.

---

## Current inventory

**Library:** 8 sources frozen. No membership proposal.  
**Objects:** six accepted. Phase 1+2 Frozen v1.0 (6/6). Object freeze complete.  
**Phase 3:** approved and frozen (one hub + six topic pages; no A′; no T2D remission-pair import).  
**Phase 4:** charter, outline, and public-copy Frozen v1.0. HTML **live** under `intervention-maps/obesity*.html`. Color locked `#96720a` / `#684e08`. Sitemap and index plate added.

---

## Parallel condition libraries

[`../adhd/`](../adhd/) · [`../depression/`](../depression/) · [`../anxiety/`](../anxiety/) · [`../rheumatoid-arthritis/`](../rheumatoid-arthritis/) · [`../osteoarthritis/`](../osteoarthritis/) · [`../chronic-low-back-pain/`](../chronic-low-back-pain/) · [`../hypertension/`](../hypertension/) · [`../hyperlipidemia/`](../hyperlipidemia/) · [`../type-2-diabetes/`](../type-2-diabetes/)
