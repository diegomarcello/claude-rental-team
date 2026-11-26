---
template: dcf-cap-rate-model
approved_by: Avaliador Imobiliário
---

# Modelo de Avaliação pela Renda (Cap Rate Direto e FCD)

**Imóvel:** {{endereco_imovel}} | **Data-Base:** {{data_avaliacao}}  
**Avaliador:** {{nome_avaliador}} ({{registro_profissional}})

## 1. Premissas Operacionais (NOI — Net Operating Income)
| Item | Valor Mensal (BRL) | Valor Anual (BRL) | Premissa / Origem |
|---|---|---|---|
| Receita Bruta Potencial (RBP) | {{rbp_mensal}} | {{rbp_anual}} | {{fonte_aluguel_mercado}} |
| (-) Vacância e Inadimplência ({{taxa_vacancia_pct}}%) | -{{vacancia_mensal}} | -{{vacancia_anual}} | {{fonte_vacancia}} |
| (=) Receita Bruta Efetiva (RBE) | {{rbe_mensal}} | {{rbe_anual}} | Calculado |
| (-) Despesas Operacionais Não Reembolsáveis | -{{despesas_mensais}} | -{{despesas_anuais}} | {{detalhe_despesas}} |
| **(=) Resultado Operacional Líquido (NOI)** | **{{noi_mensal}}** | **{{noi_anual}}** | Calculado |

## 2. Capitalização Direta (Cap Rate)
- **Cap Rate de Mercado Adotado:** {{cap_rate_pct}}% *(Fonte: {{fonte_cap_rate}})*
- **Valor Estimado (NOI Anual / Cap Rate):** **R$ {{valor_cap_rate}}**

## 3. Fluxo de Caixa Descontado (FCD — Horizonte {{horizonte_anos}} anos)
- **Taxa de Desconto (TMA / WACC):** {{taxa_desconto_pct}}% a.a. | **Cap Rate de Saída:** {{exit_cap_rate_pct}}%
- **VPL dos Fluxos + Perpetuidade:** **R$ {{valor_fcd}}**

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| endereco_imovel | string | sim | Cadastro imóvel |
| data_avaliacao | date | sim | `income-capitalization` |
| nome_avaliador | string | sim | Avaliador |
| registro_profissional | string | sim | CREA/CAU/CNAI |
| rbp_mensal | decimal (BRL) | sim | `income-capitalization` |
| rbp_anual | decimal (BRL) | sim | Calculado |
| fonte_aluguel_mercado | string | sim | `comparative-market-analysis` |
| taxa_vacancia_pct | decimal (%) | sim | `income-capitalization` |
| vacancia_mensal | decimal (BRL) | sim | Calculado |
| vacancia_anual | decimal (BRL) | sim | Calculado |
| fonte_vacancia | string | sim | Estudo de mercado |
| rbe_mensal | decimal (BRL) | sim | Calculado |
| rbe_anual | decimal (BRL) | sim | Calculado |
| despesas_mensais | decimal (BRL) | sim | `income-capitalization` |
| despesas_anuais | decimal (BRL) | sim | Calculado |
| detalhe_despesas | string | sim | `income-capitalization` |
| noi_mensal | decimal (BRL) | sim | Calculado |
| noi_anual | decimal (BRL) | sim | Calculado |
| cap_rate_pct | decimal (%) | sim | `income-capitalization` |
| fonte_cap_rate | string | sim | Pesquisa / `company-context.md` |
| valor_cap_rate | decimal (BRL) | sim | Calculado |
| horizonte_anos | integer | sim | `income-capitalization` |
| taxa_desconto_pct | decimal (%) | sim | `income-capitalization` |
| exit_cap_rate_pct | decimal (%) | sim | `income-capitalization` |
| valor_fcd | decimal (BRL) | sim | Calculado |
