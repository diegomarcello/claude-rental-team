---
description: "Qualify buying and leasing leads using objective criteria (budget, move timeline, purpose, financing/guarantee readiness), scoring priority without discriminatory inquiries."
argument-hint: "<lead notes>"
disable-model-invocation: true
---

# /rt-qualify-lead

Input: `$ARGUMENTS`

## Skills

- `lead-qualification`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `lead-qualification` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
