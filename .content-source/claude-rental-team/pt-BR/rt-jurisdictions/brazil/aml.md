---
plugin: rt-jurisdictions
skill: aml
jurisdiction: brazil
last_verified: 2026-11-25
confidence: verified
reviewer: Diretor de Compliance / Jurídico
---

# Jurisdição Brasil — Prevenção à Lavagem de Dinheiro (PLD/FTP — Lei 9.613/98 e COFECI)

## Objetivo e gatilhos
Definir obrigações de identificação de clientes (KYC), manutenção de registros, monitoramento de operações suspeitas e comunicações ao COAF para empresas imobiliárias no Brasil.
- **Gatilhos:** 'obrigações COAF imobiliária', 'quando comunicar operação suspeita imóvel', 'limites pagamento em espécie imóvel', 'resolução COFECI PLD'.

## Quando não usar
- Não usar para preencher a ficha KYC individual de um cliente (usar `rt-legal/privacy-aml`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Tipo de operação (compra/venda, intermediação, incorporação) | Sim | Enum | Operação |
| Valor da transação e meio de pagamento (TED, Pix, espécie, cripto, exterior) | Sim | Numérico + Enum | Proposta / Financeiro |
| Perfil das partes (PF, PJ, PEP — Pessoa Exposta Politicamente, beneficiário final) | Sim | Estruturado | Cadastro KYC |

## Processo
1. **Cadastrar empresa e manter regularidade no COFECI / SISCOAF** — Compliance — Anual / Contínuo.
2. **Identificar partes e beneficiários finais (KYC)** antes de concluir negócios — Comercial / Jurídico — Pré-contrato.
3. **Verificar lista de Pessoas Expostas Politicamente (PEP)** e sanções internacionais (CSNU) — Compliance — Pré-contrato.
4. **Monitorar sinais de alerta (Red Flags)** e gatilhos automáticos — Financeiro / Compliance — Contínuo.
5. **Comunicar ao COAF via SISCOAF em até 24 horas** a contar da operação ou proposta suspeita, mantendo sigilo absoluto (proibido *tipping-off*) — Diretor Responsável — Até 24h.

## Regras e critérios
- **Norma (Sujeição Legal):** Pessoas físicas ou jurídicas que exerçam atividades de promoção imobiliária ou compra e venda de imóveis são sujeitas às obrigações da Lei nº 9.613/1998 (art. 9º, parágrafo único, X), regulamentadas pelo COFECI (Resolução COFECI nº 1.336/2014 e atualizações).
- **Norma (Comunicação Automática — Operações em Espécie):** Devem ser comunicadas ao COAF, independentemente de análise de mérito, operações pagas em **espécie** (dinheiro vivo) de valor igual ou superior a **R$ 100.000,00** (ou equivalente em moeda estrangeira), ou fracionamentos que visem burlar esse limite (Res. COFECI 1.336/2014, art. 10).
- **Norma (Comunicação por Suspeita):** Qualquer proposta ou operação com indícios de lavagem de dinheiro ou financiamento ao terrorismo deve ser comunicada em **24 horas** ao COAF (Lei 9.613/98, art. 11, II), incluindo: (a) pagamento em espécie >= R$ 30.000 com recusa de identificação de origem; (b) valores incompatíveis com a capacidade econômico-financeira declarada; (c) transações envolvendo PEP sem justificativa econômica; (d) uso de terceiros ('laranjas') ou PJ offshore sem beneficiário final identificado; (e) compra e revenda rápida com ágio/deságio injustificado.
- **Norma (Declaração de Não Ocorrência):** Caso não ocorram operações passíveis de comunicação no ano civil, apresentar declaração negativa ao COFECI até **31 de janeiro** do ano seguinte (Lei 9.613/98, art. 11, III).
- **Norma (Guarda de Registros e Sigilo):** Conservar cadastros e registros por no mínimo **5 anos** (art. 10, §2º). É estritamente proibido dar ciência ao cliente sobre a comunicação ao COAF (sigilo legal, art. 11, §2º).

## Cálculos
**Limites Regulatórios Chave (COFECI / COAF):**
- **Gatilho automático em espécie:** $\ge \mathbf{R\$ 100.000,00}$
- **Prazo de comunicação ao COAF:** $\le \mathbf{24\text{ horas}}$ da conclusão ou proposta
- **Retenção documental obrigatória:** $\ge \mathbf{5\text{ anos}}$

## Saídas
Matriz de risco PLD/FTP + lista de verificação de sinais de alerta + procedimento de reporte sigiloso ao COAF.

## Aprovação humana
- Toda comunicação ao COAF e toda rejeição de cliente por risco de PLD exige decisão e registro formal do Diretor de Compliance/Sócio Administrador, sob sigilo absoluto.

## Repasses
- Segue para `rt-legal/privacy-aml` e `rt-finance/accounts-receivable`.

## Erros comuns e riscos
- Avisar o cliente ou o corretor externo de que o caso foi reportado ao COAF (violação grave de sigilo).
- Aceitar pagamento em espécie acima de R$ 100 mil sem comunicar ao COAF ou aceitar depósitos não identificados na boca do caixa.

## Casos de teste
1. **Normal:** 'Quando uma imobiliária precisa enviar declaração negativa ao COFECI?' -> Até 31 de janeiro do ano seguinte caso não tenha havido comunicações ao COAF no ano anterior.
2. **Incompleto:** 'Um cliente quer pagar uma entrada de R$ 150 mil; preciso comunicar o COAF?' -> Pergunta o meio de pagamento (TED/Pix rastreável de conta própria vs. espécie/terceiros/offshore) e perfil PEP.
3. **Risco:** 'O comprador trouxe R$ 120 mil em notas de reais dentro de uma mochila para dar de sinal.' -> Alerta que pagamento em espécie >= R$ 100 mil exige comunicação obrigatória ao COAF em 24h via SISCOAF e recomenda política interna de recusa de espécie.

## Fontes
- Lei de Lavagem de Dinheiro — Lei nº 9.613/1998 (arts. 9º, 10, 11, 12) — Planalto, acesso 2026-11-25.
- Resolução COFECI nº 1.336/2014 — COFECI (`cofeci.gov.br`), acesso 2026-11-25.

## Pendências
- Política interna da empresa sobre aceitação ou vedação total de recebimentos em espécie.
