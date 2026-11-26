---
name: router-post-sales
description: "Use when a Post Sales request needs routing to the right skill: complaint-resolution, customer-retention, property-handover, warranty-claims."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: post-sales
  status: draft
---

# Router Post Sales

## Routing

| Skill | Use it to |
|---|---|
| `complaint-resolution` | Resolve formal complaints from buyers, tenants, and landlords under strict SLAs, structured escalation tiers, and proactive resolution prior to regulatory filings. |
| `customer-retention` | Measure NPS/CSAT at key lifecycle milestones, trigger proactive detractor recovery, and drive compliant landlord/buyer referrals. |
| `property-handover` | Formalize physical handover of sold or renovated properties via Key Handover Certificate, delivery of manuals/warranties/as-built plans, and utility/property-tax account transfers. |
| `warranty-claims` | Triage post-handover defect claims distinguishing statutory/contractual builder warranties from owner lack of maintenance, enforcing cure obligations within statutory limitation periods. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `sales-purchase`, `brokerage-advertising-consumer`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
