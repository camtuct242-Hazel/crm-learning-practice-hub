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

# Extract raw texts
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

raw_map = {
    "CASE-TESCO-01": tesco_cleaned,
    "CASE-WALMART-01": walmart_raw,
    "CASE-IKEA-01": ikea_raw,
    "CASE-DISNEY-01": disney_raw,
    "CASE-AIRBNB-01": airbnb_raw,
    "CASE-MCDONALD-01": mcdonald_raw,
    "CASE-CHANEL-01": chanel_raw,
    "CASE-NIKE-01": nike_raw,
    "CASE-ESTEE-01": estee_raw,
    "CASE-GAFA-SYNTHESIS": gafa_raw,
}

# Load current cases to maintain backward compatibility
with open(data_dir / "cases.json", "r", encoding="utf-8") as f:
    existing_cases = json.load(f)
existing_by_id = {c["case_id"]: c for c in existing_cases}

def build_10_dimension_guide(problem_def_vi, problem_def_en,
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
            "title": {"vi": "1. Xác định Vấn đề & Bối cảnh Chiến lược", "en": "1. Strategic Problem & Context Definition"},
            "prompt": {"vi": "Xác định rõ vấn đề cốt lõi, triệu chứng bên ngoài và phạm vi ảnh hưởng tới trải nghiệm khách hàng.", "en": "Define core strategic problem, symptoms, and impact scope on customer experience."},
            "guidelines": {"vi": problem_def_vi, "en": problem_def_en}
        },
        "evidenceObservations": {
            "title": {"vi": "2. Bằng chứng & Dữ liệu Nguồn Thực chứng", "en": "2. Empirical Evidence & Source Data"},
            "prompt": {"vi": "Trích dẫn các sự kiện định lượng, trích đoạn nguyên văn và số liệu thực chứng từ tài liệu gốc.", "en": "Cite quantitative facts, verbatim quotes, and empirical data points from source text."},
            "guidelines": {"vi": evidence_vi, "en": evidence_en}
        },
        "stakeholdersPerspectives": {
            "title": {"vi": "3. Các Bên Liên quan & Đa Góc nhìn", "en": "3. Stakeholders & Multi-Perspective Analysis"},
            "prompt": {"vi": "Phân tích quyền lợi, kỳ vọng và điểm đau (pain points) của từng nhóm liên quan (khách hàng, nhân viên tuyến đầu, quản lý, đối tác).", "en": "Analyze stakes, expectations, and pain points across all relevant groups (customers, front-line staff, managers, partners)."},
            "guidelines": {"vi": stakeholders_vi, "en": stakeholders_en}
        },
        "rootCauseAnalysis": {
            "title": {"vi": "4. Phân tích Nguyên nhân Gốc rễ", "en": "4. Root Cause Analysis (5 Whys / Ishikawa)"},
            "prompt": {"vi": "Áp dụng phương pháp 5 Whys hoặc biểu đồ Xương cá để truy tìm nguyên nhân nền tảng về tổ chức, công nghệ, hoặc văn hóa.", "en": "Apply 5 Whys or Fishbone analysis to uncover structural, technological, or cultural root causes."},
            "guidelines": {"vi": root_cause_vi, "en": root_cause_en}
        },
        "alternativeSolutions": {
            "title": {"vi": "5. Các Phương án Chiến lược Thay thế", "en": "5. Strategic Alternative Formulations"},
            "prompt": {"vi": "Đề xuất ít nhất 2-3 phương án chiến lược khả thi thay thế nhau để giải quyết vấn đề.", "en": "Formulate at least 2-3 viable strategic alternative options to address the issue."},
            "guidelines": {"vi": alternatives_vi, "en": alternatives_en}
        },
        "evaluationCriteria": {
            "title": {"vi": "6. Tiêu chí Đánh giá & So sánh Đánh đổi", "en": "6. Evaluation Criteria & Trade-off Matrix"},
            "prompt": {"vi": "Thiết lập các tiêu chí so sánh (chi phí, độ phức tạp công nghệ, rủi ro văn hóa, tác động tới CLV) để chọn lọc phương án.", "en": "Define evaluation criteria (financial feasibility, tech complexity, cultural risk, CLV impact) to rank options."},
            "guidelines": {"vi": criteria_vi, "en": criteria_en}
        },
        "recommendation": {
            "title": {"vi": "7. Khuyến nghị Giải pháp Tối ưu", "en": "7. Optimal Strategic Recommendation"},
            "prompt": {"vi": "Lựa chọn giải pháp tối ưu nhất kèm luận cứ bảo vệ sắc bén và tuyên bố giá trị rõ ràng.", "en": "Select optimal recommendation with compelling rationale and clear value proposition."},
            "guidelines": {"vi": recommendation_vi, "en": recommendation_en}
        },
        "implementationPlan": {
            "title": {"vi": "8. Kế hoạch Triển khai & Lộ trình Thực thi", "en": "8. Phased Implementation Roadmap"},
            "prompt": {"vi": "Xây dựng lộ trình thực thi theo các giai đoạn (Ngắn hạn - Trung hạn - Dài hạn) với nguồn lực và vai trò cụ thể.", "en": "Construct phased execution roadmap (Short, Medium, Long term) detailing resources and ownership."},
            "guidelines": {"vi": implementation_vi, "en": implementation_en}
        },
        "risksTradeoffs": {
            "title": {"vi": "9. Quản trị Rủi ro, Ma sát Vận hành & Dự phòng", "en": "9. Friction, Unavoidable Trade-offs & Mitigations"},
            "prompt": {"vi": "Nhận diện những rủi ro lớn nhất, điểm ma sát vận hành và các sự đánh đổi không thể tránh khỏi kèm giải pháp giảm thiểu.", "en": "Identify major risks, operational friction, unavoidable trade-offs, and mitigation safeguards."},
            "guidelines": {"vi": risks_vi, "en": risks_en}
        },
        "successMetrics": {
            "title": {"vi": "10. Chỉ số Đo lường Thành công (KPIs & Metrics)", "en": "10. Quantitative Success Metrics & KPIs"},
            "prompt": {"vi": "Xác định các chỉ số đo lường hiệu quả định lượng (CSAT, NPS, CLV, Tỷ lệ rời bỏ, Doanh thu trung bình trên khách hàng).", "en": "Establish quantitative success metrics and KPIs (CSAT, NPS, CLV, Churn rate, Average Basket Value)."},
            "guidelines": {"vi": metrics_vi, "en": metrics_en}
        }
    }

# Build rich cases dictionary
rich_cases = []

# 1. TESCO
tesco = existing_by_id["CASE-TESCO-01"]
tesco["originalCaseText"] = {
    "en": raw_map["CASE-TESCO-01"],
    "vi": "## Tình huống 5: Định hướng Khách hàng tại Tesco (Customer Orientation at Tesco)\n\n### Tác giả & Xuất xứ\nGiáo sư Gerhard Raab (Đại học Khoa học Ứng dụng Ludwigshafen, Đức). Trích giáo trình *Customer Relationship Management*, trang 173–183.\n\n### Lịch sử & Khởi đầu\nThành lập năm 1924 bởi Sir Jack Cohen, Tesco là nhà tiên phong bán lẻ thực phẩm tại Anh với việc mở siêu thị tự phục vụ đầu tiên năm 1948 và áp dụng tem đổi quà trong thập niên 1960. Đến năm 1985, Tesco mở đại siêu thị thứ 100 và chuyển hướng chiến lược sang chất lượng dịch vụ thay vì chỉ cạnh tranh về giá rẻ.\n\n### Cuộc cách mạng Thẻ Thân thiết Clubcard\nNăm 1995, Tesco bắt tay cùng công ty phân tích dữ liệu Dunnhumby giới thiệu thẻ Clubcard. Bằng cách phân tích dữ liệu giỏ hàng, Tesco phân chia khách hàng thành các cụm đặc trưng (Tiết kiệm, Truyền thống, Tiện lợi, Cao cấp, Sinh viên). Tesco gửi hàng triệu voucher giảm giá cá nhân hóa (hơn 8 triệu biến thể), đạt tỷ lệ phản hồi 8-14% (cao gấp nhiều lần mức 1-2% của toàn ngành). Dữ liệu này giúp Tesco vượt qua Sainsbury's để vươn lên dẫn đầu thị trường bán lẻ Anh quốc."
}
tesco["source_reference"] = {
    "document": "Customer Relationship Management",
    "authors": "Gerhard Raab, Riad A. Ajami, Vidyaranya B. Gargeya, G. Jason Goddard",
    "chapter": "Case Study 5: Customer Orientation at Tesco",
    "pages": "173-183",
    "publisher": "Academic Publication",
    "pdf_filename": "Case Study_Tesco.pdf",
    "extraction_method": "direct_pdf_text_verified"
}
tesco["discussion_questions"] = [
    {
        "q_num": 1,
        "prompt": {
            "vi": "Kết quả từ việc phân tích dữ liệu diện rộng đem lại cho Tesco kiến thức chi tiết về cấu trúc khách hàng phân hóa và nhu cầu đa dạng của họ. Đâu là những hệ quả trực tiếp và gián tiếp đối với doanh nghiệp từ việc sở hữu nguồn tri thức này?",
            "en": "As a result of its broad data analysis, Tesco receives detailed knowledge about the existing, differentiated customer structure, and the various needs, expectations, and desires that these customers have. What are the direct and indirect consequences of having this knowledge for the company?"
        },
        "model_answer": {
            "vi": "Hệ quả trực tiếp: Tối ưu danh mục sản phẩm từng siêu thị địa phương; tăng tỷ lệ quy đổi voucher lên 8-14%; cắt giảm lãng phí tiếp thị đại trà. Hệ quả gián tiếp: Tạo rào cản chuyển đổi cấu trúc (structural switching barrier); gia tăng CLV; mở rộng thành công sang Tesco Personal Finance và Tesco.com.",
            "en": "Direct: Localized merchandising, 8-14% voucher redemption, elimination of mass-mail waste. Indirect: Structural switching barriers, higher CLV, and low-risk expansion into financial services and e-commerce."
        }
    },
    {
        "q_num": 2,
        "prompt": {
            "vi": "Chiến lược quốc tế hóa của Tesco tại thời điểm nghiên cứu tình huống được mô tả như thế nào? Những rủi ro tiềm ẩn khi chuyển giao năng lực CRM từ thị trường quê nhà sang các thị trường quốc tế là gì?",
            "en": "How would you describe Tesco's international strategy at the time of the case? What were the underlying risks of transferring home-market CRM capabilities abroad?"
        },
        "model_answer": {
            "vi": "Tesco thâm nhập Trung Âu và Châu Á (Thái Lan, Hàn Quốc). Rủi ro lớn nhất là sự khác biệt văn hóa mua sắm và giả định sai lầm rằng thuật toán Clubcard có thể thay thế việc thấu hiểu thói quen tiêu dùng bản địa (minh chứng là sự sụp đổ của chuỗi Fresh & Easy tại Mỹ).",
            "en": "Tesco expanded across Central Europe and Asia. The fatal risk was algorithmic hubris—assuming UK loyalty models could replace deep local cultural immersion, which later caused the multibillion-dollar collapse of Fresh & Easy in the US."
        }
    },
    {
        "q_num": 3,
        "prompt": {
            "vi": "Chương trình 'First Class Service' của Tesco yêu cầu toàn thể nhân viên đánh giá 4 khía cạnh: Products, Presentation, Processes, People theo góc nhìn của khách hàng. Hãy phân tích vai trò của yếu tố Con người và Văn hóa tổ chức trong thành công của CRM tại Tesco.",
            "en": "Tesco's 'First Class Service' program requires all employees to examine 4 areas: Products, Presentation, Processes, People through the eyes of the customer. Analyze the role of People and Organizational Culture in Tesco's CRM success."
        },
        "model_answer": {
            "vi": "Đúng theo bộ ba Kostojohn et al. (80% Con người & Quy trình, 20% Công nghệ), dữ liệu Dunnhumby chỉ tạo ra giá trị khi nhân viên siêu thị tuyến đầu am hiểu các cụm khách hàng và chuyển hóa dữ liệu thành thái độ phục vụ ân cần tại quầy thanh toán.",
            "en": "Consistent with Kostojohn et al.'s finding that People and Process drive 80% of CRM outcomes, Dunnhumby's algorithms achieved competitive advantage only because frontline store staff embraced customer empathy at the cash register."
        }
    }
]
tesco["frameworkGuide"] = build_10_dimension_guide(
    "Bài toán dịch chuyển từ cạnh tranh giảm giá đơn thuần sang định vị chất lượng và gắn kết khách hàng bền vững bằng dữ liệu lớn.",
    "Strategic shift from commodity price wars to quality positioning and customer loyalty driven by big data analytics.",
    "Dữ liệu giỏ hàng Dunnhumby, hơn 8 triệu biến thể voucher, tỷ lệ phản hồi 8-14% so với 1-2% của ngành.",
    "Dunnhumby basket data, >8 million coupon variants, 8-14% redemption versus 1-2% industry benchmark.",
    "Khách hàng mua sắm gia đình, nhân viên thu ngân siêu thị, các nhà cung cấp hàng hóa, và đối tác phân tích Dunnhumby.",
    "Household shoppers, frontline cashiers, FMCG brand suppliers, and Dunnhumby data science partners.",
    "Các chiến dịch marketing đại trà không nắm bắt được sự phân hóa của người tiêu dùng hiện đại, gây lãng phí chi phí tiếp thị.",
    "Mass marketing treats heterogeneous shoppers homogeneously, leaking marketing capital and driving defection to discounters.",
    "Phương án 1: Đua giá rẻ với Asda; Phương án 2: Thẻ tích điểm cơ bản; Phương án 3: Nền tảng phân tích giỏ hàng cá nhân hóa siêu vi mô.",
    "Option 1: Price war with discounters; Option 2: Basic loyalty points; Option 3: Hyper-personalized predictive customer analytics platform.",
    "Chi phí đầu tư IT, Rào cản chuyển đổi khách hàng, Tác động lên biên lợi nhuận, và Khả năng nhân rộng hệ sinh thái.",
    "IT capital requirements, Structural switching barriers, Net margin protection, and Cross-category ecosystem extensibility.",
    "Khuyến nghị Phương án 3: Hợp tác sâu rộng với Dunnhumby, tích hợp dữ liệu Clubcard vào mọi quyết định nhập hàng và tiếp thị.",
    "Recommend Option 3: Deep strategic partnership with Dunnhumby, hardwiring Clubcard data into every purchasing and direct marketing workflow.",
    "Giai đoạn 1: Triển khai thử nghiệm; Giai đoạn 2: Phát hành tạp chí cá nhân hóa toàn quốc; Giai đoạn 3: Mở rộng Tesco Personal Finance và Tesco.com.",
    "Phase 1: Regional Clubcard pilot; Phase 2: Nationwide personalized coupon quarterly mailings; Phase 3: Financial services and online grocery scaling.",
    "Nguy cơ xâm phạm quyền riêng tư và sự bất mãn của các cửa hàng trưởng quen với việc quản lý cảm tính.",
    "Mitigate customer privacy concerns and frontline store manager skepticism toward centralized algorithmic directives.",
    "Tỷ lệ quét thẻ Clubcard trên tổng doanh thu, Tỷ lệ đổi voucher, NPS phân khúc, và Giá trị vòng đời khách hàng (CLV).",
    "Clubcard scan share of sales, Voucher redemption velocity, Segment NPS, and Customer Lifetime Value (CLV)."
)
tesco["socraticGuidance"] = {
    "key_strengths_to_look_for": ["Dunnhumby granular basket data", "Customer lifetime value (CLV)", "Direct marketing response rate vs mass advertising", "People-Process-Technology alignment via First Class Service"],
    "critical_tradeoffs": ["High data infrastructure costs vs uncertain redemption gains", "Centralized algorithmic merchandising vs local store manager autonomy"],
    "devil_advocate_questions": [
        "Nếu đối thủ sao chép chương trình thẻ tích điểm trong vòng 6 tháng (như Sainsbury's đã làm), điều gì thực sự ngăn cản khách hàng rời bỏ Tesco?",
        "Tesco đã mở rộng thành công tại Anh nhưng thất bại nặng nề với Fresh & Easy tại Mỹ. Dữ liệu Clubcard có làm lãnh đạo Tesco quá tự tin mù quáng (data hubris) hay không?"
    ]
}
rich_cases.append(tesco)

# Helper for Batat Cases
def make_batat(case_id, comp, t_vi, t_en, ind, ch, pp, bg_vi, bg_en, sp_vi, sp_en, steps, qs, chal, guide_args, soc_args):
    c_raw = raw_map[case_id]
    return {
        "case_id": case_id,
        "company": comp,
        "title": {"vi": t_vi, "en": t_en},
        "industry": ind,
        "source_reference": {
            "document": "Experiential Marketing: Case Studies in Customer Experience",
            "authors": "Wided Batat",
            "publisher": "Routledge",
            "chapter": ch,
            "pages": pp,
            "pdf_filename": "Case Study_" + ch.split(":")[0].replace(" ", "_") + ".pdf",
            "extraction_method": "windows_media_ocr_verified"
        },
        "background": {"vi": bg_vi, "en": bg_en},
        "strategic_problem": {"vi": sp_vi, "en": sp_en},
        "crm_framework_steps": steps,
        "originalCaseText": {
            "en": c_raw,
            "vi": f"## {t_vi}\n\n### Bối cảnh Tình huống Nguồn\n{bg_vi}\n\n### Thách thức Chiến lược Cốt lõi\n{sp_vi}\n\n### Trích đoạn Văn bản Giáo trình Gốc\n{c_raw[:2500]}\n\n*(Xem toàn bộ bản gốc tiếng Anh ở chế độ song ngữ bên trên)*"
        },
        "discussion_questions": qs,
        "challenge_prompt": chal,
        "frameworkGuide": build_10_dimension_guide(*guide_args),
        "socraticGuidance": soc_args
    }

# 2. WALMART
rich_cases.append(make_batat(
    "CASE-WALMART-01", "Walmart",
    "Tình huống 2: Ưu tiên Hàng đầu của Walmart: Trải nghiệm Khách hàng & Mua sắm Số hóa",
    "Case 2: Walmart's Top Priority: Customer Experience & Digitized Shopping",
    "Mass Retail & Omnichannel Supermarket",
    "Chapter 3: Customer Experience in the Retail Sector, Case 8", "87-92",
    existing_by_id["CASE-WALMART-01"]["background"]["vi"],
    existing_by_id["CASE-WALMART-01"]["background"]["en"],
    existing_by_id["CASE-WALMART-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-WALMART-01"]["strategic_problem"]["en"],
    existing_by_id["CASE-WALMART-01"]["crm_framework_steps"],
    [
        {
            "q_num": 1,
            "prompt": {
                "vi": "Phân tích cách Walmart sử dụng ứng dụng di động và công nghệ số để chuyển đổi trải nghiệm tại cửa hàng vật lý từ mua sắm truyền thống sang mua sắm số hóa (Phygital)?",
                "en": "Analyze how Walmart leverages its mobile app and digital technologies to transform in-store shopping from legacy retail into digitized phygital experiences?"
            },
            "model_answer": {
                "vi": "Walmart biến chiếc smartphone của khách hàng thành trợ lý mua sắm trực tiếp: định vị lối đi (Store Map), quét mã vạch kiểm tra giá, thanh toán Walmart Pay và đổi trả hàng trong 30 giây với Mobile Express Returns. Điều này loại bỏ điểm nghẽn xếp hàng chờ đợi lớn nhất tại các siêu thị lớn.",
                "en": "Walmart transforms the shopper's smartphone into an in-store navigator and copilot: real-time aisle mapping, barcode price checks, Walmart Pay touchless checkout, and 30-second Mobile Express Returns, eliminating retail's biggest friction point."
            }
        },
        {
            "q_num": 2,
            "prompt": {
                "vi": "Làm thế nào Walmart có thể triển khai mô hình 7Es của Marketing Trải nghiệm (Excite, Educate, Entertain, Elevate, Evangelize, Empower, Enrich) để cạnh tranh với sự bành trướng của Amazon?",
                "en": "How can Walmart implement the 7Es experiential marketing mix framework to differentiate its grocery retail model against Amazon's relentless expansion?"
            },
            "model_answer": {
                "vi": "Walmart tận dụng lợi thế vật lý độc nhất (90% người dân Mỹ sống trong bán kính 10 dặm của một cửa hàng Walmart) kết hợp cùng ứng dụng số để kích hoạt 7Es: Empower (trao quyền chọn giao hàng hoặc curbside pickup), Elevate (nâng tầm trải nghiệm thực phẩm tươi sống), Enrich (tiết kiệm thời gian quý giá của các gia đình bận rộn).",
                "en": "Walmart mobilizes its unmatched physical asset density (90% of US population within 10 miles of a store) alongside digital agility to activate the 7Es: Empowering shoppers with flexible curbside pickup, Elevating fresh food quality inspection, and Enriching household well-being through time savings."
            }
        }
    ],
    {
        "role": "Chief Experience Officer (CXO) at Walmart",
        "prompt": {
            "vi": "Hãy tưởng tượng bạn được bổ nhiệm làm Giám đốc Trải nghiệm (CXO) tại Walmart. Bạn muốn tạo ra một cửa hàng ý tưởng trải nghiệm mới kết hợp cả góc nhìn của người tiêu dùng lẫn nhân viên. Bạn sẽ sử dụng 7Es như thế nào để khách hàng cảm thấy thích thú và nhân viên gắn kết?",
            "en": "Imagine you have been hired to be the Chief Experience Officer (CXO) at Walmart. You want to create a new experiential concept store that integrates both consumer and employee perspectives. How would you use the 7Es to design the ultimate experience where shoppers are enchanted and employees are committed?"
        }
    },
    (
        "Thách thức chuyển đổi từ siêu thị chi phí thấp sang hệ sinh thái bán lẻ phygital đa kênh đối đầu trực diện với Amazon.",
        "Strategic pivot from low-cost transactional discount warehouse to omnichannel phygital powerhouse confronting Amazon.",
        "Mạng lưới 4.700+ siêu thị tại Mỹ, ứng dụng Walmart App với Mobile Express Returns, Scan & Go, dịch vụ Curbside Grocery Pickup.",
        "Footprint across 4,700+ US stores, Walmart App adoption, Mobile Express Returns, and Curbside Grocery Pickup statistics.",
        "Khách hàng gia đình, nhân viên nhặt hàng tại lối đi, nhân viên thu ngân, và ban điều hành chuỗi cung ứng.",
        "Budget-conscious family shoppers, in-store floor associates, e-commerce order pickers, and corporate logistics executives.",
        "Quy mô vật lý đồ sộ và văn hóa tiết kiệm chi phí nghiêm ngặt trong lịch sử làm chậm tốc độ cải tiến trải nghiệm người dùng.",
        "Legacy footprint inertia and ultra-frugal corporate DNA historically underinvesting in digital customer journey ergonomics.",
        "Phương án 1: Mở rộng bán lẻ online đơn thuần qua Jet.com; Phương án 2: Tích hợp Phygital biến 4.700 siêu thị thành trung tâm giao nhận và trải nghiệm.",
        "Option 1: Pure-play digital expansion via acquired Jet.com; Option 2: Unified Phygital transformation turning 4,700 stores into local fulfillment & experience hubs.",
        "Mức độ giảm thiểu điểm ma sát (Friction reduction), Chi phí hoàn tất đơn hàng trên mỗi giỏ, và Tỷ lệ hài lòng CSAT.",
        "Friction reduction, Supply chain last-mile fulfillment cost per order, and In-store Customer Satisfaction (CSAT).",
        "Khuyến nghị Phương án 2: Tận dụng mật độ cửa hàng thực tế để dẫn đầu dịch vụ nhận hàng tạp hóa lề đường (Curbside Grocery Pickup).",
        "Recommend Option 2: Capitalize on physical store proximity to dominate same-day grocery pickup while integrating Walmart App as the in-store digital companion.",
        "Lộ trình: Nâng cấp trải nghiệm ứng dụng di động, đào tạo chuyên viên nhặt hàng Personal Shoppers, và lắp đặt tháp nhận hàng tự động.",
        "Phased roadmap: Standardize mobile ordering UX, upskill store associates as dedicated Personal Shoppers, and scale automated pickup towers.",
        "Nguy cơ xung đột không gian giữa nhân viên đẩy xe nhặt hàng và khách hàng đi lại trong lối đi hẹp.",
        "Address physical congestion between store pickers and shoppers in aisles, and mitigate quality variance in fresh produce selection.",
        "Thời gian chờ nhận hàng tại bãi xe (<5 phút), Tỷ lệ tái đặt hàng qua app, và Doanh số bán hàng đa kênh.",
        "Curbside pickup parking dwell time (<5 minutes), mobile app repeat order velocity, and omnichannel customer lifetime value."
    ),
    {
        "key_strengths_to_look_for": ["Phygital integration", "Omnichannel convenience", "Curbside grocery pickup leverage", "7Es framework alignment"],
        "critical_tradeoffs": ["Investing billions in digital app features vs maintaining 'Everyday Low Price' (EDLP) margin structure"],
        "devil_advocate_questions": [
            "Nếu khách hàng thích mua sắm online hoàn toàn tại nhà, liệu chiến lược kéo họ đến bãi đỗ xe lấy hàng (Curbside Pickup) có phải chỉ là bước đệm tạm thời?",
            "Làm thế nào để Walmart nâng cao trải nghiệm khách hàng khi nhân viên tuyến đầu vẫn nhận mức lương cơ bản và đối mặt với áp lực ca kíp căng thẳng?"
        ]
    }
))

# 3. IKEA
rich_cases.append(make_batat(
    "CASE-IKEA-01", "IKEA",
    "Tình huống 3: Thiết kế Trải nghiệm Kỳ diệu & Hành trình Sống Thường nhật tại IKEA",
    "Case 3: Designing a Magical Customer Experience & Everyday Life Journey at IKEA",
    "Home Furnishing & Ready-to-Assemble Furniture",
    "Chapter 3: Customer Experience in the Retail Sector, Case 9", "92-98",
    existing_by_id["CASE-IKEA-01"]["background"]["vi"],
    existing_by_id["CASE-IKEA-01"]["background"]["en"],
    existing_by_id["CASE-IKEA-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-IKEA-01"]["strategic_problem"]["en"],
    existing_by_id["CASE-IKEA-01"]["crm_framework_steps"],
    [
        {
            "q_num": 1,
            "prompt": {
                "vi": "IKEA đã phát triển chiến lược marketing như thế nào để tích hợp trải nghiệm khách hàng dựa trên cuộc sống thực tế của họ ('Life at Home')?",
                "en": "How has Ikea evolved its marketing strategy to integrate customer experience based on the real lives of its customers ('Life at Home')?"
            },
            "model_answer": {
                "vi": "IKEA thực hiện các chuyến thăm nhà dân tộc học (ethnographic home visits) hàng năm để nghiên cứu thói quen sinh hoạt thực tế, từ đó thiết kế các giải pháp nội thất giải quyết đúng không gian chật hẹp, kết hợp ứng dụng AR IKEA Place cho phép người dùng ướm thử đồ nội thất 3D vào căn phòng thật trước khi mua.",
                "en": "IKEA conducts thousands of ethnographic in-home visits annually to uncover latent domestic pain points, designing modular furniture for cramped urban spaces, augmented by the IKEA Place AR app enabling customers to visualize 3D items in their living rooms before purchasing."
            }
        },
        {
            "q_num": 2,
            "prompt": {
                "vi": "Phân tích cách IKEA kết hợp giữa mê cung bán hàng (maze showroom), nhà hàng thịt viên Thụy Điển và khu vui chơi Småland để tạo nên một hành trình trải nghiệm giác quan khó quên.",
                "en": "Analyze how IKEA blends the guided maze showroom, Swedish meatball restaurant, and Småland children's playground to create an immersive sensory customer journey."
            },
            "model_answer": {
                "vi": "IKEA kéo dài thời gian lưu lại cửa hàng (dwell time) bằng cách biến chuyến mua sắm thành chuyến dã ngoại gia đình. Bữa ăn giá rẻ tại khu ẩm thực giải tỏa cảm giác đói và mệt mỏi, khu gửi trẻ Småland giải phóng phụ huynh khỏi sự phân tâm, và lối đi một chiều có chủ ý kích thích mua sắm bốc đồng (impulse buys) với các mặt hàng nhỏ giá rẻ bố trí dọc đường.",
                "en": "IKEA extends store dwell time by engineering shopping into a family leisure outing. Low-cost Swedish meatballs satisfy physical fatigue, Småland child care alleviates parental stress, and the serpentine one-way showroom path maximizes browsing exposure to trigger high-margin impulse purchases."
            }
        }
    ],
    {
        "role": "Chief Experience Officer (CXO) at IKEA",
        "prompt": {
            "vi": "IKEA có thể điều chỉnh các cửa hàng của mình như thế nào để phục vụ người khuyết tật và người cao tuổi một cách tiện lợi và dễ dàng nhất trong suốt các giai đoạn mua sắm?",
            "en": "Explain how Ikea can adapt its stores to accommodate disabled and elderly people by offering them a suitable and convenient shopping experience across all purchase phases?"
        }
    },
    (
        "Dịch chuyển từ mô hình siêu thị mê cung ngoại ô sang hệ thống cửa hàng vệ tinh trung tâm thành phố và giải pháp số hóa AR.",
        "Strategic evolution from suburban self-assembly warehouse labyrinths to accessible omnichannel urban satellite formats.",
        "Khảo sát dân tộc học 'Life at Home', ứng dụng IKEA Place trên nền tảng Apple ARKit, doanh thu ẩm thực nhà hàng Thụy Điển.",
        "Empirical data from annual 'Life at Home' ethnographic field research, IKEA Place AR spatial analytics, and food court revenue.",
        "Các hộ gia đình trẻ, người cao tuổi, người tiêu dùng căn hộ nhỏ đô thị, và đội ngũ nhân viên hậu cần kho.",
        "Young urban apartment dwellers, elderly shoppers, warehouse logistics staff, and Ingka Group store managers.",
        "Hành trình một chiều cố định gây kiệt sức và bất tiện cho nhóm khách hàng có nhu cầu mua nhanh hoặc hạn chế về khả năng vận động.",
        "Rigid one-way maze layout induces sensory fatigue and friction for mission-driven shoppers needing quick targeted item retrieval.",
        "Phương án 1: Duy trì quy mô đại siêu thị ngoại ô; Phương án 2: Mô hình kết hợp studio thiết kế đô thị và kho tự động giao hàng tận nhà.",
        "Option 1: Retain massive out-of-town warehouse model; Option 2: Hybrid Phygital network pairing downtown planning studios with centralized automated delivery.",
        "Mức độ nỗ lực của khách hàng (Customer Effort Score), Độ phủ tại các đô thị đông đúc, và Chi phí giao hàng chặng cuối.",
        "Customer journey friction, Geographic penetration, Last-mile assembly/delivery cost, and Circular economy sustainability.",
        "Khuyến nghị Phương án 2: Phát triển chuỗi IKEA Planning Studio tại lõi đô thị kết hợp dịch vụ lắp đặt TaskRabbit và công cụ AR.",
        "Recommend Option 2: Deploy urban Planning Studios in major metropolitan centers, seamlessly linked to online catalog and white-glove TaskRabbit assembly.",
        "Lộ trình: Khai trương studio tại trung tâm đô thị lớn, tích hợp nền tảng hoạch định 3D trên đám mây, và tối ưu hóa logistics giao hàng nhanh.",
        "Roadmap: Pilot urban format in major metros, streamline local micro-fulfillment logistics, and integrate AI-assisted room layout generators.",
        "Rủi ro suy giảm doanh số mua sắm bốc đồng (impulse buys) khi khách hàng không đi qua toàn bộ lối đi trưng bày dài.",
        "Mitigate drop in spontaneous impulse purchases that traditionally occur along the serpentine warehouse path.",
        "Customer Effort Score (CES), Tỷ lệ chuyển đổi đơn hàng qua ứng dụng AR, Điểm hài lòng về dịch vụ giao lắp, và Doanh thu trên mỗi m2.",
        "Digital planner conversion rate, Customer Effort Score (CES), Omnichannel average order value, and Assembly satisfaction score."
    ),
    {
        "key_strengths_to_look_for": ["Ethnographic research ('Life at Home')", "IKEA Effect (co-creation of value via assembly)", "Sensory journey mapping (food + showroom)", "AR Phygital integration"],
        "critical_tradeoffs": ["The convenience of urban quick-shops vs the high-margin impulse browsing created by the suburban maze"],
        "devil_advocate_questions": [
            "Hiện tượng 'IKEA Effect' (người dùng yêu quý món đồ hơn khi tự tay lắp ráp) có còn đúng với thế hệ Gen Z chuộng sự tiện lợi và tức thì hay không?",
            "Nếu IKEA chuyển sang bán hàng trực tuyến nhiều hơn, làm sao bù đắp được khoảng trống doanh thu và cảm xúc từ nhà hàng ẩm thực Thụy Điển?"
        ]
    }
))

# 4. DISNEY
rich_cases.append(make_batat(
    "CASE-DISNEY-01", "The Walt Disney Company",
    "Tình huống 4: Làm thế nào Disney Tạo nên Trải nghiệm Khách hàng Kỳ diệu?",
    "Case 4: How Does Disney Create a Magical Customer Experience?",
    "Theme Parks, Entertainment & Leisure",
    "Chapter 4: Customer Experience: Food, Tourism, Leisure, Case 10", "102-108",
    existing_by_id["CASE-DISNEY-01"]["background"]["vi"],
    existing_by_id["CASE-DISNEY-01"]["background"]["en"],
    existing_by_id["CASE-DISNEY-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-DISNEY-01"]["strategic_problem"]["en"],
    existing_by_id["CASE-DISNEY-01"]["crm_framework_steps"],
    [
        {
            "q_num": 1,
            "prompt": {
                "vi": "Điều gì tạo nên sự độc đáo và đáng nhớ trong trải nghiệm tại Disneyland? Disneyland đã thích ứng như thế nào khi mở rộng sang các nền văn hóa khác nhau (Paris, Tokyo, Shanghai)?",
                "en": "What makes the experience in Disneyland unique and memorable? How is Disneyland adapting to other cultures (Paris, Tokyo, Shanghai)?"
            },
            "model_answer": {
                "vi": "Trải nghiệm Disney độc đáo nhờ nghệ thuật kể chuyện nhập vai (immersive storytelling), sự tận tâm của các 'Cast Members' được đào tạo theo triết lý 'The Disney Way', và công nghệ vòng đeo tay MagicBand (MyMagic+) giúp loại bỏ ma sát tại các điểm chạm (mở cửa phòng khách sạn, thanh toán, vào cổng không cần vé giấy, đặt chỗ trò chơi FastPass). Khi mở rộng quốc tế, Disney bản địa hóa ẩm thực, phong tục nhưng vẫn giữ chuẩn mực dịch vụ hiếu khách cốt lõi.",
                "en": "The Disney experience is anchored in immersive storytelling, obsessive Cast Member hospitality culture ('The Disney Way'), and frictionless RFID MagicBand touchpoints (hotel key, ticketless park entry, FastPass reservations, and cashless dining). Internationally, Disney localizes culinary preferences and folklore while fiercely preserving its baseline showmanship standards."
            }
        },
        {
            "q_num": 2,
            "prompt": {
                "vi": "Làm thế nào Disneyland tạo ra digital storytelling và đảm bảo giá trị chia sẻ với khách hàng cả trực tuyến lẫn tại công viên?",
                "en": "How does Disneyland create digital storytelling and guarantee the value shared with its customers online and in its parks?"
            },
            "model_answer": {
                "vi": "Disney kết nối hành trình trước chuyến đi (ứng dụng My Disney Experience lên lịch trình, đặt bàn), trong chuyến đi (ảnh chụp tự động PhotoPass đồng bộ tức thì vào tài khoản qua RFID), và sau chuyến đi (album kỷ niệm số hóa), biến một kỳ nghỉ hữu hình thành ký ức tinh thần sống mãi.",
                "en": "Disney bridges the pre-trip phase (My Disney Experience itinerary planning and dining reservations), in-park phase (automated PhotoPass ride captures synced via RFID to mobile wallets), and post-trip phase (digital memory albums), transforming a perishable vacation into lifelong emotional brand equity."
            }
        }
    ],
    {
        "role": "Chief Experience Officer (CXO) at Disney Parks",
        "prompt": {
            "vi": "Hãy tưởng tượng bạn được bổ nhiệm làm Giám đốc Trải nghiệm (CXO) tại Disneyland. Công việc của bạn là thực hiện chiến lược tiếp thị trải nghiệm tổng thể và kết nối công viên giải trí vật lý với các nền tảng trực tuyến. Đâu là điểm khởi đầu của bạn để mang lại hành trình du khách liền mạch?",
            "en": "Imagine you have been hired to be the Chief Experience Officer (CXO) at Disneyland. Your job is to implement Disney's overall experiential marketing strategy and connect its physical amusement park with online platforms. What would be your starting point to identify touchpoints and fluidify the visitor journey?"
        }
    },
    (
        "Thách thức cân bằng giữa việc nâng cao công nghệ số tự động hóa (MagicBand, Genie+) và bảo tồn cảm xúc ma thuật nhân văn từ đội ngũ nhân viên Cast Members.",
        "Balancing high-tech frictionless automation (MagicBand, Genie+ algorithms) with high-touch human emotional magic delivered by frontline Cast Members.",
        "Hệ thống vòng tay RFID MagicBand trị giá 1 tỷ USD, ứng dụng My Disney Experience, chương trình FastPass/Genie+, tỷ lệ giữ chân khách quay lại 70%.",
        "$1 Billion MyMagic+ investment, MagicBand RFID sensors across resorts, My Disney Experience mobile platform, and 70% repeat guest loyalty.",
        "Du khách gia đình có trẻ nhỏ, nhân viên công viên (Cast Members), quản lý vận hành trò chơi, và ban lãnh đạo bộ phận Disney Parks & Experiences.",
        "Family vacationers with young children, park frontline Cast Members, ride attraction operations, and Disney Parks & Experiences leadership.",
        "Thời gian chờ đợi xếp hàng kéo dài (queuing friction) và sự đông đúc vào mùa cao điểm làm suy giảm nghiêm trọng chỉ số hài lòng của du khách.",
        "Excessive queue dwell times and seasonal park overcrowding degrading guest emotional satisfaction and triggering parental fatigue.",
        "Phương án 1: Tăng giá vé để thanh lọc lượng khách; Phương án 2: Tối ưu hóa điều phối dòng khách bằng hệ sinh thái IoT MagicBand và thuật toán đặt chỗ ảo.",
        "Option 1: Aggressive surge pricing to cap crowd capacity; Option 2: Virtual queuing, smart algorithmic load-balancing, and IoT MagicBand ecosystem.",
        "Mức độ giảm thời gian chờ đợi tại hàng xếp, Chi tiêu trung bình của mỗi gia đình (Per-capita guest spend), và Điểm cảm xúc hạnh phúc Net Promoter Score.",
        "Average queue dwell reduction, In-park per-capita guest spend, Family emotional Net Promoter Score, and Cast Member engagement.",
        "Khuyến nghị Phương án 2: Hoàn thiện hệ sinh thái MyMagic+ và ứng dụng thuật toán đề xuất hành trình thời gian thực để phân tán dòng người.",
        "Recommend Option 2: Deploy comprehensive MyMagic+ IoT ecosystem with dynamic real-time ride recommendations to balance guest distribution.",
        "Lộ trình: Nâng cấp cảm biến RFID toàn công viên, đào tạo văn hóa 'Traditions' cho Cast Members, và ra mắt tính năng đặt món di động trước.",
        "Phased roadmap: Expand parkwide ultra-wideband RFID sensors, reinforce legendary 'Traditions' training for staff, and scale mobile food pre-ordering.",
        "Rủi ro du khách cảm thấy bị quá tải bởi việc phải nhìn vào màn hình điện thoại liên tục thay vì tận hưởng không khí cùng gia đình.",
        "Mitigate 'screen fatigue' where parents spend entire vacations managing itineraries on smartphones rather than being emotionally present with children.",
        "Thời gian xếp hàng thực tế so với kỳ vọng, Tỷ lệ nụ cười và đánh giá Cast Member xuất sắc, Chi tiêu dịch vụ gia tăng, và Tỷ lệ quay lại trong 3 năm.",
        "Wait-time deviation ratio, Frontline Cast Member compliment scores, In-park food & merch spend, and 3-year guest return velocity."
    ),
    {
        "key_strengths_to_look_for": ["MyMagic+ / MagicBand RFID ecosystem", "Frictionless guest journey", "Cast Member emotional empowerment ('The Disney Way')", "Narrative digital storytelling"],
        "critical_tradeoffs": ["Frictionless smartphone scheduling vs destroying spontaneous vacation wandering", "Surge pricing for crowd control vs alienating working-class families"],
        "devil_advocate_questions": [
            "Khi Disney chuyển từ hệ thống FastPass miễn phí sang dịch vụ trả phí Genie+ / Lightning Lane, liệu công ty có đang hy sinh lòng tin thương hiệu vì lợi nhuận ngắn hạn?",
            "Nếu một vòng tay MagicBand theo dõi mọi bước chân của du khách, lằn ranh giữa 'dịch vụ chu đáo cá nhân hóa' và 'giám sát vi phạm quyền riêng tư' nằm ở đâu?"
        ]
    }
))

# 5. AIRBNB
rich_cases.append(make_batat(
    "CASE-AIRBNB-01", "Airbnb",
    "Tình huống 5: Airbnb: Chuyển đổi Ngành Lưu trú qua Trải nghiệm Khách hàng & Cộng đồng",
    "Case 5: Airbnb: Transforming Hospitality through Customer Experience & Community",
    "Hospitality, Peer-to-Peer Platform & Travel Tech",
    "Chapter 4: Customer Experience: Food, Tourism, Leisure, Case 11", "108-113",
    existing_by_id["CASE-AIRBNB-01"]["background"]["vi"],
    existing_by_id["CASE-AIRBNB-01"]["background"]["en"],
    existing_by_id["CASE-AIRBNB-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-AIRBNB-01"]["strategic_problem"]["en"],
    existing_by_id["CASE-AIRBNB-01"]["crm_framework_steps"],
    [
        {
            "q_num": 1,
            "prompt": {
                "vi": "Nền tảng chia sẻ của Airbnb tạo dựng niềm tin và lòng trung thành của khách hàng như thế nào so với các chuỗi khách sạn truyền thống?",
                "en": "How does Airbnb's peer-to-peer platform cultivate customer trust and loyalty compared to traditional hotel chains?"
            },
            "model_answer": {
                "vi": "Airbnb thiết kế kiến trúc niềm tin (Trust Architecture) thông qua việc xác thực danh tính nhiều lớp, hệ thống đánh giá hai chiều mù đôi (double-blind mutual reviews), bảo hiểm thiệt hại Host Guarantee trị giá 1 triệu USD và cổng thanh toán giữ tiền bảo đảm escrow. Khác với sự đồng nhất vô cảm của khách sạn chuỗi, Airbnb mang lại trải nghiệm bản địa độc bản giúp khách cảm nhận thông điệp 'Belong Anywhere'.",
                "en": "Airbnb architects systemic peer trust via multi-factor identity verification, double-blind reciprocal reviews, a $1 Million Host Guarantee safety net, and secure escrow payments. In contrast to sterile hotel homogenization, Airbnb delivers authentic localized immersion, actualizing the core brand promise of 'Belong Anywhere.'"
            }
        },
        {
            "q_num": 2,
            "prompt": {
                "vi": "Airbnb đã phát triển chiến lược marketing như thế nào để tích hợp trải nghiệm khách hàng với các chiến lược số và truyền thông? Những thay đổi này có phù hợp với nhu cầu du khách hiện đại?",
                "en": "How has Airbnb evolved its marketing strategy to integrate customer experience with digital and communication strategies? Are these changes in line with the needs of today's tourists?"
            },
            "model_answer": {
                "vi": "Airbnb mở rộng từ việc cho thuê chỗ ở thuần túy sang cung cấp trải nghiệm do người dân bản địa dẫn dắt (Airbnb Experiences), kết hợp thuật toán gợi ý điểm đến dựa trên sở thích cá nhân, đồng thời xây dựng cộng đồng gắn kết thông qua các câu chuyện kể từ chính các chủ nhà (Superhost community).",
                "en": "Airbnb expanded beyond pure lodging transactions into handcrafted localized Airbnb Experiences, deploying machine learning destination curation while nurturing organic user-generated storytelling across its high-status Superhost network."
            }
        }
    ],
    {
        "role": "Chief Experience Officer (CXO) at Airbnb",
        "prompt": {
            "vi": "Hãy tưởng tượng bạn được bổ nhiệm làm Giám đốc Trải nghiệm (CXO) tại Airbnb. Công việc của bạn là tạo ra một chuỗi khách sạn vật lý của Airbnb kết hợp trải nghiệm của khách với công nghệ và dữ liệu. Bạn sẽ sử dụng 7Es như thế nào để định vị Airbnb trong lĩnh vực lưu trú?",
            "en": "Imagine you have been hired to be the Chief Experience Officer (CXO) at Airbnb. Your job is to create a physical Airbnb hotel chain that integrates the guest experience and the use of technology and data. How would you use the 7Es tool of experiential marketing to design the ultimate guest experience?"
        }
    },
    (
        "Thách thức kiểm soát chất lượng đồng đều và quản trị an toàn trên một mạng lưới hàng triệu chủ nhà độc lập mà không làm mất đi tính độc bản nguyên sơ.",
        "Scaling quality consistency, security, and trust compliance across millions of independent peer hosts without destroying local grassroots authenticity.",
        "Quy mô hàng triệu phòng lưu trú tại 190+ quốc gia, chương trình Superhost, chính sách bảo hiểm Host Guarantee, dịch vụ Airbnb Experiences.",
        "Over 6 million active listings across 190+ countries, Superhost retention rates, $1M Host Guarantee claims data, and Airbnb Experiences ratings.",
        "Khách du lịch (Guests), Chủ nhà cá nhân (Hosts), Cư dân địa phương tại các khu phố, và Cơ quan quản lý chính quyền sở tại.",
        "Global travelers, residential property hosts, local neighborhood communities, and municipal regulatory bodies.",
        "Mô hình kinh tế chia sẻ phụ thuộc hoàn toàn vào niềm tin giữa hai người xa lạ; bất kỳ sự cố an toàn hoặc phân biệt đối xử nào cũng đe dọa sự tồn vong của thương hiệu.",
        "Two-sided platform vulnerability where a single safety violation, property damage incident, or discrimination dispute damages brand goodwill.",
        "Phương án 1: Chuyển hướng sang vận hành các tòa nhà căn hộ do công ty trực tiếp quản lý; Phương án 2: Tăng cường hệ thống xác thực AI, chuẩn hóa Superhost và cơ chế xử lý tranh chấp 24/7.",
        "Option 1: Pivot toward company-leased, professionally managed apart-hotels; Option 2: Reinforce algorithmic trust verification, Superhost status tiers, and 24/7 rapid mediation.",
        "Mức độ tin cậy và an toàn (Safety rating), Tỷ lệ hoàn thành đặt phòng thành công, Tỷ lệ tranh chấp khiếu nại, và Tỷ lệ khách hàng quay lại.",
        "Platform trust score, Booking fulfillment rate, Dispute escalation frequency, and Lifetime guest retention.",
        "Khuyến nghị Phương án 2: Đầu tư sâu vào công nghệ xác thực danh tính số, bảo vệ cả hai phía và phát triển danh mục Airbnb Plus/Luxe để đáp ứng tiêu chuẩn cao cấp.",
        "Recommend Option 2: Fortify double-blind review integrity, scale AI risk scoring on bookings, and elevate verified Airbnb Plus/Luxe quality audits.",
        "Lộ trình: Thắt chặt chính sách chống phân biệt đối xử, ra mắt hỗ trợ khẩn cấp tại chỗ qua hotline toàn cầu, và mở rộng phân khúc du lịch trải nghiệm.",
        "Roadmap: Enforce strict anti-bias community commitments, deploy dedicated 24/7 Safety Response Teams, and expand curated Airbnb Experiences.",
        "Rủi ro phản ứng pháp lý từ chính quyền các thành phố du lịch do đẩy giá thuê nhà lên cao và làm mất trật tự dân cư.",
        "Mitigate municipal regulatory crackdowns and local tenant protests regarding rental inflation and neighborhood gentrification.",
        "Chỉ số NPS từ cả phía Host và Guest, Tỷ lệ tranh chấp được giải quyết trong 2 giờ, Tỷ lệ chuyển đổi sang Airbnb Experiences, và Lợi nhuận gộp trên mỗi lượt đêm.",
        "Reciprocal Host/Guest NPS, Median dispute resolution speed (<2 hours), Cross-booking into Experiences, and Gross Booking Value per Night."
    ),
    {
        "key_strengths_to_look_for": ["Two-sided platform trust architecture", "Double-blind reviews", "Belong Anywhere emotional branding", "Community co-creation"],
        "critical_tradeoffs": ["Standardized safety and cleaning checklists vs organic idiosyncratic homeowner charm"],
        "devil_advocate_questions": [
            "Khi các công ty quản lý bất động sản chuyên nghiệp (commercial property managers) chiếm tỷ lệ ngày càng lớn trên Airbnb, liệu nền tảng có đang biến thành một trang đặt phòng khách sạn thông thường?",
            "Nếu một chủ nhà hủy phòng của khách vào phút chót tại một thành phố xa lạ, hệ thống CRM của Airbnb xử lý trải nghiệm tồi tệ này ra sao để giữ chân khách hàng?"
        ]
    }
))

print("Cases 1-5 built. Building 6-10...")

# 6. MCDONALD'S
rich_cases.append(make_batat(
    "CASE-MCDONALD-01", "McDonald's",
    "Tình huống 6: Nâng tầm Trải nghiệm Thức ăn Nhanh Cả Trực tuyến & Trực tiếp tại McDonald's",
    "Case 6: Elevating Fast-Food Customer Experience Online & Offline at McDonald's",
    "Fast Food & Quick Service Restaurants (QSR)",
    "Chapter 4: Customer Experience: Food, Tourism, Leisure, Case 12", "113-121",
    existing_by_id["CASE-MCDONALD-01"]["background"]["vi"],
    existing_by_id["CASE-MCDONALD-01"]["background"]["en"],
    existing_by_id["CASE-MCDONALD-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-MCDONALD-01"]["strategic_problem"]["en"],
    existing_by_id["CASE-MCDONALD-01"]["crm_framework_steps"],
    [
        {
            "q_num": 1,
            "prompt": {
                "vi": "Kiosk tự phục vụ và ứng dụng di động đã giúp McDonald's cải thiện hành trình khách hàng như thế nào?",
                "en": "How have self-order kiosks and the mobile app enhanced McDonald's customer journey?"
            },
            "model_answer": {
                "vi": "Màn hình tự đặt món (kiosks) và app di động giúp khách hàng không còn phải chịu áp lực xếp hàng chờ đợi trước quầy thu ngân, cho phép tự do tùy biến nguyên liệu (thêm phô mai, bớt muối), thanh toán nhanh chóng và lựa chọn phục vụ tận bàn. Thuật toán gợi ý thông minh trên màn hình tự động đề xuất món kèm theo, giúp gia tăng giá trị đơn hàng trung bình từ 15-20% so với gọi món truyền thống.",
                "en": "Touchscreen self-order kiosks and mobile ordering liberate guests from cashier queue pressure, allowing stress-free ingredient customization, seamless cashless payment, and table delivery service. Predictive cross-selling algorithms systematically boost average ticket sizes by 15-20% compared to legacy verbal counter interactions."
            }
        },
        {
            "q_num": 2,
            "prompt": {
                "vi": "Làm thế nào McDonald's có thể sử dụng ứng dụng di động để tạo giá trị khác biệt so với các nền tảng giao đồ ăn như Uber Eats hay DoorDash?",
                "en": "How can McDonald's use its app to provide value to customers and differentiate itself from third-party delivery aggregators like Uber Eats?"
            },
            "model_answer": {
                "vi": "McDonald's giữ quyền kiểm soát dữ liệu khách hàng bằng cách cung cấp chương trình tích điểm độc quyền MyMcDonald's Rewards, các ưu đãi siêu cá nhân hóa dựa trên lịch sử mua sắm, tích hợp tùy chọn nhận hàng tại quầy Drive-Thru hoặc bãi đỗ xe curbside mà các ứng dụng giao hàng bên thứ ba không thể cung cấp.",
                "en": "McDonald's reclaims first-party customer relationships by locking high-value loyalty perks inside MyMcDonald's Rewards, serving hyper-personalized deal feeds based on past purchase history, and enabling geofenced curbside and drive-thru pickup workflows that third-party delivery apps cannot duplicate."
            }
        }
    ],
    {
        "role": "Chief Experience Officer (CXO) at McDonald's",
        "prompt": {
            "vi": "Hãy tưởng tượng bạn được bổ nhiệm làm Giám đốc Trải nghiệm (CXO) tại McDonald's. Công việc của bạn là nâng cấp thương hiệu để nhắm vào nhóm người tiêu dùng sành công nghệ và cao cấp hơn, đồng thời bảo tồn giá trị tiện lợi cốt lõi. Bạn sẽ tạo ra trải nghiệm phygital cao cấp cho McDonald's như thế nào?",
            "en": "Imagine you have been hired to be the Chief Experience Officer (CXO) at McDonald's. Your job is to upgrade the fast-food brand to target luxury, tech-savvy consumers while preserving convenience as part of its DNA. How would you create the McDonald's luxury phygital experience?"
        }
    },
    (
        "Thách thức chuyển mình từ chuỗi đồ ăn nhanh truyền thống sang mô hình ẩm thực số hóa 'Experience of the Future' (EOTF) trong bối cảnh người tiêu dùng đòi hỏi sự tươi ngon và sức khỏe.",
        "Reinventing legacy fast-food speed and standardization into a modern, health-conscious, personalized 'Experience of the Future' (EOTF).",
        "Hơn 38.000 nhà hàng tại 100+ quốc gia, hệ thống màn hình cảm ứng tự đặt hàng, thương vụ mua lại công ty AI Dynamic Yield, ứng dụng MyMcDonald's Rewards.",
        "Scale across 38,000+ restaurants, Dynamic Yield algorithmic menu boards, kiosk conversion rates, and MyMcDonald's Rewards loyalty adoption.",
        "Khách hàng gia đình, tài xế Drive-thru bận rộn, nhân viên chế biến bếp, và các chủ sở hữu nhượng quyền (Franchisees).",
        "Fast-food consumers, drive-thru commuters, kitchen assembly crew members, and independent franchise owner-operators.",
        "Áp lực thời gian giao đồ ăn trong vài chục giây khiến việc cá nhân hóa món ăn dễ gây nhầm lẫn và quá tải cho dây chuyền bếp truyền thống.",
        "Strict speed-of-service mandates clashing with order customization complexity, risking kitchen bottlenecks and order inaccuracy.",
        "Phương án 1: Giảm bớt thực đơn để tối đa hóa tốc độ phục vụ truyền thống; Phương án 2: Tự động hóa toàn diện quy trình đặt hàng và điều phối bếp bằng màn hình hiển thị số hóa KDS.",
        "Option 1: Menu simplification strictly prioritizing drive-thru speed; Option 2: Full-scale digital transformation with dynamic AI menus, kiosks, and kitchen display automation.",
        "Tốc độ phục vụ (Service time in seconds), Giá trị đơn hàng trung bình (Average ticket size), và Tỷ lệ chính xác của đơn hàng (Order accuracy %).",
        "Drive-thru cycle time (seconds), Average order value increase (%), Order accuracy rate, and Franchisee return on technology investment.",
        "Khuyến nghị Phương án 2: Triển khai toàn diện mô hình EOTF kết hợp bảng thực đơn thông minh thay đổi theo thời tiết và thời gian trong ngày (Dynamic Yield).",
        "Recommend Option 2: Scale Experience of the Future (EOTF) architecture, deploying AI-driven dynamic menu boards optimized for real-time weather and traffic.",
        "Lộ trình: Hỗ trợ tài chính cho các đối tác nhượng quyền nâng cấp cửa hàng, tích hợp chương trình khách hàng thân thiết toàn cầu trên app, và nâng cấp quầy McCafé.",
        "Phased roadmap: Subsidize franchisee kiosk/drive-thru retrofit capital, launch MyMcDonald's unified digital rewards, and elevate premium McCafé touchpoints.",
        "Sự phản kháng của các đối tác nhượng quyền về chi phí đầu tư công nghệ đắt đỏ và rủi ro gián đoạn khi hệ thống mạng gặp sự cố.",
        "Overcome franchisee resistance regarding heavy capital expenditure and mitigate tech system outage disruptions during peak rush hours.",
        "Doanh số bán hàng cùng cửa hàng (Same-store sales growth), Tỷ lệ đơn hàng qua kênh số (% Digital mix), và Tỷ lệ chính xác đơn hàng tại bàn.",
        "Digital sales penetration (% of total transactions), Drive-thru throughput speed, Ticket size uplift from AI recommendations, and Mobile retention."
    ),
    {
        "key_strengths_to_look_for": ["Experience of the Future (EOTF)", "Self-service touchscreen kiosks", "Dynamic Yield AI menu adaptation", "Table delivery service"],
        "critical_tradeoffs": ["High franchisee technology capex vs incremental basket size uplift", "Digital kiosk isolation vs friendly crew counter interaction"],
        "devil_advocate_questions": [
            "Nếu toàn bộ khách hàng đều đặt món qua màn hình cảm ứng hoặc ứng dụng điện thoại, vai trò và bản sắc của nhân viên McDonald's sẽ thay đổi như thế nào?",
            "Việc cá nhân hóa món ăn sâu có làm phá vỡ triết lý 'Speedee Service' cốt lõi làm nên tên tuổi của McDonald's suốt 70 năm qua không?"
        ]
    }
))

# 7. CHANEL
rich_cases.append(make_batat(
    "CASE-CHANEL-01", "Chanel",
    "Tình huống 7: Câu chuyện Cổ tích & Chiến lược Marketing Trải nghiệm Xa xỉ tại Chanel",
    "Case 7: Fairytale Heritage & Luxury Experiential Strategy at Chanel",
    "Haute Couture, Luxury Goods & Fragrances",
    "Chapter 5: Customer Experience: Luxury and Fashion, Case 13", "126-131",
    existing_by_id["CASE-CHANEL-01"]["background"]["vi"],
    existing_by_id["CASE-CHANEL-01"]["background"]["en"],
    existing_by_id["CASE-CHANEL-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-CHANEL-01"]["strategic_problem"]["en"],
    existing_by_id["CASE-CHANEL-01"]["crm_framework_steps"],
    [
        {
            "q_num": 1,
            "prompt": {
                "vi": "Chanel đã thay đổi chiến lược tiếp thị như thế nào để tập trung nhiều hơn vào trải nghiệm khách hàng? Những thay đổi này có phù hợp với nhu cầu mua sắm xa xỉ của người tiêu dùng hiện đại?",
                "en": "How has Chanel modified its marketing strategy to focus more on the customer experience? Are these changes in line with today's consumer needs in luxury consumption?"
            },
            "model_answer": {
                "vi": "Chanel kiên định duy trì sự độc quyền và khan hiếm bằng cách từ chối bán các sản phẩm thời trang cao cấp và túi xách trực tuyến qua sàn thương mại điện tử đại trà. Thay vào đó, hãng đầu tư vào các cửa hàng flagship tráng lệ với không gian tiếp khách riêng tư (salons privés), triển lãm nghệ thuật 'Mademoiselle Privé', và sử dụng nội dung số hóa độc quyền (Inside Chanel) để kể lại câu chuyện di sản của Coco Chanel.",
                "en": "Chanel fiercely protects luxury exclusivity by refusing to sell haute couture and iconic leather handbags on mass e-commerce websites. Instead, it invests in lavish architectural flagship boutiques featuring private salons, immersive 'Mademoiselle Privé' exhibitions, and digital storytelling portals ('Inside Chanel') that evoke the timeless mythology of Coco Chanel."
            }
        },
        {
            "q_num": 2,
            "prompt": {
                "vi": "Chanel định nghĩa trải nghiệm khách hàng như thế nào? Làm sao thương hiệu dung hòa giữa tính bí mật, đẳng cấp và việc tiếp cận thế hệ trẻ qua truyền thông số?",
                "en": "How does Chanel define the customer experience? How does the brand reconcile mystery, prestige, and reaching younger demographics through digital media?"
            },
            "model_answer": {
                "vi": "Đối với Chanel, trải nghiệm xa xỉ không chỉ là sản phẩm vật lý mà là một nghi thức cảm xúc (emotional ritual) dựa trên sự phục vụ tận tụy của chuyên gia tư vấn (Fashion Advisors). Để tiếp cận thế hệ trẻ mà không làm loãng thương hiệu, Chanel cho phép mua sắm trực tuyến đối với các ngành hàng mỹ phẩm, nước hoa (Beauty & Fragrance), đồng thời tổ chức các pop-up concept sáng tạo như Chanel Beauty House.",
                "en": "For Chanel, luxury customer experience is an emotional ritual mediated by intimate Fashion Advisor relationships. To engage affluent Gen-Z without diluting prestige, Chanel uses beauty and fragrances as accessible digital entry points while hosting playful experiential pop-up concepts like the Chanel Beauty House."
            }
        }
    ],
    {
        "role": "Chief Experience Officer (CXO) at Chanel",
        "prompt": {
            "vi": "Hãy tưởng tượng bạn được bổ nhiệm làm Giám đốc Trải nghiệm (CXO) tại Chanel để nâng cao sự hiện diện trực tuyến bằng cách xem xét lại nội dung và chiến lược mạng xã hội. Đâu là điểm khởi đầu của bạn để kết nối điểm chạm của người mua sắm trực tuyến và trực tiếp nhằm mang lại hành trình khách hàng toàn cầu liền mạch mà không làm mất đi tính độc quyền?",
            "en": "Imagine you have been hired to be the Chief Experience Officer (CXO) at Chanel to enhance its online presence by rethinking e-commerce, website, and social media content. What would be your starting point to identify online and offline touchpoints to deliver a fluid luxury journey while preserving exclusivity?"
        }
    },
    (
        "Bảo tồn tính khan hiếm, di sản quý tộc và mối quan hệ tư vấn trực tiếp (high-touch relationship) trong kỷ nguyên số hóa đại trà.",
        "Preserving brand scarcity, bespoke craftsmanship, and intimate high-touch boutique rituals amidst digital commoditization.",
        "Di sản số 31 Rue Cambon, loạt phim tài liệu 'Inside Chanel', chính sách phân phối mỹ phẩm trực tuyến có chọn lọc, sự kiện triển lãm 'Mademoiselle Privé'.",
        "Legacy of 31 Rue Cambon, 'Inside Chanel' cinematic video views, selective beauty e-commerce metrics, and 'Mademoiselle Privé' exhibition attendance.",
        "Khách hàng thượng lưu trung thành (VICs - Very Important Clients), thế hệ người tiêu dùng trẻ mới nổi (Gen Z), các chuyên viên tư vấn thời trang, và nhà thiết kế sáng tạo.",
        "Ultra-high-net-worth VICs (Very Important Clients), aspirational younger luxury consumers, bespoke Fashion Advisors, and creative directors.",
        "Mâu thuẫn căn bản của hàng xa xỉ: Sự tiện lợi của thương mại điện tử đại trà thường triệt tiêu cảm giác độc quyền, khan hiếm và vị thế xã hội của khách hàng thượng lưu.",
        "The fundamental luxury paradox: Mass digital convenience erodes perceived rarity, bespoke prestige, and social distinction.",
        "Phương án 1: Bán toàn bộ túi xách và trang phục qua sàn thương mại điện tử để tối đa hóa doanh thu; Phương án 2: Chiến lược 'Digital for Romance, Boutique for Ceremony' (Số hóa để truyền cảm hứng, Cửa hàng để trải nghiệm nghi thức).",
        "Option 1: Complete e-commerce expansion across all product categories; Option 2: 'Digital for Romance, Boutique for Ceremony' hybrid strategy.",
        "Độ bảo vệ định vị thương hiệu (Brand prestige index), Mức độ trung thành của nhóm khách hàng VIP (VIC retention), và Giá trị đơn hàng trung bình.",
        "Brand prestige protection index, High-net-worth VIC retention rate, Fashion Advisor relationship longevity, and Gross margin stability.",
        "Khuyến nghị Phương án 2: Giữ vững nguyên tắc không bán trang phục may sẵn và túi xách online; sử dụng công nghệ số để đặt lịch hẹn riêng tại phòng VIP (Private Appointments).",
        "Recommend Option 2: Uphold refusal of online ready-to-wear sales; deploy clienteling mobile apps empowering Fashion Advisors to prepare customized boutique viewings.",
        "Lộ trình: Phát triển ứng dụng khách hàng chuyên biệt cho chuyên viên tư vấn (Clienteling App), mở rộng salon riêng tư tại các kinh đô thời trang, và số hóa bảo hành sản phẩm.",
        "Roadmap: Roll out dedicated iPad clienteling tools for boutique staff, establish private VIP salons globally, and introduce blockchain authenticity passports.",
        "Rủi ro mất đi một bộ phận người tiêu dùng trẻ quen với việc mua sắm chỉ bằng một cú nhấp chuột trên điện thoại.",
        "Mitigate alienating younger digital-native consumers who demand instant one-click gratification.",
        "Tỷ lệ giữ chân khách hàng VIP (VIC retention rate), Thời gian gắn bó trung bình của chuyên viên tư vấn với khách hàng, và NPS tại các buổi tiếp đón riêng tư.",
        "VIC annual spend retention, Fashion Advisor-to-Client relationship tenure, Private salon NPS, and Brand desirability index."
    ),
    {
        "key_strengths_to_look_for": ["Luxury customer experience definition", "High-touch clienteling vs mass e-commerce", "Scarcity and exclusivity preservation", "Storytelling via 'Inside Chanel'"],
        "critical_tradeoffs": ["Immediate e-commerce revenue growth vs long-term brand equity preservation"],
        "devil_advocate_questions": [
            "Khi các đối thủ xa xỉ như Gucci và Louis Vuitton đều đầu tư hàng trăm triệu USD vào thương mại điện tử, liệu sự cứng rắn từ chối bán túi xách online của Chanel là sáng suốt hay bảo thủ?",
            "Làm thế nào Chanel có thể chứng minh các buổi triển lãm nghệ thuật tốn kém như 'Mademoiselle Privé' thực sự mang lại giá trị hoàn vốn CRM (ROI)?"
        ]
    }
))

# 8. NIKE
rich_cases.append(make_batat(
    "CASE-NIKE-01", "Nike",
    "Tình huống 8: Mua sắm Số hóa như một Phần Tất yếu trong Trải nghiệm Khách hàng tại Nike",
    "Case 8: Nike's Focus on Digitized Shopping as an Integral Part of Customer Experience",
    "Athletic Footwear, Apparel & Sports Tech",
    "Chapter 5: Customer Experience: Luxury and Fashion, Case 14", "131-143",
    existing_by_id["CASE-NIKE-01"]["background"]["vi"],
    existing_by_id["CASE-NIKE-01"]["background"]["en"],
    existing_by_id["CASE-NIKE-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-NIKE-01"]["strategic_problem"]["en"],
    existing_by_id["CASE-NIKE-01"]["crm_framework_steps"],
    [
        {
            "q_num": 1,
            "prompt": {
                "vi": "Nike đã tích hợp trải nghiệm khách hàng với chiến lược kỹ thuật số và marketing như thế nào? Những đổi mới này có đáp ứng nhu cầu của người tiêu dùng thời trang thể thao ngày nay?",
                "en": "How has Nike integrated customer experience with its digital and marketing strategy? Are these changes in line with today's sports fashion consumer needs?"
            },
            "model_answer": {
                "vi": "Nike xây dựng hệ sinh thái kết nối chặt chẽ giữa ứng dụng số (Nike App, SNKRS, Nike Run Club, Nike Training Club) và chuỗi cửa hàng tương lai 'House of Innovation'. Tại cửa hàng, người dùng sử dụng ứng dụng để quét mã giày tự động yêu cầu nhân viên mang đúng cỡ giày tới phòng thử (Scan to Try), thanh toán tức thì trên điện thoại (Instant Checkout), và tự thiết kế giày theo sở thích cá nhân tại khu vực Nike By You.",
                "en": "Nike orchestrates an interconnected ecosystem bridging mobile lifestyle apps (Nike App, SNKRS, NRC, NTC) with its flagship 'House of Innovation' stores. Shoppers use the Nike App to scan shoes on display mannequins to trigger automated fitting room trials (Scan to Try), skip cashier lines via Instant Checkout, and customize bespoke colorways at the Nike By You design lab."
            }
        },
        {
            "q_num": 2,
            "prompt": {
                "vi": "Chiến lược Bán hàng Trực tiếp tới Người tiêu dùng (Direct-to-Consumer - Nike Direct) đã thay đổi mối quan hệ giữa Nike và khách hàng như thế nào so with việc bán qua các nhà bán lẻ trung gian?",
                "en": "How has Nike's Direct-to-Consumer (Nike Direct) strategy reshaped its customer relationships compared to traditional wholesale distribution?"
            },
            "model_answer": {
                "vi": "Bằng cách cắt giảm các nhà bán lẻ trung gian không đáp ứng chuẩn mực trải nghiệm và tập trung vào kênh Nike Direct, Nike giành lại quyền sở hữu toàn bộ dữ liệu người dùng (first-party customer data). Dữ liệu chạy bộ, tập luyện và lịch sử mua sắm từ ứng dụng cho phép Nike dự báo chính xác nhu cầu sản xuất, loại bỏ hàng tồn kho ứ đọng và nâng cao biên lợi nhuận ròng.",
                "en": "By severing ties with undifferentiated wholesale retailers and scaling Nike Direct, Nike secured full ownership of first-party consumer data. Fitness telemetry from its running and training apps informs predictive demand planning, eliminates margin-killing markdowns, and dramatically increases direct customer lifetime value."
            }
        }
    ],
    {
        "role": "Chief Experience Officer (CXO) at Nike",
        "prompt": {
            "vi": "Hãy tưởng tượng bạn được bổ nhiệm làm Giám đốc Trải nghiệm (CXO) tại Nike. Công việc của bạn là tạo ra một cửa hàng ý tưởng trải nghiệm thể thao thời trang mới nhắm vào các gia đình. Bạn sẽ sử dụng mô hình 7Es như thế nào để thiết kế trải nghiệm mua sắm tối ưu cho cả trẻ em và cha mẹ?",
            "en": "Imagine you have been hired to be the Chief Experience Officer (CXO) at Nike. Your job is to create a new fashion sports experiential concept store targeting families. How would you use the 7Es tool to design the ultimate shopping experience for both kids and their parents?"
        }
    },
    (
        "Chuyển dịch cơ cấu phân phối từ bán buôn truyền thống sang hệ sinh thái Direct-to-Consumer (DTC) do dữ liệu và ứng dụng số dẫn dắt.",
        "Strategic channel pivot from wholesale distribution to member-driven Direct-to-Consumer (Nike Direct) ecosystem.",
        "Chuỗi cửa hàng House of Innovation (New York, Thượng Hải, Paris), hệ thống ứng dụng SNKRS và NRC, doanh thu thành viên Nike Member cao gấp 3 lần khách vãng lai.",
        "Metrics from House of Innovation flagships, SNKRS drop engagement, and data showing Nike Members spend 3x more than non-members.",
        "Vận động viên và người yêu thể thao, cộng đồng sưu tầm giày (Sneakerheads), nhân viên bán hàng cửa hàng (Athletes), và các đối tác bán lẻ bị cắt giảm.",
        "Everyday athletes, dedicated sneakerhead collectors, in-store sales athletes, and terminated wholesale partners.",
        "Sự phụ thuộc vào các chuỗi cửa hàng bán lẻ truyền thống làm loãng hình ảnh thương hiệu và khiến Nike mất quyền kiểm soát dữ liệu hành vi của người tiêu dùng.",
        "Reliance on undifferentiated wholesale accounts diluted brand storytelling and severed Nike's access to end-user behavioral data.",
        "Phương án 1: Tiếp tục phân phối đại trà qua mọi kênh bán buôn; Phương án 2: Thu hẹp mạng lưới bán buôn, dồn toàn lực đầu tư vào ứng dụng Nike App và trải nghiệm cửa hàng Flagship thông minh.",
        "Option 1: Maintain broad wholesale distribution; Option 2: Ruthlessly trim wholesale partners to channel resources into Nike Direct and digital membership platforms.",
        "Tỷ trọng doanh thu kênh bán hàng trực tiếp (% DTC revenue), Tỷ lệ tương tác của thành viên Nike Member, và Biên lợi nhuận gộp.",
        "Direct-to-Consumer revenue share (%), Active Nike Member monthly engagement, and Gross margin expansion.",
        "Khuyến nghị Phương án 2: Tăng tốc chiến lược Consumer Direct Acceleration, biến việc đăng ký thành viên Nike Member thành cánh cổng kết nối toàn bộ hệ sinh thái sản phẩm và dịch vụ.",
        "Recommend Option 2: Execute Consumer Direct Acceleration, treating the free Nike Membership as the master identity unifying digital fitness, drops, and flagship perks.",
        "Lộ trình: Cắt bỏ các nhà bán lẻ không đạt chuẩn, tích hợp thẻ thành viên kỹ thuật số tại toàn bộ cửa hàng, và mở rộng định dạng cửa hàng địa phương Nike Live.",
        "Phased roadmap: Terminate mediocre wholesale accounts, integrate RFID digital fitting rooms across fleet, and scale neighborhood-focused Nike Live stores.",
        "Nguy cơ phản ứng tiêu cực khi ứng dụng SNKRS bị nghẽn mạng do lượng truy cập đột biến và vấn nạn đầu cơ mua gom giày của các 'bot' tự động.",
        "Mitigate sneakerhead outrage during high-demand SNKRS drops caused by server crashes and automated scalping bots.",
        "Tỷ lệ thâm nhập doanh thu thành viên (% Member sales), Tỷ lệ giữ chân người dùng trên các app thể thao, và Tần suất mua sắm lặp lại.",
        "Member revenue contribution %, Monthly active users on NRC/NTC apps, In-store Scan-to-Try conversion rate, and Full-price sell-through %."
    ),
    {
        "key_strengths_to_look_for": ["Consumer Direct Acceleration (Nike Direct)", "House of Innovation Phygital features (Scan to Try, Instant Checkout)", "Community membership ecosystem", "Lifestyle app integration (NRC, NTC, SNKRS)"],
        "critical_tradeoffs": ["Severing wholesale retail partners vs taking on entire inventory and last-mile shipping risk"],
        "devil_advocate_questions": [
            "Khi Nike cắt hợp đồng bán buôn với hàng nghìn đại lý nhỏ lẻ, liệu thương hiệu có tự thu hẹp sự hiện diện vật lý tại các vùng nông thôn và thị trấn nhỏ không?",
            "Làm thế nào Nike cân bằng giữa việc phục vụ nhóm khách hàng thể thao đại chúng với việc làm hài lòng cộng đồng Sneakerheads khó tính?"
        ]
    }
))

# 9. ESTEE LAUDER
rich_cases.append(make_batat(
    "CASE-ESTEE-01", "The Estée Lauder Companies",
    "Tình huống 9: Marketing Trải nghiệm tại Trọng tâm Chuyển đổi Số của Estée Lauder",
    "Case 9: Experiential Marketing at the Core of Estée Lauder's Digital Transformation",
    "Prestige Beauty, Cosmetics & Skincare",
    "Chapter 5: Customer Experience: Luxury and Fashion, Case 15", "143-148",
    existing_by_id["CASE-ESTEE-01"]["background"]["vi"],
    existing_by_id["CASE-ESTEE-01"]["background"]["en"],
    existing_by_id["CASE-ESTEE-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-ESTEE-01"]["strategic_problem"]["en"],
    existing_by_id["CASE-ESTEE-01"]["crm_framework_steps"],
    [
        {
            "q_num": 1,
            "prompt": {
                "vi": "Estée Lauder đã cải tiến trải nghiệm làm đẹp như thế nào thông qua việc kết hợp chẩn đoán cá nhân hóa, công nghệ thử trang điểm ảo và không gian mở?",
                "en": "How has Estée Lauder advanced the beauty experience by combining personalized diagnosis, virtual try-on technology, and open-format counters?"
            },
            "model_answer": {
                "vi": "Estée Lauder phá bỏ quầy mỹ phẩm truyền thống khép kín để thay thế bằng các 'Makeup Bars' mở, nơi khách hàng tự do trải nghiệm sản phẩm. Thương hiệu tích hợp công nghệ AI và thực tế tăng cường (AR) như máy quét tông da kỹ thuật số (iMatch Digital Shade Finder), cho phép người dùng thử hàng trăm màu son và kem nền tức thì trên gương số hoặc ứng dụng điện thoại mà không cần bôi thử lên da thật.",
                "en": "Estée Lauder dismantled intimidating traditional glass counters in favor of open, self-guided Makeup Bars. It embedded AI and AR computer vision—such as the iMatch Digital Shade Finder—enabling shoppers to virtually try on hundreds of lipstick and foundation shades in real time without physical skin application."
            }
        },
        {
            "q_num": 2,
            "prompt": {
                "vi": "Chiến lược mở rộng các cửa hàng chuyên biệt độc lập (freestanding specialty stores) đã giúp Estée Lauder kiểm soát trải nghiệm thương hiệu tốt hơn so với việc chỉ bán tại trung tâm thương mại (department stores) như thế nào?",
                "en": "How has expanding freestanding specialty stores allowed Estée Lauder to control its brand experience better than relying solely on traditional department stores?"
            },
            "model_answer": {
                "vi": "Trước sự suy thoái của các trung tâm thương mại truyền thống, việc mở các cửa hàng độc lập giúp Estée Lauder tự do thiết kế toàn bộ hành trình đa giác quan: âm nhạc, ánh sáng, quầy tư vấn chăm sóc da chuyên sâu và tổ chức các sự kiện độc quyền, từ đó thu thập dữ liệu khách hàng trực tiếp và xây dựng lòng trung thành sâu sắc hơn.",
                "en": "Counteracting declining foot traffic in legacy department stores, freestanding specialty boutiques grant Estée Lauder complete autonomy over sensory environmental design—lighting, acoustic branding, bespoke skincare consultations, and direct CRM data capture."
            }
        }
    ],
    {
        "role": "Chief Experience Officer (CXO) at Estée Lauder",
        "prompt": {
            "vi": "Hãy tưởng tượng bạn được bổ nhiệm làm Giám đốc Trải nghiệm (CXO) tại Estée Lauder. Công việc của bạn là thiết kế một trải nghiệm mới: 'Estée Lauder Coffee Shop Experience'. Bạn sẽ thiết kế nó như thế nào để nắm bắt đúng DNA của thương hiệu và bạn sẽ sử dụng nghiên cứu marketing nào để hiểu nhu cầu làm đẹp của khách hàng?",
            "en": "Imagine you have been hired to be the Chief Experience Officer (CXO) at Estée Lauder. Your job is to design a new experiential offer, the 'Estée Lauder Coffee Shop Experience.' How would you design it to capture the brand's DNA, and what marketing research would you use to learn about consumer needs?"
        }
    },
    (
        "Chuyển dịch từ quầy bán hàng truyền thống tại trung tâm thương mại sang trải nghiệm làm đẹp số hóa cá nhân hóa cao độ bằng AI.",
        "Transitioning from legacy department store counters to high-engagement, AI-powered personalized beauty consultations.",
        "Công nghệ iMatch Shade Finder quét tông màu da chính xác 99%, các quầy trải nghiệm tương tác Makeup Bars, danh mục thương hiệu cao cấp (MAC, Clinique, Jo Malone).",
        "iMatch Shade Finder accuracy metrics, interactive Makeup Bar dwell times, and multi-brand portfolio direct-to-consumer digital sales figures.",
        "Người tiêu dùng làm đẹp đa thế hệ (từ trung niên đến Gen Z), các chuyên gia tư vấn sắc đẹp (Beauty Advisors), và các đối tác bán lẻ mỹ phẩm (Sephora, Ulta).",
        "Multi-generational beauty shoppers, frontline Beauty Advisors, dermatology specialists, and specialty retail partners (Sephora, Ulta).",
        "Người tiêu dùng hiện đại cảm thấy e ngại và bất tiện khi phải tẩy trang nhiều lần để thử màu mỹ phẩm tại các quầy bán hàng truyền thống.",
        "Frictional discomfort of physical cosmetic product testing requiring repeated facial cleansing and skin irritation at public counters.",
        "Phương án 1: Giữ nguyên cách thử mỹ phẩm trực tiếp truyền thống; Phương án 2: Đầu tư mạnh vào công nghệ thực tế tăng cường AR thử trang điểm ảo và chẩn đoán da bằng AI trên đa kênh.",
        "Option 1: Rely on traditional physical testers and counter staff consultations; Option 2: Omnichannel deployment of AR virtual makeup try-on and AI diagnostic tools.",
        "Tỷ lệ chuyển đổi sau khi thử sản phẩm ảo, Mức độ chính xác của đề xuất màu son/kem nền, và Giá trị giỏ hàng trung bình.",
        "Virtual try-on conversion rate, Foundation shade match accuracy, Average basket value, and Cross-brand category discovery.",
        "Khuyến nghị Phương án 2: Tích hợp công nghệ AI chẩn đoán da và thử đồ ảo trên toàn bộ website, mạng xã hội và gương thông minh tại cửa hàng.",
        "Recommend Option 2: Embed computer vision shade finders across all mobile touchpoints, social commerce integrations, and in-store interactive smart mirrors.",
        "Lộ trình: Trang bị máy tính bảng chẩn đoán da cho toàn bộ chuyên viên tư vấn, ra mắt tính năng thử màu son ảo trên Instagram/TikTok, và mở rộng cửa hàng độc lập.",
        "Phased roadmap: Equip frontline Beauty Advisors with diagnostic tablets, launch AR try-ons on social platforms, and scale freestanding experiential boutiques.",
        "Rủi ro màu sắc hiển thị trên màn hình điện thoại của người dùng bị sai lệch do ánh sáng môi trường, dẫn đến tỷ lệ đổi trả hàng cao.",
        "Mitigate device screen calibration variance causing perceived shade mismatch upon product arrival, leading to returns.",
        "Tỷ lệ hoàn hàng do sai tông màu (Shade return rate reduction), Thời gian tương tác với công cụ AI, và Doanh số bán hàng lặp lại trực tuyến.",
        "Foundation shade return rate reduction, Virtual try-on engagement duration, Repeat omnichannel purchase velocity, and Beauty Rewards tier advancement."
    ),
    {
        "key_strengths_to_look_for": ["iMatch AI shade matching", "Interactive open Makeup Bars", "Freestanding boutique sensory design", "Virtual try-on friction reduction"],
        "critical_tradeoffs": ["Digital AR convenience vs the high-touch tactile emotional bonding of an expert human beauty consultation"],
        "devil_advocate_questions": [
            "Công nghệ thử son môi ảo trên điện thoại có thể thay thế được cảm giác chạm vào chất son thật và mùi hương đặc trưng của mỹ phẩm cao cấp không?",
            "Làm thế nào để Estée Lauder bảo vệ tính bí mật của dữ liệu khuôn mặt và tình trạng da của khách hàng khi áp dụng các công cụ chẩn đoán AI?"
        ]
    }
))

# 10. BIG FOUR GAFA
rich_cases.append(make_batat(
    "CASE-GAFA-SYNTHESIS", "The Big Four (GAFA: Google, Apple, Facebook, Amazon)",
    "Tình huống 10: Nhóm 'Big Four' Công nghệ & Chiến lược Định hình Trải nghiệm Khách hàng Toàn cầu",
    "Case 10: The 'Big Four' Digital Firms: GAFA and the Customer Experience Transformation",
    "Big Tech, Digital Ecosystems & Platforms",
    "Chapter 1: The 'Big Four' Digital Firms: GAFA and Customer Experience", "2-30",
    existing_by_id["CASE-GAFA-SYNTHESIS"]["background"]["vi"],
    existing_by_id["CASE-GAFA-SYNTHESIS"]["background"]["en"],
    existing_by_id["CASE-GAFA-SYNTHESIS"]["strategic_problem"]["vi"],
    existing_by_id["CASE-GAFA-SYNTHESIS"]["strategic_problem"]["en"],
    existing_by_id["CASE-GAFA-SYNTHESIS"]["crm_framework_steps"],
    [
        {
            "q_num": 1,
            "prompt": {
                "vi": "Phân tích và so sánh các điểm chạm trải nghiệm khách hàng (touchpoints) của 4 công ty công nghệ lớn: Google, Apple, Facebook và Amazon. Ưu và nhược điểm của từng điểm chạm là gì?",
                "en": "Analyze and compare the customer experience touchpoints across the Big Four digital companies: Google, Apple, Facebook, and Amazon. What are the advantages and disadvantages of each?"
            },
            "model_answer": {
                "vi": "Google kiểm soát điểm chạm tìm kiếm thông tin với sự tiện lợi tối đa nhưng thiếu trải nghiệm vật lý sâu sắc; Apple sở hữu hệ sinh thái khép kín hoàn hảo giữa phần cứng, phần mềm và chuỗi cửa hàng Apple Store nhưng chi phí chuyển đổi cao; Facebook (Meta) tạo kết nối xã hội mạnh mẽ nhưng chịu nhiều tai tiếng về bảo mật dữ liệu; Amazon thống trị điểm chạm mua sắm và giao vận không ma sát (1-Click, Prime) nhưng thiếu tính cảm xúc và nghệ thuật kể chuyện thương hiệu.",
                "en": "Google dominates information discovery touchpoints with effortless utility but limited sensory depth; Apple controls an integrated hardware-software-retail ecosystem delivering premium sensory enchantment but with rigid lock-in; Facebook drives peer social connection but battles severe privacy trust deficits; Amazon optimizes zero-friction logistical commerce (1-Click, Prime delivery) but lacks brand emotional romance."
            }
        },
        {
            "q_num": 2,
            "prompt": {
                "vi": "Bốn công ty GAFA đang tận dụng dữ liệu người dùng như thế nào để thấu hiểu nhu cầu và mục tiêu của khách hàng? Công ty nào sở hữu sự thấu hiểu sâu sắc nhất?",
                "en": "How are the four GAFA companies leveraging customer data to understand consumer needs and goals? Which firm has developed the deepest customer understanding?"
            },
            "model_answer": {
                "vi": "Google hiểu khách hàng muốn biết gì (Intent Data); Facebook hiểu khách hàng quan tâm đến ai và điều gì (Affinity/Social Graph); Amazon hiểu khách hàng sẵn sàng bỏ tiền mua gì (Transactional Data); Apple hiểu cách khách hàng sống và sử dụng thiết bị hàng ngày (Behavioral Hardware Ecosystem). Amazon và Apple sở hữu sự thấu hiểu bền vững nhất vì dữ liệu gắn liền trực tiếp với hành vi thanh toán và lòng trung thành hữu hình.",
                "en": "Google captures consumer intent (Search queries); Facebook captures social identity and emotional affinity (Social graph); Amazon captures actual commercial purchasing behavior (Transaction history); Apple captures holistic lifestyle usage (Device ecosystem). Amazon and Apple build the most durable advantage because their data directly correlates with demonstrated willingness to pay and everyday physical reliance."
            }
        }
    ],
    {
        "role": "Chief Experience Officer (CXO) across Tech Platforms",
        "prompt": {
            "vi": "Nếu bạn được mời tư vấn cho một doanh nghiệp truyền thống muốn áp dụng mô hình kinh nghiệm của nhóm 'Big Four' để số hóa hành trình khách hàng, bạn sẽ khuyến nghị những nguyên tắc cốt lõi nào và cảnh báo những cạm bẫy đạo đức dữ liệu nào?",
            "en": "If you were advising a traditional enterprise looking to adopt the Big Four experiential playbook to digitize its customer journeys, what foundational principles would you recommend, and what data ethics pitfalls would you warn against?"
        }
    },
    (
        "Thách thức cân bằng giữa việc tạo ra trải nghiệm người dùng liền mạch, không ma sát và bảo vệ quyền riêng tư, sự kiểm soát dữ liệu cá nhân của người tiêu dùng.",
        "Balancing hyper-personalized frictionless convenience with growing consumer demands for algorithmic transparency and personal data sovereignty.",
        "Quy mô hàng tỷ người dùng hàng ngày trên toàn cầu, mô hình Prime của Amazon, mạng lưới Apple Store, doanh thu quảng cáo nhắm mục tiêu của Google và Facebook.",
        "Billions of daily active global users across GAFA services, Amazon Prime retention rates, Apple Store revenue per square foot, and targeted ad margins.",
        "Người tiêu dùng kỹ thuật số toàn cầu, các nhà phát triển ứng dụng bên thứ ba, các nhà bán hàng độc lập, và cơ quan quản lý chống độc quyền.",
        "Global digital citizens, third-party developers, marketplace merchants, privacy watchdogs, and anti-trust regulatory authorities.",
        "Hiệu ứng mạng lưới khép kín (Walled Gardens) tạo ra sự tiện lợi to lớn nhưng đồng thời triệt tiêu quyền lựa chọn và khóa chặt khách hàng vào hệ sinh thái độc quyền.",
        "Walled garden network lock-in maximizing operating convenience while creating structural switching barriers and reducing competitive consumer alternatives.",
        "Phương án 1: Tiếp tục tối đa hóa việc khai thác dữ liệu hành vi để tối ưu hóa quảng cáo nhắm chọn; Phương án 2: Chuyển dịch sang mô hình trải nghiệm lấy quyền riêng tư làm trọng tâm (Privacy-First Customer Experience).",
        "Option 1: Maximize monetization of behavioral surplus via predictive targeting; Option 2: Transition toward a Privacy-First Customer Experience architecture.",
        "Mức độ tin cậy của người dùng (Trust index), Chi phí tuân thủ quy định pháp lý (GDPR/CCPA), và Mức độ gắn kết dài hạn của khách hàng.",
        "Consumer institutional trust index, Regulatory compliance overhead (GDPR/CCPA/DMA), Platform stickiness, and Customer Lifetime Value (CLV).",
        "Khuyến nghị Phương án 2: Xây dựng trải nghiệm minh bạch, cho phép người dùng toàn quyền kiểm soát dữ liệu và nhận lại giá trị hữu hình từ việc chia sẻ thông tin.",
        "Recommend Option 2: Architect transparent data reciprocity where consumers explicitly consent and receive direct tangible utility for data sharing.",
        "Lộ trình: Thiết lập bảng điều khiển quản lý quyền riêng tư trực quan, giảm thiểu dữ liệu thu thập không cần thiết, và xây dựng cộng đồng hỗ trợ mở.",
        "Phased roadmap: Deploy intuitive privacy control dashboards, minimize passive surveillance telemetry, and open up cross-platform portability APIs.",
        "Rủi ro suy giảm hiệu quả của các thuật toán gợi ý khi người dùng hạn chế chia sẻ dữ liệu theo dõi hành vi.",
        "Mitigate algorithm precision degradation when users opt out of cross-app tracking mechanisms.",
        "Chỉ số niềm tin thương hiệu (Brand Trust Score), Tỷ lệ rời bỏ hệ sinh thái, Điểm CSAT về tính bảo mật, và Tỷ lệ tương tác chủ động.",
        "Platform Brand Trust Score, Annual churn rate from subscription ecosystems, Privacy satisfaction rating, and Active ecosystem engagement."
    ),
    {
        "key_strengths_to_look_for": ["GAFA comparative touchpoint analysis", "Data intent vs social graph vs transactional history", "Ecosystem lock-in & switching barriers", "Privacy-convenience trade-off"],
        "critical_tradeoffs": ["Hyper-personalized frictionless service vs invasive surveillance capitalism (Shoshana Zuboff)"],
        "devil_advocate_questions": [
            "Khi Amazon hay Apple tối ưu hóa trải nghiệm khách hàng đến mức 'không còn ma sát' (frictionless), liệu người tiêu dùng có đang dần mất đi khả năng tư duy và lựa chọn phản biện độc lập?",
            "Liệu một doanh nghiệp nhỏ có thể thực sự cạnh tranh về trải nghiệm khách hàng với nhóm Big Four mà không bị buộc phải phụ thuộc vào chính nền tảng của họ?"
        ]
    }
))

print(f"Successfully compiled {len(rich_cases)} rich cases.")

# Write to cases.json
output_file = data_dir / "cases.json"
output_file.write_text(json.dumps(rich_cases, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Successfully written {output_file} ({output_file.stat().st_size} bytes).")
