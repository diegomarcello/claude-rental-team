---
plugin: rt-acquisitions
skill: deal-feasibility
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Diretor de Aquisições / CFO
---

# Deal Feasibility & Underwriting Model (ROI, IRR, NPV)

## Objective & Triggers
Model full acquisition cash flows including entry closing costs, carrying costs, CapEx/renovation, exit selling costs, taxes, and return metrics (Net Margin, ROI, IRR, NPV) across base, upside, and downside scenarios.
- **Triggers:** Invoke `rt-acquisitions/deal-feasibility` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for standalone market valuation without project cash flows (`rt-appraisal/comparative-market-analysis`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Purchase price, entry closing/transfer costs, rehab budget + contingency, holding timeline (months), monthly carry (property tax, HOA, insurance, debt service), ARV (exit price), exit brokerage & taxes, hurdle rate (discount rate). | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Consolidate validated inputs (CMA-backed ARV + rehab estimate + preliminary title) — Acquisitions Analyst — Day 1.
2. Build monthly cash flow schedule and compute ROI, monthly/annual IRR, and NPV — Analyst — Day 2.
3. Run sensitivity matrix (-10% ARV, +15% CapEx, +3 months exit delay) — Analyst — Day 2.
4. Submit to Investment Committee for offer approval — Acquisitions Director — Day 3.

## Rules & Criteria
Market practice: Include 10%–15% renovation contingency; stress-test 90-day exit delay and 5%–10% ARV compression. Company decision: `[PENDING: Set minimum IRR hurdle and net margin threshold]`.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**Financial Formulas (Rounding: 2 decimal places):**
- $\text{Total Project Cost} = \text{Purchase} + \text{Entry Closing} + \text{Rehab (w/ Contingency)} + \text{Total Carry} + \text{Exit Selling/Tax Costs}$
- $\text{Net Profit} = \text{ARV} - \text{Total Project Cost}$
- $\text{Cash-on-Cash / Simple ROI (\%)} = \frac{\text{Net Profit}}{\text{Total Cash Invested}} \times 100$
- $\text{NPV} = \sum_{t=0}^{n} \frac{CF_t}{(1 + r)^t}$ and $\text{Annualized IRR} = (1 + \text{IRR}_{\text{monthly}})^{12} - 1$
- **Numerical Example (8-month unlevered flip):**
  - Purchase: $500,000 | Entry Closing (2%): $10,000 | Rehab: $110,000 | Carry (8m x $2,000): $16,000 | Exit Costs (6% brokerage + 1.5% transfer/closing on $800k ARV): $60,000.
  - $\text{Total Cost} = 500k + 10k + 110k + 16k + 60k = \mathbf{\$696,000}$.
  - $\text{Net Profit} = 800k - 696k = \mathbf{\$104,000}$ | $\text{ROI on $636k cash invested} = \mathbf{16.35\%}$ in 8 months (~**25.49% annualized**).

## Outputs
Standardized `deal-feasibility` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Diretor de Aquisições / CFO**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `deal-feasibility` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `deal-feasibility` request missing Member State or core inputs (Purchase price) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Diretor de Aquisições / CFO** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
