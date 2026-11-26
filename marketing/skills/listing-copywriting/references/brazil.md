---
plugin: rt-marketing
skill: listing-copywriting
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Marketing / Compliance
---

# Redação de Anúncios Imobiliários e Conformidade com Portais

## Objetivo e gatilhos
Criar títulos e descrições persuasivas e precisas para portais imobiliários e fichas comerciais, garantindo inclusão de dados obrigatórios e eliminação de termos proibidos ou discriminatórios.
- **Gatilhos:** acionar `rt-marketing/listing-copywriting` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para roteiros de redes sociais (`social-media`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Ficha técnica completa do imóvel (área privativa/útil, dormitórios, suítes, vagas, valor, condomínio, IPTU/tax, EPC na EU, CRECI/licença), diferenciais, público-alvo. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Validar informações obrigatórias da jurisdição (CRECI no BR; brokerage name/Equal Housing nos EUA; EPC A–G e honorários na EU) — Marketing — Pré-redação.
2. Redigir título orientado a benefícios + descrição estruturada (Resumo -> Planta/Ambientes -> Condomínio/Lazer -> Localização/Mobilidade -> Valores e Encargos) — Copywriter — Dia 1.
3. Rodar filtro de conformidade (Fair Housing / CDC / veracidade de metragem) antes de publicar — Coordenador — Pré-publicação.

## Regras e critérios
Norma: Proibido discriminação direta ou indireta (Fair Housing Act 42 U.S.C. § 3604(c); CF/88 art. 3º IV e CDC art. 37; Diretiva EU 2005/29/CE). Descrever exclusivamente características físicas do imóvel e infraestrutura do bairro, nunca o perfil demográfico do morador ideal.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `listing-copywriting` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Marketing / Compliance**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `listing-copywriting` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `listing-copywriting` sem dados obrigatórios (Ficha técnica completa do imóvel (área privativa/útil) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Marketing / Compliance ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
