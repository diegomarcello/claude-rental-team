---
plugin: rt-appraisal
skill: cost-approach
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro Avaliador (CREA) / Arquiteto (CAU) / Quantity Surveyor
---

# Método Evolutivo / Custo de Reprodução e Depreciação

## Objetivo e gatilhos
Estimar valor de imóveis singulares, galpões, construções novas ou seguro patrimonial somando o valor do terreno ao custo de reprodução/reposição da benfeitoria descontada a depreciação física e funcional.
- **Gatilhos:** acionar `rt-appraisal/cost-approach` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar isoladamente para apartamentos usados em mercados líquidos onde o método comparativo é soberano.

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Valor do terreno (por comparativo ou involutivo), área construída equivalente, custo unitário básico (CUB/SINAPI no BR; RSMeans/Marshall & Swift nos EUA; BKI/RICS BCIS na EU), BDI, idade aparente e vida útil. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Avaliar terreno separadamente pelo método comparativo — Avaliador — Dia 1.
2. Calcular Custo de Reedição/Reposição Novo (RCN) usando índice oficial regional + BDI — Engenheiro — Dia 1.
3. Calcular depreciação física (Ross-Heidecke no Brasil; Age-Life / Breakdown nos EUA/EU) e obsolescência funcional — Engenheiro — Dia 2.
4. Somar terreno + benfeitoria depreciada (e aplicar Fator de Comercialização no Método Evolutivo NBR 14653) — Avaliador — Dia 2.

## Regras e critérios
Norma: NBR 14653-2 (Método Evolutivo / Quantificação de Custo), USPAP SR 1-4(b), RICS Red Book / ImmoWertV (Sachwertverfahren).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmula do Método do Custo / Evolutivo:**
$$V_{\text{total}} = \left(V_{\text{terreno}} + \text{RCN} \times (1 - D)\right) \times FC$$
- **Exemplo numérico (Galpão Industrial):**
  - Terreno = R$ 800.000 ($800k) | Área construída = 1.000 m² | Custo unitário c/ BDI = R$ 2.500/m² -> $\text{RCN} = R\$ 2.500.000$.
  - Idade aparente = 10 anos; Vida útil = 50 anos; Estado 'Regular' (coeficiente Ross-Heidecke $D \approx 0,22$):
  - $\text{Benfeitoria Depreciada} = 2.500.000 \times (1 - 0,22) = \mathbf{R\$ 1.950.000}$.
  - Com Fator de Comercialização $FC = 1,00$: $V_{\text{total}} = 800.000 + 1.950.000 = \mathbf{R\$ 2.750.000,00}$.

## Saídas
Entregável padronizado da skill `cost-approach` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Engenheiro Avaliador (CREA) / Arquiteto (CAU) / Quantity Surveyor**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `cost-approach` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `cost-approach` sem dados obrigatórios (Valor do terreno (por comparativo ou involutivo)) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Engenheiro Avaliador (CREA) / Arquiteto (CAU) / Quantity Surveyor ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
