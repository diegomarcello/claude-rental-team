---
plugin: rt-pre-sales
skill: lead-qualification
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Pré-vendas (SDR)
---

# Qualificação Objetiva de Leads (Sem Viés Discriminatório)

## Objetivo e gatilhos
Qualificar leads de compra e locação com critérios objetivos (orçamento, prazo de mudança, finalidade, forma de pagamento/garantia), pontuando prioridade sem perguntas discriminatórias.
- **Gatilhos:** acionar `rt-pre-sales/lead-qualification` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para análise formal de crédito e aprovação final de inquilino (`rt-property-management/tenant-screening`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Dados do lead, imóvel de origem, orçamento declarado, prazo, forma de pagamento/garantia. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Realizar primeiro contato em <= 5 minutos (Speed-to-Lead) — SDR — <= 5 min.
2. Aplicar roteiro consultivo objetivo (Orçamento, Prazo, Tipologia/Região, Forma de Pagamento ou Garantia Locatícia) — SDR — Contato 1.
3. Classificar lead (Quente: visita imediata <= 7 dias; Morno: nutrição 30–90 dias; Frio/Fora de perfil: descarte educado) e transferir ao Corretor/Consultor — SDR — Mesmo dia.

## Regras e critérios
Norma: Proibido perguntar ou pontuar com base em estado civil/filhos, origem nacional, religião, orientação sexual, deficiência ou raça (Fair Housing Act; Lei 7.716/89; Diretiva EU 2000/43/CE).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `lead-qualification` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Pré-vendas (SDR)**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `lead-qualification` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `lead-qualification` sem dados obrigatórios (Dados do lead) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Pré-vendas (SDR) ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
