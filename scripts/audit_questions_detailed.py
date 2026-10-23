import json
from collections import Counter
from pathlib import Path

qb_path = Path("output/data/question-bank.json")
with open(qb_path, "r", encoding="utf-8") as f:
    qb = json.load(f)

print(f"Total questions: {len(qb)}")

# 1. Non-4 options
non_4 = [q for q in qb if len(q.get("options", [])) != 4]
print(f"Questions with != 4 options: {len(non_4)}")
for q in non_4:
    print(f"  ID: {q['id']}, Exam: {q['exam_id']}, Options count: {len(q['options'])}")
    for o in q["options"]:
        print(f"    [{o['id']}] {o['text']['en']}")

# 2. Answer key distribution
key_dist = Counter(q["correct_answer"] for q in qb)
print(f"\nOverall Answer Key Distribution: {key_dist}")

# 3. Check duplicate question texts or near-duplicates
seen_vi = {}
seen_en = {}
duplicates = []
for q in qb:
    txt_vi = q["question"]["vi"].strip().lower()
    txt_en = q["question"]["en"].strip().lower()
    if txt_vi in seen_vi:
        duplicates.append((q["id"], seen_vi[txt_vi], "VI duplicate"))
    if txt_en in seen_en:
        duplicates.append((q["id"], seen_en[txt_en], "EN duplicate"))
    seen_vi[txt_vi] = q["id"]
    seen_en[txt_en] = q["id"]

print(f"\nExact duplicate questions found: {len(duplicates)}")
for d in duplicates:
    print(f"  {d}")

# 4. Check whether correct_answer is mentioned in options
invalid_keys = []
for q in qb:
    opt_ids = [o["id"] for o in q.get("options", [])]
    if q["correct_answer"] not in opt_ids:
        invalid_keys.append((q["id"], q["correct_answer"], opt_ids))

print(f"\nQuestions with invalid correct_answer: {len(invalid_keys)}")
for inv in invalid_keys:
    print(f"  {inv}")
