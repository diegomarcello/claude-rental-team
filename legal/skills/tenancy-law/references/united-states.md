---
plugin: rt-legal
skill: tenancy-law
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Advogado Imobiliário
---

# Tenancy Law Advisory & Precedent Guide

## Objective & Triggers
Resolve day-to-day operational questions on landlord-tenant rights and duties (improvements, right of first refusal, subletting, sale of tenant-occupied property, repair allocation).
- **Triggers:** Invoke `rt-legal/tenancy-law` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use once formal default or litigation is triggered (`disputes-eviction`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Jurisdiction, relevant lease clause, factual scenario, dates, and prior notices sent. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Identify mandatory vs. default statutory rule in the jurisdiction — Counsel — Same day.
2. Cross-check against executed lease language — Counsel — Same day.
3. Recommend preventive action with notice template if needed — Counsel — Within 24h.

## Rules & Criteria
Statutory (Key examples): Tenant right of first refusal upon sale (FR Loi 1989 art. 15-II; BR Lei 8.245/91 art. 27 — 30 days). Essential habitability repairs remain landlord duty regardless of lease waivers.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `tenancy-law` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Advogado Imobiliário**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `tenancy-law` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `tenancy-law` request missing mandatory inputs (Jurisdiction) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Advogado Imobiliário** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
