---
plugin: rt-property-management
skill: lease-administration
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Administração de Carteira
---

# Lease Administration, Annual Rent Indexation & Renewals

## Objective & Triggers
Manage active lease lifecycles, compute annual rent indexation using official indices (IPCA/IGP-M in BR; CPI/AB 1482 in US; IRL/INE/HICP in EU), trigger D-90 renewal workflows, and calculate prorated termination fees.
- **Triggers:** Invoke `rt-property-management/lease-administration` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for past-due rent collections (`rt-finance/collections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Current rent, anniversary date, contractual index, 12-month index variation, statutory rent cap, lease expiration date. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Trigger D-90 expiration alert to align renewal terms with landlord — Portfolio Analyst — D-90.
2. Pull trailing 12-month official index rate at anniversary and enforce statutory caps — Analyst — D-30.
3. Deliver statutory rent-increase notice / renewal addendum within legal notice window — Analyst — D-30.
4. Update ERP billing schedule — Finance — D-15.

## Rules & Criteria
Statutory: Annual minimum indexation in BR (Lei 10.192/2001); 1-yr IRL claim limit in FR (Loi 1989 art. 17-1); 30/90-day notice rules in CA (Cal. Civ. Code § 827).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
**Annual Indexation Formula:** $\text{New Rent} = \text{Current Rent} \times (1 + I_{12m})$. Example: $3,500.00 \times 1.0462 = \mathbf{3,661.70}$.

## Outputs
Standardized `lease-administration` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Coordenador de Administração de Carteira**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `lease-administration` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `lease-administration` request missing mandatory inputs (Current rent) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Administração de Carteira** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
