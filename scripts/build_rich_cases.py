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

# Load current cases to maintain backward compatibility
with open(data_dir / "cases.json", "r", encoding="utf-8") as f:
    existing_cases = json.load(f)
existing_by_id = {c["case_id"]: c for c in existing_cases}

def make_10_dimension_guide(problem_def_vi, problem_def_en,
                            evidence_vi, evidence_en,
                            stakeholders_vi, stakeholders_en,
                            root_cause_vi, root_cause_en,
                            alternatives_vi, alternatives_en,
                            criteria_vi, criteria_en,
                            recommendation_vi, recommendation_en,
                            implementation_vi, implementation_en,
                            risks_vi, risks_en,
                            metrics_vi, metrics_en):
    return {
        "problemDefinition": {
            "prompt": {"vi": "Xác định rõ vấn đề cốt lõi, triệu chứng bên ngoài và phạm vi ảnh hưởng tới trải nghiệm khách hàng.", "en": "Define core strategic problem, symptoms, and impact scope on customer experience."},
            "guidelines": {"vi": problem_def_vi, "en": problem_def_en}
        },
        "evidenceObservations": {
            "prompt": {"vi": "Trích dẫn các sự kiện định lượng, trích đoạn nguyên văn và số liệu thực chứng từ tài liệu gốc.", "en": "Cite quantitative facts, verbatim quotes, and empirical data points from source text."},
            "guidelines": {"vi": evidence_vi, "en": evidence_en}
        },
        "stakeholdersPerspectives": {
            "prompt": {"vi": "Phân tích quyền lợi, kỳ vọng và điểm đau (pain points) của từng nhóm liên quan (khách hàng, nhân viên tuyến đầu, quản lý, đối tác).", "en": "Analyze stakes, expectations, and pain points across all relevant groups (customers, front-line staff, managers, partners)."},
            "guidelines": {"vi": stakeholders_vi, "en": stakeholders_en}
        },
        "rootCauseAnalysis": {
            "prompt": {"vi": "Áp dụng phương pháp 5 Whys hoặc biểu đồ Xương cá để truy tìm nguyên nhân nền tảng về tổ chức, công nghệ, hoặc văn hóa.", "en": "Apply 5 Whys or Fishbone analysis to uncover structural, technological, or cultural root causes."},
            "guidelines": {"vi": root_cause_vi, "en": root_cause_en}
        },
        "alternativeSolutions": {
            "prompt": {"vi": "Đề xuất ít nhất 2-3 phương án chiến lược khả thi thay thế nhau để giải quyết vấn đề.", "en": "Formulate at least 2-3 viable strategic alternative options to address the issue."},
            "guidelines": {"vi": alternatives_vi, "en": alternatives_en}
        },
        "evaluationCriteria": {
            "prompt": {"vi": "Thiết lập các tiêu chí so sánh (chi phí, độ phức tạp công nghệ, rủi ro văn hóa, tác động tới CLV) để chọn lọc phương án.", "en": "Define evaluation criteria (financial feasibility, tech complexity, cultural risk, CLV impact) to rank options."},
            "guidelines": {"vi": criteria_vi, "en": criteria_en}
        },
        "recommendation": {
            "prompt": {"vi": "Lựa chọn giải pháp tối ưu nhất kèm luận cứ bảo vệ sắc bén và tuyên bố giá trị rõ ràng.", "en": "Select optimal recommendation with compelling rationale and clear value proposition."},
            "guidelines": {"vi": recommendation_vi, "en": recommendation_en}
        },
        "implementationPlan": {
            "prompt": {"vi": "Xây dựng lộ trình thực thi theo các giai đoạn (Ngắn hạn - Trung hạn - Dài hạn) với nguồn lực và vai trò cụ thể.", "en": "Construct phased execution roadmap (Short, Medium, Long term) detailing resources and ownership."},
            "guidelines": {"vi": implementation_vi, "en": implementation_en}
        },
        "risksTradeoffs": {
            "prompt": {"vi": "Nhận diện những rủi ro lớn nhất, điểm ma sát vận hành và các sự đánh đổi không thể tránh khỏi kèm giải pháp giảm thiểu.", "en": "Identify major risks, operational friction, unavoidable trade-offs, and mitigation safeguards."},
            "guidelines": {"vi": risks_vi, "en": risks_en}
        },
        "successMetrics": {
            "prompt": {"vi": "Xác định các chỉ số đo lường hiệu quả định lượng (CSAT, NPS, CLV, Tỷ lệ rời bỏ, Doanh thu trung bình trên khách hàng).", "en": "Establish quantitative success metrics and KPIs (CSAT, NPS, CLV, Churn rate, Average Basket Value)."},
            "guidelines": {"vi": metrics_vi, "en": metrics_en}
        }
    }

print("Loaded framework builder.")
