---
name: router-sales
description: "Use when a Sales request needs routing to the right skill: closing-checklist, commission-calculation, financing-simulation, proposal-negotiation."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: sales
  status: draft
---

# Router Sales

## Routing

| Skill | Use it to |
|---|---|
| `closing-checklist` | Orchestrate every post-acceptance milestone through escrow/notary closing, funding, and title recording, tracking statutory deadlines and owners. |
| `commission-calculation` | Calculate gross brokerage commission, tax/franchise deductions, splits across listing agent, buyer/leasing agent, management, and co-brokers, and verify payout triggers. |
| `financing-simulation` | Simulate loan payments, interest, principal amortization, mandatory mortgage insurance (PMI / MIP-DFI), and debt-to-income (DTI) limits across French Annuity/Price (US/EU) and SAC (Brazil) systems, with mandatory non-binding disclosures. |
| `proposal-negotiation` | Manage receipt, formalization, and negotiation of purchase and lease offers, presenting all offers objectively to the seller/landlord, handling objections, and enforcing concession gates. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `sales-purchase`, `brokerage-advertising-consumer`, `taxes`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
