#!/usr/bin/env python3
"""SessionStart hook: report pending company setup items.

Reads only the "Setup status" table of company-context.md and prints only item
names from ITEMS, so file content never reaches the session through this hook.
It never fails the session.
"""
import json
import os
import re
import sys
from pathlib import Path

ITEMS = (
    "company-context",
    "approval-limits",
    "collections-ladder",
    "template:collection-notice",
    "template:receivables-aging",
    "template:lease-summary",
    "template:move-inspection-record",
    "template:tenant-application",
)
MAX_BYTES = 1_000_000


def pending_items(text):
    """Items not marked confirmed (with a name) or not-applicable."""
    section = re.search(r"^## Setup status[ \t]*$(.*?)(?=^## |\Z)", text, re.M | re.S)
    done = set()
    for line in (section.group(1).splitlines() if section else []):
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or cells[0] not in ITEMS:
            continue
        status, who = cells[1].lower(), cells[2]
        if status == "not-applicable" or (status == "confirmed" and who):
            done.add(cells[0])
    return [item for item in ITEMS if item not in done]


def message(project, data_dir):
    """Return (text for the user, text for Claude), or None to stay silent."""
    context = project / "company-context.md"
    if context.is_file():
        with context.open(encoding="utf-8", errors="replace") as handle:
            pending = pending_items(handle.read(MAX_BYTES))
        if not pending:
            return None
        return (
            f"claude-rental-team: {len(pending)} setup item(s) pending. Run /rt-executive:company-setup.",
            "claude-rental-team setup is incomplete. Pending items: " + ", ".join(pending) + ". "
            "When a request depends on one of them, ask the user before relying on it. "
            "The rt-executive:company-setup skill runs the whole interview. Do not interrupt unrelated work.",
        )
    # No context file: offer setup once after installation, not in every project.
    if not data_dir:
        return None
    marker = Path(data_dir) / "setup-offered"
    if marker.exists():
        return None
    marker.parent.mkdir(parents=True, exist_ok=True)
    marker.write_text("offered\n", encoding="utf-8")
    return (
        "claude-rental-team installed. Run /rt-executive:company-setup in your company project.",
        "claude-rental-team was installed and this project has no company-context.md. "
        "At the first suitable moment, ask the user whether to run the rt-executive:company-setup skill here. "
        "Pending items: " + ", ".join(ITEMS) + ".",
    )


def main():
    try:
        try:
            event = json.load(sys.stdin)
        except ValueError:
            event = {}
        project = os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or os.getcwd()
        result = message(Path(project), os.environ.get("CLAUDE_PLUGIN_DATA"))
        if result:
            print(json.dumps({
                "systemMessage": result[0],
                "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": result[1]},
            }))
    except Exception as error:  # a setup reminder must never break a session
        print(f"setup check skipped: {type(error).__name__}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
