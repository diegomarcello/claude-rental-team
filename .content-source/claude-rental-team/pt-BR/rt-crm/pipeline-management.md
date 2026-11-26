---
plugin: rt-crm
skill: pipeline-management
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de Operações / RevOps
---

# Gestão de Funis de Venda e Locação no CRM

## Objetivo e gatilhos
Definir estágios claros, critérios objetivos de entrada/saída, SLAs máximos por etapa e regras de perda/estagnação nos funis de venda, locação e captação.
- **Gatilhos:** acionar `rt-crm/pipeline-management` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para higiene de registros duplicados (`crm-data-hygiene`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Funil alvo (Venda, Locação, Captação), estágios atuais do CRM, histórico de conversão e tempo médio por etapa. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Estruturar estágios baseados em compromissos verificáveis (Lead Novo -> Qualificado -> Visita Agendada -> Visita Realizada -> Proposta/Ficha -> Análise/Contrato -> Fechado Ganho/Perdido) — RevOps — Setup.
2. Configurar alertas de estagnação (SLA vencido) — RevOps — Automático.
3. Exigir motivo estruturado obrigatório ao mover negócio para 'Perdido' — Comercial — Contínuo.

## Regras e critérios
Prática de mercado: Limitar cada funil a 6–8 estágios objetivos; proibir avanço sem campos obrigatórios.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `pipeline-management` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Gerente de Operações / RevOps**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `pipeline-management` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `pipeline-management` sem dados obrigatórios (Funil alvo (Venda) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Gerente de Operações / RevOps ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
