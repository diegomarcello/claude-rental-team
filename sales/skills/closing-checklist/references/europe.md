---
plugin: rt-sales
skill: closing-checklist
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Fechamento (Closing Coordinator)
---

# Closing Checklist (From Accepted Offer to Deed Recording)

## Objective & Triggers
Orchestrate every post-acceptance milestone through escrow/notary closing, funding, and title recording, tracking statutory deadlines and owners.
- **Triggers:** Invoke `rt-sales/closing-checklist` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for physical post-closing key handover (`rt-post-sales/property-handover`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Accepted offer/PSA, jurisdiction, cash vs. financed status, party list. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Verify earnest money deposit and trigger title due diligence (`rt-legal/title-due-diligence`) — Closing Coordinator — Days 1–3.
2. Track physical inspection, lender appraisal, and final loan clear-to-close — Closing Coordinator — Days 5–25.
3. Audit final settlement statements (TRID CD / Deed / Notarial Act) and transfer tax bills — Legal/Closing — D-5.
4. Confirm wire funding, deed execution, and county/land registry recording — Closing Agent — D0 to D+15.

## Rules & Criteria
Market practice: Conduct a final buyer walk-through 24 hours prior to closing to verify property condition and vacant possession.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `closing-checklist` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Fechamento (Closing Coordinator)**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `closing-checklist` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `closing-checklist` request missing Member State or core inputs (Accepted offer/PSA) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Fechamento (Closing Coordinator)** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
