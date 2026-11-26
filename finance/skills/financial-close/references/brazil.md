---
plugin: rt-finance
skill: financial-close
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Controller / Contador
---

# Fechamento Contábil Mensal e Reconhecimento de Receita

## Objetivo e gatilhos
Conduzir o fechamento mensal até o 5º dia útil com conciliação bancária/fiduciária e apropriação de receitas por competência (IFRS 15 / ASC 606).
- **Gatilhos:** acionar `rt-finance/financial-close` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para planejamento tributário anual (`tax-planning`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Razão contábil, extratos bancários, relatórios ERP, folha, notas fiscais. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. D+1 a D+2: Fechar conciliação bancária e fiduciária — Analistas Contábeis — D+2.
2. D+3: Reconhecer receita por competência (ASC 606 / CPC 47) — Contador — D+3.
3. D+4: Revisar balancete e DRE por unidade de negócio — Controller — D+4.
4. D+5: Travar período e publicar pacote executivo — CFO — D+5.

## Regras e critérios
Norma: ASC 606 / IFRS 15 (CPC 47) — Receita de intermediação reconhecida no fechamento/transferência do controle.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `financial-close` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Controller / Contador**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `financial-close` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `financial-close` sem dados obrigatórios (Razão contábil) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Controller / Contador ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
