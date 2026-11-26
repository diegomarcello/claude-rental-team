---
description: "Forecast operating cash inflows and outflows over a rolling 13-week horizon with minimum liquidity alerts."
argument-hint: "<balances and entries>"
disable-model-invocation: true
---

# /rt-cash-flow

Input: `$ARGUMENTS`

## Skills

- `cash-flow-forecast`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `cash-flow-forecast` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
