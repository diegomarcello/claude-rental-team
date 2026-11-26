---
description: "Build itemized renovation budgets with takeoffs, benchmark unit costs (SINAPI/TCPO/RSMeans), overhead/profit (BDI), contingency reserves, and budget-vs-actual variance tracking."
argument-hint: "<scope or quantities>"
disable-model-invocation: true
---

# /rt-renovation-budget

Input: `$ARGUMENTS`

## Skills

- `renovation-budget`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `renovation-budget` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
