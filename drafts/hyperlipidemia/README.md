# Hyperlipidemia Evidence

**Status:** Step 0 owner-approved · Phase 0 library **frozen** (11 sources) · object index **accepted** (7) · Phase 1+2 **Frozen v1.0 (7/7)** · object freeze **complete** · Phase 3 Evidence Landscape **approved and frozen** · Phase 4 language **frozen** · HTML **live** (2026-08-12) · awareness color **locked** (`#92293a`)  
**Campaign brief:** [`hyperlipidemia-campaign-brief-v0.1.md`](hyperlipidemia-campaign-brief-v0.1.md) (owner-approved August 12, 2026)  
**Methodology:** [`../adhd/condition-evidence-methodology-v1.0.md`](../adhd/condition-evidence-methodology-v1.0.md) adopted as-is (Metabolic batch)  
**Product philosophy:** [`../../evidence/evidence-product-charter.md`](../../evidence/evidence-product-charter.md)  
**Freeze register:** [`freeze-register-v1.0.md`](freeze-register-v1.0.md) (object freeze complete; Phase 3 approved and frozen; Phase 4 language frozen)  
**Phase 3 landscape:** [`hyperlipidemia-evidence-landscape-phase3-v0.1.md`](hyperlipidemia-evidence-landscape-phase3-v0.1.md) (**approved and frozen**)  
**Phase 4:** [`hyperlipidemia-page-reader-charter-phase4-v0.1.md`](hyperlipidemia-page-reader-charter-phase4-v0.1.md) · [`hyperlipidemia-page-outline-phase4-v0.1.md`](hyperlipidemia-page-outline-phase4-v0.1.md) · [`public-copy/`](public-copy/) (**language frozen**)  
**Object index:** [`proposals/2026-08-12-object-index-proposal.md`](proposals/2026-08-12-object-index-proposal.md) (**accepted** as revised)

This folder holds two layers:

1. A permanent, versioned scientific reference collection.  
2. A claim-calibration synthesis layer (objects → freeze register → Phase 3 landscape).

The goal is to understand hyperlipidemia as an **intervention landscape**, not reproduce a source library. Research begins with the broad clinical population appropriate to high lipids / cholesterol as people search it. Phenotype rails, prevention-context architecture, and reader architecture are findings, not scaffold assumptions. Lifestyle foundations, lipid-lowering medicines, diet tools, supplements, herbs, and popular home remedies are all in scope for investigation; seats are earned by evidence. Plant-based analogues are checked when appropriate ([`.cursor/rules/plant-based-analogue-check.mdc`](../../.cursor/rules/plant-based-analogue-check.mdc)). Owner nutrition curiosity does not lower the membership bar.

---

## Files

### Campaign and library layer

| File | Role | Status |
|---|---|---|
| [`hyperlipidemia-campaign-brief-v0.1.md`](hyperlipidemia-campaign-brief-v0.1.md) | Step 0 decision problem and research object | Owner-approved |
| [`hyperlipidemia-evidence-library-v0.1.md`](hyperlipidemia-evidence-library-v0.1.md) | Canonical membership, roles, rationale, controversies | **Frozen v0.1 · 11 sources** |
| [`citation-log-v0.1.md`](citation-log-v0.1.md) | Verified citations and primary identifiers | Locked to frozen membership |
| [`CHANGELOG.md`](CHANGELOG.md) | Library and campaign version history | Updated |
| [`proposals/`](proposals/) | Proposed membership changes and decision notes | Object index accepted |

### Synthesis layer

| File | Role | Status |
|---|---|---|
| [`hyperlipidemia-thinking-artifact-workflow-v0.1.md`](hyperlipidemia-thinking-artifact-workflow-v0.1.md) | Phase status, object index, merge/split decisions | Object freeze complete · Phase 3 frozen · Phase 4 language frozen |
| [`objects/`](objects/) | Per-object Stability Checks and Thinking Artifacts | 7 checks Frozen v1.0 · 7 artifacts Frozen v1.0 |
| [`freeze-register-v1.0.md`](freeze-register-v1.0.md) | Frozen §12 claims, shapes, and Phase 3 architecture | Object freeze complete · Phase 3 approved and frozen · Phase 4 language frozen |
| [`hyperlipidemia-evidence-landscape-phase3-v0.1.md`](hyperlipidemia-evidence-landscape-phase3-v0.1.md) | Comparative claim ladder and reader architecture | **Approved and frozen** |
| [`hyperlipidemia-page-reader-charter-phase4-v0.1.md`](hyperlipidemia-page-reader-charter-phase4-v0.1.md) | Phase 4 reader and product charter | **Language frozen** |
| [`hyperlipidemia-page-outline-phase4-v0.1.md`](hyperlipidemia-page-outline-phase4-v0.1.md) | Phase 4 page structure | **Language frozen** |
| [`public-copy/`](public-copy/) | Hub + seven topic public-copy drafts | **Language frozen** |

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
- **B** Landscape syntheses that preserve guideline disagreement or a SOC the A set does not fully carry  
- **C** Domain-defining syntheses  
- **D** Landmark trials (only when needed)  
- **E** Not used as a separate “comparator-only” shelf in this campaign; lifestyle and medicines sit in A/B/C/D because they are on the map

Exact counts lock with Phase 0 membership.

---

## Current inventory

**Library:** 11 sources frozen.  
**Objects:** 7 accepted; Phase 1+2 **Frozen v1.0**; object freeze **complete**.  
**Phase 3:** **approved and frozen** · one hub + seven topic pages locked · A/A′/A″ internal only · lipid≠events grammar locked.

**Phase 4:** **language frozen** · HTML built under `noindex` · awareness color locked (`#92293a` / `#6a1e2b`) · 2×2 role landscape retained · not on index/sitemap yet.

---

## Parallel condition libraries

[`../adhd/`](../adhd/) · [`../depression/`](../depression/) · [`../anxiety/`](../anxiety/) · [`../rheumatoid-arthritis/`](../rheumatoid-arthritis/) · [`../osteoarthritis/`](../osteoarthritis/) · [`../chronic-low-back-pain/`](../chronic-low-back-pain/) · [`../hypertension/`](../hypertension/)
