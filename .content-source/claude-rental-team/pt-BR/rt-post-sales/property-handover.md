---
plugin: rt-post-sales
skill: property-handover
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Pós-Venda / Entrega
---

# Entrega de Chaves, Manuais e Transferência de Titularidade

## Objetivo e gatilhos
Formalizar a entrega física do imóvel vendido ou reformado por meio de Termo de Entrega de Chaves, entrega de manuais/garantias/projetos as-built e protocolo de transferência de água, luz, gás e IPTU.
- **Gatilhos:** acionar `rt-post-sales/property-handover` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para entrega de locação (`rt-property-management/move-inspections`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Comprovante de quitação/registro, termo de vistoria de entrega, manuais de equipamentos, leituras finais de medidores. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Confirmar liquidação financeira integral ou registro antes de liberar chaves — Fechamento/Pós-venda — Dia 0.
2. Realizar vistoria conjunta e assinar Termo de Entrega de Chaves com leitura dos medidores — Pós-venda — Dia 0.
3. Entregar pasta com Manual do Proprietário, garantias e plantas — Pós-venda — Dia 0.
4. Monitorar troca de titularidade de concessionárias em até 15 dias — Pós-venda — D+15.

## Regras e critérios
Prática de mercado: Nunca entregar chaves antecipadamente sem aditivo jurídico expresso e aprovação da diretoria.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `property-handover` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Pós-Venda / Entrega**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `property-handover` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `property-handover` sem dados obrigatórios (Comprovante de quitação/registro) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Pós-Venda / Entrega ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
