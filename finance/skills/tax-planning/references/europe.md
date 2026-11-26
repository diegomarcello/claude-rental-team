---
plugin: rt-finance
skill: tax-planning
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Contador Tributarista / CPA
---

# Tax Planning & Statutory Compliance Calendar

## Objective & Triggers
Compare tax regimes across business lines and maintain statutory filing calendars.
- **Triggers:** Invoke `rt-finance/tax-planning` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for generic jurisdictional tax lookups (`rt-jurisdictions/*/taxes`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Revenue by business line, operating margins, payroll expense, current legal entity structure. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Segregate revenue streams by tax character — CPA/Tax Advisor — Quarterly.
2. Model entity/regime elections prior to fiscal year cutoff — CPA — Q4.
3. Maintain automated tax filing calendar with dual review — Tax Team — Monthly.

## Rules & Criteria
Statutory: Maintain genuine business purpose and entity separateness across SPVs/LLCs.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `tax-planning` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Contador Tributarista / CPA**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `tax-planning` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `tax-planning` request missing Member State or core inputs (Revenue by business line) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Contador Tributarista / CPA** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
