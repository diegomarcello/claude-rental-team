---
plugin: rt-procurement
skill: vendor-management
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Compras / Compliance
---

# Homologação de Fornecedores e Mitigação de Risco Trabalhista

## Objetivo e gatilhos
Qualificar e monitorar empreiteiros e fornecedores verificando regularidade fiscal, seguros (RC / Workers' Comp), habilitação técnica e ausência de risco trabalhista.
- **Gatilhos:** acionar `rt-procurement/vendor-management` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para contratar corretores ou funcionários internos (`rt-human-resources/recruiting`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: CNPJ/EIN/NIF, certidões negativas, apólices de seguro vigentes, registro profissional, referências. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Exigir pacote de homologação antes do 1º Pedido de Compra — Compras — Pré-cadastro.
2. Bloquear automaticamente no ERP fornecedores com seguro vencido — Sistema/Compras — Automático.
3. Avaliar desempenho pós-serviço trimestralmente — Obras/Manutenção — Trimestral.

## Regras e critérios
Norma: Responsabilidade subsidiária/solidária trabalhista e previdenciária na terceirização de obras (BR Súmula 331 TST; US Workers' Comp / DOL; EU subcontracting liability).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `vendor-management` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Compras / Compliance**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `vendor-management` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `vendor-management` sem dados obrigatórios (CNPJ/EIN/NIF) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Compras / Compliance ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
