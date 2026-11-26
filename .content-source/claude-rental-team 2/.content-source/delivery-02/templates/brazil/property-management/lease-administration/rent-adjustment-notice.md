---
template: rent-adjustment-notice
approved_by: Coordenador de Locação
---

# Notificação de Reajuste Anual de Aluguel

**Local e Data:** {{cidade_uf}}, {{data_emissao}}

**Ao(À) Sr.(a) Locatário(a):** {{nome_locatario}}  
**Imóvel Locado:** {{endereco_imovel}}  
**Contrato nº:** {{numero_contrato}} (Início em {{data_inicio_contrato}})

Prezado(a) Locatário(a),

Em cumprimento ao disposto na Cláusula {{clausula_reajuste}} do Contrato de Locação firmado em {{data_inicio_contrato}}, bem como nos termos da Lei nº 8.245/1991, comunicamos que o valor mensal do aluguel sofrerá reajuste anual pelo índice **{{indice_reajuste}}**, acumulado nos últimos 12 meses ({{periodo_apuracao_indice}}), no percentual de **{{percentual_reajuste}}%**.

## Demonstrativo do Novo Valor
- **Valor Anterior do Aluguel:** R$ {{valor_aluguel_anterior}}
- **Índice Aplicado ({{indice_reajuste}}):** {{percentual_reajuste}}%
- **Novo Valor do Aluguel:** **R$ {{valor_aluguel_reajustado}}**
- **Vigência do Novo Valor:** A partir de {{data_vigencia_reajuste}} (com vencimento em {{data_primeiro_vencimento}})

Os demais encargos locatícios (condomínio, IPTU, seguro incêndio e taxas) permanecem regidos pelas condições contratuais vigentes.

Permanecemos à disposição para quaisquer esclarecimentos.

Atenciosamente,

**{{nome_administradora}}**  
Administração de Locações — {{telefone_contato}} | {{email_contato}}

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| cidade_uf | string | sim | `company-context.md` |
| data_emissao | date | sim | Data de geração |
| nome_locatario | string | sim | Contrato de locação |
| endereco_imovel | string | sim | Cadastro do imóvel |
| numero_contrato | string | sim | Contrato de locação |
| data_inicio_contrato | date | sim | Contrato de locação |
| clausula_reajuste | string | sim | Contrato de locação |
| indice_reajuste | string | sim | `lease-administration` |
| periodo_apuracao_indice | string | sim | `lease-administration` |
| percentual_reajuste | decimal (%) | sim | `lease-administration` |
| valor_aluguel_anterior | decimal (BRL) | sim | `lease-administration` |
| valor_aluguel_reajustado | decimal (BRL) | sim | `lease-administration` |
| data_vigencia_reajuste | date | sim | `lease-administration` |
| data_primeiro_vencimento | date | sim | Financeiro |
| nome_administradora | string | sim | `company-context.md` |
| telefone_contato | string | sim | `company-context.md` |
| email_contato | string | sim | `company-context.md` |
