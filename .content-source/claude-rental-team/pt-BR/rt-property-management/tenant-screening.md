---
plugin: rt-property-management
skill: tenant-screening
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Locação / Compliance
---

# Análise de Crédito e Seleção Objetiva de Inquilinos

## Objetivo e gatilhos
Avaliar candidatos à locação por meio de critérios numéricos padronizados (relação renda/aluguel, score de crédito, histórico locatício, garantia), documentando justificativas objetivas e direitos de contestação.
- **Gatilhos:** acionar `rt-property-management/tenant-screening` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para triagem inicial comercial antes da visita (`rt-pre-sales/lead-qualification`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Valor do aluguel + encargos, renda mensal comprovada dos proponentes, relatório de bureau de crédito, garantia oferecida, histórico de despejos. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Coletar autorização expressa do candidato para consulta aos bureaus de crédito — Analista de Locação — Dia 0.
2. Calcular comprometimento de renda ($\text{Renda Bruta} \ge 3\times (\text{Aluguel} + \text{Encargos})$) e verificar apontamentos — Analista — Dia 1.
3. Emitir parecer objetivo — Coordenador — Dia 1.
4. Em caso de recusa ou condicionante baseada em bureau, enviar notificação formal com fonte da informação (FCRA nos EUA; transparência LGPD/GDPR no BR/EU) — Analista — Imediato.

## Regras e critérios
Norma: Fair Housing Act; vedada dupla garantia no BR (Lei 8.245/91 art. 37); lista fechada do Décret 2015-1437 na FR.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Critério padrão de mercado: $\text{Renda Mensal Comprovada} \ge 3,0 \times (\text{Aluguel} + \text{Condomínio} + \text{IPTU})$.

## Saídas
Entregável padronizado da skill `tenant-screening` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Locação / Compliance**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `tenant-screening` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `tenant-screening` sem dados obrigatórios (Valor do aluguel + encargos) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Locação / Compliance ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
