import json
from pathlib import Path

data_dir = Path(r"C:\Kiến thức cần học\CRM\output\data")

# Load existing curriculum
curr_file = data_dir / "curriculum.json"
existing_curr = json.loads(curr_file.read_text(encoding="utf-8")) if curr_file.exists() else []

# Update Kostojohn Ch 2 in existing_curr to qualify the 80/20 claim
for c in existing_curr:
    if c["id"] == "mod-fund-ch02":
        c["detailed_notes"]["vi"] = c["detailed_notes"]["vi"].replace(
            "Kostojohn et al. nhấn mạnh rằng công nghệ chỉ đóng góp khoảng 20% vào thành công của dự án, 80% còn lại phụ thuộc vào Con người và Quy trình.",
            "Kostojohn et al. (2011, tr. 11) xác định Bốn Trụ Cột của Thành Công CRM: Con người (People), Quy trình (Process), Công nghệ (Technology), và Kỳ vọng (Expectations). Trong khi quy tắc kinh nghiệm phổ biến trong giới tư vấn thường cho rằng '80% thành công nằm ở Con người & Quy trình và chỉ 20% là Công nghệ', các tác giả nhấn mạnh rằng cả 4 trụ cột đều có tính chất sống còn và công nghệ chỉ phát huy giá trị khi kỳ vọng của con người và quy trình vận hành được thiết kế chuẩn mực."
        )
        c["detailed_notes"]["en"] = c["detailed_notes"]["en"].replace(
            "Kostojohn et al. argue that technology represents roughly 20% of CRM project success; the remaining 80% hinges on organizational alignment (People) and rigorous operating discipline (Process).",
            "Kostojohn et al. (2011, p. 11) formally establish Four Pillars of CRM Success: People, Process, Technology, and Expectations. While popular consulting folklore frequently cites an '80% People-Process / 20% Technology' rule of thumb, the authors emphasize that all four pillars are mutually indispensable and that technology fails whenever human expectations and operational processes are misaligned."
        )

# Map existing IDs
existing_ids = {c["id"] for c in existing_curr}

new_chapters = [
    # --- BARAN & GALKA CHAPTERS 5 - 7 (Part II) ---
    {
        "id": "mod-baran-ch05",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part II",
        "part_title": {
            "vi": "Phần II: Quản trị Dữ liệu và Công nghệ",
            "en": "Part II: Data Management and Technology"
        },
        "chapter_num": 5,
        "title": {
            "vi": "Chương 5: CRM và Quản trị Dữ liệu Khách hàng",
            "en": "Chapter 5: CRM and Data Management"
        },
        "pdf_page_start": 140,
        "book_page": 128,
        "learning_objectives": {
            "vi": [
                "Nắm vững các phương pháp thu thập dữ liệu sơ cấp và thứ cấp tại các điểm chạm khách hàng.",
                "Giải quyết bài toán tích hợp dữ liệu khách hàng (Customer Data Integration - CDI).",
                "Hiểu rõ khái niệm Hộ gia đình hóa (Householding) và khử trùng lặp dữ liệu (Deduplication).",
                "Xây dựng góc nhìn khách hàng hợp nhất (Single Customer View - SCV) xuyên suốt tổ chức."
            ],
            "en": [
                "Master primary and secondary data capture methods across customer touchpoints.",
                "Solve the Customer Data Integration (CDI) challenge across fragmented legacy systems.",
                "Understand Householding concepts, entity resolution, and data deduplication.",
                "Build an accurate Single Customer View (SCV) across enterprise silos."
            ]
        },
        "key_concepts": [
            {
                "term": "Customer Data Integration (CDI)",
                "name": { "vi": "Tích hợp Dữ liệu Khách hàng (CDI)", "en": "Customer Data Integration (CDI)" },
                "definition": {
                    "vi": "Quy trình hợp nhất, làm sạch và đồng bộ dữ liệu khách hàng từ nhiều nguồn tiếp xúc phân mảnh thành một bản ghi chuẩn hóa duy nhất.",
                    "en": "The technical process of consolidating, cleansing, and synchronizing customer records from disparate operational silos into a single master identity."
                }
            },
            {
                "term": "Householding",
                "name": { "vi": "Hộ gia đình hóa (Householding)", "en": "Householding" },
                "definition": {
                    "vi": "Kỹ thuật gom nhóm các cá nhân cùng chung sống tại một địa chỉ thực tế hoặc cùng một đơn vị kinh tế để tránh gửi thông điệp tiếp thị trùng lặp và tối ưu hóa ngân sách.",
                    "en": "The analytical practice of linking individual customer records residing at the same physical address or economic unit to prevent redundant marketing solicitations."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 5.1 Quản trị Dữ liệu - Động cơ của CRM\nDữ liệu là tài sản cốt lõi thúc đẩy mọi quyết định trong CRM. Nếu dữ liệu bị sai lệch, phân mảnh hoặc thiếu cập nhật (hiện tượng 'Rác vào, rác ra' - Garbage In, Garbage Out), mọi nỗ lực tự động hóa và phân tích đều sẽ thất bại.\n\n### 5.2 Thách thức Tích hợp Dữ liệu Khách hàng (CDI)\nDoanh nghiệp thường vận hành nhiều hệ thống riêng lẻ: phần mềm bán hàng tại cửa hàng (POS), trang thương mại điện tử, tổng đài chăm sóc khách hàng, và phần mềm kế toán. Cùng một khách hàng có thể xuất hiện với tên gọi 'Nguyen Van A' ở POS nhưng lại là 'A. Nguyen' trên website. CDI thực hiện 5 bước cốt lõi:\n1. *Thu thập dữ liệu (Ingestion):* Gom dữ liệu từ mọi điểm chạm.\n2. *Chuẩn hóa (Standardization):* Định dạng lại số điện thoại, địa chỉ, email.\n3. *Khử trùng lặp (Deduplication / Matching):* Áp dụng thuật toán so khớp mờ (fuzzy matching) để xác định các bản ghi trùng lặp.\n4. *Hộ gia đình hóa (Householding):* Gom nhóm các thành viên trong gia đình.\n5. *Hợp nhất thành Bản ghi Vàng (Golden Record):* Tạo ra Chân dung Khách hàng Hợp nhất (SCV).\n\n### 5.3 Nguồn Dữ liệu Sơ cấp vs. Thứ cấp\n- **Dữ liệu Sơ cấp:** Do doanh nghiệp trực tiếp thu thập qua giao dịch, đăng ký thành viên, tương tác ứng dụng.\n- **Dữ liệu Thứ cấp:** Mua từ các nhà môi giới dữ liệu (data brokers) như Nielsen, Experian để bổ sung nhân khẩu học, thu nhập ước tính và sở thích lối sống.",
            "en": "### 5.1 Data Management as the Engine of CRM\nData is the foundational fuel of CRM strategy. Dirty, fragmented, or obsolete data produces the 'Garbage In, Garbage Out' dilemma, paralyzing analytical insights and operational execution.\n\n### 5.2 The Customer Data Integration (CDI) Challenge\nEnterprises inherently run siloed architectures: in-store POS terminals, e-commerce web storefronts, call center logs, and ERP accounting systems. A single customer may appear with subtle variations across touchpoints. CDI executes a five-stage harmonization discipline:\n1. *Ingestion:* Aggregating raw feeds from all transactional and digital touchpoints.\n2. *Standardization:* Parsing postal addresses, phone numbers, and names into unified formats.\n3. *Matching & Deduplication:* Employing deterministic and probabilistic fuzzy matching algorithms to reconcile duplicate records.\n4. *Householding:* Clustered aggregation of individuals within the same household.\n5. *Golden Record Generation:* Producing an authoritative Single Customer View (SCV).\n\n### 5.3 Primary vs. Secondary Customer Data\n- **Primary Data:** Proprietary first-party data captured directly through purchases, warranty registrations, and digital app usage.\n- **Secondary Data:** Third-party data syndicated from brokers (e.g., Acxiom, Experian) to append credit indicators, lifestyle segmentation, and household income estimates."
        },
        "key_takeaways": {
            "vi": [
                "Tích hợp dữ liệu khách hàng (CDI) là bước kỹ thuật bắt buộc để xóa bỏ ốc đảo thông tin.",
                "Householding giúp doanh nghiệp tiết kiệm hàng triệu USD chi phí gửi thư tiếp thị và tránh gây khó chịu cho khách hàng."
            ],
            "en": [
                "Customer Data Integration (CDI) is the essential architectural prerequisite for eliminating data silos.",
                "Householding optimizes marketing expenditure and shields consumers from annoying duplicate solicitations."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b05-01",
                "question": {
                    "vi": "Trình bày 5 bước trong quy trình Tích hợp Dữ liệu Khách hàng (CDI). Tại sao việc tạo ra 'Bản ghi Vàng' (Golden Record) lại quyết định chất lượng dịch vụ khách hàng?",
                    "en": "Detail the 5 steps of the Customer Data Integration (CDI) process. Why is creating a 'Golden Record' decisive for customer service excellence?"
                },
                "model_answer": {
                    "vi": "5 bước gồm: Thu thập, Chuẩn hóa, Khử trùng lặp, Hộ gia đình hóa và Hợp nhất Bản ghi Vàng. Bản ghi Vàng hợp nhất mọi lịch sử mua sắm và sự cố, giúp nhân viên phục vụ khách hàng tức thì mà không yêu cầu khách hàng phải lặp lại thông tin.",
                    "en": "The 5 steps are Ingestion, Standardization, Matching/Deduplication, Householding, and Golden Record synthesis. The Golden Record equips front-line agents with complete context, eliminating repetitive customer questioning."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 5",
            "pages": "140-179 (Book pp. 128-166)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-baran-ch06",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part II",
        "part_title": {
            "vi": "Phần II: Quản trị Dữ liệu và Công nghệ",
            "en": "Part II: Data Management and Technology"
        },
        "chapter_num": 6,
        "title": {
            "vi": "Chương 6: Công nghệ và Nền tảng Dữ liệu CRM",
            "en": "Chapter 6: Technology and Data Platforms"
        },
        "pdf_page_start": 180,
        "book_page": 167,
        "learning_objectives": {
            "vi": [
                "Phân tích kiến trúc tổng thể của hệ thống CNTT hỗ trợ CRM.",
                "Hiểu rõ sự khác biệt và vai trò phối hợp giữa Kho Dữ liệu (Data Warehouse - DW), Kho Lưu trữ Dữ liệu Vận hành (ODS), và Data Mart.",
                "Đánh giá Ma trận Gartner Magic Quadrant trong việc lựa chọn nhà cung cấp giải pháp CRM.",
                "Nắm vững các phương thức tích hợp hệ thống qua API, Web Services và Middleware."
            ],
            "en": [
                "Analyze enterprise IT architecture supporting modern CRM ecosystems.",
                "Distinguish the roles of Data Warehouses (DW), Operational Data Stores (ODS), and Data Marts.",
                "Apply Gartner Magic Quadrants to evaluate CRM platform vendor competencies.",
                "Master integration mechanisms including APIs, Web Services, and Enterprise Service Buses (ESB)."
            ]
        },
        "key_concepts": [
            {
                "term": "Operational Data Store (ODS)",
                "name": { "vi": "Kho Dữ liệu Vận hành (ODS)", "en": "Operational Data Store (ODS)" },
                "definition": {
                    "vi": "Cơ sở dữ liệu trung gian lưu trữ dữ liệu tác nghiệp thời gian thực (hoặc gần thực) phục vụ các hoạt động hàng ngày của nhân viên mặt tiền.",
                    "en": "An interim operational database providing real-time snapshot data for front-office transaction processing and immediate query resolution."
                }
            },
            {
                "term": "Data Warehouse (DW)",
                "name": { "vi": "Kho Dữ liệu Doanh nghiệp (Data Warehouse)", "en": "Enterprise Data Warehouse (EDW)" },
                "definition": {
                    "vi": "Hệ thống lưu trữ dữ liệu lịch sử tổng hợp quy mô lớn được tối ưu hóa cho việc truy vấn phân tích, báo cáo quản trị và khai phá dữ liệu (OLAP).",
                    "en": "A centralized repository of historical, aggregated enterprise data optimized for analytical reporting, business intelligence, and data mining (OLAP)."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 6.1 Kiến trúc Nền tảng Công nghệ CRM\nMột hệ thống CRM hoàn chỉnh không hoạt động độc lập mà nằm trong một hệ sinh thái kiến trúc dữ liệu gồm 3 tầng cơ sở dữ liệu chính:\n1. **Cơ sở dữ liệu Tác nghiệp (OLTP / ODS):** Xử lý các giao dịch tức thời (đặt hàng, cập nhật vé hỗ trợ). Dữ liệu thay đổi liên tục từng giây, ưu tiên tốc độ đọc/ghi đơn lẻ.\n2. **Kho Dữ liệu Doanh nghiệp (Enterprise Data Warehouse - EDW):** Định kỳ (hàng đêm/hàng tuần), dữ liệu từ các hệ thống tác nghiệp được trích xuất, chuyển đổi và nạp (ETL) vào EDW. Dữ liệu ở đây là bất biến (read-only) và có tính lịch sử nhiều năm.\n3. **Data Mart:** Là các phân vùng kho dữ liệu chuyên biệt phục vụ riêng cho một phòng ban (ví dụ: Marketing Data Mart để chạy chiến dịch email, Sales Data Mart để tính hoa hồng).\n\n### 6.2 Đánh giá Nhà cung cấp qua Gartner Magic Quadrant\nBaran & Galka giới thiệu phương pháp phân loại nhà cung cấp của Gartner dựa trên 2 trục:\n- *Khả năng Thực thi (Ability to Execute):* Năng lực tài chính, mạng lưới hỗ trợ, khả năng mở rộng sản phẩm.\n- *Tầm nhìn Chiến lược (Completeness of Vision):* Khả năng đón đầu xu hướng công nghệ (Cloud, AI, di động).\nBốn góc phần tư gồm: Leaders (Dẫn đầu), Challengers (Thách thức), Visionaries (Tầm nhìn), và Niche Players (Thị trường ngách).",
            "en": "### 6.1 CRM Technological Architecture & Data Hierarchy\nAn enterprise CRM does not function as an island, but anchors a tri-tiered database architecture:\n1. **Operational Databases (OLTP / ODS):** Real-time transactional stores handling high-throughput read/write operations (e.g. active cart checkouts, ticket updates).\n2. **Enterprise Data Warehouse (EDW):** Historical repository populated via periodic Extract-Transform-Load (ETL) pipelines. Read-only and structured for deep longitudinal query analysis (OLAP).\n3. **Data Marts:** Departmental analytical subsets tailored to specific business domains (e.g., Marketing Campaign Marts, Sales Commission Marts).\n\n### 6.2 Vendor Selection via Gartner's Magic Quadrant\nBaran & Galka examine Gartner's two-axis market categorization:\n- *Ability to Execute:* Financial viability, support ecosystem, product scalability.\n- *Completeness of Vision:* Innovation roadmaps, cloud alignment, AI capabilities.\nFour quadrants: Leaders, Challengers, Visionaries, and Niche Players."
        },
        "key_takeaways": {
            "vi": [
                "ODS phục vụ tác nghiệp thời gian thực; Data Warehouse phục vụ phân tích chiến lược dài hạn.",
                "Ma trận Gartner giúp doanh nghiệp chọn nhà cung cấp phù hợp với quy mô và mức độ trưởng thành công nghệ."
            ],
            "en": [
                "ODS powers instant operational queries; EDW powers strategic longitudinal analytics.",
                "Gartner Magic Quadrants guide platform selection matched to corporate architectural maturity."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b06-01",
                "question": {
                    "vi": "Phân biệt vai trò của ODS và Data Warehouse trong hệ thống CRM. Tại sao không nên chạy các báo cáo phân tích phức tạp trực tiếp trên cơ sở dữ liệu tác nghiệp (OLTP)?",
                    "en": "Distinguish the roles of an ODS and a Data Warehouse in CRM. Why should complex analytical queries never be run directly on operational OLTP databases?"
                },
                "model_answer": {
                    "vi": "Chạy truy vấn phân tích nặng trên hệ thống OLTP sẽ làm khóa bảng dữ liệu (table locking), làm nghẽn hệ thống xử lý giao dịch bán hàng tại cửa hàng. ODS chỉ giữ dữ liệu tức thời phục vụ giao dịch; Data Warehouse được thiết kế chuyên biệt để xử lý truy vấn phân tích phức tạp mà không ảnh hưởng đến tác nghiệp.",
                    "en": "Running heavy analytical queries on OLTP transactional engines locks tables and degrades front-line POS throughput. ODS supports real-time tactical tasks; EDWs are decoupled and indexed specifically for intense multi-dimensional queries."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 6",
            "pages": "180-207 (Book pp. 167-193)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-baran-ch07",
        "book_id": "TB-BARAN-2017",
        "book_title": "Customer Relationship Management (Baran & Galka 2017)",
        "part_num": "Part II",
        "part_title": {
            "vi": "Phần II: Quản trị Dữ liệu và Công nghệ",
            "en": "Part II: Data Management and Technology"
        },
        "chapter_num": 7,
        "title": {
            "vi": "Chương 7: Phát triển Cơ sở Dữ liệu & Dữ liệu Khách hàng",
            "en": "Chapter 7: Database and Customer Data Development"
        },
        "pdf_page_start": 208,
        "book_page": 194,
        "learning_objectives": {
            "vi": [
                "Hiểu rõ thiết kế mô hình dữ liệu quan hệ (Relational Database) và cấu trúc sơ đồ hình sao (Star Schema).",
                "Nắm vững các kỹ thuật kiểm soát chất lượng dữ liệu (Data Quality Management).",
                "Phân tích vòng đời phát triển cơ sở dữ liệu khách hàng từ thu thập đến khai thác.",
                "Tuân thủ các nguyên tắc bảo mật và phân quyền truy cập dữ liệu nhạy cảm."
            ],
            "en": [
                "Understand relational database models and dimensional star-schema designs for CRM.",
                "Master enterprise Data Quality Management (DQM) controls.",
                "Analyze the customer database lifecycle from acquisition to deprecation.",
                "Enforce security protocols and role-based access controls for PII data."
            ]
        },
        "key_concepts": [
            {
                "term": "Star Schema",
                "name": { "vi": "Sơ đồ Hình sao (Star Schema)", "en": "Star Schema" },
                "definition": {
                    "vi": "Mô hình cấu trúc dữ liệu đa chiều gồm một bảng sự kiện trung tâm (Fact Table) chứa các chỉ số đo lường, liên kết với các bảng chiều (Dimension Tables) chứa thuộc tính khách hàng, thời gian, sản phẩm.",
                    "en": "A dimensional data warehouse architecture consisting of a central Fact Table holding quantitative metrics surrounded by Dimension Tables describing context."
                }
            },
            {
                "term": "Data Hygiene",
                "name": { "vi": "Vệ sinh Dữ liệu (Data Hygiene)", "en": "Data Hygiene" },
                "definition": {
                    "vi": "Các quy trình định kỳ nhằm rà soát, sửa lỗi chính tả, chuẩn hóa cú pháp, loại bỏ bản ghi rác và cập nhật thông tin địa chỉ khách hàng.",
                    "en": "Periodic data-cleansing routines to identify typos, standardize formats, eliminate obsolete records, and update moving addresses."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 7.1 Xây dựng Cơ sở Dữ liệu Khách hàng\nCơ sở dữ liệu khách hàng là 'trái tim' của CRM phân tích. Baran & Galka phân tích hai mô hình lưu trữ chủ đạo:\n- **Mô hình Quan hệ (Relational Model):** Sử dụng các khóa chính (Primary Key) và khóa ngoại (Foreign Key) để chuẩn hóa dữ liệu (3NF), tránh dư thừa dữ liệu.\n- **Mô hình Đa chiều (Dimensional Model / Star Schema):** Tối ưu cho việc truy vấn kinh doanh. Ví dụ: Bảng Fact ghi nhận doanh số giao dịch, được bao quanh bởi các Dimension: Thời gian (Date), Khách hàng (Customer), Kênh bán hàng (Channel), và Sản phẩm (Product).\n\n### 7.2 Vệ sinh Dữ liệu (Data Hygiene) và Suy thoái Dữ liệu (Data Decay)\nMỗi năm, trung bình khoảng 15-20% dữ liệu khách hàng bị 'chết' hoặc lỗi thời do khách hàng chuyển nhà, đổi số điện thoại, đổi việc làm hoặc qua đời. Nếu không có quy trình bảo dưỡng dữ liệu thường xuyên, doanh nghiệp sẽ lãng phí ngân sách tiếp thị và gửi thông điệp đến sai đối tượng.",
            "en": "### 7.1 Customer Database Architecture\nThe customer database is the intellectual heart of analytical CRM. Baran & Galka examine two dominant structures:\n- **Relational Normalized Models (3NF):** Designed with Primary and Foreign Keys to eradicate transactional redundancy.\n- **Dimensional Models (Star Schema):** Optimized for high-speed business intelligence. A central Fact Table (transaction dollars, units sold) is encircled by Dimension Tables (Customer, Time, Geography, Product).\n\n### 7.2 Data Decay & Hygiene Routines\nCustomer databases degrade naturally at a rate of 15–20% annually due to residential relocations, career changes, email abandoned accounts, and mortality. Without automated hygiene schedules (e.g. National Change of Address - NCOA matching), corporate marketing waste compounds rapidly."
        },
        "key_takeaways": {
            "vi": [
                "Suy thoái dữ liệu là quy luật tự nhiên (15-20%/năm); duy trì vệ sinh dữ liệu là nhiệm vụ định kỳ bắt buộc.",
                "Sơ đồ hình sao (Star Schema) là cấu trúc tối ưu cho việc phân tích dữ liệu đa chiều trong CRM."
            ],
            "en": [
                "Data decays at 15–20% annually; routine data hygiene is mandatory to preserve database efficacy.",
                "Star Schema dimensional modeling enables rapid, intuitive multi-dimensional slice-and-dice analytics."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-b07-01",
                "question": {
                    "vi": "Hiện tượng suy thoái dữ liệu (Data Decay) là gì? Doanh nghiệp cần triển khai các biện pháp kỹ thuật nào để kiểm soát chất lượng dữ liệu?",
                    "en": "What is Data Decay? What technical controls must an enterprise implement to maintain data quality?"
                },
                "model_answer": {
                    "vi": "Data Decay là hiện tượng thông tin khách hàng bị lỗi thời theo thời gian. Doanh nghiệp cần triển khai: xác thực dữ liệu ngay tại điểm nhập liệu (form validation), đối chiếu định kỳ với cơ sở dữ liệu thay đổi địa chỉ quốc gia, và tự động gửi email xác nhận thông tin định kỳ.",
                    "en": "Data decay is the progressive obsolescence of customer records. Firms combat it through front-end input validation, regular NCOA registry verification, and automated profile re-engagement workflows."
                }
            }
        ],
        "source": {
            "document": "Customer Relationship Management (Baran & Galka 2017)",
            "chapter": "Chapter 7",
            "pages": "208-238 (Book pp. 194-223)",
            "evidence_type": "source-derived"
        }
    },

    # --- KOSTOJOHN ET AL. CHAPTERS 3 & 4 ---
    {
        "id": "mod-fund-ch03",
        "book_id": "TB-KOSTOJOHN-2011",
        "book_title": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
        "chapter_num": 3,
        "title": {
            "vi": "Chương 3: Xây dựng Lộ trình CRM (Building a CRM Roadmap)",
            "en": "Chapter 3: Building a CRM Roadmap"
        },
        "pdf_page_start": 61,
        "book_page": 47,
        "learning_objectives": {
            "vi": [
                "Giải thích lý do tại sao phương pháp tiếp cận theo giai đoạn (Phased Approach) luôn vượt trội so với cách tiếp cận 'Big Bang'.",
                "Nắm vững quy trình 5 bước xây dựng lộ trình CRM từ 1 đến 3 năm.",
                "Áp dụng ma trận Ưu tiên Giá trị vs. Độ phức tạp (Value vs. Complexity Matrix).",
                "Điều chỉnh và thích ứng lộ trình khi doanh nghiệp gặp biến động chiến lược giữa chặng đường."
            ],
            "en": [
                "Explain why a Phased Approach systematically outperforms high-risk 'Big Bang' deployments.",
                "Master the 5-step process for developing a rolling 1- to 3-year CRM roadmap.",
                "Apply the Value vs. Complexity Prioritization Matrix to sequence initiative releases.",
                "Adapt and recalibrate roadmaps midstream when strategic conditions pivot."
            ]
        },
        "key_concepts": [
            {
                "term": "Phased Implementation Approach",
                "name": { "vi": "Cách tiếp cận Triển khai theo Giai đoạn", "en": "Phased Implementation Approach" },
                "definition": {
                    "vi": "Phương pháp chia nhỏ dự án CRM tổng thể thành nhiều đợt phát hành ngắn hạn (mỗi đợt 3-6 tháng), mang lại giá trị nhanh và giảm thiểu rủi ro.",
                    "en": "A deployment strategy breaking the comprehensive CRM scope into manageable 3- to 6-month release cycles to deliver rapid ROI and mitigate risk."
                }
            },
            {
                "term": "Value vs. Complexity Matrix",
                "name": { "vi": "Ma trận Giá trị vs. Độ phức tạp", "en": "Value vs. Complexity Matrix" },
                "definition": {
                    "vi": "Công cụ phân loại các tính năng CRM dựa trên giá trị kinh doanh mang lại và mức độ khó khăn kỹ thuật để ưu tiên các 'thắng lợi nhanh' (Quick Wins).",
                    "en": "A strategic prioritization framework plotting CRM initiatives by business value against implementation complexity to capture 'Quick Wins'."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 3.1 Tại sao phải Tiếp cận theo Giai đoạn (Phased Approach)?\nKostojohn et al. cảnh báo về cám dỗ chết người của việc cố gắng hiện thực hóa toàn bộ tầm nhìn CRM chỉ trong một đợt phát hành duy nhất (cách tiếp cận 'Big Bang'). Big Bang đòi hỏi thời gian triển khai 12-18 tháng mà không mang lại kết quả thực tế nào trong thời gian đó, khiến lãnh đạo mất kiên nhẫn và nhân viên nản lòng.\n\n### 3.2 Lợi thế của Lộ trình theo Giai đoạn\n1. *Thu hồi vốn đầu tư nhanh (Faster ROI):* Mỗi giai đoạn (3-6 tháng) đưa vào hoạt động một nhóm tính năng cốt lõi (ví dụ: Giai đoạn 1 triển khai SFA; Giai đoạn 2 triển khai Customer Service; Giai đoạn 3 tích hợp Marketing Automation).\n2. *Học hỏi và Tinh chỉnh:* Tổ chức rút kinh nghiệm từ phản hồi thực tế của người dùng ở Giai đoạn 1 để cải thiện thiết kế cho các giai đoạn tiếp theo.\n3. *Giảm thiểu rủi ro gián đoạn:* Không làm đảo lộn toàn bộ hoạt động kinh doanh cùng một lúc.\n\n### 3.3 Ma trận Ưu tiên Giá trị vs. Độ phức tạp\n- **Nhóm 1 - Giá trị Cao, Độ phức tạp Thấp (Quick Wins):** Ưu tiên triển khai ngay trong Giai đoạn 1 để tạo động lực và chứng minh hiệu quả.\n- **Nhóm 2 - Giá trị Cao, Độ phức tạp Cao (Strategic Bets):** Lên kế hoạch kỹ lưỡng, chia nhỏ thành các cấu phần để triển khai ở Giai đoạn 2 và 3.\n- **Nhóm 3 - Giá trị Thấp, Độ phức tạp Thấp (Low Hanging Fruit):** Triển khai khi có thời gian nhàn rỗi.\n- **Nhóm 4 - Giá trị Thấp, Độ phức tạp Cao (Money Pits):** Loại bỏ hoàn toàn khỏi phạm vi dự án.",
            "en": "### 3.1 The Flaw of the 'Big Bang' Approach\nKostojohn et al. caution against the seductive urge to implement an entire enterprise CRM vision in a monolithic 'Big Bang' rollout. Big Bangs require 12–18 months of development without interim business value, breeding executive cynicism and user fatigue.\n\n### 3.2 Virtues of the Phased CRM Roadmap\n1. *Rapid Value Realization:* 3- to 6-month release increments deploy tangible capabilities (e.g., Phase 1: Core SFA; Phase 2: Customer Service Desk; Phase 3: Omnichannel Marketing Automation).\n2. *Adaptive Learning Feedback:* User adoption feedback from Phase 1 directly informs Phase 2 UI configurations and data models.\n3. *Risk Mitigation:* Isolates organizational disruption to specific operational groups.\n\n### 3.3 The Value vs. Complexity Prioritization Matrix\n- **Quadrant 1 - High Value, Low Complexity (Quick Wins):** Fast-tracked in Phase 1 to build organizational momentum.\n- **Quadrant 2 - High Value, High Complexity (Strategic Investments):** Broken down and scheduled for Phase 2/3.\n- **Quadrant 3 - Low Value, Low Complexity (Fill-ins):** Opportunistic backlog candidates.\n- **Quadrant 4 - Low Value, High Complexity (Money Pits):** Ruthlessly purged from the roadmap."
        },
        "key_takeaways": {
            "vi": [
                "'Big Bang' là công thức dẫn đến thất bại; Lộ trình theo giai đoạn (Phased Roadmap) là chuẩn mực thành công.",
                "Luôn bắt đầu bằng các sáng kiến Giá trị Cao - Độ phức tạp Thấp để tạo 'chiến thắng nhanh'."
            ],
            "en": [
                "'Big Bang' is a recipe for disaster; a Phased Roadmap is the proven blueprint for enterprise CRM success.",
                "Prioritize High-Value / Low-Complexity 'Quick Wins' first to galvanize enterprise adoption."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-f03-01",
                "question": {
                    "vi": "So sánh cách tiếp cận Phased Approach và Big Bang Approach trong triển khai CRM. Làm thế nào để áp dụng ma trận Giá trị vs. Độ phức tạp để chọn tính năng cho Giai đoạn 1?",
                    "en": "Compare the Phased Approach and the Big Bang Approach in CRM rollouts. How should the Value vs. Complexity matrix be applied to select Phase 1 scope?"
                },
                "model_answer": {
                    "vi": "Phased Approach triển khai từng đợt ngắn 3-6 tháng giúp thu hồi vốn nhanh và giảm rủi ro; Big Bang kéo dài hơn 1 năm và dễ thất bại. Áp dụng ma trận: Giai đoạn 1 phải chọn các tính năng thuộc góc 'Giá trị cao - Độ phức tạp thấp' (ví dụ: quản lý danh bạ và phễu cơ hội cơ bản) để chứng minh hiệu quả tức thì cho ban lãnh đạo.",
                    "en": "Phased rollouts deliver rapid ROI every 3-6 months with iterative feedback, whereas Big Bangs accumulate massive untested risk. For Phase 1, strictly select 'High Value, Low Complexity' initiatives (e.g. core lead tracking) to prove immediate ROI and win executive buy-in."
                }
            }
        ],
        "source": {
            "document": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
            "chapter": "Chapter 3",
            "pages": "61-76 (Book pp. 47-62)",
            "evidence_type": "source-derived"
        }
    },
    {
        "id": "mod-fund-ch04",
        "book_id": "TB-KOSTOJOHN-2011",
        "book_title": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
        "chapter_num": 4,
        "title": {
            "vi": "Chương 4: Đánh giá Phần mềm & Lựa chọn Nhà tư vấn",
            "en": "Chapter 4: Evaluating Software and Consultants"
        },
        "pdf_page_start": 77,
        "book_page": 63,
        "learning_objectives": {
            "vi": [
                "Phân tích cấu trúc thị trường phần mềm CRM theo phân khúc: Enterprise, Mid-Market và Small Business.",
                "So sánh toàn diện giữa mô hình Điện toán đám mây (Cloud/SaaS) và Cài đặt tại chỗ (On-Premises).",
                "Thiết lập quy trình mời thầu (RFP) và chấm điểm giải pháp khách quan.",
                "Nhận diện các tiêu chí cốt lõi khi lựa chọn đối tác tư vấn triển khai và phòng tránh bẫy chi phí."
            ],
            "en": [
                "Segment the CRM software market into Enterprise, Mid-Market, and Small Business tiers.",
                "Execute a comprehensive trade-off analysis between Cloud/SaaS and On-Premises architectures.",
                "Structure Request for Proposal (RFP) processes and objective vendor scorecards.",
                "Establish consultant selection criteria and avoid contractual budget traps."
            ]
        },
        "key_concepts": [
            {
                "term": "Total Cost of Ownership (TCO)",
                "name": { "vi": "Tổng Chi phí Sở hữu (TCO)", "en": "Total Cost of Ownership (TCO)" },
                "definition": {
                    "vi": "Toàn bộ chi phí phát sinh trong suốt vòng đời sử dụng hệ thống CRM, bao gồm bản quyền phần mềm, hạ tầng phần cứng, phí tư vấn triển khai, bảo trì, đào tạo và nâng cấp.",
                    "en": "The holistic sum of all direct and indirect expenses incurred across the CRM lifecycle, including licensing, infrastructure, consulting, maintenance, and training."
                }
            },
            {
                "term": "Time-and-Materials vs. Fixed-Fee",
                "name": { "vi": "Hợp đồng Theo Thời gian & Vật liệu vs. Trọn gói", "en": "Time-and-Materials vs. Fixed-Fee" },
                "definition": {
                    "vi": "Hai mô hình hợp đồng tư vấn: Time-and-Materials tính phí theo số giờ công thực tế phát sinh; Fixed-Fee ấn định tổng chi phí cố định cho một phạm vi xác định.",
                    "en": "Consulting engagement models: Time-and-Materials bills actual hours expended; Fixed-Fee sets an absolute price cap for tightly bounded deliverables."
                }
            }
        ],
        "detailed_notes": {
            "vi": "### 4.1 Phân khúc Thị trường Phần mềm CRM\nKostojohn et al. chia thị trường CRM thành 3 phân khúc chính:\n1. *Enterprise Tier (Doanh nghiệp Lớn):* Các hệ thống như SAP CRM, Oracle Siebel, Salesforce Enterprise. Ưu điểm: Tùy biến cực kỳ sâu rộng, xử lý hàng triệu bản ghi phức tạp. Nhược điểm: Chi phí bản quyền và tư vấn khổng lồ, thời gian triển khai dài.\n2. *Mid-Market Tier (Doanh nghiệp Vừa):* Microsoft Dynamics CRM, Salesforce Professional, SugarCRM. Ưu điểm: Linh hoạt, dễ tích hợp với hệ sinh thái Microsoft/văn phòng, chi phí hợp lý.\n3. *Small Business Tier (Doanh nghiệp Nhỏ):* Các giải pháp chuyên biệt, triển khai nhanh, cấu hình đơn giản.\n\n### 4.2 Đánh giá Cloud/SaaS vs. On-Premises\n- **Cloud/SaaS:** Không cần mua máy chủ, cập nhật tính năng tự động, chi phí trả theo tháng/năm (OPEX). Phù hợp với đa số doanh nghiệp hiện đại.\n- **On-Premises:** Dữ liệu nằm hoàn toàn trong trung tâm dữ liệu nội bộ. Thường được các ngân hàng hoặc cơ quan chính phủ có quy định bảo mật gắt gao lựa chọn, nhưng đòi hỏi đội ngũ IT chuyên trách bảo trì phần cứng và sao lưu.\n\n### 4.3 Cạm bẫy khi Thuê Nhà Tư vấn Triển khai\nPhần lớn hợp đồng tư vấn CRM được ký theo dạng **Time-and-Materials (T&M)** vì phạm vi ban đầu không thể chi tiết 100%. Rủi ro lớn nhất là đối tác tư vấn cố tình báo giá thấp (underbidding) để thắng thầu, sau đó liên tục phát sinh chi phí phát triển thêm (change orders). Doanh nghiệp cần thẩm định kỹ lịch sử thực hiện ngân sách (budget performance) của đối tác trong các dự án quá khứ.",
            "en": "### 4.1 CRM Software Market Segmentation\nKostojohn et al. stratify the vendor ecosystem into three tiers:\n1. *Enterprise Tier:* SAP, Oracle Siebel, Salesforce Enterprise. Strengths: near-infinite extensibility, multi-currency/multi-org scalability. Weaknesses: staggering TCO, protracted deployment cycles.\n2. *Mid-Market Tier:* Microsoft Dynamics CRM, Salesforce Professional. Strengths: balance of agility, deep desktop integration, and reasonable TCO.\n3. *Small Business Tier:* Lightweight contact managers with minimal customization overhead.\n\n### 4.2 Architectural Trade-Offs: Cloud vs. On-Premises\n- **Cloud/SaaS:** Low initial barriers, rapid provisioning, outsourced DR/backups, predictable OPEX.\n- **On-Premises:** Total governance over physical data sovereignty, preferred by defense or heavily regulated banking institutions, but burdened with ongoing IT maintenance and hardware refresh cycles.\n\n### 4.3 Mitigating Consulting Partner Risks\nMost enterprise CRM consulting engagements operate under **Time-and-Materials (T&M)** because initial requirements cannot be fully locked down. The chief pitfall is vendor underbidding—low-balling initial estimates to secure the contract, followed by an explosion of change orders. Buyers must audit a prospective partner's historical budget performance on comparable projects."
        },
        "key_takeaways": {
            "vi": [
                "Lựa chọn phần mềm phải dựa trên Tổng Chi phí Sở hữu (TCO) trong 3-5 năm chứ không chỉ nhìn vào phí bản quyền năm đầu.",
                "Hợp đồng Time-and-Materials đòi hỏi khách hàng phải kiểm soát chặt chẽ tiến độ và thẩm định năng lực thực tế của đối tác tư vấn."
            ],
            "en": [
                "Software selection must evaluate multi-year Total Cost of Ownership (TCO), not merely Year 1 subscription license fees.",
                "Time-and-Materials contracts mandate vigilant scope governance and historical budget performance vetting."
            ]
        },
        "review_questions": [
            {
                "q_id": "rev-f04-01",
                "question": {
                    "vi": "Phân tích ưu và nhược điểm của mô hình Cloud/SaaS so với On-Premises. Doanh nghiệp cần lưu ý những bẫy chi phí nào khi ký hợp đồng tư vấn triển khai dạng Time-and-Materials?",
                    "en": "Analyze the pros and cons of Cloud/SaaS vs. On-Premises. What cost pitfalls must firms watch for when entering Time-and-Materials consulting contracts?"
                },
                "model_answer": {
                    "vi": "Cloud/SaaS triển khai nhanh, không tốn chi phí phần cứng nhưng tốn phí thuê bao lâu dài. On-Premises kiểm soát dữ liệu tuyệt đối nhưng chi phí vận hành máy chủ rất đắt. Trong hợp đồng Time-and-Materials, bẫy lớn nhất là nhà tư vấn báo giá thấp để trúng thầu rồi sau đó kéo dài thời gian làm việc để thu thêm tiền. Doanh nghiệp cần đặt ra các mốc nghiệm thu (milestones) và kiểm soát chặt chẽ biên bản chấm công.",
                    "en": "Cloud/SaaS eliminates hardware CAPEX but incurs indefinite subscription OPEX. On-Premises gives sovereign data control but requires costly in-house infrastructure. In T&M contracts, the prime danger is vendor underbidding followed by billable hour inflation. Clients must institute strict milestone gates and time-tracking audits."
                }
            }
        ],
        "source": {
            "document": "CRM Fundamentals (Kostojohn, Johnson & Paulen 2011)",
            "chapter": "Chapter 4",
            "pages": "77-104 (Book pp. 63-90)",
            "evidence_type": "source-derived"
        }
    }
]

# Append new chapters to curriculum
for ch in new_chapters:
    if ch["id"] not in existing_ids:
        existing_curr.append(ch)
        existing_ids.add(ch["id"])

# Sort curriculum: Baran chapters then Kostojohn chapters
def sort_key(c):
    book_order = 0 if c["book_id"] == "TB-BARAN-2017" else 1
    return (book_order, c["chapter_num"])

existing_curr.sort(key=sort_key)

curr_file.write_text(json.dumps(existing_curr, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Curriculum successfully updated. Total chapters now: {len(existing_curr)}")
