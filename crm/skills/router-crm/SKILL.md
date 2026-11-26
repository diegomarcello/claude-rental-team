---
name: router-crm
description: "Use when a CRM request needs routing to the right skill: crm-data-hygiene, customer-segmentation, journey-automation, pipeline-management."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: crm
  status: draft
---

# Router CRM

## Routing

| Skill | Use it to |
|---|---|
| `crm-data-hygiene` | Maintain CRM database integrity through input validation rules, contact/property deduplication, and scheduled archiving/anonymization per statutory retention limits. |
| `customer-segmentation` | Segment buyers, tenants, and landlords by behavioral intent, portfolio size, and investment profile without using protected or discriminatory attributes. |
| `journey-automation` | Configure automated CRM workflows for landlord/tenant onboarding, lease renewal alerts, contract anniversaries, and reactivation, enforcing consent gates and exit triggers. |
| `pipeline-management` | Define clear pipeline stages, objective entry/exit criteria, maximum stage aging SLAs, and loss/stagnation rules across sales, leasing, and listing-acquisition funnels. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `privacy`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
