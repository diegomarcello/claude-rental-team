---
plugin: rt-legal
skill: disputes-eviction
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Advogado Contencioso Imobiliário
---

# Legal Notices, Judicial Collections & Eviction

## Objective & Triggers
Manage legal escalation after soft collections fail: statutory default notices, cash-for-keys / surrender agreements, eviction filings, and writ of possession enforcement.
- **Triggers:** Invoke `rt-legal/disputes-eviction` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for early-stage friendly delinquency reminders <= 15 days (`rt-finance/collections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Executed lease, itemized ledger of arrears, guarantee/deposit proof, collection log, service address. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Audit statutory pre-suit notice requirements (e.g., 3-day notice in FL/TX/CA; 6-week commandement de payer in FR) — Counsel — Day 1.
2. Serve statutory notice via certified mail/process server/huissier — Counsel — Day 2.
3. Evaluate voluntary surrender / cash-for-keys vs. filing eviction complaint — Counsel/Leadership — Day 7.
4. File lawsuit and track hearing, judgment, and sheriff/bailiff lockout — Counsel — Day 10+.

## Rules & Criteria
Statutory: Strict ban on 'self-help eviction' (changing locks or shutting off utilities is illegal across US, EU, and BR). Statute of limitations for rent arrears: 3 yrs (BR/FR), 4–6 yrs (US by state).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `disputes-eviction` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Advogado Contencioso Imobiliário**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `disputes-eviction` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `disputes-eviction` request missing mandatory inputs (Executed lease) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Advogado Contencioso Imobiliário** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
