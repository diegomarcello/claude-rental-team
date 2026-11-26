---
plugin: rt-property-management
skill: condo-administration
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Analista de Carteira / Patrimônio
---

# Condominium / HOA Governance, Assemblies & Expense Allocation

## Objective & Triggers
Manage condominium/HOA obligations for managed properties, separate ordinary operating charges (tenant) from extraordinary capital assessments (landlord), and represent owners at assemblies via proxy.
- **Triggers:** Invoke `rt-property-management/condo-administration` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for full-building HOA/condo association management.

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Itemized HOA/condo statement, bylaws/CC&Rs, assembly notice, owner proxy form. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Audit monthly condo/HOA statement separating ordinary operating expenses from capital reserves/special assessments — Analyst — Monthly.
2. Deliver HOA rules/CC&Rs to tenant at lease signing — Leasing — Move-in.
3. Notify landlord of upcoming HOA/condo meetings at least 10 days ahead — Analyst — Pre-meeting.

## Rules & Criteria
Statutory: BR Lei 8.245/91 art. 22 §1 vs. art. 23 XII; France Décret n° 87-713 (*charges récupérables*).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `condo-administration` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Analista de Carteira / Patrimônio**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `condo-administration` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `condo-administration` request missing Member State or core inputs (Itemized HOA/condo statement) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Analista de Carteira / Patrimônio** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
