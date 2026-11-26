---
plugin: rt-sales
skill: closing-checklist
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Fechamento (Closing Coordinator)
---

# Checklist de Fechamento (Da Proposta Aceita ao Registro)

## Objetivo e gatilhos
Orquestrar todas as etapas pós-aceite da proposta até a escritura/closing, pagamento e registro definitivo, controlando prazos críticos e responsáveis.
- **Gatilhos:** acionar `rt-sales/closing-checklist` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para entrega física pós-escritura (`rt-post-sales/property-handover`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Proposta/contrato assinado, jurisdição, forma de pagamento (à vista vs. financiamento), lista de partes. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Validar depósito de sinal e acionar due diligence documental (`rt-legal/title-due-diligence`) — Closing Coordinator — Dias 1–3.
2. Acompanhar vistoria técnica, avaliação bancária e aprovação final de crédito — Closing Coordinator — Dias 5–25.
3. Conferir minutas finais (Escritura / TRID Closing Disclosure / Acte Authentique) e guias de impostos (ITBI/Transfer Tax) — Jurídico/Closing — D-5.
4. Confirmar liquidação financeira, assinatura e protocolar registro no cartório/Land Registry — Closing/Despachante — D0 a D+15.

## Regras e critérios
Prática de mercado: Realizar walk-through final do imóvel 24h antes do closing para confirmar estado de conservação e desocupação.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `closing-checklist` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Fechamento (Closing Coordinator)**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `closing-checklist` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `closing-checklist` sem dados obrigatórios (Proposta/contrato assinado) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Fechamento (Closing Coordinator) ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
