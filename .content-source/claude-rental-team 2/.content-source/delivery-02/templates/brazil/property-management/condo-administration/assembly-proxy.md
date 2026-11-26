---
template: assembly-proxy
approved_by: Advogado Imobiliário
---

# Procuração para Representação em Assembleia Condominial

**OUTORGANTE:** {{nome_outorgante}}, inscrito(a) no CPF/CNPJ sob o nº {{documento_outorgante}}, proprietário(a) da unidade **{{identificacao_unidade}}** do **{{nome_condominio}}**, localizado em {{endereco_condominio}}.

**OUTORGADO(A):** {{nome_outorgado}}, inscrito(a) no CPF sob o nº {{cpf_outorgado}}.

**PODERES:** Pelo presente instrumento particular, o(a) OUTORGANTE nomeia e constitui seu(sua) bastante procurador(a) o(a) OUTORGADO(A) para representá-lo(a) na Assembleia Geral {{tipo_assembleia}} *(Ordinária / Extraordinária)* do referido condomínio, a realizar-se no dia **{{data_assembleia}}**, às {{hora_assembleia}}, podendo comparecer, assinar lista de presença, discutir matérias da ordem do dia, votar e aprovar ou rejeitar deliberações, inclusive aprovação de contas, previsão orçamentária e eleição de síndico, vedado o substabelecimento.

{{cidade_uf}}, {{data_emissao}}.

______________________________________  
**OUTORGANTE ({{nome_outorgante}})**  
*(Observação: Verificar na Convenção do Condomínio a exigência de firma reconhecida ou limite de procurações por mandatário.)*

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| nome_outorgante | string | sim | Cadastro proprietário |
| documento_outorgante | string | sim | Cadastro proprietário |
| identificacao_unidade | string | sim | Cadastro imóvel |
| nome_condominio | string | sim | Cadastro condomínio |
| endereco_condominio | string | sim | Cadastro condomínio |
| nome_outorgado | string | sim | Usuário / Mandatário |
| cpf_outorgado | string | sim | Usuário / Mandatário |
| tipo_assembleia | enum (ORDINARIA\|EXTRAORDINARIA) | sim | Edital |
| data_assembleia | date | sim | Edital |
| hora_assembleia | string | sim | Edital |
| cidade_uf | string | sim | `company-context.md` |
| data_emissao | date | sim | Data de geração |
