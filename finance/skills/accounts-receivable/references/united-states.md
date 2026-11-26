---
plugin: rt-finance
skill: accounts-receivable
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador Financeiro
---

# Accounts Receivable, Billing & Bank Reconciliation

## Objective & Triggers
Generate rent, pass-through expense, and commission invoices, process bank settlement files (ACH/NACHA, SEPA CAMT.053, CNAB 240/400), post cash receipts, and reconcile trust/operating accounts daily.
- **Triggers:** Invoke `rt-finance/accounts-receivable` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for delinquent collections outreach (`collections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Active ERP lease schedules, monthly pass-through charges, bank statements/files. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Consolidate monthly variable pass-through charges by D-10 — AR Analyst — D-10.
2. Issue rent invoices / initiate ACH or SEPA Direct Debit runs by D-7 — System/AR — D-7.
3. Import daily bank settlement files and reconcile trust/escrow sub-ledgers daily — AR Analyst — Daily.

## Rules & Criteria
Statutory: Strict separation between operating accounts and client trust/escrow accounts.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
**AR Aging Buckets:** Current, 1–15d, 16–30d, 31–60d, 61–90d, > 90d.

## Outputs
Standardized `accounts-receivable` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador Financeiro**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `accounts-receivable` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `accounts-receivable` request missing mandatory inputs (Active ERP lease schedules) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador Financeiro** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
