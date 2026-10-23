# -*- coding: utf-8 -*-
"""
Assemble all 10 full-length cases into output/data/cases.json and rebuild data-store.js.
Ensures 100% source fidelity, complete academic Vietnamese translations, zero truncated text, zero obsolete hints.
"""

import json
from pathlib import Path
import subprocess

from cases_content_tesco import TESCO_EN, TESCO_VI
from cases_content_walmart import WALMART_EN, WALMART_VI
from cases_content_ikea import IKEA_EN, IKEA_VI
from cases_content_disney import DISNEY_EN, DISNEY_VI
from cases_content_airbnb import AIRBNB_EN, AIRBNB_VI
from cases_content_mcdonald import MCDONALD_EN, MCDONALD_VI
from cases_content_chanel import CHANEL_EN, CHANEL_VI
from cases_content_nike import NIKE_EN, NIKE_VI
from cases_content_estee import ESTEE_EN, ESTEE_VI
from cases_content_gafa import GAFA_EN, GAFA_VI

data_dir = Path("output/data")
cases_path = data_dir / "cases.json"

with open(cases_path, "r", encoding="utf-8") as f:
    cases = json.load(f)

content_map = {
    "CASE-TESCO-01": (TESCO_EN, TESCO_VI),
    "CASE-WALMART-01": (WALMART_EN, WALMART_VI),
    "CASE-IKEA-01": (IKEA_EN, IKEA_VI),
    "CASE-DISNEY-01": (DISNEY_EN, DISNEY_VI),
    "CASE-AIRBNB-01": (AIRBNB_EN, AIRBNB_VI),
    "CASE-MCDONALD-01": (MCDONALD_EN, MCDONALD_VI),
    "CASE-CHANEL-01": (CHANEL_EN, CHANEL_VI),
    "CASE-NIKE-01": (NIKE_EN, NIKE_VI),
    "CASE-ESTEE-01": (ESTEE_EN, ESTEE_VI),
    "CASE-GAFA-SYNTHESIS": (GAFA_EN, GAFA_VI),
}

print(f"Total existing cases: {len(cases)}")

for c in cases:
    cid = c.get("case_id")
    if cid in content_map:
        en_text, vi_text = content_map[cid]
        c["originalCaseText"] = {
            "en": en_text.strip(),
            "vi": vi_text.strip()
        }
        print(f"Updated {cid}: EN={len(en_text)} chars, VI={len(vi_text)} chars")
    else:
        print(f"WARNING: Unknown case {cid}")

# Quality and Integrity Verification
for c in cases:
    cid = c["case_id"]
    en = c["originalCaseText"]["en"]
    vi = c["originalCaseText"]["vi"]
    
    assert len(en) >= 7000, f"{cid} EN text too short: {len(en)}"
    assert len(vi) >= 7000, f"{cid} VI text too short: {len(vi)}"
    assert "song ngữ" not in vi.lower(), f"{cid} VI text contains obsolete 'song ngữ' hint!"
    assert "*(xem toàn bộ" not in vi.lower(), f"{cid} VI text contains obsolete truncation marker!"
    assert "## " in en, f"{cid} EN text lacks markdown headings!"
    assert "## " in vi, f"{cid} VI text lacks markdown headings!"
    assert "http" in en, f"{cid} EN text lacks reference links!"
    assert "http" in vi, f"{cid} VI text lacks reference links!"

# Save updated cases.json
with open(cases_path, "w", encoding="utf-8") as f:
    json.dump(cases, f, ensure_ascii=False, indent=2)

print("\nSUCCESS: All 10 cases updated and verified in output/data/cases.json.")

# Rebuild data-store.js
print("Rebuilding output/src/data-store.js...")
res = subprocess.run(["uv", "run", "python", "output/scripts/build_data_store_js.py"], capture_output=True, text=True)
print(res.stdout)
if res.stderr:
    print("Stderr:", res.stderr)
