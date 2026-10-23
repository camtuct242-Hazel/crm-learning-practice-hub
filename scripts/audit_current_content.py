import json
from pathlib import Path

data_dir = Path(r"C:\Kiến thức cần học\CRM\output\data")

def audit():
    report = {}

    # 1. CURRICULUM
    curr_file = data_dir / "curriculum.json"
    if curr_file.exists():
        curr_data = json.loads(curr_file.read_text(encoding="utf-8"))
        chaps = []
        for c in curr_data:
            has_vi_notes = bool(c.get("detailed_notes", {}).get("vi", "").strip())
            has_en_notes = bool(c.get("detailed_notes", {}).get("en", "").strip())
            vi_len = len(c.get("detailed_notes", {}).get("vi", ""))
            en_len = len(c.get("detailed_notes", {}).get("en", ""))
            chaps.append({
                "id": c.get("id"),
                "book": c.get("book_id"),
                "chapter_num": c.get("chapter_num"),
                "title_vi": c.get("title", {}).get("vi"),
                "title_en": c.get("title", {}).get("en"),
                "has_vi": has_vi_notes,
                "has_en": has_en_notes,
                "vi_char_count": vi_len,
                "en_char_count": en_len,
                "objectives_count": len(c.get("learning_objectives", {}).get("vi", [])),
                "review_q_count": len(c.get("review_questions", []))
            })
        report["curriculum"] = {
            "total_chapters": len(curr_data),
            "chapters": chaps
        }

    # 2. GLOSSARY
    gloss_file = data_dir / "glossary.json"
    if gloss_file.exists():
        gloss_data = json.loads(gloss_file.read_text(encoding="utf-8"))
        valid_terms = 0
        for t in gloss_data:
            has_vi = bool(t.get("definition", {}).get("vi", "").strip())
            has_en = bool(t.get("definition", {}).get("en", "").strip())
            if has_vi and has_en:
                valid_terms += 1
        report["glossary"] = {
            "total_terms": len(gloss_data),
            "fully_bilingual_terms": valid_terms
        }

    # 3. FLASHCARDS
    fc_file = data_dir / "flashcards.json"
    if fc_file.exists():
        fc_data = json.loads(fc_file.read_text(encoding="utf-8"))
        valid_fc = 0
        for f in fc_data:
            has_f_vi = bool(f.get("front", {}).get("vi", "").strip())
            has_f_en = bool(f.get("front", {}).get("en", "").strip())
            has_b_vi = bool(f.get("back", {}).get("vi", "").strip())
            has_b_en = bool(f.get("back", {}).get("en", "").strip())
            if has_f_vi and has_f_en and has_b_vi and has_b_en:
                valid_fc += 1
        report["flashcards"] = {
            "total_cards": len(fc_data),
            "fully_bilingual_cards": valid_fc
        }

    # 4. CASES
    cases_file = data_dir / "cases.json"
    if cases_file.exists():
        cases_data = json.loads(cases_file.read_text(encoding="utf-8"))
        c_list = []
        for cs in cases_data:
            c_list.append({
                "case_id": cs.get("case_id"),
                "company": cs.get("company"),
                "has_framework": len(cs.get("crm_framework_steps", [])) > 0,
                "framework_steps": len(cs.get("crm_framework_steps", [])),
                "discussion_q_count": len(cs.get("discussion_questions", [])),
                "source": cs.get("source_reference", {})
            })
        report["cases"] = {
            "total_cases": len(cases_data),
            "cases": c_list
        }

    # 5. EXAMS
    exams_file = data_dir / "exams.json"
    if exams_file.exists():
        exams_data = json.loads(exams_file.read_text(encoding="utf-8"))
        e_list = []
        for e in exams_data:
            e_list.append({
                "id": e.get("id"),
                "title_vi": e.get("title", {}).get("vi"),
                "target_domain": e.get("target_domain"),
                "question_ids_count": len(e.get("question_ids", []))
            })
        report["exams"] = {
            "total_exams": len(exams_data),
            "exams": e_list
        }

    # 6. QUESTION BANK
    qb_file = data_dir / "question-bank.json"
    if qb_file.exists():
        qb_data = json.loads(qb_file.read_text(encoding="utf-8"))
        valid_q = 0
        for q in qb_data:
            has_q_vi = bool(q.get("question", {}).get("vi", "").strip())
            has_q_en = bool(q.get("question", {}).get("en", "").strip())
            has_ans = bool(q.get("correct_answer") in ["A", "B", "C", "D"])
            has_exp_vi = bool(q.get("explanation", {}).get("vi", "").strip())
            has_exp_en = bool(q.get("explanation", {}).get("en", "").strip())
            if has_q_vi and has_q_en and has_ans and has_exp_vi and has_exp_en:
                valid_q += 1
        report["question_bank"] = {
            "total_questions": len(qb_data),
            "fully_validated_questions": valid_q
        }

    print(json.dumps(report, indent=2, ensure_ascii=False))

audit()
