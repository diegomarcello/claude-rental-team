---
plugin: rt-jurisdictions
skill: privacy
jurisdiction: europe
last_verified: 2026-11-25
confidence: verified
reviewer: European Data Protection Officer (DPO / CIPP/E)
---

# Jurisdiction Europe — Data Protection & Electronic Marketing (GDPR & ePrivacy)

## Objective & Triggers
Establish EU GDPR (Regulation (EU) 2016/679) and ePrivacy Directive (2002/58/EC) rules for tenant screening, lead generation, CCTV, data retention, Data Subject Access Requests (DSARs), and 72-hour breach notification.
- **Triggers:** 'GDPR rules tenant screening documents', '72 hour data breach GDPR', 'cold email B2C real estate Europe ePrivacy', 'how long keep tenant passport copy GDPR'.

## When Not to Use
- Do not use to populate company-specific ROPA entries (use `rt-legal/privacy-aml`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Processing activity (Lead outreach, Tenant vetting, Lease execution, CCTV) | Yes | Enum | Process |
| Data subject category (B2C consumer vs. B2B corporate contact) | Yes | Enum | CRM |
| Member State (for national supervisory authority / labor overlays) | Yes | Text | Operations |

## Process


## Rules & Criteria
- **EU Regulation (GDPR — Regulation (EU) 2016/679):**
  - *Lawful Bases (Art. 6):* Contract / pre-contractual steps at data subject's request (Art. 6(1)(b) — viewings, lease drafting); Legal obligation (Art. 6(1)(c) — tax/AML records); Legitimate interests (Art. 6(1)(f) — fraud prevention, existing client relationship, subject to LIA); Consent (Art. 6(1)(a) — freely given, specific, informed, unambiguous opt-in).
  - *Data Minimization (Art. 5(1)(c)):* European DPAs (CNIL in France, AEPD in Spain, CNPD in Portugal, BfDI/state DPAs in Germany) strictly sanction landlords/agencies demanding excessive documents during initial viewing/screening (e.g., bank statements showing spending habits, medical info, criminal records without statutory basis, or collecting full dossiers before viewing). In France, *Décret n° 2015-1437* establishes an **exhaustive statutory list** of documents a landlord may request from a tenant.
  - *DSAR Timeline (Art. 12(3)):* Respond without undue delay and within **1 month** of receipt (extendable by 2 months for complex requests).
  - *Breach Notification (Art. 33 & 34):* Notify national Supervisory Authority within **72 hours** of becoming aware; notify affected individuals without undue delay if high risk.
  - *Administrative Fines (Art. 83(5)):* Up to **€20,000,000** or **4% of total worldwide annual turnover**, whichever is higher.
- **EU Directive (ePrivacy — Directive 2002/58/EC, Art. 13):** Unsolicited commercial email/SMS/automated calls to natural persons (B2C) require **prior opt-in consent**, except for the 'soft opt-in' for similar products/services offered to existing customers with clear opt-out at every message.

## Calculations
**Key Statutory GDPR Timelines & Fine Ceilings:**
- Breach notification to DPA: $\le \mathbf{72\text{ hours}}$
- DSAR response deadline: $\le \mathbf{1\text{ month}}$
- Maximum fine tier: $\max(\mathbf{€20,000,000},\ \mathbf{4\%\text{ global annual turnover}})$

## Outputs
GDPR & ePrivacy compliance matrix covering lawful basis, document minimization rules, DSAR workflow, and 72h incident protocol.

## Human Approval Gates
- DPO must approve any cross-border data transfer outside the EEA (Standard Contractual Clauses + TIA), CCTV deployment, or breach notification to a Supervisory Authority.

## Handoffs
- Hands off to `rt-legal/privacy-aml`, `rt-property-management/tenant-screening`, and `rt-crm/crm-data-hygiene`.

## Common Errors & Risks
- Demanding full tax returns, bank statements, and ID copies from prospective tenants *before* they even attend a property viewing (violates GDPR Art. 5(1)(c) minimization and national rules like French Décret 2015-1437).
- Sending cold marketing emails/WhatsApp messages to individual property owners scraped from portals without prior consent.

## Test Cases
1. **Normal:** 'What is the deadline to report a personal data breach under GDPR?' -> Within 72 hours of becoming aware to the competent Supervisory Authority (unless unlikely to pose a risk to rights and freedoms).
2. **Incompleto:** 'What documents can we ask a tenant applicant for in Europe?' -> Explains GDPR Art. 5(1)(c) data minimization and highlights strict national lists (e.g., France Décret 2015-1437; Germany staged disclosure before vs. after viewing).
3. **Risco:** 'Scrape owner phone numbers from Idealista and send automated WhatsApp pitches.' -> Blocks immediately for violating GDPR Art. 6 and ePrivacy Art. 13.

## Sources
- General Data Protection Regulation — Regulation (EU) 2016/679 (arts. 5, 6, 12, 13, 33, 34, 83) — EUR-Lex, accessed 2026-11-25.
- ePrivacy Directive — Directive 2002/58/EC (art. 13) — EUR-Lex, accessed 2026-11-25.
- France Décret n° 2015-1437 (liste des pièces justificatives locataire) — Légifrance, accessed 2026-11-25.

## Pending Items
- Appoint EU DPO / Article 27 EU Representative if operating without an EU establishment.
