---
name: router-executive
description: "Use when a Executive request needs routing to the right skill: approval-gates, company-kpis, company-setup, strategic-planning."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: executive
  status: draft
---

# Router Executive

## Routing

| Skill | Use it to |
|---|---|
| `approval-gates` | Establish financial thresholds, mandatory approvers, documentary evidence, and segregation of duties (requester cannot approve or disburse). |
| `company-kpis` | Define, compute, and audit core real estate KPIs across sales, leasing, renovation, and cash management with standardized formulas, benchmarks, and cadence. |
| `company-setup` | Ask for the company context, approval limits, collections ladder and missing leasing templates. |
| `strategic-planning` | Structure annual/quarterly OKR planning cycles, capital allocation across property management, brokerage, and fix-and-flip/development, and geographic expansion criteria. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `sales-purchase`, `leasing`, `taxes`, `valuation-standards`, `construction-permits`, `privacy`, `aml`, `brokerage-advertising-consumer`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Company context

If the project has no `company-context.md`, or its setup items are pending, offer `rt-executive:company-setup`. It creates the file from [the questionnaire](assets/company-context.md) ([Portuguese version](assets/company-context.pt-BR.md)). Without it, mark company decisions as pending.

## Cross-department requests

Name the owning department for each step and call its router. The six flows are in the repository folder `orchestration/workflows/`.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
