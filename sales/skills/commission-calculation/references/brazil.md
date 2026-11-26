---
plugin: rt-sales
skill: commission-calculation
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Controller / Gerente Comercial
---

# Cálculo e Rateio de Comissões de Venda e Locação

## Objetivo e gatilhos
Calcular comissão bruta da imobiliária, descontos de impostos/taxas, rateio entre captação, venda/locação, gerência e parceiros externos, e definir o gatilho financeiro de pagamento.
- **Gatilhos:** acionar `rt-sales/commission-calculation` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para repasse de aluguel mensal de proprietários (`rt-finance/owner-payouts`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Valor fechado da transação, percentual de comissão acordado, tabela de rateio interna, parceiro externo (co-brokerage), impostos incidentes, status do recebimento financeiro. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Confirmar recebimento efetivo dos recursos na conta da imobiliária — Financeiro — Dia 0.
2. Deduzir eventual parceria externa (50/50 co-brokerage) e impostos diretos conforme regime — Controller — Dia 1.
3. Aplicar percentuais internos (Captação, Venda, Coordenação/Casa) e emitir demonstrativo individual — Controller — Dia 1.
4. Liberar pagamento mediante emissão de Nota Fiscal pelo corretor PJ/autônomo — Contas a Pagar — Dia 2.

## Regras e critérios
Norma: No Brasil, corretor associado sem vínculo empregatício rege-se pela Lei nº 6.530/78 (art. 6º, §§ 2º–4º). Nos EUA, pagar somente a entidades licenciadas ou agentes vinculados via 1099-NEC. Decisão da empresa: `[PENDENTE: Confirmar tabela oficial de rateio interno]`.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmula de Rateio Padrão:**
$$\text{Comissão Bruta} = \text{Valor Venda} \times \%\text{Comissão}$$
- **Exemplo numérico (Venda de R$ 1.000.000, comissão 6% = R$ 60.000; 30% Captação, 40% Venda, 30% Casa):**
  - Captador: **R$ 18.000,00** | Vendedor: **R$ 24.000,00** | Casa: **R$ 18.000,00**.

## Saídas
Entregável padronizado da skill `commission-calculation` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Controller / Gerente Comercial**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `commission-calculation` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `commission-calculation` sem dados obrigatórios (Valor fechado da transação) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Controller / Gerente Comercial ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
