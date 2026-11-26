---
plugin: rt-executive
skill: approval-gates
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: CFO / Diretor de Compliance
---

# Matriz de Alçadas e Segregação de Funções

## Objetivo e gatilhos
Estabelecer limites financeiros, aprovadores obrigatórios, evidências documentais e segregação de funções (quem solicita não aprova nem paga).
- **Gatilhos:** acionar `rt-executive/approval-gates` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para conferência operacional de boletos (`rt-finance/accounts-payable`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Tipo de ato (compra, desconto, pagamento, contrato, acordo), valor envolvido, centro de custo, cargo do solicitante. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Classificar natureza e valor total da obrigação (considerando valor global do contrato, não parcela isolada) — Solicitante — Início.
2. Verificar alçada na matriz corporativa e anexar dossiê mínimo obrigatório — Sistema/Analista — Pré-aprovação.
3. Coletar aprovação formal com trilha auditável (ERP/assinatura digital) — Aprovador Designado — SLA 24–48h.
4. Executar pagamento ou assinatura por agente distinto do aprovador — Financeiro/Jurídico — Execução.

## Regras e critérios
Norma / Governança (COSO / SOX princípios): Segregação estrita entre (1) iniciação/cotação, (2) aprovação de mérito, (3) cadastro bancário de fornecedor e (4) liberação de pagamento. Proibido fracionar compras para fugir de alçada. Decisão da empresa: `[PENDENTE: Preencher valores exatos das faixas de alçada na Seção 1]`.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável (matriz de governança e limites).

## Saídas
Entregável padronizado da skill `approval-gates` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **CFO / Diretor de Compliance**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `approval-gates` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `approval-gates` sem dados obrigatórios (Tipo de ato (compra) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do CFO / Diretor de Compliance ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
