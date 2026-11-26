---
description: "Simulate loan payments, interest, principal amortization, mandatory mortgage insurance (PMI / MIP-DFI), and debt-to-income (DTI) limits across French Annuity/Price (US/EU) and SAC (Brazil) systems, with mandatory non-binding disclosures."
argument-hint: "<price> <down payment> <term> <rate>"
disable-model-invocation: true
---

# /rt-financing-simulation

Input: `$ARGUMENTS`

## Skills

- `financing-simulation`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `financing-simulation` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
