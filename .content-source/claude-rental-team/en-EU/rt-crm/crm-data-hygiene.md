---
plugin: rt-crm
skill: crm-data-hygiene
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Administrador de CRM / DPO
---

# CRM Data Hygiene, Deduplication & Retention Purging

## Objective & Triggers
Maintain CRM database integrity through input validation rules, contact/property deduplication, and scheduled archiving/anonymization per statutory retention limits.
- **Triggers:** Invoke `rt-crm/crm-data-hygiene` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for building automated outreach flows (`journey-automation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: CRM contact and property tables, unique identifiers (email, E.164 phone, tax ID, parcel/title ID), retention schedule. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Enforce input normalization (E.164 phone, lowercase email, tax/parcel ID validation) — RevOps — Automated.
2. Run monthly duplicate merge jobs preserving full activity timelines — CRM Admin — Monthly.
3. Anonymize inactive non-customer leads past retention window and execute erasure requests — DPO/CRM Admin — Quarterly.

## Rules & Criteria
Statutory: Data accuracy and storage limitation principles (GDPR Art. 5(1)(d)–(e); LGPD Art. 6 V & Art. 16).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `crm-data-hygiene` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Administrador de CRM / DPO**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `crm-data-hygiene` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `crm-data-hygiene` request missing Member State or core inputs (CRM contact and property tables) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Administrador de CRM / DPO** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
