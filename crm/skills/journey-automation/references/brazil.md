---
plugin: rt-crm
skill: journey-automation
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Especialista de Automação CRM
---

# Automação de Jornadas e Gatilhos de Ciclo de Vida

## Objetivo e gatilhos
Configurar fluxos automatizados no CRM para onboarding de proprietários/inquilinos, alertas de renovação, aniversários de contrato e reengajamento, sempre com trava de consentimento e saída.
- **Gatilhos:** acionar `rt-crm/journey-automation` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para cadência inicial de prospecção fria (`rt-pre-sales/follow-up-cadence`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Evento gatilho, canal, status de opt-in, critérios de saída. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Validar pré-condições de entrada (consentimento ativo + ausência de bloqueio jurídico) — RevOps — Setup.
2. Configurar ações e condições de saída imediata — Admin CRM — Setup.
3. Auditar taxas de entrega e descadastro semanalmente — RevOps — Semanal.

## Regras e critérios
Norma: Usar exclusivamente APIs oficiais aprovadas com templates pré-aprovados e mecanismo de saída.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `journey-automation` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Especialista de Automação CRM**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `journey-automation` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `journey-automation` sem dados obrigatórios (Evento gatilho) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Especialista de Automação CRM ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
