---
plugin: rt-jurisdictions
skill: construction-permits
jurisdiction: brazil
last_verified: 2026-11-25
confidence: verified
reviewer: Engenheiro Civil / Arquiteto (CREA/CAU)
---

# Jurisdição Brasil — Licenças de Obra, Reforma em Condomínio (NBR 16280) e Segurança

## Objetivo e gatilhos
Estabelecer requisitos legais e normativos para reformas, alvarás municipais, responsabilidade técnica, segurança do trabalho e aprovação em condomínios no Brasil.
- **Gatilhos:** 'precisa de ART para reforma em apartamento', 'regras NBR 16280 reforma condomínio', 'alvará de reforma prefeitura', 'normas de segurança em obra NR 18'.

## Quando não usar
- Não usar para elaborar memorial descritivo de escopo (usar `rt-renovation/scope-of-work`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Tipo de imóvel (unidade em condomínio, casa de rua, comercial) | Sim | Enum | Cadastro |
| Escopo da intervenção (pintura/acabamento vs. demolição, elétrica, hidráulica, ar-condicionado, aumento de área) | Sim | Texto | Escopo |
| Município/UF | Sim | Texto | Cadastro |

## Processo
1. **Classificar intervenção** (manutenção simples sem alteração de sistema vs. reforma com impacto estrutural, elétrico, hidrossanitário, vedação ou fachada) — Engenheiro/Arquiteto — Dia 0.
2. **Providenciar ART (CREA) ou RRT (CAU)** e Plano de Reforma quando aplicável — Responsável Técnico — Dias 1 a 3.
3. **Protocolar junto ao Síndico** (em condomínios, conforme NBR 16280) e/ou **Prefeitura** (se houver acréscimo/demolição de área construída ou alteração de fachada) — Gestor de Obras — Dias 3 a 10.
4. **Garantir conformidade trabalhista e SST** (NR-18, NR-10, NR-35, PGR) antes do início físico — Técnico de Segurança / Empreiteiro — Pré-obra.

## Regras e critérios
- **Norma (Reformas em Edificações — ABNT NBR 16280:2024):** Toda reforma que altere ou comprometa a segurança da edificação ou de seu entorno (ex.: remoção/abertura de paredes, troca de revestimentos com uso de martelete, alterações elétricas/hidrossanitárias/gás, fechamento de sacada, instalação de ar-condicionado) exige **Plano de Reforma** acompanhado de **ART ou RRT** emitido por profissional habilitado, submetido previamente ao responsável legal da edificação (síndico).
- **Norma (Direito de Vizinhança e Condomínio — Código Civil):** O condômino não pode realizar obras que comprometam a segurança da edificação ou alterem a forma e a cor da fachada, das partes e esquadrias externas (CC, art. 1.336, II e III). Obras necessárias podem ser feitas pelo síndico; úteis exigem maioria dos condôminos; voluptuárias exigem 2/3 (CC, art. 1.341).
- **Norma (Alvará Municipal):** Pintura interna e troca de pisos sem alteração de área construída ou estrutura geralmente dispensam alvará municipal (dispensa de licença para pequenas reformas conforme Códigos de Obras municipais, ex.: Lei 16.642/2017 de São Paulo), mas acréscimo de área, mudança de uso ou intervenção estrutural exigem Alvará de Aprovação e Execução e posterior Certificado de Conclusão (Habite-se) + averbação no CRI e CNO (Cadastro Nacional de Obras — RFB).
- **Norma (Segurança do Trabalho):** NR-18 (Condições de Segurança e Saúde no Trabalho na Indústria da Construção), NR-35 (Trabalho em Altura > 2,00m) e NR-10 (Instalações Elétricas).
- **Penalidades:** Embargo administrativo da obra pelo síndico ou prefeitura, multa condominial/municipal e responsabilidade civil e criminal objetiva por danos estruturais.

## Cálculos
Não aplicável (regras qualitativas e enquadramento regulatório; prazos variam por município).

## Saídas
Matriz de licenciamento e documentação exigida (Prefeitura, Condomínio, CREA/CAU, Receita Federal CNO).

## Aprovação humana
- Nenhuma obra que envolva demolição, elétrica, hidráulica ou carga estrutural pode iniciar sem ART/RRT assinada e ciência formal do síndico/prefeitura.

## Repasses
- Segue para `rt-renovation/scope-of-work` e `rt-renovation/works-schedule`.

## Erros comuns e riscos
- Iniciar troca de piso com martelete em apartamento apenas com 'aviso ao zelador', sem ART/RRT (risco de dano em laje protendida ou alvenaria estrutural).
- Alterar esquadria de varanda sem aprovação em assembleia de condomínio.

## Casos de teste
1. **Normal:** 'Vou reformar um apartamento trocando piso, pontos elétricos e quebrando uma parede da cozinha. O que preciso?' -> Exige Plano de Reforma + ART/RRT + projeto estrutural atestando que a parede não é estrutural + entrega ao síndico (NBR 16280).
2. **Incompleto:** 'Preciso de alvará para reformar um imóvel?' -> Pergunta município, tipo de imóvel (casa ou condomínio) e detalhamento do escopo.
3. **Risco:** 'O construtor disse que o prédio é antigo e não precisa de ART para quebrar uma parede interna.' -> Bloqueia a execução e alerta sobre risco de colapso estrutural (alvenaria estrutural) e ilegalidade perante a NBR 16280.

## Fontes
- ABNT NBR 16280:2024 (Reforma em edificações — Sistema de gestão de reformas) — ABNT, acesso 2026-11-25.
- Código Civil Brasileiro — Lei nº 10.406/2002 (arts. 1.336 e 1.341) — Planalto, acesso 2026-11-25.
- NR-18 e NR-35 — Ministério do Trabalho e Emprego (`gov.br/trabalho-e-emprego`), acesso 2026-11-25.

## Pendências
- Regras específicas dos Códigos de Obras dos municípios onde a empresa realiza flipping/incorporação.
