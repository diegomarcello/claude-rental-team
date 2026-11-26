---
plugin: rt-sales
skill: financing-simulation
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Consultor de Crédito Imobiliário
---

# Mortgage & Financing Simulation (SAC, Price/Annuity & Fixed-Rate)

## Objective & Triggers
Simulate loan payments, interest, principal amortization, mandatory mortgage insurance (PMI / MIP-DFI), and debt-to-income (DTI) limits across French Annuity/Price (US/EU) and SAC (Brazil) systems, with mandatory non-binding disclosures.
- **Triggers:** Invoke `rt-sales/financing-simulation` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use as an official bank loan commitment (only licensed lenders underwrite and issue binding loan commitments).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Property price, down payment, term (months), annual interest rate, amortization method (French Annuity/Price vs. SAC), gross monthly borrower income. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Compute loan principal ($PV = \text{Price} - \text{Down Payment}$) and LTV ($PV / \text{Price}$) — Advisor — Immediate.
2. Calculate payment schedule under selected system (Annuity/Price vs. SAC) + estimated insurance/escrows — Advisor — Immediate.
3. Check Debt-to-Income (DTI / DSTI) ratio (US QM <= 43% back-end; EU/France HCSF & Portugal <= 35% DSTI; BR <= 30% gross income) — Advisor — Immediate.
4. Display mandatory disclaimer that figures are illustrative estimates subject to lender underwriting — System — Mandatory.

## Rules & Criteria
Statutory: Mandatory disclaimer that simulation is not a binding credit offer (EU MCD Directive 2014/17/EU; US TILA/Reg Z 12 CFR § 1026.24; BR CMN Res. 4.676/2018).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**Amortization Formulas (Monthly rate $i$):**
- **Fixed-Rate Annuity / Price (Standard US/EU & BR option):**
  $$PMT = PV \times \frac{i(1+i)^n}{(1+i)^n - 1}$$
- **Constant Amortization / SAC (Standard BR):**
  $$A = \frac{PV}{n}, \quad I_t = OB_{t-1} \times i, \quad PMT_t = A + I_t$$
- **Numerical Example ($PV = \$400,000$, $n = 360\text{ months}$, $6.60\%\text{ APR} \Rightarrow i = 0.55\%/\text{mo}$):**
  - **Fixed Annuity:** $PMT = 400,000 \times \frac{0.0055(1.0055)^{360}}{(1.0055)^{360}-1} = \mathbf{\$2,554.63/\text{mo}}$ (P&I only).
  - **SAC (Month 1):** $A = 400,000/360 = \$1,111.11$; $I_1 = 400,000 \times 0.0055 = \$2,200.00$; $PMT_1 = \mathbf{\$3,311.11}$.

## Outputs
Standardized `financing-simulation` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Consultor de Crédito Imobiliário**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `financing-simulation` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `financing-simulation` request missing Member State or core inputs (Property price) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Consultor de Crédito Imobiliário** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
