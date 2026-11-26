---
plugin: rt-jurisdictions
skill: privacy
jurisdiction: brazil
last_verified: 2026-11-25
confidence: verified
reviewer: Encarregado de Dados (DPO) / Advogado Digital
---

# Jurisdição Brasil — Privacidade e Proteção de Dados (LGPD — Lei nº 13.709/2018)

## Objetivo e gatilhos
Definir bases legais, regras de coleta, retenção, compartilhamento, direitos dos titulares, prospecção comercial e resposta a incidentes sob a LGPD no setor imobiliário.
- **Gatilhos:** 'regras LGPD imobiliária', 'posso mandar WhatsApp para lead sem consentimento', 'quanto tempo guardar documentos de inquilino', 'prazo comunicação vazamento ANPD'.

## Quando não usar
- Não usar para preencher o Registro de Operações de Tratamento (ROPA) específico da empresa (usar `rt-legal/privacy-aml`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Finalidade do tratamento (prospecção, visita, análise de crédito, contrato) | Sim | Enum | Processo |
| Categoria de dados (cadastrais, financeiros, biométricos/câmeras, menores) | Sim | Lista | Fluxo |
| Papel da empresa (Controladora ou Operadora) | Sim | Enum | Contrato |

## Processo
1. **Mapear fluxo de dados e definir base legal** (art. 7º ou art. 11 LGPD) antes de qualquer coleta — DPO / Jurídico — Pré-operação.
2. **Fornecer aviso de privacidade transparente** na captura de leads (formulário/WhatsApp) e na ficha cadastral — Marketing / Pré-vendas — No momento da coleta.
3. **Aplicar minimização e controle de acesso** aos documentos de análise de crédito (IRPF, holerites, certidões) — Locação / TI — Contínuo.
4. **Atender solicitações de titulares** (confirmação/acesso simplificado imediato; declaração completa em até **15 dias** — art. 19) — DPO — Até 15 dias.
5. **Comunicar incidentes de segurança** com risco ou dano relevante à ANPD e aos titulares em **3 dias úteis** (Resolução CD/ANPD nº 15/2024) — DPO / TI — Até 3 dias úteis.

## Regras e critérios
- **Norma (Bases Legais Aplicáveis no Imobiliário — Art. 7º):**
  - *Execução de contrato ou procedimentos preliminares (art. 7º, V):* Visitas, elaboração de proposta, contrato de locação/compra.
  - *Proteção do crédito (art. 7º, X):* Consulta a bureaus (Serasa/SPC) e análise documental para locação.
  - *Cumprimento de obrigação legal/regulatória (art. 7º, II):* Retenção de dados para DIMOB (Receita Federal) e PLD/COAF (Lei 9.613/98).
  - *Legítimo interesse (art. 7º, IX):* Prospecção B2B ou relacionamento com clientes ativos, exigindo LIA (Teste de Balanceamento) e opção fácil de *opt-out*.
  - *Consentimento (art. 7º, I):* Envio de newsletters/ofertas de terceiros para leads frios sem relação prévia.
- **Norma (Dados Sensíveis — Art. 11):** Reconhecimento facial em portarias/visitas ou dados de saúde exigem base específica do art. 11 (ex.: consentimento destacado ou prevenção à fraude/segurança).
- **Norma (Prazos de Incidentes — Res. CD/ANPD nº 15/2024):** Comunicação à ANPD e aos titulares em **3 dias úteis** contados do conhecimento do incidente com risco ou dano relevante (6 dias úteis para agentes de pequeno porte).
- **Norma (Sanções — Art. 52):** Advertência, multa simples de até **2% do faturamento** (limitada a R$ 50 milhões por infração), bloqueio ou eliminação dos dados.
- **Prática de Mercado:** Nunca compartilhar dossiê completo de inquilino (IRPF, contracheques) com o proprietário quando há seguro-fiança ou aprovação garantida; compartilhar apenas o parecer de aprovação, salvo previsão contratual estrita.
- **Decisão da Empresa:** `[PENDENTE: Nomeação formal do Encarregado (DPO) e tabela de temporalidade de descarte]`. 

## Cálculos
**Prazos Legais Críticos (LGPD / ANPD):**
- Resposta a pedido de acesso completo do titular: **15 dias corridos** (art. 19, II).
- Notificação de incidente relevante à ANPD e titulares: **3 dias úteis** (Res. CD/ANPD 15/2024, art. 6º).
- Guarda mínima fiscal/PLD (referência cruzada): **5 anos** após término da relação (Lei 9.613/98, art. 10, §2º e CTN, art. 173).

## Saídas
Tabela de mapeamento de base legal por etapa da jornada imobiliária + checklist de conformidade LGPD.

## Aprovação humana
- Qualquer comunicação externa à ANPD, compartilhamento de base de leads com parceiros ou implantação de biometria exige aprovação expressa do DPO e da Diretoria Jurídica.

## Repasses
- Segue para `rt-legal/privacy-aml`, `rt-crm/crm-data-hygiene` e `rt-marketing/lead-generation`.

## Erros comuns e riscos
- Comprar listas frias de contatos ('mailing de investidores') e disparar WhatsApp em massa sem base legal e sem opt-out.
- Pedir foto de certidão de nascimento de filhos ou antecedentes criminais sem finalidade legal estrita e proporcional.

## Casos de teste
1. **Normal:** 'Qual base legal usar para consultar o CPF de um candidato a inquilino no Serasa?' -> Proteção ao crédito (art. 7º, X) e procedimentos preliminares de contrato (art. 7º, V).
2. **Incompleto:** 'Quanto tempo devo guardar os contratos encerrados?' -> Explica necessidade de distinguir finalidade LGPD de obrigações legais (5 anos PLD/fiscal; prescrição cível 3 a 10 anos).
3. **Risco:** 'Um corretor perdeu um notebook sem criptografia com 400 fichas cadastrais e IRPF de clientes. O que fazer?' -> Aciona protocolo de incidente relevante (notificação à ANPD e titulares em até 3 dias úteis, contenção imediata).

## Fontes
- Lei Geral de Proteção de Dados — Lei nº 13.709/2018 (arts. 7º, 11, 18, 19, 48, 52) — Planalto, acesso 2026-11-25.
- Resolução CD/ANPD nº 15/2024 (Regulamento de Comunicação de Incidente de Segurança) — ANPD (`gov.br/anpd`), acesso 2026-11-25.

## Pendências
- Designação oficial do DPO e canal público de atendimento aos titulares.
