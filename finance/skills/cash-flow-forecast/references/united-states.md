---
plugin: rt-finance
skill: cash-flow-forecast
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: CFO / Tesoureiro
---

# 13-Week Direct Cash Flow Forecast & Scenario Modeling

## Objective & Triggers
Forecast operating cash inflows and outflows over a rolling 13-week horizon with minimum liquidity alerts.
- **Triggers:** Invoke `rt-finance/cash-flow-forecast` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for individual landlord remittance statements (`owner-payouts`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Opening operating cash balance, probability-weighted AR, committed AP, payroll, and tax schedules. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Strictly segregate operating cash from client trust balances — Treasurer — Monday.
2. Project weekly probability-weighted inflows — FP&A — Monday.
3. Project outflows and stress-test downside (-20% closings) — FP&A — Tuesday.
4. Trigger red alert if projected cash breaches minimum floor — CFO — Tuesday.

## Rules & Criteria
Market practice: Rolling 13-week forecast updated weekly; minimum operating cash buffer >= 3 months fixed overhead.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
**Formula:** $\text{Ending Cash}_t = \text{Beginning Cash}_t + \text{Inflows}_t - \text{Outflows}_t - \text{CapEx}_t$. Example: $250k + 110k - 100k = \mathbf{\$260k}$.

## Outputs
Standardized `cash-flow-forecast` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **CFO / Tesoureiro**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `cash-flow-forecast` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `cash-flow-forecast` request missing mandatory inputs (Opening operating cash balance) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **CFO / Tesoureiro** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
