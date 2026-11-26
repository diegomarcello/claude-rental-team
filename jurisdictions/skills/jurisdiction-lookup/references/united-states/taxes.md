---
plugin: rt-jurisdictions
skill: taxes
jurisdiction: united-states
last_verified: 2026-11-25
confidence: verified
reviewer: US Real Estate CPA
---

# Jurisdiction United States — Real Estate Taxation (Federal IRC, 1031 Exchange, Depreciation, State Property/Income Tax)

## Objective & Triggers
Map US federal and state real estate tax rules covering rental income, MACRS depreciation, passive activity rules, capital gains, IRC § 1031 like-kind exchanges, property taxes, and 1099 reporting.
- **Triggers:** 'US rental property depreciation', '1031 exchange deadlines', 'capital gains on US real estate', 'Florida vs Texas vs California property tax'.

## When Not to Use
- Do not use for entity formation tax election or final tax return filing (use `rt-finance/tax-planning`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Taxpayer status (US Citizen/Resident, LLC, C-Corp, Foreign NRA) | Yes | Enum | Entity Profile |
| Activity type (Long-term rental, Short-term rental, Fix & Flip dealer property) | Yes | Enum | Business Line |
| Acquisition cost, land allocation, holding period, and sale price | Yes | Numeric (USD) | Accounting |

## Process


## Rules & Criteria
- **Federal Statute (MACRS Straight-Line Depreciation — IRC § 168):** Residential rental buildings are depreciated over **27.5 years**; commercial/non-residential real property over **39 years** (mid-month convention). Land is never depreciable. Cost segregation studies can reclassify 5-, 7-, and 15-year personal property/land improvements.
- **Federal Statute (Capital Gains & Depreciation Recapture):** Long-term capital gains (> 1 year) taxed at **0%, 15%, or 20%** + **3.8% Net Investment Income Tax (NIIT, IRC § 1411)** for high earners; Unrecaptured **Section 1250 Gain** (accumulated straight-line depreciation) taxed up to **25%**. Fix-and-flip 'dealer' properties are taxed as **ordinary income** (up to 37%) + **15.3% Self-Employment Tax**.
- **Federal Statute (Primary Residence Exclusion — IRC § 121):** Exclude up to **$250,000** ($500,000 married filing jointly) of gain if owned and used as principal residence for at least 2 of the preceding 5 years.
- **Federal Statute (IRC § 1031 Like-Kind Exchange):** Defers capital gains and § 1250 recapture on investment/business real property exchanged for like-kind US real property. Strict statutory deadlines: **45 calendar days** from relinquished closing to identify replacement property in writing; **180 calendar days** (or tax return due date) to close on replacement property. Taxpayer cannot touch proceeds (must use a Qualified Intermediary).
- **State Taxes (FL / TX / CA):**
  - *Florida & Texas:* **0% state individual income tax**; TX imposes franchise tax above no-tax-due threshold ($2.47M annualized revenue); TX relies heavily on local ad valorem property taxes (~1.6%–2.2% effective rate).
  - *California:* State income/capital gains taxed as ordinary income up to **13.3%** (14.4% with SDI on wages); does not conform to federal Qualified Opportunity Zones; Prop 13 caps property tax base rate at 1% + local bonds, limited to 2% annual assessed value growth until change of ownership.
- **Information Reporting:** Form **1099-NEC** for unincorporated vendors/contractors paid >= $600/year; Form **1099-MISC** for owner rent disbursements >= $600/year; Form **1099-S** for real estate closings.

## Calculations
**Annual Straight-Line Depreciation (Residential 27.5 Years):**
$$\text{Annual Depreciation} = \frac{\text{Purchase Price} + \text{Capitalized Closing Costs} - \text{Land Value}}{27.5}$$
- **Numerical Example ($550,000 Duplex, $110,000 Land Value = 20%, $440,000 Building Basis):**
  - $\text{Annual Depreciation} = \frac{\$440,000}{27.5} = \mathbf{\$16,000.00/\text{year}}$ ($1,333.33/month).
  - If sold after 5 years ($80,000 depreciation taken) for $650,000 (net of selling costs): Total Gain = $650k - ($550k - $80k) = $180,000 -> **$80,000** taxed as Unrecaptured § 1250 gain (max 25%) + **$100,000** taxed at LTCG rates (15%/20%) + 3.8% NIIT if applicable.

## Outputs
Tax impact schedule covering annual depreciation shield, holding-period tax classification, 1031 exchange timeline, and 1099 obligations.

## Human Approval Gates
- Claude **never** structures a 1031 exchange, cost segregation allocation, or foreign investor withholding election without a licensed US CPA or Tax Attorney.

## Handoffs
- Hands off to `rt-finance/tax-planning` and `rt-acquisitions/deal-feasibility`.

## Common Errors & Risks
- Treating fix-and-flip properties as eligible for § 1031 exchanges or long-term capital gains (inventory held primarily for sale is excluded under IRC § 1031(a)(2)).
- Letting sale proceeds hit the seller's bank account before engaging a 1031 Qualified Intermediary (constructive receipt disqualifies the exchange).

## Test Cases
1. **Normal:** 'Calculate annual depreciation on a $600k single-family rental with 25% land value.' -> $450,000 / 27.5 = $16,363.64/year.
2. **Incompleto:** 'Can we do a 1031 exchange on our latest flip?' -> Asks how long it was held and whether intent was resale (dealer inventory) vs. rental investment.
3. **Risco:** 'We closed on the sale of our rental property yesterday and have the cash in our operating account; can we start a 1031 exchange today?' -> Explains constructive receipt rules permanently bar 1031 deferral once funds are received.

## Sources
- Internal Revenue Code §§ 121, 168, 469, 1031, 1250, 1411 — IRS (`irs.gov`), accessed 2026-11-25.
- IRS Publication 527 (Residential Rental Property) & Publication 544 (Sales and Other Dispositions of Assets) — IRS, accessed 2026-11-25.

## Pending Items
- Confirm exact LLC/corporate tax structure of the operating company.
