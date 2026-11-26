---
plugin: rt-pre-sales
skill: follow-up-cadence
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Pré-vendas
---

# Omnichannel Follow-Up Cadences & Contact Compliance

## Objective & Triggers
Define structured multi-channel outreach sequences (phone, SMS/WhatsApp, email) for new and post-tour leads while enforcing quiet hours, frequency caps, and instant opt-out.
- **Triggers:** Invoke `rt-pre-sales/follow-up-cadence` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for delinquent rent collections (`rt-finance/collections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Lead funnel stage, consented channels, lead time zone, interaction history. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Execute high-touch 5-day cadence for inbound leads (D0: call + SMS/WhatsApp + email; D1, D2, D4, D5) strictly within quiet-hour limits (8am–8pm lead local time) — SDR — Days 0–5.
2. Transition unresponsive leads to low-frequency biweekly/monthly value-nurture — CRM Automation — Days 6–90.
3. Immediately suppress any channel upon opt-out ('STOP', unsubscribe) and lock against re-enrollment — CRM — Real-time.

## Rules & Criteria
Statutory: TCPA quiet hours (8:00 AM – 9:00 PM local time, 47 CFR § 64.1200(c)(1)) and PEWC for SMS; GDPR/ePrivacy and LGPD Art. 18 for immediate opt-out.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `follow-up-cadence` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador de Pré-vendas**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `follow-up-cadence` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `follow-up-cadence` request missing mandatory inputs (Lead funnel stage) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Pré-vendas** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
