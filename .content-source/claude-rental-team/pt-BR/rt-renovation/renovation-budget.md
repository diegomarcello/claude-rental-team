---
plugin: rt-renovation
skill: renovation-budget
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Engenheiro Orçamentista / Controller
---

# Orçamento Paramétrico e Analítico de Obra, BDI e Contingência

## Objetivo e gatilhos
Elaborar orçamento analítico de reforma com quantitativos, preços unitários de referência (SINAPI/TCPO/RSMeans), BDI, reserva de contingência e controle de desvio previsto vs. realizado.
- **Gatilhos:** acionar `rt-renovation/renovation-budget` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para equalizar propostas concorrentes de empreiteiros (`rt-procurement/quote-comparison`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Memorial descritivo (`scope-of-work`), quantitativos por serviço, base de custos regional, percentual de contingência e regime de contratação. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Levantar quantitativos por item do memorial descritivo — Orçamentista — Dia 1.
2. Aplicar custos unitários de materiais e mão de obra + encargos sociais e BDI — Orçamentista — Dia 2.
3. Adicionar reserva de contingência (10% reforma leve; 15%–20% reforma estrutural/imóvel antigo) — Gerente de Obras — Dia 2.
4. Acompanhar curva físico-financeira semanalmente e exigir aditivo aprovado antes de qualquer extra — Gerente de Obras — Semanal.

## Regras e critérios
Prática de mercado: BDI típico para reformas residenciais entre 15% e 25% conforme complexidade e responsabilidade tributária. Bloquear pagamentos acima do orçamento aprovado sem Change Order assinada.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmulas de Orçamento e Desvio:**
$$\text{Preço de Venda Obra} = \text{Custo Direto} \times (1 + \text{BDI}) \times (1 + \text{Contingência})$$
$$\text{Desvio Orçamentário (\%)} = \frac{\text{Custo Realizado} - \text{Orçamento Base}}{\text{Orçamento Base}} \times 100$$
- **Exemplo numérico:** Custo Direto (materiais + mão de obra) = R$ 80.000 ($80k); BDI = 20%; Contingência = 10% sobre custo com BDI:
  - $\text{Subtotal c/ BDI} = 80.000 \times 1,20 = \mathbf{R\$ 96.000}$ ($96k)
  - $\text{Orçamento Total c/ Contingência (10\%)} = 96.000 \times 1,10 = \mathbf{R\$ 105.600,00}$ ($105.6k).
  - Se o realizado fechar em R$ 101.000: $\text{Desvio} = \frac{101.000 - 105.600}{105.600} = \mathbf{-4,36\%}$ (economia de R$ 4.600).

## Saídas
Entregável padronizado da skill `renovation-budget` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Engenheiro Orçamentista / Controller**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `renovation-budget` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `renovation-budget` sem dados obrigatórios (Memorial descritivo (`scope-of-work`)) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Engenheiro Orçamentista / Controller ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
