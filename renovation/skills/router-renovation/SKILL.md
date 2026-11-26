---
name: router-renovation
description: "Use when a Renovation request needs routing to the right skill: renovation-budget, scope-of-work, works-quality-inspection, works-schedule."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: renovation
  status: draft
---

# Router Renovation

## Routing

| Skill | Use it to |
|---|---|
| `renovation-budget` | Build itemized renovation budgets with takeoffs, benchmark unit costs (SINAPI/TCPO/RSMeans), overhead/profit (BDI), contingency reserves, and budget-vs-actual variance tracking. |
| `scope-of-work` | Translate inspection findings and commercial strategy (rent-ready turn vs. high-end flip) into a trade-by-trade Scope of Work detailing materials, exclusions, and acceptance criteria. |
| `works-quality-inspection` | Verify finished renovation quality against performance standards, run functional tests (flood/waterproofing, electrical load, floor slope), and issue Substantial/Final Completion sign-off. |
| `works-schedule` | Sequence construction trades with technical dependencies, identify critical-path bottlenecks (windows, custom millwork, inspections), and tie progress draws to verified physical milestones. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `construction-permits`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
