---
plugin: rt-renovation
skill: works-schedule
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de Obras
---

# Cronograma Físico-Financeiro, Caminho Crítico e Marcos de Pagamento

## Objetivo e gatilhos
Sequenciar etapas de obra com dependências técnicas, identificar caminho crítico (lead time de esquadrias/marcenaria/aprovações) e vincular desembolsos a entregas físicas verificadas.
- **Gatilhos:** acionar `rt-renovation/works-schedule` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para orçamento analítico (`renovation-budget`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Memorial descritivo, orçamento aprovado, restrições de horário de trabalho, lead times de fornecedores. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Estruturar EAP em ordem lógica: Proteção/Demolição -> Infraestrutura (Elétrica/Hidráulica/Ar) -> Alvenaria/Gesso -> Impermeabilização/Revestimentos -> Pintura 1ª demão -> Esquadrias/Marcenaria/Louças -> Pintura final/Limpeza — Gerente de Obras — Pré-obra.
2. Mapear caminho crítico e disparar pedidos de itens de longo prazo na Semana 1 — Compras/Obras — Semana 1.
3. Vincular pagamentos exclusivamente a marcos concluídos e vistoriados — Gerente de Obras/Financeiro — Contínuo.

## Regras e critérios
Prática de mercado: Sinal de mobilização máximo de 10%–15%; retenção técnica (holdback/retainage) de 5%–10% liberada apenas após conclusão integral da lista de pendências (punch list).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `works-schedule` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Gerente de Obras**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `works-schedule` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `works-schedule` sem dados obrigatórios (Memorial descritivo) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Gerente de Obras ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
