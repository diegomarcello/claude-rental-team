---
plugin: rt-jurisdictions
skill: construction-permits
jurisdiction: united-states
last_verified: 2026-11-25
confidence: verified
reviewer: Licensed General Contractor / Construction Attorney
---

# Jurisdiction United States — Building Permits, Zoning, OSHA, Lien Waivers & HOA Rules

## Objective & Triggers
Establish US building permitting, zoning/code compliance (IBC/IRC), OSHA jobsite safety, Mechanic's Lien waiver protocols, and HOA/COA architectural approvals.
- **Triggers:** 'when is a building permit required US', 'unpermitted work risk flip', 'mechanic lien waiver rules', 'OSHA construction safety'.

## When Not to Use
- Do not use to draft a detailed trade scope of work (use `rt-renovation/scope-of-work`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Municipality & State | Yes | Text | Property Record |
| Scope (Cosmetic vs. MEP, structural, roof, windows, addition) | Yes | Text | Scope |
| Governance (Fee-simple vs. HOA/Condo Association) | Yes | Enum | Title / HOA Docs |

## Process


## Rules & Criteria
- **Code Standard (ICC Codes):** Most US jurisdictions adopt the International Building Code (IBC), International Residential Code (IRC), National Electrical Code (NEC / NFPA 70), and International Plumbing Code (IPC). Cosmetic work (paint, flooring, cabinet refacing without moving plumbing/electrical) typically requires no permit; structural changes, load-bearing wall removal, roof replacement, HVAC/electrical/plumbing alterations, and window replacements generally require permits.
- **Federal Safety (OSHA 29 CFR Part 1926):** Mandatory fall protection at **6 feet** or more in construction (29 CFR § 1926.501), scaffolding standards, trenching/excavation rules, and EPA **RRP Rule** (40 CFR Part 745) requiring Lead-Safe Certified Renovators for work disturbing lead paint in pre-1978 housing.
- **State Mechanic's Lien Laws:** Contractors, subcontractors, and material suppliers hold statutory lien rights against the property if unpaid (e.g., Fla. Stat. Ch. 713 — Notice to Owner within 45 days; Tex. Prop. Code Ch. 53; Cal. Civ. Code § 8000 et seq.). Always require **Conditional and Unconditional Lien Waivers** (progress and final) before releasing draw funds.
- **Penalties:** Stop-work orders, double/triple permit fee penalties, forced demolition of unpermitted additions, and title exceptions blocking resale financing.

## Calculations
Not applicable (regulatory checklist; budget contingency handled in `rt-renovation/renovation-budget`).

## Outputs
Permitting & compliance matrix (AHJ, HOA/ARB, EPA RRP, OSHA, Lien Waiver checklist).

## Human Approval Gates
- Claude **never** authorizes starting structural, electrical, plumbing, or exterior work without an issued municipal permit and verified contractor COI (General Liability + Workers' Comp).

## Handoffs
- Hands off to `rt-renovation/scope-of-work` and `rt-procurement/vendor-management`.

## Common Errors & Risks
- Buying a flip with unpermitted garage conversions without budgeting for retroactive permitting or demolition.
- Paying a GC in full without obtaining unconditional final lien waivers from major subcontractors and suppliers.

## Test Cases
1. **Normal:** 'We are renovating a 1965 house in Texas, replacing windows, rewiring, and scraping old paint. What permits/rules apply?' -> Municipal electrical/window permits + mandatory EPA Lead RRP certification (pre-1978).
2. **Incompleto:** 'Do we need a permit to remodel a bathroom?' -> Asks city/state and whether plumbing/electrical lines are being moved or layout changed.
3. **Risco:** 'The contractor wants to start opening load-bearing walls tomorrow and pull the permit next week.' -> Blocks work immediately due to stop-work and structural safety risk.

## Sources
- OSHA Construction Standards — 29 CFR Part 1926 — US Dept. of Labor (`osha.gov`), accessed 2026-11-25.
- EPA Lead Renovation, Repair and Painting (RRP) Rule — 40 CFR Part 745 — EPA (`epa.gov`), accessed 2026-11-25.
- Fla. Stat. Ch. 713; Tex. Prop. Code Ch. 53; Cal. Civ. Code § 8000 et seq. — State Legislatures, accessed 2026-11-25.

## Pending Items
- Local municipal permitting portals and expediter SLAs per target city.
