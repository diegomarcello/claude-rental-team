---
name: owner-payouts
plugin: rt-property-management
jurisdiction: pt-BR
version: 1.0.0
---

# `owner-payouts` — Repasse ao Proprietário e Prestação de Contas

## 1. Objetivo
Calcular o valor líquido devido ao proprietário após a compensação do pagamento do locatário, deduzindo taxa de administração, taxa de intermediação, retenções tributárias (IRRF) e reparos autorizados, gerando o extrato detalhado e a ordem de pagamento.

## 2. Quando Usar
- Após confirmação de baixa bancária de aluguel ou encargos em `accounts-receivable`.
- No fechamento mensal de prestação de contas aos proprietários.

## 3. Entradas Necessárias
- Valores recebidos conciliados (`aluguel_recebido`, `encargos_reembolsaveis`, `data_compensacao`).
- Parâmetros do contrato de administração (`taxa_adm_pct`, `taxa_intermediacao`, `dias_uteis_prazo`).
- Retenções fiscais (`retencoes_irrf`) e despesas aprovadas (`reparos_autorizados`).
- Dados bancários do proprietário.

## 4. Processo de Execução
1. Seguir rigorosamente a especificação matemática em `calculations/owner-payouts.md`.
2. Calcular `valor_taxa_adm = round(aluguel_recebido * (taxa_adm_pct / 100), 2)`.
3. Deduzir `taxa_intermediacao`, `retencoes_irrf` e `reparos_autorizados`.
4. Verificar se `repasse_liquido >= 0`: se negativo, bloquear pagamento, registrar saldo devedor e notificar financeiro/proprietário.
5. Calcular `data_pagamento_repasse` somando `dias_uteis_prazo` (padrão D+3) à `data_compensacao`.
6. Gerar o extrato utilizando o template `owner-statement.md`.

## 5. Regras de Jurisdição (Brasil)
- **Lei nº 8.245/1991, Art. 22, VI e VII:** Obrigação de prestação de contas e discriminação de encargos.
- **Legislação do Imposto de Renda (RIR/2018, Art. 687):** A taxa de administração e despesas de cobrança pagas pelo locador são dedutíveis do rendimento bruto tributável do aluguel.

## 6. Saídas
- Extrato de repasse formatado (`owner-statement.md`).
- Ordem de pagamento bancário (`valor_liquido_repasse`, `data_pagamento_repasse`, dados bancários de destino).

## 7. Repasses
- **Ordem de pagamento gerada:** Encaminhar para `rt-finance/accounts-payable` (execução bancária) e `rt-finance/cash-flow-forecast` (atualização de fluxo de caixa).
- **Se `repasse_liquido < 0`:** Encaminhar para `rt-finance/accounts-receivable` para emissão de cobrança de reembolso ao proprietário ou compensação no próximo ciclo.

## 8. Limites e Alçadas
- Descontos de reparos no repasse acima do limite emergencial de `company-context.md` exigem aprovação prévia documentada do proprietário e nota fiscal conferida (`three-way-match.md`).

## 9. Erros Comuns e Riscos
- Incidir taxa de administração sobre valores de condomínio e IPTU repassados (a taxa incide apenas sobre o aluguel, salvo pactuação expressa).
- Efetuar repasse sem verificar retenção de IRRF informada pelo locatário Pessoa Jurídica (gerando divergência na DIMOB anual).
- Liberar transferência para conta bancária de terceiro sem procuração/autorização formal do proprietário.

## 10. Casos de Teste
1. **Repasse normal com reparo:** Aluguel recebido R$ 5.000,00, taxa de administração 10% (R$ 500,00), reparo autorizado R$ 350,00 → Valor líquido repassado **R$ 4.150,00** em D+3 dias úteis.
2. **Repasse com saldo negativo:** Aluguel recebido R$ 5.000,00, taxa 10% (R$ 500,00), reparo emergencial aprovado R$ 6.000,00 → Saldo líquido **-R$ 1.500,00** (bloqueia transferência e registra saldo a compensar).
3. **Recusa por ausência de taxa:** Solicitação de repasse de R$ 4.000,00 sem informar `taxa_adm_pct` → Recusa o cálculo e solicita o percentual contratual.

## 11. Fontes
- **Lei do Inquilinato (Lei nº 8.245/1991)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/l8245.htm — Art. 22 — Acesso em: 2026-11-25.
- **Regulamento do Imposto de Renda (Decreto nº 9.580/2018)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm — Art. 687 — Acesso em: 2026-11-25.

## 12. Pendências
- Confirmar prazo padrão de repasse (D+X dias úteis) e regra de compensação de saldo negativo em `company-context.md` (Responsável: Gerente Financeiro).

## 13. Templates Associados
- `templates/brazil/property-management/owner-payouts/owner-statement.md`
