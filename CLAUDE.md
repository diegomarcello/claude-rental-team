# CLAUDE.md

Guidance for Claude Code in this repository.

## Purpose

A library of Claude plugins to run a real estate company in Brazil, the US and Europe. It is not an application.

## Status

Draft. Reference content is integrated and pending professional review; see `CONTENT-REVIEW.md`. Four Brazil calculation scripts exist; after changing one, run `python3 -m unittest discover -s tests`. Templates without a country suffix are headings only.

## Map

- `<department>/`: one plugin per department, each with its own `CLAUDE.md`
- `jurisdictions/`: country rules shared by all departments
- `orchestration/`: cross-department workflows
- `standards/`, `templates/`: how to write and review files
- `.content-source/`: the original content package. Do not load or edit it for normal work.

## Rules

- Follow `CONVENTIONS.md`.
- Never commit client, tenant, owner, employee or financial data.
- A plugin cannot read files outside its own folder once installed: refer to other departments by skill name, never by relative path.
- After changing a plugin, run `claude plugin validate <folder>`. With `--strict`, the warning about the plugin-root `CLAUDE.md` is expected.
