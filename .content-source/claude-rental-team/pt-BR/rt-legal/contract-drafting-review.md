---
plugin: rt-legal
skill: contract-drafting-review
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Advogado Imobiliário
---

# Elaboração e Revisão de Contratos Imobiliários

## Objetivo e gatilhos
Redigir e revisar contratos de compra e venda, locação, administração, corretagem e empreitada, validando cláusulas obrigatórias, eliminando abusividades e destacando pontos negociáveis.
- **Gatilhos:** acionar `rt-legal/contract-drafting-review` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para negociar preço comercial sem pedido de minuta (`rt-sales/proposal-negotiation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Tipo de contrato, jurisdição, qualificação das partes, objeto, preço/aluguel, prazos, garantias, minutas base da empresa. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Selecionar template aprovado da jurisdição — Jurídico — Dia 0.
2. Preencher qualificação, objeto, preço, garantias e condições especiais — Advogado — Dia 1.
3. Auditar cláusulas obrigatórias (ex.: garantia única no BR; disclosures obrigatórios nos EUA/EU) e remover nulidades — Advogado Sênior — Dia 1.
4. Enviar para assinatura eletrônica após aprovação das alçadas — Operações — Dia 2.

## Regras e critérios
Norma: Proibição de cláusula de renúncia antecipada a direitos irrenunciáveis do inquilino ou consumidor; exigência de testemunhas/assinatura eletrônica qualificada conforme lei local (MP 2.200-2/2001 no BR; ESIGN/UETA nos EUA; eIDAS na EU).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `contract-drafting-review` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Advogado Imobiliário**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `contract-drafting-review` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `contract-drafting-review` sem dados obrigatórios (Tipo de contrato) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Advogado Imobiliário ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
