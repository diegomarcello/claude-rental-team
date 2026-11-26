---
description: "Orchestrate every post-acceptance milestone through escrow/notary closing, funding, and title recording, tracking statutory deadlines and owners."
argument-hint: "<deal>"
disable-model-invocation: true
---

# /rt-closing-checklist

Input: `$ARGUMENTS`

## Skills

- `closing-checklist`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `closing-checklist` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
