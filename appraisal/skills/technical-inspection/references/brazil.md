---
plugin: rt-appraisal
skill: technical-inspection
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro Civil / Inspetor Predial
---

# Vistoria Técnica de Engenharia e Diagnóstico de Patologias

## Objetivo e gatilhos
Executar inspeção física pré-aquisição ou pré-entrega avaliando estrutura, cobertura, impermeabilização, elétrica, hidrossanitário e HVAC, classificando criticidade e necessidade de perícia especializada.
- **Gatilhos:** acionar `rt-appraisal/technical-inspection` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para vistoria locatícia cosmética de entrada/saída de inquilino (`rt-property-management/move-inspections`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Tipologia e idade da edificação, plantas existentes, acesso a cobertura/quadros/shafts, histórico de reformas. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Inspecionar sistemas por ordem crítica: Estrutura -> Cobertura/Impermeabilização -> Elétrica -> Hidrossanitário -> HVAC -> Esquadrias/Acabamentos — Inspetor — Dia 1.
2. Registrar evidências fotográficas georreferenciadas/datadas e classificar gravidade (Crítico/Segurança, Alto/CapEx Relevante, Moderado/Manutenção, Cosmético) — Inspetor — Dia 1.
3. Recomendar ensaios destrutivos/especializados (termografia, estanqueidade, sondagem, esclerometria) quando houver indício oculto — Engenheiro — Dia 2.

## Regras e critérios
Norma: ABNT NBR 16747 (Inspeção Predial — Diretrizes, conceitos, terminologia e procedimento) no Brasil; InterNACHI / ASTM E2018 (Property Condition Assessments — PCA) nos EUA; RICS Home Survey Standards na Europa.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável (classificação técnica por criticidade: Grau 1 Mínimo, Grau 2 Regular, Grau 3 Crítico).

## Saídas
Entregável padronizado da skill `technical-inspection` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Engenheiro Civil / Inspetor Predial**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `technical-inspection` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `technical-inspection` sem dados obrigatórios (Tipologia e idade da edificação) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Engenheiro Civil / Inspetor Predial ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
