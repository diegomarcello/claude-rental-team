---
plugin: rt-crm
skill: journey-automation
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Especialista de Automação CRM
---

# Lifecycle Journey Automation & Event Triggers

## Objective & Triggers
Configure automated CRM workflows for landlord/tenant onboarding, lease renewal alerts, contract anniversaries, and reactivation, enforcing consent gates and exit triggers.
- **Triggers:** Invoke `rt-crm/journey-automation` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for cold outbound prospecting (`rt-pre-sales/follow-up-cadence`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Trigger event, channel, opt-in flag, exit conditions. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Enforce entry guardrails (active opt-in + no legal hold) — RevOps — Setup.
2. Configure workflow steps and instant exit triggers — CRM Admin — Setup.
3. Audit delivery rates and opt-outs weekly — RevOps — Weekly.

## Rules & Criteria
Statutory / Carrier Rule: Use only approved business messaging APIs with registered templates and opt-out handling.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `journey-automation` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Especialista de Automação CRM**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `journey-automation` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `journey-automation` request missing Member State or core inputs (Trigger event) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Especialista de Automação CRM** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
