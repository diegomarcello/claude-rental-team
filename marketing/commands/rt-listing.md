---
description: "Write high-converting, accurate listing titles and descriptions for MLS/portals and brochures, ensuring mandatory statutory disclosures and zero discriminatory or prohibited phrasing."
argument-hint: "<property>"
disable-model-invocation: true
---

# /rt-listing

Input: `$ARGUMENTS`

## Skills

- `listing-copywriting`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `listing-copywriting` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
