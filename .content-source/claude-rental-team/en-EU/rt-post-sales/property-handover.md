---
plugin: rt-post-sales
skill: property-handover
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Pós-Venda / Entrega
---

# Property Handover, Manuals & Utility Transfer

## Objective & Triggers
Formalize physical handover of sold or renovated properties via Key Handover Certificate, delivery of manuals/warranties/as-built plans, and utility/property-tax account transfers.
- **Triggers:** Invoke `rt-post-sales/property-handover` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for rental tenant move-ins (`rt-property-management/move-inspections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Proof of closing/funding, handover inspection checklist, equipment manuals, final utility meter readings. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Confirm cleared closing funds/deed recording prior to releasing keys — Closing/Post-Sales — Day 0.
2. Walk property with buyer and execute Key Handover & Possession Certificate with meter readings — Post-Sales — Day 0.
3. Deliver Owner's Manual, appliance warranties, and as-built plans — Post-Sales — Day 0.
4. Track utility and municipal tax account transfers within 15 days — Post-Sales — D+15.

## Rules & Criteria
Market practice: Never grant early pre-closing possession without a formal Use & Occupancy Agreement approved by Legal and Leadership.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `property-handover` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Pós-Venda / Entrega**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `property-handover` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `property-handover` request missing Member State or core inputs (Proof of closing/funding) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Pós-Venda / Entrega** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
