---
template: registry-risk-opinion
approved_by: Advogado Imobiliário
---

# Parecer Jurídico de Análise Registral e Risco Imobiliário

**Protocolo:** {{protocolo_analise}} | **Data:** {{data_parecer}}  
**Imóvel:** {{endereco_imovel}}  
**Matrícula nº:** {{numero_matricula}} — **Cartório:** {{cartorio_ri}}  
**Proprietário(s) Registral(is):** {{proprietarios_registrais}}

## 1. Classificação Geral de Risco
- **Semáforo Jurídico:** `{{classificacao_risco}}` *(VERDE: Apto | AMARELO: Apto com ressalvas/saneamento | VERMELHO: Inapto / Alto risco)*

## 2. Quadro de Gravames, Ônus e Ações
| Análise | Status | Detalhamento / Averbação |
|---|---|---|
| Cadeia Dominial (20 anos) | {{status_cadeia_dominial}} | {{detalhe_cadeia_dominial}} |
| Hipoteca / Alienação Fiduciária | {{status_onus_reais}} | {{detalhe_onus_reais}} |
| Penhoras / Indisponibilidades (CNIB) | {{status_penhoras}} | {{detalhe_penhoras}} |
| Certidões Cíveis, Trabalhistas e Fiscais | {{status_certidoes}} | {{detalhe_certidoes}} |
| Regularidade Fiscal (IPTU / Condomínio) | {{status_debitos_imovel}} | {{detalhe_debitos_imovel}} |

## 3. Conclusão e Providências Recomendadas
{{conclusao_e_condicionantes}}

**Responsável Técnico:** {{nome_advogado}} — OAB/{{uf_oab}} {{numero_oab}}

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| protocolo_analise | string | sim | Jurídico |
| data_parecer | date | sim | Jurídico |
| endereco_imovel | string | sim | Cadastro imóvel |
| numero_matricula | string | sim | Certidão de matrícula |
| cartorio_ri | string | sim | Certidão de matrícula |
| proprietarios_registrais | string | sim | Certidão de matrícula |
| classificacao_risco | enum (VERDE\|AMARELO\|VERMELHO) | sim | `title-due-diligence` |
| status_cadeia_dominial | string | sim | `title-due-diligence` |
| detalhe_cadeia_dominial | text | sim | `title-due-diligence` |
| status_onus_reais | string | sim | `title-due-diligence` |
| detalhe_onus_reais | text | sim | `title-due-diligence` |
| status_penhoras | string | sim | `title-due-diligence` |
| detalhe_penhoras | text | sim | `title-due-diligence` |
| status_certidoes | string | sim | `title-due-diligence` |
| detalhe_certidoes | text | sim | `title-due-diligence` |
| status_debitos_imovel | string | sim | `title-due-diligence` |
| detalhe_debitos_imovel | text | sim | `title-due-diligence` |
| conclusao_e_condicionantes | text | sim | `title-due-diligence` |
| nome_advogado | string | sim | Jurídico |
| uf_oab | string | sim | Jurídico |
| numero_oab | string | sim | Jurídico |
