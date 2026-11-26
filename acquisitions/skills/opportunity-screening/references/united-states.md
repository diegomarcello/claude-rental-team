---
plugin: rt-acquisitions
skill: opportunity-screening
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de Aquisições
---

# Opportunity Screening & Auction Triage

## Objective & Triggers
Screen acquisition opportunities (on-market, off-market, foreclosure/judicial auctions, distressed assets) using knock-out criteria and weighted scoring prior to full underwriting.
- **Triggers:** Invoke `rt-acquisitions/opportunity-screening` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for detailed IRR/NPV underwriting (`deal-feasibility`) or full legal title review (`rt-legal/title-due-diligence`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Location, asset type, area, asking price/minimum bid, occupancy status, visible physical condition, source (auction/owner/broker), preliminary title summary. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Apply hard knock-out filters — Acquisitions Analyst — Day 0.
2. Score asset across 5 pillars (Location/Liquidity, Discount to Market, Rehab Complexity, Legal/Occupancy Risk, Strategic Fit) — Analyst — Day 1.
3. Issue triage verdict (Advance to Underwriting, Watchlist, or Pass) — Acquisitions Manager — Day 1.

## Rules & Criteria
Market practice: Target discount to After-Repair Value (ARV) >= 25%–30% for flips; entry cap rate >= risk-free rate + 300 bps for hold. Typical knock-outs: severe flood/geotechnical hazard, incurable title cloud, non-conforming uninsurable structure. Company decision: `[PENDING: Confirm target submarkets and minimum passing score]`.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Weighted score (0–100 pts; standard pass >= 70 pts): Location (30%), Discount/Spread (30%), Rehab Scope (15%), Title/Occupancy (15%), Liquidity (10%).

## Outputs
Standardized `opportunity-screening` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Gerente de Aquisições**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `opportunity-screening` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `opportunity-screening` request missing mandatory inputs (Location) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de Aquisições** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
