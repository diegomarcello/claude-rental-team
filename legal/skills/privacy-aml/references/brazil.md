---
plugin: rt-legal
skill: privacy-aml
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: DPO / Compliance Officer (MLRO)
---

# Governança de Privacidade (ROPA) e Prevenção à Lavagem de Dinheiro (KYC/AML)

## Objetivo e gatilhos
Operacionalizar o Registro de Operações de Tratamento de Dados (ROPA), fichas de diligência KYC/UBO, matriz de risco PLD e protocolos de reporte regulatório (ANPD/COAF, FinCEN/FTC, DPA/FIU).
- **Gatilhos:** acionar `rt-legal/privacy-aml` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para interpretar legislação abstrata sem caso concreto (`rt-jurisdictions/*/privacy` e `aml`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Identificação das partes (PF/PJ), documentos societários/UBO, origem dos recursos, canal de captação do dado, consentimentos. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Coletar ficha KYC e documentos de identificação/beneficiário final — Comercial/Compliance — Pré-contrato.
2. Cruzar listas PEP, OFAC/CSNU e avaliar sinais de alerta PLD — Compliance — Pré-contrato.
3. Registrar base legal LGPD/GDPR/CCPA no ROPA e aplicar política de retenção — DPO — Contínuo.
4. Escalar casos de alto risco ao MLRO/DPO para decisão ou reporte sigiloso — Compliance — Imediato.

## Regras e critérios
Norma: Manter dossiês KYC/AML por no mínimo 5 anos (10 anos na Espanha) em repositório criptografado com acesso restrito.
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
Não aplicável.

## Saídas
Entregável padronizado da skill `privacy-aml` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **DPO / Compliance Officer (MLRO)**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `privacy-aml` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `privacy-aml` sem dados obrigatórios (Identificação das partes (PF/PJ)) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do DPO / Compliance Officer (MLRO) ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
