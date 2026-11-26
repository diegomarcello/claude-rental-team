---
plugin: rt-human-resources
skill: employee-onboarding
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de RH / TI
---

# Employee Onboarding & Associate Broker Credentialing

## Objective & Triggers
Execute documentary, contractual, and IT onboarding while strictly separating statutory employees from independent associate brokers.
- **Triggers:** Invoke `rt-human-resources/employee-onboarding` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for maintenance/construction vendors (`rt-procurement/vendor-management`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Engagement classification, personal/tax forms, active brokerage license, team assignment, RBAC profile. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Collect classification-specific paperwork (W-2/CLT/CDI vs. Associate Broker IRC § 3508 / BR Lei 6.530/78) — HR — Pre-start.
2. Provision RBAC accounts with MFA — IT — Day 1.
3. Complete mandatory compliance training within 7 days — HR/Compliance — D+7.

## Rules & Criteria
Statutory: US IRC § 3508 statutory nonemployee criteria; BR Lei 6.530/78 art. 6 §2.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `employee-onboarding` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Gerente de RH / TI**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `employee-onboarding` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `employee-onboarding` request missing mandatory inputs (Engagement classification) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de RH / TI** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
