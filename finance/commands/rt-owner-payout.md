---
description: "Compute net monthly owner disbursements, issue itemized owner statements, and feed annual tax reporting (1099-MISC / DIMOB)."
argument-hint: "<owner> <period>"
disable-model-invocation: true
---

# /rt-owner-payout

Input: `$ARGUMENTS`

## Skills

- `owner-payouts`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `owner-payouts` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
