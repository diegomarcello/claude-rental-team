---
name: lease-administration
description: "Use when the task is to manage active lease lifecycles, compute annual rent indexation using official indices (IPCA/IGP-M in BR; CPI/AB 1482 in US; IRL/INE/HICP in EU), trigger D-90 renewal workflows, and calculate prorated termination fees. Covers Brazil, US and Europe. PT: Administração de Contratos, Reajuste Anual e Renovações."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: property-management
  status: draft
---

# Lease Administration

Manage active lease lifecycles, compute annual rent indexation using official indices (IPCA/IGP-M in BR; CPI/AB 1482 in US; IRL/INE/HICP in EU), trigger D-90 renewal workflows, and calculate prorated termination fees.

## How to use

1. Identify the jurisdiction: Brazil, United States (and state) or Europe (and member state). Ask if it is unclear.
2. Read **only** the matching reference and follow its inputs, process, rules, approval gates and test cases:
   - [Brazil](references/brazil.md) (in Portuguese)
   - [United States](references/united-states.md)
   - [Europe](references/europe.md)
3. Check for corrections. Then read [known issues](references/known-issues.md): it overrides the reference.
4. Read `company-context.md` in the working project if it exists (if it is missing, offer `rt-executive:company-setup`).
5. For local rules, use `rt-jurisdictions:jurisdiction-lookup`. Usual topics here: `leasing`, `privacy`.
6. Answer in the user's language.

## Brazil: pilot reference

- Status: draft. The new reference has no `confidence`, `last_verified` or `reviewer` field, and nobody has signed a review.
- Human approval: **Coordenador de Administração de Carteira**. Stop and ask before any signature, payment, notice or exception to policy.
- In the reference, `calculations/<name>.md` is `references/calculation-spec-brazil.md` of that skill, and `templates/brazil/.../<name>.md` is `assets/<name>.brazil.md` of that skill.

## Setup questions (ask on first use)

Before producing the deliverable, check every item below and ask each question that applies to the current task. Ask before producing it; if you cannot wait for an answer, deliver a draft marked pending and end the reply with all open questions, numbered. Drop none. The user may answer "later": continue, and mark the item pending in the output.

1. `company-context.md` is missing, or `company-context` is not `confirmed` in its `Setup status` table: ask for the company values this task depends on. If the file is missing, offer `rt-executive:company-setup`.
2. The task needs an approval and `approval-limits` is not `confirmed`: ask who approves and up to what value. Do not use the unconfirmed table.
3. The task needs the `lease-summary` template: use `company-templates/lease-summary.<country>.md` from the working project (`brazil`, `united-states` or `europe`). If it does not exist, ask whether the user (a) has a company model, and give the path of an anonymized copy; (b) wants a draft written now from the reference file, for review; or (c) prefers to do it later, with the gaps marked pending. Save (a) or (b) to that path, never inside the plugin folder. Mark `template:lease-summary` as `confirmed` only when the user approves the text.

## Templates

### Brazil

Unreviewed drafts. Fill every `{{field}}` from the source named in the template's field table, and never invent a value.

- [Rent Adjustment Notice](assets/rent-adjustment-notice.brazil.md)

### Not yet written

Headings only, not yet written, for every country. Use it only through the `lease-summary` setup question.

- [Lease Summary](assets/lease-summary.md)

## Calculations

**Brazil:** run the script instead of computing by hand, and show its `avisos` to the user. Inputs and rules: [calculation spec](references/calculation-spec-brazil.md).

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/lease-administration/scripts/lease_administration.py reajuste --aluguel-atual 3500.00 --indice IPCA --variacao-pct 4.62
```

The values above are examples: use the user's data. Run with `--help` for all options.

**Other countries:** no script exists. Compute with the formulas in the reference file and show every input and step.

## Handoffs

- No end-to-end flow continues from this skill. Use `rt-property-management:router-property-management` if the work goes on.

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
