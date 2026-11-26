---
plugin: rt-technology-data
skill: bi-reporting
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro de Dados / Controller
---

# Modelo de Dados Analítico e Painéis de BI

## Objetivo e gatilhos
Estruturar modelo dimensional unificando CRM, ERP financeiro e obras para painéis executivos com Row-Level Security.
- **Gatilhos:** acionar `rt-technology-data/bi-reporting` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para definir fórmulas de negócio dos KPIs (`rt-executive/company-kpis`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Fontes de dados integradas, dicionário de KPIs, perfis de acesso RBAC/RLS. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Modelar tabelas dimensão e fato com mascaramento de PII — Engenheiro de Dados — Setup.
2. Reconciliar números com razão contábil do ERP antes de publicar — Controller/Dados — Homologação.
3. Aplicar Row-Level Security (RLS) por carteira/cargo — BI/Segurança — Produção.

## Regras e critérios
Norma: Minimização e pseudonimização em ambientes analíticos (LGPD art. 13; GDPR art. 89).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `bi-reporting` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Engenheiro de Dados / Controller**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `bi-reporting` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `bi-reporting` sem dados obrigatórios (Fontes de dados integradas) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Engenheiro de Dados / Controller ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
