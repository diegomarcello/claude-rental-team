---
plugin: rt-property-management
skill: maintenance-requests
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Manutenção
---

# Maintenance Triage, Urgency SLAs & Repair Responsibility

## Objective & Triggers
Triage maintenance tickets by severity (Emergency, Urgent, Routine), assign cost responsibility (structural/habitability = landlord; misuse/routine consumables = tenant), and dispatch vetted vendors.
- **Triggers:** Invoke `rt-property-management/maintenance-requests` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for major capital renovations (`rt-renovation/scope-of-work`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Issue description and photo/video, occupancy duration, appliance/system history, landlord pre-approved repair limit. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Classify urgency: Emergency (SLA <= 2–4h), Urgent (SLA <= 24–48h), Routine (SLA <= 5 business days) — Triage — Immediate.
2. Determine legal/lease responsibility — Analyst — Day 0.
3. Dispatch vetted vendor within landlord pre-authorized NTE limit — Maintenance — Day 0–1.
4. Verify completion photo and tenant sign-off prior to payment — Maintenance/Finance — Post-repair.

## Rules & Criteria
Statutory: Maintaining habitability and making urgent structural/system repairs is a mandatory landlord duty.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `maintenance-requests` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Manutenção**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `maintenance-requests` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `maintenance-requests` request missing Member State or core inputs (Issue description and photo/video) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Manutenção** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
