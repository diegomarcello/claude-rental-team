import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / "executive/hooks/setup_check.py"
STATUS = (ROOT / "executive/skills/company-setup/assets/setup-status.md").read_text(encoding="utf-8")
sys.path.insert(0, str(HOOK.parent))
sys.dont_write_bytecode = True
import setup_check  # noqa: E402


class SetupCheckTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.project = Path(tmp.name) / "project"
        self.project.mkdir()
        self.data = Path(tmp.name) / "data"

    def run_hook(self, stdin="{}"):
        env = dict(os.environ, CLAUDE_PROJECT_DIR=str(self.project), CLAUDE_PLUGIN_DATA=str(self.data))
        done = subprocess.run([sys.executable, "-B", str(HOOK)], input=stdin, env=env,
                              capture_output=True, text=True, check=True)
        return json.loads(done.stdout) if done.stdout else None

    def write(self, text):
        (self.project / "company-context.md").write_text(text, encoding="utf-8")

    def test_offers_setup_only_once_without_context(self):
        first = self.run_hook()
        self.assertIn("company-setup", first["systemMessage"])
        self.assertIsNone(self.run_hook())

    def test_status_template_lists_every_item_as_pending(self):
        self.assertEqual(setup_check.pending_items(STATUS), list(setup_check.ITEMS))

    def test_file_without_status_table_is_unconfirmed(self):
        self.write("## 3. Approvals\n| Payment | up to 2000 | A | B | C |\n")
        context = self.run_hook()["hookSpecificOutput"]["additionalContext"]
        for item in setup_check.ITEMS:
            self.assertIn(item, context)

    def test_confirmed_needs_a_name(self):
        text = STATUS.replace("| approval-limits | pending | |", "| approval-limits | confirmed | |")
        self.assertIn("approval-limits", setup_check.pending_items(text))
        text = STATUS.replace("| approval-limits | pending | |", "| approval-limits | confirmed | Director |")
        self.assertNotIn("approval-limits", setup_check.pending_items(text))

    def test_silent_when_everything_is_done(self):
        text = STATUS.replace("| pending | | |", "| confirmed | Director | 2026-11-26 |")
        text = text.replace("| template:lease-summary | confirmed | Director |", "| template:lease-summary | not-applicable | |")
        self.write(text)
        self.assertIsNone(self.run_hook())

    def test_file_content_is_never_echoed(self):
        self.write("SECRET-VALUE\n## Setup status\n| SECRET-ITEM | pending | |\n")
        self.assertNotIn("SECRET", json.dumps(self.run_hook()))

    def test_bad_input_does_not_fail(self):
        self.assertIsNotNone(self.run_hook(stdin="not json"))

    def test_ladder_proposals_are_identical_in_both_plugins(self):
        name = "references/collections-ladder-options.md"
        self.assertEqual((ROOT / "executive/skills/company-setup" / name).read_bytes(),
                         (ROOT / "finance/skills/collections" / name).read_bytes())


if __name__ == "__main__":
    unittest.main()
