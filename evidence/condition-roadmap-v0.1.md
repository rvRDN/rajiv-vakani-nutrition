# Evidence condition roadmap · v0.1

**Status:** Living product log · not a freeze  
**Started:** July 18, 2026  
**Applies to:** Condition selection and expansion for the Evidence product  
**Does not replace:** [`evidence-product-charter.md`](evidence-product-charter.md), methodology v1.0, or per-condition freeze registers  
**Companions:** [`new-condition-playbook-v0.1.md`](new-condition-playbook-v0.1.md) · [`methodology-changelog-v0.1.md`](methodology-changelog-v0.1.md)

This file is the running log for where Evidence goes next, why a condition earns a seat, and what philosophy we extracted along the way. Append dated entries. Do not silently rewrite history; bump the version when the queue or selection rules change materially.

---

## Product realization (locked in conversation, July 18, 2026)

We are not building a library of diseases.

We are building a library of **decision landscapes**.

| What people do | What the product answers |
|---|---|
| Search by **condition** (“how do I treat migraines?”) | One coherent map of the therapeutic landscape |
| Think by **intervention** (“should I try magnesium?”) | Where that option sits among everything else studied |

Most health sites answer: *Does magnesium help migraines?*

This product answers: *Where does magnesium fit among everything else we know about migraines?*

That is closer to how clinicians think (a map of options and seats) than how content farms think (one intervention article at a time). ADHD and depression were the pilot of that product shape, not a mental-health niche.

### Selection criteria (use these, not prevalence alone)

A condition earns a campaign when it meets **all three**:

1. **Common enough** that real readers arrive.  
2. **Crowded therapy landscape:** medications, lifestyle, supplements, behavioral therapies, and/or popular alternatives compete in public conversation.  
3. **High decision uncertainty:** patients are actively searching because there is not one obvious answer.

Prefer long-term management with many competing claims over acute conditions with a clear standard of care (e.g. strep throat, appendicitis). Those do not need a giant evidence landscape.

### Research object vs reader architecture

| Decision | When |
|---|---|
| **Research object** (what literature counts; decision problem) | Before Phase 0 (Step 0 brief) |
| **Reader architecture** (one map vs branches vs separate hubs) | After Phase 2/3, when the evidence has spoken |

Define the campaign by the reader’s decision problem. Collect the common landscape for that condition. Let synthesis decide whether natural branches, annotations, or later separate campaigns are earned. Do not invent exclusions for neatness. Exclude later only when evidence shows a substantially different landscape, rarity, or no useful data for the desperate-reader test.

ADHD did not start as “adult vs child pages.” Research revealed the age rail. Every new condition gets the same research-first treatment, but **adult + pediatric collection is not a universal default**. Begin with the broad clinical population appropriate to the condition and let evidence show whether age-specific coverage changes the map.

Default public shell stays familiar: hub → topic pages. Do not pre-decide a different IA in Step 0.

### Scope discipline

| Prefer | Avoid as a single page |
|---|---|
| Hypertension, hyperlipidemia, coronary disease (separate when landscapes differ) | “Cardiovascular disease” as one mega-page |
| Osteoarthritis, rheumatoid arthritis (separate when landscapes differ) | “Arthritis” as one mega-page |
| Distinct decision problems (anxiety vs insomnia vs migraine) | Vague “mental health” buckets as the product |

Split when synthesis shows the therapeutic landscape is substantially different. The condition is the doorway; the intervention map is the product.

### How readers actually think (design for this)

Someone rarely wakes up and Googles an obscure supplement name first. They Google the condition, then ask:

- Should I try X?  
- Which form / dose / protocol?  
- Is it actually worth trying?  
- Before or after medication?  
- What do guidelines say?  
- Is there anything better on this map?

The public page places each option. It does not recommend one.

### Methodology release rule

Run a condition **batch** on one frozen methodology version. Review. Then bump (e.g. v1.0 → v1.1) only if a change is broadly applicable. Freeze that version for the next batch. Do not tweak phases every condition.

See [`methodology-changelog-v0.1.md`](methodology-changelog-v0.1.md).

---

## Batching plan (owner, July 18, 2026)

Prove the methodology is generalizable; refine the system between batches, not mid-condition.

| Batch | Conditions | Methodology |
|---|---|---|
| **Brain & mental health** | ADHD ✓ · Depression ✓ · Anxiety ✓ (batch closed Aug 10, 2026; public polish may continue later) | v1.0; Brain review logged with no methodology bump |
| **Pain & musculoskeletal** | Rheumatoid arthritis ✓ · Osteoarthritis ✓ · Chronic low back pain ✓ (fibromyalgia watch) | v1.0 carried forward |
| **Metabolic health** | Hypertension ✓ · Hyperlipidemia ✓ · Type 2 diabetes ✓ (obesity queued after the batch) | v1.0 carried forward; Pain post-condition checkpoints remain open and are not a gate |
| **After those batches** | Owner decides order for insomnia, migraine, IBS, remaining watch list | — |

✓ = campaign complete through Phase 4 owner approval (or owner batch-close decision).

---

## Suggested site families (navigation, not methodology)

Families are for eventual hub navigation. They do **not** change Phases 0–4 or claim calibration.

| Family | Candidate conditions |
|---|---|
| Brain & mental health | ADHD ✓ · Depression ✓ · Anxiety ✓ · Insomnia · Migraine |
| Pain & musculoskeletal | Rheumatoid arthritis ✓ · Osteoarthritis ✓ · Chronic low back pain ✓ · Fibromyalgia (later) |
| Metabolic health | Hypertension ✓ · Hyperlipidemia ✓ · Type 2 diabetes ✓ · Obesity · Metabolic syndrome (later) |
| Digestive health | IBS · GERD · IBD (later) |
| Women’s health | PCOS · Menopause · Endometriosis (later) |

---

## Priority queue

Owner-aligned working order. Reorder only with an explicit log entry.

| # | Condition | Fit notes | Status |
|---|---|---|---|
| 1 | Anxiety disorders | Brain batch closeout | **Batch-closed · Phase 4 pages built; further polish deferred** |
| 2 | Rheumatoid arthritis | Pain batch lead | **Live · sitemap repaired 2026-08-11** |
| 3 | Osteoarthritis | Pain batch; exercise, weight, PT, topicals, supplements, injections | **Live · 2026-08-11** |
| 4 | Chronic low back pain | Pain batch; one of the densest evidence landscapes in medicine | **Live · 2026-08-11** |
| 5 | Hypertension | Metabolic batch lead; huge lifestyle + supplement landscape | **Live · 2026-08-12** |
| 6 | Hyperlipidemia | Metabolic batch; split from “CVD” | **Live · 2026-08-12** |
| 7 | Type 2 diabetes | Metabolic batch third seat (locked Aug 12, 2026) | **Live · 2026-08-12** |
| 8 | Obesity | After Metabolic batch; separate decision problem from T2D | Queued (post-batch) |
| 9 | Migraine | Classic supplement + device + lifestyle decision map | Queued (post-batch) |
| 10 | Insomnia | CBT-I, hygiene, meds, supplements, light | Queued (post-batch) |
| 11 | IBS | Diets, gut-directed therapies, probiotics, psychotherapies | Queued (post-batch) |
| — | Fibromyalgia, PCOS, GERD, eczema, allergic rhinitis, asthma | Second wave | Watch |

**Depression Phase 4 owner review is done (July 18, 2026).** Brain batch closed Aug 10, 2026. Pain batch live Aug 11, 2026 (RA, OA, CLBP). Metabolic batch live Aug 12, 2026 (Hypertension, Hyperlipidemia, Type 2 diabetes). Next: Obesity after Metabolic, or owner pick from the post-batch queue. Pain-batch and Metabolic post-condition “one process change?” checkpoints remain open by owner choice and are not a live gate.

---

## Efficiency thesis

**Yes, a few-step spin-up is possible** for scaffolding and process. Depression already proved the methodology transfers without reinventing Phases 0–4.

What becomes fast:

- Folder scaffold, file naming, source ID scheme, freeze register shape  
- Shared charter, writing rules, hub → topic grammar, CSS system  
- Object checklist and Phase gates  

What must stay slow (and honest):

- Phase 0 library membership judgment  
- Phase 1 adversarial Stability Checks  
- Phase 3 relative calibration  
- Phase 4 teaching that does not exceed §12 claims  

Efficiency means reusable scaffolding and a clear playbook, not skipping claim calibration. See [`new-condition-playbook-v0.1.md`](new-condition-playbook-v0.1.md).

---

## Decision log

### 2026-08-12 · Full site pre-publish remediation (typography + mobile)

**Participants:** Owner + Cursor.

**Decisions:**

1. Ran the full Intervention Maps checklist (items 1–10) and site-wide pre-publish checklist (items 1–8) on the six conditions that skipped mobile QA (RA, OA, CLBP, hypertension, hyperlipidemia, type 2 diabetes) plus room landings (home, Insights, Library, Intervention Maps index, Emerging Therapies, Seeing Food Differently, Therapy Profiles). Widths checked: ~1100 / ~768 / ~390.  
2. Unusual layouts checked: hyperlipidemia and type 2 diabetes 2×2 role landscapes; hypertension named strata; CLBP route map.  
3. Fixes: display-type `&nbsp;` binds; meta descriptions brought into ~120–155; Intervention Maps index mini-strata labels no longer clip inside the shortest band; Seeing Food Differently header wraps the place name onto its own row at ≤720px; placeholder em dash on the “More conditions” plate replaced with an en dash.  
4. SEO/sitemap were already live. This log is the missing typography + mobile Pass, not a second go-live.

**Open:** Obesity campaign start remains queued.

### 2026-08-12 · Metabolic batch live (Hypertension, Hyperlipidemia, Type 2 diabetes)

**Participants:** Owner + Cursor.

**Decisions:**

1. Hypertension, hyperlipidemia, and type 2 diabetes go live together as the Metabolic batch.  
2. Removed `noindex` from 23 pages (HTN 8 · HL 8 · T2D 7). Added those URLs to `sitemap.xml`.  
3. Intervention Maps index is now nine live plates. Insights morph, homepage exhibit, and Library counts updated to match.  
4. Obesity remains queued after the Metabolic batch. Post-condition “one process change?” checkpoints remain open and are not a live gate.

**Open:** Obesity campaign start, or owner pick from the post-batch queue. Metabolic process checkpoint.

---

### 2026-08-12 · Type 2 diabetes public-copy frozen; HTML built (pre-publish)

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner froze the public-copy layer after three targeted copy edits. No science, object, or architecture reopen. Everything else frozen as written.  
2. Structured-remission opening defines remission generally (blood sugar below the diabetes threshold without glucose-lowering medicines for a defined period). DiRECT's A1C <6.5% / two-month off-drug rule stays in participation.  
3. Supplements first screen: A1C changes in studies; mixed and often thin. No “a little” magnitude judgment.  
4. Hub structured-remission sentence names eligible, recently diagnosed adults not using insulin at one year.  
5. HTML built: `intervention-maps/type-2-diabetes.html` + six topic pages. All `noindex, nofollow`. Not on Intervention Maps index. `sitemap.xml` untouched.  
6. First-render awareness tokens: `--condition: #2f6499` · `--condition-ink: #234a73` on `body.ev--type-2-diabetes`. Family remains IDF / World Diabetes Day blue. Exact pair pending owner judgment on the rendered hub.

**Open:** Owner visual judgment of the diabetes-blue/ink pair on the hub; then publish checklist when ready (sitemap, index plate, remove noindex). Hypertension and hyperlipidemia publish checklists remain independently parked.

---

### 2026-08-12 · Type 2 diabetes Phase 4 charter + outline frozen; public-copy drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner froze the Phase 4 reader charter and page outline as drafted. No revision before public copy.  
2. At a Glance grouping locked as orientation, not equal treatments or a recommendation chart.  
3. Six pages mean six decisions worth teaching. Hierarchy from order, space, and Bottom lines.  
4. Awareness color **family locked** to IDF / World Diabetes Day blue. Site's own condition token. Not type-2-exclusive. No IDF circle mark. Exact hex deferred until first rendered page on Intervention Maps paper. No CSS before the public-copy gate.  
5. Public-copy drafts written. HTML remains blocked until public-copy freeze.

**Closed later the same day:** Owner froze public copy after three targeted edits. HTML built under `noindex`. First-render diabetes blue `#2f6499` / `#234a73` pending hub judgment.

---

### 2026-08-12 · Type 2 diabetes Phase 3 frozen; Phase 4 authorized

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner froze the Phase 3 Evidence Landscape as drafted. No revision before Phase 4.  
2. Architecture locked: one Type 2 diabetes hub + six topic pages. Earned from the six frozen objects, not imposed. Not insulin/non-insulin, organ-protection/glucose-lowering, remission, or obesity hubs.  
3. Claim ladder A–F locked as internal bands, not efficacy grades. **No A′.** B and C are two uncollapsed remission routes, not a prime pair.  
4. Frozen with the landscape: non-collapse rules and annotations; relative-space and cross-link requirements; named gaps as non-seats; A1C/glucose/weight ≠ hard outcomes and remission ≠ cure as landscape grammar; six distinct evidentiary shapes; a topic page is not evidentiary parity.  
5. Phase 4 authorized. Reader charter and page outline drafted. Awareness color remains deferred until the Phase 4 design decision.

**Closed later the same day:** Owner froze the charter and outline as drafted. Public-copy drafted. Diabetes-blue family locked; hex deferred.

---

### 2026-08-12 · Type 2 diabetes Phase 2 frozen (6/6); object freeze complete; Phase 3 drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner froze all six Phase 2 Thinking Artifacts as drafted. No artifact-level leakage, hidden architecture decision, §12 weakening, or new claim requiring Phase 1 reopen.  
2. Distinct evidentiary shapes preserved rather than one common “evidence summary” template.  
3. Object freeze complete. Campaign state: Phase 0 frozen at 13; six-object index frozen; Phase 1 frozen for all six; Phase 2 frozen for all six.  
4. Phase 3 Evidence Landscape drafted: [`../drafts/type-2-diabetes/type-2-diabetes-evidence-landscape-phase3-v0.1.md`](../drafts/type-2-diabetes/type-2-diabetes-evidence-landscape-phase3-v0.1.md). Proposed: one hub + six topic pages; no A′ for surgery; B and C as two uncollapsed remission routes. Awaiting owner approval. Phase 4 remains blocked.

**Closed later the same day:** Owner froze Phase 3 as drafted. Phase 4 authorized.

---

### 2026-08-12 · Type 2 diabetes Phase 1 frozen (6/6); Phase 2 drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner froze all six Phase 1 Stability Checks as drafted. No §12 wording changes.  
2. Library remains **13**. No membership proposal. No seventh object.  
3. Broader lock: the six objects have genuinely different evidentiary shapes. Phase 2 must preserve those differences rather than forcing an identical argumentative template.  
   - Diabetes medicines: hard-outcome class evidence plus sequencing conflict  
   - Eating patterns / exercise: comparative surrogate/risk-factor gradients  
   - Structured weight-loss remission: dose-response plus protocol/durability  
   - Metabolic surgery: long-term remission plus RCT/observational design tension  
   - Popular supplements: deliberately negative promotion result  
4. Phase 2 Thinking Artifacts drafted for all six objects. §12 carried verbatim. Awaiting owner freeze of Phase 2.

**Closed later the same day:** Owner froze Phase 2 as drafted. Object freeze complete. Phase 3 drafted.

---

### 2026-08-12 · Type 2 diabetes object index accepted as revised; Phase 1 drafted (6/6)

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted the six-object structure after one wording/scope change: **Glucose-lowering medicines → Diabetes medicines.** Folder: `objects/diabetes-medicines/`.  
2. Internal definition: medicines used within T2D care whose decision value may be glycemic, cardiovascular, kidney, weight-related, or some combination. Organ protection versus glucose lowering remains mandatory internal structure, not two objects.  
3. Finerenone stays a CKD-context organ-protective branch. ADA 2026 treats it as a nonsteroidal mineralocorticoid receptor antagonist for kidney/CV protection in T2D with CKD and distinguishes that mechanism from glucose lowering. B1 finds no HbA1c reduction for finerenone. The old glycemic heading would have smuggled that mismatch.  
4. Nothing else added or removed. No seventh object. CGM and DSMES remain not-objects. Eating-pattern / DiRECT split, structured-remission / surgery split, one exercise object with mode branches, and popular supplements with no seated C all stand.  
5. Look AHEAD (D2) is an annotation against hard-outcome overreach of an intensive multicomponent lifestyle intervention. It is not “diet didn't prevent CVD” and not “exercise didn't prevent CVD.”  
6. Library membership remains **13**. Folders opened. Phase 1 Evidence Stability Checks drafted for all six objects. No Phase 2 artifacts. No §12 owner-frozen yet.

**Open:** Owner freeze (or revise) of each §12, then Phase 2 Thinking Artifacts.

---

### 2026-08-12 · Type 2 diabetes Phase 0 frozen at 13; object index proposed

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner refused to freeze the 12-source Phase 0 draft unchanged. Surgery as a named gap failed the library’s own pressure-test and the Step 0 crowded-landscape / watch-list rule. Dietary remission (C4 + D3) without a surgery seat would have made the remission landscape asymmetric.  
2. **C5 added:** Yang et al., 2024. Long-term metabolic/bariatric surgery vs pharmacologic therapy in T2D (*Diabetes Metab Res Rev*; DOI 10.1002/dmrr.3830). T2D-specific ≥5-year systematic review, not a single procedure trial.  
3. ARMMS-T2D (Courcoulas 2024 *JAMA*) stays companion for RCT-only 7–12 year follow-up, adverse-event costs, and no MACE difference. Observational event/mortality pools in C5 must not overwrite that grain.  
4. Nothing else added or removed. D1–D4 retained. CGM, DSMES, and supplements/CAM remain named gaps.  
5. Phase 0 frozen at **13 sources** (A1–A3 + B1 + C1–C5 + D1–D4). Citation log locked.  
6. Object index proposed: [`../drafts/type-2-diabetes/proposals/2026-08-12-object-index-proposal.md`](../drafts/type-2-diabetes/proposals/2026-08-12-object-index-proposal.md) (six objects). Folders not opened until acceptance.

**Open:** Owner acceptance of the six-object index, then Phase 1.

---

### 2026-08-12 · Type 2 diabetes Step 0 frozen; scaffold + Phase 0 library drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Type 2 diabetes Step 0 brief **owner-approved and frozen as drafted** (no changes).  
2. Step 1 scaffold complete under `drafts/type-2-diabetes/` (README, citation log, workflow, freeze-register header, proposals, empty objects).  
3. Phase 0 minimal library **drafted** (12 sources) from a currentness-first search through 12 August 2026: [`../drafts/type-2-diabetes/type-2-diabetes-evidence-library-v0.1.md`](../drafts/type-2-diabetes/type-2-diabetes-evidence-library-v0.1.md).  
4. Seated inventory: **A1–A3** (ADA Standards 2026; 2023 ESC CVD-in-diabetes; NICE NG28 reviewed 18 Feb 2026) · **B1** (Nong 2025 *BMJ* living medicines NMA) · **C1–C4** (Kunutsor intensive glucose; Yuan diet-pattern NMA; Michielsen exercise; Kanbour remission meta-regression) · **D1–D4** (ACCORD; Look AHEAD; DiRECT; SURPASS-CVOT).  
5. Explicit gaps preserved: cinnamon/berberine/chromium-class products, Ayurveda/CAM, CGM-as-object, metabolic surgery, DSMES-as-forced-C, insulin landmark, finerenone dedicated D, SELECT/obesity-without-diabetes CVOTs, algae-oil analogue.  
6. No objects opened. No architecture. No claims frozen. Awareness color remains deferred.  
7. Hypertension and hyperlipidemia publish checklists remain open and remain not gates.

**Open:** Owner acceptance of the 12-source Phase 0 library, then object-index proposal.

---

### 2026-08-12 · Type 2 diabetes Step 0 opened

**Participants:** Owner + Cursor.

**Decisions:**

1. Hypertension and hyperlipidemia Phase 4 remain **complete pre-publish** (themes locked; `noindex`; sitemap/index deferred). Those publish checklists are owner-gated and are **not** a gate on Type 2 diabetes.  
2. Type 2 diabetes is the next Metabolic-batch campaign after hyperlipidemia. Methodology remains **v1.0**.  
3. Step 0 brief drafted: [`../drafts/type-2-diabetes/type-2-diabetes-campaign-brief-v0.1.md`](../drafts/type-2-diabetes/type-2-diabetes-campaign-brief-v0.1.md).  
4. Research object is **broad clinical type 2 diabetes** as people search it, not a cardiometabolic mega-page, not a premature insulin vs non-insulin split, and not a merge with obesity. Prediabetes, type 1, remission headlines, complication-specific care, and youth-onset T2D remain watch-list questions for Phase 0–3.  
5. Standard of care stays on the map (lifestyle foundations and glucose-lowering medicines), same Metabolic-batch stance as hypertension and hyperlipidemia.  
6. Awareness color deferred to Phase 4. IDF / World Diabetes Day **blue circle** is the documented candidate (diabetes-wide, not type-2-only; circle mark itself is not for use). Ask the owner before CSS.  
7. Phase 0 library stays closed until the owner accepts this brief.

**Open:** Owner approval of the type 2 diabetes Step 0 brief, then scaffold + Phase 0 library.

---

### 2026-08-12 · Hyperlipidemia awareness color locked; 2×2 landscape retained

1. Owner confirmed 2×2 role landscape stays (roles, not a descending ladder) and sticky jump fix stays.
2. Awareness color locked to deeper wine red `#92293a` / ink `#6a1e2b`, sibling to hypertension’s brighter `#c0242b` / `#8a1a1f`.
3. Still `noindex`; publish checklist remains owner-gated.

### 2026-08-12 · Hyperlipidemia Phase 4 HTML built under noindex

1. Built `intervention-maps/hyperlipidemia.html` + seven topic pages from frozen public-copy.
2. All pages `noindex`; not on Intervention Maps index or `sitemap.xml`.
3. Awareness color remains owner-gated. Temporary ink-family tokens in `sketch.css` only so pages do not inherit ADHD-orange fallbacks; not a ribbon/theme lock.
4. Next: owner color lock, then publish checklist.

### 2026-08-12 · Hyperlipidemia Phase 4 language frozen

1. Owner completed revise-then-freeze gate on `public-copy/` (no Phase 3 / object reopen).
2. Translated Other TG and hub “narrow / phenotype-cautious / not-first” into ordinary reader language.
3. Neutralized Popular Supplements guideline sentence; kept “Inclusion here is honesty after looking, not endorsement.”
4. Participation/safety source-check retained package-supported details and trimmed unsupported peripheral monitoring checklist items (see campaign CHANGELOG).
5. Phase 4 charter, outline, and public-copy **language frozen**. Next: HTML / theme under `noindex`; awareness color still deferred.

### 2026-08-12 · Hyperlipidemia Phase 3 approved and frozen; Phase 4 public-copy drafted

1. Owner **approved Phase 3 as drafted** (no architecture revision before Phase 4).
2. Architecture locked: **one hub + seven topic pages**. A / A′ / A″ / B / C / D / E remain internal only (primes are parallel hard-outcome placements, not demotions). No primary/secondary or LDL/TG sub-hubs.
3. Landscape grammar locked: lipid-panel change ≠ hard cardiovascular outcomes. Cross-link / non-collapse locks preserved for Phase 4.
4. Awareness color remains deferred (does not block copy architecture).
5. Phase 4 opened under `drafts/hyperlipidemia/`: reader charter, outline, and `public-copy/` (hub + seven topics) **drafted · awaiting owner language review**. No HTML / sketch.css / sitemap yet.
6. Library stays at 11; objects stay at 7; §12s unchanged.

### 2026-08-12 · Hyperlipidemia Phase 2 frozen; object freeze complete; Phase 3 drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Phase 2 Thinking Artifacts **frozen as drafted** (Frozen v1.0) for all seven objects. Status line only; §12 and other artifact content unchanged.  
2. Object freeze **complete** (Phase 1 + 2 pairs for all seven). Freeze register updated.  
3. Phase 3 Evidence Landscape **drafted** at [`../drafts/hyperlipidemia/hyperlipidemia-evidence-landscape-phase3-v0.1.md`](../drafts/hyperlipidemia/hyperlipidemia-evidence-landscape-phase3-v0.1.md). Status: Phase 3 drafted · awaiting owner approval · August 12, 2026.  
4. Architecture finding argued: **one hyperlipidemia hub + seven topic pages**. Do not split hubs by primary/secondary prevention or LDL-only vs TG-only labels.  
5. Claim ladder bands (internal letters only; prefer bands/roles over tiers): **A** statins · **A′** non-statin LDL medicines · **A″** icosapent ethyl · **B** eating patterns (three lines) · **C** plant sterols · **D** other TG medicines · **E** popular supplements. A′ and A″ are parallel hard-outcome placements, not ordinal demotions.  
6. Library membership remains **11**. Object index remains **7**. Membership gates stay closed.

**Open:** Owner approval of Phase 3. No Phase 4 until approved.

---

### 2026-08-12 · Hyperlipidemia Phase 1 frozen; Phase 2 Thinking Artifacts drafted (7/7)

**Participants:** Owner + Cursor.

**Decisions:**

1. Phase 1 Evidence Stability Checks **frozen as drafted** (Frozen v1.0) for all seven objects. §12 wording unchanged.  
2. Phase 2 Thinking Artifacts **drafted** for all seven objects (`thinking-artifact-v0.1.md` in each folder). Status: Drafted · awaiting owner freeze · August 12, 2026.  
3. Each artifact carries that object's Stability Check §12 **verbatim**.  
4. Library membership remains **11**. Object index remains **7**. Fiber / other-TG / popular-supplements membership gates stay closed.  
5. Freeze register, workflow, README, CHANGELOG, and proposals README updated to match.

**Open:** Owner freeze of Phase 2 artifacts, then object freeze (Phase 1 + 2 pairs) into the freeze register, then Phase 3.

---

### 2026-08-12 · Hyperlipidemia Phase 1 Stability Checks drafted (7/7)

**Participants:** Owner + Cursor.

**Decisions:**

1. Object index remained **accepted as revised** (seven objects).  
2. Phase 1 Evidence Stability Checks **drafted** for all seven objects. Status: Drafted · awaiting owner freeze of §12 · August 12, 2026.  
3. Membership gates closed: soluble fiber stays a diet branch (no C/split proposal); other TG medicines and popular supplements calibrated with labeled working evidence (no seated C/D). Library stays at **11**.  
4. No Phase 2 artifacts yet. No claims frozen.

**Open:** Owner freeze (or revise) of each §12, then Phase 2 Thinking Artifacts.

---

### 2026-08-12 · Hyperlipidemia object index revised to 7 and accepted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner refused the six-object index unchanged. Core logic held; two targeted revisions required.  
2. **Soluble/viscous fiber restored** inside the diet object as a mandatory named internal branch with a Phase 1 working-evidence Stability Check. Portfolio’s viscous-fiber *component* is not the fiber-alone reader decision. Not a separate fiber object unless Phase 1 later forces a split. Diet object retitled: Eating patterns, saturated fat, and soluble fiber.  
3. **Seventh object added:** Other triglyceride-lowering medicines (`other-triglyceride-medicines`). Fibrates are the mandatory starting branch. Niacin and other prescription omega-3 formulations examined as appropriate. No dedicated Phase 0 C/D; library membership ≠ object existence (same test that opened popular supplements). Narrow placement after Phase 1 is allowed.  
4. **Icosapent ethyl remains separate.** REDUCE-IT fence must not be dumped into a general TG-drug bucket.  
5. Exercise, weight, Lp(a) drugs, FH/apheresis, and primary/secondary-as-objects stay context/gaps as proposed. Statin intolerance stays context inside non-statin LDL medicines.  
6. Index accepted as revised. Seven folders opened. Phase 1 unlocked. Library stays at **11**.

**Open:** Phase 1 Evidence Stability Checks for all seven objects.

---

### 2026-08-12 · Hyperlipidemia Phase 0 frozen at 11; object index proposed

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted Phase 0 at **11 sources** as drafted. Minimal did not become narrow: SOC triad, statin/LDL events spine, non-statin outcomes, diet at surrogate and event levels, plant sterols, PCSK9, bempedoic/statin-intolerance, purified-EPA story all seated.  
2. Gaps stay gaps (RYR, berberine, OTC fish oil, algae analogue, garlic/turmeric-class, exercise, fibrates/niacin, Lp(a) drugs, FH/apheresis). Working evidence later if objects demand.  
3. STRENGTH remains companion to D3 (not a twelfth seat). Lipid change ≠ hard outcomes stays structural.  
4. Citation log locked.  
5. Object index proposed: [`../drafts/hyperlipidemia/proposals/2026-08-12-object-index-proposal.md`](../drafts/hyperlipidemia/proposals/2026-08-12-object-index-proposal.md) (six objects). Folders not opened until acceptance.

**Open:** Owner acceptance of the object index, then Phase 1.

---

### 2026-08-12 · Hyperlipidemia Step 0 frozen; scaffold + Phase 0 library drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Hyperlipidemia Step 0 brief **owner-approved and frozen as drafted** (no changes).  
2. Step 1 scaffold complete under `drafts/hyperlipidemia/` (README, citation log, workflow, freeze-register header, proposals, empty objects).  
3. Phase 0 minimal library **drafted** (11 sources) from a currentness-first search through 12 August 2026: [`../drafts/hyperlipidemia/hyperlipidemia-evidence-library-v0.1.md`](../drafts/hyperlipidemia/hyperlipidemia-evidence-library-v0.1.md).  
4. Seated inventory: **A1–A3** (2026 ACC/AHA; 2025 ESC/EAS Focused Update; NICE NG238) · **B1** (Khan 2022 ezetimibe/PCSK9 NMA) · **C1–C4** (CTT 2010; Chiavaroli Portfolio; Hooper saturated fat; Ras plant sterols) · **D1–D3** (FOURIER; CLEAR Outcomes; REDUCE-IT with STRENGTH companion).  
5. Explicit gaps preserved: RYR, berberine, OTC fish oil, algae-oil analogue (no claim transfer), garlic/turmeric-class products, exercise-as-lipid-first C, fibrates/niacin routine add-on, Lp(a)-lowering drugs, FH/apheresis specialty pathways.  
6. No objects opened. No architecture. No claims frozen.  
7. Hypertension publish checklist and Pain post-condition checkpoints remain open and remain not gates.

**Open:** Owner acceptance of the 11-source Phase 0 library, then object-index proposal.

---

### 2026-08-12 · Hyperlipidemia Step 0 opened

**Participants:** Owner + Cursor.

**Decisions:**

1. Hypertension Phase 4 remains **complete pre-publish** (theme locked; `noindex`; sitemap/index deferred). That publish checklist is owner-gated and is **not** a gate on Hyperlipidemia.  
2. Hyperlipidemia is the next Metabolic-batch campaign after hypertension. Methodology remains **v1.0**.  
3. Step 0 brief drafted: [`../drafts/hyperlipidemia/hyperlipidemia-campaign-brief-v0.1.md`](../drafts/hyperlipidemia/hyperlipidemia-campaign-brief-v0.1.md).  
4. Research object is **broad clinical hyperlipidemia** as people search it (high cholesterol / lipids / dyslipidemia vocabulary), not a CVD mega-page and not a premature primary-vs-secondary or LDL-only split. Phenotype rails, familial pathways, and prevention-context architecture remain watch-list questions for Phase 0–3.  
5. Standard of care stays on the map (lifestyle foundations and lipid-lowering medicines), same Metabolic-batch stance as hypertension.  
6. Awareness color deferred to Phase 4 (heart-disease red collision with hypertension’s locked `#c0242b`). Ask the owner before CSS.  
7. Phase 0 library stays closed until the owner accepts this brief.

**Open:** Resolved same day: Step 0 approved; see freeze + Phase 0 draft entry above.

---

### 2026-08-12 · Metabolic batch opened; T2D locked; plant-based preference restated

**Participants:** Owner + Cursor.

**Decisions:**

1. Pain-batch post-condition “one process change?” checkpoints for RA, OA, and CLBP stay **open** for now. They remain not a live gate.  
2. Metabolic batch third seat is **type 2 diabetes**, not obesity. Obesity stays a separate later campaign (overlap with T2D is real; landscapes are not the same map).  
3. Metabolic batch order: **Hypertension → Hyperlipidemia → Type 2 diabetes**. Obesity follows after the batch.  
4. Plant-based preference restated for this batch and site-wide: keep including strong studies as usual; when an animal-derived intervention is on the map, also consider the plant-based analogue readers will ask about **when appropriate**. Report what was studied or that it was not. Do not invent claim transfer. Canonical rule remains [`.cursor/rules/plant-based-analogue-check.mdc`](../.cursor/rules/plant-based-analogue-check.mdc).  
5. Methodology stays **v1.0** for Metabolic (no Pain-review bump yet). Hypertension Step 0 brief drafted at `drafts/hypertension/hypertension-campaign-brief-v0.1.md`.

**Open (resolved in next entry):** Owner approval of the hypertension Step 0 brief, then scaffold + Phase 0 library.

---

### 2026-08-12 · Hypertension Step 0 frozen; Step 1 scaffold complete

**Participants:** Owner + Cursor.

**Decisions:**

1. Hypertension Step 0 brief **owner-approved and frozen as drafted** (no changes).  
2. Step 1 scaffold complete under `drafts/hypertension/` (README, empty library + citation log, workflow, freeze-register header, proposals, empty objects).  
3. No sources seated. No objects opened. No claims frozen.  
4. Pain post-condition checkpoints remain open and remain not a gate.

**Open:** Phase 0 currentness-first library draft for hypertension.

---

### 2026-08-12 · Hypertension Phase 0 library drafted (12 sources; mislabeled 13)

**Participants:** Owner + Cursor.

**Decisions / draft notes:**

1. Phase 0 minimal library drafted. Seated inventory was always A1–A3 + B1 + C1–C6 + D1–D2 = **12**; early labels incorrectly said 13.  
2. Search stayed high-bar and unbiased. Owner nutrition curiosity noted; diet/plant-based seats earned only when they survived the same pressure-test (Gibbs pattern-level certainty grades, including vegan low certainty).  
3. Popular supplements left as explicit gaps. Alcohol-reduction Cochrane kept as companion/gap (too thin for a C).  
4. No objects opened. No architecture.

**Open (resolved in next entry):** Owner acceptance after count reconciliation.

---

### 2026-08-12 · Hypertension Phase 0 frozen at 12; object index proposed

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted Phase 0 once membership count was reconciled to **12**. No source added to pad the number.  
2. Citation log locked to A1–A3, B1, C1–C6, D1–D2.  
3. Object-index proposal drafted at `drafts/hypertension/proposals/2026-08-12-object-index-proposal.md`. Folders not opened until acceptance.

**Open:** Owner acceptance of the object index, then Phase 1.

---

### 2026-08-12 · Hypertension object index accepted; Phase 1 Stability Checks drafted (7/7)

**Participants:** Owner + Cursor.

**Decisions:**

1. Object index **accepted** as written (seven objects). Folders opened under `drafts/hypertension/objects/`.  
2. Phase 1 Evidence Stability Checks **drafted** for all seven objects (`evidence-stability-check-v0.1.md` in each folder). Status: Drafted · awaiting owner freeze of §12 · August 12, 2026.  
3. Library membership remains **12**. Popular supplements calibrated with labeled working evidence; membership gate closed; no membership proposal opened.  
4. No Phase 2 artifacts yet. No §12 owner-frozen yet.

**Open (resolved in next entry):** Owner freeze (or revise) of each §12, then Phase 2 Thinking Artifacts.

---

### 2026-08-12 · Hypertension Phase 1 frozen; Phase 2 Thinking Artifacts drafted (7/7)

**Participants:** Owner + Cursor.

**Decisions:**

1. Phase 1 Evidence Stability Checks **frozen as drafted** (Frozen v1.0) for all seven objects. §12 wording unchanged.  
2. Phase 2 Thinking Artifacts **drafted** for all seven objects (`thinking-artifact-v0.1.md` in each folder). Status: Drafted · awaiting owner freeze · August 12, 2026.  
3. Each artifact carries that object's Stability Check §12 **verbatim**.  
4. Library membership remains **12**. Object index remains **7**. Popular-supplements membership gate stays closed.  
5. Freeze register, workflow, README, CHANGELOG, and proposals README updated to match.

**Open (resolved in next entry):** Owner freeze of Phase 2 artifacts, then object freeze (Phase 1 + 2 pairs) into the freeze register, then Phase 3.

---

### 2026-08-12 · Hypertension Phase 2 frozen; object freeze complete; Phase 3 drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Phase 2 Thinking Artifacts **frozen as drafted** (Frozen v1.0) for all seven objects. Status line only; §12 and other artifact content unchanged.  
2. Object freeze **complete** (Phase 1 + 2 pairs for all seven). Freeze register updated.  
3. Phase 3 Evidence Landscape **drafted** at `drafts/hypertension/hypertension-evidence-landscape-phase3-v0.1.md`. Status: Phase 3 drafted · awaiting owner approval · August 12, 2026.  
4. Architecture finding argued: **one hypertension hub + seven topic pages**. Do not split hubs by stage/threshold. Sodium ≠ salt substitutes and eating patterns ≠ weight-reducing diets stay separate topic pages.  
5. Claim ladder bands (internal letters only; prefer bands/roles over tiers): **A** antihypertensive medicines · **A′** salt substitutes (parallel hard-outcome band) · **B** eating patterns · **C** sodium reduction · **D** exercise · **E** weight-reducing diets · **F** popular supplements.  
6. Library membership remains **12**. Object index remains **7**. Popular-supplements membership gate stays closed.

**Open:** Owner approval of Phase 3. No Phase 4 until approved.

---

### 2026-08-12 · Hypertension Phase 3 approved and frozen; Phase 4 public teaching opened

**Participants:** Owner + Cursor.

**Decisions:**

1. Phase 3 Evidence Landscape **approved and frozen as drafted**. No research reopening. Library stays at **12**. Objects stay at **7**.  
2. Architecture locked: **one hub + seven topic pages**. Do not split hubs by stage or guideline threshold. Threshold/target disagreement and measurement teaching stay annotations / topic self-ID.  
3. Internal bands A / A′ / B / C / D / E / F stay internal only. Prefer bands/roles over tiers. **A′ is parallel** to medicines (hard outcomes in studied settings), not a weaker grade.  
4. Non-collapse locks preserved for Phase 4: sodium advice ≠ potassium salt substitute; eating patterns ≠ weight-reducing diets; DASH BP ≠ hard events; exercise-mode BP ranking ≠ hard outcomes.  
5. Landscape grammar locked: lowering blood pressure is not the same as proven protection from heart attack, stroke, or death.  
6. Phase 4 authorized: reader charter, page outline, and `public-copy/` drafts created under `drafts/hypertension/`. Status: Drafted · awaiting owner language review · August 12, 2026. **No HTML / sketch.css / sitemap yet.**
7. Awareness color still **deferred** (heart-disease red remains a candidate, not a hypertension-only ribbon). Ask owner before `ev--hypertension` CSS.

**Open:** Owner language review of Phase 4 charter / outline / public-copy, then HTML.

---

### 2026-08-12 · Hypertension Phase 4 public-copy frozen; HTML built (pre-publish)

**Decisions:**

1. Phase 4 public-copy **Frozen v1.0** (hub + seven topics + charter + outline) after three language edits: hub medicines precision; exercise participation sourced-only; supplements product voice.
2. HTML built: `intervention-maps/hypertension.html` + seven topic pages. `body.ev--hypertension` present; **no** `--condition` color tokens in `sketch.css` yet.
3. All eight pages carry `noindex, nofollow`. Not listed on Intervention Maps index plates. `sitemap.xml` untouched.
4. Awareness color still **deferred**. Sitemap / index / remove-noindex reserved for explicit publish step.

**Open:** Owner visual review of HTML; lock awareness color when ready; then publish checklist (sitemap, index plate, remove noindex).

---

### 2026-08-12 · Hypertension awareness color locked (pre-publish)

**Decisions:**

1. Hypertension awareness/theme family locked to **red** (AHA high-BP / World Hypertension Day ecosystem; not a hypertension-only ribbon claim).
2. Exact tokens locked (shade A): `--condition: #c0242b` · `--condition-ink: #8a1a1f` on `body.ev--hypertension`.
3. Wired in `sketch.css`; documented in `.cursor/rules/evidence-condition-awareness-colors.mdc`.
4. Pre-publish intact: `noindex, nofollow` on all eight pages; not on Intervention Maps index; not in `sitemap.xml`.

**Open:** Publish checklist when ready (remove noindex → index plate → sitemap → live verification).

---

### 2026-08-11 · Pain batch live (RA, OA, CLBP)

**Participants:** Owner + Cursor.

**Decisions:**

1. Osteoarthritis and chronic low back pain go live together, with rheumatoid arthritis’s missing sitemap entries repaired in the same pass.  
2. Removed `noindex` from OA (13) and CLBP (13). Added those URLs plus RA hub and seven topics to `sitemap.xml`.  
3. Intervention Maps index is now six live plates. Insights morph, homepage exhibit, and Library counts updated to match.  
4. Post-condition “one process change?” checkpoints for RA, OA, and CLBP remain open and are not a live gate.

**Open:** Metabolic batch start (hypertension first). Pain-batch process checkpoint.

---

### 2026-08-10 · Brain batch closed; Pain batch opened with RA

**Participants:** Owner + Cursor.

**Decisions:**

1. Brain & mental health batch is **closed for expansion** (ADHD, Depression, Anxiety). Anxiety Phase 4 pages remain built; further public polish is deferred, not a gate on Pain.  
2. Pain & musculoskeletal batch is next: **Rheumatoid arthritis → Osteoarthritis → Chronic low back pain** (fibromyalgia watch unchanged).  
3. Product stance reaffirmed for this room: educate and empower with a faithful full landscape; find where real help sits (including drug spine and home remedies / CAM), calibrated by evidence, not by shortlist or neat taxonomy.  
4. RA Step 0 brief approved; scaffold opened.  
5. **Brain batch process question:** no methodology bump named at closeout. Pain batch adopts **v1.0** unchanged. v1.1 remains reserved if a later broadly applicable change appears.  
6. RA Phase 0 minimal library drafted, pressure-tested, and **owner-accepted** as frozen v0.1 (14 sources): [`../drafts/rheumatoid-arthritis/rheumatoid-arthritis-evidence-library-v0.1.md`](../drafts/rheumatoid-arthritis/rheumatoid-arthritis-evidence-library-v0.1.md).  
7. RA Phase 4: reader charter frozen; outline language refinement locked; hub + seven topic pages built under `intervention-maps/`. Reader-first At a Glance groups; no public A–F; exercise/rehab two-rail page shipped; indigo awareness color. Sitemap updated.

**Open:** Owner review of RA public pages (then post-condition checkpoint).

---

### 2026-08-11 · RA public pages frozen; Phase 4 writing standard

**Participants:** Owner + Cursor.

**Decisions:**

1. RA hub and all seven topic pages frozen after a public-language pass. Science unchanged.  
2. RA showed that first public drafts still used Thinking Artifact vocabulary. Later conditions, starting with osteoarthritis, should write ordinary-language pages on the first pass.  
3. Adopted a Phase 4 writing rule without bumping methodology off v1.0: [`.cursor/rules/intervention-maps-public-language.mdc`](../.cursor/rules/intervention-maps-public-language.mdc). Logged in [`methodology-changelog-v0.1.md`](methodology-changelog-v0.1.md).  

**Open:** Osteoarthritis next in the Pain batch (Step 0 in a new thread). Full RA post-condition checkpoint can wait until the owner closes the campaign.

---

### 2026-08-11 · Osteoarthritis Step 0 opened

**Participants:** Owner + Cursor.

**Decisions:**

1. Osteoarthritis is the next Pain-batch campaign after RA Phase 4 freeze. Methodology remains **v1.0**.  
2. Step 0 brief drafted: [`../drafts/osteoarthritis/osteoarthritis-campaign-brief-v0.1.md`](../drafts/osteoarthritis/osteoarthritis-campaign-brief-v0.1.md).  
3. Research object is **broad clinical OA**, not a knee-only split and not a generic “arthritis” page. Joint-site rails, surgery as a page vs a destination, and spine-OA vs chronic low back pain remain watch-list questions for Phase 0–3.  
4. Standard of care stays on the map (exercise, weight, topicals, oral medicines, injections, surgery), same Pain-batch stance as RA. No assumed disease-modifying drug spine.  
5. Awareness color is unsettled (generic arthritis blue vs Arthritis Foundation green heart vs no OA-owned ribbon). Defer to Phase 4; ask the owner before CSS.  
6. Phase 0 library stays closed until the owner accepts this brief.

**Open:** Owner approval of the OA Step 0 brief, then Step 1 scaffold. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · Osteoarthritis Step 0 approved; Phase 0 library drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner approved the OA Step 0 brief. Awareness-color wording corrected so Step 0 is not described as a source investigation. Research discipline recorded: joint-site metadata; symptom vs structure; surgery on the map; currentness through August 2026. No added architecture, exclusions, or object families.  
2. Step 1 scaffold opened under `drafts/osteoarthritis/`.  
3. Phase 0 library drafted (18 sources) from a currentness-first search: [`../drafts/osteoarthritis/osteoarthritis-evidence-library-v0.1.md`](../drafts/osteoarthritis/osteoarthritis-evidence-library-v0.1.md). Knee and hip exercise kept as separate Cochranes. STEP 9 seated; Shahid 2025 weight NMA does not include it. Hall 2025 hip VLCD RCT is a companion (knee weight findings do not automatically transfer).  
4. Methodology remains **v1.0**.

**Open (resolved in next entry):** Owner acceptance of the 18-source library, then object-index proposal. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · Osteoarthritis Phase 0 frozen at 19; object index proposed

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted Phase 0 conceptually but required one membership correction: add Frydendal et al., *NEJM* 2024 (D4; total hip replacement vs resistance training in people aged 50+ with severe hip OA already indicated for surgery). D3 cannot carry hip. Surgery follows the same site discipline as C1/C2.  
2. Permanent library is **19 sources**. Frozen as canonical v0.1.  
3. Explicit gap #1 (hip arthroplasty vs continued nonsurgical care) is closed. Joint replacement now sits on D3, D4, and A2.  
4. Do not add the July 2026 lorecivivint meta-analysis or the 2025 curcumin SR/MA to the library. Those are object-index problems. PRP and stem cells stay uncollapsed.  
5. Object index proposed: [`../drafts/osteoarthritis/proposals/2026-08-11-object-index-proposal.md`](../drafts/osteoarthritis/proposals/2026-08-11-object-index-proposal.md). Folders not opened until the owner accepts the index.  
6. Methodology remains **v1.0**.

**Open (resolved in next entry):** Owner acceptance of the object index, then Phase 1 Stability Checks. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · Osteoarthritis object index accepted; Phase 1+2 drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted the twelve-object index as-is.  
2. Folders opened. Phase 1 Stability Checks and Phase 2 Thinking Artifacts drafted for all twelve objects.  
3. Knee/hip non-collapse held for exercise and for joint replacement. PRP and stem cells uncollapsed.  
4. Curcumin and possible DMOADs membership gates closed. Library stays at 19. da Costa, Hall 2025, and Zeng 2024 remain companions.  
5. Methodology remains **v1.0**.

**Open (resolved in next entry):** Owner freeze of the twelve §12 claims, then Phase 3 landscape. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · Osteoarthritis objects frozen; Phase 3 drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Nine §12 claims frozen as written.  
2. Three wording corrections before freeze: glucosamine/chondroitin (C8 does not carry chondroitin); stem cells (structure not established, not “was not shown”); IA corticosteroids (greatest / smaller / no clear benefit at 26 weeks).  
3. All twelve objects Frozen v1.0. No membership changes. Library stays at 19.  
4. Phase 3 landscape drafted: one hub, twelve topic pages, no DMOAD spine, knee/hip as rails not separate hubs.  
5. Methodology remains **v1.0**.

**Open (resolved in next entry):** Owner approval of Phase 3, then Phase 4. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · Osteoarthritis Phase 3 frozen; Phase 4 opened

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner approved Phase 3 with two calibration edits. Architecture unchanged: one hub, twelve topic pages, site differences as rails and annotations, no DMOAD spine.  
2. Weight A′ wording softened: C3’s ~7% figure is a meta-regression signal that pain relief may be anticipated around ≥7% loss, not an individual prescription or hard threshold.  
3. Prime letters (A/A′, D/D′, G/G′) defined as parallel landscape-band placements, not ordinal subtiers. G′ is not a worse G.  
4. Hub “visible core” shorthand stays; Phase 4 must not turn it into “everyone with OA should lose weight.”  
5. No new research, sources, objects, or architecture. Objects remain frozen.  
6. Phase 4 opened: reader charter and page outline. Awareness color still unsettled; ask before CSS. Methodology remains **v1.0**.

**Open (resolved in next entry):** Owner review of Phase 4 charter and outline; awareness color before HTML theme. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · Osteoarthritis awareness green locked; hub drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted the Phase 4 reader charter and outline.  
2. OA theme: restrained arthritis green `#007636`, derived from Arthritis Foundation Green `#00AD50` (Green Heart / PMS 2257) and darkened for contrast. This is the site's OA identity, not a claim of an official OA-specific green ribbon. RA remains indigo/gold. Depression keeps its separate mental-health green.  
3. First public-language hub drafted at `intervention-maps/osteoarthritis.html`. `noindex`. Not added to the Intervention Maps index. Twelve topic pages not started pending hub review.  
4. Methodology remains **v1.0**.

**Open (resolved in next entry):** Owner review of the OA hub HTML. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · Osteoarthritis hub frozen; exercise and weight drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Hub accepted as the Phase 4 public-language reference after landscape recomposition (no rank column) and copy edits.  
2. Stem-cell hub preview aligned to pain and function at low certainty. Creams/pills hub line left short; topic page will use “stomach, kidney, and heart risks.”  
3. Topic pages started with exercise (knee/hip split; recommendation ≠ average size) and weight management (when relevant; meta-regression not a personal threshold; hip non-transfer).  
4. Remaining ten topic pages still to write. Not live: `noindex`, not on the series index, not in the sitemap. Methodology remains **v1.0**.

**Open:** Remaining OA topic pages. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · OA topic grammar locked; creams and four injections drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Exercise and weight approved as the Phase 4 topic-page model after public-writing fidelity fixes. No object reopen. No new research.  
2. Exercise fixes: hip placebo sentence (“evidence for pain relief becomes less clear”); structured repeated programs vs one-time “exercise more”; land-based examples (walking, strength, cycling, mixed).  
3. Weight fixes: STEP 9 compared semaglutide plus counseling with placebo plus the same counseling; participation grounded in the studies, not “a real plan.”  
4. Creams/pills and four injection topic pages drafted (`noindex`). Next: glucosamine/chondroitin, curcumin, possible disease-modifying drugs, arthroscopy, joint replacement.  
5. Methodology remains **v1.0**.

**Open:** Remaining five OA topic pages. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · OA creams and four injections frozen; final five drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Creams/pills and four injection pages frozen as public copy after specified wording fixes. No object reopen. No new research.  
2. Injection architecture survived translation: steroid clock + repeated-use structure; HA large-trial placebo result + guideline conflict; PRP vs-placebo signal + guideline conflict + product heterogeneity; stem cells slight low-certainty symptoms + unestablished regeneration.  
3. Final five topic pages drafted: glucosamine/chondroitin (IPD null does not carry chondroitin); curcumin kept short; possible disease-modifying drugs taught as concept-then-finding, not a spine; arthroscopy short negative; joint replacement already-indicated first with knee/hip split.  
4. Methodology remains **v1.0**. Still `noindex`; not on the series index; not in the sitemap.

**Open:** Owner review of the final five OA topic pages. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · OA public-copy layer closed

**Participants:** Owner + Cursor.

**Decisions:**

1. Final five topic pages frozen as public copy after specified wording/source-boundary fixes. No object reopen. No new research.  
2. Glucosamine: symptom IPD does not imply a structural null; analogue language is fermented/non-shellfish. Curcumin frozen as written.  
3. Possible DMOADs: sprifermin remains a named internal branch only; no bibliographic source in the frozen package, so the public paragraph was removed rather than cited. RA-medicine sentence rewritten as an evidence claim.  
4. Arthroscopy and joint replacement frozen after one wording change each.  
5. Public-copy layer closed. Hub plus twelve topic pages frozen. Still `noindex`; not on the series index; not in the sitemap until live checklist. Methodology remains **v1.0**.

**Open:** Live checklist when the owner is ready to publish. RA post-condition checkpoint still deferred.

---

### 2026-08-11 · Chronic low back pain Step 0 opened

**Participants:** Owner + Cursor.

**Decisions:**

1. Chronic low back pain is the next Pain-batch campaign after OA public-copy freeze. Methodology remains **v1.0**.  
2. OA live/publish checklist and RA post-condition checkpoint remain owner-gated and are not gates on CLBP Step 0.  
3. Step 0 brief drafted: [`../drafts/chronic-low-back-pain/chronic-low-back-pain-campaign-brief-v0.1.md`](../drafts/chronic-low-back-pain/chronic-low-back-pain-campaign-brief-v0.1.md).  
4. Research object is **broad clinical chronic low back pain**, not a nonspecific-only split, not sciatica-only, and not a generic “spine” page. Phenotype rails, surgery as a page vs a destination, and spine-OA vs OA overlap remain watch-list questions for Phase 0–3.  
5. Standard of care stays on the map (education, remaining active, exercise/rehab, medicines, injections, surgery), same Pain-batch stance as RA and OA.  
6. Awareness color is unsettled (U.S. Pain Foundation blue vs retailer purple vs no CLBP-owned ribbon). Defer to Phase 4; ask the owner before CSS.  
7. Phase 0 library stays closed until the owner accepts this brief.

**Open:** Owner approval of the CLBP Step 0 brief, then Step 1 scaffold.

---

### 2026-08-11 · Chronic low back pain Step 0 approved; Phase 0 library drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner approved the CLBP Step 0 brief as written. Frozen. No added architecture, exclusions, or object families.  
2. Awareness-color note corrected on approval: no authoritative CLBP-specific ribbon. Teal remains a Phase 4 candidate. Teal, blue, purple, and other colors appear across pain/back-pain sources with inconsistent authority. Final color is a design decision, not a claim of an official ribbon.  
3. Research discipline confirmed: broad clinical CLBP first, phenotype-aware throughout; surgery and injections stay inside the landscape; symptom/function vs structural or regenerative claims; likely-object table stays provisional.  
4. Step 1 scaffold opened under `drafts/chronic-low-back-pain/`.  
5. Phase 0 library drafted (16 sources) from a currentness-first search through 11 August 2026: [`../drafts/chronic-low-back-pain/chronic-low-back-pain-evidence-library-v0.1.md`](../drafts/chronic-low-back-pain/chronic-low-back-pain-evidence-library-v0.1.md). NICE NG59 (July 2026 psych withdrawal) seated with WHO 2023 and VA/DoD 2022. Phenotype seats preserved for epidural/disc surgery (radicular), stenosis, and radiofrequency. SPORT disc RCT seated as D1.  
6. Methodology remains **v1.0**.

**Open:** Superseded the same day: owner refused 16 unchanged; see freeze entry below.

---

### 2026-08-11 · Chronic low back pain Phase 0 frozen at 17; object index proposed

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner refused to freeze the 16-source draft unchanged. Architecture was strong; SCS as explicit gap #1 failed the library’s own pressure-test and the desperate-reader / Step 0 device-in-scope rule.  
2. **C10 added:** Traeger AC, Gilbert SE, Harris IA, Maher CG. Spinal cord stimulation for low back pain. Cochrane Database Syst Rev. 2023;(3):CD014789. Search to 10 June 2022; 13 RCTs, 699 participants; moderate-certainty no meaningful benefit vs placebo at six months. Unique placebo-controlled warrant no other seat carries.  
3. SOLIS 2025 (North et al., *Reg Anesth Pain Med*; NCT04676022) and Eldabe 2026 chronic-pain NMA stay **companions** for the Phase 1 currentness check. Not stacked as seats 18–19.  
4. Zaina 2016 kept. A1–A3 not reopened. ACP/NASS not added. Regenerative-injection 2024 MA not seated. Dedicated acupuncture/massage/TENS/yoga/supplement reviews not forced into Phase 0.  
5. Phase 0 frozen at **17 sources**.  
6. Object index first proposed at ten objects. Folders not opened.

**Open:** Superseded the same day: owner refused ten unchanged; see twelve-object revision below.

---

### 2026-08-11 · Chronic low back pain object index revised to 12

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner refused the ten-object index. Library-membership test and object-existence test are different tests. A therapy can fail to earn a permanent C and still require investigation.  
2. **Added:** regenerative / intradiscal therapies as an investigated object without a seated C. Schol 2024 and any stronger/current RCT syntheses found in Phase 1 are working evidence. Pain/function ≠ disc regeneration. “Insufficient evidence” is an allowed result after examination, not a reason to skip the object.  
3. **Split:** multidisciplinary / combined rehabilitation is its own object. Psychological therapies remain one object for CBT/ACT/pain education. Combined rehab is not a subtype of talking therapy. B2, C2, and Kamper 2014 (working) calibrate it.  
4. Fusion for nonspecific CLBP stays a Phase 3 / watch-list question. A1’s “RCT only” is an evidence conclusion, not a conceptual exclusion from the landscape.  
5. Supplements/herbs, TENS/traction/belts/massage remain watch items. Do not manufacture objects for symmetry with OA or other Intervention Maps pages.  
6. Revised index: [`../drafts/chronic-low-back-pain/proposals/2026-08-11-object-index-proposal.md`](../drafts/chronic-low-back-pain/proposals/2026-08-11-object-index-proposal.md). Twelve objects. Folders not opened. Phase 1 not started.

**Open:** Owner acceptance of the twelve-object index, then Phase 1. RA post-condition checkpoint and OA live checklist still deferred.

---

### 2026-08-11 · Chronic low back pain object index accepted; Phase 1 drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted the twelve-object index as revised. Conceptual safeguards locked: library membership ≠ object existence; multidisciplinary rehab is a combination intervention, not a psych subtype; regenerative therapies can earn “insufficient evidence” only after investigation; phenotype boundaries intact; fusion remains unresolved rather than quietly excluded.  
2. Twelve folders opened. Library remains frozen at 17. No architecture decisions.  
3. Phase 1 Evidence Stability Checks drafted for all twelve objects. Regenerative membership gate closed (Schol 2024 plus later RCT syntheses remain working evidence; not C11). Acupuncture membership gate closed (Mu 2020 remains working evidence).  
4. Phase 2 blocked until owner freezes §12 claims.

**Open:** Owner pressure-test of Phase 1 §12 claims, then Phase 2. RA post-condition checkpoint and OA live checklist still deferred.

---

### 2026-08-11 · Chronic low back pain Phase 1 frozen; Phase 2 drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted Phase 1 subject to two wording corrections. No further Phase 1 review round. Library stayed at 17. Object index stayed at 12. Source universe not reopened. No architecture.  
2. **MBR:** Remove implied interaction. C2 supports the narrower claim that clinically important effects clustered in psychological-intervention + physiotherapy nodes. Do not say talking therapies “work better with physiotherapy than in isolation.” Do not turn that pattern into a demonstrated synergy.  
3. **SCS:** Correct the §12 denominator. C10 contains 13 trials / 699 participants overall. The moderate-certainty six-month placebo-controlled null comes from one trial (Hara 2022, n=50). Do not attach 13/699 directly to that six-month estimate. SOLIS/Eldabe remain companions; newer does not mean better controlled.  
4. Regenerative wording preserved as insufficient evidence that these therapies regenerate discs, not evidence that regeneration has been disproven. The other ten Stability Checks frozen as written.  
5. Twelve Phase 2 Thinking Artifacts drafted, carrying frozen §12 sentences verbatim.

**Open:** Owner pressure-test of Phase 2 artifacts, then object freeze and Phase 3. RA post-condition checkpoint and OA live checklist still deferred.

---

### 2026-08-11 · Chronic low back pain Phase 2 frozen; Phase 3 drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted Phase 2 subject to one wording correction. No Phase 1 reopen. Library stayed at 17. Object index stayed at 12. §12 claims unchanged.  
2. **Spinal manipulation artifact:** working question now says NICE places SMT only within a package including exercise, rather than an unqualified “allowed only inside an exercise package.” Intellectual-shape shorthand “package-with-exercise” retained; Orientation already attributed the rule to A1.  
3. All twelve Thinking Artifacts frozen. Object freeze complete. Individual-object research finished.  
4. Phase 3 comparative landscape drafted: claim ladder with internal tiers A–J (A′ multidisciplinary parallel to exercise; I′ stenosis parallel to disc surgery); one hub + twelve topic pages; hard phenotype routing; fusion and other non-objects kept as watch/hub annotations. Architecture finally decided here, not earlier.

**Open:** Owner pressure-test of Phase 3 (ladder, one-hub finding, phenotype routing, watch list), then Phase 4. RA post-condition checkpoint and OA live checklist still deferred.

---

### 2026-08-11 · Chronic low back pain Phase 3 frozen; Phase 4 opened

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted Phase 3 subject to three architecture corrections. Band placements A–J with A′/I′ parallel unchanged. No objects, sources, or §12s reopened.  
2. **One-hub rationale revised:** Keep one CLBP hub + twelve topic pages because the reader enters through one broad decision problem, while the frozen evidence supports phenotype-specific destinations and care-context locks rather than three independently calibrated treatment landscapes. Do not justify unity by saying conservative evidence is largely shared or that separate hubs would merely duplicate exercise framing. C1 cannot simply export to stenosis or acute sciatica.  
3. **Phenotype + care-context routing:** Radicular pain and stenosis are phenotype locks. RF is a selected suspected-generator pathway. SCS is persistent/refractory implant consideration. “Refractory device” is not a phenotype.  
4. **Direct-entry rule frozen:** Phenotype- or context-restricted topic pages must identify that restriction in title/subtitle/first screen. Hub routing alone is not enough.  
5. Prefer “bands/roles” over “tiers” in later drafts to reduce report-card leakage. Letters stay internal.  
6. Phase 4 reader charter and page outline drafted.

**Open:** Owner pressure-test of Phase 4 charter/outline, then public HTML. RA post-condition checkpoint and OA live checklist still deferred.

---

### 2026-08-11 · Chronic low back pain Phase 4 charter frozen; public copy drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner accepted Phase 4 charter/outline subject to four production corrections plus a “who it may fit” guardrail. No science or architecture reopen.  
2. Hub disease-modification sentence: most treatments studied for pain/function/day-to-day life; no established reliable disc rebuild or disease-modifying treatment; no RA comparator in the public lede.  
3. Public titles: RF = when a specific source of back pain is suspected; regenerative page title = PRP and stem-cell-type intradiscal injections; SCS prefers “hard-to-treat” over “refractory.”  
4. Fusion annotation rewritten without “evidence seat.”  
5. Safety-context slot added after how-to-use; campaign red-flag categories (fracture, infection, malignancy, cauda equina) reserved without inventing a detailed checklist in the outline.  
6. “Who it may fit” means studied population/clinical context, not individualized candidacy.  
7. Public-copy drafts written under `drafts/chronic-low-back-pain/public-copy/` for language review before HTML.

**Open:** Owner language review of public copy, then HTML. RA post-condition checkpoint and OA live checklist still deferred.

---

### 2026-08-11 · Chronic low back pain color locked; HTML drafted

**Participants:** Owner + Cursor.

**Decisions:**

1. Owner locked CLBP accent **C**: `#1a6b78` / ink `#134e58` (slate-teal). Ranking C > D > E. Same broad teal family as Anxiety (`#0f766e`), deliberately different shade. Design identity only; not an official CLBP ribbon claim.  
2. `ev--chronic-low-back-pain` added to `intervention-maps/sketch.css`; awareness-colors rule updated; Intervention Maps CSS cache key bumped.  
3. Hub + twelve topic pages drafted under `intervention-maps/chronic-low-back-pain*.html` from frozen public copy. `noindex`. Not added to sitemap or Intervention Maps index (same gate as OA).  
4. Generator: `scripts/build-clbp-html.py`.

**Open:** Owner HTML review, then live promote when ready. RA post-condition checkpoint and OA live checklist still deferred.

---

### 2026-07-18 · Expansion philosophy and queue

**Participants:** Owner + GPT planning pass; logged into Evidence product docs for continuity with Cursor agents.

**Decisions:**

1. Expand beyond ADHD/depression into other common **decision-rich** chronic conditions.  
2. Prioritize by crowded competing interventions + search uncertainty, not prevalence alone.  
3. Split broad umbrellas (CVD, arthritis) into distinct landscapes when evidence shows different maps.  
4. Include rheumatoid arthritis in the near queue (owner interest + strong fit).  
5. Treat the product as maps of interventions inside a condition doorway.  
6. Create this living roadmap + a new-condition playbook so the next dozen campaigns reuse one system.

**Open questions (do not invent answers):**

- How obesity Evidence pages relate to the Emerging Therapies peptide studio (separate products; need a boundary note when obesity starts).  
- Whether site navigation ships as the family table above or a flatter condition index first.  
- Which metabolic third seat (T2D vs obesity) when that batch starts.

---

### 2026-07-18 · Depression Phase 4 locked

**Participants:** Owner + Cursor closeout.

**Decisions:**

1. Owner approved Depression Phase 4: hub + all 11 topic pages.  
2. Closeout checklist A–D complete; product readiness remains deferred.  
3. Depression gate cleared: new condition campaigns may start.  
4. Science freeze unchanged; public copy must not exceed §12.

**Record:** `../drafts/depression/proposals/2026-07-18-phase4-public-approval.md`

---

### 2026-07-18 · Anxiety first; research-first scoping; batching

**Participants:** Owner + GPT planning pass; Cursor implements Step 0 + system docs.

**Decisions:**

1. Next campaign is **Anxiety disorders** (Brain & Mental Health batch closeout).  
2. **Research object ≠ presentation.** Step 0 defines the decision problem and starting research object only. Reader architecture (branches, separate hubs) waits for Phase 2/3.  
3. Do not pre-exclude diagnoses (e.g. OCD, PTSD) for neatness. Synthesis may later branch, annotate, or split campaigns when the landscape is substantially different, rare, or lacks useful data.  
4. Batching: Brain (ADHD, Depression, Anxiety) → Pain (RA, OA, chronic LBP) → Metabolic (hypertension, hyperlipidemia, T2D or obesity). Owner decides remaining order after those batches.  
5. Methodology **v1.0** frozen through Anxiety. After the Brain batch, ask the one-process-change question; bump only if broadly applicable ([`methodology-changelog-v0.1.md`](methodology-changelog-v0.1.md)).  
6. Playbook Step 0 rewritten so agents do not lock hub/branch IA before research.

**Active artifact:** [`../drafts/anxiety/anxiety-campaign-brief-v0.1.md`](../drafts/anxiety/anxiety-campaign-brief-v0.1.md) (Step 0 owner-approved).

---

### 2026-07-18 · Population scope correction before Anxiety Step 1

**Decision:** “Begin with adult and pediatric evidence” was an ADHD-derived example, not a universal rule. New campaigns begin with the broad clinical population appropriate to the condition. Age-specific evidence enters when common, decision-relevant, or map-changing; synthesis decides whether age rails are warranted. This corrects new expansion scaffolding without changing methodology v1.0.

---

### 2026-07-18 · Anxiety Phase 0 minimal library drafted

**What happened:** Built and pressure-tested the Anxiety minimal library to **16 sources** and verified citations.

- **SOC (4):** NICE CG113 (GAD + panic), NICE CG159 (social anxiety), Katzman 2014 (cross-disorder + special populations), WFSBP v3 Part I 2023 (international).  
- **Transdiagnostic (2):** Cuijpers 2016 (waitlist inflation), Carpenter 2018 (placebo-controlled, exposure signal).  
- **Disorder/domain (8):** Papola 2024 (GAD psychotherapies), Mayo-Wilson 2014 (social anxiety psych + drug), Papola 2022 (panic psychotherapies), Tam 2026 (exercise), Haller 2021 (mindfulness/acceptance), Zhang 2022 (herbal NMA), Pauley 2023 (digital CBT), Pittler & Ernst 2003 (kava safety).  
- **Landmark (1):** Hoge 2023 TAME (MBSR noninferior to escitalopram).  
- **Comparator (1):** Slee 2019 (GAD drug NMA).

**Observations for the batch review (not acted on now):** the three core disorders share one psychotherapy + medication + lifestyle spine, which suggests one hub with disorder annotations rather than three hubs. This is a hypothesis for Phase 2/3, not a locked architecture. Nine explicit gaps recorded (diet, probiotics, acupuncture, CBD, breathing-only, panic/social drug NMAs, pediatric rail, specific phobia, OCD/PTSD boundary).

**Gate:** Awaiting owner acceptance of the library, then a proposed object index. Methodology v1.0 unchanged.

**Records:** [`../drafts/anxiety/anxiety-evidence-library-v0.1.md`](../drafts/anxiety/anxiety-evidence-library-v0.1.md) · [`../drafts/anxiety/citation-log-v0.1.md`](../drafts/anxiety/citation-log-v0.1.md)

---

### 2026-07-18 · Anxiety Phase 0 accepted; object index proposed

**Decisions:**

1. Owner accepted the 16-source Phase 0 library as drafted.  
2. Do not promote or split interventions on familiarity or popularity before the object phase. Ashwagandha stays inside Zhang 2022 (C6).  
3. During the herbal object's Stability Check, compare against [`therapy-profiles/ashwagandha.html`](../therapy-profiles/ashwagandha.html). Promote to a standalone Anxiety object only if the evidence earns a distinct decision placement; otherwise keep as a named herbal branch and cross-reference the TT page.  
4. Object index proposed (five objects + medication comparator): psychotherapy-and-acute-choice; exercise; mindfulness-and-acceptance; herbal-and-nutraceutical; digital-cbt. Awaiting owner acceptance before folders open or Phase 1 begins.

**Record:** [`../drafts/anxiety/proposals/2026-07-18-object-index-proposal.md`](../drafts/anxiety/proposals/2026-07-18-object-index-proposal.md)

---

### 2026-07-18 · Anxiety object index accepted; Phase 1 opened

**Decisions:**

1. Owner accepted the five-object structure: Psychotherapy choices, Exercise, Mindfulness and acceptance, Herbal and nutraceutical, and Digital CBT.  
2. Medication remains comparator only; psychotherapy subtypes and exercise modalities remain internal branches.  
3. Herbs remain one object with the accepted ashwagandha promotion gate.  
4. “Psychotherapy choices” is the simpler display title; `psychotherapy-and-acute-choice` remains the stable folder slug.  
5. Five Phase 1 Evidence Stability Checks opened. No claims are frozen.

**Record:** [`../drafts/anxiety/anxiety-thinking-artifact-workflow-v0.1.md`](../drafts/anxiety/anxiety-thinking-artifact-workflow-v0.1.md)

---

### 2026-07-18 · Anxiety Phase 1 Stability Checks drafted

**What happened:** All five Evidence Stability Checks written as Phase 1 working artifacts. Ashwagandha promotion gate executed: not promoted; remains an internal herbal branch with TT cross-reference. No claims frozen. Awaiting owner §12 review before Phase 2.

**Records:** [`../drafts/anxiety/objects/`](../drafts/anxiety/objects/) · [`../drafts/anxiety/anxiety-thinking-artifact-workflow-v0.1.md`](../drafts/anxiety/anxiety-thinking-artifact-workflow-v0.1.md)

---

### 2026-07-18 · Anxiety Phase 1 accepted; Phase 2 opened

**Decision:** Owner accepted all five §12 strongest earned claims and moved the campaign to Phase 2. Thinking Artifacts opened for all five objects. No objects frozen; Phase 3 remains blocked.

**Record:** [`../drafts/anxiety/anxiety-thinking-artifact-workflow-v0.1.md`](../drafts/anxiety/anxiety-thinking-artifact-workflow-v0.1.md)

---

### 2026-07-18 · Anxiety Phase 2 Thinking Artifacts drafted

**What happened:** All five Thinking Artifacts drafted with one intellectual shape each and verbatim §12 claims. Freeze register still empty pending owner acceptance. Phase 3 blocked.

**Record:** [`../drafts/anxiety/objects/`](../drafts/anxiety/objects/)

---

### 2026-07-18 · Anxiety object freeze; Phase 3 opened

**Decisions:**

1. Owner accepted all five Phase 2 Thinking Artifacts. Check + artifact pairs frozen in [`../drafts/anxiety/freeze-register-v1.0.md`](../drafts/anxiety/freeze-register-v1.0.md).  
2. Phase 3 comparative calibration opened.  
3. Methodology watch item (no v1.0 change): monitor whether Phase 2 needs both a Bottom line and Belief to carry forward in addition to the intellectual shape and strongest earned claim. Revisit after Anxiety and one more condition; make endings optional in a future release only if they repeatedly become duplicative.

---

### 2026-07-18 · Anxiety Phase 3 landscape drafted

**What happened:** Drafted [`../drafts/anxiety/anxiety-evidence-landscape-phase3-v0.1.md`](../drafts/anxiety/anxiety-evidence-landscape-phase3-v0.1.md) and aligned the claim ladder to freeze-register hypotheses (Psychotherapy A; Digital CBT A′; Mindfulness B; Exercise C; Herbal/nutraceutical D). Architecture finding: one hub plus five topic pages with GAD / panic / social annotations.

---

### 2026-07-18 · Anxiety Phase 3 approved

**Decisions:**

1. Owner approved the claim ladder, relative space, boundaries, and one-hub architecture. Phase 4 planning opened.
2. No medication page and no pediatric rail are earned in this campaign.
3. The Anxiety architecture remains an evidence output, not a template. Future conditions may earn multiple hubs, medication pages, age rails, or another structure.
4. Methodology watch item (no v1.0 change): Phase 3 combines permanent evidence synthesis with workflow scaffolding. Observe through the next condition whether approval and next-step material should move to a companion document.

---

### 2026-07-18 · Anxiety Phase 4 planning opened

**What happened:** Drafted the Phase 4 reader/product charter and hub-plus-topic page outline: [`../drafts/anxiety/anxiety-page-reader-charter-phase4-v0.1.md`](../drafts/anxiety/anxiety-page-reader-charter-phase4-v0.1.md) and [`../drafts/anxiety/anxiety-page-outline-phase4-v0.1.md`](../drafts/anxiety/anxiety-page-outline-phase4-v0.1.md). One hub, five topic pages, disorder annotations rather than rails, medication as backdrop only.

---

### 2026-07-18 · Anxiety Phase 4 public pages built

**What happened:** Owner chose a teal `ev--anxiety` theme (`#0f766e`). Built `evidence/anxiety.html` and five topic pages (psychotherapy, digital CBT, mindfulness, exercise, herbal and nutraceutical), added Anxiety to `evidence/index.html`, and bumped the shared `sketch.css` cache key across all Evidence pages. No em dashes, no claims beyond frozen §12, links resolve, no lint errors. Awaiting owner review of the built pages.

---

## Pointers

| Doc | Role |
|---|---|
| [`evidence-product-charter.md`](evidence-product-charter.md) | Why the product exists |
| [`README.md`](README.md) | Current build state and Phase 4 closeout |
| [`new-condition-playbook-v0.1.md`](new-condition-playbook-v0.1.md) | How to start the next condition in a few steps |
| [`methodology-changelog-v0.1.md`](methodology-changelog-v0.1.md) | Methodology version history |
| [`../drafts/adhd/condition-evidence-methodology-v1.0.md`](../drafts/adhd/condition-evidence-methodology-v1.0.md) | Claim calibration Phases 0–4 |
| [`../drafts/type-2-diabetes/type-2-diabetes-campaign-brief-v0.1.md`](../drafts/type-2-diabetes/type-2-diabetes-campaign-brief-v0.1.md) | Type 2 diabetes Step 0 brief (owner-approved) |
| [`../drafts/type-2-diabetes/type-2-diabetes-evidence-library-v0.1.md`](../drafts/type-2-diabetes/type-2-diabetes-evidence-library-v0.1.md) | Type 2 diabetes Phase 0 library (frozen v0.1 · 13 sources) |
| [`../drafts/type-2-diabetes/proposals/2026-08-12-object-index-proposal.md`](../drafts/type-2-diabetes/proposals/2026-08-12-object-index-proposal.md) | Type 2 diabetes object index (**accepted as revised** · 6 objects · Diabetes medicines) |
| [`../drafts/type-2-diabetes/type-2-diabetes-evidence-landscape-phase3-v0.1.md`](../drafts/type-2-diabetes/type-2-diabetes-evidence-landscape-phase3-v0.1.md) | Type 2 diabetes Phase 3 landscape (**approved and frozen**) |
| [`../drafts/type-2-diabetes/type-2-diabetes-page-reader-charter-phase4-v0.1.md`](../drafts/type-2-diabetes/type-2-diabetes-page-reader-charter-phase4-v0.1.md) | Type 2 diabetes Phase 4 reader charter (**Frozen v1.0**) |
| [`../drafts/type-2-diabetes/type-2-diabetes-page-outline-phase4-v0.1.md`](../drafts/type-2-diabetes/type-2-diabetes-page-outline-phase4-v0.1.md) | Type 2 diabetes Phase 4 page outline (**Frozen v1.0**) |
| [`../drafts/type-2-diabetes/public-copy/`](../drafts/type-2-diabetes/public-copy/) | Type 2 diabetes public-copy (**Frozen v1.0**) |
| [`../intervention-maps/type-2-diabetes.html`](../intervention-maps/type-2-diabetes.html) | Type 2 diabetes hub HTML (**drafted · `noindex`**) |
| [`../drafts/chronic-low-back-pain/chronic-low-back-pain-campaign-brief-v0.1.md`](../drafts/chronic-low-back-pain/chronic-low-back-pain-campaign-brief-v0.1.md) | CLBP Step 0 brief (owner-approved) |
| [`../drafts/chronic-low-back-pain/chronic-low-back-pain-evidence-library-v0.1.md`](../drafts/chronic-low-back-pain/chronic-low-back-pain-evidence-library-v0.1.md) | CLBP Phase 0 library (frozen v0.1 · 17 sources) |
| [`../drafts/chronic-low-back-pain/chronic-low-back-pain-evidence-landscape-phase3-v0.1.md`](../drafts/chronic-low-back-pain/chronic-low-back-pain-evidence-landscape-phase3-v0.1.md) | CLBP Phase 3 landscape (**approved and frozen**) |
| [`../drafts/chronic-low-back-pain/chronic-low-back-pain-page-reader-charter-phase4-v0.1.md`](../drafts/chronic-low-back-pain/chronic-low-back-pain-page-reader-charter-phase4-v0.1.md) | CLBP Phase 4 reader charter (**frozen**) |
| [`../drafts/chronic-low-back-pain/chronic-low-back-pain-page-outline-phase4-v0.1.md`](../drafts/chronic-low-back-pain/chronic-low-back-pain-page-outline-phase4-v0.1.md) | CLBP Phase 4 page outline (**frozen**) |
| [`../drafts/chronic-low-back-pain/public-copy/`](../drafts/chronic-low-back-pain/public-copy/) | CLBP public-copy drafts (**frozen**; HTML emitted) |
| [`../intervention-maps/chronic-low-back-pain.html`](../intervention-maps/chronic-low-back-pain.html) | CLBP hub HTML (**drafted · `noindex`**) |
| [`../drafts/osteoarthritis/osteoarthritis-campaign-brief-v0.1.md`](../drafts/osteoarthritis/osteoarthritis-campaign-brief-v0.1.md) | OA Step 0 brief (owner-approved) |
| [`../drafts/osteoarthritis/osteoarthritis-evidence-library-v0.1.md`](../drafts/osteoarthritis/osteoarthritis-evidence-library-v0.1.md) | OA Phase 0 library (frozen v0.1 · 19 sources) |
| [`../drafts/osteoarthritis/proposals/2026-08-11-object-index-proposal.md`](../drafts/osteoarthritis/proposals/2026-08-11-object-index-proposal.md) | OA object index (accepted) |
| [`../drafts/osteoarthritis/osteoarthritis-evidence-landscape-phase3-v0.1.md`](../drafts/osteoarthritis/osteoarthritis-evidence-landscape-phase3-v0.1.md) | OA Phase 3 landscape (**approved and frozen**) |
| [`../drafts/osteoarthritis/osteoarthritis-page-reader-charter-phase4-v0.1.md`](../drafts/osteoarthritis/osteoarthritis-page-reader-charter-phase4-v0.1.md) | OA Phase 4 reader charter (drafted) |
| [`../drafts/osteoarthritis/osteoarthritis-page-outline-phase4-v0.1.md`](../drafts/osteoarthritis/osteoarthritis-page-outline-phase4-v0.1.md) | OA Phase 4 page outline (drafted) |
| [`../drafts/adhd/`](../drafts/adhd/) · [`../drafts/depression/`](../drafts/depression/) · [`../drafts/anxiety/`](../drafts/anxiety/) · [`../drafts/rheumatoid-arthritis/`](../drafts/rheumatoid-arthritis/) | Worked examples |
