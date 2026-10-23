import json
from pathlib import Path

data_dir = Path(r"C:\Kiến thức cần học\CRM\output\data")

flashcards = [
    {
        "id": "fc-001",
        "topic": "CRM Foundations",
        "chapter_id": "mod-baran-ch01",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Bốn khía cạnh (4 dimensions) cấu thành nên một chiến lược CRM toàn diện là gì?",
            "en": "What are the four core dimensions comprising a comprehensive CRM strategy?"
        },
        "back": {
            "vi": "1. CRM Chiến lược (Strategic CRM)\n2. CRM Tác nghiệp (Operational CRM)\n3. CRM Phân tích (Analytical CRM)\n4. CRM Hợp tác (Collaborative CRM)",
            "en": "1. Strategic CRM\n2. Operational CRM\n3. Analytical CRM\n4. Collaborative CRM"
        },
        "hint": {
            "vi": "Bao gồm tầm nhìn lãnh đạo, tự động hóa tại điểm chạm, khai phá dữ liệu và chia sẻ thông tin liên phòng ban.",
            "en": "Spans leadership vision, front-office automation, data mining, and cross-departmental alignment."
        },
        "difficulty": "medium",
        "tags": ["foundations", "baran-ch1"],
        "source": { "document": "Baran & Galka (2017) pp. 8-15" }
    },
    {
        "id": "fc-002",
        "topic": "Metrics",
        "chapter_id": "mod-baran-ch01",
        "card_type": "definition_to_term",
        "front": {
            "vi": "Thước đo giá trị hiện tại ròng của tổng dòng lợi nhuận tương lai mà một khách hàng đóng góp cho doanh nghiệp trong suốt toàn bộ mối quan hệ được gọi là gì?",
            "en": "What is the metric representing the net present value of the future stream of profits attributed to the entire relationship with a customer?"
        },
        "back": {
            "vi": "Giá trị Vòng đời Khách hàng (Customer Lifetime Value - CLV)",
            "en": "Customer Lifetime Value (CLV)"
        },
        "hint": {
            "vi": "Viết tắt là CLV hoặc LTV.",
            "en": "Commonly abbreviated as CLV or LTV."
        },
        "difficulty": "easy",
        "tags": ["metrics", "clv"],
        "source": { "document": "Baran & Galka (2017) pp. 24-28" }
    },
    {
        "id": "fc-003",
        "topic": "Relationship Marketing",
        "chapter_id": "mod-baran-ch03",
        "card_type": "compare_and_contrast",
        "front": {
            "vi": "So sánh 3 cấp độ gắn kết mối quan hệ: Tài chính, Xã hội và Cấu trúc. Cấp độ nào tạo ra rào cản chuyển đổi (Switching Costs) bền vững nhất?",
            "en": "Compare the 3 levels of relationship bonding: Financial, Social, and Structural. Which creates the most durable switching barrier?"
        },
        "back": {
            "vi": "- Cấp 1 (Tài chính): Điểm thưởng, giảm giá (dễ bị đối thủ sao chép nhất).\n- Cấp 2 (Xã hội): Giao tiếp cá nhân hóa, thấu hiểu cảm xúc.\n- Cấp 3 (Cấu trúc): Tích hợp hệ thống công nghệ, quy trình vận hành chung (bền vững nhất và khó chuyển đổi nhất).",
            "en": "- Level 1 (Financial): Price discounts, reward points (easiest for rivals to duplicate).\n- Level 2 (Social): Personalization, emotional rapport.\n- Level 3 (Structural): Joint technology integration, embedded processes (most durable switching barrier)."
        },
        "hint": {
            "vi": "Cấp độ 3 liên quan đến việc tích hợp kỹ thuật hoặc API/quy trình giữa hai bên.",
            "en": "Level 3 involves deep systems or process embedding between the firm and client."
        },
        "difficulty": "hard",
        "tags": ["relationship-marketing", "bonds"],
        "source": { "document": "Baran & Galka (2017) pp. 88-95" }
    },
    {
        "id": "fc-004",
        "topic": "Implementation & Governance",
        "chapter_id": "mod-fund-ch02",
        "card_type": "framework",
        "front": {
            "vi": "Theo Kostojohn et al. (2011), Bốn Trụ Cột Thành Công của một chương trình CRM là gì?",
            "en": "According to Kostojohn et al. (2011), what are the Four Pillars of CRM Success?"
        },
        "back": {
            "vi": "1. Con người (People): Đúng người đúng việc, phân rõ trách nhiệm.\n2. Quy trình (Process): Quy trình nội bộ và hướng ngoại được thiết kế chuẩn mực.\n3. Công nghệ (Technology): Nền tảng công cụ hỗ trợ phù hợp.\n4. Kỳ vọng (Expectations): Đặt ra kỳ vọng thực tế về kết quả, chi phí và nỗ lực cần bỏ ra.",
            "en": "1. People: Right people in right roles with clear responsibilities.\n2. Process: Well-thought-out, well-designed internal and customer-facing workflows.\n3. Technology: The right supporting technology tools.\n4. Expectations: Setting reasonable expectations for success, effort, and cost."
        },
        "hint": {
            "vi": "Tác giả nêu rõ 4 trụ cột chứ không đơn thuần chỉ có 3 yếu tố như quan niệm phổ biến.",
            "en": "The authors define 4 pillars, explicitly adding Expectations to the classic triad."
        },
        "difficulty": "medium",
        "tags": ["governance", "four-pillars", "kostojohn-ch2"],
        "source": { "document": "Kostojohn et al. (2011) p. 11" }
    },
    {
        "id": "fc-005",
        "topic": "Governance",
        "chapter_id": "mod-fund-ch02",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Vai trò chính của Ban Chỉ đạo Dự án (Steering Committee) trong triển khai CRM là gì?",
            "en": "What is the primary role of the CRM Steering Committee during implementation?"
        },
        "back": {
            "vi": "Định hướng chiến lược liên phòng ban, phê duyệt ngân sách, giải quyết xung đột chính trị nội bộ và kiểm soát ngăn chặn hiện tượng phình to phạm vi dự án (Scope Creep).",
            "en": "Provide cross-functional governance, approve budget, arbitrate internal conflicts, and prevent fatal project scope creep."
        },
        "hint": {
            "vi": "Là hội đồng lãnh đạo cấp cao họp định kỳ để ra các quyết định then chốt.",
            "en": "A high-level executive body that meets periodically to resolve major scope decisions."
        },
        "difficulty": "medium",
        "tags": ["governance", "kostojohn-ch2"],
        "source": { "document": "Kostojohn et al. (2011) pp. 25-27" }
    },
    {
        "id": "fc-006",
        "topic": "Data Management",
        "chapter_id": "mod-baran-ch05",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Khái niệm Hộ gia đình hóa (Householding) trong quản trị dữ liệu CRM là gì và mang lại lợi ích gì?",
            "en": "What is Householding in CRM data management and what business benefit does it deliver?"
        },
        "back": {
            "vi": "Householding là kỹ thuật gom nhóm các cá nhân cùng chung sống tại một địa chỉ thực tế hoặc cùng một hộ gia đình. Lợi ích: Ngăn chặn gửi các bức thư tiếp thị hoặc danh mục sản phẩm trùng lặp, tiết kiệm hàng triệu USD chi phí in ấn/bưu chính và tránh gây khó chịu cho khách hàng.",
            "en": "Householding links individual customer records residing at the same physical address into a unified household unit. Benefit: Prevents sending redundant marketing mailings, saving millions in print/postage while eliminating consumer annoyance."
        },
        "hint": {
            "vi": "Liên quan đến việc nhận diện các thành viên trong cùng một gia đình sống chung địa chỉ.",
            "en": "Involves clustering multiple family members sharing the same residence."
        },
        "difficulty": "medium",
        "tags": ["data-management", "householding"],
        "source": { "document": "Baran & Galka (2017) Ch. 5, pp. 155-160" }
    },
    {
        "id": "fc-007",
        "topic": "Technology Platforms",
        "chapter_id": "mod-baran-ch06",
        "card_type": "compare_and_contrast",
        "front": {
            "vi": "Phân biệt sự khác nhau giữa Cơ sở dữ liệu Tác nghiệp (ODS/OLTP) và Kho Dữ liệu (Data Warehouse / OLAP).",
            "en": "Distinguish between an Operational Data Store (ODS/OLTP) and a Data Warehouse (EDW/OLAP)."
        },
        "back": {
            "vi": "- ODS/OLTP: Lưu trữ dữ liệu tức thời thời gian thực phục vụ nhân viên xử lý giao dịch hàng ngày (tối ưu tốc độ đọc/ghi đơn lẻ).\n- Data Warehouse/OLAP: Lưu trữ dữ liệu lịch sử tổng hợp nhiều năm phục vụ báo cáo quản trị và khai phá dữ liệu (tối ưu hóa truy vấn phân tích phức tạp đa chiều).",
            "en": "- ODS/OLTP: Real-time transactional store powering front-line daily interactions (optimized for rapid single-row read/writes).\n- Data Warehouse/OLAP: Historical multi-year analytical repository structured for complex business intelligence and slice-and-dice data mining."
        },
        "hint": {
            "vi": "Một bên phục vụ giao dịch hàng ngày; một bên phục vụ báo cáo phân tích chiến lược.",
            "en": "One powers real-time transactions; the other powers strategic analytical reporting."
        },
        "difficulty": "medium",
        "tags": ["technology", "data-warehouse"],
        "source": { "document": "Baran & Galka (2017) Ch. 6, pp. 185-192" }
    },
    {
        "id": "fc-008",
        "topic": "Roadmap Strategy",
        "chapter_id": "mod-fund-ch03",
        "card_type": "framework",
        "front": {
            "vi": "Tại sao Kostojohn et al. khuyến nghị triển khai CRM theo phương pháp Tiếp cận theo Giai đoạn (Phased Approach) thay vì 'Big Bang'?",
            "en": "Why do Kostojohn et al. advocate a Phased Implementation Approach over a 'Big Bang' rollout?"
        },
        "back": {
            "vi": "Big Bang kéo dài 1-2 năm không có kết quả trung gian, gây rủi ro thất bại khổng lồ. Phased Approach chia dự án thành các giai đoạn ngắn 3-6 tháng, giúp thu hồi vốn nhanh (Faster ROI), tiếp nhận phản hồi thực tế từ người dùng để cải tiến hệ thống và giảm thiểu gián đoạn kinh doanh.",
            "en": "Big Bang deployments risk catastrophic failure by requiring 12-18 months of silent development without business value. A Phased Approach delivers rapid ROI every 3-6 months, incorporates iterative end-user feedback, and mitigates enterprise disruption."
        },
        "hint": {
            "vi": "Liên quan đến tốc độ tạo ra giá trị kinh doanh và sự kiên nhẫn của ban lãnh đạo.",
            "en": "Tied to rapid ROI realization and mitigating enterprise-wide operational risk."
        },
        "difficulty": "easy",
        "tags": ["roadmap", "phased-approach"],
        "source": { "document": "Kostojohn et al. (2011) Ch. 3, pp. 49-55" }
    },
    {
        "id": "fc-009",
        "topic": "B2B CRM",
        "chapter_id": "mod-baran-ch08",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Trung tâm Mua hàng (Buying Center / DMU) trong B2B gồm những vai trò nào?",
            "en": "What roles constitute the organizational Buying Center (DMU) in B2B CRM?"
        },
        "back": {
            "vi": "Gồm 7 vai trò:\n1. Người khởi xướng (Initiator)\n2. Người sử dụng (User)\n3. Người ảnh hưởng (Influencer)\n4. Người quyết định (Decider)\n5. Người phê duyệt (Approver)\n6. Người mua / Thu mua (Buyer)\n7. Người gác cổng (Gatekeeper)",
            "en": "Comprises 7 roles:\n1. Initiator\n2. User\n3. Influencer\n4. Decider\n5. Approver\n6. Buyer (Procurement)\n7. Gatekeeper"
        },
        "hint": {
            "vi": "Bao gồm từ người trực tiếp dùng máy đến giám đốc ký duyệt ngân sách và thư ký gác cổng.",
            "en": "Spans actual operational users up to economic deciders and administrative gatekeepers."
        },
        "difficulty": "hard",
        "tags": ["b2b", "buying-center"],
        "source": { "document": "Baran & Galka (2017) Ch. 8, pp. 242-248" }
    },
    {
        "id": "fc-010",
        "topic": "Metrics & Evaluation",
        "chapter_id": "mod-baran-ch12",
        "card_type": "framework",
        "front": {
            "vi": "Tỷ lệ chuẩn mực giữa Giá trị Vòng đời Khách hàng (CLV) và Chi phí Thu hút Khách hàng (CAC) là bao nhiêu?",
            "en": "What is the industry benchmark ratio between Customer Lifetime Value (CLV) and Customer Acquisition Cost (CAC)?"
        },
        "back": {
            "vi": "Tỷ lệ vàng chuẩn mực là tối thiểu **3:1** (CLV phải gấp ít nhất 3 lần CAC). Nếu là 1:1, doanh nghiệp đang bị lỗ ròng; nếu vượt quá 5:1, doanh nghiệp đang chi quá ít cho việc thu hút khách hàng mới.",
            "en": "The benchmark ratio is at least **3:1** (CLV must be at least 3x CAC). A 1:1 ratio represents margin destruction; a ratio exceeding 5:1 suggests under-investment in growth acquisition."
        },
        "hint": {
            "vi": "Lợi nhuận trọn đời phải lớn gấp mấy lần chi phí bỏ ra để mua khách hàng.",
            "en": "Lifetime gross profit must comfortably exceed acquisition expenditure."
        },
        "difficulty": "medium",
        "tags": ["metrics", "clv-cac"],
        "source": { "document": "Baran & Galka (2017) Ch. 12, pp. 360-365" }
    },
    {
        "id": "fc-011",
        "topic": "Social CRM",
        "chapter_id": "mod-baran-ch13",
        "card_type": "scenario",
        "front": {
            "vi": "Vụ việc 'United Breaks Guitars' (2009) minh họa cho nguyên lý căn bản nào trong kỷ nguyên Social CRM?",
            "en": "What core principle of the Social CRM era does the 'United Breaks Guitars' incident illustrate?"
        },
        "back": {
            "vi": "Minh họa cho sự đảo chiều quyền lực từ doanh nghiệp sang khách hàng. Trong kỷ nguyên mạng xã hội, một lời phàn nàn công khai của một cá nhân có thể lan truyền theo cấp số nhân và hủy hoại uy tín thương hiệu trị giá hàng triệu USD nếu doanh nghiệp thiếu quy trình phản hồi nhanh nhạy.",
            "en": "Illustrates the inversion of communication power from corporate monopolies to networked consumers. In the Social CRM era, a single aggrieved customer's viral post can inflict millions of dollars in market capitalization damage if service support remains unresponsive."
        },
        "hint": {
            "vi": "Một bài hát trên YouTube có thể làm bốc hơi hàng chục triệu USD giá trị cổ phiếu.",
            "en": "A single viral YouTube video can destroy corporate shareholder value."
        },
        "difficulty": "easy",
        "tags": ["social-crm", "united-breaks-guitars"],
        "source": { "document": "Baran & Galka (2017) Ch. 13, p. 431" }
    },
    {
        "id": "fc-012",
        "topic": "Execution & Testing",
        "chapter_id": "mod-fund-ch06",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Kiểm thử Chấp nhận của Người dùng (UAT) khác với Kiểm thử Hệ thống (System Testing) ở điểm nào?",
            "en": "How does User Acceptance Testing (UAT) differ from System Integration Testing (SIT)?"
        },
        "back": {
            "vi": "- System Testing do đội ngũ kỹ thuật thực hiện để kiểm tra xem phần mềm có bị lỗi code hay lỗi tích hợp dữ liệu hay không.\n- UAT do chính những người dùng nghiệp vụ thực tế thực hiện theo các kịch bản công việc hàng ngày để xác nhận phần mềm có giải quyết được bài toán kinh doanh trước khi Go-Live.",
            "en": "- System Testing is executed by technical engineers to verify code stability, API contracts, and integration integrity.\n- UAT is conducted directly by business operational end-users executing daily work tasks to formally sign off that the solution meets business requirements."
        },
        "hint": {
            "vi": "Một bên do IT kiểm tra lỗi kỹ thuật; một bên do nhân viên nghiệp vụ kiểm tra tính thực tiễn công việc.",
            "en": "One is executed by technical developers; the other by actual business end-users."
        },
        "difficulty": "medium",
        "tags": ["testing", "uat", "kostojohn-ch6"],
        "source": { "document": "Kostojohn et al. (2011) Ch. 6, pp. 183-195" }
    }
]

(data_dir / "flashcards.json").write_text(json.dumps(flashcards, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Flashcards successfully expanded to {len(flashcards)} cards.")
