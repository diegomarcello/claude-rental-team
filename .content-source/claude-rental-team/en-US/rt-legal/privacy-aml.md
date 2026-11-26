---
plugin: rt-legal
skill: privacy-aml
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: DPO / Compliance Officer (MLRO)
---

# Privacy Governance (ROPA) & AML/KYC Compliance

## Objective & Triggers
Operationalize Record of Processing Activities (ROPA), KYC/UBO onboarding files, AML risk scoring matrices, and regulatory reporting workflows (COAF/ANPD, FinCEN/FTC, EU FIUs/DPAs).
- **Triggers:** Invoke `rt-legal/privacy-aml` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for general statutory lookup without operational workflow execution (`rt-jurisdictions/*/privacy` & `aml`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Party identification (individual/entity), corporate/UBO docs, source of funds, data capture channel, consent timestamps. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Collect KYC intake and ID/UBO verification documents — Sales/Compliance — Pre-contract.
2. Screen PEP, OFAC/EU sanctions lists and evaluate AML red flags — Compliance — Pre-contract.
3. Log GDPR/LGPD/CCPA lawful basis in ROPA and enforce retention schedules — DPO — Continuous.
4. Escalate high-risk flags to MLRO/DPO for decision or confidential SAR/STR filing — Compliance — Immediate.

## Rules & Criteria
Statutory: Retain KYC/AML files for at least 5 years (10 years in Spain) in an encrypted, access-controlled repository.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `privacy-aml` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **DPO / Compliance Officer (MLRO)**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `privacy-aml` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `privacy-aml` request missing mandatory inputs (Party identification (individual/entity)) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **DPO / Compliance Officer (MLRO)** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
