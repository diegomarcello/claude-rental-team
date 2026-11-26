---
plugin: rt-jurisdictions
skill: taxes
jurisdiction: brazil
last_verified: 2026-11-25
confidence: verified
reviewer: Contador Tributarista (CRC) / Advogado Tributarista
---

# Jurisdição Brasil — Tributação Imobiliária e Reforma Tributária (EC 132/2023 e LC 214/2025)

## Objetivo e gatilhos
Mapear tributos incidentes sobre compra, posse, ganho de capital, locação e administração imobiliária no Brasil, incluindo a transição para IBS e CBS.
- **Gatilhos:** 'impostos na venda de imóvel', 'ganho de capital imóvel PF', 'tributação de aluguel PF vs PJ', 'reforma tributária locação IBS CBS'.

## Quando não usar
- Não usar para planejamento tributário individualizado ou apuração de DARF/DAS mensal (usar `rt-finance/tax-planning`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Natureza do contribuinte (PF ou PJ — Lucro Presumido/Real/Simples) | Sim | Enum | Cadastro |
| Fato gerador (venda, ganho de capital, aluguel, intermediação) | Sim | Enum | Operação |
| Valor da operação e custo de aquisição | Sim | Numérico (BRL) | Contabilidade |

## Processo
1. **Identificar fato gerador e sujeito passivo** (PF vs. PJ) — Analista Fiscal — Dia 0.
2. **Apurar base de cálculo e deduções legais** (benfeitorias averbadas, corretagem paga pelo alienante, fatores de redução) — Contador — Dia 1.
3. **Aplicar alíquota vigente e verificar isenções** (ex.: imóvel único <= R$ 440 mil ou reinvestimento residencial em 180 dias para PF) — Contador — Dia 1.
4. **Monitorar regras de transição IBS/CBS** a partir de 2026/2027 conforme LC 214/2025 — Consultoria Tributária — Contínuo.

## Regras e critérios
- **Norma (ITBI — Transmissão Inter Vivos):** Competência municipal (CF/88, art. 156, II); alíquotas típicas de 2% a 3%.
- **Norma (IPTU — Propriedade):** Competência municipal (CF/88, art. 156, I), fato gerador anual (1º de janeiro).
- **Norma (Ganho de Capital — Pessoa Física):** Alíquotas progressivas (Lei 13.259/2016): **15%** até R$ 5 milhões; **17,5%** de R$ 5M a R$ 10M; **20%** de R$ 10M a R$ 30M; **22,5%** acima de R$ 30M. Recolhimento até o último dia útil do mês subsequente via GCAP/DARF.
- **Norma (Isenções de Ganho de Capital PF):** (a) Alienação de único imóvel por valor até **R$ 440.000,00**, desde que não tenha realizado outra alienação nos últimos 5 anos (Lei 9.250/95, art. 23); (b) Produto da venda de imóvel residencial aplicado na aquisição de outro imóvel residencial no Brasil no prazo de **180 dias**, uma vez a cada 5 anos (Lei 11.196/2005, art. 39); (c) Fatores de redução antigos (1969–1988, Lei 7.713/88) e fatores FR1/FR2 (Lei 11.196/2005, art. 40).
- **Norma (Aluguel — PF vs. PJ Lucro Presumido):** PF tributa no Carnê-Leão pela tabela progressiva mensal do IRPF (até 27,5%), deduzindo IPTU/condomínio se pagos pelo locador e taxa de administração. PJ (Lucro Presumido — atividade imobiliária CNAE 6810-2): presunção de 32% para IRPJ/CSLL sobre receita de aluguel + PIS/COFINS (3,65% cumulativo) = carga efetiva ~11,33% a 14,53% (com adicional de IRPJ); na venda de estoque imobiliário próprio, presunção de 8% (IRPJ) e 12% (CSLL) = carga efetiva ~5,93% a 6,73%.
- **Norma (Reforma Tributária — LC 214/2025 — IBS/CBS):** Institui regime específico para operações com bens imóveis com redutor de **50%** na alíquota padrão para venda/incorporação e redutor de **70%** para locação, cessão onerosa e arrendamento, além de redutor de ajuste (custo histórico corrigido) e redutor social (ex.: R$ 600/mês por imóvel residencial locado, corrigido pelo IPCA). Sujeição de PF à tributação regular de IBS/CBS na locação caso possua mais de 3 imóveis distintos e receita anual superior a R$ 240.000,00 (com regra de gatilho excedente de 20%), conforme transição iniciada em 2026 (alíquota teste 0,9% CBS + 0,1% IBS compensável) e vigência plena escalonada 2027–2033.
- **Obrigações Acessórias:** DIMOB (Declaração de Informações sobre Atividades Imobiliárias — entrega anual até último dia útil de fevereiro para imobiliárias/incorporadoras) e CIB (Cadastro Imobiliário Brasileiro).

## Cálculos
**1. Ganho de Capital PF (Venda acima de R$ 440 mil sem reinvestimento):**
$$\text{Ganho} = (\text{Valor Venda} - \text{Corretagem Vendedor}) - (\text{Custo Aquisição} + \text{Benfeitorias Averbadas} + \text{ITBI/Registro pagos na compra})$$
- **Exemplo numérico:** Compra em 2020 por R$ 500.000 (com ITBI/registro R$ 20.000 = R$ 520.000). Venda em 2026 por R$ 820.000, com R$ 49.200 de corretagem (6%):
  - Valor líquido alienação = $820.000 - 49.200 = R\$ 770.800,00$
  - Ganho bruto = $770.800 - 520.000 = R\$ 250.800,00$
  - Aplicando fator de redução simplificado ilustrativo (ex.: ~14%): Base tributável $\approx R\$ 215.688,00 \times 15\% = \mathbf{R\$ 32.353,20}$ de IR.

## Saídas
Quadro comparativo tributário (PF vs. PJ) com base de cálculo, alíquota, prazo de vencimento e obrigações acessórias.

## Aprovação humana
- Claude **nunca** emite guia de recolhimento nem define enquadramento societário/holding sem assinatura de Contador (CRC) ou Advogado Tributarista.

## Repasses
- Segue para `rt-finance/tax-planning` e `rt-acquisitions/deal-feasibility`.

## Erros comuns e riscos
- Omitir despesas de corretagem e ITBI pago na aquisição ao apurar ganho de capital.
- Desconsiderar a retenção de IRRF (tabela progressiva) quando PJ paga aluguel a locador PF (responsabilidade da fonte pagadora).

## Casos de teste
1. **Normal:** 'Qual o imposto sobre venda de imóvel próprio no Lucro Presumido?' -> Explica presunção de 8% IRPJ e 12% CSLL + 3,65% PIS/COFINS (~5,93% a 6,73%).
2. **Incompleto:** 'Quanto vou pagar de imposto vendendo meu apartamento?' -> Pergunta se é PF ou PJ, valor de compra, valor de venda, data de aquisição e se pretende comprar outro residencial em 180 dias.
3. **Risco:** 'Um cliente PF tem 5 imóveis alugados somando R$ 30 mil/mês; ele entra no IBS/CBS?' -> Sinaliza o critério da LC 214/2025 (> 3 imóveis e receita > R$ 240 mil/ano) e recomenda revisão contábil.

## Fontes
- Lei nº 9.250/1995 (art. 23), Lei nº 11.196/2005 (arts. 39–40), Lei nº 13.259/2016 — Planalto, acesso 2026-11-25.
- Emenda Constitucional nº 132/2023 e Lei Complementar nº 214/2025 (Regime Específico de Bens Imóveis — IBS/CBS) — Planalto, acesso 2026-11-25.
- IN RFB nº 1.115/2010 (DIMOB) — Receita Federal, acesso 2026-11-25.

## Pendências
- Regulamentação infralegal final da Receita Federal/Comitê Gestor sobre o redutor de ajuste e CIB no cronograma 2027.
