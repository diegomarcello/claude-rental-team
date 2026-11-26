# Known Issues

Found during integration. This file overrides the reference files, which were copied unchanged.

- `europe.md`: the numeric example is the United States one (US dollars or US units), not a European one. Use the formulas only; take currency, units and local rules from the Europe jurisdiction files.

## Delivery 02 (Brazil)

- `cost-approach-report.brazil.md` has a broken formula: a tab character replaced `\t` in `\times`. Read it as `V_I = (V_T + C_D) × FC`.
