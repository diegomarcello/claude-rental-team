---
plugin: rt-jurisdictions
skill: leasing
jurisdiction: brazil
last_verified: 2026-11-25
confidence: verified
reviewer: Advogado Imobiliário (OAB)
---

# Jurisdição Brasil — Locação Urbana (Lei do Inquilinato)

## Objetivo e gatilhos
Consolidar regras da Lei nº 8.245/1991 (Lei do Inquilinato) sobre modalidades de locação, garantias, reajuste anual, rescisão, denúncia, direito de preferência e despejo.
- **Gatilhos:** 'regras de locação Brasil', 'multa de rescisão de aluguel', 'garantias permitidas lei do inquilinato', 'prazo de despejo por falta de pagamento'.

## Quando não usar
- Não usar para calcular o reajuste específico de um contrato ativo (usar `rt-property-management/lease-administration`).
- Não usar para redigir petição inicial de despejo (usar `rt-legal/disputes-eviction`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Finalidade (residencial, não residencial, temporada) | Sim | Enum | Contrato / CRM |
| Prazo contratual (meses) | Sim | Inteiro | Contrato |
| Garantia escolhida | Sim | Enum | Proposta |
| Valor do aluguel e encargos | Sim | Numérico (BRL) | Contrato |

## Processo
1. **Enquadrar modalidade locatícia** (Residencial >= 30 meses, Residencial < 30 meses, Temporada <= 90 dias, ou Não Residencial) — Analista de Locação — Dia 0.
2. **Validar garantia única** (vedada dupla garantia sob pena de nulidade e contravenção penal) — Jurídico — Dia 1.
3. **Definir cláusulas de encargos e reajuste** (periodicidade mínima anual, índice oficial) — Jurídico — Dia 1.
4. **Executar vistoria inicial detalhada** antes da entrega das chaves (art. 22, V) — Vistoriador — Dia da entrega.

## Regras e critérios
- **Norma (Garantia Única):** É vedada, sob pena de nulidade, mais de uma das seguintes modalidades de garantia num mesmo contrato de locação: I - caução; II - fiança; III - seguro de fiança locatícia; IV - cessão fiduciária de quotas de fundo de investimento (Lei 8.245/91, art. 37, parágrafo único). Exigir mais de uma constitui contravenção penal (art. 43, II).
- **Norma (Caução em Dinheiro):** Não pode exceder o equivalente a 3 meses de aluguel e deve ser depositada em caderneta de poupança autorizada pelo Poder Público, revertendo ao locatário os respectivos rendimentos no levantamento (art. 38, §2º).
- **Norma (Multa Rescisória):** Durante o prazo estipulado, o locador não pode reaver o imóvel; o locatário pode devolvê-lo pagando a multa pactuada, **proporcional** ao período de cumprimento do contrato (CC, art. 413 e Lei 8.245/91, art. 4º). O locatário fica dispensado da multa se a devolução decorrer de transferência pelo seu empregador (privado ou público) para outra localidade, mediante notificação prévia escrita de no mínimo 30 dias (art. 4º, parágrafo único).
- **Norma (Denúncia Vazia vs. Cheia):** Nos contratos residenciais escritos com prazo >= 30 meses, findo o prazo, opera-se a denúncia vazia (art. 46). Nos contratos inferiores a 30 meses, findo o prazo, a locação prorroga-se por prazo indeterminado e o locador só pode retomar nas hipóteses do art. 47 (denúncia cheia, ex.: uso próprio, após 5 anos ininterruptos).
- **Norma (Temporada):** Prazo máximo de 90 dias; o locador pode receber antecipadamente o aluguel e encargos de uma só vez (arts. 48–49).
- **Norma (Despejo Liminar):** Cabe liminar para desocupação em 15 dias, independentemente de audiência da parte contrária e desde que prestada caução no valor equivalente a 3 meses de aluguel, nas hipóteses do art. 59, §1º, inclusive falta de pagamento de aluguel e acessórios quando o contrato estiver **desprovido de qualquer garantia** (inciso IX).
- **Prática de Mercado:** Multa compensatória padrão de 3 aluguéis (proporcional ao tempo restante) e adoção de IPCA ou IGPM como índice de reajuste anual.
- **Decisão da Empresa:** `[PENDENTE: Política de aceitação de garantias e índice preferencial da carteira]`. 

## Cálculos
**Multa Rescisória Proporcional (Art. 4º):**
$$\text{Multa Devida} = \left(\frac{\text{Multa Pactuada}}{\text{Prazo Total (meses)}}\right) \times \text{Meses Restantes}$$
- **Exemplo numérico:** Contrato de 30 meses, aluguel de R$ 4.000,00, multa pactuada de 3 aluguéis (R$ 12.000,00). Inquilino sai após 18 meses (restam 12 meses):
  - $\text{Multa} = (12.000 / 30) \times 12 = 400 \times 12 = \mathbf{R\$ 4.800,00}$.

## Saídas
Parecer de enquadramento locatício com tabela de prazos, direitos, deveres (art. 22 locador vs. art. 23 locatário) e cálculo de multa.

## Aprovação humana
- Claude **nunca** aprova contrato com dupla garantia, nem autoriza isenção de multa fora da hipótese legal de transferência de trabalho sem aprovação da diretoria.

## Repasses
- Segue para `rt-legal/contract-drafting-review` (minuta contratual) e `rt-property-management/lease-administration` (cadastro de reajuste e vigência).

## Erros comuns e riscos
- Exigir fiador E caução simultaneamente (nulidade + crime/contravenção).
- Cobrar despesas extraordinárias de condomínio (fundo de reserva, pintura de fachada, obras estruturais — art. 22, X) do inquilino.
- Cobrar aluguel antecipado em locação residencial comum com garantia (contravenção penal, art. 43, III).

## Casos de teste
1. **Normal:** 'Qual a multa se o inquilino sair no 10º mês de um contrato de 30 meses de R$ 3.000?' -> Calcula R$ 6.000,00 (proporcional aos 20 meses restantes).
2. **Incompleto:** 'Posso pedir despejo liminar porque o inquilino não pagou?' -> Pergunta se o contrato possui garantia vigente, pois a liminar por falta de pagamento exige contrato sem garantia (art. 59, §1º, IX).
3. **Risco:** 'O inquilino tem restrição no Serasa; podemos pedir caução de 3 meses mais um fiador?' -> Bloqueia imediatamente por violação ao art. 37, parágrafo único (vedação à dupla garantia).

## Fontes
- Lei do Inquilinato — Lei nº 8.245/1991 (arts. 4º, 22, 23, 37, 38, 43, 46, 47, 48, 59) — Planalto (`planalto.gov.br`), acesso 2026-11-25.

## Pendências
- Regras específicas de ação renovatória comercial (art. 51 — prazo de 5 anos e decadência de 1 ano a 6 meses antes do término) caso a empresa atue forte em varejo.
