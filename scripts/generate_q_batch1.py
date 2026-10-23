import json
from pathlib import Path

# Exam 01, 02, 03 question generator
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

questions_batch1 = []

# ==========================================
# EXAM 01: CRM FOUNDATIONS & STRATEGY (q-01-01 to q-01-20)
# ==========================================
e1 = [
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
        "Marketing giao dịch xem bán hàng là điểm kết thúc; CRM xem giao dịch đầu tiên là điểm khởi đầu để nuôi dưỡng quan hệ lâu dài nhằm gia tăng CLV.",
        "Transactional marketing treats the sale as an endpoint; CRM views it as the beginning of an ongoing relationship to maximize CLV.",
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
        "CRM Phân tích (Analytical CRM) xử lý, phân tích và mô hình hóa dữ liệu khách hàng (như mô hình dự báo churn, phân khúc RFM) để cung cấp tri thức kinh doanh.",
        "Analytical CRM captures, synthesizes, and models customer data (such as churn forecasting, RFM segmentation) to deliver business insights.",
        "Baran & Galka (2017)", "Chapter 1", "pp. 14-16", ["dimensions", "analytical-crm"]
    ),
    (
        "q-01-03", "Strategic Orientation", "medium", "single_choice",
        "Một công ty phần mềm triển khai trung tâm dịch vụ khách hàng (Customer Service Portal) đồng bộ dữ liệu giữa tổng đài và email. Đây là biểu hiện của khía cạnh CRM nào?",
        "A software company integrates its service portal so phone agents and email support access synchronized real-time data. This exemplifies which CRM dimension?",
        {
            "A": ("CRM Tác nghiệp (Operational CRM) và Hợp tác (Collaborative CRM)", "Operational CRM and Collaborative CRM"),
            "B": ("Chỉ là CRM Chiến lược thuần túy", "Pure Strategic CRM only"),
            "C": ("Marketing đại trà (Mass Marketing)", "Mass Marketing"),
            "D": ("Quản trị cơ sở dữ liệu phi quan hệ", "Non-relational Database Management")
        },
        "A",
        "Hệ thống portal và tổng đài tự động hóa quy trình hỗ trợ khách hàng (CRM Tác nghiệp) đồng thời chia sẻ thông tin liền mạch giữa các kênh tiếp xúc (CRM Hợp tác).",
        "Service portals automate support workflows (Operational CRM) while sharing synchronized customer context across touchpoints (Collaborative CRM).",
        "Baran & Galka (2017)", "Chapter 1", "pp. 12-16", ["operational-crm", "collaborative-crm"]
    ),
    (
        "q-01-04", "Customer Lifetime Value", "hard", "single_choice",
        "Khái niệm Giá trị Vòng đời Khách hàng (CLV) được định nghĩa chuẩn xác nhất là gì?",
        "How is Customer Lifetime Value (CLV) most rigorously defined in CRM literature?",
        {
            "A": ("Tổng doanh thu gộp mà khách hàng chi trả trong năm đầu tiên ký hợp đồng.", "The gross revenue paid by a customer during their initial contract year."),
            "B": ("Giá trị hiện tại ròng (NPV) của toàn bộ dòng lợi nhuận trong tương lai mà một khách hàng đóng góp cho doanh nghiệp trong suốt thời gian duy trì quan hệ.", "The net present value (NPV) of all future projected net profit cash flows generated by a customer over their entire relationship lifetime."),
            "C": ("Số tiền thưởng công ty chi trả cho nhân viên kinh doanh khi chốt hợp đồng thành công.", "The sales commission paid to representatives upon closing an account."),
            "D": ("Tổng chi phí quảng cáo đã chi ra để thu hút một khách hàng mới (CAC).", "The cumulative advertising expenditure incurred to acquire a single customer (CAC).")
        },
        "B",
        "CLV là tổng giá trị hiện tại ròng (chiết khấu theo lãi suất chiết khấu) của các dòng lợi nhuận biên ròng trong tương lai từ khách hàng sau khi trừ chi phí phục vụ và giữ chân.",
        "CLV represents the discounted net present value of all future margin contributions generated across the customer tenure, deducting servicing and retention costs.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 310-318", ["clv", "financial-metrics"]
    ),
    (
        "q-01-05", "Customer Equity", "hard", "single_choice",
        "Tài sản Khách hàng (Customer Equity) của một doanh nghiệp là:",
        "Customer Equity of a commercial enterprise is defined as:",
        {
            "A": ("Tổng vốn chủ sở hữu trên bảng cân đối kế toán tài chính.", "Total shareholder equity reported on the corporate financial balance sheet."),
            "B": ("Tổng giá trị vòng đời (CLV) của toàn bộ các khách hàng hiện tại và tiềm năng trong tương lai của doanh nghiệp.", "The aggregated Customer Lifetime Value (CLV) of all current and prospective future customers of the firm."),
            "C": ("Giá trị thị trường của thương hiệu theo định giá của sàn chứng khoán.", "The stock market enterprise capitalization of the corporate brand."),
            "D": ("Số lượng tài khoản đã đăng ký trên hệ thống website.", "The raw count of registered user accounts in the corporate web database.")
        },
        "B",
        "Tài sản Khách hàng (Customer Equity) phản ánh tổng CLV của toàn bộ cơ sở khách hàng của công ty, là thước đo giá trị dài hạn của chiến lược CRM.",
        "Customer Equity represents the sum total of lifetime values of all active and acquired customers, quantifying the enduring asset value created by CRM.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 320-325", ["customer-equity", "valuation"]
    ),
    (
        "q-01-06", "Evolution of Marketing", "medium", "single_choice",
        "Theo lịch sử phát triển của Marketing, thứ tự chuyển dịch trọng tâm chiến lược diễn ra như thế nào?",
        "According to marketing evolution, what is the chronological progression of strategic orientation?",
        {
            "A": ("Định hướng Sản xuất -> Định hướng Bán hàng -> Định hướng Marketing -> Định hướng Quan hệ Khách hàng (CRM)", "Production Orientation -> Sales Orientation -> Marketing Orientation -> Customer Relationship Orientation (CRM)"),
            "B": ("CRM -> Định hướng Sản xuất -> Định hướng Bán hàng -> Định hướng Sản phẩm", "CRM -> Production Orientation -> Sales Orientation -> Product Orientation"),
            "C": ("Định hướng Quan hệ -> Marketing đại trà -> Sản xuất tinh gọn -> Bán hàng cá nhân", "Relational Orientation -> Mass Marketing -> Lean Manufacturing -> Personal Selling"),
            "D": ("Bán lẻ đa kênh -> Bán buôn truyền thống -> Marketing trực tiếp -> Bán hàng giao dịch", "Omnichannel Retail -> Traditional Wholesale -> Direct Marketing -> Transactional Sales")
        },
        "A",
        "Doanh nghiệp đi từ tập trung tối đa sản lượng (Production), sang đẩy mạnh bán hàng (Sales), đến thấu hiểu nhu cầu thị trường (Marketing), và hiện nay là xây dựng quan hệ gắn kết sinh lời (CRM).",
        "Enterprises evolved from maximizing volume (Production), pushing units (Sales), meeting market needs (Marketing), to fostering profitable enduring relationships (CRM).",
        "Baran & Galka (2017)", "Chapter 1", "pp. 5-10", ["marketing-evolution", "strategy"]
    ),
    (
        "q-01-07", "Four Pillars", "hard", "single_choice",
        "Theo Kostojohn et al. (2011, tr. 11), Bốn Trụ cột của Thành công trong Dự án CRM (Four Pillars of CRM Success) bao gồm:",
        "According to Kostojohn et al. (2011, p. 11), the Four Pillars of CRM Success consist of:",
        {
            "A": ("Con người (People), Quy trình (Process), Công nghệ (Technology), và Kỳ vọng (Expectations)", "People, Process, Technology, and Expectations"),
            "B": ("Phần mềm, Cơ sở dữ liệu, Máy chủ đám mây, Ngân sách IT", "Software, Database, Cloud Servers, and IT Budget"),
            "C": ("Giám đốc điều hành, Phòng Bán hàng, Phòng Marketing, Bộ phận Kế toán", "CEO, Sales Department, Marketing Department, Accounting"),
            "D": ("Giá cả, Khuyến mãi, Phân phối, Sản phẩm (4Ps)", "Price, Promotion, Place, and Product (4Ps)")
        },
        "A",
        "Kostojohn et al. nhấn mạnh rằng công nghệ chỉ là một phần tư; thất bại thường xuất phát từ việc quản lý kỳ vọng yếu kém, con người thiếu động lực và quy trình nghiệp vụ rối ren.",
        "Kostojohn et al. establish that software is merely one quarter; CRM failures stem from unmanaged expectations, inadequate human adoption, and broken processes.",
        "Kostojohn et al. (2011)", "Chapter 1", "p. 11", ["four-pillars", "crm-governance"]
    ),
    (
        "q-01-08", "80-20 Consulting Folklore", "medium", "single_choice",
        "Nhận định '80% thành công của CRM phụ thuộc vào Con người và Quy trình, chỉ 20% phụ thuộc vào Công nghệ' được đánh giá như thế nào trong bối cảnh học thuật và nguồn tài liệu dự án?",
        "How is the claim '80% of CRM success depends on People and Process, and only 20% on Technology' evaluated in academic and project literature?",
        {
            "A": ("Là một định lý toán học chính thức được chứng minh trong tất cả các nghiên cứu của Kostojohn.", "An official mathematical theorem proven across all studies by Kostojohn."),
            "B": ("Là quy tắc kinh nghiệm (rule of thumb) phổ biến trong giới tư vấn nhấn mạnh vai trò quản trị thay đổi, nhưng nguồn gốc chính thức của Kostojohn (tr. 11) là Bốn Trụ cột bình đẳng (People, Process, Technology, Expectations).", "A popular consulting rule of thumb emphasizing change management, but the authoritative textbook framework (Kostojohn p. 11) establishes the Four Pillars (People, Process, Technology, Expectations)."),
            "C": ("Là quy định bắt buộc của tổ chức ISO đối với các nhà cung cấp phần mềm CRM.", "A mandatory ISO standard requirement for CRM technology vendors."),
            "D": ("Là phát biểu hoàn toàn sai lầm vì CRM 100% phụ thuộc vào việc chọn đúng nhà cung cấp giải pháp đám mây.", "A completely erroneous claim because CRM success is 100% determined by cloud vendor selection.")
        },
        "B",
        "Tài liệu làm rõ đây là kinh nghiệm tư vấn để cảnh báo việc sa đà vào công nghệ mà quên con người, trong khi sách gốc xác lập mô hình 4 trụ cột cân bằng.",
        "The project clarifies this folklore reminds managers of human-process primacy, while the core textbook establishes the balanced Four Pillars model.",
        "Kostojohn et al. (2011)", "Chapter 1", "p. 11", ["methodology", "consulting-folklore", "four-pillars"]
    ),
    (
        "q-01-09", "Tangible CRM Components", "medium", "single_choice",
        "Theo Kostojohn et al. (2011, tr. 14-22), các thành phần hữu hình cốt lõi của một hệ thống CRM bao gồm:",
        "According to Kostojohn et al. (2011, pp. 14-22), the tangible core components of a CRM system comprise:",
        {
            "A": ("Quản lý Liên hệ/Tài khoản, Quản lý Khách hàng tiềm năng, Quản trị Cơ hội Bán hàng, Báo cáo & Phân tích", "Contact/Account Management, Lead Management, Opportunity Management, and Reporting & Analytics"),
            "B": ("Hệ thống quản lý chuỗi cung ứng (SCM) và kiểm soát tồn kho kho bãi", "Supply Chain Management (SCM) and warehouse inventory control"),
            "C": ("Phần mềm chấm công, tính lương và tuyển dụng nhân sự", "HR time tracking, payroll processing, and talent acquisition software"),
            "D": ("Thiết kế đồ họa, biên tập video và quản trị mạng xã hội cá nhân", "Graphic design, video editing, and personal social media administration")
        },
        "A",
        "Hệ thống CRM hữu hình cung cấp các module chuẩn: Contact/Account (hồ sơ khách hàng), Lead (đầu mối), Opportunity (cơ hội kinh doanh), và Reporting (báo cáo dashboard).",
        "Tangible CRM suites center on foundational modules: Contact/Account records, Lead intake, Opportunity pipeline, and Business Reporting/Analytics.",
        "Kostojohn et al. (2011)", "Chapter 1", "pp. 14-22", ["tangible-components", "crm-modules"]
    ),
    (
        "q-01-10", "Strategic CRM Alignment", "medium", "single_choice",
        "Tại sao chiến lược CRM phải bắt nguồn từ chiến lược kinh doanh tổng thể của doanh nghiệp thay vì khởi xướng đơn độc từ phòng IT?",
        "Why must a CRM strategy originate from corporate business strategy rather than being initiated independently by the IT department?",
        {
            "A": ("Vì phòng IT không có quyền phê duyệt mua máy chủ.", "Because IT departments lack authority to purchase computer hardware."),
            "B": ("Vì CRM là phương tiện định hình lại trải nghiệm khách hàng và tạo lợi thế cạnh tranh; công nghệ phải phục vụ các mục tiêu doanh thu, giữ chân và phân khúc của doanh nghiệp.", "Because CRM reshapes customer experiences to drive competitive advantage; technology must serve business goals in revenue, retention, and segmentation."),
            "C": ("Vì nhà cung cấp phần mềm CRM từ chối ký hợp đồng trực tiếp với Trưởng phòng Công nghệ thông tin.", "Because CRM software vendors refuse to sign enterprise contracts with Chief Information Officers."),
            "D": ("Vì chi phí phần mềm CRM luôn được khấu hao vào ngân sách marketing của công ty.", "Because CRM license fees are always amortized under the marketing department's budget.")
        },
        "B",
        "CRM nếu không xuất phát từ định hướng kinh doanh sẽ biến thành một dự án công nghệ tốn kém nhưng người dùng không sử dụng và không mang lại giá trị gia tăng.",
        "Without corporate alignment, CRM degenerates into an expensive IT utility with poor user adoption and zero measurable commercial return.",
        "Baran & Galka (2017)", "Chapter 2", "pp. 35-42", ["strategic-crm", "business-alignment"]
    ),
    (
        "q-01-11", "Customer Portfolio Management", "hard", "single_choice",
        "Quản trị Danh mục Khách hàng (Customer Portfolio Management - CPM) trong CRM dựa trên nguyên lý then chốt nào?",
        "Customer Portfolio Management (CPM) in strategic CRM is predicated on which fundamental premise?",
        {
            "A": ("Tất cả mọi khách hàng đều có giá trị và tiềm năng đóng góp lợi nhuận như nhau.", "Every individual customer possesses identical profit potential and lifetime value."),
            "B": ("Khách hàng có giá trị và nhu cầu khác nhau rõ rệt; do đó doanh nghiệp phải phân bổ nguồn lực và chi phí phục vụ một cách có chọn lọc và tối ưu.", "Customers vary dramatically in value and behavioral needs; enterprises must allocate servicing resources selectively and optimally."),
            "C": ("Doanh nghiệp phải loại bỏ hoàn toàn các khách hàng mua hàng số lượng nhỏ ngay lập tức.", "Enterprises must immediately terminate all low-volume accounts without analysis."),
            "D": ("Chi phí giữ chân khách hàng (Retention Cost) luôn cố định bất kể giá trị đơn hàng.", "Customer retention costs remain mathematically fixed regardless of transaction size.")
        },
        "B",
        "CPM phân loại khách hàng thành các nhóm giá trị khác nhau (ví dụ: Platinum, Gold, Iron, Lead) để áp dụng chiến lược chăm sóc và mức độ đầu tư tương xứng.",
        "CPM segments customer bases into differentiated tiers to align costly relationship investments with customer profit potential.",
        "Baran & Galka (2017)", "Chapter 3", "pp. 68-75", ["cpm", "customer-segmentation"]
    ),
    (
        "q-01-12", "CRM ROI Expectations", "medium", "single_choice",
        "Một nguyên nhân phổ biến khiến ban lãnh đạo thất vọng về Tỷ suất sinh lời (ROI) của dự án CRM trong năm đầu tiên là gì?",
        "What is a common root cause of executive dissatisfaction with CRM ROI during the first year of rollout?",
        {
            "A": ("Nhân viên bán hàng sử dụng CRM quá nhiều khiến họ bỏ bê việc gặp gỡ khách hàng.", "Sales personnel use CRM so extensively that they neglect customer-facing meetings."),
            "B": ("Kỳ vọng lợi nhuận phi thực tế trong ngắn hạn và thiếu các chỉ số đo lường trung gian (leading indicators) như tỷ lệ chấp nhận của người dùng (adoption rate).", "Unrealistic short-term financial expectations and failure to track leading indicators such as user adoption and data accuracy."),
            "C": ("Giá bản quyền phần mềm CRM luôn giảm đi một nửa sau năm đầu tiên vận hành.", "Software licensing costs are automatically cut in half after the first year of operation."),
            "D": ("Dữ liệu khách hàng tự động biến mất sau 12 tháng kể từ ngày cài đặt.", "Customer data automatically self-deletes 12 months after system installation.")
        },
        "B",
        "Lợi ích tài chính của CRM có độ trễ; việc quản lý kỳ vọng (Expectations) đòi hỏi theo dõi các chỉ số hành vi trước khi thấy kết quả doanh thu và lợi nhuận ròng.",
        "CRM benefits exhibit substantial time lag; managing expectations requires tracking process leading indicators before bottom-line financial gains materialize.",
        "Kostojohn et al. (2011)", "Chapter 1 & 7", "pp. 23-26, 210-215", ["expectations", "roi", "governance"]
    ),
    (
        "q-01-13", "Relational Bonds", "hard", "single_choice",
        "Theo mô hình liên kết quan hệ trong CRM, 'Liên kết Cấu trúc' (Structural Bonds) được tạo lập thông qua:",
        "In relationship marketing frameworks, 'Structural Bonds' are primarily created through:",
        {
            "A": ("Việc tặng quà sinh nhật và gửi thiệp chúc mừng cho người đại diện mua hàng.", "Sending personalized birthday greetings and holiday gift baskets to purchasing agents."),
            "B": ("Việc tích hợp hệ thống phần mềm, trao đổi dữ liệu điện tử (EDI) và quy trình vận hành gắn chặt giữa hai tổ chức mà đối thủ khó sao chép.", "Integrating software systems, automated electronic data interchanges (EDI), and joint operating workflows between partner organizations that are hard to replicate."),
            "C": ("Việc giảm giá 5% cho các đơn hàng thanh toán bằng tiền mặt.", "Granting a 5% price concession on orders settled via immediate cash payment."),
            "D": ("Các cuộc trò chuyện thân mật ngoài giờ làm việc giữa nhân viên bán hàng và khách hàng.", "Informal social conversations between sales representatives and buyers outside office hours.")
        },
        "B",
        "Liên kết cấu trúc tạo ra rào cản chuyển đổi (switching costs) rất cao vì hai bên đã tích hợp sâu về mặt công nghệ, chuỗi cung ứng và quy trình xử lý thông tin.",
        "Structural bonds erect high switching barriers by intertwining technology, supply chain data, and collaborative operational workflows.",
        "Baran & Galka (2017)", "Chapter 2 & 8", "pp. 45-48, 240-244", ["relational-bonds", "switching-costs"]
    ),
    (
        "q-01-14", "CRM Business Case", "medium", "single_choice",
        "Khi xây dựng Bản thuyết minh kinh doanh (Business Case) cho dự án CRM, đâu là nhóm lợi ích định tính (intangible benefits) thường được ghi nhận?",
        "When constructing a CRM Business Case, which of the following represents an intangible benefit?",
        {
            "A": ("Giảm 15% chi phí giấy tờ in ấn văn phòng.", "A 15% reduction in office paper printing expenses."),
            "B": ("Cải thiện sự hài lòng và tinh thần gắn bó của nhân viên nhờ giảm thiểu các thao tác nhập liệu thủ công lặp đi lặp lại.", "Enhanced employee morale and satisfaction resulting from the elimination of redundant manual data entry."),
            "C": ("Gia tăng doanh số bán chéo thêm 2,5 triệu USD trong quý 3.", "A $2.5 million increase in cross-selling revenue during Q3."),
            "D": ("Tiết kiệm 50.000 USD phí duy trì hệ thống máy chủ cũ.", "Saving $50,000 in legacy server hardware maintenance fees.")
        },
        "B",
        "Các lợi ích vô hình (tinh thần nhân viên, trải nghiệm khách hàng mượt mà, văn hóa minh bạch) rất quan trọng dù khó quy đổi trực tiếp thành số tiền trên hóa đơn.",
        "Intangible benefits (user morale, brand trust, seamless internal collaboration) are vital value drivers despite being hard to measure in immediate cash metrics.",
        "Kostojohn et al. (2011)", "Chapter 3", "pp. 65-72", ["business-case", "intangible-benefits"]
    ),
    (
        "q-01-15", "Customer-Centric Culture", "easy", "single_choice",
        "Văn hóa 'Lấy khách hàng làm trung tâm' (Customer-Centricity) trong tổ chức đòi hỏi điều gì?",
        "A true 'Customer-Centric' organizational culture requires which of the following?",
        {
            "A": ("Mọi quyết định kinh doanh, cấu trúc quy trình và hệ thống khen thưởng phải được thiết kế xoay quanh nhu cầu và giá trị của khách hàng.", "Aligning all corporate decisions, workflow architectures, and incentive schemes around customer needs and value creation."),
            "B": ("Chỉ phòng chăm sóc khách hàng mới cần quan tâm đến trải nghiệm của khách hàng.", "Restricting customer satisfaction concerns exclusively to customer service department staff."),
            "C": ("Đáp ứng vô điều kiện mọi yêu cầu vô lý của bất kỳ khách hàng nào mà không cần xét đến chi phí.", "Fulfilling every irrational client demand unconditionally regardless of margin impact."),
            "D": ("Loại bỏ hoàn toàn chỉ tiêu doanh số và lợi nhuận khỏi đánh giá nhân sự.", "Completely removing sales quotas and profitability metrics from performance reviews.")
        },
        "A",
        "Lấy khách hàng làm trung tâm là sự chuyển dịch toàn diện về tư duy của toàn bộ công ty, chứ không phải là trách nhiệm riêng của phòng dịch vụ khách hàng.",
        "Customer-centricity is an enterprise-wide operating philosophy, not a segregated duty assigned solely to front-line customer care reps.",
        "Baran & Galka (2017)", "Chapter 2 & 4", "pp. 52-56, 110-115", ["customer-centricity", "culture"]
    ),
    (
        "q-01-16", "Lead vs Contact vs Account", "medium", "single_choice",
        "Trong thuật ngữ CRM chuẩn, sự khác biệt giữa 'Lead' (Khách hàng tiềm năng) và 'Contact' (Người liên hệ) là gì?",
        "In standardized CRM nomenclature, what differentiates a 'Lead' from a 'Contact'?",
        {
            "A": ("Lead là một người đã mua hàng nhiều năm; Contact là người vừa ghé thăm website.", "A Lead is an established account buyer; a Contact is an anonymous web visitor."),
            "B": ("Lead là đầu mối chưa được thẩm định tư cách mua hàng (unqualified); khi đã xác nhận nhu cầu và ngân sách, Lead sẽ được chuyển đổi thành Contact gắn với một Account cụ thể.", "A Lead is an unqualified prospect; once verified for budget and intent, it converts into a qualified Contact associated with a specific Account record."),
            "C": ("Lead chỉ áp dụng cho cá nhân B2C; Contact chỉ áp dụng cho doanh nghiệp B2B.", "Leads exist solely in B2C; Contacts exist solely in enterprise B2B."),
            "D": ("Không có bất kỳ sự khác biệt nào giữa hai khái niệm.", "There is no functional or conceptual difference between the two entities.")
        },
        "B",
        "Quá trình chuyển đổi (Lead Conversion) là cột mốc phân tách một đầu mối sơ khai với một khách hàng tiềm năng đã được xác thực thông tin và thẩm định cơ hội bán.",
        "Lead conversion marks the threshold where raw inquiry data is vetted and mapped into persistent relational tables (Account, Contact, Opportunity).",
        "Kostojohn et al. (2011)", "Chapter 1", "pp. 16-19", ["data-model", "lead-management"]
    ),
    (
        "q-01-17", "Opportunity Pipeline", "medium", "single_choice",
        "Trong module Quản lý Cơ hội (Opportunity Management), tỷ lệ phần trăm xác suất thành công (Win Probability) thường được gán cho:",
        "In CRM Opportunity Management pipelines, a deal's win probability percentage is typically assigned based on:",
        {
            "A": ("Tâm trạng cá nhân của nhân viên bán hàng vào ngày đầu tuần.", "The personal subjective mood of the account executive on Monday morning."),
            "B": ("Các giai đoạn cụ thể, có thể kiểm chứng được trong quy trình bán hàng (Sales Stages) mà cơ hội đã vượt qua.", "Verifiable objective milestone criteria satisfied within each sequential sales stage."),
            "C": ("Tổng số ký tự trong tên công ty của khách hàng.", "The total number of characters in the prospective client's corporate name."),
            "D": ("Mức độ thân thiết giữa giám đốc hai bên qua các bữa tiệc tối.", "The informal social rapport established between executive leaders at dinner parties.")
        },
        "B",
        "Quy trình bán hàng chuẩn xác định xác suất dựa trên các mốc khách quan (ví dụ: Đã gửi báo giá = 50%, Đã chốt điều khoản pháp lý = 90%).",
        "A rigorous sales methodology maps probability to documented exit criteria per milestone stage (e.g., proposal submitted = 50%, legal terms agreed = 90%).",
        "Kostojohn et al. (2011)", "Chapter 1 & 2", "pp. 18-21, 45-48", ["opportunity-pipeline", "sales-process"]
    ),
    (
        "q-01-18", "Customer Retention Economics", "hard", "single_choice",
        "Theo các nghiên cứu kinh điển về kinh tế học CRM được trích dẫn bởi Baran & Galka, tại sao chi phí thu hút khách hàng mới (CAC) thường cao gấp 5 đến 7 lần chi phí giữ chân khách hàng cũ?",
        "According to foundational CRM retention economics cited by Baran & Galka, why does Customer Acquisition Cost (CAC) typically exceed Customer Retention Cost by 5 to 7 times?",
        {
            "A": ("Vì khách hàng mới đòi hỏi chi phí quảng cáo, tiếp thị, hoa hồng thẩm định và làm quen hệ thống cao hơn rất nhiều so với khách hàng hiện tại đã có niềm tin và quy trình giao dịch ổn định.", "Because acquiring new prospects entails heavy advertising, prospecting commissions, and initial setup overhead, unlike existing accounts with established trust and automated reordering."),
            "B": ("Vì khách hàng cũ không bao giờ đòi hỏi chiết khấu giá hay hỗ trợ dịch vụ.", "Because existing customers never request price discounts or post-sales technical support."),
            "C": ("Vì các ngân hàng thương mại áp dụng phí giao dịch cao hơn cho người mua hàng mới.", "Because commercial banks levy punitive merchant transaction fees on new customers."),
            "D": ("Vì pháp luật yêu cầu doanh nghiệp phải đóng bảo hiểm cho mỗi hợp đồng khách hàng mới.", "Because corporate statutes mandate liability insurance premiums on all new customer contracts.")
        },
        "A",
        "Chi phí tiếp thị, quảng cáo, giới thiệu và xác thực tài khoản ban đầu cho khách hàng mới rất đắt đỏ so với chi phí duy trì quan hệ với khách hàng quen.",
        "Acquisition involves heavy promotional overhead and onboarding costs, making customer retention dramatically more cost-efficient.",
        "Baran & Galka (2017)", "Chapter 1 & 10", "pp. 15-18, 312-315", ["retention-economics", "cac"]
    ),
    (
        "q-01-19", "Attitudinal vs Behavioral Loyalty", "hard", "single_choice",
        "Phân biệt giữa 'Lòng trung thành hành vi' (Behavioral Loyalty) và 'Lòng trung thành thái độ' (Attitudinal Loyalty):",
        "What distinguishes 'Behavioral Loyalty' from 'Attitudinal Loyalty'?",
        {
            "A": ("Lòng trung thành hành vi chỉ là thói quen mua lại do tiện lợi hoặc chi phí chuyển đổi cao; lòng trung thành thái độ thể hiện sự gắn kết cảm xúc, niềm tin sâu sắc và sự ủng hộ thương hiệu.", "Behavioral loyalty is repeat purchasing driven by convenience, inertia, or high switching costs; attitudinal loyalty reflects emotional commitment, genuine trust, and brand advocacy."),
            "B": ("Lòng trung thành thái độ chỉ xuất hiện ở những khách hàng không có tiền mua sản phẩm.", "Attitudinal loyalty occurs exclusively among individuals who lack funds to buy products."),
            "C": ("Lòng trung thành hành vi là loại lòng trung thành bền vững nhất mà đối thủ không thể phá vỡ bằng giảm giá.", "Behavioral loyalty represents the most unbreakable bond that competitors cannot disrupt via discounts."),
            "D": ("Không có sự khác biệt vì khách hàng cứ mua lại nhiều lần là đã có tình yêu thương hiệu mãnh liệt.", "There is no difference because repeat purchases always signify profound emotional love.")
        },
        "A",
        "Khách hàng chỉ trung thành hành vi có thể rời bỏ ngay khi đối thủ đưa ra khuyến mãi lớn hơn, trong khi khách hàng có lòng trung thành thái độ sẽ chủ động bảo vệ và giới thiệu thương hiệu.",
        "Behaviorally loyal buyers may defect as soon as an alternative lowers prices, whereas attitudinally loyal customers actively advocate and resist minor price variances.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 275-280", ["loyalty", "attitudinal-loyalty"]
    ),
    (
        "q-01-20", "CRM Definition Scope", "medium", "single_choice",
        "Một phát biểu toàn diện và chính xác nhất về bản chất của CRM là:",
        "Which statement provides the most comprehensive and accurate definition of CRM's essence?",
        {
            "A": ("CRM là một phần mềm cơ sở dữ liệu trên máy chủ cục bộ dùng để lưu trữ danh bạ điện thoại của khách hàng.", "CRM is an on-premise database software used exclusively to store customer phone directories."),
            "B": ("CRM là một chiến lược kinh doanh toàn diện kết hợp giữa con người, quy trình nghiệp vụ và công nghệ hiện đại nhằm tối ưu hóa giá trị vòng đời và sự gắn kết sinh lời của khách hàng.", "CRM is an enterprise-wide business strategy integrating people, business processes, and modern technology to maximize customer lifetime value and profitable engagement."),
            "C": ("CRM là một chiến dịch quảng cáo gửi email hàng loạt cho mọi địa chỉ thu thập được trên mạng.", "CRM is a promotional blast campaign sending mass spam emails to scraped web contact lists."),
            "D": ("CRM là một bộ phận nhỏ trong phòng kế toán chịu trách nhiệm phát hành hóa đơn đỏ.", "CRM is a minor billing sub-unit within accounting responsible for issuing tax receipts.")
        },
        "B",
        "CRM tích hợp chiến lược, văn hóa, tổ chức và công nghệ để xây dựng mối quan hệ có lợi cho cả khách hàng và doanh nghiệp.",
        "CRM integrates corporate strategy, culture, cross-functional processes, and technology platforms to cultivate mutually beneficial relationships.",
        "Baran & Galka (2017) p. 9; Kostojohn (2011) p. 11", "Chapter 1", "pp. 8-12", ["crm-definition", "strategic-orientation"]
    )
]

for item in e1:
    questions_batch1.append(make_q(
        item[0], "EXAM-01", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

# ==========================================
# EXAM 02: ORGANIZATION, CULTURE & GOVERNANCE (q-02-01 to q-02-20)
# ==========================================
e2 = [
    (
        "q-02-01", "Governance Structure", "medium", "single_choice",
        "Theo Kostojohn et al. (2011, tr. 32-38), vai trò quan trọng nhất của Ban Chỉ đạo Dự án CRM (CRM Steering Committee) là gì?",
        "According to Kostojohn et al. (2011, pp. 32-38), what is the most critical function of the CRM Steering Committee?",
        {
            "A": ("Tự tay viết mã nguồn (code) cho giao diện người dùng và kiểm thử cơ sở dữ liệu.", "Directly writing software code for the user interface and conducting unit testing on database tables."),
            "B": ("Cung cấp định hướng chiến lược, giải quyết xung đột lợi ích giữa các phòng ban, phê duyệt ngân sách và đảm bảo dự án bám sát mục tiêu kinh doanh.", "Providing executive strategic direction, resolving cross-departmental friction, approving budgets, and keeping the initiative aligned with business goals."),
            "C": ("Thay thế hoàn toàn bộ phận nhân sự trong việc chấm công hàng ngày cho nhân viên kỹ thuật.", "Replacing the Human Resources department in monitoring daily engineering punch cards."),
            "D": ("Tham gia trực tiếp vào tất cả các cuộc gọi tư vấn bán hàng của nhân viên kinh doanh.", "Participating in all sales calls made by field account representatives.")
        },
        "B",
        "Ban chỉ đạo gồm các lãnh đạo cấp cao giúp phá vỡ các rào cản phòng ban, phân bổ tài nguyên và giữ vững cam kết tài trợ cho dự án.",
        "The Steering Committee unites senior executives across silos to enforce organizational alignment, allocate resources, and resolve policy disagreements.",
        "Kostojohn et al. (2011)", "Chapter 2", "pp. 32-38", ["steering-committee", "crm-governance"]
    ),
    (
        "q-02-02", "Departmental Champions", "medium", "single_choice",
        "Tại sao 'Đại sứ phòng ban' (Departmental Champions / Super Users) lại là nhân tố quyết định sự thành bại của việc áp dụng CRM?",
        "Why are 'Departmental Champions' (Super Users) considered pivotal to successful CRM system adoption?",
        {
            "A": ("Vì họ là những người được trả lương cao nhất trong toàn bộ công ty.", "Because they receive the highest base compensation in the entire corporation."),
            "B": ("Vì họ là những nhân sự hiểu rõ nghiệp vụ thực tế, có uy tín với đồng nghiệp, đóng vai trò cầu nối hướng dẫn và thúc đẩy nhân viên vượt qua sức ỳ thay đổi.", "Because they combine deep functional workflow knowledge with peer respect, acting as on-the-ground advocates to guide colleagues past resistance to change."),
            "C": ("Vì họ là lập trình viên duy nhất được cấp quyền truy cập vào máy chủ cơ sở dữ liệu.", "Because they are the only engineers granted root database access permissions."),
            "D": ("Vì họ chịu trách nhiệm sa thải những nhân viên không chịu nhập thông tin vào CRM.", "Because they hold formal authority to terminate staff members failing to input records.")
        },
        "B",
        "Super Users là những người đi đầu và hỗ trợ tại chỗ ngay khi đồng nghiệp gặp khó khăn trong quy trình hàng ngày.",
        "Champions translate business needs into system requirements and provide informal, peer-to-peer coaching during go-live transition periods.",
        "Kostojohn et al. (2011)", "Chapter 2", "pp. 39-43", ["super-users", "change-management"]
    ),
    (
        "q-02-03", "Overcoming Silos", "hard", "single_choice",
        "Hiện tượng 'Ốc đảo phòng ban' (Functional Silos) gây tác hại nghiêm trọng nhất như thế nào đến trải nghiệm khách hàng?",
        "How do 'Functional Silos' inflict the most severe damage on customer experience?",
        {
            "A": ("Làm tăng chi phí tiền điện của tòa nhà văn phòng.", "By increasing commercial office electric utility expenses."),
            "B": ("Dữ liệu khách hàng bị phân mảnh giữa Bán hàng, Marketing và Dịch vụ, khiến khách hàng phải lặp lại thông tin nhiều lần và nhận thông điệp mâu thuẫn.", "Customer data is fragmented across Sales, Marketing, and Support, forcing customers to repeat their history repeatedly and receive conflicting communications."),
            "C": ("Làm cho nhân viên phải gửi quá nhiều email nội bộ hỏi thăm nhau.", "By causing employees to send excessive internal courtesy greeting emails."),
            "D": ("Khiến ban giám đốc không thể tổ chức các chuyến du lịch dã ngoại chung cho công ty.", "By preventing senior management from coordinating joint company retreats.")
        },
        "B",
        "Ốc đảo thông tin ngăn cản việc xây dựng Chân dung khách hàng 360 độ (Single Customer View), dẫn đến trải nghiệm khách hàng đứt gãy và thiếu chuyên nghiệp.",
        "Silos obstruct the creation of a Single Customer View (SCV), producing disjointed touchpoints, customer frustration, and missed cross-sell signals.",
        "Baran & Galka (2017)", "Chapter 4", "pp. 102-108", ["functional-silos", "single-customer-view"]
    ),
    (
        "q-02-04", "Sales Force Resistance", "hard", "single_choice",
        "Đâu là lý do phổ biến nhất khiến đội ngũ nhân viên kinh doanh phản đối việc cập nhật dữ liệu vào hệ thống CRM?",
        "What is the primary underlying driver of sales representative resistance to entering data into a CRM system?",
        {
            "A": ("Họ lo sợ thông tin khách hàng bị biến thành tài sản chung của công ty (mất vị thế đàm phán cá nhân) và cảm thấy bị cấp quản lý vi mô giám sát (Big Brother syndrome).", "Fear of losing personal leverage by turning client rolodexes into corporate property, coupled with apprehension over micromanagement surveillance ('Big Brother' syndrome)."),
            "B": ("Phần mềm CRM không hỗ trợ tiếng Anh.", "The CRM software interface strictly forbids English language input."),
            "C": ("Bàn phím máy tính quá khó sử dụng đối với nhân viên bán hàng.", "Desktop computer keyboards present insurmountable physical ergonomics barriers for reps."),
            "D": ("Họ muốn công ty chi thêm tiền điện thoại cố định tại văn phòng.", "Reps demand company subsidization for landline office telephone lines.")
        },
        "A",
        "Nhân viên bán hàng thường xem danh bạ khách hàng là 'quyền lực bí mật' của riêng họ và phản đối CRM vì sợ bị giám sát và mất quyền kiểm soát.",
        "Sales reps frequently perceive customer relationships as personal career leverage and resist administrative overhead that feels like management surveillance.",
        "Kostojohn et al. (2011)", "Chapter 2", "pp. 43-47", ["sales-force-resistance", "incentive-alignment"]
    ),
    (
        "q-02-05", "Incentive Alignment", "medium", "single_choice",
        "Để khuyến khích nhân viên chủ động sử dụng và làm giàu dữ liệu CRM, ban lãnh đạo nên áp dụng giải pháp nào sau đây?",
        "To foster sustained CRM adoption and data enrichment among frontline staff, management should implement which policy?",
        {
            "A": ("Quy định: 'Nếu dữ liệu không có trên CRM, cơ hội bán hàng đó không tồn tại và không được tính hoa hồng' kết hợp với việc công nhận và thưởng cho dữ liệu sạch.", "Enforcing the 'If it is not in the CRM, it does not exist and earns zero commission' rule, combined with recognition and rewards for data quality."),
            "B": ("Phạt tiền gấp đôi lương cơ bản đối với bất kỳ ai gõ sai chính tả trên hệ thống.", "Levying double-salary fines on anyone committing a typographical error."),
            "C": ("Tắt hoàn toàn quyền truy cập internet của nhân viên tại văn phòng.", "Shutting off all workplace internet access for sales employees."),
            "D": ("Thuê một công ty bảo vệ đứng giám sát màn hình làm việc của từng nhân viên.", "Hiring security guards to physically inspect computer monitors throughout the day.")
        },
        "A",
        "Nguyên tắc 'Nếu không có trên CRM, cơ hội không tồn tại' gắn chặt hành vi nhập liệu với quyền lợi hoa hồng sát sườn của nhân sự.",
        "Tying commission eligibility and pipeline reviews directly to CRM records aligns self-interest with system compliance far better than punitive threats.",
        "Kostojohn et al. (2011)", "Chapter 2", "pp. 47-52", ["incentives", "adoption-strategy"]
    ),
    (
        "q-02-06", "Culture Types", "hard", "single_choice",
        "Theo mô hình của Baran & Galka (2017, tr. 110-116), một nền văn hóa tổ chức hướng ngoại và linh hoạt, tập trung vào thấu hiểu và đáp ứng nhu cầu khách hàng được gọi là:",
        "According to organizational culture taxonomies in Baran & Galka (2017, pp. 110-116), a flexible, externally focused culture centering on customer responsiveness is termed:",
        {
            "A": ("Văn hóa thứ bậc quan liêu (Hierarchical/Bureaucratic Culture)", "Hierarchical / Bureaucratic Culture"),
            "B": ("Văn hóa hướng đến thị trường và khách hàng (Market/Adhocracy Customer-Focused Culture)", "Market / Adhocracy Customer-Focused Culture"),
            "C": ("Văn hóa khép kín bảo thủ", "Closed Conservative Culture"),
            "D": ("Văn hóa độc quyền kỹ thuật", "Technical Monopolistic Culture")
        },
        "B",
        "Văn hóa hướng thị trường kết hợp tính linh hoạt cao là mảnh đất màu mỡ nhất để triển khai CRM thành công vì mọi thành viên đều chủ động cải tiến vì khách hàng.",
        "Customer-centric market cultures empower staff to act autonomously on customer insights, contrasting sharply with rule-bound, inward-looking bureaucracies.",
        "Baran & Galka (2017)", "Chapter 4", "pp. 110-116", ["organizational-culture", "market-orientation"]
    ),
    (
        "q-02-07", "Executive Sponsorship", "medium", "single_choice",
        "Tại sao 'Sự cam kết của Lãnh đạo cấp cao' (Executive Sponsorship) là điều kiện tiên quyết cho một dự án CRM?",
        "Why is continuous 'Executive Sponsorship' an indispensable prerequisite for enterprise CRM initiatives?",
        {
            "A": ("Vì lãnh đạo cấp cao là người duy nhất biết cách cài đặt hệ điều hành máy chủ.", "Because executive sponsors are the sole individuals capable of installing server software."),
            "B": ("Vì việc tái cấu trúc quy trình kinh doanh và phân bổ lại quyền lực thông tin luôn vấp phải sự kháng cự; chỉ có lãnh đạo cấp cao mới có đủ thẩm quyền duy trì định hướng và cấp vốn kiên trì.", "Because process reengineering and data sharing redistribute organizational influence; only top leadership holds the authority to sustain focus, mandate compliance, and protect budgets."),
            "C": ("Vì nhà cung cấp phần mềm chỉ giao tiếp với nhân sự có chức danh C-level.", "Because software vendors only communicate with C-suite executives."),
            "D": ("Vì pháp luật yêu cầu Chủ tịch hội đồng quản trị phải trực tiếp ký nhận từng hóa đơn phần mềm.", "Because corporate law requires board chairs to sign every software maintenance invoice.")
        },
        "B",
        "Không có sự ủng hộ kiên quyết từ cấp C-suite, dự án CRM sẽ nhanh chóng bị các phòng ban tẩy chay khi quyền lợi cục bộ bị đụng chạm.",
        "Without steadfast C-level advocacy, cross-departmental CRM projects stall when functional leaders retreat to protect legacy departmental fiefdoms.",
        "Kostojohn et al. (2011)", "Chapter 2", "pp. 28-32", ["executive-sponsorship", "governance"]
    ),
    (
        "q-02-08", "Project Manager Role", "medium", "single_choice",
        "Theo Kostojohn et al., phẩm chất quan trọng nhất của một Giám đốc Dự án CRM (CRM Project Manager) là:",
        "According to Kostojohn et al., the most essential capability of a dedicated CRM Project Manager is:",
        {
            "A": ("Khả năng lập trình chuyên sâu mọi ngôn ngữ máy tính cổ điển.", "Deep assembly and low-level code hacking proficiency in legacy mainframe languages."),
            "B": ("Khả năng dung hòa giữa ngôn ngữ nghiệp vụ kinh doanh và ngôn ngữ kỹ thuật IT, quản lý tiến độ, phạm vi và truyền thông tích cực giữa các bên liên quan.", "The ability to bridge business requirements and IT technical realities, managing scope, schedule, and stakeholder expectations diplomatically."),
            "C": ("Kinh nghiệm làm kế toán trưởng ít nhất 15 năm.", "At least fifteen years of certified public accounting experience."),
            "D": ("Thói quen làm việc độc lập hoàn toàn không cần tương tác với người dùng cuối.", "A preference for solitary isolation with minimal end-user interaction.")
        },
        "B",
        "PM của dự án CRM phải là chuyên gia giao tiếp và quản trị phạm vi, đảm bảo nhóm kỹ thuật hiểu đúng nhu cầu người dùng và người dùng hiểu rõ giới hạn hệ thống.",
        "Effective CRM project managers excel at cross-functional diplomacy, translating business aspirations into technical tasks and preventing runaway scope creep.",
        "Kostojohn et al. (2011)", "Chapter 2", "pp. 35-39", ["project-management", "leadership"]
    ),
    (
        "q-02-09", "Change Management Model", "hard", "single_choice",
        "Trong quản trị thay đổi (Change Management) cho dự án CRM, giai đoạn 'Rã đông' (Unfreezing) theo mô hình Kurt Lewin đòi hỏi tổ chức phải:",
        "In organizational change management for CRM, the 'Unfreezing' stage of Kurt Lewin's framework requires the enterprise to:",
        {
            "A": ("Cài đặt ngay lập tức phiên bản phần mềm mới nhất lên máy tính của nhân viên.", "Immediately deploy latest software builds to staff workstations without warning."),
            "B": ("Giúp nhân viên nhận thức rõ những bất cập, thiệt hại của hiện trạng cũ (như mất khách hàng, dữ liệu phân mảnh) và tạo ra động lực cấp bách cần phải thay đổi.", "Create urgency by transparently demonstrating the painful inefficiencies of the status quo (lost sales, disjointed records) and making a compelling case for change."),
            "C": ("Khóa vĩnh viễn tài khoản của những người có ý kiến phản biện.", "Permanently lock the network accounts of staff voicing critical concerns."),
            "D": ("Ký hợp đồng gia hạn 10 năm với nhà cung cấp phần mềm cũ.", "Sign a ten-year extension contract with the incumbent legacy software vendor.")
        },
        "B",
        "Rã đông là bước phá vỡ sự tự mãn và thói quen cũ; nếu nhân viên không thấy được nỗi đau của quy trình hiện tại, họ sẽ không có lý do để chấp nhận hệ thống CRM mới.",
        "Unfreezing disrupts institutional inertia by showing why legacy habits harm the business, cultivating psychological readiness for adoption.",
        "Baran & Galka (2017)", "Chapter 4", "pp. 118-124", ["change-management", "lewin-model"]
    ),
    (
        "q-02-10", "Business Process Reengineering", "hard", "single_choice",
        "Một sai lầm 'chết người' mà nhiều doanh nghiệp mắc phải khi tự động hóa quy trình với CRM là:",
        "A fatal mistake commonly committed when automating workflows with a CRM system is:",
        {
            "A": ("Tự động hóa nguyên xi các quy trình thủ công lạc hậu và rối rắm hiện có mà không tiến hành Tái cấu trúc Quy trình Nghiệp vụ (BPR) trước khi số hóa.", "Automating broken, bloated, and outdated manual workflows without first undergoing Business Process Reengineering (BPR)."),
            "B": ("Tổ chức các buổi đào tạo thực hành cho người dùng cuối.", "Coordinating hands-on laboratory training sessions for frontline staff."),
            "C": ("Rút ngắn thời gian xử lý khiếu nại của khách hàng từ 3 ngày xuống 3 giờ.", "Compressing customer issue resolution time from three business days to three hours."),
            "D": ("Thiết lập các trường dữ liệu chuẩn hóa trên giao diện.", "Standardizing picklist dropdown fields on user interface screens.")
        },
        "A",
        "Tự động hóa một quy trình tồi chỉ tạo ra một quy trình tồi hoạt động nhanh hơn và tốn kém hơn. BPR phải đi trước công nghệ.",
        "Paving cow paths by automating defective processes merely yields faster chaos at greater expense. Process optimization must precede digital automation.",
        "Baran & Galka (2017) p. 105; Kostojohn (2011) p. 30", "Chapter 2 & 4", "pp. 105-108, 30-33", ["bpr", "process-optimization"]
    ),
    (
        "q-02-11", "Cross-Functional Collaboration", "medium", "single_choice",
        "Khi bộ phận Marketing và Bán hàng phối hợp nhịp nhàng trên CRM, khái niệm 'SLA giữa Bán hàng và Marketing' (Sales-Marketing Service Level Agreement) thường quy định điều gì?",
        "When Marketing and Sales collaborate effectively via CRM, what does a Sales-Marketing Service Level Agreement (SLA) define?",
        {
            "A": ("Số lượng bánh ngọt phòng Marketing phải mua cho phòng Bán hàng vào chiều thứ Sáu.", "The number of pastries marketing must deliver to sales on Friday afternoons."),
            "B": ("Tiêu chuẩn cụ thể của một Đầu mối Đủ tiêu chuẩn (MQL), thời hạn cam kết phòng Bán hàng phải liên hệ với đầu mối đó, và phản hồi ngược từ Bán hàng về chất lượng đầu mối.", "Precise qualifying criteria for Marketing Qualified Leads (MQL), guaranteed sales contact response times, and structured feedback loops on lead conversion viability."),
            "C": ("Lương cứng của nhân viên phòng ban này được trích từ hoa hồng của phòng ban kia.", "Direct salary deductions between respective departmental payroll accounts."),
            "D": ("Hai phòng ban phải hợp nhất thành một phòng duy nhất và ngồi chung một bàn làm việc.", "Mandatory organizational merger of both teams into a single physical room.")
        },
        "B",
        "SLA xóa bỏ tình trạng 'Marketing than thở Bán hàng không chịu gọi điện, còn Bán hàng chê Marketing mang về toàn đầu mối rác'.",
        "A formalized SLA establishes objective shared accountability, setting clear volume/quality metrics for leads and mandatory follow-up deadlines.",
        "Baran & Galka (2017)", "Chapter 4", "pp. 112-115", ["sales-marketing-alignment", "sla"]
    ),
    (
        "q-02-12", "Training Strategy", "medium", "single_choice",
        "Theo Kostojohn et al., chiến lược đào tạo người dùng CRM hiệu quả nhất nên tuân theo nguyên tắc nào?",
        "According to Kostojohn et al., which principle underpins the most effective CRM end-user training strategy?",
        {
            "A": ("Tổ chức một buổi thuyết trình lý thuyết kéo dài 8 tiếng liên tục trước ngày vận hành 3 tháng.", "A single eight-hour marathon lecture conducted three months prior to go-live day."),
            "B": ("Đào tạo phân theo vai trò nghiệp vụ (Role-based), dựa trên kịch bản thực tế công việc, tổ chức ngay sát ngày vận hành và có tài liệu trợ giúp nhanh tại chỗ.", "Role-based training customized to daily practical scenarios, scheduled immediately before go-live, and reinforced with quick-reference job aids."),
            "C": ("Gửi tài liệu hướng dẫn dày 500 trang qua email và yêu cầu nhân viên tự đọc ở nhà vào cuối tuần.", "Emailing a 500-page generic manual and requiring staff to review it at home on weekends."),
            "D": ("Chỉ đào tạo cho cấp giám đốc và không cần đào tạo cho nhân viên nhập liệu.", "Exclusively educating C-level managers while leaving operational users untrained.")
        },
        "B",
        "Người dùng chỉ ghi nhớ kiến thức khi được thực hành trên dữ liệu mô phỏng công việc cụ thể của họ ngay trước khi hệ thống chính thức hoạt động.",
        "Generic technical training fails; role-specific sessions using real scenarios immediately prior to rollout ensure high retention and operational readiness.",
        "Kostojohn et al. (2011)", "Chapter 2 & 6", "pp. 49-53, 178-182", ["training-strategy", "user-enablement"]
    ),
    (
        "q-02-13", "Resistance Management", "hard", "single_choice",
        "Nếu một nhân viên bán hàng kỳ cựu (top performer) từ chối sử dụng CRM và công khai chế nhạo hệ thống trước mặt các nhân viên trẻ, hành động thích hợp nhất của ban lãnh đạo là gì?",
        "If a senior top-performing sales rep openly flouts CRM adoption and disparages the system to younger colleagues, what is management's most effective response?",
        {
            "A": ("Nhượng bộ và miễn trừ vĩnh viễn việc sử dụng CRM cho cá nhân đó để bảo vệ doanh số ngắn hạn.", "Surrender and grant a permanent system exemption to that rep to protect immediate quarterly billing."),
            "B": ("Lãnh đạo cấp cao gặp riêng để lắng nghe khúc mắc, giải thích tầm nhìn chiến lược, yêu cầu tuân thủ nguyên tắc chung và gắn quyền lợi quản lý tài khoản vào hệ thống mà không có ngoại lệ.", "Executive sponsors hold a private counseling session to resolve legitimate friction, clarify strategic mandates, enforce standard compliance, and eliminate unilateral exemptions."),
            "C": ("Hủy bỏ toàn bộ dự án CRM của toàn công ty.", "Immediately abort the enterprise-wide CRM rollout."),
            "D": ("Phát động một cuộc bình chọn công khai trên mạng xã hội để phán xét nhân viên đó.", "Launch an anonymous public poll on social media to shame the dissident representative.")
        },
        "B",
        "Tạo ra 'vùng miễn trừ' cho nhân viên kỳ cựu sẽ phá hủy kỷ luật của toàn bộ dự án; các nhân viên khác sẽ noi theo và hệ thống sẽ thất bại.",
        "Allowing sacred cows or granting selective exemptions torpedoes enterprise credibility and fatally undermines collective project adoption.",
        "Kostojohn et al. (2011)", "Chapter 2", "pp. 45-48", ["governance", "adoption", "change-resistance"]
    ),
    (
        "q-02-14", "Steering Committee Frequency", "easy", "single_choice",
        "Trong các giai đoạn nước rút của dự án triển khai CRM, tần suất họp Ban Chỉ đạo được khuyến nghị là:",
        "During critical execution phases of a CRM rollout, the recommended Steering Committee cadence is:",
        {
            "A": ("Mỗi năm một lần.", "Once per calendar year."),
            "B": ("Hàng tuần hoặc hai tuần một lần (Bi-weekly) để kịp thời tháo gỡ điểm nghẽn và kiểm soát tiến độ.", "Weekly or bi-weekly to proactively resolve roadblocks and audit milestone health."),
            "C": ("Chỉ họp khi dự án đã bị quá hạn ngân sách gấp đôi.", "Meeting only after project expenditures have doubled initial budget allowances."),
            "D": ("Mỗi ngày 5 lần.", "Five times per business day.")
        },
        "B",
        "Tần suất định kỳ hàng tuần hoặc hai tuần một lần duy trì nhịp độ giải quyết vấn đề và giữ cho dự án luôn ở mức ưu tiên cao.",
        "A bi-weekly rhythm prevents bureaucratic inertia, allowing rapid escalation of risks, budget reallocation, and milestone sign-offs.",
        "Kostojohn et al. (2011)", "Chapter 2", "pp. 36-38", ["steering-committee", "meeting-cadence"]
    ),
    (
        "q-02-15", "Customer-Centric KPI Design", "hard", "single_choice",
        "Để chuyển đổi sang tổ chức lấy khách hàng làm trung tâm, một công ty bán lẻ nên thay đổi hệ thống KPI truyền thống (doanh số đơn hàng) sang nhóm chỉ số nào?",
        "To operationalize a customer-centric transformation, which metric shift should a retailer prioritize over pure single-transaction volume?",
        {
            "A": ("Tỷ lệ giữ chân khách hàng (Retention Rate), Giá trị Vòng đời Khách hàng (CLV), và Điểm số Hài lòng/NPS.", "Customer Retention Rate, Customer Lifetime Value (CLV), and Net Promoter Score (NPS)."),
            "B": ("Số giờ nhân viên ngồi tại bàn làm việc.", "Total physical hours clocked at office cubicles."),
            "C": ("Số lượng hóa đơn giấy in ra trong ngày.", "Gross volume of thermal paper receipt rolls printed daily."),
            "D": ("Tỷ lệ lưu kho hàng lỗi.", "Inventory scrap defect ratios in local warehouses.")
        },
        "A",
        "Chỉ tiêu đo lường quyết định hành vi; nếu chỉ thưởng theo doanh số ngắn hạn, nhân viên sẽ tiếp tục ép khách mua hàng giao dịch mà không quan tâm đến sự gắn bó lâu dài.",
        "Incentives govern human behavior; shifting KPIs toward retention and NPS forces staff to prioritize sustained relationship health over myopic deal-pushing.",
        "Baran & Galka (2017)", "Chapter 4 & 11", "pp. 125-130, 350-355", ["kpi-design", "customer-centricity"]
    ),
    (
        "q-02-16", "Communication Plan", "medium", "single_choice",
        "Theo Kostojohn et al., Kế hoạch Truyền thông (Communication Plan) trong dự án CRM cần phải:",
        "According to Kostojohn et al., an enterprise CRM Communication Plan must ensure:",
        {
            "A": ("Giữ bí mật toàn bộ thông tin dự án cho đến đúng ngày khai trương hệ thống.", "Total institutional secrecy until the sudden sunrise launch of the production software."),
            "B": ("Chủ động giải thích rõ ràng 'WIIFM' (What's In It For Me? - Điều này đem lại lợi ích gì cho tôi?) cho từng nhóm đối tượng người dùng xuyên suốt dự án.", "Transparently articulating 'WIIFM' (What's In It For Me?) across every specific end-user cohort throughout the initiative lifecycle."),
            "C": ("Chỉ gửi thông báo bằng văn bản pháp lý có đóng dấu đỏ của tòa án.", "Sending formal legal summonses drafted by outside judicial counsel."),
            "D": ("Đăng tải thông tin nội bộ của công ty lên các diễn đàn mạng xã hội công cộng.", "Publishing confidential rollout spreadsheets on public social networks.")
        },
        "B",
        "Người dùng chỉ đón nhận thay đổi khi họ hiểu rõ CRM giúp họ làm việc dễ dàng hơn, tiết kiệm thời gian và kiếm thêm hoa hồng như thế nào.",
        "End-user acceptance hinges on articulating tangible personal benefits ('WIIFM') rather than abstract corporate platitudes about operational efficiency.",
        "Kostojohn et al. (2011)", "Chapter 2", "pp. 41-45", ["wiifm", "communication-plan"]
    ),
    (
        "q-02-17", "Culture Resistance Symptoms", "medium", "single_choice",
        "Đâu là dấu hiệu cảnh báo sớm (early warning indicator) cho thấy văn hóa công ty đang âm thầm chống đối hệ thống CRM mới?",
        "Which symptom serves as a critical early warning sign of passive institutional resistance to a newly deployed CRM system?",
        {
            "A": ("Nhân viên tích cực đóng góp ý kiến để tinh chỉnh giao diện báo cáo.", "Staff proactively submitting constructive feedback tickets to polish report views."),
            "B": ("Nhân viên tiếp tục duy trì các bảng tính Excel riêng lẻ ('Shadow Systems') để lưu trữ dữ liệu khách hàng thay vì cập nhật lên CRM.", "Employees maintaining clandestine personal Excel spreadsheets ('Shadow Systems') to store client data rather than populating the CRM."),
            "C": ("Tỷ lệ đăng nhập hệ thống hàng ngày đạt 98%.", "Daily active user login rates reaching 98% across regional branches."),
            "D": ("Thời gian phản hồi khiếu nại của khách hàng giảm mạnh.", "Support ticket resolution times dropping dramatically.")
        },
        "B",
        "Sự xuất hiện của 'hệ thống bóng tối' (Shadow Systems / Excel riêng) là bằng chứng rõ nhất cho thấy người dùng không tin tưởng và né tránh CRM.",
        "Proliferation of shadow spreadsheets signals fundamental lack of trust in the enterprise system, representing passive aggressive resistance to adoption.",
        "Baran & Galka (2017) p. 115; Kostojohn (2011) p. 44", "Chapter 4", "pp. 114-117", ["shadow-systems", "passive-resistance"]
    ),
    (
        "q-02-18", "Pilot Group Selection", "hard", "single_choice",
        "Khi triển khai thử nghiệm hệ thống CRM (Pilot Rollout), nhóm người dùng nào sau đây là lựa chọn tối ưu nhất?",
        "When launching an enterprise CRM pilot phase, which user cohort represents the most strategic candidate pool?",
        {
            "A": ("Chi nhánh có thành tích kém nhất và có tinh thần phản đối công nghệ gay gắt nhất.", "The lowest-performing regional branch harboring militant anti-technology resentment."),
            "B": ("Một đơn vị kinh doanh hoặc chi nhánh có quy mô vừa phải, lãnh đạo địa phương nhiệt huyết, quy trình đại diện và sẵn sàng hợp tác đóng góp phản hồi.", "A representative mid-sized business unit with an enthusiastic branch leader, standard workflows, and strong collaborative appetite for feedback."),
            "C": ("Toàn bộ các văn phòng đại diện trên toàn cầu cùng một thời điểm.", "Every single global overseas subsidiary simultaneously in a big-bang flash cut."),
            "D": ("Chỉ riêng các thực tập sinh mới vào làm việc được một tuần.", "Brand new college interns who started their employment one week ago.")
        },
        "B",
        "Pilot thành công ở một đơn vị mẫu mực sẽ tạo ra hiệu ứng lan tỏa (lighthouse effect), trở thành minh chứng thực tế thuyết phục các bộ phận khác.",
        "A successful mid-sized pilot generates credible local success stories ('lighthouse effect') that dismantle peer skepticism during broader enterprise rollout.",
        "Kostojohn et al. (2011)", "Chapter 2 & 6", "pp. 48-52, 175-178", ["pilot-strategy", "rollout-management"]
    ),
    (
        "q-02-19", "Organizational Structure Shift", "hard", "single_choice",
        "Để chuyển dịch từ cơ cấu tổ chức quản lý theo dòng sản phẩm (Product-based) sang cơ cấu quản lý theo phân khúc khách hàng (Customer-based), doanh nghiệp cần:",
        "Transitioning from a product-based organizational structure to a customer-based structure fundamentally entails:",
        {
            "A": ("Bổ nhiệm các Giám đốc Phân khúc Khách hàng (Customer Segment Managers) có thẩm quyền điều phối nhiều sản phẩm để phục vụ trọn vẹn nhu cầu của nhóm khách hàng đó.", "Appointing dedicated Customer Segment Managers empowered to bundle cross-product portfolios around tailored client cohort requirements."),
            "B": ("Buộc mỗi nhân viên bán hàng chỉ được bán một linh kiện duy nhất trong danh mục.", "Restricting each field representative to selling a single isolated SKU."),
            "C": ("Đóng cửa các chi nhánh địa phương và chỉ bán hàng qua bưu điện.", "Shuttering all regional retail branches and switching exclusively to postal mail orders."),
            "D": ("Bỏ qua mọi yêu cầu phân tích dữ liệu thị trường.", "Ignoring all market intelligence and econometric data feeds.")
        },
        "A",
        "Quản lý theo khách hàng giúp loại bỏ việc 3 nhân viên của cùng một công ty đến chào 3 sản phẩm khác nhau cho cùng một khách hàng trong cùng một ngày.",
        "Customer segment management unifies enterprise touchpoints, preventing fragmented product silos from uncoordinatedly bombarding the same corporate buyer.",
        "Baran & Galka (2017)", "Chapter 4", "pp. 95-102", ["organizational-design", "segment-management"]
    ),
    (
        "q-02-20", "Post-Launch Governance", "medium", "single_choice",
        "Sau khi hệ thống CRM đã chính thức đi vào hoạt động (Post-Launch), cơ chế quản trị nào cần được duy trì thường xuyên?",
        "Following initial CRM go-live into production, which governance mechanism must remain permanently operational?",
        {
            "A": ("Giải tán ngay Ban chỉ đạo và để hệ thống tự vận hành mà không cần ai phụ trách.", "Immediately disbanding the Steering Committee and allowing the database to run unmonitored."),
            "B": ("Hội đồng Đánh giá Thay đổi (Change Advisory Board / Governance Board) định kỳ thẩm định các yêu cầu nâng cấp tính năng, giám sát chất lượng dữ liệu và đo lường mức độ tương tác.", "A permanent Change Advisory Board meeting regularly to prioritize enhancement requests, audit data quality hygiene, and track user engagement."),
            "C": ("Yêu cầu tất cả nhân viên thi lại chứng chỉ tin học mỗi tháng.", "Requiring all personnel to retake desktop computer certification exams monthly."),
            "D": ("Cấm bổ sung bất kỳ trường dữ liệu mới nào trong suốt 10 năm tiếp theo.", "Freezing the schema and forbidding any new field additions for the next decade.")
        },
        "B",
        "CRM là một hành trình liên tục tiến hóa; việc quản trị sau phát hành đảm bảo hệ thống thích ứng với sự thay đổi của thị trường và nhu cầu người dùng.",
        "CRM is a continuous lifecycle; persistent governance prioritizes continuous enhancement backlogs, maintains data hygiene, and prevents system atrophy.",
        "Kostojohn et al. (2011)", "Chapter 2 & 7", "pp. 51-54, 215-220", ["post-launch-governance", "continuous-improvement"]
    )
]

for item in e2:
    questions_batch1.append(make_q(
        item[0], "EXAM-02", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

# ==========================================
# EXAM 03: CUSTOMER DATA ARCHITECTURE & ANALYTICS (q-03-01 to q-03-20)
# ==========================================
e3 = [
    (
        "q-03-01", "Single Customer View", "medium", "single_choice",
        "Khái niệm 'Chân dung khách hàng 360 độ' (Single Customer View - SCV) trong kiến trúc dữ liệu CRM có nghĩa là gì?",
        "What does the concept of a 'Single Customer View' (SCV / 360-degree view) denote in CRM data architecture?",
        {
            "A": ("Khách hàng phải chụp ảnh khuôn mặt 360 độ khi đăng ký tài khoản.", "A customer must submit a 360-degree facial biometric scan upon opening an account."),
            "B": ("Bản ghi thông tin tổng hợp, nhất quán và phi trùng lặp tập hợp mọi tương tác, giao dịch, khiếu nại và hành vi của khách hàng từ tất cả các kênh vào một hồ sơ duy nhất.", "A unified, deduplicated, and synchronized profile aggregating all customer transactions, touchpoints, tickets, and preferences into a consolidated relational master record."),
            "C": ("Một màn hình máy tính có thể quay tròn 360 độ trên bàn làm việc của giao dịch viên.", "A hardware swivel monitor that physically rotates 360 degrees on a teller's desk."),
            "D": ("Bảng dữ liệu chỉ lưu trữ duy nhất một giao dịch gần nhất của khách hàng.", "A minimal flat table that retains only the single most recent transaction of a buyer.")
        },
        "B",
        "SCV hợp nhất dữ liệu từ POS, website, ứng dụng di động, tổng đài và mạng xã hội để mọi nhân viên đều nắm trọn vẹn lịch sử của khách hàng.",
        "An SCV aggregates fragmented transactional, behavioral, and servicing logs across channels into an authoritative master record.",
        "Baran & Galka (2017)", "Chapter 5", "pp. 140-148", ["scv", "data-architecture"]
    ),
    (
        "q-03-02", "Data Decay Rate", "hard", "single_choice",
        "Theo các nghiên cứu phân tích dữ liệu được trích dẫn trong Baran & Galka (2017, tr. 150-155), tốc độ suy thoái tự nhiên hàng năm của cơ sở dữ liệu khách hàng (Data Decay) là khoảng:",
        "According to customer database analytics cited in Baran & Galka (2017, pp. 150-155), the average annual rate of organic Customer Data Decay is approximately:",
        {
            "A": ("0.1% mỗi năm.", "0.1% annually."),
            "B": ("15% đến 20% mỗi năm do thay đổi chỗ ở, chuyển công tác, đổi số điện thoại, kết hôn hoặc qua đời.", "15% to 20% annually due to residential relocation, career changes, phone updates, marital status shifts, or death."),
            "C": ("85% mỗi năm.", "85% annually."),
            "D": ("Dữ liệu số không bao giờ bị suy thoái theo thời gian.", "Digital records remain permanently pristine with zero natural decay over time.")
        },
        "B",
        "Do biến động đời sống xã hội, khoảng 15-20% dữ liệu danh bạ khách hàng trở nên lỗi thời mỗi năm; nếu không duy trì vệ sinh dữ liệu, cơ sở dữ liệu sẽ nhanh chóng biến thành 'rác'.",
        "Societal mobility degrades contact databases at 15–20% per year; continuous data hygiene workflows are required to prevent massive operational drift.",
        "Baran & Galka (2017)", "Chapter 5", "pp. 150-155", ["data-decay", "data-hygiene"]
    ),
    (
        "q-03-03", "Data Hygiene Steps", "medium", "single_choice",
        "Quy trình 'Vệ sinh Dữ liệu' (Data Hygiene / Data Scrubbing) trong CRM bao gồm các bước kỹ thuật cốt lõi nào?",
        "Which sequence of technical actions constitutes the core of a CRM 'Data Hygiene' (Scrubbing) pipeline?",
        {
            "A": ("Lau chùi bụi bẩn trên vỏ máy chủ và màn hình máy tính của nhân viên.", "Dusting physical server chassis and cleaning employee desktop monitors."),
            "B": ("Chuẩn hóa định dạng (Standardization), xác thực địa chỉ/email (Verification), phát hiện và hợp nhất trùng lặp (Deduplication), và làm giàu dữ liệu (Enrichment).", "Format standardization, postal/email address validation, fuzzy duplicate record merging (Deduplication), and external data appending (Enrichment)."),
            "C": ("Xóa ngẫu nhiên 50% cơ sở dữ liệu để tiết kiệm dung lượng ổ cứng.", "Randomly purging 50% of database records to conserve solid-state storage."),
            "D": ("Mã hóa dữ liệu bằng mật khẩu dài 4 chữ số.", "Encrypting database tables with basic four-digit numeric pin codes.")
        },
        "B",
        "Vệ sinh dữ liệu loại bỏ các lỗi chính tả, chuẩn hóa số điện thoại theo mã quốc gia, ghép nối các bản ghi trùng lặp do nhập sai tên và bổ sung thêm thông tin định danh.",
        "Data hygiene parses messy text strings, validates against authoritative reference tables, executes fuzzy deduplication, and appends missing demographic attributes.",
        "Baran & Galka (2017)", "Chapter 5", "pp. 152-158", ["data-hygiene", "deduplication"]
    ),
    (
        "q-03-04", "RFM Model Components", "easy", "single_choice",
        "Trong phân tích hành vi khách hàng của CRM, mô hình RFM bao gồm ba biến số cốt lõi là:",
        "In analytical CRM customer behavioral scoring, the classic RFM model comprises which three core metrics?",
        {
            "A": ("Doanh thu (Revenue), Tần suất (Frequency), Ký quỹ (Margin)", "Revenue, Frequency, Margin"),
            "B": ("Tính gần đây của giao dịch (Recency), Tần suất mua hàng (Frequency), và Giá trị tiền tệ đã chi tiêu (Monetary Value)", "Recency (time since last purchase), Frequency (purchase count), and Monetary Value (total spend)"),
            "C": ("Lợi nhuận ròng (ROI), Khả năng thanh toán (Fluidity), Thị phần (Market Share)", "Return on Investment, Fluidity, Market Share"),
            "D": ("Phạm vi tiếp cận (Reach), Mức độ trung thành (Fidelity), Trọng số thị trường (Market Weight)", "Reach, Fidelity, Market Weight")
        },
        "B",
        "RFM là công cụ kinh điển để phân khúc khách hàng: Recency (mua gần đây nhất khi nào?), Frequency (mua bao nhiêu lần?), và Monetary (tổng chi tiêu bao nhiêu?).",
        "RFM groups accounts by how recently they bought (R), how often they buy (F), and how much aggregate revenue they generate (M).",
        "Baran & Galka (2017)", "Chapter 7", "pp. 210-218", ["rfm", "customer-segmentation"]
    ),
    (
        "q-03-05", "RFM Predictive Power", "hard", "single_choice",
        "Trong ba yếu tố của mô hình RFM, yếu tố nào trong thực nghiệm luôn có năng lực dự báo cao nhất về khả năng khách hàng sẽ tiếp tục phản hồi hoặc mua lại trong đợt tiếp thị tiếp theo?",
        "Empirically, which single dimension of the RFM framework demonstrates the highest predictive weight in forecasting immediate future response to promotional campaigns?",
        {
            "A": ("Giá trị tiền tệ (Monetary Value)", "Monetary Value (M)"),
            "B": ("Tần suất mua hàng (Frequency)", "Frequency (F)"),
            "C": ("Tính gần đây của giao dịch (Recency)", "Recency (R)"),
            "D": ("Cả ba yếu tố luôn có trọng số toán học bằng nhau 100%.", "All three variables carry mathematically identical predictive weight in every dataset.")
        },
        "C",
        "Thực nghiệm ngành bán lẻ và direct marketing chỉ ra rằng khách hàng vừa mới giao dịch gần đây (high Recency) luôn có xác suất mở email và mua hàng cao hơn hẳn khách hàng chi nhiều tiền nhưng đã không tương tác từ 2 năm trước.",
        "Direct marketing empirical studies prove that customers who transacted most recently (Recency) show vastly superior response propensities compared to dormant high-spenders.",
        "Baran & Galka (2017)", "Chapter 7", "pp. 214-219", ["recency", "rfm-analytics", "predictive-power"]
    ),
    (
        "q-03-06", "Data Warehouse vs Data Mart", "medium", "single_choice",
        "Sự khác biệt về phạm vi giữa Kho dữ liệu doanh nghiệp (Enterprise Data Warehouse - EDW) và Chợ dữ liệu (Data Mart) là gì?",
        "What defines the architectural scope difference between an Enterprise Data Warehouse (EDW) and a Data Mart?",
        {
            "A": ("EDW là kho lưu trữ dữ liệu tập trung toàn diện của toàn bộ doanh nghiệp; Data Mart là tập con dữ liệu được tổ chức chuyên biệt cho một phòng ban hoặc chức năng cụ thể (ví dụ: Marketing Data Mart).", "An EDW is a comprehensive centralized repository spanning enterprise data assets; a Data Mart is a departmental subset structured for specific functional analysis (e.g., Marketing Data Mart)."),
            "B": ("EDW chỉ chứa dữ liệu âm thanh; Data Mart chỉ chứa văn bản viết tay.", "An EDW stores audio voice logs; a Data Mart stores handwritten paper memos."),
            "C": ("Data Mart luôn đắt tiền và có dung lượng lớn gấp 100 lần EDW.", "A Data Mart is invariably one hundred times larger and more expensive than an EDW."),
            "D": ("EDW chỉ dành cho người tiêu dùng cá nhân truy cập miễn phí qua internet.", "An EDW is an open-source public repository accessed freely by consumers online.")
        },
        "A",
        "EDW tích hợp dữ liệu từ mọi nguồn trong công ty theo một mô hình dữ liệu chuẩn; Data Mart trích xuất các lát cắt dữ liệu để phục vụ nhu cầu phân tích nhanh của từng phòng ban.",
        "An EDW provides an enterprise single version of truth; Data Marts parse focused slices (e.g., sales pipeline, campaign clickstreams) optimized for departmental analysts.",
        "Baran & Galka (2017)", "Chapter 5", "pp. 160-166", ["data-warehouse", "data-mart"]
    ),
    (
        "q-03-07", "ETL Process", "medium", "single_choice",
        "Trong quy trình quản trị dữ liệu CRM, quy trình trích xuất, biến đổi và nạp dữ liệu được viết tắt là ETL, đại diện cho:",
        "In CRM data integration pipelines, the acronym ETL represents which three core procedural stages?",
        {
            "A": ("Enter, Test, Launch", "Enter, Test, Launch"),
            "B": ("Extract, Transform, Load", "Extract, Transform, Load"),
            "C": ("Evaluate, Train, License", "Evaluate, Train, License"),
            "D": ("Encrypt, Transfer, Lock", "Encrypt, Transfer, Lock")
        },
        "B",
        "ETL là tiến trình kỹ thuật trích xuất dữ liệu từ các hệ thống nguồn (Extract), làm sạch và chuyển đổi định dạng (Transform), và nạp vào kho dữ liệu CRM (Load).",
        "ETL extracts operational data across disparate touchpoints, transforms structures into standardized schema via cleansing logic, and loads records into analytical warehouses.",
        "Baran & Galka (2017)", "Chapter 5", "pp. 162-168", ["etl", "data-pipeline"]
    ),
    (
        "q-03-08", "Tesco Clubcard Case Grounding", "hard", "single_choice",
        "Theo tình huống nghiên cứu Tesco Clubcard (Case Study 5, tr. 173-183), yếu tố cốt lõi nào đã đưa Tesco từ vị trí thứ hai vươn lên thành nhà bán lẻ dẫn đầu nước Anh?",
        "According to the Tesco Clubcard case study (Raab et al., Case Study 5, pp. 173-183), what analytical capability catalyzed Tesco's ascension to UK grocery leadership?",
        {
            "A": ("Việc giảm giá 70% toàn bộ các mặt hàng trên toàn quốc và chấp nhận chịu lỗ 5 năm.", "Slashing retail shelf prices by 70% nationwide while absorbing operating losses for five straight years."),
            "B": ("Khai thác dữ liệu giao dịch thẻ Clubcard thông qua đối tác Dunnhumby để phân đoạn lối sống khách hàng (lifestyle clustering) và gửi voucher khuyến mãi cá nhân hóa chính xác với tỷ lệ đổi thưởng cực cao.", "Leveraging granular Clubcard POS basket telemetry via Dunnhumby to build lifestyle clusters, sending hyper-personalized quarterly coupon mailings with industry-leading redemption rates."),
            "C": ("Thuê các ngôi sao Hollywood đóng quảng cáo trên truyền hình vào khung giờ vàng.", "Contracting Hollywood movie celebrities for prime-time television commercials."),
            "D": ("Bán dữ liệu cá nhân của khách hàng cho các công ty bảo hiểm nhân thọ để kiếm lời.", "Selling member contact data to life insurance brokers to generate auxiliary cash.")
        },
        "B",
        "Tesco và Dunnhumby không xem thẻ thành viên là công cụ giảm giá đại trà, mà là công cụ lắng nghe dữ liệu mua sắm để gửi các ưu đãi cá nhân hóa đến từng giỏ hàng.",
        "Tesco rejected blanket promotional discounts, employing Dunnhumby algorithms to deliver bespoke coupon variants tailored to specific basket lifestyle clusters.",
        "Customer Relationship Management (Raab et al.)", "Case Study 5", "pp. 173-183", ["tesco-case", "dunnhumby", "loyalty-analytics"]
    ),
    (
        "q-03-09", "Dunnhumby Basket Analysis", "hard", "single_choice",
        "Trong tình huống Tesco, việc phân tích dữ liệu giỏ hàng (Market Basket Analysis) giúp phát hiện những quy luật nào sau đây?",
        "In the Tesco Clubcard ecosystem, how did analytical Market Basket Analysis generate commercial insights?",
        {
            "A": ("Tìm ra các sản phẩm thường được mua cùng nhau (như tã giấy và bia, hoặc rượu vang cao cấp và phô mai) để tối ưu hóa vị trí quầy kệ và chương trình khuyến mãi chéo.", "Identifying statistical co-purchase affinities (e.g., diapers and beer, or premium wines and artisan cheeses) to optimize shelf placement and targeted cross-promotions."),
            "B": ("Dự đoán chính xác thời tiết ngày mai mưa hay nắng dựa trên số lượng bao bì carton.", "Predicting tomorrow's weather based on the thickness of cardboard shipping crates."),
            "C": ("Xác định mã cổ phiếu nào trên sàn London sẽ tăng giá vào tuần tới.", "Forecasting which London Stock Exchange equities will surge next week."),
            "D": ("Tự động phát hiện khách hàng nào có ý định trộm cắp tại quầy thu ngân.", "Automatically flagging customers with potential shoplifting intent at self-checkout lanes.")
        },
        "A",
        "Phân tích liên kết giỏ hàng (Association Rules / Affinity Analysis) giúp phát hiện các hành vi tiêu dùng kết hợp tự nhiên để kích thích mua thêm.",
        "Affinity analysis mines transaction logs to discover non-obvious purchase combinations, informing shelf merchandising, bundle pricing, and targeted mailings.",
        "Customer Relationship Management (Raab et al.)", "Case Study 5", "pp. 175-180", ["basket-analysis", "affinity-rules", "cross-sell"]
    ),
    (
        "q-03-10", "Structured vs Unstructured Data", "medium", "single_choice",
        "Trong các nguồn dữ liệu khách hàng sau đây, đâu là ví dụ tiêu biểu của 'Dữ liệu phi cấu trúc' (Unstructured Data)?",
        "Among the following customer data feeds, which represents 'Unstructured Data'?",
        {
            "A": ("Số tiền thanh toán trên hóa đơn (ví dụ: 150.000 VNĐ).", "An invoice transaction total (e.g., $150.00)."),
            "B": ("Ngày tháng năm sinh của chủ tài khoản.", "The date of birth recorded on an account profile."),
            "C": ("Bản ghi âm cuộc gọi phàn nàn của khách hàng gửi tới tổng đài và bài viết nhận xét tự do trên mạng xã hội.", "Audio call recordings of customer complaints submitted to support desks and free-text social media reviews."),
            "D": ("Mã bưu chính gồm 5 chữ số của địa chỉ giao hàng.", "A five-digit postal zip code field in a shipping address record.")
        },
        "C",
        "Dữ liệu phi cấu trúc (văn bản tự do, giọng nói, video, hình ảnh) không nằm trong các bảng cột chuẩn và đòi hỏi các công nghệ như NLP hoặc AI để phân tích sắc thái cảm xúc.",
        "Unstructured data lacks predefined relational tabular schemas, requiring text mining and Natural Language Processing (NLP) to parse sentiment and intent.",
        "Baran & Galka (2017)", "Chapter 5", "pp. 142-146", ["unstructured-data", "nlp", "sentiment-analysis"]
    ),
    (
        "q-03-11", "Predictive Churn Modeling", "hard", "single_choice",
        "Mô hình dự báo khách hàng rời bỏ (Predictive Churn Model) trong CRM phân tích thường sử dụng các biến số đầu vào nào để phát hiện sớm khách hàng sắp defection?",
        "Which input variables are most critical when constructing a Predictive Customer Churn Model in analytical CRM?",
        {
            "A": ("Sự sụt giảm đột ngột về tần suất giao dịch, giảm thời gian đăng nhập ứng dụng, gia tăng số lượng cuộc gọi khiếu nại chưa giải quyết và điểm CSAT giảm.", "Sudden dips in purchase frequency, declining app login sessions, surging unresolved customer service tickets, and deteriorating CSAT responses."),
            "B": ("Màu sắc logo của công ty khách hàng.", "The hexadecimal color code of the prospective corporate client's logo."),
            "C": ("Số lượng chữ ký của giám đốc đối tác trên hợp đồng.", "The physical length of the customer CEO's handwritten signature on contract sheets."),
            "D": ("Khoảng cách địa lý từ nhà khách hàng đến trụ sở chính của ngân hàng trung ương.", "The aerial distance between a buyer's residence and the central national bank headquarters.")
        },
        "A",
        "Dấu hiệu rời bỏ xuất hiện rõ rệt qua các tín hiệu suy giảm hành vi tương tác và bất mãn về dịch vụ trước khi khách hàng chính thức đóng tài khoản.",
        "Early warning churn indicators manifest as behavioral velocity drops (session dormancy, drop in basket volume) compounded by friction points like support disputes.",
        "Baran & Galka (2017)", "Chapter 7 & 10", "pp. 225-232, 325-330", ["churn-prediction", "predictive-analytics"]
    ),
    (
        "q-03-12", "Data Governance Policy", "medium", "single_choice",
        "Chính sách 'Quản trị Dữ liệu' (Data Governance) trong dự án CRM nhằm đảm bảo điều gì?",
        "What is the primary objective of a CRM 'Data Governance' framework?",
        {
            "A": ("Khóa kín toàn bộ máy tính và không cho phép nhân viên bán hàng truy cập dữ liệu.", "Locking all computer terminals and barring field personnel from querying accounts."),
            "B": ("Quy định rõ ràng quyền sở hữu dữ liệu (Data Ownership), trách nhiệm duy trì chất lượng, chuẩn mực bảo mật và quy trình thu thập dữ liệu nhất quán trong toàn công ty.", "Establishing clear Data Ownership, data quality accountability, security privacy compliance standards, and uniform lifecycle management rules across the firm."),
            "C": ("Bắt buộc mọi báo cáo phải in ra giấy khổ lớn A0.", "Mandating that all monthly executive summaries be plotted on oversize A0 paper rolls."),
            "D": ("Chuyển giao toàn bộ dữ liệu bí mật kinh doanh cho các đối thủ cạnh tranh.", "Publishing confidential customer trade records to industry competitors.")
        },
        "B",
        "Nếu không có người chịu trách nhiệm về chất lượng từng trường dữ liệu (Data Steward), cơ sở dữ liệu sẽ nhanh chóng bị ô nhiễm và vô giá trị.",
        "Data governance assigns organizational stewardship over specific data domains, ensuring definitions, validation rules, and regulatory controls are enforced.",
        "Kostojohn et al. (2011) p. 115; Baran & Galka (2017) p. 170", "Chapter 5", "pp. 170-175", ["data-governance", "data-stewardship"]
    ),
    (
        "q-03-13", "Fuzzy Matching Logic", "hard", "single_choice",
        "Thuật toán 'Khớp mờ' (Fuzzy Matching) trong xử lý dữ liệu CRM được áp dụng trong tình huống nào sau đây?",
        "In CRM data cleansing, in which situation is 'Fuzzy Matching' logic primarily deployed?",
        {
            "A": ("Khi cần phát hiện hai bản ghi khách hàng thực chất là cùng một người dù có lỗi chính tả nhỏ (ví dụ: 'Nguyen Van A, 12 Hoang Hoa Tham' và 'Nguyeen Van A, 12 Hoang Hoa Thamm').", "Detecting duplicate customer profiles representing the same individual despite minor typographical variations (e.g., misspelled names or transposed address digits)."),
            "B": ("Khi cần xóa toàn bộ ảnh đại diện của khách hàng trên hệ thống.", "When purging high-resolution avatar images to free cloud storage quotas."),
            "C": ("Khi cần dự báo tỷ giá hối đoái quốc tế trong 10 năm tới.", "When forecasting foreign currency exchange rates ten years into the future."),
            "D": ("Khi muốn gửi thư rác đến các địa chỉ email không có thật.", "When distributing bulk unsolicited emails to non-existent server inboxes.")
        },
        "A",
        "Fuzzy matching sử dụng các chỉ số khoảng cách chuỗi (như Levenshtein distance) để nhận diện các bản ghi trùng lặp mà việc so khớp chính xác tuyệt đối (exact match) sẽ bỏ qua.",
        "Fuzzy logic applies phonetic and string-distance metrics (e.g., Levenshtein algorithms) to catch near-duplicate records that exact string comparisons miss.",
        "Baran & Galka (2017)", "Chapter 5", "pp. 154-157", ["fuzzy-matching", "deduplication", "data-cleansing"]
    ),
    (
        "q-03-14", "Collaborative Filtering", "medium", "single_choice",
        "Cơ chế 'Lọc cộng tác' (Collaborative Filtering) trong các công cụ gợi ý sản phẩm (Recommendation Engines) hoạt động dựa trên nguyên lý nào?",
        "On what underlying algorithmic principle does 'Collaborative Filtering' operate within CRM recommendation engines?",
        {
            "A": ("Gợi ý ngẫu nhiên bất kỳ sản phẩm nào còn tồn kho nhiều nhất.", "Randomly recommending whichever warehouse inventory SKU has the highest surplus stock."),
            "B": ("Tìm kiếm những người dùng có hành vi mua sắm tương đồng trong quá khứ và gợi ý cho khách hàng hiện tại những món đồ mà nhóm người dùng tương đồng đó đã thích.", "Identifying users who exhibited similar purchase behavior in the past and recommending items to the current user that those peer clusters also favored."),
            "C": ("Chỉ gợi ý sản phẩm đắt tiền nhất trên trang web mà không cần biết khách hàng là ai.", "Exclusively showcasing the most exorbitant luxury item on the homepage regardless of persona."),
            "D": ("Bắt buộc khách hàng phải điền bản khảo sát 100 câu hỏi trước khi hiển thị sản phẩm.", "Forcing users to complete a 100-item questionnaire before product pages unlock.")
        },
        "B",
        "Lọc cộng tác (ví dụ như thuật toán 'Khách hàng mua món này cũng mua món kia' của Amazon) khai thác trí tuệ đám đông từ các hành vi mua sắm tương đồng.",
        "Collaborative filtering (e.g., 'Customers who bought this also bought...') leverages collective behavioral patterns across lookalike buyer clusters.",
        "Baran & Galka (2017)", "Chapter 7 & 13", "pp. 235-240, 410-415", ["collaborative-filtering", "recommendation-engine"]
    ),
    (
        "q-03-15", "Customer Lifetime Value Formula", "hard", "single_choice",
        "Trong công thức tính toán CLV đơn giản hóa: CLV = [M x r] / [1 + d - r], các ký hiệu M, r, và d lần lượt đại diện cho:",
        "In the foundational annualized Customer Lifetime Value formulation CLV = [M x r] / [1 + d - r], what do variables M, r, and d represent?",
        {
            "A": ("M = Lợi nhuận biên ròng trung bình mỗi kỳ, r = Tỷ lệ giữ chân khách hàng (Retention Rate), d = Lãi suất chiết khấu (Discount Rate).", "M = Average net margin contribution per period, r = Customer Retention Rate, d = Annual Discount Rate."),
            "B": ("M = Số triệu USD doanh thu, r = Tỷ lệ lạm phát, d = Số ngày giao hàng.", "M = Million dollar gross sales, r = National inflation index, d = Dispatch transit days."),
            "C": ("M = Khối lượng hàng tồn kho, r = Đánh giá rủi ro, d = Khoảng cách địa lý.", "M = Inventory volume, r = Operational risk metric, d = Kilometric transit distance."),
            "D": ("M = Lương của giám đốc tiếp thị, r = Tỷ lệ hoàn tiền, d = Ngày thanh toán hóa đơn.", "M = Marketing director salary, r = Cash rebate percentage, d = Billing due date.")
        },
        "A",
        "Công thức tài chính chiết khấu dòng tiền vô hạn với tỷ lệ giữ chân không đổi chứng minh rằng gia tăng tỷ lệ giữ chân (r) sẽ tạo ra mức tăng vọt về CLV.",
        "This standard infinite-horizon retention model shows how incremental gains in retention (r) yield compounding exponential increases in customer asset equity.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 312-318", ["clv-formula", "retention-economics"]
    ),
    (
        "q-03-16", "Data Privacy Regulations", "hard", "single_choice",
        "Các quy định bảo vệ dữ liệu hiện đại như GDPR (Châu Âu) đặt ra thách thức kỹ thuật lớn nhất nào cho cơ sở dữ liệu CRM?",
        "Modern regulatory frameworks such as GDPR impose which critical technical compliance challenge on CRM database architectures?",
        {
            "A": ("Cấm doanh nghiệp sử dụng máy vi tính để bán hàng.", "Forbidding corporations from utilizing personal computers to conduct sales."),
            "B": ("Bắt buộc hệ thống phải hỗ trợ 'Quyền được lãng quên' (Right to be Forgotten - xóa vĩnh viễn dữ liệu cá nhân khi được yêu cầu) và truy xuất toàn bộ dữ liệu lịch sử của người dùng.", "Mandating technical compliance for the 'Right to be Forgotten' (permanent personal data erasure upon request) and providing comprehensive data portability logs."),
            "C": ("Yêu cầu mọi khách hàng phải đến trụ sở công ty để ký giấy đồng ý bằng bút mực tím.", "Requiring citizens to visit company headquarters in person to sign purple ink waivers."),
            "D": ("Quy định chỉ được phép lưu trữ dữ liệu của khách hàng trong vòng 24 giờ sau khi mua hàng.", "Limiting consumer transaction retention strictly to 24 hours post-checkout.")
        },
        "B",
        "GDPR trao cho người tiêu dùng quyền yêu cầu xóa toàn bộ thông tin cá nhân và trích xuất dữ liệu, đòi hỏi kiến trúc CRM phải có khả năng thanh trừng dữ liệu sạch sẽ trên mọi bảng liên kết.",
        "GDPR compliance requires automated capabilities to cascade personal data purges across interconnected master and historical transaction tables upon verified request.",
        "Baran & Galka (2017)", "Chapter 12", "pp. 380-388", ["gdpr", "data-privacy", "right-to-be-forgotten"]
    ),
    (
        "q-03-17", "Real-Time Event Processing", "medium", "single_choice",
        "Tính năng 'Kích hoạt theo sự kiện thời gian thực' (Real-Time Event-Driven Marketing) trong CRM là gì?",
        "What constitutes 'Real-Time Event-Driven Marketing' in an advanced analytical CRM ecosystem?",
        {
            "A": ("Tự động gửi thông điệp hoặc ưu đãi phù hợp ngay tại thời điểm khách hàng thực hiện một hành vi cụ thể (ví dụ: vừa quẹt thẻ tại sân bay hoặc bỏ quên giỏ hàng trên ứng dụng).", "Triggering contextually tailored messages or offers at the exact moment a customer completes a specific event (e.g., airport card swipe, abandoned mobile cart)."),
            "B": ("Gửi email khuyến mãi định kỳ vào đúng 12 giờ trưa ngày mùng 1 hàng tháng cho tất cả mọi người.", "Blasting batch emails at 12:00 PM on the first calendar day of each month to all contacts."),
            "C": ("Yêu cầu nhân viên bán hàng gọi điện thoại cho khách hàng vào nửa đêm.", "Instructing account reps to dial client personal mobile numbers at midnight."),
            "D": ("Phát loa thông báo tên khách hàng khi họ bước vào cửa hàng tạp hóa.", "Announcing customer names over public store loudspeakers upon storefront entry.")
        },
        "A",
        "Marketing theo sự kiện thời gian thực nắm bắt thời điểm khách hàng có nhu cầu hoặc băn khoăn cao nhất để tương tác ngay lập tức, gia tăng tỷ lệ chuyển đổi.",
        "Event triggers capture moments of high customer intent or friction, dramatically outperforming cold, non-contextual batch broadcast messages.",
        "Baran & Galka (2017)", "Chapter 7 & 13", "pp. 230-234, 412-416", ["event-driven-marketing", "real-time-crm"]
    ),
    (
        "q-03-18", "Data Latency", "medium", "single_choice",
        "Khái niệm 'Độ trễ dữ liệu' (Data Latency) trong các hệ thống báo cáo CRM phản ánh điều gì?",
        "What does 'Data Latency' measure in enterprise CRM reporting and analytics systems?",
        {
            "A": ("Số lượng nhân viên đi làm muộn trong tuần.", "The number of employees arriving late to the corporate campus during the business week."),
            "B": ("Khoảng thời gian chênh lệch từ lúc một sự kiện giao dịch phát sinh trong thế giới thực cho đến khi dữ liệu đó xuất hiện trên bảng phân tích của hệ thống.", "The elapsed time between when an operational business event occurs in reality and when it becomes queryable in reporting dashboards."),
            "C": ("Độ dài của dây cáp mạng nối từ máy chủ đến bàn giao dịch viên.", "The physical length of category 6 twisted pair copper ethernet cables."),
            "D": ("Tuổi thọ tối đa của ổ đĩa quang CD-ROM.", "The maximum projected shelf life of legacy CD-ROM optical media.")
        },
        "B",
        "Độ trễ thấp (gần thời gian thực) rất quan trọng để nhân viên chăm sóc khách hàng nắm bắt được sự cố khách hàng vừa gặp trên website trước khi khách gọi điện lên tổng đài.",
        "Low latency ensures customer service reps and analytical algorithms act on fresh behavioral reality rather than stale, outdated batch snapshots.",
        "Baran & Galka (2017)", "Chapter 5", "pp. 165-168", ["data-latency", "real-time-analytics"]
    ),
    (
        "q-03-19", "Customer Segmentation Criteria", "hard", "single_choice",
        "Khi phân khúc cơ sở khách hàng phục vụ chiến lược CRM, phương pháp nào mang lại giá trị định hướng hành động cao nhất so với phân khúc thuần túy theo nhân khẩu học (Demographics)?",
        "When segmenting a customer base for CRM execution, which methodology yields significantly higher actionable predictive value than pure demographic clustering?",
        {
            "A": ("Phân đoạn theo Hành vi (Behavioral Segmentation) và Giá trị đóng góp (Value-based Segmentation), kết hợp với nhu cầu và lịch sử giao dịch thực tế.", "Behavioral Segmentation and Value-Based Segmentation synthesizing actual transactional telemetry, engagement velocity, and demonstrated needs."),
            "B": ("Phân đoạn theo màu mắt và nhóm máu của khách hàng.", "Segmenting customers by eye color and genetic blood types."),
            "C": ("Phân đoạn ngẫu nhiên theo số thứ tự đăng ký tài khoản.", "Randomized numeric slicing based on sequential account signup serial keys."),
            "D": ("Chỉ phân loại theo độ tuổi mà không cần xem khách hàng đã từng mua mặt hàng nào.", "Grouping purely by broad age brackets while ignoring purchase history records.")
        },
        "A",
        "Hai khách hàng có cùng độ tuổi và giới tính có thể có thói quen tiêu dùng hoàn toàn trái ngược; phân khúc hành vi và giá trị phản ánh chính xác hành động thực tế.",
        "Demographic lookalikes often exhibit wildly contradictory purchasing preferences; behavioral and value segmentation mirrors verified commercial action.",
        "Baran & Galka (2017)", "Chapter 3 & 7", "pp. 72-78, 205-212", ["behavioral-segmentation", "value-based-segmentation"]
    ),
    (
        "q-03-20", "Data Quality Dimensions", "hard", "single_choice",
        "Bộ tiêu chuẩn chất lượng dữ liệu CRM chuẩn mực bao gồm 5 khía cạnh cốt lõi nào sau đây?",
        "Standard data management frameworks evaluate CRM data quality across which five core dimensions?",
        {
            "A": ("Tính chính xác (Accuracy), Tính đầy đủ (Completeness), Tính nhất quán (Consistency), Tính kịp thời (Timeliness), và Tính duy nhất (Uniqueness/Validity).", "Accuracy, Completeness, Consistency, Timeliness, and Uniqueness/Validity."),
            "B": ("Độ nặng, Độ dày, Chiều cao, Chiều rộng, và Màu sắc của máy chủ.", "Physical weight, thickness, height, width, and chassis paint hue of server hardware."),
            "C": ("Giá thành phần mềm, Chi phí bản quyền, Tiền lương lập trình viên, Tiền điện, Tiền mạng.", "Software license fees, developer wages, electrical bills, internet bandwidth fees."),
            "D": ("Số lượng từ viết tắt tiếng Anh, Phông chữ văn bản, Kích thước lề trang, Số trang in.", "Volume of acronyms, typographic typeface, page margin offsets, printed sheet counts.")
        },
        "A",
        "Một cơ sở dữ liệu CRM đạt chuẩn phải phản ánh đúng sự thật (chính xác), không thiếu trường quan trọng (đầy đủ), đồng bộ giữa các hệ thống (nhất quán), cập nhật mới nhất (kịp thời) và không bị nhân bản bản ghi (duy nhất).",
        "High-integrity data must be factually correct (accuracy), fully populated (completeness), uniform across systems (consistency), fresh (timeliness), and deduplicated (uniqueness).",
        "Baran & Galka (2017)", "Chapter 5", "pp. 148-154", ["data-quality", "data-governance"]
    )
]

for item in e3:
    questions_batch1.append(make_q(
        item[0], "EXAM-03", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

print(f"Total questions generated in batch 1: {len(questions_batch1)}")

with open(Path(r"C:\Kiến thức cần học\CRM\output\scratch\q_batch1.json"), "w", encoding="utf-8") as f:
    json.dump(questions_batch1, f, ensure_ascii=False, indent=2)
