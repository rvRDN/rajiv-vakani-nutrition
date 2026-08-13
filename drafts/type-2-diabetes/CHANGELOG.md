# Type 2 Diabetes Evidence Library · Changelog

All notable library and campaign events are recorded here. Accepted membership changes require a proposal.

---

## v0.1 Full pre-publish checklist · 2026-08-12

- Full Intervention Maps pre-publish checklist run on hub (2×2 role landscape) + sample topics (medicines, structured weight-loss remission) at ~1100 / ~768 / ~390
- Width pass: 2×2 holds at ~1100/~768; stacks to one column at ~390; no horizontal scroll
- Typography: hub/topic lede short-word orphans bound
- Pass on items 1–10 (SEO already live; this pass covers typography + mobile that the live promote skipped)

---

## v0.1 scaffold · 2026-08-12

### Step 0 approved

- Research object: type 2 diabetes (broad clinical type 2 diabetes as people search it)
- Reader decision problem locked
- Metabolic batch continues: Hypertension (Phase 4 complete pre-publish) → Hyperlipidemia (Phase 4 HTML + wine-red theme) → Type 2 diabetes; obesity queued after the batch
- Full crowded landscape in scope: lifestyle, eating patterns, medicines, monitoring, supplements, CAM, devices, procedures, home remedies, remission/reversal claims
- Standard of care on the map (not comparator-only)
- Glycemic surrogates distinguished from kidney / CV / other hard outcomes
- Current guideline-era sequencing treated as claim hygiene
- Plant-based analogue check when appropriate (strong studies stay; analogues reported honestly)
- Reader architecture deferred to evidence synthesis
- Awareness color deferred to Phase 4 (IDF / World Diabetes Day blue is the documented candidate; not locked)
- Methodology v1.0 carried forward (hypertension and hyperlipidemia publish checklists remain open; not gates)

### Step 1 scaffold

- README and maintenance rules created
- Empty workflow and freeze-register shells created
- Proposals and objects directories created
- Phase 0 library drafted in the same pass (see below)

---

## v0.1 Phase 0 library drafted · 2026-08-12

### Currentness-first draft

- Search window through 12 August 2026
- **A1–A3:** ADA Standards of Care 2026; 2023 ESC CVD-in-diabetes; NICE NG28 (reviewed 18 February 2026)
- **B1:** Nong 2025 *BMJ* living NMA of medications (GRADE; risk-stratified absolute effects)
- **C1–C4:** Kunutsor 2024 intensive glucose (A1C ≠ MACE/mortality); Yuan 2024 diet-pattern NMA (A1C/weight; vegetarian included); Michielsen 2025 exercise (A1C + risk factors); Kanbour 2025 weight-loss/remission meta-regression
- **D1–D4:** ACCORD (intensive A1C mortality signal); Look AHEAD (lifestyle CV futility); DiRECT (remission protocol); SURPASS-CVOT (tirzepatide vs dulaglutide; living NMA predates this CVOT)
- Popular supplements, CGM-as-object, metabolic surgery, DSMES-as-object, Ayurveda/CAM left as explicit gaps
- GLP-1 / dual agonists kept on the T2D map; SELECT and obesity-without-diabetes CVOTs not imported
- **13 sources** drafted; awaiting owner acceptance

---

## v0.1 Phase 0 frozen at 13; object index proposed · 2026-08-12

### Owner pressure-test (12 → 13)

- Owner refused to freeze the 12-source draft unchanged. Architecture was strong; metabolic surgery as a named gap failed the library’s own pressure-test and the Step 0 crowded-landscape rule.
- **C5 added:** Yang, Miao, Wang, He. The long-term effect of bariatric/metabolic surgery versus pharmacologic therapy in type 2 diabetes mellitus patients. *Diabetes Metab Res Rev*. 2024. DOI: 10.1002/dmrr.3830. T2D-specific ≥5-year SR/MA vs pharmacologic therapy (15 articles; 85,473 participants).
- ARMMS-T2D (Courcoulas 2024 *JAMA*) stays **companion** for RCT-only 7–12 year follow-up, adverse events, and no-MACE-difference grain. STAMPEDE and Mingrone 10-year stay companions. Not stacked as D5.
- Nothing else added or removed. D1–D4 retained. CGM, DSMES, and supplements/CAM remain named gaps.
- Phase 0 frozen at **13 sources** (A1–A3 + B1 + C1–C5 + D1–D4).
- Object index proposed (six objects): [`proposals/2026-08-12-object-index-proposal.md`](proposals/2026-08-12-object-index-proposal.md). Folders not opened until acceptance.

---

## v0.1 object index accepted as revised; Phase 1 drafted (6/6) · 2026-08-12

### Rename, then freeze

- Owner accepted the six-object structure after one wording/scope change: **Glucose-lowering medicines → Diabetes medicines**.
- Internal definition: medicines used within T2D care whose decision value may be glycemic, cardiovascular, kidney, weight-related, or some combination. Organ protection versus glucose lowering stays mandatory internal structure, not two objects.
- Finerenone stays a CKD-context organ-protective branch. ADA 2026 distinguishes nsMRA kidney/CV protection from glucose lowering; B1 finds no HbA1c reduction for finerenone. The old glycemic heading would have smuggled that mismatch.
- Nothing else added or removed. No seventh object. CGM and DSMES remain not-objects. Library stays at 13.
- Look AHEAD (D2) locked as annotation against hard-outcome overreach of an intensive multicomponent lifestyle intervention, not as “diet didn't prevent CVD” or “exercise didn't prevent CVD.”
- Six folders opened. Phase 1 Evidence Stability Checks drafted for all six objects. Status: Drafted · awaiting owner freeze of §12. No Phase 2 artifacts yet.

---

## v0.1 Phase 1 frozen (6/6); Phase 2 drafted · 2026-08-12

### Owner freeze of all six §12 claims

- Owner froze all six Phase 1 Stability Checks as drafted. No §12 wording changes.
- Library remains **13**. No membership proposal. No seventh object.
- Broader lock before Phase 2: the six objects have genuinely different evidentiary shapes. Phase 2 must preserve those differences rather than forcing an identical argumentative template.
- Phase 2 Thinking Artifacts drafted for all six objects. Status: Drafted · awaiting owner freeze. §12 claims carried verbatim.

---

## v0.1 Phase 2 frozen (6/6); object freeze complete; Phase 3 drafted · 2026-08-12

### Owner freeze of all six Thinking Artifacts

- Owner froze all six Phase 2 artifacts as drafted. No §12 weakening, no hidden architecture decision, no new claim requiring Phase 1 reopen.
- Distinct evidentiary shapes preserved: hard-outcome class spine + internal controversies (medicines); comparative A1C/weight gradient with humility (eating patterns); mode A1C/risk-factor gradient without event ranking (exercise); C4 + DiRECT traveling together (structured remission); two-grain C5/ARMMS framing (surgery); closed promotion gate as the finding (popular supplements).
- Object freeze complete (Phase 1 + 2 pairs). Library remains **13**. No membership proposal. No seventh object.
- Phase 3 Evidence Landscape drafted: [`type-2-diabetes-evidence-landscape-phase3-v0.1.md`](type-2-diabetes-evidence-landscape-phase3-v0.1.md). Proposed architecture: one hub + six topic pages. No A′ for surgery. B and C are two uncollapsed remission routes. Awaiting owner approval. Phase 4 remains blocked.

---

## v0.1 Phase 3 frozen; Phase 4 authorized · 2026-08-12

### Owner freeze of the Evidence Landscape as drafted

- Owner froze Phase 3 as drafted. No revision before Phase 4.
- Architecture earned: one shared T2D hub + six topic pages. Divergences are internal claim types and annotations, not insulin/non-insulin, organ-protection/glucose-lowering, remission, or obesity hubs.
- Claim ladder A–F frozen, including no A′ and band-not-tier. B and C are two uncollapsed remission routes, not efficacy grades.
- Relative-space and cross-link requirements frozen. Named gaps stay non-seats. Landscape grammar frozen: A1C/glucose/weight ≠ hard outcomes; remission ≠ cure. Six evidentiary shapes preserved. A topic page is not evidentiary parity.
- Phase 4 authorized. Reader charter and page outline drafted: [`type-2-diabetes-page-reader-charter-phase4-v0.1.md`](type-2-diabetes-page-reader-charter-phase4-v0.1.md) · [`type-2-diabetes-page-outline-phase4-v0.1.md`](type-2-diabetes-page-outline-phase4-v0.1.md). Awaiting owner freeze. Awareness color remains deferred until the Phase 4 design decision.

---

## v0.1 Phase 4 charter + outline frozen; public-copy drafted · 2026-08-12

### Owner freeze of the reader charter and page outline as drafted

- Owner froze both Phase 4 teaching documents as drafted. No revision before public copy.
- At a Glance grouping locked: medicines alone in heart/kidney/death; surgery and structured programs together only as two remission routes; eating and exercise as a surrogate neighborhood; supplements as their own investigated category. Groups are orientation, not equal treatments.
- Six pages mean six decisions worth teaching. Hierarchy comes from order, space, and Bottom lines.
- Awareness color **family locked** to IDF / World Diabetes Day blue. Site's own condition token. Not type-2-exclusive. No IDF circle mark. Exact hex deferred until first rendered page. No CSS before the public-copy gate.
- Public-copy drafts written under [`public-copy/`](public-copy/). Awaiting owner freeze. HTML not started.

---

## v0.1 Phase 4 public-copy frozen · HTML built · 2026-08-12

### Owner freeze of public copy after three targeted edits

- Owner froze the public-copy layer after three copy-only patches. No science, object, or architecture reopen.
- **Structured remission opening:** general definition is blood sugar below the diabetes threshold without glucose-lowering medicines for a defined period; DiRECT's A1C <6.5% / two-month off-drug rule stays in participation.
- **Supplements first screen:** “Some products have shown A1C changes in studies. The evidence is mixed and often thin.” (no magnitude judgment of “a little”).
- **Hub structured-remission sentence:** “about half of the eligible, recently diagnosed adults not using insulin at one year, and far fewer years later.”
- Everything else in public copy frozen as written.
- HTML built: `intervention-maps/type-2-diabetes.html` + six topic pages. `noindex`. Not on Intervention Maps index. `sitemap.xml` untouched.
- First-render awareness tokens: `--condition: #2f6499` · `--condition-ink: #234a73` on `body.ev--type-2-diabetes`. Family locked; exact pair pending owner judgment on the rendered hub.

---

## v0.1 Live · 2026-08-12

### Metabolic batch live promote

- Owner approved a Metabolic-batch live promote with hypertension and hyperlipidemia
- Removed `noindex` from hub + six topic pages
- Added URLs to `sitemap.xml` and plates to the Intervention Maps index
- Insights morph, homepage exhibit, and Library counts updated to nine conditions
