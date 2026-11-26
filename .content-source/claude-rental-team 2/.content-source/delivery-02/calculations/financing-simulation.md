---
skill: financing-simulation
jurisdiction: brazil
validated_by: Gerente Financeiro / Contador
---

## Entradas
| Campo | Tipo | Obrigatório | Unidade |
|---|---|---|---|
| valor_imovel | decimal | sim | BRL |
| valor_entrada | decimal | sim | BRL |
| prazo_meses | integer | sim | meses |
| taxa_juros_anual_pct | decimal | sim | % ao ano |
| sistema | string | sim | PRICE \| SAC |
| renda_familiar_mensal | decimal | não | BRL |
| seguros_e_taxas_mensais | decimal | não (padrão 0) | BRL |

## Fórmula e regras
- `valor_financiado = valor_imovel - valor_entrada`
- **Conversão de taxa anual efetiva para mensal equivalente:**
  - `i_mensal = (1 + taxa_juros_anual_pct / 100) ** (1 / 12) - 1`
- **Tabela Price (parcelas constantes de amortização + juros):**
  - `pmt_base = valor_financiado * (i_mensal * (1 + i_mensal) ** prazo_meses) / ((1 + i_mensal) ** prazo_meses - 1)`
  - `primeira_parcela = round(pmt_base + seguros_e_taxas_mensais, 2)`
- **Tabela SAC (amortização constante):**
  - `amortizacao = valor_financiado / prazo_meses`
  - `juros_1 = valor_financiado * i_mensal`
  - `primeira_parcela = round(amortizacao + juros_1 + seguros_e_taxas_mensais, 2)`
- **Limite de comprometimento de renda:** Máximo de `30%` da `renda_familiar_mensal` (quando informada).
- **Nota de correção:** Substitui o exemplo legado incorreto (`3.394,54` -> `3.392,64` para R$ 400.000,00 financiados em 360 meses a 10% a.a. equivalente).

## Casos de teste
| Caso | Entradas | Resultado esperado |
|---|---|---|
| Normal (Price) | imovel=500000.00; entrada=100000.00; prazo=360; taxa_anual=10.0%; sistema=PRICE; renda=15000.00 | `financiado=400000.00`, `parcela=3392.64`, `comprometimento=22.62%`, `status=aprovado_renda` |
| Limite (comprometimento > 30%) | imovel=500000.00; entrada=100000.00; prazo=360; taxa_anual=10.0%; sistema=PRICE; renda=10000.00 | `parcela=3392.64`, `comprometimento=33.93%`, `status=reprovado_limite_renda` |
| Erro | entrada >= valor_imovel | Recusar simulação e informar que não há saldo a financiar |
