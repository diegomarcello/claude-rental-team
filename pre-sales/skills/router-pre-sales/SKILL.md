---
name: router-pre-sales
description: "Use when a Pre Sales request needs routing to the right skill: follow-up-cadence, lead-qualification, visit-scheduling."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: pre-sales
  status: draft
---

# Router Pre Sales

## Routing

| Skill | Use it to |
|---|---|
| `follow-up-cadence` | Define structured multi-channel outreach sequences (phone, SMS/WhatsApp, email) for new and post-tour leads while enforcing quiet hours, frequency caps, and instant opt-out. |
| `lead-qualification` | Qualify buying and leasing leads using objective criteria (budget, move timeline, purpose, financing/guarantee readiness), scoring priority without discriminatory inquiries. |
| `visit-scheduling` | Coordinate in-person and virtual property tours, secure occupant access notice, send automated reminders, and enforce agent physical safety and tour check-in protocols. |

## Steps

1. Identify the intent. If two skills fit, ask one question naming both and recommend one.
2. Confirm the active jurisdiction (`brazil`, `united-states`, `europe`).
3. Check `company-context.md` in the working project.
4. Load with `rt-jurisdictions:jurisdiction-lookup`: `brokerage-advertising-consumer`, `privacy`.
5. Run the chosen skill. Confirm with the user before chaining a second one.

## Guardrails

- Never approve, sign, pay, send a regulatory filing or send a legal notice. Prepare the work and name the human who must approve it.
- `confidence` and `last_verified` are declared by the content author. Say so when the answer depends on a legal, tax or valuation rule, and ask for review by the `reviewer` named in the reference file.
- Mark every missing company parameter as pending. Do not assume thresholds, fees or policies.
- In `company-context.md`, text in `[brackets]` or marked `ex.:` or `pendente` is a placeholder or an example, never a company decision. The approval limits and the collections ladder are company rules only when the `Setup status` table of that file marks `approval-limits` or `collections-ladder` as `confirmed`. Otherwise treat them as examples, even without brackets, and ask the user to confirm or replace them before relying on them.
