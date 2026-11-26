# Known Issues

This file overrides the reference files, which were copied unchanged.

## Delivery 02 (Brazil)

- `brazil.md` sends paid agreements to `rt-property-management/owner-payouts`. The skill is `rt-finance:owner-payouts`.
- Its collection ladder disagrees with the `accounts-receivable` calculation spec and with the company context example. Use the company's confirmed ladder; if there is none, show the conflict and ask.
