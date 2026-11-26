---
plugin: rt-sales
skill: commission-calculation
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Controller / Gerente Comercial
---

# Brokerage Commission & Split Calculation

## Objective & Triggers
Calculate gross brokerage commission, tax/franchise deductions, splits across listing agent, buyer/leasing agent, management, and co-brokers, and verify payout triggers.
- **Triggers:** Invoke `rt-sales/commission-calculation` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for monthly landlord rental remittances (`rt-finance/owner-payouts`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Closed transaction price/rent, agreed commission rate, internal split schedule, co-broker share, applicable taxes, cleared funds status. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Verify cleared commission funds in brokerage operating account — Finance — Day 0.
2. Deduct external co-broker split (e.g., 50/50) and applicable direct fees — Controller — Day 1.
3. Apply internal split tiers (Listing side, Buyer/Leasing side, House share) and generate commission statement — Controller — Day 1.
4. Disburse upon receipt of valid contractor invoice/W-9 (or NF in BR) — Accounts Payable — Day 2.

## Rules & Criteria
Statutory: In US, commissions may only be paid to licensed brokers/agents (reported on Form 1099-NEC). In BR, associate brokers operate under Lei 6.530/78 art. 6 §2 with union-registered contract and invoice (NF). Company decision: `[PENDING: Confirm internal split percentages]`.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**Standard Split Formula:**
$$\text{Gross Commission} = \text{Sale Price} \times \text{Commission Rate}$$
- **Numerical Example ($1,000,000 sale, 6% total commission = $60,000, 50/50 co-brokerage -> $30,000 to our side; 70/30 agent/brokerage split):**
  - Agent (70%): **$21,000.00** | Brokerage House Share (30%): **$9,000.00**.

## Outputs
Standardized `commission-calculation` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Controller / Gerente Comercial**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `commission-calculation` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `commission-calculation` request missing Member State or core inputs (Closed transaction price/rent) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Controller / Gerente Comercial** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
