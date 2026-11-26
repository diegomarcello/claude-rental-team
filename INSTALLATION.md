# Installation

Run inside Claude Code.

## Add the marketplace

From a local clone:

```
/plugin marketplace add /path/to/claude-rental-team
```

From GitHub (once the files are pushed):

```
/plugin marketplace add diegomarcello/claude-rental-team
```

## Install plugins

Install `rt-executive` and `rt-jurisdictions` first; the other departments refer to them.

```
/plugin install rt-executive@claude-rental-team
/plugin install rt-acquisitions@claude-rental-team
/plugin install rt-appraisal@claude-rental-team
/plugin install rt-legal@claude-rental-team
/plugin install rt-renovation@claude-rental-team
/plugin install rt-marketing@claude-rental-team
/plugin install rt-pre-sales@claude-rental-team
/plugin install rt-sales@claude-rental-team
/plugin install rt-crm@claude-rental-team
/plugin install rt-property-management@claude-rental-team
/plugin install rt-post-sales@claude-rental-team
/plugin install rt-finance@claude-rental-team
/plugin install rt-procurement@claude-rental-team
/plugin install rt-human-resources@claude-rental-team
/plugin install rt-technology-data@claude-rental-team
/plugin install rt-jurisdictions@claude-rental-team
```

## First use

Open Claude Code in your company project and run:

```
/rt-executive:company-setup
```

It asks for, and records in `company-context.md`:

1. The company context.
2. The approval limits, row by row. Values in a filled example are not rules until you confirm them.
3. The collections ladder.
4. The five leasing templates that are still headings only: collection notice, receivables aging, lease summary, move inspection record and tenant application. Your versions are saved in `company-templates/` in your project.

Claude Code has no step that runs during installation. Instead, `rt-executive` shows a reminder at the start of the first session after installation, and later whenever setup items are pending. The leasing skills also ask for what they need when you use them, even without `rt-executive`.

Never commit `company-context.md` to a public repository.
