---
plugin: rt-post-sales
skill: warranty-claims
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro de Assistência Técnica
---

# Gestão de Garantias Construtivas e Vícios Ocultos

## Objetivo e gatilhos
Triar chamados pós-entrega distinguindo garantia legal/contratual de falta de manutenção preventiva do proprietário, acionando construtora ou empreiteiros dentro dos prazos legais.
- **Gatilhos:** acionar `rt-post-sales/warranty-claims` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para chamados corriqueiros de inquilinos em imóveis de terceiros (`rt-property-management/maintenance-requests`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Data do Habite-se/entrega, sistema afetado, fotos, histórico de manutenção do proprietário. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Verificar data de entrega e enquadrar sistema na tabela de prazos de garantia — Assistência Técnica — Dia 1.
2. Vistoriar para descartar mau uso ou ausência de manutenção obrigatória — Engenheiro — Dias 2–5.
3. Acionar garantia do empreiteiro/construtora ou executar reparo coberto — Assistência Técnica — Dias 5–15.

## Regras e critérios
Norma: BR CC art. 618 (5 anos solidez/segurança) & ABNT NBR 17170; França Code civil art. 1792 (10y/2y/1y); Espanha LOE art. 17 (10y/3y/1y).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `warranty-claims` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Engenheiro de Assistência Técnica**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `warranty-claims` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `warranty-claims` sem dados obrigatórios (Data do Habite-se/entrega) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Engenheiro de Assistência Técnica ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
