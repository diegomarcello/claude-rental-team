---
name: jurisdiction-lookup
description: "Use when a task depends on the law, tax or standards of a country, state or member state (Brazil, United States, Europe). (skeleton)"
license: GPL-2.0-only
metadata:
  version: 0.1.0
  category: jurisdictions
  status: skeleton
---

# Jurisdiction Lookup

> **Skeleton.** The procedures in this file are not written yet. Tell the user so. Do not improvise legal opinions, appraisals, tax positions, contracts or financial entries from it.

## Workflow

1. Identify the country and, when relevant, the state, member state and municipality.
2. Read the matching file under `references/<country>/`.
3. If a section says `TODO` or `Last verified: TODO`, say the rule is not documented here. Do not present it as verified.

## Topics

| File |
|---|
| `sales-purchase.md` |
| `leasing.md` |
| `taxes.md` |
| `valuation-standards.md` |
| `construction-permits.md` |
| `privacy.md` |
| `aml.md` |
| `brokerage-advertising-consumer.md` |

## Countries

- [Brazil](references/brazil/)
- [United States](references/united-states/), with [state template](references/united-states/states/_template.md)
- [Europe](references/europe/), with [member state template](references/europe/member-states/_template.md)

## Guardrails

TODO
