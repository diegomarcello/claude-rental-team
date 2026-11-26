---
template: lease-agreement-commercial
approved_by: Advogado Imobiliário
---

# Contrato de Locação de Imóvel Não Residencial (Comercial)

**Contrato nº:** {{numero_contrato}}

## 1. Qualificação das Partes
- **LOCADOR(A):** {{nome_locador}}, inscrito(a) no CPF/CNPJ sob o nº {{documento_locador}}, com endereço em {{endereco_locador}}, representado(a) por **{{nome_administradora}}**, CNPJ {{cnpj_administradora}}.
- **LOCATÁRIA:** {{razao_social_locataria}}, pessoa jurídica inscrita no CNPJ sob o nº {{cnpj_locataria}}, com sede em {{endereco_locataria}}, neste ato representada por {{nome_representante_legal}}, CPF {{cpf_representante_legal}}.

## 2. Objeto e Destinação Comercial
- **Imóvel:** {{endereco_completo_imovel}}, matrícula nº {{numero_matricula}}.
- **Atividade Autorizada:** {{atividade_comercial_autorizada}} (CNAE {{cnae_principal}}).
- **Licenças e Alvarás:** Correrão por conta exclusiva da LOCATÁRIA a obtenção e manutenção de Alvará de Funcionamento, AVCB/CLCB e licenças sanitárias ou ambientais.

## 3. Prazo e Direito à Ação Renovatória
- **Prazo:** {{prazo_meses}} meses, de {{data_inicio}} a {{data_termino}}.
- **Observação Legal:** Contratos celebrados por escrito com prazo determinado igual ou superior a 60 meses asseguram à LOCATÁRIA o direito à ação renovatória, preenchidos os requisitos do Art. 51 da Lei nº 8.245/1991.

## 4. Aluguel, Retenção de IRRF e Reajuste
- **Aluguel Mensal Bruto:** R$ {{valor_aluguel_bruto}}, vencível todo dia {{dia_vencimento}}.
- **Retenção Tributária:** Sendo o LOCADOR Pessoa Física, a LOCATÁRIA efetuará a retenção e o recolhimento do IRRF na fonte na forma da legislação tributária vigente, enviando o comprovante à ADMINISTRADORA.
- **Reajuste:** Anual pelo índice **{{indice_reajuste}}**.

## 5. Garantia Locatícia
- **Modalidade Única:** {{modalidade_garantia}} — {{detalhes_garantia}}.

## 6. Benfeitorias e Devolução
- Benfeitorias voluptuárias e úteis dependem de prévia autorização escrita do LOCADOR e não serão indenizáveis nem passíveis de retenção, salvo pactuação expressa em contrário (Art. 35, Lei 8.245/91).

{{cidade_uf}}, {{data_assinatura}}.

______________________________________  
**LOCADOR(A) / ADMINISTRADORA**

______________________________________  
**LOCATÁRIA**

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| numero_contrato | string | sim | Sistema / Jurídico |
| nome_locador | string | sim | Cadastro proprietário |
| documento_locador | string | sim | Cadastro proprietário |
| endereco_locador | string | sim | Cadastro proprietário |
| nome_administradora | string | sim | `company-context.md` |
| cnpj_administradora | string | sim | `company-context.md` |
| razao_social_locataria | string | sim | `tenant-screening` |
| cnpj_locataria | string | sim | `tenant-screening` |
| endereco_locataria | string | sim | `tenant-screening` |
| nome_representante_legal | string | sim | Contrato social |
| cpf_representante_legal | string | sim | Documento representante |
| endereco_completo_imovel | string | sim | Matrícula / Cadastro |
| numero_matricula | string | sim | `title-due-diligence` |
| atividade_comercial_autorizada | string | sim | Proposta comercial |
| cnae_principal | string | sim | Cartão CNPJ |
| prazo_meses | integer | sim | Negociação |
| data_inicio | date | sim | Negociação |
| data_termino | date | sim | Calculado |
| valor_aluguel_bruto | decimal (BRL) | sim | Proposta aprovada |
| dia_vencimento | integer | sim | `company-context.md` |
| indice_reajuste | string | sim | `company-context.md` |
| modalidade_garantia | string | sim | `tenant-screening` |
| detalhes_garantia | string | sim | `tenant-screening` |
| cidade_uf | string | sim | `company-context.md` |
| data_assinatura | date | sim | Jurídico |
