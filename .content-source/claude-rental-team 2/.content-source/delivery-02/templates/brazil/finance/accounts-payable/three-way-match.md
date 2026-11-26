---
template: three-way-match
approved_by: Gerente Financeiro
---

# Conferência Três Vias (Three-Way Match) — Contas a Pagar

**Protocolo AP:** {{protocolo_ap}} | **Data:** {{data_conferencia}}  
**Fornecedor:** {{razao_social_fornecedor}} (CNPJ {{cnpj_fornecedor}})  
**Centro de Custo / Imóvel:** {{centro_custo_imovel}}

## 1. Cruzamento de Documentos
| Documento | Número / Referência | Valor (BRL) | Quantidade / Escopo | Status |
|---|---|---|---|---|
| 1. Ordem de Compra / Serviço (OC/OS) | {{numero_os}} | R$ {{valor_os}} | {{escopo_os}} | {{status_os}} |
| 2. Comprovante de Entrega / Medição / Vistoria | {{numero_medicao}} | R$ {{valor_medicao}} | {{escopo_medicao}} | {{status_medicao}} |
| 3. Nota Fiscal / Fatura | {{numero_nf}} | R$ {{valor_nf}} | {{escopo_nf}} | {{status_nf}} |

## 2. Retenções Tributárias Aplicáveis (Brasil)
- **ISS Retido:** R$ {{retencao_iss}} | **INSS (11%):** R$ {{retencao_inss}} | **IRRF / CSRF:** R$ {{retencao_irrf_csrf}}
- **Valor Líquido a Pagar:** **R$ {{valor_liquido_pagar}}** | **Vencimento:** {{data_vencimento}}

## 3. Alçada e Aprovação
- **Alçada Exigida (`company-context.md`):** {{alcada_exigida}}
- **Resultado da Conferência:** `{{resultado_match}}` *(APROVADO_PAGAMENTO | DIVERGENCIA_BLOQUEADO)*

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| protocolo_ap | string | sim | `accounts-payable` |
| data_conferencia | date | sim | `accounts-payable` |
| razao_social_fornecedor | string | sim | Nota Fiscal |
| cnpj_fornecedor | string | sim | Nota Fiscal |
| centro_custo_imovel | string | sim | Ordem de Serviço |
| numero_os | string | sim | Manutenção / Compras |
| valor_os | decimal (BRL) | sim | Ordem de Serviço |
| escopo_os | string | sim | Ordem de Serviço |
| status_os | string | sim | `accounts-payable` |
| numero_medicao | string | sim | Vistoria / Recebimento |
| valor_medicao | decimal (BRL) | sim | Vistoria / Recebimento |
| escopo_medicao | string | sim | Vistoria / Recebimento |
| status_medicao | string | sim | `accounts-payable` |
| numero_nf | string | sim | Nota Fiscal |
| valor_nf | decimal (BRL) | sim | Nota Fiscal |
| escopo_nf | string | sim | Nota Fiscal |
| status_nf | string | sim | `accounts-payable` |
| retencao_iss | decimal (BRL) | não | `accounts-payable` |
| retencao_inss | decimal (BRL) | não | `accounts-payable` |
| retencao_irrf_csrf | decimal (BRL) | não | `accounts-payable` |
| valor_liquido_pagar | decimal (BRL) | sim | `accounts-payable` |
| data_vencimento | date | sim | Nota Fiscal |
| alcada_exigida | string | sim | `company-context.md` |
| resultado_match | enum (APROVADO_PAGAMENTO\|DIVERGENCIA_BLOQUEADO) | sim | `accounts-payable` |
