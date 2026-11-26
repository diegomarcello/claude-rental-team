---
plugin: rt-jurisdictions
skill: valuation-standards
jurisdiction: europe
last_verified: 2026-11-25
confidence: verified
reviewer: RICS Chartered Surveyor (MRICS / FRICS) / HypZert Valuer
---

# Jurisdiction Europe — Valuation Standards (RICS Red Book, TEGoVA EVS, ImmoWertV & Chartered Surveyors)

## Objective & Triggers
Define European valuation frameworks (RICS Valuation – Global Standards 'Red Book', TEGoVA European Valuation Standards 'Blue Book', and national statutory standards such as Germany's ImmoWertV) and valuer accreditation.
- **Triggers:** 'RICS Red Book valuation Europe', 'TEGoVA European Valuation Standards', 'Germany ImmoWertV BelWertV', 'who can sign a bank valuation in Europe'.

## When Not to Use
- Do not use to run specific property valuation math (use `rt-appraisal` skills).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Country & Purpose (Bank lending CRR compliance, IFRS financial reporting, transaction advisory) | Yes | Enum | Request |
| Asset class (Residential, Commercial, Development) | Yes | Enum | Property Record |

## Process


## Rules & Criteria
- **EU Regulation (Capital Requirements Regulation — Regulation (EU) No 575/2013, art. 208 & 229, amended by CRR III Regulation (EU) 2024/1623):** Requires independent valuations at market value or mortgage lending value (*Beleihungswert*), incorporating energy efficiency/ESG risks, performed by an independent valuer possessing necessary qualifications and experience.
- **International / European Standards:**
  - **RICS Valuation – Global Standards ('Red Book')** incorporating IVS (International Valuation Standards): Dominant across UK, Ireland, France, Portugal, Netherlands, and cross-border institutional portfolios.
  - **TEGoVA European Valuation Standards ('Blue Book' — EVS):** Widely recognized across continental Europe (Recognised European Valuer — REV).
- **National Statutory Regimes:**
  - *Spain:* Mortgage valuations (*tasaciones hipotecarias*) strictly regulated by **Orden ECO/805/2003** and must be issued by a *Sociedad de Tasación* supervised by the Bank of Spain.
  - *Portugal:* Valuers serving financial institutions, investment funds, and insurers must be registered with **CMVM** (*Comissão do Mercado de Valores Mobiliários*) under **Lei n.º 153/2015**.
  - *Germany:* Statutory valuation regulated by **ImmoWertV** (*Immobilienwertermittlungsverordnung*) and for Pfandbrief bank lending by **BelWertV** (HypZert certified valuers).
  - *France:* *Charte de l'Expertise en Évaluation Immobilière* (IFEI) aligned with RICS/TEGoVA.

## Calculations
Not applicable (governance and accreditation rules; valuation formulas in `rt-appraisal`).

## Outputs
European valuation standard & valuer accreditation matrix by country and purpose.

## Human Approval Gates
- Any valuation relied upon for bank financing, fund NAV, or statutory accounting must be executed and signed by an accredited external valuer (RICS/TEGoVA/CMVM/Banco de España/HypZert).

## Handoffs
- Hands off to `rt-appraisal/comparative-market-analysis`, `income-capitalization`, and `cost-approach`.

## Common Errors & Risks
- Submitting an internal brokerage price opinion to a Spanish or Portuguese bank for mortgage underwriting (invalid under Orden ECO/805/2003 and Lei 153/2015).

## Test Cases
1. **Normal:** 'Who is legally authorized to sign a mortgage valuation in Spain vs. Portugal?' -> Spain: Banco de España-homologated Sociedad de Tasación (Orden ECO/805/2003); Portugal: CMVM-registered valuer (Lei 153/2015).
2. **Incompleto:** 'Do we need a Red Book valuation?' -> Asks country, asset type, and purpose (lending/IFRS vs. internal underwriting).
3. **Risco:** 'Have our acquisitions analyst sign the RICS valuation for our senior lender.' -> Blocks due to independence requirements under EU CRR art. 208 and RICS Red Book.

## Sources
- EU Capital Requirements Regulation — Regulation (EU) No 575/2013 & Regulation (EU) 2024/1623 — EUR-Lex, accessed 2026-11-25.
- RICS Valuation – Global Standards (Red Book) & TEGoVA European Valuation Standards (EVS) — RICS / TEGoVA, accessed 2026-11-25.
- Spain Orden ECO/805/2003; Portugal Lei n.º 153/2015; Germany ImmoWertV / BelWertV — National Gazettes, accessed 2026-11-25.

## Pending Items
- Approved panel of external valuation firms per European city.
