---
plugin: rt-property-management
skill: maintenance-requests
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Manutenção
---

# Triagem de Manutenção, Urgência e Responsabilidade (Locador vs. Locatário)

## Objetivo e gatilhos
Classificar chamados de manutenção por severidade (Emergência, Urgente, Rotina), definir responsabilidade financeira (estrutural/vício oculto = locador; mau uso/manutenção corriqueira = locatário) e acionar prestadores.
- **Gatilhos:** acionar `rt-property-management/maintenance-requests` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para reformas de grande porte (`rt-renovation/scope-of-work`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Descrição e fotos/vídeo do problema, tempo de ocupação, histórico do equipamento, limite de alçada pré-aprovado pelo proprietário. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Classificar urgência: Emergência (SLA <= 2–4h), Urgente (SLA <= 24–48h), Rotina (SLA <= 5 dias úteis) — Triagem — Imediato.
2. Determinar responsabilidade legal/contratual — Analista — Dia 0.
3. Acionar prestador homologado dentro da alçada pré-autorizada — Manutenção — Dia 0–1.
4. Validar conclusão com foto/aceite antes de liberar pagamento — Manutenção/Financeiro — Pós-serviço.

## Regras e critérios
Norma: Garantir habitabilidade e reparos urgentes é dever legal do locador (BR Lei 8.245/91 art. 22; US Implied Warranty of Habitability; EU tenancy statutes).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `maintenance-requests` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Manutenção**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `maintenance-requests` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `maintenance-requests` sem dados obrigatórios (Descrição e fotos/vídeo do problema) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Manutenção ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
