# Content Review

State of the content integrated in v0.2.0 (2026-11-26). Reference files were copied unchanged from `.content-source/`.

## Fix before use

| Area | Problem | Detail |
|---|---|---|
| US anti-money-laundering | FinCEN residential real estate rule presented as in force; it was vacated on 2026-03-19, appeal pending | [known issues](jurisdictions/skills/jurisdiction-lookup/references/known-issues.md) |
| US privacy | TCPA one-to-one consent presented as required; vacated on 2025-01-24 | same file |
| US leasing | Relies on HUD notice FHEO-2020-01, since withdrawn | same file |
| US and Europe jurisdictions | `Process` section empty in all 16 files | same file |
| Brazil financing | Price example shows 3,394.54; for 0.80% a month the correct value is 3,392.64 | [known issues](sales/skills/financing-simulation/references/known-issues.md) |
| Europe skills | Several numeric examples are the US ones; accounts payable cites US withholding | `references/known-issues.md` of each skill |

## Weak points

- All 24 jurisdiction files declare `confidence: verified`. Only the items above were checked; the rest was not.
- In the 177 department references, the `Outputs`, `Handoffs`, `Sources`, `Pending Items` and common-error text is largely generic and repeated. Sources point to internal folders, not to official publications.
- References mention `05-fluxos-operacionais.md`, which does not exist. Handoffs in each `SKILL.md` replace it.
- English references name reviewers in Portuguese.
- The content README says 55 department files per language; there are 59.

## Not provided by the content

- Template text: Brazil drafts exist for part of the [inventory](templates/business-template-inventory.md); the rest, and all US and Europe templates, are missing
- Agent definitions: names only. Roles here were derived from each skill's objective.
- Calculation scripts for 9 skills in Brazil and for every skill in the US and Europe
- Workflow owners, deadlines and failure paths
- Completed company questionnaire

## Delivery 02: Brazil leasing pilot (v0.3.0)

Integrated: 7 references, 4 calculation specs with scripts and tests, 19 templates.

### Not applied

| Delivered file | Why |
|---|---|
| `reviews/brazil/jurisdictions--leasing.review.md` | Describes text that is not in `leasing.md`, which already states the rules correctly. Its correction adds a false exception: assignment of investment fund quotas is the fourth guarantee type in art. 37, not an exception to the one-guarantee rule. |
| `reviews/brazil/jurisdictions--privacy.review.md` | Says the file relies only on consent; it already cites art. 7, V and X. |
| `reviews/brazil/jurisdictions--taxes.review.md` | Says the administration fee deduction and the DIMOB deadline are missing; both are there. Its art. 687 citation is unconfirmed. |
| `reviews/brazil/jurisdictions--aml.review.md` | Only confirms the open COFECI question, already recorded. |
| `reviews/*/PROCESS-STANDARD.md` | One generic process for 16 topics. The empty sections still need topic-specific text. |

No review has a registration number (placeholders only). None counts as a professional sign-off.

### Fix in the next delivery

- Financing spec: test values are wrong for 10% a year.
- References: wrong plugin names in `owner-payouts`, `accounts-receivable`, `collections`, `tenant-screening` and `move-inspections`.
- Citations: art. 22 in `owner-payouts` and `move-inspections`; RIR/2018 art. 687.
- References changed format: `Quando não usar`, `Cálculos` and `Aprovação humana` are gone, as are `confidence`, `last_verified` and `reviewer`.
- Conflicts: three delinquency ladders; cash reporting threshold of R$ 50,000 in the company context against R$ 100,000 in `aml.md`.
- Missing for the pilot: templates for collection notice, lease summary, move inspection record, tenant application form and receivables aging (headings only).
- `cost-approach-report`: broken formula.

Details: `references/known-issues.md` of each skill.

Since v0.4.0, `company-setup` and the leasing skills ask each company for the collections ladder and the five missing templates. This does not resolve the conflicts in the delivery or replace professional review.
