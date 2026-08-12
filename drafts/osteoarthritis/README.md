# Osteoarthritis Evidence

**Status:** Object freeze complete (12/12) · Phase 3 **approved and frozen** · Phase 4 hub and all twelve topic pages **live** (2026-08-11)  
**Campaign brief:** [`osteoarthritis-campaign-brief-v0.1.md`](osteoarthritis-campaign-brief-v0.1.md) (owner-approved August 11, 2026)  
**Methodology:** [`../adhd/condition-evidence-methodology-v1.0.md`](../adhd/condition-evidence-methodology-v1.0.md) adopted as-is (Pain batch)  
**Product philosophy:** [`../../evidence/evidence-product-charter.md`](../../evidence/evidence-product-charter.md)  
**Freeze register:** [`freeze-register-v1.0.md`](freeze-register-v1.0.md) (object freeze complete)

This folder holds two layers:

1. A permanent, versioned scientific reference collection.  
2. A claim-calibration synthesis layer (objects → freeze register → Phase 3 landscape).

The goal is to understand osteoarthritis as an **intervention landscape**, not reproduce a source library. Research begins with the broad clinical population appropriate to OA. Joint-site rails, object boundaries, and reader architecture are findings, not scaffold assumptions. Exercise, weight management, topical and oral medicines, injections, surgery, supplements, regenerative claims, devices, and popular home remedies are all in scope for investigation; seats are earned by evidence.

---

## Files

### Campaign and library layer

| File | Role | Status |
|---|---|---|
| [`osteoarthritis-campaign-brief-v0.1.md`](osteoarthritis-campaign-brief-v0.1.md) | Step 0 decision problem and research object | Owner-approved |
| [`osteoarthritis-evidence-library-v0.1.md`](osteoarthritis-evidence-library-v0.1.md) | Canonical membership, roles, rationale, controversies | **Frozen v0.1 · owner-accepted (19 sources)** |
| [`citation-log-v0.1.md`](citation-log-v0.1.md) | Verified citations and primary identifiers | Locked to library membership |
| [`CHANGELOG.md`](CHANGELOG.md) | Library and campaign version history | Started |
| [`proposals/`](proposals/) | Proposed membership changes and decision notes | Ready |

### Synthesis layer

| File | Role | Status |
|---|---|---|
| [`osteoarthritis-thinking-artifact-workflow-v0.1.md`](osteoarthritis-thinking-artifact-workflow-v0.1.md) | Phase status, object index, merge/split decisions | Object freeze complete; Phase 3 frozen; Phase 4 opened |
| [`proposals/2026-08-11-object-index-proposal.md`](proposals/2026-08-11-object-index-proposal.md) | Decision objects after library freeze | **Accepted** August 11, 2026 |
| [`objects/`](objects/) | Per-object Stability Checks and Thinking Artifacts | Frozen v1.0 (12/12) |
| [`freeze-register-v1.0.md`](freeze-register-v1.0.md) | Frozen §12 claims, shapes, and Phase 3 architecture | Object freeze complete; Phase 3 frozen |
| [`osteoarthritis-evidence-landscape-phase3-v0.1.md`](osteoarthritis-evidence-landscape-phase3-v0.1.md) | Comparative claim ladder and architecture | **Approved and frozen** |
| [`osteoarthritis-page-reader-charter-phase4-v0.1.md`](osteoarthritis-page-reader-charter-phase4-v0.1.md) | Phase 4 teaching constraints | Owner-accepted |
| [`osteoarthritis-page-outline-phase4-v0.1.md`](osteoarthritis-page-outline-phase4-v0.1.md) | Hub and twelve topic-page structure | Owner-accepted; hub drafted for review |

Public hub and twelve topic pages live at [`../../intervention-maps/osteoarthritis.html`](../../intervention-maps/osteoarthritis.html) and `osteoarthritis-*.html`. Awareness color locked: restrained arthritis green `#007636`. In sitemap and on the Intervention Maps index.

---

## How to maintain the library

1. **Do not silently change membership.** Open a proposal in `proposals/` first.  
2. **Prefer primary versions.** Publisher / guideline organization / PubMed / PMC / Cochrane over mirrors.  
3. **Preserve rationale.** Every source keeps its role label, site metadata, claim-type note, and “why it belongs” note.  
4. **Bump versions deliberately.**  
   - Patch (v0.1 → v0.1.1): bibliographic correction; same membership  
   - Minor (v0.1 → v0.2): membership change after approved proposal  
   - Major (v1.0): library frozen enough for first full synthesis campaign  
5. **Add a source only if it** replaces a domain winner, creates a new trial-backed domain, materially changes a controversy, or is a landmark RCT reviews will keep depending on.

---

## Source ID scheme

- **A** Standard-of-care / guideline anchors  
- **B** Landscape syntheses  
- **C** Domain-defining syntheses  
- **D** Landmark trials (only when needed)  
- **E** Not used as a separate “comparator-only” shelf in this campaign; medicines and surgery sit in A/B/C/D because they are on the map

Exact counts lock with Phase 0 membership.

---

## Parallel condition libraries

[`../adhd/`](../adhd/) · [`../depression/`](../depression/) · [`../anxiety/`](../anxiety/) · [`../rheumatoid-arthritis/`](../rheumatoid-arthritis/)
