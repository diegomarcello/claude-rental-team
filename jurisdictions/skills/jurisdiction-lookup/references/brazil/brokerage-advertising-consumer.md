---
plugin: rt-jurisdictions
skill: brokerage-advertising-consumer
jurisdiction: brazil
last_verified: 2026-11-25
confidence: verified
reviewer: Advogado Imobiliário (OAB) / Diretor Comercial
---

# Jurisdição Brasil — Corretagem, Publicidade Imobiliária e Código de Defesa do Consumidor

## Objetivo e gatilhos
Consolidar regras da Lei nº 6.530/1978, Código Civil (arts. 722–729), Resoluções COFECI e CDC (Lei nº 8.078/1990) sobre habilitação de corretores, comissão, publicidade e direitos do consumidor.
- **Gatilhos:** 'regras de anúncio de imóvel CRECI', 'quando o corretor tem direito à comissão', 'publicidade enganosa imóvel CDC', 'obrigação de colocar CRECI no anúncio'.

## Quando não usar
- Não usar para calcular rateio interno de comissão da equipe (usar `rt-sales/commission-calculation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Tipo de anúncio ou relação (venda, locação, lançamento) | Sim | Enum | Marketing / Comercial |
| Existência de autorização de venda/exclusividade | Sim | Booleano | Captação |
| Registro CRECI (PF ou PJ) | Sim | Texto | Cadastro |

## Processo
1. **Validar autorização escrita de intermediação** antes de anunciar qualquer imóvel (Res. COFECI 458/95) — Captação — Pré-anúncio.
2. **Incluir identificação obrigatória (CRECI)** em toda peça publicitária (site, portal, placa, rede social) — Marketing — Pré-publicação.
3. **Auditar veracidade das informações** (metragem privativa vs. total, valor, condomínio, IPTU, memorial descritivo) — Marketing / Jurídico — Pré-publicação.
4. **Garantir transparência na comissão** (quem paga e percentual destacado no contrato/proposta) — Comercial — Na proposta.

## Regras e critérios
- **Norma (Exercício Profissional e CRECI):** O exercício da profissão de Corretor de Imóveis é privativo dos inscritos no CRECI (Lei 6.530/78, art. 2º). É obrigatório constar o número de inscrição no CRECI (acompanhado da sigla CRECI e região, e 'J' para pessoa jurídica) em todo anúncio, impresso ou digital (Lei 6.530/78, art. 20, IV e Res. COFECI nº 1.065/2007).
- **Norma (Autorização de Anúncio):** É vedado ao corretor anunciar imóvel sem autorização escrita do proprietário (Res. COFECI nº 458/1995, art. 1º).
- **Norma (Direito à Comissão — CC, art. 725):** A remuneração é devida ao corretor uma vez que tenha conseguido o **resultado útil** previsto no contrato de mediação, ainda que este não se efetive em virtude de arrependimento das partes (salvo cláusula expressa em contrário ou desistência por vício oculto/documental não diligenciado pelo corretor).
- **Norma (Exclusividade — CC, art. 726):** Iniciado e concluído o negócio diretamente entre as partes, nenhuma remuneração será devida ao corretor; mas se, por escrito, for ajustada a corretagem com exclusividade, terá o corretor direito à remuneração integral, ainda que realizado o negócio sem a sua mediação, salvo se comprovada sua inércia ou ociosidade.
- **Norma (Código de Defesa do Consumidor — Lei 8.078/90):** Toda informação ou publicidade suficientemente precisa obriga o fornecedor que a fizer veicular e integra o contrato que vier a ser celebrado (art. 30). É proibida publicidade enganosa ou abusiva (art. 37). Na compra fora do estabelecimento comercial (ex.: stand de vendas improvisado ou 100% digital), aplica-se o direito de arrependimento em 7 dias (art. 49 e Lei 13.786/18, art. 67-A, §10). A transferência da comissão de corretagem ao comprador na planta é válida desde que previamente informada de forma clara e destacada o preço total e o valor destacado da comissão (Tema 938 STJ).
- **Canais de Reclamação:** PROCON estadual/municipal, Consumidor.gov.br e Tribunal de Ética e Disciplina do CRECI regional.

## Cálculos
Não aplicável (conformidade regulatória e ética; cálculos de comissão em `rt-sales/commission-calculation`).

## Saídas
Checklist de conformidade publicitária e contratual de intermediação.

## Aprovação humana
- Nenhuma campanha de lançamento imobiliário (incorporação) pode ser veiculada sem o número de registro do Memorial de Incorporação no CRI (Lei 4.591/64, art. 32, §3º) e validação jurídica.

## Repasses
- Segue para `rt-marketing/listing-copywriting` e `rt-sales/proposal-negotiation`.

## Erros comuns e riscos
- Anunciar imóvel 'captado por telefone' sem autorização escrita assinada (infração ética CRECI).
- Divulgar área total como se fosse área privativa, ou omitir número do RI em lançamento.
- Embutir comissão de corretagem na compra na planta sem destaque prévio no quadro-resumo (Tema 938 STJ).

## Casos de teste
1. **Normal:** 'O que precisa aparecer obrigatoriamente em um post de Instagram anunciando um apartamento?' -> Número do CRECI (PF ou PJ) e informações verídicas sobre o imóvel (metragem, valores), mediante autorização prévia de venda.
2. **Incompleto:** 'O proprietário vendeu direto para o cliente que eu levei. Tenho direito à comissão?' -> Pergunta se há comprovação da aproximação útil (ficha de visita assinada) e se houve desistência ou fechamento direto (CC arts. 725 e 727).
3. **Risco:** 'A construtora quer lançar um prédio na planta amanhã antes de sair o registro da incorporação no cartório.' -> Bloqueia a veiculação por contravenção penal (Lei 4.591/64, art. 66, I).

## Fontes
- Lei nº 6.530/1978 e Decreto nº 81.871/1978 — Planalto, acesso 2026-11-25.
- Código Civil — Lei nº 10.406/2002 (arts. 722–729) — Planalto, acesso 2026-11-25.
- Código de Defesa do Consumidor — Lei nº 8.078/1990 (arts. 30, 37, 49) e Tema 938 STJ — Planalto / STJ, acesso 2026-11-25.
- Lei de Incorporações — Lei nº 4.591/1964 (art. 32 e art. 66) — Planalto, acesso 2026-11-25.

## Pendências
- Tabelas referenciadas de honorários do CRECI estadual de atuação.
