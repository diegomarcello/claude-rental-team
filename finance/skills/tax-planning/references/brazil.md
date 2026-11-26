---
plugin: rt-finance
skill: tax-planning
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Contador Tributarista / CPA
---

# Planejamento Tributário e Calendário de Obrigações Acessórias

## Objetivo e gatilhos
Comparar regimes tributários aplicáveis às linhas da empresa e controlar calendário de obrigações principais e acessórias.
- **Gatilhos:** acionar `rt-finance/tax-planning` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para cálculos genéricos de impostos por país (`rt-jurisdictions/*/taxes`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Faturamento por linha de negócio, margem operacional, folha de pagamento, estrutura societária atual. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Segregar receitas por natureza tributária — Contador/CPA — Trimestral.
2. Simular carga tributária comparativa antes da virada do exercício fiscal — Contador/CPA — Q4.
3. Manter calendário automatizado de obrigações com dupla conferência — Fiscal — Mensal.

## Regras e critérios
Norma: Respeitar propósito negocial e substância econômica entre SPEs/LLCs.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `tax-planning` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Contador Tributarista / CPA**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `tax-planning` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `tax-planning` sem dados obrigatórios (Faturamento por linha de negócio) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Contador Tributarista / CPA ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
