---
plugin: rt-human-resources
skill: recruiting
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de RH / Jurídico Trabalhista
---

# Recruiting, Licensing Verification & Bias-Free Hiring

## Objective & Triggers
Draft job descriptions, verify mandatory brokerage/professional licenses, and run structured interviews free of discriminatory inquiries.
- **Triggers:** Invoke `rt-human-resources/recruiting` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for construction contractor onboarding (`rt-procurement/vendor-management`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Role title, engagement classification, required licenses, compensation range. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Verify statutory licensing requirements — HR — Pre-posting.
2. Publish inclusive job post and run structured interviews — HR/Hiring Manager — Selection.
3. Verify active license standing prior to offer — HR — Pre-offer.

## Rules & Criteria
Statutory: Employment anti-discrimination laws (US Title VII/ADA/ADEA; EU Directive 2000/78/EC; BR Lei 9.029/95).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `recruiting` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Gerente de RH / Jurídico Trabalhista**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `recruiting` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `recruiting` request missing mandatory inputs (Role title) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de RH / Jurídico Trabalhista** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
