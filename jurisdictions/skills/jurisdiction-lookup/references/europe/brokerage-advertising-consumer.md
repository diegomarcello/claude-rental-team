---
plugin: rt-jurisdictions
skill: brokerage-advertising-consumer
jurisdiction: europe
last_verified: 2026-11-25
confidence: verified
reviewer: European Regulatory & Consumer Law Counsel
---

# Jurisdiction Europe — Brokerage Licensing, Commission Rules, EPC Advertising & Consumer Rights

## Objective & Triggers
Consolidate European real estate brokerage licensing, written mandate requirements, commission rules, mandatory Energy Performance Certificate (EPC) ad disclosures, and EU consumer protection rules.
- **Triggers:** 'real estate agent license Portugal France Germany Spain', 'mandatory EPC in real estate ads Europe', 'Germany Bestellerprinzip commission split', 'France Loi Hoguet Carte T'.

## When Not to Use
- Do not use for internal agent commission split math (use `rt-sales/commission-calculation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Country & Region | Yes | Text | Operations |
| Transaction type (Sale vs. Rental) & Who pays commission | Yes | Enum | Mandate |
| Marketing channel (Portal, print, social media, window display) | Yes | Enum | Marketing |

## Process


## Rules & Criteria
- **EU Directive (EPBD — Directive (EU) 2024/1275):** Every advertisement in commercial media for sale or rental must state the property's **Energy Performance Certificate (EPC) indicator/class** (e.g., A–G).
- **EU Directive (Consumer Rights Directive — Directive 2011/83/EU & Omnibus Directive (EU) 2019/2161):** Consumers signing a brokerage mandate online or off-premises (e.g., at their home) have a **14-day right of withdrawal** (*droit de rétractation* / *Widerrufsrecht*). Unfair Commercial Practices Directive (2005/29/EC) prohibits misleading omissions (e.g., hiding agency fees or floor area).
- **Country Rules:**
  - *Portugal (Lei n.º 15/2013):* Requires **AMI License** issued by **IMPIC**, civil liability insurance, written *Contrato de Mediação Imobiliária* (CMI), and inclusion of AMI license number in all ads. Commission is generally due upon execution of the final deed (or CPCV if expressly agreed).
  - *France (Loi Hoguet — Loi n.º 70-9 du 2 janvier 1970):* Strict requirement for **Carte Professionnelle ('Carte T')**, financial guarantee, professional indemnity insurance, and a **written, numbered mandate** registered in the *Registre des Mandats* *before* marketing or showing a property (zero right to commission without a prior valid written mandate). Ads must display exact fee schedule (*barème*), who pays (*charge vendeur* vs. *charge acquéreur*), DPE energy class, GES emissions, and 'Climat et Résilience' estimated annual energy cost.
  - *Germany (§ 34c GewO & BGB §§ 652–656d):* Requires trade permit under § 34c GewO and continuous training (*MaBV*). Brokerage contracts for residential apartments/houses require **text form** (BGB § 656a). Under **BGB § 656c (Half-Split Rule)**, when a broker acts for both seller and buyer of a residential apartment/single-family house, both parties must pay **equal commission shares** (buyer cannot pay more than seller). For residential rentals, **Bestellerprinzip** (WoVermRG § 2(1a)) mandates that whoever orders the broker (usually the landlord) pays the fee — charging tenants is illegal.
  - *Spain (Ley 12/2023 & Regional Registries):* Residential rental agency fees and contract formalization costs must be borne by the **landlord** (*arrendador*) when landlord is a legal entity (and in practice broadly enforced under LAU art. 20(1) amended by Ley 12/2023). Mandatory energy label (*etiqueta energética*) in all ads (RD 390/2021).

## Calculations
**Germany Residential Sales Commission Split (BGB § 656c):**
$$\text{Buyer Share} \le \text{Seller Share}$$
- **Numerical Example (€500,000 apartment in Munich, total commission 7.14% incl. 19% VAT):**
  - Seller pays **3.57% (€17,850)**; Buyer pays **3.57% (€17,850)**. Charging Buyer 5.95% and Seller 1.19% is void under BGB § 656c.

## Outputs
European brokerage & advertising compliance checklist (licenses, written mandate rule, commission allocation rules, mandatory EPC/fee disclosures).

## Human Approval Gates
- Managing Broker / License Holder must approve all standard mandate templates and fee schedules (*barèmes*).

## Handoffs
- Hands off to `rt-marketing/listing-copywriting` and `rt-sales/proposal-negotiation`.

## Common Errors & Risks
- Marketing a French property before signing and registering a numbered *Mandat* under Loi Hoguet (forfeits all legal right to commission).
- Charging a prospective residential tenant an agency finder's fee in Germany (*Bestellerprinzip*) or Spain (LAU art. 20(1)).
- Publishing a listing portal ad without the property's EPC energy class.

## Test Cases
1. **Normal:** 'Can we charge the tenant a 1-month agency commission on a residential apartment in Berlin or Madrid?' -> No; prohibited under Germany's *Bestellerprinzip* (WoVermRG) and Spain's LAU art. 20(1).
2. **Incompleto:** 'What needs to go on a property listing in France?' -> DPE/GES energy & climate ratings, estimated annual energy spend, agency fee schedule (*barème*), who pays fees, and Carte T / co-ownership lot count.
3. **Risco:** 'An agent started showing a Paris apartment based on an email from the owner without a signed mandate.' -> Warns that under Loi Hoguet, no commission can legally be claimed without a prior signed, registered written mandate.

## Sources
- EU EPBD Directive (EU) 2024/1275 & Consumer Rights Directive 2011/83/EU — EUR-Lex, accessed 2026-11-25.
- Portugal Lei n.º 15/2013; France Loi n.º 70-9 (Loi Hoguet); Germany BGB §§ 656a–656d & WoVermRG; Spain LAU art. 20 & RD 390/2021 — National Gazettes, accessed 2026-11-25.

## Pending Items
- Confirm local regional brokerage registration numbers in Spain (e.g., AICAT Catalonia, RAIN Madrid).
