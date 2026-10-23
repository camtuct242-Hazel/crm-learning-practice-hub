import json
from pathlib import Path

data_dir = Path(r"C:\Kiến thức cần học\CRM\output\data")
curr_file = data_dir / "curriculum.json"
curr = json.loads(curr_file.read_text(encoding="utf-8"))
existing_ids = {c["id"] for c in curr}

new_chapters = [
    # --- BARAN & GALKA PART III: MARKETING STRATEGY ---
    {
        "id": "mod-baran-ch08",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part III",
        "part_title": {
            "vi": "Phần III: Chiến lược Tiếp thị",
            "en": "Part III: Marketing Strategy"
        },
        "chapter_num": 8,
        "title": {
            "vi": "Chương 8: Quản trị Quan hệ Khách hàng Doanh nghiệp (B2B CRM)",
            "en": "Chapter 8: Business-to-Business CRM"
        },
        "pdf_page_start": 239,
        "book_page": 224,
        "learning_objectives": {
            "vi": [
                "Phân tích các đặc trưng cốt lõi của thị trường B2B so với B2C tác động đến chiến lược CRM.",
                "Hiểu rõ cấu trúc và vai trò của Trung tâm Mua hàng (Buying Center / DMU).",
                "Nắm vững phương pháp Quản lý Tài khoản Trọng yếu (Key Account Management - KAM).",
                "Áp dụng Quản trị Quan hệ Đối tác (Partner Relationship Management - PRM) trong mạng lưới chuyển giao giá trị."
            ],
            "en": [
                "Analyze structural B2B market characteristics impacting CRM compared to consumer B2C.",
                "Understand the composition and dynamics of the organizational Buying Center (DMU).",
                "Master Key Account Management (KAM) methodologies and joint value creation.",
                "Deploy Partner Relationship Management (PRM) across value delivery networks."
            ]
        },
        "key_concepts": [
            {
                "term": "Buying Center (DMU)",
                "name": { "vi": "Trung tâm Mua hàng (Buying Center / DMU)", "en": "Buying Center (DMU)" },
                "definition": {
                    "vi": "Nhóm tất cả các cá nhân trong tổ chức tham gia vào quá trình ra quyết định mua sắm, bao gồm: Người khởi xướng (Initiator), Người sử dụng (User), Người ảnh hưởng (Influencer), Người quyết định (Decider), Người phê duyệt (Approver), Người mua (Buyer) và Người gác cổng (Gatekeeper).",
                    "en": "The informal cross-functional committee participating in procurement decisions: Initiators, Users, Influencers, Deciders, Approvers, Buyers, and Gatekeepers."
                }
            },
            {
                "term": "Key Account Management (KAM)",
                "name": { "vi": "Quản lý Tài khoản Trọng yếu (KAM)", "en": "Key Account Management (KAM)" },
                "definition": {
                    "vi": "Chiến lược hợp tác chuyên sâu dành riêng cho nhóm khách hàng doanh nghiệp chiến lược đóng góp phần lớn doanh thu hoặc lợi nhuận của tổ chức.",
                    "en": "A strategic partnership approach dedicated to serving high-priority corporate accounts that generate the vast majority of enterprise value."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 8.1 Đặc thù B2B CRM\nKhác với B2C nơi một cá nhân thường tự đưa ra quyết định mua sắm nhanh chóng, giao dịch B2B có các đặc điểm riêng biệt:\n1. *Quy mô khách hàng ít nhưng giá trị từng hợp đồng rất lớn (Nguyên lý Pareto 80/20).* Thất thoát một khách hàng lớn có thể đe dọa sự tồn vong của doanh nghiệp.\n2. *Chu kỳ bán hàng kéo dài:* Thường từ 3 tháng đến 2 năm, đòi hỏi CRM phải theo dõi lịch sử tương tác qua nhiều giai đoạn thương thảo.\n3. *Quyết định mua sắm đa người (Buying Center):* Nhân viên bán hàng B2B không chỉ tiếp xúc với một người mua mà phải quản lý mối quan hệ với 6-10 bên liên quan khác nhau trong Trung tâm Mua hàng.\n\n### 8.2 Quản lý Tài khoản Trọng yếu (KAM)\nKAM đòi hỏi doanh nghiệp phải chuyển đổi từ tư cách 'nhà cung cấp thông thường' thành 'đối tác chiến lược tin cậy'. Đội ngũ KAM gồm nhiều chuyên gia liên phòng ban (Kỹ thuật, Tài chính, Chuỗi cung ứng, Chăm sóc khách hàng) phối hợp làm việc trực tiếp với đội ngũ tương ứng bên phía khách hàng.\n\n### 8.3 Quản trị Quan hệ Đối tác (PRM)\nTrong các ngành bán lẻ, công nghệ hoặc sản xuất, doanh nghiệp bán hàng qua mạng lưới đại lý và nhà phân phối trung gian. PRM cung cấp cổng thông tin đối tác (Partner Portal) giúp đăng ký cơ hội (lead registration), quản lý quỹ hỗ trợ tiếp thị (MDF - Market Development Funds) và tránh xung đột kênh bán.",
            "en": "### 8.1 Distinctive Dimensions of B2B CRM\nUnlike B2C where individual buyers make spontaneous, emotionally charged purchases, B2B commerce exhibits unique structural realities:\n1. *Concentrated Customer Base with Immense Stakes (Pareto 80/20):* Losing a single key account can cripple corporate viability.\n2. *Protracted Sales Cycles:* Typically 3 to 24 months, requiring rigorous stage-gate tracking in CRM pipeline models.\n3. *Complex Multi-Stakeholder Buying Centers:* Sales reps must navigate 6 to 10 distinct influencers, gatekeepers, and economic decision-makers within client organizations.\n\n### 8.2 Key Account Management (KAM) Methodologies\nKAM elevates transactional vendor engagements into collaborative value-creation partnerships. Dedicated multi-disciplinary account teams (solutions architects, finance, logistics) interface directly with client counterparts to co-innovate customized solutions.\n\n### 8.3 Partner Relationship Management (PRM)\nWhen distributing products through indirect channel partners, dealers, or value-added resellers (VARs), PRM platforms provide deal registration, collaborative quoting, co-op marketing fund (MDF) allocations, and channel conflict governance."
        },
        "key_takeaways": {
            "vi": [
                "B2B CRM tập trung vào việc quản lý mối quan hệ đa bên liên quan trong Trung tâm Mua hàng thay vì một người mua cá nhân.",
                "PRM và KAM là hai vũ khí cốt lõi để duy trì và mở rộng doanh thu gián tiếp qua mạng lưới đối tác."
            ],
            "en": [
                "B2B CRM navigates multi-stakeholder organizational dynamics rather than isolated individual consumers.",
                "KAM and PRM are vital strategic capabilities for managing high-value direct relationships and complex indirect channel networks."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b08-01",
                "question": {
                    "vi": "Hãy liệt kê các vai trò trong một Trung tâm Mua hàng (Buying Center) B2B. Tại sao nhân viên bán hàng chỉ thuyết phục 'Người sử dụng' (User) là chưa đủ để chốt hợp đồng?",
                    "en": "Enumerate the roles in a B2B Buying Center. Why is convincing the 'User' alone insufficient to close an enterprise deal?"
                },
                "model_answer": {
                    "vi": "Các vai trò gồm: Người khởi xướng, Người sử dụng, Người ảnh hưởng, Người quyết định, Người phê duyệt, Người mua và Người gác cổng. Người sử dụng có thể rất thích sản phẩm nhưng họ không có thẩm quyền ký duyệt ngân sách (vai trò của Decider/Approver) và có thể bị rào cản bởi Người gác cổng hoặc Người mua chuyên nghiệp muốn ép giá.",
                    "en": "Roles comprise Initiators, Users, Influencers, Deciders, Approvers, Buyers, and Gatekeepers. While Users validate day-to-day utility, they lack budgetary sign-off authority (held by Deciders/Approvers) and can be blocked by Gatekeepers or procurement Buyers demanding cost concessions."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 8",
            "pages": "239-269 (Book pp. 224-253)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-baran-ch09",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part III",
        "part_title": {
            "vi": "Phần III: Chiến lược Tiếp thị",
            "en": "Part III: Marketing Strategy"
        },
        "chapter_num": 9,
        "title": {
            "vi": "Chương 9: Chuỗi Lợi nhuận Khách hàng - Doanh nghiệp: Sự hài lòng, Lòng trung thành và Lợi nhuận",
            "en": "Chapter 9: Understanding the Customer–Company Profit Chain: Satisfaction, Loyalty, Retention, and Profits"
        },
        "pdf_page_start": 270,
        "book_page": 254,
        "learning_objectives": {
            "vi": [
                "Nắm vững cơ chế vận hành của Chuỗi Giá trị Dịch vụ - Lợi nhuận (Service-Profit Chain).",
                "Phân biệt rạch ròi giữa Trung thành Hành vi (Behavioral Loyalty) và Trung thành Thái độ (Attitudinal Loyalty).",
                "Đo lường sự hài lòng qua CSAT, CES (Customer Effort Score) và NPS (Net Promoter Score).",
                "Hiểu rõ mối quan hệ phi tuyến tính giữa mức độ hài lòng và tỷ lệ giữ chân khách hàng."
            ],
            "en": [
                "Master the causal mechanics of Heskett's Service-Profit Chain framework.",
                "Sharply distinguish Behavioral Loyalty from Attitudinal Loyalty.",
                "Measure customer perception via CSAT, Customer Effort Score (CES), and Net Promoter Score (NPS).",
                "Analyze the non-linear relationship between customer satisfaction and retention."
            ]
        },
        "key_concepts": [
            {
                "term": "Service-Profit Chain",
                "name": { "vi": "Chuỗi Dịch vụ - Lợi nhuận", "en": "Service-Profit Chain" },
                "definition": {
                    "vi": "Mô hình lý thuyết thiết lập mối quan hệ nhân quả: Chất lượng dịch vụ nội bộ → Sự hài lòng của nhân viên → Năng suất & giá trị dịch vụ tạo ra → Sự hài lòng của khách hàng → Lòng trung thành của khách hàng → Tăng trưởng doanh thu & Lợi nhuận.",
                    "en": "A framework establishing direct causality: Internal service quality drives employee satisfaction, which fuels service value, driving customer satisfaction and loyalty, yielding revenue growth and profitability."
                }
            },
            {
                "term": "Attitudinal vs. Behavioral Loyalty",
                "name": { "vi": "Trung thành Thái độ vs. Trung thành Hành vi", "en": "Attitudinal vs. Behavioral Loyalty" },
                "definition": {
                    "vi": "Trung thành hành vi là việc khách hàng tiếp tục mua lặp lại (có thể do thói quen hoặc không có lựa chọn khác); Trung thành thái độ là sự gắn kết cảm xúc, niềm tin sâu sắc và sẵn sàng giới thiệu doanh nghiệp cho người khác.",
                    "en": "Behavioral loyalty is repeat purchasing habit (potentially spurious); Attitudinal loyalty reflects deep emotional commitment, psychological attachment, and active brand advocacy."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 9.1 Mô hình Chuỗi Dịch vụ - Lợi nhuận (Service-Profit Chain)\nBaran & Galka phân tích mô hình kinh điển của Heskett et al.: Doanh nghiệp không thể có được khách hàng hài lòng nếu nhân viên trực tiếp phục vụ đang bất mãn và kiệt sức. Sự gắn kết của nhân viên nội bộ tạo ra chất lượng dịch vụ vượt trội, từ đó làm gia tăng sự hài lòng và lòng trung thành của khách hàng.\n\n### 9.2 Mối quan hệ Phi Tuyến tính giữa Hài lòng và Giữ chân\nNhiều nhà quản lý lầm tưởng rằng chỉ cần khách hàng 'hài lòng' là họ sẽ ở lại. Nghiên cứu của Jones & Sasser chỉ ra rằng:\n- Khách hàng 'hoàn toàn hài lòng' (Completely Satisfied - Điểm 5/5) có tỷ lệ quay lại cao gấp 6 lần so với khách hàng chỉ 'hài lòng' (Satisfied - Điểm 4/5).\n- Khách hàng ở mức điểm 4/5 thực chất là nhóm rất dễ bị đối thủ lôi kéo (Vùng Đào tẩu - Zone of Defection).\n\n### 9.3 Đo lường Trải nghiệm: CSAT, CES và NPS\n1. *CSAT (Customer Satisfaction Score):* Đo lường sự hài lòng tức thời sau một giao dịch cụ thể.\n2. *CES (Customer Effort Score):* Đo lường mức độ dễ dàng/thuận tiện khi khách hàng giải quyết sự cố ('Công ty đã giúp tôi xử lý vấn đề dễ dàng đến mức nào?'). Nỗ lực khách hàng bỏ ra càng thấp thì lòng trung thành càng cao.\n3. *NPS (Net Promoter Score):* Đo lường khả năng giới thiệu thương hiệu (% Promoters - % Detractors).",
            "en": "### 9.1 The Service-Profit Chain Framework\nBaran & Galka dissect Heskett's framework: sustainable external customer loyalty cannot be engineered if internal front-line personnel are alienated or demoralized. Internal service quality underpins employee productivity, driving superior perceived customer value and retention.\n\n### 9.2 The Non-Linear Satisfaction-to-Retention Curve\nExecutives frequently assume that 'satisfied' customers remain loyal. Empirical findings from Jones & Sasser demonstrate a steep drop-off:\n- 'Completely Satisfied' customers (Score 5/5, Apostles) are up to 6 times more loyal than merely 'Satisfied' customers (Score 4/5).\n- Level 4/5 customers reside in the vulnerable 'Zone of Defection'—they harbor no overt hostility, but will readily switch when a rival offers minor inducements.\n\n### 9.3 CX Measurement Matrix: CSAT, CES, and NPS\n1. *CSAT (Customer Satisfaction):* Evaluates immediate short-term transaction sentiment.\n2. *CES (Customer Effort Score):* Measures friction minimization ('How easy was it to get your issue resolved?'). Minimizing customer effort is the single strongest predictor of repeat loyalty.\n3. *NPS (Net Promoter Score):* Gauges relational advocacy (% Promoters minus % Detractors)."
        },
        "key_takeaways": {
            "vi": [
                "Khách hàng ở mức 'Hài lòng vừa phải' (4/5) vẫn có tỷ lệ đào tẩu rất cao; mục tiêu của CRM phải là 'Hoàn toàn Hài lòng' (5/5).",
                "Giảm bớt nỗ lực và sự phiền toái cho khách hàng (CES) là yếu tố dự báo lòng trung thành chính xác nhất."
            ],
            "en": [
                "Merely satisfied customers (4/5) defect at alarming rates; CRM must aim for complete customer delight (5/5).",
                "Friction reduction (measured by Customer Effort Score) is the most potent behavioral driver of repeat business."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b09-01",
                "question": {
                    "vi": "Tại sao khách hàng chấm điểm hài lòng 4/5 (Hài lòng) vẫn dễ dàng rời bỏ doanh nghiệp sang đối thủ? Khái niệm 'Tông đồ' (Apostles) và 'Kẻ khủng bố' (Terrorists) trong CRM có ý nghĩa gì?",
                    "en": "Why do customers rating 4/5 (Satisfied) readily defect to competitors? What do the terms 'Apostles' and 'Terrorists' represent in CRM theory?"
                },
                "model_answer": {
                    "vi": "Khách hàng 4/5 không gặp sự cố nghiêm trọng nhưng chưa có sự gắn kết cảm xúc mạnh mẽ, nên sẵn sàng chuyển đổi khi đối thủ giảm giá. 'Tông đồ' là những khách hàng cực kỳ hài lòng (5/5) chủ động đi quảng bá thương hiệu cho người khác; 'Kẻ khủng bố' là những người cực kỳ bất mãn (1/5) tích cực lan truyền thông tin tiêu cực hủy hoại uy tín công ty.",
                    "en": "Score 4/5 customers experienced acceptable service but lack emotional conviction, leaving them susceptible to competitor promotions. 'Apostles' are completely delighted fans (5/5) who actively recruit peers; 'Terrorists' are deeply aggrieved defectors (1/5) who broadcast destructive negative word-of-mouth."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 9",
            "pages": "270-295 (Book pp. 254-278)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-baran-ch10",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part III",
        "part_title": {
            "vi": "Phần III: Chiến lược Tiếp thị",
            "en": "Part III: Marketing Strategy"
        },
        "chapter_num": 10,
        "title": {
            "vi": "Chương 10: Vòng lặp Chiến lược CRM: Thu hút, Giữ chân và Giành lại Khách hàng",
            "en": "Chapter 10: The CRM Strategy Cycle: Acquisition, Retention, and Win-Back"
        },
        "pdf_page_start": 296,
        "book_page": 279,
        "learning_objectives": {
            "vi": [
                "Nắm vững 3 giai đoạn của Vòng lặp Chiến lược CRM: Thu hút (Acquisition), Giữ chân (Retention) và Giành lại (Win-Back).",
                "Phân tích các chiến thuật bán thêm (Up-selling), bán chéo (Cross-selling) và nâng cấp giá trị.",
                "Thiết lập hệ thống cảnh báo sớm dấu hiệu rời bỏ của khách hàng (Early Churn Detection).",
                "Xây dựng chiến lược giành lại khách hàng (Win-Back) dựa trên phân tích chi phí - lợi ích."
            ],
            "en": [
                "Master the three phases of the CRM Strategic Cycle: Acquisition, Retention, and Win-Back.",
                "Deploy systematic Up-selling, Cross-selling, and Customer Migration strategies.",
                "Architect Early Churn Warning systems using behavioral trigger analytics.",
                "Design evidence-based Win-Back campaigns grounded in customer lifetime profitability."
            ]
        },
        "key_concepts": [
            {
                "term": "Cross-Selling & Up-Selling",
                "name": { "vi": "Bán chéo & Bán thêm", "en": "Cross-Selling & Up-Selling" },
                "definition": {
                    "vi": "Bán chéo là việc khuyến khích khách hàng mua thêm các sản phẩm bổ trợ từ danh mục khác; Bán thêm là việc thuyết phục khách hàng nâng cấp lên phiên bản sản phẩm cao cấp hơn với biên lợi nhuận lớn hơn.",
                    "en": "Cross-selling stimulates purchases of complementary offerings across categories; Up-selling encourages customers to trade up to premium, higher-margin tiers."
                }
            },
            {
                "term": "Customer Win-Back",
                "name": { "vi": "Giành lại Khách hàng Đào tẩu (Win-Back)", "en": "Customer Win-Back" },
                "definition": {
                    "vi": "Chiến dịch tiếp thị có chủ đích nhằm thu hút trở lại những khách hàng có giá trị cao đã ngừng giao dịch, dựa trên việc khắc phục nguyên nhân gốc rễ khiến họ rời bỏ.",
                    "en": "Targeted marketing interventions to re-engage lapsed high-value customers by diagnosing and remedying the root causes of their defection."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 10.1 Vòng lặp Chiến lược CRM (The CRM Strategy Cycle)\nChiến lược CRM vận hành theo một chu trình khép kín gồm 3 giai đoạn tương hỗ:\n1. **Giai đoạn Thu hút (Customer Acquisition):** Không phải thu hút bất kỳ ai, mà là thu hút 'khách hàng phù hợp' (Right Customers) có tiềm năng sinh lời cao, bằng cách sử dụng hồ sơ khách hàng mẫu (lookalike modeling).\n2. **Giai đoạn Giữ chân & Phát triển (Customer Retention & Development):** Sau khi khách hàng gia nhập, doanh nghiệp tăng cường mức độ gắn kết bằng quy trình đón tiếp chu đáo (Onboarding), bán chéo và bán thêm để gia tăng 'tỷ phần trong ví' (Share of Wallet).\n3. **Giai đoạn Giành lại (Win-Back):** Khi khách hàng có dấu hiệu rời bỏ hoặc đã chuyển sang đối thủ, doanh nghiệp kích hoạt quy trình thu hồi.\n\n### 10.2 Quản trị Đào tẩu và Cảnh báo Sớm (Churn Management)\nKhách hàng hiếm khi rời bỏ đột ngột mà luôn để lại 'dấu vết hành vi': tần suất đăng nhập giảm, số lượng giao dịch giảm dần, thời gian thanh toán chậm lại, hoặc gửi khiếu nại chưa được giải quyết thỏa đáng. Hệ thống CRM tự động phát hiện các dấu hiệu này để gửi ưu đãi can thiệp kịp thời.\n\n### 10.3 Kinh tế học của Chiến lược Giành lại (Win-Back Economics)\nKhách hàng cũ từng giao dịch có tỷ lệ chuyển đổi khi tái tiếp thị cao gấp 3-4 lần so với một người hoàn toàn xa lạ, vì họ đã quen thuộc với sản phẩm của công ty. Tuy nhiên, doanh nghiệp chỉ nên giành lại những khách hàng có lợi nhuận (profitable defectors), và kiên quyết 'buông bỏ' những khách hàng gây lỗ kinh niên.",
            "en": "### 10.1 The Tri-Partite CRM Strategy Cycle\nCRM strategy unfolds in a continuous closed loop across three interdependent phases:\n1. **Customer Acquisition:** Targeting the 'Right Customers' with attractive projected CLV, leveraging lookalike predictive models from the best current customers.\n2. **Customer Retention & Development:** Driving deeper relationship penetration via structured onboarding workflows, cross-selling, and up-selling to maximize Share of Wallet (SOW).\n3. **Customer Win-Back:** Structured diagnostic re-engagement targeting lapsed profitable accounts.\n\n### 10.2 Predictive Churn Detection\nCustomer defection is almost never an instantaneous event; it is preceded by measurable digital breadcrumbs: declining session frequency, falling basket size, delayed invoice settlement, or unaddressed ticket escalations. Modern CRM flags these early warning signals for proactive retention interventions.\n\n### 10.3 The Economics of Win-Back\nLapsed customers represent valuable assets: they possess demonstrated product familiarity and convert at 3 to 4 times the rate of cold prospects. However, win-back investments must be rationed: companies must only reclaim profitable defectors while allowing chronic loss-makers to migrate away."
        },
        "key_takeaways": {
            "vi": [
                "Chiến lược thu hút khách hàng chỉ có ý nghĩa khi doanh nghiệp thu hút đúng đối tượng có tiềm năng gắn bó lâu dài.",
                "Khách hàng cũ từng đào tẩu có tỷ lệ chuyển đổi cao hơn nhiều so với khách hàng mới, nhưng chỉ nên giành lại nhóm khách hàng sinh lời."
            ],
            "en": [
                "Acquisition strategy succeeds only when calibrated to bring in high-LTV profiles capable of being retained.",
                "Lapsed customers convert significantly better than cold prospects, but win-back efforts must be strictly filtered by lifetime profitability."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b10-01",
                "question": {
                    "vi": "Trình bày các dấu hiệu cảnh báo sớm khách hàng có nguy cơ rời bỏ (Early Churn Indicators). Doanh nghiệp có nên nỗ lực giành lại tất cả các khách hàng đã rời bỏ hay không? Tại sao?",
                    "en": "Outline early churn warning indicators in CRM. Should a firm attempt to win back every single lapsed customer? Why or why not?"
                },
                "model_answer": {
                    "vi": "Dấu hiệu gồm: tần suất mua giảm, giảm sử dụng tính năng, số lượng phàn nàn tăng, thời gian phản hồi kéo dài. Doanh nghiệp KHÔNG nên giành lại tất cả khách hàng, mà chỉ giành lại nhóm khách hàng có giá trị sinh lời ròng (CLV > Chi phí giành lại). Việc cố giành lại nhóm khách hàng liên tục đòi hỏi chiết khấu vô lý hoặc chi phí phục vụ quá cao sẽ làm tổn hại lợi nhuận của công ty.",
                    "en": "Indicators include drop in visit frequency, shrinking transaction volumes, and unresolved grievances. A firm should NOT win back everyone—only customers with positive net projected CLV. Attempting to reclaim chronically unprofitable or abusive accounts destroys enterprise margins."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 10",
            "pages": "296-316 (Book pp. 279-298)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-baran-ch11",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part III",
        "part_title": {
            "vi": "Phần III: Chiến lược Tiếp thị",
            "en": "Part III: Marketing Strategy"
        },
        "chapter_num": 11,
        "title": {
            "vi": "Chương 11: Các Khía cạnh Quyền Riêng tư và Đạo đức trong CRM",
            "en": "Chapter 11: Privacy and Ethics Considerations"
        },
        "pdf_page_start": 317,
        "book_page": 299,
        "learning_objectives": {
            "vi": [
                "Phân tích xung đột giữa nhu cầu cá nhân hóa sâu sắc của CRM và quyền riêng tư cá nhân của người tiêu dùng.",
                "Nắm vững các khung pháp lý quốc tế về bảo vệ dữ liệu (GDPR, CCPA) và các nguyên tắc đạo đức cốt lõi.",
                "Phân biệt giữa mô hình Chọn tham gia (Opt-In) và Từ chối tham gia (Opt-Out).",
                "Thiết lập cơ chế Quản trị Dữ liệu Đạo đức (Ethical Data Governance) để ngăn ngừa xói mòn niềm tin."
            ],
            "en": [
                "Analyze the tension between CRM's personalization mandates and consumer data privacy rights.",
                "Master global regulatory privacy frameworks (GDPR, CCPA) and ethical data principles.",
                "Distinguish explicit Opt-In consent models from passive Opt-Out regimes.",
                "Establish ethical data governance safeguards to prevent consumer trust erosion."
            ]
        },
        "key_concepts": [
            {
                "term": "Opt-In vs. Opt-Out",
                "name": { "vi": "Chọn Tham gia (Opt-In) vs. Từ chối (Opt-Out)", "en": "Opt-In vs. Opt-Out" },
                "definition": {
                    "vi": "Opt-In yêu cầu sự đồng ý rõ ràng, chủ động của khách hàng trước khi thu thập hoặc sử dụng dữ liệu; Opt-Out cho phép doanh nghiệp tự động thu thập cho đến khi khách hàng chủ động từ chối.",
                    "en": "Opt-In mandates explicit affirmative prior consent before data capture; Opt-Out permits default harvesting until the consumer takes action to revoke permission."
                }
            },
            {
                "term": "Privacy by Design",
                "name": { "vi": "Thiết kế Bảo mật Quyền Riêng tư (Privacy by Design)", "en": "Privacy by Design" },
                "definition": {
                    "vi": "Nguyên tắc kỹ thuật yêu cầu tích hợp tính năng bảo vệ quyền riêng tư và ẩn danh dữ liệu vào ngay từ giai đoạn thiết kế ban đầu của hệ thống CRM chứ không phải bổ sung sau.",
                    "en": "The architectural practice of embedding privacy protections and pseudonymization directly into the foundational design of CRM software."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 11.1 Nghịch lý Quyền Riêng tư trong CRM (The Privacy Paradox)\nMột mặt, khách hàng mong muốn được phục vụ cá nhân hóa và thấu hiểu nhu cầu; mặt khác, họ cảm thấy bất an và bị xâm phạm khi phát hiện doanh nghiệp âm thầm theo dõi mọi hành vi trực tuyến và vị trí địa lý của mình.\n\n### 11.2 Các Khung Pháp lý Bảo vệ Dữ liệu Toàn cầu\n- **GDPR (Quy định Chung về Bảo vệ Dữ liệu của Châu Âu):** Đặt ra tiêu chuẩn khắt khe nhất thế giới: quyền được lãng quên (Right to be Forgotten), quyền truy cập dữ liệu, yêu cầu sự đồng ý rõ ràng (Explicit Opt-In) và mức phạt lên tới 4% doanh thu toàn cầu.\n- **CCPA (Đạo luật Quyền riêng tư của California):** Cho phép người tiêu dùng biết dữ liệu nào đang được bán và quyền yêu cầu không bán dữ liệu của mình (Do Not Sell My Info).\n\n### 11.3 Xây dựng Niềm tin qua Sự Minh bạch (Transparency)\nBaran & Galka khẳng định rằng dữ liệu là một 'khoản vay tín chấp' mà khách hàng trao cho doanh nghiệp. Khi doanh nghiệp sử dụng dữ liệu mập mờ, chia sẻ cho bên thứ ba mà không xin phép (như vụ bê bối Cambridge Analytica của Facebook), hậu quả sẽ là sự tẩy chay tức thì và phá hủy hoàn toàn thương hiệu.",
            "en": "### 11.1 The CRM Privacy Paradox\nConsumers demand frictionless, tailored personalization while simultaneously expressing mounting alarm over opaque surveillance capitalism and ubiquitous behavioral tracking.\n\n### 11.2 Global Regulatory Frameworks\n- **GDPR (European General Data Protection Regulation):** Establishes the worldwide gold standard: Right to Erasure ('Right to be Forgotten'), data portability, strict explicit Opt-In mandates, and penalties reaching 4% of global turnover.\n- **CCPA (California Consumer Privacy Act):** Guarantees transparency regarding commercial data brokers and establishes the statutory right to opt out of personal data monetization.\n\n### 11.3 Sustaining Trust Through Ethical Governance\nBaran & Galka argue that personal data is a loan of trust from the customer. When enterprises harvest data surreptitiously or traffic in covert secondary broker distribution (e.g., Cambridge Analytica), the ensuing scandal unleashes catastrophic brand erosion and regulatory fines."
        },
        "key_takeaways": {
            "vi": [
                "Niềm tin về quyền riêng tư là tài sản mong manh nhất; mất niềm tin đồng nghĩa với việc mất toàn bộ mối quan hệ khách hàng.",
                "Mô hình Opt-In chủ động và nguyên tắc 'Privacy by Design' là yêu cầu bắt buộc của các hệ thống CRM hiện đại."
            ],
            "en": [
                "Consumer privacy trust is fragile; once breached, the underlying relational contract dissolves permanently.",
                "Affirmative Opt-In consent and Privacy-by-Design architectures are mandatory standards for modern enterprise CRM."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b11-01",
                "question": {
                    "vi": "Phân biệt cơ chế Opt-In và Opt-Out trong thu thập dữ liệu khách hàng. Tại sao GDPR lại bắt buộc áp dụng cơ chế Opt-In đối với dữ liệu cá nhân?",
                    "en": "Differentiate Opt-In from Opt-Out data collection regimes. Why does GDPR mandate explicit Opt-In for personal data processing?"
                },
                "model_answer": {
                    "vi": "Opt-In đòi hỏi khách hàng phải chủ động đồng ý trước (ví dụ: tự tay tích vào ô xác nhận); Opt-Out là mặc định thu thập và khách hàng phải tìm cách hủy nếu không muốn. GDPR bắt buộc Opt-In để trả lại quyền tự quyết dữ liệu cho người tiêu dùng và ngăn chặn doanh nghiệp lạm dụng các ô tích chọn sẵn.",
                    "en": "Opt-In requires affirmative prior action (e.g. un-prechecked tick boxes); Opt-Out presumes consent until the user manually navigates opt-out friction. GDPR mandates Opt-In to enforce genuine informed consent and eliminate deceptive dark patterns."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 11",
            "pages": "317-350 (Book pp. 299-332)",
            "evidence_type": "source-derived"
        }
    },

    # --- BARAN & GALKA PART IV: CRM EVALUATION ---
    {
        "id": "mod-baran-ch12",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part IV",
        "part_title": {
            "vi": "Phần IV: Đánh giá Hiệu quả CRM",
            "en": "Part IV: CRM Evaluation"
        },
        "chapter_num": 12,
        "title": {
            "vi": "Chương 12: Đo lường Hiệu quả & Công cụ Đánh giá Chương trình CRM",
            "en": "Chapter 12: CRM Program Measurement and Tools"
        },
        "pdf_page_start": 352,
        "book_page": 333,
        "learning_objectives": {
            "vi": [
                "Nắm vững các công thức định lượng: Giá trị Vòng đời Khách hàng (CLV), Chi phí Thu hút Khách hàng (CAC), và Tỷ lệ Thu hồi Đầu tư Khách hàng (ROCI).",
                "Hiểu rõ Mô hình 3E của Doanh nghiệp: Hiệu quả (Effectiveness), Hiệu suất (Efficiency), và Đóng góp Kinh tế (Employee Engagement/Economics).",
                "Thiết lập Tháp Đo lường CRM (CRM Measurement Hierarchy) và Bảng điểm Cân bằng (CRM Balanced Scorecard).",
                "Áp dụng phân tích Kohort (Cohort Analysis) để theo dõi chất lượng các lứa khách hàng theo thời gian."
            ],
            "en": [
                "Master quantitative formulations: Customer Lifetime Value (CLV), Customer Acquisition Cost (CAC), and Return on Customer Investment (ROCI).",
                "Understand the corporate 3E Evaluation Framework: Effectiveness, Efficiency, and Economics.",
                "Construct the CRM Measurement Hierarchy and executive CRM Balanced Scorecards.",
                "Apply longitudinal Cohort Analysis to track vintage customer retention over time."
            ]
        },
        "key_concepts": [
            {
                "term": "CLV Formula",
                "name": { "vi": "Công thức Tính Giá trị Vòng đời Khách hàng (CLV)", "en": "CLV Formulation" },
                "definition": {
                    "vi": "Mô hình tính toán: CLV = ∑ [ (M_t * r_t) / (1 + d)^t ] - CAC, trong đó M_t là biên lợi nhuận kỳ t, r_t là tỷ lệ giữ chân kỳ t, d là tỷ lệ chiết khấu, và CAC là chi phí thu hút ban đầu.",
                    "en": "Mathematical equation: CLV = ∑ [ (Margin_t * Retention_t) / (1 + DiscountRate)^t ] minus CAC."
                }
            },
            {
                "term": "Return on Customer Investment (ROCI)",
                "name": { "vi": "Tỷ suất Sinh lời trên Đầu tư Khách hàng (ROCI)", "en": "Return on Customer Investment (ROCI)" },
                "definition": {
                    "vi": "Tỷ số tài chính đo lường mức độ gia tăng lợi nhuận thu được so với tổng chi phí bỏ ra để phục vụ, chăm sóc và duy trì nhóm khách hàng đó.",
                    "en": "A financial ratio measuring incremental profit generated relative to the specific capital invested in servicing and retaining that customer cohort."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 12.1 Tháp Đo lường Hiệu quả CRM (CRM Measurement Hierarchy)\nBaran & Galka xây dựng hệ thống đo lường 3 tầng:\n1. **Tầng Tác nghiệp (Operational Level):** Đo lường năng suất hàng ngày (số cuộc gọi trung bình, thời gian xử lý khiếu nại - AHT, số lượng cơ hội được tạo mới).\n2. **Tầng Quan hệ Khách hàng (Customer Level):** Đo lường mức độ gắn kết và cảm nhận (chỉ số hài lòng CSAT, NPS, tỷ lệ duy trì hợp đồng r, tỷ lệ rời bỏ churn rate).\n3. **Tầng Chiến lược & Tài chính (Executive / Financial Level):** Đo lường tác động kinh tế vĩ mô (Tăng trưởng Giá trị Tài sản Khách hàng - Customer Equity, CLV trung bình, ROCI, Tỷ lệ chi phí thu hút / giá trị trọn đời CAC:CLV).\n\n### 12.2 Tỷ lệ Vàng CAC:CLV\nTrong kinh doanh hiện đại, một hệ thống CRM hoạt động hiệu quả khi tỷ lệ CLV / CAC đạt tối thiểu **3:1** trở lên. Nếu tỷ lệ này là 1:1, doanh nghiệp đang đốt tiền không hiệu quả; nếu vượt quá 5:1, doanh nghiệp có thể đang chi tiêu quá ít cho việc mở rộng thị phần.",
            "en": "### 12.1 The CRM Measurement Hierarchy\nBaran & Galka establish a tri-level performance measurement framework:\n1. **Operational Level:** Daily activity metrics (Average Handling Time - AHT, lead velocity, calls per representative).\n2. **Customer Relationship Level:** Relational health indicators (CSAT, Net Promoter Score, retention rate r, annualized churn rate).\n3. **Executive Financial Level:** Strategic balance-sheet measures (Aggregate Customer Equity, Net Present Value CLV, ROCI, and the CAC:CLV ratio).\n\n### 12.2 The Strategic CAC:CLV Golden Ratio\nIn enterprise operations, a healthy CRM engine maintains a lifetime value to acquisition cost ratio (CLV:CAC) of at least **3:1**. A 1:1 ratio indicates catastrophic margin destruction; a ratio exceeding 5:1 indicates under-investment in growth acquisition."
        },
        "key_takeaways": {
            "vi": [
                "Đo lường CRM phải kết nối từ chỉ số tác nghiệp cơ sở lên đến chỉ số tài chính của ban điều hành.",
                "Tỷ lệ CLV:CAC từ 3:1 trở lên là thước đo chuẩn mực cho một mô hình CRM tăng trưởng bền vững."
            ],
            "en": [
                "CRM metrics must establish rigorous line-of-sight from front-line operational SLAs to executive balance-sheet equity.",
                "A CLV:CAC ratio of 3:1 or higher represents the empirical benchmark of a sustainable CRM growth engine."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b12-01",
                "question": {
                    "vi": "Giải thích ý nghĩa của tỷ lệ CLV:CAC. Nếu một doanh nghiệp có tỷ lệ CLV:CAC là 1:1 hoặc 0.8:1 thì doanh nghiệp đó đang gặp phải vấn đề chiến lược gì?",
                    "en": "Explain the significance of the CLV:CAC ratio. If an enterprise exhibits a CLV:CAC ratio of 1:1 or 0.8:1, what fundamental strategic flaw exists?"
                },
                "model_answer": {
                    "vi": "Tỷ lệ CLV:CAC phản ánh mức độ sinh lời trên mỗi đồng chi phí bỏ ra để mua khách hàng. Tỷ lệ 1:1 hoặc 0.8:1 nghĩa là chi phí thu hút khách hàng bằng hoặc lớn hơn tổng lợi nhuận khách hàng mang lại trong cả cuộc đời. Doanh nghiệp đang bị lỗ ròng trên mỗi khách hàng mới và sẽ kiệt quệ tài chính nếu tiếp tục mở rộng quy mô mà không tăng giá bán hoặc giảm chi phí thu hút.",
                    "en": "The CLV:CAC ratio measures return on acquisition capital. A 1:1 or 0.8:1 ratio means the business spends as much or more to acquire customers than they will ever return in gross profit. Scaling under these conditions accelerates insolvency unless acquisition costs are slashed or retention expansion dramatically increases."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 12",
            "pages": "352-397 (Book pp. 333-377)",
            "evidence_type": "source-derived"
        }
    },

    # --- BARAN & GALKA PART V: CRM NEW HORIZONS ---
    {
        "id": "mod-baran-ch13",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part V",
        "part_title": {
            "vi": "Phần V: Những Chân trời Mới của CRM",
            "en": "Part V: CRM New Horizons"
        },
        "chapter_num": 13,
        "title": {
            "vi": "Chương 13: Mạng Xã hội và Social CRM (SCRM)",
            "en": "Chapter 13: Social Networking and CRM"
        },
        "pdf_page_start": 398,
        "book_page": 378,
        "learning_objectives": {
            "vi": [
                "Hiểu rõ sự dịch chuyển từ CRM Truyền thống sang Social CRM (SCRM).",
                "Áp dụng công cụ Lắng nghe Mạng xã hội (Social Listening) và Phân tích Sắc thái Cảm xúc (Sentiment Analysis).",
                "Quản lý khủng hoảng truyền thông trực tuyến và bài học 'United Breaks Guitars'.",
                "Xây dựng cộng đồng thương hiệu đồng sáng tạo giá trị (Co-Creation Communities)."
            ],
            "en": [
                "Understand the paradigm shift from Traditional CRM to Social CRM (SCRM).",
                "Deploy Social Listening tools and natural language Sentiment Analysis.",
                "Navigate viral brand crises and analyze the seminal 'United Breaks Guitars' case.",
                "Build collaborative co-creation brand communities."
            ]
        },
        "key_concepts": [
            {
                "term": "Social CRM (SCRM)",
                "name": { "vi": "Social CRM (SCRM)", "en": "Social CRM (SCRM)" },
                "definition": {
                    "vi": "Triết lý và công nghệ tích hợp các kênh truyền thông xã hội vào hệ thống CRM nhằm lắng nghe, tham gia đối thoại hai chiều và giải quyết sự cố của khách hàng trong không gian công cộng.",
                    "en": "The strategic integration of social media channels into CRM to listen, engage in bidirectional dialogues, and resolve customer issues in public social spaces."
                }
            },
            {
                "term": "Social Listening",
                "name": { "vi": "Lắng nghe Mạng Xã hội (Social Listening)", "en": "Social Listening" },
                "definition": {
                    "vi": "Quá trình tự động quét, theo dõi và phân tích các bài đăng, bình luận trên mạng xã hội liên quan đến thương hiệu để phát hiện sớm các khủng hoảng tiềm ẩn.",
                    "en": "Automated crawling and semantic monitoring of digital social conversations mentioning brand terms to detect sentiment shifts and nascent PR crises."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 13.1 Từ CRM Truyền thống sang Social CRM\nTrong CRM truyền thống, doanh nghiệp nắm quyền kiểm soát kênh giao tiếp (thoại, email, trực tiếp tại cửa hàng). Khách hàng phàn nàn một-đối-một trong vòng bí mật. Trong kỷ nguyên mạng xã hội (Social CRM), cán cân quyền lực đã đảo chiều hoàn toàn: khách hàng nói chuyện với nhau (Peer-to-Peer), và một lời phàn nàn công khai có thể lan truyền theo cấp số nhân.\n\n### 13.2 Bài học 'United Breaks Guitars'\nBaran & Galka nhắc lại trường hợp kinh điển của nhạc sĩ Dave Carroll khi cây đàn guitar của anh bị nhân viên United Airlines làm hỏng. Sau nhiều tháng bị tổng đài từ chối bồi thường, anh đã sáng tác bài hát 'United Breaks Guitars' tải lên YouTube, thu hút hàng triệu lượt xem và khiến giá cổ phiếu của hãng bay bốc hơi hàng chục triệu USD trong vài ngày. Đây là minh chứng rõ nét cho thấy một cá nhân có thể 'bắt giữ thương hiệu làm con tin' nếu doanh nghiệp thiếu hệ thống Social CRM phản hồi nhanh nhạy.",
            "en": "### 13.1 Shifting Power Dynamics: Traditional CRM to Social CRM\nUnder traditional CRM, corporations maintained an asymmetric monopoly on communication channels (toll-free lines, direct mail). Aggrieved customers complained in private one-on-one silos. Social CRM represents an inversion of power: consumers communicate horizontally (Peer-to-Peer), and a single unsatisfied customer can ignite viral public outrage.\n\n### 13.2 The 'United Breaks Guitars' Paradigm\nBaran & Galka examine the seminal case of musician Dave Carroll, whose instrument was destroyed by United Airlines ground handlers. Stonewalled by bureaucratic call center scripts for nine months, Carroll published a humorous YouTube music video that accumulated millions of views, inflicting tens of millions of dollars in market cap damage within days. The incident proved that in the Social CRM era, unresponsive customer support poses an existential brand hazard."
        },
        "key_takeaways": {
            "vi": [
                "Trong kỷ nguyên Social CRM, dịch vụ khách hàng không còn là cuộc đối thoại riêng tư mà là buổi trình diễn công khai.",
                "Lắng nghe mạng xã hội là công cụ phòng vệ sống còn để dập tắt khủng hoảng từ lúc mới manh nha."
            ],
            "en": [
                "In Social CRM, customer support is no longer a private exchange, but a public performance.",
                "Social listening is an indispensable defensive sensor to intercept customer grievances before viral escalation."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b13-01",
                "question": {
                    "vi": "Social CRM khác với CRM truyền thống ở những điểm căn bản nào? Vụ việc 'United Breaks Guitars' mang lại bài học gì cho các nhà quản trị dịch vụ khách hàng?",
                    "en": "How does Social CRM fundamentally differ from Traditional CRM? What lessons does 'United Breaks Guitars' impart to customer service executives?"
                },
                "model_answer": {
                    "vi": "Khác biệt lớn nhất: CRM truyền thống là giao tiếp 1-1 khép kín do công ty kiểm soát; Social CRM là tương tác công khai đa chiều do khách hàng dẫn dắt. Bài học từ United Airlines: Không được dùng quy trình máy móc để chối bỏ trách nhiệm với khách hàng, và phải giải quyết khiếu nại ngay từ điểm chạm đầu tiên trước khi nó biến thành khủng hoảng truyền thông.",
                    "en": "Traditional CRM is closed, asymmetric, and firm-controlled; Social CRM is transparent, networked, and consumer-led. The United lesson: bureaucratic script-following inflames customer fury, and complaints must be empowered with rapid first-contact resolution before they metastasize into viral PR disasters."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 13",
            "pages": "398-430 (Book pp. 378-409)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-baran-ch14",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part V",
        "part_title": {
            "vi": "Phần V: Những Chân trời Mới của CRM",
            "en": "Part V: CRM New Horizons"
        },
        "chapter_num": 14,
        "title": {
            "vi": "Chương 14: Xu hướng, Thách thức và Cơ hội Mới của CRM",
            "en": "Chapter 14: CRM Trends, Challenges, and Opportunities"
        },
        "pdf_page_start": 431,
        "book_page": 410,
        "learning_objectives": {
            "vi": [
                "Khám phá các xu hướng công nghệ tiên phong: Trí tuệ Nhân tạo (AI), Học máy (Machine Learning), và Internet Vạn vật (IoT) trong CRM.",
                "Hiểu rõ khái niệm Phygital - sự xóa nhòa ranh giới giữa trải nghiệm thực tế và kỹ thuật số.",
                "Giải quyết thách thức quản trị dữ liệu lớn (Big Data: Volume, Velocity, Variety).",
                "Định hình tương lai của Quản trị Trải nghiệm Khách hàng (Customer Experience Management - CEM/CX)."
            ],
            "en": [
                "Explore vanguard technological frontiers: Artificial Intelligence (AI), Machine Learning, and IoT in CRM.",
                "Understand Phygital convergence—blurring boundaries between physical and digital touchpoints.",
                "Solve Big Data velocity, volume, and variety governance challenges in customer analytics.",
                "Anticipate the evolution from transactional CRM to predictive Customer Experience Management (CXM)."
            ]
        },
        "key_concepts": [
            {
                "term": "Phygital Experience",
                "name": { "vi": "Trải nghiệm Phygital (Vật lý - Kỹ thuật số)", "en": "Phygital Experience" },
                "definition": {
                    "vi": "Sự kết hợp liền mạch giữa không gian vật lý (Physical) và công nghệ số (Digital) nhằm mang lại trải nghiệm tiện lợi, trực quan và không ma sát cho người tiêu dùng.",
                    "en": "The seamless fusion of physical retail environments with digital capabilities (mobile apps, IoT sensors, AR) to deliver frictionless consumer journeys."
                }
            },
            {
                "term": "Predictive CRM & AI",
                "name": { "vi": "CRM Dự đoán & Trí tuệ Nhân tạo", "en": "Predictive CRM & AI" },
                "definition": {
                    "vi": "Ứng dụng các thuật toán máy học để tự động dự báo nhu cầu tiếp theo của khách hàng (Next Best Action) và tự động hóa tương tác qua trợ lý ảo thông minh.",
                    "en": "Deploying machine learning models to anticipate customer intent, recommend Next Best Actions, and automate conversational service interactions."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 14.1 Làn sóng Trí tuệ Nhân tạo & Tự động hóa Thông minh\nCRM tương lai chuyển dịch từ việc 'ghi nhận lịch sử' sang 'dự đoán tương lai'. Nhờ các thuật toán học máy, CRM có thể gợi ý cho nhân viên bán hàng: 'Hôm nay nên gọi điện cho khách hàng nào, chào bán sản phẩm gì, và với mức giá nào thì xác suất thành công cao nhất' (Next Best Action / Next Best Offer).\n\n### 14.2 Xu hướng Phygital và IoT\nSự bùng nổ của các thiết bị thông minh kết nối mạng (Internet of Things - IoT) cho phép sản phẩm tự động giao tiếp với CRM. Ví dụ: Máy giặt thông minh tự phát hiện lỗi linh kiện và tự động gửi yêu cầu bảo dưỡng về hệ thống CRM của nhà sản xuất trước khi khách hàng nhận ra sự cố.\n\n### 14.3 Từ CRM sang CEM/CX (Customer Experience Management)\nCông nghệ CRM không còn bị đóng khung trong phòng kinh doanh hay marketing mà trở thành nền tảng thiết kế toàn bộ Hành trình Khách hàng (Customer Journey Mapping), từ lúc khách hàng nảy sinh nhận thức cho đến mọi điểm chạm hậu mãi.",
            "en": "### 14.1 Artificial Intelligence and Predictive Next-Best-Action\nCRM is undergoing an epochal transformation from descriptive record-keeping into predictive behavioral anticipation. Machine learning engines ingest real-time contextual signals to prompt sales agents with dynamic 'Next Best Actions' and calibrated pricing models.\n\n### 14.2 The Phygital Frontier and IoT Integration\nThe explosion of Internet of Things (IoT) sensors enables physical assets to communicate autonomously with CRM backends. Connected appliances diagnose component wear and automatically generate proactive dispatch tickets before the consumer experiences a breakdown.\n\n### 14.3 Evolution from CRM to Holistic CXM\nCRM has expanded beyond sales automation into enterprise-wide Customer Experience Management (CXM), orchestrating every micro-moment across omni-channel customer journey lifecycles."
        },
        "key_takeaways": {
            "vi": [
                "Tương lai của CRM là chuyển từ phản ứng thụ động sang chủ động dự báo bằng AI và IoT.",
                "Phygital là chìa khóa để các nhà bán lẻ truyền thống đánh bại các đối thủ thương mại điện tử thuần túy."
            ],
            "en": [
                "The frontier of CRM lies in transitioning from reactive logging to autonomous, AI-driven predictive intervention.",
                "Phygital convergence enables brick-and-mortar operators to outmaneuver pure-play digital commerce."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b14-01",
                "question": {
                    "vi": "Trình bày khái niệm 'Trải nghiệm Phygital' và 'Hành động Tối ưu Tiếp theo' (Next Best Action) trong CRM hiện đại. Cho ví dụ thực tế.",
                    "en": "Explain 'Phygital Experience' and 'Next Best Action' in contemporary CRM. Provide real-world examples."
                },
                "model_answer": {
                    "vi": "Phygital là kết hợp vật lý và số (ví dụ: Nike House of Innovation cho phép quét giày trong cửa hàng để nhận kích cỡ mang đến phòng thử đồ qua app). Next Best Action là thuật toán AI gợi ý bước đi tiếp theo (ví dụ: hệ thống CRM của ngân hàng phát hiện khách hàng vừa bán nhà và tự động nhắc chuyên viên tư vấn gọi điện đề xuất gói gửi tiết kiệm sinh lời cao).",
                    "en": "Phygital merges physical with digital (e.g. Nike House of Innovation where shoppers scan footwear via app for instant fitting room delivery). Next Best Action is an AI prompt (e.g. a bank CRM detects a mortgage settlement and prompts the advisor to offer wealth management solutions)."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 14",
            "pages": "431-451 (Book pp. 410-430)",
            "evidence_type": "source-derived"
        }
    },

    # --- KOSTOJOHN ET AL. CHAPTERS 5 - 7 ---
    {
        "id": "mod-fund-ch05",
        "book_id": "TB-KOSTOJOHN-2011",
        "book_title": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
        "chapter_num": 5,
        "title": {
            "vi": "Chương 5: Lập Kế hoạch Triển khai Dự án CRM Ban đầu",
            "en": "Chapter 5: Planning the Initial CRM Implementation"
        },
        "pdf_page_start": 105,
        "book_page": 91,
        "learning_objectives": {
            "vi": [
                "Thiết lập cấu trúc quản trị dự án CRM chuyên nghiệp (Project Governance Framework).",
                "So sánh phương pháp quản lý dự án Thác nước (Waterfall) và Linh hoạt (Agile) trong bối cảnh CRM.",
                "Xác định và kiểm soát phạm vi dự án (Scoping & Work Breakdown Structure).",
                "Lập ngân sách dự án, quản trị rủi ro và xây dựng kế hoạch truyền thông nội bộ."
            ],
            "en": [
                "Establish an enterprise CRM Project Governance Framework.",
                "Evaluate Waterfall vs. Agile implementation methodologies for CRM systems.",
                "Define and defend project scope boundaries via Work Breakdown Structures (WBS).",
                "Manage project budgeting, contingency reserves, and internal communication plans."
            ]
        },
        "key_concepts": [
            {
                "term": "Project Scope Creep",
                "name": { "vi": "Phình to Phạm vi Dự án (Scope Creep)", "en": "Scope Creep" },
                "definition": {
                    "vi": "Hiện tượng các yêu cầu tính năng mới liên tục được bổ sung vào dự án mà không có sự điều chỉnh tương ứng về ngân sách, thời gian hoặc tài nguyên.",
                    "en": "The uncontrolled growth or addition of new project features without proportional adjustments to budget, time, or technical resources."
                }
            },
            {
                "term": "Agile vs. Waterfall in CRM",
                "name": { "vi": "Agile vs. Thác nước trong Triển khai CRM", "en": "Agile vs. Waterfall in CRM" },
                "definition": {
                    "vi": "Thác nước lập kế hoạch tuần tự khắt khe từ đầu đến cuối; Agile chia nhỏ thành các chu kỳ chạy nước rút (sprints 2-4 tuần) cho phép người dùng trải nghiệm và phản hồi liên tục.",
                    "en": "Waterfall enforces linear, stage-gated sequences; Agile deploys 2- to 4-week iterative sprints enabling continuous user validation and configuration flexibility."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 5.1 Lập Kế hoạch Dự án CRM - Nền móng Quyết định\nKostojohn et al. nhấn mạnh: 'Nếu bạn thất bại trong việc lập kế hoạch, bạn đang lên kế hoạch cho sự thất bại'. Một kế hoạch triển khai CRM phải làm rõ 4 câu hỏi cơ bản: Chúng ta đang xây dựng cái gì? Ai sẽ làm? Mất bao lâu? Và tốn bao nhiêu chi phí?\n\n### 5.2 Lựa chọn Phương pháp Luận: Waterfall vs. Agile\n- **Phương pháp Thác nước (Waterfall):** Yêu cầu chốt 100% tài liệu phân tích nghiệp vụ (BRD) trước khi lập trình. Phù hợp với các dự án có phạm vi cố định, ít thay đổi và yêu cầu kiểm toán nghiêm ngặt.\n- **Phương pháp Linh hoạt (Agile):** Chia dự án thành các đợt chạy nước rút (Sprints). Người dùng được nhìn thấy giao diện và dùng thử sau mỗi 2-3 tuần. Phù hợp với CRM vì người dùng chỉ thực sự hiểu họ cần gì khi được trực tiếp thao tác trên màn hình.\n- **Mô hình Lai (Hybrid):** Lập kế hoạch tổng thể theo Waterfall nhưng thiết kế và phát triển chi tiết theo Agile.\n\n### 5.3 Quản trị Rủi ro và Ngăn ngừa Phình to Phạm vi (Scope Creep)\nNguyên nhân hàng đầu khiến dự án CRM vượt ngân sách là do các phòng ban liên tục đòi hỏi thêm các tính năng 'đẹp mắt nhưng không thiết yếu'. Ban chỉ đạo phải thiết lập quy trình kiểm soát thay đổi (Change Control Board - CCB): mọi yêu cầu bổ sung phải được lượng hóa chi phí và hoãn sang Giai đoạn 2 nếu không nằm trong phạm vi bắt buộc của Giai đoạn 1.",
            "en": "### 5.1 Project Planning as the Critical Foundation\nKostojohn et al. stress: rigorous planning establishes the architectural guardrails for implementation. A sound plan provides definitive clarity on scope, team allocation, timeline milestones, and capital budgets.\n\n### 5.2 Methodological Choices: Waterfall vs. Agile vs. Hybrid\n- **Waterfall:** Demands exhaustive upfront Business Requirements Documents (BRD). Beneficial for fixed-cost, rigid regulatory integrations, but vulnerable to late-stage discovery shocks.\n- **Agile:** Iterates via 2- to 4-week Sprints. Highly recommended for CRM because business users rarely articulate exact field configurations until they physically interact with prototype screens.\n- **Hybrid:** Employs Waterfall stage-gates for budget governance and architecture, while executing sprint iterations for functional configuration.\n\n### 5.3 Mitigating Scope Creep\nThe primary culprit behind CRM budget blowouts is uncontrolled scope creep—stakeholders demanding peripheral enhancements mid-flight. The project must establish a Change Control Board (CCB): non-critical requests are formally ticketed and deferred to Phase 2 backlog releases."
        },
        "key_takeaways": {
            "vi": [
                "Phương pháp lai (Hybrid Agile) là cách tiếp cận lý tưởng nhất cho triển khai CRM hiện đại.",
                "Quy trình kiểm soát thay đổi (Change Control) nghiêm ngặt là rào chắn bắt buộc để bảo vệ ngân sách dự án."
            ],
            "en": [
                "A Hybrid Agile delivery model strikes the optimal balance between budgetary governance and user-experience flexibility.",
                "A formal Change Control Board is mandatory to defend project budgets against fatal scope creep."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-f05-01",
                "question": {
                    "vi": "Tại sao các dự án CRM áp dụng phương pháp Agile thường có tỷ lệ chấp nhận của người dùng (User Adoption) cao hơn phương pháp Waterfall thuần túy?",
                    "en": "Why do CRM projects employing Agile methodologies routinely achieve superior user adoption compared to pure Waterfall?"
                },
                "model_answer": {
                    "vi": "Bởi vì trong Agile, người dùng cuối được xem các bản mẫu (prototypes) và phản hồi sau mỗi 2-3 tuần, giúp phát hiện và sửa các điểm bất hợp lý trên giao diện ngay lập tức. Trong Waterfall, người dùng phải chờ 6-12 tháng mới được thấy hệ thống, lúc đó nếu giao diện khó dùng thì chi phí sửa đổi đã quá đắt đỏ.",
                    "en": "Agile exposes end-users to functional prototypes every 2-3 weeks, enabling real-time ergonomic feedback and co-ownership. Under Waterfall, users only see the system after 6-12 months of development, by which time UI remedies are prohibitively expensive."
                }
            }
        ],
        "source": {
            "document": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
            "chapter": "Chapter 5",
            "pages": "105-141 (Book pp. 91-126)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-fund-ch06",
        "book_id": "TB-KOSTOJOHN-2011",
        "book_title": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
        "chapter_num": 6,
        "title": {
            "vi": "Chương 6: Thực thi Triển khai Dự án CRM Ban đầu",
            "en": "Chapter 6: Executing the Initial CRM Implementation"
        },
        "pdf_page_start": 142,
        "book_page": 127,
        "learning_objectives": {
            "vi": [
                "Nắm vững các giai đoạn thực thi kỹ thuật: Thiết kế, Phát triển Tùy biến, Tích hợp Hệ thống.",
                "Quản lý quy trình Chuyển đổi và Làm sạch Dữ liệu (Data Migration & Cleansing).",
                "Tổ chức 4 cấp độ kiểm thử hệ thống: Unit Testing, System Testing, UAT, và Performance Testing.",
                "Lập kế hoạch chuyển giao (Cutover), Đào tạo người dùng cuối và Vận hành Go-Live an toàn."
            ],
            "en": [
                "Master core execution phases: Functional Design, Customization, and System Integration.",
                "Govern Data Cleansing and Migration pipelines without corrupting production targets.",
                "Architect 4 rigorous testing tiers: Unit Testing, System Testing, UAT, and Performance Testing.",
                "Orchestrate cutover readiness, end-user training curricula, and Go-Live support war-rooms."
            ]
        },
        "key_concepts": [
            {
                "term": "User Acceptance Testing (UAT)",
                "name": { "vi": "Kiểm thử Chấp nhận của Người dùng (UAT)", "en": "User Acceptance Testing (UAT)" },
                "definition": {
                    "vi": "Giai đoạn kiểm thử then chốt trong đó những người dùng thực tế từ các phòng ban nghiệp vụ trực tiếp thao tác các kịch bản công việc hàng ngày để xác nhận hệ thống hoạt động đúng kỳ vọng trước khi Go-Live.",
                    "en": "The definitive testing milestone where actual departmental business users execute real-world scenarios to validate that the CRM meets business requirements prior to Go-Live."
                }
            },
            {
                "term": "Data Migration Strategy",
                "name": { "vi": "Chiến lược Chuyển đổi Dữ liệu", "en": "Data Migration Strategy" },
                "definition": {
                    "vi": "Quy trình trích xuất dữ liệu từ các hệ thống cũ, làm sạch, ánh xạ trường thông tin (field mapping) và nạp vào hệ thống CRM mới. Kostojohn khuyên chỉ nên di chuyển dữ liệu đang hoạt động (active data) thay vì chuyển toàn bộ dữ liệu rác lịch sử.",
                    "en": "The disciplined pipeline of extracting, cleansing, mapping, and loading legacy records into the new CRM. Authors advise strictly limiting migration to active records."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 6.1 Bẫy Phát triển Tùy biến (Custom Development)\nKostojohn et al. khuyến cáo nguyên tắc vàng: 'Cấu hình trước, Lập trình sau' (Configuration over Customization). Việc viết mã lập trình tùy biến quá nhiều (custom code) làm tăng rủi ro lỗi phần mềm và gây khó khăn cho việc nâng cấp phiên bản sau này. Chỉ viết code khi tính năng đó mang lại lợi thế cạnh tranh cốt lõi mà cấu hình có sẵn không thể đáp ứng.\n\n### 6.2 Chuyển đổi Dữ liệu (Data Migration) - Nhiệm vụ Khó khăn Nhất\nChuyển đổi dữ liệu luôn tốn nhiều thời gian và chi phí hơn dự kiến. Quy tắc quan trọng:\n- Không mang rác từ nhà cũ sang nhà mới: Lọc bỏ các khách hàng đã ngừng hoạt động hơn 5 năm.\n- Ánh xạ trường dữ liệu (Field Mapping) chi tiết từng cột giữa cơ sở dữ liệu cũ và mới.\n- Thực hiện chạy thử nghiệm chuyển đổi (Dry Runs) ít nhất 2-3 lần trước ngày chuyển giao chính thức.\n\n### 6.3 Bốn Cấp độ Kiểm thử Bắt buộc\n1. *Unit Testing:* Lập trình viên kiểm tra từng tính năng đơn lẻ.\n2. *System Integration Testing (SIT):* Kiểm tra dòng luân chuyển dữ liệu giữa CRM và ERP/Billing.\n3. *User Acceptance Testing (UAT):* Người dùng nghiệp vụ kiểm tra theo kịch bản thực tế. Đây là mốc quyết định xem hệ thống đã sẵn sàng Go-Live hay chưa.\n4. *Performance/Load Testing:* Kiểm tra khả năng chịu tải khi hàng nghìn nhân viên đăng nhập cùng lúc vào giờ cao điểm.\n\n### 6.4 Kế hoạch Chuyển giao (Cutover) & Đào tạo\nLên kế hoạch chi tiết từng giờ cho cuối tuần chuyển giao (Cutover Weekend), thiết lập phòng điều hành trực chiến (War Room) và cử các Đại sứ CRM hỗ trợ nhân viên ngay tại bàn làm việc trong 2 tuần đầu Go-Live.",
            "en": "### 6.1 The Custom Development Dilemma\nKostojohn et al. mandate the golden maxim: 'Configure before Customize.' Heavy custom code introduces technical debt, escalates defect rates, and imperils future platform upgrades. Custom code must be quarantined exclusively for unique competitive differentiators.\n\n### 6.2 Data Migration: The Unforgiving Challenge\nData migration is notoriously underestimated in cost and schedule. Best practices:\n- Never migrate legacy debris into the new platform: prune records inactive for over 3-5 years.\n- Detailed field-level mapping dictionaries matching source columns to destination schema.\n- Execute at least 2 to 3 mock migration dry-runs to validate data integrity and benchmark run-times.\n\n### 6.3 The Four Essential Testing Tiers\n1. *Unit Testing:* Developers validate isolated modules and workflows.\n2. *System Integration Testing (SIT):* Asserts data flow integrity between CRM and back-office ERP/finance.\n3. *User Acceptance Testing (UAT):* Business users execute scripted end-to-end work tasks. Serves as the ultimate go/no-go quality gate.\n4. *Performance & Load Testing:* Asserts sub-second latency under concurrent peak-user loads.\n\n### 6.4 Cutover Orchestration and Go-Live Support\nMinute-by-minute scheduling across Cutover Weekend, an active Go-Live War Room, and elbow-to-elbow floor support provided by Departmental Champions throughout the initial 14-day operational stabilization."
        },
        "key_takeaways": {
            "vi": [
                "Ưu tiên Cấu hình hơn Tùy biến (Configuration over Customization) để bảo vệ tính ổn định của hệ thống.",
                "UAT là chốt chặn chất lượng quan trọng nhất; không bao giờ Go-Live nếu chưa đạt nghiệm thu UAT."
            ],
            "en": [
                "Prioritize Configuration over Customization to preserve upgradeability and system resilience.",
                "UAT is the definitive go/no-go quality gate; never launch into production without formal business user sign-off."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-f06-01",
                "question": {
                    "vi": "Tại sao Kostojohn et al. khuyên doanh nghiệp nên hạn chế di chuyển toàn bộ dữ liệu lịch sử cũ sang hệ thống CRM mới? Các bước thực hiện Data Migration an toàn là gì?",
                    "en": "Why do Kostojohn et al. recommend restricting historical data migration to the new CRM? What are the key steps for safe data migration?"
                },
                "model_answer": {
                    "vi": "Di chuyển toàn bộ dữ liệu cũ sẽ làm ô nhiễm hệ thống mới bằng dữ liệu rác, tốn kém chi phí lưu trữ và làm chậm hệ thống. Các bước an toàn: (1) Lọc bỏ dữ liệu chết, (2) Làm sạch dữ liệu nguồn, (3) Lập bảng ánh xạ trường thông tin, (4) Chạy thử nghiệm di chuyển (dry runs) nhiều lần, và (5) Đối chiếu kiểm toán số lượng bản ghi sau khi nạp chính thức.",
                    "en": "Migrating exhaustive history pollutes the clean CRM with obsolete duplicates, inflates storage, and slows performance. Safe steps: (1) Scope to active accounts, (2) Clean source records, (3) Detailed field mapping, (4) Multiple mock dry-runs, and (5) Systematic pre- and post-load record reconciliation audits."
                }
            }
        ],
        "source": {
            "document": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
            "chapter": "Chapter 6",
            "pages": "142-207 (Book pp. 127-192)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-fund-ch07",
        "book_id": "TB-KOSTOJOHN-2011",
        "book_title": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
        "part_num": "Part II",
        "part_title": {
            "vi": "Phần II: Vận hành & Phát triển CRM",
            "en": "Part II: CRM Operations and Evolution"
        },
        "chapter_num": 7,
        "title": {
            "vi": "Chương 7: Duy trì và Phát triển Hệ thống CRM (Maintaining and Evolving CRM)",
            "en": "Chapter 7: Maintaining and Evolving CRM"
        },
        "pdf_page_start": 208,
        "book_page": 193,
        "learning_objectives": {
            "vi": [
                "Duy trì vai trò và nhịp họp định kỳ của Ban Chỉ đạo Dự án (Steering Committee) sau Go-Live.",
                "Phân biệt rõ ràng giữa hoạt động Bảo trì thường nhật (Maintenance) và Hoạt động Nâng cấp (Enhancement).",
                "Đo lường mức độ chấp nhận thực tế của người dùng (User Adoption Metrics).",
                "Theo dõi hệ sinh thái nhà cung cấp (Vendor Ecosystem) và quản lý các đợt phát hành phiên bản tiếp theo."
            ],
            "en": [
                "Sustain Steering Committee governance cadence and oversight post-launch.",
                "Disentangle day-to-day Maintenance operations from strategic Release Enhancements.",
                "Measure authentic User Adoption metrics to preempt system abandonment.",
                "Monitor partner vendor ecosystems and govern multi-year roadmap evolutions."
            ]
        },
        "key_concepts": [
            {
                "term": "User Adoption Metrics",
                "name": { "vi": "Chỉ số Chấp nhận của Người dùng (Adoption Metrics)", "en": "User Adoption Metrics" },
                "definition": {
                    "vi": "Các thước đo khách quan phản ánh mức độ sử dụng CRM thực tế của nhân viên: tần suất đăng nhập hàng ngày, số bản ghi mới được tạo, tỷ lệ điền đầy đủ thông tin trường, và khối lượng giao dịch được xử lý qua hệ thống.",
                    "en": "Objective telemetry measuring actual software usage: daily active users (DAU), records created, profile completeness, and pipeline updates."
                }
            },
            {
                "term": "Maintenance vs. Enhancement",
                "name": { "vi": "Bảo trì vs. Nâng cấp Hệ thống", "en": "Maintenance vs. Enhancement" },
                "definition": {
                    "vi": "Bảo trì là các hoạt động duy trì hệ thống chạy ổn định (sửa lỗi, sao lưu, hỗ trợ người dùng, cấp quyền); Nâng cấp là việc phát triển các tính năng nghiệp vụ mới giúp mở rộng năng lực kinh doanh.",
                    "en": "Maintenance ensures operational stability (bug fixes, backups, helpdesk, provisioning); Enhancement delivers new business functionality expanding enterprise capabilities."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 7.1 Go-Live Chỉ là Điểm Khởi đầu\nNhiều tổ chức mắc sai lầm nghiêm trọng khi giải tán Ban chỉ đạo và cắt giảm nhân sự ngay sau ngày Go-Live. Kostojohn et al. nhấn mạnh: 'Go-Live không phải là vạch đích của dự án, mà là phát súng mở màn cho hành trình CRM thực sự'.\n\n### 7.2 Đo lường Sự Chấp nhận của Người dùng (User Adoption)\nNhân viên bán hàng thường tìm cách 'lách luật' (ví dụ: chỉ đăng nhập một lần vào cuối tuần để nhập đối phó vài thông tin cơ bản). Đội ngũ quản trị phải theo dõi các chỉ số đo lường thực tế:\n- Tần suất đăng nhập và thời gian hoạt động trên hệ thống.\n- Tỷ lệ các trường thông tin quan trọng bị bỏ trống.\n- Sự gia tăng đột ngột của các 'bản ghi rác'.\nLãnh đạo cần đưa việc sử dụng CRM vào tiêu chí đánh giá hiệu quả công việc chính thức (KPI).\n\n### 7.3 Quản lý Nâng cấp và Hệ sinh thái Nhà cung cấp\nMột hệ thống CRM phát triển lành mạnh phải có chu kỳ phát hành nâng cấp định kỳ (mỗi 3-6 tháng một bản phát hành mới). Đồng thời, doanh nghiệp phải liên tục theo dõi hệ sinh thái của nhà cung cấp phần mềm (AppExchange, Marketplace) để bổ sung các tiện ích mở rộng (như tổng đài ảo CTI, ký hợp đồng điện tử) thay vì tự lập trình tốn kém.",
            "en": "### 7.1 Go-Live is the Starting Line, Not the Finish\nOrganizations frequently commit the fatal error of disbanding governance teams immediately after Go-Live. Kostojohn et al. stress: Go-Live is not the conclusion of the effort, but the birth of the active operational CRM journey.\n\n### 7.2 Auditing Real User Adoption\nSales reps notoriously attempt workarounds (e.g., logging in once weekly to dump minimal records). Administrators must monitor systemic adoption telemetry:\n- Daily Active Users (DAU) and session duration.\n- Mandatory field completeness ratios.\n- Transaction volume processed through the CRM rather than rogue spreadsheets.\nSystem utilization must be codified into formal employee performance appraisals.\n\n### 7.3 Managing Releases and the Vendor Ecosystem\nA mature CRM program establishes predictable release cycles (e.g. quarterly feature drops). Enterprises must monitor the vendor marketplace (e.g. Salesforce AppExchange, Microsoft AppSource) to license vetted plug-ins (e.g., CTI telephony, e-signatures) rather than engineering costly bespoke code."
        },
        "key_takeaways": {
            "vi": [
                "Go-Live là điểm khởi đầu; thành công bền vững phụ thuộc vào việc đo lường sự chấp nhận của người dùng và duy trì Ban chỉ đạo.",
                "Tận dụng hệ sinh thái ứng dụng có sẵn của nhà cung cấp giúp tiết kiệm chi phí phát triển tính năng mới."
            ],
            "en": [
                "Go-Live is the inception; enduring value requires relentless adoption tracking and sustained Steering Committee governance.",
                "Leverage the vendor app marketplace ecosystem to source pre-built extensions rather than reinventing the wheel."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-f07-01",
                "question": {
                    "vi": "Tại sao việc duy trì Ban Chỉ đạo (Steering Committee) sau ngày Go-Live lại có tính chất quyết định đến sự tiến hóa của hệ thống CRM?",
                    "en": "Why is sustaining the Steering Committee post-Go-Live decisive for the ongoing evolution of the CRM system?"
                },
                "model_answer": {
                    "vi": "Sau Go-Live, người dùng sẽ gửi về hàng trăm yêu cầu thay đổi và tính năng mới. Nếu không có Ban Chỉ đạo, đội ngũ kỹ thuật sẽ bị quá tải, ngân sách bị phân tán vào các việc vụn vặt và hệ thống sẽ dần bị thoái hóa. Ban Chỉ đạo giữ vai trò 'người gác cổng' định hướng chiến lược, phân loại ưu tiên cho các đợt phát hành tiếp theo.",
                    "en": "Post-launch brings an avalanche of user enhancement requests. Without the Steering Committee acting as strategic gatekeeper, developers become overwhelmed, budgets fragment into trivial tweaks, and the platform decays. The committee evaluates business cases and prioritizes the multi-year release roadmap."
                }
            }
        ],
        "source": {
            "document": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
            "chapter": "Chapter 7",
            "pages": "208-235 (Book pp. 193-220)",
            "evidence_type": "source-derived"
        }
    }
]

for ch in new_chapters:
    if ch["id"] not in existing_ids:
        curr.append(ch)
        existing_ids.add(ch["id"])

def sort_key(c):
    book_order = 0 if c["book_id"] == "TB-BARAN-2017" else 1
    return (book_order, c["chapter_num"])

curr.sort(key=sort_key)
curr_file.write_text(json.dumps(curr, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"All chapters successfully written to curriculum.json! Total chapters: {len(curr)}")
