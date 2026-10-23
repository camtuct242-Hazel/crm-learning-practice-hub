import json
import unittest
from pathlib import Path

class TestCRMHubValidation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data_dir = Path(r"C:\Kiến thức cần học\CRM\output\data")
        cls.src_dir = Path(r"C:\Kiến thức cần học\CRM\output\src")
        
        with open(cls.data_dir / "question-bank.json", "r", encoding="utf-8") as f:
            cls.qb = json.load(f)
            
        with open(cls.data_dir / "exams.json", "r", encoding="utf-8") as f:
            cls.exams = json.load(f)
            
        with open(cls.data_dir / "curriculum.json", "r", encoding="utf-8") as f:
            cls.curriculum = json.load(f)
            
        with open(cls.data_dir / "glossary.json", "r", encoding="utf-8") as f:
            cls.glossary = json.load(f)
            
        with open(cls.data_dir / "flashcards.json", "r", encoding="utf-8") as f:
            cls.flashcards = json.load(f)
            
        with open(cls.data_dir / "cases.json", "r", encoding="utf-8") as f:
            cls.cases = json.load(f)

    def test_question_bank_exact_200(self):
        """Assert exactly 200 questions and 200 unique IDs in question bank."""
        self.assertEqual(len(self.qb), 200, f"Expected exactly 200 questions, got {len(self.qb)}")
        ids = [q["id"] for q in self.qb]
        self.assertEqual(len(ids), len(set(ids)), "Duplicate question IDs detected in question bank!")

    def test_ten_curated_exams_structure(self):
        """Assert exactly 10 exams with exactly 20 distinct questions each, mapping all 200 questions."""
        self.assertEqual(len(self.exams), 10, f"Expected 10 exams, got {len(self.exams)}")
        qb_dict = {q["id"]: q for q in self.qb}
        
        all_assigned = set()
        for idx, ex in enumerate(self.exams, 1):
            q_ids = ex.get("question_ids", [])
            self.assertEqual(len(q_ids), 20, f"Exam {ex['id']} must have exactly 20 questions, got {len(q_ids)}")
            for qid in q_ids:
                self.assertIn(qid, qb_dict, f"Question {qid} in Exam {ex['id']} not found in question bank!")
                self.assertNotIn(qid, all_assigned, f"Question {qid} assigned to multiple exams!")
                all_assigned.add(qid)
                
        self.assertEqual(len(all_assigned), 200, "All 200 questions must be assigned to exams!")

    def test_question_bilingual_and_data_integrity(self):
        """Assert 100% bilingual parity and valid answer keys across all 200 questions."""
        valid_keys = {"A", "B", "C", "D"}
        for q in self.qb:
            qid = q["id"]
            # Question text
            self.assertTrue(q.get("question", {}).get("vi"), f"Missing VI question text for {qid}")
            self.assertTrue(q.get("question", {}).get("en"), f"Missing EN question text for {qid}")
            
            # Options
            options = q.get("options", [])
            self.assertGreaterEqual(len(options), 4, f"Question {qid} must have at least 4 options")
            opt_ids = {opt["id"] for opt in options}
            self.assertTrue(valid_keys.issubset(opt_ids), f"Question {qid} missing options A, B, C, or D")
            for opt in options:
                self.assertTrue(opt["text"]["vi"], f"Missing VI text in option {opt['id']} of {qid}")
                self.assertTrue(opt["text"]["en"], f"Missing EN text in option {opt['id']} of {qid}")
                
            # Answer key
            correct = q.get("correct_answer")
            self.assertIn(correct, valid_keys, f"Invalid correct answer '{correct}' in {qid}")
            
            # Explanation
            self.assertTrue(q.get("explanation", {}).get("vi"), f"Missing VI explanation for {qid}")
            self.assertTrue(q.get("explanation", {}).get("en"), f"Missing EN explanation for {qid}")
            
            # Source
            source = q.get("source", {})
            self.assertTrue(source.get("document"), f"Missing source document for {qid}")
            self.assertTrue(source.get("chapter"), f"Missing source chapter for {qid}")
            self.assertTrue(source.get("pages"), f"Missing source pages for {qid}")

    def test_curriculum_completeness(self):
        """Assert all 21 chapters exist with bilingual notes and learning objectives."""
        self.assertEqual(len(self.curriculum), 21, f"Expected 21 chapters, got {len(self.curriculum)}")
        baran_count = sum(1 for c in self.curriculum if c.get("book_id") == "TB-BARAN-2017")
        fund_count = sum(1 for c in self.curriculum if c.get("book_id") == "TB-KOSTOJOHN-2011")
        self.assertEqual(baran_count, 14, f"Expected 14 Baran chapters, got {baran_count}")
        self.assertEqual(fund_count, 7, f"Expected 7 Kostojohn chapters, got {fund_count}")
        
        for c in self.curriculum:
            cid = c["id"]
            self.assertTrue(c["title"]["vi"], f"Missing VI title in {cid}")
            self.assertTrue(c["title"]["en"], f"Missing EN title in {cid}")
            objs = c.get("learning_objectives", {})
            self.assertGreaterEqual(len(objs.get("vi", [])), 3, f"Too few VI objectives in {cid}")
            self.assertGreaterEqual(len(objs.get("en", [])), 3, f"Too few EN objectives in {cid}")
            notes = c.get("detailed_notes", {})
            self.assertTrue(notes.get("vi"), f"Empty VI detailed notes in {cid}")
            self.assertTrue(notes.get("en"), f"Empty EN detailed notes in {cid}")

    def test_glossary_completeness(self):
        """Assert at least 50 glossary terms with full bilingual details."""
        self.assertGreaterEqual(len(self.glossary), 50, f"Expected at least 50 terms, got {len(self.glossary)}")
        for t in self.glossary:
            tid = t["id"]
            self.assertTrue(t["term"]["vi"], f"Missing VI term in {tid}")
            self.assertTrue(t["term"]["en"], f"Missing EN term in {tid}")
            self.assertTrue(t["definition"]["vi"], f"Missing VI definition in {tid}")
            self.assertTrue(t["definition"]["en"], f"Missing EN definition in {tid}")
            
            ctx = t.get("context") or t.get("operational_context") or {}
            self.assertTrue(ctx.get("vi"), f"Missing VI context in {tid}")
            self.assertTrue(ctx.get("en"), f"Missing EN context in {tid}")
            self.assertTrue(t.get("source", {}).get("document"), f"Missing source in {tid}")

    def test_flashcards_completeness(self):
        """Assert at least 40 flashcards with full bilingual front/back and hints."""
        self.assertGreaterEqual(len(self.flashcards), 40, f"Expected at least 40 cards, got {len(self.flashcards)}")
        for fc in self.flashcards:
            fcid = fc["id"]
            self.assertTrue(fc["front"]["vi"], f"Missing VI front in {fcid}")
            self.assertTrue(fc["front"]["en"], f"Missing EN front in {fcid}")
            self.assertTrue(fc["back"]["vi"], f"Missing VI back in {fcid}")
            self.assertTrue(fc["back"]["en"], f"Missing EN back in {fcid}")
            self.assertTrue(fc["hint"]["vi"], f"Missing VI hint in {fcid}")
            self.assertTrue(fc["hint"]["en"], f"Missing EN hint in {fcid}")
            self.assertIn(fc.get("difficulty"), ["easy", "medium", "hard"], f"Invalid difficulty in {fcid}")

    def test_cases_completeness(self):
        """Assert 10 enterprise case studies with frameworks and verified citations."""
        self.assertEqual(len(self.cases), 10, f"Expected 10 cases, got {len(self.cases)}")
        for cs in self.cases:
            cid = cs["case_id"]
            self.assertTrue(cs["title"]["vi"], f"Missing VI title in {cid}")
            self.assertTrue(cs["title"]["en"], f"Missing EN title in {cid}")
            self.assertTrue(cs.get("background", {}).get("vi"), f"Missing VI background in {cid}")
            self.assertTrue(cs.get("background", {}).get("en"), f"Missing EN background in {cid}")
            self.assertGreaterEqual(len(cs.get("crm_framework_steps", [])), 1, f"Missing framework steps in {cid}")
            self.assertGreaterEqual(len(cs.get("discussion_questions", [])), 1, f"Missing questions in {cid}")
            src = cs.get("source_reference") or cs.get("source") or {}
            self.assertTrue(src.get("document"), f"Missing source in {cid}")

    def test_data_store_js_synced(self):
        """Assert that data-store.js contains the bundled data and matches question count."""
        store_file = self.src_dir / "data-store.js"
        self.assertTrue(store_file.exists(), "data-store.js does not exist!")
        content = store_file.read_text(encoding="utf-8")
        self.assertIn("window.CRM_DATA", content, "window.CRM_DATA missing in data-store.js")
        self.assertIn('"q-01-01"', content, "Question q-01-01 missing from bundled data-store.js")
        self.assertIn('"q-10-20"', content, "Question q-10-20 missing from bundled data-store.js")
        self.assertIn('"term-service-recovery-paradox"', content, "New glossary terms missing from bundle")
        self.assertIn('"fc-040"', content, "New flashcards missing from bundle")

    def test_answer_key_distribution_balanced(self):
        """Assert answer key does not systematically favor one option: exactly 50 A, 50 B, 50 C, 50 D."""
        from collections import Counter
        dist = Counter(q["correct_answer"] for q in self.qb)
        self.assertEqual(dist, {"A": 50, "B": 50, "C": 50, "D": 50}, f"Unbalanced answer keys: {dist}")
        
        # Also check each of the 10 exams has exactly 5 A, 5 B, 5 C, 5 D
        for ex in self.exams:
            exam_q = [q for q in self.qb if q["exam_id"] == ex["id"]]
            ex_dist = Counter(q["correct_answer"] for q in exam_q)
            self.assertEqual(ex_dist, {"A": 5, "B": 5, "C": 5, "D": 5}, f"Exam {ex['id']} key distribution unbalanced: {ex_dist}")

    def test_exact_four_options_per_question(self):
        """Assert every single question has exactly 4 options with IDs A, B, C, D."""
        for q in self.qb:
            qid = q["id"]
            self.assertEqual(len(q["options"]), 4, f"Question {qid} does not have exactly 4 options! Has {len(q['options'])}")
            opt_ids = [o["id"] for o in q["options"]]
            self.assertEqual(opt_ids, ["A", "B", "C", "D"], f"Question {qid} options order error: {opt_ids}")

    def test_random_practice_engine_sampling(self):
        """Simulate random practice generator: samples correctly by count and difficulty."""
        import random
        for count in [10, 20, 30]:
            for diff in ["all", "easy", "medium", "hard"]:
                pool = self.qb if diff == "all" else [q for q in self.qb if q["difficulty"] == diff]
                sampled = random.sample(pool, min(count, len(pool)))
                self.assertLessEqual(len(sampled), count)
                if diff != "all":
                    self.assertTrue(all(q["difficulty"] == diff for q in sampled))
                # Test score calculation logic
                mock_answers = {q["id"]: q["correct_answer"] for q in sampled[:5]}
                score = sum(1 for q in sampled if mock_answers.get(q["id"]) == q["correct_answer"])
                self.assertEqual(score, 5)

if __name__ == "__main__":
    unittest.main()

