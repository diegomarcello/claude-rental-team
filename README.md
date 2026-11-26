# claude-rental-team

Rental company team for Brazil, the US and Europe designed for Claude.

Agents, skills, commands and templates to run a real estate company: buying, appraisal, sales, renovation and property management, plus the supporting departments.

> **Status: draft (v0.4.0).** Skills carry reference content for Brazil, the United States and Europe, pending professional review. A Brazil leasing pilot adds draft templates and four calculation scripts (`python3 -m unittest discover -s tests`); everything else in the templates is headings only. Read [CONTENT-REVIEW.md](CONTENT-REVIEW.md) before use. Nothing here is legal, tax or valuation advice.

## First use

After installing, run `/rt-executive:company-setup` in your company project. It asks for the company context, approval limits, collections ladder and missing leasing templates. See [Installation](INSTALLATION.md).

## Departments

16 plugins, 42 agents, 76 skills, 21 commands.

| Folder | Scope | Agents | Skills | Commands |
|---|---|---|---|---|
| [acquisitions](acquisitions/) | Property sourcing, opportunity screening, feasibility and purchase negotiation. | 3 | 4 | 2 |
| [appraisal](appraisal/) | Market, income and cost valuation, and technical property inspection. | 4 | 5 | 2 |
| [crm](crm/) | Pipeline, segmentation, data quality and automated customer journeys. | 2 | 5 | 0 |
| [executive](executive/) | Company setup, direction, KPIs, approval authority and cross-department routing. | 3 | 5 | 0 |
| [finance](finance/) | Payables, receivables, collections, cash, owner payouts, close and taxes. | 4 | 8 | 2 |
| [human-resources](human-resources/) | Recruiting, onboarding, performance and compensation. | 1 | 4 | 0 |
| [legal](legal/) | Title due diligence, contracts, tenancy law, disputes, privacy and anti-money-laundering. | 5 | 6 | 4 |
| [marketing](marketing/) | Campaigns, listings, content, paid media and lead generation. | 3 | 6 | 1 |
| [post-sales](post-sales/) | Handover, warranty, complaints and customer retention. | 3 | 5 | 0 |
| [pre-sales](pre-sales/) | Lead qualification, visit scheduling and follow-up before the sales stage. | 2 | 4 | 1 |
| [procurement](procurement/) | Suppliers, contractors and quote comparison. | 1 | 3 | 1 |
| [property-management](property-management/) | Leasing, tenants, inspections, maintenance and condominium administration. | 4 | 6 | 3 |
| [renovation](renovation/) | Scope, budget, schedule and quality control of renovation works. | 3 | 5 | 2 |
| [sales](sales/) | Proposals, negotiation, financing, closing and commissions. | 3 | 5 | 3 |
| [technology-data](technology-data/) | Systems integration, business intelligence and information security. | 1 | 4 | 0 |
| [jurisdictions](jurisdictions/) | Brazil, United States and Europe rules | 0 | 1 | 0 |

## Layout

```
.claude-plugin/marketplace.json   plugin registry
<department>/
  .claude-plugin/plugin.json
  agents/rt-*.md
  commands/rt-*.md
  skills/<skill>/SKILL.md, references/, assets/, scripts/
jurisdictions/                    shared country rules
orchestration/                    cross-department workflows
standards/                        company standards
templates/                        models for new files
docs/                             documentation site
```

## Documentation

- [Site and user guide (Portuguese)](docs/README.md)
- [Content review](CONTENT-REVIEW.md)
- [Installation](INSTALLATION.md)
- [Conventions](CONVENTIONS.md)
- [Skill authoring standard](SKILL-AUTHORING-STANDARD.md)
- [Orchestration](orchestration/ORCHESTRATION.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Changelog](CHANGELOG.md)

## License

See [LICENSE](LICENSE) (GPL v2).
