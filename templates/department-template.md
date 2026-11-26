# New Department Checklist

1. Create `<department>/.claude-plugin/plugin.json` with exactly: `name` (`rt-<department>`), `description`, `version`, `author`, `homepage`, `repository`, `license`, `skills` (`./skills`).
2. Add `README.md` and `CLAUDE.md`.
3. Add `agents/`, `commands/` and `skills/<department>-router/SKILL.md`.
4. Register the plugin in `.claude-plugin/marketplace.json`.
5. Run `claude plugin validate <department>`.
