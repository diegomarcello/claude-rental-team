---
template: lease-agreement-residential
approved_by: Advogado Imobiliário
---

# Contrato de Locação de Imóvel Residencial

**Contrato nº:** {{numero_contrato}}

## 1. Qualificação das Partes
- **LOCADOR(A):** {{nome_locador}}, {{nacionalidade_locador}}, {{estado_civil_locador}}, {{profissao_locador}}, inscrito(a) no CPF/CNPJ sob o nº {{documento_locador}}, residente/sediado(a) em {{endereco_locador}}, neste ato representado(a) por **{{nome_administradora}}**, CNPJ {{cnpj_administradora}}, CRECI {{creci_administradora}}.
- **LOCATÁRIO(A):** {{nome_locatario}}, {{nacionalidade_locatario}}, {{estado_civil_locatario}}, {{profissao_locatario}}, inscrito(a) no CPF sob o nº {{cpf_locatario}}, e-mail {{email_locatario}}.

## 2. Objeto e Finalidade
- **Imóvel:** {{endereco_completo_imovel}}, matrícula nº {{numero_matricula}} do {{cartorio_registro_imoveis}}.
- **Finalidade:** Exclusivamente residencial, sendo vedada a sublocação, cessão ou empréstimo sem prévia anuência escrita do LOCADOR.

## 3. Prazo da Locação
- **Prazo:** {{prazo_meses}} meses, iniciando-se em {{data_inicio}} e terminando em {{data_termino}}.
- **Multa Rescisória:** Equivalente a {{multa_rescisoria_alugueis}} aluguéis vigentes, calculada proporcionalmente ao tempo restante do contrato (Art. 4º da Lei nº 8.245/1991).

## 4. Aluguel, Encargos e Reajuste
- **Aluguel Mensal:** R$ {{valor_aluguel}} ({{valor_aluguel_extenso}}), com vencimento todo dia {{dia_vencimento}} de cada mês.
- **Reajuste:** Anual, pela variação acumulada do índice **{{indice_reajuste}}** (vedada deflação nominal).
- **Encargos:** Caberá ao LOCATÁRIO o pagamento pontual de condomínio ordinário, IPTU, consumo de água, energia elétrica, gás e seguro complementar contra incêndio.
- **Mora:** Multa moratória de {{percentual_multa_mora}}%, juros de mora de 1% ao mês pro rata die e correção monetária.

## 5. Garantia Locatícia
- **Modalidade Única (Art. 37, Lei 8.245/91):** {{modalidade_garantia}} — {{detalhes_garantia}}.

## 6. Vistoria e Conservação
- O estado de conservação do imóvel consta do **Termo de Vistoria Inicial** anexo, que integra este instrumento.

## 7. Proteção de Dados (LGPD) e Foro
- Os dados pessoais tratados destinam-se exclusivamente à execução deste contrato e cumprimento de obrigações legais/regulatórias (Lei nº 13.709/2018).
- **Foro:** Comarca de {{comarca_foro}}.

{{cidade_uf}}, {{data_assinatura}}.

______________________________________  
**LOCADOR(A) / ADMINISTRADORA**

______________________________________  
**LOCATÁRIO(A)**

______________________________________  
**GARANTIDOR(A) / TESTEMUNHAS**

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| numero_contrato | string | sim | Sistema / Jurídico |
| nome_locador | string | sim | Cadastro proprietário |
| nacionalidade_locador | string | sim | Cadastro proprietário |
| estado_civil_locador | string | sim | Cadastro proprietário |
| profissao_locador | string | sim | Cadastro proprietário |
| documento_locador | string | sim | Cadastro proprietário |
| endereco_locador | string | sim | Cadastro proprietário |
| nome_administradora | string | sim | `company-context.md` |
| cnpj_administradora | string | sim | `company-context.md` |
| creci_administradora | string | sim | `company-context.md` |
| nome_locatario | string | sim | `tenant-screening` |
| nacionalidade_locatario | string | sim | `tenant-screening` |
| estado_civil_locatario | string | sim | `tenant-screening` |
| profissao_locatario | string | sim | `tenant-screening` |
| cpf_locatario | string | sim | `tenant-screening` |
| email_locatario | string | sim | `tenant-screening` |
| endereco_completo_imovel | string | sim | Matrícula / Cadastro |
| numero_matricula | string | sim | `title-due-diligence` |
| cartorio_registro_imoveis | string | sim | `title-due-diligence` |
| prazo_meses | integer | sim | Negociação / `company-context.md` |
| data_inicio | date | sim | Negociação |
| data_termino | date | sim | Calculado |
| multa_rescisoria_alugueis | decimal | sim | `company-context.md` |
| valor_aluguel | decimal (BRL) | sim | Proposta aprovada |
| valor_aluguel_extenso | string | sim | Gerado |
| dia_vencimento | integer | sim | `company-context.md` |
| indice_reajuste | string | sim | `company-context.md` |
| percentual_multa_mora | decimal (%) | sim | `company-context.md` |
| modalidade_garantia | string | sim | `tenant-screening` |
| detalhes_garantia | string | sim | `tenant-screening` |
| comarca_foro | string | sim | Localização do imóvel |
| cidade_uf | string | sim | `company-context.md` |
| data_assinatura | date | sim | Jurídico |
