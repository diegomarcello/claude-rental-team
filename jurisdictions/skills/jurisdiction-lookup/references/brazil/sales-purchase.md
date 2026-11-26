---
plugin: rt-jurisdictions
skill: sales-purchase
jurisdiction: brazil
last_verified: 2026-11-25
confidence: verified
reviewer: Advogado Imobiliário (OAB) / Tabelião
---

# Jurisdição Brasil — Compra, Venda, Registro e Financiamento

## Objetivo e gatilhos
Consolidar as regras legais brasileiras de transferência imobiliária, registro público, certidões, distrato e alienação fiduciária.
- **Gatilhos:** 'regras de compra e venda no Brasil', 'como funciona o registro de imóvel', 'prazo de distrato lei 13.786', 'custos de escritura e ITBI'.

## Quando não usar
- Não usar para análise de certidão específica de um imóvel concreto (usar `rt-legal/title-due-diligence`).
- Não usar para cálculo de parcelas SAC/Price de um cliente (usar `rt-sales/financing-simulation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Município e UF do imóvel | Sim | Texto (ex.: São Paulo/SP) | Usuário / CRM |
| Valor da transação | Sim | Numérico (BRL) | Proposta / Contrato |
| Forma de pagamento (à vista, SFH, SFI, incorporação) | Sim | Enum | Proposta |
| Tipo de vendedor (PF ou PJ) | Sim | Enum | Cadastro |

## Processo
1. **Identificar natureza do negócio** (imóvel pronto vs. na planta; à vista vs. financiado) — Analista Jurídico — Dia 0.
2. **Levantar certidões reais e pessoais** (matrícula atualizada, ônus, ações reais/reipersecutórias, distribuidores cíveis/trabalhistas/fiscais) — Paralegal — Dias 1 a 5.
3. **Formalizar instrumento** (Escritura Pública no Tabelionato de Notas para imóveis > 30 salários mínimos, ou Contrato com força de escritura no SFH/SFI) — Tabelião / Banco — Dias 5 a 15.
4. **Recolher ITBI e emolumentos** antes da lavratura ou do registro, conforme lei municipal — Financeiro / Comprador — Dia 15.
5. **Protocolar no Cartório de Registro de Imóveis (CRI)** para transferência efetiva da propriedade (*só é dono quem registra*) — Despachante / Jurídico — Dias 15 a 30.

## Regras e critérios
- **Norma (Transferência de Propriedade):** A propriedade imobiliária entre vivos só se adquire pelo registro do título translativo no CRI competente (Código Civil, art. 1.245).
- **Norma (Escritura Pública):** Obrigatória para negócios jurídicos que visem à constituição, transferência, modificação ou renúncia de direitos reais sobre imóveis de valor superior a 30 vezes o maior salário mínimo vigente no País (CC, art. 108), salvo exceções legais como contratos no âmbito do SFH/SFI (Lei 4.380/64, art. 61, §5º e Lei 9.514/97, art. 38).
- **Norma (Concentração na Matrícula):** Não podem ser opostos ao adquirente de boa-fé atos jurídicos precedentes não averbados ou registrados na matrícula do imóvel (Lei 13.097/2015, art. 54, com redação da Lei 14.382/2022), ressalvadas hipóteses de fraude contra credores/execução fiscal conforme jurisprudência.
- **Norma (Distrato na Incorporação):** Na resolução por inadimplemento do adquirente em incorporação imobiliária, a retenção pela incorporadora limita-se a até **25%** da quantia paga (regra geral) ou até **50%** quando a incorporação estiver submetida ao regime de patrimônio de afetação, além da comissão de corretagem (Lei 13.786/2018, art. 67-A). Prazo de restituição: 180 dias após o distrato (sem afetação) ou 30 dias após o Habite-se (com afetação).
- **Norma (Alienação Fiduciária):** Consolidada a propriedade fiduciária após intimação e purgação da mora em 15 dias (Lei 9.514/97, art. 26), o credor deve realizar 1º leilão em 30 dias (valor mínimo = avaliação contratual) e 2º leilão em 15 dias (valor mínimo = dívida + despesas, respeitado o piso de 50% do valor de avaliação atualizado conforme Lei 14.711/2023).
- **Prática de Mercado:** Sinal (arras confirmatórias, CC arts. 417–420) costuma variar entre 5% e 10% na assinatura do Compromisso de Compra e Venda.
- **Decisão da Empresa:** `[PENDENTE: Definir política própria de custeio de certidões e despacho]`. 

## Cálculos
**Custo Estimado de Transferência (Composição Base):**
$$\text{Custo Transferência} = \text{ITBI} + \text{Escritura Pública} + \text{Registro (CRI)} + \text{Certidões}$$
- **ITBI:** Alíquota municipal (ex.: São Paulo/SP = 3% sobre valor venal de referência ou valor da transação, o que for maior — Tema 1.113 STJ determina presunção de boa-fé do valor declarado pelo contribuinte, salvo processo administrativo).
- **Exemplo numérico (Imóvel em SP de R$ 1.000.000,00 à vista):**
  - ITBI (3%): R$ 30.000,00
  - Escritura Pública (Tabela TJSP 2026 estimada): ~R$ 7.800,00
  - Registro no CRI (Tabela TJSP 2026 estimada): ~R$ 4.600,00
  - Certidões: ~R$ 450,00
  - **Total aproximado:** **R$ 42.850,00** (~4,29% do valor do imóvel).

## Saídas
Relatório estruturado em Markdown com: (1) Checklist de etapas e prazos; (2) Tabela de custos cartorários/fiscais estimados; (3) Alertas de risco registral.

## Aprovação humana
- Claude **nunca** assina escritura, dispensa certidão positiva com efeito de negativa ou altera cláusula de arras/distrato sem validação expressa de advogado inscrito na OAB.

## Repasses
- Segue para `rt-legal/title-due-diligence` (com matrícula e dados dos vendedores) e `rt-sales/closing-checklist` (com cronograma de assinatura).

## Erros comuns e riscos
- Confundir assinatura de Compromisso de Compra e Venda com transferência de propriedade.
- Ignorar a necessidade de outorga conjugal (CC, art. 1.647, I), exceto no regime de separação absoluta.
- Desconsiderar indisponibilidade de bens (CNIB) antes do pagamento do sinal.

## Casos de teste
1. **Normal:** 'Quais etapas e impostos incidem na compra à vista de um apartamento de R$ 800 mil em São Paulo?' -> Lista escritura pública, ITBI 3%, registro CRI e prazos.
2. **Incompleto:** 'Quanto custa passar um imóvel para o meu nome?' -> Solicita município/UF, valor e forma de pagamento.
3. **Risco:** 'O vendedor tem uma execução fiscal, mas não consta nada na matrícula. Posso comprar tranquilo?' -> Alerta sobre exceção à concentração na matrícula (crédito tributário / fraude à execução, CTN art. 185) e exige parecer jurídico.

## Fontes
- Código Civil Brasileiro — Lei nº 10.406/2002 (arts. 108, 417–420, 1.245, 1.647) — Planalto (`planalto.gov.br`), acesso 2026-11-25.
- Lei dos Registros Públicos — Lei nº 6.015/1973 e Lei nº 13.097/2015 (art. 54) — Planalto, acesso 2026-11-25.
- Lei do Distrato — Lei nº 13.786/2018 — Planalto, acesso 2026-11-25.
- Lei da Alienação Fiduciária — Lei nº 9.514/1997 e Marco Legal das Garantias — Lei nº 14.711/2023 — Planalto, acesso 2026-11-25.

## Pendências
- Tabelas estaduais exatas de emolumentos de notas e registro de cada UF de atuação.
- Alíquotas municipais específicas de ITBI fora de São Paulo/SP.
