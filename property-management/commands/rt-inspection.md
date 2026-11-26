---
description: "Conduct detailed room-by-room move-in and move-out inspections with timestamped photos, distinguishing chargeable tenant damage from normal wear and tear, and managing dispute and security deposit timelines."
argument-hint: "<property> <move-in or move-out>"
disable-model-invocation: true
---

# /rt-inspection

Input: `$ARGUMENTS`

## Skills

- `move-inspections`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `move-inspections` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
