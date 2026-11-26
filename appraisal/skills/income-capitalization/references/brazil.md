---
plugin: rt-appraisal
skill: income-capitalization
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Avaliador Habilitado / Analista de Investimentos
---

# Avaliação pelo Método da Capitalização da Renda (Cap Rate e DCF)

## Objetivo e gatilhos
Avaliar imóveis comerciais, multifamiliares e carteiras de locação pela capitalização direta do NOI (Net Operating Income) ou Fluxo de Caixa Descontado (DCF).
- **Gatilhos:** acionar `rt-appraisal/income-capitalization` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para residências unifamiliares ocupadas pelo proprietário onde o mercado se guia por comparáveis de venda (`comparative-market-analysis`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Receita bruta potencial (PGI), taxa de vacância e inadimplência, despesas operacionais do proprietário (OPEX: IPTU/tax, seguro, manutenção, taxa adm, fundo reposição), Cap Rate de mercado ou taxa de desconto + Cap Rate de saída. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Apurar Receita Bruta Potencial (PGI) com base em contratos vigentes e aluguel de mercado — Analista — Dia 1.
2. Deduzir vacância/perdas de crédito para obter Receita Efetiva (EGI) e subtrair OPEX para apurar o NOI — Analista — Dia 1.
3. Aplicar Direct Cap ($V = NOI / R$) e/ou DCF de 5–10 anos com valor terminal — Avaliador — Dia 2.
4. Montar matriz de sensibilidade (Cap Rate +/- 50 bps vs. NOI +/- 5%) — Avaliador — Dia 2.

## Regras e critérios
Norma: NBR 14653-2 (Método da Renda), USPAP SR 1-4(c), RICS Red Book / IVS 105. Regra crítica: Nunca incluir serviço da dívida (juros/amortização) nem imposto de renda do proprietário dentro do OPEX para cálculo de NOI.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmulas de Capitalização da Renda:**
$$EGI = PGI \times (1 - v) + \text{Outras Receitas}$$
$$NOI = EGI - OPEX_{\text{proprietário}}$$
$$\text{Valor pelo Direct Cap} = \frac{NOI}{\text{Cap Rate}}$$
- **Exemplo numérico (Edifício Comercial):**
  - PGI anual = $240,000 | Vacância/inadimplência (5%) = -$12,000 -> EGI = **$228,000**
  - OPEX proprietário (Property Tax $22k + Seguro $6k + Manutenção/Adm $20k) = **$48,000**
  - $NOI = 228.000 - 48.000 = \mathbf{\$180,000/\text{ano}}$
  - Com Cap Rate de mercado = **7,50%**: $\text{Valor} = \frac{180.000}{0,075} = \mathbf{\$2.400.000,00}$.

## Saídas
Entregável padronizado da skill `income-capitalization` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Avaliador Habilitado / Analista de Investimentos**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `income-capitalization` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `income-capitalization` sem dados obrigatórios (Receita bruta potencial (PGI)) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Avaliador Habilitado / Analista de Investimentos ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
