---
name: router-finance
description: "Use when a Finance request needs routing to the right skill: accounts-payable, accounts-receivable, cash-flow-forecast, collections, financial-close, owner-payouts, tax-planning."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: finance
  status: draft
---

# Router Finance

## Routing

| Skill | Use it to |
|---|---|
| `accounts-payable` | Process vendor, contractor, and utility disbursements using 3-way matching (PO x Delivery/Inspection x Invoice), tax withholding calculation, and anti-fraud wire/ACH/boleto verification. |
| `accounts-receivable` | Generate rent, pass-through expense, and commission invoices, process bank settlement files (ACH/NACHA, SEPA CAMT.053, CNAB 240/400), post cash receipts, and reconcile trust/operating accounts daily. |
| `cash-flow-forecast` | Forecast operating cash inflows and outflows over a rolling 13-week horizon with minimum liquidity alerts. |
| `collections` | Execute structured past-due rent collection cadences (D+1 to D+30), applying late fees and interest within statutory caps while strictly prohibiting abusive or harassing collection tactics. |
| `financial-close` | Execute monthly accounting close by Business Day 5 covering bank/trust reconciliations and accrual revenue recognition (ASC 606 / IFRS 15). |
| `owner-payouts` | Compute net monthly owner disbursements, issue itemized owner statements, and feed annual tax reporting (1099-MISC / DIMOB). |
| `tax-planning` | Compare tax regimes across business lines and maintain statutory filing calendars. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `taxes`, `aml`, `leasing`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
