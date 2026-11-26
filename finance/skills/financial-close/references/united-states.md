---
plugin: rt-finance
skill: financial-close
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Controller / Contador
---

# Monthly Financial Close & Revenue Recognition

## Objective & Triggers
Execute monthly accounting close by Business Day 5 covering bank/trust reconciliations and accrual revenue recognition (ASC 606 / IFRS 15).
- **Triggers:** Invoke `rt-finance/financial-close` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for annual tax structuring (`tax-planning`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: General ledger, bank statements, ERP sub-ledgers, payroll registers, invoices. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. D+1 to D+2: Complete bank and trust reconciliations — Staff Accountants — D+2.
2. D+3: Recognize revenue under ASC 606 / IFRS 15 — Senior Accountant — D+3.
3. D+4: Review trial balance and business-line P&L — Controller — D+4.
4. D+5: Lock period and publish executive reporting package — CFO — D+5.

## Rules & Criteria
Statutory / GAAP: ASC 606 / IFRS 15 — Brokerage commission revenue recognized upon closing.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `financial-close` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Controller / Contador**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `financial-close` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `financial-close` request missing mandatory inputs (General ledger) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Controller / Contador** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
