---
description: "Value commercial, multifamily, and rental portfolios via Direct Capitalization of Net Operating Income (NOI) or Discounted Cash Flow (DCF)."
argument-hint: "<property> <income and expenses>"
disable-model-invocation: true
---

# /rt-appraise-income

Input: `$ARGUMENTS`

## Skills

- `income-capitalization`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `income-capitalization` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
