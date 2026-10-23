import json
from pathlib import Path

glossary_path = Path("output/data/glossary.json")
with open(glossary_path, "r", encoding="utf-8") as f:
    terms = json.load(f)

existing_ids = {t["id"] for t in terms}

new_terms = [
    {
        "id": "term-cpm",
        "term": { "vi": "Quản trị Danh mục Khách hàng (CPM)", "en": "Customer Portfolio Management (CPM)" },
        "acronym": "CPM",
        "category": "Strategy",
        "definition": {
            "vi": "Quá trình phân tích, phân bổ và tối ưu hóa nguồn lực doanh nghiệp cho các nhóm khách hàng khác nhau dựa trên giá trị vòng đời và tiềm năng sinh lời của từng nhóm.",
            "en": "The disciplined practice of analyzing, allocating, and optimizing corporate resources across differentiated customer segments based on their relative lifetime value and profit potential."
        },
        "operational_context": {
            "vi": "Giúp doanh nghiệp tránh phân bổ nguồn lực dàn trải, tập trung chi phí chăm sóc vào nhóm khách hàng sinh lời cao (Platinum/Gold) và tinh giản chi phí với nhóm ít sinh lời.",
            "en": "Prevents blanket service expenditures, aligning high-touch relationship investments with premium cohorts (Platinum/Gold) while streamlining servicing overhead for lower tiers."
        },
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 3", "pages": "pp. 68-75" }
    },
    {
        "id": "term-customer-equity",
        "term": { "vi": "Tài sản Khách hàng", "en": "Customer Equity" },
        "acronym": "CE",
        "category": "Economics & Metrics",
        "definition": {
            "vi": "Tổng giá trị hiện tại ròng (NPV) của toàn bộ Giá trị Vòng đời (CLV) của tất cả khách hàng hiện tại và tiềm năng trong tương lai của doanh nghiệp.",
            "en": "The aggregated net present value (NPV) of Customer Lifetime Values (CLV) across all current and prospective future customers of the enterprise."
        },
        "operational_context": {
            "vi": "Được coi là thước đo tối hậu đánh giá giá trị dài hạn của chiến lược tiếp thị và chăm sóc khách hàng của công ty.",
            "en": "Regarded as the ultimate forward-looking metric evaluating the long-term enterprise valuation created by relationship marketing strategies."
        },
        "formula": "Customer Equity = Sum of CLV of all customer cohorts",
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 10", "pages": "pp. 320-325" }
    },
    {
        "id": "term-edw",
        "term": { "vi": "Kho Dữ liệu Doanh nghiệp", "en": "Enterprise Data Warehouse (EDW)" },
        "acronym": "EDW",
        "category": "Data & Analytics",
        "definition": {
            "vi": "Kho lưu trữ dữ liệu trung tâm, tích hợp từ nhiều hệ thống tác nghiệp phân tán của toàn tổ chức, được chuẩn hóa và tối ưu hóa cho mục đích phân tích và ra quyết định.",
            "en": "A centralized data repository consolidating transactional telemetry across disparate operational systems, transformed and optimized for analytical querying and executive decision support."
        },
        "operational_context": {
            "vi": "Đóng vai trò là nền tảng để trích xuất dữ liệu cho CRM phân tích, xây dựng Chân dung khách hàng 360 độ và chạy các mô hình AI dự báo.",
            "en": "Forms the architectural foundation for analytical CRM data extraction, Single Customer View generation, and predictive machine learning models."
        },
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 5", "pages": "pp. 160-166" }
    },
    {
        "id": "term-data-mart",
        "term": { "vi": "Chợ Dữ liệu Chuyên biệt", "en": "Data Mart" },
        "acronym": "DM",
        "category": "Data & Analytics",
        "definition": {
            "vi": "Một tập con dữ liệu được trích xuất từ kho dữ liệu tổng thể (EDW) hoặc hệ thống tác nghiệp, được cấu trúc chuyên biệt để phục vụ nhu cầu phân tích của một phòng ban cụ thể (như Marketing Data Mart).",
            "en": "A departmental subset of an enterprise data warehouse, focused on a specific line of business or functional domain (e.g., Marketing Data Mart) to optimize query speed and analytical relevance."
        },
        "operational_context": {
            "vi": "Giúp các nhà phân tích marketing hoặc quản lý bán hàng truy vấn nhanh chóng các báo cáo chuyên sâu mà không làm ảnh hưởng đến hiệu năng của kho dữ liệu chính.",
            "en": "Enables departmental analysts to run intensive pipeline or campaign analytics without competing for compute bandwidth on the central enterprise warehouse."
        },
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 5", "pages": "pp. 162-167" }
    },
    {
        "id": "term-etl",
        "term": { "vi": "Quy trình Trích xuất, Biến đổi, Nạp dữ liệu", "en": "Extract, Transform, Load (ETL)" },
        "acronym": "ETL",
        "category": "Data Architecture",
        "definition": {
            "vi": "Quy trình kỹ thuật gồm ba bước: Trích xuất dữ liệu từ các hệ thống nguồn (Extract), Làm sạch và chuyển đổi định dạng (Transform), và Nạp vào kho dữ liệu CRM (Load).",
            "en": "A data integration pipeline comprising three sequential stages: extracting telemetry from disparate operational touchpoints, cleansing and transforming schemas, and loading consolidated records into analytical warehouses."
        },
        "operational_context": {
            "vi": "Là huyết mạch kỹ thuật đảm bảo dữ liệu đổ về CRM luôn sạch sẽ, chính xác, đồng nhất định dạng và phi trùng lặp.",
            "en": "The technical lifeblood ensuring data entering CRM data lakes is formatted, deduplicated, and validated against canonical master standards."
        },
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 5", "pages": "pp. 162-168" }
    },
    {
        "id": "term-sow",
        "term": { "vi": "Thị phần Chi tiêu", "en": "Share of Wallet (SOW)" },
        "acronym": "SOW",
        "category": "Customer Analytics",
        "definition": {
            "vi": "Tỷ lệ phần trăm ngân sách chi tiêu của khách hàng dành cho một thương hiệu cụ thể so với tổng số tiền khách hàng đó chi trả cho toàn bộ danh mục sản phẩm/dịch vụ đó.",
            "en": "The percentage of a customer's total category expenditure allocated to a specific enterprise brand relative to all competing options in that vertical."
        },
        "operational_context": {
            "vi": "Giúp phát hiện những khách hàng có tiềm năng ngân sách lớn nhưng mới chỉ chi một phần nhỏ cho công ty, từ đó thiết kế chiến dịch bán chéo và bán gia tăng.",
            "en": "Uncovers wallet expansion opportunities by highlighting accounts that spend heavily in the sector but allocate only a fraction to the firm."
        },
        "formula": "SOW (%) = (Chi tiêu cho Thương hiệu / Tổng Chi tiêu Toàn Ngành) * 100",
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 10", "pages": "pp. 322-328" }
    },
    {
        "id": "term-crv",
        "term": { "vi": "Giá trị Giới thiệu của Khách hàng", "en": "Customer Referral Value (CRV)" },
        "acronym": "CRV",
        "category": "Customer Economics",
        "definition": {
            "vi": "Giá trị kinh tế ròng bằng tiền được tạo ra từ những khách hàng mới được thu hút nhờ sự giới thiệu trực tiếp hoặc truyền miệng tích cực của một khách hàng hiện tại.",
            "en": "The net financial dollar contribution generated by new customers acquired directly through the positive word-of-mouth recommendations and referrals of an existing account."
        },
        "operational_context": {
            "vi": "Cho phép doanh nghiệp đánh giá đúng giá trị của các khách hàng có mức chi tiêu cá nhân khiêm tốn nhưng lại là 'đại sứ thương hiệu' mang về nhiều khách hàng lớn.",
            "en": "Ensures firms recognize the asset value of modest personal spenders who serve as potent evangelists, bringing high-margin accounts at zero acquisition cost."
        },
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 10", "pages": "pp. 320-326" }
    },
    {
        "id": "term-tco",
        "term": { "vi": "Tổng Chi phí Sở hữu", "en": "Total Cost of Ownership (TCO)" },
        "acronym": "TCO",
        "category": "Technology & Finance",
        "definition": {
            "vi": "Tổng hợp toàn bộ các chi phí trực tiếp và gián tiếp liên quan đến một hệ thống CRM trong suốt vòng đời dự án (thường là 3-5 năm), bao gồm bản quyền, phần cứng, tích hợp, đào tạo và bảo trì.",
            "en": "A comprehensive financial estimate aggregating all direct and indirect capital and operating expenditures incurred over the full CRM lifecycle (typically 3–5 years), including licenses, integration, training, and maintenance."
        },
        "operational_context": {
            "vi": "Ngăn chặn bẫy chỉ nhìn vào giá bản quyền ban đầu; bản quyền thường chỉ chiếm 20-30% TCO, phần lớn chi phí nằm ở khâu tích hợp, dữ liệu và quản trị con người.",
            "en": "Prevents executive blind spots during vendor selection, revealing that upfront license fees represent a minority slice compared to integration, customization, and continuous change enablement."
        },
        "source": { "document": "Kostojohn et al. (2011)", "chapter": "Chapter 4", "pages": "pp. 102-108" }
    },
    {
        "id": "term-api",
        "term": { "vi": "Giao diện Lập trình Ứng dụng", "en": "Application Programming Interface (API)" },
        "acronym": "API",
        "category": "Technology Architecture",
        "definition": {
            "vi": "Tập hợp các giao thức, định dạng và quy tắc chuẩn hóa cho phép các phần mềm độc lập giao tiếp và trao đổi dữ liệu tự động theo thời gian thực.",
            "en": "A standardized set of protocols, endpoints, and definitions that enable distinct software applications to communicate and synchronize data bidirectionally in real time."
        },
        "operational_context": {
            "vi": "Là cầu nối cho phép CRM kết nối với hệ thống kế toán ERP, cổng thanh toán, website thương mại điện tử và các ứng dụng di động bên ngoài.",
            "en": "The technical conduit integrating front-office CRM platforms with back-office ERP ledgers, payment gateways, e-commerce storefronts, and third-party SaaS ecosystems."
        },
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 6", "pages": "pp. 180-186" }
    },
    {
        "id": "term-rfp",
        "term": { "vi": "Bản Yêu cầu Báo giá / Giải pháp", "en": "Request for Proposal (RFP)" },
        "acronym": "RFP",
        "category": "Procurement & Planning",
        "definition": {
            "vi": "Tài liệu chi tiết do doanh nghiệp soạn thảo gửi đến các nhà cung cấp giải pháp CRM, mô tả các yêu cầu chức năng, phi chức năng, phạm vi và tiêu chí đánh giá lựa chọn phần mềm.",
            "en": "A structured document issued by an enterprise to prospective CRM software vendors and consulting partners, delineating functional requirements, technical specifications, and objective evaluation criteria."
        },
        "operational_context": {
            "vi": "Tạo ra thang đo khách quan để chấm điểm và so sánh các nhà cung cấp, tránh bị cuốn theo những bài thuyết trình bán hàng phi thực tế.",
            "en": "Establishes a rigorous scoring rubric for comparing competing proposals, ensuring selection teams assess operational fit rather than slick sales presentations."
        },
        "source": { "document": "Kostojohn et al. (2011)", "chapter": "Chapter 4", "pages": "pp. 82-90" }
    },
    {
        "id": "term-wbs",
        "term": { "vi": "Cơ cấu Phân chia Công việc", "en": "Work Breakdown Structure (WBS)" },
        "acronym": "WBS",
        "category": "Project Management",
        "definition": {
            "vi": "Sơ đồ phân rã có thứ bậc toàn bộ phạm vi dự án CRM thành các gói công việc nhỏ hơn, có thể quản lý, ước lượng thời gian, chi phí và phân công trách nhiệm rõ ràng.",
            "en": "A hierarchical decomposition of the total CRM project scope into discrete, manageable deliverables and work packages with explicit time, budget, and ownership bounds."
        },
        "operational_context": {
            "vi": "Là xương sống để lập tiến độ Gantt, xác định các mối quan hệ phụ thuộc và kiểm soát không bị bỏ sót các hạng mục công việc quan trọng.",
            "en": "The foundational artifact for project scheduling, critical path derivation, milestone sequencing, and scope verification."
        },
        "source": { "document": "Kostojohn et al. (2011)", "chapter": "Chapter 5", "pages": "pp. 125-132" }
    },
    {
        "id": "term-fcr",
        "term": { "vi": "Giải quyết ngay từ Lần tiếp xúc Đầu tiên", "en": "First-Contact Resolution (FCR)" },
        "acronym": "FCR",
        "category": "Service Operations",
        "definition": {
            "vi": "Tỷ lệ phần trăm các cuộc gọi hoặc yêu cầu hỗ trợ của khách hàng được giải quyết thỏa đáng ngay trong lần tương tác đầu tiên mà không cần gọi lại hoặc chuyển tuyến phức tạp.",
            "en": "The percentage of incoming customer service inquiries or support tickets resolved completely and satisfactorily during the initial interaction without requiring follow-up callbacks or transfers."
        },
        "operational_context": {
            "vi": "FCR cao vừa giúp tiết kiệm chi phí vận hành tổng đài, vừa là yếu tố thúc đẩy sự hài lòng và lòng trung thành của khách hàng mạnh mẽ nhất.",
            "en": "High FCR drives both operational cost efficiency and superior customer satisfaction, eliminating multi-agent bounce loops and customer frustration."
        },
        "formula": "FCR (%) = (Số yêu cầu giải quyết ngay lần đầu / Tổng số yêu cầu tiếp nhận) * 100",
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 11", "pages": "pp. 355-358" }
    },
    {
        "id": "term-aht",
        "term": { "vi": "Thời gian Xử lý Trung bình", "en": "Average Handle Time (AHT)" },
        "acronym": "AHT",
        "category": "Contact Center Metrics",
        "definition": {
            "vi": "Thời lượng trung bình của một tương tác dịch vụ khách hàng, bao gồm thời gian đàm thoại trực tiếp, thời gian chờ máy (hold) và thời gian hoàn tất thủ tục sau cuộc gọi (wrap-up time).",
            "en": "The average duration of a customer service interaction, summing talk time, hold time, and post-call administrative wrap-up documentation."
        },
        "operational_context": {
            "vi": "Là chỉ số đo hiệu năng tổng đài, nhưng cần cân bằng với chất lượng giải quyết vấn đề (FCR) để tránh việc nhân viên vội vàng cúp máy khiến khách hàng bức xúc.",
            "en": "A standard operational efficiency metric that must be balanced against resolution quality (FCR) to prevent agents from rushing callers and degrading service quality."
        },
        "formula": "AHT = (Tổng Thời gian Nói + Tổng Thời gian Chờ + Tổng Thời gian Ghi chú Sau gọi) / Tổng Số cuộc gọi",
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 11", "pages": "pp. 356-360" }
    },
    {
        "id": "term-hypercare",
        "term": { "vi": "Giai đoạn Hỗ trợ Tăng cường Sau Golive", "en": "Hypercare Period" },
        "acronym": "HYPERCARE",
        "category": "Project Execution",
        "definition": {
            "vi": "Khoảng thời gian từ 2 đến 6 tuần ngay sau khi hệ thống CRM Golive, trong đó đội dự án và các chuyên gia tư vấn túc trực hỗ trợ người dùng tại chỗ, xử lý sự cố ưu tiên cao và ổn định hóa quy trình.",
            "en": "An elevated support window spanning 2 to 6 weeks immediately following CRM production launch, featuring dedicated floor coaching, rapid incident triaging, and system stabilization."
        },
        "operational_context": {
            "vi": "Giúp người dùng giải tỏa tâm lý hoang mang trong những ngày đầu tiếp xúc với phần mềm mới, dập tắt các phản kháng tiêu cực và ổn định hóa vận hành trước khi bàn giao sang đội BAU.",
            "en": "Provides psychological safety for anxious end-users, ensuring minor operational teething troubles do not metastasize into widespread system rejection."
        },
        "source": { "document": "Kostojohn et al. (2011)", "chapter": "Chapter 6", "pages": "pp. 176-180" }
    },
    {
        "id": "term-bopis",
        "term": { "vi": "Mua Trực tuyến, Nhận tại Cửa hàng", "en": "Buy Online, Pick-up In-Store (BOPIS / Click-and-Collect)" },
        "acronym": "BOPIS",
        "category": "Omnichannel Retail",
        "definition": {
            "vi": "Mô hình bán lẻ omnichannel cho phép khách hàng duyệt và đặt mua hàng trên website hoặc ứng dụng di động, sau đó đến nhận hàng trực tiếp tại cửa hàng vật lý gần nhất.",
            "en": "An omnichannel retail fulfillment model allowing consumers to browse and purchase items via digital storefronts and collect their packaged orders in person at a local retail outlet."
        },
        "operational_context": {
            "vi": "Giúp khách hàng nhận hàng ngay trong ngày mà không mất phí ship, đồng thời tạo cơ hội cho cửa hàng vật lý bán thêm (upsell) các sản phẩm kèm theo khi khách đến nhận hàng.",
            "en": "Delivers instant gratification without freight delays, while creating valuable foot traffic that drives impulse add-on purchases at the physical counter."
        },
        "source": { "document": "Experiential Marketing (Batat 2019/2021)", "chapter": "Chapter 3", "pages": "pp. 87-92" }
    },
    {
        "id": "term-d2c",
        "term": { "vi": "Bán hàng Trực tiếp đến Người tiêu dùng", "en": "Direct-to-Consumer (D2C)" },
        "acronym": "D2C",
        "category": "Channel Strategy",
        "definition": {
            "vi": "Mô hình kinh doanh trong đó nhà sản xuất tiếp thị, bán và phân phối sản phẩm trực tiếp đến người tiêu dùng cuối cùng thông qua các kênh riêng (web, ứng dụng, cửa hàng flagship), bỏ qua các đại lý trung gian.",
            "en": "A commercial channel model where manufacturers market, sell, and fulfill products directly to end consumers via proprietary touchpoints, bypassing wholesale intermediaries and third-party dealers."
        },
        "operational_context": {
            "vi": "Giúp thương hiệu kiểm soát trọn vẹn dữ liệu hành vi của khách hàng, cá nhân hóa trải nghiệm và gia tăng đáng kể biên lợi nhuận ròng (như trường hợp của Nike Direct).",
            "en": "Enables brands to capture full first-party customer telemetry, protect brand identity, and capture full retail gross margins (exemplified by Nike Direct)."
        },
        "source": { "document": "Experiential Marketing (Batat 2019/2021)", "chapter": "Chapter 5", "pages": "pp. 131-143" }
    },
    {
        "id": "term-dark-patterns",
        "term": { "vi": "Mẫu Thiết kế Giao diện Đen / Lừa dối", "en": "Dark Patterns" },
        "acronym": "DP",
        "category": "Ethics & UX",
        "definition": {
            "vi": "Các thủ thuật thiết kế giao diện người dùng có chủ đích thao túng, đánh lừa hoặc ép buộc người dùng thực hiện các hành động có lợi cho doanh nghiệp nhưng bất lợi cho người dùng (như tự động thêm phí, khó hủy tài khoản).",
            "en": "Intentionally deceptive user interface and experience patterns engineered to nudge, mislead, or manipulate users into taking actions contrary to their intent (e.g., hidden subscriptions, forced continuity, disguised ads)."
        },
        "operational_context": {
            "vi": "Là hành vi bị nghiêm cấm trong các nguyên tắc đạo đức CRM hiện đại và đối mặt với các án phạt nặng nề từ các cơ quan quản lý bảo vệ người tiêu dùng quốc tế.",
            "en": "Represents an unethical betrayal of customer trust that triggers legal penalties under consumer protection statutes and permanently erodes brand equity."
        },
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 12", "pages": "pp. 390-395" }
    },
    {
        "id": "term-surveillance-capitalism",
        "term": { "vi": "Chủ nghĩa Tư bản Giám sát", "en": "Surveillance Capitalism" },
        "acronym": "SC",
        "category": "Ethics & Society",
        "definition": {
            "vi": "Hệ thống kinh tế số khai thác trải nghiệm riêng tư của con người làm nguyên liệu thô để thu thập dữ liệu hành vi (behavioral surplus), chuyển đổi thành các sản phẩm dự đoán và thao túng hành vi tiêu dùng.",
            "en": "An economic order that claims human personal experience as free raw material for behavioral data extraction, packaging insights into behavioral prediction products sold to commercial actors."
        },
        "operational_context": {
            "vi": "Đặt ra cảnh báo đạo đức sâu sắc cho các chuyên gia CRM: cần cân bằng giữa việc khai phá dữ liệu phục vụ khách hàng với việc tôn trọng quyền tự chủ và quyền riêng tư cá nhân.",
            "en": "Presents a foundational ethical challenge for CRM practitioners, delineating the line between customer-centric value creation and predatory behavioral surveillance."
        },
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 12", "pages": "pp. 392-398" }
    },
    {
        "id": "term-co-creation",
        "term": { "vi": "Đồng kiến tạo Giá trị", "en": "Value Co-Creation" },
        "acronym": "VCC",
        "category": "Relationship Marketing",
        "definition": {
            "vi": "Quá trình hợp tác chủ động giữa doanh nghiệp và khách hàng/đối tác nhằm cùng nhau thiết kế sản phẩm, cải tiến dịch vụ và tạo ra giá trị chung mà không một bên nào có thể đơn độc tạo ra.",
            "en": "A collaborative paradigm where enterprises and customers or developers jointly innovate, configure services, and generate mutual value across interactive ecosystems."
        },
        "operational_context": {
            "vi": "Biến khách hàng từ đối tượng tiếp thị thụ động thành những người đồng sáng tạo nhiệt huyết, củng cố lòng trung thành thái độ và tạo ra hiệu ứng mạng lưới tự sinh.",
            "en": "Transforms customers from passive targets into active brand collaborators, forging deep psychological ownership and catalyzing self-sustaining platform flywheels."
        },
        "source": { "document": "Experiential Marketing (Batat 2019/2021)", "chapter": "Chapter 1", "pages": "pp. 8-16" }
    },
    {
        "id": "term-nrr",
        "term": { "vi": "Tỷ lệ Duy trì Doanh thu Ròng", "en": "Net Revenue Retention (NRR)" },
        "acronym": "NRR",
        "category": "SaaS & Recurring Revenue",
        "definition": {
            "vi": "Tỷ lệ phần trăm doanh thu định kỳ được duy trì và tăng trưởng từ nhóm khách hàng hiện tại qua một khoảng thời gian, sau khi cộng doanh thu bán thêm/mở rộng và trừ đi doanh thu sụt giảm/hủy dịch vụ.",
            "en": "The percentage of recurring revenue retained from an existing customer cohort over a period, incorporating expansions (upsell/cross-sell) minus contractions and churn."
        },
        "operational_context": {
            "vi": "Là thước đo sức khỏe vàng trong mô hình B2B SaaS; NRR > 100% chứng minh doanh nghiệp tự tăng trưởng doanh thu ngay cả khi không có khách hàng mới.",
            "en": "The gold standard metric for recurring SaaS business health; an NRR exceeding 100% demonstrates organic compound growth powered entirely by existing cohort expansion."
        },
        "formula": "NRR (%) = [(Doanh thu Đầu kỳ + Mở rộng - Thu hẹp - Rời bỏ) / Doanh thu Đầu kỳ] * 100",
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 8 & 10", "pages": "pp. 252-256" }
    },
    {
        "id": "term-cab",
        "term": { "vi": "Hội đồng Cố vấn Thay đổi", "en": "Change Advisory Board (CAB)" },
        "acronym": "CAB",
        "category": "Governance & Maintenance",
        "definition": {
            "vi": "Ủy ban liên chức năng gồm đại diện kinh doanh, IT và quản lý dự án, chịu trách nhiệm thẩm định, ưu tiên và phê duyệt các yêu cầu thay đổi tính năng hoặc nâng cấp phần mềm CRM.",
            "en": "A cross-functional governance body comprising business leads, IT architects, and project managers responsible for reviewing, prioritizing, and approving system enhancement requests."
        },
        "operational_context": {
            "vi": "Đóng vai trò là bộ lọc bảo vệ hệ thống không bị phình to vô tội vạ hoặc phát sinh xung đột quy trình do các yêu cầu cá nhân thiếu kiểm soát.",
            "en": "Acts as an institutional gatekeeper preventing scope creep, managing technical debt, and ensuring customizations deliver documented commercial value."
        },
        "source": { "document": "Kostojohn et al. (2011)", "chapter": "Chapter 7", "pages": "pp. 218-223" }
    },
    {
        "id": "term-service-recovery-paradox",
        "term": { "vi": "Nghịch lý Khắc phục Dịch vụ", "en": "Service Recovery Paradox (SRP)" },
        "acronym": "SRP",
        "category": "Service Excellence",
        "definition": {
            "vi": "Hiện tượng thực nghiệm trong đó một khách hàng gặp phải sự cố dịch vụ nhưng sau đó được doanh nghiệp tiếp nhận, giải quyết thỏa đáng và đền bù vượt mong đợi có thể trở nên trung thành và hài lòng hơn cả một khách hàng chưa từng gặp sự cố nào.",
            "en": "The empirical phenomenon wherein a customer who experiences a service failure that is resolved with exceptional empathy and speed exhibits higher post-recovery loyalty than a customer who encountered zero service flaws."
        },
        "operational_context": {
            "vi": "Chứng minh giá trị sống còn của việc trao quyền cho nhân viên tuyến đầu và biến quy trình xử lý khiếu nại thành cơ hội gắn kết cảm xúc mạnh mẽ với khách hàng.",
            "en": "Highlights the strategic imperative of frontline empowerment, demonstrating that flawless service recovery humanizes the brand and converts disgruntled buyers into fervent apostles."
        },
        "source": { "document": "Baran & Galka (2017)", "chapter": "Chapter 9", "pages": "pp. 290-295" }
    }
]

added_count = 0
for nt in new_terms:
    if nt["id"] not in existing_ids:
        terms.append(nt)
        existing_ids.add(nt["id"])
        added_count += 1

with open(glossary_path, "w", encoding="utf-8") as f:
    json.dump(terms, f, ensure_ascii=False, indent=2)

print(f"Added {added_count} new terms. Total glossary terms now: {len(terms)}")
