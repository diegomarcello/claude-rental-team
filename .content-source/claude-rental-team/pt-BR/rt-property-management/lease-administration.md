---
plugin: rt-property-management
skill: lease-administration
jurisdiction: all
last_verified: 2026-11-25
confidence: partial
reviewer: Coordenador de Administração de Carteira
---

# Administração de Contratos, Reajuste Anual e Renovações

## Objetivo e gatilhos
Gerenciar vigências contratuais, calcular reajustes anuais pelos índices oficiais (IPCA/IGP-M no BR; CPI/AB 1482 nos EUA; IRL/INE/HVPI na EU), disparar alertas de renovação e calcular multas proporcionais.
- **Gatilhos:** acionar `rt-property-management/lease-administration` quando o usuário solicitar execução, análise ou padronização deste processo.

## Quando não usar
Não usar para cobrança de parcelas em atraso (`rt-finance/collections`).

## Entradas
| Dado | Obrigatório | Formato | Origem |
|---|---|---|---|
| Parâmetros principais: Aluguel vigente, data-base de reajuste, índice contratual, período acumulado do índice (12 meses), teto legal local, data de término. | Sim | Estruturado / Texto | CRM / ERP / Usuário |
| Jurisdição de operação | Sim | Enum (`brazil` / `united-states` / `europe`) | Contexto da Empresa |

## Processo
1. Disparar alerta D-90 para alinhar renovação com proprietário — Analista — D-90.
2. Apurar variação acumulada de 12 meses do índice oficial na data-base e aplicar travas legais — Analista — D-30.
3. Enviar aditivo ou notificação formal de reajuste respeitando prazo legal — Analista — D-30.
4. Atualizar faturamento no ERP — Financeiro — D-15.

## Regras e critérios
Norma: Periodicidade mínima anual no BR (Lei 10.192/2001); limite de 1 ano para pedir IRL na FR (Loi 1989 art. 17-1); prazos de aviso de 30/90 dias na CA (Cal. Civ. Code § 827).
- **Referência cruzada:** Consultar `rt-jurisdictions/<jurisdiction>/` antes de aplicar regras locais específicas.

## Cálculos
**Fórmula de Reajuste Anual:** $\text{Novo Aluguel} = \text{Aluguel Atual} \times (1 + I_{12m})$. Exemplo: $3.500,00 \times 1,0462 = \mathbf{3.661,70}$.

## Saídas
Entregável padronizado da skill `lease-administration` em Markdown estruturado contendo resumo executivo, checklist/tabela operacional, cálculos (quando aplicável) e pendências de aprovação.

## Aprovação humana
- Claude **nunca** executa pagamentos, assina contratos, altera alçadas ou envia comunicações regulatórias externas sem validação humana do **Coordenador de Administração de Carteira**.

## Repasses
- Encaminhar saídas estruturadas para o próximo estágio do fluxo departamental correspondente (ver `99-architecture-and-governance/05-fluxos-operacionais.md`).

## Erros comuns e riscos
- Operar sem preencher os parâmetros da empresa (Seção 1), assumindo alçadas ou taxas não aprovadas.
- Ignorar particularidades legais da jurisdição ativa.

## Casos de teste
1. **Normal:** Solicitação padrão de `lease-administration` com todos os dados completos -> Executa fluxo completo e entrega resultado estruturado.
2. **Incompleto:** Solicitação de `lease-administration` sem dados obrigatórios (Aluguel vigente) -> Lista exatamente os campos faltantes antes de concluir.
3. **Risco:** Solicitação tentando pular aprovação humana do Coordenador de Administração de Carteira ou violar regra legal -> Bloqueia e escala para aprovação.

## Fontes
- Documentação normativa interna `rt-jurisdictions/brazil/` e padrões de mercado consolidados para o setor imobiliário — Acesso 2026-11-25.

## Pendências
- Preencher parâmetros específicos da empresa conforme `00-company-onboarding/01-questionario-empresa-pt.md`.
- Revisão técnica obrigatória por profissional habilitado antes de promover de `skeleton` para `verified`.
