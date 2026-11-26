# Known Issues

Found during integration. This file overrides the reference files, which were copied unchanged.

- `brazil.md`: the Price example is wrong. For PV 400,000, n = 360 and i = 0.80% per month the payment is **3,392.64**, not 3,394.54.
- `united-states.md` and `europe.md`: the annuity payment rounds to 2,554.64, not 2,554.63.
- `europe.md`: the numeric example is the United States one (US dollars or US units), not a European one. Use the formulas only; take currency, units and local rules from the Europe jurisdiction files.

## Delivery 02 (Brazil)

- The calculation spec expects 3,392.64 (22.62% of 15,000) for 400,000 over 360 months at **10% a year**. That payment is for **0.80% a month** (10.03% a year). At 10% effective a year the payment is **3,383.56** (22.56% of 15,000; 33.84% of 10,000). The script and its tests use the correct values.
