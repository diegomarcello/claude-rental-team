---
plugin: rt-crm
skill: crm-data-hygiene
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Administrador de CRM / DPO
---

# Higiene de Dados, Deduplicação e Retenção no CRM

## Objetivo e gatilhos
Manter integridade cadastral no CRM por meio de regras de validação na entrada, fusão de contatos/imóveis duplicados e expurgo/anonimização conforme prazos legais de retenção.
- **Gatilhos:** acionar `rt-crm/crm-data-hygiene` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para criar réguas de automação (`journey-automation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Base de contatos e imóveis do CRM, chaves únicas (e-mail, telefone E.164, CPF/SSN/NIF, matrícula/parcel ID), tabela de temporalidade. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Padronizar chaves únicas na entrada — RevOps — Automático.
2. Rodar rotina mensal de detecção e fusão de duplicidades preservando histórico — Admin CRM — Mensal.
3. Anonimizar leads inativos sem relação contratual após prazo da política de privacidade — DPO/Admin CRM — Trimestral.

## Regras e critérios
Norma: Princípio da qualidade/exatidão e limitação da conservação (LGPD art. 6º, V e art. 16; GDPR art. 5(1)(d)–(e)).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `crm-data-hygiene` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Administrador de CRM / DPO**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `crm-data-hygiene` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `crm-data-hygiene` sem dados obrigatórios (Base de contatos e imóveis do CRM) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Administrador de CRM / DPO ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
