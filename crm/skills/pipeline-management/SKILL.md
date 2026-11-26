---
name: pipeline-management
description: "Use when the task is to define clear pipeline stages, objective entry/exit criteria, maximum stage aging SLAs, and loss/stagnation rules across sales, leasing, and listing-acquisition funnels. Covers Brazil, US and Europe. PT: Gestão de Funis de Venda e Locação no CRM."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: crm
  status: draft
---

# Pipeline Management

Define clear pipeline stages, objective entry/exit criteria, maximum stage aging SLAs, and loss/stagnation rules across sales, leasing, and listing-acquisition funnels.

## How to use

1. Identify the jurisdiction: Brazil, United States (and state) or Europe (and member state). Ask if it is unclear.
2. Read **only** the matching reference and follow its inputs, process, rules, approval gates and test cases:
   - [Brazil](references/brazil.md) (in Portuguese)
   - [United States](references/united-states.md)
   - [Europe](references/europe.md)
3. Check for corrections. No `known-issues.md` was recorded for this skill.
4. Read `company-context.md` in the working project if it exists (if it is missing, offer `rt-executive:company-setup`).
5. For local rules, use `rt-jurisdictions:jurisdiction-lookup`. Usual topics here: `privacy`.
6. Answer in the user's language.

## Templates

Headings only, not yet written. Fill them from the reference file.

- [Pipeline Stages](assets/pipeline-stages.md)

## Handoffs

- No end-to-end flow continues from this skill. Use `rt-crm:router-crm` if the work goes on.

## Notation used in the reference files

| In the file | Means |
|---|---|
| `rt-<plugin>/<skill>` | skill `rt-<plugin>:<skill>` |
| `rt-jurisdictions/<country>/<topic>` | topic file of the `rt-jurisdictions:jurisdiction-lookup` skill |
| `00-company-onboarding/...` | the project's `company-context.md` |
| `99-architecture-and-governance/...` | the Handoffs section below |

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
