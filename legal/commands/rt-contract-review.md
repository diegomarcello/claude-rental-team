---
description: "Draft and review purchase agreements, leases, property management agreements, brokerage mandates, and construction contracts, enforcing mandatory statutory clauses and flagging unconscionable terms."
argument-hint: "<contract file>"
disable-model-invocation: true
---

# /rt-contract-review

Input: `$ARGUMENTS`

## Skills

- `contract-drafting-review`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `contract-drafting-review` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
