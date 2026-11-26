---
plugin: rt-jurisdictions
skill: leasing
jurisdiction: europe
last_verified: 2026-11-25
confidence: verified
reviewer: European Tenancy Lawyer
---

# Jurisdiction Europe — Residential & Commercial Leasing, Rent Controls & Eviction (PT / ES / DE / FR)

## Objective & Triggers
Consolidate tenancy duration, security deposit caps, indexation/rent control rules, notice periods, and eviction rules across Portugal, Spain, Germany, and France.
- **Triggers:** 'rental laws Portugal NRAU', 'Spain LAU residential lease rules', 'Germany Mietpreisbremse deposit cap', 'France Loi Alur deposit and winter eviction ban'.

## When Not to Use
- Do not use for individual tenant screening workflows (use `rt-property-management/tenant-screening`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Country & City | Yes | Text | Property Record |
| Lease type (Primary residence, Short-term/AL, Commercial) | Yes | Enum | Lease |
| Monthly rent & furnished status | Yes | Numeric (EUR) + Enum | Lease |

## Process


## Rules & Criteria
- **Portugal (NRAU — Lei n.º 6/2006 & Código Civil arts. 1022–1113):**
  - *Deposit & Advance Rent:* Security deposit (*caução*) plus advance rent capped by Law 56/2023 (*Mais Habitação* amendments to CC art. 1076): maximum **2 months** advance rent and **2 months** security deposit.
  - *Duration & Renewal:* Fixed-term residential leases without specified term default to 5 years; minimum 1-year term for standard fixed-term contracts (automatically renewing for 3 years unless otherwise stipulated, CC art. 1096). Annual rent update follows INE statutory coefficient (*coeficiente de atualização de rendas*).
  - *Eviction:* Special Eviction Procedure (*Procedimento Especial de Despejo — PED*) via **BAS** (*Balcão do Arrendatário e do Senhorio*) after 3 months arrears (or 8 days delay > 4 times in 12 months).
- **Spain (LAU — Ley 29/1994 de Arrendamientos Urbanos, reformed by Ley 12/2023 de Vivienda):**
  - *Minimum Term:* **5 years** mandatory extension if landlord is an individual, or **7 years** if landlord is a legal entity (LAU art. 9), plus 3-year tacit extension (art. 10). Tenant may terminate after 6 months with 30 days' notice.
  - *Deposit:* Mandatory statutory *fianza* of **1 month** (residential) or **2 months** (commercial), deposited with regional housing agency (e.g., IVIMA/INCASÒL), plus maximum **2 months** additional guarantee for residential leases <= 5/7 years (LAU art. 36).
  - *Rent Caps:* In declared Stressed Residential Market Zones (*Zonas de Mercado Residencial Tensionado*, e.g., Catalonia), large landlords (*gran tenedor*, >= 5 or 10 units per regional definition) face reference price index caps.
- **Germany (BGB §§ 535–580a):**
  - *Indefinite Term:* Standard residential leases are indefinite (*unbefristet*); fixed-term (*Zeitmietvertrag*, § 575) is valid only for strict statutory reasons (e.g., landlord own use). Landlord termination requires legitimate interest (*berechtigtes Interesse*, e.g., *Eigenbedarf* — personal use, § 573), with 3 to 9 months' notice depending on tenancy length.
  - *Deposit:* Capped at **3 months' net cold rent** (*Kaltmiete*, BGB § 551), payable in 3 monthly installments and held in an insolvency-protected segregated account.
  - *Rent Control:* *Mietpreisbremse* (§ 556d) caps new lease rents at local comparative rent (*Mietspiegel*) + 10% in tight markets; existing rent increases capped at 15%–20% over 3 years (*Kappungsgrenze*, § 558).
- **France (Loi n.º 89-462 du 6 juillet 1989 & Loi ALUR):**
  - *Minimum Term:* **3 years** unfurnished (*location vide*) if landlord is individual (**6 years** if legal entity); **1 year** furnished (*location meublée*, or 9 months student lease).
  - *Deposit:* Capped at **1 month** excluding charges (unfurnished) or **2 months** (furnished).
  - *Rent Control & Winter Ban:* *Encadrement des loyers* applies in Paris, Lyon, Lille, Bordeaux, etc.; indexation tied to INSEE **IRL** (*Indice de Référence des Loyers*), with rent freezes for F/G energy-rated dwellings (*passoires thermiques*). **Trêve hivernale** prohibits physical eviction between **November 1 and March 31** each year.

## Calculations
**Maximum Statutory Security Deposit Comparison:**
- **Portugal:** Max **2 months** deposit + max **2 months** advance rent.
- **Spain:** **1 month** statutory *fianza* + max **2 months** additional guarantee = **3 months** total.
- **Germany:** Max **3 months** *Kaltmiete* (net cold rent).
- **France:** Max **1 month** (unfurnished) / **2 months** (furnished) excluding charges.

## Outputs
Jurisdictional tenancy matrix covering minimum term, deposit limits, rent indexation/caps, and eviction constraints.

## Human Approval Gates
- Claude **never** issues a landlord termination notice (*Eigenbedarf*, *congé pour reprise*, or *oposição à renovação*) without local tenancy counsel verifying statutory notice periods and form requirements.

## Handoffs
- Hands off to `rt-property-management/lease-administration` and `rt-legal/disputes-eviction`.

## Common Errors & Risks
- Demanding 6 months' rent upfront + 3 months' deposit in Portugal (illegal under CC art. 1076).
- Attempting to schedule a physical eviction in France during the *trêve hivernale* (Nov 1 – Mar 31).
- Using a fixed-term 1-year residential lease in Germany without a valid BGB § 575 statutory justification (automatically converts to an indefinite lease).

## Test Cases
1. **Normal:** 'What is the maximum security deposit for an unfurnished apartment in France vs. Germany?' -> France: 1 month excluding charges; Germany: 3 months net cold rent (*Kaltmiete*).
2. **Incompleto:** 'Can we raise the rent by 8% on our apartment in Spain?' -> Asks whether the property is in a declared Stressed Zone (*Zona Tensionada*), whether the landlord is a *gran tenedor*, and checks the annual INE housing rent update index.
3. **Risco:** 'Schedule the bailiff to evict the non-paying Paris tenant on January 15.' -> Blocks action due to the French *trêve hivernale* (Nov 1 – Mar 31) prohibiting physical evictions.

## Sources
- Portugal: Código Civil (arts. 1076, 1096) & NRAU (Lei 6/2006) — Diário da República (`diariodarepublica.pt`), accessed 2026-11-25.
- Spain: Ley 29/1994 (LAU) & Ley 12/2023 — BOE (`boe.es`), accessed 2026-11-25.
- Germany: Bürgerliches Gesetzbuch (BGB §§ 551, 556d, 558, 573, 575) — Gesetze im Internet, accessed 2026-11-25.
- France: Loi n° 89-462 du 6 juillet 1989 — Légifrance (`legifrance.gouv.fr`), accessed 2026-11-25.

## Pending Items
- Regional stressed-zone maps in Spain and annual INE/IRL coefficients.
