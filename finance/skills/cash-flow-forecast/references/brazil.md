---
plugin: rt-finance
skill: cash-flow-forecast
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: CFO / Tesoureiro
---

# Projeção de Fluxo de Caixa Direto (13 Semanas) e Cenários

## Objetivo e gatilhos
Projetar entradas e saídas operacionais próprias da imobiliária em horizonte de 13 semanas com alertas de caixa mínimo.
- **Gatilhos:** acionar `rt-finance/cash-flow-forecast` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para demonstrativo de repasse de proprietários (`owner-payouts`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Saldo inicial caixa próprio, contas a receber projetadas, contas a pagar comprometidas, folha e tributos. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Separar rigorosamente saldo próprio de saldo fiduciário — Tesoureiro — Segunda-feira.
2. Projetar entradas semanais ponderadas — FP&A — Segunda-feira.
3. Projetar saídas e testar cenário conservador (-20% comissões) — FP&A — Terça-feira.
4. Acionar alerta vermelho se romper caixa mínimo — CFO — Terça-feira.

## Regras e critérios
Prática de mercado: Rolling forecast semanal de 13 semanas; caixa mínimo >= 3 meses de despesas fixas.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmula:** $\text{Caixa Final}_t = \text{Caixa Inicial}_t + \text{Entradas}_t - \text{Saídas}_t - \text{CapEx}_t$. Exemplo: $250k + 110k - 100k = \mathbf{260k}$.

## Saídas
Entregável padronizado da skill `cash-flow-forecast` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **CFO / Tesoureiro**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `cash-flow-forecast` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `cash-flow-forecast` sem dados obrigatórios (Saldo inicial caixa próprio) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do CFO / Tesoureiro ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
