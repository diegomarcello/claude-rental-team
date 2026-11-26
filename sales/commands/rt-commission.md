---
description: "Calculate gross brokerage commission, tax/franchise deductions, splits across listing agent, buyer/leasing agent, management, and co-brokers, and verify payout triggers."
argument-hint: "<price> <rate> <split>"
disable-model-invocation: true
---

# /rt-commission

Input: `$ARGUMENTS`

## Skills

- `commission-calculation`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `commission-calculation` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
