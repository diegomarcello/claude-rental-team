---
template: image-release
approved_by: Advogado / Marketing
---

# Termo de Autorização de Uso de Imagem, Voz e Captação de Imóvel

Pelo presente instrumento, **{{nome_autorizante}}**, inscrito(a) no CPF sob o nº {{cpf_autorizante}}, na qualidade de {{qualidade_autorizante}} *(proprietário / morador / corretor / modelo)*, autoriza **{{nome_administradora}}**, CNPJ {{cnpj_administradora}}, a captar, editar e divulgar fotografias e vídeos do imóvel localizado em **{{endereco_imovel}}** (e/ou de sua imagem/voz, quando aplicável) para fins exclusivos de divulgação imobiliária em site institucional, portais imobiliários e redes sociais.

- **Vigência da Autorização:** {{prazo_autorizacao}} (gratuita e sem ônus).
- **Proteção de Dados e Privacidade:** Compromete-se a empresa a não expor objetos pessoais identificáveis, placas de veículos ou documentos sensíveis nas mídias publicadas (Lei nº 13.709/2018).

{{cidade_uf}}, {{data_assinatura}}.

______________________________________  
**AUTORIZANTE ({{nome_autorizante}})**

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| nome_autorizante | string | sim | Cadastro |
| cpf_autorizante | string | sim | Cadastro |
| qualidade_autorizante | string | sim | Marketing |
| nome_administradora | string | sim | `company-context.md` |
| cnpj_administradora | string | sim | `company-context.md` |
| endereco_imovel | string | sim | Cadastro imóvel |
| prazo_autorizacao | string | sim | Marketing |
| cidade_uf | string | sim | `company-context.md` |
| data_assinatura | date | sim | Marketing |
