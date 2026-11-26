---
plugin: rt-post-sales
skill: warranty-claims
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro de Assistência Técnica
---

# Construction Warranty Claims & Latent Defects

## Objective & Triggers
Triage post-handover defect claims distinguishing statutory/contractual builder warranties from owner lack of maintenance, enforcing cure obligations within statutory limitation periods.
- **Triggers:** Invoke `rt-post-sales/warranty-claims` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for routine tenant maintenance on third-party managed rentals (`rt-property-management/maintenance-requests`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Certificate of Occupancy / handover date, affected system, photos, owner maintenance records. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Verify handover date and map affected system to statutory warranty table — Warranty Engineer — Day 1.
2. Inspect to rule out occupant misuse or lack of routine owner maintenance — Engineer — Days 2–5.
3. Enforce contractor/subcontractor warranty cure or dispatch covered repair — Warranty Team — Days 5–15.

## Rules & Criteria
Statutory: France Civil Code art. 1792 (10-yr/2-yr/1-yr); Spain LOE art. 17 (10-yr/3-yr/1-yr); Brazil CC art. 618 & ABNT NBR 17170.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `warranty-claims` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Engenheiro de Assistência Técnica**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `warranty-claims` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `warranty-claims` request missing mandatory inputs (Certificate of Occupancy / handover date) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Engenheiro de Assistência Técnica** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
