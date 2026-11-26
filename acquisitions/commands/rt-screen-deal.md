---
description: "Screen acquisition opportunities (on-market, off-market, foreclosure/judicial auctions, distressed assets) using knock-out criteria and weighted scoring prior to full underwriting."
argument-hint: "<property or listing>"
disable-model-invocation: true
---

# /rt-screen-deal

Input: `$ARGUMENTS`

## Skills

- `opportunity-screening`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `opportunity-screening` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
