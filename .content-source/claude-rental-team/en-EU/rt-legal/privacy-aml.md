---
plugin: rt-legal
skill: privacy-aml
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: DPO / Compliance Officer (MLRO)
---

# Privacy Governance (ROPA) & AML/KYC Compliance

## Objective & Triggers
Operationalize Record of Processing Activities (ROPA), KYC/UBO onboarding files, AML risk scoring matrices, and regulatory reporting workflows (COAF/ANPD, FinCEN/FTC, EU FIUs/DPAs).
- **Triggers:** Invoke `rt-legal/privacy-aml` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for general statutory lookup without operational workflow execution (`rt-jurisdictions/*/privacy` & `aml`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Party identification (individual/entity), corporate/UBO docs, source of funds, data capture channel, consent timestamps. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Collect KYC intake and ID/UBO verification documents — Sales/Compliance — Pre-contract.
2. Screen PEP, OFAC/EU sanctions lists and evaluate AML red flags — Compliance — Pre-contract.
3. Log GDPR/LGPD/CCPA lawful basis in ROPA and enforce retention schedules — DPO — Continuous.
4. Escalate high-risk flags to MLRO/DPO for decision or confidential SAR/STR filing — Compliance — Immediate.

## Rules & Criteria
Statutory: Retain KYC/AML files for at least 5 years (10 years in Spain) in an encrypted, access-controlled repository.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `privacy-aml` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **DPO / Compliance Officer (MLRO)**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `privacy-aml` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `privacy-aml` request missing Member State or core inputs (Party identification (individual/entity)) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **DPO / Compliance Officer (MLRO)** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
