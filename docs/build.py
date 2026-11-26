#!/usr/bin/env python3
"""Build the documentation site: docs/content/*.md -> docs/*.html.

Standard library only. The department catalog and the workflows are read from
the repository, so run this again after changing plugins:  python3 docs/build.py
"""
import html
import json
import re
import unicodedata
from pathlib import Path

DOCS = Path(__file__).resolve().parent
ROOT = DOCS.parent
REPOSITORY = "https://github.com/diegomarcello/claude-rental-team"

# file name (without extension) and menu label, in reading order
PAGES = (
    ("index", "Visão geral"),
    ("como-funciona", "Como funciona"),
    ("primeiros-passos", "Primeiros passos"),
    ("dia-a-dia", "Uso no dia a dia"),
    ("fluxos", "Fluxos de trabalho"),
    ("departamentos", "Departamentos"),
    ("governanca", "Governança e limites"),
)

DEPARTMENTS = {
    "executive": ("Direção", "Configuração da empresa, planejamento, indicadores, alçadas e encaminhamento entre áreas."),
    "acquisitions": ("Aquisições", "Busca e triagem de oportunidades, viabilidade e negociação de compra."),
    "appraisal": ("Avaliação", "Métodos de mercado, renda e custo, além de vistoria técnica."),
    "legal": ("Jurídico", "Due diligence, contratos, direito locatício, litígios, privacidade e prevenção à lavagem de dinheiro."),
    "renovation": ("Reformas", "Escopo, orçamento, cronograma e qualidade das obras."),
    "marketing": ("Marketing", "Campanhas, anúncios, conteúdo, mídia paga e captação de leads."),
    "pre-sales": ("Pré-vendas", "Qualificação de leads, visitas e acompanhamento."),
    "sales": ("Vendas", "Propostas, financiamento, fechamento e comissões."),
    "crm": ("CRM", "Funil, segmentação, qualidade de dados e jornadas automatizadas."),
    "property-management": ("Administração de imóveis", "Locação, inquilinos, vistorias, manutenção e condomínio."),
    "post-sales": ("Pós-venda", "Entrega de chaves, garantias, reclamações e retenção."),
    "finance": ("Financeiro", "Pagamentos, recebimentos, cobrança, caixa, repasses, fechamento e tributos."),
    "procurement": ("Suprimentos", "Fornecedores, prestadores e comparação de cotações."),
    "human-resources": ("Pessoas", "Recrutamento, admissão, desempenho e remuneração."),
    "technology-data": ("Tecnologia e dados", "Integrações, indicadores analíticos e segurança da informação."),
    "jurisdictions": ("Jurisdições", "Regras do Brasil, dos Estados Unidos e da Europa usadas pelos demais."),
}

FIXED_TITLES = {"jurisdiction-lookup": "Consulta de regras por país"}

# workflow file -> (title, {stage in the source file: stage on the site})
WORKFLOWS = {
    "lease-lifecycle": ("Locação, da captação ao repasse", {
        "Intake and move-in inspection": "Captação e vistoria de entrada",
        "Listing": "Anúncio",
        "Qualify and visit": "Qualificação e visita",
        "Screen tenant": "Análise do pretendente",
        "Contract and guarantee": "Contrato e garantia",
        "Monthly billing": "Faturamento mensal",
        "Owner payout": "Repasse ao proprietário",
        "Annual adjustment": "Reajuste anual",
    }),
    "delinquency-to-eviction": ("Inadimplência, cobrança e despejo", {
        "Overdue D+1": "Atraso identificado (D+1)",
        "Amicable collection D+1 to D+30": "Cobrança amigável (D+1 a D+30)",
        "Notice, agreement or eviction": "Notificação, acordo ou despejo",
        "Move-out inspection and deposit": "Vistoria de saída e garantia",
        "Accounting closure": "Baixa contábil",
    }),
    "listing-to-sale": ("Da captação à venda", {
        "Campaign": "Campanha",
        "Sale mandate": "Autorização de venda",
        "Price": "Precificação",
        "Listing": "Anúncio",
        "Qualify leads": "Qualificação de leads",
        "Visit": "Visita",
        "Proposal": "Proposta",
        "Due diligence and KYC": "Due diligence e identificação das partes",
        "Closing": "Fechamento",
        "Receive and pay commission": "Recebimento e comissão",
        "Handover and retention": "Entrega e relacionamento",
    }),
    "buy-renovate-resell": ("Compra, reforma e revenda", {
        "Screen": "Triagem",
        "Inspect and price": "Vistoria e precificação",
        "Due diligence": "Due diligence",
        "Feasibility": "Viabilidade",
        "Approve": "Aprovação",
        "Negotiate": "Negociação",
        "Scope and budget": "Escopo e orçamento",
        "Procure": "Contratação",
        "Execute and accept": "Execução e aceite",
        "Relist, then continue in listing-to-sale": "Novo anúncio, seguindo o fluxo de venda",
    }),
    "maintenance-and-warranty": ("Manutenção e garantia", {
        "Open ticket": "Abertura do chamado",
        "Classify urgency and responsibility": "Urgência e responsabilidade",
        "Vetted vendor": "Fornecedor homologado",
        "Execute and accept": "Execução e aceite",
        "Pay with three-way match": "Pagamento conferido com pedido e entrega",
        "Post to owner statement": "Lançamento no demonstrativo do proprietário",
    }),
    "governance-and-close": ("Governança e fechamento mensal", {
        "Daily reconciliation": "Conciliação diária",
        "Close by business day 5": "Fechamento até o 5º dia útil",
        "Executive KPIs": "Indicadores executivos",
        "13-week cash flow": "Caixa de 13 semanas",
        "BI and security": "Painéis e segurança",
    }),
}


def slug(text):
    plain = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", plain.lower()).strip("-")


def inline(text):
    """Inline markdown (code, bold, links) to HTML."""
    parts = re.split(r"(`[^`]+`)", text)
    for index, part in enumerate(parts):
        if index % 2:
            parts[index] = f"<code>{html.escape(part[1:-1])}</code>"
            continue
        part = html.escape(part, quote=False)
        part = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", part)

        def link(match):
            target = match.group(2)
            if "://" not in target:
                target = re.sub(r"\.md(?=$|#)", ".html", target)
            return f'<a href="{html.escape(target)}">{match.group(1)}</a>'

        parts[index] = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, part)
    return "".join(parts)


def table(rows, caption=None):
    """rows: list of lists of HTML cells; the first one is the header."""
    head = "".join(f'<th scope="col">{cell}</th>' for cell in rows[0])
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows[1:])
    label = f' aria-label="{html.escape(caption)}"' if caption else ' aria-label="Tabela"'
    return (f'<div class="table" role="region" tabindex="0"{label}>'
            f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div>")


def markdown(text, blocks):
    """Convert the markdown subset used in docs/content. Returns (html, h2 list)."""
    lines = text.split("\n")
    out, sections, i = [], [], 0
    special = re.compile(r"(#{1,3} |\||```|> |- |\d+\. |\{\{)")
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
        elif line.startswith("```"):
            end = lines.index("```", i + 1)
            code = html.escape("\n".join(lines[i + 1:end]), quote=False)
            out.append(f'<pre tabindex="0"><code>{code}</code></pre>')
            i = end + 1
        elif match := re.match(r"(#{1,3}) (.+)", line):
            level, title = len(match.group(1)), match.group(2)
            anchor = slug(title)
            if level == 2:
                sections.append((anchor, title))
            attr = f' id="{anchor}"' if level > 1 else ""
            out.append(f"<h{level}{attr}>{inline(title)}</h{level}>")
            i += 1
        elif match := re.fullmatch(r"\{\{(\w+)\}\}", line.strip()):
            block, extra = blocks[match.group(1)]()
            out.append(block)
            sections.extend(extra)
            i += 1
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append([inline(c) for c in cells])
                i += 1
            out.append(table(rows))
        elif line.startswith("> "):
            quote = []
            while i < len(lines) and lines[i].startswith("> "):
                quote.append(lines[i][2:])
                i += 1
            out.append(f'<aside class="callout"><p>{inline(" ".join(quote))}</p></aside>')
        elif re.match(r"(- |\d+\. )", line):
            ordered = line[0].isdigit()
            marker = re.compile(r"\d+\. " if ordered else r"- ")
            items = []
            while i < len(lines) and marker.match(lines[i]):
                items.append(marker.sub("", lines[i], count=1))
                i += 1
            if items and items[0].startswith("[ ] "):
                body = "".join(f"<li>{inline(item[4:])}</li>" for item in items)
                out.append(f'<ul class="checklist">{body}</ul>')
            else:
                tag = "ol" if ordered else "ul"
                body = "".join(f"<li>{inline(item)}</li>" for item in items)
                out.append(f"<{tag}>{body}</{tag}>")
        else:
            paragraph = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not special.match(lines[i]):
                paragraph.append(lines[i])
                i += 1
            out.append(f"<p>{inline(' '.join(paragraph))}</p>")
    return "\n".join(out), sections


def field(text, name):
    match = re.search(rf"^{name}: (.*)$", text, re.M)
    return match.group(1).strip() if match else ""


def plugins():
    market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
    return [(entry["name"], entry["source"].removeprefix("./"), entry["version"]) for entry in market["plugins"]]


def skill_title(path):
    text = path.read_text(encoding="utf-8")
    name = field(text, "name")
    if name.startswith("router-"):
        return name, "Escolhe a skill adequada ao pedido"
    if name in FIXED_TITLES:
        return name, FIXED_TITLES[name]
    match = re.search(r'PT: (.+?)\.?"?$', field(text, "description"))
    if not match:
        raise SystemExit(f"skill without Portuguese title (PT:) in description: {path}")
    return name, match.group(1)


def skills_section(path):
    """Skill names listed under '## Skills' or '## Skills used' in an agent or command."""
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## Skills(?: used)?\n\n(.*?)(?=\n## |\Z)", text, re.M | re.S)
    return re.findall(r"^- `([a-z-]+)`", match.group(1), re.M) if match else []


def numbers():
    folders = [folder for _, folder, _ in plugins()]
    counts = (
        (len(folders), "plugins"),
        (sum(len(list((ROOT / f).glob("agents/*.md"))) for f in folders), "agentes"),
        (sum(len(list((ROOT / f).glob("skills/*/SKILL.md"))) for f in folders), "skills"),
        (sum(len(list((ROOT / f).glob("commands/*.md"))) for f in folders), "comandos"),
    )
    items = "".join(f"<div><dt>{label}</dt><dd>{count}</dd></div>" for count, label in counts)
    return f'<dl class="numbers">{items}</dl>', []


def catalog():
    out, sections, index = [], [], [["Departamento", "Plugin", "Skills", "Comandos", "Agentes"]]
    for plugin, folder, _ in plugins():
        label, summary = DEPARTMENTS[folder]
        anchor = slug(label)
        skills = dict(skill_title(p) for p in sorted((ROOT / folder).glob("skills/*/SKILL.md")))
        commands = sorted((ROOT / folder).glob("commands/*.md"))
        agents = sorted((ROOT / folder).glob("agents/*.md"))
        index.append([f'<a href="#{anchor}">{label}</a>', f"<code>{plugin}</code>",
                      str(len(skills)), str(len(commands)), str(len(agents))])
        sections.append((anchor, label))
        out.append(f'<section class="department"><h2 id="{anchor}">{label}</h2><p>{summary}</p>')
        out.append(f"<p>Instalação: <code>/plugin install {plugin}@claude-rental-team</code></p>")
        out.append("<h3>Skills</h3>")
        out.append(table([["Skill", "O que atende"]] + [
            [f"<code>{plugin}:{name}</code>", html.escape(title)]
            for name, title in sorted(skills.items(), key=lambda s: (s[0].startswith("router-"), s[0]))
        ], f"Skills de {label}"))
        for heading, paths, form in (("Comandos", commands, "/{}:{}"), ("Agentes", agents, "{}")):
            if not paths:
                continue
            rows = [[heading[:-1], "Skills usadas"]]
            for path in paths:
                name = form.format(plugin, path.stem) if heading == "Comandos" else path.stem
                used = ", ".join(html.escape(skills[s]) for s in skills_section(path))
                rows.append([f"<code>{name}</code>", used])
            out.append(f"<h3>{heading}</h3>" + table(rows, f"{heading} de {label}"))
        out.append("</section>")
    return table(index, "Resumo dos departamentos") + "".join(out), sections


def workflows():
    files = {p.stem for p in (ROOT / "orchestration/workflows").glob("*.md")}
    if files != set(WORKFLOWS):
        raise SystemExit(f"workflow list out of date: {sorted(files ^ set(WORKFLOWS))}")
    titles = {(folder, name): title
              for _, folder, _ in plugins()
              for name, title in map(skill_title, (ROOT / folder).glob("skills/*/SKILL.md"))}
    out, sections = [], []
    for stem, (title, stages) in WORKFLOWS.items():
        anchor = slug(title)
        sections.append((anchor, title))
        out.append(f'<h2 id="{anchor}">{title}</h2><ol class="flow">')
        source = (ROOT / f"orchestration/workflows/{stem}.md").read_text(encoding="utf-8")
        for _, stage, cell in re.findall(r"^\| (\d+) \| (.+?) \| (.+?) \|$", source, re.M):
            if stage not in stages:
                raise SystemExit(f"untranslated stage in {stem}: {stage}")
            used = [f'<li><code>rt-{folder}:{name}</code> <span>{html.escape(titles[folder, name])}</span></li>'
                    for folder, name in re.findall(r"`rt-([a-z-]+):([a-z-]+)`", cell)]
            detail = f"<ul>{''.join(used)}</ul>" if used else "<p>Sem skill específica.</p>"
            out.append(f"<li><strong>{stages[stage]}</strong>{detail}</li>")
        out.append("</ol>")
    return "".join(out), sections


def page(position, body, sections):
    name, label = PAGES[position]
    version = plugins()[0][2]
    current = ' aria-current="page"'
    menu = "".join(f'<li><a href="{n}.html"{current if n == name else ""}>{l}</a></li>' for n, l in PAGES)
    contents = ""
    if position and len(sections) > 1:  # the first page is short and has its own reading guide
        links = "".join(f'<li><a href="#{a}">{html.escape(t)}</a></li>' for a, t in sections)
        contents = f'<nav class="contents" aria-labelledby="contents-title"><p id="contents-title">Nesta página</p><ul>{links}</ul></nav>'
    pager = []
    for step, rel, text in ((-1, "prev", "Anterior"), (1, "next", "Próxima")):
        if 0 <= position + step < len(PAGES):
            n, l = PAGES[position + step]
            pager.append(f'<a rel="{rel}" href="{n}.html"><span>{text}</span> {l}</a>')
    # place the table of contents after the title and the introduction
    body = body.replace("</p>", "</p>\n" + contents, 1) if contents else body
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{label} · claude-rental-team</title>
<meta name="description" content="Documentação do claude-rental-team: plugins para o Claude Code voltados à operação imobiliária.">
<link rel="icon" href="assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/style.css">
<script src="assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#conteudo">Ir para o conteúdo</a>
<header class="masthead">
<a class="brand" href="index.html">claude-rental-team</a>
<p>Documentação · versão {version} (rascunho)</p>
<a class="repository" href="{REPOSITORY}">Repositório</a>
</header>
<div class="layout">
<nav class="menu" aria-label="Seções da documentação"><ol>{menu}</ol></nav>
<main id="conteudo">
<article>
{body}
</article>
<nav class="pager" aria-label="Páginas vizinhas">{"".join(pager)}</nav>
<footer>
<p>Projeto independente distribuído sob a licença GPL versão 2. Claude e Claude Code são produtos da Anthropic.</p>
<p>O conteúdo é um rascunho e não constitui parecer jurídico, tributário ou de avaliação.</p>
</footer>
</main>
</div>
</body>
</html>
"""


def build():
    """Return {output path: html} for every page."""
    blocks = {"numeros": numbers, "catalogo": catalog, "fluxos": workflows}
    result = {}
    for position, (name, _) in enumerate(PAGES):
        source = (DOCS / "content" / f"{name}.md").read_text(encoding="utf-8")
        body, sections = markdown(source, blocks)
        result[DOCS / f"{name}.html"] = page(position, body, sections)
    return result


if __name__ == "__main__":
    for path, text in build().items():
        path.write_text(text, encoding="utf-8")
        print(path.relative_to(ROOT))
