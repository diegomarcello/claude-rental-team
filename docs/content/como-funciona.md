# Como funciona

Cada departamento da empresa é um plugin independente. A empresa instala apenas os departamentos que usa, e o Claude passa a seguir os processos descritos neles.

## As peças

| Peça | O que é | Exemplo |
|---|---|---|
| Plugin | O pacote de um departamento | `rt-finance` |
| Skill | O roteiro de uma tarefa: entradas, processo, regras, aprovação e casos de teste | `rt-finance:collections` |
| Roteador | A skill que escolhe qual outra skill atende o pedido | `rt-finance:router-finance` |
| Agente | Um papel especializado que reúne uma ou mais skills | `rt-lease-admin` |
| Comando | Um atalho acionado somente pela pessoa | `/rt-finance:rt-owner-payout` |
| Referência | O conteúdo da skill para um país | `brazil.md` |
| Problemas conhecidos | Correções que prevalecem sobre a referência | `known-issues.md` |
| Jurisdições | Regras por país compartilhadas pelos departamentos | `rt-jurisdictions:jurisdiction-lookup` |
| Script | Um cálculo executado por programa, e não estimado | `accounts_receivable.py` |

## O caminho de um pedido

1. **Pedido.** A pessoa descreve a tarefa em linguagem comum ou usa um comando.
2. **Skill.** O Claude carrega a skill correspondente. Se duas servirem, o roteador pergunta qual.
3. **País.** A jurisdição é identificada. Se não estiver clara, o Claude pergunta.
4. **Referência.** O Claude lê apenas a referência daquele país e os problemas conhecidos.
5. **Empresa.** O Claude consulta o `company-context.md` do projeto e pergunta o que falta.
6. **Entrega.** O resultado traz o que foi feito, os cálculos com suas entradas e as pendências.
7. **Aprovação.** A entrega indica quem precisa aprovar. A decisão é sempre de uma pessoa.

## Três tipos de informação

O pacote procura separar, em cada resposta, três origens que têm pesos diferentes:

| Tipo | Origem | Como tratar |
|---|---|---|
| Regra legal | Referência do país | Conferir na fonte oficial antes de decidir |
| Prática de mercado | Referência do país | Avaliar se vale para a sua praça |
| Decisão da empresa | `company-context.md` confirmado | Vale como regra interna |

## Arquivos no projeto da empresa

O pacote é instalado no Claude Code. Os dados da empresa ficam na pasta de trabalho dela, fora dos plugins.

| Arquivo ou pasta | Conteúdo | Cuidado |
|---|---|---|
| `company-context.md` | Perfil, alçadas, taxas, políticas e tabela de confirmação | Nunca publicar |
| `company-templates/` | Modelos da empresa ou minutas aprovadas por ela | Usar cópias sem dados pessoais |
| `private/` | Documentos que não devem ser versionados | Manter fora do git |

## Confirmação das decisões da empresa

O `company-context.md` tem uma tabela chamada `Setup status`. Um item só vale como regra da empresa quando está como `confirmed` e registra quem confirmou.

| Situação | Significado |
|---|---|
| `pending` | Ainda não respondido. O Claude pergunta ou marca a lacuna. |
| `confirmed` | Uma pessoa identificada afirmou que é a regra real. |
| `not-applicable` | Não se aplica à empresa, com o motivo registrado. |

Valores preenchidos como exemplo não se tornam regra apenas por estarem no arquivo. Isso vale especialmente para a matriz de alçadas e a régua de cobrança.

## Países

| Região | Idioma da referência | Observação |
|---|---|---|
| Brasil | Português | Inclui o piloto de locação, com modelos em rascunho e cálculos |
| Estados Unidos | Inglês | Regras estaduais apenas onde o arquivo as cita |
| Europa | Inglês | Foco em Portugal, Espanha, Alemanha e França |

O Claude responde no idioma de quem pergunta.
