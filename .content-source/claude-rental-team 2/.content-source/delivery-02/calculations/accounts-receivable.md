---
skill: accounts-receivable
jurisdiction: brazil
validated_by: Gerente Financeiro / Advogado Imobiliário
---

## Entradas
| Campo | Tipo | Obrigatório | Unidade |
|---|---|---|---|
| valor_principal | decimal | sim | BRL |
| data_vencimento | date | sim | AAAA-MM-DD |
| data_pagamento | date | sim | AAAA-MM-DD |
| multa_moratoria_pct | decimal | não (padrão 2.0) | % |
| juros_mensal_pct | decimal | não (padrão 1.0) | % ao mês |
| indice_correcao_pct | decimal | não (padrão 0.0) | % acumulado no período |

## Fórmula e regras
- `dias_atraso = max(0, (data_pagamento - data_vencimento).days)`
- **Faixas de atraso:**
  - `0 dias`: em dia (sem encargos).
  - `1 a 15 dias`: cobrança administrativa amigável.
  - `16 a 30 dias`: notificação extrajudicial / protesto.
  - `> 30 dias`: encaminhamento ao jurídico (`collections` -> `disputes-eviction`).
- **Cálculo de encargos (se `dias_atraso > 0`):**
  - `multa = round(valor_principal * (multa_moratoria_pct / 100), 2)`
  - `juros = round(valor_principal * (juros_mensal_pct / 100) * (dias_atraso / 30), 2)`
  - `correcao = round(valor_principal * (indice_correcao_pct / 100), 2)` (aplicável normalmente a partir de 30 dias)
  - `valor_atualizado = round(valor_principal + multa + juros + correcao, 2)`

## Casos de teste
| Caso | Entradas | Resultado esperado |
|---|---|---|
| Normal (atraso 10 dias) | principal=2500.00; venc=2026-11-05; pagto=2026-11-15; multa=2%; juros=1%/mês | `dias_atraso=10`, `multa=50.00`, `juros=8.33`, `total=2558.33`, `faixa=1_a_15_dias` |
| Limite (pagamento no vencimento) | principal=2500.00; venc=2026-11-05; pagto=2026-11-05 | `dias_atraso=0`, `multa=0.00`, `juros=0.00`, `total=2500.00`, `faixa=em_dia` |
| Erro | data_pagamento anterior à data_vencimento sem regra de desconto | Tratar `dias_atraso=0` (sem multa/juros) e alertar pagamento antecipado |
