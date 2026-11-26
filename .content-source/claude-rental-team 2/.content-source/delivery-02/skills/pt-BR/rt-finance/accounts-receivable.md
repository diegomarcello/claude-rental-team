---
name: accounts-receivable
plugin: rt-finance
jurisdiction: pt-BR
version: 1.0.0
---

# `accounts-receivable` — Contas a Receber e Encargos Locatícios

## 1. Objetivo
Controlar o faturamento mensal dos contratos de locação (aluguel, condomínio, IPTU, seguro e reembolsos), conciliar baixas bancárias e calcular encargos moratórios em pagamentos em atraso.

## 2. Quando Usar
- Geração mensal de boletos/faturas de locação.
- Conciliação de pagamentos recebidos (em dia ou em atraso).
- Emissão de segunda via atualizada de boleto vencido.

## 3. Entradas Necessárias
- Dados da cobrança (`valor_principal`, `data_vencimento`, `data_pagamento`, encargos acessórios).
- Parâmetros contratuais de mora (`multa_moratoria_pct`, `juros_mensal_pct`, `indice_correcao_pct`).

## 4. Processo de Execução
1. Seguir a especificação de cálculo em `calculations/accounts-receivable.md`.
2. Verificar `dias_atraso = max(0, (data_pagamento - data_vencimento).days)`.
3. Se `dias_atraso > 0`, calcular multa moratória, juros proporcionais aos dias (`dias_atraso / 30`) e correção monetária conforme contrato.
4. Classificar o título na faixa de atraso (`em_dia`, `1_a_15_dias`, `16_a_30_dias`, `> 30_dias`).

## 5. Regras de Jurisdição (Brasil)
- **Código Civil (Art. 395 e Art. 406) e Lei nº 8.245/1991:** Cobrança de multa moratória contratual (observando limites jurisprudenciais aplicáveis a contratos de locação) e juros de mora pro rata die.

## 6. Saídas
- Demonstrativo de atualização de boleto (`valor_principal`, `multa`, `juros`, `correcao`, `valor_atualizado`, `faixa_atraso`).
- Registro de baixa financeira para disparo de repasse.

## 7. Repasses
- **Título baixado/pago:** Encaminhar imediatamente para `rt-property-management/owner-payouts` com o valor líquido recebido e data de compensação.
- **Título vencido (`dias_atraso >= 1`):** Encaminhar para `rt-finance/collections` conforme faixa de atraso.

## 8. Limites e Alçadas
- Abono ou desconto de multa e juros segue estritamente a tabela de alçadas de `company-context.md`.

## 9. Erros Comuns e Riscos
- Repassar valor de aluguel ao proprietário antes da efetiva compensação bancária do boleto do locatário.
- Calcular juros mensais cheios para atraso de poucos dias sem aplicar proporcionalidade (`dias_atraso / 30`).
- Não discriminar no boleto os valores de condomínio ordinário (responsabilidade do locatário) e fundo de reserva/obras extraordinárias (responsabilidade do proprietário, Art. 22, X, Lei 8.245/91).

## 10. Casos de Teste
1. **Pagamento com 10 dias de atraso:** Aluguel de R$ 2.500,00, vencimento 2026-11-05, pagamento 2026-11-15, multa 2%, juros 1%/mês → Multa R$ 50,00 + Juros R$ 8,33 = **R$ 2.558,33** (`faixa: 1_a_15_dias`).
2. **Pagamento no vencimento:** Aluguel de R$ 2.500,00, vencimento 2026-11-05, pagamento 2026-11-05 → Encargos R$ 0,00, total **R$ 2.500,00** (`faixa: em_dia`).
3. **Atraso superior a 30 dias:** Aluguel de R$ 4.000,00 com 35 dias de atraso → Calcula multa, juros pro rata, correção e classifica em `> 30_dias` acionando `collections`.

## 11. Fontes
- **Lei do Inquilinato (Lei nº 8.245/1991)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/l8245.htm — Arts. 22, X e 23, I — Acesso em: 2026-11-25.
- **Código Civil (Lei nº 10.406/2002)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm — Arts. 394 a 406 — Acesso em: 2026-11-25.

## 12. Pendências
- Confirmar percentuais padrão de multa moratória (2% ou 10%) na política comercial em `company-context.md` (Responsável: Gerente Financeiro / Jurídico).

## 13. Templates Associados
- Nenhum template dedicado no inventário (utiliza demonstrativo estruturado na saída e integração com `owner-statement.md`).
