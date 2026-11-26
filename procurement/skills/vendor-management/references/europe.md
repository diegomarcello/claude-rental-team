---
plugin: rt-procurement
skill: vendor-management
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Compras / Compliance
---

# Vendor Onboarding, Compliance & Joint-Employer Risk Control

## Objective & Triggers
Vet and monitor contractors and suppliers by verifying tax status, insurance (General Liability / Workers' Comp), trade licenses, and independent-contractor compliance.
- **Triggers:** Invoke `rt-procurement/vendor-management` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for hiring internal employees or associate brokers (`rt-human-resources/recruiting`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Tax ID, tax/social-security clearance certificates, active COI (GL & Workers' Comp), trade license, references. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Require onboarding packet before issuing first PO — Procurement — Pre-onboarding.
2. Automatically block ERP payments/POs when insurance or licenses expire — System/Procurement — Automated.
3. Score post-job performance quarterly — Construction/PM — Quarterly.

## Rules & Criteria
Statutory: Subcontractor joint/vicarious liability for unpaid wages or uninsured jobsite injuries.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `vendor-management` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Compras / Compliance**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `vendor-management` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `vendor-management` request missing Member State or core inputs (Tax ID) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Compras / Compliance** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
