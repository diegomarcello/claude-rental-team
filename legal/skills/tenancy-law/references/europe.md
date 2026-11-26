---
plugin: rt-legal
skill: tenancy-law
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Advogado Imobiliário
---

# Tenancy Law Advisory & Precedent Guide

## Objective & Triggers
Resolve day-to-day operational questions on landlord-tenant rights and duties (improvements, right of first refusal, subletting, sale of tenant-occupied property, repair allocation).
- **Triggers:** Invoke `rt-legal/tenancy-law` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use once formal default or litigation is triggered (`disputes-eviction`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Jurisdiction, relevant lease clause, factual scenario, dates, and prior notices sent. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Identify mandatory vs. default statutory rule in the jurisdiction — Counsel — Same day.
2. Cross-check against executed lease language — Counsel — Same day.
3. Recommend preventive action with notice template if needed — Counsel — Within 24h.

## Rules & Criteria
Statutory (Key examples): Tenant right of first refusal upon sale (FR Loi 1989 art. 15-II; BR Lei 8.245/91 art. 27 — 30 days). Essential habitability repairs remain landlord duty regardless of lease waivers.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `tenancy-law` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Advogado Imobiliário**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `tenancy-law` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `tenancy-law` request missing Member State or core inputs (Jurisdiction) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Advogado Imobiliário** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
