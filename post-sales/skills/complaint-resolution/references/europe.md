---
plugin: rt-post-sales
skill: complaint-resolution
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Ouvidoria / Gerente de Qualidade
---

# Complaint Resolution, Escalation & Consumer Protection

## Objective & Triggers
Resolve formal complaints from buyers, tenants, and landlords under strict SLAs, structured escalation tiers, and proactive resolution prior to regulatory filings.
- **Triggers:** Invoke `rt-post-sales/complaint-resolution` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for active court litigation (`rt-legal/disputes-eviction`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Intake channel, client history, issue category, financial impact. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Acknowledge receipt within 4 business hours and classify tier — Support — <= 4h.
2. Conduct root-cause audit within 24h — Ombuds/QA — <= 24h.
3. Deliver written resolution within 48h and confirm closure — QA/Manager — <= 48h.

## Rules & Criteria
Statutory: EU/France mandatory Consumer Mediator disclosure (Code de la consommation art. L612-1); BR Decree 11.034/2022 & PROCON.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `complaint-resolution` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Ouvidoria / Gerente de Qualidade**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `complaint-resolution` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `complaint-resolution` request missing Member State or core inputs (Intake channel) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Ouvidoria / Gerente de Qualidade** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
