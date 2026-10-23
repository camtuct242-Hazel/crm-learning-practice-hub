import pypdf
from pathlib import Path
import json

ref_dir = Path("references")

# Let's inspect pages in Baran & Galka
baran_pdf = ref_dir / "Roger J. Baran  Robert J. Galka - Customer Relationship Management (0).pdf"
kosto_pdf = ref_dir / "CRM-Fundamentals.pdf"
tesco_pdf = ref_dir / "Case studies" / "Case Study_Tesco.pdf"

print("Opening PDFs...")
reader_b = pypdf.PdfReader(str(baran_pdf))
reader_k = pypdf.PdfReader(str(kosto_pdf))
reader_t = pypdf.PdfReader(str(tesco_pdf))

print(f"Baran pages: {len(reader_b.pages)}")
print(f"Kostojohn pages: {len(reader_k.pages)}")
print(f"Tesco pages: {len(reader_t.pages)}")

# 1. Kostojohn Four Pillars
print("\n--- Checking Kostojohn p. 11 / Four Pillars ---")
# Let's search Kostojohn pages 10-30 for 'pillars' or 'people, process'
for pno in range(10, 30):
    txt = reader_k.pages[pno].extract_text() or ""
    if "pillar" in txt.lower() or "four" in txt.lower():
        lines = [l for l in txt.splitlines() if any(w in l.lower() for w in ["pillar", "four", "people", "expectation"])]
        if lines:
            print(f"PDF page {pno+1}: {lines[:3]}")

# 2. Baran RFM and Recency
print("\n--- Checking Baran RFM ---")
for pno in range(190, 235):
    txt = reader_b.pages[pno].extract_text() or ""
    if "recency" in txt.lower() and "frequency" in txt.lower():
        lines = [l for l in txt.splitlines() if "rfm" in l.lower() or "recency" in l.lower()]
        print(f"PDF page {pno+1}: {lines[:2]}")
        break

# 3. Baran Customer Lifetime Value & Reichheld
print("\n--- Checking Baran CLV & Reichheld ---")
for pno in range(290, 335):
    txt = reader_b.pages[pno].extract_text() or ""
    if "reichheld" in txt.lower() or "5 percent" in txt.lower() or "5%" in txt:
        lines = [l for l in txt.splitlines() if "reichheld" in l.lower() or "retention" in l.lower()]
        print(f"PDF page {pno+1}: {lines[:2]}")
        break

# 4. Baran Balanced Scorecard
print("\n--- Checking Baran Balanced Scorecard ---")
for pno in range(330, 370):
    txt = reader_b.pages[pno].extract_text() or ""
    if "balanced scorecard" in txt.lower():
        lines = [l for l in txt.splitlines() if "balanced scorecard" in l.lower() or "kaplan" in l.lower()]
        print(f"PDF page {pno+1}: {lines[:2]}")
        break
