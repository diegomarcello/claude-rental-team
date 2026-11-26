---
plugin: rt-appraisal
skill: comparative-market-analysis
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Avaliador Habilitado (CRECI/CNAI, CREA/CAU, Appraiser, MRICS)
---

# Comparative Market Analysis (CMA) & Sales Comparison Adjustment

## Objective & Triggers
Estimate market sale or rental value via the Sales Comparison Approach using sample cleansing, attribute adjustment factors/regression, and statistical confidence intervals.
- **Triggers:** Invoke `rt-appraisal/comparative-market-analysis` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for pure income-producing properties lacking comps (`income-capitalization`) or special-purpose assets (`cost-approach`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Subject property attributes (address, net area, beds/baths, parking, finish grade, floor, condition) and sample of >= 5 recent comparables (closed sales or active listings). | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Gather >= 5–10 comparable properties in the same micro-market (past 6–12 months) — Valuer — Day 1.
2. Apply listing-to-sale elasticity adjustment and attribute adjustments (size, condition, parking, floor/view) — Valuer — Day 2.
3. Remove statistical outliers (Chauvenet criterion or +/- 2 SD) and compute adjusted mean, median, and 80% CI — Valuer — Day 2.
4. Validate conclusion and issue valuation report — Credentialed Reviewer — Day 3.

## Rules & Criteria
Standards: ABNT NBR 14653-2 (BR), USPAP Standards Rule 1-4(a) (US), RICS Red Book / ImmoWertV (EU). Market practice: Typical listing-to-close factor of 0.90–0.95 (5%–10% negotiation discount); minimum 5 valid comparables post-cleansing.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**Adjusted Unit Price Formula ($P_{\text{adj}}$):**
$$P_{\text{adj},i} = \left(\frac{\text{Price}_i}{\text{Area}_i}\right) \times F_{\text{listing}} \times F_{\text{location}} \times F_{\text{condition}} \times F_{\text{amenities}}$$
$$\text{Indicated Value} = \overline{P}_{\text{adj}} \times \text{Subject Area}$$
- **Numerical Example (1,000 sq ft condo, 3 cleansed comps):**
  - Comp 1: $520/sq ft (active listing) x 0.94 (listing factor) x 1.00 = **$488.80/sq ft**
  - Comp 2: $495/sq ft (closed sale) x 1.00 x 1.02 (condition) = **$504.90/sq ft**
  - Comp 3: $510/sq ft (closed sale) x 1.00 x 0.98 (floor) = **$499.80/sq ft**
  - $\overline{P}_{\text{adj}} = (488.80 + 504.90 + 499.80)/3 = \mathbf{\$497.83/\text{sq ft}}$ -> $\text{Indicated Value (1,000 sq ft)} = \mathbf{\$497,830.00}$.

## Outputs
Standardized `comparative-market-analysis` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Avaliador Habilitado (CRECI/CNAI, CREA/CAU, Appraiser, MRICS)**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `comparative-market-analysis` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `comparative-market-analysis` request missing Member State or core inputs (Subject property attributes (address) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Avaliador Habilitado (CRECI/CNAI, CREA/CAU, Appraiser, MRICS)** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
