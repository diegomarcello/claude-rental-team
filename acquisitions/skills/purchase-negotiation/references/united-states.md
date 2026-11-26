---
plugin: rt-acquisitions
skill: purchase-negotiation
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Diretor de Aquisições / Jurídico
---

# Purchase Negotiation, Earnest Money & Contingencies

## Objective & Triggers
Structure purchase offers, negotiation anchors, protected earnest money deposits governed by conditions precedent (due diligence, financing, vacant possession), and penalty-free walk-away triggers.
- **Triggers:** Invoke `rt-acquisitions/purchase-negotiation` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for brokerage client resale negotiations (`rt-sales/proposal-negotiation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Approved maximum walk-away price, asset physical/title status, due diligence timelines, payment schedule. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Set initial anchor bid and approved ceiling price from underwriting — Acquisitions Manager — Day 0.
2. Draft LOI or Binding Offer with explicit conditions precedent — Legal/Acquisitions — Day 1.
3. Release earnest money only after preliminary title check and into protected escrow — Finance/Legal — Day 3.
4. Execute price-reduction addendum if inspection/title uncovers hidden liabilities — Acquisitions/Legal — During DD.

## Rules & Criteria
Statutory: Earnest money forfeiture vs. walk-away protection governed by PSA contingency clauses. Market practice: Condition closing on satisfactory title commitment, inspection, and vacant possession within 15–30 days with 100% earnest money refund upon contingency failure.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable (negotiation playbook and protective clauses).

## Outputs
Standardized `purchase-negotiation` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Diretor de Aquisições / Jurídico**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `purchase-negotiation` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `purchase-negotiation` request missing mandatory inputs (Approved maximum walk-away price) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Diretor de Aquisições / Jurídico** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
