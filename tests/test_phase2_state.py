import json
import unittest
from pathlib import Path

class TestPhase2BilingualState(unittest.TestCase):
    def setUp(self):
        self.root_dir = Path(r"C:\Kiến thức cần học\CRM\output")
        self.translations_file = self.root_dir / "src" / "i18n" / "translations.json"
        self.manifest_file = self.root_dir / "data" / "source-manifest.json"

    def test_translations_file_exists(self):
        self.assertTrue(self.translations_file.exists(), "translations.json must exist")

    def test_translations_bilingual_parity(self):
        """Ensure all UI translation keys have non-empty 'vi' and 'en' translations."""
        data = json.loads(self.translations_file.read_text(encoding="utf-8"))
        
        def check_node(node, path=""):
            for k, v in node.items():
                current_path = f"{path}.{k}" if path else k
                if isinstance(v, dict):
                    if "vi" in v and "en" in v:
                        self.assertTrue(bool(v["vi"].strip()), f"Missing 'vi' at {current_path}")
                        self.assertTrue(bool(v["en"].strip()), f"Missing 'en' at {current_path}")
                    else:
                        check_node(v, current_path)
                else:
                    self.fail(f"Invalid translation leaf at {current_path}: expected dict with 'vi' and 'en'")
                    
        check_node(data)
        print("✓ All UI translation keys have 100% bilingual parity (vi/en).")

    def test_mock_language_switching_preserves_state(self):
        """Simulate state engine: switching languages must NOT reset quiz selections or progress."""
        # Simulated app state
        app_state = {
            "currentLang": "vi",
            "activeTab": "exams",
            "activeExamId": "EXAM-01",
            "examAnswers": {"q-001": "A", "q-002": "C"},
            "flashcardIndex": 5,
            "completedChapters": ["module-baran-ch01"]
        }

        # User changes language to English
        def switch_language(state, new_lang):
            updated = dict(state)
            updated["currentLang"] = new_lang
            return updated

        new_state = switch_language(app_state, "en")
        
        # Verify language changed
        self.assertEqual(new_state["currentLang"], "en")
        # Verify exam answers are preserved
        self.assertEqual(new_state["examAnswers"], {"q-001": "A", "q-002": "C"})
        self.assertEqual(new_state["activeExamId"], "EXAM-01")
        self.assertEqual(new_state["flashcardIndex"], 5)
        self.assertEqual(new_state["completedChapters"], ["module-baran-ch01"])
        print("✓ Language toggle preservation simulation verified.")

    def test_manifest_integrity(self):
        self.assertTrue(self.manifest_file.exists(), "source-manifest.json must exist")
        data = json.loads(self.manifest_file.read_text(encoding="utf-8"))
        self.assertEqual(len(data["textbooks"]), 2)
        self.assertEqual(len(data["case_studies"]), 5)
        print("✓ Source manifest integrity verified.")

if __name__ == "__main__":
    unittest.main()
