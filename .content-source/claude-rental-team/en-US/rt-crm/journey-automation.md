---
plugin: rt-crm
skill: journey-automation
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Especialista de Automação CRM
---

# Lifecycle Journey Automation & Event Triggers

## Objective & Triggers
Configure automated CRM workflows for landlord/tenant onboarding, lease renewal alerts, contract anniversaries, and reactivation, enforcing consent gates and exit triggers.
- **Triggers:** Invoke `rt-crm/journey-automation` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for cold outbound prospecting (`rt-pre-sales/follow-up-cadence`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Trigger event, channel, opt-in flag, exit conditions. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Enforce entry guardrails (active opt-in + no legal hold) — RevOps — Setup.
2. Configure workflow steps and instant exit triggers — CRM Admin — Setup.
3. Audit delivery rates and opt-outs weekly — RevOps — Weekly.

## Rules & Criteria
Statutory / Carrier Rule: Use only approved business messaging APIs with registered templates and opt-out handling.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `journey-automation` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Especialista de Automação CRM**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `journey-automation` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `journey-automation` request missing mandatory inputs (Trigger event) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Especialista de Automação CRM** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
