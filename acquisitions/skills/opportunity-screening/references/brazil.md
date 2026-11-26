---
plugin: rt-acquisitions
skill: opportunity-screening
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de Aquisições
---

# Triagem de Oportunidades e Leilões Imobiliários

## Objetivo e gatilhos
Filtrar oportunidades de compra (mercado aberto, off-market, leilões judiciais/extrajudiciais, distressed) aplicando critérios eliminatórios e matriz de pontuação antes da modelagem financeira profunda.
- **Gatilhos:** acionar `rt-acquisitions/opportunity-screening` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para modelagem financeira detalhada de TIR/VPL (`deal-feasibility`) nem para due diligence jurídica completa (`rt-legal/title-due-diligence`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Localização, tipologia, área, preço pedido/lance mínimo, estado de ocupação, estado físico aparente, fonte (leilão/proprietário/corretor), matrícula resumida. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Aplicar filtros eliminatórios (Knock-out) — Analista de Aquisições — Dia 0.
2. Pontuar ativo nos 5 pilares (Localização/Liquidez, Desconto vs. Mercado, Complexidade de Obra, Risco Jurídico/Ocupação, Fit Estratégico) — Analista — Dia 1.
3. Emitir veredito (Avançar para Viabilidade, Banco de Reserva ou Descartar) — Gerente de Aquisições — Dia 1.

## Regras e critérios
Prática de mercado: Desconto mínimo alvo sobre valor de mercado pós-reforma (ARV) >= 25%–30% para flipping; cap rate de entrada >= taxa livre de risco + 300 bps para renda. Critérios eliminatórios típicos: área de risco geotécnico/inundação severa, fraude à execução comprovada, indisponibilidade patrimonial sem baixa possível, imóvel sem acesso regular. Decisão da empresa: `[PENDENTE: Confirmar bairros-alvo e nota de corte]`.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Pontuação ponderada (0 a 100 pontos; corte padrão >= 70 pts): Localização (30%), Desconto/Spread (30%), Obra (15%), Jurídico/Ocupação (15%), Liquidez (10%).

## Saídas
Entregável padronizado da skill `opportunity-screening` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Gerente de Aquisições**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `opportunity-screening` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `opportunity-screening` sem dados obrigatórios (Localização) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Gerente de Aquisições ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
