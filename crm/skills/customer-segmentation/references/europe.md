---
plugin: rt-crm
skill: customer-segmentation
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de CRM / DPO
---

# Customer Segmentation & Compliant Attribute Governance

## Objective & Triggers
Segment buyers, tenants, and landlords by behavioral intent, portfolio size, and investment profile without using protected or discriminatory attributes.
- **Triggers:** Invoke `rt-crm/customer-segmentation` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for automated campaign execution (`journey-automation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: CRM contact database, transaction/tour history, property preferences, landlord tier. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Build dynamic behavioral and portfolio segments — RevOps — Setup.
2. Prohibit custom tags or fields referencing protected classes — DPO/RevOps — Governance.
3. Map each segment to tailored lifecycle messaging — Marketing/CRM — Continuous.

## Rules & Criteria
Statutory: Fair Housing Act, GDPR Art. 9, and LGPD Art. 11 prohibit discriminatory profiling or unconsented sensitive data attributes.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `customer-segmentation` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Gerente de CRM / DPO**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `customer-segmentation` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `customer-segmentation` request missing Member State or core inputs (CRM contact database) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de CRM / DPO** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
