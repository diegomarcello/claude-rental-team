---
description: "Manage active lease lifecycles, compute annual rent indexation using official indices (IPCA/IGP-M in BR; CPI/AB 1482 in US; IRL/INE/HICP in EU), trigger D-90 renewal workflows, and calculate prorated termination fees."
argument-hint: "<lease data>"
disable-model-invocation: true
---

# /rt-rent-adjustment

Input: `$ARGUMENTS`

## Skills

- `lease-administration`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `lease-administration` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
