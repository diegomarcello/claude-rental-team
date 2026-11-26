---
plugin: rt-property-management
skill: move-inspections
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Vistorias
---

# Move-In / Move-Out Inspections & Normal Wear and Tear

## Objective & Triggers
Conduct detailed room-by-room move-in and move-out inspections with timestamped photos, distinguishing chargeable tenant damage from normal wear and tear, and managing dispute and security deposit timelines.
- **Triggers:** Invoke `rt-property-management/move-inspections` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for pre-acquisition structural engineering inspections (`rt-appraisal/technical-inspection`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Signed move-in inspection report, timestamped move-out photos, repair invoices/quotes, statutory deposit return deadline. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Complete move-in inspection prior to key release with high-res photos and meter readings — Inspector — Move-in.
2. Grant tenant inspection objection window — Analyst — Post-move-in.
3. At move-out, compare item-by-item separating normal wear and tear from chargeable damage — Inspector — Move-out.
4. Return security deposit balance strictly within statutory deadlines — Finance/PM — Statutory deadline.

## Rules & Criteria
Statutory: Return premises in received condition except for normal wear and tear (BR Lei 8.245/91 art. 23, III; US deposit laws; FR Décret 2016-382).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `move-inspections` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Vistorias**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `move-inspections` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `move-inspections` request missing Member State or core inputs (Signed move-in inspection report) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Vistorias** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
