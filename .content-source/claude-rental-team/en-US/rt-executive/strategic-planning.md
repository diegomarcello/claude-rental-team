---
plugin: rt-executive
skill: strategic-planning
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Diretoria Executiva / CFO
---

# Strategic Planning & Capital Allocation

## Objective & Triggers
Structure annual/quarterly OKR planning cycles, capital allocation across property management, brokerage, and fix-and-flip/development, and geographic expansion criteria.
- **Triggers:** Invoke `rt-executive/strategic-planning` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for monthly operational metric tracking (use `company-kpis`) or single-deal underwriting (`rt-acquisitions/deal-feasibility`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Annual targets, available cash, cost of capital (WACC/Fed Funds/ECB), margin by business line, team operational capacity. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Consolidate 12M financial and operational baseline — CFO — Week 1.
2. Set recurring revenue (PM) vs. transactional (brokerage/flip) targets — CEO/Leadership — Week 2.
3. Establish own-capital exposure caps per project and submarket — Investment Committee — Week 3.
4. Cascade departmental OKRs and run quarterly reviews — Department Heads — Quarterly.

## Rules & Criteria
Statutory: Strict fiduciary segregation between client trust/escrow funds and operating/CapEx capital. Market practice: Maintain >= 6 months fixed OPEX liquidity reserve; cap single-asset principal exposure at 20% of equity. Company decision: `[PENDING: Set target revenue mix and minimum ROE hurdle]`.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable (portfolio allocation framework; deal-level IRR/NPV math in `deal-feasibility`).

## Outputs
Standardized `strategic-planning` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Diretoria Executiva / CFO**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `strategic-planning` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `strategic-planning` request missing mandatory inputs (Annual targets) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Diretoria Executiva / CFO** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
