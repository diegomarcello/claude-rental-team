---
plugin: rt-legal
skill: title-due-diligence
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Advogado Imobiliário
---

# Due Diligence Imobiliária e Análise de Matrícula/Certidões

## Objetivo e gatilhos
Auditar cadeia dominial, ônus reais, penhoras, ações judiciais dos vendedores/antecessores, débitos de IPTU/condomínio e regularidade edilícia antes de fechar compra ou locação comercial relevante.
- **Gatilhos:** acionar `rt-legal/title-due-diligence` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para KYC/AML de origem de recursos (`privacy-aml`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Matrícula atualizada (< 30 dias), dados completos dos vendedores (PF/PJ e cônjuges), IPTU/cadastro municipal, certidão de condomínio. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Analisar matrícula vintenária, cadeia dominial e averbações de construção/estado civil — Paralegal/Advogado — Dias 1–2.
2. Emitir certidões fiscais, trabalhistas, cíveis, execuções e protestos em nome dos vendedores e sócios — Paralegal — Dias 2–4.
3. Verificar débitos propter rem (IPTU e condomínio) e regularidade do Habite-se/CO — Paralegal — Dias 3–5.
4. Emitir parecer de risco (Aprovado, Aprovado com Retenção/Escrow, ou Reprovado) — Advogado Sênior — Dia 5.

## Regras e critérios
Norma: Dívidas de IPTU e condomínio têm natureza propter rem e acompanham o imóvel (BR CC art. 1.345; EUA/EU super-priority liens). Validade padrão de certidões: 30 a 90 dias conforme emissor.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `title-due-diligence` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Advogado Imobiliário**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `title-due-diligence` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `title-due-diligence` sem dados obrigatórios (Matrícula atualizada (< 30 dias)) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Advogado Imobiliário ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
