---
plugin: rt-acquisitions
skill: deal-feasibility
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Diretor de Aquisições / CFO
---

# Estudo de Viabilidade Econômico-Financeira (ROI, TIR, VPL)

## Objetivo e gatilhos
Modelar fluxo de caixa completo de aquisição, impostos de entrada, custo de posse (carry), reforma, comercialização, impostos de saída e indicadores de retorno (Margem, ROI, TIR, VPL) em cenários base, otimista e estressado.
- **Gatilhos:** acionar `rt-acquisitions/deal-feasibility` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para avaliação mercadológica isolada sem fluxo de caixa de projeto (`rt-appraisal/comparative-market-analysis`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Preço de compra, custos de transferência/registro, orçamento de obra + contingência, prazo de obra e venda (meses), custos mensais de posse (IPTU/Property Tax, condomínio/HOA, seguro, financiamento), ARV (valor de revenda), comissão e impostos de saída, TMA (taxa mínima de atratividade). | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Consolidar premissas de entrada (ARV validado por CMA + orçamento de obra + certidões) — Analista de Aquisições — Dia 1.
2. Construir fluxo de caixa mensal e calcular ROI, TIR mensal/anual e VPL — Analista — Dia 2.
3. Rodar análise de sensibilidade (-10% ARV, +15% obra, +3 meses prazo de venda) — Analista — Dia 2.
4. Submeter ao Comitê de Investimentos para aprovação de oferta — Diretor de Aquisições — Dia 3.

## Regras e critérios
Prática de mercado: Incluir contingência mínima de 10%–15% no orçamento de obra; testar cenário de estresse onde venda atrasa 90 dias e preço cai 5%–10%. Decisão da empresa: `[PENDENTE: Definir TIR mínima (hurdle rate) e margem líquida mínima por linha]`.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmulas Financeiras (Arredondamento: 2 casas decimais):**
- $\text{Custo Total Projeto} = \text{Compra} + \text{Impostos/Registro Entrada} + \text{Obra (c/ Contingência)} + \text{Carry Total} + \text{Comissão/Impostos Saída}$
- $\text{Lucro Líquido} = \text{ARV} - \text{Custo Total Projeto}$
- $\text{ROI Simples (\%)} = \frac{\text{Lucro Líquido}}{\text{Capital Investido}} \times 100$
- $\text{VPL (NPV)} = \sum_{t=0}^{n} \frac{FC_t}{(1 + i)^t}$ e $\text{TIR Anual} = (1 + \text{TIR}_{\text{mensal}})^{12} - 1$
- **Exemplo numérico (Flipping 8 meses, sem alavancagem):**
  - Compra: R$ 500.000 ($500k) | Entrada (ITBI/Registro 4%): R$ 20.000 ($20k) | Obra: R$ 110.000 ($110k) | Carry (8m x R$ 2.500): R$ 20.000 ($20k) | Saída (Comissão 6% + Imposto 6% sobre R$ 800k ARV): R$ 96.000 ($96k).
  - $\text{Custo Total} = 500k + 20k + 110k + 20k + 96k = \mathbf{R\$ 746.000}$ ($746k).
  - $\text{Lucro Líquido} = 800k - 746k = \mathbf{R\$ 54.000}$ ($54k) | $\text{ROI sobre custo caixa (650k)} = \mathbf{8,31\%}$ em 8 meses (~**12,72% a.a.**).

## Saídas
Entregável padronizado da skill `deal-feasibility` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Diretor de Aquisições / CFO**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `deal-feasibility` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `deal-feasibility` sem dados obrigatórios (Preço de compra) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Diretor de Aquisições / CFO ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
