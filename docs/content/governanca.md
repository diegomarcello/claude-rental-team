# Governança e limites

O pacote apoia o trabalho da equipe. A responsabilidade pelas decisões continua sendo da empresa e dos profissionais habilitados.

## Aprovação humana

- Nenhuma operação financeira, assinatura ou comunicação regulatória ocorre sem aprovação de uma pessoa.
- Quem solicita não aprova nem executa o próprio pagamento.
- Contas da empresa ficam separadas das contas de clientes, proprietários e garantias.

Esses limites são instruções dadas ao modelo. Eles não substituem os controles de acesso dos bancos e sistemas da empresa.

## Dados pessoais

- Colete e informe o mínimo necessário à tarefa.
- O que é digitado ou anexado é processado pelo serviço Claude. Siga a política de dados da empresa e os termos do plano contratado.
- Use cópias anonimizadas como modelos.
- Confira nos arquivos de jurisdição os prazos legais de privacidade aplicáveis.

## O que roda no computador

| Item | O que faz |
|---|---|
| Aviso de configuração | Ao iniciar a sessão, lê apenas a tabela `Setup status` e informa os nomes dos itens pendentes. Grava um marcador na pasta de dados do plugin e não usa rede. |
| Scripts de cálculo | Executados quando a tarefa pede o cálculo. Recebem os valores informados e devolvem o resultado. |

## Estado do conteúdo

| Parte | Situação |
|---|---|
| Referências das skills | Presentes para os três recortes, pendentes de revisão profissional |
| Cálculos | Quatro scripts, somente para o Brasil |
| Modelos | Rascunhos brasileiros para parte do inventário; os demais têm apenas títulos |
| Fluxos | Sequência definida, sem responsáveis nem prazos |

## Problemas já identificados

| Área | Problema registrado |
|---|---|
| Estados Unidos, lavagem de dinheiro | A regra da FinCEN para imóveis residenciais aparece como vigente; a revisão interna registra anulação em 19/03/2026, com recurso pendente |
| Estados Unidos, privacidade | O consentimento individual da TCPA aparece como exigido; a revisão interna registra anulação em 24/01/2025 |
| Estados Unidos, locação | Há apoio em orientação do HUD que foi retirada |
| Jurisdições dos EUA e da Europa | A seção de processo está vazia nos arquivos de jurisdição |
| Brasil, financiamento | Um exemplo traz 3.394,54; para 0,80% ao mês o correto é 3.392,64 |
| Europa | Vários exemplos numéricos são norte-americanos |
| Cobrança | Há três réguas de atraso divergentes; a empresa precisa escolher a sua |

Os arquivos originais foram preservados, e as correções ficam nos problemas conhecidos de cada skill. A relação completa está na [revisão de conteúdo](https://github.com/diegomarcello/claude-rental-team/blob/main/CONTENT-REVIEW.md).

A indicação de confiança presente em um arquivo é uma declaração do autor do conteúdo, e não uma certificação.

## Antes de adotar na empresa

1. Concluir a configuração da empresa.
2. Obter revisão de advogado, contador e avaliador nas áreas que serão usadas.
3. Testar cada rotina com casos fictícios.
4. Definir responsáveis e prazos dos fluxos.
5. Registrar quem pode aprovar cada tipo de entrega.

## Perguntas frequentes

### Preciso instalar todos os departamentos?

Não. Instale a direção, as jurisdições e os departamentos que usa. Uma skill pode indicar a continuação em um departamento que precisa então ser instalado.

### Funciona sem o arquivo da empresa?

Funciona, mas as decisões internas aparecem como pendentes e o resultado fica incompleto.

### Posso alterar o conteúdo?

Sim, nos termos da licença GPL versão 2. Altere uma cópia do repositório, porque atualizações substituem os arquivos dos plugins instalados.

### Onde relato um erro?

No [repositório do projeto](https://github.com/diegomarcello/claude-rental-team), sem incluir dados de clientes.
