---
plugin: rt-sales
skill: proposal-negotiation
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Diretor Comercial / Gerente de Vendas
---

# Gestão de Propostas, Contrapropostas e Negociação de Venda

## Objetivo e gatilhos
Conduzir o recebimento, formalização e negociação de propostas de compra e locação, apresentando todas as ofertas ao proprietário, gerenciando objeções e respeitando alçadas de desconto.
- **Gatilhos:** acionar `rt-sales/proposal-negotiation` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar quando a própria empresa é a compradora investidora (`rt-acquisitions/purchase-negotiation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Proposta escrita do comprador, preço pedido, laudo/ACM de referência, condições de pagamento, alçada de desconto de comissão. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Formalizar toda proposta por escrito com preço, sinal, prazos, forma de pagamento e validade (ex.: 48h–72h) — Corretor — Dia 0.
2. Apresentar obrigatoriamente todas as propostas recebidas ao proprietário com comparativo objetivo de mercado (ACM) — Corretor/Gerente — <= 24h.
3. Formalizar contraproposta assinada pelas partes até o aceite integral e encaminhar para due diligence/contrato — Gerente de Vendas — Dias 1–3.

## Regras e critérios
Norma / Ética: O corretor tem dever fiduciário/legal de transmitir fielmente todas as propostas ao cliente (BR CC art. 723; NAR Code of Ethics Article 1, Standard of Practice 1-6; EU national brokerage codes). Desconto na comissão exige aprovação prévia da gerência.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `proposal-negotiation` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Diretor Comercial / Gerente de Vendas**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `proposal-negotiation` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `proposal-negotiation` sem dados obrigatórios (Proposta escrita do comprador) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Diretor Comercial / Gerente de Vendas ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
