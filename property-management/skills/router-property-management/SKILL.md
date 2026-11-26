---
name: router-property-management
description: "Use when a Property Management request needs routing to the right skill: condo-administration, lease-administration, maintenance-requests, move-inspections, tenant-screening."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: property-management
  status: draft
---

# Router Property Management

## Routing

| Skill | Use it to |
|---|---|
| `condo-administration` | Manage condominium/HOA obligations for managed properties, separate ordinary operating charges (tenant) from extraordinary capital assessments (landlord), and represent owners at assemblies via proxy. |
| `lease-administration` | Manage active lease lifecycles, compute annual rent indexation using official indices (IPCA/IGP-M in BR; CPI/AB 1482 in US; IRL/INE/HICP in EU), trigger D-90 renewal workflows, and calculate prorated termination fees. |
| `maintenance-requests` | Triage maintenance tickets by severity (Emergency, Urgent, Routine), assign cost responsibility (structural/habitability = landlord; misuse/routine consumables = tenant), and dispatch vetted vendors. |
| `move-inspections` | Conduct detailed room-by-room move-in and move-out inspections with timestamped photos, distinguishing chargeable tenant damage from normal wear and tear, and managing dispute and security deposit timelines. |
| `tenant-screening` | Evaluate rental applicants using standardized, objective numerical thresholds (income-to-rent ratio, credit score, rental history, security/guarantor), logging objective adverse reasons and dispute notices. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `leasing`, `privacy`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
