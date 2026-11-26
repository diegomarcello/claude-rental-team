---
plugin: rt-legal
skill: disputes-eviction
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Advogado Contencioso Imobiliário
---

# Notificações Extrajudiciais, Cobrança Judicial e Despejo

## Objetivo e gatilhos
Conduzir o rito jurídico após falha da cobrança amigável: notificação formal de constituição em mora, negociação de acordo de desocupação, ação de despejo/execução e cumprimento de mandado.
- **Gatilhos:** acionar `rt-legal/disputes-eviction` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para lembretes amigáveis de atraso <= 15 dias (`rt-finance/collections`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Contrato de locação, demonstrativo atualizado do débito, comprovante de garantia, histórico de cobrança, endereço de citação. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Auditar requisitos formais de notificação prévia na jurisdição (ex.: 3-day notice nos EUA; commandement de payer de 6 semanas/2 meses na FR; denúncia prévia no BR) — Advogado — Dia 1.
2. Enviar notificação extrajudicial com aviso de recebimento/cartório/bailiff — Advogado — Dia 2.
3. Avaliar acordo de desocupação amigável (Cash-for-Keys) vs. ajuizamento de despejo — Advogado/Diretoria — Dia 7.
4. Protocolar ação judicial e acompanhar liminar/audiência/desocupação — Advogado — Dia 10+.

## Regras e critérios
Norma: Proibição absoluta de autotutela / despejo extrajudicial forçado ('self-help eviction' — trocar fechaduras ou cortar água/energia é crime/ilícito civil grave em BR, EUA e EU). Prescrição cobrança aluguéis: 3 anos no BR (CC art. 206, §3º, I); 4–6 anos nos EUA conforme estado; 3 anos na FR (Loi 1989 art. 7-1).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `disputes-eviction` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Advogado Contencioso Imobiliário**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `disputes-eviction` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `disputes-eviction` sem dados obrigatórios (Contrato de locação) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Advogado Contencioso Imobiliário ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
