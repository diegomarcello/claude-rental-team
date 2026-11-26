---
plugin: rt-technology-data
skill: information-security
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: CISO / DPO
---

# Segurança da Informação, Controle de Acesso, Backup e Resposta a Incidentes

## Objetivo e gatilhos
Estabelecer políticas técnicas de segurança cibernética (MFA, RBAC, criptografia, backup 3-2-1 e plano de resposta a incidentes).
- **Gatilhos:** acionar `rt-technology-data/information-security` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para comunicação jurídica regulatória sem contenção técnica (`rt-jurisdictions/*/privacy`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Inventário de sistemas críticos, matriz RBAC, política de backup, contatos CSIRT. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Exigir MFA em 100% das contas e revisar acessos trimestralmente — TI/Segurança — Contínuo.
2. Manter criptografia AES-256 / TLS 1.3 e backup 3-2-1 — Infraestrutura — Contínuo.
3. Em incidentes: Conter (< 1h) -> Preservar logs -> Notificar DPO/Jurídico para cumprir prazos legais (72h GDPR / 3d úteis ANPD / 30d FTC) — CSIRT/DPO — Imediato.

## Regras e critérios
Norma: FTC Safeguards Rule (16 CFR Part 314), GDPR Art. 32, LGPD Art. 46, NIST CSF / ISO 27001.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Regra **3-2-1**: 3 cópias, 2 mídias distintas, 1 cópia off-site/imutável. RPO <= 24h; RTO <= 4h.

## Saídas
Entregável padronizado da skill `information-security` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **CISO / DPO**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `information-security` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `information-security` sem dados obrigatórios (Inventário de sistemas críticos) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do CISO / DPO ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
