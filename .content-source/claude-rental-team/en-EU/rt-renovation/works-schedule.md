---
plugin: rt-renovation
skill: works-schedule
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de Obras
---

# Renovation Schedule, Critical Path & Draw Milestones

## Objective & Triggers
Sequence construction trades with technical dependencies, identify critical-path bottlenecks (windows, custom millwork, inspections), and tie progress draws to verified physical milestones.
- **Triggers:** Invoke `rt-renovation/works-schedule` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for itemized cost estimation (`renovation-budget`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Scope of work, approved budget, building work-hour restrictions, vendor lead times. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Build WBS in trade sequence: Protection/Demo -> Rough-in MEP -> Framing/Drywall -> Waterproofing/Tile -> Primer -> Millwork/Fixtures/Trim -> Final Coat/Punch/Clean — Construction Manager — Pre-work.
2. Flag critical-path long-lead items and release POs in Week 1 — Procurement/Construction — Week 1.
3. Tie contractor draws strictly to inspected physical milestones — Construction/Finance — Continuous.

## Rules & Criteria
Market practice: Cap mobilization deposit at 10%–15%; retain 5%–10% holdback/retainage until 100% punch-list completion and lien waivers are delivered.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `works-schedule` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Gerente de Obras**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `works-schedule` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `works-schedule` request missing Member State or core inputs (Scope of work) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de Obras** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
