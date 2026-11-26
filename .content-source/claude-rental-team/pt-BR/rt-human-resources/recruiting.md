---
plugin: rt-human-resources
skill: recruiting
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de RH / Jurídico Trabalhista
---

# Recrutamento, Licenças Profissionais e Seleção Sem Viés

## Objetivo e gatilhos
Estruturar descrições de vagas, validar licenças profissionais obrigatórias e conduzir entrevistas estruturadas livres de perguntas discriminatórias.
- **Gatilhos:** acionar `rt-human-resources/recruiting` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para contratação de empreiteiros de obra (`rt-procurement/vendor-management`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Cargo, tipo de vínculo, requisitos técnicos, faixa salarial/comissionamento. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Verificar exigência legal de licença (CRECI / Real Estate License / AMI / Carte T) — RH — Pré-vaga.
2. Publicar vaga inclusiva e aplicar entrevista estruturada — RH/Gestor — Seleção.
3. Validar licença ativa no órgão regulador antes da proposta — RH — Pré-oferta.

## Regras e critérios
Norma: Leis antidiscriminação no emprego (US Title VII/ADA/ADEA; BR Lei 9.029/95; EU Directive 2000/78/EC).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `recruiting` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Gerente de RH / Jurídico Trabalhista**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `recruiting` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `recruiting` sem dados obrigatórios (Cargo) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Gerente de RH / Jurídico Trabalhista ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
