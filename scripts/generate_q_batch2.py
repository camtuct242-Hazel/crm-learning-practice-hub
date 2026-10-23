import json
import os
from pathlib import Path

# Exam 04, 05, 06 question generator
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

questions_batch2 = []

# ==========================================
# EXAM 04: TECHNOLOGY PLATFORMS & ARCHITECTURE (q-04-01 to q-04-20)
# ==========================================
e4 = [
    (
        "q-04-01", "SaaS vs On-Premise", "easy", "single_choice",
        "Ưu điểm lớn nhất của mô hình Phần mềm Dịch vụ (SaaS / Cloud CRM) so với mô hình Cài đặt tại chỗ (On-Premise) đối với doanh nghiệp vừa và nhỏ là gì?",
        "What is the greatest advantage of Software-as-a-Service (SaaS / Cloud CRM) over traditional On-Premise deployments for mid-market enterprises?",
        {
            "A": ("Không đòi hỏi chi phí đầu tư hạ tầng máy chủ ban đầu (CapEx thấp), triển khai nhanh chóng và nhà cung cấp tự động bảo trì, nâng cấp phần mềm.", "Lower upfront capital expenditure (CapEx) on server infrastructure, faster deployment timelines, and vendor-managed software maintenance and updates."),
            "B": ("Cho phép công ty sở hữu vĩnh viễn toàn bộ mã nguồn của phần mềm mà không phải trả thêm tiền.", "Permanent corporate ownership of the entire proprietary source code base at zero additional fee."),
            "C": ("Hoạt động bình thường ngay cả khi không có kết nối mạng internet hoặc mất điện toàn bộ.", "Uninterrupted operation even during catastrophic internet outages or complete power loss."),
            "D": ("Cho phép nhân viên tự do thay đổi cấu trúc bảng cơ sở dữ liệu vật lý theo ý muốn.", "Permitting non-technical employees to arbitrarily alter physical database relational schemas.")
        },
        "A",
        "SaaS chuyển đổi chi phí đầu tư ban đầu lớn (CapEx) thành chi phí vận hành định kỳ có thể dự đoán (OpEx), giảm thiểu gánh nặng quản trị hạ tầng phần cứng cho doanh nghiệp.",
        "SaaS shifts heavy upfront capital expense (CapEx) into predictable operating expenditures (OpEx) while outsourcing infrastructure patching and uptime SLAs to cloud hosts.",
        "Kostojohn et al. (2011)", "Chapter 4", "pp. 95-102", ["saas", "cloud-crm", "capex-vs-opex"]
    ),
    (
        "q-04-02", "Total Cost of Ownership", "hard", "single_choice",
        "Khi tính toán Tổng chi phí sở hữu (Total Cost of Ownership - TCO) cho một hệ thống CRM trong vòng đời 5 năm, yếu tố 'chi phí ẩn' (hidden costs) nào thường bị đánh giá thấp nhất?",
        "When calculating the 5-year Total Cost of Ownership (TCO) of an enterprise CRM, which 'hidden cost' is most frequently underestimated?",
        {
            "A": ("Tiền mua bàn ghế và văn phòng phẩm cho phòng kinh doanh.", "The acquisition costs of office furniture and paper stationery for sales reps."),
            "B": ("Chi phí tích hợp hệ thống (System Integration), tùy biến mã nguồn, đào tạo người dùng liên tục và chi phí vệ sinh dữ liệu định kỳ.", "Systems integration fees, ongoing custom code maintenance, continuous end-user retraining, and routine data hygiene cleansing."),
            "C": ("Tiền điện thắp sáng phòng máy chủ của nhà cung cấp dịch vụ đám mây.", "The commercial electric utility charges incurred by third-party data center operators."),
            "D": ("Chi phí in danh thiếp cho nhân viên hỗ trợ khách hàng.", "Business card printing expenses for customer service representatives.")
        },
        "B",
        "Bản quyền phần mềm thường chỉ chiếm 20-30% TCO; phần lớn chi phí nằm ở khâu tích hợp hệ thống cũ, tùy biến quy trình và quản trị thay đổi con người liên tục.",
        "Software licensing typically represents only 20–30% of multi-year TCO; integration with legacy systems, change management, and continuous data hygiene dominate real spend.",
        "Kostojohn et al. (2011)", "Chapter 4", "pp. 102-108", ["tco", "hidden-costs", "cost-estimation"]
    ),
    (
        "q-04-03", "API Integration", "medium", "single_choice",
        "Giao diện lập trình ứng dụng (Application Programming Interface - API) đóng vai trò gì trong kiến trúc giải pháp CRM hiện đại?",
        "What core functional role does an Application Programming Interface (API) play in modern CRM architecture?",
        {
            "A": ("Tự động thanh lý tài sản cố định của công ty khi doanh thu giảm.", "Automatically liquidating corporate fixed assets when quarterly sales dip."),
            "B": ("Cung cấp cầu nối kỹ thuật chuẩn hóa cho phép hệ thống CRM trao đổi dữ liệu hai chiều theo thời gian thực với các hệ thống ERP, thương mại điện tử và cổng thanh toán.", "Providing standardized technical endpoints enabling real-time, bi-directional data synchronization between CRM, ERP, e-commerce storefronts, and billing gateways."),
            "C": ("In sao kê ngân hàng ra giấy vào cuối mỗi ngày làm việc.", "Printing physical bank transaction ledgers onto paper at close of business daily."),
            "D": ("Ngăn chặn hoàn toàn mọi người dùng không được gửi tin nhắn thoại qua điện thoại.", "Preventing end-users from transmitting voicemail recordings over telecommunications.")
        },
        "B",
        "API (RESTful/SOAP) cho phép hệ thống CRM hoạt động như một trung tâm điều phối mở, kết nối thông suốt với ERP (kho, kế toán) và các kênh bán hàng bên ngoài.",
        "Modern APIs serve as the connectivity tissue connecting CRM data models with ERP back-offices, marketing automation clouds, and custom web applications.",
        "Baran & Galka (2017)", "Chapter 6", "pp. 180-186", ["api", "system-integration", "erp-crm"]
    ),
    (
        "q-04-04", "RFP Development", "medium", "single_choice",
        "Theo Kostojohn et al., mục đích chính của việc xây dựng 'Bản Yêu cầu Báo giá / Giải pháp' (Request for Proposal - RFP) chi tiết khi chọn phần mềm CRM là gì?",
        "According to Kostojohn et al., what is the primary objective of authoring a comprehensive Request for Proposal (RFP) for CRM vendor selection?",
        {
            "A": ("Để dọa các nhà cung cấp phần mềm hạ giá xuống mức miễn phí.", "To intimidate software vendors into dropping prices to zero."),
            "B": ("Định hình rõ ràng các yêu cầu chức năng (functional) và phi chức năng (non-functional) của doanh nghiệp, tạo thang đo khách quan để so sánh năng lực của các nhà cung cấp.", "Articulating clear functional and non-functional enterprise requirements to establish an objective evaluation rubric for comparing competing vendor proposals."),
            "C": ("Yêu cầu nhà cung cấp phải cử giám đốc sang làm việc không lương tại văn phòng công ty.", "Mandating that the vendor assign their executive director to work unpaid at the client site."),
            "D": ("Hoàn thành thủ tục hành chính để nộp thuế thu nhập doanh nghiệp cuối năm.", "Fulfilling formal bureaucratic filings required for corporate tax year-end audits.")
        },
        "B",
        "RFP chuẩn hóa nhu cầu thực tế của các phòng ban thành tiêu chí đánh giá có trọng số, tránh việc bị dẫn dắt bởi các bài thuyết trình bán hàng hoa mỹ của vendor.",
        "An RFP forces internal consensus on operational requirements and prevents selection teams from being swayed by generic, polished vendor sales demonstrations.",
        "Kostojohn et al. (2011)", "Chapter 4", "pp. 82-90", ["rfp", "vendor-evaluation"]
    ),
    (
        "q-04-05", "Vendor Demonstration Scripts", "hard", "single_choice",
        "Khi tổ chức buổi thuyết trình demo sản phẩm của các nhà cung cấp CRM (Vendor Demos), phương pháp tốt nhất để đánh giá thực chất năng lực phần mềm là:",
        "When coordinating CRM vendor demonstrations, what is the best practice to objectively evaluate real software capabilities?",
        {
            "A": ("Để nhà cung cấp tự do trình diễn bản demo chuẩn bị sẵn của họ với dữ liệu mẫu hoàn hảo do họ tự tạo.", "Permitting vendors to execute their pre-packaged, canned demonstrations using perfect fictional demo datasets."),
            "B": ("Cung cấp cho các nhà cung cấp một 'Kịch bản Thuyết trình Dựa trên Nghiệp vụ Thực tế' (Scripted Scenarios) sử dụng các ca xử lý khó của chính doanh nghiệp và chấm điểm theo tiêu chí định sẵn.", "Mandating that vendors execute a structured, company-specific demonstration script modeling real-world edge cases and complex workflows under a standardized scoring rubric."),
            "C": ("Chọn nhà cung cấp nào có nhân viên thuyết trình ăn mặc đẹp nhất.", "Selecting the vendor whose sales presenters are dressed in the most fashionable business suits."),
            "D": ("Yêu cầu nhà cung cấp trình diễn tính năng quản lý nhân sự thay vì tính năng CRM.", "Demanding that vendors demo enterprise human resource payroll rather than CRM pipelines.")
        },
        "B",
        "Kịch bản demo có cấu trúc buộc nhà cung cấp phải giải quyết đúng bài toán nghiệp vụ gai góc của doanh nghiệp trên phần mềm thực tế, lộ rõ điểm mạnh và điểm yếu.",
        "Scripted scenarios using actual company workflows expose functional gaps and prevent vendors from sidestepping difficult customization requirements during demos.",
        "Kostojohn et al. (2011)", "Chapter 4", "pp. 91-95", ["vendor-demos", "scripted-scenarios"]
    ),
    (
        "q-04-06", "Consultant Selection Criteria", "medium", "single_choice",
        "Theo Kostojohn et al. (2011, tr. 108-115), khi lựa chọn Đối tác Tư vấn Triển khai CRM (Implementation Partner / Consultant), tiêu chí nào sau đây quan trọng nhất?",
        "According to Kostojohn et al. (2011, pp. 108-115), which criterion is most critical when selecting an external CRM Implementation Consultant?",
        {
            "A": ("Công ty tư vấn có trụ sở đặt tại nước ngoài xa nhất có thể.", "The consulting firm maintaining offices situated in the most distant overseas time zone."),
            "B": ("Kinh nghiệm thực chiến đã triển khai thành công các dự án CRM trong cùng ngành nghề (Industry-specific expertise), phương pháp luận rõ ràng và đội ngũ nhân sự trực tiếp tham gia có năng lực đã được kiểm chứng.", "Proven industry-specific track record in successful peer deployments, transparent implementation methodology, and verified expertise of the assigned deployment personnel."),
            "C": ("Mức giá báo thầu rẻ nhất bất kể uy tín và số lượng nhân sự cam kết.", "The lowest rock-bottom pricing bid regardless of vendor reputation or resource allocation."),
            "D": ("Công ty tư vấn có đông nhân viên bảo vệ nhất.", "The consulting company employing the largest roster of physical campus security guards.")
        },
        "B",
        "Kinh nghiệm ngành giúp đối tác hiểu ngay các quy trình kinh doanh đặc thù mà không cần doanh nghiệp phải 'dạy lại từ đầu', giảm thiểu rủi ro thiết kế sai quy trình.",
        "Domain-specific fluency ensures consultants grasp subtle vertical workflows out-of-the-box, mitigating the severe risk of flawed architectural blueprints.",
        "Kostojohn et al. (2011)", "Chapter 4", "pp. 108-115", ["consultant-selection", "partner-evaluation"]
    ),
    (
        "q-04-07", "ERP vs CRM Architectural Focus", "medium", "single_choice",
        "Sự khác biệt căn bản về trọng tâm nghiệp vụ giữa hệ thống ERP (Hoạch định Nguồn lực Doanh nghiệp) và CRM là gì?",
        "What is the foundational operational distinction between an ERP system and a CRM platform?",
        {
            "A": ("ERP chỉ dùng cho ngành giáo dục; CRM chỉ dùng cho ngành y tế.", "ERP applies exclusively to education; CRM applies solely to healthcare."),
            "B": ("ERP tập trung vào hậu sảnh (Back-office: tài chính, kho vận, sản xuất, kiểm soát chi phí); CRM tập trung vào tiền sảnh (Front-office: khách hàng, tiếp thị, bán hàng, dịch vụ, gia tăng doanh thu).", "ERP centers on back-office operations (accounting, inventory, manufacturing, cost control); CRM centers on front-office engagement (customers, marketing, sales pipeline, service, revenue generation)."),
            "C": ("ERP không có cơ sở dữ liệu; CRM có cơ sở dữ liệu.", "ERP operates without databases; CRM incorporates database tables."),
            "D": ("ERP được cài đặt trên máy tính để bàn; CRM chỉ dùng được trên đồng hồ thông minh.", "ERP runs solely on desktop workstations; CRM runs exclusively on digital smartwatches.")
        },
        "B",
        "ERP quản lý nội bộ và nguồn lực hậu cần để tối ưu hóa chi phí; CRM quản lý các điểm tiếp xúc hướng ngoại với khách hàng để tối đa hóa doanh thu và mối quan hệ.",
        "ERP optimizes operational efficiency and ledger integrity across internal back-office resources; CRM drives front-office revenue and relationship value.",
        "Baran & Galka (2017)", "Chapter 6", "pp. 175-180", ["erp-vs-crm", "front-office", "back-office"]
    ),
    (
        "q-04-08", "Mobile CRM Requirements", "medium", "single_choice",
        "Khi triển khai tính năng CRM trên thiết bị di động (Mobile CRM) cho đội ngũ nhân viên kinh doanh thị trường, yêu cầu kỹ thuật nào sau đây là quan trọng hàng đầu?",
        "When rolling out Mobile CRM for field sales personnel, which technical capability is of paramount importance?",
        {
            "A": ("Ứng dụng phải hỗ trợ xem video độ phân giải 8K trực tuyến.", "The mobile client application must stream continuous 8K resolution video feeds."),
            "B": ("Khả năng hoạt động ngoại tuyến (Offline capability) với cơ chế tự động đồng bộ hai chiều khi có kết nối mạng, giao diện tinh gọn tối ưu cho thao tác một tay.", "Robust offline functionality with automatic two-way background synchronization upon reconnection, and an uncluttered UI streamlined for single-hand input."),
            "C": ("Bắt buộc điện thoại phải cắm dây cáp mạng LAN cố định.", "Mandating that mobile smartphones remain hard-wired to local LAN ethernet cables."),
            "D": ("Tự động phát chuông báo động mỗi 5 phút.", "Emitting a loud audible siren alert tone every five minutes.")
        },
        "B",
        "Nhân viên thị trường thường xuyên làm việc tại những khu vực sóng yếu hoặc không có mạng; khả năng lưu trữ cục bộ và đồng bộ tự động quyết định tỷ lệ sử dụng.",
        "Field reps regularly operate in network dead zones; offline caching with resilient collision-resolution syncing is mandatory to maintain frontline adoption.",
        "Baran & Galka (2017)", "Chapter 6", "pp. 188-192", ["mobile-crm", "offline-sync", "field-enablement"]
    ),
    (
        "q-04-09", "Customization vs Configuration", "hard", "single_choice",
        "Trong triển khai công nghệ CRM, sự khác biệt giữa 'Cấu hình' (Configuration) và 'Tùy biến' (Customization) là gì?",
        "In CRM technology implementation, what distinguishes 'Configuration' from 'Customization'?",
        {
            "A": ("Không có sự khác biệt, hai từ này hoàn toàn đồng nghĩa.", "There is no difference; the terms are entirely synonymous in software engineering."),
            "B": ("Cấu hình là điều chỉnh các thiết lập sẵn có không cần lập trình (thêm trường, sửa menu, tạo luồng công việc qua giao diện kéo thả); Tùy biến là viết mã nguồn mới (custom code) để mở rộng chức năng ngoài phạm vi chuẩn của phần mềm.", "Configuration alters built-in settings without coding (adding fields, picklists, declarative workflows); Customization involves writing proprietary code to extend core capabilities beyond native platform limits."),
            "C": ("Cấu hình là xóa dữ liệu; Tùy biến là nhập dữ liệu mới.", "Configuration purges data records; Customization inputs new customer rows."),
            "D": ("Cấu hình luôn tốn kém gấp 10 lần Tùy biến.", "Configuration is invariably ten times more costly than custom software development.")
        },
        "B",
        "Doanh nghiệp nên ưu tiên tối đa việc Cấu hình (declarative); lạm dụng Tùy biến mã nguồn sẽ gây khó khăn, tốn kém và dễ phát sinh lỗi khi nhà cung cấp nâng cấp phiên bản.",
        "Enterprises should maximize declarative configuration; excessive custom code creates technical debt and breaks when cloud platforms deploy automated version upgrades.",
        "Kostojohn et al. (2011)", "Chapter 4 & 5", "pp. 104-107, 135-139", ["configuration", "customization", "technical-debt"]
    ),
    (
        "q-04-10", "Scalability Testing", "medium", "single_choice",
        "Yêu cầu về 'Khả năng mở rộng' (Scalability) của nền tảng CRM đảm bảo điều gì cho doanh nghiệp?",
        "What does the 'Scalability' requirement of a CRM platform ensure for a growing business?",
        {
            "A": ("Hệ thống có thể tự động tăng số lượng phòng họp trong tòa nhà văn phòng.", "The software can physically expand the square footage of office conference rooms."),
            "B": ("Hệ thống có khả năng xử lý khối lượng bản ghi tăng trưởng theo cấp số nhân, mở rộng số lượng người dùng đồng thời mà không bị suy giảm hiệu năng hoặc sập máy chủ.", "The platform maintains sub-second query response and uptime SLAs as transaction volumes, database records, and concurrent users expand exponentially over time."),
            "C": ("Cho phép nhân viên thoải mái đổi sang các loại màn hình máy tính lớn hơn.", "Allowing employees to freely swap display monitors for wider physical aspect ratios."),
            "D": ("Bắt buộc mọi dữ liệu phải được nén lại thành tệp ZIP trước khi đọc.", "Requiring all records to be manually compressed into ZIP files before viewing.")
        },
        "B",
        "Khả năng mở rộng (dọc và ngang) đảm bảo khi cơ sở khách hàng tăng từ 10.000 lên 10.000.000 bản ghi, hệ thống vẫn duy trì tốc độ truy xuất mượt mà.",
        "Horizontal and vertical scalability ensures that as enterprise customer data scales from thousands to millions of records, transaction throughput remains steady.",
        "Baran & Galka (2017)", "Chapter 6", "pp. 182-187", ["scalability", "architecture", "performance"]
    ),
    (
        "q-04-11", "Data Security Architecture", "hard", "single_choice",
        "Mô hình 'Bảo mật Theo vai trò' (Role-Based Access Control - RBAC) trong CRM hoạt động như thế nào?",
        "How does a 'Role-Based Access Control' (RBAC) security model operate within enterprise CRM software?",
        {
            "A": ("Tất cả mọi nhân viên trong công ty đều có quyền đọc, sửa và xuất toàn bộ cơ sở dữ liệu khách hàng ra tệp Excel.", "Every employee across the entire firm possesses unrestricted read, write, and bulk export permissions over all customer records."),
            "B": ("Quyền truy cập, chỉnh sửa và xuất dữ liệu được phân bổ nghiêm ngặt dựa trên vị trí công việc, thứ bậc quản lý và phạm vi lãnh thổ phụ trách của người dùng.", "Data access, editing, and export permissions are strictly granted according to predefined organizational roles, managerial hierarchies, and geographic territories."),
            "C": ("Chỉ những nhân viên có thâm niên trên 20 năm mới được phép bật máy tính.", "Only employees with greater than twenty years of corporate tenure are permitted to log in."),
            "D": ("Hệ thống ngẫu nhiên thay đổi mật khẩu của người dùng sau mỗi 10 phút.", "The system randomly scrambles end-user network passwords every ten minutes.")
        },
        "B",
        "RBAC ngăn ngừa việc nhân viên cấp dưới đánh cắp toàn bộ danh sách khách hàng của công ty hoặc phòng ban này can thiệp trái phép vào cơ hội bán của phòng ban khác.",
        "RBAC enforces the principle of least privilege, shielding sensitive account records against unauthorized data exfiltration and accidental tampering.",
        "Baran & Galka (2017) p. 190; Kostojohn (2011) p. 105", "Chapter 6", "pp. 189-193", ["rbac", "data-security", "access-control"]
    ),
    (
        "q-04-12", "Master Data Management", "hard", "single_choice",
        "Trong kiến trúc CNTT tích hợp nhiều phần mềm, giải pháp 'Quản lý Dữ liệu Tổng thể' (Master Data Management - MDM) giải quyết vấn đề gì giữa CRM và ERP?",
        "In a multi-system enterprise IT architecture, what foundational challenge does Master Data Management (MDM) resolve between CRM and ERP?",
        {
            "A": ("Tự động thanh toán lương thưởng cho giám đốc tài chính.", "Automating executive bonus disbursement ledgers for the Chief Financial Officer."),
            "B": ("Thiết lập 'Bản ghi Vàng' (Golden Record) duy nhất có thẩm quyền về thông tin khách hàng, đồng bộ danh tính thực thể và quy định hệ thống nào là nguồn gốc chân lý (System of Record).", "Establishing an authoritative 'Golden Record' for customer entities, resolving identity discrepancies, and declaring clear Systems of Record for specific attributes."),
            "C": ("Cung cấp dịch vụ đồ ăn trưa miễn phí cho kỹ sư phần mềm.", "Supplying complimentary catered luncheons to database administrators."),
            "D": ("Xóa bỏ hoàn toàn các loại hợp đồng thương mại bằng văn bản giấy.", "Abolishing all paper commercial contracts and written signatures.")
        },
        "B",
        "MDM định nghĩa rõ ràng: CRM là hệ thống sở hữu thông tin đầu mối và liên hệ bán hàng (System of Record for Contacts/Leads), còn ERP là hệ thống sở hữu thông tin hóa đơn và hạn mức tín dụng.",
        "MDM reconciles conflicting master entity records across applications, governing canonical data lifecycles and authoritative data ownership.",
        "Baran & Galka (2017)", "Chapter 5 & 6", "pp. 168-174", ["mdm", "golden-record", "system-of-record"]
    ),
    (
        "q-04-13", "Vendor Lock-in Risk", "medium", "single_choice",
        "Khái niệm 'Bẫy phụ thuộc nhà cung cấp' (Vendor Lock-in) trong việc mua phần mềm CRM độc quyền thể hiện rủi ro nào?",
        "What risk does 'Vendor Lock-in' represent when procuring proprietary commercial CRM software suites?",
        {
            "A": ("Nhà cung cấp sẽ khóa cửa văn phòng không cho nhân viên công ty ra về.", "The software vendor physically padlocks corporate office doors at closing time."),
            "B": ("Dữ liệu, mã tùy biến và quy trình bị khóa chặt trong định dạng độc quyền của nhà cung cấp, khiến chi phí chuyển đổi (Switching Costs) sang giải pháp khác trở nên quá đắt đỏ và phức tạp.", "Customer data, custom code, and operating logic become tightly coupled to proprietary architectures, rendering migration to alternative platforms prohibitively expensive."),
            "C": ("Doanh nghiệp phải mua thêm cổ phần của công ty phần mềm.", "The purchasing firm is legally compelled to purchase corporate stock in the software vendor."),
            "D": ("Hệ thống CRM tự động từ chối cài đặt trên hệ điều hành Windows.", "The CRM software client refuses to execute on Microsoft Windows desktop environments.")
        },
        "B",
        "Vendor lock-in khiến doanh nghiệp mất vị thế đàm phán khi gia hạn hợp đồng và bị ép giá vì chi phí trích xuất dữ liệu và làm lại hệ thống là quá lớn.",
        "Proprietary formats and walled-garden cloud ecosystems create steep switching penalties, leaving enterprises vulnerable to aggressive renewal pricing hikes.",
        "Kostojohn et al. (2011)", "Chapter 4", "pp. 98-102", ["vendor-lock-in", "switching-costs", "procurement-risk"]
    ),
    (
        "q-04-14", "Service-Oriented Architecture", "hard", "single_choice",
        "Kiến trúc Hướng Dịch vụ (Service-Oriented Architecture - SOA) hoặc Microservices hỗ trợ mở rộng hệ thống CRM như thế nào?",
        "How does a Service-Oriented Architecture (SOA) or Microservices paradigm enhance enterprise CRM agility?",
        {
            "A": ("Bằng cách kết hợp toàn bộ mã nguồn của công ty thành một tệp thực thi duy nhất nặng 100GB.", "By compiling all enterprise software into a single 100-gigabyte monolithic binary."),
            "B": ("Bằng cách chia nhỏ các chức năng nghiệp vụ (như tính giá, gửi thông báo, tra cứu tồn kho) thành các dịch vụ độc lập, giao tiếp qua giao thức mở, giúp dễ dàng nâng cấp mà không làm sập toàn bộ hệ thống.", "By decomposing business capabilities (pricing, messaging, inventory checks) into loosely coupled autonomous services communicating via open standards, enabling modular upgrades without systemic downtime."),
            "C": ("Bằng cách yêu cầu tất cả người dùng phải học thuộc lòng các lệnh dòng lệnh DOS.", "By forcing all business users to memorize low-level DOS command-line syntax."),
            "D": ("Bằng cách loại bỏ hoàn toàn các giao diện đồ họa web.", "By completely eradicating graphic web user interfaces.")
        },
        "B",
        "Kiến trúc vi dịch vụ (Microservices/SOA) giúp hệ thống linh hoạt, cho phép cập nhật chức năng quản lý khách hàng mà không ảnh hưởng đến hệ thống thanh toán hay kho vận.",
        "Decoupled microservices architecture isolates faults and allows independent development and deployment of customer-facing modules without monolithic dependencies.",
        "Baran & Galka (2017)", "Chapter 6", "pp. 182-186", ["soa", "microservices", "modularity"]
    ),
    (
        "q-04-15", "CTI Integration", "medium", "single_choice",
        "Tính năng Tích hợp Máy tính và Điện thoại (Computer Telephony Integration - CTI) trong module CRM Dịch vụ Khách hàng mang lại lợi ích nổi bật nào?",
        "In customer contact center operations, what is the primary operational benefit of Computer Telephony Integration (CTI)?",
        {
            "A": ("Tự động phát nhạc hòa tấu cổ điển khi khách hàng ngắt máy.", "Automatically playing classical symphonies whenever an incoming caller hangs up."),
            "B": ("Tự động nhận diện số điện thoại người gọi đến, hiển thị ngay lập tức hồ sơ khách hàng (Screen Pop) trên màn hình của điện thoại viên trước khi nhấc máy.", "Automatically identifying caller phone numbers to trigger an instantaneous screen pop of the customer profile on the agent monitor before answering."),
            "C": ("Chuyển toàn bộ các cuộc gọi phàn nàn của khách hàng sang số điện thoại của đối thủ.", "Routing all angry inbound customer complaint calls to competitor telephone hotlines."),
            "D": ("Tự động tính tiền cước viễn thông cho người gọi với giá gấp 10 lần.", "Automatically charging callers ten times the standard telecommunications tariff.")
        },
        "B",
        "CTI giúp giao dịch viên biết ngay ai đang gọi đến, lịch sử mua hàng và các vấn đề mở, giúp chào đón khách hàng thân thiết bằng tên và rút ngắn thời gian xử lý.",
        "CTI screen pops eliminate repetitive customer authentication questions, reducing average handle time (AHT) and increasing first-call resolution (FCR).",
        "Baran & Galka (2017)", "Chapter 6", "pp. 184-188", ["cti", "contact-center", "screen-pop"]
    ),
    (
        "q-04-16", "Disaster Recovery & Backup", "medium", "single_choice",
        "Kế hoạch Khôi phục sau Thảm họa (Disaster Recovery - DR) cho hệ thống cơ sở dữ liệu CRM đo lường hai chỉ số RPO và RTO. Chúng có ý nghĩa gì?",
        "A Disaster Recovery (DR) plan for CRM databases tracks RPO and RTO. What do these metrics measure?",
        {
            "A": ("RPO = Số lượng khách hàng phản đối; RTO = Số lượng khách hàng đồng tình.", "RPO = Opposing customer count; RTO = Endorsing customer count."),
            "B": ("RPO (Mục tiêu Điểm Khôi phục) đo lường lượng dữ liệu tối đa chấp nhận bị mất; RTO (Mục tiêu Thời gian Khôi phục) đo lường thời gian tối đa để đưa hệ thống hoạt động trở lại.", "RPO (Recovery Point Objective) measures acceptable data loss window; RTO (Recovery Time Objective) measures maximum permissible downtime before restoration."),
            "C": ("RPO = Tỷ lệ chuyển đổi đơn hàng; RTO = Tỷ lệ hủy đơn hàng.", "RPO = Sales conversion velocity; RTO = Order return cancellation rate."),
            "D": ("RPO = Số lượng máy tính xách tay; RTO = Số lượng máy tính bàn.", "RPO = Deployed laptop inventory; RTO = Deployed desktop terminal count.")
        },
        "B",
        "RPO và RTO xác định mức độ sẵn sàng và ngân sách đầu tư cho hệ thống sao lưu dự phòng (backup) của trung tâm dữ liệu CRM.",
        "RPO dictates backup frequency to cap data loss in disaster events; RTO establishes architectural redundancy required to minimize business interruption.",
        "Kostojohn et al. (2011)", "Chapter 4", "pp. 106-110", ["dr", "rpo", "rto", "business-continuity"]
    ),
    (
        "q-04-17", "Multi-Tenant Architecture", "hard", "single_choice",
        "Đặc điểm cốt lõi của 'Kiến trúc Đa người thuê' (Multi-Tenant Architecture) trong các nền tảng Cloud CRM hiện đại như Salesforce hay HubSpot là gì?",
        "What defines the architectural core of 'Multi-Tenant Architecture' in modern Cloud CRM platforms such as Salesforce or HubSpot?",
        {
            "A": ("Nhiều công ty khách hàng cùng dùng chung một phiên bản ứng dụng và cơ sở dữ liệu vật lý hạ tầng, nhưng dữ liệu của từng công ty được phân tách logic an toàn tuyệt đối.", "Multiple customer enterprises share a single application instance and common hardware infrastructure, while each organization's data remains logically segregated and secured."),
            "B": ("Mỗi công ty khách hàng bắt buộc phải cử một nhân viên đến ở chung phòng ký túc xá với kỹ sư của Salesforce.", "Every customer company must send an employee to cohabitate in vendor engineering dormitories."),
            "C": ("Mỗi khách hàng được cấp riêng một tòa nhà trung tâm dữ liệu biệt lập.", "Each individual enterprise customer receives a dedicated physical data center building."),
            "D": ("Tất cả các công ty sử dụng hệ thống đều có thể xem trộm danh sách khách hàng của nhau.", "All subscriber corporations can view and share each other's proprietary customer accounts.")
        },
        "A",
        "Multi-tenancy giúp nhà cung cấp tối ưu hóa hiệu năng, giảm chi phí vận hành và cập nhật phiên bản mới đồng loạt cho mọi khách hàng mà không làm gián đoạn hệ thống.",
        "Multi-tenancy maximizes infrastructure efficiency, ensuring all clients benefit from seamless, centralized platform upgrades while maintaining complete logical data isolation.",
        "Baran & Galka (2017)", "Chapter 6", "pp. 180-184", ["multi-tenancy", "cloud-architecture"]
    ),
    (
        "q-04-18", "Data Migration Tooling", "medium", "single_choice",
        "Khi thực hiện chuyển đổi dữ liệu (Data Migration) từ các hệ thống cũ sang nền tảng CRM mới, bước nào sau đây là quan trọng nhất?",
        "When executing legacy Data Migration into a newly implemented CRM platform, which technical step is most vital?",
        {
            "A": ("Sao chép toàn bộ dữ liệu rác, trùng lặp và thiếu sót từ hệ thống cũ sang hệ thống mới để tiết kiệm thời gian.", "Copying all duplicate, corrupt, and legacy junk records directly into the new production database to expedite cutover."),
            "B": ("Ánh xạ trường dữ liệu (Field Mapping), làm sạch dữ liệu cũ trước khi nạp, và tiến hành nạp thử nghiệm (Mock Runs) trên môi trường kiểm thử (Sandbox).", "Field schema mapping, rigorous pre-load data cleansing, and conducting mock migration dry-runs in an isolated sandbox environment."),
            "C": ("Xóa vĩnh viễn toàn bộ cơ sở dữ liệu cũ trước khi bắt đầu triển khai hệ thống mới.", "Permanently wiping all legacy operational databases prior to initiating new software deployment."),
            "D": ("Nhập dữ liệu bằng tay từng bản ghi một mà không sử dụng công cụ nạp tự động.", "Manually re-typing millions of customer records keystroke-by-keystroke without automated tools.")
        },
        "B",
        "Nạp thử nghiệm (Mock Migration) giúp phát hiện xung đột định dạng trường dữ liệu và loại bỏ dữ liệu rác trước khi tiến hành chuyển đổi chính thức trên môi trường thật.",
        "Mock migration rehearsals in a sandbox surface schema transformation errors, identify boundary constraints, and ensure clean production data loading on go-live day.",
        "Kostojohn et al. (2011)", "Chapter 5 & 6", "pp. 142-148, 168-172", ["data-migration", "mock-runs", "sandbox"]
    ),
    (
        "q-04-19", "Automated Workflow Engine", "easy", "single_choice",
        "Công cụ tự động hóa luồng công việc (Workflow Engine) trong CRM cho phép thiết lập hành động nào sau đây?",
        "What capability does an automated CRM Workflow Engine provide to business process designers?",
        {
            "A": ("Tự động tạo nhiệm vụ cho nhân viên kinh doanh khi có một cơ hội mới đạt giá trị trên 50.000 USD hoặc gửi email thông báo khi khiếu nại quá hạn 24 giờ.", "Automatically spawning tasks for reps when an opportunity exceeds $50,000, or routing alert emails when an urgent customer ticket exceeds a 24-hour SLA breach threshold."),
            "B": ("Tự động sa thải nhân viên khi họ đi làm muộn 5 phút.", "Automatically generating termination letters for staff clocking in five minutes late."),
            "C": ("Tự động tắt nguồn máy tính của giám đốc khi giá cổ phiếu giảm.", "Automatically cutting executive PC power when global financial stock indices dip."),
            "D": ("Tự động thay đổi giá bán sản phẩm trên hóa đơn thành 0 đồng.", "Automatically setting invoice product billing totals to zero dollars.")
        },
        "A",
        "Workflow rules giúp chuẩn hóa quy trình, tự động hóa các tác vụ lặp đi lặp lại và đảm bảo các cam kết chất lượng dịch vụ (SLA) được thực thi nhất quán.",
        "Workflow engines eliminate administrative friction, triggering conditional notifications, task assignments, and field updates based on business logic rules.",
        "Kostojohn et al. (2011)", "Chapter 1 & 4", "pp. 20-22, 92-96", ["workflow-automation", "business-rules"]
    ),
    (
        "q-04-20", "Open Source CRM Considerations", "hard", "single_choice",
        "Khi một doanh nghiệp cân nhắc triển khai phần mềm CRM Mã nguồn mở (Open Source CRM như SuiteCRM hay Odoo), sự đánh đổi (trade-off) chiến lược lớn nhất là gì?",
        "When evaluating an Open Source CRM platform (e.g., SuiteCRM or Odoo), what is the primary strategic trade-off?",
        {
            "A": ("Phần mềm mã nguồn mở không cho phép kết nối máy in văn phòng.", "Open-source packages prohibit connectivity to physical desktop paper printers."),
            "B": ("Tiết kiệm chi phí bản quyền ban đầu và toàn quyền kiểm soát mã nguồn, nhưng đòi hỏi năng lực kỹ thuật nội bộ cao, tự chịu trách nhiệm về an ninh mạng, lưu trữ và nâng cấp bảo trì.", "Zero software licensing overhead and complete source code autonomy, traded off against the heavy burden of in-house technical support, security patching, hosting, and manual version upgrades."),
            "C": ("Phần mềm mã nguồn mở chỉ hoạt động được tại các nước Bắc Âu.", "Open-source distributions are legally restricted to execution in Scandinavian nations."),
            "D": ("Doanh nghiệp phải công khai toàn bộ bí mật kinh doanh lên mạng xã hội.", "The enterprise is legally obligated to publish all proprietary customer strategies on public blogs.")
        },
        "B",
        "Mã nguồn mở 'miễn phí bản quyền như một chú cún con miễn phí' - bạn không tốn tiền mua nhưng tốn rất nhiều công sức chăm sóc, nuôi dưỡng và duy trì.",
        "Open source CRM provides free code licensing, but shifts the entire burden of architecture, cybersecurity, and maintenance onto enterprise internal engineering teams.",
        "Kostojohn et al. (2011)", "Chapter 4", "pp. 100-104", ["open-source-crm", "tco", "architectural-tradeoffs"]
    )
]

for item in e4:
    questions_batch2.append(make_q(
        item[0], "EXAM-04", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

# ==========================================
# EXAM 05: ROADMAP DESIGN & IMPLEMENTATION PLANNING (q-05-01 to q-05-20)
# ==========================================
e5 = [
    (
        "q-05-01", "Phased Rollout vs Big Bang", "medium", "single_choice",
        "Tại sao chiến lược triển khai phân kỳ (Phased / Iterative Rollout) luôn được các chuyên gia CRM khuyến nghị hơn phương pháp 'Big Bang' (triển khai toàn bộ cùng lúc)?",
        "Why is a Phased / Iterative Rollout strategy universally recommended over a 'Big Bang' deployment for enterprise CRM?",
        {
            "A": ("Vì phương pháp Big Bang làm tốn nhiều giấy in hợp đồng hơn.", "Because Big Bang rollouts consume more printed contract reams."),
            "B": ("Triển khai phân kỳ giúp giảm thiểu rủi ro vận hành, sớm mang lại giá trị thấy được (Quick Wins), tạo điều kiện tiếp thu phản hồi thực tế từ người dùng và điều chỉnh lộ trình kịp thời.", "Phased rollouts isolate operational risk, deliver early quick wins, incorporate continuous real-world user feedback, and allow agile architectural adjustments before broader rollout."),
            "C": ("Vì nhà cung cấp phần mềm từ chối bàn giao toàn bộ tính năng trong một lần.", "Because software vendors refuse to release complete code builds in single batches."),
            "D": ("Vì pháp luật yêu cầu mỗi dự án CRM phải kéo dài ít nhất 10 năm.", "Because corporate regulatory statutes mandate that all CRM initiatives take ten years.")
        },
        "B",
        "Triển khai Big Bang mang rủi ro thảm họa nếu phát sinh sự cố hệ thống; phân kỳ theo chức năng hoặc chi nhánh giúp tổ chức kiểm soát tốt hơn và tích lũy bài học kinh nghiệm.",
        "Big Bang deployments invite systemic failure if unexpected gaps emerge; incremental phased releases de-risk investment and build organizational adoption confidence.",
        "Kostojohn et al. (2011)", "Chapter 3 & 5", "pp. 60-66, 128-134", ["phased-rollout", "big-bang", "risk-mitigation"]
    ),
    (
        "q-05-02", "Scope Creep Management", "hard", "single_choice",
        "Hiện tượng 'Phình phạm vi' (Scope Creep) trong dự án CRM là gì và làm thế nào để kiểm soát nó hiệu quả nhất?",
        "What is 'Scope Creep' in a CRM project and what is the primary mechanism to control it?",
        {
            "A": ("Hiện tượng màn hình máy tính hiển thị quá nhiều màu sắc rực rỡ; giải pháp là chuyển sang màn hình đen trắng.", "Computer displays rendering overly bright color palettes; resolved by reverting to monochrome terminals."),
            "B": ("Sự gia tăng không kiểm soát của các yêu cầu tính năng mới vượt quá phạm vi và ngân sách ban đầu; kiểm soát bằng quy trình Quản lý Yêu cầu Thay đổi chính thức (Formal Change Control Process) do Ban Chỉ đạo phê duyệt.", "Uncontrolled expansion of project deliverables beyond approved budgets and schedules; controlled via a formal Change Control Process requiring Steering Committee evaluation."),
            "C": ("Hiện tượng nhân viên làm việc quá nhanh trước thời hạn; giải pháp là cho nhân viên nghỉ phép.", "Staff completing tasks ahead of schedule; resolved by forcing mandatory vacations."),
            "D": ("Việc phần mềm tự động xóa các bảng dữ liệu cũ; giải pháp là cài đặt lại Windows.", "Software automatically wiping database tables; resolved by reformatting servers.")
        },
        "B",
        "Mọi yêu cầu phát sinh phải được đưa vào danh sách chờ (Backlog) để đánh giá tác động đến chi phí và thời gian, tránh làm vỡ kế hoạch của phiên bản hiện tại.",
        "Scope creep dilutes project velocity and drains reserves; rigorous change control defers non-critical enhancements to subsequent release phases.",
        "Kostojohn et al. (2011)", "Chapter 5", "pp. 136-141", ["scope-creep", "change-control", "project-governance"]
    ),
    (
        "q-05-03", "Work Breakdown Structure", "medium", "single_choice",
        "Cơ cấu Phân chia Công việc (Work Breakdown Structure - WBS) trong giai đoạn lập kế hoạch CRM có mục đích cốt lõi là gì?",
        "What is the foundational purpose of a Work Breakdown Structure (WBS) during CRM project planning?",
        {
            "A": ("Phân chia khẩu phần ăn trưa của các thành viên trong nhóm kỹ thuật.", "Allocating daily luncheon meal rations among technical development team members."),
            "B": ("Phân rã toàn bộ phạm vi dự án thành các gói công việc (work packages) nhỏ hơn, có thể quản lý, ước lượng thời gian, chi phí và giao trách nhiệm cụ thể.", "Hierarchically decomposing project deliverables into manageable, verifiable work packages with clear cost, schedule, and ownership boundaries."),
            "C": ("Lập danh sách các trang web bị cấm truy cập trong giờ làm việc.", "Cataloging forbidden websites during corporate business office hours."),
            "D": ("Ghi lại số lần gõ bàn phím của từng lập trình viên trong một giờ.", "Logging developer keystroke counts per elapsed programming hour.")
        },
        "B",
        "WBS là nền tảng để xây dựng sơ đồ Gantt, xác định đường găng (critical path) và theo dõi tiến độ hoàn thành các mốc quan trọng của dự án.",
        "A WBS provides the architectural blueprint for resource assignment, task duration estimation, dependency sequencing, and progress verification.",
        "Kostojohn et al. (2011)", "Chapter 5", "pp. 125-132", ["wbs", "project-planning", "milestones"]
    ),
    (
        "q-05-04", "Risk Register Components", "hard", "single_choice",
        "Một Sổ theo dõi Rủi ro (Risk Register) đạt chuẩn trong dự án CRM phải bao gồm những trường thông tin tối thiểu nào?",
        "A standard CRM project Risk Register must document which minimal set of parameters for each identified threat?",
        {
            "A": ("Mô tả rủi ro, Xác suất xảy ra (Probability), Mức độ tác động (Impact), Điểm rủi ro, Kế hoạch giảm thiểu/ứng phó (Mitigation Plan), và Người chịu trách nhiệm theo dõi (Owner).", "Risk description, Probability of occurrence, Severity of impact, Risk score, Mitigation/contingency plan, and assigned Risk Owner."),
            "B": ("Tên rủi ro, Số điện thoại của cảnh sát, và Địa chỉ bệnh viện gần nhất.", "Risk label, local police dispatch phone number, and nearest hospital address."),
            "C": ("Số tiền thưởng cho nhân viên nào phát hiện ra lỗi chính tả trong hợp đồng.", "Employee bonus amounts for flagging typographical errors in procurement forms."),
            "D": ("Mã định danh của các thiết bị phát wifi trong phòng họp.", "Physical MAC addresses of wireless internet routers installed in boardrooms.")
        },
        "A",
        "Risk Register giúp đội ngũ dự án chủ động nhận diện các mối đe dọa (như kháng cự của người dùng, chậm trễ dữ liệu) và chuẩn bị trước phương án xử lý thay vì bị động chữa cháy.",
        "A proactive risk log tracks risk velocity and mandates actionable mitigation contingencies, ensuring executive sponsors maintain visibility over critical blockers.",
        "Kostojohn et al. (2011)", "Chapter 5", "pp. 145-150", ["risk-register", "risk-management"]
    ),
    (
        "q-05-05", "Quick Wins Strategy", "easy", "single_choice",
        "Tại sao việc tạo ra các 'Chiến thắng Nhanh' (Quick Wins) trong 3 đến 6 tháng đầu tiên của dự án CRM lại có ý nghĩa sống còn?",
        "Why is delivering 'Quick Wins' within the first 3 to 6 months of a CRM initiative critical to overall success?",
        {
            "A": ("Để có lý do tổ chức tiệc ăn mừng tại khách sạn sang trọng.", "To provide a valid justification for hosting lavish weekend resort parties."),
            "B": ("Chứng minh giá trị thực tế của hệ thống, củng cố niềm tin của ban lãnh đạo và người dùng, đập tan tâm lý hoài nghi và tạo động lực thúc đẩy các giai đoạn tiếp theo.", "Demonstrating tangible business value early, validating executive investment, dispelling end-user cynicism, and building organizational momentum for subsequent phases."),
            "C": ("Để thanh lý sớm hợp đồng với nhà tư vấn và tự làm toàn bộ.", "To prematurely terminate external consulting contracts and proceed unassisted."),
            "D": ("Vì sau 6 tháng ban giám đốc sẽ tự động cắt giảm 90% nhân sự.", "Because corporate executives automatically lay off 90% of staff after six months.")
        },
        "B",
        "Quick Wins (như giải quyết được bài toán báo cáo doanh thu tự động cho sếp hoặc tự động gửi email chào mừng khách mới) giúp tạo dựng uy tín cho nhóm dự án.",
        "Visible quick wins validate the business case, generate positive executive buzz, and disarm organizational resistance by illustrating tangible personal benefits.",
        "Kostojohn et al. (2011)", "Chapter 3", "pp. 68-72", ["quick-wins", "change-momentum", "roi"]
    ),
    (
        "q-05-06", "Gap Analysis in CRM", "medium", "single_choice",
        "Hoạt động 'Phân tích Khoảng cách' (Gap Analysis / Fit-Gap Analysis) trong giai đoạn lập kế hoạch CRM là gì?",
        "What does a 'Fit-Gap Analysis' entail during CRM implementation planning?",
        {
            "A": ("Đo khoảng cách vật lý giữa hai máy chủ trong phòng công nghệ thông tin.", "Measuring the physical distance between two server racks in the data center."),
            "B": ("So sánh giữa các quy trình nghiệp vụ mong muốn trong tương lai (To-Be) với năng lực sẵn có nguyên bản (Out-of-the-Box) của phần mềm để xác định những khoảng trống cần cấu hình hoặc tùy biến.", "Comparing envisioned future-state business workflows (To-Be) against native out-of-the-box software capabilities to identify gaps requiring configuration or custom engineering."),
            "C": ("So sánh bảng lương của nhân viên phòng bán hàng với phòng kế toán.", "Comparing salary compensation tiers between sales staff and accounting clerks."),
            "D": ("Tìm kiếm các khoảng trống trên tường văn phòng để treo áp phích cổ động.", "Locating open wall space in corporate corridors to hang motivational posters.")
        },
        "B",
        "Fit-Gap Analysis chỉ ra tính năng nào phần mềm đáp ứng sẵn (Fit) và tính năng nào cần chỉnh sửa quy trình hoặc viết code bổ sung (Gap), từ đó dự toán chi phí và thời gian chính xác.",
        "Fit-gap exercises determine whether gaps should be closed by adapting internal business workflows (preferred) or coding expensive custom modifications.",
        "Kostojohn et al. (2011)", "Chapter 5", "pp. 132-137", ["fit-gap-analysis", "to-be-process", "requirements"]
    ),
    (
        "q-05-07", "Project Budget Buffering", "hard", "single_choice",
        "Theo thông lệ quản lý dự án CRM của Kostojohn et al., tỷ lệ ngân sách dự phòng (Contingency Reserve) khuyến nghị nên dành cho các chi phí phát sinh ngoài dự kiến là:",
        "According to CRM implementation management best practices in Kostojohn et al., the recommended Contingency Reserve percentage for unforeseen costs is:",
        {
            "A": ("0% vì kế hoạch dự án phải chính xác tuyệt đối.", "0% because well-constructed project plans should be mathematically infallible."),
            "B": ("15% đến 20% tổng ngân sách dự án để ứng phó với các yêu cầu tích hợp phức tạp hơn dự kiến, làm sạch dữ liệu và thay đổi nhân sự.", "15% to 20% of total project budget to absorb unexpected integration complexity, data hygiene overruns, and staffing adjustments."),
            "C": ("95% tổng ngân sách.", "95% of total enterprise operating budget."),
            "D": ("Dự phòng bằng toàn bộ doanh thu năm trước của công ty.", "Buffering with the entire gross corporate revenue of the preceding fiscal year.")
        },
        "B",
        "Dự án CRM hiếm khi đi đúng 100% ngân sách lý thuyết do các phát sinh về dữ liệu cũ bị bẩn hoặc tích hợp hệ thống gặp trục trặc kỹ thuật ngoài tầm kiểm soát.",
        "Unforeseen data migration hurdles and legacy API integration quirks routinely demand financial buffers; a 15–20% reserve prevents project paralysis.",
        "Kostojohn et al. (2011)", "Chapter 3 & 5", "pp. 72-76, 148-152", ["contingency-reserve", "budgeting", "financial-planning"]
    ),
    (
        "q-05-08", "Critical Path Method", "medium", "single_choice",
        "Trong sơ đồ tiến độ dự án CRM, 'Đường găng' (Critical Path) là:",
        "In a CRM project schedule network diagram, what does the 'Critical Path' represent?",
        {
            "A": ("Lối thoát hiểm khẩn cấp khi tòa nhà văn phòng xảy ra hỏa hoạn.", "The physical emergency fire egress corridor inside the corporate office building."),
            "B": ("Chuỗi các công việc phụ thuộc lẫn nhau có tổng thời gian dài nhất, quyết định thời điểm hoàn thành sớm nhất của toàn bộ dự án; bất kỳ sự chậm trễ nào trên đường găng cũng làm lùi ngày bàn giao dự án.", "The longest contiguous sequence of dependent tasks determining the minimum project duration; any delay to a task on the critical path directly postpones project completion."),
            "C": ("Đường dây điện cao thế cấp điện cho trung tâm dữ liệu.", "The primary high-voltage electrical cable powering the corporate data facility."),
            "D": ("Danh sách các công việc không quan trọng có thể bỏ qua mà không cần làm.", "A list of inconsequential trivial tasks that may be arbitrarily skipped.")
        },
        "B",
        "Người quản lý dự án phải tập trung giám sát chặt chẽ các nhiệm vụ trên đường găng (như ánh xạ dữ liệu, phê duyệt thiết kế quy trình) để không làm vỡ hạn chót.",
        "Project managers must fiercely guard critical path activities against slippage, as every day lost on these milestones pushes out final production cutover.",
        "Kostojohn et al. (2011)", "Chapter 5", "pp. 128-132", ["critical-path", "schedule-management", "gantt"]
    ),
    (
        "q-05-09", "Agile vs Waterfall in CRM", "hard", "single_choice",
        "Lợi thế lớn nhất của việc áp dụng phương pháp luận Linh hoạt (Agile / Scrum) so với Thác nước (Waterfall) trong triển khai cấu hình CRM là gì?",
        "What is the most significant operational advantage of leveraging Agile (Scrum) over traditional Waterfall for CRM declarative configuration?",
        {
            "A": ("Agile cho phép loại bỏ hoàn toàn giai đoạn kiểm thử phần mềm.", "Agile completely eliminates the need to perform software quality testing."),
            "B": ("Agile chia nhỏ dự án thành các chu kỳ chạy nước rút (Sprints 2-3 tuần), bàn giao các tính năng hoạt động được liên tục, giúp người dùng sớm trải nghiệm và phản hồi trước khi cấu hình đi quá xa thực tế.", "Agile delivers functional software increments in short 2–3 week sprints, enabling rapid user validation, frequent inspection, and continuous requirement refinement."),
            "C": ("Agile cho phép lập trình viên làm việc mà không cần biết mục tiêu của dự án là gì.", "Agile allows software engineers to build features without understanding business objectives."),
            "D": ("Agile đảm bảo không bao giờ phát sinh bất kỳ lỗi kỹ thuật nào.", "Agile guarantees that software code will possess zero technical bugs.")
        },
        "B",
        "Phương pháp Agile giúp khắc phục tình trạng 'sau 12 tháng làm việc kín phòng, nhóm IT bàn giao một hệ thống hoàn toàn khác với những gì người dùng thực sự cần'.",
        "Agile sprints expose design mismatches early, ensuring software evolves iteratively in sync with evolving user realities rather than delivering rigid year-old specs.",
        "Kostojohn et al. (2011)", "Chapter 5", "pp. 138-144", ["agile", "scrum", "waterfall", "iterative-development"]
    ),
    (
        "q-05-10", "Resource Allocation Matrix", "medium", "single_choice",
        "Ma trận Phân định Trách nhiệm RACI trong kế hoạch dự án CRM là viết tắt của 4 vai trò nào?",
        "In CRM project governance frameworks, what do the four letters in a RACI Matrix designate?",
        {
            "A": ("Responsible (Người trực tiếp thực hiện), Accountable (Người chịu trách nhiệm giải trình cuối cùng), Consulted (Người được tham vấn ý kiến), Informed (Người được thông báo cập nhật).", "Responsible, Accountable, Consulted, and Informed."),
            "B": ("Review, Approve, Cancel, Ignore", "Review, Approve, Cancel, Ignore"),
            "C": ("Read, Access, Copy, Install", "Read, Access, Copy, Install"),
            "D": ("Report, Audit, Calculate, Invest", "Report, Audit, Calculate, Invest")
        },
        "A",
        "RACI làm rõ trách nhiệm của từng bên liên quan (ai là người làm, ai là người duyệt cuối cùng, ai cần hỏi ý kiến, ai chỉ cần nhận thông báo), tránh đùn đẩy trách nhiệm.",
        "A RACI matrix eliminates accountability vacuums, ensuring every project deliverable has exactly one accountable owner and clear communication lines.",
        "Kostojohn et al. (2011)", "Chapter 5", "pp. 142-146", ["raci", "governance", "roles-and-responsibilities"]
    ),
    (
        "q-05-11", "Legacy System Sunsetting Plan", "medium", "single_choice",
        "Kế hoạch 'Cho ngừng hoạt động hệ thống cũ' (Legacy System Sunsetting / Decommissioning) cần lưu ý điều gì quan trọng nhất?",
        "What is the most critical consideration when formulating a Legacy System Sunsetting (Decommissioning) plan during CRM migration?",
        {
            "A": ("Đập phá ngay máy chủ cũ vào đúng ngày khai trương hệ thống mới.", "Physically smashing legacy hardware servers on new system go-live day."),
            "B": ("Xác lập rõ thời hạn chấm dứt nhập liệu trên hệ thống cũ, duy trì bản sao lưu lưu trữ (Archive) chỉ đọc để phục vụ yêu cầu kiểm toán pháp lý và lịch sử dữ liệu.", "Setting a definitive cut-off date for legacy write operations while preserving read-only immutable archives to satisfy compliance and historical audit mandates."),
            "C": ("Bắt buộc khách hàng phải tự lưu trữ lịch sử đơn hàng của mình.", "Requiring consumers to self-host their historical order transaction archives."),
            "D": ("Tặng máy chủ cũ cho nhân viên mang về nhà chơi điện tử.", "Donating retired enterprise servers to frontline staff for recreational gaming.")
        },
        "B",
        "Nếu không có ngày khóa sổ (cut-off) dứt khoát, nhân viên sẽ tiếp tục dùng lén hệ thống cũ; đồng thời lưu trữ dữ liệu chỉ đọc là bắt buộc theo luật thuế và kế toán.",
        "Clear cut-off dates prevent employees from retreating to legacy habits, while read-only archives maintain compliance with statutory financial retention laws.",
        "Kostojohn et al. (2011)", "Chapter 5 & 7", "pp. 154-158, 222-225", ["sunsetting", "legacy-systems", "compliance-archive"]
    ),
    (
        "q-05-12", "Data Cleansing Milestone Placement", "hard", "single_choice",
        "Trong tiến độ dự án triển khai CRM, hoạt động Vệ sinh Dữ liệu (Data Cleansing) nên được bắt đầu vào thời điểm nào?",
        "Within an enterprise CRM project schedule, when should the Data Cleansing workstream officially commence?",
        {
            "A": ("Sau khi hệ thống mới đã chính thức vận hành được 6 tháng.", "Six months after the new production system has already gone live."),
            "B": ("Ngay từ giai đoạn đầu của dự án (Analysis & Planning), song song với quá trình phân tích thiết kế quy trình.", "At the very inception of the project (Analysis & Planning phase), running in parallel with workflow discovery."),
            "C": ("Vào đúng 24 giờ trước thời điểm cắt chuyển hệ thống (Go-Live Cutover).", "Exactly twenty-four hours prior to final production cutover."),
            "D": ("Chỉ tiến hành khi khách hàng gửi đơn kiện công ty vì gửi nhầm hóa đơn.", "Only after a client files a civil lawsuit over an erroneous invoice dispatch.")
        },
        "B",
        "Vệ sinh dữ liệu luôn tốn nhiều thời gian gấp đôi so với dự kiến ban đầu; nếu để sát ngày mới làm thì 100% dự án sẽ bị vỡ tiến độ hoặc nạp dữ liệu bẩn vào hệ thống mới.",
        "Data profiling and scrubbing invariably uncovers massive unforeseen rot; deferring cleansing until late stages universally causes catastrophic go-live delays.",
        "Kostojohn et al. (2011)", "Chapter 5", "pp. 146-150", ["data-cleansing", "project-schedule", "early-start"]
    ),
    (
        "q-05-13", "Stakeholder Matrix Mapping", "medium", "single_choice",
        "Khi phân tích các bên liên quan (Stakeholder Analysis), nhóm đối tượng có 'Quyền lực cao nhưng Mức độ ủng hộ thấp' (High Power, Low Support) cần được quản lý theo chiến lược nào?",
        "In CRM Stakeholder Mapping, which management strategy must be applied to individuals possessing 'High Influence / Low Alignment' (High Power, Low Support)?",
        {
            "A": ("Phớt lờ hoàn toàn và không mời họ tham dự bất kỳ cuộc họp nào.", "Completely ignoring them and barring them from all project meetings."),
            "B": ("Chủ động tiếp cận sâu sát, lắng nghe và thấu hiểu nguyên nhân lo ngại, giải quyết các khúc mắc về quyền lợi và tìm cách chuyển hóa họ thành đồng minh chiến lược.", "Engaging intensely in 1-on-1 consultations, uncovering root objections, addressing structural concerns, and proactively converting them into strategic allies."),
            "C": ("Công khai chỉ trích họ trước toàn thể công ty trong cuộc họp toàn thể.", "Publicly reprimanding their skepticism during company-wide town halls."),
            "D": ("Chỉ gửi cho họ các bản tin tiếp thị quảng cáo ngoài trời.", "Mailing them standard public consumer billboards.")
        },
        "B",
        "Những nhân sự có quyền lực cao nhưng phản đối (ví dụ: một Giám đốc Bán hàng khu vực kỳ cựu) có thể phá hỏng cả dự án nếu không được hòa giải và tháo gỡ lo lắng.",
        "High-power detractors possess the political capital to derail implementations; executive sponsors must actively manage their concerns to preempt silent vetoes.",
        "Kostojohn et al. (2011)", "Chapter 2 & 3", "pp. 40-45, 64-68", ["stakeholder-analysis", "change-strategy"]
    ),
    (
        "q-05-14", "Contingency Fallback Planning", "hard", "single_choice",
        "Kế hoạch Dự phòng Rút lui (Rollback / Fallback Plan) trong triển khai phần mềm CRM quy định điều gì?",
        "What does a CRM implementation Fallback / Rollback Plan formally prescribe?",
        {
            "A": ("Kế hoạch trả lại tiền bản quyền cho nhà cung cấp nếu giá cổ phiếu giảm.", "Procedures to demand software refund checks if tech stock prices slide."),
            "B": ("Kịch bản các bước kỹ thuật khẩn cấp và tiêu chí kích hoạt để hoàn nguyên hệ thống về trạng thái cũ an toàn nếu đợt triển khai trực tiếp gặp sự cố nghiêm trọng không thể khắc phục ngay.", "Detailed technical procedures and trigger thresholds to revert environments back to the stable pre-launch state if catastrophic, unresolvable issues occur during go-live cutover."),
            "C": ("Hướng dẫn nhân viên cách xin nghỉ việc đồng loạt.", "Guidelines instructing staff how to execute synchronized resignations."),
            "D": ("Quy trình tắt nguồn toàn bộ hệ thống internet của thành phố.", "Protocols to shut down the entire municipal metropolitan internet grid.")
        },
        "B",
        "Một kế hoạch triển khai chuyên nghiệp luôn phải có đường lùi an toàn được định nghĩa trước (Rollback Strategy) để bảo vệ hoạt động kinh doanh liên tục nếu ngày Golive thất bại.",
        "A rollback plan is an indispensable insurance policy, establishing clear criteria and technical execution scripts to restore business continuity if deployment fails.",
        "Kostojohn et al. (2011)", "Chapter 5 & 6", "pp. 152-156, 172-176", ["rollback-plan", "business-continuity", "cutover"]
    ),
    (
        "q-05-15", "Minimum Viable Product in CRM", "easy", "single_choice",
        "Khái niệm Sản phẩm Khả dụng Tối thiểu (Minimum Viable Product - MVP) khi áp dụng vào giai đoạn 1 của dự án CRM có nghĩa là gì?",
        "What does a 'Minimum Viable Product' (MVP) represent in Phase 1 of an enterprise CRM rollout?",
        {
            "A": ("Hệ thống CRM chỉ chứa đúng một tên khách hàng duy nhất.", "A CRM software package containing exactly one customer account record."),
            "B": ("Phiên bản hệ thống ban đầu chỉ chứa các tính năng cốt lõi nhất đủ để người dùng vận hành trơn tru và mang lại giá trị thiết thực, tránh ôm đồm phức tạp.", "The lean initial system release featuring only core essential workflows required to solve baseline business friction and deliver immediate utility without bloated complexity."),
            "C": ("Phần mềm rẻ tiền bị lỗi 90% các chức năng.", "A heavily discounted software build with 90% non-functioning features."),
            "D": ("Bản vẽ giao diện trên giấy ăn chưa lập trình.", "A conceptual interface wireframe sketched on a paper luncheon napkin.")
        },
        "B",
        "MVP giúp đưa hệ thống vào sử dụng thực tế sớm nhất có thể, tránh tình trạng thiết kế cầu toàn kéo dài nhiều năm mà không mang lại kết quả.",
        "An MVP establishes early baseline operational utility, prioritizing must-have workflows and validating adoption before layering on advanced automation.",
        "Kostojohn et al. (2011)", "Chapter 3 & 5", "pp. 62-66, 130-134", ["mvp", "lean-implementation", "phase-1"]
    ),
    (
        "q-05-16", "Vendor SLA Negotiations", "medium", "single_choice",
        "Khi đàm phán Thỏa thuận Mức độ Dịch vụ (SLA) với nhà cung cấp Cloud CRM, chỉ số Uptime tối thiểu phổ biến đạt chuẩn cho các doanh nghiệp thương mại là:",
        "When negotiating a Service Level Agreement (SLA) with a commercial Cloud CRM host, the industry-standard minimum enterprise Uptime guarantee is typically:",
        {
            "A": ("50.0% Uptime (cho phép sập máy chủ 15 ngày mỗi tháng).", "50.0% Uptime (permitting fifteen days of outages monthly)."),
            "B": ("99.9% Uptime ('Ba số 9') hoặc 99.95%, kèm theo các điều khoản bồi thường tài chính (Service Credits) nếu vi phạm.", "99.9% ('Three Nines') or 99.95% Uptime, accompanied by financial service credit penalties for unexcused outages."),
            "C": ("100.0% tuyệt đối không bao giờ được phép mất kết nối dù thiên tai xảy ra.", "Absolute 100.0% with zero downtime permitted even under extreme natural disasters."),
            "D": ("20.0% Uptime.", "20.0% Uptime.")
        },
        "B",
        "Chuẩn 'Three Nines' (99.9%) cho phép thời gian chết không mong muốn tối đa khoảng 8.7 giờ mỗi năm; vi phạm cam kết này nhà cung cấp phải đền bù phí dịch vụ.",
        "Enterprise cloud contracts standardise on 99.9% or 99.95% uptime guarantees backed by clear financial remedies (service credits) if outages breach agreed thresholds.",
        "Kostojohn et al. (2011)", "Chapter 4", "pp. 96-100", ["sla", "uptime", "vendor-contracts"]
    ),
    (
        "q-05-17", "User Journey Mapping", "medium", "single_choice",
        "Hoạt động 'Vẽ Bản đồ Hành trình Người dùng Nội bộ' (Internal User Journey Mapping) trước khi cấu hình CRM giúp ích gì?",
        "How does 'Internal User Journey Mapping' assist business analysts prior to CRM configuration?",
        {
            "A": ("Vẽ sơ đồ chỉ dẫn đường đi từ nhà nhân viên đến cơ quan để tránh tắc đường.", "Plotting commuting routes from employee residences to corporate offices to avoid traffic."),
            "B": ("Ghi lại từng bước thao tác hàng ngày của nhân viên (như nhân viên bán hàng tiếp nhận đầu mối, gọi điện, gửi báo giá) để tối ưu hóa số lượng cú nhấp chuột và tự động hóa thao tác.", "Documenting daily staff touchpoints (lead intake, dialing, quote drafting) to optimize screen flow, eliminate redundant clicks, and automate repetitive administrative burdens."),
            "C": ("Xác định ai là người đi bộ nhiều nhất trong khuôn viên công ty.", "Measuring which employee logs the highest pedometer count across corridors."),
            "D": ("Vẽ tranh phong cảnh trang trí cho văn phòng làm việc.", "Painting aesthetic landscapes to decorate corporate conference rooms.")
        },
        "B",
        "Hiểu được hành trình thao tác của nhân viên giúp đội ngũ kỹ thuật thiết kế giao diện CRM tiện lợi, giảm thiểu sự ức chế khi phải nhấp chuột qua quá nhiều màn hình.",
        "Understanding front-line cognitive friction allows designers to build streamlined layouts that respect user workflow tempo and drive voluntary adoption.",
        "Baran & Galka (2017) p. 118; Kostojohn (2011) p. 134", "Chapter 4", "pp. 118-122", ["user-journey", "ux-design", "adoption"]
    ),
    (
        "q-05-18", "Project Communication Cadence", "easy", "single_choice",
        "Trong giai đoạn triển khai dự án CRM, bản tin cập nhật tiến độ (Project Status Newsletter / Briefing) nên được gửi đến toàn thể công ty với mục đích gì?",
        "What is the strategic objective of circulating periodic Project Status Briefings to all enterprise staff during a CRM rollout?",
        {
            "A": ("Để khoe khoang thành tích cá nhân của giám đốc dự án.", "Flaunting the individual career achievements of the project manager."),
            "B": ("Duy trì sự minh bạch, thông báo các mốc tiến độ đã đạt được, giới thiệu các tính năng sắp ra mắt và chuẩn bị tâm lý sẵn sàng đón nhận thay đổi cho người dùng.", "Maintaining transparency, celebrating accomplished milestones, previewing upcoming capabilities, and fostering psychological readiness for change across business units."),
            "C": ("Cảnh báo nhân viên không được phép bàn luận về dự án trong giờ ăn trưa.", "Forbidding employees from discussing the deployment during lunch hours."),
            "D": ("Yêu cầu nhân viên đóng tiền ủng hộ kinh phí mua bản quyền phần mềm.", "Soliciting personal cash donations from staff to subsidize software licenses.")
        },
        "B",
        "Truyền thông đều đặn giúp dập tắt các tin đồn thất thiệt, giúp nhân viên thấy dự án đang tiến triển tốt và chuẩn bị tinh thần tham gia đào tạo.",
        "Proactive status communication eliminates the vacuum where toxic rumors thrive, framing the impending go-live as a shared organizational accomplishment.",
        "Kostojohn et al. (2011)", "Chapter 2 & 5", "pp. 42-45, 140-143", ["internal-communications", "change-readiness"]
    ),
    (
        "q-05-19", "Dependency Identification", "hard", "single_choice",
        "Trong lập kế hoạch tiến độ CRM, mối quan hệ phụ thuộc 'Bắt đầu - để - Bắt đầu' (Start-to-Start - SS) có nghĩa là gì?",
        "In CRM project schedule logic, what does a 'Start-to-Start' (SS) task dependency specify?",
        {
            "A": ("Công việc B chỉ có thể bắt đầu sau khi Công việc A đã hoàn thành 100%.", "Task B cannot commence until Task A has reached 100% completion."),
            "B": ("Công việc B có thể bắt đầu đồng thời ngay khi Công việc A bắt đầu (có thể kèm theo độ trễ / lag time), ví dụ: Bắt đầu viết kịch bản kiểm thử ngay khi bắt đầu giai đoạn cấu hình quy trình.", "Task B can begin in parallel as soon as Task A commences (potentially with lead/lag offsets), such as drafting test scripts concurrently alongside workflow configuration."),
            "C": ("Cả hai công việc đều bị hủy bỏ vĩnh viễn.", "Both activities are permanently terminated simultaneously."),
            "D": ("Công việc B phải kết thúc trước khi Công việc A được phép bắt đầu.", "Task B must reach completion before Task A is allowed to initiate.")
        },
        "B",
        "Quan hệ Start-to-Start cho phép tiến hành song song các luồng công việc để rút ngắn tổng thời gian dự án (fast-tracking).",
        "Start-to-Start dependencies facilitate fast-tracking, allowing downstream teams to begin preliminary drafting without waiting for full upstream finalization.",
        "Kostojohn et al. (2011)", "Chapter 5", "pp. 129-133", ["task-dependencies", "schedule-logic", "fast-tracking"]
    ),
    (
        "q-05-20", "Pilot Success Criteria", "medium", "single_choice",
        "Trước khi quyết định mở rộng hệ thống CRM ra toàn bộ doanh nghiệp sau giai đoạn Pilot, tiêu chí nào sau đây phải được đáp ứng?",
        "Before expanding a CRM deployment enterprise-wide following a pilot phase, which milestone criteria must be satisfied?",
        {
            "A": ("Nhà cung cấp phần mềm phải hạ giá bản quyền xuống 0 đồng.", "The software vendor must reduce ongoing subscription fees to zero dollars."),
            "B": ("Đạt các chỉ số chấp nhận của người dùng (User Adoption Rate > 85%), tỷ lệ lỗi nghiêm trọng trong vận hành bằng 0, và quy trình xử lý công việc thực tế được xác nhận là trơn tru.", "Meeting defined adoption thresholds (e.g., active user logins > 85%), zero unresolved severity-1 blockers, and qualitative sign-off confirming smooth daily execution."),
            "C": ("Tất cả nhân viên tham gia pilot đều xin chuyển sang công ty khác làm việc.", "All participating pilot reps requesting transfers to outside corporations."),
            "D": ("Doanh số toàn cầu của công ty phải tăng gấp 10 lần trong 2 tuần thử nghiệm.", "Global enterprise revenues surging tenfold within two pilot weeks.")
        },
        "B",
        "Giai đoạn pilot là bài kiểm tra thực tế; chỉ khi đơn vị thí điểm chứng minh được sự ổn định và người dùng tích cực sử dụng thì mới nên triển khai diện rộng.",
        "Exit criteria for a successful pilot require quantitative adoption metrics and qualitative workflow validation before rolling out enterprise-wide changes.",
        "Kostojohn et al. (2011)", "Chapter 5 & 6", "pp. 148-152, 175-179", ["pilot-criteria", "gate-review", "rollout"]
    )
]

for item in e5:
    questions_batch2.append(make_q(
        item[0], "EXAM-05", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

# ==========================================
# EXAM 06: CRM EXECUTION, TESTING & SYSTEM LAUNCH (q-06-01 to q-06-20)
# ==========================================
e6 = [
    (
        "q-06-01", "Testing Hierarchy", "easy", "single_choice",
        "Trật tự chuẩn mực của các giai đoạn kiểm thử phần mềm trong dự án triển khai CRM là:",
        "What is the standard chronological sequence of software testing phases during CRM implementation?",
        {
            "A": ("Kiểm thử Chấp nhận Người dùng (UAT) -> Kiểm thử Đơn vị (Unit Test) -> Kiểm thử Hệ thống (System Test).", "User Acceptance Testing (UAT) -> Unit Testing -> System Testing."),
            "B": ("Kiểm thử Đơn vị (Unit Testing) -> Kiểm thử Tích hợp (Integration Testing) -> Kiểm thử Hệ thống (System Testing) -> Kiểm thử Chấp nhận của Người dùng (User Acceptance Testing - UAT).", "Unit Testing -> Integration Testing -> System Testing -> User Acceptance Testing (UAT)."),
            "C": ("Chỉ cần đưa lên môi trường thật và để khách hàng tự kiểm thử.", "Directly releasing to live production and relying on external customers to report bugs."),
            "D": ("Kiểm thử Tải (Load Test) -> Khai tử hệ thống -> Kiểm thử Giao diện.", "Load Testing -> System Sunsetting -> UI Testing.")
        },
        "B",
        "Kiểm thử đi từ mức độ vi mô (từng hàm, từng trường dữ liệu) đến liên kết giữa các hệ thống, toàn bộ luồng nghiệp vụ và cuối cùng là người dùng cuối xác nhận.",
        "Testing progresses systematically from granular component logic (unit) to multi-system data flows (integration), end-to-end performance (system), and user sign-off (UAT).",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 160-166", ["testing-hierarchy", "qa", "uat"]
    ),
    (
        "q-06-02", "User Acceptance Testing (UAT)", "medium", "single_choice",
        "Mục đích tối hậu của Kiểm thử Chấp nhận Người dùng (UAT) trong dự án CRM là gì?",
        "What is the ultimate objective of User Acceptance Testing (UAT) in a CRM deployment?",
        {
            "A": ("Để các lập trình viên tự kiểm tra xem code của mình viết có đẹp không.", "Permitting software engineers to verify the aesthetic elegance of their source code."),
            "B": ("Để người dùng nghiệp vụ thực tế xác nhận rằng hệ thống đáp ứng đầy đủ và chính xác các quy trình công việc hàng ngày của họ trước khi ký biên bản nghiệm thu.", "Empowering actual business end-users to validate that the configured system faithfully supports their daily operational workflows prior to formal go-live sign-off."),
            "C": ("Để tìm lý do từ chối thanh toán tiền điện cho văn phòng.", "Finding a legal rationale to default on commercial office electric utilities."),
            "D": ("Để đếm xem giao diện có bao nhiêu hình ảnh minh họa.", "Counting the total number of graphic icons rendered on desktop interface views.")
        },
        "B",
        "UAT là chốt chặn quan trọng nhất của phía nghiệp vụ; nếu người dùng không tham gia UAT, họ sẽ từ chối sử dụng hệ thống khi vận hành chính thức.",
        "UAT establishes formal business ownership; business champions validate that real work can be executed efficiently before formal production cutover.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 165-170", ["uat", "business-validation", "sign-off"]
    ),
    (
        "q-06-03", "Test Scripts Quality", "hard", "single_choice",
        "Một Kịch bản Kiểm thử UAT (UAT Test Script) đạt chuẩn chất lượng cao cần phải thể hiện:",
        "A rigorous, high-quality UAT Test Script must specify which set of elements?",
        {
            "A": ("Một câu ngắn gọn: 'Hãy dùng thử phần mềm và báo lại nếu thấy chán'.", "A single vague prompt: 'Try using the software and let us know if you find it dull.'"),
            "B": ("Mã kịch bản, Quy trình nghiệp vụ kiểm tra, Dữ liệu đầu vào cụ thể, Các bước thực hiện chi tiết từng bước, Kết quả mong đợi (Expected Result), và Cột ghi nhận Kết quả thực tế (Pass/Fail kèm bằng chứng ảnh chụp).", "Script ID, Business scenario, Prerequisites, Specific test inputs, Step-by-step action instructions, Expected Result, and Actual Result (Pass/Fail with screenshot logs)."),
            "C": ("Số trang in của tài liệu hướng dẫn sử dụng phần mềm.", "The total page count of the vendor's generic user manual."),
            "D": ("Danh sách các bài hát mà nhân viên kiểm thử ưa thích.", "A curated playlist of songs preferred by quality assurance testers.")
        },
        "B",
        "Kịch bản kiểm thử rõ ràng giúp người dùng biết chính xác cần thao tác gì và giúp nhóm kỹ thuật tái hiện (reproduce) được lỗi ngay lập tức khi có sự cố.",
        "Granular scripts provide unambiguous reproducibility for bugs, ensuring that defects are documented against explicit acceptance criteria rather than subjective whims.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 166-171", ["test-scripts", "uat", "defect-tracking"]
    ),
    (
        "q-06-04", "Data Cutover Window", "medium", "single_choice",
        "Cửa sổ Cắt chuyển Dữ liệu (Cutover Window) khi đưa CRM vào vận hành trực tiếp thường được lên lịch vào thời điểm nào?",
        "When is an enterprise CRM Go-Live Cutover Window typically scheduled to take place?",
        {
            "A": ("Vào sáng thứ Hai lúc 9 giờ sáng khi toàn bộ nhân viên đang bắt đầu giao dịch với khách hàng.", "On Monday morning at 9:00 AM when all sales representatives are actively engaging clients."),
            "B": ("Vào cuối tuần hoặc các kỳ nghỉ lễ dài ngày, khi khối lượng giao dịch kinh doanh ở mức thấp nhất, tạo đủ thời gian để nạp dữ liệu cuối cùng và kiểm tra trước khi mở cửa sáng thứ Hai.", "Over a weekend or extended public holiday window when transaction volumes are dormant, providing sufficient runway for delta data migration and verification."),
            "C": ("Vào giờ ăn trưa các ngày trong tuần (từ 12h00 đến 12h30).", "During standard weekday lunch hours (between 12:00 PM and 12:30 PM)."),
            "D": ("Ngẫu nhiên bất kỳ lúc nào mà không cần thông báo trước cho các phòng ban.", "Randomly at any unannounced moment without informing operational staff.")
        },
        "B",
        "Cắt chuyển cuối tuần giúp đội ngũ kỹ thuật có 48-72 giờ để hoàn thành nạp dữ liệu bổ sung (Delta sync), chạy kiểm thử xác nhận (Sanity checks) và xử lý sự cố mà không làm gián đoạn việc bán hàng.",
        "Weekend cutovers isolate operational disruption, providing a buffer window to perform final delta loads, execute sanity tests, and resolve migration edge cases.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 170-176", ["cutover-window", "go-live", "delta-migration"]
    ),
    (
        "q-06-05", "Go/No-Go Decision Gate", "hard", "single_choice",
        "Cuộc họp 'Quyết định Tiến hành hay Dừng lại' (Go/No-Go Decision Gate) trước thời điểm triển khai chính thức CRM phải dựa trên tiêu chí cốt lõi nào?",
        "On what foundational governance criteria must the executive Go/No-Go Decision Gate meeting be adjudicated prior to production cutover?",
        {
            "A": ("Dựa trên cảm xúc ngẫu nhiên của người điều hành cuộc họp.", "The subjective emotional mood of the meeting facilitator."),
            "B": ("Đánh giá nghiêm ngặt bảng kiểm tiêu chí: Không còn lỗi nghiêm trọng cấp độ 1 (Severity 1 / Showstopper bugs), kết quả UAT được ký duyệt 100%, dữ liệu đã sẵn sàng, và kế hoạch hỗ trợ trực tiếp (Hypercare) đã được bố trí.", "Objective audit of launch criteria: Zero open Severity-1 / blocker defects, signed UAT acceptance certificates, verified clean migration delta, and active hypercare readiness."),
            "C": ("Nếu hôm đó trời mưa thì quyết định dừng lại; nếu trời nắng thì tiến hành.", "Halting if it rains on cutover day; proceeding if sky conditions are clear."),
            "D": ("Chỉ cần nhà cung cấp phần mềm cam kết gửi quà tặng cho ban lãnh đạo.", "Solely requiring the software vendor to promise luxury gift baskets to executives.")
        },
        "B",
        "Nếu vẫn còn lỗi nghiêm trọng làm gián đoạn quy trình kinh doanh (Blocker bugs) mà vẫn cố tình 'Go', hệ thống sẽ sụp đổ và gây thiệt hại nặng nề cho hoạt động của công ty.",
        "A disciplined Go/No-Go gate prevents premature launches; deploying with open Severity-1 defects destroys organizational credibility and paralyzes revenue operations.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 172-176", ["go-no-go", "gate-review", "launch-readiness"]
    ),
    (
        "q-06-06", "Hypercare Period", "medium", "single_choice",
        "Giai đoạn 'Hỗ trợ Tăng cường' (Hypercare Period) ngay sau khi hệ thống CRM Golive thường kéo dài bao lâu và có nhiệm vụ gì?",
        "How long does the post-go-live 'Hypercare Period' typically last, and what is its operational purpose?",
        {
            "A": ("Kéo dài đúng 15 phút rồi rút toàn bộ đội ngũ kỹ thuật về.", "Exactly fifteen minutes, followed by the immediate withdrawal of all engineering staff."),
            "B": ("Kéo dài từ 2 đến 6 tuần, trong đó đội dự án và nhà tư vấn túc trực hỗ trợ người dùng tại chỗ, xử lý sự cố phát sinh ưu tiên cao và ổn định hóa quy trình vận hành.", "Lasting 2 to 6 weeks, during which project teams and consultants provide high-touch, on-the-ground floor support, rapid bug triaging, and stabilization coaching."),
            "C": ("Kéo dài 10 năm liên tục.", "Ten continuous calendar years."),
            "D": ("Là giai đoạn nhân viên được nghỉ phép hưởng nguyên lương ở nhà.", "A vacation period where all corporate employees stay home on full pay.")
        },
        "B",
        "Trong những tuần đầu tiên, người dùng rất dễ bỡ ngỡ và hoang mang; sự có mặt trực tiếp của đội ngũ hỗ trợ giúp giải tỏa lo âu và ngăn chặn việc bỏ rơi hệ thống.",
        "Hypercare provides immediate psychological safety and tactical floor support, ensuring minor teething frustrations do not metastasize into widespread system rejection.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 176-180", ["hypercare", "post-go-live", "floor-support"]
    ),
    (
        "q-06-07", "Defect Severity Classification", "hard", "single_choice",
        "Trong quản lý lỗi kiểm thử CRM, lỗi thuộc 'Cấp độ 1' (Severity 1 / Blocker / Critical) được định nghĩa chuẩn xác là:",
        "In CRM software quality assurance, how is a 'Severity 1' (Critical / Blocker) defect rigorously defined?",
        {
            "A": ("Lỗi chính tả nhỏ trên trang trợ giúp không ảnh hưởng đến việc nhập liệu.", "A minor typographical error inside an auxiliary help page that does not affect data entry."),
            "B": ("Lỗi nghiêm trọng làm sập hệ thống (System Crash), mất dữ liệu hoặc làm tắc nghẽn hoàn toàn một quy trình kinh doanh cốt lõi (như không thể tạo đơn hàng hoặc không thể lưu thông tin khách hàng) mà không có giải pháp tạm thời (no workaround).", "A catastrophic flaw causing complete system crashes, data corruption, or total blockage of a critical business path (e.g., cannot book orders, cannot save customer accounts) with zero workaround."),
            "C": ("Màu sắc của một nút bấm trên màn hình hơi nhạt hơn so với thiết kế.", "A screen command button hue rendering slightly paler than the graphic design spec."),
            "D": ("Biểu tượng logo của công ty nằm lệch sang phải 2 milimet.", "The company header logo icon sitting offset two millimeters to the right.")
        },
        "B",
        "Lỗi Severity 1 phải được coi là tình trạng khẩn cấp và bắt buộc phải khắc phục xong trước khi hệ thống được phép phát hành trực tiếp ra môi trường sản xuất.",
        "Severity 1 defects represent catastrophic stop-ship emergencies; releasing software with active Sev-1 issues paralyzes live operational capability.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 167-171", ["defect-severity", "severity-1", "quality-assurance"]
    ),
    (
        "q-06-08", "Regression Testing", "medium", "single_choice",
        "Hoạt động 'Kiểm thử Hồi quy' (Regression Testing) trong các đợt cập nhật hoặc sửa lỗi CRM nhằm đảm bảo điều gì?",
        "What is the explicit purpose of conducting 'Regression Testing' following CRM defect fixes or software updates?",
        {
            "A": ("Đảm bảo máy tính của công ty không bị giảm dung lượng RAM.", "Ensuring corporate office workstations do not lose physical RAM capacity."),
            "B": ("Đảm bảo rằng các đoạn mã mới được sửa hoặc tính năng mới thêm vào không vô tình làm hỏng các chức năng cũ đang hoạt động ổn định của hệ thống.", "Verifying that newly introduced bug fixes, configurations, or enhancements have not unintentionally broken existing, previously verified system workflows."),
            "C": ("Kiểm tra xem nhân viên có nhớ mật khẩu đăng nhập cũ hay không.", "Testing whether employees recall their legacy expired login passwords."),
            "D": ("Xóa sạch tất cả các bản sao lưu dự phòng cũ trong quá khứ.", "Purging all historical database backups stored in cold storage archives.")
        },
        "B",
        "Kiểm thử hồi quy ngăn chặn hiện tượng 'sửa được một lỗi ở chỗ này nhưng lại làm nảy sinh ba lỗi mới ở chỗ khác'.",
        "Regression testing guards against unintended side effects, validating that the interconnected platform logic remains pristine after software codebase modifications.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 164-168", ["regression-testing", "software-quality", "defect-fixes"]
    ),
    (
        "q-06-09", "Performance & Load Testing", "medium", "single_choice",
        "Kiểm thử Tải và Hiệu năng (Load & Stress Testing) trước ngày Golive của CRM nhằm trả lời câu hỏi nào?",
        "What critical operational question does pre-launch Load and Stress Testing answer for enterprise CRM systems?",
        {
            "A": ("Liệu văn phòng có đủ ghế ngồi cho toàn bộ nhân viên hay không?", "Whether corporate conference rooms contain enough chairs for all employees?"),
            "B": ("Hệ thống có duy trì được thời gian phản hồi nhanh và tính ổn định khi hàng nghìn người dùng đồng thời truy cập và thực hiện giao dịch trong các đợt cao điểm bán hàng hay không?", "Can the application infrastructure maintain acceptable response times and stability when subjected to concurrent peak user traffic and heavy query volume?"),
            "C": ("Nhân viên có thể gõ bàn phím nhanh bao nhiêu từ trong một phút?", "How many alphanumeric words per minute can frontline staff type on keyboards?"),
            "D": ("Hệ điều hành của máy chủ có cần cài thêm phần mềm diệt virus miễn phí hay không?", "Whether the server operating system requires third-party freeware utilities?")
        },
        "B",
        "Kiểm thử tải mô phỏng lượng người dùng cao điểm thực tế để phát hiện sớm các điểm nghẽn cổ chai (bottlenecks) về bộ nhớ máy chủ, băng thông mạng hoặc khóa bảng cơ sở dữ liệu.",
        "Stress testing pushes cloud infrastructure to peak projected thresholds, unmasking database deadlock conditions and memory bottlenecks prior to real-world traffic.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 162-166", ["load-testing", "stress-testing", "performance"]
    ),
    (
        "q-06-10", "End-User Onboarding Job Aids", "easy", "single_choice",
        "Để hỗ trợ người dùng thao tác chính xác trên CRM trong những ngày đầu Golive, công cụ hỗ trợ nào sau đây mang lại hiệu quả cao nhất?",
        "To assist frontline personnel in navigating CRM workflows during early go-live days, which job aid provides the greatest tactical efficacy?",
        {
            "A": ("Gửi một tệp PDF lý thuyết dày 800 trang cho nhân viên tự tra cứu.", "Mailing an 800-page dense theoretical textbook PDF for self-directed study."),
            "B": ("Các bản tóm tắt quy trình thao tác nhanh (Quick Reference Cards / Cheat Sheets dài 1-2 trang), kẹp trực tiếp cạnh màn hình hoặc video hướng dẫn ngắn 2 phút cho từng nghiệp vụ cụ thể.", "Laminated 1-2 page Quick Reference Cards (Cheat Sheets) posted at workstations and bite-sized 2-minute video clips walking through specific discrete tasks."),
            "C": ("Cử người đứng sau lưng nhắc nhở và quát mắng nhân viên mỗi khi họ thao tác chậm.", "Stationing monitors behind staff to scold them whenever navigation pauses."),
            "D": ("Tắt toàn bộ hệ thống để nhân viên quay lại viết giấy tay.", "Deactivating the CRM software to let staff revert to handwritten notepads.")
        },
        "B",
        "Nhân viên bận rộn không có thời gian đọc sách hướng dẫn dài dòng; tài liệu 'mì ăn liền' 1 trang tóm tắt các bước bấm nút thực tế giúp họ làm được việc ngay.",
        "Frontline staff require instant, contextual guidance; laminated job aids and concise task videos resolve operational confusion immediately at the point of action.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 177-182", ["job-aids", "quick-reference", "user-enablement"]
    ),
    (
        "q-06-11", "Delta Data Sync Logic", "hard", "single_choice",
        "Trong đợt cắt chuyển dữ liệu Golive, 'Đồng bộ Dữ liệu Chênh lệch' (Delta Synchronization) là gì?",
        "During live cutover execution, what does 'Delta Synchronization' accomplish?",
        {
            "A": ("Xóa toàn bộ các chữ cái Hy Lạp trong cơ sở dữ liệu.", "Purging all Greek mathematical symbols stored within database text fields."),
            "B": ("Sau khi đã nạp trước khối lượng lớn dữ liệu lịch sử vào cuối tuần, tiến trình này chỉ trích xuất và nạp bổ sung những bản ghi được tạo mới hoặc chỉnh sửa trong hệ thống cũ trong khoảng thời gian từ lúc sao lưu đến lúc cắt chuyển chính thức.", "After pre-loading massive historical archives, this process extracts and migrates only the incremental records created or updated in legacy systems during the cutover window."),
            "C": ("Tự động làm tròn số tiền trên hóa đơn của khách hàng.", "Automatically rounding all invoice monetary amounts up to the nearest integer."),
            "D": ("Thay thế toàn bộ tên của khách hàng bằng các mã số ngẫu nhiên.", "Overwriting all customer proper names with randomized alphanumeric serials.")
        },
        "B",
        "Delta Sync giúp rút ngắn thời gian dừng hệ thống (downtime); thay vì nạp lại từ đầu 10 triệu bản ghi (mất nhiều ngày), hệ thống chỉ cần nạp vài nghìn bản ghi mới phát sinh.",
        "Delta loading compresses deployment downtime windows by migrating solely records altered since the primary baseline snapshot was taken.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 171-175", ["delta-sync", "data-migration", "cutover-strategy"]
    ),
    (
        "q-06-12", "Sanity Testing Post Go-Live", "medium", "single_choice",
        "Kiểm tra 'Sanity' (Sanity Check / Smoke Test) ngay sau khi hoàn tất nạp dữ liệu trên môi trường thật (Production) bao gồm các thao tác nào?",
        "What constitutes a 'Smoke / Sanity Test' executed immediately following production deployment cutover?",
        {
            "A": ("Đốt một nén hương trong phòng máy chủ để cầu may mắn.", "Lighting incense inside the physical server room to solicit good fortune."),
            "B": ("Thực hiện thử một số giao dịch mẫu tối thiểu mang tính đại diện (tạo một khách hàng mới, chuyển đổi một đầu mối, xuất một báo cáo) để đảm bảo các chức năng sống còn hoạt động bình thường trước khi mở quyền truy cập cho toàn thể nhân viên.", "Executing a minimal suite of end-to-end baseline transactions (creating an account, converting a lead, generating a core report) to confirm platform health before granting access."),
            "C": ("Gửi email cho tất cả các khách hàng thông báo công ty sắp đổi tên.", "Emailing all corporate accounts announcing an impending corporate rebranding."),
            "D": ("Kiểm tra nhiệt độ của điều hòa không khí trong văn phòng.", "Measuring the ambient temperature of office room air conditioning units.")
        },
        "B",
        "Smoke test nhanh chóng xác nhận hệ thống thật đã thông suốt và sẵn sàng; nếu một chức năng cơ bản bị lỗi, quản trị viên có thể kịp thời sửa chữa trước giờ nhân viên vào làm.",
        "Smoke tests verify that the production build is fundamentally stable and functional before exposing the software to thousands of active end-users.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 172-176", ["smoke-test", "sanity-check", "production-readiness"]
    ),
    (
        "q-06-13", "User Feedback Loop", "medium", "single_choice",
        "Trong tuần đầu tiên Golive, kênh tiếp nhận phản hồi của người dùng nên được thiết lập như thế nào để tránh quá tải cho phòng IT?",
        "During early go-live, how should user feedback channels be structured to prevent overwhelming the IT support desk?",
        {
            "A": ("Khóa hoàn toàn hòm thư góp ý và cấm nhân viên phàn nàn.", "Locking all internal feedback inboxes and penalizing staff for submitting inquiries."),
            "B": ("Thiết lập cơ chế lọc qua Đại sứ phòng ban (Super Users) làm tuyến hỗ trợ cấp 1 (Tier 1 Support) để giải quyết các thắc mắc thao tác cơ bản, chỉ chuyển lên đội kỹ thuật các lỗi phần mềm thực sự.", "Routing questions through designated Departmental Champions as Tier-1 floor support to resolve basic operational queries, escalating only true software bugs to technical teams."),
            "C": ("Bắt buộc mọi câu hỏi phải được viết thành văn bản tay gửi qua đường bưu điện.", "Requiring all system queries to be handwritten on paper and submitted via postal mail."),
            "D": ("Tự động trả lời tự động tất cả các yêu cầu bằng thông điệp: 'Hệ thống hoàn hảo, không có lỗi'.", "Configuring an automated responder stating: 'The platform is perfect; no bugs exist.'")
        },
        "B",
        "Super Users đóng vai trò là 'bộ giảm xóc'; 80% câu hỏi ban đầu là do người dùng chưa quen thao tác chứ không phải lỗi phần mềm. Lọc qua Super Users giúp nhóm IT tập trung sửa lỗi kỹ thuật.",
        "Tier-1 triage by Super Users absorbs the tsunami of routine navigation queries, shielding core IT engineers so they can remediate genuine systemic defects.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 178-183", ["user-feedback", "tier-1-support", "super-users"]
    ),
    (
        "q-06-14", "Rollout Blackout Period", "hard", "single_choice",
        "Khái niệm 'Giai đoạn Đóng băng Thay đổi' (Code Freeze / Blackout Period) trước ngày Golive CRM có ý nghĩa gì?",
        "What does a 'Code Freeze / Change Blackout Period' mandate immediately prior to enterprise CRM go-live?",
        {
            "A": ("Tắt điều hòa phòng làm việc để hạ nhiệt độ xuống mức đóng băng.", "Lowering office thermostat settings to freezing temperatures."),
            "B": ("Nghiêm cấm tuyệt đối việc bổ sung tính năng mới hoặc chỉnh sửa cấu trúc mã nguồn/cơ sở dữ liệu trong khoảng thời gian sát ngày triển khai, chỉ tập trung vào kiểm thử và ổn định môi trường.", "Strictly prohibiting any new feature enhancements, code merges, or schema alterations immediately prior to launch, dedicating the baseline purely to final stabilization and regression verification."),
            "C": ("Cấm nhân viên không được uống cà phê trong văn phòng.", "Forbidding employees from consuming coffee within the corporate office."),
            "D": ("Xóa sạch tất cả các tài liệu dự án để bảo mật thông tin.", "Shredding all project documentation to enforce operational secrecy.")
        },
        "B",
        "Code freeze đảm bảo môi trường kiểm thử và môi trường triển khai thực tế hoàn toàn đồng nhất; việc thêm nếm tính năng vào phút chót là nguyên nhân hàng đầu gây sập hệ thống khi Golive.",
        "A code freeze stabilizes the target environment, preventing last-minute developer tampering that introduces untested regressions hours before production cutover.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 168-173", ["code-freeze", "change-freeze", "deployment-stability"]
    ),
    (
        "q-06-15", "Adoption Tracking Metrics", "medium", "single_choice",
        "Trong 30 ngày đầu tiên sau Golive, ban lãnh đạo nên theo dõi chỉ số đo lường mức độ tiếp nhận (Adoption Metric) nào sau đây?",
        "During the first 30 days post-launch, which User Adoption metric provides the most actionable insight into daily employee engagement?",
        {
            "A": ("Số lượng khách hàng đã qua đời trong tháng.", "The number of enterprise customer accounts registered as deceased."),
            "B": ("Tỷ lệ đăng nhập hàng ngày (Daily Active Users - DAU), số lượng bản ghi mới/cập nhật được tạo bởi từng phòng ban, và tỷ lệ các trường dữ liệu bắt buộc được điền đầy đủ.", "Daily Active Users (DAU) percentage, volume of new/updated records logged per department, and completeness ratio of mandatory master data fields."),
            "C": ("Số lượng bánh quy nhân viên đã tiêu thụ trong giờ giải lao.", "The gross count of bakery cookies consumed during employee office tea breaks."),
            "D": ("Độ sáng màn hình máy tính trung bình của toàn công ty.", "The average display brightness setting across corporate desktop monitors.")
        },
        "B",
        "Đo lường DAU và khối lượng giao dịch thực tế trên CRM giúp phát hiện ngay chi nhánh hoặc bộ phận nào đang có biểu hiện trốn tránh sử dụng để kịp thời can thiệp.",
        "Tracking DAU, interaction logging, and data completeness highlights which regional offices are lagging in adoption, allowing swift remedial coaching.",
        "Kostojohn et al. (2011)", "Chapter 6 & 7", "pp. 182-186, 210-215", ["adoption-metrics", "dau", "user-engagement"]
    ),
    (
        "q-06-16", "Post-Implementation Review", "medium", "single_choice",
        "Cuộc họp Đánh giá Sau Triển khai (Post-Implementation Review / Retrospective) nhằm mục đích gì?",
        "What is the formal purpose of conducting a CRM Post-Implementation Review (Retrospective)?",
        {
            "A": ("Tìm ra một cá nhân để đổ lỗi và sa thải công khai.", "Identifying a single individual to publicly blame and terminate."),
            "B": ("Đánh giá khách quan những gì đã làm tốt, những điểm còn thiếu sót, đo lường kết quả thực tế so với mục tiêu ban đầu, và đúc kết các bài học kinh nghiệm (Lessons Learned) cho các giai đoạn sau.", "Objectively evaluating successes, identifying friction points, comparing real outcomes against the original business case, and codifying Lessons Learned for future iterations."),
            "C": ("Yêu cầu nhà cung cấp phải hoàn trả 100% tiền mua phần mềm.", "Demanding that the software vendor issue an unconditional 100% contract refund."),
            "D": ("Xóa bỏ toàn bộ các biên bản cuộc họp trong quá khứ.", "Burning all historical paper minutes recorded during executive meetings.")
        },
        "B",
        "Đánh giá sau triển khai giúp tổ chức học hỏi từ những sai lầm thực tế (như ước tính sai thời gian làm sạch dữ liệu) để tối ưu hóa việc quản lý các dự án tiếp theo.",
        "A blameless post-mortem captures invaluable institutional knowledge, ensuring future release cycles avoid identical operational and architectural pitfalls.",
        "Kostojohn et al. (2011)", "Chapter 7", "pp. 205-212", ["post-implementation-review", "lessons-learned", "continuous-learning"]
    ),
    (
        "q-06-17", "User Account Provisioning", "easy", "single_choice",
        "Quy trình cấp phát tài khoản người dùng (User Account Provisioning) trong lễ ra mắt CRM cần đảm bảo:",
        "What must the User Account Provisioning workflow ensure on the day of CRM platform launch?",
        {
            "A": ("Tất cả tài khoản đều sử dụng chung một tên đăng nhập và mật khẩu là '123456'.", "All corporate users share a single identical username and password '123456'."),
            "B": ("Mỗi người dùng được cấp một tài khoản định danh duy nhất gắn với đúng quyền hạn vai trò (Role/Profile), được kích hoạt đồng bộ và gửi thông tin hướng dẫn đăng nhập an toàn.", "Every user receives a unique authenticated credential mapped to their designated role/profile, activated in sync, with secure first-time login guidance."),
            "C": ("Chỉ cấp tài khoản cho nhân viên nam, nhân viên nữ không được dùng.", "Granting accounts exclusively to male employees while barring female staff."),
            "D": ("Bắt buộc người dùng phải trả phí bằng tiền mặt mới được mở tài khoản.", "Requiring staff to pay cash fees at the reception desk to activate logins.")
        },
        "B",
        "Tài khoản định danh riêng biệt đảm bảo tính giải trình (accountability), lưu vết lịch sử thao tác (audit trail) và tuân thủ các quy định bảo mật thông tin doanh nghiệp.",
        "Individual credentials enforce role-based segregation, maintain immutable audit logging, and safeguard enterprise data security integrity.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 169-173", ["user-provisioning", "accountability", "security-compliance"]
    ),
    (
        "q-06-18", "Go-Live Celebration & Recognition", "easy", "single_choice",
        "Tại sao việc công nhận và khen thưởng đội ngũ dự án trong ngày Golive lại có ý nghĩa văn hóa quan trọng?",
        "Why is executive recognition and celebration of the deployment team at Go-Live strategically important?",
        {
            "A": ("Vì công việc của toàn bộ dự án CRM đã vĩnh viễn kết thúc và không còn việc gì cần làm nữa.", "Because all CRM project tasks are now permanently concluded forever."),
            "B": ("Ghi nhận những nỗ lực phi thường của đội ngũ kỹ thuật và người dùng nòng cốt, tạo niềm tự hào chung của tổ chức và tiếp thêm năng lượng cho giai đoạn vận hành lâu dài.", "Validating the intense effort of the core implementation team, fostering shared institutional pride, and rejuvenating collective energy for long-term operational success."),
            "C": ("Để hợp thức hóa việc chi tiêu quỹ phúc lợi của công đoàn.", "To balance residual funds inside the trade union discretionary account."),
            "D": ("Để nhà báo bên ngoài đến chụp ảnh quảng cáo.", "To solicit local newspaper journalists to snap promotional publicity photos.")
        },
        "B",
        "Triển khai CRM là một chặng đường đầy áp lực; sự công nhận kịp thời của ban lãnh đạo giúp củng cố tinh thần đoàn kết và khẳng định cam kết lâu dài với dự án.",
        "Recognizing team dedication transforms a taxing software rollout into a shared cultural victory, cementing cross-functional bonds for ongoing system evolution.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 180-184", ["celebration", "executive-recognition", "morale"]
    ),
    (
        "q-06-19", "Triage Meeting Rhythm", "medium", "single_choice",
        "Trong tuần đầu tiên của giai đoạn Hypercare, các cuộc họp phân loại lỗi hàng ngày (Daily Bug Triage Meetings) có chức năng gì?",
        "During the first week of Hypercare, what is the core operational function of Daily Bug Triage Meetings?",
        {
            "A": ("Bình chọn xem nhân viên nào đi làm muộn nhất để phạt tiền.", "Voting on which team member arrived latest to impose financial penalties."),
            "B": ("Rà soát toàn bộ các sự cố và phản ánh mới phát sinh trong ngày, xác định mức độ nghiêm trọng (Severity), gán mức độ ưu tiên xử lý (Priority), và phân công kỹ sư khắc phục nhanh chóng.", "Reviewing all incoming defect tickets logged during the day, validating severity ratings, establishing remediation priority, and assigning developers for rapid turnaround."),
            "C": ("Thuyết trình lại từ đầu toàn bộ các tính năng của phần mềm.", "Re-delivering the introductory software features slide deck from scratch."),
            "D": ("Đọc to các bức thư khen ngợi của khách hàng trên mạng xã hội.", "Reading customer social media praise letters aloud over desktop speakers.")
        },
        "B",
        "Triage meeting giữ nhịp độ xử lý sự cố nhanh chóng, ngăn ngừa tình trạng tồn đọng lỗi khiến người dùng mất lòng tin vào hệ thống mới.",
        "Daily triage prevents defect logjams, aligning technical capacity against the most urgent frontline workflow blockers with disciplined urgency.",
        "Kostojohn et al. (2011)", "Chapter 6", "pp. 177-181", ["bug-triage", "defect-management", "hypercare"]
    ),
    (
        "q-06-20", "Transition to Support Team", "medium", "single_choice",
        "Khi kết thúc giai đoạn Hypercare, việc bàn giao hệ thống từ Nhóm Dự án (Project Team) sang Nhóm Hỗ trợ Vận hành Thường trực (BAU / IT Support Team) đòi hỏi điều kiện nào?",
        "At the conclusion of Hypercare, what is required to execute a formal transition from the Project Team to Business-As-Usual (BAU) Operations?",
        {
            "A": ("Nhóm dự án xóa sạch toàn bộ mã nguồn của hệ thống trước khi rời đi.", "The project team destroying all source code repositories before departing."),
            "B": ("Hoàn tất tài liệu kiến trúc kỹ thuật và hướng dẫn vận hành, chuyển giao kho tri thức về các lỗi đã biết (Known Errors), và nhóm BAU chính thức ký biên bản tiếp nhận trách nhiệm.", "Complete technical architecture documentation, knowledge transfer on known workarounds, and formal sign-off by operational support leaders accepting system custody."),
            "C": ("Tất cả các thành viên trong nhóm hỗ trợ phải thi đỗ bằng lái xe ô tô.", "Every member of the permanent IT support desk passing a commercial driver's license exam."),
            "D": ("Ngừng hoàn toàn việc sửa lỗi phần mềm trong tương lai.", "Permanently ceasing all future software defect patching activities.")
        },
        "B",
        "Bàn giao sang BAU (Business As Usual) chuẩn mực đảm bảo hệ thống tiếp tục được vận hành, giám sát và bảo trì ổn định lâu dài sau khi các chuyên gia tư vấn rút lui.",
        "A structured handover equips permanent BAU teams with the architectural documentation and troubleshooting runbooks required to maintain platform health autonomously.",
        "Kostojohn et al. (2011)", "Chapter 6 & 7", "pp. 182-186, 215-220", ["bau-transition", "knowledge-transfer", "operational-support"]
    )
]

for item in e6:
    questions_batch2.append(make_q(
        item[0], "EXAM-06", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

print(f"Total questions generated in batch 2: {len(questions_batch2)}")

with open(Path(r"C:\Kiến thức cần học\CRM\output\scratch\q_batch2.json"), "w", encoding="utf-8") as f:
    json.dump(questions_batch2, f, ensure_ascii=False, indent=2)
