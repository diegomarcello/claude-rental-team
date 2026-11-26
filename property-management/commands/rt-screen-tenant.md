---
description: "Evaluate rental applicants using standardized, objective numerical thresholds (income-to-rent ratio, credit score, rental history, security/guarantor), logging objective adverse reasons and dispute notices."
argument-hint: "<application>"
disable-model-invocation: true
---

# /rt-screen-tenant

Input: `$ARGUMENTS`

## Skills

- `tenant-screening`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `tenant-screening` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
