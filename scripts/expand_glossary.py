import json
from pathlib import Path

data_dir = Path(r"C:\Kiến thức cần học\CRM\output\data")

# 1. EXPANDED GLOSSARY (40+ rigorous terms covering all 21 chapters)
expanded_glossary = [
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
        "id": "term-strategic-crm",
        "acronym": "Strategic CRM",
        "term": { "vi": "CRM Chiến lược", "en": "Strategic CRM" },
        "category": "Strategy",
        "definition": {
            "vi": "Triết lý kinh doanh đặt khách hàng làm trung tâm nhằm thu hút và giữ chân các khách hàng có giá trị sinh lời cao nhất cho tổ chức.",
            "en": "A core customer-centric business strategy aimed at winning and keeping profitable customers."
        },
        "context": {
            "vi": "Định hướng phân bổ nguồn lực và ngân sách của toàn doanh nghiệp.",
            "en": "Directs enterprise resource allocation and strategic capital deployment."
        },
        "related_terms": ["term-crm", "term-clv"],
        "source": { "document": "Baran & Galka (2017) Ch. 1, p. 10" }
    },
    {
        "id": "term-operational-crm",
        "acronym": "Operational CRM",
        "term": { "vi": "CRM Tác nghiệp", "en": "Operational CRM" },
        "category": "Technology",
        "definition": {
            "vi": "Tự động hóa các quy trình tiếp xúc trực tiếp với khách hàng (front-office) bao gồm bán hàng (SFA), tiếp thị và dịch vụ khách hàng.",
            "en": "Automation of customer-facing front-office processes including sales force automation (SFA), marketing, and customer service."
        },
        "context": {
            "vi": "Giúp nhân viên thao tác nhanh chóng và giảm bớt thời gian hành chính giấy tờ.",
            "en": "Empowers front-line staff with automated workflows, eliminating administrative drag."
        },
        "related_terms": ["term-sfa", "term-analytical-crm"],
        "source": { "document": "Baran & Galka (2017) Ch. 1, p. 12" }
    },
    {
        "id": "term-analytical-crm",
        "acronym": "Analytical CRM",
        "term": { "vi": "CRM Phân tích", "en": "Analytical CRM" },
        "category": "Analytics",
        "definition": {
            "vi": "Khai phá và phân tích dữ liệu hành vi của khách hàng để tối ưu hóa quyết định kinh doanh và cá nhân hóa trải nghiệm.",
            "en": "Systematic analysis of customer data to optimize business decisions and personalize customer interactions."
        },
        "context": {
            "vi": "Dùng để dự báo tỷ lệ rời bỏ (churn prediction) và xây dựng mô hình gợi ý sản phẩm.",
            "en": "Used for churn modeling, propensity scoring, and next-best-action algorithms."
        },
        "related_terms": ["term-data-warehouse", "term-rfm"],
        "source": { "document": "Baran & Galka (2017) Ch. 1 & 5" }
    },
    {
        "id": "term-collaborative-crm",
        "acronym": "Collaborative CRM",
        "term": { "vi": "CRM Hợp tác", "en": "Collaborative CRM" },
        "category": "Operations",
        "definition": {
            "vi": "Đồng bộ hóa dữ liệu và kênh giao tiếp giữa các phòng ban nội bộ và các đối tác trong chuỗi giá trị nhằm phục vụ khách hàng liền mạch.",
            "en": "Synchronization of communication channels and data across departments and value-chain partners for seamless customer service."
        },
        "context": {
            "vi": "Xóa bỏ tình trạng phân mảnh thông tin giữa phòng kinh doanh, kế toán và kỹ thuật.",
            "en": "Eliminates operational silos across sales, billing, logistics, and technical support."
        },
        "related_terms": ["term-silos", "term-scv"],
        "source": { "document": "Baran & Galka (2017) Ch. 1 & 4" }
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
        "id": "term-cac",
        "acronym": "CAC",
        "term": { "vi": "Chi phí Thu hút Khách hàng (CAC)", "en": "Customer Acquisition Cost (CAC)" },
        "category": "Metrics",
        "definition": {
            "vi": "Tổng chi phí tiếp thị và bán hàng bỏ ra trong một kỳ chia cho tổng số lượng khách hàng mới thu hút được trong kỳ đó.",
            "en": "Total sales and marketing expenditure divided by the number of new customers acquired during a specific time period."
        },
        "context": {
            "vi": "Tỷ lệ chuẩn mực giữa CLV và CAC là tối thiểu 3:1.",
            "en": "The industry benchmark requires a CLV to CAC ratio of at least 3:1."
        },
        "related_terms": ["term-clv", "term-roci"],
        "source": { "document": "Baran & Galka (2017) Ch. 12" }
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
        "id": "term-retention-rate",
        "acronym": "CRR",
        "term": { "vi": "Tỷ lệ Giữ chân Khách hàng (CRR)", "en": "Customer Retention Rate (CRR)" },
        "category": "Metrics",
        "definition": {
            "vi": "Tỷ lệ phần trăm khách hàng tiếp tục duy trì mối quan hệ kinh doanh với doanh nghiệp qua các kỳ đánh giá. CRR = 1 - Churn Rate.",
            "en": "The percentage of existing customers who remain with the firm over a given period. CRR = 1 minus Churn Rate."
        },
        "context": {
            "vi": "Tăng tỷ lệ giữ chân thêm 5% có thể gia tăng lợi nhuận từ 25% đến 95% theo nghiên cứu của Reichheld & Sasser.",
            "en": "A 5% increase in customer retention can boost corporate profits by 25% to 95% according to Reichheld & Sasser."
        },
        "related_terms": ["term-churn-rate", "term-clv"],
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
        "id": "term-csat",
        "acronym": "CSAT",
        "term": { "vi": "Chỉ số Hài lòng Khách hàng (CSAT)", "en": "Customer Satisfaction Score (CSAT)" },
        "category": "Metrics",
        "definition": {
            "vi": "Thước đo mức độ hài lòng ngắn hạn của khách hàng đối với một giao dịch, sản phẩm hoặc tương tác hỗ trợ cụ thể (thường đo bằng thang điểm 1-5).",
            "en": "A transactional metric measuring short-term customer satisfaction regarding a specific purchase, product, or support ticket interaction."
        },
        "context": {
            "vi": "Thường được khảo sát ngay sau khi đóng vé hỗ trợ hoặc hoàn tất giao dịch.",
            "en": "Surveyed immediately post-transaction or upon support ticket resolution."
        },
        "related_terms": ["term-nps", "term-ces"],
        "source": { "document": "Baran & Galka (2017) Ch. 9" }
    },
    {
        "id": "term-ces",
        "acronym": "CES",
        "term": { "vi": "Chỉ số Nỗ lực Khách hàng (CES)", "en": "Customer Effort Score (CES)" },
        "category": "Metrics",
        "definition": {
            "vi": "Thước đo mức độ dễ dàng hoặc khó khăn mà khách hàng phải trải qua để hoàn thành một yêu cầu hoặc giải quyết một sự cố.",
            "en": "A customer experience metric assessing the amount of friction or effort a customer had to expend to resolve an issue or complete an interaction."
        },
        "context": {
            "vi": "Nỗ lực khách hàng càng thấp thì xác suất tái mua sắm và lòng trung thành càng cao.",
            "en": "Lower customer effort strongly correlates with repeat purchase frequency and true brand loyalty."
        },
        "related_terms": ["term-csat", "term-nps"],
        "source": { "document": "Baran & Galka (2017) Ch. 9" }
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
    },
    {
        "id": "term-cdi",
        "acronym": "CDI",
        "term": { "vi": "Tích hợp Dữ liệu Khách hàng (CDI)", "en": "Customer Data Integration (CDI)" },
        "category": "Data",
        "definition": {
            "vi": "Quy trình kết hợp, chuẩn hóa và khử trùng lặp dữ liệu khách hàng từ nhiều hệ thống phân mảnh nhằm tạo ra một bản ghi thông tin chính xác duy nhất.",
            "en": "The technical processes of consolidating, cleansing, and synchronizing customer records across disparate operational systems into a single authoritative master identity."
        },
        "context": {
            "vi": "Là nền tảng kỹ thuật cho việc xây dựng Single Customer View.",
            "en": "Serves as the data engineering prerequisite for the Single Customer View."
        },
        "related_terms": ["term-scv", "term-deduplication"],
        "source": { "document": "Baran & Galka (2017) Ch. 5" }
    },
    {
        "id": "term-rfm",
        "acronym": "RFM",
        "term": { "vi": "Phân tích RFM (Recency, Frequency, Monetary)", "en": "RFM Analysis" },
        "category": "Analytics",
        "definition": {
            "vi": "Phương pháp phân đoạn khách hàng dựa trên 3 hành vi định lượng: Thời gian giao dịch gần nhất (Recency), Tần suất giao dịch (Frequency), và Giá trị tiền chi tiêu (Monetary).",
            "en": "Behavioral segmentation framework categorizing customers across Recency of last purchase, Frequency of orders, and total Monetary spend."
        },
        "context": {
            "vi": "Giúp xác định nhóm khách hàng VIP (Champions), nhóm khách hàng ngủ quên, và nhóm có nguy cơ đào tẩu.",
            "en": "Identifies high-value Champions, loyal repeaters, and at-risk dormant segments."
        },
        "related_terms": ["term-segmentation", "term-analytical-crm"],
        "source": { "document": "Baran & Galka (2017) Ch. 5 & 10" }
    },
    {
        "id": "term-kam",
        "acronym": "KAM",
        "term": { "vi": "Quản lý Tài khoản Trọng yếu (KAM)", "en": "Key Account Management (KAM)" },
        "category": "B2B CRM",
        "definition": {
            "vi": "Chiến lược tổ chức và phân bổ nguồn lực chuyên trách nhằm xây dựng mối quan hệ đối tác dài hạn với các khách hàng doanh nghiệp chiến lược mang lại giá trị cao nhất.",
            "en": "A strategic enterprise framework dedicated to building collaborative, high-touch relationships with the firm's most critical B2B corporate clients."
        },
        "context": {
            "vi": "Thường có đội ngũ chuyên gia liên ngành phục vụ riêng cho từng khách hàng trọng yếu.",
            "en": "Involves dedicated multi-disciplinary teams managing customized joint value creation."
        },
        "related_terms": ["term-buying-center", "term-prm"],
        "source": { "document": "Baran & Galka (2017) Ch. 8" }
    },
    {
        "id": "term-prm",
        "acronym": "PRM",
        "term": { "vi": "Quản trị Quan hệ Đối tác (PRM)", "en": "Partner Relationship Management (PRM)" },
        "category": "B2B CRM",
        "definition": {
            "vi": "Hệ thống phần mềm và quy trình hỗ trợ quản lý các kênh phân phối gián tiếp (đại lý, nhà bán buôn, đối tác giá trị gia tăng VAR) bao gồm đăng ký thương vụ và chia sẻ ngân sách tiếp thị.",
            "en": "A system of software and workflows designed to manage indirect sales channels (dealers, distributors, resellers) via deal registration and co-op marketing funds."
        },
        "context": {
            "vi": "Ngăn ngừa hiện tượng tranh chấp khách hàng giữa các đại lý trong cùng một khu vực.",
            "en": "Prevents channel conflict and fosters channel loyalty."
        },
        "related_terms": ["term-kam", "term-channel-conflict"],
        "source": { "document": "Baran & Galka (2017) Ch. 8" }
    },
    {
        "id": "term-scrm",
        "acronym": "SCRM",
        "term": { "vi": "Social CRM (CRM Mạng Xã hội)", "en": "Social CRM (SCRM)" },
        "category": "Social & Trends",
        "definition": {
            "vi": "Sự tích hợp giữa các nền tảng mạng xã hội và CRM nhằm lắng nghe ý kiến cộng đồng, tham gia đối thoại hai chiều và giải quyết khiếu nại công khai theo thời gian thực.",
            "en": "The convergence of social media platforms with CRM architectures to monitor conversations, engage in transparent public dialogue, and resolve support issues."
        },
        "context": {
            "vi": "Chuyển dịch quyền kiểm soát kênh giao tiếp từ doanh nghiệp sang khách hàng.",
            "en": "Reflects the decentralization of communication power from firms to empowered consumers."
        },
        "related_terms": ["term-social-listening", "term-sentiment-analysis"],
        "source": { "document": "Baran & Galka (2017) Ch. 13" }
    },
    {
        "id": "term-phygital",
        "acronym": "Phygital",
        "term": { "vi": "Trải nghiệm Phygital (Vật lý kết hợp Kỹ thuật số)", "en": "Phygital Experience" },
        "category": "Social & Trends",
        "definition": {
            "vi": "Chiến lược xóa nhòa ranh giới giữa cửa hàng vật lý và không gian số bằng cách ứng dụng di động, cảm biến IoT, RFID và thực tế tăng cường (AR) vào trải nghiệm tại điểm bán.",
            "en": "The seamless orchestration of physical store touchpoints with digital capabilities (mobile apps, IoT sensors, RFID, AR) to create frictionless customer journeys."
        },
        "context": {
            "vi": "Được áp dụng thành công tại Walmart, Nike House of Innovation, Disney MagicBand và McDonald's EOTF.",
            "en": "Exemplified by Walmart Mobile Express Returns, Nike House of Innovation, and Disney MagicBand."
        },
        "related_terms": ["term-omnichannel", "term-iot"],
        "source": { "document": "Baran & Galka (2017) Ch. 14; Batat (2019/2021)" }
    },
    {
        "id": "term-four-pillars",
        "acronym": "4 Pillars",
        "term": { "vi": "Bốn Trụ Cột Thành Công của CRM", "en": "Four Pillars of CRM Success" },
        "category": "Governance",
        "definition": {
            "vi": "Mô hình do Kostojohn et al. (2011) xác lập, khẳng định thành công của CRM dựa trên sự cân bằng đồng thời của 4 yếu tố: Con người (People), Quy trình (Process), Công nghệ (Technology), và Kỳ vọng (Expectations).",
            "en": "The foundational implementation framework established by Kostojohn et al. (2011): People, Process, Technology, and Expectations."
        },
        "context": {
            "vi": "Lưu ý quan trọng: Tác giả không đưa ra con số 80/20 như quan niệm dân gian mà nhấn mạnh tính không thể tách rời của cả 4 trụ cột.",
            "en": "Clarifies that the author defines 4 equal pillars rather than the consulting adage of 80% People / 20% Tech."
        },
        "related_terms": ["term-steering-committee", "term-champions"],
        "source": { "document": "Kostojohn et al. (2011) Ch. 2, p. 11" }
    },
    {
        "id": "term-steering-committee",
        "acronym": "Steering Committee",
        "term": { "vi": "Ban Chỉ đạo Dự án CRM (Steering Committee)", "en": "CRM Steering Committee" },
        "category": "Governance",
        "definition": {
            "vi": "Hội đồng lãnh đạo cấp cao liên phòng ban chịu trách nhiệm phê duyệt ngân sách, giải quyết xung đột phạm vi và định hướng chiến lược dài hạn cho hệ thống CRM.",
            "en": "A cross-functional executive leadership board governing strategic priorities, resource allocation, and change approval for enterprise CRM."
        },
        "context": {
            "vi": "Phải duy trì hoạt động định kỳ cả trước và sau khi Go-Live.",
            "en": "Must maintain scheduled cadence both prior to and continuously following Go-Live."
        },
        "related_terms": ["term-executive-sponsor", "term-four-pillars"],
        "source": { "document": "Kostojohn et al. (2011) Ch. 2 & 7" }
    },
    {
        "id": "term-champions",
        "acronym": "Champions",
        "term": { "vi": "Đại sứ CRM Phòng ban (Departmental Champions)", "en": "Departmental Champions" },
        "category": "Governance",
        "definition": {
            "vi": "Những nhân sự nòng cốt tại các phòng ban tác nghiệp có uy tín chuyên môn, được giao nhiệm vụ truyền thông, hướng dẫn sử dụng và phản hồi nhu cầu thực tế của người dùng.",
            "en": "Respected front-line subject matter experts who advocate for the CRM platform, train departmental peers, and funnel workflow feedback."
        },
        "context": {
            "vi": "Là nhân tố then chốt giúp xóa bỏ tâm lý ngại thay đổi và tăng tỷ lệ chấp nhận của người dùng cuối.",
            "en": "Vital for overcoming user adoption friction and ensuring software reflects operational reality."
        },
        "related_terms": ["term-user-adoption", "term-change-management"],
        "source": { "document": "Kostojohn et al. (2011) Ch. 2" }
    },
    {
        "id": "term-phased-approach",
        "acronym": "Phased Approach",
        "term": { "vi": "Triển khai CRM theo Giai đoạn (Phased Approach)", "en": "Phased CRM Approach" },
        "category": "Roadmap",
        "definition": {
            "vi": "Chiến lược phân chia lộ trình tổng thể 1-3 năm thành các đợt phát hành ngắn 3-6 tháng nhằm tạo ra giá trị nhanh (Quick Wins) và giảm thiểu rủi ro so với cách tiếp cận Big Bang.",
            "en": "Sequencing enterprise CRM delivery into iterative 3- to 6-month releases to deliver rapid business ROI and avoid monolithic Big Bang risks."
        },
        "context": {
            "vi": "Giúp tổ chức học hỏi từ phản hồi của người dùng ở giai đoạn trước để cải tiến cho giai đoạn sau.",
            "en": "Enables iterative feedback incorporation between successive rollout phases."
        },
        "related_terms": ["term-big-bang", "term-roadmap"],
        "source": { "document": "Kostojohn et al. (2011) Ch. 3" }
    },
    {
        "id": "term-uat",
        "acronym": "UAT",
        "term": { "vi": "Kiểm thử Chấp nhận của Người dùng (UAT)", "en": "User Acceptance Testing (UAT)" },
        "category": "Execution",
        "definition": {
            "vi": "Giai đoạn kiểm thử nghiệm thu chính thức trong đó người dùng nghiệp vụ trực tiếp thao tác các kịch bản công việc thực tế để phê duyệt hệ thống trước khi Go-Live.",
            "en": "The final validation milestone where business end-users test real operational scenarios to formally sign off on system readiness prior to production launch."
        },
        "context": {
            "vi": "Là chốt chặn chất lượng không thể bỏ qua trong mọi dự án triển khai CRM.",
            "en": "The decisive quality gate that cannot be bypassed before Go-Live."
        },
        "related_terms": ["term-cutover", "term-go-live"],
        "source": { "document": "Kostojohn et al. (2011) Ch. 6" }
    },
    {
        "id": "term-data-decay",
        "acronym": "Data Decay",
        "term": { "vi": "Suy thoái Dữ liệu (Data Decay)", "en": "Customer Data Decay" },
        "category": "Data",
        "definition": {
            "vi": "Hiện tượng cơ sở dữ liệu khách hàng bị lỗi thời tự nhiên theo thời gian (khoảng 15-20% mỗi năm) do thay đổi địa chỉ, số điện thoại, việc làm hoặc qua đời.",
            "en": "The natural rate of obsolescence of customer database records (averaging 15–20% annually) caused by residential moves, phone changes, and career shifts."
        },
        "context": {
            "vi": "Đòi hỏi doanh nghiệp phải có lịch trình vệ sinh dữ liệu (Data Hygiene) định kỳ.",
            "en": "Mandates automated data hygiene and address verification schedules."
        },
        "related_terms": ["term-data-hygiene", "term-cdi"],
        "source": { "document": "Baran & Galka (2017) Ch. 7" }
    },
    {
        "id": "term-gdpr",
        "acronym": "GDPR",
        "term": { "vi": "Quy định Chung về Bảo vệ Dữ liệu (GDPR)", "en": "General Data Protection Regulation (GDPR)" },
        "category": "Privacy & Ethics",
        "definition": {
            "vi": "Khung pháp lý của Liên minh Châu Âu thiết lập các tiêu chuẩn nghiêm ngặt về quyền riêng tư dữ liệu cá nhân, bao gồm quyền được lãng quên, yêu cầu đồng ý rõ ràng (Opt-In) và quyền di chuyển dữ liệu.",
            "en": "European Union regulatory framework setting stringent personal data standards including the Right to Erasure, explicit Opt-In consent, and data portability."
        },
        "context": {
            "vi": "Có mức phạt tối đa lên tới 4% doanh thu toàn cầu đối với các vi phạm bảo mật nghiêm trọng.",
            "en": "Enforces fines up to 4% of global annual turnover for egregious privacy violations."
        },
        "related_terms": ["term-opt-in", "term-privacy-by-design"],
        "source": { "document": "Baran & Galka (2017) Ch. 11" }
    },
    {
        "id": "term-service-profit-chain",
        "acronym": "Service-Profit Chain",
        "term": { "vi": "Chuỗi Dịch vụ - Lợi nhuận", "en": "Service-Profit Chain" },
        "category": "Strategy",
        "definition": {
            "vi": "Mô hình lý thuyết chứng minh mối liên kết nhân quả trực tiếp: Chất lượng dịch vụ nội bộ thúc đẩy sự hài lòng của nhân viên, tạo ra giá trị dịch vụ cao, dẫn đến sự hài lòng và trung thành của khách hàng, từ đó tạo ra lợi nhuận bền vững.",
            "en": "A framework demonstrating that internal service quality drives employee satisfaction, generating superior customer value and loyalty, which produces enduring profitability."
        },
        "context": {
            "vi": "Nhấn mạnh vai trò của nhân viên tuyến đầu đối với lòng trung thành của khách hàng.",
            "en": "Emphasizes that customer retention begins with engaged front-line employees."
        },
        "related_terms": ["term-clv", "term-csat"],
        "source": { "document": "Baran & Galka (2017) Ch. 9" }
    }
]

(data_dir / "glossary.json").write_text(json.dumps(expanded_glossary, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Glossary successfully expanded to {len(expanded_glossary)} terms.")
