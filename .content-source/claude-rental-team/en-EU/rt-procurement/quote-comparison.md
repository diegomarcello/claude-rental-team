---
plugin: rt-procurement
skill: quote-comparison
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Compras / Orçamentista
---

# Bid Leveling & Quote Comparison Matrix

## Objective & Triggers
Level competing contractor and vendor bids by normalizing scope exclusions, missing line items, lead times, and payment terms.
- **Triggers:** Invoke `rt-procurement/quote-comparison` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for building initial internal cost estimates (`rt-renovation/renovation-budget`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Standardized SOW, minimum 3 vendor quotes, payment milestones, and warranty terms. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Collect minimum 3 comparable bids — Procurement — Day 1.
2. Level bids by plugging estimated market cost for excluded scope items — Procurement/Estimator — Day 2.
3. Score using weighted matrix and submit award recommendation — Procurement — Day 3.

## Rules & Criteria
Market practice: Never award to lowest nominal bid without leveling 100% of scope.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**Formula:** $\text{Leveled Price}_k = \text{Bid}_k + \sum \text{Missing Scope Plugs}_k$. Example: Bidder B ($90k + $3k haul-away = $93k) vs. Bidder A ($92k all-in -> Winner).

## Outputs
Standardized `quote-comparison` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Compras / Orçamentista**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `quote-comparison` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `quote-comparison` request missing Member State or core inputs (Standardized SOW) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Compras / Orçamentista** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
