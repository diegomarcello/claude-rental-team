# Primeiros passos

A instalação é feita dentro do Claude Code. Em seguida, a empresa registra suas próprias decisões antes do primeiro uso real.

## Requisitos

- Claude Code instalado e autenticado.
- `python3` disponível no computador, para o aviso de configuração e para os cálculos.
- Uma pasta de trabalho da empresa, separada deste repositório.

## 1. Adicionar o catálogo

Abra o Claude Code na pasta da empresa e execute:

```
/plugin marketplace add diegomarcello/claude-rental-team
```

## 2. Instalar os plugins

Instale primeiro a direção e as jurisdições, porque os demais se apoiam nelas:

```
/plugin install rt-executive@claude-rental-team
/plugin install rt-jurisdictions@claude-rental-team
```

Depois, instale os departamentos do seu tipo de operação.

| Operação | Plugins adicionais |
|---|---|
| Administração de locação | `rt-property-management`, `rt-finance`, `rt-legal`, `rt-marketing`, `rt-pre-sales` |
| Venda e corretagem | `rt-marketing`, `rt-pre-sales`, `rt-sales`, `rt-appraisal`, `rt-legal`, `rt-finance`, `rt-post-sales` |
| Compra, reforma e revenda | `rt-acquisitions`, `rt-appraisal`, `rt-legal`, `rt-renovation`, `rt-procurement`, `rt-marketing`, `rt-finance` |

Cada departamento é instalado com o mesmo formato:

```
/plugin install rt-property-management@claude-rental-team
/plugin install rt-finance@claude-rental-team
/plugin install rt-legal@claude-rental-team
```

A lista completa está em [Departamentos](departamentos.md). Se o Claude Code pedir, reinicie a sessão para carregar os plugins.

## 3. Configurar a empresa

```
/rt-executive:company-setup
```

A configuração pergunta, um bloco por vez:

| Item | O que informar |
|---|---|
| Contexto da empresa | Identificação, praças, linhas de negócio, responsáveis, taxas, garantias, prazos e sistemas |
| Alçadas de aprovação | Cada linha da matriz: operação, limite, quem solicita, quem aprova e evidência |
| Régua de cobrança | Dias, ação, canal, responsável, aprovador e prazo de aviso ao garantidor |
| Modelos de locação | Notificação de cobrança, aging de recebíveis, resumo do contrato, registro de vistoria e ficha do pretendente |

Para cada modelo, é possível indicar um documento próprio sem dados pessoais, pedir uma minuta para revisão, deixar para depois ou marcar que não se aplica. Responder "depois" é sempre permitido: o item fica pendente.

> **Quando o aviso aparece.** O Claude Code não executa nada durante a instalação. O `rt-executive` mostra um lembrete na primeira sessão depois de instalado e volta a mostrá-lo enquanto o `company-context.md` do projeto tiver pendências. As skills de locação também perguntam o que precisam no momento do uso.

## 4. Proteger os dados

Se a pasta da empresa for um repositório git, inclua no arquivo `.gitignore`:

```
/company-context.md
/private/
```

Avalie também se `company-templates/` deve ficar fora do repositório.

## 5. Conferir

- Execute `/plugin` e confirme que os departamentos aparecem como instalados.
- Abra o `company-context.md` e revise a tabela `Setup status`.
- Faça um pedido de teste com dados fictícios, como os de [Uso no dia a dia](dia-a-dia.md).

## Atualizações

```
/plugin marketplace update claude-rental-team
```

Depois, atualize os plugins instalados pelo menu `/plugin`. Os arquivos da empresa ficam na pasta de trabalho e não são substituídos.
