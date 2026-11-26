---
plugin: rt-marketing
skill: seo-paid-media
jurisdiction: united-states
last_verified: 2026-11-25
confidence: partial
reviewer: Especialista de Performance / Compliance
---

# Local SEO & Paid Media (Housing Ad Restrictions)

## Objective & Triggers
Manage local SEO (Google Business Profile, neighborhood landing pages) and paid acquisition (Google Ads, Meta Ads) strictly adhering to Housing Special Ad Category restrictions.
- **Triggers:** Invoke `rt-marketing/seo-paid-media` whenever a user requests execution, analysis, or templates for this workflow.

## When Not to Use
Do not use for portal listing copy (`listing-copywriting`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Core inputs: Target keywords, focus neighborhoods, media budget, landing pages, conversion tracking setup. | Yes | Structured / Text | CRM / PMS / User |
| Operating jurisdiction | Yes | Enum (`united-states` / `brazil` / `europe`) | Company Context |

## Process
1. Enable mandatory 'Housing' Special Ad Category in Meta Ads (and Google Ads personalized housing ad limits), removing age, gender, ZIP/postal code, and exclusionary demographic targeting — Media Buyer — Setup.
2. Optimize Google Business Profile and hyper-local neighborhood/property-type landing pages — SEO Specialist — Continuous.
3. Pipe offline CRM conversion events (Tour Completed, Offer, Closed Lease/Sale) back to ad platforms to optimize true CAC — Performance/Tech — Continuous.

## Rules & Criteria
Platform Policy / Law: Meta Housing Special Ad Category and Google Ads Housing Policy prohibit ZIP/postal code targeting (minimum radius required), age, gender, or discriminatory lookalike audiences in compliance with Fair Housing and anti-discrimination statutes.
- **Cross-reference:** Always check `rt-jurisdictions/united-states/` for federal and state-specific statutory rules.

## Calculations
Not applicable.

## Outputs
Standardized `seo-paid-media` deliverable in structured Markdown containing executive summary, operational checklist/table, calculations (where applicable), and approval gates.

## Human Approval Gates
- Claude **never** executes wire disbursements, binds contracts, overrides approval thresholds, or submits regulatory filings without human sign-off by **Especialista de Performance / Compliance**.

## Handoffs
- Pass structured outputs to the downstream workflow stage (see `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Common Errors & Risks
- Operating without company onboarding parameters (Section 1) and assuming unapproved fee/threshold policies.
- Overlooking state-specific statutory rules (e.g., FL vs. TX vs. CA).

## Test Cases
1. **Normal:** Standard `seo-paid-media` request with complete inputs -> Executes full workflow and outputs structured deliverable.
2. **Incomplete:** `seo-paid-media` request missing mandatory inputs (Target keywords) -> Requests missing fields before proceeding.
3. **Risk:** Request attempting to bypass **Especialista de Performance / Compliance** approval gate or statutory rule -> Blocks execution and escalates.

## Sources
- `rt-jurisdictions/united-states/` statutory reference files and US institutional real estate benchmarks — Accessed 2026-11-25.

## Pending Items
- Populate company-specific parameters from `00-company-onboarding/01-company-intake-questionnaire-en.md`.
- Mandatory sign-off by credentialed domain reviewer before promoting from `skeleton` to `verified`.
