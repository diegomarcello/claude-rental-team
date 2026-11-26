---
plugin: rt-pre-sales
skill: follow-up-cadence
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Pré-vendas
---

# Cadências de Follow-up Omnichannel e Limites Legais de Contato

## Objetivo e gatilhos
Definir sequências estruturadas de contato (telefone, WhatsApp/SMS, e-mail) para leads novos e pós-visita, respeitando horários permitidos, limites de frequência e descadastro imediato.
- **Gatilhos:** acionar `rt-pre-sales/follow-up-cadence` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para cobrança de inadimplentes (`rt-finance/collections`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Estágio do lead no funil, canal com consentimento registrado, fuso horário do lead, histórico de interações. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Executar cadência intensiva nos primeiros 5 dias para leads inbound (D0: ligação + WhatsApp/SMS + e-mail; D1, D2, D4, D5) dentro do horário comercial (08h–20h no fuso do lead) — SDR — Dias 0–5.
2. Migrar leads sem resposta para cadência de nutrição quinzenal/mensal de baixo atrito — Automação CRM — Dias 6–90.
3. Interromper imediatamente qualquer canal diante de pedido de saída ('SAIR', 'STOP', descadastro) e bloquear reativação automática — CRM — Tempo real.

## Regras e critérios
Norma: TCPA quiet hours (8:00 AM – 9:00 PM local time, 47 CFR § 64.1200(c)(1)) e consentimento expresso escrito para SMS; LGPD art. 18 e ePrivacy/GDPR para opt-out imediato.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `follow-up-cadence` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Pré-vendas**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `follow-up-cadence` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `follow-up-cadence` sem dados obrigatórios (Estágio do lead no funil) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Pré-vendas ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
