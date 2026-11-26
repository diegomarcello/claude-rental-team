---
name: lease-administration
plugin: rt-property-management
jurisdiction: pt-BR
version: 1.0.0
---

# `lease-administration` — Administração de Contratos, Reajustes e Rescisões

## 1. Objetivo
Gerir o ciclo de vida operacional dos contratos de locação ativos, calculando reajustes anuais, multas rescisórias proporcionais, aluguéis proporcionais e prazos de renovação ou denúncia.

## 2. Quando Usar
- Ativação de contrato novo após vistoria de entrada.
- Aniversário anual do contrato para aplicação de reajuste pelo índice contratual.
- Pedido de rescisão antecipada ou encerramento contratual.
- Controle de vencimento de prazo determinado (30 ou 60 meses).

## 3. Entradas Necessárias
- Dados do contrato ativo (`aluguel_atual`, `data_inicio`, `prazo_total_meses`, `indice_nome`, `multa_contratual_alugueis`).
- Variação acumulada em 12 meses do índice oficial (`IPCA`, `IGPM`, `INPC` ou `IVAR`).
- Data pretendida de desocupação (em caso de rescisão).

## 4. Processo de Execução
1. Seguir a especificação matemática em `calculations/lease-administration.md`.
2. Para reajuste anual: aplicar `novo_aluguel = round(aluguel_atual * (1 + variacao_indice_pct / 100), 2)` quando `variacao_indice_pct >= 0`; se negativo e deflação não autorizada, manter `aluguel_atual`.
3. Gerar a notificação formal ao locatário usando `rent-adjustment-notice.md` com antecedência mínima de 30 dias.
4. Para rescisão antecipada: calcular `multa_proporcional` conforme Art. 4º da Lei 8.245/91 e aluguel proporcional aos dias ocupados no mês.

## 5. Regras de Jurisdição (Brasil)
- **Lei nº 8.245/1991, Art. 4º:** Proporcionalidade obrigatória da multa rescisória ao período restante do contrato.
- **Lei nº 10.192/2001, Art. 2º:** Periodicidade mínima anual para reajuste monetário de contratos de locação.

## 6. Saídas
- Memória de cálculo de reajuste ou rescisão.
- Notificação de reajuste (`rent-adjustment-notice.md`) ou demonstrativo de encerramento.

## 7. Repasses
- **Reajuste calculado:** Enviar novo valor de aluguel para `rt-finance/accounts-receivable` atualizar o faturamento futuro.
- **Rescisão solicitada:** Enviar valores proporcionais e multa para `rt-property-management/move-inspections` (agendar vistoria de saída) e `rt-legal/disputes-eviction` (`move-out-agreement.md`).

## 8. Limites e Alçadas
- Isenção ou redução de multa rescisória exige aprovação conforme tabela de alçadas em `company-context.md` e anuência do proprietário.

## 9. Erros Comuns e Riscos
- Aplicar reajuste em periodicidade inferior a 12 meses (nulidade legal).
- Cobrar multa cheia de 3 aluguéis sem aplicar a proporcionalidade do tempo já cumprido.
- Aplicar índice negativo reduzindo o aluguel quando o contrato veda deflação nominal.

## 10. Casos de Teste
1. **Reajuste anual positivo:** Aluguel de R$ 3.500,00 com IPCA acumulado de 4,62% → Novo aluguel de **R$ 3.661,70** (diferença de R$ 161,70) e emissão de `rent-adjustment-notice.md`.
2. **Índice negativo sem deflação:** Aluguel de R$ 3.000,00 com IGP-M de -1,20% e cláusula de proteção nominal → Mantém **R$ 3.000,00** sem redução.
3. **Rescisão proporcional:** Contrato de 30 meses, aluguel de R$ 3.000,00, multa de 3 aluguéis (R$ 9.000,00), desocupação após 12 meses cumpridos (18 meses restantes) → Multa proporcional de **R$ 5.400,00**.

## 11. Fontes
- **Lei do Inquilinato (Lei nº 8.245/1991)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/l8245.htm — Arts. 4º, 17 e 18 — Acesso em: 2026-11-25.
- **Lei nº 10.192/2001 (Plano Real / Reajuste Anual)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/leis_2001/l10192.htm — Art. 2º — Acesso em: 2026-11-25.

## 12. Pendências
- Confirmar índice padrão preferencial para novos contratos em `company-context.md` (Responsável: Coordenador de Locação).

## 13. Templates Associados
- `templates/brazil/property-management/lease-administration/rent-adjustment-notice.md`
