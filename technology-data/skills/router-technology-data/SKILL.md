---
name: router-technology-data
description: "Use when a Technology Data request needs routing to the right skill: bi-reporting, information-security, systems-integration."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: technology-data
  status: draft
---

# Router Technology Data

## Routing

| Skill | Use it to |
|---|---|
| `bi-reporting` | Structure dimensional data models unifying CRM, financial ERP, and construction data for executive BI dashboards with Row-Level Security. |
| `information-security` | Establish cybersecurity controls (MFA, RBAC, encryption, 3-2-1 backups, and incident response playbooks). |
| `systems-integration` | Design and document integrations across CRM, ERP/PMS, listing portals, e-signature, banking rails, and `claude-rental-team` MCP servers. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `privacy`, `aml`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
