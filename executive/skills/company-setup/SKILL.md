---
name: company-setup
description: "Use right after installing the rental team plugins, or when company setup is incomplete: asks the user for the company context, confirms approval limits, defines the collections ladder and completes the missing leasing templates. PT: Configuração inicial da empresa, alçadas, régua de cobrança e templates."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: executive
  status: draft
---

# Company Setup

Collect the company decisions that the other skills depend on, and record who confirmed each one.

## Before asking

1. Look for `company-context.md` in the working project. Never overwrite an existing one.
2. If it is missing, ask the user's language and create it from [the questionnaire](../router-executive/assets/company-context.md) or the [Portuguese version](../router-executive/assets/company-context.pt-BR.md).
3. If it has no `Setup status` section, append [the status table](assets/setup-status.md). Content that was already in the file stays unconfirmed until the user confirms it.
4. If the project is a git repository and `.gitignore` does not cover `/company-context.md` and `/private/`, say so and offer to add both.
5. Tell the user which items are not `confirmed` or `not-applicable`, and ask only about those.

## Questions

Ask one block per message, in this order. Use a question tool when the answer is a choice. The user may answer "later" to anything: keep it `pending` and go on.

### 1. `company-context`

Ask for the empty or placeholder fields: identification, countries and cities, business lines, responsible people (roles), fees and commissions, guarantees, deadlines, data protection and systems. Text in `[brackets]` or marked `ex.:` or `pendente` is not an answer.

### 2. `approval-limits`

Warn the user that values in the approval table may be examples even when they have no brackets. Show every row and ask, for each one, whether to confirm, change or remove it: operation, limit, requester, approver and evidence. Ask which operations are missing. Silence or "looks fine" about part of the table does not confirm the rest.

### 3. `collections-ladder`

Follow [the ladder proposals](references/collections-ladder-options.md).

### 4. Leasing templates

These were delivered as headings only:

| Template | Used by |
|---|---|
| `collection-notice` | `rt-finance:collections` |
| `receivables-aging` | `rt-finance:accounts-receivable` |
| `lease-summary` | `rt-property-management:lease-administration` |
| `move-inspection-record` | `rt-property-management:move-inspections` |
| `tenant-application` | `rt-property-management:tenant-screening` |

For each, ask which applies:

1. **The company has a model:** ask for the path of an anonymized copy (no names, tax numbers or bank data) and copy it to `company-templates/<template>.<country>.md` in the working project.
2. **Draft one now:** use the skill named above, which holds the reference. If its plugin is not installed, ask the user to install it. Save the draft to the same path and show it for review.
3. **Later:** keep `pending`.
4. **Not needed:** mark `not-applicable` and write why.

`<country>` is `brazil`, `united-states` or `europe`. Never write inside a plugin folder: updates replace it.

## Record

After each block, show what will be written and ask for confirmation. Then update `company-context.md` and its `Setup status` row with the name or role of who confirmed and the date. Finish by listing the pending items and what stays limited because of them.

## Guardrails

- Never invent a company value, and never mark an item `confirmed` without an explicit answer from the user.
- Do not send `company-context.md` or company templates to any external service.
- Notices, contracts and eviction steps need review by a lawyer before use, even after the company confirms the template.
