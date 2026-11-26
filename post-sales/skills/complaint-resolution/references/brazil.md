---
plugin: rt-post-sales
skill: complaint-resolution
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Ouvidoria / Gerente de Qualidade
---

# Resolução de Reclamações, Ouvidoria e Defesa do Consumidor

## Objetivo e gatilhos
Tratar reclamações formais de clientes, inquilinos e proprietários com SLAs rígidos, matriz de escalonamento e prevenção de demandas em órgãos de defesa do consumidor.
- **Gatilhos:** acionar `rt-post-sales/complaint-resolution` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para litígios judiciais já protocolados (`rt-legal/disputes-eviction`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Canal de origem, histórico do cliente, natureza da falha, impacto financeiro. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Acusar recebimento formal em até 4 horas úteis e classificar severidade — Atendimento — <= 4h.
2. Investigar causa raiz com área envolvida em até 24h — Ouvidoria — <= 24h.
3. Apresentar solução objetiva ao cliente em até 48h e colher aceite — Ouvidoria/Gerência — <= 48h.

## Regras e critérios
Norma: França/EU *Médiateur de la Consommation* obrigatório (Code de la consommation art. L612-1); Brasil Decreto 11.034/2022 e PROCON.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `complaint-resolution` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Ouvidoria / Gerente de Qualidade**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `complaint-resolution` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `complaint-resolution` sem dados obrigatórios (Canal de origem) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Ouvidoria / Gerente de Qualidade ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
