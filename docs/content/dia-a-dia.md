# Uso no dia a dia

No cotidiano, a equipe descreve a tarefa, confere o que o Claude perguntou e leva a entrega para quem aprova.

## Formas de pedir

| Forma | Quando usar | Exemplo |
|---|---|---|
| Linguagem comum | Na maior parte dos casos | "Prepare a cobrança de um aluguel vencido há 20 dias" |
| Skill direta | Quando já se sabe o processo | `/rt-finance:collections` |
| Comando | Tarefas recorrentes com entrada definida | `/rt-property-management:rt-screen-tenant` |
| Agente | Tarefa que envolve um papel inteiro | "Use o agente rt-lease-admin para revisar a carteira" |
| Roteador | Quando não se sabe quem atende | `/rt-executive:router-executive` |

## Um bom pedido

Informe sempre:

1. **País e cidade**, ou estado.
2. **Objetivo**: o que precisa sair pronto.
3. **Dados**: valores, datas, índice, garantia e cláusulas relevantes.
4. **Situação**: o que já aconteceu e qual é o prazo.

Compare:

| Pedido vago | Pedido completo |
|---|---|
| "Faz o reajuste do aluguel" | "Brasil. Contrato fictício reajustado pelo IPCA. Calcule o novo aluguel a partir de R$ 3.500,00, com variação acumulada de 4,62%, e prepare o aviso ao locatário para revisão" |

Use nomes e documentos somente quando forem necessários à tarefa. Em testes, use dados fictícios.

## Rotina sugerida

As cadências abaixo são um ponto de partida. O pacote não define responsáveis nem prazos: cada empresa ajusta os seus.

| Quando | Atividade | Onde pedir |
|---|---|---|
| Diariamente | Conciliar recebimentos e identificar atrasos | `rt-finance:accounts-receivable` |
| Diariamente | Qualificar leads e agendar visitas | `rt-pre-sales:lead-qualification`, `rt-pre-sales:visit-scheduling` |
| Diariamente | Triar chamados de manutenção | `rt-property-management:maintenance-requests` |
| Semanalmente | Retomar contatos em aberto | `rt-pre-sales:follow-up-cadence` |
| Semanalmente | Atualizar a projeção de caixa | `rt-finance:cash-flow-forecast` |
| Mensalmente | Repassar valores aos proprietários | `rt-finance:owner-payouts` |
| Mensalmente | Fechar o mês e revisar indicadores | `rt-finance:financial-close`, `rt-executive:company-kpis` |
| No aniversário do contrato | Reajustar o aluguel | `rt-property-management:lease-administration` |
| A cada nova locação | Analisar pretendente, contratar e vistoriar | `rt-property-management:tenant-screening`, `rt-legal:contract-drafting-review`, `rt-property-management:move-inspections` |

## Pedidos por área

| Área | Exemplo de pedido |
|---|---|
| Locação | "Brasil. Monte o dossiê de análise do pretendente com os documentos anexados e aponte o que falta" |
| Financeiro | "Brasil. Prepare o demonstrativo de repasse do mês com taxa de administração de 10% e um reparo autorizado de R$ 350,00" |
| Jurídico | "Brasil. Revise esta minuta de locação residencial e liste cláusulas em risco" |
| Marketing | "Escreva o anúncio deste apartamento sem linguagem discriminatória" |
| Vendas | "Brasil. Simule o financiamento nos sistemas SAC e Price e mostre o comprometimento de renda" |
| Avaliação | "Faça a análise comparativa de mercado com estas seis amostras" |
| Obras | "Monte o escopo e o orçamento da reforma deste imóvel, com contingência" |
| Direção | "Revise a matriz de alçadas e aponte conflitos de segregação de funções" |

## Exemplo: aluguel em atraso

Dados fictícios: aluguel de R$ 2.500,00, vencimento em 05/11/2026 e pagamento em 15/11/2026. O Claude executa o script de contas a receber:

```
python3 accounts_receivable.py --valor-principal 2500.00 --data-vencimento 2026-11-05 --data-pagamento 2026-11-15
```

| Resultado | Valor |
|---|---|
| Dias de atraso | 10 |
| Multa | R$ 50,00 |
| Juros | R$ 8,33 |
| Valor atualizado | R$ 2.558,33 |

O script avisa que aplicou os percentuais padrão de 2% de multa e 1% de juros ao mês. **Confira o contrato antes de usar o valor.**

## Exemplo: repasse ao proprietário

Dados fictícios: aluguel recebido de R$ 5.000,00, taxa de administração de 10%, reparo autorizado de R$ 350,00 e compensação em 10/11/2026.

```
python3 owner_payout.py --aluguel-recebido 5000 --taxa-adm-pct 10 --reparos-autorizados 350 --data-compensacao 2026-11-10
```

| Resultado | Valor |
|---|---|
| Taxa de administração | R$ 500,00 |
| Total de descontos | R$ 850,00 |
| Repasse líquido | R$ 4.150,00 |
| Data prevista | 13/11/2026 |

O prazo padrão é de três dias úteis. Feriados precisam ser informados, ou a data considera apenas fins de semana.

## Como ler a entrega

| O que aparece | O que fazer |
|---|---|
| Pendências | Fornecer o dado ou registrar a decisão |
| Itens marcados como proposta | Escolher e confirmar antes de aplicar |
| Aprovador indicado | Levar a entrega a essa pessoa |
| Referência em rascunho | Pedir revisão profissional para o que for decisivo |
| Avisos do cálculo | Conferir contrato e premissas |

## Antes de usar uma entrega

- [ ] O país e o estado estão corretos.
- [ ] Os valores e datas conferem com o contrato.
- [ ] As decisões da empresa usadas estão confirmadas.
- [ ] A regra legal decisiva foi conferida na fonte oficial.
- [ ] A pessoa com alçada aprovou.
