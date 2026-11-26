# Security

- Do not commit personal data, credentials, contracts or financial records.
- Keep `company-context.md` out of public repositories.
- `rt-executive` runs a session start hook (`executive/hooks/setup_check.py`). It reads only the `Setup status` table of the project's `company-context.md`, prints item names, writes one marker file in the plugin data folder and uses no network.

## Reporting a vulnerability

TODO

## Handling an exposed secret or personal data

TODO
