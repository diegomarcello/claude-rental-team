---
description: "Estimate market sale or rental value via the Sales Comparison Approach using sample cleansing, attribute adjustment factors/regression, and statistical confidence intervals."
argument-hint: "<property> <comparables>"
disable-model-invocation: true
---

# /rt-appraise-cma

Input: `$ARGUMENTS`

## Skills

- `comparative-market-analysis`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `comparative-market-analysis` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
