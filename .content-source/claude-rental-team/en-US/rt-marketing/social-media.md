---
plugin: rt-marketing
skill: social-media
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Analista de Social Media / Jurídico
---

# Social Media Content & Image/Likeness Rights

## Objective & Triggers
Plan editorial calendars (Reels/Shorts, educational carousels, property walkthroughs, client testimonials) while enforcing media copyright, tenant privacy in occupied homes, and likeness releases.
- **Triggers:** Invoke `rt-marketing/social-media` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for paid performance media buying (`seo-paid-media`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Authorized property portfolio, brand content pillars, filming/likeness release forms. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Confirm owner filming consent (and tenant notice/consent if occupied) prior to shooting interior video — Leasing/Marketing — Pre-shoot.
2. Blur license plates, personal documents, family photos, and sensitive security codes — Video Editor — Post-production.
3. Obtain signed Likeness Release from featured clients/agents and display brokerage license ID — Marketing — Pre-post.

## Rules & Criteria
Statutory: Right of publicity and privacy (GDPR/LGPD for identifiable individuals; US state publicity rights; commercial music licensing rules for business accounts).
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `social-media` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Analista de Social Media / Jurídico**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `social-media` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `social-media` request missing mandatory inputs (Authorized property portfolio) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Analista de Social Media / Jurídico** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
