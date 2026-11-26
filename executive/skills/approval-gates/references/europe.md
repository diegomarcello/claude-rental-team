---
plugin: rt-executive
skill: approval-gates
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: CFO / Diretor de Compliance
---

# Approval Gates & Segregation of Duties

## Objective & Triggers
Establish financial thresholds, mandatory approvers, documentary evidence, and segregation of duties (requester cannot approve or disburse).
- **Triggers:** Invoke `rt-executive/approval-gates` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for operational invoice/payment verification (`rt-finance/accounts-payable`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Action type (acquisition, concession, disbursement, contract, settlement), amount, cost center, requester role. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Classify action type and total contract commitment (full multi-year value, not single installment) — Requester — Start.
2. Match threshold on corporate matrix and attach mandatory evidence packet — Analyst/System — Pre-approval.
3. Capture auditable approval (ERP workflow / e-signature) — Designated Approver — 24–48h SLA.
4. Execute disbursement or signing by an officer segregated from the approver — Finance/Legal — Execution.

## Rules & Criteria
Governance (COSO internal control principles): Strict segregation among (1) initiation/bidding, (2) merit approval, (3) vendor bank master setup, and (4) payment release. Splitting invoices to bypass thresholds is prohibited. Company decision: `[PENDING: Populate exact dollar/euro thresholds from Section 1]`.
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
Not applicable (governance matrix and threshold rules).

## Outputs
Standardized `approval-gates` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **CFO / Diretor de Compliance**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `approval-gates` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `approval-gates` request missing Member State or core inputs (Action type (acquisition) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **CFO / Diretor de Compliance** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
