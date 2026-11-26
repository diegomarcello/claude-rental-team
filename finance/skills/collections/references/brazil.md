---
name: collections
plugin: rt-finance
jurisdiction: pt-BR
version: 1.0.0
---

# `collections` — Régua de Cobrança e Recuperação Extrajudicial

## 1. Objetivo
Executar a régua de cobrança escalonada de aluguéis e encargos em atraso, formalizando notificações extrajudiciais, acordos de parcelamento e o encaminhamento tempestivo para ação judicial de despejo.

## 2. Quando Usar
- Recebimento de alertas de inadimplência provenientes de `accounts-receivable` (`dias_atraso >= 1`).
- Negociação de parcelamento de débitos locatícios antes da judicialização.

## 3. Entradas Necessárias
- Ficha financeira atualizada do contrato (`accounts-receivable`).
- Histórico de contatos anteriores e modalidade de garantia do contrato.
- Regras da régua de cobrança e alçadas de desconto em `company-context.md`.

## 4. Processo de Execução
1. Aplicar o estágio correspondente da régua de cobrança:
   - **D+1 a D+5:** Contato preventivo/amigável (e-mail/WhatsApp) com segunda via atualizada.
   - **D+6 a D+15:** Cobrança ativa e alerta de negativação/acionamento da garantia (seguradora fiança ou fiador).
   - **D+16 a D+30:** Notificação extrajudicial formal com prazo peremptório para purgação da mora e comunicação ao garantidor.
   - **Acima de D+30:** Encerramento da fase amigável e dossiê para ação de despejo por falta de pagamento.
2. Registrar todos os contatos sem exposição vexatória ao devedor (CDC, Art. 42).

## 5. Regras de Jurisdição (Brasil)
- **Código de Defesa do Consumidor (Lei nº 8.078/1990, Art. 42):** Proibição de cobrança ridicularizante, constrangedora ou ameaçadora.
- **Lei nº 8.245/1991, Arts. 59 e 62:** Requisitos para ação de despejo por falta de pagamento e liminar de desocupação em 15 dias (quando desprovido de garantia).

## 6. Saídas
- Registro de acionamento da régua de cobrança com estágio, canal utilizado e próximo passo.
- Minuta de notificação extrajudicial ou proposta de acordo formal.

## 7. Repasses
- **Acordo pago / débito quitado:** Encaminhar para `rt-finance/accounts-receivable` para baixa e `rt-property-management/owner-payouts` para repasse.
- **Inadimplência > 30 dias sem acordo ou quebra de acordo:** Encaminhar dossiê completo para `rt-legal/disputes-eviction`.

## 8. Limites e Alçadas
- Parcelamentos superiores a 3 vezes ou qualquer concessão de desconto sobre principal/multa dependem de aprovação conforme `company-context.md` e autorização expressa do proprietário.

## 9. Erros Comuns e Riscos
- Deixar de notificar o fiador ou a seguradora fiança dentro do prazo previsto na apólice (risco de perda da cobertura securitária).
- Cobrar o locatário em horário indevido ou perante terceiros não garantidores (dano moral / Art. 42 CDC).
- Demorar mais de 45 dias para judicializar contratos sem garantia (perda da oportunidade prática de mitigação de prejuízo).

## 10. Casos de Teste
1. **Atraso de 3 dias (D+3):** Boleto de R$ 2.800,00 vencido há 3 dias → Envia mensagem amigável com boleto atualizado (multa + 3 dias de juros) e agenda retorno para D+7.
2. **Atraso de 20 dias com Seguro Fiança:** Boleto de R$ 3.500,00 vencido há 20 dias → Emite notificação extrajudicial e abre aviso de sinistro/expectativa junto à seguradora fiança conforme prazo da apólice.
3. **Atraso de 35 dias sem garantia:** Contrato com caução já esgotada ou sem garantia, 35 dias em aberto → Encaminha dossiê para `rt-legal/disputes-eviction` instruindo pedido de despejo com liminar (Art. 59, § 1º, IX, Lei 8.245/91).

## 11. Fontes
- **Lei do Inquilinato (Lei nº 8.245/1991)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/l8245.htm — Arts. 59 e 62 — Acesso em: 2026-11-25.
- **Código de Defesa do Consumidor (Lei nº 8.078/1990)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/l8078compilado.htm — Art. 42 — Acesso em: 2026-11-25.

## 12. Pendências
- Definir prazos exatos da régua de cobrança e regras de acionamento de seguradoras em `company-context.md` (Responsável: Coordenador Financeiro).

## 13. Templates Associados
- Integra-se com `templates/brazil/legal/disputes-eviction/move-out-agreement.md` em caso de acordo com entrega de chaves.
