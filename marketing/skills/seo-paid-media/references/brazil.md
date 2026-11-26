---
plugin: rt-marketing
skill: seo-paid-media
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Especialista de Performance / Compliance
---

# SEO Local e Mídia Paga com Restrições Habitacionais

## Objetivo e gatilhos
Gerenciar SEO local (Google Business Profile, páginas de bairros) e campanhas pagas (Google Ads, Meta Ads) em total conformidade com políticas de categoria especial de moradia (Housing Special Ad Category).
- **Gatilhos:** acionar `rt-marketing/seo-paid-media` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para redação de anúncios em portais (`listing-copywriting`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Palavras-chave alvo, bairros de atuação, orçamento de mídia, landing pages, pixels/conversões offline. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Ativar obrigatoriamente a categoria 'Habitação / Housing' na Meta Ads (e restrições equivalentes no Google Ads), removendo segmentação por idade, gênero, CEP restrito ou interesses discriminatórios — Gestor de Tráfego — Setup.
2. Otimizar Google Business Profile e páginas locais por tipologia + bairro — Especialista SEO — Contínuo.
3. Configurar envio de conversões offline do CRM (visita realizada, proposta, contrato) para otimizar CPA real e não apenas lead bruto — Performance/TI — Contínuo.

## Regras e critérios
Norma / Política de Plataforma: Meta Housing Special Ad Category e Google Ads Housing Policy proíbem segmentação por CEP/código postal (exige raio mínimo de 15 milhas/km), idade, sexo ou públicos semelhantes (Lookalike) baseados em atributos protegidos, em cumprimento ao Fair Housing Act e leis antidiscriminação.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `seo-paid-media` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Especialista de Performance / Compliance**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `seo-paid-media` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `seo-paid-media` sem dados obrigatórios (Palavras-chave alvo) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Especialista de Performance / Compliance ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
