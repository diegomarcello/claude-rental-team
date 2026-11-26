---
plugin: rt-sales
skill: financing-simulation
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Consultor de Crédito Imobiliário
---

# Simulação de Financiamento Imobiliário (SAC, Price e Hipoteca Fixa)

## Objetivo e gatilhos
Simular parcelas, juros, amortização, seguros obrigatórios (MIP/DFI ou PMI) e comprometimento máximo de renda nos sistemas SAC (Brasil) e Tabela Price / Amortização Constante (EUA/Europa), sempre com aviso legal de simulação.
- **Gatilhos:** acionar `rt-sales/financing-simulation` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar como aprovação oficial de crédito bancário (somente instituições financeiras autorizadas concedem crédito).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Valor do imóvel, valor de entrada, prazo (meses), taxa de juros nominal/efetiva anual, sistema de amortização (SAC vs. Price), renda mensal comprovada dos proponentes. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Calcular valor financiado ($PV = \text{Valor Imóvel} - \text{Entrada}$) e LTV ($PV / \text{Valor Imóvel}$) — Consultor — Imediato.
2. Calcular cronograma de parcelas no sistema escolhido (Price/Annuity ou SAC) + seguros/taxas estimados — Consultor — Imediato.
3. Verificar comprometimento de renda (DTI <= 30% no BR; Front-end <= 28% / Back-end <= 36%–43% nos EUA; DSTI <= 35% na EU como no Banco de Portugal/HCSF França) — Consultor — Imediato.
4. Exibir aviso obrigatório de que os valores são estimativas sujeitas à aprovação de crédito e TR/indexadores — Sistema — Obrigatório.

## Regras e critérios
Norma: Aviso obrigatório de que simulação não constitui oferta vinculante de crédito (EU MCD Directive 2014/17/EU art. 14 ESIS; US TILA/Reg Z 12 CFR § 1026.24; BR Res. CMN 4.676/2018).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmulas de Amortização (Taxa mensal $i$):**
- **Tabela Price (Anuidade Constante — Padrão EUA/EU e opção BR):**
  $$PMT = PV \times \frac{i(1+i)^n}{(1+i)^n - 1}$$
- **Sistema SAC (Amortização Constante — Padrão BR):**
  $$A = \frac{PV}{n}, \quad J_t = SD_{t-1} \times i, \quad PMT_t = A + J_t$$
- **Exemplo numérico ($PV = 400.000$, $n = 360\text{ meses}$, taxa mensal $i = 0,80\%\text{ a.m.}$):**
  - **Price:** $PMT = 400.000 \times \frac{0,008(1,008)^{360}}{(1,008)^{360}-1} = \mathbf{3.394,54}$ fixos (excl. seguros).
  - **SAC (1ª parcela):** $A = 400.000/360 = 1.111,11$; $J_1 = 400.000 \times 0,008 = 3.200,00$; $PMT_1 = \mathbf{4.311,11}$ (decrescendo R$ 8,89/mês até R$ 1.120,00 na última).

## Saídas
Entregável padronizado da skill `financing-simulation` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Consultor de Crédito Imobiliário**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `financing-simulation` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `financing-simulation` sem dados obrigatórios (Valor do imóvel) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Consultor de Crédito Imobiliário ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
