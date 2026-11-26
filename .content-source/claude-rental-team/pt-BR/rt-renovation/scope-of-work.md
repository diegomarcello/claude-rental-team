---
plugin: rt-renovation
skill: scope-of-work
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro / Arquiteto Coordenador
---

# Memorial Descritivo e Escopo Técnico de Reforma

## Objetivo e gatilhos
Transformar o diagnóstico físico e o objetivo comercial (locação rápida vs. revenda alto padrão) em memorial descritivo detalhado por disciplina, especificando materiais, exclusões e critérios de aceite.
- **Gatilhos:** acionar `rt-renovation/scope-of-work` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para precificar itens ou calcular BDI (`renovation-budget`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Laudo de vistoria técnica, padrão-alvo do imóvel, plantas/medidas, restrições de condomínio/prefeitura. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Definir padrão de acabamento alinhado ao ARV ou aluguel-alvo (evitar over-improving) — Aquisições/Obras — Dia 1.
2. Detalhar serviços por disciplina (Demolição, Alvenaria, Hidráulica, Elétrica, Gesso, Revestimentos, Pintura, Esquadrias, Marcenaria, Limpeza) — Engenheiro/Arquiteto — Dias 2–3.
3. Listar expressamente exclusões (ex.: eletrodomésticos, decoração) e critérios objetivos de aceite — Engenheiro — Dia 3.

## Regras e critérios
Prática de mercado: Padronizar kits de acabamento por faixa de imóvel para ganho de escala em compras e manutenção futura.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `scope-of-work` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Engenheiro / Arquiteto Coordenador**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `scope-of-work` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `scope-of-work` sem dados obrigatórios (Laudo de vistoria técnica) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Engenheiro / Arquiteto Coordenador ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
