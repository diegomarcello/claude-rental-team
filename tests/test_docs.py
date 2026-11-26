import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
sys.path.insert(0, str(DOCS))
sys.dont_write_bytecode = True
import build  # noqa: E402

CONTENT = {p.name: p.read_text(encoding="utf-8") for p in (DOCS / "content").glob("*.md")}


class DocsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = build.build()

    def test_generated_pages_are_up_to_date(self):
        for path, text in self.pages.items():
            self.assertEqual(path.read_text(encoding="utf-8"), text,
                             f"{path.name} is out of date: run python3 docs/build.py")
        self.assertEqual(sorted(DOCS.glob("*.html")), sorted(self.pages))

    def test_every_content_file_is_a_page(self):
        self.assertEqual(sorted(CONTENT), sorted(f"{name}.md" for name, _ in build.PAGES))

    def test_local_links_and_anchors_resolve(self):
        ids = {p.name: set(re.findall(r' id="([^"]+)"', t)) for p, t in self.pages.items()}
        for path, text in self.pages.items():
            found = re.findall(r' id="([^"]+)"', text)
            self.assertEqual(len(found), len(set(found)), f"repeated id in {path.name}")
            for target in re.findall(r'(?:href|src)="([^"]+)"', text):
                if "://" in target:
                    continue
                file, _, anchor = target.partition("#")
                self.assertTrue((DOCS / (file or path.name)).is_file(), f"{path.name}: {target}")
                if anchor:
                    self.assertIn(anchor, ids[file or path.name], f"{path.name}: {target}")

    def test_names_mentioned_in_the_text_exist(self):
        plugins = {name: ROOT / folder for name, folder, _ in build.plugins()}
        for file, text in CONTENT.items():
            for plugin, kind in re.findall(r"`/?(rt-[a-z-]+):([a-z-]+)`", text):
                found = [plugins[plugin] / "skills" / kind / "SKILL.md",
                         plugins[plugin] / "commands" / f"{kind}.md"]
                self.assertTrue(any(p.is_file() for p in found), f"{file}: {plugin}:{kind}")
            for plugin in re.findall(r"(rt-[a-z-]+)@claude-rental-team", text):
                self.assertIn(plugin, plugins, file)
            for plugin in re.findall(r"`(rt-[a-z-]+)`", text):
                agent = list(ROOT.glob(f"*/agents/{plugin}.md"))
                self.assertTrue(plugin in plugins or agent, f"{file}: {plugin}")

    def test_calculation_examples_match_the_scripts(self):
        text = CONTENT["dia-a-dia.md"]
        expected = {
            "accounts_receivable.py": ('"8.33"', '"2558.33"'),
            "owner_payout.py": ('"4150.00"', '"2026-11-13"'),
        }
        commands = re.findall(r"^python3 (\w+\.py) (.+)$", text, re.M)
        self.assertEqual({name for name, _ in commands}, set(expected))
        for name, args in commands:
            script = next(ROOT.glob(f"*/skills/*/scripts/{name}"))
            out = subprocess.run([sys.executable, "-B", str(script), *args.split()],
                                 capture_output=True, text=True, check=True).stdout
            for value in expected[name]:
                self.assertIn(value, out)
        for shown in ("R$ 8,33", "R$ 2.558,33", "R$ 4.150,00", "13/11/2026"):
            self.assertIn(shown, text)


if __name__ == "__main__":
    unittest.main()
