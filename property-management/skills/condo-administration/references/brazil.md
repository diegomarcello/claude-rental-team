---
plugin: rt-property-management
skill: condo-administration
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Analista de Carteira / Patrimônio
---

# Interface com Condomínios, Assembleias e Rateio de Despesas

## Objetivo e gatilhos
Gerenciar obrigações condominiais dos imóveis sob gestão, separar despesas ordinárias (inquilino) de extraordinárias (proprietário) e representar proprietários em assembleias mediante procuração.
- **Gatilhos:** acionar `rt-property-management/condo-administration` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para administrar o condomínio inteiro como síndico profissional.

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Boleto discriminado do condomínio, convenção/regimento interno, edital de convocação de assembleia, procuração do proprietário. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Auditar composição do boleto mensal separando despesas ordinárias de extraordinárias — Analista — Mensal.
2. Repassar convenção e regimento interno ao inquilino na assinatura — Locação — Move-in.
3. Alertar proprietário sobre assembleias relevantes com 10 dias de antecedência — Analista — Pré-assembleia.

## Regras e critérios
Norma: BR Lei 8.245/91 art. 22 §1 vs. art. 23 XII; França Décret n° 87-713 (*charges récupérables*).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `condo-administration` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Analista de Carteira / Patrimônio**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `condo-administration` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `condo-administration` sem dados obrigatórios (Boleto discriminado do condomínio) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Analista de Carteira / Patrimônio ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
