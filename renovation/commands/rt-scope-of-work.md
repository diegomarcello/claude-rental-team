---
description: "Translate inspection findings and commercial strategy (rent-ready turn vs. high-end flip) into a trade-by-trade Scope of Work detailing materials, exclusions, and acceptance criteria."
argument-hint: "<property> <objective>"
disable-model-invocation: true
---

# /rt-scope-of-work

Input: `$ARGUMENTS`

## Skills

- `scope-of-work`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `scope-of-work` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
