---
plugin: rt-human-resources
skill: performance-compensation
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de RH / Jurídico Trabalhista
---

# Metas, Remuneração Variável e Conformidade Trabalhista

## Objetivo e gatilhos
Estruturar planos de metas, comissões e bônus garantindo clareza de regras e conformidade trabalhista/previdenciária.
- **Gatilhos:** acionar `rt-human-resources/performance-compensation` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para cálculo individual de rateio de uma venda (`rt-sales/commission-calculation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Cargo/função, regime de contratação, indicadores elegíveis, periodicidade, regras de desligamento. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Formalizar política escrita de remuneração variável antes do ciclo — RH/Diretoria — Pré-ciclo.
2. Garantir conformidade trabalhista de reflexos (CLT/W-2) vs. remuneração por resultado (associados) — RH/Jurídico — Revisão.
3. Definir regra objetiva de pipeline tail no desligamento — Jurídico — Política.

## Regras e critérios
Norma: Proibido estornar comissão após conclusão útil do negócio sem culpa do corretor (BR CC art. 725; US state wage/procuring-cause laws).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `performance-compensation` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Gerente de RH / Jurídico Trabalhista**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `performance-compensation` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `performance-compensation` sem dados obrigatórios (Cargo/função) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Gerente de RH / Jurídico Trabalhista ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
