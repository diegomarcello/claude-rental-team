---
plugin: rt-jurisdictions
skill: privacy
jurisdiction: united-states
last_verified: 2026-11-25
confidence: verified
reviewer: US Privacy & Compliance Counsel
---

# Jurisdiction United States — Privacy, Consumer Data & Marketing Compliance (CCPA/CPRA, TCPA, CAN-SPAM, GLBA)

## Objective & Triggers
Establish US federal and state privacy, telemarketing, SMS/email outreach, and tenant financial data safeguards (CCPA/CPRA, TCPA, CAN-SPAM, FCRA, FTC Safeguards Rule).
- **Triggers:** 'TCPA SMS rules real estate leads', 'CCPA privacy notice property management', 'FCRA adverse action notice tenant screening'.

## When Not to Use
- Do not use for company-specific data inventory population (use `rt-legal/privacy-aml`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Outreach channel (SMS/text, autodialed call, prerecorded voice, email) | Yes | Enum | Marketing / Pre-sales |
| Consumer state of residence (e.g., CA, TX, FL) | Yes | Text | CRM |
| Data type (Lead contact, Consumer credit report, SSN/bank info) | Yes | Enum | Intake |

## Process


## Rules & Criteria
- **Federal Statute (TCPA — 47 U.S.C. § 227 & FCC Rules):** Prohibits autodialed or prerecorded/artificial-voice calls and marketing text messages to wireless numbers without **Prior Express Written Consent (PEWC)** (clear and conspicuous disclosure, one-to-one seller consent, electronic signature). Statutory damages: **$500 per violation**, trebled to **$1,500** for willful violations. Always scrub against the National Do-Not-Call (DNC) Registry.
- **Federal Statute (CAN-SPAM Act — 15 U.S.C. § 7701):** Commercial emails must include accurate header/subject lines, physical postal address, and a clear opt-out mechanism honored within **10 business days**.
- **Federal Statute (FCRA — 15 U.S.C. § 1681m):** When denying a rental applicant or requiring conditional approval based in whole or in part on a consumer report, landlord/PM must provide an **Adverse Action Notice** naming the Consumer Reporting Agency (CRA), stating the CRA did not make the decision, and notifying the applicant of their right to a free report within 60 days and to dispute inaccuracies.
- **Federal Rule (FTC Safeguards Rule — 16 CFR Part 314):** Financial institutions (including real estate brokers/property managers handling mortgage/credit underwriting data) must maintain a written Information Security Program, encrypt customer data at rest and in transit, enforce MFA, and notify the FTC within **30 days** of a breach affecting >= 500 consumers.
- **State Privacy (CCPA/CPRA — Cal. Civ. Code § 1798.100 et seq.; TDPSA in TX; FDBR in FL):** Applies to covered businesses meeting statutory thresholds (e.g., CA: > $25M gross revenue, or >= 100k consumers/households, or >= 50% revenue from selling/sharing data); requires Privacy Policy at collection and **45-day** response to access/deletion/opt-out requests.
- **Company Decision:** `[PENDING: Confirm whether company meets CCPA/TDPSA applicability thresholds and configure TCPA consent logs]`. 

## Calculations
**Key Statutory Timelines & Penalties:**
- TCPA statutory penalty: **$500 – $1,500 per unlawful call/text**
- CAN-SPAM opt-out processing: $\le \mathbf{10\text{ business days}}$
- FTC Safeguards breach notice (>= 500 consumers): $\le \mathbf{30\text{ days}}$
- CCPA/CPRA consumer request response: $\le \mathbf{45\text{ calendar days}}$ (extendable by 45 days with notice)

## Outputs
Omnichannel outreach & tenant data compliance checklist (TCPA, CAN-SPAM, FCRA, Safeguards).

## Human Approval Gates
- Claude **never** launches bulk SMS/autodialer campaigns without verified PEWC timestamps, nor sends tenant denial notices without FCRA-compliant Adverse Action disclosures.

## Handoffs
- Hands off to `rt-pre-sales/follow-up-cadence`, `rt-property-management/tenant-screening`, and `rt-technology-data/information-security`.

## Common Errors & Risks
- Buying third-party 'motivated seller' phone lists and blasting automated SMS without 1-to-1 TCPA written consent.
- Verbally telling a rejected tenant 'your credit score is too low' without sending a written FCRA Adverse Action Notice.

## Test Cases
1. **Normal:** 'What must be included when we reject a tenant due to their TransUnion screening report?' -> Written FCRA Adverse Action Notice with CRA contact details, non-decision disclaimer, 60-day free report right, and dispute right.
2. **Incompleto:** 'Can we text expired MLS listings?' -> Explains DNC scrubbing and strict TCPA ban on automated/platform SMS without Prior Express Written Consent.
3. **Risco:** 'Upload this purchased CSV of 10,000 homeowner cell numbers into our auto-texting sequence.' -> Blocks action due to severe TCPA class-action exposure ($500–$1,500 per text).

## Sources
- Telephone Consumer Protection Act (TCPA) — 47 U.S.C. § 227 — FCC (`fcc.gov`), accessed 2026-11-25.
- Fair Credit Reporting Act (FCRA) — 15 U.S.C. § 1681m — FTC (`ftc.gov`), accessed 2026-11-25.
- FTC Safeguards Rule — 16 CFR Part 314 & CCPA/CPRA — Cal. Civ. Code § 1798.100 — FTC / CA Attorney General, accessed 2026-11-25.

## Pending Items
- Verify annual revenue/consumer volume against CCPA and Texas TDPSA statutory thresholds.
