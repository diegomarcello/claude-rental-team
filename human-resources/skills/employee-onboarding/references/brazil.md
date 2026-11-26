---
plugin: rt-human-resources
skill: employee-onboarding
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de RH / TI
---

# Admissão de Empregados e Credenciamento de Corretores Associados

## Objetivo e gatilhos
Conduzir onboarding documental, contratual e de acessos separando empregados subordinados de corretores autônomos/associados.
- **Gatilhos:** acionar `rt-human-resources/employee-onboarding` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para prestadores PJ de manutenção/obra (`rt-procurement/vendor-management`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Tipo de vínculo, documentos pessoais, registro profissional, cargo/equipe, matriz RBAC. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Coletar documentação legal conforme vínculo (CLT/W-2/CDI vs. Corretor Associado Lei 6.530/78 / IRC § 3508) — RH — Pré-início.
2. Provisionar acessos RBAC com MFA — TI — Dia 1.
3. Aplicar treinamento obrigatório de Compliance nos primeiros 7 dias — RH/Compliance — D+7.

## Regras e critérios
Norma: US IRC § 3508 statutory nonemployee criteria; BR Lei 6.530/78 art. 6º, §2º (contrato registrado sem subordinação de horário).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `employee-onboarding` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Gerente de RH / TI**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `employee-onboarding` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `employee-onboarding` sem dados obrigatórios (Tipo de vínculo) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Gerente de RH / TI ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
