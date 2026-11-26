---
plugin: rt-renovation
skill: scope-of-work
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro / Arquiteto Coordenador
---

# Renovation Scope of Work (SOW) & Specifications

## Objective & Triggers
Translate inspection findings and commercial strategy (rent-ready turn vs. high-end flip) into a trade-by-trade Scope of Work detailing materials, exclusions, and acceptance criteria.
- **Triggers:** Invoke `rt-renovation/scope-of-work` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for unit pricing or contractor markup math (`renovation-budget`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Technical inspection report, target finish tier, floor plans/measurements, HOA/municipal restrictions. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Align finish specification tier with target ARV or market rent (avoid over-improving) — Acquisitions/Construction — Day 1.
2. Detail trade-by-trade tasks (Demo, Framing, Plumbing, Electrical, Drywall, Tile/Flooring, Paint, Windows/Doors, Millwork, Final Clean) — Engineer/Architect — Days 2–3.
3. Explicitly state exclusions (e.g., appliances, staging) and objective acceptance criteria — Engineer — Day 3.

## Rules & Criteria
Market practice: Standardize material finish packages by asset tier to capture bulk procurement discounts and simplify future maintenance.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `scope-of-work` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Engenheiro / Arquiteto Coordenador**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `scope-of-work` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `scope-of-work` request missing mandatory inputs (Technical inspection report) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Engenheiro / Arquiteto Coordenador** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
