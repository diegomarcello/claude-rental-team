---
plugin: rt-jurisdictions
skill: brokerage-advertising-consumer
jurisdiction: united-states
last_verified: 2026-11-25
confidence: verified
reviewer: Managing Broker / Real Estate Counsel
---

# Jurisdiction United States — Brokerage Licensing, NAR Settlement Rules, Advertising & RESPA

## Objective & Triggers
Consolidate US state real estate brokerage licensing, post-NAR settlement buyer representation/commission rules, Fair Housing advertising standards, and RESPA Section 8 anti-kickback prohibitions.
- **Triggers:** 'NAR settlement buyer broker agreement rules', 'RESPA Section 8 referral fee rules', 'real estate advertising compliance US', 'blind ad rules'.

## When Not to Use
- Do not use for internal agent commission split calculations (use `rt-sales/commission-calculation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| State of brokerage operation | Yes | Text | License Record |
| Representation role (Listing broker, Buyer broker, Dual/Designated agency) | Yes | Enum | Engagement |
| Marketing asset or referral arrangement | Yes | Text | Marketing / BizDev |

## Process


## Rules & Criteria
- **Industry / Antitrust Rule (Post-NAR Settlement Practice Changes, effective Aug 2024):** (1) MLS participants working with a buyer **must enter into a written agreement** with the buyer *before* touring a home (in-person or live virtual tour); (2) the written agreement must specify a **conspicuous, objective rate or amount of compensation** (not open-ended) and state that broker fees are **not set by law and are fully negotiable**; (3) offers of buyer-broker compensation are **prohibited on the MLS** (may be negotiated off-MLS or requested as seller concessions in the offer).
- **Federal Statute (RESPA Section 8 — 12 U.S.C. § 2607):** Prohibits giving or accepting any fee, kickback, or thing of value pursuant to an agreement/understanding for referrals of settlement service business involving a federally related mortgage loan. Cooperative brokerage splits between licensed real estate brokers are exempt (12 U.S.C. § 2607(c)(2)), as are compliant Affiliated Business Arrangements (AfBAs) with proper disclosure and no required use.
- **Federal Statute (Fair Housing Advertising — 42 U.S.C. § 3604(c)):** Unlawful to make, print, or publish any notice, statement, or advertisement indicating any preference, limitation, or discrimination based on protected classes (describe the *property*, never the *ideal occupant*).
- **State Licensing Rules:** Strict prohibition on 'blind ads' (ads failing to display the licensed brokerage firm's registered name); unlicensed assistants cannot host open houses, negotiate terms, or earn transaction-based commissions.

## Calculations
Not applicable (regulatory & ethical rules; split math in `rt-sales/commission-calculation`).

## Outputs
Brokerage & advertising compliance checklist covering buyer agreements, MLS rules, RESPA § 8, and Fair Housing ad copy review.

## Human Approval Gates
- Managing Broker must approve any dual agency disclosure, off-MLS compensation concession structure, or Affiliated Business Arrangement.

## Handoffs
- Hands off to `rt-marketing/listing-copywriting`, `rt-pre-sales/visit-scheduling`, and `rt-sales/proposal-negotiation`.

## Common Errors & Risks
- Touring a listed property with a prospective buyer before obtaining a signed Buyer Representation Agreement.
- Paying a 'bird-dog' / referral fee to an unlicensed individual (illegal under state licensing laws and RESPA § 8).
- Writing ad copy like 'perfect for young professionals or empty nesters' (Fair Housing familial status/age steering risk).

## Test Cases
1. **Normal:** 'Can we tour a house with a buyer today and sign the buyer agreement tomorrow?' -> No; written buyer representation agreement with objective compensation terms is required *before* touring.
2. **Incompleto:** 'Can we pay a $500 gift card to a past client who refers a buyer?' -> Flags violation of state real estate license laws (paying unlicensed person for referral) and potential RESPA § 8 violation.
3. **Risco:** 'Post an ad saying: Quiet adult-only building, great for bachelors.' -> Blocks ad immediately for violating Fair Housing Act familial status protections (42 U.S.C. § 3604(c)).

## Sources
- Real Estate Settlement Procedures Act (RESPA) Section 8 — 12 U.S.C. § 2607 & 12 CFR § 1024.14 — CFPB, accessed 2026-11-25.
- Fair Housing Act — 42 U.S.C. § 3604(c) — HUD, accessed 2026-11-25.
- NAR Settlement Practice Changes Summary — National Association of Realtors (`nar.realtor`), accessed 2026-11-25.

## Pending Items
- State-specific statutory buyer agency form requirements (e.g., FL Stat. § 475.278; TX Info About Brokerage Services IABS; CA BRBC).
