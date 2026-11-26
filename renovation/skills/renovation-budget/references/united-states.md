---
plugin: rt-renovation
skill: renovation-budget
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro Orçamentista / Controller
---

# Renovation Budget, Markup (BDI) & Variance Control

## Objective & Triggers
Build itemized renovation budgets with takeoffs, benchmark unit costs (SINAPI/TCPO/RSMeans), overhead/profit (BDI), contingency reserves, and budget-vs-actual variance tracking.
- **Triggers:** Invoke `rt-renovation/renovation-budget` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for leveling competing contractor bids (`rt-procurement/quote-comparison`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Scope of work, quantity takeoffs, regional cost database, contingency rate, and contracting model (lump sum vs. cost-plus). | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Perform quantity takeoffs for every SOW line item — Estimator — Day 1.
2. Apply unit material & labor rates plus burden/overhead & profit — Estimator — Day 2.
3. Add contingency reserve (10% cosmetic turn; 15%–20% heavy/older-building rehab) — Construction Manager — Day 2.
4. Track weekly committed vs. spent costs and require signed Change Orders before extra work — Construction Manager — Weekly.

## Rules & Criteria
Market practice: Typical contractor overhead & profit (GC fee) ranges 15%–25% depending on scope and risk. Block disbursements exceeding approved line items without a signed Change Order.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
**Budget & Variance Formulas:**
$$\text{Total Budget} = \text{Direct Cost} \times (1 + \text{GC Overhead/Profit}) \times (1 + \text{Contingency})$$
$$\text{Budget Variance (\%)} = \frac{\text{Actual Cost} - \text{Baseline Budget}}{\text{Baseline Budget}} \times 100$$
- **Numerical Example:** Direct Cost = $80,000; GC Overhead/Profit = 20%; Contingency = 10%:
  - $\text{Subtotal w/ GC Fee} = \$80,000 \times 1.20 = \mathbf{\$96,000}$
  - $\text{Total Budget w/ 10\% Contingency} = \$96,000 \times 1.10 = \mathbf{\$105,600.00}$.
  - If final actuals equal $101,000: $\text{Variance} = \frac{101,000 - 105,600}{105,600} = \mathbf{-4.36\%}$ ($4,600 under budget).

## Outputs
Standardized `renovation-budget` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Engenheiro Orçamentista / Controller**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `renovation-budget` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `renovation-budget` request missing mandatory inputs (Scope of work) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Engenheiro Orçamentista / Controller** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
