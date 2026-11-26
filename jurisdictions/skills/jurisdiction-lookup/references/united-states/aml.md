---
plugin: rt-jurisdictions
skill: aml
jurisdiction: united-states
last_verified: 2026-11-25
confidence: verified
reviewer: US BSA/AML Compliance Officer / Legal Counsel
---

# Jurisdiction United States — Anti-Money Laundering (FinCEN Real Estate Reporting Rule, BSA, CTA, OFAC)

## Objective & Triggers
Define US AML/BSA obligations for non-financed residential real estate transfers (FinCEN Residential Real Estate Rule), cash reporting (IRS Form 8300), OFAC sanctions screening, and beneficial ownership compliance.
- **Triggers:** 'FinCEN real estate reporting rule', 'all-cash LLC buyer AML rules', 'IRS Form 8300 cash threshold', 'OFAC SDN check real estate'.

## When Not to Use
- Do not use to complete an individual buyer's KYC intake form (use `rt-legal/privacy-aml`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Property type (Residential 1–4 family/condo/land vs. Commercial) | Yes | Enum | Property Record |
| Financing status (Non-financed/All-cash/Private non-BSA lender vs. Traditional mortgage) | Yes | Enum | PSA |
| Buyer entity structure (Individual vs. LLC, Corporation, Partnership, Trust) | Yes | Enum | KYC |
| Payment method & currency/wire origin | Yes | Text | Escrow / Finance |

## Process


## Rules & Criteria
- **Federal Rule (FinCEN Non-Financed Residential Real Estate Rule — 31 CFR § 1031.320, 89 FR 70258):** Requires reporting persons in the settlement cascade to file a Real Estate Report with FinCEN for **non-financed transfers** (including all-cash deals and loans from private lenders without BSA AML/SAR programs) of **residential real property** (1–4 family structures, condos, co-ops, or land intended for 1–4 family construction) to a **transferee legal entity or trust** (regardless of purchase price). Reporting deadline: the later of **30 calendar days** post-closing or the **last day of the month following** the closing month. Records retained for **5 years**.
- **Federal Statute (IRS/FinCEN Form 8300 — 31 U.S.C. § 5331):** Any person in a trade or business who receives more than **$10,000 in cash** (currency or certain monetary instruments) in a single transaction or related transactions must file Form 8300 within **15 days** and furnish a written statement to the payer by January 31 of the following year.
- **Federal Statute (OFAC Sanctions — 31 CFR Ch. V):** Strict liability prohibition on transacting with Specially Designated Nationals (SDNs) or blocked persons/jurisdictions. Screen all buyers, sellers, members, and beneficiaries.
- **Red Flags:** All-cash purchases via multi-layered shell LLCs/offshore trusts, reluctance to disclose beneficial owners, third-party wires from unrelated jurisdictions, rapid flipping without economic rationale.

## Calculations
**Key Federal AML Thresholds & Deadlines:**
- **FinCEN Non-Financed Entity/Trust Residential Rule:** **$0 threshold** (applies to any non-financed transfer to an entity/trust, including gifts); filing due **later of 30 calendar days or end of following month**; record retention **5 years**.
- **IRS Form 8300 Cash Reporting:** **> $10,000** in cash/related transactions; filing due within **15 calendar days**.

## Outputs
AML/OFAC screening checklist + FinCEN reporting determination worksheet.

## Human Approval Gates
- Claude **never** clears an OFAC potential match or waives Beneficial Ownership disclosure on an all-cash entity purchase; escalate immediately to Legal/BSA Officer.

## Handoffs
- Hands off to `rt-legal/privacy-aml` and `rt-sales/closing-checklist`.

## Common Errors & Risks
- Assuming all-cash residential sales to LLCs remain exempt from federal AML reporting (FinCEN's nationwide rule replaced the old geographic GTOs).
- Accepting > $10,000 in physical cash/money orders without filing Form 8300 within 15 days.

## Test Cases
1. **Normal:** 'An all-cash LLC is buying a $350,000 single-family rental in Texas without a bank loan. Does FinCEN reporting apply?' -> Yes, non-financed transfer of residential property to a legal entity triggers the FinCEN Real Estate Reporting Rule.
2. **Incompleto:** 'Do we need to collect beneficial owner passports on this deal?' -> Asks if the property is residential (1–4 units), whether it is non-financed, and whether the buyer is an entity/trust.
3. **Risco:** 'A buyer's name matches an OFAC SDN entry, though their middle initial is unclear.' -> Halts transaction immediately and escalates to Compliance/Legal for formal OFAC verification.

## Sources
- FinCEN Anti-Money Laundering Regulations for Residential Real Estate Transfers — 31 CFR § 1031.320 (89 FR 70258) — FinCEN (`fincen.gov`), accessed 2026-11-25.
- IRS Form 8300 Reference Guide — 31 U.S.C. § 5331 — IRS (`irs.gov`), accessed 2026-11-25.
- OFAC Sanctions Compliance Guidance for Real Estate — US Treasury (`ofac.treasury.gov`), accessed 2026-11-25.

## Pending Items
- Confirm company policy prohibiting acceptance of physical currency and defining escrow-agent responsibility for FinCEN filings.
