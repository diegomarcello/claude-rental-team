---
plugin: rt-property-management
skill: tenant-screening
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Locação / Compliance
---

# Objective Tenant Screening & Credit Underwriting

## Objective & Triggers
Evaluate rental applicants using standardized, objective numerical thresholds (income-to-rent ratio, credit score, rental history, security/guarantor), logging objective adverse reasons and dispute notices.
- **Triggers:** Invoke `rt-property-management/tenant-screening` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for pre-tour commercial lead qualification (`rt-pre-sales/lead-qualification`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Monthly rent + mandatory charges, verified gross applicant income, consumer credit/eviction report, proposed guarantee/deposit. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Obtain written applicant authorization prior to pulling consumer credit/background reports — Leasing Analyst — Day 0.
2. Compute income-to-rent ratio ($\text{Gross Income} \ge 3\times \text{Monthly Rent}$) and review credit/eviction history under uniform written criteria — Analyst — Day 1.
3. Issue objective decision — Coordinator — Day 1.
4. Deliver written FCRA Adverse Action Notice (US) or transparency disclosure (EU/BR) whenever a consumer report contributes to denial/conditions — Analyst — Immediate.

## Rules & Criteria
Statutory: Fair Housing Act; single-guarantee rule in BR (Lei 8.245/91 art. 37); exhaustive document list in France (Décret 2015-1437).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Standard market benchmark: $\text{Verified Gross Monthly Income} \ge 3.0 \times \text{Monthly Rent}$.

## Outputs
Standardized `tenant-screening` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador de Locação / Compliance**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `tenant-screening` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `tenant-screening` request missing mandatory inputs (Monthly rent + mandatory charges) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Locação / Compliance** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
