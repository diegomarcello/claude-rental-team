---
plugin: rt-finance
skill: accounts-payable
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador Financeiro / Controller
---

# Accounts Payable, Tax Withholding & Payment Fraud Prevention

## Objective & Triggers
Process vendor, contractor, and utility disbursements using 3-way matching (PO x Delivery/Inspection x Invoice), tax withholding calculation, and anti-fraud wire/ACH/boleto verification.
- **Triggers:** Invoke `rt-finance/accounts-payable` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for monthly landlord rental remittances (`owner-payouts`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Vendor invoice, approved PO/inspection sign-off, payee tax/bank details, vendor tax classification, approval gate threshold. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Perform 3-way match (Approved PO + Verified Delivery/Inspection + Valid Invoice) — AP Analyst — Day 0.
2. Calculate statutory withholdings — Tax/AP — Day 1.
3. Execute out-of-band phone call-back verification on any vendor bank/wire change — AP Analyst — Pre-payment.
4. Route batch to segregated approver and disburse — Controller/Director — Payment.

## Rules & Criteria
Governance / Internal Control: Never update vendor or landlord bank routing/IBAN details based solely on an email request.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
**Numerical Example (US Vendor Invoice $10,000 without valid Form W-9 — IRC § 3406):** 24% Backup Withholding ($2,400) -> Net = **$7,600.00**.

## Outputs
Standardized `accounts-payable` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador Financeiro / Controller**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `accounts-payable` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `accounts-payable` request missing mandatory inputs (Vendor invoice) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador Financeiro / Controller** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
