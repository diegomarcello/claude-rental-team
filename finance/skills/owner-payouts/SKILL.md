---
name: owner-payouts
description: "Use when the task is to compute net monthly owner disbursements, issue itemized owner statements, and feed annual tax reporting (1099-MISC / DIMOB). Covers Brazil, US and Europe. PT: Prestação de Contas e Repasse Mensal aos Proprietários."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: finance
  status: draft
---

# Owner Payouts

Compute net monthly owner disbursements, issue itemized owner statements, and feed annual tax reporting (1099-MISC / DIMOB).

## How to use

1. Identify the jurisdiction: Brazil, United States (and state) or Europe (and member state). Ask if it is unclear.
2. Read **only** the matching reference and follow its inputs, process, rules, approval gates and test cases:
   - [Brazil](references/brazil.md) (in Portuguese)
   - [United States](references/united-states.md)
   - [Europe](references/europe.md)
3. Check for corrections. Then read [known issues](references/known-issues.md): it overrides the reference.
4. Read `company-context.md` in the working project if it exists (if it is missing, offer `rt-executive:company-setup`).
5. For local rules, use `rt-jurisdictions:jurisdiction-lookup`. Usual topics here: `taxes`, `aml`, `leasing`.
6. Answer in the user's language.

## Brazil: pilot reference

- Status: draft. The new reference has no `confidence`, `last_verified` or `reviewer` field, and nobody has signed a review.
- Human approval: **Coordenador Financeiro / Contador**. Stop and ask before any signature, payment, notice or exception to policy.
- In the reference, `calculations/<name>.md` is `references/calculation-spec-brazil.md` of that skill, and `templates/brazil/.../<name>.md` is `assets/<name>.brazil.md` of that skill.

## Templates

### Brazil

Unreviewed drafts. Fill every `{{field}}` from the source named in the template's field table, and never invent a value.

- [Owner Statement](assets/owner-statement.brazil.md)

### Other countries

Headings only, not yet written.

- [Owner Statement](assets/owner-statement.md)

## Calculations

**Brazil:** run the script instead of computing by hand, and show its `avisos` to the user. Inputs and rules: [calculation spec](references/calculation-spec-brazil.md).

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/skills/owner-payouts/scripts/owner_payout.py --aluguel-recebido 5000.00 --taxa-adm-pct 10 --reparos-autorizados 350.00
```

The values above are examples: use the user's data. Run with `--help` for all options.

**Other countries:** no script exists. Compute with the formulas in the reference file and show every input and step.

## Handoffs

- `lease-lifecycle` flow: continue with `rt-property-management:lease-administration`

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
