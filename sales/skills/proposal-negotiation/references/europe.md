---
plugin: rt-sales
skill: proposal-negotiation
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Diretor Comercial / Gerente de Vendas
---

# Offer Management, Counteroffers & Sales Negotiation

## Objective & Triggers
Manage receipt, formalization, and negotiation of purchase and lease offers, presenting all offers objectively to the seller/landlord, handling objections, and enforcing concession gates.
- **Triggers:** Invoke `rt-sales/proposal-negotiation` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use when the company itself is the principal buyer (`rt-acquisitions/purchase-negotiation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Written buyer offer, asking price, reference CMA, payment terms, commission concession approval gate. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Formalize every offer in writing specifying price, earnest money, contingencies, payment terms, and expiration (e.g., 48–72h) — Agent — Day 0.
2. Present all written offers promptly and objectively to the owner alongside CMA benchmarks — Agent/Manager — <= 24h.
3. Document signed counteroffers until mutual acceptance and hand off to closing/legal — Sales Manager — Days 1–3.

## Rules & Criteria
Statutory / Ethics: Brokers have a legal/fiduciary duty to submit all offers objectively and promptly to the seller (NAR Code of Ethics SOP 1-6; BR CC art. 723; EU brokerage codes). Any commission reduction requires prior manager approval.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `proposal-negotiation` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Diretor Comercial / Gerente de Vendas**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `proposal-negotiation` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `proposal-negotiation` request missing Member State or core inputs (Written buyer offer) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Diretor Comercial / Gerente de Vendas** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
