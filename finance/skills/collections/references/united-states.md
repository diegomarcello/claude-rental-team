---
plugin: rt-finance
skill: collections
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Cobrança / Jurídico
---

# Delinquent Rent Collections & Statutory Limits

## Objective & Triggers
Execute structured past-due rent collection cadences (D+1 to D+30), applying late fees and interest within statutory caps while strictly prohibiting abusive or harassing collection tactics.
- **Triggers:** Invoke `rt-finance/collections` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for judicial eviction filings (`rt-legal/disputes-eviction`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Lease terms, past-due balance, due date, contractual late fee/interest rate, active guarantee/deposit. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. D+1 to D+3: Automated friendly payment reminder — Finance Automation — D+1.
2. D+5 to D+10: Direct outreach with updated ledger including statutory late fees — Collections Analyst — D+5.
3. D+15: Formal default warning and guarantor/surety notice — Collections — D+15.
4. D+30 unresolved: Escalate to `rt-legal/disputes-eviction` — Coordinator — D+30.

## Rules & Criteria
Statutory: Strict ban on harassment or third-party disclosure (US FDCPA; BR CDC arts. 42 & 71; FR Loi 1989 art. 4).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `collections` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador de Cobrança / Jurídico**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `collections` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `collections` request missing mandatory inputs (Lease terms) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Cobrança / Jurídico** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
