---
plugin: rt-marketing
skill: campaign-planning
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de Marketing
---

# Real Estate Campaign Planning (Listings, Sales & Leasing)

## Objective & Triggers
Design demand-generation and inventory-acquisition campaigns defining target personas, value proposition, channel mix (portals, Meta, Google, local OOH), budget allocation, and funnel KPIs.
- **Triggers:** Invoke `rt-marketing/campaign-planning` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for individual listing copy (`listing-copywriting`) or paid bid optimization (`seo-paid-media`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Campaign goal (resale inventory, new development, lease-up, landlord acquisition), submarket, budget, campaign window. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Define target persona, positioning, and reverse-engineered lead/tour/deal goals — Marketing Manager — Day 1.
2. Allocate budget across high-intent channels (Portals/Google Search) vs. discovery/landlord acquisition (Meta/YouTube) — Media Specialist — Day 2.
3. Produce visual assets (pro photography, 3D tour, vertical video) and clear compliance — Creative Team — Days 3–5.

## Rules & Criteria
Market practice: Listings with professional photography and floor plans achieve 2x–3x higher portal CTR. Enforce housing ad targeting restrictions (Special Ad Category).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `campaign-planning` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Gerente de Marketing**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `campaign-planning` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `campaign-planning` request missing mandatory inputs (Campaign goal (resale inventory) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de Marketing** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
