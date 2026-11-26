---
plugin: rt-finance
skill: collections
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Cobrança / Jurídico
---

# Régua de Cobrança Amigável e Limites Legais

## Objetivo e gatilhos
Executar régua estruturada de cobrança de aluguéis e encargos em atraso (D+1 a D+30), aplicando multa e juros dentro dos tetos legais e proibindo práticas abusivas ou constrangimento.
- **Gatilhos:** acionar `rt-finance/collections` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para ações judiciais de despejo (`rt-legal/disputes-eviction`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Contrato, valor vencido, data de vencimento, multa e juros pactuados, garantia vigente. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. D+1 a D+3: Envio automático de lembrete preventivo amigável — Automação Financeira — D+1.
2. D+5 a D+10: Contato ativo e envio de boleto atualizado com multa/juros legais — Analista Cobrança — D+5.
3. D+15: Notificação formal e aviso à seguradora/fiador — Cobrança — D+15.
4. D+30 sem acordo: Transferir dossiê para `rt-legal/disputes-eviction` — Coordenador — D+30.

## Regras e critérios
Norma: Proibido constrangimento ou exposição ao ridículo (BR CDC arts. 42 & 71; US FDCPA; EU consumer law; FR Loi 1989 art. 4).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `collections` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Cobrança / Jurídico**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `collections` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `collections` sem dados obrigatórios (Contrato) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Cobrança / Jurídico ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
