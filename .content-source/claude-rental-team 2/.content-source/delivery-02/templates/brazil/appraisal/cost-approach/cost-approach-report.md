---
template: cost-approach-report
approved_by: Avaliador Imobiliário
---

# Laudo de Avaliação pelo Método Evolutivo / Custo de Reedição (ABNT NBR 14653)

**Imóvel:** {{endereco_imovel}} | **Data-Base:** {{data_avaliacao}}  
**Norma Aplicável:** ABNT NBR 14653-2 | **Grau de Fundamentação:** {{grau_fundamentacao}}

## 1. Valor do Terreno (Método Comparativo)
- **Área do Terreno:** {{area_terreno_m2}} m² | **Valor Unitário:** R$ {{valor_unitario_terreno}}/m²
- **Valor Total do Terreno ($V_T$):** **R$ {{valor_terreno}}**

## 2. Custo de Reedição das Benfeitorias
- **Área Construída Equivalente:** {{area_construida_m2}} m² | **Padrão Construtivo:** {{padrao_construtivo}}
- **CUB Referência ({{mes_referencia_cub}} — Sinduscon/{{uf_cub}}):** R$ {{valor_cub_m2}}/m²
- **BDI Adotado:** {{bdi_pct}}% | **Custo de Reprodução Novo ($C_N$):** R$ {{custo_reproducao_novo}}
- **Idade Aparente:** {{idade_aparente}} anos | **Vida Útil:** {{vida_util}} anos | **Estado:** {{estado_conservacao_ross_heidecke}}
- **Fator de Depreciação (Ross-Heidecke):** {{fator_depreciacao}}
- **Custo Depreciado da Benfeitoria ($C_D$):** **R$ {{custo_depreciado}}**

## 3. Composição Final (Fator de Comercialização = {{fator_comercializacao}})
- **Valor do Imóvel ($V_I = (V_T + C_D) 	imes FC$):** **R$ {{valor_final_imovel}}**

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| endereco_imovel | string | sim | Cadastro imóvel |
| data_avaliacao | date | sim | `cost-approach` |
| grau_fundamentacao | string | sim | ABNT NBR 14653 |
| area_terreno_m2 | decimal | sim | Matrícula / Planta |
| valor_unitario_terreno | decimal (BRL) | sim | `comparative-market-analysis` |
| valor_terreno | decimal (BRL) | sim | Calculado |
| area_construida_m2 | decimal | sim | Matrícula / Projeto |
| padrao_construtivo | string | sim | NBR 12721 |
| mes_referencia_cub | string | sim | Sinduscon |
| uf_cub | string | sim | Sinduscon |
| valor_cub_m2 | decimal (BRL) | sim | Sinduscon |
| bdi_pct | decimal (%) | sim | `cost-approach` |
| custo_reproducao_novo | decimal (BRL) | sim | Calculado |
| idade_aparente | integer | sim | Vistoria técnica |
| vida_util | integer | sim | Tabela Ross-Heidecke |
| estado_conservacao_ross_heidecke | string | sim | Vistoria técnica |
| fator_depreciacao | decimal | sim | Calculado |
| custo_depreciado | decimal (BRL) | sim | Calculado |
| fator_comercializacao | decimal | sim | `cost-approach` |
| valor_final_imovel | decimal (BRL) | sim | Calculado |
