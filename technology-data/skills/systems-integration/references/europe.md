---
plugin: rt-technology-data
skill: systems-integration
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Arquiteto de Soluções / TI
---

# Systems Integration, APIs & MCP Connectors

## Objective & Triggers
Design and document integrations across CRM, ERP/PMS, listing portals, e-signature, banking rails, and `claude-rental-team` MCP servers.
- **Triggers:** Invoke `rt-technology-data/systems-integration` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for analytics dashboard modeling (`bi-reporting`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Active tech stack, available APIs/webhooks, auth method, sync frequency. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Define Single Source of Truth per entity — Solutions Architect — Phase 1.
2. Build idempotent webhooks and MCP connectors with DLQ — Integration Engineer — Phase 2.
3. Store all tokens/API keys in a managed Secrets Vault — InfoSec — Continuous.

## Rules & Criteria
Market practice: Event-driven webhooks for real-time workflows and nightly batch jobs for ledger reconciliation.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `systems-integration` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Arquiteto de Soluções / TI**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `systems-integration` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `systems-integration` request missing Member State or core inputs (Active tech stack) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Arquiteto de Soluções / TI** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
