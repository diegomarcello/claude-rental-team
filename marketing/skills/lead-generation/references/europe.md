---
plugin: rt-marketing
skill: lead-generation
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Marketing / DPO
---

# Lead Capture, Consent Logging & Attribution

## Objective & Triggers
Design web forms, click-to-WhatsApp flows, and landing pages with minimal friction fields, auditable consent timestamps (LGPD/TCPA/GDPR), and end-to-end UTM attribution.
- **Triggers:** Invoke `rt-marketing/lead-generation` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for sales follow-up sequences (`rt-pre-sales/follow-up-cadence`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Source channel, form fields, privacy/consent disclosure copy, CRM webhook endpoint. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Restrict initial lead forms to essential fields (Name, Phone/SMS, Email, Intent) to maximize conversion and enforce data minimization — Marketing — Setup.
2. Store `consent_timestamp`, `consent_text_version`, `ip_address`, and UTM parameters (`utm_source`, `utm_medium`, `utm_campaign`) in CRM — Tech/Marketing — Automated.
3. Route lead immediately (< 60 seconds) to Pre-Sales queue — CRM — Real-time.

## Rules & Criteria
Statutory: Demonstrable proof of consent required under GDPR Art. 7(1), LGPD Art. 8 §2, and US TCPA (PEWC for automated calls/SMS).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `lead-generation` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Marketing / DPO**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `lead-generation` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `lead-generation` request missing Member State or core inputs (Source channel) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Marketing / DPO** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
