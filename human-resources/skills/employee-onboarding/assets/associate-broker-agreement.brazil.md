---
template: associate-broker-agreement
approved_by: Advogado Trabalhista / Imobiliário
---

# Contrato de Associação de Corretor de Imóveis (Lei nº 6.530/1978, Art. 6º, §§ 2º a 4º)

## 1. Partes
- **IMOBILIÁRIA:** {{nome_administradora}}, CNPJ {{cnpj_administradora}}, CRECI Jurídico {{creci_administradora}}, com sede em {{endereco_administradora}}.
- **CORRETOR(A) ASSOCIADO(A):** {{nome_corretor}}, CPF {{cpf_corretor}}, inscrito(a) no CRECI/{{uf_creci}} sob o nº {{numero_creci}}, residente em {{endereco_corretor}}.

## 2. Objeto e Natureza Jurídica
O presente instrumento regula a associação autônoma entre as partes para atuação conjunta na intermediação imobiliária, sem vínculo empregatício, subordinação jurídica, controle de jornada ou exclusividade obrigatória, nos estritos termos dos §§ 2º a 4º do Art. 6º da Lei nº 6.530/1978 (incluídos pela Lei nº 13.097/2015).

## 3. Rateio de Honorários e Tributação
- Os honorários decorrentes das intermediações realizadas em conjunto serão partilhados conforme a tabela de rateio vigente da IMOBILIÁRIA ({{resumo_tabela_rateio}}), mediante emissão de documento fiscal hábil pelo(a) CORRETOR(A) ASSOCIADO(A) ou retenção tributária legal aplicável.

## 4. Confidencialidade, LGPD e Uso de Sistemas
- O(A) CORRETOR(A) ASSOCIADO(A) obriga-se a tratar os dados de clientes e proprietários obtidos nos sistemas da IMOBILIÁRIA exclusivamente para fins de intermediação autorizada, observando a Lei nº 13.709/2018 (LGPD).

## 5. Registro Sindical
- Este contrato deverá ser devidamente registrado no Sindicato dos Corretores de Imóveis da respectiva base territorial, nos termos do Art. 6º, § 2º da Lei nº 6.530/1978.

{{cidade_uf}}, {{data_assinatura}}.

______________________________________  
**IMOBILIÁRIA**

______________________________________  
**CORRETOR(A) ASSOCIADO(A)**

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| nome_administradora | string | sim | `company-context.md` |
| cnpj_administradora | string | sim | `company-context.md` |
| creci_administradora | string | sim | `company-context.md` |
| endereco_administradora | string | sim | `company-context.md` |
| nome_corretor | string | sim | RH / Onboarding |
| cpf_corretor | string | sim | RH / Onboarding |
| uf_creci | string | sim | RH / Onboarding |
| numero_creci | string | sim | RH / Onboarding |
| endereco_corretor | string | sim | RH / Onboarding |
| resumo_tabela_rateio | string | sim | `company-context.md` |
| cidade_uf | string | sim | `company-context.md` |
| data_assinatura | date | sim | RH / Jurídico |
