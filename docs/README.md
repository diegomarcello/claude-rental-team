# Documentação e site

Apresentação do pacote em português, publicada como site estático.

| Caminho | Conteúdo |
|---|---|
| `content/*.md` | Texto das páginas. Edite aqui. |
| `build.py` | Gera os arquivos `.html` a partir do texto e do repositório. |
| `assets/` | Estilo, ícone e o botão de copiar. |
| `*.html` | Gerados. Não edite à mão. |

## Gerar

```bash
python3 docs/build.py
python3 -m unittest discover -s tests
```

Gere novamente depois de editar o texto ou de mudar plugins, skills, comandos, agentes ou fluxos. O catálogo e os fluxos são lidos do repositório. O teste falha se os arquivos `.html` estiverem desatualizados.

## Ver localmente

Abra `docs/index.html` no navegador.

## Publicar no GitHub Pages

1. Envie a pasta para a branch `main`.
2. No repositório, abra **Settings → Pages**.
3. Em **Source**, escolha **Deploy from a branch**, branch `main`, pasta `/docs`.

O site fica público. Não coloque nesta pasta dados da empresa, de clientes ou de pessoas.
