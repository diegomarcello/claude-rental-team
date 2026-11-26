---
plugin: rt-post-sales
skill: property-handover
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Pós-Venda / Entrega
---

# Property Handover, Manuals & Utility Transfer

## Objective & Triggers
Formalize physical handover of sold or renovated properties via Key Handover Certificate, delivery of manuals/warranties/as-built plans, and utility/property-tax account transfers.
- **Triggers:** Invoke `rt-post-sales/property-handover` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for rental tenant move-ins (`rt-property-management/move-inspections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Proof of closing/funding, handover inspection checklist, equipment manuals, final utility meter readings. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Confirm cleared closing funds/deed recording prior to releasing keys — Closing/Post-Sales — Day 0.
2. Walk property with buyer and execute Key Handover & Possession Certificate with meter readings — Post-Sales — Day 0.
3. Deliver Owner's Manual, appliance warranties, and as-built plans — Post-Sales — Day 0.
4. Track utility and municipal tax account transfers within 15 days — Post-Sales — D+15.

## Rules & Criteria
Market practice: Never grant early pre-closing possession without a formal Use & Occupancy Agreement approved by Legal and Leadership.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `property-handover` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador de Pós-Venda / Entrega**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `property-handover` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `property-handover` request missing mandatory inputs (Proof of closing/funding) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Pós-Venda / Entrega** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
