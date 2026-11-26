---
plugin: rt-crm
skill: customer-segmentation
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Gerente de CRM / DPO
---

# Segmentação de Clientes e Atributos Permitidos

## Objetivo e gatilhos
Segmentar compradores, inquilinos e proprietários por comportamento, perfil de portfólio e objetivo financeiro sem utilizar atributos sensíveis ou discriminatórios.
- **Gatilhos:** acionar `rt-crm/customer-segmentation` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para disparos em massa sem consentimento (`journey-automation`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Base de contatos CRM, histórico de transações/visitas, preferências de imóvel, perfil de proprietário. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Criar segmentos dinâmicos baseados em comportamento e capacidade objetiva — RevOps — Setup.
2. Bloquear criação de tags ou campos personalizados referentes a atributos protegidos — DPO/RevOps — Governança.
3. Vincular cada segmento a ofertas e comunicações relevantes — Marketing/CRM — Contínuo.

## Regras e critérios
Norma: Fair Housing Act, LGPD art. 11 e GDPR art. 9º proíbem tratamento discriminatório ou coleta de dados sensíveis sem base estrita.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `customer-segmentation` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Gerente de CRM / DPO**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `customer-segmentation` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `customer-segmentation` sem dados obrigatórios (Base de contatos CRM) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Gerente de CRM / DPO ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
