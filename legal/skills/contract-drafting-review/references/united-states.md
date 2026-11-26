---
plugin: rt-legal
skill: contract-drafting-review
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Advogado Imobiliário
---

# Real Estate Contract Drafting & Review

## Objective & Triggers
Draft and review purchase agreements, leases, property management agreements, brokerage mandates, and construction contracts, enforcing mandatory statutory clauses and flagging unconscionable terms.
- **Triggers:** Invoke `rt-legal/contract-drafting-review` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for commercial price haggling without contract drafting/review (`rt-sales/proposal-negotiation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Contract type, jurisdiction, party details, property description, price/rent, timelines, security/guarantees, company base templates. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Select approved jurisdictional template — Legal — Day 0.
2. Populate party details, premises, economics, security, and special riders — Counsel — Day 1.
3. Audit mandatory statutory disclosures/clauses and strip unenforceable terms — Senior Counsel — Day 1.
4. Route for e-signature post-approval gate clearance — Operations — Day 2.

## Rules & Criteria
Statutory: Prohibition on pre-dispute waivers of non-waivable tenant/consumer statutory rights; e-signature validity governed by ESIGN/UETA (US), eIDAS (EU), and MP 2.200-2/2001 (BR).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `contract-drafting-review` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Advogado Imobiliário**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `contract-drafting-review` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `contract-drafting-review` request missing mandatory inputs (Contract type) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Advogado Imobiliário** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
