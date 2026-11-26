---
plugin: rt-jurisdictions
skill: sales-purchase
jurisdiction: europe
last_verified: 2026-11-25
confidence: verified
reviewer: European Real Estate Lawyer / Civil Law Notary
---

# Jurisdiction Europe — Property Conveyance, Notaries, Land Registry & Mortgage Credit (PT / ES / DE / FR)

## Objective & Triggers
Consolidate EU-level mortgage consumer rules (MCD) and national civil-law conveyance, notarial authentication, land registry, and pre-emption rules across key markets (Portugal, Spain, Germany, France).
- **Triggers:** 'buying property in Portugal Spain Germany France', 'EU mortgage credit directive reflection period', 'notary and land registry Europe', 'compromis de vente cooling off'.

## When Not to Use
- Do not use for property-specific title/encumbrance verification (use `rt-legal/title-due-diligence`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Country & Municipality | Yes | Text (e.g., Lisbon/PT, Madrid/ES, Berlin/DE, Paris/FR) | User / CRM |
| Purchase price & financing status | Yes | Numeric (EUR) + Enum | Offer |
| Buyer residency (EU/EEA vs. Non-EU) | Yes | Enum | KYC |

## Process


## Rules & Criteria
- **EU Directive (Mortgage Credit Directive — Directive 2014/17/EU):** Mandates European Standardised Information Sheet (ESIS) and a minimum **7-day reflection/withdrawal period** for consumer residential mortgages across all EU Member States.
- **EU Directive (Energy Performance of Buildings — Directive (EU) 2024/1275 EPBD):** Mandatory valid Energy Performance Certificate (EPC) required at listing and handover.
- **Country Rules:**
  - *Portugal:* Preliminary contract (**CPCV** — Código Civil art. 410) typically carries a 10%–20% deposit (*sinal*); buyer default forfeits deposit, seller default requires returning double (*sinal em dobro*, CC art. 442). Final deed (*Escritura Pública* or *Documento Particular Autenticado — DPA*) registered at Conservatória do Registo Predial; requires *Caderneta Predial*, *Certidão Permanente*, *Licença de Utilização* (note Simplex Urbanístico DL 10/2024 simplifications), and *Ficha Técnica de Habitação*.
  - *Spain:* *Contrato de Arras Penitenciales* (Código Civil art. 1454) permits either party to withdraw (buyer loses deposit; seller pays double). Public Deed (*Escritura Pública*) executed before a Spanish Notary and inscribed in *Registro de la Propiedad*. Foreign buyers require a **NIE** (*Número de Identidad de Extranjero*).
  - *Germany:* Strict **Abstraction Principle** (*Abstraktionsprinzip*): preliminary agreements are void unless notarized (BGB § 311b). Ownership passes only upon notarized conveyance agreement (*Auflassung*, BGB § 925) **and** registration in the Land Register (*Grundbuch*, BGB § 873), following clearance of municipal pre-emption (*Vorkaufsrecht*) and tax clearance certificate (*Unbedenklichkeitsbescheinigung*).
  - *France:* After signing *Compromis* or *Promesse Unilatérale de Vente*, a non-professional residential buyer enjoys a mandatory **10-day cooling-off period** (*délai de rétractation*, Code de la construction et de l'habitation art. L271-1). Mandatory technical diagnostic file (**DDT** — lead, asbestos, termites, gas, electricity, ERP, DPE energy rating). Final *Acte Authentique* executed by a French *Notaire*.
- **Company Decision:** `[PENDING: Confirm target European countries and local notarial/legal counsel]`. 

## Calculations
**Estimated Acquisition Transaction Costs (Buyer Side, Resale Residential):**
- **Portugal (€400,000 urban primary residence):** IMT (progressive scale ~€18,700) + Stamp Duty 0.8% (€3,200) + Notary/Registration (~€1,000) = **~€22,900 (~5.7%)**.
- **Spain (€400,000 resale in Madrid vs. Catalonia):** ITP (6% Madrid = €24,000; 10% Catalonia = €40,000) + Notary/Registry (~€2,200) = **€26,200 – €42,200 (6.5% – 10.5%)**.
- **Germany (€400,000 resale in Berlin):** Grunderwerbsteuer (6.0% Berlin = €24,000; ranges 3.5% Bavaria to 6.5% NRW) + Notary & Grundbuch (~2.0% = €8,000) = **~€32,000 (~8.0%)**.
- **France (€400,000 resale in Paris):** *Frais de notaire* (transfer taxes ~5.8% + notary emoluments/disbursements ~1.7% = ~7.5%) = **~€30,000 (~7.5%)**.

## Outputs
Country-specific conveyance roadmap, mandatory diagnostics/certificates checklist, and transaction cost breakdown.

## Human Approval Gates
- Claude **never** drafts binding CPCV/Arras/Compromis agreements or waives municipal/tenant pre-emption rights without a local qualified lawyer or civil-law notary.

## Handoffs
- Hands off to `rt-legal/title-due-diligence` and `rt-sales/closing-checklist`.

## Common Errors & Risks
- Treating an un-notarized reservation agreement in Germany as legally binding.
- Signing a Portuguese CPCV without verifying municipal/heritage pre-emption rights (*direito de preferência* via Casa Pronta).
- Delivering a French *Compromis* without starting the mandatory 10-day statutory cooling-off notification properly.

## Test Cases
1. **Normal:** 'What is the cooling-off period after signing a Compromis de Vente in France?' -> 10 calendar days under Art. L271-1 CCH for non-professional residential buyers.
2. **Incompleto:** 'How much are closing taxes for a €500k apartment in Europe?' -> Asks for the specific country and region/autonomous community (rates range from ~5% to >11%).
3. **Risco:** 'The seller in Portugal wants to sign a CPCV today without showing the Land Registry extract (Certidão Permanente) or energy certificate.' -> Advises against signing without verifying title encumbrances and mandatory EPC.

## Sources
- EU Mortgage Credit Directive — Directive 2014/17/EU — EUR-Lex (`eur-lex.europa.eu`), accessed 2026-11-25.
- Energy Performance of Buildings Directive — Directive (EU) 2024/1275 — EUR-Lex, accessed 2026-11-25.
- Código Civil Português (arts. 410, 442); Código Civil Español (art. 1454); German BGB (§§ 311b, 873, 925); French CCH (art. L271-1) — National Official Gazettes, accessed 2026-11-25.

## Pending Items
- Confirm exact European target jurisdictions beyond PT, ES, DE, and FR.
