---
plugin: rt-crm
skill: pipeline-management
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de Operações / RevOps
---

# CRM Pipeline Management (Sales & Leasing Funnels)

## Objective & Triggers
Define clear pipeline stages, objective entry/exit criteria, maximum stage aging SLAs, and loss/stagnation rules across sales, leasing, and listing-acquisition funnels.
- **Triggers:** Invoke `rt-crm/pipeline-management` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for deduplication or retention purging (`crm-data-hygiene`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Target funnel (Sales, Leasing, Acquisitions/Listings), current CRM stages, historical stage conversion and aging metrics. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Structure stages around verifiable commitments (New Lead -> Qualified -> Tour Scheduled -> Tour Completed -> Offer/Application -> Underwriting/Contract -> Closed Won/Lost) — RevOps — Setup.
2. Configure stage-aging alerts — RevOps — Automated.
3. Enforce mandatory structured Loss Reason codes before closing a deal as Lost — Sales/Leasing — Continuous.

## Rules & Criteria
Market practice: Keep pipelines to 6–8 objective stages; enforce mandatory Stage Gate fields before advancing deals.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable.

## Outputs
Standardized `pipeline-management` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Gerente de Operações / RevOps**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `pipeline-management` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `pipeline-management` request missing Member State or core inputs (Target funnel (Sales) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Gerente de Operações / RevOps** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
