---
plugin: rt-technology-data
skill: bi-reporting
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro de Dados / Controller
---

# Analytics Data Model & BI Reporting

## Objective & Triggers
Structure dimensional data models unifying CRM, financial ERP, and construction data for executive BI dashboards with Row-Level Security.
- **Triggers:** Invoke `rt-technology-data/bi-reporting` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use to define business KPI formulas (`rt-executive/company-kpis`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Integrated data sources, KPI dictionary, RBAC/RLS access levels. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Model star-schema dimensions and facts with PII masking — Data Engineer — Setup.
2. Reconcile BI totals against ERP general ledger prior to release — Controller/Data — UAT.
3. Enforce Row-Level Security (RLS) by portfolio/role — BI/InfoSec — Production.

## Rules & Criteria
Statutory: Data minimization and pseudonymization in analytics warehouses (GDPR Art. 89; LGPD Art. 13).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `bi-reporting` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Engenheiro de Dados / Controller**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `bi-reporting` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `bi-reporting` request missing mandatory inputs (Integrated data sources) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Engenheiro de Dados / Controller** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
