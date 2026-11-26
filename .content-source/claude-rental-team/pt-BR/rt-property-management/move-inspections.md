---
plugin: rt-property-management
skill: move-inspections
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Vistorias
---

# Vistoria Locatícia de Entrada e Saída e Desgaste Natural

## Objetivo e gatilhos
Executar vistorias comparativas detalhadas com fotos datadas na entrada e na saída do inquilino, distinguindo danos indenizáveis de desgaste natural pelo uso normal e gerindo prazos de contestação e devolução de caução.
- **Gatilhos:** acionar `rt-property-management/move-inspections` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para inspeção estrutural de compra (`rt-appraisal/technical-inspection`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Laudo de vistoria de entrada assinado, fotos comparativas de saída, orçamentos de reparo, prazo legal de devolução de caução. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Realizar vistoria de entrada antes da entrega das chaves com fotos e leitura de medidores — Vistoriador — Move-in.
2. Conceder prazo de contestação ao inquilino — Analista — Pós-move-in.
3. Na desocupação, comparar item a item separando desgaste natural vs. dano — Vistoriador — Move-out.
4. Liberar saldo da caução dentro do prazo legal da jurisdição — Financeiro/Locação — Prazo legal.

## Regras e critérios
Norma: Restituição no estado recebido, salvas deteriorações decorrentes do uso normal (BR Lei 8.245/91 art. 23, III; US/EU normal wear and tear doctrines).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `move-inspections` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Vistorias**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `move-inspections` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `move-inspections` sem dados obrigatórios (Laudo de vistoria de entrada assinado) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Vistorias ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
