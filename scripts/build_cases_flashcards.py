import json
from pathlib import Path

data_dir = Path(r"C:\Kiến thức cần học\CRM\output\data")

# 1. FLASHCARDS
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
            "vi": "Theo Kostojohn et al., ba yếu tố trong bộ ba thành công của CRM là gì? Yếu tố nào chiếm tỷ trọng quyết định cao nhất?",
            "en": "According to Kostojohn et al., what are the three pillars of CRM success? Which pillar drives the highest percentage of outcome?"
        },
        "back": {
            "vi": "Bộ ba: Con người (People), Quy trình (Process), và Công nghệ (Technology).\nCon người và Quy trình chiếm 80% quyết định thành công; Công nghệ chỉ đóng góp khoảng 20%.",
            "en": "The triad: People, Process, and Technology.\nPeople and Process account for ~80% of project success; Technology accounts for only ~20%."
        },
        "hint": {
            "vi": "Công nghệ không thể cứu vãn một quy trình lộn xộn hoặc tổ chức thiếu văn hóa chia sẻ dữ liệu.",
            "en": "Technology cannot fix broken operating processes or poor cultural buy-in."
        },
        "difficulty": "easy",
        "tags": ["implementation", "kostojohn-ch2"],
        "source": { "document": "Kostojohn et al. (2011) pp. 24-25" }
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
    }
]

(data_dir / "flashcards.json").write_text(json.dumps(flashcards, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Generated flashcards.json with {len(flashcards)} validated cards.")

# 2. BUSINESS CASES (All 10 Enterprise Cases)
cases = [
    {
        "case_id": "CASE-TESCO-01",
        "company": "Tesco PLC",
        "title": {
            "vi": "Tình huống 1: Định hướng Khách hàng tại Tesco & Cuộc cách mạng Thẻ Clubcard",
            "en": "Case 1: Customer Orientation at Tesco & The Clubcard Loyalty Revolution"
        },
        "industry": "Grocery Retail & Supermarket, E-Commerce, Financial Services",
        "source_reference": {
            "document": "Customer Relationship Management (Raab et al.)",
            "chapter": "Case Study 5",
            "pages": "173-183"
        },
        "background": {
            "vi": "Được thành lập năm 1924 bởi Sir Jack Cohen, Tesco từng đối mặt với cuộc khủng hoảng thị phần khốc liệt vào đầu những năm 1990 trước sự cạnh tranh giá rẻ từ Aldi, Lidl và chuỗi siêu thị cao cấp Sainsbury.",
            "en": "Founded in 1924 by Sir Jack Cohen, Tesco faced intense market share pressure in the early 1990s from deep discounters (Aldi, Lidl) and upscale rival Sainsbury."
        },
        "strategic_problem": {
            "vi": "Làm thế nào để thoát khỏi cuộc chiến giá rẻ thuần túy, thấu hiểu giỏ hàng của từng hộ gia đình và xây dựng lòng trung thành bền vững mà không làm suy giảm biên lợi nhuận?",
            "en": "How to escape ruinous price discounting, decode individual basket purchase patterns, and build enduring loyalty without margin erosion?"
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Xác định Vấn đề Cốt lõi", "en": "Define Core Business Problem" },
                "details": {
                    "vi": "Sự thiếu hụt dữ liệu người mua tại điểm bán khiến các chương trình khuyến mãi đại trà tốn kém nhưng không ngăn được khách hàng chuyển sang đối thủ.",
                    "en": "Lack of point-of-sale customer visibility rendered mass promotions expensive and ineffective against rival discounting."
                }
            },
            {
                "step_num": 2,
                "step_name": { "vi": "Giải pháp CRM Đột phá: Thẻ Clubcard", "en": "CRM Innovation: Clubcard Launch" },
                "details": {
                    "vi": "Năm 1995, Tesco hợp tác với Dunnhumby triển khai thẻ Clubcard, biến dữ liệu quét mã vạch thành cơ sở dữ liệu phân đoạn khách hàng tinh vi nhất nước Anh.",
                    "en": "In 1995, Tesco partnered with Dunnhumby to launch Clubcard, transforming raw barcode scans into the UK's most sophisticated behavioral database."
                }
            },
            {
                "step_num": 3,
                "step_name": { "vi": "Phân đoạn Lối sống (Lifestyle Segmentation)", "en": "Lifestyle Segmentation" },
                "details": {
                    "vi": "Phân chia hàng triệu khách hàng thành các nhóm: Tiết kiệm (Frugal), Truyền thống (Traditional), Tiện lợi (Convenient), Cao cấp (Upmarket), và Sinh viên (Students).",
                    "en": "Segmented millions of shoppers into distinct lifestyle clusters: Frugal, Traditional, Convenient, Upmarket, and Students."
                }
            },
            {
                "step_num": 4,
                "step_name": { "vi": "Cá nhân hóa Siêu quy mô (Hyper-Personalization)", "en": "Mass Hyper-Personalization" },
                "details": {
                    "vi": "Gửi phiếu mua hàng trực tiếp với hơn 8 triệu biến thể khác nhau mỗi quý, đạt tỷ lệ đổi phiếu (redemption rate) lên tới 10-20% (so với mức trung bình ngành 1-2%).",
                    "en": "Distributed quarterly direct mail statements generating over 8 million unique voucher permutations, achieving unprecedented 10-20% redemption rates."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. Phân tích các yếu tố tạo nên thành công của thẻ Tesco Clubcard. Dữ liệu khách hàng đã giúp Tesco vượt qua Sainsbury như thế nào?",
                    "en": "1. Analyze the core success factors of Tesco Clubcard. How did customer data enable Tesco to surpass Sainsbury?"
                },
                "model_answer": {
                    "vi": "Tesco thành công vì không xem Clubcard là công cụ giảm giá đơn thuần mà là 'cửa sổ quan sát khách hàng'. Nhờ Dunnhumby, Tesco biết chính xác hộ gia đình nào mua sữa bột trẻ em, từ đó gửi phiếu giảm giá tã giấy đúng thời điểm, tạo sự gắn kết cảm xúc và sự tiện lợi vượt trội so với Sainsbury vốn coi thường thẻ thành viên.",
                    "en": "Tesco succeeded by treating Clubcard not as a rebate tool, but as a lens into customer behavior. Via Dunnhumby, Tesco detected life-stage triggers (e.g., buying baby milk), sending timely diaper coupons that drove deep emotional loyalty while Sainsbury dismissed cards as modern green stamps."
                }
            }
        ]
    },
    {
        "case_id": "CASE-WALMART-01",
        "company": "Walmart",
        "title": {
            "vi": "Tình huống 2: Ưu tiên Hàng đầu của Walmart: Trải nghiệm Khách hàng & Mua sắm Số hóa",
            "en": "Case 2: Walmart's Top Priority: Customer Experience & Digitized Shopping"
        },
        "industry": "Mass Retail & Omnichannel Supermarket",
        "source_reference": {
            "document": "Experiential Marketing (Batat 2019/2021)",
            "chapter": "Chapter 3, Case 8",
            "pages": "87-92"
        },
        "background": {
            "vi": "Được Sam Walton thành lập với triết lý giá rẻ mỗi ngày (EDLP) và dịch vụ khách hàng tận tâm, Walmart đối mặt với mối đe dọa sinh tồn từ đế chế thương mại điện tử Amazon.",
            "en": "Founded by Sam Walton on everyday low prices (EDLP) and dedicated service, Walmart confronted an existential digital threat from Amazon."
        },
        "strategic_problem": {
            "vi": "Làm thế nào để tích hợp 4.700 cửa hàng vật lý với nền tảng di động số nhằm tạo ra trải nghiệm mua sắm đa kênh (Phygital) không ma sát?",
            "en": "How to seamlessly integrate 4,700 brick-and-mortar supercenters with digital mobile ecosystems to create frictionless phygital retail?"
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Xóa bỏ Điểm đau khi Đổi trả (Mobile Express Returns)", "en": "Frictionless Returns" },
                "details": {
                    "vi": "Cho phép khách hàng khai báo đổi trả trên ứng dụng Walmart và chỉ cần quét mã QR tại quầy tiếp đón cửa hàng trong vòng chưa đầy 30 giây.",
                    "en": "Empowered shoppers to initiate returns in the Walmart app and simply scan a QR code at store express lanes in under 30 seconds."
                }
            },
            {
                "step_num": 2,
                "step_name": { "vi": "Dịch vụ Nhận hàng Tạp hóa (Curbside Grocery Pickup)", "en": "Curbside Grocery Pickup" },
                "details": {
                    "vi": "Tận dụng lợi thế mạng lưới cửa hàng trong bán kính 10 dặm của 90% dân số Mỹ để cung cấp dịch vụ giao hàng hoặc nhận hàng tận xe trong ngày.",
                    "en": "Leveraged physical store density within 10 miles of 90% of US households to dominate same-day curbside grocery pickup."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. Phân tích cách Walmart sử dụng ứng dụng di động để chuyển đổi trải nghiệm tại cửa hàng vật lý từ mua sắm truyền thống sang mua sắm số hóa (Phygital).",
                    "en": "1. Analyze how Walmart leverages its mobile app to transform in-store shopping from legacy retail into digitized phygital experiences."
                },
                "model_answer": {
                    "vi": "Walmart biến chiếc điện thoại thông minh của khách hàng thành trợ lý mua sắm: tìm vị trí kệ hàng chính xác (Store Map), quét mã vạch kiểm tra giá, thanh toán qua Walmart Pay và đổi trả nhanh bằng Mobile Express Returns, loại bỏ sự chờ đợi tại quầy thu ngân.",
                    "en": "Walmart converts the customer smartphone into an in-store copilot: real-time aisle navigation, barcode price scanning, Walmart Pay, and Mobile Express Returns, eliminating checkout friction."
                }
            }
        ]
    },
    {
        "case_id": "CASE-IKEA-01",
        "company": "IKEA",
        "title": {
            "vi": "Tình huống 3: Thiết kế Trải nghiệm Kỳ diệu & Hành trình Sống Thường nhật tại IKEA",
            "en": "Case 3: Designing a Magical Customer Experience & Everyday Life Journey at IKEA"
        },
        "industry": "Home Furnishing & Ready-to-Assemble Furniture",
        "source_reference": {
            "document": "Experiential Marketing (Batat 2019/2021)",
            "chapter": "Chapter 3, Case 9",
            "pages": "92-98"
        },
        "background": {
            "vi": "Ingvar Kamprad sáng lập IKEA với sứ mệnh 'tạo ra cuộc sống thường nhật tốt đẹp hơn cho số đông mọi người'.",
            "en": "Ingvar Kamprad founded IKEA with the mission 'to create a better everyday life for the many people.'"
        },
        "strategic_problem": {
            "vi": "Duy trì vị thế nhà bán lẻ nội thất lớn nhất thế giới bằng mô hình Thiết kế Dân chủ (Democratic Design) và nghiên cứu nhân chủng học tại gia đình khách hàng.",
            "en": "Sustaining global furniture leadership via Democratic Design and anthropological in-home customer research."
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Báo cáo 'Cuộc sống tại Nhà' (Life at Home Report)", "en": "'Life at Home' Field Research" },
                "details": {
                    "vi": "Các chuyên gia IKEA trực tiếp đến thăm hàng nghìn ngôi nhà trên khắp thế giới để quan sát thói quen sinh hoạt thực tế của khách hàng.",
                    "en": "IKEA researchers conduct in-home anthropological observational visits across global households to capture unarticulated living habits."
                }
            },
            {
                "step_num": 2,
                "step_name": { "vi": "Hành trình Mê cung & Trải nghiệm Đa giác quan", "en": "Sensory Showroom Maze" },
                "details": {
                    "vi": "Bố trí showroom theo lối đi định hướng, khu vui chơi trẻ em Småland và nhà hàng ẩm thực Thụy Điển giúp biến chuyến mua sắm thành chuyến dã ngoại gia đình.",
                    "en": "One-way maze layouts, Småland playrooms, and Swedish meatball food courts transform routine shopping into a full-day family outing."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. Phân loại các yếu tố trải nghiệm của IKEA đáp ứng 5 nhu cầu của khách hàng: Chức năng, Xã hội, Cảm xúc, Môi trường và Ý thức hệ.",
                    "en": "1. Categorize IKEA's experiential elements across the 5 customer needs: Functional, Social, Emotional, Environmental, and Ideological."
                },
                "model_answer": {
                    "vi": "Chức năng: Nội thất đa năng dễ lắp ráp; Xã hội: Chuyến đi chơi của gia đình; Cảm xúc: Cảm giác ấm cúng tại các gian phòng mẫu; Môi trường: Vật liệu tái chế; Ý thức hệ: Mọi người đều xứng đáng có nhà đẹp với chi phí hợp lý.",
                    "en": "Functional: Multi-functional flat-pack utility; Social: Family weekend outing; Emotional: Warmth of realistic room vignettes; Environmental: Sustainable sourcing; Ideological: Democratic accessibility to beautiful living."
                }
            }
        ]
    },
    {
        "case_id": "CASE-DISNEY-01",
        "company": "The Walt Disney Company",
        "title": {
            "vi": "Tình huống 4: Kiến tạo Trải nghiệm Khách hàng Kỳ diệu tại Công viên Walt Disney",
            "en": "Case 4: Creating a Magical Customer Experience at Walt Disney Parks"
        },
        "industry": "Theme Parks, Leisure & Entertainment",
        "source_reference": {
            "document": "Experiential Marketing (Batat 2019/2021)",
            "chapter": "Chapter 4, Case 10",
            "pages": "102-108"
        },
        "background": {
            "vi": "Walt Disney mở công viên Disneyland đầu tiên năm 1955, đặt khách tham quan vào trung tâm của những câu chuyện cổ tích sống động.",
            "en": "Walt Disney inaugurated the first Disneyland in 1955, placing guests at the emotional heart of living storytelling."
        },
        "strategic_problem": {
            "vi": "Làm thế nào để loại bỏ hoàn toàn các điểm đau (hàng dài chờ đợi, mang theo tiền mặt, giữ vé giấy) trong một khu phức hợp rộng hàng trăm hecta với hàng triệu lượt khách?",
            "en": "How to eliminate physical friction (queuing lines, cash handling, paper passes) across vast multi-acre resort complexes?"
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Hệ sinh thái Vòng đeo tay Thông minh MagicBand", "en": "MagicBand RFID Ecosystem" },
                "details": {
                    "vi": "Đầu tư 1 tỷ USD vào hệ sinh thái MyMagic+ với vòng đeo tay RFID tích hợp vé vào cửa, chìa khóa phòng khách sạn, cổng thanh toán không tiếp xúc và đặt trước trò chơi FastPass+.",
                    "en": "Invested $1B in the MyMagic+ RFID MagicBand ecosystem, unifying park admission, hotel room keys, contactless payments, and FastPass+ queues."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. Vòng tay MagicBand giải quyết các điểm đau nào trong hành trình khách hàng tại công viên Disney?",
                    "en": "1. What customer journey pain points does the MagicBand resolve at Disney parks?"
                },
                "model_answer": {
                    "vi": "MagicBand loại bỏ hoàn toàn việc xếp hàng mua vé, việc lục tìm ví tiền mặt và chìa khóa phòng, biến toàn bộ trải nghiệm thành một dòng chảy liên tục và kỳ diệu.",
                    "en": "MagicBand eliminates ticket booth queuing, wallet retrieval, and physical room keys, orchestrating a seamless, frictionless vacation flow."
                }
            }
        ]
    },
    {
        "case_id": "CASE-AIRBNB-01",
        "company": "Airbnb",
        "title": {
            "vi": "Tình huống 5: Chuyển đổi Ngành Lưu trú qua Trải nghiệm Khách hàng & Cộng đồng tại Airbnb",
            "en": "Case 5: Transforming Hospitality through Customer Experience & Community at Airbnb"
        },
        "industry": "Hospitality, Peer-to-Peer Platform & Travel Tech",
        "source_reference": {
            "document": "Experiential Marketing (Batat 2019/2021)",
            "chapter": "Chapter 4, Case 11",
            "pages": "108-113"
        },
        "background": {
            "vi": "Khởi đầu từ việc cho thuê đệm hơi tại San Francisco, Brian Chesky và Joe Gebbia đã tạo nên một nền tảng lưu trú toàn cầu không sở hữu bất kỳ phòng khách sạn nào.",
            "en": "Originating from renting air mattresses in San Francisco, Brian Chesky and Joe Gebbia built a global lodging leader without owning real estate."
        },
        "strategic_problem": {
            "vi": "Xây dựng kiến trúc niềm tin (Trust Architecture) giữa hai người hoàn toàn xa lạ (chủ nhà và khách thuê) để tạo cảm giác 'Thuộc về Bất cứ nơi đâu' (Belong Anywhere).",
            "en": "Architecting systemic mutual trust between total strangers (hosts and guests) to deliver the promise of 'Belong Anywhere.'"
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Hệ thống Đánh giá Hai chiều (Two-Way Reviews)", "en": "Two-Way Review System" },
                "details": {
                    "vi": "Cả chủ nhà và khách đều phải đánh giá lẫn nhau một cách trung thực sau mỗi kỳ nghỉ để duy trì chuẩn mực hành vi văn minh trên nền tảng.",
                    "en": "Double-blind reciprocal ratings hold both parties accountable to civilized behavioral norms."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. Nền tảng chia sẻ của Airbnb tạo dựng niềm tin và lòng trung thành của khách hàng như thế nào so với các khách sạn truyền thống?",
                    "en": "1. How does Airbnb's peer-to-peer platform cultivate customer trust and loyalty compared to traditional hotel chains?"
                },
                "model_answer": {
                    "vi": "Airbnb xây dựng lòng tin dựa trên xác minh danh tính số, bảo hiểm Host Guarantee và đánh giá hai chiều, kết hợp trải nghiệm hòa mình vào đời sống cư dân bản địa mà khách sạn truyền thống không có.",
                    "en": "Airbnb cultivates trust through verified digital identities, $1M Host Guarantees, and reciprocal reviews, pairing it with authentic local community immersion."
                }
            }
        ]
    },
    {
        "case_id": "CASE-MCDONALD-01",
        "company": "McDonald's",
        "title": {
            "vi": "Tình huống 6: Nâng tầm Trải nghiệm Thức ăn Nhanh Cả Trực tuyến & Trực tiếp tại McDonald's",
            "en": "Case 6: Elevating Fast-Food Experience Online and Offline at McDonald's"
        },
        "industry": "Fast Food & Quick Service Restaurants (QSR)",
        "source_reference": {
            "document": "Experiential Marketing (Batat 2019/2021)",
            "chapter": "Chapter 4, Case 12",
            "pages": "113-121"
        },
        "background": {
            "vi": "Từ hệ thống Speedee Service năm 1948, McDonald's phát triển thành chuỗi thức ăn nhanh lớn nhất thế giới với hơn 38.000 cửa hàng.",
            "en": "From the 1948 Speedee Service System, McDonald's expanded into the world's preeminent QSR giant with over 38,000 restaurants."
        },
        "strategic_problem": {
            "vi": "Tái định vị thương hiệu trước sự cạnh tranh của xu hướng ăn uống lành mạnh và các đối thủ 'fast-casual' như Chipotle, Shake Shack.",
            "en": "Repositioning the brand against health-conscious consumer shifts and fast-casual rivals like Chipotle and Shake Shack."
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Mô hình Trải nghiệm Tương lai (Experience of the Future - EOTF)", "en": "Experience of the Future (EOTF)" },
                "details": {
                    "vi": "Lắp đặt màn hình cảm ứng tự đặt món (kiosks), dịch vụ phục vụ tại bàn, quầy cà phê McCafé và ứng dụng di động Mobile Order & Pay.",
                    "en": "Installed self-order touchscreen kiosks, table delivery service, McCafé counters, and Mobile Order & Pay integration."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. Kiosk tự phục vụ và ứng dụng di động đã giúp McDonald's cải thiện hành trình khách hàng như thế nào?",
                    "en": "1. How have self-order kiosks and the mobile app enhanced McDonald's customer journey?"
                },
                "model_answer": {
                    "vi": "Giảm thời gian chờ đợi, loại bỏ sai sót khi nhân viên nghe nhầm món, cho phép khách hàng tự do cá nhân hóa món ăn và gia tăng giá trị đơn hàng trung bình qua gợi ý tự động.",
                    "en": "Reduces queuing anxiety, eliminates order miscommunication, empowers custom ingredient selections, and raises average ticket size via algorithmic upsells."
                }
            }
        ]
    },
    {
        "case_id": "CASE-CHANEL-01",
        "company": "Chanel",
        "title": {
            "vi": "Tình huống 7: Câu chuyện Cổ tích & Chiến lược Marketing Trải nghiệm Xa xỉ tại Chanel",
            "en": "Case 7: Fairytale Heritage & Luxury Experiential Strategy at Chanel"
        },
        "industry": "Haute Couture, Luxury Goods & Fragrances",
        "source_reference": {
            "document": "Experiential Marketing (Batat 2019/2021)",
            "chapter": "Chapter 5, Case 13",
            "pages": "126-131"
        },
        "background": {
            "vi": "Được thành lập bởi Gabrielle 'Coco' Chanel tại Paris, thương hiệu biểu trưng cho sự thanh lịch tối thượng và di sản thời trang quý phái.",
            "en": "Founded by Gabrielle 'Coco' Chanel in Paris, standing as the timeless global icon of haute couture elegance."
        },
        "strategic_problem": {
            "vi": "Bảo vệ tính độc quyền, khan hiếm và dịch vụ tiếp xúc trực tiếp (high-touch) trong kỷ nguyên số hóa đại trà.",
            "en": "Preserving brand scarcity, exclusivity, and intimate high-touch boutique service amidst digital mass-market commoditization."
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Tính Độc quyền & Giới hạn Kênh số", "en": "Digital Restraint & Boutique Exclusivity" },
                "details": {
                    "vi": "Chanel kiên quyết không bán thời trang may sẵn trên mạng để buộc khách hàng phải bước chân vào cửa hàng tận hưởng dịch vụ tư vấn trực tiếp.",
                    "en": "Chanel deliberately refrains from selling ready-to-wear fashion online, compelling clients to experience physical boutique luxury."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. Tại sao các thương hiệu xa xỉ như Chanel lại hạn chế bán hàng thời trang qua thương mại điện tử đại trà?",
                    "en": "1. Why do ultra-luxury houses like Chanel exercise deliberate restraint regarding mass e-commerce?"
                },
                "model_answer": {
                    "vi": "Bởi vì giá trị cốt lõi của hàng xa xỉ nằm ở sự khan hiếm, nghi thức mua sắm và sự chăm sóc đặc quyền của chuyên gia thời trang tại cửa hàng. Bán online đại trà sẽ làm loãng sự độc quyền.",
                    "en": "Luxury value derives from scarcity, shopping ceremony, and bespoke personal attention. Ubiquitous e-commerce erodes aura and commoditizes exclusivity."
                }
            }
        ]
    },
    {
        "case_id": "CASE-NIKE-01",
        "company": "Nike",
        "title": {
            "vi": "Tình huống 8: Cách Nike Kiến tạo Trải nghiệm Khách hàng Đỉnh cao & Hệ sinh thái Thể thao",
            "en": "Case 8: How Nike Delivers an Outstanding Customer Experience & Sports Ecosystem"
        },
        "industry": "Athletic Footwear, Apparel & Digital Sports Ecosystem",
        "source_reference": {
            "document": "Experiential Marketing (Batat 2019/2021)",
            "chapter": "Chapter 5, Case 14",
            "pages": "131-143"
        },
        "background": {
            "vi": "Phil Knight và Bill Bowerman sáng lập Nike từ đam mê cải tiến giày chạy bộ cho vận động viên, phát triển thành thương hiệu thể thao số 1 thế giới.",
            "en": "Phil Knight and Bill Bowerman co-founded Nike to elevate athlete performance, evolving into the world's leading sports brand."
        },
        "strategic_problem": {
            "vi": "Chuyển đổi từ mô hình bán buôn trung gian sang mô hình bán trực tiếp tới người tiêu dùng (Nike Direct - D2C) gắn liền với hệ sinh thái thành viên số.",
            "en": "Transitioning from wholesale distributor dependency to high-margin Direct-to-Consumer (Nike Direct) membership ecosystems."
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Hệ sinh thái Ứng dụng Thành viên (Nike Membership Ecosystem)", "en": "Digital Membership Apps" },
                "details": {
                    "vi": "Kết nối người dùng qua Nike App, SNKRS, Nike Run Club (NRC) và Nike Training Club (NTC), thu thập dữ liệu tập luyện để cá nhân hóa đề xuất sản phẩm.",
                    "en": "Unifies athletes across Nike App, SNKRS, NRC, and NTC, harvesting biometric training data to tailor product recommendations."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. Chiến lược Nike Direct (D2C) và hệ sinh thái ứng dụng đã giúp Nike kiểm soát trải nghiệm khách hàng như thế nào?",
                    "en": "1. How has Nike Direct (D2C) and its app suite enabled complete control over customer relationships?"
                },
                "model_answer": {
                    "vi": "D2C giúp Nike sở hữu dữ liệu khách hàng trực tiếp thay vì phụ thuộc vào nhà bán lẻ, thấu hiểu thói quen tập luyện và gắn kết người dùng qua cộng đồng thể thao toàn cầu.",
                    "en": "D2C grants Nike proprietary first-party data ownership, cutting retail intermediaries and binding consumers to an ongoing fitness lifestyle."
                }
            }
        ]
    },
    {
        "case_id": "CASE-ESTEE-01",
        "company": "The Estée Lauder Companies",
        "title": {
            "vi": "Tình huống 9: Mối Quan hệ Khách hàng Thân thiết & Trải nghiệm Làm đẹp tại Estée Lauder",
            "en": "Case 9: High-Touch Customer Relationships in Beauty at Estée Lauder"
        },
        "industry": "Prestige Beauty, Skincare & Cosmetics",
        "source_reference": {
            "document": "Experiential Marketing (Batat 2019/2021)",
            "chapter": "Chapter 5, Case 15",
            "pages": "143-148"
        },
        "background": {
            "vi": "Bà Estée Lauder tiên phong triết lý 'chạm vào khách hàng', phát minh ra hình thức tặng quà khi mua hàng (Gift-with-Purchase) và dùng thử sản phẩm tận tay.",
            "en": "Estée Lauder pioneered the high-touch philosophy, inventing the 'Gift-with-Purchase' promotion and hands-on client demonstrations."
        },
        "strategic_problem": {
            "vi": "Kết hợp tư vấn làm đẹp chuyên sâu truyền thống với công nghệ trí tuệ nhân tạo (AI) và thực tế tăng cường (AR) thử trang điểm ảo.",
            "en": "Harmonizing traditional personalized beauty counter advisory with AI diagnostics and AR virtual try-on tech."
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Trang điểm Ảo qua Thực tế Tăng cường (AR Virtual Try-On)", "en": "AR Virtual Try-On Innovation" },
                "details": {
                    "vi": "Tích hợp công nghệ YouCam trên quầy hàng và website giúp khách hàng thử hàng trăm màu son và phấn nền ngay lập tức mà không cần thoa lên da thật.",
                    "en": "Integrated YouCam AR mirrors across boutiques and web channels, allowing clients to test hundreds of lipstick shades instantaneously."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. Phân tích sự kết hợp giữa triết lý 'high-touch' truyền thống và công nghệ AR trong trải nghiệm làm đẹp của Estée Lauder.",
                    "en": "1. Analyze the synthesis of traditional high-touch consultation and AR technology in Estée Lauder's customer experience."
                },
                "model_answer": {
                    "vi": "AR đóng vai trò thu hút và loại bỏ sự ngần ngại khi thử nhiều màu son, trong khi chuyên viên tư vấn đóng vai trò xây dựng niềm tin và chốt đơn dựa trên sự am hiểu làn da khách hàng.",
                    "en": "AR eliminates sampling friction and encourages experimentation, while human beauty advisors provide empathetic reassurance and expert skin diagnosis."
                }
            }
        ]
    },
    {
        "case_id": "CASE-GAFA-SYNTHESIS",
        "company": "GAFA (Google, Apple, Facebook, Amazon)",
        "title": {
            "vi": "Tình huống 10: 'Bộ Tứ Công nghệ' (GAFA) & Sự Thay đổi Căn bản Trải nghiệm Khách hàng Số",
            "en": "Case 10: The 'Big Four' (GAFA) & The Paradigm Shift in Digital Customer Experience"
        },
        "industry": "Digital Tech Platforms, Ecosystems, Hardware, Social Media, E-Commerce",
        "source_reference": {
            "document": "Experiential Marketing (Batat 2019/2021)",
            "chapter": "Chapter 1",
            "pages": "2-30"
        },
        "background": {
            "vi": "Bốn gã khổng lồ công nghệ định hình toàn bộ chuẩn mực tương tác, tiêu dùng nội dung, mua sắm và kết nối xã hội của nhân loại trong thế kỷ 21.",
            "en": "Four digital titans establishing 21st-century benchmarks for information access, hardware aesthetics, social connection, and e-commerce fulfillment."
        },
        "strategic_problem": {
            "vi": "So sánh các mô hình trải nghiệm khách hàng: Quảng cáo dựa trên dữ liệu (Google, Meta) đối đầu với Hệ sinh thái phần cứng khép kín (Apple) và Bánh đà ám ảnh khách hàng (Amazon).",
            "en": "Comparing customer experience models: Data-driven ad monetization (Google, Meta) vs. closed device ecosystems (Apple) vs. customer obsession flywheels (Amazon)."
        },
        "crm_framework_steps": [
            {
                "step_num": 1,
                "step_name": { "vi": "Bánh đà Ám ảnh Khách hàng của Amazon", "en": "Amazon's Customer Obsession Flywheel" },
                "details": {
                    "vi": "Đặt khách hàng làm trung tâm tối thượng với mua hàng 1-Click, giao hàng hỏa tốc qua Amazon Prime và thuật toán gợi ý sản phẩm cá nhân hóa.",
                    "en": "Prioritizes customer obsession above competitor focus via 1-Click purchasing, Prime delivery speed, and predictive recommendations."
                }
            },
            {
                "step_num": 2,
                "step_name": { "vi": "Hệ sinh thái Thiết bị Liền mạch của Apple", "en": "Apple's Seamless Hardware-Software Ecosystem" },
                "details": {
                    "vi": "Khóa chặt lòng trung thành của người dùng bằng tính năng AirDrop, iCloud, iMessage kết hợp dịch vụ hỗ trợ cao cấp tại quầy Genius Bar của Apple Store.",
                    "en": "Solidifies customer retention through walled-garden synergy (AirDrop, iCloud) backed by Genius Bar empathetic customer support."
                }
            }
        ],
        "discussion_questions": [
            {
                "q_num": 1,
                "prompt": {
                    "vi": "1. So sánh triết lý giữ chân khách hàng của Apple (Hệ sinh thái khép kín & dịch vụ Genius Bar) và Amazon (Đăng ký Prime & giao hàng thần tốc).",
                    "en": "1. Compare retention philosophies between Apple (closed device ecosystem & Genius Bar) and Amazon (Prime subscription & rapid fulfillment)."
                },
                "model_answer": {
                    "vi": "Apple giữ chân bằng thiết kế hoàn mỹ, chi phí chuyển đổi sang Android cao và dịch vụ hỗ trợ trực tiếp nhân văn tại Genius Bar. Amazon giữ chân bằng sự tiện lợi tuyệt đối, tiết kiệm thời gian và giá trị gia tăng khổng lồ của gói Prime.",
                    "en": "Apple locks in users via design elegance, prohibitive ecosystem switching barriers, and high-touch Genius Bar hospitality. Amazon retains through friction reduction, convenience, and Prime subscription value."
                }
            }
        ]
    }
]

(data_dir / "cases.json").write_text(json.dumps(cases, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Generated cases.json with all {len(cases)} enterprise case studies.")
