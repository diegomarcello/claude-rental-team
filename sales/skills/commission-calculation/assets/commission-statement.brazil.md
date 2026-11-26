---
template: commission-statement
approved_by: Gerente Financeiro
---

# Demonstrativo de Rateio e Pagamento de Comissão

**Venda / Locação Ref.:** {{referencia_negocio}} | **Data:** {{data_fechamento}}  
**Imóvel:** {{endereco_imovel}}  
**Valor Base da Transação:** R$ {{valor_transacao}} | **Comissão Total ({{percentual_comissao}}%):** R$ {{valor_comissao_bruta}}

## Quadro de Rateio
| Beneficiário / Papel | Registro (CRECI) | Percentual (%) | Valor Bruto (BRL) | Retenções / Descontos | Valor Líquido (BRL) |
|---|---|---|---|---|---|
| Imobiliária ({{nome_administradora}}) | {{creci_administradora}} | {{pct_imobiliaria}}% | {{bruto_imobiliaria}} | {{desconto_imobiliaria}} | {{liquido_imobiliaria}} |
| Corretor Captador ({{nome_captador}}) | {{creci_captador}} | {{pct_captador}}% | {{bruto_captador}} | {{desconto_captador}} | {{liquido_captador}} |
| Corretor Vendedor ({{nome_vendedor}}) | {{creci_vendedor}} | {{pct_vendedor}}% | {{bruto_vendedor}} | {{desconto_vendedor}} | {{liquido_vendedor}} |

- **Condição de Liberação:** {{condicao_pagamento}} *(ex.: Compensação do sinal / Escritura)*

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| referencia_negocio | string | sim | Vendas |
| data_fechamento | date | sim | Vendas |
| endereco_imovel | string | sim | Cadastro imóvel |
| valor_transacao | decimal (BRL) | sim | Contrato |
| percentual_comissao | decimal (%) | sim | `commission-calculation` |
| valor_comissao_bruta | decimal (BRL) | sim | `commission-calculation` |
| nome_administradora | string | sim | `company-context.md` |
| creci_administradora | string | sim | `company-context.md` |
| pct_imobiliaria | decimal (%) | sim | `commission-calculation` |
| bruto_imobiliaria | decimal (BRL) | sim | `commission-calculation` |
| desconto_imobiliaria | decimal (BRL) | não | `commission-calculation` |
| liquido_imobiliaria | decimal (BRL) | sim | `commission-calculation` |
| nome_captador | string | sim | CRM |
| creci_captador | string | sim | RH / Cadastro |
| pct_captador | decimal (%) | sim | `commission-calculation` |
| bruto_captador | decimal (BRL) | sim | `commission-calculation` |
| desconto_captador | decimal (BRL) | não | `commission-calculation` |
| liquido_captador | decimal (BRL) | sim | `commission-calculation` |
| nome_vendedor | string | sim | CRM |
| creci_vendedor | string | sim | RH / Cadastro |
| pct_vendedor | decimal (%) | sim | `commission-calculation` |
| bruto_vendedor | decimal (BRL) | sim | `commission-calculation` |
| desconto_vendedor | decimal (BRL) | não | `commission-calculation` |
| liquido_vendedor | decimal (BRL) | sim | `commission-calculation` |
| condicao_pagamento | string | sim | `company-context.md` |
