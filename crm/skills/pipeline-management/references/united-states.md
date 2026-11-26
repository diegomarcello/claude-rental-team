---
plugin: rt-crm
skill: pipeline-management
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de Operações / RevOps
---

# CRM Pipeline Management (Sales & Leasing Funnels)

## Objective & Triggers
Define clear pipeline stages, objective entry/exit criteria, maximum stage aging SLAs, and loss/stagnation rules across sales, leasing, and listing-acquisition funnels.
- **Triggers:** Invoke `rt-crm/pipeline-management` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for deduplication or retention purging (`crm-data-hygiene`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Target funnel (Sales, Leasing, Acquisitions/Listings), current CRM stages, historical stage conversion and aging metrics. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Structure stages around verifiable commitments (New Lead -> Qualified -> Tour Scheduled -> Tour Completed -> Offer/Application -> Underwriting/Contract -> Closed Won/Lost) — RevOps — Setup.
2. Configure stage-aging alerts — RevOps — Automated.
3. Enforce mandatory structured Loss Reason codes before closing a deal as Lost — Sales/Leasing — Continuous.

## Rules & Criteria
Market practice: Keep pipelines to 6–8 objective stages; enforce mandatory Stage Gate fields before advancing deals.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `pipeline-management` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Gerente de Operações / RevOps**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `pipeline-management` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `pipeline-management` request missing mandatory inputs (Target funnel (Sales) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de Operações / RevOps** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
