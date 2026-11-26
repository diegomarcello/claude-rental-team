---
plugin: rt-jurisdictions
skill: aml
jurisdiction: europe
last_verified: 2026-11-25
confidence: verified
reviewer: European MLRO (Money Laundering Reporting Officer)
---

# Jurisdiction Europe — Anti-Money Laundering (EU AML Directives / AMLR, Real Estate Agents & High-Value Rentals)

## Objective & Triggers
Define European AML/CFT obligations for real estate agents, brokers, developers, and high-value leasing under the EU AML framework (AMLD5/6 and EU Single Rulebook Regulation (EU) 2024/1624 — AMLR) and national FIUs.
- **Triggers:** 'EU AML rules real estate agents', 'rental threshold AML Europe 10000 euros', 'Beneficial Owner UBO check real estate Europe', 'TRACFIN SEPBLAC IMPIC FIU reporting'.

## When Not to Use
- Do not use to complete a specific client's KYC file (use `rt-legal/privacy-aml`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Transaction type (Purchase/Sale vs. Lease) & monthly rent / sale price | Yes | Enum + Numeric (EUR) | Deal |
| Client structure (Natural person, Legal entity, Trust/Foundation, PEP) | Yes | Enum | KYC |
| Country of operation (PT, ES, DE, FR) | Yes | Text | Operations |

## Process


## Rules & Criteria
- **EU Regulation / Directives (AMLD5 Directive (EU) 2018/843 & EU Anti-Money Laundering Regulation — Regulation (EU) 2024/1624 'AMLR'):**
  - *Obliged Entities:* Estate agents and brokers are obliged entities not only for **buying and selling** real estate, but also when acting as intermediaries in the **letting of immovable property** where the **monthly rent amounts to €10,000 or more** (or equivalent).
  - *EU-Wide Cash Payment Limit (AMLR Art. 80):* Introduces an EU-wide cap of **€10,000** on cash payments in commercial transactions (with stricter national caps already in force: **€1,000** in Spain for resident business transactions under Ley 11/2021; **€1,000** in France for residents; **€3,000** in Portugal under Lei 92/2017; **€0 cash prohibition** for real estate purchases in Germany since April 2023 under GwG § 16a — real estate cannot be paid in cash, crypto, or commodities!).
  - *Beneficial Ownership (UBO):* Mandatory identification and verification against national UBO registers (RCBE in PT; Registro Mercantil UBO in ES; Transparenzregister in DE; Registre des Bénéficiaires Effectifs in FR).
  - *Record Retention:* **5 years** after the end of the business relationship or occasional transaction (10 years in Spain under Ley 10/2010 art. 25).
  - *Tipping-Off Prohibition:* Strict criminal/administrative ban on disclosing to the customer or third parties that an STR has been or will be filed.

## Calculations
**Key European AML Thresholds & Cash Caps:**
- **Leasing CDD Trigger (EU-wide):** Monthly rent $\ge \mathbf{€10,000/\text{month}}$
- **Real Estate Cash Caps:** Germany = **€0** (strictly prohibited, GwG § 16a); Spain & France = **€1,000** (residents); Portugal = **€3,000**; EU AMLR ceiling = **€10,000**.
- **Record Retention:** **5 years** (EU standard) / **10 years** (Spain).

## Outputs
European AML/CDD determination matrix, national cash-cap table, and FIU escalation protocol.

## Human Approval Gates
- MLRO must approve onboarding of any PEP, high-risk third-country buyer, or complex corporate/trust structure, and holds sole authority to file STRs with national FIUs.

## Handoffs
- Hands off to `rt-legal/privacy-aml` and `rt-finance/accounts-receivable`.

## Common Errors & Risks
- Failing to run full KYC/UBO checks on a luxury lease at €12,000/month (covered by EU AML rules since AMLD5).
- Accepting physical cash for a property deposit in Germany (violates GwG § 16a ban on cash/crypto in real estate transactions).

## Test Cases
1. **Normal:** 'When does a residential rental trigger mandatory EU AML customer due diligence?' -> When the monthly rent is €10,000 or more.
2. **Incompleto:** 'Can a buyer pay a €5,000 deposit in cash?' -> Asks for the country (prohibited in Germany under GwG § 16a, above €1,000 cap in France/Spain, above €3,000 cap in Portugal).
3. **Risco:** 'A corporate buyer refuses to disclose its natural-person UBOs behind a BVI holding company.' -> Blocks transaction immediately; AML rules prohibit establishing a business relationship when CDD/UBO cannot be completed.

## Sources
- EU Anti-Money Laundering Regulation — Regulation (EU) 2024/1624 & Directive (EU) 2018/843 (AMLD5) — EUR-Lex, accessed 2026-11-25.
- Germany Geldwäschegesetz (GwG § 16a); Spain Ley 10/2010 & Ley 11/2021; Portugal Lei 83/2017 & Lei 92/2017; France Code monétaire et financier (art. L561-2) — National Gazettes, accessed 2026-11-25.

## Pending Items
- Confirm national regulator registrations (e.g., IMPIC AMI license in Portugal; Carte T in France; § 34c GewO in Germany).
