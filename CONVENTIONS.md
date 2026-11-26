# Conventions

## Names

- Folders and files: lowercase `kebab-case`, in English.
- Plugins: `rt-<folder>`. Agents: `rt-<role>`. Commands: `rt-<action>`.
- Skill names are unique across the repository and never equal a Claude Code built-in command (`review`, `status`, `help`, ...).
- Each department has one `<department>-router` skill.

## Frontmatter

| File | Fields |
|---|---|
| `SKILL.md` | `name`, `description`, `license`, `metadata` |
| Agent | `name`, `description`, `model` |
| Command | `description`, `argument-hint`, `disable-model-invocation` |

Every skill and agent `description` starts with "Use when".

## plugin.json

Only `name`, `description`, `version`, `author`, `homepage`, `repository`, `license`, `skills`. Claude Code rejects unknown keys.

## Skeleton files

Keep the skeleton notice and `status: skeleton` until the procedure is written and reviewed.
