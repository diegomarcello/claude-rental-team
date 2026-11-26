---
plugin: rt-legal
skill: title-due-diligence
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Advogado Imobiliário
---

# Title Due Diligence & Encumbrance Search

## Objective & Triggers
Audit chain of title, liens, mortgages, easements, seller litigation/tax warrants, HOA/property tax arrears, and zoning/occupancy permits prior to acquisition or major commercial lease.
- **Triggers:** Invoke `rt-legal/title-due-diligence` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for AML source-of-funds KYC (`privacy-aml`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Updated title extract (< 30 days), full seller/spouse details (individual/entity), tax parcel ID, HOA estoppel/status letter. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Review full chain of title, easements, and building/marital status endorsements — Paralegal/Counsel — Days 1–2.
2. Run tax, labor, civil litigation, bankruptcy, and judgment searches on sellers and principals — Paralegal — Days 2–4.
3. Verify propter rem property tax and HOA arrears plus Certificate of Occupancy — Paralegal — Days 3–5.
4. Issue Title Risk Opinion (Clear, Clear w/ Escrow Holdback, or Reject) — Senior Counsel — Day 5.

## Rules & Criteria
Statutory: Property tax and HOA assessments often carry super-priority / propter rem status attaching to the land. Standard certificate validity: 30–90 days depending on issuing authority.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `title-due-diligence` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Advogado Imobiliário**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `title-due-diligence` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `title-due-diligence` request missing Member State or core inputs (Updated title extract (< 30 days)) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Advogado Imobiliário** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
