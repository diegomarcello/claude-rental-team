---
name: router-acquisitions
description: "Use when a Acquisitions request needs routing to the right skill: deal-feasibility, opportunity-screening, purchase-negotiation."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: acquisitions
  status: draft
---

# Router Acquisitions

## Routing

| Skill | Use it to |
|---|---|
| `deal-feasibility` | Model full acquisition cash flows including entry closing costs, carrying costs, CapEx/renovation, exit selling costs, taxes, and return metrics (Net Margin, ROI, IRR, NPV) across base, upside, and downside scenarios. |
| `opportunity-screening` | Screen acquisition opportunities (on-market, off-market, foreclosure/judicial auctions, distressed assets) using knock-out criteria and weighted scoring prior to full underwriting. |
| `purchase-negotiation` | Structure purchase offers, negotiation anchors, protected earnest money deposits governed by conditions precedent (due diligence, financing, vacant possession), and penalty-free walk-away triggers. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `sales-purchase`, `taxes`, `valuation-standards`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
