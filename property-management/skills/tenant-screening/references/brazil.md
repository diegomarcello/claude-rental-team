---
name: tenant-screening
plugin: rt-property-management
jurisdiction: pt-BR
version: 1.0.0
---

# `tenant-screening` — Análise Cadastral e Risco de Locatário

## 1. Objetivo
Avaliar a capacidade financeira, idoneidade cadastral e adequação da garantia locatícia de pretendentes (Pessoa Física ou Jurídica) e fiadores, emitindo parecer fundamentado para aprovação ou recusa da locação.

## 2. Quando Usar
- Recebimento de proposta de locação com ficha cadastral e documentos comprobatórios.
- Substituição de fiador ou alteração de modalidade de garantia durante a vigência do contrato.

## 3. Entradas Necessárias
- Dados do imóvel e valor total do pacote mensal (aluguel + condomínio + IPTU + taxas).
- Ficha cadastral do pretendente (e fiador, se aplicável) com documentos de identificação e comprovação de renda/faturamento.
- Certidões negativas de protesto, consultas a birôs de crédito (SPC/Serasa) e distribuidores cíveis/executivos.
- Parâmetros de política de crédito definidos em `company-context.md`.

## 4. Processo de Execução
1. Validar completude documental e conformidade com o aviso de privacidade (LGPD, Art. 7º, V e X).
2. Calcular o pacote mensal total e verificar o múltiplo de renda líquida exigido em `company-context.md` (padrão >= 3,0x).
3. Verificar apontamentos restritivos (SPC/Serasa/protestos) e ações judiciais (especialmente despejo e execução).
4. Validar a suficiência da garantia única escolhida (Art. 37 da Lei nº 8.245/1991).
5. Gerar o parecer estruturado usando o template `tenant-screening-dossier.md`.

## 5. Regras de Jurisdição (Brasil)
- **Lei do Inquilinato (Lei nº 8.245/1991, Art. 37):** É nula a exigência de mais de uma modalidade de garantia no mesmo contrato.
- **LGPD (Lei nº 13.709/2018):** Tratar apenas dados estritamente necessários à análise de crédito e excluir documentos de cadastros reprovados no prazo definido em `company-context.md`.
- **Proibição de discriminação:** É vedada recusa baseada em origem, raça, sexo, idade, orientação sexual ou condição familiar.

## 6. Saídas
Entregável estruturado (`tenant-screening-dossier.md`) contendo:
- `protocolo_cadastro` (string): Identificador único da análise.
- `valor_pacote_mensal` (decimal BRL): Soma de aluguel, condomínio e IPTU.
- `renda_comprovada` (decimal BRL) e `multiplo_atingido` (decimal).
- `status_credito` (`CONFORME` | `NAO_CONFORME`) com detalhamento de apontamentos.
- `parecer_final` (`APROVADO` | `APROVADO_COM_CONDICIONANTE` | `REPROVADO`) e `justificativa_parecer`.

## 7. Repasses
- **Se `APROVADO` ou `APROVADO_COM_CONDICIONANTE`:** Encaminhar para `rt-legal/contract-drafting-review` enviando `protocolo_cadastro`, qualificação completa das partes, `modalidade_garantia` aprovada e condições comerciais.
- **Se `REPROVADO`:** Encaminhar para `rt-sales/lead-qualification` (ou corretor responsável) com motivo objetivo não discriminatório e solicitar nova garantia ou pretendente.

## 8. Limites e Alçadas
- A skill não aprova exceções à política de crédito (ex.: renda abaixo de 3,0x ou restrições acima do teto); exceções exigem aprovação formal conforme tabela de alçadas em `company-context.md`.

## 9. Erros Comuns e Riscos
- Calcular o múltiplo de renda apenas sobre o aluguel seco, ignorando condomínio e IPTU (risco de inadimplência precoce).
- Aceitar caução em dinheiro superior a 3 meses de aluguel (infração ao Art. 38, § 2º da Lei 8.245/91).
- Cumular fiador e caução no mesmo contrato (nulidade da segunda garantia).

## 10. Casos de Teste
1. **Aprovação padrão:** Pretendente PF com renda líquida de R$ 12.000,00 para pacote mensal de R$ 3.500,00 (múltiplo 3,43x), sem restrições SPC/Serasa, garantia Seguro Fiança → `parecer_final: APROVADO`.
2. **Aprovação com condicionante:** Pretendente PF com renda de R$ 8.200,00 para pacote de R$ 3.000,00 (múltiplo 2,73x < 3,0x), sem restrições, apresentando Título de Capitalização de 8x o pacote → `parecer_final: APROVADO_COM_CONDICIONANTE` (sujeito à alçada de exceção).
3. **Reprovação por ação de despejo:** Pretendente com renda de R$ 15.000,00 para pacote de R$ 3.200,00, porém com ação de despejo por falta de pagamento em curso nos últimos 12 meses → `parecer_final: REPROVADO`.

## 11. Fontes
- **Lei do Inquilinato (Lei nº 8.245/1991)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/leis/l8245.htm — Arts. 37 a 42 — Acesso em: 2026-11-25.
- **Lei Geral de Proteção de Dados (Lei nº 13.709/2018)** — Presidência da República — https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm — Arts. 7º e 9º — Acesso em: 2026-11-25.

## 12. Pendências
- Confirmar regras específicas de pontuação de score interno em `company-context.md` (Responsável: Coordenador de Locação).

## 13. Templates Associados
- `templates/brazil/property-management/tenant-screening/tenant-screening-dossier.md`
