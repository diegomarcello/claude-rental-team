---
template: sensitivity-matrix
approved_by: Diretoria / Investimentos
---

# Matriz de Sensibilidade e Viabilidade de Aquisição

**Ativo / Projeto:** {{nome_ativo}} | **Data:** {{data_estudo}}  
**Cenário Base — TIR:** {{tir_base_pct}}% a.a. | **VPL:** R$ {{vpl_base}} | **TMA Exigida:** {{tma_exigida_pct}}% a.a.

## Matriz de TIR (% a.a.) — Preço de Venda/Aluguel vs. Custo de Obra/Aquisição
| Variação Preço \ Custo | -10% Custo | Cenário Base (0%) | +10% Custo | +20% Custo |
|---|---|---|---|---|
| **+10% Receita** | {{tir_m10_p10}}% | {{tir_0_p10}}% | {{tir_p10_p10}}% | {{tir_p20_p10}}% |
| **Receita Base (0%)** | {{tir_m10_0}}% | **{{tir_base_pct}}%** | {{tir_p10_0}}% | {{tir_p20_0}}% |
| **-10% Receita** | {{tir_m10_m10}}% | {{tir_0_m10}}% | {{tir_p10_m10}}% | {{tir_p20_m10}}% |

## Recomendação de Comitê
- **Parecer:** `{{parecer_viabilidade}}` *(APROVAR | RENEGOCIAR_PRECO | DESCARTAR)*
- **Preço Máximo de Aquisição para atingir TMA:** R$ {{preco_teto_aquisicao}}

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| nome_ativo | string | sim | `deal-feasibility` |
| data_estudo | date | sim | `deal-feasibility` |
| tir_base_pct | decimal (%) | sim | `deal-feasibility` |
| vpl_base | decimal (BRL) | sim | `deal-feasibility` |
| tma_exigida_pct | decimal (%) | sim | `company-context.md` |
| tir_m10_p10 | decimal (%) | sim | `deal-feasibility` |
| tir_0_p10 | decimal (%) | sim | `deal-feasibility` |
| tir_p10_p10 | decimal (%) | sim | `deal-feasibility` |
| tir_p20_p10 | decimal (%) | sim | `deal-feasibility` |
| tir_m10_0 | decimal (%) | sim | `deal-feasibility` |
| tir_p10_0 | decimal (%) | sim | `deal-feasibility` |
| tir_p20_0 | decimal (%) | sim | `deal-feasibility` |
| tir_m10_m10 | decimal (%) | sim | `deal-feasibility` |
| tir_0_m10 | decimal (%) | sim | `deal-feasibility` |
| tir_p10_m10 | decimal (%) | sim | `deal-feasibility` |
| tir_p20_m10 | decimal (%) | sim | `deal-feasibility` |
| parecer_viabilidade | enum (APROVAR\|RENEGOCIAR_PRECO\|DESCARTAR) | sim | `deal-feasibility` |
| preco_teto_aquisicao | decimal (BRL) | sim | `deal-feasibility` |
