---
plugin: rt-marketing
skill: social-media
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Analista de Social Media / Jurídico
---

# Social Media Content & Image/Likeness Rights

## Objective & Triggers
Plan editorial calendars (Reels/Shorts, educational carousels, property walkthroughs, client testimonials) while enforcing media copyright, tenant privacy in occupied homes, and likeness releases.
- **Triggers:** Invoke `rt-marketing/social-media` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for paid performance media buying (`seo-paid-media`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Authorized property portfolio, brand content pillars, filming/likeness release forms. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Confirm owner filming consent (and tenant notice/consent if occupied) prior to shooting interior video — Leasing/Marketing — Pre-shoot.
2. Blur license plates, personal documents, family photos, and sensitive security codes — Video Editor — Post-production.
3. Obtain signed Likeness Release from featured clients/agents and display brokerage license ID — Marketing — Pre-post.

## Rules & Criteria
Statutory: Right of publicity and privacy (GDPR/LGPD for identifiable individuals; US state publicity rights; commercial music licensing rules for business accounts).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `social-media` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Analista de Social Media / Jurídico**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `social-media` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `social-media` request missing Member State or core inputs (Authorized property portfolio) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Analista de Social Media / Jurídico** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
