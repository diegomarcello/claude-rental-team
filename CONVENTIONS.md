# Conventions

## Names

- Folders and files: lowercase `kebab-case`, in English.
- `SKILL.md`, agents, commands and repository documents are in English. Brazil references are in Portuguese.
- Plugins: `rt-<folder>`. Agents: `rt-<role>`. Commands: `rt-<action>`.
- Skill names are unique across the repository and never equal a Claude Code built-in command (`review`, `status`, `help`, ...).
- Each department has one `router-<department>` skill.

## Frontmatter

| File | Fields |
|---|---|
| `SKILL.md` | `name`, `description`, `license`, `metadata` |
| Agent | `name`, `description`, `model` |
| Command | `description`, `argument-hint`, `disable-model-invocation` |

Every skill and agent `description` starts with "Use when".

## plugin.json

Only `name`, `description`, `version`, `author`, `homepage`, `repository`, `license`, `skills`. Claude Code rejects unknown keys.

## Skill content

```
<skill>/
├── SKILL.md                      how to use, handoffs, guardrails
├── references/brazil.md          Portuguese
├── references/united-states.md
├── references/europe.md
├── references/known-issues.md    optional; overrides the references
├── assets/                       business templates
└── scripts/                      deterministic calculations
```

Skills are `status: draft` until a qualified professional signs off.

## Company setup

A skill that depends on a company decision asks for it when used and records nothing without the user's confirmation. Item names in the `Setup status` table are defined in `executive/skills/company-setup/assets/setup-status.md` and `executive/hooks/setup_check.py`; change both together.
