---
plugin: rt-jurisdictions
skill: construction-permits
jurisdiction: europe
last_verified: 2026-11-25
confidence: verified
reviewer: European Architect / Chartered Building Surveyor
---

# Jurisdiction Europe — Building Permits, Energy Performance (EPBD), Heritage & Condominium Rules

## Objective & Triggers
Establish European building permit requirements, Energy Performance of Buildings Directive (EPBD) renovation obligations, heritage protections, and condominium/co-ownership rules.
- **Triggers:** 'building permit renovation Portugal Spain France Germany', 'EU EPBD energy efficiency renovation rules', 'condominium approval renovation Europe'.

## When Not to Use
- Do not use to write detailed renovation bills of quantities (use `rt-renovation/scope-of-work`).

## Inputs
| Input | Required | Format | Source |
|---|---|---|---|
| Country & Municipality | Yes | Text | Property Record |
| Scope (Interior non-structural vs. structural, facade, MEP, change of use) | Yes | Text | Scope |
| Building status (Listed heritage monument, historic center, co-ownership/condominium) | Yes | Enum | Title / Cadastre |

## Process


## Rules & Criteria
- **EU Directive (EPBD — Directive (EU) 2024/1275):** Major renovations must meet minimum energy performance requirements where technically and economically feasible; Member States must phase out fossil-fuel boilers and progressively renovate worst-performing buildings.
- **EU Directive (Temporary or Mobile Construction Sites — Directive 92/57/EEC):** Requires appointment of a Health & Safety Coordinator (*Coordinateur SPS* in FR; *SiGeKo* in DE; *Coordinador de Seguridad y Salud* in ES) whenever multiple contractors operate on site.
- **Country Rules:**
  - *Portugal (RJUE — DL n.º 555/99, amended by Simplex Urbanístico DL n.º 10/2024):* Interior works not affecting structure, facade, or roof shape are exempt from prior municipal control (*obras isentas*), though condominium rules (CC art. 1422) prohibit altering architectural lines or aesthetic arrangement without 2/3 assembly approval.
  - *Spain (LOE — Ley 38/1999 & Ley de Propiedad Horizontal):* *Obra menor* (cosmetic/non-structural) typically proceeds via *Declaración Responsable* or *Comunicación Previa*; *Obra mayor* (structural, layout expansion, facade) requires architect project (*proyecto visado*) and municipal *Licencia de Obra Mayor* + *ICIO* tax. Condominium structural/facade alterations require community consent (LPH art. 7 & 10).
  - *Germany (Landesbauordnungen — LBO & WEG):* *Verfahrensfreie Vorhaben* covers minor interior finishes, but structural changes, roof windows, or change of use (*Nutzungsänderung*) require *Baugenehmigung*. Under *Wohnungseigentumsgesetz* (WEG § 20), structural alterations affecting common property require owner resolution (*Beschluss*).
  - *France (Code de l'urbanisme & Loi du 10 juillet 1965):* Exterior appearance changes (windows, shutters, heat pumps on facade) require *Déclaration Préalable de Travaux* (DP) at the *Mairie*; extensions > 20m² (or 40m² in urban zones) require *Permis de Construire*. Any work touching common parts or exterior appearance in a *copropriété* requires prior *Assemblée Générale* vote (Art. 25/26).

## Calculations
Not applicable (regulatory & permitting rules).

## Outputs
Country-specific permitting path, condominium voting requirement, and H&S coordinator checklist.

## Human Approval Gates
- Claude **never** authorizes structural demolition, facade modification, or change of use without a licensed local Architect/Engineer sign-off and issued municipal/co-ownership approvals.

## Handoffs
- Hands off to `rt-renovation/scope-of-work` and `rt-renovation/works-schedule`.

## Common Errors & Risks
- Replacing windows or installing external AC/heat-pump units in Paris, Lisbon, or Madrid historic centers without municipal heritage and co-ownership approval (frequently results in mandatory removal orders).

## Test Cases
1. **Normal:** 'We want to replace windows and install a heat pump on the exterior facade of a Paris apartment. What approvals are needed?' -> Copropriété General Assembly vote (Art. 25) + municipal *Déclaration Préalable*.
2. **Incompleto:** 'Do we need a building permit in Portugal for an apartment remodel?' -> Asks whether work is purely interior non-structural (*isenta* under RJUE) or alters structure, facade, or use.
3. **Risco:** 'Begin gutting load-bearing walls in a Madrid building today and file the Licencia de Obra Mayor next month.' -> Blocks work immediately; requires *proyecto visado*, municipal license, and community approval beforehand.

## Sources
- EU Energy Performance of Buildings Directive (EU) 2024/1275 & Construction Sites Directive 92/57/EEC — EUR-Lex, accessed 2026-11-25.
- Portugal RJUE (DL 555/99 & DL 10/2024); Spain LOE (Ley 38/1999) & LPH; Germany LBO & WEG § 20; France Code de l'urbanisme & Loi 65-557 — National Gazettes, accessed 2026-11-25.

## Pending Items
- Municipal heritage overlay maps for target European cities.
