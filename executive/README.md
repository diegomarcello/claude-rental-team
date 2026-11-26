# Executive

Company direction, KPIs, approval authority and cross-department routing.

Plugin: `rt-executive` · Status: draft. Each business skill has references for Brazil (Portuguese), the United States and Europe (English). Review by a qualified professional is pending.

## Install

Run inside Claude Code, from the marketplace in this repository.

```
/plugin marketplace add diegomarcello/claude-rental-team
/plugin install rt-executive@claude-rental-team
```

## First use

Run `/rt-executive:company-setup` in your company project. It asks for the company context, approval limits, collections ladder and missing leasing templates.

A session start hook (`hooks/setup_check.py`, needs `python3`) reminds you once after installation, and then whenever the project's `company-context.md` has pending items. It reads only the `Setup status` table.

## Agents

- `rt-strategy-planner`
- `rt-kpi-auditor`
- `rt-governance-gatekeeper`

## Skills

- `router-executive`
- `approval-gates`
- `company-kpis`
- `company-setup`
- `strategic-planning`

## Commands

- None. Use the router or the agents.
