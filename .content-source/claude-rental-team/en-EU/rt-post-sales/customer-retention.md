---
plugin: rt-post-sales
skill: customer-retention
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Sucesso do Cliente
---

# Customer Retention, NPS & Referral Programs

## Objective & Triggers
Measure NPS/CSAT at key lifecycle milestones, trigger proactive detractor recovery, and drive compliant landlord/buyer referrals.
- **Triggers:** Invoke `rt-post-sales/customer-retention` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for technical CRM workflow setup (`rt-crm/journey-automation`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Completed milestone, NPS score (0–10), verbatim feedback. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Trigger transactional NPS survey 7 days post-closing or 60 days post-move-in — CS Automation — D+7 / D+60.
2. Trigger 'Detractor (0–6)' manager outreach within 24h — CS Manager — <= 24h.
3. Invite 'Promoters (9–10)' to review on Google and join compliant referral programs — CS — D+3.

## Rules & Criteria
Statutory: In the US, paying cash/gift-card referral fees to unlicensed individuals violates state licensing acts and RESPA § 8.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**NPS Formula:** $\text{NPS} = \%\text{Promoters (9–10)} - \%\text{Detractors (0–6)}$ (scale -100 to +100).

## Outputs
Standardized `customer-retention` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Sucesso do Cliente**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `customer-retention` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `customer-retention` request missing Member State or core inputs (Completed milestone) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Sucesso do Cliente** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
