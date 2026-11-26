---
plugin: rt-marketing
skill: listing-copywriting
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Marketing / Compliance
---

# Property Listing Copywriting & Portal Compliance

## Objective & Triggers
Write high-converting, accurate listing titles and descriptions for MLS/portals and brochures, ensuring mandatory statutory disclosures and zero discriminatory or prohibited phrasing.
- **Triggers:** Invoke `rt-marketing/listing-copywriting` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for social media content calendars (`social-media`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Full property fact sheet (net living area, beds/baths, parking, price/rent, HOA/condo fee, property tax, EU EPC rating, brokerage license ID), key features. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Verify mandatory jurisdictional disclosures (CRECI in BR; Brokerage Name/Equal Housing in US; EPC class & fee schedule in EU) — Marketing — Pre-draft.
2. Write benefit-led headline + structured copy (Hook -> Layout/Rooms -> Building Amenities -> Neighborhood/Transit -> Pricing & Fees) — Copywriter — Day 1.
3. Run Fair Housing / Truth-in-Advertising compliance check before publishing — Coordinator — Pre-publish.

## Rules & Criteria
Statutory: Strict ban on direct or coded discriminatory language (Fair Housing Act 42 U.S.C. § 3604(c); EU Unfair Commercial Practices Directive; BR CDC). Describe property features and neighborhood amenities strictly, never ideal resident demographics.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `listing-copywriting` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Marketing / Compliance**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `listing-copywriting` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `listing-copywriting` request missing Member State or core inputs (Full property fact sheet (net living area) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Marketing / Compliance** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
