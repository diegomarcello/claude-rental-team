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

## Company context

Copy `executive/skills/executive-router/assets/company-context.md` to your working project as `company-context.md` and fill it in.
