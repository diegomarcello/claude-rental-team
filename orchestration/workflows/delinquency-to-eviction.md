# Delinquency To Eviction

Delinquency, collection and eviction. Source: content architecture document `03`.

| # | Stage | Skills |
|---|---|---|
| 1 | Overdue D+1 | `rt-finance:accounts-receivable` |
| 2 | Amicable collection D+1 to D+30 | `rt-finance:collections` |
| 3 | Notice, agreement or eviction | `rt-legal:disputes-eviction` |
| 4 | Move-out inspection and deposit | `rt-property-management:move-inspections` |
| 5 | Accounting closure | `rt-finance:financial-close` |

Owners, deadlines, exit criteria and failure paths are not defined yet.
