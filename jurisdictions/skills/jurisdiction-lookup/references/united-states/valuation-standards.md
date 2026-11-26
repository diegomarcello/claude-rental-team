---
plugin: rt-jurisdictions
skill: valuation-standards
jurisdiction: united-states
last_verified: 2026-11-25
confidence: verified
reviewer: MAI / Certified General Appraiser
---

# Jurisdiction United States — Appraisal Standards (USPAP), BPOs & Licensing

## Objective & Triggers
Define US appraisal standards (USPAP), state appraiser licensing tiers, Broker Price Opinions (BPOs), and the three recognized valuation approaches.
- **Triggers:** 'USPAP appraisal rules', 'when is a licensed appraiser required vs BPO', 'FIRREA appraisal threshold'.

## When Not to Use
- Do not use to compute a specific property's valuation (use `rt-appraisal/comparative-market-analysis`, `income-capitalization`, or `cost-approach`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Purpose of valuation (Federally related mortgage, litigation, internal underwriting, listing price) | Yes | Enum | Request |
| Property type & transaction value | Yes | Enum + Numeric (USD) | Property Record |

## Process


## Rules & Criteria
- **Federal / Industry Standard (USPAP — Uniform Standards of Professional Appraisal Practice):** Promulgated by The Appraisal Foundation (ASB) under FIRREA (Title XI, 12 U.S.C. § 3331 et seq.). Mandatory for all federally related real estate transactions.
- **Federal Thresholds (12 CFR Part 34 / Part 225):** Residential real estate transactions <= **$400,000** and commercial real estate transactions <= **$500,000** may qualify for an 'evaluation' rather than a full USPAP appraisal under federal banking regulations (subject to lender/agency overlays like Fannie Mae/Freddie Mac).
- **USPAP Workfile Retention (Record Keeping Rule):** Appraisers must retain a workfile for at least **5 years** after preparation or at least **2 years** after final disposition of any judicial proceeding in which testimony was given, whichever period expires last.
- **State Licensing & BPO Restrictions:** States issue Trainee, Licensed Residential, Certified Residential, and Certified General (unlimited commercial/residential) credentials. Broker Price Opinions (BPOs) and CMAs are permitted for listing/acquisition guidance in most states (e.g., FL Stat. § 475.612; TX Occ. Code § 1101.002), but **cannot** be represented as an 'appraisal' or used for federally related mortgage lending; some mandatory states restrict paid BPOs for non-brokerage purposes.

## Calculations
**USPAP Record Retention Minimum:**
$$\text{Retention} = \max\left(5\text{ years from report date},\ 2\text{ years post-litigation disposition}\right)$$

## Outputs
Valuation governance matrix detailing when USPAP Certified Appraiser vs. Licensed Broker CMA/BPO is legally permitted.

## Human Approval Gates
- Any valuation used for lender financing, investor reporting, or litigation must be signed by a state-certified appraiser compliant with USPAP.

## Handoffs
- Hands off to `rt-appraisal/comparative-market-analysis`, `income-capitalization`, and `cost-approach`.

## Common Errors & Risks
- Calling an internal CMA or BPO an 'appraisal' in investor decks or lender packets (statutory violation of state appraisal licensing acts).

## Test Cases
1. **Normal:** 'How long must a USPAP appraisal workfile be kept?' -> Minimum 5 years after preparation, or 2 years after final disposition of judicial proceedings, whichever is longer.
2. **Incompleto:** 'Can our broker write an appraisal for a commercial loan?' -> Asks loan type and value; clarifies federally related commercial loans > $500k require a Certified General Appraiser.
3. **Risco:** 'Label our automated CMA report as an Official Appraisal for the bank.' -> Blocks misrepresentation and requires engaging a state-certified appraiser.

## Sources
- USPAP (Uniform Standards of Professional Appraisal Practice) — The Appraisal Foundation (`appraisalfoundation.org`), accessed 2026-11-25.
- FIRREA Title XI — 12 U.S.C. § 3331 et seq. & 12 CFR Part 34 — OCC / Federal Reserve, accessed 2026-11-25.

## Pending Items
- State-by-state BPO fee restrictions if offering standalone valuation services.
