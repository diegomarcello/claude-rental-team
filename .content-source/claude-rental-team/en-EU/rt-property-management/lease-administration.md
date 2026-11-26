---
plugin: rt-property-management
skill: lease-administration
jurisdiction: europe
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Administração de Carteira
---

# Lease Administration, Annual Rent Indexation & Renewals

## Objective & Triggers
Manage active lease lifecycles, compute annual rent indexation using official indices (IPCA/IGP-M in BR; CPI/AB 1482 in US; IRL/INE/HICP in EU), trigger D-90 renewal workflows, and calculate prorated termination fees.
- **Triggers:** Invoke `rt-property-management/lease-administration` whenever a user requests execution, analysis, or templates for this European workflow.

## When Not to Use
Do not use for past-due rent collections (`rt-finance/collections`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Current rent, anniversary date, contractual index, 12-month index variation, statutory rent cap, lease expiration date. | Yes | Structured / Text | CRM / PMS / User |
| Target EU Member State | Yes | Enum (`PT` / `ES` / `DE` / `FR` / other) | Company Context |

## Process
1. Trigger D-90 expiration alert to align renewal terms with landlord — Portfolio Analyst — D-90.
2. Pull trailing 12-month official index rate at anniversary and enforce statutory caps — Analyst — D-30.
3. Deliver statutory rent-increase notice / renewal addendum within legal notice window — Analyst — D-30.
4. Update ERP billing schedule — Finance — D-15.

## Rules & Criteria
Statutory: Annual minimum indexation in BR (Lei 10.192/2001); 1-yr IRL claim limit in FR (Loi 1989 art. 17-1); 30/90-day notice rules in CA (Cal. Civ. Code § 827).
- **Cross-reference:** Always check `rt-jurisdictions/europe/` for EU Directives (GDPR, AMLR, EPBD, MCD) and national Member State rules (PT, ES, DE, FR).

## Calculations
**Annual Indexation Formula:** $\text{New Rent} = \text{Current Rent} \times (1 + I_{12m})$. Example: $3,500.00 \times 1.0462 = \mathbf{3,661.70}$.

## Outputs
Standardized `lease-administration` deliverable in structured Markdown tailored for European operations, containing executive summary, compliance checklist, calculations, and approval gates.

## Human Approval Gates
- Claude **never** executes SEPA/wire disbursements, binds notarial/preliminary contracts, overrides approval thresholds, or files regulatory notices without human sign-off by **Coordenador de Administração de Carteira**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Applying generic EU-level assumptions without checking national Member State rules (e.g., Loi Hoguet in FR, Bestellerprinzip/GwG in DE, LAU in ES, NRAU/AMI in PT).
- Operating without company onboarding parameters (Section 1).

## Test Cases
1. **Normal:** Standard `lease-administration` request in PT/ES/DE/FR with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `lease-administration` request missing Member State or core inputs (Current rent) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Coordenador de Administração de Carteira** approval gate or EU/national statutory mandate -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/europe/` statutory reference files and European institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific European parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed European domain reviewer before promoting from `skeleton` to `verified`.
