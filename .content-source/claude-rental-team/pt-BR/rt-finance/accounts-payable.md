---
plugin: rt-finance
skill: accounts-payable
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador Financeiro / Controller
---

# Contas a Pagar, Retenções Tributárias e Prevenção a Fraude Bancária

## Objetivo e gatilhos
Processar pagamentos a fornecedores, empreiteiros e prestadores com conferência tripartite (Pedido x Medição/Entrega x Nota Fiscal), apuração de retenções na fonte e protocolo anti-fraude de boleto/PIX/wire.
- **Gatilhos:** acionar `rt-finance/accounts-payable` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para repasse mensal de aluguéis a proprietários (`owner-payouts`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Nota Fiscal/Invoice, pedido/medição aprovada, dados cadastrais e bancários do favorecido, regime tributário do prestador, alçada de aprovação. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Executar conferência tripartite (Pedido + Evidência de entrega/obra + NF válida) — Analista AP — Dia 0.
2. Calcular retenções obrigatórias na fonte — Fiscal/AP — Dia 1.
3. Validar dados bancários via Call-back obrigatório em alterações de conta — Analista AP — Pré-agendamento.
4. Submeter lote ao aprovador segregado e liquidar na janela semanal — Controller/Diretor — Pagamento.

## Regras e critérios
Norma / Controle Interno: Nunca alterar conta bancária de fornecedor ou proprietário com base apenas em e-mail (prevenção contra BEC).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Exemplo numérico (Serviço PJ Lucro Presumido BR — NF R$ 10.000,00):** IRRF 1,5% (R$ 150) + CSRF 4,65% (R$ 465) + ISS 5% (R$ 500) -> Líquido = **R$ 8.885,00**.

## Saídas
Entregável padronizado da skill `accounts-payable` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador Financeiro / Controller**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `accounts-payable` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `accounts-payable` sem dados obrigatórios (Nota Fiscal/Invoice) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador Financeiro / Controller ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
