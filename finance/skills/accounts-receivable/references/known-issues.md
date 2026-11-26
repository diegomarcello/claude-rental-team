# Known Issues

This file overrides the reference files, which were copied unchanged.

## Delivery 02 (Brazil)

- `brazil.md` sends paid items to `rt-property-management/owner-payouts`. The skill is `rt-finance:owner-payouts`.
- `brazil.md` says to follow `calculations/accounts-receivable.md`: that file is `calculation-spec-brazil.md`.
- Three delinquency ladders disagree: the calculation spec (1-15 amicable, 16-30 notice, over 30 legal), the `collections` reference (D+1-5, D+6-15, D+16-30, over 30) and the company context example (formal notice D+5, legal D+15, lawsuit D+30). Use the company's confirmed ladder; if there is none, show the conflict and ask.
