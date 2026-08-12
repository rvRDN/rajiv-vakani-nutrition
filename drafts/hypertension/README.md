# Hypertension Evidence

**Status:** Step 0 owner-approved · Phase 0 library **frozen** (12 sources) · object index **accepted** (7) · Phase 1+2 **Frozen v1.0 (7/7)** · object freeze **complete** · Phase 3 Evidence Landscape **approved and frozen** · Phase 4 public-copy **Frozen v1.0** · HTML **live** (2026-08-12) · theme **locked** (`#c0242b`)  
**Campaign brief:** [`hypertension-campaign-brief-v0.1.md`](hypertension-campaign-brief-v0.1.md) (owner-approved August 12, 2026)  
**Methodology:** [`../adhd/condition-evidence-methodology-v1.0.md`](../adhd/condition-evidence-methodology-v1.0.md) adopted as-is (Metabolic batch)  
**Product philosophy:** [`../../evidence/evidence-product-charter.md`](../../evidence/evidence-product-charter.md)  
**Freeze register:** [`freeze-register-v1.0.md`](freeze-register-v1.0.md) (object freeze complete; Phase 3 frozen; Phase 4 public-copy frozen)  
**Phase 3 landscape:** [`hypertension-evidence-landscape-phase3-v0.1.md`](hypertension-evidence-landscape-phase3-v0.1.md) (**approved and frozen**)  
**Phase 4:** [`hypertension-page-reader-charter-phase4-v0.1.md`](hypertension-page-reader-charter-phase4-v0.1.md) · [`hypertension-page-outline-phase4-v0.1.md`](hypertension-page-outline-phase4-v0.1.md) · [`public-copy/`](public-copy/) (**Frozen v1.0**) · HTML: [`../../intervention-maps/hypertension.html`](../../intervention-maps/hypertension.html)

This folder holds two layers:

1. A permanent, versioned scientific reference collection.  
2. A claim-calibration synthesis layer (objects → freeze register → Phase 3 landscape).

The goal is to understand hypertension as an **intervention landscape**, not reproduce a source library. Research begins with the broad clinical population appropriate to hypertension. Stage rails, object boundaries, and reader architecture are findings, not scaffold assumptions. Lifestyle foundations, medicines, monitoring, diet patterns, supplements, herbs, devices, and popular home remedies are all in scope for investigation; seats are earned by evidence. Plant-based analogues are checked when appropriate ([`.cursor/rules/plant-based-analogue-check.mdc`](../../.cursor/rules/plant-based-analogue-check.mdc)). Owner nutrition curiosity does not lower the membership bar.

---

## Files

### Campaign and library layer

| File | Role | Status |
|---|---|---|
| [`hypertension-campaign-brief-v0.1.md`](hypertension-campaign-brief-v0.1.md) | Step 0 decision problem and research object | Owner-approved |
| [`hypertension-evidence-library-v0.1.md`](hypertension-evidence-library-v0.1.md) | Canonical membership, roles, rationale, controversies | **Frozen v0.1 · 12 sources** |
| [`citation-log-v0.1.md`](citation-log-v0.1.md) | Verified citations and primary identifiers | Locked to frozen membership |
| [`CHANGELOG.md`](CHANGELOG.md) | Library and campaign version history | Updated |
| [`proposals/`](proposals/) | Proposed membership changes and decision notes | Object index accepted |

### Synthesis layer

| File | Role | Status |
|---|---|---|
| [`hypertension-thinking-artifact-workflow-v0.1.md`](hypertension-thinking-artifact-workflow-v0.1.md) | Phase status, object index, merge/split decisions | Object freeze complete · Phase 3 frozen · Phase 4 in progress |
| [`objects/`](objects/) | Per-object Stability Checks and Thinking Artifacts | 7 checks Frozen v1.0 · 7 artifacts Frozen v1.0 |
| [`freeze-register-v1.0.md`](freeze-register-v1.0.md) | Frozen §12 claims, shapes, and Phase 3 architecture | Object freeze complete · Phase 3 frozen |
| [`hypertension-evidence-landscape-phase3-v0.1.md`](hypertension-evidence-landscape-phase3-v0.1.md) | Comparative claim ladder and reader architecture | **Approved and frozen** · August 12, 2026 |
| [`hypertension-page-reader-charter-phase4-v0.1.md`](hypertension-page-reader-charter-phase4-v0.1.md) | Phase 4 reader / product charter | **Frozen v1.0** |
| [`hypertension-page-outline-phase4-v0.1.md`](hypertension-page-outline-phase4-v0.1.md) | Phase 4 page outline / IA | **Frozen v1.0** |
| [`public-copy/`](public-copy/) | Hub + seven topic public-copy | **Frozen v1.0** · HTML under `intervention-maps/` |

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

**Library:** 12 sources frozen.  
**Objects:** 7 accepted; Phase 1+2 **Frozen v1.0**; object freeze **complete**.  
**Phase 3:** **approved and frozen** · one hub + seven topic pages.  
**Phase 4:** charter, outline, and public-copy drafts drafted · awaiting owner language review · no HTML yet. Awareness color still deferred.

---

## Parallel condition libraries

[`../adhd/`](../adhd/) · [`../depression/`](../depression/) · [`../anxiety/`](../anxiety/) · [`../rheumatoid-arthritis/`](../rheumatoid-arthritis/) · [`../osteoarthritis/`](../osteoarthritis/) · [`../chronic-low-back-pain/`](../chronic-low-back-pain/)
