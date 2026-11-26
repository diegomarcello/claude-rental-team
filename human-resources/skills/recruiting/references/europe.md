---
plugin: rt-human-resources
skill: recruiting
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de RH / Jurídico Trabalhista
---

# Recruiting, Licensing Verification & Bias-Free Hiring

## Objective & Triggers
Draft job descriptions, verify mandatory brokerage/professional licenses, and run structured interviews free of discriminatory inquiries.
- **Triggers:** Invoke `rt-human-resources/recruiting` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for construction contractor onboarding (`rt-procurement/vendor-management`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Role title, engagement classification, required licenses, compensation range. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Verify statutory licensing requirements — HR — Pre-posting.
2. Publish inclusive job post and run structured interviews — HR/Hiring Manager — Selection.
3. Verify active license standing prior to offer — HR — Pre-offer.

## Rules & Criteria
Statutory: Employment anti-discrimination laws (US Title VII/ADA/ADEA; EU Directive 2000/78/EC; BR Lei 9.029/95).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `recruiting` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Gerente de RH / Jurídico Trabalhista**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `recruiting` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `recruiting` request missing Member State or core inputs (Role title) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de RH / Jurídico Trabalhista** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
