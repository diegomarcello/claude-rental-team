---
template: management-agreement
approved_by: Advogado Imobiliário
---

# Contrato de Prestação de Serviços de Administração Imobiliária

**Contrato de Administração nº:** {{numero_contrato_adm}}

## 1. Partes
- **PROPRIETÁRIO(A) / OUTORGANTE:** {{nome_proprietario}}, CPF/CNPJ {{documento_proprietario}}, residente/sediado(a) em {{endereco_proprietario}}, e-mail {{email_proprietario}}.
- **ADMINISTRADORA / OUTORGADA:** {{nome_administradora}}, CNPJ {{cnpj_administradora}}, CRECI Jurídico {{creci_administradora}}, com sede em {{endereco_administradora}}.

## 2. Objeto e Poderes
O(A) PROPRIETÁRIO(A) confere à ADMINISTRADORA poderes para administrar, divulgar, selecionar pretendentes, celebrar contratos de locação, receber aluguéis e encargos, emitir recibos, realizar vistorias e promover cobranças extrajudiciais do imóvel situado em **{{endereco_imovel}}** (Matrícula nº {{numero_matricula}}).

## 3. Remuneração da Administradora
- **Taxa de Intermediação (1º Aluguel):** {{percentual_taxa_intermediacao}}% sobre o primeiro aluguel pactuado.
- **Taxa de Administração Mensal:** {{percentual_taxa_administracao}}% sobre o valor bruto do aluguel efetivamente recebido.

## 4. Repasse e Prestação de Contas
- Os valores recebidos serão repassados em até **{{dias_uteis_repasse}} dias úteis** após a compensação bancária, deduzidas as taxas pactuadas, tributos retidos e despesas autorizadas, na conta bancária de titularidade do(a) PROPRIETÁRIO(A): Banco {{banco_proprietario}}, Ag. {{agencia_proprietario}}, Conta {{conta_proprietario}}.

## 5. Autorização para Reparos Emergenciais
- Fica a ADMINISTRADORA autorizada a executar reparos urgentes para preservação do imóvel até o limite de **R$ {{limite_reparo_emergencial}}**, mediante apresentação de notas fiscais e registro fotográfico.

## 6. Vigência e Rescisão
- Vigência por prazo indeterminado, podendo ser rescindido mediante aviso prévio escrito de 30 dias, ressalvados os direitos sobre contratos de locação em curso intermediados pela ADMINISTRADORA.

{{cidade_uf}}, {{data_assinatura}}.

______________________________________  
**PROPRIETÁRIO(A)**

______________________________________  
**ADMINISTRADORA**

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| numero_contrato_adm | string | sim | Sistema |
| nome_proprietario | string | sim | Cadastro proprietário |
| documento_proprietario | string | sim | Cadastro proprietário |
| endereco_proprietario | string | sim | Cadastro proprietário |
| email_proprietario | string | sim | Cadastro proprietário |
| nome_administradora | string | sim | `company-context.md` |
| cnpj_administradora | string | sim | `company-context.md` |
| creci_administradora | string | sim | `company-context.md` |
| endereco_administradora | string | sim | `company-context.md` |
| endereco_imovel | string | sim | Cadastro imóvel |
| numero_matricula | string | sim | Matrícula |
| percentual_taxa_intermediacao | decimal (%) | sim | `company-context.md` |
| percentual_taxa_administracao | decimal (%) | sim | `company-context.md` |
| dias_uteis_repasse | integer | sim | `company-context.md` |
| banco_proprietario | string | sim | Cadastro bancário |
| agencia_proprietario | string | sim | Cadastro bancário |
| conta_proprietario | string | sim | Cadastro bancário |
| limite_reparo_emergencial | decimal (BRL) | sim | `company-context.md` |
| cidade_uf | string | sim | `company-context.md` |
| data_assinatura | date | sim | Jurídico |
