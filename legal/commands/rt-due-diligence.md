---
description: "Audit chain of title, liens, mortgages, easements, seller litigation/tax warrants, HOA/property tax arrears, and zoning/occupancy permits prior to acquisition or major commercial lease."
argument-hint: "<property documents>"
disable-model-invocation: true
---

# /rt-due-diligence

Input: `$ARGUMENTS`

## Skills

- `title-due-diligence`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `title-due-diligence` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
