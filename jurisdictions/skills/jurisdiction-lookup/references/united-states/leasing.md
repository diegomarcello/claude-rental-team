---
plugin: rt-jurisdictions
skill: leasing
jurisdiction: united-states
last_verified: 2026-11-25
confidence: verified
reviewer: Landlord-Tenant Attorney
---

# Jurisdiction United States — Residential & Commercial Leasing, Fair Housing & Eviction

## Objective & Triggers
Consolidate US federal Fair Housing Act mandates and state landlord-tenant rules (security deposits, habitability, rent control, notice periods, and eviction procedures) across FL, TX, and CA.
- **Triggers:** 'US security deposit rules', 'Fair Housing Act protected classes', 'how long does eviction take in Florida Texas California', 'California AB 1482 rent cap'.

## When Not to Use
- Do not use for individual tenant credit scoring (use `rt-property-management/tenant-screening`).
- Do not use to draft an active eviction complaint (use `rt-legal/disputes-eviction`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| State & Municipality | Yes | Text | Property Record |
| Lease type (Fixed-term residential, Month-to-month, Commercial NNN) | Yes | Enum | Lease |
| Monthly rent & security deposit amount | Yes | Numeric (USD) | Lease |

## Process


## Rules & Criteria
- **Federal Statute (Fair Housing Act — 42 U.S.C. § 3604):** Prohibits discrimination in housing rental, sale, advertising, or terms based on **7 protected classes**: race, color, religion, national origin, sex (including sexual orientation and gender identity per HUD guidance), familial status, and disability (including mandatory reasonable accommodations/modifications for Assistance Animals / ESAs without pet fees under HUD FHEO-2020-01). Many states/cities add **Source of Income (Section 8 / Housing Choice Vouchers)** (e.g., CA Gov. Code § 12955).
- **Federal Statute (SCRA — 50 U.S.C. § 3955):** Active-duty servicemembers receiving PCS or deployment orders (>= 90 days) may terminate residential leases without penalty upon written notice + orders, effective 30 days after next rent due date.
- **State Rules (FL / TX / CA):**
  - *Florida (Fla. Stat. Ch. 83, Part II):* No statutory cap on security deposit; must hold in separate FL bank account (non-interest or interest-bearing) or post surety bond and notify tenant within **30 days** (§ 83.49(2)). Return deposit within **15 days** if no claim, or send certified notice of claim within **30 days** (§ 83.49(3)(a)). Non-payment notice: **3 business days** (§ 83.56(3)). Preempts local rent control (§ 125.0103).
  - *Texas (Tex. Prop. Code Ch. 92):* No statutory deposit cap; must return deposit + itemized deductions within **30 days** of surrender (§ 92.103). Non-payment Notice to Vacate: **3 days** unless lease specifies shorter/longer (§ 24.005). State-level ban on rent control (§ 214.902).
  - *California (Cal. Civ. Code §§ 1946.2, 1947.12, 1950.5 — AB 1482 & AB 12):* Security deposit capped at **1 month's rent** (2 months exception only for small landlords owning <= 2 properties totaling <= 4 units, effective July 1, 2024 under AB 12). Return deposit within **21 calendar days**. Statewide rent cap (AB 1482) limits annual increases to **5% + local CPI, max 10%** and requires Just Cause for eviction after 12 months tenancy (exemptions: single-family homes owned by individuals/non-corporate LLCs with mandatory statutory exemption notice, and buildings < 15 years old). Non-payment notice: **3 business days** (Cal. CCP § 1161(2)).
- **Market Practice:** 12-month standard residential lease; 1-month security deposit; 3x monthly gross income threshold.
- **Company Decision:** `[PENDING: Confirm ESA verification partner and state-specific lease templates]`. 

## Calculations
**California AB 1482 Maximum Annual Rent Increase:**
$$\text{Max Increase (\%)} = \min\left(5\% + \text{Regional CPI},\ 10\%\right)$$
- **Numerical Example (Los Angeles/Orange County, assuming Regional CPI = 3.2%, Current Rent = $3,000):**
  - $\text{Allowable Increase} = \min(5\% + 3.2\%,\ 10\%) = \mathbf{8.2\%}$
  - $\text{New Max Monthly Rent} = \$3,000 \times 1.082 = \mathbf{\$3,246.00}$.

## Outputs
Jurisdictional leasing compliance summary covering deposit handling, rent caps, protected classes, and statutory notice periods.

## Human Approval Gates
- Claude **never** denies an Emotional Support Animal (ESA) accommodation request or issues an eviction notice without Landlord-Tenant Attorney sign-off.

## Handoffs
- Hands off to `rt-property-management/tenant-screening`, `rt-property-management/lease-administration`, and `rt-legal/disputes-eviction`.

## Common Errors & Risks
- Charging a 'pet deposit' or 'pet rent' for a verified Assistance Animal / ESA (violates Fair Housing Act).
- Missing Florida's strict 30-day certified mail deadline to claim against a security deposit (forfeits right to deduct, though landlord may still sue separately).

## Test Cases
1. **Normal:** 'How many days does a landlord have to return a security deposit in FL, TX, and CA?' -> FL: 15 days (no claim) / 30 days (notice of claim); TX: 30 days; CA: 21 days.
2. **Incompleto:** 'Can I raise rent by 12% on renewal?' -> Asks for State, City, property age, and ownership structure (e.g., prohibited in CA if covered by AB 1482, permitted in FL/TX if lease has expired).
3. **Risco:** 'An applicant has a pitbull ESA letter and our HOA bans pitbulls. Should we reject the application?' -> Warns that FHA reasonable accommodation overrides breed restrictions unless direct threat is proven on individualized assessment; escalates to Legal.

## Sources
- Fair Housing Act — 42 U.S.C. § 3601 et seq. & HUD Guidance FHEO-2020-01 — HUD (`hud.gov`), accessed 2026-11-25.
- Servicemembers Civil Relief Act — 50 U.S.C. § 3955 — Cornell LII, accessed 2026-11-25.
- Fla. Stat. Ch. 83; Tex. Prop. Code Ch. 24 & 92; Cal. Civ. Code §§ 1946.2, 1947.12, 1950.5 (AB 1482 & AB 12) — State Legislatures, accessed 2026-11-25.

## Pending Items
- Add county/city rent stabilization overlays (e.g., NYC, San Francisco, Los Angeles RSO) if operating in those municipalities.
