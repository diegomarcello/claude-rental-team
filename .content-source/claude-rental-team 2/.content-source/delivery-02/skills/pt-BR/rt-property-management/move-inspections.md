---
name: move-inspections
plugin: rt-property-management
jurisdiction: pt-BR
version: 1.0.0
---

# `move-inspections` — Vistoria de Entrada, Saída e Periódica

## 1. Objetivo
Documentar objetivamente o estado físico, funcional e de conservação do imóvel no início, durante e ao término da locação, protegendo proprietário e locatário contra disputas sobre reparos e devolução de chaves.

## 2. Quando Usar
- Antes da entrega das chaves ao locatário (`ENTRADA`).
- Durante a vigência contratual para acompanhamento preventivo (`PERIODICA`).
- Na devolução do imóvel e encerramento do contrato (`SAIDA`).

## 3. Entradas Necessárias
- Dados do contrato (`numero_contrato`, partes, endereço do imóvel).
- Registro fotográfico datado por ambiente, leitura de medidores (água, luz, gás) e inventário de chaves/controles.
- Na vistoria de saída: o Laudo de Vistoria de Entrada para comparação item a item.

## 4. Processo de Execução
1. Registrar data, participantes e leitura exata dos medidores de consumo.
2. Descrever cada ambiente por categoria (pintura, piso, esquadrias, instalações elétricas e hidráulicas, mobiliário) classificando em `NOVO`, `BOM`, `REGULAR` ou `DANIFICADO`.
3. Na vistoria de saída, confrontar cada item com a vistoria de entrada, separando desgaste natural do uso normal de danos imputáveis ao locatário (Art. 23, III da Lei 8.245/91).
4. Gerar o laudo usando `inspection-report.md` e coletar assinaturas.

## 5. Regras de Jurisdição (Brasil)
- **Lei nº 8.245/1991, Art. 22, V e Art. 23, III:** O locador deve entregar o imóvel em estado de servir ao uso a que se destina; o locatário deve restituí-lo no estado em que o recebeu, salvo as deteriorações decorrentes do seu uso normal.

## 6. Saídas
- Laudo de vistoria preenchido (`inspection-report.md`).
- Na saída com divergências: lista discriminada de reparos necessários para cotação e cobrança.

## 7. Repasses
- **Vistoria de Entrada concluída:** Encaminhar para `rt-property-management/lease-administration` liberando a entrega de chaves e ativação do contrato.
- **Vistoria de Saída com danos:** Encaminhar lista de reparos para `rt-property-management/quote-comparison` (orçamento) e `rt-legal/disputes-eviction` (`move-out-agreement.md`).
- **Vistoria de Saída sem pendências:** Encaminhar para `rt-legal/disputes-eviction` para assinatura do distrato e quitação.

## 8. Limites e Alçadas
- A skill não arbitra valores finais de indenização sem orçamentos; orçamentos de reparo seguem as alçadas de `company-context.md`.

## 9. Erros Comuns e Riscos
- Realizar vistoria de saída sem o laudo de entrada como referência (impossibilita comprovar dano causado durante a locação).
- Cobrar pintura nova completa quando o imóvel foi entregue com pintura usada e apresenta apenas desgaste natural.
- Esquecer de registrar leitura final dos medidores de água, luz e gás na entrega das chaves.

## 10. Casos de Teste
1. **Vistoria de entrada completa:** Apartamento 2 dormitórios, pintura nova, medidor luz 14.520 kWh, 4 chaves entregues → Gera `inspection-report.md` tipo `ENTRADA` e libera entrega de chaves.
2. **Vistoria de saída com dano:** Porta do banheiro quebrada (constava como `BOM` na entrada) e pintura da sala com manchas de infiltração externa → Aponta porta para reparo pelo locatário e infiltração estrutural para responsabilidade do proprietário.
3. **Vistoria de saída sem laudo de entrada:** Solicitação de vistoria de saída sem histórico de entrada anexado → Emitir alerta de risco probatório e solicitar arquivo de entrada antes de concluir cobrança de reparos.

## 11. Fontes
- **Lei do Inquilinato (Lei nº 8.245/1991)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/l8245.htm — Arts. 22, V e 23, III — Acesso em: 2026-11-25.

## 12. Pendências
- Definir checklist fotográfico mínimo padrão por tipologia de imóvel (Responsável: Coordenador de Locação).

## 13. Templates Associados
- `templates/brazil/property-management/move-inspections/inspection-report.md`
