---
name: jurisdiction-lookup
description: "Use when a task depends on the law, tax or standards of Brazil, the United States or Europe: sales and purchase, leasing, taxes, valuation standards, construction permits, privacy, anti-money-laundering, brokerage, advertising and consumer rules."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: jurisdictions
  status: draft
---

# Jurisdiction Lookup

Country rules shared by every department.

## Workflow

1. Identify the country and, when relevant, the state, member state and municipality.
2. Read [known issues](references/known-issues.md) **first**. It overrides the topic files.
3. Read only the topic file you need.
4. Quote the rule with the source the file cites, and say its `confidence` is the author's declaration.
5. Brazil files are in Portuguese. Answer in the user's language.

## Topics

| Topic | Brazil | United States | Europe |
|---|---|---|---|
| `sales-purchase` | [brazil](references/brazil/sales-purchase.md) | [united-states](references/united-states/sales-purchase.md) | [europe](references/europe/sales-purchase.md) |
| `leasing` | [brazil](references/brazil/leasing.md) | [united-states](references/united-states/leasing.md) | [europe](references/europe/leasing.md) |
| `taxes` | [brazil](references/brazil/taxes.md) | [united-states](references/united-states/taxes.md) | [europe](references/europe/taxes.md) |
| `valuation-standards` | [brazil](references/brazil/valuation-standards.md) | [united-states](references/united-states/valuation-standards.md) | [europe](references/europe/valuation-standards.md) |
| `construction-permits` | [brazil](references/brazil/construction-permits.md) | [united-states](references/united-states/construction-permits.md) | [europe](references/europe/construction-permits.md) |
| `privacy` | [brazil](references/brazil/privacy.md) | [united-states](references/united-states/privacy.md) | [europe](references/europe/privacy.md) |
| `aml` | [brazil](references/brazil/aml.md) | [united-states](references/united-states/aml.md) | [europe](references/europe/aml.md) |
| `brokerage-advertising-consumer` | [brazil](references/brazil/brokerage-advertising-consumer.md) | [united-states](references/united-states/brokerage-advertising-consumer.md) | [europe](references/europe/brokerage-advertising-consumer.md) |

## Coverage limits

- United States: where state rules appear, check which states the file covers. For any other state say the rule is not documented, and start from the [state template](references/united-states/states/_template.md).
- Europe: the files focus on Portugal, Spain, Germany and France. For any other country say the rule is not documented, and start from the [member state template](references/europe/member-states/_template.md).

## Guardrails

Not legal or tax advice. Time-sensitive rules must be checked against the official source before use.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
