---
plugin: rt-executive
skill: strategic-planning
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Diretoria Executiva / CFO
---

# Planejamento Estratégico e Alocação de Capital

## Objetivo e gatilhos
Estruturar ciclos de planejamento anual/trimestral (OKRs), alocação de capital entre carteira de locação, intermediação e flipping/incorporação, e avaliação de expansão geográfica.
- **Gatilhos:** acionar `rt-executive/strategic-planning` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para apuração mensal de indicadores operacionais (usar `company-kpis`) nem para aprovação de um imóvel específico (`rt-acquisitions/deal-feasibility`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Metas anuais, caixa disponível, custo de capital (WACC/Selic/Fed Funds/ECB), margem por linha de negócio, capacidade operacional da equipe. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Consolidar histórico financeiro e operacional (12M) — CFO — Semana 1.
2. Definir metas de receita recorrente (locação) vs. transacional (venda/flip) — CEO/Diretoria — Semana 2.
3. Estabelecer limites de exposição de capital próprio por projeto e praça — Comitê de Investimentos — Semana 3.
4. Desdobrar OKRs departamentais e revisar trimestralmente — Diretores — Trimestral.

## Regras e critérios
Norma: Segregação patrimonial entre caixa operacional de terceiros (aluguéis/cauções) e capital de giro próprio. Prática de mercado: Manter reserva de liquidez >= 6 meses de OPEX fixo; limitar exposição máxima em um único ativo de flipping a 20% do patrimônio líquido. Decisão da empresa: `[PENDENTE: Definir meta de mix de receita e retorno mínimo sobre capital próprio (ROE)]`.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável (planejamento qualitativo e alocação de portfólio; cálculos de retorno em `deal-feasibility`).

## Saídas
Entregável padronizado da skill `strategic-planning` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Diretoria Executiva / CFO**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `strategic-planning` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `strategic-planning` sem dados obrigatórios (Metas anuais) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Diretoria Executiva / CFO ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
