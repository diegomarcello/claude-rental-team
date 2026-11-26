---
template: owner-statement
approved_by: Gerente Financeiro
---

# Extrato de Repasse de Locação — {{mes_referencia}}

**Administradora:** {{nome_administradora}} (CRECI {{creci_administradora}})  
**Proprietário(a):** {{nome_proprietario}} | **CPF/CNPJ:** {{documento_proprietario}}  
**Imóvel:** {{endereco_imovel}} (Cód. {{codigo_imovel}})  
**Locatário(a):** {{nome_locatario}}  
**Competência:** {{mes_referencia}} | **Data do Crédito:** {{data_pagamento_repasse}}

---

## 1. Resumo Financeiro
| Descrição | Tipo | Valor (BRL) |
|---|---|---|
| Aluguel recebido (Competência {{mes_referencia}}) | Crédito | {{valor_aluguel_recebido}} |
| Reembolso de encargos (IPTU / Condomínio / Seguro) | Crédito | {{valor_encargos_reembolsaveis}} |
| Taxa de administração ({{percentual_taxa_adm}}%) | Débito | -{{valor_taxa_administracao}} |
| Taxa de intermediação / 1º aluguel | Débito | -{{valor_taxa_intermediacao}} |
| Retenção de IRRF na fonte | Débito | -{{valor_retencao_irrf}} |
| Manutenções e reparos autorizados (OS #{{numero_os}}) | Débito | -{{valor_reparos}} |
| **Valor Líquido Repassado** | **Total** | **{{valor_liquido_repasse}}** |

## 2. Dados Bancários de Destino
- **Banco / Instituição:** {{banco_destino}} | **Agência:** {{agencia_destino}} | **Conta:** {{conta_destino}}
- **Chave PIX / Comprovante:** {{identificador_transferencia}}

## 3. Observações
{{observacoes_extrato}}

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| mes_referencia | string (MM/AAAA) | sim | `owner-payouts` / financeiro |
| nome_administradora | string | sim | `company-context.md` |
| creci_administradora | string | sim | `company-context.md` |
| nome_proprietario | string | sim | Cadastro do proprietário |
| documento_proprietario | string (mascarado) | sim | Cadastro do proprietário |
| endereco_imovel | string | sim | Cadastro do imóvel |
| codigo_imovel | string | sim | Cadastro do imóvel |
| nome_locatario | string | sim | Contrato de locação |
| data_pagamento_repasse | date (DD/MM/AAAA) | sim | `owner-payouts` |
| valor_aluguel_recebido | decimal (BRL) | sim | `accounts-receivable` |
| valor_encargos_reembolsaveis | decimal (BRL) | não | `accounts-receivable` |
| percentual_taxa_adm | decimal (%) | sim | Contrato / `company-context.md` |
| valor_taxa_administracao | decimal (BRL) | sim | `owner-payouts` |
| valor_taxa_intermediacao | decimal (BRL) | não | `owner-payouts` |
| valor_retencao_irrf | decimal (BRL) | não | `owner-payouts` |
| numero_os | string | não | Manutenção |
| valor_reparos | decimal (BRL) | não | `accounts-payable` |
| valor_liquido_repasse | decimal (BRL) | sim | `owner-payouts` |
| banco_destino | string | sim | Cadastro bancário |
| agencia_destino | string | sim | Cadastro bancário |
| conta_destino | string | sim | Cadastro bancário |
| identificador_transferencia | string | não | Comprovante bancário |
| observacoes_extrato | text | não | Analista financeiro |
