# `claude-rental-team` — Base de Conhecimento Operacional e Jurídica (Brasil, EUA e Europa)

Este pacote contém a arquitetura completa e os arquivos Markdown estruturados do ecossistema **`claude-rental-team`**, organizados em **3 idiomas/jurisdições** (`pt-BR`, `en-US`, `en-EU`), cobrindo:

- **`00-company-onboarding/`**: Questionário de parametrização da empresa (Seção 1 — PT-BR e EN) para preencher geografia, linhas de negócio, stack tecnológico, alçadas, políticas e regime tributário.
- **`pt-BR/` (Brasil — Português)**:
  - `rt-jurisdictions/brazil/` (8 arquivos): Compra e Venda, Locação (Lei 8.245/91), Tributação & Reforma Tributária (LC 214/2025), Avaliação (NBR 14653/COFECI), Obras (NBR 16280), Privacidade (LGPD), PLD/AML (COAF/COFECI) e Corretagem/CDC.
  - 15 plugins departamentais completos (55 arquivos Markdown no padrão de 13 seções).
- **`en-US/` (United States — English)**:
  - `rt-jurisdictions/united-states/` (8 files): Sales/Title/Escrow/FIRPTA (FL/TX/CA), Leasing & Fair Housing/SCRA/AB 1482, Taxation (MACRS/1031/State), USPAP Appraisal Standards, Building Permits/OSHA/EPA RRP/Lien Waivers, Privacy (TCPA/CCPA/FCRA/Safeguards), AML (FinCEN Real Estate Rule/Form 8300/OFAC), and Brokerage/NAR Settlement/RESPA § 8.
  - 15 departmental plugins (55 Markdown files in the 13-section schema).
- **`en-EU/` (Europe — English)**:
  - `rt-jurisdictions/europe/` (8 files): Conveyance/Notaries/MCD (PT/ES/DE/FR), Tenancy/Rent Caps/Eviction (NRAU/LAU/BGB/Loi 1989), Taxation/VAT/10-yr Rule/IRNR/LMNP, Valuation (RICS Red Book/TEGoVA/ImmoWertV), Permits/EPBD/Condominiums, Privacy (GDPR/ePrivacy), AML (AMLD5/AMLR €10k rental threshold/cash caps), and Brokerage/EPC Ads/Bestellerprinzip/Loi Hoguet.
  - 15 departmental plugins (55 Markdown files in the 13-section schema).
- **`99-architecture-and-governance/`**: Catálogo dos 42 Agentes, 15 Roteadores, 21 Comandos, 48 Templates, 6 Fluxos End-to-End e 6 Padrões Corporativos.

## Próximos Passos Recomendados
1. Preencher `00-company-onboarding/01-questionario-empresa-pt.md` (e/ou versão em inglês).
2. Submeter os arquivos de `rt-jurisdictions/` e os cálculos financeiros/tributários à revisão do Jurídico e Contador locais para promover `confidence` de `partial` para `verified`.
3. Conectar os servidores MCP do CRM, ERP/PMS, Assinatura Eletrônica e Repositório documental.
