import json
from pathlib import Path

data_dir = Path("output/data")
with open(data_dir / "exams.json", "r", encoding="utf-8") as f:
    exams = json.load(f)

with open(data_dir / "question-bank.json", "r", encoding="utf-8") as f:
    qb = json.load(f)

qb_dict = {q["id"]: q for q in qb}
total_exam_questions = 0

print(f"Total exams: {len(exams)}")
print(f"Total questions in bank: {len(qb)}")

all_assigned_ids = set()

for ex in exams:
    q_ids = ex.get("question_ids", [])
    total_exam_questions += len(q_ids)
    assert len(q_ids) == 20, f"Exam {ex['id']} does not have 20 questions! Has {len(q_ids)}"
    for qid in q_ids:
        assert qid in qb_dict, f"Missing question {qid} in question bank!"
        assert qid not in all_assigned_ids, f"Question {qid} is duplicated across exams!"
        all_assigned_ids.add(qid)
    print(f"  - {ex['id']}: 20 distinct verified questions (OK)")

print(f"\nTotal exam mapped questions across 10 exams: {total_exam_questions}")
print(f"Total unique assigned question IDs: {len(all_assigned_ids)}")
assert total_exam_questions == 200, f"Expected 200 mapped questions, got {total_exam_questions}"
assert len(all_assigned_ids) == 200, "Not all 200 questions are assigned to exactly one exam!"
print("VERIFICATION SUCCESSFUL: Exactly 10 curated exams with 20 distinct verified questions each, matching all 200 questions in question-bank.json!")
