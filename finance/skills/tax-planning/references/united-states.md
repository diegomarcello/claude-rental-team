---
plugin: rt-finance
skill: tax-planning
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Contador Tributarista / CPA
---

# Tax Planning & Statutory Compliance Calendar

## Objective & Triggers
Compare tax regimes across business lines and maintain statutory filing calendars.
- **Triggers:** Invoke `rt-finance/tax-planning` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for generic jurisdictional tax lookups (`rt-jurisdictions/*/taxes`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Revenue by business line, operating margins, payroll expense, current legal entity structure. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Segregate revenue streams by tax character — CPA/Tax Advisor — Quarterly.
2. Model entity/regime elections prior to fiscal year cutoff — CPA — Q4.
3. Maintain automated tax filing calendar with dual review — Tax Team — Monthly.

## Rules & Criteria
Statutory: Maintain genuine business purpose and entity separateness across SPVs/LLCs.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `tax-planning` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Contador Tributarista / CPA**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `tax-planning` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `tax-planning` request missing mandatory inputs (Revenue by business line) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Contador Tributarista / CPA** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
