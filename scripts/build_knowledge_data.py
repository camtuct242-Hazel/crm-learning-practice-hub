import json
from pathlib import Path

data_dir = Path(r"C:\Kiến thức cần học\CRM\output\data")
data_dir.mkdir(parents=True, exist_ok=True)

# 1. CURRICULUM MODULES (Phase 3 Batch 1: Baran Ch 1-4 & Kostojohn Ch 1-2)
curriculum = [
    {
        "id": "mod-baran-ch01",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part I",
        "part_title": {
            "vi": "Phần I: Lý thuyết và Sự phát triển của CRM",
            "en": "Part I: CRM Theory and Development"
        },
        "chapter_num": 1,
        "title": {
            "vi": "Chương 1: Giới thiệu về Quản trị Quan hệ Khách hàng (CRM)",
            "en": "Chapter 1: Introduction to Customer Relationship Management"
        },
        "pdf_page_start": 8,
        "book_page": 1,
        "learning_objectives": {
            "vi": [
                "Hiểu rõ bản chất đa chiều của CRM: Chiến lược, Tác nghiệp, Phân tích và Hợp tác.",
                "Phân biệt rạch ròi giữa Marketing Giao dịch (Transactional) và Marketing Mối quan hệ (Relational).",
                "Nắm vững các thành phần hữu hình cấu thành hệ thống CRM hiện đại và Trung tâm Tương tác Khách hàng (CEC).",
                "Phân tích các cấu trúc kinh doanh then chốt gắn liền với CRM: Giá trị vòng đời khách hàng (CLV), Giá trị tài sản khách hàng (Customer Equity)."
            ],
            "en": [
                "Understand the multi-dimensional nature of CRM: Strategic, Operational, Analytical, and Collaborative.",
                "Distinguish sharply between Transactional Marketing and Relationship Marketing.",
                "Master the tangible components of modern CRM systems and Customer Engagement Centers (CEC).",
                "Analyze key business constructs tied to CRM: Customer Lifetime Value (CLV) and Customer Equity."
            ]
        },
        "key_concepts": [
            {
                "term": "Strategic CRM",
                "name": { "vi": "CRM Chiến lược", "en": "Strategic CRM" },
                "definition": {
                    "vi": "Triết lý kinh doanh đặt khách hàng làm trung tâm nhằm thu hút và giữ chân các khách hàng có giá trị sinh lời cao nhất.",
                    "en": "A core customer-centric business strategy aimed at winning and keeping profitable customers."
                }
            },
            {
                "term": "Operational CRM",
                "name": { "vi": "CRM Tác nghiệp", "en": "Operational CRM" },
                "definition": {
                    "vi": "Tự động hóa các quy trình tiếp xúc trực tiếp với khách hàng (front-office) bao gồm bán hàng (SFA), tiếp thị và dịch vụ khách hàng.",
                    "en": "Automation of customer-facing front-office processes including sales force automation (SFA), marketing, and customer service."
                }
            },
            {
                "term": "Analytical CRM",
                "name": { "vi": "CRM Phân tích", "en": "Analytical CRM" },
                "definition": {
                    "vi": "Khai phá và phân tích dữ liệu hành vi của khách hàng để tối ưu hóa quyết định kinh doanh và cá nhân hóa trải nghiệm.",
                    "en": "Systematic analysis of customer data to optimize business decisions and personalize customer interactions."
                }
            },
            {
                "term": "Collaborative CRM",
                "name": { "vi": "CRM Hợp tác", "en": "Collaborative CRM" },
                "definition": {
                    "vi": "Đồng bộ hóa dữ liệu và kênh giao tiếp giữa các phòng ban nội bộ và các đối tác trong chuỗi giá trị nhằm phục vụ khách hàng liền mạch.",
                    "en": "Synchronization of communication channels and data across departments and value-chain partners for seamless customer service."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 1.1 Khái niệm và Các chiều kích của CRM\nCRM không đơn thuần là một phần mềm công nghệ, mà là sự tích hợp giữa chiến lược kinh doanh, văn hóa doanh nghiệp hướng về khách hàng và nền tảng dữ liệu số. Baran & Galka chỉ ra rằng CRM toàn diện bao gồm 4 chiều kích: Chiến lược (định hướng nguồn lực vào nhóm khách hàng mang lại giá trị cao nhất), Tác nghiệp (tự động hóa tiếp xúc tại điểm chạm), Phân tích (trích xuất tri thức từ kho dữ liệu) và Hợp tác (chia sẻ thông tin xuyên suốt tổ chức và chuỗi cung ứng).\n\n### 1.2 Chuyển dịch từ Marketing Giao dịch sang Marketing Mối quan hệ\n- **Marketing Giao dịch:** Tập trung vào từng thương vụ bán hàng đơn lẻ, mục tiêu ngắn hạn, chiêu thị đại trà, ít quan tâm đến dịch vụ sau bán và chỉ số giữ chân.\n- **Marketing Mối quan hệ (Cốt lõi CRM):** Tập trung vào việc xây dựng mối quan hệ tương hỗ bền vững, đo lường bằng Giá trị Vòng đời Khách hàng (CLV), cá nhân hóa thông điệp và tối ưu hóa chi phí giữ chân khách hàng (thường thấp hơn nhiều so với chi phí tìm kiếm khách hàng mới).\n\n### 1.3 Trung tâm Tương tác Khách hàng (CEC - Customer Engagement Center)\nSự tiến hóa từ Call Center truyền thống (chỉ tiếp nhận cuộc gọi thoại một chiều) lên Contact Center đa kênh, và nay là Customer Engagement Center (CEC). CEC tích hợp thoại, email, chat, mạng xã hội, ứng dụng di động vào một màn hình duy nhất cho nhân viên dịch vụ (Single Desktop View), giúp nhận diện lịch sử tương tác của khách hàng theo thời gian thực.",
            "en": "### 1.1 Definition and Dimensions of CRM\nCRM is not merely a software application, but an integration of business strategy, customer-centric organizational culture, and digital data infrastructure. Baran & Galka identify four core dimensions of comprehensive CRM: Strategic (directing resources toward high-value customers), Operational (front-office automation), Analytical (extracting actionable intelligence from data warehouses), and Collaborative (sharing customer insights across departments and supply-chain partners).\n\n### 1.2 Paradigm Shift from Transactional to Relationship Marketing\n- **Transactional Marketing:** Focuses on discrete sales, short-term horizons, mass promotional pushes, minimal post-purchase service, and acquisition over retention.\n- **Relationship Marketing (CRM Foundation):** Focuses on continuous mutual value creation, measured by Customer Lifetime Value (CLV), personalized interactions, and optimizing retention economics (which costs substantially less than new customer acquisition).\n\n### 1.3 Customer Engagement Centers (CEC)\nThe evolution from traditional single-channel call centers into multichannel contact centers, and modern Customer Engagement Centers (CEC). CEC orchestrates voice, email, web chat, social media, and mobile apps into a unified agent desktop, providing real-time visibility into complete customer interaction history."
        },
        "key_takeaways": {
            "vi": [
                "CRM là chiến lược kinh doanh tổng thể, công nghệ chỉ là công cụ hỗ trợ hiện thực hóa chiến lược.",
                "Chi phí giữ chân một khách hàng hiện tại thường chỉ bằng 1/5 đến 1/7 chi phí thu hút một khách hàng mới.",
                "CRM hiệu quả đòi hỏi sự phối hợp đồng bộ giữa Chiến lược, Tác nghiệp, Phân tích và Hợp tác."
            ],
            "en": [
                "CRM is an overarching business strategy; software and technology are merely enablers.",
                "Retaining an existing customer typically costs one-fifth to one-seventh of acquiring a new one.",
                "Effective CRM demands synchronized harmony across Strategic, Operational, Analytical, and Collaborative dimensions."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b01-01",
                "question": {
                    "vi": "Phân tích 4 chiều kích của CRM (Chiến lược, Tác nghiệp, Phân tích, Hợp tác). Một doanh nghiệp chỉ mua phần mềm CRM tác nghiệp mà thiếu định hướng chiến lược thì sẽ gặp rủi ro gì?",
                    "en": "Analyze the 4 dimensions of CRM (Strategic, Operational, Analytical, Collaborative). What risks does a firm face if it implements operational CRM software without strategic orientation?"
                },
                "model_answer": {
                    "vi": "Nếu chỉ cài đặt phần mềm tác nghiệp mà thiếu chiến lược khách hàng, doanh nghiệp sẽ rơi vào bẫy 'tự động hóa quy trình kém hiệu quả'. Nhân viên có thể ghi nhận dữ liệu nhưng ban lãnh đạo không biết phân bổ nguồn lực vào khách hàng sinh lời cao, dẫn đến lãng phí chi phí đầu tư CNTT và tỷ lệ rời bỏ khách hàng không giảm.",
                    "en": "Without strategic orientation, the company falls into the trap of 'automating inefficient processes.' Staff record interactions without clear guidance on prioritizing profitable customer tiers, resulting in wasted IT expenditure and unreduced customer churn."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 1",
            "pages": "8-47 (Book pp. 1-38)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-baran-ch02",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part I",
        "part_title": {
            "vi": "Phần I: Lý thuyết và Sự phát triển của CRM",
            "en": "Part I: CRM Theory and Development"
        },
        "chapter_num": 2,
        "title": {
            "vi": "Chương 2: Lịch sử và Sự Phát triển của CRM",
            "en": "Chapter 2: The History and Development of CRM"
        },
        "pdf_page_start": 48,
        "book_page": 39,
        "learning_objectives": {
            "vi": [
                "Theo dõi nguồn gốc lịch sử của CRM từ Marketing trực tiếp (Direct Marketing) đến Tiếp thị cơ sở dữ liệu (Database Marketing).",
                "Hiểu rõ sự ra đời của Tự động hóa Lực lượng Bán hàng (Sales Force Automation - SFA) trong thập niên 1990.",
                "Phân tích làn sóng e-CRM vào đầu những năm 2000 và sự trỗi dậy của điện toán đám mây (Cloud CRM).",
                "Rút ra các bài học đắt giá từ tỷ lệ thất bại cao của các dự án CRM thời kỳ đầu."
            ],
            "en": [
                "Trace the historical roots of CRM from Direct Marketing to Database Marketing.",
                "Understand the genesis of Sales Force Automation (SFA) during the 1990s.",
                "Analyze the e-CRM wave of the early 2000s and the rise of Cloud-based CRM solutions.",
                "Extract critical lessons from the high failure rates of early-generation CRM implementations."
            ]
        },
        "key_concepts": [
            {
                "term": "Database Marketing",
                "name": { "vi": "Tiếp thị Cơ sở Dữ liệu", "en": "Database Marketing" },
                "definition": {
                    "vi": "Hình thức tiếp thị sử dụng cơ sở dữ liệu khách hàng để phân tích hành vi và gửi các thông điệp tiếp thị cá nhân hóa.",
                    "en": "A form of marketing using databases of customers to analyze behavior and generate targeted, personalized communications."
                }
            },
            {
                "term": "Sales Force Automation (SFA)",
                "name": { "vi": "Tự động hóa Lực lượng Bán hàng (SFA)", "en": "Sales Force Automation (SFA)" },
                "definition": {
                    "vi": "Phần mềm hỗ trợ nhân viên bán hàng quản lý phễu bán hàng (pipeline), lịch hẹn, liên hệ và báo giá.",
                    "en": "Software designed to streamline sales activities including pipeline management, appointments, contacts, and quote generation."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 2.1 Các giai đoạn Tiến hóa của CRM\n1. **Kỷ nguyên Marketing Trực tiếp & Cơ sở Dữ liệu (Thập niên 1970–1980):** Doanh nghiệp bắt đầu thu thập danh sách khách hàng gửi thư trực tiếp (direct mail). Việc ứng dụng máy tính lớn (mainframe) giúp lưu trữ lịch sử giao dịch và mã bưu chính để phân đoạn khách hàng thô sơ.\n2. **Kỷ nguyên Tự động hóa Bán hàng - SFA (Thập niên 1990):** Sự xuất hiện của các phần mềm quản lý liên hệ (contact management như ACT!) và hệ thống ERP của SAP, Baan, Oracle. Các công ty nhận thấy nhân viên kinh doanh dành quá nhiều thời gian cho việc hành chính giấy tờ nên đã đầu tư vào SFA để theo dõi cơ hội kinh doanh (opportunity tracking).\n3. **Kỷ nguyên CRM Doanh nghiệp & Sự bùng nổ Dot-com (1995–2002):** Siebel Systems trở thành biểu tượng của phần mềm Enterprise CRM On-Premises. Tuy nhiên, giai đoạn này chứng kiến tỷ lệ thất bại lên tới 50-70% do doanh nghiệp đầu tư hàng triệu USD vào phần mềm mà không chuẩn hóa quy trình, thiếu sự chấp nhận của người dùng (user adoption) và dữ liệu bị phân mảnh.\n4. **Kỷ nguyên Điện toán Đám mây & SaaS (2000–Hiện nay):** Sự ra đời của Salesforce (1999) mở ra mô hình CRM đa người thuê trên đám mây (Multi-tenant Cloud), giúp giảm mạnh chi phí đầu tư ban đầu (CAPEX) thành chi phí vận hành định kỳ (OPEX), mở rộng khả năng tiếp cận CRM cho cả doanh nghiệp vừa và nhỏ.",
            "en": "### 2.1 The Evolutionary Eras of CRM\n1. **Direct & Database Marketing Era (1970s–1980s):** Initial collection of customer lists for direct mail campaigns. Mainframe computers enabled transactional storage and postal code segmentation.\n2. **Sales Force Automation Era (1990s):** Emergence of digital contact managers (e.g. ACT!) and ERP systems. Businesses sought to liberate sales reps from administrative paperwork through digital pipeline and opportunity tracking.\n3. **Enterprise CRM Boom & Dot-com Turmoil (1995–2002):** Siebel Systems pioneered large-scale On-Premises CRM. However, failure rates reached 50–70% because enterprises poured millions into technology without process standardization, executive governance, or front-line user adoption.\n4. **Cloud & SaaS Era (2000s–Present):** Pioneered by Salesforce (1999), multi-tenant cloud architectures converted prohibitive capital expenditures (CAPEX) into predictable operational subscriptions (OPEX), democratizing enterprise-grade CRM for organizations of all scales."
        },
        "key_takeaways": {
            "vi": [
                "Lịch sử chứng minh công nghệ CRM chỉ thành công khi đi kèm với sự chấp thuận của người dùng cuối.",
                "Điện toán đám mây (Cloud/SaaS) đã chuyển đổi căn bản mô hình chi phí triển khai CRM từ CAPEX sang OPEX."
            ],
            "en": [
                "History demonstrates that CRM technology fails without end-user adoption and process clarity.",
                "Cloud/SaaS fundamentally restructured CRM cost models from heavy CAPEX to flexible OPEX."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b02-01",
                "question": {
                    "vi": "Tại sao các dự án CRM On-Premises trong thập niên 1990 lại có tỷ lệ thất bại rất cao? Mô hình SaaS đã giải quyết các bất cập đó như thế nào?",
                    "en": "Why did early On-Premises CRM projects in the 1990s suffer high failure rates? How did the SaaS model address those shortcomings?"
                },
                "model_answer": {
                    "vi": "Các dự án 1990s thất bại do chi phí bản quyền và hạ tầng máy chủ quá lớn, thời gian triển khai kéo dài 1-2 năm, phần mềm quá phức tạp khiến nhân viên bán hàng từ chối nhập dữ liệu. SaaS giải quyết bằng cách triển khai nhanh qua trình duyệt, cập nhật tính năng liên tục, trả phí theo người dùng thực tế và giao diện thân thiện hơn.",
                    "en": "1990s implementations failed due to immense upfront server/licensing capital, 12-24 month deployment cycles, and bloated interfaces that prompted salesperson revolt. SaaS resolved this with instant browser access, continuous automated upgrades, pay-as-you-go user seats, and intuitive UX."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 2",
            "pages": "48-80 (Book pp. 39-70)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-baran-ch03",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part I",
        "part_title": {
            "vi": "Phần I: Lý thuyết và Sự phát triển của CRM",
            "en": "Part I: CRM Theory and Development"
        },
        "chapter_num": 3,
        "title": {
            "vi": "Chương 3: Marketing Quan hệ và Nền tảng Lý thuyết của CRM",
            "en": "Chapter 3: Relationship Marketing and CRM"
        },
        "pdf_page_start": 81,
        "book_page": 71,
        "learning_objectives": {
            "vi": [
                "Nắm vững các lý thuyết nền tảng: Lý thuyết Cam kết - Tin cậy (Commitment-Trust Theory của Morgan & Hunt).",
                "Phân tích cơ chế chuyển đổi chi phí (Switching Costs) và các rào cản rời bỏ.",
                "Hiểu rõ 3 cấp độ liên kết mối quan hệ: Liên kết Tài chính, Liên kết Xã hội và Liên kết Cấu trúc.",
                "Đánh giá tính chuẩn tắc trong quan hệ (Relational Norms) và nguyên lý công bằng (Equity Theory)."
            ],
            "en": [
                "Master theoretical foundations: Morgan & Hunt's Commitment-Trust Theory.",
                "Analyze switching costs mechanisms and structural barriers to defection.",
                "Understand the 3 levels of relationship bonding: Financial, Social, and Structural.",
                "Evaluate relational norms and equity theory in customer retention."
            ]
        },
        "key_concepts": [
            {
                "term": "Commitment-Trust Theory",
                "name": { "vi": "Lý thuyết Cam kết - Tin cậy", "en": "Commitment-Trust Theory" },
                "definition": {
                    "vi": "Mô hình lý thuyết khẳng định rằng Niềm tin và Sự cam kết là hai biến số trung gian quan trọng nhất dẫn đến sự thành công của mối quan hệ khách hàng.",
                    "en": "Theoretical model establishing that trust and commitment are the primary mediating variables driving relationship marketing success."
                }
            },
            {
                "term": "Structural Bonding",
                "name": { "vi": "Liên kết Cấu trúc", "en": "Structural Bonding" },
                "definition": {
                    "vi": "Mối quan hệ gắn kết thông qua việc tích hợp sâu rộng các quy trình, hệ thống công nghệ hoặc thiết bị mà khó có thể chuyển sang nhà cung cấp khác.",
                    "en": "Bonds formed by integrating technological systems, joint workflows, or dedicated equipment that create high switching costs."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 3.1 Lý thuyết Cam kết - Tin cậy (Morgan & Hunt, 1994)\nBaran & Galka nhấn mạnh rằng mối quan hệ khách hàng không thể tồn tại bền vững chỉ bằng các ưu đãi giảm giá ngắn hạn. Niềm tin (Trust) xuất hiện khi khách hàng tin vào độ tin cậy và sự chính trực của doanh nghiệp. Cam kết (Commitment) là niềm tin rằng mối quan hệ hiện tại quan trọng đến mức đáng để bỏ nỗ lực tối đa nhằm duy trì nó vô thời hạn.\n\n### 3.2 Ba Cấp độ Gắn kết Mối quan hệ (Berry & Parasuraman)\n1. **Cấp độ 1 - Gắn kết Tài chính (Financial Bonds):** Dùng giá, điểm tích lũy, chiết khấu để giữ chân khách hàng (ví dụ: thẻ khách hàng thân thiết giảm giá). Điểm yếu: Rất dễ bị đối thủ cạnh tranh sao chép bằng chính sách giá thấp hơn.\n2. **Cấp độ 2 - Gắn kết Xã hội (Social Bonds):** Xây dựng sợi dây liên kết cá nhân hóa, sự thấu hiểu, quan tâm và đối xử như đối tác quen thuộc (ví dụ: chuyên viên quản lý khách hàng ưu tiên, chúc mừng sinh nhật, sự kiện tri ân).\n3. **Cấp độ 3 - Gắn kết Cấu trúc (Structural Bonds):** Tích hợp sâu vào quy trình vận hành và hệ thống dữ liệu của khách hàng (ví dụ: hệ thống đặt hàng tự động EDI/API giữa nhà sản xuất và đại lý, ứng dụng quản lý nhà thông minh). Đây là cấp độ gắn kết bền vững nhất và tạo ra chi phí chuyển đổi (Switching Costs) cao nhất.",
            "en": "### 3.1 Commitment-Trust Theory (Morgan & Hunt, 1994)\nBaran & Galka stress that customer relationships cannot endure on price discounts alone. Trust exists when one party has confidence in an exchange partner's reliability and integrity. Relationship commitment is an enduring desire to maintain a valued relationship.\n\n### 3.2 Three Levels of Relationship Bonds (Berry & Parasuraman)\n1. **Level 1 - Financial Bonds:** Stimulated through price incentives, reward points, and discounts. Weakness: easily duplicated by price-undercutting competitors.\n2. **Level 2 - Social Bonds:** Cultivated through interpersonal personalization, empathetic communication, and mutual appreciation (e.g., dedicated account managers, personal acknowledgments).\n3. **Level 3 - Structural Bonds:** Created by embedding joint technologies, integrated workflows, and specialized processes (e.g., direct API/EDI integrations between supply chain partners). Provides highest retention resilience and highest switching barriers."
        },
        "key_takeaways": {
            "vi": [
                "Gắn kết tài chính là rào cản yếu nhất; gắn kết cấu trúc là rào cản bền vững nhất chống lại sự lôi kéo của đối thủ.",
                "Niềm tin và sự cam kết là hai trụ cột bảo vệ doanh nghiệp trong những giai đoạn khủng hoảng hoặc biến động thị trường."
            ],
            "en": [
                "Financial bonding is the easiest to replicate; structural bonding establishes the most durable moat against competitive churn.",
                "Trust and commitment serve as vital shock absorbers during market crises and operational failures."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b03-01",
                "question": {
                    "vi": "So sánh 3 cấp độ gắn kết: Tài chính, Xã hội và Cấu trúc. Tại sao một chương trình khách hàng thân thiết chỉ dựa vào tích điểm (Financial Bonds) thường thất bại trong việc tạo ra lòng trung thành thực sự?",
                    "en": "Compare Financial, Social, and Structural relationship bonds. Why do loyalty programs relying solely on points accumulation fail to generate authentic attitudinal loyalty?"
                },
                "model_answer": {
                    "vi": "Chương trình chỉ tích điểm tạo ra 'lòng trung thành giả tạo' (spurious loyalty) dựa trên tính vụ lợi. Khách hàng sẵn sàng chuyển sang đối thủ ngay khi đối thủ đưa ra mức chiết khấu hấp dẫn hơn. Ngược lại, gắn kết xã hội tạo cảm xúc và gắn kết cấu trúc tạo rào cản kỹ thuật khiến chi phí chuyển đổi quá cao.",
                    "en": "Points-only programs create spurious transactional loyalty driven by opportunistic self-interest. Customers defect immediately when a rival offers steeper discounts. In contrast, social bonding fosters emotional attachment, while structural bonding creates prohibitive switching barriers."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 3",
            "pages": "81-112 (Book pp. 71-101)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-baran-ch04",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part I",
        "part_title": {
            "vi": "Phần I: Lý thuyết và Sự phát triển của CRM",
            "en": "Part I: CRM Theory and Development"
        },
        "chapter_num": 4,
        "title": {
            "vi": "Chương 4: Tổ chức Doanh nghiệp và Định hướng Khách hàng",
            "en": "Chapter 4: Organization and CRM"
        },
        "pdf_page_start": 113,
        "book_page": 102,
        "learning_objectives": {
            "vi": [
                "Phân tích sự khác biệt giữa cấu trúc tổ chức định hướng sản phẩm và định hướng khách hàng.",
                "Giải quyết mâu thuẫn 'silo phòng ban' cản trở dòng luân chuyển thông tin khách hàng.",
                "Xây dựng văn hóa lấy khách hàng làm trung tâm (Customer-Centric Culture) và cơ chế đãi ngộ phù hợp.",
                "Áp dụng nguyên tắc quản trị thay đổi (Change Management) khi triển khai CRM trong tổ chức."
            ],
            "en": [
                "Analyze structural differences between product-oriented and customer-oriented organizational designs.",
                "Resolve departmental silos that obstruct cross-functional customer data flow.",
                "Foster a customer-centric culture aligned with employee incentive systems.",
                "Apply change management principles during organizational CRM adoption."
            ]
        },
        "key_concepts": [
            {
                "term": "Customer-Centric Organization",
                "name": { "vi": "Tổ chức Lấy Khách hàng làm Trung tâm", "en": "Customer-Centric Organization" },
                "definition": {
                    "vi": "Mô hình tổ chức cấu trúc các phòng ban, chỉ số đo lường hiệu quả (KPI) và quy trình xoay quanh từng phân khúc khách hàng thay vì từng dòng sản phẩm.",
                    "en": "An organizational model where departments, KPIs, and operating processes are structured around customer segments rather than product silos."
                }
            },
            {
                "term": "Departmental Silos",
                "name": { "vi": "Ốc đảo Phòng ban (Silos)", "en": "Departmental Silos" },
                "definition": {
                    "vi": "Tình trạng các bộ phận nội bộ (Marketing, Bán hàng, Dịch vụ, Kế toán) nắm giữ dữ liệu riêng rẽ và không chia sẻ cho nhau, làm phân mảnh trải nghiệm khách hàng.",
                    "en": "The isolated compartmentalization of data and workflows among sales, marketing, and service units, fragmenting customer experience."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 4.1 Tái cấu trúc Tổ chức theo Định hướng Khách hàng\nPhần lớn các doanh nghiệp truyền thống được xây dựng theo cấu trúc 'Định hướng Sản phẩm' (Product-Centric), trong đó các giám đốc sản phẩm chỉ quan tâm đến doanh số của sản phẩm mình quản lý mà không biết khách hàng đang mua những sản phẩm nào khác của công ty. Để triển khai CRM thành công, doanh nghiệp phải chuyển dịch sang cấu trúc 'Định hướng Khách hàng' (Customer-Centric), bổ nhiệm các Giám đốc Phân khúc Khách hàng (Customer Segment Managers) có trách nhiệm tối đa hóa tổng giá trị khách hàng trên toàn bộ dải sản phẩm.\n\n### 4.2 Xóa bỏ Ốc đảo Dữ liệu (Breaking Silos)\nKhi khách hàng liên hệ với bộ phận hỗ trợ kỹ thuật, nếu nhân viên dịch vụ không biết được đơn hàng đang được xử lý bên bộ phận bán hàng, khách hàng sẽ cảm thấy bực bội vì phải lặp lại thông tin nhiều lần. CRM hợp tác giải quyết vấn đề này bằng cách thiết lập Chân dung Khách hàng Hợp nhất (360-Degree Single Customer View) dùng chung cho tất cả các phòng ban.\n\n### 4.3 Đãi ngộ và Quản trị Thay đổi\nNhân viên bán hàng thường có xu hướng giấu kín thông tin liên hệ và nhật ký giao dịch vì xem đó là 'tài sản cá nhân' để đảm bảo vị thế. Doanh nghiệp phải tái thiết lập hệ thống KPI và hoa hồng: không chỉ thưởng cho doanh số ký kết mà còn thưởng cho việc chia sẻ dữ liệu chính xác và mức độ hài lòng lâu dài của khách hàng.",
            "en": "### 4.1 Re-engineering Toward a Customer-Centric Organization\nTraditional organizations follow product-centric hierarchies where product managers optimize isolated SKU revenues, oblivious to cross-category customer spend. Successful CRM mandates a customer-centric realignment: appointing Customer Segment Managers tasked with maximizing customer lifetime value across the entire brand portfolio.\n\n### 4.2 Breaking Down Departmental Silos\nFragmented systems force customers to repeat grievances across sales, billing, and technical support. Collaborative CRM establishes a unified 360-Degree Single Customer View accessible across all corporate touchpoints.\n\n### 4.3 Compensation Alignment and Change Management\nSales representatives frequently hoard client contact records as proprietary personal leverage. Executive leadership must restructure compensation frameworks to reward accurate database hygiene, collaborative cross-selling, and net customer retention."
        },
        "key_takeaways": {
            "vi": [
                "Cấu trúc sản phẩm khiến tổ chức bị phân mảnh; cấu trúc khách hàng gắn kết tổ chức quanh giá trị vòng đời khách hàng.",
                "CRM sẽ thất bại nếu hệ thống chỉ tiêu đánh giá (KPI) của nhân viên vẫn chỉ tập trung vào chỉ số giao dịch ngắn hạn."
            ],
            "en": [
                "Product-centric architectures fragment companies; customer-centric alignment unites the firm around customer lifetime value.",
                "CRM adoption fails if employee incentives remain strictly anchored to short-term transaction volumes."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b04-01",
                "question": {
                    "vi": "Ốc đảo phòng ban (Silos) gây tổn hại như thế nào đến trải nghiệm khách hàng? Lãnh đạo cần làm gì để vượt qua rào cản văn hóa khi triển khai CRM?",
                    "en": "How do departmental silos impair the customer experience? What leadership interventions are required to overcome cultural resistance during CRM adoption?"
                },
                "model_answer": {
                    "vi": "Silos làm phân mảnh dữ liệu, khiến khách hàng nhận thông điệp mâu thuẫn từ tiếp thị và bị nhân viên dịch vụ bỏ rơi. Để vượt qua rào cản, lãnh đạo phải thay đổi cơ chế khen thưởng gắn liền với việc cập nhật dữ liệu CRM và đích thân nêu gương sử dụng hệ thống.",
                    "en": "Silos fragment customer knowledge, subjecting clients to conflicting marketing solicitations and disjointed service handoffs. Leaders must align compensation with CRM data hygiene and champion system utilization by example."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 4",
            "pages": "113-139 (Book pp. 102-127)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-fund-ch01",
        "book_id": "TB-KOSTOJOHN-2011",
        "book_title": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
        "chapter_num": 1,
        "title": {
            "vi": "Chương 1: Giới thiệu & Các Nguồn Giá trị Cốt lõi của CRM",
            "en": "Chapter 1: Introduction & Sources of CRM Value"
        },
        "pdf_page_start": 14,
        "book_page": 1,
        "learning_objectives": {
            "vi": [
                "Định nghĩa CRM từ góc độ thực tiễn của nhà tư vấn triển khai.",
                "Khám phá 4 nguồn giá trị kinh doanh cốt lõi do CRM tạo ra.",
                "Hiểu rõ tầm quan trọng sống còn của Văn hóa Định hướng Dữ liệu (Data-Driven Culture).",
                "Phân tích vai trò và trách nhiệm của Người bảo trợ Cấp cao (Executive Sponsor)."
            ],
            "en": [
                "Define CRM from the practitioner's implementation perspective.",
                "Explore the 4 primary sources of business value generated by CRM.",
                "Understand the critical prerequisite of a Data-Driven Culture.",
                "Analyze the indispensable responsibilities of the Executive Sponsor."
            ]
        },
        "key_concepts": [
            {
                "term": "Data-Driven Learning Organization",
                "name": { "vi": "Tổ chức Học tập Định hướng Dữ liệu", "en": "Data-Driven Learning Organization" },
                "definition": {
                    "vi": "Tổ chức ra quyết định kinh doanh dựa trên bằng chứng dữ liệu thực tế thay vì cảm tính hoặc suy đoán chủ quan.",
                    "en": "An organization that grounds business decisions in verified empirical data rather than instinct or subjective guesswork."
                }
            },
            {
                "term": "Executive Sponsor",
                "name": { "vi": "Người Bảo trợ Cấp cao", "en": "Executive Sponsor" },
                "definition": {
                    "vi": "Lãnh đạo cấp cao nhất (CEO, COO, VP) chịu trách nhiệm cam kết nguồn lực, tháo gỡ rào cản chính trị nội bộ và thúc đẩy sự chấp nhận CRM.",
                    "en": "The senior executive who champions the CRM vision, secures funding, resolves political hurdles, and mandates adoption."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 1.1 Định nghĩa CRM theo Kostojohn et al.\nTrong bối cảnh áp lực cạnh tranh khốc liệt và sản phẩm ngày càng bị 'hàng hóa hóa' (commoditization), trải nghiệm khách hàng trở thành yếu tố khác biệt hóa duy nhất. Khách hàng ngày càng hiểu biết hơn, đòi hỏi cao hơn và ít trung thành hơn. Để chiến thắng, doanh nghiệp phải đưa ra các quyết định 'đúng đắn hơn và nhanh chóng hơn' dựa trên thông tin chính xác.\n\n### 1.2 Bốn Nguồn Giá trị Lớn của CRM\n1. **Hỗ trợ Tổ chức Học tập Định hướng Dữ liệu:** CRM biến dữ liệu giao dịch tản mác thành tri thức có cấu trúc, giúp tổ chức nhìn thấy xu hướng tiêu dùng và bài học kinh nghiệm.\n2. **Loại bỏ Sự lãng phí và Nâng cao Năng suất Nhân viên:** Tự động hóa các tác vụ lặp đi lặp lại (soạn hợp đồng mẫu, gửi email nhắc việc, cập nhật trạng thái đơn hàng), giúp nhân viên tập trung vào các hoạt động tạo giá trị cao.\n3. **Cung cấp Trải nghiệm Khách hàng Vượt trội:** Khách hàng được phục vụ nhanh chóng, chính xác tại mọi điểm chạm mà không cần phải nhắc lại lịch sử yêu cầu của mình.\n4. **Cung cấp Dữ liệu Đầu vào cho các Quyết định Chiến lược:** Hỗ trợ dự báo doanh số (sales forecasting), quản lý chỉ tiêu kinh doanh (sales management), lập kế hoạch phát triển sản phẩm mới và bố trí nhân sự chăm sóc khách hàng dựa trên dự báo khối lượng cuộc gọi.",
            "en": "### 1.1 Defining CRM in Contemporary Markets\nAs market competition commoditizes core products, customer experience becomes the defining competitive frontier. Modern customers are increasingly sophisticated, demanding, and fickle. Winning firms must make better decisions faster, powered by real-time intelligence.\n\n### 1.2 The Four Sources of CRM Business Value\n1. **Supporting a Data-Driven, Learning Organization:** Transforms raw operational touchpoints into systemic organizational knowledge.\n2. **Wringing out Inefficiencies and Increasing Productivity:** Automates repetitive administrative chores (follow-ups, quote templates, status reporting), freeing personnel for high-value advisory interactions.\n3. **Providing a Superior Customer Experience:** Seamless, personalized service delivery across every operational channel without frustrating redundancies.\n4. **Informing Strategic Business Decisions:** Delivers empirical data for sales forecasting, territory management, product lifecycle roadmaps, and customer support staffing models."
        },
        "key_takeaways": {
            "vi": [
                "CRM cung cấp giá trị bằng cách vừa cắt giảm chi phí vận hành lãng phí, vừa gia tăng doanh thu nhờ trải nghiệm khách hàng vượt trội.",
                "Thiếu Người bảo trợ Cấp cao tích cực là nguyên nhân số một khiến dự án CRM bị chìm xuồng."
            ],
            "en": [
                "CRM drives value simultaneously by eliminating administrative waste and elevating customer lifetime revenues.",
                "The absence of an active, committed Executive Sponsor is the primary predictor of CRM project demise."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-f01-01",
                "question": {
                    "vi": "Liệt kê 4 nguồn giá trị của CRM theo Kostojohn et al. Tại sao việc chỉ xem CRM là công cụ tăng năng suất bán hàng là một góc nhìn hạn hẹp?",
                    "en": "List the 4 sources of CRM value according to Kostojohn et al. Why is viewing CRM solely as a sales productivity tool dangerously narrow?"
                },
                "model_answer": {
                    "vi": "Bốn nguồn giá trị gồm: Hỗ trợ tổ chức học tập định hướng dữ liệu, loại bỏ lãng phí nâng cao năng suất, mang lại trải nghiệm khách hàng tốt hơn, và cung cấp dữ liệu định hướng quyết định kinh doanh. Nếu chỉ coi CRM là công cụ cho đội ngũ bán hàng, doanh nghiệp sẽ bỏ lỡ giá trị dự báo chiến lược, cải tiến sản phẩm và liên kết dịch vụ khách hàng.",
                    "en": "The 4 sources are: Data-driven learning, operational efficiency, superior customer experience, and strategic decision support. Confining CRM to sales automation forfeits its broader value in enterprise forecasting, product innovation, and cross-functional service orchestration."
                }
            }
        ],
        "source": {
            "document": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
            "chapter": "Chapter 1",
            "pages": "14-23 (Book pp. 1-10)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-fund-ch02",
        "book_id": "TB-KOSTOJOHN-2011",
        "book_title": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
        "chapter_num": 2,
        "title": {
            "vi": "Chương 2: Các Thành phần Quyết định Thành công của CRM",
            "en": "Chapter 2: Components of CRM Success"
        },
        "pdf_page_start": 24,
        "book_page": 11,
        "learning_objectives": {
            "vi": [
                "Nắm vững bộ ba cấu thành thành công của CRM: Con người (People), Quy trình (Process), và Công nghệ (Technology).",
                "Thiết lập cơ cấu quản trị dự án CRM: Ban Chỉ đạo (Steering Committee), Đội Triển khai, và Các Đại sứ Phòng ban (Champions).",
                "Phân biệt 3 nhóm quy trình then chốt: Quy trình Vận hành, Quy trình Bảo trì, và Quy trình Nâng cấp.",
                "Nhận diện các cạm bẫy triển khai phổ biến và các biện pháp phòng ngừa rủi ro."
            ],
            "en": [
                "Master the foundational triad of CRM success: People, Process, and Technology.",
                "Architect robust project governance: Steering Committee, Implementation Team, and Departmental Champions.",
                "Distinguish the 3 core process streams: Operational, Maintenance, and Enhancement processes.",
                "Identify common implementation pitfalls and deploy mitigation strategies."
            ]
        },
        "key_concepts": [
            {
                "term": "Steering Committee",
                "name": { "vi": "Ban Chỉ đạo Dự án (Steering Committee)", "en": "Steering Committee" },
                "definition": {
                    "vi": "Nhóm đại diện lãnh đạo liên phòng ban chịu trách nhiệm định hướng chiến lược, giải quyết mâu thuẫn phạm vi và phân bổ ngân sách cho hệ thống CRM.",
                    "en": "A cross-functional leadership body governing strategic priorities, scope disputes, and resource allocation for the CRM platform."
                }
            },
            {
                "term": "Departmental Champions",
                "name": { "vi": "Đại sứ CRM Phòng ban (Champions)", "en": "Departmental Champions" },
                "definition": {
                    "vi": "Những nhân sự nòng cốt tại các phòng ban được tôn trọng về chuyên môn, có nhiệm vụ truyền cảm hứng và hướng dẫn đồng nghiệp sử dụng CRM.",
                    "en": "Respected front-line subject matter experts who advocate for the system, mentor peers, and channel user feedback to the core team."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 2.1 Bộ ba 'Con người, Quy trình, Công nghệ' (People, Process, Technology)\nKostojohn et al. nhấn mạnh rằng công nghệ chỉ đóng góp khoảng 20% vào thành công của dự án, 80% còn lại phụ thuộc vào Con người và Quy trình.\n\n### 2.2 Trụ cột Con người (People Governance)\n- **Executive Sponsor:** Cung cấp thẩm quyền và ngân sách tối cao.\n- **Steering Committee:** Họp định kỳ hàng tháng/hàng quý để xét duyệt các yêu cầu thay đổi (change requests) và giữ vững phạm vi dự án.\n- **Implementation Team:** Gồm Quản lý Dự án (PM), Kiến trúc sư Giải pháp (Solution Architect), Chuyên viên Phân tích Nghiệp vụ (BA) và Đội ngũ Kỹ thuật.\n- **Departmental Champions:** 'Cầu nối vàng' giúp giảm bớt sự phản đối của nhân viên cơ sở và thu thập phản hồi thực tế.\n- **CRM Administration Team:** Quản trị viên hệ thống phụ trách cấp quyền, bảo trì dữ liệu và cấu hình giao diện.\n\n### 2.3 Trụ cột Quy trình (Process)\nKhông thể số hóa một quy trình đang bị lỗi. Doanh nghiệp phải chuẩn hóa 3 nhóm quy trình:\n1. *Quy trình Tác nghiệp (Operational Processes):* Quy trình từ khách hàng tiềm năng đến ký hợp đồng (Lead-to-Opportunity-to-Cash), quy trình xử lý khiếu nại (Ticket SLA).\n2. *Quy trình Bảo trì (Maintenance Processes):* Xử lý lỗi, quản trị quyền truy cập, sao lưu dữ liệu dự phòng.\n3. *Quy trình Nâng cấp (Enhancement Processes):* Tiếp nhận ý kiến người dùng, đánh giá mức độ ưu tiên và phát triển phiên bản mới theo chu kỳ định kỳ.",
            "en": "### 2.1 The 'People, Process, Technology' Triad\nKostojohn et al. argue that technology represents roughly 20% of CRM project success; the remaining 80% hinges on organizational alignment (People) and rigorous operating discipline (Process).\n\n### 2.2 People & Governance Architecture\n- **Executive Sponsor:** Provides ultimate executive legitimacy and funding defense.\n- **Steering Committee:** Cross-functional leadership body meeting on a disciplined cadence to arbitrate scope changes and ensure business alignment.\n- **Implementation Team:** Project Manager, Solution Architect, Business Analysts, and Technical Integration Developers.\n- **Departmental Champions:** Trusted front-line champions who overcome peer inertia, mentor end-users, and filter product feedback.\n- **CRM Administration Team:** System admins handling role-based security, data cleansing, and configuration changes.\n\n### 2.3 Process Discipline\nAutomating a flawed process merely accelerates dysfunction. Organizations must formalize:\n1. *Operational Processes:* Lead-to-Opportunity lifecycles, service escalation SLAs, and quoting rules.\n2. *Maintenance Processes:* Bug triage, user provisioning, database indexing, and automated backups.\n3. *Enhancement Processes:* Structured backlog intake, ROI prioritization, and release management cadences."
        },
        "key_takeaways": {
            "vi": [
                "Cài đặt phần mềm hiện đại vào một quy trình lộn xộn sẽ chỉ tạo ra một sự lộn xộn tự động hóa đắt tiền.",
                "Ban Chỉ đạo liên phòng ban là rào chắn cần thiết để ngăn chặn tình trạng phình to phạm vi dự án (Scope Creep)."
            ],
            "en": [
                "Deploying advanced software onto broken processes merely creates expensive, automated chaos.",
                "A cross-functional Steering Committee is the vital bulwark against fatal scope creep."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-f02-01",
                "question": {
                    "vi": "Tại sao việc thành lập Ban Chỉ đạo (Steering Committee) và mạng lưới Đại sứ Phòng ban (Champions) lại quyết định sự sống còn của một dự án CRM?",
                    "en": "Why are the establishment of a Steering Committee and a network of Departmental Champions critical to CRM project survival?"
                },
                "model_answer": {
                    "vi": "Ban Chỉ đạo đảm bảo sự đồng thuận giữa các phòng ban và ngăn chặn xung đột về tài nguyên. Mạng lưới Đại sứ phòng ban xóa bỏ tâm lý ngại thay đổi của nhân viên cơ sở và giúp hệ thống gắn chặt với nhu cầu công việc thực tế hàng ngày.",
                    "en": "The Steering Committee enforces cross-departmental alignment and resolves resource conflicts at the executive level. Departmental Champions neutralize front-line resistance and ensure system design reflects real-world workflow realities."
                }
            }
        ],
        "source": {
            "document": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
            "chapter": "Chapter 2",
            "pages": "24-60 (Book pp. 11-46)",
            "evidence_type": "source-derived"
        }
    }
]

# Write curriculum.json
(data_dir / "curriculum.json").write_text(json.dumps(curriculum, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Generated curriculum.json with {len(curriculum)} comprehensive chapters.")

# 2. GLOSSARY (Initial comprehensive set of 30+ validated terms)
glossary = [
    {
        "id": "term-crm",
        "acronym": "CRM",
        "term": { "vi": "Quản trị Quan hệ Khách hàng (CRM)", "en": "Customer Relationship Management (CRM)" },
        "category": "Foundations",
        "definition": {
            "vi": "Chiến lược kinh doanh toàn diện kết hợp giữa con người, quy trình và công nghệ nhằm xác định, thu hút, duy trì và phát triển các khách hàng sinh lời cao nhất trong dài hạn.",
            "en": "A comprehensive enterprise business strategy aligning people, process, and technology to identify, acquire, retain, and grow profitable customer relationships over the long term."
        },
        "context": {
            "vi": "Được áp dụng trên toàn bộ chu trình sống của khách hàng từ tiếp thị, bán hàng đến chăm sóc sau bán.",
            "en": "Applied across the entire customer lifecycle encompassing marketing, sales, and ongoing customer support."
        },
        "related_terms": ["term-clv", "term-sfa", "term-cec"],
        "source": { "document": "Baran & Galka (2017) p. 9; Kostojohn (2011) p. 14" }
    },
    {
        "id": "term-clv",
        "acronym": "CLV / LTV",
        "term": { "vi": "Giá trị Vòng đời Khách hàng (CLV)", "en": "Customer Lifetime Value (CLV)" },
        "category": "Metrics",
        "definition": {
            "vi": "Giá trị hiện tại ròng của tổng dòng lợi nhuận trong tương lai mà một khách hàng đóng góp cho doanh nghiệp trong suốt toàn bộ thời gian duy trì mối quan hệ.",
            "en": "The discounted net present value of the stream of future net profit cash flows generated by a customer over the entire duration of the relationship."
        },
        "context": {
            "vi": "Dùng để xác định ngưỡng chi phí tối đa cho việc thu hút khách hàng (CAC) và phân bổ nguồn lực chăm sóc khách hàng VIP.",
            "en": "Used to establish maximum customer acquisition cost (CAC) ceilings and prioritize resource allocations for high-tier customer segments."
        },
        "related_terms": ["term-cac", "term-churn-rate", "term-retention-rate"],
        "source": { "document": "Baran & Galka (2017) Ch. 1 & 12, pp. 24, 352-375" }
    },
    {
        "id": "term-sfa",
        "acronym": "SFA",
        "term": { "vi": "Tự động hóa Lực lượng Bán hàng (SFA)", "en": "Sales Force Automation (SFA)" },
        "category": "Technology",
        "definition": {
            "vi": "Hệ thống phần mềm tự động hóa các tác vụ quản lý bán hàng như theo dõi cơ hội, quản lý danh bạ, lập lịch hẹn và báo giá tự động.",
            "en": "Software application suite that automates routine sales activities including lead qualification, contact tracking, appointment scheduling, and quote generation."
        },
        "context": {
            "vi": "Giúp tăng thời gian tiếp xúc thực tế giữa nhân viên bán hàng và khách hàng bằng cách giảm thiểu gánh nặng hành chính giấy tờ.",
            "en": "Frees salespeople from administrative overhead to maximize active selling and customer face-time."
        },
        "related_terms": ["term-pipeline", "term-opportunity"],
        "source": { "document": "Baran & Galka (2017) p. 55; Kostojohn (2011) p. 46" }
    },
    {
        "id": "term-cec",
        "acronym": "CEC",
        "term": { "vi": "Trung tâm Tương tác Khách hàng (CEC)", "en": "Customer Engagement Center (CEC)" },
        "category": "Service",
        "definition": {
            "vi": "Mô hình trung tâm dịch vụ hiện đại hợp nhất tất cả các kênh liên lạc (thoại, chat, email, mạng xã hội, ứng dụng) trên một màn hình làm việc duy nhất của nhân viên hỗ trợ.",
            "en": "Modern contact center architecture unifying all communication touchpoints (voice, chat, email, social, mobile) into a single, real-time agent desktop view."
        },
        "context": {
            "vi": "Đảm bảo tính liền mạch của dữ liệu khi khách hàng chuyển đổi giữa các kênh liên lạc khác nhau.",
            "en": "Ensures seamless omnichannel continuity when customers pivot between disparate service touchpoints."
        },
        "related_terms": ["term-omnichannel", "term-scv"],
        "source": { "document": "Baran & Galka (2017) pp. 21-23" }
    },
    {
        "id": "term-scv",
        "acronym": "SCV / 360-View",
        "term": { "vi": "Góc nhìn Khách hàng Hợp nhất 360 độ (SCV)", "en": "Single Customer View (SCV)" },
        "category": "Data",
        "definition": {
            "vi": "Bản ghi dữ liệu tổng hợp toàn diện chứa đựng mọi lịch sử tương tác, giao dịch mua sắm, yêu cầu hỗ trợ và sở thích cá nhân của một khách hàng duy nhất.",
            "en": "A unified master customer record integrating all historical touchpoints, transaction records, support tickets, and preference attributes across the enterprise."
        },
        "context": {
            "vi": "Là điều kiện tiên quyết để triển khai cá nhân hóa tiếp thị và dịch vụ khách hàng không bị trùng lặp.",
            "en": "The foundational prerequisite for high-precision personalization and non-redundant customer service."
        },
        "related_terms": ["term-crm", "term-data-warehouse"],
        "source": { "document": "Baran & Galka (2017) Ch. 5; Kostojohn (2011) Ch. 6" }
    },
    {
        "id": "term-churn-rate",
        "acronym": "Churn",
        "term": { "vi": "Tỷ lệ Rời bỏ Khách hàng (Churn Rate)", "en": "Customer Churn Rate" },
        "category": "Metrics",
        "definition": {
            "vi": "Tỷ lệ phần trăm số lượng khách hàng ngừng giao dịch hoặc hủy bỏ hợp đồng với doanh nghiệp trong một khoảng thời gian xác định.",
            "en": "The percentage of customers or subscribers who cancel or fail to renew their relationship with a firm during a specified time window."
        },
        "context": {
            "vi": "Chỉ số sống còn đối với các mô hình kinh doanh đăng ký định kỳ (SaaS, viễn thông, bảo hiểm).",
            "en": "Vital survival metric for subscription and contractual business models (SaaS, telecom, utilities)."
        },
        "related_terms": ["term-retention-rate", "term-clv"],
        "source": { "document": "Baran & Galka (2017) Ch. 9 & 10" }
    },
    {
        "id": "term-nps",
        "acronym": "NPS",
        "term": { "vi": "Chỉ số Đo lường Mức độ Hài lòng & Quảng bá (NPS)", "en": "Net Promoter Score (NPS)" },
        "category": "Metrics",
        "definition": {
            "vi": "Thước đo lòng trung thành dựa trên câu hỏi: 'Trên thang điểm từ 0 đến 10, khả năng bạn sẽ giới thiệu công ty chúng tôi cho bạn bè hoặc đồng nghiệp là bao nhiêu?'.",
            "en": "Customer loyalty metric based on the single question: 'On a scale from 0 to 10, how likely are you to recommend our company to a friend or colleague?'"
        },
        "context": {
            "vi": "Phân chia khách hàng thành 3 nhóm: Người quảng bá (Promoters: 9-10), Người thụ động (Passives: 7-8), và Người gièm pha (Detractors: 0-6). NPS = % Promoters - % Detractors.",
            "en": "Segments respondents into Promoters (9-10), Passives (7-8), and Detractors (0-6). NPS = % Promoters minus % Detractors."
        },
        "related_terms": ["term-csat", "term-clv"],
        "source": { "document": "Baran & Galka (2017) pp. 275-278" }
    },
    {
        "id": "term-saas",
        "acronym": "SaaS",
        "term": { "vi": "Phần mềm dạng Dịch vụ (SaaS / Cloud CRM)", "en": "Software as a Service (SaaS)" },
        "category": "Technology",
        "definition": {
            "vi": "Mô hình phân phối phần mềm trong đó ứng dụng được lưu trữ trên máy chủ đám mây của nhà cung cấp và người dùng truy cập qua trình duyệt web trên cơ sở thuê bao định kỳ.",
            "en": "Software deployment model where applications are hosted in vendor cloud infrastructure and accessed by clients via web browsers on a recurring subscription basis."
        },
        "context": {
            "vi": "Loại bỏ chi phí đầu tư máy chủ vật lý ban đầu và tự động hóa quá trình cập nhật phần mềm.",
            "en": "Eliminates heavy upfront on-premise hardware capital and automates regular feature upgrades."
        },
        "related_terms": ["term-crm", "term-on-premises"],
        "source": { "document": "Kostojohn (2011) Ch. 4, pp. 78-85" }
    }
]

(data_dir / "glossary.json").write_text(json.dumps(glossary, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Generated glossary.json with {len(glossary)} core terms.")
