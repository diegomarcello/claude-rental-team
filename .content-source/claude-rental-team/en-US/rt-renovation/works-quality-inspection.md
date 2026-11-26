---
plugin: rt-renovation
skill: works-quality-inspection
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro Fiscal / Inspetor de Qualidade
---

# Construction Quality Control, Testing & Punch List

## Objective & Triggers
Verify finished renovation quality against performance standards, run functional tests (flood/waterproofing, electrical load, floor slope), and issue Substantial/Final Completion sign-off.
- **Triggers:** Invoke `rt-renovation/works-quality-inspection` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for tenant move-in/move-out inspections (`rt-property-management/move-inspections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Scope of work, shop drawings, schedule, system-by-system test checklists. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Run rough-in tests before closing walls/ceilings (hydrostatic pressure test, 72h flood test on wet areas, circuit/GFCI/AFCI load tests) — QA Inspector — Mid-construction.
2. Walk every room to generate a photo-documented Punch List with a 5-business-day cure window — QA Inspector — Substantial Completion.
3. Release final retainage only upon 100% Punch List clearance and delivery of warranties/manuals — Construction/Finance — Final Closeout.

## Rules & Criteria
Standards: ABNT NBR 15575 (Residential Building Performance) in Brazil; IRC/IBC and NAHB Residential Construction Performance Guidelines in US.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `works-quality-inspection` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Engenheiro Fiscal / Inspetor de Qualidade**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `works-quality-inspection` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `works-quality-inspection` request missing mandatory inputs (Scope of work) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Engenheiro Fiscal / Inspetor de Qualidade** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
