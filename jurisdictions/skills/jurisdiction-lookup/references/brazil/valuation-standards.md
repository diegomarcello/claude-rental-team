---
plugin: rt-jurisdictions
skill: valuation-standards
jurisdiction: brazil
last_verified: 2026-11-25
confidence: verified
reviewer: Engenheiro Avaliador (CREA) / Arquiteto (CAU) / Perito Avaliador (CNAI)
---

# Jurisdição Brasil — Normas de Avaliação de Imóveis (ABNT NBR 14653, COFECI e CONFEA/CAU)

## Objetivo e gatilhos
Definir normas técnicas, metodologias aceitas, requisitos de fundamentação/precisão e habilitação profissional para avaliações imobiliárias no Brasil.
- **Gatilhos:** 'norma de avaliação de imóveis Brasil', 'quem pode assinar laudo de avaliação', 'diferença entre PTAM e laudo NBR 14653'.

## Quando não usar
- Não usar para rodar o cálculo comparativo de um imóvel específico (usar `rt-appraisal/comparative-market-analysis`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Finalidade da avaliação (garantia bancária, judicial, venda, contábil) | Sim | Enum | Solicitante |
| Tipologia do bem (urbano, rural, gleba, empreendimento) | Sim | Enum | Cadastro |
| Profissional emissor (Corretor CNAI vs. Engenheiro/Arquiteto) | Sim | Enum | Operação |

## Processo
1. **Definir finalidade e nível de rigor exigido** (bancário/judicial exige Laudo conforme ABNT NBR 14653; comercial aceita PTAM) — Coordenador de Avaliação — Dia 0.
2. **Vistoriar o imóvel** (obrigatória na NBR 14653, salvo justificativa expressa em casos especiais) — Avaliador — Dia 1.
3. **Selecionar metodologia** (Comparativo Direto de Dados de Mercado, Involutivo, Evolutivo ou Capitalização da Renda) — Avaliador — Dias 2 a 4.
4. **Tratar dados e emitir documento técnico** com ART/RRT (CREA/CAU) ou Selo Certificador (COFECI/CNAI) — Avaliador — Dia 5.

## Regras e critérios
- **Norma (Norma Técnica Principal):** ABNT **NBR 14653-1** (Procedimentos Gerais) e **NBR 14653-2** (Imóveis Urbanos). Classifica os trabalhos em Graus de Fundamentação (I, II e III) e Graus de Precisão (I, II e III, medidos pela amplitude do intervalo de confiança de 80%).
- **Norma (Habilitação Profissional):**
  - **Engenheiros (CREA — Lei 5.194/66) e Arquitetos (CAU — Lei 12.378/2010):** Habilitados para elaborar **Laudo de Avaliação** completo, incluindo análise estrutural, patologias e método evolutivo/custo de reprodução, mediante emissão de ART ou RRT.
  - **Corretores de Imóveis (COFECI — Lei 6.530/78, art. 3º e Resolução COFECI nº 1.066/2007):** Habilitados a emitir **PTAM (Parecer Técnico de Avaliação Mercadológica)** para determinação do valor de mercado, preferencialmente inscritos no **CNAI** (Cadastro Nacional de Avaliadores Imobiliários) com Selo Certificador.
- **Norma (Conteúdo Mínimo NBR 14653-1 / Res. COFECI 1.066/07):** Identificação do solicitante, finalidade, identificação e caracterização do imóvel (matrícula, medidas, estado de conservação), diagnóstico do mercado, indicação do(s) método(s), tratamento dos dados (fatores ou inferência estatística), especificação da fundamentação e precisão, resultado e data de referência, qualificação e assinatura do responsável.
- **Prática de Mercado:** Bancos públicos/privados (Caixa, BB, Itaú) exigem Laudo NBR 14653 assinado por Engenheiro ou Arquiteto credenciado para concessão de crédito imobiliário.

## Cálculos
**Grau de Precisão — NBR 14653-2 (Amplitude do Intervalo de Confiança de 80% em torno da estimativa central):**
- **Grau III (maior precisão):** Amplitude $\le 30\%$
- **Grau II:** $30\% < \text{Amplitude} \le 40\%$
- **Grau I:** $40\% < \text{Amplitude} \le 50\%$
$$\text{Amplitude (\%)} = \frac{\text{Limite Superior}_{80\%} - \text{Limite Inferior}_{80\%}}{\text{Valor Estimado}} \times 100$$
- **Exemplo numérico:** Valor central estimado = R$ 600.000,00; IC 80% entre R$ 530.000,00 e R$ 670.000,00:
  - $\text{Amplitude} = \frac{670.000 - 530.000}{600.000} \times 100 = \frac{140.000}{600.000} \times 100 = \mathbf{23,33\%}$ (**Grau III de Precisão**).

## Saídas
Checklist de conformidade normativa do laudo/PTAM + tabela de enquadramento de grau de fundamentação e precisão.

## Aprovação humana
- Todo laudo ou PTAM exige revisão técnica e assinatura física/digital (ICP-Brasil) de profissional habilitado (CREA, CAU ou CRECI/CNAI).

## Repasses
- Segue para `rt-appraisal/comparative-market-analysis`, `rt-appraisal/income-capitalization` e `rt-appraisal/cost-approach`.

## Erros comuns e riscos
- Entregar PTAM de corretor quando o cliente necessita de laudo de garantia bancária ou perícia de engenharia estrutural.
- Utilizar apenas ofertas anunciadas sem aplicar fator de elasticidade/fonte (desconto de negociação) devidamente justificado.

## Casos de teste
1. **Normal:** 'Qual a diferença entre PTAM e Laudo NBR 14653?' -> Explica habilitação (CRECI/CNAI vs. CREA/CAU), escopo e aceitação bancária.
2. **Incompleto:** 'Preciso avaliar um galpão para garantia de empréstimo.' -> Pergunta localização, área e confirma exigência bancária de Laudo NBR 14653 por Engenheiro/Arquiteto.
3. **Risco:** 'Posso usar uma média simples de 3 anúncios da internet como laudo judicial?' -> Rejeita por descumprir NBR 14653 (amostra insuficiente, ausência de tratamento estatístico/fatores e vistoria).

## Fontes
- ABNT NBR 14653-1:2019 e ABNT NBR 14653-2:2011 — Associação Brasileira de Normas Técnicas, acesso 2026-11-25.
- Resolução COFECI nº 1.066/2007 e Ato Normativo nº 001/2011 — Conselho Federal de Corretores de Imóveis (`cofeci.gov.br`), acesso 2026-11-25.

## Pendências
- Critérios internos da empresa sobre quando contratar laudo externo CREA/CAU vs. emitir PTAM interno.
