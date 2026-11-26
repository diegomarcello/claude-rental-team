---
plugin: rt-crm
skill: crm-data-hygiene
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Administrador de CRM / DPO
---

# CRM Data Hygiene, Deduplication & Retention Purging

## Objective & Triggers
Maintain CRM database integrity through input validation rules, contact/property deduplication, and scheduled archiving/anonymization per statutory retention limits.
- **Triggers:** Invoke `rt-crm/crm-data-hygiene` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for building automated outreach flows (`journey-automation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: CRM contact and property tables, unique identifiers (email, E.164 phone, tax ID, parcel/title ID), retention schedule. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Enforce input normalization (E.164 phone, lowercase email, tax/parcel ID validation) — RevOps — Automated.
2. Run monthly duplicate merge jobs preserving full activity timelines — CRM Admin — Monthly.
3. Anonymize inactive non-customer leads past retention window and execute erasure requests — DPO/CRM Admin — Quarterly.

## Rules & Criteria
Statutory: Data accuracy and storage limitation principles (GDPR Art. 5(1)(d)–(e); LGPD Art. 6 V & Art. 16).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `crm-data-hygiene` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Administrador de CRM / DPO**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `crm-data-hygiene` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `crm-data-hygiene` request missing mandatory inputs (CRM contact and property tables) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Administrador de CRM / DPO** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
