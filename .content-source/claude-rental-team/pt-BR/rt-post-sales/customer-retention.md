---
plugin: rt-post-sales
skill: customer-retention
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Sucesso do Cliente
---

# Retenção de Clientes, NPS e Programa de Indicação

## Objetivo e gatilhos
Medir satisfação (NPS/CSAT) nos marcos críticos da jornada, acionar detratores proativamente e estimular indicações de novos proprietários e compradores dentro das regras éticas.
- **Gatilhos:** acionar `rt-post-sales/customer-retention` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para automação técnica de CRM (`rt-crm/journey-automation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Marco concluído, nota NPS (0–10), comentário qualitativo. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Disparar pesquisa transacional NPS 7 dias após entrega de chaves ou 60 dias após início da locação — Automação CS — D+7 / D+60.
2. Acionar protocolo 'Detrator (0–6)' com ligação da gerência em até 24h — Gerente CS — <= 24h.
3. Convidar 'Promotores (9–10)' a avaliar no Google e participar de programa de indicação conforme regras locais — CS — D+3.

## Regras e critérios
Norma: Nos EUA, prêmios por indicação de compra/venda a pessoas não licenciadas são proibidos por leis estaduais de corretagem e RESPA § 8.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmula do NPS:** $\text{NPS} = \%\text{Promotores (9–10)} - \%\text{Detratores (0–6)}$ (escala de -100 a +100).

## Saídas
Entregável padronizado da skill `customer-retention` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Sucesso do Cliente**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `customer-retention` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `customer-retention` sem dados obrigatórios (Marco concluído) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Sucesso do Cliente ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
