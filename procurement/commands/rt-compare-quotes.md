---
description: "Level competing contractor and vendor bids by normalizing scope exclusions, missing line items, lead times, and payment terms."
argument-hint: "<quote files>"
disable-model-invocation: true
---

# /rt-compare-quotes

Input: `$ARGUMENTS`

## Skills

- `quote-comparison`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `quote-comparison` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
