import json
from pathlib import Path

data_dir = Path(r"C:\Kiến thức cần học\CRM\output\data")

# 1. 10 CURATED EXAMS BLUEPRINTS
exams = [
    {
        "id": "EXAM-01",
        "exam_number": 1,
        "title": {
            "vi": "Đề thi 01: Nền tảng & Định hướng Chiến lược CRM",
            "en": "Exam 01: CRM Foundations & Strategic Orientation"
        },
        "description": {
            "vi": "Kiểm tra nhận thức toàn diện về các chiều kích của CRM, sự chuyển dịch từ Marketing Giao dịch sang Marketing Mối quan hệ, Giá trị Vòng đời Khách hàng (CLV) và các thành phần hữu hình.",
            "en": "Comprehensive assessment on CRM dimensions, the shift from Transactional to Relationship Marketing, Customer Lifetime Value (CLV), and tangible components."
        },
        "target_domain": "Foundations & Strategy",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Baran & Galka Ch. 1-3", "Kostojohn et al. Ch. 1"],
        "question_ids": [f"q-01-{i:02d}" for i in range(1, 21)]
    },
    {
        "id": "EXAM-02",
        "exam_number": 2,
        "title": {
            "vi": "Đề thi 02: Tổ chức, Văn hóa & Quản trị Dự án CRM",
            "en": "Exam 02: Organizational Alignment, Culture & Governance"
        },
        "description": {
            "vi": "Đánh giá kiến thức về bộ ba Con người - Quy trình - Công nghệ, cơ cấu Ban Chỉ đạo, Đại sứ phòng ban, xóa bỏ ốc đảo phòng ban và quản trị thay đổi.",
            "en": "Evaluates People-Process-Technology triad, Steering Committee governance, Departmental Champions, silo dismantling, and change management."
        },
        "target_domain": "Organization & Governance",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Kostojohn et al. Ch. 2", "Baran & Galka Ch. 4"],
        "question_ids": [f"q-02-{i:02d}" for i in range(1, 21)]
    },
    {
        "id": "EXAM-03",
        "exam_number": 3,
        "title": {
            "vi": "Đề thi 03: Kiến trúc Dữ liệu Khách hàng & Phân tích",
            "en": "Exam 03: Customer Data Architecture & Analytics"
        },
        "description": {
            "vi": "Kiểm tra chuyên sâu về Chân dung khách hàng 360 độ (SCV), vệ sinh dữ liệu, kho dữ liệu (Data Warehouse), phân đoạn khách hàng và phân tích RFM.",
            "en": "In-depth testing on Single Customer View (SCV), data hygiene, data warehousing, behavioral segmentation, and RFM analytics."
        },
        "target_domain": "Data & Analytics",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Baran & Galka Ch. 5, 7", "Tesco Case Study"],
        "question_ids": [f"q-03-{i:02d}" for i in range(1, 21)]
    },
    {
        "id": "EXAM-04",
        "exam_number": 4,
        "title": {
            "vi": "Đề thi 04: Nền tảng Công nghệ & Hạ tầng CRM",
            "en": "Exam 04: CRM Technology Platforms & Infrastructure"
        },
        "description": {
            "vi": "Đánh giá hiểu biết về Cloud/SaaS vs On-Premises, môi trường Dev/Test/Production, quản lý mã nguồn và kiến trúc tích hợp API.",
            "en": "Assesses Cloud/SaaS vs On-Premises trade-offs, multi-tier environments (Dev/Test/Prod), source control, and API integrations."
        },
        "target_domain": "Technology & Architecture",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Baran & Galka Ch. 6", "Kostojohn et al. Ch. 4"],
        "question_ids": [f"q-04-{i:02d}" for i in range(1, 21)]
    },
    {
        "id": "EXAM-05",
        "exam_number": 5,
        "title": {
            "vi": "Đề thi 05: Thiết kế Lộ trình & Lập kế hoạch Triển khai",
            "en": "Exam 05: Roadmap Design & Implementation Planning"
        },
        "description": {
            "vi": "Phân tích phương pháp tiếp cận theo giai đoạn (phased approach), ma trận giá trị vs độ phức tạp, phương pháp Waterfall vs Agile và quản lý ngân sách.",
            "en": "Analyzes phased implementation roadmaps, value vs. complexity matrices, Waterfall vs. Agile methodologies, and project budgeting."
        },
        "target_domain": "Roadmap & Planning",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Kostojohn et al. Ch. 3, 5"],
        "question_ids": [f"q-05-{i:02d}" for i in range(1, 21)]
    },
    {
        "id": "EXAM-06",
        "exam_number": 6,
        "title": {
            "vi": "Đề thi 06: Thực thi Triển khai, Kiểm thử & Đưa vào Vận hành",
            "en": "Exam 06: CRM Execution, Testing & System Launch"
        },
        "description": {
            "vi": "Kiểm tra chi tiết về thiết kế chức năng, chuyển đổi dữ liệu (data migration), các cấp độ kiểm thử (Unit, System, UAT, Performance) và kế hoạch Go-Live.",
            "en": "Tests functional design, data cleansing & migration, testing tiers (Unit, System, UAT, Performance), and go-live cutover playbooks."
        },
        "target_domain": "Execution & Testing",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Kostojohn et al. Ch. 6"],
        "question_ids": [f"q-06-{i:02d}" for i in range(1, 21)]
    },
    {
        "id": "EXAM-07",
        "exam_number": 7,
        "title": {
            "vi": "Đề thi 07: Kinh tế học về Sự Hài lòng, Lòng Trung thành & Giữ chân",
            "en": "Exam 07: Satisfaction, Loyalty & Retention Economics"
        },
        "description": {
            "vi": "Nắm vững chuỗi lợi nhuận dịch vụ, đo lường CSAT/NPS, trung thành hành vi vs thái độ, kinh tế học giữ chân và chiến lược giành lại khách hàng (win-back).",
            "en": "Mastering the service-profit chain, CSAT/NPS metrics, behavioral vs. attitudinal loyalty, retention economics, and customer win-back."
        },
        "target_domain": "Loyalty & Retention",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Baran & Galka Ch. 9, 10"],
        "question_ids": [f"q-07-{i:02d}" for i in range(1, 21)]
    },
    {
        "id": "EXAM-08",
        "exam_number": 8,
        "title": {
            "vi": "Đề thi 08: CRM Doanh nghiệp với Doanh nghiệp (B2B) & Đối tác",
            "en": "Exam 08: Business-to-Business (B2B) CRM & Partnerships"
        },
        "description": {
            "vi": "Đặc thù CRM trong môi trường B2B: Trung tâm mua sắm (Buying Centers), Quản lý tài khoản trọng yếu (KAM), chu kỳ bán hàng dài và hợp đồng quan hệ.",
            "en": "Specifics of B2B CRM: Buying Centers, Key Account Management (KAM), extended sales cycles, and relational contracting."
        },
        "target_domain": "B2B CRM",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Baran & Galka Ch. 8", "GAFA / Platform Cases"],
        "question_ids": [f"q-08-{i:02d}" for i in range(1, 21)]
    },
    {
        "id": "EXAM-09",
        "exam_number": 9,
        "title": {
            "vi": "Đề thi 09: Trải nghiệm Đa kênh, Social CRM & Xu hướng Mới",
            "en": "Exam 09: Omnichannel, Social CRM & Emerging Trends"
        },
        "description": {
            "vi": "Trải nghiệm Phygital kết hợp online/offline, lắng nghe mạng xã hội (Social Listening), trí tuệ nhân tạo (AI) và tự động hóa trải nghiệm khách hàng.",
            "en": "Phygital omnichannel integration, social listening & SCRM, conversational AI, and personalized customer journey orchestration."
        },
        "target_domain": "Omnichannel & SCRM",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Baran & Galka Ch. 13, 14", "Disney / Nike Cases"],
        "question_ids": [f"q-09-{i:02d}" for i in range(1, 21)]
    },
    {
        "id": "EXAM-10",
        "exam_number": 10,
        "title": {
            "vi": "Đề thi 10: Đo lường Hiệu quả, Đạo đức, Bảo mật & Tiến hóa CRM",
            "en": "Exam 10: Metrics, Privacy, Ethics & Maintenance"
        },
        "description": {
            "vi": "Tính toán CLV/CAC/ROCI, tuân thủ quyền riêng tư dữ liệu (GDPR/quy định), đạo đức thuật toán, và quy trình bảo trì, nâng cấp CRM sau Go-Live.",
            "en": "Quantitative CLV/CAC/ROCI formulas, data privacy regulations (GDPR), ethical governance, and post-go-live maintenance and evolution."
        },
        "target_domain": "Metrics, Privacy & Evolution",
        "question_count": 20,
        "time_limit_minutes": 30,
        "primary_sources": ["Baran & Galka Ch. 11, 12", "Kostojohn et al. Ch. 7"],
        "question_ids": [f"q-10-{i:02d}" for i in range(1, 21)]
    }
]

(data_dir / "exams.json").write_text(json.dumps(exams, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Generated exams.json with 10 curated exam blueprints.")

# 2. INITIAL VALIDATED QUESTIONS (Linked directly to EXAM-01)
questions = [
    {
        "id": "q-01-01",
        "exam_id": "EXAM-01",
        "topic": "Foundations",
        "difficulty": "easy",
        "question_type": "single_choice",
        "question": {
            "vi": "Theo Baran & Galka (2017), sự khác biệt căn bản nhất giữa Marketing Giao dịch (Transactional Marketing) và Marketing Mối quan hệ (Relationship Marketing/CRM) là gì?",
            "en": "According to Baran & Galka (2017), what is the most fundamental difference between Transactional Marketing and Relationship Marketing (CRM)?"
        },
        "options": [
            {
                "id": "A",
                "text": {
                    "vi": "Marketing giao dịch tập trung tối đa hóa lợi nhuận của từng thương vụ riêng lẻ, trong khi CRM tập trung xây dựng mối quan hệ lâu dài để tối đa hóa Giá trị Vòng đời Khách hàng (CLV).",
                    "en": "Transactional marketing focuses on maximizing profits from discrete individual sales, whereas CRM focuses on cultivating enduring relationships to maximize Customer Lifetime Value (CLV)."
                }
            },
            {
                "id": "B",
                "text": {
                    "vi": "Marketing giao dịch chỉ áp dụng cho doanh nghiệp B2B, trong khi CRM chỉ áp dụng cho doanh nghiệp B2C.",
                    "en": "Transactional marketing applies exclusively to B2B firms, while CRM applies solely to B2C firms."
                }
            },
            {
                "id": "C",
                "text": {
                    "vi": "Marketing giao dịch dựa hoàn toàn vào dữ liệu khách hàng, trong khi CRM chỉ dựa vào trực giác của người bán hàng.",
                    "en": "Transactional marketing relies entirely on customer databases, while CRM relies solely on salesperson intuition."
                }
            },
            {
                "id": "D",
                "text": {
                    "vi": "CRM yêu cầu doanh nghiệp phải đối xử công bằng và đầu tư chi phí như nhau cho tất cả mọi khách hàng.",
                    "en": "CRM mandates that the enterprise invest an identical amount of resources into every single customer."
                }
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "vi": "Marketing giao dịch xem việc bán hàng là điểm kết thúc của quy trình; CRM xem việc bán hàng đầu tiên là điểm khởi đầu của mối quan hệ nhằm gia tăng giá trị trọn đời của khách hàng.",
            "en": "Transactional marketing treats the sale as the termination of the interaction; CRM regards the initial transaction as the inception of an ongoing relationship to maximize lifetime value."
        },
        "source": {
            "document": "Baran & Galka (2017)",
            "chapter": "Chapter 1",
            "pages": "10-15"
        },
        "tags": ["foundations", "transactional-vs-relational"],
        "validation_status": "verified"
    },
    {
        "id": "q-01-02",
        "exam_id": "EXAM-01",
        "topic": "Foundations",
        "difficulty": "medium",
        "question_type": "single_choice",
        "question": {
            "vi": "Một ngân hàng thương mại triển khai phần mềm quản lý phân tích dữ liệu giao dịch thẻ tín dụng để dự báo khách hàng có nguy cơ rời bỏ (churn). Hoạt động này thuộc chiều kích nào của CRM?",
            "en": "A commercial bank deploys software to analyze credit card transaction histories to predict customer churn risks. Which dimension of CRM does this represent?"
        },
        "options": [
            { "id": "A", "text": { "vi": "CRM Tác nghiệp (Operational CRM)", "en": "Operational CRM" } },
            { "id": "B", "text": { "vi": "CRM Phân tích (Analytical CRM)", "en": "Analytical CRM" } },
            { "id": "C", "text": { "vi": "CRM Hợp tác (Collaborative CRM)", "en": "Collaborative CRM" } },
            { "id": "D", "text": { "vi": "CRM Tự động hóa tiếp thị đơn thuần", "en": "Simple Marketing Automation" } }
        ],
        "correct_answer": "B",
        "explanation": {
            "vi": "CRM Phân tích (Analytical CRM) chịu trách nhiệm khai phá, phân tích dữ liệu hành vi của khách hàng nhằm đưa ra các mô hình dự báo và hỗ trợ ra quyết định kinh doanh.",
            "en": "Analytical CRM is specifically responsible for capturing, mining, and analyzing customer behavioral data to build predictive models and inform decision-making."
        },
        "source": {
            "document": "Baran & Galka (2017)",
            "chapter": "Chapter 1",
            "pages": "12-14"
        },
        "tags": ["dimensions", "analytical-crm"],
        "validation_status": "verified"
    },
    {
        "id": "q-01-03",
        "exam_id": "EXAM-01",
        "topic": "Foundations",
        "difficulty": "medium",
        "question_type": "single_choice",
        "question": {
            "vi": "Theo Kostojohn et al. (2011), yếu tố nào sau đây KHÔNG phải là một trong bốn nguồn giá trị kinh doanh cốt lõi của CRM?",
            "en": "According to Kostojohn et al. (2011), which of the following is NOT one of the four primary sources of CRM business value?"
        },
        "options": [
            { "id": "A", "text": { "vi": "Hỗ trợ xây dựng tổ chức học tập định hướng dữ liệu.", "en": "Supporting a data-driven, learning organization." } },
            { "id": "B", "text": { "vi": "Loại bỏ sự lãng phí và tăng năng suất của nhân viên.", "en": "Wringing out inefficiencies and increasing employee productivity." } },
            { "id": "C", "text": { "vi": "Cung cấp một trải nghiệm khách hàng vượt trội hơn.", "en": "Providing a superior customer experience." } },
            { "id": "D", "text": { "vi": "Bảo đảm doanh thu tăng trưởng tự động mà không cần nhân sự giám sát.", "en": "Guaranteeing automated revenue growth without human supervision." } }
        ],
        "correct_answer": "D",
        "explanation": {
            "vi": "Bốn nguồn giá trị được Kostojohn et al. nêu rõ gồm: (1) Tổ chức học tập định hướng dữ liệu, (2) Loại bỏ lãng phí nâng cao năng suất, (3) Trải nghiệm khách hàng tốt hơn, và (4) Cung cấp dữ liệu định hướng quyết định kinh doanh. CRM không bao giờ bảo đảm tăng trưởng tự động thiếu sự tham gia của con người.",
            "en": "The four sources defined by Kostojohn et al. are data-driven learning, productivity/efficiency, better CX, and strategic decision support. CRM never guarantees automated growth without human involvement."
        },
        "source": {
            "document": "Kostojohn et al. (2011)",
            "chapter": "Chapter 1",
            "pages": "15-20"
        },
        "tags": ["kostojohn-ch1", "sources-of-value"],
        "validation_status": "verified"
    }
]

(data_dir / "question-bank.json").write_text(json.dumps(questions, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Generated question-bank.json with initial validated questions.")
