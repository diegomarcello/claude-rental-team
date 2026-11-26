---
plugin: rt-appraisal
skill: cost-approach
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro Avaliador (CREA) / Arquiteto (CAU) / Quantity Surveyor
---

# Cost Approach (Replacement Cost & Depreciation)

## Objective & Triggers
Estimate value of special-purpose buildings, warehouses, new construction, or insurable value by adding land value to depreciated replacement/reproduction cost of improvements.
- **Triggers:** Invoke `rt-appraisal/cost-approach` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use standalone for existing condominium units in liquid markets where Sales Comparison governs.

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Land value (via sales comparison or residual), gross building area, unit construction cost (CUB/SINAPI in BR; RSMeans/Marshall & Swift in US; BKI/BCIS in EU), contractor overhead/profit, effective age, and economic useful life. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Value underlying land separately via comparable land sales — Valuer — Day 1.
2. Compute Replacement Cost New (RCN) via regional cost index + entrepreneurial profit/overhead — Engineer/QS — Day 1.
3. Deduct physical depreciation (Age-Life / Breakdown / Ross-Heidecke) and functional/external obsolescence — Engineer — Day 2.
4. Sum land value + depreciated improvements — Valuer — Day 2.

## Rules & Criteria
Standards: NBR 14653-2 (Evolutionary / Cost Method), USPAP SR 1-4(b), RICS Red Book / ImmoWertV (Sachwertverfahren).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**Cost Approach Formula:**
$$V_{\text{total}} = V_{\text{land}} + \left(\text{RCN} - \text{Physical Dep.} - \text{Functional/External Obs.}\right)$$
- **Numerical Example (Industrial Warehouse):**
  - Land Value = $800,000 | Area = 10,000 sq ft | Unit Cost = $250/sq ft -> $\text{RCN} = \$2,500,000$.
  - Effective Age = 10 yrs; Total Economic Life = 50 yrs -> Age-Life Depreciation = $10/50 = 20\%$ ($500,000).
  - $\text{Depreciated Improvements} = \$2,500,000 - \$500,000 = \mathbf{\$2,000,000}$.
  - $V_{\text{total}} = \$800,000 + \$2,000,000 = \mathbf{\$2,800,000.00}$.

## Outputs
Standardized `cost-approach` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Engenheiro Avaliador (CREA) / Arquiteto (CAU) / Quantity Surveyor**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `cost-approach` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `cost-approach` request missing Member State or core inputs (Land value (via sales comparison or residual)) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Engenheiro Avaliador (CREA) / Arquiteto (CAU) / Quantity Surveyor** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
