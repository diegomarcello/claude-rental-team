---
plugin: rt-finance
skill: owner-payouts
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador Financeiro / Contador
---

# Prestação de Contas e Repasse Mensal aos Proprietários

## Objetivo e gatilhos
Calcular o repasse líquido mensal ao proprietário, emitir extrato detalhado e gerar dados fiscais anuais (DIMOB / 1099-MISC).
- **Gatilhos:** acionar `rt-finance/owner-payouts` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para comissões de corretores (`rt-sales/commission-calculation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Aluguel recebido no mês, taxa de administração (%), notas fiscais de reparos autorizados, perfil fiscal do proprietário, dados bancários. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Conferir compensação bancária do pagamento do inquilino — Financeiro — D+1.
2. Deduzir taxa de administração, reparos com NF e retenções fiscais — Financeiro — D+2.
3. Emitir extrato analítico e transferir líquido dentro do SLA — Financeiro — D+3 a D+5.
4. Alimentar informe anual (DIMOB / Form 1099-MISC) — Contabilidade — Anual.

## Regras e critérios
Norma: Dever fiduciário de prestação de contas documentada (BR CC art. 668; US Trust Rules; FR Loi Hoguet).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmula:** $\text{Repasse} = \text{Aluguel} - \text{Taxa Adm} - \text{Retenções} - \text{Reparos}$. Exemplo: $5.000 - 500 - 350 = \mathbf{4.150,00}$.

## Saídas
Entregável padronizado da skill `owner-payouts` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador Financeiro / Contador**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `owner-payouts` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `owner-payouts` sem dados obrigatórios (Aluguel recebido no mês) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador Financeiro / Contador ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
