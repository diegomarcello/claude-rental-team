---
plugin: rt-post-sales
skill: customer-retention
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Sucesso do Cliente
---

# Customer Retention, NPS & Referral Programs

## Objective & Triggers
Measure NPS/CSAT at key lifecycle milestones, trigger proactive detractor recovery, and drive compliant landlord/buyer referrals.
- **Triggers:** Invoke `rt-post-sales/customer-retention` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for technical CRM workflow setup (`rt-crm/journey-automation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Completed milestone, NPS score (0–10), verbatim feedback. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Trigger transactional NPS survey 7 days post-closing or 60 days post-move-in — CS Automation — D+7 / D+60.
2. Trigger 'Detractor (0–6)' manager outreach within 24h — CS Manager — <= 24h.
3. Invite 'Promoters (9–10)' to review on Google and join compliant referral programs — CS — D+3.

## Rules & Criteria
Statutory: In the US, paying cash/gift-card referral fees to unlicensed individuals violates state licensing acts and RESPA § 8.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
**NPS Formula:** $\text{NPS} = \%\text{Promoters (9–10)} - \%\text{Detractors (0–6)}$ (scale -100 to +100).

## Outputs
Standardized `customer-retention` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador de Sucesso do Cliente**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `customer-retention` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `customer-retention` request missing mandatory inputs (Completed milestone) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Sucesso do Cliente** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
