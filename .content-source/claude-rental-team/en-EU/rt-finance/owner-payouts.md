---
plugin: rt-finance
skill: owner-payouts
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador Financeiro / Contador
---

# Landlord Statements & Monthly Owner Payouts

## Objective & Triggers
Compute net monthly owner disbursements, issue itemized owner statements, and feed annual tax reporting (1099-MISC / DIMOB).
- **Triggers:** Invoke `rt-finance/owner-payouts` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for agent commission splits (`rt-sales/commission-calculation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Cleared rent collected, management fee (%), approved repair invoices, landlord tax status, bank routing/IBAN. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Confirm cleared tenant funds in trust account — Finance — D+1.
2. Deduct management fee, receipt-backed repairs, and statutory withholdings — Finance — D+2.
3. Publish itemized Owner Statement and execute payout within SLA — Finance — D+3 to D+5.
4. Consolidate annual year-end owner tax summary (1099-MISC / DIMOB) — Accounting — Annual.

## Rules & Criteria
Statutory: Fiduciary duty to provide itemized, receipt-backed accounting.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**Formula:** $\text{Net Payout} = \text{Rent} - \text{Mgmt Fee} - \text{Withholdings} - \text{Repairs}$. Example: $5,000 - 500 - 350 = \mathbf{\$4,150.00}$.

## Outputs
Standardized `owner-payouts` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador Financeiro / Contador**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `owner-payouts` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `owner-payouts` request missing Member State or core inputs (Cleared rent collected) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador Financeiro / Contador** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
