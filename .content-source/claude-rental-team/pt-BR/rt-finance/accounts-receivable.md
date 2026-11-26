---
plugin: rt-finance
skill: accounts-receivable
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador Financeiro
---

# Contas a Receber, Faturamento e Conciliação Bancária

## Objetivo e gatilhos
Gerar cobranças de aluguéis, encargos e comissões, processar arquivos de retorno bancário (CNAB 240/400, ACH/NACHA, SEPA CAMT.053), realizar baixa automática e conciliar saldos diários.
- **Gatilhos:** acionar `rt-finance/accounts-receivable` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para cobrança de inadimplentes (`collections`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Contratos ativos no ERP, encargos do mês, extratos/arquivos bancários. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Consolidar encargos variáveis do mês até D-10 — Analista AR — D-10.
2. Emitir boletos/faturas até D-7 — Sistema/AR — D-7.
3. Importar retornos bancários diariamente e conciliar conta vinculada (Trust/Escrow) — Analista AR — Diário.

## Regras e critérios
Norma: Segregação obrigatória entre conta de movimento próprio e conta fiduciária/de terceiros.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Aging de Recebíveis:** Corrente, 1–15d, 16–30d, 31–60d, 61–90d, > 90d.

## Saídas
Entregável padronizado da skill `accounts-receivable` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador Financeiro**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `accounts-receivable` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `accounts-receivable` sem dados obrigatórios (Contratos ativos no ERP) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador Financeiro ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
