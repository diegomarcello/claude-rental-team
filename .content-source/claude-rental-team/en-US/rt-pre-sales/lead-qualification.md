---
plugin: rt-pre-sales
skill: lead-qualification
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Pré-vendas (SDR)
---

# Objective Lead Qualification (Bias-Free Screening)

## Objective & Triggers
Qualify buying and leasing leads using objective criteria (budget, move timeline, purpose, financing/guarantee readiness), scoring priority without discriminatory inquiries.
- **Triggers:** Invoke `rt-pre-sales/lead-qualification` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for formal tenant credit underwriting and final approval (`rt-property-management/tenant-screening`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Lead contact details, source listing, stated budget, timeline, financing/guarantee method. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Initiate first contact within <= 5 minutes (Speed-to-Lead) — SDR — <= 5 min.
2. Run objective discovery script (Budget, Timeline, Property Specs/Area, Payment/Financing or Lease Guarantee readiness) — SDR — Call 1.
3. Score lead (Hot: tour within <= 7 days; Warm: 30–90 day nurture; Unqualified: polite close) and hand off to Agent — SDR — Same day.

## Rules & Criteria
Statutory: Strictly prohibited to inquire about or score leads based on familial status/children, national origin, religion, sexual orientation, disability, or race (Fair Housing Act; EU Racial Equality Directive; BR Anti-Discrimination Laws).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `lead-qualification` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador de Pré-vendas (SDR)**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `lead-qualification` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `lead-qualification` request missing mandatory inputs (Lead contact details) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Pré-vendas (SDR)** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
