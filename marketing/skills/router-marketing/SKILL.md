---
name: router-marketing
description: "Use when a Marketing request needs routing to the right skill: campaign-planning, lead-generation, listing-copywriting, seo-paid-media, social-media."
license: GPL-2.0-only
metadata:
  version: 0.4.0
  category: marketing
  status: draft
---

# Router Marketing

## Routing

| Skill | Use it to |
|---|---|
| `campaign-planning` | Design demand-generation and inventory-acquisition campaigns defining target personas, value proposition, channel mix (portals, Meta, Google, local OOH), budget allocation, and funnel KPIs. |
| `lead-generation` | Design web forms, click-to-WhatsApp flows, and landing pages with minimal friction fields, auditable consent timestamps (LGPD/TCPA/GDPR), and end-to-end UTM attribution. |
| `listing-copywriting` | Write high-converting, accurate listing titles and descriptions for MLS/portals and brochures, ensuring mandatory statutory disclosures and zero discriminatory or prohibited phrasing. |
| `seo-paid-media` | Manage local SEO (Google Business Profile, neighborhood landing pages) and paid acquisition (Google Ads, Meta Ads) strictly adhering to Housing Special Ad Category restrictions. |
| `social-media` | Plan editorial calendars (Reels/Shorts, educational carousels, property walkthroughs, client testimonials) while enforcing media copyright, tenant privacy in occupied homes, and likeness releases. |

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
