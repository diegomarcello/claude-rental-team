---
template: move-out-agreement
approved_by: Advogado Imobiliário
---

# Termo de Distrato, Entrega de Chaves e Acordo de Desocupação

**Contrato Rescindido nº:** {{numero_contrato}}  
**Imóvel:** {{endereco_imovel}}

## 1. Partes
- **LOCADOR(A):** {{nome_locador}}, representado(a) por {{nome_administradora}}.
- **LOCATÁRIO(A):** {{nome_locatario}}, CPF/CNPJ {{documento_locatario}}.

## 2. Entrega das Chaves e Vistoria Final
As partes formalizam, nesta data ({{data_entrega_chaves}}), a devolução das chaves e da posse direta do imóvel acima descrito, conforme **Laudo de Vistoria de Saída** realizado em {{data_vistoria_saida}}.

## 3. Acerto Financeiro Final
| Item | Valor (BRL) | Observação |
|---|---|---|
| Aluguel proporcional ({{dias_proporcionais}} dias) | {{valor_aluguel_proporcional}} | Até {{data_entrega_chaves}} |
| Multa rescisória proporcional (Art. 4º, Lei 8.245/91) | {{valor_multa_rescisoria}} | {{observacao_multa}} |
| Reparos apontados na vistoria de saída | {{valor_reparos_saida}} | Conforme orçamento anexo |
| Encargos pendentes (IPTU / Condomínio / Consumo) | {{valor_encargos_pendentes}} | Comprovantes anexos |
| **Saldo Total a Pagar pelo(a) LOCATÁRIO(A)** | **{{valor_total_acordo}}** | Vencimento em {{data_vencimento_acordo}} |

## 4. Quitação Condicionada
A quitação plena das obrigações locatícias fica condicionada à efetiva compensação do valor acordado no item 3 e à apresentação dos comprovantes finais de desligamento de água, luz e gás.

{{cidade_uf}}, {{data_entrega_chaves}}.

______________________________________  
**LOCADOR(A) / ADMINISTRADORA**

______________________________________  
**LOCATÁRIO(A)**

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| numero_contrato | string | sim | Contrato |
| endereco_imovel | string | sim | Cadastro imóvel |
| nome_locador | string | sim | Cadastro proprietário |
| nome_administradora | string | sim | `company-context.md` |
| nome_locatario | string | sim | Contrato |
| documento_locatario | string | sim | Contrato |
| data_entrega_chaves | date | sim | `move-inspections` |
| data_vistoria_saida | date | sim | `move-inspections` |
| dias_proporcionais | integer | sim | `lease-administration` |
| valor_aluguel_proporcional | decimal (BRL) | sim | `lease-administration` |
| valor_multa_rescisoria | decimal (BRL) | sim | `lease-administration` |
| observacao_multa | string | não | Jurídico |
| valor_reparos_saida | decimal (BRL) | sim | `move-inspections` |
| valor_encargos_pendentes | decimal (BRL) | sim | `accounts-receivable` |
| valor_total_acordo | decimal (BRL) | sim | Calculado |
| data_vencimento_acordo | date | sim | Jurídico / Financeiro |
| cidade_uf | string | sim | `company-context.md` |
