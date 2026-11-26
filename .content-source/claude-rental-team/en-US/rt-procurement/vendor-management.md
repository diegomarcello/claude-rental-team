---
plugin: rt-procurement
skill: vendor-management
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Compras / Compliance
---

# Vendor Onboarding, Compliance & Joint-Employer Risk Control

## Objective & Triggers
Vet and monitor contractors and suppliers by verifying tax status, insurance (General Liability / Workers' Comp), trade licenses, and independent-contractor compliance.
- **Triggers:** Invoke `rt-procurement/vendor-management` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for hiring internal employees or associate brokers (`rt-human-resources/recruiting`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Tax ID, tax/social-security clearance certificates, active COI (GL & Workers' Comp), trade license, references. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Require onboarding packet before issuing first PO — Procurement — Pre-onboarding.
2. Automatically block ERP payments/POs when insurance or licenses expire — System/Procurement — Automated.
3. Score post-job performance quarterly — Construction/PM — Quarterly.

## Rules & Criteria
Statutory: Subcontractor joint/vicarious liability for unpaid wages or uninsured jobsite injuries.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `vendor-management` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador de Compras / Compliance**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `vendor-management` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `vendor-management` request missing mandatory inputs (Tax ID) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Compras / Compliance** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
