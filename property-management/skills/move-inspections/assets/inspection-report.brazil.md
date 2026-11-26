---
template: inspection-report
approved_by: Coordenador de Locação
---

# Laudo de Vistoria de Imóvel ({{tipo_vistoria}})

**Contrato nº:** {{numero_contrato}} | **Data da Vistoria:** {{data_vistoria}}  
**Imóvel:** {{endereco_imovel}}  
**Vistoriador:** {{nome_vistoriador}}  
**Acompanhante:** {{nome_acompanhante}} ({{papel_acompanhante}})

## 1. Leitura de Medidores e Chaves Entregues
| Item | Identificação / Medidor | Leitura Atual | Observação |
|---|---|---|---|
| Energia Elétrica | {{medidor_energia}} | {{leitura_energia}} kWh | {{obs_energia}} |
| Água / Saneamento | {{medidor_agua}} | {{leitura_agua}} m³ | {{obs_agua}} |
| Gás | {{medidor_gas}} | {{leitura_gas}} m³ | {{obs_gas}} |
| Chaves / Controles | {{quantidade_chaves}} chaves / {{quantidade_controles}} controles | Conferido | {{obs_chaves}} |

## 2. Estado de Conservação por Ambiente
| Ambiente | Item | Estado ({{tipo_vistoria}}) | Observações e Evidência Fotográfica |
|---|---|---|---|
| {{ambiente_1}} | Pintura / Paredes / Piso | {{estado_1}} | {{descricao_1}} (Foto #{{foto_1}}) |
| {{ambiente_2}} | Esquadrias / Elétrica / Hidráulica | {{estado_2}} | {{descricao_2}} (Foto #{{foto_2}}) |

## 3. Divergências Apuradas (Aplicável na Vistoria de Saída)
{{resumo_divergencias_saida}}

## 4. Aceite e Prazo de Contestação
As partes declaram ter conferido o imóvel e o acervo fotográfico anexo. Eventuais divergências deverão ser comunicadas por escrito no prazo contratual de **{{prazo_contestacao_dias}} dias corridos**.

______________________________________  
**VISTORIADOR / ADMINISTRADORA**

______________________________________  
**LOCATÁRIO(A)**

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| tipo_vistoria | enum (ENTRADA\|SAIDA\|PERIODICA) | sim | `move-inspections` |
| numero_contrato | string | sim | Contrato |
| data_vistoria | date | sim | `move-inspections` |
| endereco_imovel | string | sim | Cadastro imóvel |
| nome_vistoriador | string | sim | Operação |
| nome_acompanhante | string | sim | Operação |
| papel_acompanhante | string | sim | Operação |
| medidor_energia | string | sim | Vistoria |
| leitura_energia | decimal | sim | Vistoria |
| obs_energia | string | não | Vistoria |
| medidor_agua | string | sim | Vistoria |
| leitura_agua | decimal | sim | Vistoria |
| obs_agua | string | não | Vistoria |
| medidor_gas | string | não | Vistoria |
| leitura_gas | decimal | não | Vistoria |
| obs_gas | string | não | Vistoria |
| quantidade_chaves | integer | sim | Vistoria |
| quantidade_controles | integer | não | Vistoria |
| obs_chaves | string | não | Vistoria |
| ambiente_1 | string | sim | Vistoria |
| estado_1 | enum (NOVO\|BOM\|REGULAR\|DANIFICADO) | sim | Vistoria |
| descricao_1 | text | sim | Vistoria |
| foto_1 | string | sim | Acervo fotográfico |
| ambiente_2 | string | não | Vistoria |
| estado_2 | enum (NOVO\|BOM\|REGULAR\|DANIFICADO) | não | Vistoria |
| descricao_2 | text | não | Vistoria |
| foto_2 | string | não | Acervo fotográfico |
| resumo_divergencias_saida | text | não | `move-inspections` |
| prazo_contestacao_dias | integer | sim | Contrato / `company-context.md` |
