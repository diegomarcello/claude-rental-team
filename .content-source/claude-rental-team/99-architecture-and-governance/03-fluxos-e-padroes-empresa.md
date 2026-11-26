---
plugin: rt-architecture
skill: end-to-end-flows-and-standards
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Diretoria Executiva / Operações
---

# Fluxos Operacionais End-to-End (6) e Padrões Corporativos (6)

## 1. Os 6 Fluxos Integrados End-to-End
1. **Fluxo 1 — Captação, Marketing e Venda (Intermediação):**
   `rt-marketing/campaign-planning` -> `rt-legal/contract-drafting-review` (Autorização/Mandato) -> `rt-appraisal/comparative-market-analysis` -> `rt-marketing/listing-copywriting` -> `rt-pre-sales/lead-qualification` -> `rt-pre-sales/visit-scheduling` -> `rt-sales/proposal-negotiation` -> `rt-legal/title-due-diligence` + `rt-legal/privacy-aml` -> `rt-sales/closing-checklist` -> `rt-finance/accounts-receivable` + `rt-sales/commission-calculation` -> `rt-post-sales/property-handover` + `customer-retention`.
2. **Fluxo 2 — Compra, Reforma e Revenda (House Flipping):**
   `rt-acquisitions/opportunity-screening` -> `rt-appraisal/technical-inspection` + `comparative-market-analysis` -> `rt-legal/title-due-diligence` -> `rt-acquisitions/deal-feasibility` -> `rt-executive/approval-gates` -> `rt-acquisitions/purchase-negotiation` -> `rt-renovation/scope-of-work` + `renovation-budget` -> `rt-procurement/quote-comparison` + `vendor-management` -> `rt-renovation/works-schedule` + `works-quality-inspection` -> `rt-marketing/listing-copywriting` -> Venda (Fluxo 1).
3. **Fluxo 3 — Locação Ponta a Ponta (Onboarding ao Repasse):**
   Captação & Vistoria Entrada (`rt-property-management/move-inspections`) -> Anúncio (`rt-marketing/listing-copywriting`) -> Qualificação & Visita (`rt-pre-sales`) -> Análise de Crédito (`rt-property-management/tenant-screening`) -> Contrato & Garantia (`rt-legal/contract-drafting-review`) -> Faturamento Mensal (`rt-finance/accounts-receivable`) -> Repasse Proprietário (`rt-finance/owner-payouts`) -> Reajuste Anual (`rt-property-management/lease-administration`).
4. **Fluxo 4 — Inadimplência, Cobrança e Despejo:**
   Atraso D+1 (`rt-finance/accounts-receivable`) -> Régua Amigável D+1 a D+30 (`rt-finance/collections`) -> Notificação Extrajudicial & Acordo ou Despejo (`rt-legal/disputes-eviction`) -> Vistoria de Saída & Apuração Caução (`rt-property-management/move-inspections`) -> Encerramento Contábil (`rt-finance/financial-close`).
5. **Fluxo 5 — Manutenção e Garantias Pós-Entrega:**
   Chamado (`rt-property-management/maintenance-requests` ou `rt-post-sales/warranty-claims`) -> Classificação Urgência & Responsabilidade -> Cotação/Prestador Homologado (`rt-procurement/vendor-management`) -> Execução & Aceite -> Pagamento 3-Way Match (`rt-finance/accounts-payable`) -> Lançamento Extrato Proprietário (`rt-finance/owner-payouts`).
6. **Fluxo 6 — Governança, Fechamento Mensal e Auditoria:**
   Conciliação Diária (`rt-finance/accounts-receivable`) -> Fechamento D+5 (`rt-finance/financial-close`) -> KPIs Executivos (`rt-executive/company-kpis`) -> Fluxo de Caixa 13 Semanas (`rt-finance/cash-flow-forecast`) -> BI & Segurança (`rt-technology-data/bi-reporting` + `information-security`).

## 2. Os 6 Padrões Obrigatórios da Empresa
1. **Padrão de Qualidade Documental (`schema-standard`):** Toda skill e entregável segue frontmatter YAML + 13 seções padronizadas com separação explícita entre Norma Legal, Prática de Mercado e Decisão da Empresa.
2. **Padrão de Segregação de Funções e Alçadas (`approval-gates-standard`):** Nenhuma transação financeira, assinatura contratual ou reporte regulatório ocorre sem aprovação humana segregada.
3. **Padrão de Privacidade e Minimização (`privacy-by-design-standard`):** Coleta mínima, consentimento auditável, mascaramento de PII em BI e cumprimento estrito de prazos legais (72h GDPR / 3d úteis ANPD / 30d FTC).
4. **Padrão de Integridade Fiduciária (`trust-accounting-standard`):** Segregação absoluta entre contas próprias da empresa e contas vinculadas de clientes/proprietários/cauções.
5. **Padrão de Comunicação Inclusiva e Ética (`fair-housing-ethics-standard`):** Tolerância zero a discriminação direta ou indireta em anúncios, triagem de leads, análise de crédito e recrutamento.
6. **Padrão de Versionamento e Revisão Jurídica (`verified-governance-standard`):** Nenhuma skill é promovida a `confidence: verified` sem revisão assinada por profissional habilitado na jurisdição correspondente e preenchimento da Seção 1 pela empresa.
