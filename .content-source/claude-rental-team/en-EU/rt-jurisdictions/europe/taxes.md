---
plugin: rt-jurisdictions
skill: taxes
jurisdiction: europe
last_verified: 2026-11-25
confidence: verified
reviewer: European Cross-Border Tax Advisor
---

# Jurisdiction Europe — Real Estate Taxation, VAT, Rental Income & Capital Gains (PT / ES / DE / FR)

## Objective & Triggers
Map European real estate taxes across acquisition, holding, rental income, VAT/IVA/TVA/USt on new builds/commercial leases, and capital gains in Portugal, Spain, Germany, and France.
- **Triggers:** 'property taxes Portugal IMT IMI', 'Spain non-resident rental tax IRNR', 'Germany 10-year speculation period capital gains', 'France LMNP furnished rental tax'.

## When Not to Use
- Do not use for cross-border corporate structuring or tax return filing (use `rt-finance/tax-planning`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Country & Region | Yes | Text | Property Record |
| Owner profile (Resident individual, Non-resident EU/Non-EU individual, Corporate entity) | Yes | Enum | Entity Profile |
| Transaction type (New build vs. resale, Residential vs. commercial rental, Disposal) | Yes | Enum | Operation |

## Process


## Rules & Criteria
- **EU VAT Directive (Directive 2006/112/EC):** Leasing of immovable property is generally VAT-exempt (art. 135(1)(l)), with an option to tax commercial leases in most Member States (e.g., Germany § 9 UStG, France TVA option, Portugal renúncia à isenção) to recover input VAT on CapEx. First supply of new buildings is generally subject to VAT.
- **Country Rules:**
  - *Portugal:* **IMT** (progressive up to 7.5% urban residential; 6.5% other urban; 10% blacklisted jurisdictions) + **Imposto do Selo** (0.8%). Annual **IMI** (0.3%–0.45% urban VPT) + **AIMI** (wealth surcharge 0.7% above €600k for individuals; 0.4% flat for companies). Residential rental income taxed at flat **25%** (reduced progressively down to **10%** for long-term contracts >= 20 years, CIRS art. 72). Capital gains for residents & non-residents taxed on 50% of gain at progressive IRS rates (exemption if primary residence reinvested in EU/EEA within 36 months).
  - *Spain:* New build: **10% IVA** + 0.5%–1.5% AJD; Resale: **ITP** (6%–11% by region). Annual **IBI**. Non-resident rental tax (**IRNR**): **19%** for EU/EEA residents (with expense deductions) vs. **24%** for non-EU residents (on gross income, no deductions). Capital gains: 19%–28% progressive savings tax for residents; 19% flat for non-residents (with **3% buyer withholding** on gross sale price, Modelo 211).
  - *Germany:* **Grunderwerbsteuer** (3.5%–6.5%). Annual **Grundsteuer** (reformed effective 2025). Straight-line building depreciation (**AfA**): 2% p.a. (3% for residential buildings completed after Dec 31, 2022, EStG § 7(4)). **10-Year Rule (*Spekulationsfrist*, EStG § 23):** Private individuals holding real estate for **> 10 years** pay **0% capital gains tax** upon sale (unless commercial trading threshold '3-object rule' is breached).
  - *France:* Annual **Taxe Foncière** + **IFI** (Real Estate Wealth Tax on net real estate > €1.3M). Furnished rentals (**LMNP** — *Loueur en Meublé Non Professionnel*) allow component depreciation (*amortissement*) reducing taxable rental income, though 2025 Finance Law requires recapturing taken depreciation in capital gains calculation. Private capital gains (*Plus-value immobilière*): 19% income tax + 17.2% social charges (7.5% solidarity levy for EU/EEA/Swiss social-security residents), with full income tax exemption after **22 years** and social charges exemption after **30 years**.

## Calculations
**Spain Non-Resident Disposal Withholding (Modelo 211):**
$$\text{Mandatory Buyer Withholding} = 3\% \times \text{Gross Sale Price}$$
- **Numerical Example (€600,000 sale by non-resident in Spain):**
  - Buyer withholds **$18,000 (€600,000 \times 3\%)$** at closing and remits to Agencia Tributaria within 1 month; seller reconciles actual 19% net capital gain tax via Modelo 210 within 4 months.

## Outputs
Multi-country European tax matrix covering acquisition, ongoing rental taxation, depreciation, and exit capital gains.

## Human Approval Gates
- Claude **never** files tax declarations (Modelo 210/211, IRS Anexo F/G, Elster, Cerfa) or structures cross-border SPVs without a licensed local Tax Advisor.

## Handoffs
- Hands off to `rt-finance/tax-planning` and `rt-acquisitions/deal-feasibility`.

## Common Errors & Risks
- Breaching Germany's 'three-object rule' (*Drei-Objekt-Grenze* — selling > 3 properties within 5 years), which reclassifies a private investor into a commercial trader subject to trade tax (*Gewerbesteuer*) and forfeits the 10-year tax-free exit.
- Overlooking Portugal's AIMI surcharge when holding residential properties inside a corporate entity (0.4% from euro 1, without the €600k personal allowance).

## Test Cases
1. **Normal:** 'When is a private individual exempt from capital gains tax when selling a rental apartment in Germany vs. France?' -> Germany: after 10 years holding period; France: after 22 years (income tax) and 30 years (social charges).
2. **Incompleto:** 'What tax applies to rental income in Spain?' -> Asks whether the owner is a Spanish tax resident, EU/EEA resident (19% net), or non-EU resident (24% gross).
3. **Risco:** 'A non-EU owner is selling a villa in Marbella for €1M and wants the buyer to wire 100% of the price.' -> Flags mandatory 3% (€30,000) statutory retention under Spanish IRNR rules.

## Sources
- EU VAT Directive — Directive 2006/112/EC (art. 135) — EUR-Lex, accessed 2026-11-25.
- Portugal CIRS, CIMT, CIMI; Spain Ley IRNR (RDL 5/2004); Germany EStG (§§ 7, 23); France CGI (arts. 150 U–150 VH) — National Tax Authorities, accessed 2026-11-25.

## Pending Items
- Local municipal IMI/IBI/Grundsteuer multipliers per target city.
