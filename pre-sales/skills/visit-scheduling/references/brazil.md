---
plugin: rt-pre-sales
skill: visit-scheduling
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Pré-vendas / Operações
---

# Agendamento, Confirmação e Protocolo de Segurança em Visitas

## Objetivo e gatilhos
Organizar agenda de visitas presenciais ou virtuais, obter autorização do ocupante, enviar lembretes automáticos e aplicar protocolo de segurança física e registro de visita.
- **Gatilhos:** acionar `rt-pre-sales/visit-scheduling` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para vistoria técnica de engenharia ou entrega de chaves (`rt-property-management/move-inspections`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Imóvel, status de ocupação, disponibilidade do corretor e do cliente, documento de identificação do visitante. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Respeitar aviso prévio legal ao inquilino atual quando o imóvel estiver ocupado (ex.: 24h–48h nos EUA/EU; acordo prévio no BR Lei 8.245/91 art. 23, IX) — SDR — Pré-agendamento.
2. Coletar nome completo e documento com foto antes de visitas em imóveis vazios/isolados (protocolo de segurança do corretor) e ativar check-in/check-out no CRM — SDR/Corretor — Pré-visita.
3. Enviar confirmação 24h e 2h antes com endereço, ponto de encontro e regras do condomínio — Automação CRM — T-24h / T-2h.
4. Registrar ficha de visita assinada (prova de aproximação útil para corretagem) e feedback pós-visita — Corretor — Pós-visita.

## Regras e critérios
Norma: Inviolabilidade do domicílio (entrar em imóvel alugado sem consentimento do inquilino ou ordem judicial configura violação de domicílio / trespassing). Nos EUA, exigir Buyer Representation Agreement assinado antes da visita (regra pós-acordo NAR).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `visit-scheduling` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Pré-vendas / Operações**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `visit-scheduling` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `visit-scheduling` sem dados obrigatórios (Imóvel) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Pré-vendas / Operações ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
