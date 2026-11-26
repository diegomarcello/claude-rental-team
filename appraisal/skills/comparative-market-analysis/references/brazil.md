---
plugin: rt-appraisal
skill: comparative-market-analysis
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Avaliador Habilitado (CRECI/CNAI, CREA/CAU, Appraiser, MRICS)
---

# Análise Comparativa de Mercado (ACM / CMA) e Homogeneização

## Objetivo e gatilhos
Estimar valor de mercado de compra, venda ou locação por meio do Método Comparativo Direto de Dados de Mercado com saneamento de amostra, homogeneização por fatores/regressão e intervalo de confiança.
- **Gatilhos:** acionar `rt-appraisal/comparative-market-analysis` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para avaliação de ativos geradores de renda pura sem comparáveis (`income-capitalization`) ou imóveis especiais sem mercado (`cost-approach`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Características do imóvel avaliando (endereço, área privativa, dormitórios, vagas, padrão, andar, estado de conservação) e amostra de >= 5 comparáveis recentes (transações fechadas ou ofertas). | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Coletar >= 5 a 10 imóveis comparáveis na mesma zona homogênea (últimos 6–12 meses) — Avaliador — Dia 1.
2. Aplicar fator de fonte/elasticidade (desconto de oferta anunciada para transação real) e ajustar atributos (área, padrão, vagas, conservação) — Avaliador — Dia 2.
3. Eliminar outliers (critério de Chauvenet ou +/- 2 desvios-padrão) e calcular média saneada, mediana e IC 80% — Avaliador — Dia 2.
4. Validar resultado e emitir parecer/relatório — Responsável Técnico — Dia 3.

## Regras e critérios
Norma: ABNT NBR 14653-2 (BR), USPAP Standards Rule 1-4(a) (US), RICS Red Book / ImmoWertV (EU). Prática de mercado: Fator de oferta típico entre 0,90 e 0,95 (desconto de 5% a 10% sobre preço anunciado); mínimo de 5 dados efetivamente utilizados após saneamento.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmula de Valor Unitário Homogeneizado ($VU_h$):**
$$VU_{h,i} = \left(\frac{\text{Preço}_i}{\text{Área}_i}\right) \times F_{\text{oferta}} \times F_{\text{localização}} \times F_{\text{padrão/conservação}} \times F_{\text{vagas}}$$
$$\text{Valor Avaliado} = \overline{VU}_h \times \text{Área Avaliando}$$
- **Exemplo numérico (Apartamento 100 m², 3 comparáveis saneados):**
  - Comp 1: R$ 950.000 / 100 m² = R$ 9.500/m² x 0,92 (oferta) x 1,00 = **R$ 8.740/m²**
  - Comp 2: R$ 880.000 / 95 m² = R$ 9.263/m² x 0,95 (oferta) x 1,02 (padrão) = **R$ 8.976/m²**
  - Comp 3: R$ 910.000 / 100 m² (venda fechada) = R$ 9.100/m² x 1,00 x 0,98 (andar) = **R$ 8.918/m²**
  - $\overline{VU}_h = (8.740 + 8.976 + 8.918)/3 = \mathbf{R\$ 8.878,00/m^2}$ -> $\text{Valor Estimado (100 m²)} = \mathbf{R\$ 887.800,00}$.

## Saídas
Entregável padronizado da skill `comparative-market-analysis` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Avaliador Habilitado (CRECI/CNAI, CREA/CAU, Appraiser, MRICS)**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `comparative-market-analysis` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `comparative-market-analysis` sem dados obrigatórios (Características do imóvel avaliando (endereço) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Avaliador Habilitado (CRECI/CNAI, CREA/CAU, Appraiser, MRICS) ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
