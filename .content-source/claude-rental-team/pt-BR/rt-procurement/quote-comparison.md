---
plugin: rt-procurement
skill: quote-comparison
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Compras / Orçamentista
---

# Mapa Comparativo e Equalização de Cotações

## Objetivo e gatilhos
Equalizar propostas de empreiteiros e fornecedores normalizando escopos divergentes, itens omissos, prazos e condições de pagamento.
- **Gatilhos:** acionar `rt-procurement/quote-comparison` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para elaborar o orçamento interno inicial (`rt-renovation/renovation-budget`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Memorial descritivo padrão, mínimo de 3 propostas comerciais, condições de pagamento e garantia. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Coletar mínimo de 3 cotações comparáveis — Compras — Dia 1.
2. Equalizar propostas adicionando o custo estimado dos itens omitidos ('plug' de equalização) — Compras/Orçamentista — Dia 2.
3. Aplicar matriz ponderada e recomendar vencedor — Compras — Dia 3.

## Regras e critérios
Prática de mercado: Nunca adjudicar pelo menor preço nominal sem equalizar escopo completo.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmula:** $\text{Preço Equalizado}_k = \text{Proposta}_k + \sum \text{Itens Omitidos}_k$. Exemplo: Proposta B ($90k + $3k entulho = $93k) vs. Proposta A ($92k completo -> Vencedora).

## Saídas
Entregável padronizado da skill `quote-comparison` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Compras / Orçamentista**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `quote-comparison` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `quote-comparison` sem dados obrigatórios (Memorial descritivo padrão) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Compras / Orçamentista ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
