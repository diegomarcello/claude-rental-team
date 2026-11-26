---
description: "Operationalize Record of Processing Activities (ROPA), KYC/UBO onboarding files, AML risk scoring matrices, and regulatory reporting workflows (COAF/ANPD, FinCEN/FTC, EU FIUs/DPAs)."
argument-hint: "<party documents>"
disable-model-invocation: true
---

# /rt-kyc-aml

Input: `$ARGUMENTS`

## Skills

- `privacy-aml`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `privacy-aml` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
