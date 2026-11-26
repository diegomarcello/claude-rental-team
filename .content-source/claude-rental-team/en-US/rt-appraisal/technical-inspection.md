---
plugin: rt-appraisal
skill: technical-inspection
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro Civil / Inspetor Predial
---

# Technical Property Inspection & Defect Triage

## Objective & Triggers
Perform pre-acquisition or pre-handover physical inspection covering structure, roof, waterproofing, electrical, plumbing, and HVAC, classifying severity and specialist escalation triggers.
- **Triggers:** Invoke `rt-appraisal/technical-inspection` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for cosmetic tenant move-in/move-out condition reports (`rt-property-management/move-inspections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Building type and age, available plans, access to roof/electrical panels/risers, renovation history. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Inspect building systems in risk order: Structure -> Roof/Waterproofing -> Electrical -> Plumbing -> HVAC -> Envelope/Finishes — Inspector — Day 1.
2. Capture timestamped photo evidence and classify severity (Critical/Life-Safety, High/Major CapEx, Moderate/Maintenance, Cosmetic) — Inspector — Day 1.
3. Recommend invasive/specialist testing (thermography, hydrostatic test, core sampling, sewer scope) when concealed defects are suspected — Engineer — Day 2.

## Rules & Criteria
Standards: ABNT NBR 16747 (Building Inspection) in Brazil; ASTM E2018 (Property Condition Assessments — PCA) / InterNACHI in US; RICS Home Survey Standards in Europe.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable (technical severity rating: Grade 1 Minor, Grade 2 Moderate, Grade 3 Critical).

## Outputs
Standardized `technical-inspection` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Engenheiro Civil / Inspetor Predial**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `technical-inspection` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `technical-inspection` request missing mandatory inputs (Building type and age) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Engenheiro Civil / Inspetor Predial** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
