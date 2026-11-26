---
plugin: rt-marketing
skill: lead-generation
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Marketing / DPO
---

# Captura de Leads, Consentimento e Atribuição de Origem

## Objetivo e gatilhos
Estruturar formulários web, WhatsApp click-to-chat e landing pages com campos mínimos, registro auditável de consentimento (LGPD/TCPA/GDPR) e rastreamento UTM até o fechamento.
- **Gatilhos:** acionar `rt-marketing/lead-generation` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para cadência de follow-up comercial (`rt-pre-sales/follow-up-cadence`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Canal de origem, campos do formulário, texto de aviso de privacidade/consentimento, webhook de integração CRM. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Limitar formulário inicial ao mínimo necessário (Nome, Telefone/WhatsApp, E-mail e Interesse) para maximizar conversão e cumprir minimização de dados — Marketing — Setup.
2. Gravar no CRM: `consent_timestamp`, `consent_text_version`, `ip_address` e parâmetros UTM (`utm_source`, `utm_medium`, `utm_campaign`) — TI/Marketing — Automático.
3. Rotear lead instantaneamente (< 60 segundos) para a fila de Pré-vendas — CRM — Tempo real.

## Regras e critérios
Norma: Registro auditável de consentimento exigido por LGPD art. 8º, §2º, GDPR art. 7(1) e TCPA (PEWC para SMS/ligações automatizadas).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `lead-generation` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Marketing / DPO**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `lead-generation` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `lead-generation` sem dados obrigatórios (Canal de origem) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Marketing / DPO ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
