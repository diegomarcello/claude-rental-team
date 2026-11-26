---
skill: owner-payouts
jurisdiction: brazil
validated_by: Gerente Financeiro / Contador
---

## Entradas
| Campo | Tipo | Obrigatório | Unidade |
|---|---|---|---|
| aluguel_recebido | decimal | sim | BRL |
| taxa_adm_pct | decimal | sim | % (ex.: 10.0) |
| taxa_intermediacao | decimal | não (padrão 0) | BRL |
| retencoes_irrf | decimal | não (padrão 0) | BRL |
| reparos_autorizados | decimal | não (padrão 0) | BRL |
| encargos_reembolsaveis | decimal | não (padrão 0) | BRL |
| dias_uteis_prazo | integer | não (padrão 3) | dias úteis |

## Fórmula e regras
- `valor_taxa_adm = round(aluguel_recebido * (taxa_adm_pct / 100), 2)`
- `total_descontos = valor_taxa_adm + taxa_intermediacao + retencoes_irrf + reparos_autorizados`
- `repasse_liquido = round(aluguel_recebido + encargos_reembolsaveis - total_descontos, 2)`
- **Prazo de pagamento:** `data_compensacao + dias_uteis_prazo` (padrão D+3 dias úteis).
- **Regra de saldo negativo:** Se `repasse_liquido < 0`, o repasse financeiro é bloqueado (`0.00`), gera-se um saldo devedor (`abs(repasse_liquido)`) a ser compensado nos repasses futuros ou cobrado via boleto ao proprietário conforme política em `company-context.md`.
- **Arredondamento:** 2 casas decimais (padrão `ROUND_HALF_UP`).

## Casos de teste
| Caso | Entradas | Resultado esperado |
|---|---|---|
| Normal | aluguel=5000.00; taxa_adm=10%; intermediacao=0; irrf=0; reparos=350.00; reembolso=0 | `taxa_adm=500.00`, `repasse_liquido=4150.00`, `status=liberar_pagamento` |
| Limite (saldo negativo) | aluguel=5000.00; taxa_adm=10%; intermediacao=0; irrf=0; reparos=6000.00; reembolso=0 | `taxa_adm=500.00`, `repasse_liquido=-1500.00`, `status=saldo_negativo_reter` |
| Erro | aluguel=5000.00; taxa_adm=ausente | Recusar cálculo e solicitar `taxa_adm_pct` (ou consultar `company-context.md`) |
