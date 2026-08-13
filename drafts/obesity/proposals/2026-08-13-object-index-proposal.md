# Proposal: Obesity object index (post Phase 0 acceptance)

**Date:** August 13, 2026  
**Proposer:** Cursor (owner froze the 8-source library as drafted)  
**Affects:** Workflow object index · merge/split locks · folder creation  
**Library status:** 8-source Phase 0 library owner-accepted and frozen as canonical v0.1 (no membership change in this proposal)

## Recommendation

Accept the **six-object** index below. Lifestyle foundations, obesity medicines, behavioural programmes, and procedures are **on the map**, matching the obesity campaign brief. Do not invent seats for remaining watch items. Do not add green-tea Cochrane, a Garcinia review, STEP 1, SURMOUNT-1, SOS, EASO 2026, Obesity Canada 2020, or a dedicated behavioural-programme C to the library in order to open objects.

Two tests stay distinct:

- **Library membership** is the minimal permanent warrant. A therapy can fail it and still be investigated.  
- **Object existence** is whether the campaign must calibrate the decision before public framing. Step 0 put popular weak claims and behavioural services in scope. Those are investigated before they are framed.

Two objects have **no seated C**: behavioural weight-management programmes, and popular supplements / nutraceuticals. That is intentional. Phase 1 uses named working evidence. A membership proposal is allowed later only if a Stability Check cannot calibrate the object without a permanent C.

**Owner acceptance:** Accepted August 13, 2026. Six objects. Library remains frozen at 8. Behavioural programmes kept as its own object (membership ≠ existence). Phase 1 gates remain: null/insufficient permitted; promotion requires evidence.

## Owner constraints already locked

1. Same claim-calibration method as the Metabolic batch; different research-object breadth (lifestyle, medicines, surgery, and popular claims on-map). This is a **post-batch** campaign, not a fourth Metabolic-batch seat.  
2. Broad clinical obesity as people search it. BMI, waist, composition, comorbidity context, and guideline era stay claim hygiene.  
3. Weight / waist / composition change stays distinct from hard cardiovascular outcomes when the claim requires it.  
4. Durability and regain are claim hygiene, not a later editorial add-on.  
5. Plant-based analogue check when appropriate; vegetarian/Ornish-class programmes are inside C1; do not invent unstudied vegan patterns from Mediterranean evidence.  
6. Popular home remedies and supplements stay in scope for investigation; seats are earned by evidence. Dedicated supplement **library** reviews were not forced into Phase 0 for aisle completeness.  
7. Hub / topic architecture waits for Phase 3. This index locks decision objects only.  
8. SELECT stays **on this map**, inside obesity medicines. Do not export it to type 2 diabetes, and do not make SELECT its own object.  
9. Do not merge this campaign with type 2 diabetes. Dual agonists are investigable here for the obesity decision problem. T2D remission / DiRECT / SURPASS-CVOT architecture stays on that map.  
10. Do not import the Emerging Therapies peptide studio as this campaign’s object index. Overlapping molecules are expected. Investigational neighbors stay named internal watches until a Stability Check promotion gate succeeds.  
11. Guideline recommendation and quantitative warrant stay separate where they disagree (especially AACE complication-centric algorithms vs Obesity Canada GRADE drug recs vs NICE service pathway, and B1 weight ranking vs SELECT-informed MACE).

## Breadth survival check (Step 0 → objects)

Each Step 0 crowded area either earns an object, becomes explicit context, or stays a named gap.

| Step 0 crowded area | Survives as | Rationale |
|---|---|---|
| Anti-obesity medicines, including incretins and older agents | **Object:** Obesity medicines | B1 is the comparative GRADE spine. D1 preserves SELECT as an obesity-without-diabetes MACE warrant. A1–A2 carry complication-centric and GRADE sequencing. One object; named internal branches. Weight ranking ≠ MACE ranking is mandatory internal structure. |
| Eating patterns / named diets / calorie strategies | **Object:** Eating patterns | C1. Named-programme and macronutrient-pattern decision. 6-month ranking ≠ 12-month durability. Vegetarian is on the map. Not surgery. Not a shot. |
| VLCD / formula diets | **Mandatory named internal branch** of eating patterns | A3 places them. No seated C. Public shake/formula decision is real; Ge’s named-programme network is not that protocol. Split later only if Phase 1 forces it. Do not import DiRECT from the type 2 diabetes campaign. |
| Exercise | **Object:** Exercise | C2. Modest mean weight; composition, fitness, and lean-mass preservation are different jobs. Not hard events. |
| Behavioural / commercial weight-management programmes | **Object:** Behavioural weight-management programmes | No seated C. Library membership ≠ object existence. A3’s behavioural-services pathway is a different reader question from “which named diet.” Working evidence in Phase 1. |
| Metabolic / bariatric surgery | **Object:** Metabolic surgery and endoscopic procedures | C3. Long-term surgery vs short-term incretin; SAE costs. Procedure types internal. |
| Endoscopic procedures (balloons, ESG, and neighbors) | **Mandatory named internal branch** of the procedures object | C3’s finding is that endoscopic procedures are not surgery and, except ESG, were less effective than newer medicines. Not collapsed into “surgery.” Not a seventh object unless Phase 1 forces a split. |
| Popular supplements / CAM / “fat burners” | **Object:** Popular supplements | No seated C. Investigated before any “not first” public framing. |
| Investigational incretins (retatrutide, CagriSema, orforglipron, survodutide) | **Named internal watch inside obesity medicines** | B1 reports several at low or mixed certainty. Emerging Therapies studio remains the molecule-level room. Promotion only via Phase 1 gate. |
| Compounded / unregulated peptides | **Safety fence inside obesity medicines** | A2 recommends against them. Not its own object. |
| Sleep | **Not an object** | Discoverable under lifestyle / A-set teaching. |
| Pediatric / adolescent obesity | **Watch / Phase 3** | A3 includes children; this index does not pre-split IA. |
| Type 2 diabetes overlap / SELECT-as-diabetes | **Not an object on this map** | Sibling campaign. SELECT is D1 here. |
| Emerging Therapies studio as architecture | **Not objects** | Boundary, not merge. |

## Proposed object index

| Object (display) | Folder | Primary source IDs | Provisional intellectual shape |
|---|---|---|---|
| Obesity medicines | `objects/obesity-medicines/` | B1, A1, A2, A3, D1 | On-map pharmacologic decision for medicines used in chronic weight management whose decision value may be weight, cardiovascular, or complication-specific (OSA, HFpEF, MASH, and neighbors A2 names). B1 carries one-year weight, harms, lean/fat mass, and selected hard outcomes. D1 is internal to the semaglutide branch: MACE reduction in established CVD without diabetes. **Mandatory named internal branches:** semaglutide 2.4 mg; tirzepatide; older approved agents that surface (liraglutide, phentermine-topiramate, naltrexone-bupropion, orlistat). **Mandatory internal structure:** weight ranking ≠ mortality/MI ranking; SELECT population ≠ everyone with obesity; long-term use/regain (A2) vs a course of treatment. **Named watches, not promotions:** CagriSema, orforglipron, retatrutide, and neighbors B1 reports at low or mixed certainty. **Safety fence:** compounded products (A2). Not a lifestyle-vs-drugs popularity contest. Not a type 2 diabetes medicines object. Not an Emerging Therapies folio. |
| Eating patterns | `objects/eating-patterns/` | C1, A1, A2, A3 | Pattern-level diet object. C1: low-carbohydrate and low-fat similar at six months; named-diet differences small; weight loss diminished at 12 months; risk-factor benefits largely disappeared except Mediterranean. Vegetarian/Ornish-class programmes are on the map. Weight/risk-factor change ≠ hard events. **Mandatory named internal branch:** VLCD / formula diets (A3 placement; no seated C; working evidence in Phase 1; not DiRECT imported from type 2 diabetes). Internal branches by named programme / macronutrient pattern. Do not invent unstudied vegan-only claims from Mediterranean evidence. |
| Exercise | `objects/exercise/` | C2, A1, A3 | All-mode exercise map. C2: aerobic preferentially for weight and fat (average not more than 2–3 kg); resistance for lean-mass preservation during weight loss; any mode for fitness and insulin sensitivity. Mode ranking is composition/fitness ranking, not hard-outcome ranking and not an incretin-rival weight ranking. Modes are internal branches. Bellicha 2021 is a working companion. |
| Behavioural weight-management programmes | `objects/behavioural-programmes/` | A3 (pathway placement only) | Investigated delivery object with **no seated C**: structured counselling, commercial programmes, and NICE-style behavioural services. Start from A3, then search working evidence. “Which programme do I join?” is not “which named diet” and not “should I exercise.” Absence of a permanent C is allowed. Do not manufacture a WW-or-equivalent C for aisle completeness. |
| Metabolic surgery and endoscopic procedures | `objects/metabolic-and-endoscopic-procedures/` | C3, A3 | On-map procedural decision. C3: surgery appears superior long term (RYGB, sleeve, SADI, BPD); endoscopic procedures except ESG were less effective than newer medicines; semaglutide and tirzepatide showed no inferior short-term weight results vs some surgery; long-term data lacking for most medicines and all endoscopic procedures; SAE higher with procedures than with medicines, highest long-term with BPD. **Mandatory named internal branches:** metabolic/bariatric surgery (procedure types internal); endoscopic procedures (ESG, balloons, and neighbors). SOS observational mortality is a **mandatory working companion**, not a SELECT-class CVOT. Short-term incretin comparison annotates; it does not merge this object with obesity medicines. Not a type 2 diabetes surgery object. |
| Popular supplements and nutraceuticals | `objects/popular-supplements/` | A1, A2, A3 (class placement only) | Investigated popular market with **no seated C**: green tea, Garcinia, CLA, chromium, and neighbors Phase 1 finds people actually chase, including Ayurvedic products that surface. Start from guideline honesty, then search working evidence. Absence of a permanent C is allowed. Do not manufacture a representative-supplement C for aisle completeness. Plant-based analogue check applies if an animal-derived product opens. |

**Not an object:** SELECT as a standalone destination, investigational peptides as studio-imported objects, compounded peptides as a therapy, sleep, pediatric obesity as this campaign’s map, VLCD as a seventh object (lives as mandatory branch), endoscopic procedures as a seventh object (lives as mandatory branch), or type 2 diabetes overlap as a merge.

## Proposed merge / split locks

| Decision | Lock |
|---|---|
| Semaglutide vs tirzepatide vs older anti-obesity medicines | One **obesity-medicines** object. Named internal branches. |
| Weight ranking vs MACE / mortality | Same medicines object. B1 weight network ≠ D1 SELECT warrant. Mandatory internal divider, not two medicines objects. |
| SELECT population (established CVD, no diabetes) | Internal to the semaglutide branch. Not a second medicines object and not a primary-prevention export. |
| CagriSema / orforglipron / retatrutide / survodutide | Named watches inside **obesity medicines**. Not objects. Promotion only via Phase 1 membership/object proposal. |
| Compounded peptides | Safety fence inside **obesity medicines**. Not an object. |
| Mediterranean vs low-carbohydrate vs vegetarian vs other named programmes | One **eating-patterns** object. C1 6- vs 12-month grain is mandatory. |
| Eating patterns vs VLCD / formula diets | One eating-patterns object with VLCD as a **mandatory named internal branch**. Split later only if Phase 1 forces it. |
| Eating patterns vs behavioural programmes | **Separate objects.** Named-diet quality ≠ programme delivery. |
| Eating patterns vs exercise | **Separate objects.** |
| Aerobic vs resistance vs combined vs HIIT | One **exercise** object. Modes internal. |
| RYGB vs sleeve vs other operations | One procedures object. Surgery types internal. |
| Surgery vs endoscopic procedures | One procedures object with **two mandatory named branches**. C3’s non-collapse (endoscopic ≠ surgery; EBP except ESG < newer medicines) is internal structure, not a reason to skip endoscopic investigation. Split later only if Phase 1 forces it. |
| Short-term incretin vs surgery | Annotation across medicines and procedures objects. **Not** a merge. |
| Green tea vs Garcinia vs CLA vs chromium vs other aisle names | One **popular-supplements** object. Named internal branches. Do not invent five objects before Phase 1. |
| GLP-1 for type 2 diabetes / SURPASS-CVOT / DiRECT | **Not objects on this map.** Sibling campaign. |
| Pediatric obesity as a hub | Phase 3. This index does not pre-split IA. |

## Explicit gaps (do not invent seats)

1. Sleep as a major destination  
2. Dedicated VLCD library C (branch first)  
3. Dedicated endoscopic library C separate from C3  
4. Named single-supplement deep dives beyond the popular-supplements shelf (unless a Stability Check promotion gate succeeds)  
5. Investigational incretins as approved-medicine objects  
6. SURMOUNT-MMO and other unfinished CVOTs as extra D seats  
7. STEP 1 / SURMOUNT-1 / SOS as extra library D seats (companions)  
8. Pediatric / adolescent obesity as this campaign’s map  
9. Type 2 diabetes merge, DiRECT import, or SURPASS-CVOT import  
10. Emerging Therapies studio folios as this campaign’s objects

## Obesity-medicines gate (Stability Check instruction)

When opening `objects/obesity-medicines/`:

1. Carry B1 as the comparative GRADE spine. A1–A2 sequencing and subpopulation recs are mandatory internal structure.  
2. Named branches as locked above. D1 is internal to semaglutide 2.4 mg.  
3. Explicit non-collapse: one-year weight ranking ≠ mortality/MI ranking; SELECT’s established-CVD enrollment ≠ everyone with obesity; tirzepatide’s larger weight and lean-mass loss ≠ a SELECT-class MACE warrant.  
4. Investigational neighbors stay watches unless a promotion gate succeeds. Do not import Emerging Therapies claim ladders.  
5. Compounded products are a safety fence from A2, not a therapy branch to optimize.  
6. Do not import SURPASS-CVOT or type 2 diabetes sequencing as this object’s architecture.  
7. Membership proposal only if Phase 1 needs a seated D that B1 plus SELECT cannot carry. Library stays at 8 unless that proposal is accepted.

## Eating-patterns gate (Stability Check instruction)

When opening `objects/eating-patterns/`:

1. Carry C1 as the seated named-programme warrant. 6-month vs 12-month fade is mandatory.  
2. Vegetarian/Ornish-class presence is honesty, not a transferred Mediterranean warrant.  
3. VLCD / formula diets are a mandatory named internal branch with working evidence. Do not import DiRECT. Do not treat Ge’s named-diet network as a formula-diet protocol.  
4. Weight and risk-factor change ≠ hard events.  
5. Split proposal only if VLCD evidence cannot live as a branch.

## Procedures gate (Stability Check instruction)

When opening `objects/metabolic-and-endoscopic-procedures/`:

1. Carry C3 as the seated GRADE warrant.  
2. Read SOS as a **mandatory working companion** for long-term observational mortality. Do not treat it as a SELECT-class CVOT.  
3. Explicit non-collapse: surgery ≠ endoscopic procedures; endoscopic (except ESG) ≠ newer medicines; short-term incretin non-inferiority ≠ long-term surgical advantage.  
4. Procedure types are named internal branches. A3 referral thresholds are guideline placement, not an individual prescription.  
5. SAE costs, including BPD’s long-term SAE signal, are part of the claim.  
6. Membership proposal only if Phase 1 needs a seated D that C3 plus SOS cannot carry. Library stays at 8 unless that proposal is accepted.

## Behavioural-programmes gate (Stability Check instruction)

When opening `objects/behavioural-programmes/`:

1. Read A3 behavioural-services placement. Do not invent a representative-programme C.  
2. Ask what the strongest **weight** claim current working evidence earns, separately from named-diet (C1) and exercise (C2) warrants. Separately: any **hard-outcome** claim?  
3. Ask: does any named programme earn a **distinct decision placement** that this shelf plus A3 cannot already carry?  
4. If yes, open a membership/object proposal. If no, keep named branches. “Insufficient evidence” is an allowed, valuable result.

## Popular-supplements gate (Stability Check instruction)

When opening `objects/popular-supplements/`:

1. Read A-set supplement honesty. Do not invent a representative-supplement C.  
2. For each crowded name (green tea, Garcinia, CLA, chromium, and others that surface, including Ayurvedic products), ask: what is the strongest **weight** claim the current working evidence earns? Separately: any **hard-outcome** claim?  
3. Ask: does any named product earn a **distinct decision placement** that the shelf plus guideline class judgment cannot already carry?  
4. If an animal-derived product opens, run the plant-based analogue check at the same decision question.  
5. If yes for a product promotion, open a membership/object proposal. If no, keep it as a named branch. “Insufficient evidence” is an allowed, valuable result.

## Impact if accepted

- Creates six object folders after owner approval.  
- Unlocks Phase 1 Evidence Stability Checks.  
- Does not reopen library membership.  
- Does not lock public hub architecture.

## Decision

**Accepted** August 13, 2026. Six objects. Library membership remains 8.

Owner lock (substance, not only “accepted”):

- Keep behavioural weight-management programmes as its own object. Library membership and object existence are different tests. A decision people actually face can deserve calibration even when Phase 0 found no permanent domain-level C.
- The six partition the decision landscape: eating pattern ≠ programme delivery ≠ exercise; medicines retain the weight-versus-MACE divider; procedures remain one object because surgery and endoscopy are protected as mandatory non-collapsed branches.
- Behavioural programmes and supplements keep explicit Phase 1 gates rather than manufactured evidence. A null/insufficient finding is permitted. Promotion requires evidence rather than popularity.

Folders opened. Phase 1 Stability Checks drafted. No membership proposal.
