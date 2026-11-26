---
name: contract-drafting-review
plugin: rt-legal
jurisdiction: pt-BR
version: 1.0.0
---

# `contract-drafting-review` — Elaboração e Revisão de Contratos Imobiliários

## 1. Objetivo
Redigir e revisar minutas de contratos de locação residencial, locação comercial e administração imobiliária em conformidade com a legislação brasileira e as políticas aprovadas da empresa.

## 2. Quando Usar
- Após aprovação cadastral (`tenant-screening`) e validação registral do imóvel (`title-due-diligence`).
- Na captação de novos imóveis para administração (`management-agreement`).
- Na revisão de minutas enviadas por terceiros (locatários corporativos ou proprietários).

## 3. Entradas Necessárias
- Dossiê de aprovação cadastral (`tenant-screening-dossier.md`).
- Matrícula atualizada do imóvel ou parecer registral (`registry-risk-opinion.md`).
- Condições comerciais negociadas (prazo, valor, índice de reajuste, dia de vencimento, garantia única).
- Parâmetros institucionais em `company-context.md`.

## 4. Processo de Execução
1. Verificar se há impeditivos registrais na matrícula do imóvel (penhora impeditiva, ausência de legitimidade do locador).
2. Selecionar o template adequado (`lease-agreement-residential.md`, `lease-agreement-commercial.md` ou `management-agreement.md`).
3. Preencher todas as cláusulas obrigatórias: qualificação, objeto, prazo, aluguel, índice de reajuste (sem deflação nominal), garantia única (Art. 37) e foro.
4. Revisar cláusulas atípicas (carência para obras, benfeitorias, built-to-suit) e sinalizar pontos para validação de advogado habilitado (OAB).

## 5. Regras de Jurisdição (Brasil)
- **Lei nº 8.245/1991:** Observância integral aos Arts. 4º (multa proporcional), 17 a 26 (aluguel e deveres), 35 (benfeitorias), 37 (garantia única) e 51 (renovatória comercial).
- **Código Civil (Lei nº 10.406/2002):** Capacidade das partes, representação e outorga conjugal quando aplicável (Art. 3º da Lei 8.245/91 para locação >= 10 anos).

## 6. Saídas
- Minuta contratual preenchida (`lease-agreement-residential.md`, `lease-agreement-commercial.md` ou `management-agreement.md`).
- Quadro-resumo de cláusulas críticas e lista de pontos pendentes de assinatura/registro.

## 7. Repasses
- **Após geração da minuta aprovada:** Encaminhar para `rt-property-management/move-inspections` (agendamento da vistoria de entrada antes da entrega de chaves) e `rt-property-management/lease-administration` (implantação do contrato no sistema financeiro).

## 8. Limites e Alçadas
- Alterações em cláusulas padrão de multa, isenção de garantia ou renúncia de direitos exigem aprovação do Jurídico e da Diretoria conforme `company-context.md`.

## 9. Erros Comuns e Riscos
- Omitir outorga conjugal em contratos com prazo igual ou superior a 10 anos (Art. 3º da Lei 8.245/91).
- Incluir cláusula de renúncia antecipada ao direito de preferência sem observar requisitos legais.
- Deixar campos de matrícula ou descrição do imóvel incompletos, inviabilizando futura averbação no Registro de Imóveis.

## 10. Casos de Teste
1. **Locação residencial padrão:** Contrato de 30 meses, aluguel R$ 3.500,00, IPCA, Seguro Fiança → Gera `lease-agreement-residential.md` com multa proporcional de 3 aluguéis (Art. 4º) e garantia única.
2. **Locação comercial de 60 meses:** Locatária PJ, aluguel R$ 12.000,00, locador PF → Gera `lease-agreement-commercial.md` incluindo cláusula de retenção de IRRF na fonte pela PJ e menção ao direito à ação renovatória (Art. 51).
3. **Contrato com prazo de 120 meses sem cônjuge:** Locador casado em comunhão parcial firmando contrato de 10 anos sem assinatura do cônjuge → Bloquear emissão final e exigir outorga conjugal (Art. 3º, Lei 8.245/91).

## 11. Fontes
- **Lei do Inquilinato (Lei nº 8.245/1991)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/l8245.htm — Arts. 3º, 4º, 35, 37 e 51 — Acesso em: 2026-11-25.
- **Código Civil (Lei nº 10.406/2002)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/2002/l10406compilada.htm — Arts. 104 e 421 — Acesso em: 2026-11-25.

## 12. Pendências
- Revisão final das minutas-padrão pelo advogado imobiliário da empresa (Responsável: Jurídico Imobiliário).

## 13. Templates Associados
- `templates/brazil/legal/contract-drafting-review/lease-agreement-residential.md`
- `templates/brazil/legal/contract-drafting-review/lease-agreement-commercial.md`
- `templates/brazil/legal/contract-drafting-review/management-agreement.md`
