# Metabolic surgery and endoscopic procedures · Evidence Stability Check v0.1

**Status:** Frozen v1.0 · August 13, 2026  
**Type:** Evidence Stability Check (internal peer review)  
**Artifact:** [`./thinking-artifact-v0.1.md`](./thinking-artifact-v0.1.md) (**Frozen v1.0**)  
**Object:** Metabolic/bariatric surgery and endoscopic bariatric procedures as one object with two mandatory named branches  
**First conclusion under review:** Procedures earn an on-map seat from a GRADE network of medicines, endoscopic procedures, and surgery (C3), surgery appears superior for long-term weight, endoscopic procedures except ESG were less effective than newer medicines, and the two branches must not collapse.

**Accepted evidence used:** C3 De Luca 2026 *Obesity* GRADE NMA; A3 NICE NG246. A1’s surgery-out-of-scope boundary is a coverage note, not a deletion of this object. **Working companion (not seated):** Sjöström et al. SOS 2007 *NEJM* (and later life-expectancy follow-up). SOS is observational, not a SELECT-class randomized CVOT. Short-term incretin comparison annotates this object; it does not merge with obesity medicines.

---

## 1. Object definition

| Candidate unit | Treatment |
|---|---|
| Metabolic/bariatric surgery and endoscopic bariatric procedures | Core object |
| Surgery (RYGB, sleeve, SADI, BPD, and neighbors as internal procedure types) | **Mandatory named branch** |
| Endoscopic procedures (ESG, balloons, and neighbors) | **Mandatory named branch** |
| Short-term weight comparison with semaglutide/tirzepatide | Annotation, not a merge |
| SOS long-term mortality / life expectancy | Mandatory working companion, not a seated D-class CVOT |
| A1 surgery-out-of-scope | Coverage note for that guideline, not an object veto |
| Split into two public objects from this check | Closed unless Phase 1 cannot keep both branches honest |

**Combine risk:** Collapsing endoscopy into “surgery-lite,” or treating C3’s short-term incretin-versus-some-surgery node as a reason to merge this object with medicines.  
**Split risk:** Promoting endoscopy to a seventh object before the branches fail.  
**Inflation risk:** SOS observational mortality becoming a SELECT-class randomized CVOT; short-term weight parity becoming long-term procedure-vs-shot equivalence.  
**Unit the evidence suggests:** One **procedures** object with two non-collapsed branches.

---

## 2. Confidence

| Claim | Confidence | Basis |
|---|---|---|
| Most surgeries and tirzepatide produce TBWL >10% at 26–52 weeks | High as C3 direction | 139 RCTs (54 MBS n=61,961; 21 EBP n=2,934; 64 OMM n=5,991) |
| Surgery is superior for long-term weight (RYGB, SG, SADI, BPD) | High as C3 long-term grain | C3: MBS superior long term |
| Endoscopic procedures except ESG were less effective than newer obesity medicines | Moderate as C3’s EBP vs OMM grain | C3: EBP except ESG less effective than newer OMM |
| Semaglutide and tirzepatide showed no inferior short-term weight results vs some surgery | Moderate as C3 short-term node | Annotates; does not merge objects |
| Long-term data are lacking for most OMM and all EBP | High as C3’s own limit | Durability humility |
| SAE higher with EBP/MBS than OMM; BPD highest long-term SAE | High as C3 harm grain | Harm is part of the object, not a footnote |
| SOS shows lower long-term mortality after surgery vs matched controls | Moderate as observational direction | Sjöström 2007: n=4,047 non-randomized; 10.9 years; adjusted mortality HR 0.71. Later life-expectancy companion HR 0.77; about 3.0 years longer median life expectancy vs control |
| SOS is a SELECT-class randomized CVOT | Low, reject | Non-randomized Swedish cohort. Different claim type from D1 |
| Collapse endoscopy into surgery | Low, reject | Object-index lock: two mandatory named branches |
| Merge with obesity medicines because of short-term weight overlap | Low, reject | Annotation, not architecture |
| A1’s surgery-out-of-scope deletes this object | Low, reject | A3 and C3 cover the decision |

**Disagreement lives in:** How to teach short-term incretin-versus-some-surgery without converting it into “shots replaced surgery”; how loudly SOS mortality may speak without wearing SELECT’s clothes; and whether ESG should be featured more loudly than other endoscopic procedures given C3’s exception.

---

## 3. Alternative interpretations

**A. "Tirzepatide matches some surgery at one year, so surgery is obsolete."**  
C3’s long-term grain is the opposite for MBS. Long-term data lacking for most medicines and all endoscopic procedures.

**B. "SOS mortality means surgery has a SELECT-class heart warrant."**  
Wrong claim type. Observational, non-randomized, mixed diabetes status historically. Keep it as a working companion.

**C. "Endoscopy is just weaker surgery, so one branch."**  
C3 distinguishes EBP from MBS (effectiveness vs newer medicines; SAE profile; absence of long-term EBP data). Index forbids collapse.

**D. "A1 omitted surgery, so this object is out of scope for the campaign."**  
A1’s algorithm scope is not the research object. A3 and C3 put procedures on the map.

**E. "Seat SOS as D2."**  
Membership inflation. It calibrates as a labeled companion. It is not a randomized CVOT.

---

## 4. Competing narrative

| Orientation | Story |
|---|---|
| **A (chosen)** | One procedures object: C3 GRADE spine; surgery vs endoscopy as mandatory branches; short-term incretin annotation; SOS observational companion; SAE honesty; no merge with medicines. |
| **B** | Shots replaced surgery. |
| **C** | Surgery is the only real procedure; endoscopy is decoration. |
| **D** | SOS is SELECT for surgery. |

**Why A survives:** C3’s long-term vs short-term split blocks B. Two-branch lock and EBP-vs-OMM grain block C. Claim-type honesty blocks D.

**Intellectual shape:** **On-map procedures; surgery and endoscopy as non-collapsed branches; short-term incretin annotates; SOS observational, not SELECT-class; SAE costs are part of the claim.**

---

## 5. Magnitude

C3 (De Luca 2026): search to 1 December 2024; 139 RCTs. TBWL >10% with most surgeries and tirzepatide at 26–52 weeks. MBS superior long term (RYGB, SG, SADI, BPD). EBP except ESG less effective than newer OMM. Semaglutide/tirzepatide no inferior short-term vs some MBS. Long-term data lacking for most OMM and all EBP. SAE higher with EBP/MBS than OMM; BPD highest long-term SAE.

SOS (working): 4,047 people; non-randomized; 10.9-year mortality HR 0.71 adjusted; later life-expectancy follow-up HR 0.77 and about three years longer median life expectancy vs control. Observational. Not D1.

A3 places surgery (and relevant endoscopic options as the pathway names them) inside UK obesity care. A1’s surgery-out-of-scope is recorded as that document’s boundary.

That magnitude supports **surgery as the long-term weight leader among studied procedures, endoscopy as a distinct and generally weaker (except ESG) branch, and honest SAE costs**, not procedure-vs-shot merger and not a randomized CVOT for surgery.

---

## 6. Hidden assumptions

| Assumption | Risk | Correction |
|---|---|---|
| Short-term TBWL parity is long-term equivalence | Durability leak | C3: long-term MBS superiority; missing long-term OMM/EBP |
| Observational mortality is a randomized CVOT | Claim-type leak | SOS ≠ SELECT |
| Endoscopy inherits surgery’s long-term grain | Branch leak | All EBP lack long-term data in C3 |
| Highest-effect surgery (BPD) is therefore first-line | Harm leak | Highest long-term SAE |
| A1 omitted it, so we omit it | Coverage leak | Research object follows C3/A3 |

---

## 7. Boundary conditions

**Applies most clearly to:** Adults with obesity considering surgery or an endoscopic procedure, including people comparing those options with medicines.

**Does not earn:** SELECT-class randomized CVOT for surgery from SOS; collapse of endoscopy; merge with obesity medicines; a seventh endoscopic object from this check; seating SOS.

### Split / membership gates

| Question | Reading |
|---|---|
| Can surgery and endoscopy stay honest as two branches of one object? | **Yes.** C3 already distinguishes them. |
| Must SOS be seated as D2? | **No.** Working companion. |
| Gate decision | **Do not split. Do not open a membership proposal.** Library stays at 8. |

---

## 8. Evidence map

| Decision | Verdict |
|---|---|
| Earn a procedures seat? | **Yes, on-map** |
| Collapse endoscopy? | **No** |
| Merge with medicines? | **No** |
| SOS as SELECT-class D? | **No** |
| Membership proposal? | **No** |

---

## 9. Final stress test

1. **Why one object if the branches differ?**  
   Because C3 is one network. Branches protect the difference without inventing a seventh object.

2. **Does short-term incretin parity retire surgery?**  
   No. Long-term MBS is C3’s other grain.

3. **Does SOS HR 0.71 force a D seat?**  
   No. Observational companions do not become randomized CVOTs by being important.

4. **Does A1’s out-of-scope line veto the object?**  
   No. That is A1’s algorithm scope.

---

## 10. What would change my mind?

| Direction | Evidence that would move the claim |
|---|---|
| **Split endoscopy** | A Stability Check showing the branch cannot live beside surgery without distorting both claims |
| **Give surgery a SELECT-class randomized MACE warrant** | An RCT CVOT C3 and SOS cannot carry |
| **Merge with medicines** | Never as architecture; annotation stays annotation |

---

## 11. Missing evidence

1. Long-term RCTs of endoscopic procedures.  
2. Long-term RCTs of newer medicines vs surgery (beyond C3’s short-term node).  
3. Randomized mortality/MACE trials of surgery in obesity without diabetes.

**Unresolved before object freeze:** Phase 2 must keep the short-term incretin annotation from swallowing long-term surgery, and must keep SOS from wearing SELECT’s clothes.

---

## 12. Strongest earned claim

**Metabolic surgery and endoscopic procedures earn an on-map seat from a GRADE network of medicines, endoscopic procedures, and surgery (C3): surgery appears superior for long-term weight (especially RYGB, sleeve, SADI, BPD), endoscopic procedures except ESG were less effective than newer medicines, semaglutide and tirzepatide showed no inferior short-term weight results versus some surgery, SAE costs are higher with procedures than medicines and highest long-term with BPD, SOS observational mortality is a mandatory working companion rather than a SELECT-class randomized CVOT, endoscopic and surgical branches must not collapse, short-term incretin comparison annotates rather than merging this object with obesity medicines, and the library stays at 8.**

## What survives into the artifact

1. Intellectual shape: **on-map procedures; surgery and endoscopy as non-collapsed branches; short-term incretin annotates; SOS observational, not SELECT-class**.  
2. SAE honesty, including BPD.  
3. A1 out-of-scope as a coverage note, not a veto.

**Does not survive:** Shots-replaced-surgery; endoscopy-as-surgery-lite; SOS-as-SELECT; seating SOS; a seventh endoscopic object from this check.
