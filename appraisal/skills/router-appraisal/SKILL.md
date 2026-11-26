---
name: router-appraisal
description: "Use when a Appraisal request needs routing to the right skill: comparative-market-analysis, cost-approach, income-capitalization, technical-inspection."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: appraisal
  status: draft
---

# Router Appraisal

## Routing

| Skill | Use it to |
|---|---|
| `comparative-market-analysis` | Estimate market sale or rental value via the Sales Comparison Approach using sample cleansing, attribute adjustment factors/regression, and statistical confidence intervals. |
| `cost-approach` | Estimate value of special-purpose buildings, warehouses, new construction, or insurable value by adding land value to depreciated replacement/reproduction cost of improvements. |
| `income-capitalization` | Value commercial, multifamily, and rental portfolios via Direct Capitalization of Net Operating Income (NOI) or Discounted Cash Flow (DCF). |
| `technical-inspection` | Perform pre-acquisition or pre-handover physical inspection covering structure, roof, waterproofing, electrical, plumbing, and HVAC, classifying severity and specialist escalation triggers. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `valuation-standards`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
