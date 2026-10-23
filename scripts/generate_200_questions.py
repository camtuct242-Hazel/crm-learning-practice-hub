import json
from pathlib import Path

out_dir = Path(r"C:\Kiến thức cần học\CRM\output")
qb_path = out_dir / "data" / "question-bank.json"

# Helper to build question
def make_q(qid, exam_id, topic, diff, q_type, q_vi, q_en, opts, correct, exp_vi, exp_en, doc, ch, pages, tags):
    formatted_opts = []
    for opt_id, (opt_vi, opt_en) in opts.items():
        formatted_opts.append({
            "id": opt_id,
            "text": { "vi": opt_vi, "en": opt_en }
        })
    return {
        "id": qid,
        "exam_id": exam_id,
        "topic": topic,
        "difficulty": diff,
        "question_type": q_type,
        "question": { "vi": q_vi, "en": q_en },
        "options": formatted_opts,
        "correct_answer": correct,
        "explanation": { "vi": exp_vi, "en": exp_en },
        "source": { "document": doc, "chapter": ch, "pages": pages },
        "tags": tags,
        "validation_status": "verified"
    }

questions = []

# ==========================================
# EXAM 01: CRM FOUNDATIONS & STRATEGY (q-01-01 to q-01-20)
# ==========================================
exam1_data = [
    (
        "q-01-01", "CRM Foundations", "easy", "single_choice",
        "Theo Baran & Galka (2017), sự khác biệt căn bản nhất giữa Marketing Giao dịch và CRM là gì?",
        "According to Baran & Galka (2017), what is the most fundamental difference between Transactional Marketing and CRM?",
        {
            "A": ("Marketing giao dịch tập trung vào từng thương vụ riêng lẻ; CRM tập trung tối đa hóa Giá trị Vòng đời Khách hàng (CLV) qua mối quan hệ dài hạn.", "Transactional marketing focuses on discrete sales; CRM focuses on maximizing Customer Lifetime Value (CLV) through enduring relationships."),
            "B": ("Marketing giao dịch chỉ dành cho B2B; CRM chỉ dành cho B2C.", "Transactional marketing applies only to B2B; CRM applies solely to B2C."),
            "C": ("Marketing giao dịch dựa vào dữ liệu; CRM dựa vào cảm tính.", "Transactional marketing relies on data; CRM relies on intuition."),
            "D": ("CRM bắt buộc phải đối xử bình đẳng và chi phí bằng nhau cho mọi khách hàng.", "CRM mandates equal resource allocation to every single customer.")
        },
        "A",
        "Marketing giao dịch xem bán hàng là điểm kết thúc; CRM xem giao dịch đầu tiên là điểm khởi đầu để nuôi dưỡng quan hệ lâu dài.",
        "Transactional marketing treats the sale as an endpoint; CRM views it as the beginning of an ongoing relationship.",
        "Baran & Galka (2017)", "Chapter 1", "pp. 10-15", ["foundations", "transactional-vs-relational"]
    ),
    (
        "q-01-02", "Dimensions", "medium", "single_choice",
        "Hoạt động khai phá dữ liệu giao dịch thẻ để xây dựng mô hình dự báo tỷ lệ rời bỏ (churn) thuộc chiều kích nào của CRM?",
        "Mining credit card transactions to build customer churn prediction models falls under which CRM dimension?",
        {
            "A": ("CRM Tác nghiệp (Operational CRM)", "Operational CRM"),
            "B": ("CRM Phân tích (Analytical CRM)", "Analytical CRM"),
            "C": ("CRM Hợp tác (Collaborative CRM)", "Collaborative CRM"),
            "D": ("CRM Chiến lược đơn thuần", "Simple Strategic CRM")
        },
        "B",
        "CRM Phân tích chịu trách nhiệm khai phá dữ liệu hành vi để xây dựng mô hình dự báo và tối ưu hóa quyết định kinh doanh.",
        "Analytical CRM captures and mines customer behavioral data to build predictive intelligence models.",
        "Baran & Galka (2017)", "Chapter 1", "pp. 12-14", ["dimensions", "analytical-crm"]
    ),
    (
        "q-01-03", "Sources of Value", "medium", "single_choice",
        "Yếu tố nào sau đây KHÔNG phải là một trong bốn nguồn giá trị cốt lõi của CRM theo Kostojohn et al. (2011)?",
        "Which of the following is NOT one of the four core sources of CRM value according to Kostojohn et al. (2011)?",
        {
            "A": ("Hỗ trợ tổ chức học tập định hướng dữ liệu.", "Supporting a data-driven, learning organization."),
            "B": ("Loại bỏ sự lãng phí và nâng cao năng suất nhân viên.", "Wringing out inefficiencies and increasing employee productivity."),
            "C": ("Cung cấp trải nghiệm khách hàng vượt trội.", "Providing a better customer experience."),
            "D": ("Bảo đảm doanh thu tăng trưởng tự động mà không cần nhân sự giám sát.", "Guaranteeing automated revenue growth without human supervision.")
        },
        "D",
        "Bốn nguồn giá trị gồm: Học tập định hướng dữ liệu, Tăng năng suất, Trải nghiệm khách hàng và Cung cấp dữ liệu ra quyết định. CRM không bao giờ bảo đảm tăng trưởng tự động thiếu con người.",
        "The 4 sources are data-driven learning, productivity, customer experience, and decision support. CRM never guarantees automated growth without people.",
        "Kostojohn et al. (2011)", "Chapter 1", "pp. 15-20", ["kostojohn-ch1", "sources-of-value"]
    ),
    (
        "q-01-04", "Foundations", "easy", "single_choice",
        "Thành phần nào sau đây đại diện cho CRM Tác nghiệp (Operational CRM)?",
        "Which of the following represents an Operational CRM component?",
        {
            "A": ("Kho dữ liệu doanh nghiệp (Enterprise Data Warehouse).", "Enterprise Data Warehouse (EDW)."),
            "B": ("Tự động hóa lực lượng bán hàng (Sales Force Automation - SFA).", "Sales Force Automation (SFA)."),
            "C": ("Thuật toán phân cụm RFM.", "RFM clustering algorithms."),
            "D": ("Báo cáo dự báo churn đa biến.", "Multivariate churn prediction models.")
        },
        "B",
        "SFA tự động hóa các tác vụ trực tiếp tiếp xúc khách hàng của nhân viên bán hàng, là thành phần cốt lõi của CRM tác nghiệp.",
        "SFA automates customer-facing front-office sales workflows, representing core operational CRM.",
        "Baran & Galka (2017)", "Chapter 1", "pp. 12-13", ["operational-crm", "sfa"]
    ),
    (
        "q-01-05", "Customer Equity", "medium", "single_choice",
        "Theo Baran & Galka, 'Giá trị Tài sản Khách hàng' (Customer Equity) của một doanh nghiệp được định nghĩa là gì?",
        "According to Baran & Galka, how is a firm's 'Customer Equity' defined?",
        {
            "A": ("Tổng tài sản hữu hình ghi nhận trên bảng cân đối kế toán.", "Total physical assets recorded on the corporate balance sheet."),
            "B": ("Tổng giá trị vòng đời (CLV) được chiết khấu của tất cả các khách hàng hiện tại và tương lai của công ty.", "The discounted sum of the lifetime values (CLVs) of all current and prospective customers."),
            "C": ("Tổng doanh thu bán lẻ trong một năm tài chính.", "Total gross revenue generated in a single fiscal year."),
            "D": ("Giá trị vốn hóa thị trường của cổ phiếu công ty.", "The total stock market capitalization of the enterprise.")
        },
        "B",
        "Customer Equity là tổng giá trị hiện tại ròng của toàn bộ dòng lợi nhuận tương lai từ tất cả khách hàng của doanh nghiệp.",
        "Customer Equity is the aggregate discounted net present value of all future customer cash flows across the entire customer base.",
        "Baran & Galka (2017)", "Chapter 1", "pp. 24-26", ["customer-equity", "clv"]
    ),
    (
        "q-01-06", "Relationship Marketing", "hard", "single_choice",
        "Theo Lý thuyết Cam kết - Tin cậy của Morgan & Hunt (1994), hai biến số trung gian quan trọng nhất dẫn đến thành công của mối quan hệ là gì?",
        "In Morgan & Hunt's (1994) Commitment-Trust Theory, what are the two primary mediating variables driving relationship marketing success?",
        {
            "A": ("Chiết khấu giá và Quảng cáo khuyến mãi.", "Price discounts and Promotional advertising."),
            "B": ("Niềm tin (Trust) và Sự cam kết (Commitment).", "Trust and Relationship Commitment."),
            "C": ("Sức mạnh đàm phán và Sự phụ thuộc tài chính.", "Bargaining power and Financial dependency."),
            "D": ("Tốc độ giao hàng và Mẫu mã bao bì.", "Delivery speed and Packaging design.")
        },
        "B",
        "Morgan & Hunt khẳng định niềm tin và cam kết là hai trụ cột nền tảng quyết định sự hợp tác và giữ chân trong Marketing Mối quan hệ.",
        "Morgan & Hunt demonstrate that trust and commitment are the essential mediating pillars producing relationship marketing efficacy.",
        "Baran & Galka (2017)", "Chapter 3", "pp. 82-87", ["relationship-marketing", "trust-commitment"]
    ),
    (
        "q-01-07", "Relationship Bonds", "medium", "single_choice",
        "Loại liên kết mối quan hệ nào sau đây DỄ BỊ đối thủ cạnh tranh sao chép và phá vỡ nhất?",
        "Which type of relationship bond is EASIEST for competitors to duplicate and undermine?",
        {
            "A": ("Liên kết Xã hội (Social Bonds).", "Social Bonds."),
            "B": ("Liên kết Cấu trúc (Structural Bonds).", "Structural Bonds."),
            "C": ("Liên kết Tài chính (Financial Bonds).", "Financial Bonds."),
            "D": ("Liên kết Quy trình (Process Bonds).", "Process Bonds.")
        },
        "C",
        "Liên kết tài chính (giảm giá, tích điểm) rất dễ bị đối thủ phá vỡ bằng chính sách giá thấp hơn; liên kết cấu trúc là bền vững nhất.",
        "Financial bonds (price discounts, points) are easily undercut by price cuts; structural bonds create the most resilient moat.",
        "Baran & Galka (2017)", "Chapter 3", "pp. 90-94", ["relationship-bonds", "financial-bonds"]
    ),
    (
        "q-01-08", "Relationship Bonds", "hard", "single_choice",
        "Một nhà cung cấp phần mềm tích hợp cổng API trực tiếp vào hệ thống hoạch định tài nguyên (ERP) của khách hàng, tạo nên loại gắn kết nào?",
        "A software provider embeds an API directly into a client's ERP workflows, establishing which type of relationship bond?",
        {
            "A": ("Liên kết Tài chính (Financial Bond).", "Financial Bond."),
            "B": ("Liên kết Xã hội (Social Bond).", "Social Bond."),
            "C": ("Liên kết Cấu trúc (Structural Bond).", "Structural Bond."),
            "D": ("Liên kết Pháp lý đơn thuần.", "Pure Legal Bond.")
        },
        "C",
        "Liên kết cấu trúc được hình thành khi hệ thống kỹ thuật và quy trình của hai bên được tích hợp sâu, tạo chi phí chuyển đổi (Switching Costs) rất cao.",
        "Structural bonds arise when technical architectures and workflows are embedded, erecting prohibitive switching costs.",
        "Baran & Galka (2017)", "Chapter 3", "pp. 92-95", ["structural-bonds", "switching-costs"]
    ),
    (
        "q-01-09", "CEC", "medium", "single_choice",
        "Điểm khác biệt cốt lõi giữa Customer Engagement Center (CEC) hiện đại và Contact Center truyền thống là gì?",
        "What is the defining distinction between a modern Customer Engagement Center (CEC) and a traditional Contact Center?",
        {
            "A": ("CEC chỉ xử lý cuộc gọi thoại; Contact Center xử lý email.", "CEC handles only voice calls; Contact Center handles email."),
            "B": ("CEC hợp nhất toàn bộ các kênh thoại, chat, mạng xã hội, ứng dụng trên một màn hình duy nhất cho nhân viên dịch vụ theo thời gian thực.", "CEC unifies voice, chat, social, and mobile into a single real-time agent desktop view."),
            "C": ("CEC hoàn toàn sa thải nhân viên con người để thay bằng chatbot.", "CEC completely eliminates human staff in favor of automated bots."),
            "D": ("CEC không lưu trữ lịch sử tương tác trước đây của khách hàng.", "CEC maintains zero historical interaction logs.")
        },
        "B",
        "CEC cung cấp góc nhìn hợp nhất đa kênh trên một giao diện duy nhất, đảm bảo tính liền mạch của dữ liệu khi khách hàng chuyển kênh.",
        "CEC integrates all communication channels into a single consolidated agent desktop with real-time customer context.",
        "Baran & Galka (2017)", "Chapter 1", "pp. 21-23", ["cec", "omnichannel"]
    ),
    (
        "q-01-10", "History", "easy", "single_choice",
        "Giai đoạn nào trong lịch sử CRM chứng kiến sự ra đời của các công cụ Tự động hóa Lực lượng Bán hàng (SFA) trên máy tính cá nhân?",
        "Which era in CRM history witnessed the inception of Sales Force Automation (SFA) tools on personal computers?",
        {
            "A": ("Thập niên 1970 với hệ thống máy tính lớn (Mainframe).", "1970s mainframe era."),
            "B": ("Thập niên 1990 với phần mềm quản lý liên hệ và SFA sơ khai.", "1990s client-server contact management era."),
            "C": ("Giai đoạn trước năm 1950.", "Pre-1950s ledger era."),
            "D": ("Giai đoạn bùng nổ mạng xã hội sau năm 2010.", "Post-2010 social networking boom.")
        },
        "B",
        "Thập niên 1990 đánh dấu sự xuất hiện của các phần mềm quản lý danh bạ và SFA nhằm giải phóng nhân viên bán hàng khỏi thủ tục giấy tờ.",
        "The 1990s ushered in PC contact management software and SFA to liberate sales reps from administrative paperwork.",
        "Baran & Galka (2017)", "Chapter 2", "pp. 52-58", ["crm-history", "sfa-origins"]
    ),
    (
        "q-01-11", "History", "medium", "single_choice",
        "Tại sao các dự án Enterprise CRM On-Premises trong giai đoạn 1995-2002 lại có tỷ lệ thất bại rất cao (50-70%)?",
        "Why did enterprise On-Premises CRM projects in 1995–2002 suffer catastrophic failure rates (50–70%)?",
        {
            "A": ("Do máy tính thời đó không có kết nối Internet.", "Because computers lacked Internet connectivity."),
            "B": ("Do doanh nghiệp quá chú trọng mua phần mềm đắt tiền mà bỏ qua chuẩn hóa quy trình, quản trị thay đổi và tỷ lệ chấp nhận của người dùng.", "Because firms over-invested in software while neglecting process re-engineering, change management, and user adoption."),
            "C": ("Do các phần mềm CRM thời đó hoàn toàn miễn phí nên không được coi trọng.", "Because CRM software was completely free, reducing organizational commitment."),
            "D": ("Do khách hàng thời kỳ này không quan tâm đến dịch vụ chăm sóc.", "Because consumers during that era were indifferent to customer service.")
        },
        "B",
        "Đầu tư công nghệ mà không chuẩn hóa quy trình và không có sự ủng hộ của nhân viên sử dụng là nguyên nhân chính gây thất bại.",
        "Purchasing expensive software without process standardization or front-line end-user buy-in caused widespread failure.",
        "Baran & Galka (2017)", "Chapter 2", "pp. 60-65", ["crm-history", "implementation-failures"]
    ),
    (
        "q-01-12", "Cloud CRM", "easy", "single_choice",
        "Mô hình Điện toán Đám mây (SaaS CRM) do Salesforce tiên phong từ năm 1999 đã thay đổi cơ cấu chi phí triển khai CRM như thế nào?",
        "How did the Cloud/SaaS CRM model pioneered by Salesforce in 1999 fundamentally alter CRM deployment cost structures?",
        {
            "A": ("Chuyển đổi từ chi phí đầu tư ban đầu lớn (CAPEX) sang chi phí vận hành định kỳ theo người dùng (OPEX).", "Converted heavy upfront capital expenditure (CAPEX) into predictable subscription operational expenditure (OPEX)."),
            "B": ("Bắt buộc doanh nghiệp phải mua thêm máy chủ vật lý đắt tiền.", "Forced enterprises to purchase more on-premise physical servers."),
            "C": ("Tăng chi phí bản quyền lên gấp 10 lần so với phần mềm On-Premises.", "Increased licensing costs by 10x compared to On-Premises systems."),
            "D": ("Ngăn chặn hoàn toàn việc tích hợp với các hệ thống khác.", "Prohibited integration with any third-party business software.")
        },
        "A",
        "SaaS CRM biến các khoản đầu tư máy chủ và giấy phép đắt đỏ thành phí thuê bao hàng tháng/hàng năm linh hoạt theo số người dùng.",
        "SaaS transformed prohibitive server/license CAPEX into flexible, per-seat subscription OPEX.",
        "Baran & Galka (2017)", "Chapter 2", "pp. 68-72", ["saas", "cloud-crm"]
    ),
    (
        "q-01-13", "Foundations", "medium", "single_choice",
        "Theo Kostojohn et al. (2011), yếu tố nào sau đây là điều kiện tiên quyết về mặt văn hóa để một tổ chức triển khai CRM thành công?",
        "According to Kostojohn et al. (2011), which cultural prerequisite is indispensable for successful CRM adoption?",
        {
            "A": ("Văn hóa ra quyết định hoàn toàn dựa vào kinh nghiệm cá nhân của giám đốc bán hàng.", "A culture relying exclusively on the sales director's gut instinct."),
            "B": ("Văn hóa định hướng dữ liệu (Data-Driven Culture) nơi quyết định được soi chiếu bằng chứng cứ thực tế.", "A Data-Driven Culture where decisions are informed by empirical evidence."),
            "C": ("Văn hóa cạnh tranh nội bộ gay gắt không chia sẻ danh bạ khách hàng giữa các phòng ban.", "A culture of aggressive internal competition where teams hoard customer lists."),
            "D": ("Văn hóa chấp nhận tỷ lệ thất thoát khách hàng cao để tìm kiếm khách hàng mới.", "A culture accepting high customer churn to chase new customer acquisition.")
        },
        "B",
        "Tổ chức phải xây dựng văn hóa định hướng dữ liệu thì nhân viên mới có động lực nhập dữ liệu chính xác và khai thác CRM hiệu quả.",
        "A data-driven culture is necessary so employees willingly maintain high data hygiene and leverage CRM intelligence.",
        "Kostojohn et al. (2011)", "Chapter 1", "pp. 20-22", ["data-driven-culture", "kostojohn-ch1"]
    ),
    (
        "q-01-14", "Executive Support", "easy", "single_choice",
        "Vai trò quan trọng nhất của 'Người bảo trợ Cấp cao' (Executive Sponsor) trong dự án CRM là gì?",
        "What is the most critical function of the Executive Sponsor in a CRM implementation?",
        {
            "A": ("Trực tiếp viết mã lập trình các tính năng tùy biến của phần mềm.", "Directly writing the custom code for software modules."),
            "B": ("Cung cấp thẩm quyền lãnh đạo, bảo vệ ngân sách, tháo gỡ xung đột chính trị và thúc đẩy sự chấp nhận của toàn tổ chức.", "Providing executive authority, defending funding, breaking political impasses, and mandating adoption."),
            "C": ("Trực tiếp đào tạo kỹ năng tin học văn phòng cho nhân viên bán hàng.", "Conducting remedial typing training for front-line sales staff."),
            "D": ("Tự tay cài đặt máy chủ và cấu hình tường lửa mạng nội bộ.", "Personally configuring on-premise server hardware and network firewalls.")
        },
        "B",
        "Executive Sponsor là lãnh đạo cấp cao đảm bảo nguồn lực, tháo gỡ rào cản liên phòng ban và truyền thông tầm nhìn cho dự án.",
        "The Executive Sponsor defends budgets, aligns cross-functional priorities, and mandates enterprise-wide system adoption.",
        "Kostojohn et al. (2011)", "Chapter 1 & 2", "pp. 21-25", ["executive-sponsor", "governance"]
    ),
    (
        "q-01-15", "Foundations", "hard", "single_choice",
        "Mô hình 'Chuỗi Lợi nhuận Khách hàng - Doanh nghiệp' (Customer-Company Profit Chain) khẳng định điều gì về mặt chiến lược?",
        "What does the 'Customer-Company Profit Chain' strategically assert regarding business value?",
        {
            "A": ("Sự hài lòng của khách hàng tự động dẫn đến lợi nhuận mà không cần kiểm soát chi phí phục vụ.", "Customer satisfaction automatically generates profit without managing cost-to-serve."),
            "B": ("Nâng cao sự hài lòng và lòng trung thành của khách hàng sẽ thúc đẩy tỷ lệ giữ chân, gia tăng chi tiêu trọn đời và tối ưu hóa lợi nhuận bền vững.", "Elevating customer satisfaction and loyalty drives retention, increasing lifetime revenues and enduring profitability."),
            "C": ("Lợi nhuận doanh nghiệp hoàn toàn độc lập với mức độ hài lòng của khách hàng.", "Firm profitability is completely decoupled from customer satisfaction metrics."),
            "D": ("Doanh nghiệp nên tối đa hóa doanh số ngắn hạn bằng cách cắt giảm toàn bộ chi phí chăm sóc sau bán.", "Firms should maximize short-term revenue by cutting all post-purchase customer support.")
        },
        "B",
        "Chuỗi lợi nhuận chỉ ra rằng giữ chân khách hàng thông qua sự hài lòng vượt trội là động cơ bền vững nhất của lợi nhuận dài hạn.",
        "The profit chain demonstrates that retention through superior customer value is the primary engine of sustainable profitability.",
        "Baran & Galka (2017)", "Chapter 1 & 9", "pp. 24-28, 270-275", ["profit-chain", "retention-economics"]
    ),
    (
        "q-01-16", "Strategy", "medium", "single_choice",
        "Thuật ngữ 'Share of Wallet' (Tỷ phần trong Ví) trong chiến lược phát triển khách hàng của CRM có nghĩa là gì?",
        "What does 'Share of Wallet' (SOW) signify in CRM customer development strategy?",
        {
            "A": ("Số lượng tiền mặt thực tế mà khách hàng mang trong ví khi đi mua sắm.", "The physical currency a customer carries when shopping."),
            "B": ("Tỷ lệ phần trăm tổng chi tiêu của khách hàng trong một danh mục sản phẩm được dành riêng cho thương hiệu của doanh nghiệp.", "The percentage of a customer's total spending in a category allocated to a specific firm."),
            "C": ("Khoản tiền giảm giá mà doanh nghiệp hoàn lại cho khách hàng.", "The cash rebate returned to a consumer via promotional coupons."),
            "D": ("Tổng số thẻ tín dụng mà một người tiêu dùng đang sở hữu.", "The total number of credit cards owned by a consumer.")
        },
        "B",
        "Share of Wallet đo lường mức độ thâm nhập của doanh nghiệp vào tổng ngân sách chi tiêu của khách hàng cho danh mục đó.",
        "Share of Wallet measures the percentage of a customer's total category spend captured by the enterprise.",
        "Baran & Galka (2017)", "Chapter 1 & 10", "pp. 30-32", ["share-of-wallet", "customer-development"]
    ),
    (
        "q-01-17", "Foundations", "easy", "single_choice",
        "Trong một dự án CRM, việc nhân viên bán hàng dùng sổ tay cá nhân hoặc file Excel riêng để lưu thông tin khách hàng là biểu hiện của vấn đề gì?",
        "In a CRM environment, sales reps maintaining private paper notebooks or rogue spreadsheets signifies what problem?",
        {
            "A": ("Khả năng bảo mật thông tin tuyệt đối của đội ngũ kinh doanh.", "Superior data security demonstrated by the sales team."),
            "B": ("Thiếu sự chấp nhận hệ thống (Poor User Adoption) và tình trạng phân mảnh dữ liệu khách hàng.", "Poor user adoption and rogue data fragmentation undermining the Single Customer View."),
            "C": ("Sự tuân thủ nghiêm ngặt quy trình làm việc theo chuẩn CRM.", "Strict adherence to standardized CRM workflows."),
            "D": ("Tiết kiệm chi phí lưu trữ cơ sở dữ liệu cho công ty.", "Prudent database storage cost savings for the IT department.")
        },
        "B",
        "Việc lưu trữ rời rạc bằng Excel chứng tỏ nhân viên không tin tưởng hoặc từ chối sử dụng CRM, làm suy giảm giá trị của cơ sở dữ liệu chung.",
        "Rogue spreadsheets indicate user resistance and data hoarding, defeating the purpose of an enterprise Single Customer View.",
        "Kostojohn et al. (2011)", "Chapter 1 & 2", "pp. 16-18", ["user-adoption", "data-silos"]
    ),
    (
        "q-01-18", "Strategy", "hard", "single_choice",
        "Một công ty viễn thông nhận thấy chi phí để thu hút một thuê bao mới là $150, trong khi chi phí để giữ chân thuê bao hiện tại chỉ là $25 mỗi năm. Nguyên lý kinh tế nào của CRM giải thích điều này?",
        "A telecom finds acquiring a new subscriber costs $150, whereas retaining an existing customer costs $25 annually. What CRM principle explains this disparity?",
        {
            "A": ("Nguyên lý Kinh tế học Giữ chân Khách hàng (Retention Economics): Chi phí thu hút luôn cao gấp 5-7 lần chi phí giữ chân.", "Retention Economics: Acquiring new accounts typically costs 5 to 7 times more than retaining existing relationships."),
            "B": ("Nguyên lý cân bằng doanh thu của thị trường độc quyền.", "The revenue parity principle of monopolistic markets."),
            "C": ("Quy luật phá sản của các công ty cung cấp dịch vụ hạ tầng mạng.", "The inevitable insolvency law of network infrastructure operators."),
            "D": ("Khách hàng cũ luôn tiêu ít tiền hơn khách hàng mới.", "Existing customers inherently spend less than new customers.")
        },
        "A",
        "Chi phí quảng cáo, hoa hồng môi giới và thiết lập hợp đồng ban đầu cho khách hàng mới rất đắt đỏ so với chi phí chăm sóc khách hàng quen.",
        "Acquisition involves heavy promotional overhead and onboarding costs, making customer retention dramatically more cost-efficient.",
        "Baran & Galka (2017)", "Chapter 1 & 10", "pp. 15-18", ["retention-economics", "cac"]
    ),
    (
        "q-01-19", "Foundations", "medium", "single_choice",
        "Theo Baran & Galka, khách hàng nào sau đây mang lại giá trị cao nhất cho doanh nghiệp trong dài hạn?",
        "According to Baran & Galka, which type of customer generates the greatest long-term value for an enterprise?",
        {
            "A": ("Khách hàng chỉ mua hàng khi có chương trình đại hạ giá cắt lỗ.", "Bargain-hunting switchers who only purchase during loss-leader clearance sales."),
            "B": ("Khách hàng trung thành thái độ (Attitudinal Loyalty), có CLV cao và chủ động giới thiệu thương hiệu cho người khác.", "Attitudinally loyal customers with high CLV who actively advocate the brand to peers."),
            "C": ("Khách hàng mua một đơn hàng khổng lồ một lần duy nhất rồi vĩnh viễn không quay lại.", "One-off buyers who make a single massive purchase and permanently defect."),
            "D": ("Khách hàng thường xuyên gọi điện phàn nàn và đòi bồi thường vô căn cứ.", "High-maintenance accounts that consume disproportionate support costs with frivolous claims.")
        },
        "B",
        "Khách hàng trung thành thái độ không chỉ mang lại dòng tiền ổn định mà còn đóng vai trò là 'đại sứ thương hiệu' giúp thu hút thêm khách hàng mới với CAC bằng 0.",
        "Attitudinally loyal customers provide recurring margin and generate zero-cost referral acquisition via positive advocacy.",
        "Baran & Galka (2017)", "Chapter 1 & 9", "pp. 25-28", ["attitudinal-loyalty", "brand-advocacy"]
    ),
    (
        "q-01-20", "Summary", "medium", "single_choice",
        "Một doanh nghiệp tuyên bố: 'Chúng tôi vừa hoàn thành dự án CRM vì đã cài đặt xong phần mềm Salesforce trên máy tính của tất cả nhân viên'. Nhận định này sai lầm ở điểm nào?",
        "A firm claims: 'We have finished our CRM initiative because Salesforce is now installed on all employee PCs.' What is the fundamental flaw in this claim?",
        {
            "A": ("Salesforce không phải là một phần mềm CRM.", "Salesforce is not an authentic CRM platform."),
            "B": ("Họ đã nhầm lẫn việc cài đặt công cụ công nghệ với một chiến lược kinh doanh toàn diện đòi hỏi chuyển đổi con người và quy trình.", "They confused software installation with an ongoing business strategy requiring people and process transformation."),
            "C": ("Họ bắt buộc phải cài đặt phần mềm trên điện thoại thay vì máy tính.", "They were required to install mobile apps rather than desktop interfaces."),
            "D": ("Dự án CRM chỉ được coi là hoàn thành khi sa thải toàn bộ đội ngũ bán hàng truyền thống.", "A CRM project is only complete when all traditional sales reps are terminated.")
        },
        "B",
        "CRM là một chiến lược kinh doanh và văn hóa lấy khách hàng làm trung tâm; công nghệ chỉ là công cụ hỗ trợ. Cài đặt phần mềm chỉ là bước khởi đầu.",
        "CRM is an overarching business strategy and culture; technology is merely an enabler. Software installation is just the starting point.",
        "Baran & Galka (2017) p. 9; Kostojohn (2011) p. 11", "Chapter 1", "pp. 9-11", ["crm-definition", "strategy-vs-tool"]
    )
]

for item in exam1_data:
    questions.append(make_q(
        item[0], "EXAM-01", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

print(f"Generated Exam 01 questions: {len(questions)}")
