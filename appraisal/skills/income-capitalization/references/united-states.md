---
plugin: rt-appraisal
skill: income-capitalization
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Avaliador Habilitado / Analista de Investimentos
---

# Income Capitalization Approach (Direct Cap & DCF)

## Objective & Triggers
Value commercial, multifamily, and rental portfolios via Direct Capitalization of Net Operating Income (NOI) or Discounted Cash Flow (DCF).
- **Triggers:** Invoke `rt-appraisal/income-capitalization` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for owner-occupied single-family residences driven by sales comps (`comparative-market-analysis`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Potential Gross Income (PGI), vacancy & credit loss rate, landlord operating expenses (OPEX: property tax, insurance, R&M, management fee, CapEx reserve), market Cap Rate or discount rate + exit Cap Rate. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Compute Potential Gross Income (PGI) from in-place leases and market rents — Analyst — Day 1.
2. Deduct vacancy/credit loss to derive Effective Gross Income (EGI) and subtract OPEX for NOI — Analyst — Day 1.
3. Apply Direct Cap ($V = NOI / R$) and/or 5–10 year DCF with terminal value — Valuer — Day 2.
4. Build sensitivity table (Cap Rate +/- 50 bps vs. NOI +/- 5%) — Valuer — Day 2.

## Rules & Criteria
Standards: NBR 14653-2 (Income Method), USPAP SR 1-4(c), RICS Red Book / IVS 105. Critical rule: Never include debt service (principal/interest) or owner income taxes inside OPEX when computing NOI.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
**Income Capitalization Formulas:**
$$EGI = PGI \times (1 - v) + \text{Other Income}$$
$$NOI = EGI - OPEX_{\text{landlord}}$$
$$\text{Direct Cap Value} = \frac{NOI}{\text{Cap Rate}}$$
- **Numerical Example (Commercial Retail/Office Asset):**
  - Annual PGI = $240,000 | Vacancy & Credit Loss (5%) = -$12,000 -> EGI = **$228,000**
  - Landlord OPEX (Taxes $22k + Insurance $6k + R&M/PM $20k) = **$48,000**
  - $NOI = 228,000 - 48,000 = \mathbf{\$180,000/\text{yr}}$
  - At **7.50%** Market Cap Rate: $\text{Value} = \frac{180,000}{0.075} = \mathbf{\$2,400,000.00}$.

## Outputs
Standardized `income-capitalization` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Avaliador Habilitado / Analista de Investimentos**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `income-capitalization` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `income-capitalization` request missing mandatory inputs (Potential Gross Income (PGI)) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Avaliador Habilitado / Analista de Investimentos** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
