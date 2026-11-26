---
name: router-legal
description: "Use when a Legal request needs routing to the right skill: contract-drafting-review, disputes-eviction, privacy-aml, tenancy-law, title-due-diligence."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: legal
  status: draft
---

# Router Legal

## Routing

| Skill | Use it to |
|---|---|
| `contract-drafting-review` | Draft and review purchase agreements, leases, property management agreements, brokerage mandates, and construction contracts, enforcing mandatory statutory clauses and flagging unconscionable terms. |
| `disputes-eviction` | Manage legal escalation after soft collections fail: statutory default notices, cash-for-keys / surrender agreements, eviction filings, and writ of possession enforcement. |
| `privacy-aml` | Operationalize Record of Processing Activities (ROPA), KYC/UBO onboarding files, AML risk scoring matrices, and regulatory reporting workflows (COAF/ANPD, FinCEN/FTC, EU FIUs/DPAs). |
| `tenancy-law` | Resolve day-to-day operational questions on landlord-tenant rights and duties (improvements, right of first refusal, subletting, sale of tenant-occupied property, repair allocation). |
| `title-due-diligence` | Audit chain of title, liens, mortgages, easements, seller litigation/tax warrants, HOA/property tax arrears, and zoning/occupancy permits prior to acquisition or major commercial lease. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `sales-purchase`, `leasing`, `taxes`, `valuation-standards`, `construction-permits`, `privacy`, `aml`, `brokerage-advertising-consumer`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
