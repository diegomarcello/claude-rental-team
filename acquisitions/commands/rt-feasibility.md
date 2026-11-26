---
description: "Model full acquisition cash flows including entry closing costs, carrying costs, CapEx/renovation, exit selling costs, taxes, and return metrics (Net Margin, ROI, IRR, NPV) across base, upside, and downside scenarios."
argument-hint: "<deal data>"
disable-model-invocation: true
---

# /rt-feasibility

Input: `$ARGUMENTS`

## Skills

- `deal-feasibility`

## Steps

1. Parse the input. Ask for the jurisdiction and any mandatory input in the reference file that is missing.
2. Run the `deal-feasibility` skill with the reference for that jurisdiction and any `known-issues.md`.
3. Do not guess values, rates or thresholds.

## Report format

Summary first, then the checklist or table, the calculations with their inputs, and the pending items.

## Approval required

Name the reviewer from the reference file. Nothing is signed, paid, filed or sent by this command.
