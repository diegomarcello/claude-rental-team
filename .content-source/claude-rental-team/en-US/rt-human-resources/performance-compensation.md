---
plugin: rt-human-resources
skill: performance-compensation
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de RH / Jurídico Trabalhista
---

# Performance Goals, Variable Compensation & Labor Compliance

## Objective & Triggers
Design KPI targets, commission accelerators, and bonus plans with transparent rules and payroll-tax compliance.
- **Triggers:** Invoke `rt-human-resources/performance-compensation` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for individual deal commission split calculations (`rt-sales/commission-calculation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Role, employment vs. contractor status, eligible KPIs, measurement cadence, post-termination tail rules. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Publish written variable compensation plan prior to period — HR/Leadership — Pre-cycle.
2. Ensure payroll compliance for W-2/CLT vs. output-only pay for independent agents — HR/Legal — Review.
3. Define post-termination commission rules for pending escrows — Legal — Policy.

## Rules & Criteria
Statutory: Prohibits clawing back earned commissions after closing absent broker misconduct.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `performance-compensation` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Gerente de RH / Jurídico Trabalhista**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `performance-compensation` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `performance-compensation` request missing mandatory inputs (Role) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de RH / Jurídico Trabalhista** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
