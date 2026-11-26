---
plugin: rt-marketing
skill: campaign-planning
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de Marketing
---

# Planejamento de Campanhas Imobiliárias (Captação, Venda e Locação)

## Objetivo e gatilhos
Estruturar campanhas de geração de demanda e captação de imóveis definindo público-alvo, proposta de valor, mix de canais (portais, Meta, Google, mídia local), orçamento e metas de funil.
- **Gatilhos:** acionar `rt-marketing/campaign-planning` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para redação de anúncio individual (`listing-copywriting`) ou execução técnica de lances (`seo-paid-media`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Objetivo (venda estoque, lançamento, locação rápida, captação proprietários), praça, orçamento disponível, prazo da campanha. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Definir persona, diferencial competitivo e meta de leads/visitas/fechamentos — Gerente de Marketing — Dia 1.
2. Distribuir verba por canal conforme intenção (Google Search/Portais para alta intenção; Meta/YouTube para descoberta e captação) — Especialista Mídia — Dia 2.
3. Produzir ativos visuais (fotos profissionais, tour 360°, vídeo vertical) e aprovar peças — Equipe Criativa — Dias 3–5.

## Regras e critérios
Prática de mercado: Imóveis com fotografia profissional e planta baixa recebem 2x–3x mais cliques nos portais. Respeitar restrições de segmentação habitacional (Special Ad Category).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `campaign-planning` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Gerente de Marketing**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `campaign-planning` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `campaign-planning` sem dados obrigatórios (Objetivo (venda estoque) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Gerente de Marketing ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
