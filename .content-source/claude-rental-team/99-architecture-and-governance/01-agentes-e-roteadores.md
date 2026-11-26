---
plugin: rt-architecture
skill: agents-and-routers
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Arquiteto de IA / Diretoria de Operações
---

# Catálogo de Agentes (42) e Roteadores Departamentais (15)

## 1. Roteadores Departamentais (15)
Cada um dos 15 plugins departamentais possui um roteador primário responsável por identificar intenção, validar jurisdição ativa (`brazil`, `united-states`, `europe`), checar parâmetros da empresa e despachar para o agente especialista:

| # | Plugin | Roteador | Jurisdições Carregadas Automaticamente |
|---|---|---|---|
| 1 | `rt-executive` | `router-executive` | Todas (consolidação multi-país) |
| 2 | `rt-acquisitions` | `router-acquisitions` | `sales-purchase`, `taxes`, `valuation-standards` |
| 3 | `rt-appraisal` | `router-appraisal` | `valuation-standards` |
| 4 | `rt-legal` | `router-legal` | Todas as 8 skills da jurisdição |
| 5 | `rt-renovation` | `router-renovation` | `construction-permits` |
| 6 | `rt-marketing` | `router-marketing` | `brokerage-advertising-consumer`, `privacy` |
| 7 | `rt-pre-sales` | `router-pre-sales` | `brokerage-advertising-consumer`, `privacy` |
| 8 | `rt-sales` | `router-sales` | `sales-purchase`, `brokerage-advertising-consumer`, `taxes` |
| 9 | `rt-crm` | `router-crm` | `privacy` |
| 10 | `rt-property-management` | `router-property-management` | `leasing`, `privacy` |
| 11 | `rt-post-sales` | `router-post-sales` | `sales-purchase`, `brokerage-advertising-consumer` |
| 12 | `rt-finance` | `router-finance` | `taxes`, `aml`, `leasing` |
| 13 | `rt-procurement` | `router-procurement` | `construction-permits` |
| 14 | `rt-human-resources` | `router-human-resources` | `brokerage-advertising-consumer`, `privacy` |
| 15 | `rt-technology-data` | `router-technology-data` | `privacy`, `aml` |

## 2. Catálogo dos 42 Agentes Especialistas
- **Executivo (3):** `agent-strategy-planner`, `agent-kpi-auditor`, `agent-governance-gatekeeper`
- **Aquisições (3):** `agent-deal-screener`, `agent-underwriting-modeler`, `agent-acquisition-negotiator`
- **Avaliação (4):** `agent-cma-valuer`, `agent-income-valuer`, `agent-cost-valuer`, `agent-building-inspector`
- **Jurídico & Compliance (5):** `agent-title-diligence`, `agent-contract-counsel`, `agent-tenancy-advisor`, `agent-eviction-litigator`, `agent-dpo-mlro`
- **Obras & Engenharia (3):** `agent-scope-architect`, `agent-cost-estimator`, `agent-site-supervisor`
- **Marketing (3):** `agent-campaign-strategist`, `agent-listing-copywriter`, `agent-growth-compliance`
- **Pré-vendas (2):** `agent-sdr-qualifier`, `agent-tour-coordinator`
- **Vendas (3):** `agent-offer-negotiator`, `agent-mortgage-simulator`, `agent-closing-coordinator`
- **CRM & RevOps (2):** `agent-pipeline-ops`, `agent-lifecycle-automator`
- **Administração de Locação (4):** `agent-tenant-underwriter`, `agent-lease-admin`, `agent-inspection-specialist`, `agent-maintenance-dispatcher`
- **Pós-venda (3):** `agent-handover-coordinator`, `agent-warranty-engineer`, `agent-ombuds-retention`
- **Financeiro & Fiscal (4):** `agent-ap-ar-controller`, `agent-collections-specialist`, `agent-treasury-forecaster`, `agent-owner-accounting-tax`
- **Compras & RH & TI (3):** `agent-procurement-leveler`, `agent-hr-licensing`, `agent-data-infosec`
