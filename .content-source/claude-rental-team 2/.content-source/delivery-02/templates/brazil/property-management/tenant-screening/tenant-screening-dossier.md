---
template: tenant-screening-dossier
approved_by: Coordenador de Locação
---

# Parecer de Análise Cadastral e Risco de Locação

**Protocolo:** {{protocolo_cadastro}} | **Data:** {{data_analise}}  
**Imóvel Pretendido:** {{endereco_imovel}}  
**Pacote Mensal (Aluguel + Condomínio + IPTU):** R$ {{valor_pacote_mensal}}

## 1. Identificação do(a) Pretendente
- **Nome / Razão Social:** {{nome_pretendente}}  
- **Tipo:** {{tipo_pessoa}} (PF / PJ)  
- **Garantia Selecionada:** {{modalidade_garantia}}

## 2. Indicadores Financeiros e de Crédito
| Critério | Apurado | Parâmetro da Empresa | Status |
|---|---|---|---|
| Renda Líquida Comprovada | R$ {{renda_comprovada}} | Mín. {{multiplo_renda_exigido}}x pacote (R$ {{renda_minima_exigida}}) | {{status_renda}} |
| Comprometimento de Renda | {{percentual_comprometimento}}% | Máx. {{comprometimento_maximo_pct}}% | {{status_comprometimento}} |
| Restrições SPC / Serasa / Protestos | {{valor_restricoes}} ({{qtd_apontamentos}} apont.) | {{regra_restricoes}} | {{status_credito}} |
| Processos Judiciais (Despejo/Execução) | {{resumo_processos}} | Zero ações de despejo/execução ativa | {{status_judicial}} |

## 3. Parecer Final e Condicionantes
- **Decisão:** `{{parecer_final}}` *(APROVADO | APROVADO_COM_CONDICIONANTE | REPROVADO)*
- **Justificativa:** {{justificativa_parecer}}

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| protocolo_cadastro | string | sim | `tenant-screening` |
| data_analise | date | sim | `tenant-screening` |
| endereco_imovel | string | sim | Cadastro imóvel |
| valor_pacote_mensal | decimal (BRL) | sim | Cadastro imóvel |
| nome_pretendente | string | sim | Ficha cadastral |
| tipo_pessoa | enum (PF\|PJ) | sim | Ficha cadastral |
| modalidade_garantia | string | sim | Proposta |
| renda_comprovada | decimal (BRL) | sim | Documentos de renda |
| multiplo_renda_exigido | decimal | sim | `company-context.md` |
| renda_minima_exigida | decimal (BRL) | sim | Calculado |
| status_renda | enum (CONFORME\|NAO_CONFORME) | sim | `tenant-screening` |
| percentual_comprometimento | decimal (%) | sim | Calculado |
| comprometimento_maximo_pct | decimal (%) | sim | `company-context.md` |
| status_comprometimento | enum (CONFORME\|NAO_CONFORME) | sim | `tenant-screening` |
| valor_restricoes | decimal (BRL) | sim | Consulta birô |
| qtd_apontamentos | integer | sim | Consulta birô |
| regra_restricoes | string | sim | `company-context.md` |
| status_credito | enum (CONFORME\|NAO_CONFORME) | sim | `tenant-screening` |
| resumo_processos | string | sim | Certidões forenses |
| status_judicial | enum (CONFORME\|NAO_CONFORME) | sim | `tenant-screening` |
| parecer_final | enum (APROVADO\|APROVADO_COM_CONDICIONANTE\|REPROVADO) | sim | `tenant-screening` |
| justificativa_parecer | text | sim | `tenant-screening` |
