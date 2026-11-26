---
plugin: rt-technology-data
skill: information-security
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: CISO / DPO
---

# Information Security, Access Control, Backup & Incident Response

## Objective & Triggers
Establish cybersecurity controls (MFA, RBAC, encryption, 3-2-1 backups, and incident response playbooks).
- **Triggers:** Invoke `rt-technology-data/information-security` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for regulatory legal filings without technical containment (`rt-jurisdictions/*/privacy`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Critical systems inventory, RBAC role matrix, backup schedule, CSIRT contacts. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Enforce MFA across 100% of accounts and audit permissions quarterly — IT/InfoSec — Continuous.
2. Enforce AES-256 / TLS 1.3 encryption and 3-2-1 backups — Infrastructure — Continuous.
3. Upon incident: Contain (< 1h) -> Preserve logs -> Notify DPO/Legal to meet statutory deadlines (72h GDPR / 3 business days ANPD / 30d FTC) — CSIRT/DPO — Immediate.

## Rules & Criteria
Standards / Statutory: FTC Safeguards Rule (16 CFR Part 314), GDPR Art. 32, LGPD Art. 46, NIST CSF / ISO 27001.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
**3-2-1** Rule: 3 copies, 2 distinct media types, 1 off-site/immutable copy. RPO <= 24h; RTO <= 4h.

## Outputs
Standardized `information-security` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **CISO / DPO**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `information-security` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `information-security` request missing mandatory inputs (Critical systems inventory) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **CISO / DPO** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
