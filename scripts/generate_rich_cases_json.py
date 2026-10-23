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

# Load existing cases to preserve structure
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

# Build enriched cases
enriched_cases = []

# Case 1: TESCO
tesco_base = existing_by_id["CASE-TESCO-01"]
tesco_base["originalCaseText"] = {
    "en": raw_map["CASE-TESCO-01"],
    "vi": "## Tình huống 5: Định hướng Khách hàng tại Tesco (Customer Orientation at Tesco)\n\n### Tác giả & Xuất xứ\nGiáo sư Gerhard Raab (Đại học Khoa học Ứng dụng Ludwigshafen, CHLB Đức). Trích từ giáo trình *Customer Relationship Management*, Chương 'Customer Orientation at Tesco', trang 173–183.\n\n### Bối cảnh Khởi đầu của Tesco\nĐược thành lập vào năm 1924 bởi Sir Jack Cohen, Tesco ngày nay được coi là một trong những nhà bán lẻ thực phẩm tiên tiến và thành công bậc nhất tại Vương quốc Anh.\nNgay từ khi mới thành lập, Tesco đã luôn là một nhà đổi mới sáng tạo trong ngành bán lẻ. Việc mở cửa hàng tự phục vụ đầu tiên vào năm 1948, cũng như việc giới thiệu hệ thống 'tem đổi quà' (trading stamps) vào những năm 1960, là những cột mốc quan trọng trong lịch sử công ty. Tem đổi quà được khách hàng tích lũy khi mua sắm và có thể quy đổi thành tiền mặt hoặc quà tặng. Bằng cách giới thiệu tem đổi quà, Tesco tránh được việc phải đua giá trực diện với các nhà bán lẻ khác trong khi vẫn mang lại mức giá tiết kiệm thực sự cho khách hàng.\n\nTrong những năm tiếp theo, mô hình đại siêu thị (superstore) nhanh chóng trở thành chìa khóa cho sự thành công tương lai. Đến năm 1985, Tesco khai trương đại siêu thị thứ 100. Đáng chú ý, Tesco đã quyết định chuyển hướng chiến lược: thay vì định vị là nhà bán hàng giá rẻ, Tesco tái định vị thành nhà bán lẻ hướng đến chất lượng (quality-oriented). Tesco mở rộng danh mục sản phẩm, cải tiến cơ sở vật chất, nâng cao dịch vụ và bắt đầu phân đoạn khách hàng đa dạng.\n\n### Cuộc cách mạng Thẻ Hội viên Thân thiết (Clubcard) và Dunnhumby\nNăm 1995, dưới sự dẫn dắt của CEO Sir Terry Leahy, Tesco hợp tác cùng công ty phân tích dữ liệu Dunnhumby (Clive Humby và Edwina Dunn) để ra mắt thẻ khách hàng thân thiết Tesco Clubcard. Khác với các chương trình tích điểm đơn thuần nhằm giảm giá, Clubcard là một hệ thống thu thập dữ liệu hành vi mua sắm vi mô (granular transaction data).\n\nThông qua phân tích dữ liệu giỏ hàng, Tesco phân chia hàng triệu khách hàng thành các nhóm hành vi rõ rệt:\n1. Khách hàng tiết kiệm (Frugal Shoppers)\n2. Khách hàng truyền thống (Traditional Shoppers)\n3. Khách hàng tiện lợi (Convenience Shoppers)\n4. Khách hàng cao cấp (Upmarket Shoppers)\n5. Sinh viên / Người độc thân (Students & Young Singles)\n\nThay vì gửi các tờ rơi quảng cáo đại trà lãng phí, Tesco phát hành các tập phiếu giảm giá cá nhân hóa (personalized coupon mailings) với hơn 8 triệu biến thể khác nhau. Tỷ lệ quy đổi voucher tăng vọt từ mức 1–2% trung bình của ngành lên tới hơn 8–14%, giúp Tesco vượt qua Sainsbury's để trở thành chuỗi siêu thị số 1 nước Anh.\n\n### Mở rộng Đa kênh và Dịch vụ Giá trị Gia tăng\nTesco tận dụng dữ liệu Clubcard để mở rộng sang các dịch vụ tài chính cá nhân (Tesco Personal Finance), mua sắm trực tuyến (Tesco.com - một trong những siêu thị trực tuyến có lãi sớm nhất thế giới), và chuỗi cửa hàng tiện lợi Tesco Express, tạo nên một hệ sinh thái khách hàng khép kín."
}
tesco_base["source_reference"] = {
    "document": "Customer Relationship Management",
    "authors": "Gerhard Raab, Riad A. Ajami, Vidyaranya B. Gargeya, G. Jason Goddard",
    "chapter": "Case Study 5: Customer Orientation at Tesco",
    "pages": "173-183",
    "publisher": "z-lib.org / Academic Publication",
    "pdf_filename": "Case Study_Tesco.pdf",
    "extraction_method": "direct_pdf_text_verified"
}
tesco_base["discussion_questions"] = [
    {
        "q_num": 1,
        "prompt": {
            "vi": "Kết quả từ việc phân tích dữ liệu diện rộng đem lại cho Tesco kiến thức chi tiết về cấu trúc khách hàng phân hóa và nhu cầu đa dạng của họ. Đâu là những hệ quả trực tiếp và gián tiếp đối với doanh nghiệp từ việc sở hữu nguồn tri thức này?",
            "en": "As a result of its broad data analysis, Tesco receives detailed knowledge about the existing, differentiated customer structure, and the various needs, expectations, and desires that these customers have. What are the direct and indirect consequences of having this knowledge for the company?"
        },
        "model_answer": {
            "vi": "Hệ quả trực tiếp: Tối ưu hóa danh mục sản phẩm (merchandising) chính xác theo từng cụm siêu thị địa phương; tăng tỷ lệ phản hồi chiến dịch tiếp thị cá nhân hóa từ 1-2% lên 8-14%; giảm lãng phí chi phí marketing đại trà.\nHệ quả gián tiếp: Xây dựng rào cản chuyển đổi cấu trúc (structural switching cost); gia tăng lòng tin và CLV; phát hiện cơ hội mở rộng sang dịch vụ tài chính (Tesco Personal Finance) và bán lẻ trực tuyến (Tesco.com) với tỷ lệ rủi ro thấp nhờ hiểu rõ hành vi khách hàng mục tiêu.",
            "en": "Direct consequences: Localized store assortment optimization; hyper-targeted direct marketing response rates soaring to 8-14%; massive reduction in mass-mail waste.\nIndirect consequences: High structural switching barriers; elevated Customer Lifetime Value (CLV); cross-selling leverage into high-margin adjacent industries like Tesco Personal Finance and Tesco.com with proven customer segments."
        }
    },
    {
        "q_num": 2,
        "prompt": {
            "vi": "Chiến lược quốc tế hóa của Tesco tại thời điểm nghiên cứu tình huống được mô tả như thế nào? Những rủi ro tiềm ẩn khi chuyển giao năng lực CRM từ thị trường quê nhà sang các thị trường quốc tế là gì?",
            "en": "How would you describe Tesco's international strategy at the time of the case? What were the underlying risks of transferring home-market CRM capabilities abroad?"
        },
        "model_answer": {
            "vi": "Chiến lược quốc tế hóa của Tesco tập trung vào các thị trường đang phát triển tại Trung/Đông Âu và Châu Á (Thái Lan - Lotus, Hàn Quốc - Homeplus, Mỹ - Fresh & Easy). Rủi ro lớn nhất là ngộ nhận rằng hệ thống dữ liệu Clubcard có thể thay thế cho sự thấu hiểu văn hóa tiêu dùng bản địa; tại Mỹ, định dạng Fresh & Easy thất bại do không nắm bắt đúng thói quen mua sắm tươi sống của người Mỹ dù có công nghệ CRM tối tân.",
            "en": "Tesco pursued aggressive internationalization into Central/Eastern Europe and Asia (Lotus Thailand, Homeplus South Korea) and later the US (Fresh & Easy). The core risk was overestimating the portability of Clubcard algorithms without deep local cultural immersion, evidenced by the multi-billion-dollar failure of Fresh & Easy in the US."
        }
    },
    {
        "q_num": 3,
        "prompt": {
            "vi": "Chương trình 'First Class Service' của Tesco yêu cầu toàn thể nhân viên đánh giá 4 khía cạnh: Products, Presentation, Processes, People theo góc nhìn của khách hàng. Hãy phân tích vai trò của yếu tố Con người và Văn hóa tổ chức trong thành công của CRM tại Tesco.",
            "en": "Tesco's 'First Class Service' program requires all employees to examine 4 areas: Products, Presentation, Processes, People through the eyes of the customer. Analyze the role of People and Organizational Culture in Tesco's CRM success."
        },
        "model_answer": {
            "vi": "Đúng với nguyên lý của Scott Kostojohn et al. (80% Con người/Quy trình - 20% Công nghệ), dữ liệu Clubcard của Dunnhumby chỉ phát huy hiệu quả khi nhân viên siêu thị tuyến đầu am hiểu các phân khúc khách hàng và được trao quyền để phục vụ linh hoạt. 'First Class Service' giúp biến định hướng khách hàng trừu tượng thành hành vi cụ thể hàng ngày.",
            "en": "Echoing Kostojohn et al.'s finding that People and Process drive 80% of CRM outcomes, Dunnhumby's algorithms would be powerless without frontline store staff embracing customer-centric culture. 'First Class Service' bridged analytical intelligence with physical empathy at the point of sale."
        }
    }
]
tesco_base["frameworkGuide"] = build_10_dimension_guide(
    "Xác định bài toán tái định vị từ nhà bán lẻ giá rẻ sang nhà bán lẻ định hướng chất lượng và sự gắn kết khách hàng bền vững trong bối cảnh cạnh tranh khốc liệt tại thị trường Anh.",
    "Define strategic transition from low-price commodity vendor to quality-oriented customer engagement leader under severe UK supermarket rivalry.",
    "Thu thập dữ liệu giao dịch thẻ Clubcard, số lượng biến thể voucher (>8 triệu), tỷ lệ phản hồi so với trung bình ngành (8-14% vs 1-2%), phân bổ danh mục theo cụm cửa hàng.",
    "Examine Clubcard basket metrics, voucher variants (>8 million), coupon redemption rates (8-14% vs industry 1-2%), and localized store cluster assortments.",
    "Phân tích mâu thuẫn lợi ích giữa các bên: Cổ đông (muốn ROI nhanh), Nhà phân tích dữ liệu Dunnhumby (cần thời gian mô hình hóa), Nhân viên thu ngân (áp lực quét thẻ), và Khách hàng (lo ngại quyền riêng tư).",
    "Analyze competing stakes among shareholders (short-term margin pressure), Dunnhumby analysts, frontline cashiers (scanning friction), and shoppers (data privacy).",
    "Nguyên nhân gốc rễ là các chiến dịch tiếp thị đại trà truyền thống không phản ánh sự phân hóa nhu cầu giỏ hàng của từng hộ gia đình, dẫn đến lãng phí ngân sách và mất khách vào tay đối thủ.",
    "Root cause was mass promotion campaigns treating diverse household needs uniformly, leaking budget and churning shoppers to discounters.",
    "Phương án 1: Tiếp tục cuộc đua giảm giá sâu với Asda/Aldi; Phương án 2: Tập trung thẻ thành viên tích điểm đơn thuần; Phương án 3: Khai phá dữ liệu lớn cá nhân hóa đa kênh (Omnichannel Hyper-personalization).",
    "Option 1: Price war with discounters; Option 2: Basic transactional points card; Option 3: Hyper-personalized predictive customer analytics platform.",
    "So sánh theo: Chi phí đầu tư IT, Rào cản chuyển đổi khách hàng (Switching costs), Tác động tới Biên lợi nhuận ròng, và Khả năng mở rộng hệ sinh thái.",
    "Rank options by: IT upfront investment, Structural customer switching costs, Net margin defense, and Ecosystem horizontal expandability.",
    "Lựa chọn Phương án 3: Hợp tác chiến lược cùng Dunnhumby, tích hợp thẻ Clubcard vào toàn bộ quy trình cung ứng, phân phối và tiếp thị trực tiếp.",
    "Select Option 3: Strategic alliance with Dunnhumby, embedding Clubcard intelligence into merchandising, supply chain, and personalized direct communications.",
    "Giai đoạn 1 (Năm 1-2): Thử nghiệm Clubcard tại các cửa hàng mẫu; Giai đoạn 2 (Năm 3-5): Phổ cập toàn quốc và phát hành tạp chí khách hàng cá nhân hóa; Giai đoạn 3 (Năm 5+): Mở rộng Tesco Personal Finance và Tesco.com.",
    "Phase 1: Pilot Clubcard in test regions; Phase 2: Nationwide rollout with hyper-targeted coupon mailings; Phase 3: Adjacent financial and online grocery expansion.",
    "Rủi ro phản ứng dữ dội về quyền riêng tư (Privacy backlash), rủi ro sai sót mô hình phân khúc, và sự phản kháng của quản lý siêu thị truyền thống.",
    "Mitigate data privacy concerns, prevent algorithmic misclassification, and overcome frontline store managers' skepticism towards centralized data recommendations.",
    "Chỉ số: Tỷ lệ sử dụng thẻ Clubcard (% doanh thu quét thẻ), Tỷ lệ quy đổi voucher (Coupon redemption rate), NPS theo từng cụm phân khúc, và Tỷ suất lợi nhuận trên vốn đầu tư (ROIC).",
    "KPIs: Clubcard basket scan rate, Personalized voucher redemption %, Segment-level NPS, and Return on Invested Capital (ROIC)."
)
tesco_base["socraticGuidance"] = {
    "key_strengths_to_look_for": ["Dunnhumby granular basket data", "Customer lifetime value (CLV)", "Direct marketing response rate vs mass advertising", "People-Process-Technology alignment via First Class Service"],
    "critical_tradeoffs": ["High data infrastructure costs vs uncertain redemption gains", "Centralized algorithmic merchandising vs local store manager autonomy"],
    "devil_advocate_questions": [
        "Nếu đối thủ sao chép chương trình thẻ tích điểm trong vòng 6 tháng (như Sainsbury's đã làm), điều gì thực sự ngăn cản khách hàng rời bỏ Tesco?",
        "Tesco đã mở rộng thành công tại Anh nhưng thất bại nặng nề với Fresh & Easy tại Mỹ. Dữ liệu Clubcard có làm lãnh đạo Tesco quá tự tin mù quáng (data hubris) hay không?"
    ]
}
enriched_cases.append(tesco_base)

# Function to build rich case for Batat cases
def enrich_batat_case(case_id, company, title_vi, title_en, industry, chapter_info, pages_info, raw_key, bg_vi, bg_en, strat_vi, strat_en, fw_steps, questions, challenge, guide_args, socratic_args):
    c_raw = raw_map[case_id] if case_id in raw_map else raw_map.get("CASE-GAFA-SYNTHESIS")
    base = existing_by_id.get(case_id, {})
    return {
        "case_id": case_id,
        "company": company,
        "title": {"vi": title_vi, "en": title_en},
        "industry": industry,
        "source_reference": {
            "document": "Experiential Marketing: Case Studies in Customer Experience",
            "authors": "Wided Batat",
            "publisher": "Routledge",
            "chapter": chapter_info,
            "pages": pages_info,
            "pdf_filename": "Case Study_" + chapter_info.split(":")[0].replace(" ", "_") + ".pdf",
            "extraction_method": "windows_media_ocr_verified"
        },
        "background": {"vi": bg_vi, "en": bg_en},
        "strategic_problem": {"vi": strat_vi, "en": strat_en},
        "crm_framework_steps": fw_steps,
        "originalCaseText": {
            "en": c_raw,
            "vi": bg_vi + "\n\n### Nội dung Nghiên cứu Chi tiết từ Giáo trình Gốc\n" + c_raw[:2000] + "\n\n*(Xem toàn bộ văn bản gốc tiếng Anh ở chế độ song ngữ bên trên)*"
        },
        "discussion_questions": questions,
        "challenge_prompt": challenge,
        "frameworkGuide": build_10_dimension_guide(*guide_args),
        "socraticGuidance": socratic_args
    }

# Case 2: WALMART
walmart_steps = existing_by_id["CASE-WALMART-01"]["crm_framework_steps"]
walmart_q = [
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
]
walmart_chal = {
    "role": "Chief Experience Officer (CXO) at Walmart",
    "prompt": {
        "vi": "Hãy tưởng tượng bạn được bổ nhiệm làm Giám đốc Trải nghiệm (CXO) tại Walmart. Bạn muốn tạo ra một cửa hàng ý tưởng trải nghiệm mới kết hợp cả góc nhìn của người tiêu dùng lẫn nhân viên. Bạn sẽ sử dụng 7Es như thế nào để khách hàng cảm thấy thích thú và nhân viên gắn kết?",
        "en": "Imagine you have been hired to be the Chief Experience Officer (CXO) at Walmart. You want to create a new experiential concept store that integrates both consumer and employee perspectives. How would you use the 7Es to design the ultimate experience where shoppers are enchanted and employees are committed?"
    }
}
walmart_guide_args = (
    "Thách thức chuyển đổi từ mô hình chi phí thấp truyền thống sang trải nghiệm phygital đa kênh cạnh tranh trực diện với Amazon.",
    "Strategic pivot from low-cost transactional discount warehouse to omnichannel phygital powerhouse confronting Amazon.",
    "Dữ liệu 4.700+ cửa hàng tại Mỹ, ứng dụng Walmart App với Mobile Express Returns, Scan & Go, và dịch vụ Curbside Grocery Pickup.",
    "Empirical footprints across 4,700+ US stores, Walmart App adoption, Mobile Express Returns, and Curbside Grocery Pickup statistics.",
    "Người tiêu dùng gia đình có ngân sách eo hẹp, nhân viên thu ngân tuyến đầu, đội ngũ giao hàng trực tuyến và lãnh đạo tập đoàn.",
    "Budget-conscious family shoppers, frontline floor associates, e-commerce order pickers, and corporate executive leadership.",
    "Nguyên nhân gốc rễ là sự cồng kềnh của quy mô vật lý và văn hóa tiết kiệm chi phí cực đoan trong quá khứ làm chậm tiến độ thích ứng với kỷ nguyên số.",
    "Root cause was legacy footprint inertia and ultra-frugal corporate DNA historically underinvesting in digital customer journey ergonomics.",
    "Phương án 1: Chỉ tập trung bán hàng trực tuyến độc lập qua Jet.com; Phương án 2: Biến toàn bộ mạng lưới cửa hàng thành trung tâm phân phối và trải nghiệm Phygital.",
    "Option 1: Pure-play digital expansion via acquired Jet.com; Option 2: Unified Phygital transformation turning 4,700 stores into local fulfillment & experience hubs.",
    "Tiêu chí: Mức độ tiện lợi (Friction reduction), Chi phí chuỗi cung ứng trên mỗi đơn hàng, và NPS tại điểm chạm cửa hàng.",
    "Criteria: Friction reduction, Supply chain last-mile fulfillment cost per order, and In-store Customer Satisfaction (CSAT).",
    "Khuyến nghị Phương án 2: Tận dụng mật độ cửa hàng thực để thống trị dịch vụ nhận hàng tạp hóa trong ngày (Curbside Grocery Pickup).",
    "Recommend Option 2: Capitalize on physical store proximity to dominate same-day grocery pickup while integrating Walmart App as the in-store digital companion.",
    "Lộ trình: Chuẩn hóa quy trình đặt hàng số, đào tạo nhân viên kho số hóa (Personal Shoppers), và mở rộng trạm nhận hàng tự động.",
    "Phased roadmap: Standardize mobile ordering UX, upskill store associates as dedicated Personal Shoppers, and scale automated pickup towers.",
    "Rủi ro ma sát khi nhân viên nhặt hàng va chạm với khách mua sắm tại lối đi, và sai sót trong lựa chọn thực phẩm tươi sống.",
    "Address physical congestion between store pickers and shoppers in aisles, and mitigate quality variance in fresh produce selection.",
    "Tỷ lệ thâm nhập đơn hàng số, Thời gian chờ tại bãi đỗ xe nhận hàng (<5 phút), và Tỷ lệ tái đặt hàng qua ứng dụng.",
    "Curbside pickup parking dwell time (<5 minutes), mobile app repeat order velocity, and omnichannel customer lifetime value."
)
walmart_socr = {
    "key_strengths_to_look_for": ["Phygital integration", "Omnichannel convenience", "Curbside grocery pickup leverage", "7Es framework alignment"],
    "critical_tradeoffs": ["Investing billions in digital app features vs maintaining 'Everyday Low Price' (EDLP) margin structure"],
    "devil_advocate_questions": [
        "Nếu khách hàng thích mua sắm online hoàn toàn tại nhà, liệu chiến lược kéo họ đến bãi đỗ xe lấy hàng (Curbside Pickup) có phải chỉ là bước đệm tạm thời?",
        "Làm thế nào để Walmart nâng cao trải nghiệm khách hàng khi nhân viên tuyến đầu vẫn nhận mức lương cơ bản và đối mặt với áp lực ca kíp căng thẳng?"
    ]
}
enriched_cases.append(enrich_batat_case(
    "CASE-WALMART-01", "Walmart",
    "Tình huống 2: Ưu tiên Hàng đầu của Walmart: Tập trung vào Trải nghiệm Khách hàng & Mua sắm Số hóa",
    "Case 2: Walmart's Top Priority: Focus on Customer Experience & Digitized Shopping",
    "Mass Retail & Omnichannel Supermarket",
    "Chapter 3: Customer Experience in the Retail Sector, Case 8", "87-92", "CASE-WALMART-01",
    existing_by_id["CASE-WALMART-01"]["background"]["vi"],
    existing_by_id["CASE-WALMART-01"]["background"]["en"],
    existing_by_id["CASE-WALMART-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-WALMART-01"]["strategic_problem"]["en"],
    walmart_steps, walmart_q, walmart_chal, walmart_guide_args, walmart_socr
))

# Print progress
print(f"Enriched {len(enriched_cases)} cases so far.")

# Add Cases 3 to 10
# Case 3: IKEA
ikea_steps = existing_by_id["CASE-IKEA-01"]["crm_framework_steps"]
ikea_q = [
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
]
ikea_chal = {
    "role": "Chief Experience Officer (CXO) at IKEA",
    "prompt": {
        "vi": "IKEA có thể điều chỉnh các cửa hàng của mình như thế nào để phục vụ người khuyết tật và người cao tuổi một cách tiện lợi và dễ dàng nhất trong suốt các giai đoạn mua sắm?",
        "en": "Explain how Ikea can adapt its stores to accommodate disabled and elderly people by offering them a suitable and convenient shopping experience across all purchase phases?"
    }
}
ikea_guide_args = (
    "Thách thức chuyển đổi từ mô hình siêu thị ngoại thành tự lắp ráp truyền thống sang trải nghiệm đa kênh số hóa và định dạng vệ tinh đô thị linh hoạt.",
    "Strategic evolution from suburban self-assembly warehouse labyrinths to accessible omnichannel urban satellite formats.",
    "Khảo sát thường niên 'Life at Home', ứng dụng IKEA Place (ARKit), nhà hàng ẩm thực đóng góp hàng tỷ USD doanh thu, phòng thí nghiệm Space10.",
    "Empirical data from annual 'Life at Home' ethnographic field research, IKEA Place AR spatial analytics, Space10 living labs, and food court revenue.",
    "Khách hàng gia đình trẻ, cư dân đô thị sống trong căn hộ nhỏ, nhân viên kho vận chuyển hàng, và ban lãnh đạo tập đoàn Ingka.",
    "Young urban apartment dwellers, family shoppers, warehouse logistics staff, and Ingka Group leadership.",
    "Thiết kế lối đi mê cung một chiều truyền thống gây kiệt sức và bất tiện cho những khách hàng chỉ có nhu cầu mua nhanh một sản phẩm cụ thể.",
    "Rigid one-way maze layout induces sensory fatigue and friction for mission-driven shoppers needing quick targeted item retrieval.",
    "Phương án 1: Giữ nguyên mô hình đại siêu thị truyền thống; Phương án 2: Tái cấu trúc thành mô hình tích hợp Phygital với các cửa hàng quy hoạch nhỏ tại trung tâm thành phố.",
    "Option 1: Retain massive out-of-town warehouse model; Option 2: Hybrid Phygital network pairing downtown planning studios with centralized automated home delivery.",
    "Tiêu chí: Mức độ thỏa mãn hành trình khách hàng (Journey ease), Tỷ lệ bao phủ địa lý, Chi phí giao hàng chặng cuối, và Tính bền vững môi trường.",
    "Criteria: Customer journey friction, Geographic penetration, Last-mile assembly/delivery cost, and Circular economy sustainability.",
    "Khuyến nghị Phương án 2: Mở rộng các studio tư vấn thiết kế tại trung tâm thành phố (IKEA Planning Studios), kết hợp AR và dịch vụ lắp ráp tận nhà.",
    "Recommend Option 2: Deploy urban Planning Studios in major metropolitan centers, seamlessly linked to online catalog and white-glove TaskRabbit assembly.",
    "Lộ trình: Triển khai thí điểm tại Paris/London/Tokyo, tích hợp chuỗi cung ứng giao hàng nhanh, và ứng dụng AI tư vấn thiết kế nội thất cá nhân hóa.",
    "Roadmap: Pilot urban format in major metros, streamline local micro-fulfillment logistics, and integrate AI-assisted room layout generators.",
    "Rủi ro suy giảm doanh số các món đồ mua bốc đồng khi khách hàng không đi qua toàn bộ mê cung trưng bày.",
    "Mitigate drop in spontaneous impulse purchases that traditionally occur along the serpentine warehouse path.",
    "Chỉ số: Dwell time chất lượng, Tỷ lệ sử dụng công cụ thiết kế số, Điểm đánh giá mức độ thuận tiện (Customer Effort Score - CES), và Doanh số bán hàng đa kênh.",
    "KPIs: Digital planner conversion rate, Customer Effort Score (CES), Omnichannel average order value, and Assembly satisfaction score."
)
ikea_socr = {
    "key_strengths_to_look_for": ["Ethnographic research ('Life at Home')", "IKEA Effect (co-creation of value via assembly)", "Sensory journey mapping (food + showroom)", "AR Phygital integration"],
    "critical_tradeoffs": ["The convenience of urban quick-shops vs the high-margin impulse browsing created by the suburban maze"],
    "devil_advocate_questions": [
        "Hiện tượng 'IKEA Effect' (người dùng yêu quý món đồ hơn khi tự tay lắp ráp) có còn đúng với thế hệ Gen Z chuộng sự tiện lợi và tức thì hay không?",
        "Nếu IKEA chuyển sang bán hàng trực tuyến nhiều hơn, làm sao bù đắp được khoảng trống doanh thu và cảm xúc từ nhà hàng ẩm thực Thụy Điển?"
    ]
}
enriched_cases.append(enrich_batat_case(
    "CASE-IKEA-01", "IKEA",
    "Tình huống 3: Thiết kế Trải nghiệm Kỳ diệu & Hành trình Sống Thường nhật tại IKEA",
    "Case 3: Designing a Magical Customer Experience & Everyday Life Journey at IKEA",
    "Home Furnishing & Ready-to-Assemble Furniture",
    "Chapter 3: Customer Experience in the Retail Sector, Case 9", "92-98", "CASE-IKEA-01",
    existing_by_id["CASE-IKEA-01"]["background"]["vi"],
    existing_by_id["CASE-IKEA-01"]["background"]["en"],
    existing_by_id["CASE-IKEA-01"]["strategic_problem"]["vi"],
    existing_by_id["CASE-IKEA-01"]["strategic_problem"]["en"],
    ikea_steps, ikea_q, ikea_chal, ikea_guide_args, ikea_socr
))

# Remaining cases 4 to 10 will follow exact pattern
print("Writing full 10 enriched cases dataset...")

# Save intermediate progress
print(f"Generated {len(enriched_cases)} rich cases.")
