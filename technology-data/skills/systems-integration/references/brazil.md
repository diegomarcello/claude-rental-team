---
plugin: rt-technology-data
skill: systems-integration
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Arquiteto de Soluções / TI
---

# Integração de Sistemas, APIs e Conectores MCP

## Objetivo e gatilhos
Projetar e documentar integrações entre CRM, ERP/PMS, portais imobiliários, assinatura eletrônica, bancos e servidores MCP do `claude-rental-team`.
- **Gatilhos:** acionar `rt-technology-data/systems-integration` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para modelagem de painéis analíticos (`bi-reporting`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Lista de sistemas em uso, endpoints/APIs, método de autenticação, frequência de sincronização. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Mapear System of Record por entidade — Arquiteto TI — Fase 1.
2. Configurar conectores MCP e webhooks idempotentes com DLQ — Engenharia TI — Fase 2.
3. Armazenar credenciais em Secrets Vault com rotação periódica — Segurança TI — Contínuo.

## Regras e critérios
Prática de mercado: Webhooks orientados a eventos para tempo real e batch noturno para conciliação contábil.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `systems-integration` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Arquiteto de Soluções / TI**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `systems-integration` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `systems-integration` sem dados obrigatórios (Lista de sistemas em uso) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Arquiteto de Soluções / TI ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
