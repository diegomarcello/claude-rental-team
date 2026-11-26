---
plugin: rt-executive
skill: company-kpis
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Controller / CFO
---

# Painel de KPIs Executivos (Venda, Locação, Obra e Caixa)

## Objetivo e gatilhos
Definir, calcular e auditar indicadores-chave de desempenho (KPIs) da operação imobiliária com fórmulas padronizadas, metas de referência e periodicidade.
- **Gatilhos:** acionar `rt-executive/company-kpis` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para projeção diária de tesouraria (`rt-finance/cash-flow-forecast`) nem para modelagem de esquema de banco de dados (`rt-technology-data/bi-reporting`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: VGV vendido, receita de comissões, carteira ativa de locação, vacância física/financeira, inadimplência (>30d), desvio de obra, saldo de caixa e OPEX. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Extrair dados fechados do ERP/CRM até o 3º dia útil — Controller — Mensal.
2. Calcular KPIs por unidade de negócio e comparar com meta e período anterior — FP&A — Dia 4.
3. Sinalizar desvios críticos (> 10% da meta) com plano de ação — Diretores — Dia 5.

## Regras e critérios
Prática de mercado (Benchmarks): Vacância física carteira < 5%; Inadimplência > 30 dias < 2,5%; Churn anual de proprietários < 12%; Conversão lead-to-visita > 15%; Desvio de orçamento de obra <= 5%. Decisão da empresa: `[PENDENTE: Definir metas oficiais por praça]`.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmulas Padronizadas (Arredondamento: 2 casas decimais):**
- $\text{Vacância Física (\%)} = \frac{\text{Unidades Vagas}}{\text{Total de Unidades sob Gestão}} \times 100$
- $\text{Inadimplência (\%)} = \frac{\text{Aluguéis Vencidos > 30d}}{\text{Faturamento Total de Aluguéis no Mês}} \times 100$
- $\text{Net Dollar Retention (Carteira)} = \frac{\text{Receita Taxa Adm}_{t} + \text{Expansão} - \text{Churn}}{\text{Receita Taxa Adm}_{t-1}} \times 100$
- **Exemplo numérico:** Carteira com 400 imóveis, 16 vagos; faturamento mensal de aluguéis = R$ 1.200.000 (ou $1,200,000), atrasos > 30d = R$ 24.000 ($24,000):
  - $\text{Vacância Física} = (16 / 400) \times 100 = \mathbf{4,00\%}$
  - $\text{Inadimplência} = (24.000 / 1.200.000) \times 100 = \mathbf{2,00\%}$.

## Saídas
Entregável padronizado da skill `company-kpis` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Controller / CFO**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `company-kpis` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `company-kpis` sem dados obrigatórios (VGV vendido) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Controller / CFO ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
