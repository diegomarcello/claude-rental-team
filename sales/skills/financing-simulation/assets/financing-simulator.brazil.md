---
template: financing-simulator
approved_by: Gerente Comercial / Financeiro
---

# Simulação de Financiamento Imobiliário

**Cliente:** {{nome_cliente}} | **Data:** {{data_simulacao}}  
**Imóvel:** {{descricao_imovel}}

## Parâmetros da Operação
- **Valor do Imóvel:** R$ {{valor_imovel}}
- **Entrada ({{percentual_entrada}}%):** R$ {{valor_entrada}}
- **Valor Financiado:** R$ {{valor_financiado}}
- **Prazo:** {{prazo_meses}} meses | **Taxa Efetiva:** {{taxa_juros_anual_pct}}% a.a.
- **Renda Familiar Informada:** R$ {{renda_familiar_mensal}} (Limite 30%: R$ {{limite_parcela_renda}})

## Comparativo SAC vs. Tabela Price
| Indicador | Sistema SAC | Tabela Price |
|---|---|---|
| 1ª Parcela (inclui seguros/taxas) | R$ {{primeira_parcela_sac}} | R$ {{primeira_parcela_price}} |
| Última Parcela Estimada | R$ {{ultima_parcela_sac}} | R$ {{ultima_parcela_price}} |
| Comprometimento de Renda (1ª Parcela) | {{comprometimento_sac_pct}}% | {{comprometimento_price_pct}}% |
| Enquadramento na Política de Renda | {{enquadramento_sac}} | {{enquadramento_price}} |

> *Simulação de caráter informativo, sujeita à análise de crédito e avaliação de engenharia pela instituição financeira.*

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| nome_cliente | string | sim | CRM / Vendas |
| data_simulacao | date | sim | `financing-simulation` |
| descricao_imovel | string | sim | Cadastro imóvel |
| valor_imovel | decimal (BRL) | sim | `financing-simulation` |
| percentual_entrada | decimal (%) | sim | Calculado |
| valor_entrada | decimal (BRL) | sim | `financing-simulation` |
| valor_financiado | decimal (BRL) | sim | `financing-simulation` |
| prazo_meses | integer | sim | `financing-simulation` |
| taxa_juros_anual_pct | decimal (%) | sim | `financing-simulation` |
| renda_familiar_mensal | decimal (BRL) | não | `financing-simulation` |
| limite_parcela_renda | decimal (BRL) | não | Calculado |
| primeira_parcela_sac | decimal (BRL) | sim | `financing-simulation` |
| primeira_parcela_price | decimal (BRL) | sim | `financing-simulation` |
| ultima_parcela_sac | decimal (BRL) | sim | `financing-simulation` |
| ultima_parcela_price | decimal (BRL) | sim | `financing-simulation` |
| comprometimento_sac_pct | decimal (%) | não | Calculado |
| comprometimento_price_pct | decimal (%) | não | Calculado |
| enquadramento_sac | string | não | `financing-simulation` |
| enquadramento_price | string | não | `financing-simulation` |
