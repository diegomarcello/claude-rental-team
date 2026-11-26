---
plugin: rt-legal
skill: tenancy-law
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Advogado Imobiliário
---

# Consultoria de Direito Locatício e Jurisprudência

## Objetivo e gatilhos
Responder dúvidas operacionais do dia a dia sobre direitos e deveres de locadores e locatários (benfeitorias, direito de preferência, sublocação, venda de imóvel locado, reparos).
- **Gatilhos:** acionar `rt-legal/tenancy-law` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar quando já houver inadimplência grave ou necessidade de ação judicial (`disputes-eviction`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Jurisdição, cláusula contratual específica, situação fática ocorrida, datas e notificações já enviadas. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Identificar regra legal supletiva ou cogente na jurisdição — Advogado — Mesmo dia.
2. Confrontar com a redação do contrato assinado — Advogado — Mesmo dia.
3. Orientar ação preventiva com modelo de notificação extrajudicial se cabível — Advogado — Até 24h.

## Regras e critérios
Norma (Exemplos chave): Direito de preferência do inquilino na venda (BR Lei 8.245/91 art. 27 — prazo 30 dias; FR Loi 1989 art. 15-II em congé pour vendre). Benfeitorias necessárias são indenizáveis mesmo sem autorização (BR art. 35).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `tenancy-law` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Advogado Imobiliário**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `tenancy-law` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `tenancy-law` sem dados obrigatórios (Jurisdição) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Advogado Imobiliário ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
