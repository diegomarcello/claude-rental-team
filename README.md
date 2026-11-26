# claude-rental-team

Rental company team for Brazil, the US and Europe designed for Claude.

Agents, skills, commands and templates to run a real estate company: buying, appraisal, sales, renovation and property management, plus the supporting departments.

> **Status: skeleton (v0.1.0).** Structure and file models only. Procedures, scripts and business content are marked `TODO`. Jurisdiction references are not verified. Nothing here is legal, tax or valuation advice.

## Departments

16 plugins, 42 agents, 75 skills, 21 commands.

| Folder | Scope | Agents | Skills | Commands |
|---|---|---|---|---|
| [executive](executive/) | Company direction, KPIs, approval authority and cross-department routing. | 3 | 4 | 1 |
| [acquisitions](acquisitions/) | Property sourcing, opportunity screening, feasibility and purchase negotiation. | 3 | 4 | 1 |
| [appraisal](appraisal/) | Market, income and cost valuation, and technical property inspection. | 3 | 5 | 1 |
| [legal](legal/) | Title due diligence, contracts, tenancy law, disputes, privacy and anti-money-laundering. | 4 | 6 | 2 |
| [renovation](renovation/) | Scope, budget, schedule and quality control of renovation works. | 3 | 5 | 1 |
| [marketing](marketing/) | Campaigns, listings, content, paid media and lead generation. | 4 | 6 | 2 |
| [pre-sales](pre-sales/) | Lead qualification, visit scheduling and follow-up before the sales stage. | 2 | 4 | 1 |
| [sales](sales/) | Proposals, negotiation, financing, closing and commissions. | 3 | 5 | 2 |
| [crm](crm/) | Pipeline, segmentation, data quality and automated customer journeys. | 2 | 5 | 1 |
| [property-management](property-management/) | Leasing, tenants, inspections, maintenance and condominium administration. | 3 | 6 | 2 |
| [post-sales](post-sales/) | Handover, warranty, complaints and customer retention. | 2 | 5 | 1 |
| [finance](finance/) | Payables, receivables, collections, cash, owner payouts, close and taxes. | 5 | 8 | 3 |
| [procurement](procurement/) | Suppliers, contractors and quote comparison. | 1 | 3 | 1 |
| [human-resources](human-resources/) | Recruiting, onboarding, performance and compensation. | 2 | 4 | 1 |
| [technology-data](technology-data/) | Systems integration, business intelligence and information security. | 2 | 4 | 1 |
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
```

## Documentation

- [Installation](INSTALLATION.md)
- [Conventions](CONVENTIONS.md)
- [Skill authoring standard](SKILL-AUTHORING-STANDARD.md)
- [Orchestration](orchestration/ORCHESTRATION.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Changelog](CHANGELOG.md)

## License

See [LICENSE](LICENSE) (GPL v2).
