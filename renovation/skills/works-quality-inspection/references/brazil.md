---
plugin: rt-renovation
skill: works-quality-inspection
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro Fiscal / Inspetor de Qualidade
---

# Inspeção de Qualidade de Obra, Testes e Lista de Pendências (Punch List)

## Objetivo e gatilhos
Verificar conformidade técnica da obra concluída contra normas de desempenho, realizar testes funcionais (estanqueidade, carga elétrica, caimento) e emitir Termo de Recebimento de Obra.
- **Gatilhos:** acionar `rt-renovation/works-quality-inspection` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para vistoria locatícia com inquilino (`rt-property-management/move-inspections`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Memorial descritivo, projetos executivos, cronograma, checklists de testes por sistema. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Executar testes de infraestrutura antes de fechar forros/paredes (teste hidrostático, estanqueidade 72h em áreas molhadas, continuidade elétrica) — Fiscal de Obra — Durante obra.
2. Realizar vistoria final ambiente por ambiente gerando Punch List com prazo de correção (ex.: 5 dias úteis) — Fiscal de Obra — Entrega.
3. Liberar retenção final somente após baixa de 100% dos itens da Punch List e entrega de garantias/manuais — Gerente de Obras/Financeiro — Encerramento.

## Regras e critérios
Norma: ABNT NBR 15575 (Desempenho de Edificações Habitacionais) no Brasil; IRC/IBC e tolerâncias NAHB Residential Construction Performance Guidelines nos EUA.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `works-quality-inspection` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Engenheiro Fiscal / Inspetor de Qualidade**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `works-quality-inspection` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `works-quality-inspection` sem dados obrigatórios (Memorial descritivo) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Engenheiro Fiscal / Inspetor de Qualidade ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
