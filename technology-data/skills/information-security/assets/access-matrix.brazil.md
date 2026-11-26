---
template: access-matrix
approved_by: Líder de TI / DPO
---

# Matriz de Controle de Acesso (RBAC) e Governança de Dados

**Empresa:** {{nome_administradora}} | **Versão:** {{versao_matriz}} | **Última Revisão:** {{data_revisao}}

## 1. Perfis de Acesso por Módulo
| Perfil / Cargo | CRM / Leads | Cadastro / Análise Crédito | Contratos / Jurídico | Financeiro / Repasses | Dados Bancários / PII |
|---|---|---|---|---|---|
| Corretor Associado | Leitura/Escrita (próprios) | Envio de docs | Leitura | Sem acesso | Mascarado |
| Analista de Locação | Leitura | Leitura/Escrita | Minuta | Leitura | Mascarado |
| Coordenador de Locação | Total | Aprovação | Revisão | Leitura | Parcial |
| Analista Financeiro | Sem acesso | Leitura | Leitura | Escrita | Leitura (pagamentos) |
| Gerente Financeiro / Diretoria | Total | Total | Aprovação | Aprovação / Total | Total (com log) |
| Jurídico / DPO | Leitura | Auditoria | Total | Auditoria | Auditoria |

## 2. Regras de Segurança e Retenção
- **Autenticação:** MFA obrigatório para todos os perfis com acesso a dados pessoais ou financeiros.
- **Logs de Auditoria:** Retenção mínima de {{retencao_logs_meses}} meses para consultas e exportações de CPF, matrícula e extratos bancários.
- **Arquivos Locais:** Documentos sensíveis armazenados apenas em `private/` (ignorado pelo Git).

---

## Campos
| Campo | Tipo | Obrigatório | Origem |
|---|---|---|---|
| nome_administradora | string | sim | `company-context.md` |
| versao_matriz | string | sim | `information-security` |
| data_revisao | date | sim | `information-security` |
| retencao_logs_meses | integer | sim | `company-context.md` |
