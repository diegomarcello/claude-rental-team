---
plugin: rt-pre-sales
skill: visit-scheduling
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Pré-vendas / Operações
---

# Tour Scheduling, Confirmation & Agent Safety Protocol

## Objective & Triggers
Coordinate in-person and virtual property tours, secure occupant access notice, send automated reminders, and enforce agent physical safety and tour check-in protocols.
- **Triggers:** Invoke `rt-pre-sales/visit-scheduling` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for engineering inspections or move-in key handover (`rt-property-management/move-inspections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Property ID, occupancy status, agent and prospect availability, visitor photo ID. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Honor statutory advance notice to current tenant if occupied (e.g., 24h–48h in US/EU; prior arrangement in BR Lei 8.245/91 art. 23, IX) — SDR — Pre-booking.
2. Collect visitor full name and photo ID prior to vacant/isolated property showings (agent safety protocol) and enable CRM tour check-in/out — SDR/Agent — Pre-tour.
3. Send 24h and 2h automated confirmations with address, parking instructions, and HOA rules — CRM Automation — T-24h / T-2h.
4. Log signed showing receipt (procuring-cause evidence) and post-tour feedback — Agent — Post-tour.

## Rules & Criteria
Statutory: Tenant quiet enjoyment / inviolability of the home (entering an occupied rental without tenant consent or court order is illegal trespass). In the US, obtain a signed Buyer Representation Agreement prior to touring (post-NAR settlement rule).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `visit-scheduling` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Pré-vendas / Operações**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `visit-scheduling` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `visit-scheduling` request missing Member State or core inputs (Property ID) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Pré-vendas / Operações** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
