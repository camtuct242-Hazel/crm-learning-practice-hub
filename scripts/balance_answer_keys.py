import json
import random
from collections import Counter
from pathlib import Path

qb_path = Path("output/data/question-bank.json")
with open(qb_path, "r", encoding="utf-8") as f:
    qb = json.load(f)

print(f"Total questions loaded: {len(qb)}")

# 1. Fix q-09-01 (remove option E if present)
for q in qb:
    if q["id"] == "q-09-01":
        if len(q["options"]) > 4:
            print(f"Trimming options for {q['id']} from {len(q['options'])} to 4...")
            q["options"] = [o for o in q["options"] if o["id"] in ["A", "B", "C", "D"]]

# 2. Balance answer key distribution per exam
# Each exam has 20 questions. We want exactly 5 'A', 5 'B', 5 'C', 5 'D' per exam.
target_exam_pattern = ["A"] * 5 + ["B"] * 5 + ["C"] * 5 + ["D"] * 5

# Use a deterministic seed for reproducibility
rng = random.Random(2026)

for ex_idx in range(10):
    pattern = target_exam_pattern.copy()
    rng.shuffle(pattern)
    exam_slice = qb[ex_idx * 20 : (ex_idx + 1) * 20]
    
    for i, q in enumerate(exam_slice):
        target_key = pattern[i]
        curr_key = q["correct_answer"]
        if target_key == curr_key:
            continue
            
        # Swap options between curr_key and target_key
        # Find index of option curr_key and target_key
        opts = q["options"]
        opt_curr_idx = next(idx for idx, o in enumerate(opts) if o["id"] == curr_key)
        opt_target_idx = next(idx for idx, o in enumerate(opts) if o["id"] == target_key)
        
        # Swap text contents
        text_curr = opts[opt_curr_idx]["text"]
        text_target = opts[opt_target_idx]["text"]
        
        opts[opt_curr_idx]["text"] = text_target
        opts[opt_target_idx]["text"] = text_curr
        
        # Update correct_answer
        q["correct_answer"] = target_key

# Verify distribution
new_dist = Counter(q["correct_answer"] for q in qb)
print(f"New overall Answer Key Distribution: {new_dist}")

for ex_idx in range(10):
    exam_slice = qb[ex_idx * 20 : (ex_idx + 1) * 20]
    sub_dist = Counter(q["correct_answer"] for q in exam_slice)
    assert sub_dist == {"A": 5, "B": 5, "C": 5, "D": 5}, f"Exam {ex_idx+1} distribution mismatch: {sub_dist}"

print("All 10 exams verified: exactly 5 A, 5 B, 5 C, 5 D each!")

# Verify all questions have exactly 4 options
for q in qb:
    assert len(q["options"]) == 4, f"Question {q['id']} has {len(q['options'])} options!"
    opt_ids = [o["id"] for o in q["options"]]
    assert opt_ids == ["A", "B", "C", "D"], f"Question {q['id']} options order error: {opt_ids}"
    assert q["correct_answer"] in ["A", "B", "C", "D"], f"Invalid key in {q['id']}"

print("All 200 questions have exactly 4 options (A, B, C, D)!")

# Save to question-bank.json
with open(qb_path, "w", encoding="utf-8") as f:
    json.dump(qb, f, ensure_ascii=False, indent=2)

print("Saved updated question-bank.json successfully.")
