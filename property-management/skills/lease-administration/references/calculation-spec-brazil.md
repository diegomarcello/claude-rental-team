---
skill: lease-administration
jurisdiction: brazil
validated_by: Coordenador de Locação / Advogado Imobiliário
---

## Entradas
| Campo | Tipo | Obrigatório | Unidade |
|---|---|---|---|
| aluguel_atual | decimal | sim | BRL |
| indice_nome | string | sim | IPCA \| IGPM \| INPC \| IVAR |
| variacao_indice_pct | decimal | sim | % (ex.: 4.62) |
| permite_deflacao | boolean | não (padrão false) | booleano |
| multa_contratual_alugueis | decimal | não (padrão 3.0) | múltiplos de aluguel |
| prazo_total_meses | integer | não (padrão 30) | meses |
| meses_cumpridos | integer | não (padrão 0) | meses |

## Fórmula e regras
- **Reajuste anual:**
  - Se `variacao_indice_pct < 0` e `permite_deflacao == false`: `fator = 1.0` (mantém o valor nominal atual, sem redução, conforme cláusula padrão de proteção).
  - Caso contrário: `fator = 1 + (variacao_indice_pct / 100)`.
  - `novo_aluguel = round(aluguel_atual * fator, 2)`.
- **Multa rescisória proporcional (Art. 4º da Lei 8.245/91):**
  - Se `meses_cumpridos >= prazo_total_meses`: `multa_proporcional = 0.00`.
  - Caso contrário: `multa_cheia = aluguel_atual * multa_contratual_alugueis` e `multa_proporcional = round(multa_cheia * ((prazo_total_meses - meses_cumpridos) / prazo_total_meses), 2)`.
- **Arredondamento:** 2 casas decimais (`ROUND_HALF_UP`).

## Casos de teste
| Caso | Entradas | Resultado esperado |
|---|---|---|
| Normal (reajuste) | aluguel_atual=3500.00; indice=IPCA; variacao=4.62% | `novo_aluguel=3661.70`, `diferenca=161.70` |
| Limite (índice negativo + multa proporcional) | aluguel_atual=3000.00; variacao=-1.20%; permite_deflacao=false; prazo=30; cumpridos=12; multa=3 | `novo_aluguel=3000.00`; `multa_proporcional=5400.00` |
| Erro | aluguel_atual=3500.00; variacao_indice_pct=ausente | Recusar cálculo e solicitar a variação acumulada em 12 meses do índice |
