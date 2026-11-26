---
plugin: rt-finance
skill: financial-close
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Controller / Contador
---

# Monthly Financial Close & Revenue Recognition

## Objective & Triggers
Execute monthly accounting close by Business Day 5 covering bank/trust reconciliations and accrual revenue recognition (ASC 606 / IFRS 15).
- **Triggers:** Invoke `rt-finance/financial-close` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for annual tax structuring (`tax-planning`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: General ledger, bank statements, ERP sub-ledgers, payroll registers, invoices. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. D+1 to D+2: Complete bank and trust reconciliations — Staff Accountants — D+2.
2. D+3: Recognize revenue under ASC 606 / IFRS 15 — Senior Accountant — D+3.
3. D+4: Review trial balance and business-line P&L — Controller — D+4.
4. D+5: Lock period and publish executive reporting package — CFO — D+5.

## Rules & Criteria
Statutory / GAAP: ASC 606 / IFRS 15 — Brokerage commission revenue recognized upon closing.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `financial-close` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Controller / Contador**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `financial-close` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `financial-close` request missing Member State or core inputs (General ledger) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Controller / Contador** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
