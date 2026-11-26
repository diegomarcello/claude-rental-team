---
plugin: rt-marketing
skill: social-media
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Analista de Social Media / Jurídico
---

# Conteúdo para Redes Sociais e Direito de Imagem

## Objetivo e gatilhos
Planejar calendário editorial (Reels/TikTok, carrosséis educativos, tours de imóveis, prova social) respeitando direitos autorais de mídia, sigilo de imóveis ocupados e autorização de uso de imagem.
- **Gatilhos:** acionar `rt-marketing/social-media` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para tráfego pago de performance (`seo-paid-media`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Portfólio de imóveis autorizados, pilares de conteúdo da marca, autorizações de filmagem/imagem. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Confirmar autorização expressa do proprietário (e ciência do inquilino, se ocupado) antes de gravar vídeo interno — Captação/Marketing — Pré-gravação.
2. Desfocar placas de veículos, documentos pessoais, obras de arte identificáveis e fotos de família do morador — Edição — Pós-produção.
3. Coletar Termo de Autorização de Uso de Imagem de clientes/corretores participantes e incluir CRECI/licença — Marketing — Pré-postagem.

## Regras e critérios
Norma: Direito à imagem e privacidade (BR CF/88 art. 5º, X e CC art. 20; GDPR/LGPD para pessoas identificáveis; direitos autorais de trilhas sonoras comerciais em contas empresariais).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `social-media` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Analista de Social Media / Jurídico**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `social-media` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `social-media` sem dados obrigatórios (Portfólio de imóveis autorizados) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Analista de Social Media / Jurídico ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
