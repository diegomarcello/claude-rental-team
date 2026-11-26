---
plugin: rt-executive
skill: company-kpis
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Controller / CFO
---

# Executive KPIs Dashboard (Sales, Leasing, Renovation & Cash)

## Objective & Triggers
Define, compute, and audit core real estate KPIs across sales, leasing, renovation, and cash management with standardized formulas, benchmarks, and cadence.
- **Triggers:** Invoke `rt-executive/company-kpis` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for daily treasury forecasting (`rt-finance/cash-flow-forecast`) or BI warehouse schema design (`rt-technology-data/bi-reporting`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Closed sales volume, commission revenue, active managed doors, physical/economic vacancy, delinquency (>30d), CapEx variance, cash balance, and OPEX. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Extract closed ERP/CRM figures by Business Day 3 — Controller — Monthly.
2. Compute business-line KPIs against budget and prior period — FP&A — Day 4.
3. Flag critical variances (> 10% off target) with remediation plans — Department Heads — Day 5.

## Rules & Criteria
Market practice (Benchmarks): Portfolio physical vacancy < 5%; 30+ day delinquency < 2.5%; Annual owner churn < 12%; Lead-to-tour conversion > 15%; Renovation budget variance <= 5%. Company decision: `[PENDING: Confirm official submarket KPI targets]`.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**Standardized Formulas (Rounding: 2 decimal places):**
- $\text{Physical Vacancy (\%)} = \frac{\text{Vacant Units}}{\text{Total Managed Units}} \times 100$
- $\text{Delinquency Rate (\%)} = \frac{\text{Rent Past Due > 30d}}{\text{Total Monthly Billed Rent}} \times 100$
- $\text{Owner Churn (\%)} = \frac{\text{Lost Doors in Period}}{\text{Beginning Doors}} \times 100$
- **Numerical Example:** 400 managed doors, 16 vacant; monthly billed rent = $1,200,000, 30+ day arrears = $24,000:
  - $\text{Physical Vacancy} = (16 / 400) \times 100 = \mathbf{4.00\%}$
  - $\text{Delinquency Rate} = (24,000 / 1,200,000) \times 100 = \mathbf{2.00\%}$.

## Outputs
Standardized `company-kpis` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Controller / CFO**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `company-kpis` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `company-kpis` request missing Member State or core inputs (Closed sales volume) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Controller / CFO** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
