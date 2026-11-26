---
plugin: rt-acquisitions
skill: purchase-negotiation
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Diretor de Aquisições / Jurídico
---

# Negociação de Compra, Sinal e Condições Suspensivas

## Objetivo e gatilhos
Estruturar propostas de compra, âncoras de negociação, pagamento de sinal (arras) protegido por condições suspensivas (due diligence, financiamento, desocupação) e gatilhos de desistência sem multa.
- **Gatilhos:** acionar `rt-acquisitions/purchase-negotiation` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para negociação de venda de imóvel de cliente da corretagem (`rt-sales/proposal-negotiation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Preço máximo aprovado (Walk-away price), condições físicas/jurídicas do ativo, prazos de due diligence, estrutura de pagamento. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Definir preço âncora inicial e preço-teto aprovado no estudo de viabilidade — Gerente de Aquisições — Dia 0.
2. Redigir Carta de Intenções (LOI) ou Proposta Vinculante com condições suspensivas expressas — Jurídico/Aquisições — Dia 1.
3. Depositar sinal somente após verificação preliminar de matrícula e em conta escrow/condicionada — Financeiro/Jurídico — Dia 3.
4. Formalizar aditivo de ajuste de preço caso a vistoria/due diligence revele passivos ocultos — Aquisições/Jurídico — Durante DD.

## Regras e critérios
Norma: Arras confirmatórias (BR CC arts. 417–420) vs. arras penitenciais (direito de arrependimento). Prática de mercado: Condicionar eficácia do negócio à aprovação integral das certidões pessoais/reais e vistoria técnica em 15–30 dias, com devolução integral e corrigida do sinal em caso de apontamento impeditivo.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável (roteiro negocial e cláusulas de proteção).

## Saídas
Entregável padronizado da skill `purchase-negotiation` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Diretor de Aquisições / Jurídico**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `purchase-negotiation` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `purchase-negotiation` sem dados obrigatórios (Preço máximo aprovado (Walk-away price)) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Diretor de Aquisições / Jurídico ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
