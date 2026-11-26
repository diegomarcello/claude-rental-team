---
description: "Manage legal escalation after soft collections fail: statutory default notices, cash-for-keys / surrender agreements, eviction filings, and writ of possession enforcement."
argument-hint: "<case facts>"
disable-model-invocation: true
---

# /rt-eviction

Input: `$ARGUMENTS`

## Skills

- `disputes-eviction`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `disputes-eviction` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
