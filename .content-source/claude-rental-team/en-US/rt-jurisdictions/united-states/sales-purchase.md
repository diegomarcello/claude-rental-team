---
plugin: rt-jurisdictions
skill: sales-purchase
jurisdiction: united-states
last_verified: 2026-11-25
confidence: verified
reviewer: Licensed Real Estate Attorney / Title Officer
---

# Jurisdiction United States — Real Estate Sales, Title, Escrow & Financing (FL / TX / CA)

## Objective & Triggers
Consolidate US real estate conveyance rules, title insurance, escrow closing procedures, statutory disclosures, and mortgage/foreclosure frameworks across priority states (Florida, Texas, California).
- **Triggers:** 'US real estate closing process', 'title insurance vs deed recording', 'judicial vs non-judicial foreclosure FL TX CA', 'seller disclosure rules'.

## When Not to Use
- Do not use for property-specific title commitment review (use `rt-legal/title-due-diligence`).
- Do not use for borrower PITI/amortization modeling (use `rt-sales/financing-simulation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| State & County of property | Yes | Text (e.g., Miami-Dade, FL; Travis, TX; Los Angeles, CA) | User / CRM |
| Purchase price & financing type (Cash, Conventional, FHA/VA, DSCR) | Yes | Numeric (USD) + Enum | Offer / PSA |
| Seller entity type (Individual, LLC, Foreign Person — FIRPTA) | Yes | Enum | Intake |

## Process


## Rules & Criteria
- **Statute (Statute of Frauds):** All contracts for the sale of real property must be in writing and signed by the party to be charged (e.g., Fla. Stat. § 725.01; Tex. Bus. & Com. Code § 26.01; Cal. Civ. Code § 1624).
- **Statute (Federal Lead-Based Paint Disclosure):** Mandatory for target housing built prior to 1978, granting a 10-day inspection window unless waived (42 U.S.C. § 4852d; 24 CFR Part 35).
- **Statute (FIRPTA Withholding):** If Seller is a 'foreign person', Buyer/Settlement Agent must withhold **15%** of the gross amount realized (10% if acquired as residence between $300k–$1M; 0% if residence <= $300k) and remit to IRS via Form 8288 within 20 days (IRC § 1445).
- **Statute (State Disclosure & Foreclosure Variations):**
  - *Florida:* Duty to disclose known material facts not readily observable (*Johnson v. Davis*, 480 So. 2d 625); **Judicial foreclosure** state; Documentary Stamp Tax on deeds ($0.70 per $100 statewide; $0.60 in Miami-Dade).
  - *Texas:* Mandatory Seller's Disclosure Notice (Tex. Prop. Code § 5.008); **Non-judicial foreclosure** state (Tex. Prop. Code § 51.002 — 20-day notice to cure + 21-day notice of sale on first Tuesday of month); no state transfer tax.
  - *California:* Mandatory Transfer Disclosure Statement (TDS) & Natural Hazard Disclosure (NHD) (Cal. Civ. Code § 1102); **Non-judicial foreclosure** state (Cal. Civ. Code § 2924 — 90-day Notice of Default + 21-day Notice of Sale).
- **Market Practice:** Earnest Money Deposit (EMD) typically 1%–3% of purchase price; Title Insurance replaces abstract/notarial title guarantees used in civil-law countries.
- **Company Decision:** `[PENDING: Confirm target US states and approved title/escrow partners]`. 

## Calculations
**Estimated Closing Costs & FIRPTA Check (USD):**
$$\text{Total Cash to Close} = \text{Down Payment} + \text{Title & Escrow Fees} + \text{Transfer/Doc Stamps} + \text{Prepaids/Prorations} - \text{EMD}$$
- **Numerical Example (Florida $500,000 Purchase, $400,000 Mortgage):**
  - FL Deed Doc Stamps ($0.70 per $100 on $500k): **$3,500.00**
  - FL Mortgage Doc Stamps ($0.35 per $100 on $400k): **$1,400.00**
  - FL Intangible Tax (0.002 on $400k): **$800.00**
  - Owner's Title Insurance (FL promulgated rate: $5.75/k first $100k + $5.00/k next $400k): $575 + $2,000 = **$2,575.00**
  - Recording, Survey, Municipal Lien Search & Settlement Fee: ~**$1,650.00**
  - **Total Estimated Closing Costs (excl. lender points/prepaids):** **$9,925.00** (~1.99%).

## Outputs
State-specific closing roadmap, statutory disclosure checklist, and itemized closing cost estimate.

## Human Approval Gates
- Claude **never** drafts non-standard PSA addenda, waives title defects, or determines FIRPTA exemptions without review by a licensed Real Estate Attorney or CPA.

## Handoffs
- Hands off to `rt-legal/title-due-diligence` and `rt-sales/closing-checklist`.

## Common Errors & Risks
- Treating a title commitment as final insurance without verifying Schedule B-I requirements are cleared prior to funding.
- Missing the 3-business-day TRID Closing Disclosure waiting period, delaying closing.

## Test Cases
1. **Normal:** 'What are the transfer taxes and foreclosure rules for a $500k home in Florida vs. Texas?' -> Details FL doc stamps/judicial process vs. TX zero transfer tax/non-judicial first-Tuesday foreclosure.
2. **Incomplete:** 'How much are closing costs on a US property?' -> Asks for State, County, Purchase Price, and Cash vs. Financed.
3. **Risk:** 'The seller is a non-resident Brazilian citizen selling a $600k condo in Orlando and wants full proceeds wired at closing.' -> Flags mandatory 15% (or 10% primary residence exception) FIRPTA withholding under IRC § 1445.

## Sources
- Real Estate Settlement Procedures Act (RESPA) & TILA-RESPA Integrated Disclosure (TRID) — 12 CFR § 1026.19 — CFPB (`consumerfinance.gov`), accessed 2026-11-25.
- Internal Revenue Code § 1445 (FIRPTA) — IRS (`irs.gov`), accessed 2026-11-25.
- Fla. Stat. Ch. 201 & 702; Tex. Prop. Code §§ 5.008 & 51.002; Cal. Civ. Code §§ 1102 & 2924 — State Legislatures, accessed 2026-11-25.

## Pending Items
- Confirm exact state priority list (e.g., FL, TX, CA, GA, NC) and county-level transfer tax schedules.
