# Known Issues

Found during integration. This file overrides the reference files, which were copied unchanged.

- `europe.md`: the numeric example is the United States one (US dollars or US units), not a European one. Use the formulas only; take currency, units and local rules from the Europe jurisdiction files.

## Delivery 02 (Brazil)

- The calculation spec and the script do not handle the fine exemption of Lei 8.245/91, art. 4, sole paragraph: transfer of the tenant by the employer to another location, with at least 30 days' written notice. Always ask about it.
- The spec defaults `meses_cumpridos` to 0, which gives the full fine. Never run the fine without the actual months completed.
- `brazil.md` requires 30 days' notice before a rent adjustment and cites no legal source for it. Treat it as a company rule to confirm.
