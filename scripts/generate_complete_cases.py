import json
from pathlib import Path
import re

out_dir = Path(r"C:\Kiến thức cần học\CRM\output")
data_dir = out_dir / "data"

# Load OCR data and Tesco raw text
ocr_path = Path(r"C:\Users\asus\.gemini\antigravity\brain\c80c2765-67a8-4f03-860d-5941cb0b0bea\scratch\all_cases_ocr.json")
with open(ocr_path, "r", encoding="utf-8-sig") as f:
    ocr_data = json.load(f)

tesco_path = Path(r"output/scratch/tesco_raw.txt")
with open(tesco_path, "r", encoding="utf-8") as f:
    tesco_raw = f.read()

# Load existing cases to preserve structure
with open(data_dir / "cases.json", "r", encoding="utf-8") as f:
    existing_cases = json.load(f)
existing_by_id = {c["case_id"]: c for c in existing_cases}

headers = [
    r'^\d*\s*CHAPTER\s+3\s+CUSTOMER\s+EXPERIENCE\s+IN\s+THE\s+RETAIL\s+SECTOR\s*',
    r'^\d*\s*CHAPTER\s+4\s+CUSTOMER\s+EXPERIENCE:\s+FOOD,\s+TOURISM,\s+LEISURE\s*',
    r'^\d*\s*CHAPTER\s+5\s+CUSTOMER\s+EXPERIENCE:\s+LUXURY\s+AND\s+FASHION\s*',
    r'^\d*\s*CHAPTER\s+1\s+CUSTOMER\s+EXPERIENCE:\s+THE\s+TECHNOLOGY\s+SECTOR\s*',
]
pattern = re.compile('|'.join(headers), re.IGNORECASE)

def clean_page(p_text):
    return pattern.sub('', p_text.strip())

# Extract verbatim texts
walmart_pages = [clean_page(ocr_data[f"Warmart_and_IKEA_p{p:02d}"]) for p in range(1, 6)]
walmart_p6 = clean_page(ocr_data["Warmart_and_IKEA_p06"][:733])
walmart_raw = "\n\n".join(walmart_pages) + "\n\n" + walmart_p6

ikea_p6 = clean_page(ocr_data["Warmart_and_IKEA_p06"][733:])
ikea_pages = [clean_page(ocr_data[f"Warmart_and_IKEA_p{p:02d}"]) for p in range(7, 13)]
ikea_raw = ikea_p6 + "\n\n" + "\n\n".join(ikea_pages)

disney_pages = [clean_page(ocr_data[f"Disney_and_AirBnB_and_McDonald_p{p:02d}"]) for p in range(1, 7)]
disney_p7 = clean_page(ocr_data["Disney_and_AirBnB_and_McDonald_p07"][:1540])
disney_raw = "\n\n".join(disney_pages) + "\n\n" + disney_p7

airbnb_p7 = clean_page(ocr_data["Disney_and_AirBnB_and_McDonald_p07"][1540:])
airbnb_pages = [clean_page(ocr_data[f"Disney_and_AirBnB_and_McDonald_p{p:02d}"]) for p in range(8, 12)]
airbnb_p12 = clean_page(ocr_data["Disney_and_AirBnB_and_McDonald_p12"][:1173])
airbnb_raw = airbnb_p7 + "\n\n" + "\n\n".join(airbnb_pages) + "\n\n" + airbnb_p12

mcdonald_p12 = clean_page(ocr_data["Disney_and_AirBnB_and_McDonald_p12"][1173:])
mcdonald_pages = [clean_page(ocr_data[f"Disney_and_AirBnB_and_McDonald_p{p:02d}"]) for p in range(13, 21)]
mcdonald_raw = mcdonald_p12 + "\n\n" + "\n\n".join(mcdonald_pages)

chanel_pages = [clean_page(ocr_data[f"Channel_and_Nike_and_Estee_p{p:02d}"]) for p in range(1, 6)]
chanel_p6 = clean_page(ocr_data["Channel_and_Nike_and_Estee_p06"][:1808])
chanel_raw = "\n\n".join(chanel_pages) + "\n\n" + chanel_p6

nike_p6 = clean_page(ocr_data["Channel_and_Nike_and_Estee_p06"][1808:])
nike_pages = [clean_page(ocr_data[f"Channel_and_Nike_and_Estee_p{p:02d}"]) for p in range(7, 18)]
nike_p18 = clean_page(ocr_data["Channel_and_Nike_and_Estee_p18"][:2043])
nike_raw = nike_p6 + "\n\n" + "\n\n".join(nike_pages) + "\n\n" + nike_p18

estee_p18 = clean_page(ocr_data["Channel_and_Nike_and_Estee_p18"][2043:])
estee_pages = [clean_page(ocr_data[f"Channel_and_Nike_and_Estee_p{p:02d}"]) for p in range(19, 24)]
estee_raw = estee_p18 + "\n\n" + "\n\n".join(estee_pages)

gafa_pages = [clean_page(ocr_data[f"Big_four_digital_firms_p{p:02d}"]) for p in range(1, 30)]
gafa_raw = "\n\n".join(gafa_pages)

tesco_cleaned = re.sub(r'--- PAGE \d+ ---', '', tesco_raw).strip()

print("Verbatim text extracted. Building structured case objects...")
