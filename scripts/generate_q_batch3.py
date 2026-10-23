import json
from pathlib import Path

# Exam 07 and 08 question generator
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

questions_batch3 = []

# ==========================================
# EXAM 07: SATISFACTION, LOYALTY & RETENTION ECONOMICS (q-07-01 to q-07-20)
# ==========================================
e7 = [
    (
        "q-07-01", "Expectation-Confirmation Theory", "medium", "single_choice",
        "Theo Thuyết Xác nhận Kỳ vọng (Oliver's Expectation-Confirmation Theory) được trình bày trong Baran & Galka, sự không xác nhận tích cực (Positive Disconfirmation) xảy ra khi nào?",
        "According to Oliver's Expectation-Confirmation Theory cited in Baran & Galka, when does 'Positive Disconfirmation' occur?",
        {
            "A": ("Khi hiệu năng sản phẩm thực tế vượt quá kỳ vọng ban đầu của khách hàng, dẫn đến cảm xúc hài lòng cao độ hoặc thích thú (Delight).", "When perceived product performance exceeds the customer's prior baseline expectations, yielding high satisfaction or delight."),
            "B": ("Khi khách hàng từ chối nhận hàng và yêu cầu hoàn lại tiền.", "When a buyer rejects delivery and demands an immediate monetary refund."),
            "C": ("Khi sản phẩm hoạt động kém hơn rất nhiều so với những gì quảng cáo hứa hẹn.", "When actual performance falls significantly below what marketing advertisements promised."),
            "D": ("Khi doanh nghiệp tăng giá bán sản phẩm lên gấp đôi mà không báo trước.", "When the merchant doubles list prices without prior announcement.")
        },
        "A",
        "Sự không xác nhận tích cực là nền tảng tạo ra sự bất ngờ thú vị (customer delight), thúc đẩy lòng trung thành thái độ và truyền miệng tích cực.",
        "Positive disconfirmation occurs when experienced reality surpasses expectations, driving emotional delight and brand advocacy.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 270-276", ["satisfaction-theory", "expectations", "delight"]
    ),
    (
        "q-07-02", "Net Promoter Score (NPS)", "easy", "single_choice",
        "Chỉ số Đo lường Mức độ Quảng bá (Net Promoter Score - NPS) phân loại khách hàng thành 3 nhóm dựa trên câu hỏi 'Khả năng bạn giới thiệu chúng tôi cho bạn bè/đồng nghiệp là bao nhiêu?' (thang điểm 0-10). Ba nhóm đó là:",
        "The Net Promoter Score (NPS) methodology segments respondents into which three cohorts based on their likelihood to recommend the brand (0–10 scale)?",
        {
            "A": ("Nhóm Giàu có, Nhóm Trung lưu, và Nhóm Bình dân.", "Wealthy, Middle-Class, and Working-Class."),
            "B": ("Người quảng bá (Promoters: điểm 9-10), Người thụ động (Passives: điểm 7-8), và Người chỉ trích/gièm pha (Detractors: điểm 0-6).", "Promoters (score 9–10), Passives (score 7–8), and Detractors (score 0–6)."),
            "C": ("Khách hàng mua sỉ, Khách hàng mua lẻ, và Đại lý phân phối.", "Wholesale, Retail, and Distribution Agents."),
            "D": ("Nhân viên công ty, Đối tác cung cấp, và Cổ đông sở hữu.", "Internal Staff, Supply Partners, and Corporate Shareholders.")
        },
        "B",
        "Công thức tính NPS chuẩn: NPS = % Promoters - % Detractors (bỏ qua nhóm Passives). Điểm số dao động từ -100 đến +100.",
        "NPS subtracts the percentage of Detractors from Promoters, providing a transparent barometer of organic customer advocacy and churn risk.",
        "Baran & Galka (2017)", "Chapter 9 & 11", "pp. 282-286, 352-356", ["nps", "customer-advocacy", "metrics"]
    ),
    (
        "q-07-03", "Customer Effort Score (CES)", "medium", "single_choice",
        "Khái niệm Điểm số Nỗ lực của Khách hàng (Customer Effort Score - CES) đo lường điều gì và có tác động ra sao đến lòng trung thành?",
        "What does the Customer Effort Score (CES) measure, and what is its empirical relationship to customer loyalty?",
        {
            "A": ("Đo số lượng calo khách hàng tiêu hao khi đi bộ trong siêu thị.", "The physical calories burned by shoppers walking through supermarket aisles."),
            "B": ("Đo mức độ dễ dàng hay khó khăn mà khách hàng phải trải qua để giải quyết một yêu cầu hoặc sự cố dịch vụ; nghiên cứu chứng minh giảm thiểu nỗ lực của khách hàng là cách giữ chân khách hiệu quả hơn là cố gắng gây bất ngờ.", "The ease with which a customer can resolve an inquiry or service issue; research demonstrates that minimizing customer effort builds loyalty more effectively than sporadic delight."),
            "C": ("Đo số tiền tối đa khách hàng có thể vay ngân hàng.", "The maximum credit line a customer can borrow from commercial banks."),
            "D": ("Đo số lượng bạn bè mà khách hàng có trên mạng xã hội.", "The total number of contacts connected on a customer's personal social profile.")
        },
        "B",
        "Nghiên cứu của Dixon et al. (The Effortless Experience) chứng minh rằng khách hàng trung thành nhất khi họ không phải tốn công sức: không phải gọi lại nhiều lần, không phải chuyển máy qua 3 người.",
        "CES proves that eliminating operational friction and resolving issues effortlessly drives retention far more predictably than attempting to delight users.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 285-288", ["ces", "customer-effort", "service-excellence"]
    ),
    (
        "q-07-04", "Service Recovery Paradox", "hard", "single_choice",
        "Hiện tượng 'Nghịch lý Khắc phục Dịch vụ' (Service Recovery Paradox) trong CRM mô tả trường hợp nào sau đây?",
        "What empirical phenomenon does the 'Service Recovery Paradox' describe in customer relationship literature?",
        {
            "A": ("Càng nhiều nhân viên chăm sóc khách hàng thì công ty càng thua lỗ.", "Hiring additional customer support staff leads to proportional operating losses."),
            "B": ("Một khách hàng gặp phải sự cố dịch vụ nhưng sau đó được doanh nghiệp tiếp nhận, giải quyết thỏa đáng và đền bù vượt mong đợi có thể trở nên trung thành và hài lòng hơn cả một khách hàng chưa từng gặp bất kỳ sự cố nào.", "A customer who experiences a service failure that is resolved exceptionally well can develop higher satisfaction and loyalty than if no failure had occurred at all."),
            "C": ("Dịch vụ càng kém thì khách hàng càng mua nhiều hàng hơn.", "Deteriorating service quality automatically induces customers to purchase more goods."),
            "D": ("Khách hàng phàn nàn luôn là người có ít tiền nhất.", "Complaining customers are statistically the lowest income demographic cohort.")
        },
        "B",
        "Nghịch lý này chứng minh tầm quan trọng sống còn của quy trình xử lý khiếu nại (Complaint Management) và trao quyền cho nhân viên tuyến đầu để biến 'nguy cơ' thành 'cơ hội gắn kết'.",
        "The paradox demonstrates that masterful service recovery humanizes the brand, demonstrating genuine empathy and converting disgruntled clients into fierce advocates.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 290-295", ["service-recovery", "paradox", "complaint-handling"]
    ),
    (
        "q-07-05", "Retention Leverage on Profitability", "hard", "single_choice",
        "Theo nghiên cứu kinh điển của Reichheld & Sasser được dẫn trong Baran & Galka, việc tăng tỷ lệ giữ chân khách hàng thêm 5% có thể giúp gia tăng lợi nhuận doanh nghiệp từ:",
        "According to foundational research by Reichheld & Sasser cited in Baran & Galka, a 5% increase in customer retention can boost bottom-line profits by:",
        {
            "A": ("0.5% đến 1%", "0.5% to 1%"),
            "B": ("25% đến 95%, tùy thuộc vào từng ngành nghề (nhờ chi phí phục vụ giảm, giao dịch định kỳ tăng và giới thiệu khách mới miễn phí).", "25% to 95%, depending on the industry (driven by lower servicing costs, price premiums, and zero-cost referrals)."),
            "C": ("Chính xác 5% đúng bằng tỷ lệ giữ chân.", "Exactly 5.0%, matching the retention gain 1-to-1 mathematically."),
            "D": ("Không làm tăng lợi nhuận vì giữ chân khách hàng luôn làm tăng chi phí quà tặng.", "Zero gain because customer retention expenses always equal new sales revenue.")
        },
        "B",
        "Lợi nhuận từ khách hàng trung thành tăng vọt theo thời gian do: doanh số mua định kỳ tăng, chi phí phục vụ giảm dần theo đường cong kinh nghiệm, ít đòi hỏi giảm giá và giới thiệu khách hàng mới.",
        "Reichheld's retention economics prove that loyal accounts generate compounding margins over their tenure, transforming small retention gains into massive profit jumps.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 310-316", ["retention-economics", "reichheld", "profit-leverage"]
    ),
    (
        "q-07-06", "ACSI Framework", "medium", "single_choice",
        "Mô hình Chỉ số Hài lòng Khách hàng Mỹ (American Customer Satisfaction Index - ACSI) xác định hai tiền đề (antecedents) trực tiếp tác động đến 'Chất lượng cảm nhận' (Perceived Quality) và 'Giá trị cảm nhận' (Perceived Value) là:",
        "In the American Customer Satisfaction Index (ACSI) structural equation model, which two direct antecedents shape customer satisfaction?",
        {
            "A": ("Kỳ vọng của Khách hàng (Customer Expectations) và Trải nghiệm Chất lượng Thực tế.", "Customer Expectations and Actual Perceived Quality / Value."),
            "B": ("Màu sắc của biển quảng cáo và thời gian phát sóng truyền hình.", "Billboard color palettes and television broadcast duration."),
            "C": ("Số lượng cổ phiếu niêm yết và lãi suất ngân hàng trung ương.", "Listed stock shares and central bank prime lending rates."),
            "D": ("Số lượng xe tải giao hàng của nhà cung ứng.", "The fleet size of logistics carrier freight vehicles.")
        },
        "A",
        "Mô hình ACSI liên kết chuỗi nhân quả: Kỳ vọng + Chất lượng cảm nhận + Giá trị cảm nhận -> Sự hài lòng (ACSI) -> Khiếu nại và Lòng trung thành của khách hàng.",
        "ACSI links cognitive expectations and perceived value to overall satisfaction, which directly governs the downstream balance between complaints and retention.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 278-284", ["acsi", "structural-equation-modeling", "satisfaction-drivers"]
    ),
    (
        "q-07-07", "Switching Barriers Types", "hard", "single_choice",
        "Rào cản chuyển đổi (Switching Costs / Switching Barriers) được chia thành ba nhóm chính theo Baran & Galka. Đó là:",
        "According to Baran & Galka, customer switching costs are classified into which three primary categories?",
        {
            "A": ("Chi phí pháp lý, Chi phí môi trường, và Chi phí thuế quan.", "Legal costs, Environmental costs, and Tariff duties."),
            "B": ("Chi phí chuyển đổi tài chính (Financial switching costs), Chi phí thủ tục/thời gian học hỏi (Procedural switching costs), và Chi phí gắn kết quan hệ/cảm xúc (Relational switching costs).", "Financial switching costs, Procedural / learning switching costs, and Relational / psychological switching costs."),
            "C": ("Chi phí xe buýt, Chi phí tàu hỏa, và Chi phí máy bay.", "Bus fare, Train tickets, and Airfare expenses."),
            "D": ("Chi phí phần cứng, Chi phí đường truyền, và Chi phí bảo hành.", "Hardware depreciation, Bandwidth costs, and Warranty fees.")
        },
        "B",
        "Doanh nghiệp xây dựng rào cản chuyển đổi không chỉ bằng phạt tiền vi phạm hợp đồng (tài chính), mà còn qua việc làm chủ dữ liệu người dùng (chi phí thủ tục) và sự tin cậy cá nhân (quan hệ).",
        "Switching costs span economic penalties, procedural friction (learning curves, data migration), and relational inertia (emotional trust with personnel).",
        "Baran & Galka (2017)", "Chapter 10", "pp. 318-324", ["switching-costs", "customer-retention", "lock-in"]
    ),
    (
        "q-07-08", "Loyalty Program Economic Fallacy", "hard", "single_choice",
        "Một sai lầm kinh tế phổ biến khi thiết kế Chương trình Khách hàng Thân thiết (Loyalty Program) dựa trên tích điểm đổi quà là gì?",
        "What is a common economic fallacy when designing point-based commercial Loyalty Programs?",
        {
            "A": ("Chương trình quá dễ hiểu đối với người tiêu dùng.", "The reward program is excessively intuitive for retail consumers."),
            "B": ("Chi trả phần thưởng cho các hành vi mà khách hàng vốn dĩ vẫn sẽ thực hiện mà không cần thưởng (thưởng cho khách hàng quen tự nhiên), làm xói mòn lợi nhuận biên mà không thay đổi được hành vi dài hạn.", "Rewarding transactions that core loyalists would have executed anyway without subsidies, eroding margins without shifting baseline behavior or attracting incremental spend."),
            "C": ("Khách hàng sử dụng điểm thưởng để mua thêm sản phẩm có biên lợi nhuận cao.", "Customers redeeming loyalty points to buy high-margin luxury add-ons."),
            "D": ("Hệ thống máy tính tự động gửi thông báo chúc mừng sinh nhật.", "Automated servers distributing personalized birthday greeting emails.")
        },
        "B",
        "Chương trình tích điểm thường biến thành một khoản 'giảm giá trá hình' tốn kém; nếu không thúc đẩy được chi tiêu bổ sung (incremental spend) hoặc bán chéo thì chương trình chỉ gây lãng phí.",
        "Points programs often degenerate into subsidized discounts for ingrained habits; without incremental basket lift or cross-category expansion, they leak margin.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 296-304", ["loyalty-programs", "incremental-lift", "margin-erosion"]
    ),
    (
        "q-07-09", "Customer Churn Types", "medium", "single_choice",
        "Sự khác biệt giữa Rời bỏ Tự nguyện (Voluntary Churn) và Rời bỏ Không tự nguyện (Involuntary Churn) trong CRM là gì?",
        "What distinguishes 'Voluntary Churn' from 'Involuntary Churn' in subscription and recurring revenue CRM models?",
        {
            "A": ("Rời bỏ tự nguyện là do khách hàng qua đời; Rời bỏ không tự nguyện là do khách hàng trúng xổ số.", "Voluntary churn stems from death; involuntary churn stems from winning lottery jackpots."),
            "B": ("Rời bỏ tự nguyện là khi khách hàng chủ động hủy hợp đồng vì bất mãn hoặc chuyển sang đối thủ; Rời bỏ không tự nguyện xảy ra do lỗi thanh toán kỹ thuật (thẻ tín dụng hết hạn, tài khoản không đủ số dư) dù khách hàng vẫn muốn sử dụng dịch vụ.", "Voluntary churn occurs when a client actively cancels due to dissatisfaction or competitor offers; Involuntary churn happens via passive billing failures (expired cards, soft bank declines) despite user intent to remain."),
            "C": ("Không có sự khác biệt vì cả hai đều làm giảm số lượng khách hàng.", "There is no difference because both result in identical revenue attrition."),
            "D": ("Rời bỏ không tự nguyện chỉ xảy ra ở các cơ quan chính phủ.", "Involuntary churn applies exclusively to municipal government agencies.")
        },
        "B",
        "Involuntary churn chiếm từ 20-40% tổng số lượt hủy dịch vụ SaaS; doanh nghiệp có thể dễ dàng khắc phục bằng công cụ tự động cập nhật thẻ (Account Updater) và dunning emails.",
        "Involuntary churn represents frictionless recovery potential; smart dunning automation and proactive card-updater APIs recover significant subscription leakage.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 326-330", ["churn-types", "voluntary-churn", "involuntary-churn"]
    ),
    (
        "q-07-10", "Frontline Empowerment in Recovery", "medium", "single_choice",
        "Tại sao chính sách 'Trao quyền cho Nhân viên Tuyến đầu' (Frontline Empowerment) lại mang tính quyết định trong việc giữ chân khách hàng khi xảy ra sự cố dịch vụ?",
        "Why is frontline employee empowerment decisive in mitigating defection during service failure episodes?",
        {
            "A": ("Để nhân viên có thể tự do nghỉ làm bất kỳ lúc nào họ muốn.", "Allowing customer service agents to take unannounced personal leaves."),
            "B": ("Cho phép nhân viên giải quyết khiếu nại và đền bù ngay tại điểm tiếp xúc đầu tiên (First-Contact Resolution) trong một hạn mức tài chính nhất định mà không cần xin phép qua nhiều cấp quản lý rườm rà.", "Permitting frontline reps to resolve complaints and grant immediate compensatory concessions within predefined budgetary boundaries without multi-tier managerial delays."),
            "C": ("Để sa thải nhân viên trực tiếp mà không cần phòng nhân sự phê duyệt.", "Enabling on-the-spot dismissals of customer support staff without HR approval."),
            "D": ("Để nhân viên có quyền từ chối mọi yêu cầu trợ giúp của khách hàng.", "Giving reps absolute authority to decline all customer service requests.")
        },
        "B",
        "Khách hàng đang bức xúc sẽ càng giận dữ hơn nếu phải nghe câu 'Tôi phải xin ý kiến sếp và phản hồi lại sau 3 ngày'; giải quyết ngay tại chỗ giúp dập tắt khủng hoảng.",
        "Forcing aggrieved clients to endure multi-day managerial review escalates fury; on-the-spot empowerment resolves issues before complaints turn into viral detraction.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 292-297", ["frontline-empowerment", "first-contact-resolution"]
    ),
    (
        "q-07-11", "Customer Delight vs Satisfaction", "hard", "single_choice",
        "Theo nghiên cứu của Schneider & Bowen được trích dẫn trong Baran & Galka, để biến một khách hàng từ trạng thái 'Hài lòng' thông thường sang 'Thích thú / Gắn kết sâu sắc' (Delight), doanh nghiệp phải chạm đến:",
        "According to Schneider & Bowen's framework cited in Baran & Galka, transitioning customers from ordinary satisfaction to emotional 'Delight' requires fulfilling which psychological needs?",
        {
            "A": ("Tặng tiền mặt cho khách hàng mỗi khi họ bước vào cửa hàng.", "Handing unannounced cash envelopes to patrons whenever they enter a retail outlet."),
            "B": ("Thỏa mãn các nhu cầu tâm lý sâu kín về: Công lý/Công bằng (Justice), Sự tự trọng (Self-Esteem), và Cảm giác an toàn/được bảo vệ (Security).", "Fulfilling underlying psychological needs for Fairness/Justice, Personal Self-Esteem, and Security/Trust."),
            "C": ("Giảm giá toàn bộ các sản phẩm xuống dưới mức giá vốn.", "Selling all enterprise inventory permanently below manufacturing cost."),
            "D": ("Bắt buộc khách hàng phải khen ngợi sản phẩm trên báo chí.", "Requiring patrons to publish mandatory positive reviews in print newspapers.")
        },
        "B",
        "Khách hàng chỉ thực sự gắn bó về mặt cảm xúc khi doanh nghiệp tôn trọng nhân phẩm, bảo vệ quyền lợi công bằng và mang lại cho họ cảm giác an tâm tuyệt đối.",
        "Emotional delight transcends mechanical utility, cementing loyalty when firms demonstrate deep moral fairness, protect customer dignity, and provide psychological security.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 274-279", ["customer-delight", "psychological-needs", "justice"]
    ),
    (
        "q-07-12", "Zone of Defection vs Zone of Affection", "hard", "single_choice",
        "Trong sơ đồ ma trận giữa Mức độ Hài lòng và Lòng Trung thành (Satisfaction-Loyalty Framework của Heskett et al.), nhóm khách hàng nằm trong 'Vùng Thờ ơ' (Zone of Indifference) có đặc điểm gì?",
        "In Heskett et al.'s Satisfaction-Loyalty framework cited in Baran & Galka, what characterizes accounts situated in the 'Zone of Indifference'?",
        {
            "A": ("Họ cực kỳ căm ghét thương hiệu và liên tục đăng bài bôi nhọ trên mạng xã hội.", "They harbor venomous hatred for the brand and actively post online defamation."),
            "B": ("Họ có mức độ hài lòng ở mức vừa phải (từ 3 đến 4 trên thang điểm 5), không có gắn kết cảm xúc sâu sắc và rất dễ dàng chuyển đổi sang đối thủ cạnh tranh nếu có chương trình giảm giá tốt hơn.", "They express moderate satisfaction (scores 3 to 4 out of 5), possess zero emotional brand attachment, and readily defect to rivals offering nominal price cuts."),
            "C": ("Họ là những người hâm mộ cuồng nhiệt sẵn sàng trả giá cao hơn 50% cho thương hiệu.", "They are diehard brand apostles willing to pay a 50% price premium."),
            "D": ("Họ là những người không bao giờ sử dụng dịch vụ.", "They are non-consumers who never utilize the product category.")
        },
        "B",
        "Khách hàng 'hài lòng vừa phải' là nhóm nguy hiểm nhất vì doanh nghiệp thường lầm tưởng họ ổn định, nhưng thực tế họ sẵn sàng rời bỏ ngay khi có sự lựa chọn khác.",
        "Merely satisfied accounts in the Zone of Indifference represent high defection risk; lack of emotional affinity means marginal competitor incentives prompt immediate switching.",
        "Baran & Galka (2017)", "Chapter 9 & 10", "pp. 280-285, 314-318", ["zone-of-indifference", "heskett", "loyalty-matrix"]
    ),
    (
        "q-07-13", "Complaint Behavior Iceberg", "medium", "single_choice",
        "Hiện tượng 'Tảng băng trôi của hành vi khiếu nại' (The Complaint Iceberg) trong nghiên cứu dịch vụ khách hàng chỉ ra rằng:",
        "What does the 'Complaint Iceberg' phenomenon reveal about dissatisfied customer behavior?",
        {
            "A": ("100% khách hàng không hài lòng đều sẽ gửi thư khiếu nại bằng văn bản cho giám đốc.", "100% of aggrieved customers submit formal written complaints to corporate executives."),
            "B": ("Chỉ có khoảng 4% đến 6% khách hàng không hài lòng chủ động lên tiếng phàn nàn trực tiếp với công ty; hơn 90% còn lại âm thầm rời bỏ sang đối thủ và kể lại trải nghiệm tiêu cực cho người khác.", "Only 4% to 6% of dissatisfied customers actively voice complaints to company personnel; over 90% silently defect to competitors while spreading negative word-of-mouth."),
            "C": ("Khách hàng phàn nàn nhiều nhất vào mùa đông khi có băng tuyết.", "Customers file the most complaints during cold winter sub-zero blizzards."),
            "D": ("Tất cả các lời phàn nàn của khách hàng đều là bịa đặt.", "All customer complaints are statistically proven to be fraudulent fabrication.")
        },
        "B",
        "Một lời khiếu nại là một món quà (A Complaint is a Gift); khách hàng lên tiếng giúp doanh nghiệp biết chỗ hỏng để sửa, trong khi sự im lặng dẫn thẳng đến việc mất khách hàng.",
        "Unvoiced dissatisfaction is lethal; for every customer who complains, dozens exit silently, making proactive outreach and feedback solicitation mandatory.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 288-292", ["complaint-iceberg", "customer-feedback", "silent-churn"]
    ),
    (
        "q-07-14", "Share of Wallet (SOW)", "medium", "single_choice",
        "Chỉ số 'Thị phần Chi tiêu' (Share of Wallet - SOW) trong CRM phản ánh:",
        "In CRM customer analytics, what does 'Share of Wallet' (SOW) measure?",
        {
            "A": ("Số lượng ví tiền bằng da mà khách hàng sở hữu trong nhà.", "The physical count of leather wallets stored in a customer's bedroom."),
            "B": ("Tỷ lệ phần trăm chi tiêu của khách hàng dành cho thương hiệu của doanh nghiệp trong tổng số tiền mà khách hàng đó chi trả cho toàn bộ ngành hàng đó.", "The percentage of a customer's total category expenditure allocated to a specific enterprise brand relative to all competing options."),
            "C": ("Tổng số tiền khách hàng có trong tài khoản tiết kiệm ngân hàng.", "The total liquidity balance retained in a customer's personal savings account."),
            "D": ("Chi phí sản xuất ví da đựng thẻ tín dụng.", "The industrial manufacturing cost of credit card holder cases.")
        },
        "B",
        "SOW giúp phát hiện các khách hàng chi tiêu lớn nhưng công ty mới chỉ chiếm được 10% nhu cầu của họ, mở ra tiềm năng bán chéo (cross-sell) khổng lồ.",
        "SOW illuminates wallet expansion potential, highlighting customers who spend heavily in the vertical but allocate only a fractional slice to the firm.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 322-328", ["share-of-wallet", "sow", "wallet-expansion"]
    ),
    (
        "q-07-15", "Discount Rate Impact on CLV", "hard", "single_choice",
        "Trong mô hình định giá Giá trị Vòng đời Khách hàng (CLV), nếu tỷ lệ chiết khấu dòng tiền (Discount Rate - d) tăng lên do lãi suất thị trường tăng, giá trị CLV của cơ sở khách hàng sẽ thay đổi như thế nào?",
        "In Customer Lifetime Value (CLV) discounted cash flow valuation, if the corporate discount rate (d) increases due to rising macroeconomic interest rates, how does aggregate CLV respond?",
        {
            "A": ("CLV sẽ giảm xuống, vì các dòng lợi nhuận trong tương lai bị chiết khấu về giá trị hiện tại với tỷ lệ cao hơn.", "Aggregate CLV decreases, because future projected margin streams are discounted to the present value at a steeper penalty rate."),
            "B": ("CLV sẽ tăng vọt gấp đôi một cách tự động.", "Aggregate CLV automatically doubles in nominal monetary terms."),
            "C": ("CLV hoàn toàn không thay đổi vì lãi suất không ảnh hưởng đến khách hàng.", "Aggregate CLV remains mathematically invariant to macroeconomic discount rates."),
            "D": ("CLV ngay lập tức biến thành số âm.", "Aggregate CLV immediately transforms into negative equity values.")
        },
        "A",
        "Theo công thức tài chính chiết khấu, lãi suất chiết khấu nằm ở mẫu số (1 + d - r); khi d tăng lên, giá trị hiện tại ròng (NPV) của các dòng tiền tương lai sẽ bị giảm giá trị.",
        "As discount rates rise, the present value of distant retention cash flows diminishes, depressing total customer equity capitalization.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 312-317", ["clv", "discount-rate", "financial-modeling"]
    ),
    (
        "q-07-16", "Customer Win-Back Strategy", "medium", "single_choice",
        "Khi thực hiện chiến dịch 'Chinh phục lại Khách hàng đã Rời bỏ' (Customer Win-Back Campaign), bước phân tích đầu tiên cần làm là:",
        "When initiating a Customer Win-Back initiative to re-engage lapsed accounts, what is the mandatory first analytical step?",
        {
            "A": ("Gửi mã giảm giá 90% cho toàn bộ những người đã hủy tài khoản trong 10 năm qua.", "Blasting an indiscriminate 90% discount code to every lapsed account over the past decade."),
            "B": ("Phân loại nguyên nhân rời bỏ (do giá cả, do dịch vụ kém, hay do không còn nhu cầu) và tính toán lại CLV tiềm năng để chỉ tập trung vào nhóm khách hàng sinh lời cao có thể cứu vãn.", "Diagnosing defection root causes (pricing, service failures, or obsolescence) and recalculating residual CLV to selectively target high-yield, salvageable accounts."),
            "C": ("Thuê công ty đòi nợ đến nhà khách hàng để yêu cầu tiếp tục ký hợp đồng.", "Dispatching collection agencies to customer homes to demand contract renewals."),
            "D": ("Xóa sạch hồ sơ của khách hàng cũ để không làm bẩn cơ sở dữ liệu.", "Purging historical transaction files of departed accounts to save disk space.")
        },
        "B",
        "Không phải khách hàng rời bỏ nào cũng đáng để giành lại; cố gắng cứu vãn những khách hàng luôn đòi hỏi vô lý hoặc gây lỗ (unprofitable churners) chỉ làm doanh nghiệp kiệt quệ.",
        "Win-back campaigns must be laser-focused; attempting to rescue perpetually unprofitable or toxic accounts squanders marketing resources on negative-margin relationships.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 332-338", ["customer-win-back", "defection-analysis", "salvageability"]
    ),
    (
        "q-07-17", "Attitudinal Loyalty Measurement", "hard", "single_choice",
        "Để đo lường 'Lòng trung thành thái độ' (Attitudinal Loyalty) của khách hàng một cách khoa học, bảng câu hỏi nghiên cứu thường đo lường ba biến số nào?",
        "To measure 'Attitudinal Loyalty' rigorously in empirical CRM research, which three latent variables are typically assessed?",
        {
            "A": ("Cân nặng, Chiều cao, và Tốc độ đi bộ của người mua.", "Physical weight, height, and walking velocity of the respondent."),
            "B": ("Sự gắn kết cảm xúc với thương hiệu (Affective Commitment), Ý định mua lại trong tương lai (Repurchase Intent), và Sự sẵn sàng giới thiệu cho người khác (Willingness to Advocate/Recommend).", "Affective Commitment (emotional bond), Repurchase Intentions, and Willingness to Advocate (positive word-of-mouth referral)."),
            "C": ("Số lượng thẻ tín dụng trong ví và số tiền trong tài khoản thanh toán.", "The quantity of credit cards in possession and bank checking liquidity."),
            "D": ("Tần suất mở tủ lạnh và số lần bật tivi mỗi ngày.", "Daily refrigerator door opening frequency and television viewing intervals.")
        },
        "B",
        "Lòng trung thành thái độ đo lường trạng thái tâm lý gắn kết: niềm tin, sự yêu thích và chủ động bảo vệ thương hiệu trước sự chèo kéo của đối thủ.",
        "Attitudinal loyalty measures genuine psychological allegiance: emotional attachment, future buying intention, and organic peer advocacy.",
        "Baran & Galka (2017)", "Chapter 9", "pp. 276-282", ["attitudinal-loyalty", "affective-commitment", "advocacy"]
    ),
    (
        "q-07-18", "Two-Way Communication Asymmetry", "medium", "single_choice",
        "Trong thời đại kỹ thuật số, nguyên lý 'Giao tiếp Đối thoại Hai chiều' (Two-Way Symmetrical Communication) trong CRM đòi hỏi doanh nghiệp phải:",
        "In the digital landscape, what does the principle of 'Two-Way Symmetrical Communication' mandate for CRM practitioners?",
        {
            "A": ("Chỉ gửi tin nhắn quảng cáo đơn phương và khóa tính năng bình luận/trả lời của khách hàng.", "Sending unilateral promotional broadcasts while disabling all reply and comment mechanisms."),
            "B": ("Lắng nghe phản hồi thực tế của khách hàng, duy trì đối thoại cởi mở và chủ động điều chỉnh quy trình sản phẩm dựa trên các ý kiến đóng góp của người tiêu dùng.", "Actively listening to consumer feedback, sustaining open authentic dialogue, and iteratively adapting operational workflows in response to customer voice."),
            "C": ("Gửi tin nhắn thoại tự động vào lúc 3 giờ sáng mỗi ngày.", "Distributing automated robocalls to mobile phones at 3:00 AM daily."),
            "D": ("Bắt buộc khách hàng phải khen ngợi công ty trước khi được hỗ trợ kỹ thuật.", "Requiring customers to submit written praise before unlocking technical support.")
        },
        "B",
        "Giao tiếp đối xứng coi khách hàng là đối tác bình đẳng trong mối quan hệ; doanh nghiệp không chỉ 'nói' mà phải thực sự 'lắng nghe' và 'hành động' theo phản hồi.",
        "Symmetrical communication rejects manipulative corporate monologue, treating customers as authentic dialogue partners whose insights reshape service delivery.",
        "Baran & Galka (2017)", "Chapter 9 & 13", "pp. 288-294, 405-410", ["dialogue", "symmetrical-communication", "listening"]
    ),
    (
        "q-07-19", "Relationship Dissolution Stages", "hard", "single_choice",
        "Theo mô hình giải thể mối quan hệ của Dwyer, Schurr & Oh được dẫn trong Baran & Galka, giai đoạn mà một bên bắt đầu âm thầm đánh giá sự không thỏa đáng của đối tác và cân nhắc các lựa chọn thay thế được gọi là:",
        "According to Dwyer, Schurr & Oh's relationship dissolution framework cited in Baran & Galka, the stage where a partner privately evaluates dissatisfaction and weighs alternatives is called:",
        {
            "A": ("Giai đoạn Tiếp cận (Exploration Phase)", "Exploration Phase"),
            "B": ("Giai đoạn Nội tâm / Độc thoại nội tâm (Intrapsychic Phase)", "Intrapsychic Phase"),
            "C": ("Giai đoạn Gắn kết bền vững (Commitment Phase)", "Commitment Phase"),
            "D": ("Giai đoạn Công khai pháp lý trước tòa", "Public Legal Litigation Phase")
        },
        "B",
        "Trong giai đoạn Intrapsychic, khách hàng chưa lên tiếng nhưng bắt đầu nảy sinh sự thất vọng ngấm ngầm; nếu CRM phân tích phát hiện sớm dấu hiệu này có thể can thiệp trước khi khách chính thức hủy hợp đồng.",
        "In the intrapsychic phase, dissatisfaction brews silently without overt confrontation; predictive CRM telemetry must flag engagement drops to trigger preventive intervention.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 328-333", ["relationship-dissolution", "intrapsychic-phase", "churn-prevention"]
    ),
    (
        "q-07-20", "Customer Referral Value (CRV)", "medium", "single_choice",
        "Khái niệm 'Giá trị Giới thiệu của Khách hàng' (Customer Referral Value - CRV) bổ sung cho CLV truyền thống như thế nào?",
        "How does the concept of 'Customer Referral Value' (CRV) augment traditional Customer Lifetime Value (CLV)?",
        {
            "A": ("CRV đo lường số tiền công ty phải trả cho quảng cáo truyền hình.", "CRV measures gross enterprise expenditures dedicated to broadcast television advertising."),
            "B": ("CRV lượng hóa giá trị kinh tế của các khách hàng mới được mang về nhờ sự truyền miệng tích cực và giới thiệu trực tiếp của một khách hàng hiện tại.", "CRV quantifies the aggregate net profit contribution delivered by new customers acquired directly through positive word-of-mouth recommendations by an existing client."),
            "C": ("CRV là tiền hoa hồng công ty trả cho môi giới bất động sản.", "CRV represents legal broker commission payouts on real estate acquisitions."),
            "D": ("CRV đo lường số lần khách hàng chia sẻ ảnh phong cảnh trên trang cá nhân.", "CRV counts the number of landscape photos shared on private social walls.")
        },
        "B",
        "Một khách hàng có thể mua sản phẩm với giá trị thấp (CLV thấp) nhưng lại có tầm ảnh hưởng lớn và giới thiệu thành công 20 khách hàng mới (CRV cực cao); tính cả CRV giúp định giá toàn diện giá trị khách hàng.",
        "An account with modest personal purchasing volume (low CLV) may serve as a powerful brand evangelist (high CRV); synthesizing CLV and CRV yields true customer equity.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 320-326", ["crv", "customer-referral-value", "customer-equity"]
    )
]

for item in e7:
    questions_batch3.append(make_q(
        item[0], "EXAM-07", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

# ==========================================
# EXAM 08: B2B CRM & STRATEGIC PARTNERSHIPS (q-08-01 to q-08-20)
# ==========================================
e8 = [
    (
        "q-08-01", "Buying Center / DMU", "easy", "single_choice",
        "Trong môi trường B2B CRM, Trung tâm Mua hàng (Buying Center / Decision Making Unit - DMU) thường bao gồm các vai trò nào?",
        "In B2B CRM environments, the enterprise Buying Center (Decision Making Unit - DMU) typically encompasses which key roles?",
        {
            "A": ("Chỉ duy nhất một cá nhân là nhân viên bảo vệ cổng cơ quan.", "A solitary individual serving as the corporate gate security guard."),
            "B": ("Người khởi xướng (Initiator), Người sử dụng (User), Người ảnh hưởng (Influencer), Người gác cổng (Gatekeeper), Người quyết định (Decider), và Người mua/đàm phán (Buyer).", "Initiator, User, Influencer, Gatekeeper, Decider, and Buyer / Procurement Officer."),
            "C": ("Tất cả các hành khách đi trên cùng một chuyến xe buýt công cộng.", "All concurrent commuters aboard a single municipal public transport vehicle."),
            "D": ("Giám đốc điều hành của 10 công ty đối thủ cạnh tranh.", "The chief executive officers of ten competing rival enterprises.")
        },
        "B",
        "Quyết định mua B2B là một tiến trình tập thể phức tạp; CRM B2B phải lập bản đồ các mối quan hệ và vai trò của từng cá nhân trong Buying Center để tiếp cận phù hợp.",
        "B2B buying involves multi-stakeholder consensus; CRM systems must map stakeholder personas, influence weight, and decision criteria across the buying unit.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 238-245", ["buying-center", "dmu", "b2b-crm"]
    ),
    (
        "q-08-02", "Key Account Management (KAM)", "medium", "single_choice",
        "Chương trình Quản trị Khách hàng Trọng điểm (Key Account Management - KAM) trong B2B CRM nhằm mục đích cốt lõi là gì?",
        "What is the foundational strategic objective of a Key Account Management (KAM) program in B2B CRM?",
        {
            "A": ("Bán cho khách hàng một lô hàng lỗi giá rẻ để thu hồi vốn nhanh.", "Dumping defective inventory batches onto clients to recover immediate liquid cash."),
            "B": ("Thiết lập mối quan hệ đối tác chiến lược sâu sắc, tùy biến sản phẩm và quy trình chuyên biệt cho 10-20% khách hàng doanh nghiệp đóng góp tới 80% doanh thu/lợi nhuận của công ty.", "Cultivating deep strategic partnerships with tailored product/service adaptations for the vital 10–20% of corporate accounts that drive up to 80% of revenue and margin."),
            "C": ("Cấm khách hàng trọng điểm không được gọi điện thoại cho ban giám đốc.", "Barring premier accounts from telephoning executive board members."),
            "D": ("Yêu cầu khách hàng trọng điểm phải ứng trước 100% tiền hàng bằng vàng ròng.", "Requiring elite enterprise accounts to pre-fund all orders in physical gold bullion.")
        },
        "B",
        "KAM phân bổ nguồn lực chuyên biệt (nhóm phục vụ riêng, tích hợp hệ thống) để bảo vệ và mở rộng mối quan hệ với những khách hàng doanh nghiệp sống còn.",
        "KAM establishes dedicated cross-functional account teams, custom SLAs, and joint innovation initiatives to insulate high-value corporate accounts from competitor predation.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 246-254", ["kam", "key-account-management", "b2b-strategy"]
    ),
    (
        "q-08-03", "Relational Governance vs Contracts", "hard", "single_choice",
        "Trong quan hệ đối tác B2B, 'Quản trị Quan hệ' (Relational Governance) dựa trên niềm tin và sự linh hoạt khác với 'Quản trị Hợp đồng Giao dịch' (Contractual Governance) ở điểm nào?",
        "In B2B partnerships, how does 'Relational Governance' based on mutual trust and norms differ from rigid 'Contractual Governance'?",
        {
            "A": ("Quản trị quan hệ không cần ký kết bất kỳ giấy tờ nào và không có giá trị pháp lý.", "Relational governance forbids any written documentation and holds zero legal status."),
            "B": ("Quản trị hợp đồng dựa trên các điều khoản pháp lý cứng nhắc và chế tài phạt vi phạm; Quản trị quan hệ dựa trên chuẩn mực chia sẻ thông tin minh bạch, giải quyết tranh chấp thiện chí và cùng chia sẻ rủi ro/lợi ích khi bối cảnh thay đổi.", "Contractual governance relies on exhaustive legal clauses and penalty threats; Relational governance relies on shared norms, transparent communication, joint problem-solving, and mutual risk-reward sharing."),
            "C": ("Quản trị quan hệ chỉ áp dụng cho các doanh nghiệp sắp phá sản.", "Relational governance is restricted solely to firms facing immediate liquidation."),
            "D": ("Quản trị hợp đồng đảm bảo đối tác không bao giờ vi phạm cam kết.", "Contractual governance guarantees that partners never default on performance milestones.")
        },
        "B",
        "Hợp đồng không thể lường trước mọi biến động thực tế; các chuẩn mực quan hệ (relational norms) giúp đối tác thích ứng linh hoạt và bền vững hơn trước các cú sốc thị trường.",
        "Contracts cannot anticipate every contingency; relational governance provides the psychological safety and elasticity required to collaborate through unforeseen market volatility.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 242-248", ["relational-governance", "contractual-governance", "trust"]
    ),
    (
        "q-08-04", "GAFA Ecosystem Synergy", "hard", "single_choice",
        "Theo tình huống nghiên cứu 'Big Four Digital Firms - GAFA' (Experiential Marketing, Ch. 1, tr. 2-30), điểm chung cốt lõi trong chiến lược xây dựng mối quan hệ và trải nghiệm khách hàng của Google, Apple, Facebook và Amazon là gì?",
        "According to the 'Big Four Digital Firms (GAFA)' case study (Batat, Chapter 1, pp. 2-30), what is the unifying strategic core of customer experience across Google, Apple, Facebook, and Amazon?",
        {
            "A": ("Họ chỉ bán sản phẩm phần cứng vật lý truyền thống qua hệ thống siêu thị đại lý.", "They operate exclusively as traditional hardware vendors distributing via brick-and-mortar dealers."),
            "B": ("Họ xây dựng các Hệ sinh thái Nền tảng Đa diện (Multi-Sided Platform Ecosystems) liên kết chặt chẽ phần cứng, phần mềm, dịch vụ đám mây và dữ liệu hành vi, tạo ra hiệu ứng mạng lưới (Network Effects) và chi phí chuyển đổi khổng lồ giữ chân người dùng.", "They cultivate Multi-Sided Platform Ecosystems seamlessly uniting proprietary hardware, cloud services, and behavioral telemetry, generating formidable Network Effects and high switching barriers."),
            "C": ("Họ từ chối mọi hoạt động quảng cáo trên mạng internet.", "They universally refuse all digital advertising investments on the global web."),
            "D": ("Họ chỉ phục vụ các khách hàng là cơ quan nhà nước tại Hoa Kỳ.", "They serve exclusively municipal civil government agencies located in North America.")
        },
        "B",
        "GAFA không chỉ bán một sản phẩm đơn lẻ mà tạo ra cả một 'khu vườn có tường bao' (walled garden) nơi mọi tiện ích đều kết nối với nhau, khiến người dùng không muốn và không thể rời đi.",
        "The GAFA playbook embeds users in immersive ecosystems where hardware, software, and services cross-subsidize each other, engineering massive lock-in via network effects.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 1", "pp. 2-30", ["gafa-case", "platform-ecosystems", "network-effects"]
    ),
    (
        "q-08-05", "GAFA Value Co-Creation", "hard", "single_choice",
        "Trong tình huống GAFA, khái niệm 'Đồng kiến tạo Giá trị' (Value Co-Creation) được thể hiện rõ nét nhất qua hoạt động nào?",
        "In the GAFA enterprise analysis, how is 'Value Co-Creation' most vividly demonstrated across digital ecosystems?",
        {
            "A": ("Doanh nghiệp tự sản xuất 100% nội dung và không cho phép người dùng đăng bài.", "Enterprises authoring 100% of platform content while barring user contributions."),
            "B": ("Người dùng và đối tác phát triển đóng vai trò tích cực tạo ra giá trị cho nền tảng (như các lập trình viên viết ứng dụng cho Apple App Store, người dùng tạo nội dung trên Facebook, thương nhân bán hàng trên Amazon Marketplace).", "Users and third-party developers actively generating platform equity (e.g., developers building iOS apps, users publishing Facebook feeds, third-party merchants stocking Amazon Marketplace)."),
            "C": ("Nhà sản xuất gửi hàng mẫu miễn phí qua đường bưu điện cho mọi công dân.", "Distributing free physical product prototypes via government postal mail to all citizens."),
            "D": ("Công ty đóng cửa toàn bộ máy chủ vào cuối tuần để tiết kiệm điện.", "Shutting down platform cloud servers on weekends to minimize utility overhead.")
        },
        "B",
        "Đồng kiến tạo giá trị chuyển đổi người dùng từ 'người tiêu thụ thụ động' thành 'người vừa sản xuất vừa tiêu thụ' (Prosumers) và đối tác kinh doanh cùng làm giàu cho nền tảng.",
        "Platforms thrive on co-creation, harnessing external developer creativity and user-generated engagement to build flywheel effects that no single corporation could fund in-house.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 1", "pp. 8-16", ["value-co-creation", "prosumer", "platform-flywheel"]
    ),
    (
        "q-08-06", "Partner Relationship Management (PRM)", "medium", "single_choice",
        "Hệ thống Quản lý Quan hệ Đối tác (Partner Relationship Management - PRM) trong B2B CRM hỗ trợ doanh nghiệp giải quyết thách thức nào trong kênh phân phối gián tiếp?",
        "In B2B indirect sales channels, what foundational challenge does a Partner Relationship Management (PRM) system resolve?",
        {
            "A": ("Quản lý bếp ăn tập thể của nhà máy sản xuất linh kiện.", "Overseeing the cafeteria food catering services of manufacturing plants."),
            "B": ("Đăng ký và bảo vệ Cơ hội Bán hàng (Deal Registration), chia sẻ tài liệu tiếp thị kỹ thuật, cấp chứng chỉ đào tạo cho đại lý và giải quyết xung đột kênh (Channel Conflict).", "Managing Deal Registration to protect partner leads, sharing co-branded collateral, automating certification workflows, and resolving multi-tier Channel Conflict."),
            "C": ("Thay thế toàn bộ đại lý bán lẻ bằng nhân viên bán hàng trực tiếp của hãng.", "Terminating all third-party distributors and replacing them with internal sales staff."),
            "D": ("Bắt buộc các đại lý phải trả phí bằng tiền mặt hàng ngày.", "Requiring independent retail dealers to settle commission dues in daily cash.")
        },
        "B",
        "PRM portal giúp các đại lý đăng ký cơ hội kinh doanh để tránh tình trạng nhiều đại lý cùng tranh giành một khách hàng, đồng thời cung cấp công cụ bán hàng đồng bộ.",
        "PRM portals establish transparency in two-tier distribution, preventing lead poaching through formal deal registration and certifying reseller technical competency.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 250-256", ["prm", "channel-conflict", "deal-registration"]
    ),
    (
        "q-08-07", "Channel Conflict Management", "medium", "single_choice",
        "Hiện tượng 'Xung đột Kênh' (Channel Conflict) xảy ra phổ biến nhất trong tình huống nào sau đây?",
        "Under which operational scenario does 'Channel Conflict' most frequently erupt in multi-tier B2B environments?",
        {
            "A": ("Khi công ty chỉ bán hàng qua một đại lý độc quyền duy nhất trên toàn quốc.", "When an enterprise sells exclusively through a single nationwide distributor."),
            "B": ("Khi nhà sản xuất vừa mở kênh bán hàng trực tuyến (Direct-to-Consumer / D2C) cạnh tranh trực tiếp về giá với chính hệ thống đại lý bán buôn, bán lẻ truyền thống của mình.", "When a manufacturer launches a direct digital e-commerce storefront (D2C) that undercuts the retail pricing of its independent dealer and distributor network."),
            "C": ("Khi tất cả các đại lý cùng nhau tổ chức hội nghị khách hàng thường niên.", "When all regional dealers collaboratively coordinate an annual joint summit."),
            "D": ("Khi nhà sản xuất tăng thời hạn bảo hành cho sản phẩm từ 1 năm lên 2 năm.", "When a manufacturer extends product warranty coverage from one to two years.")
        },
        "B",
        "Bán hàng trực tiếp qua web giúp tăng biên lợi nhuận nhưng lại gây phẫn nộ cho hệ thống đại lý lâu năm; doanh nghiệp cần có chính sách phân chia dòng sản phẩm hoặc chia sẻ hoa hồng để dung hòa.",
        "D2C expansion threatens legacy distributor margins; mitigating channel conflict requires clear territory boundaries, differentiated SKU lines, or revenue-sharing models.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 252-257", ["channel-conflict", "d2c-vs-dealers", "omnichannel"]
    ),
    (
        "q-08-08", "B2B Sales Funnel Stages", "easy", "single_choice",
        "Trong quy trình bán hàng B2B phức tạp, giai đoạn 'Thẩm định Tư cách Mua hàng' (Lead Qualification) thường sử dụng khung tiêu chí kinh điển BANT, viết tắt của:",
        "In complex B2B sales pipelines, the classic BANT lead qualification framework evaluates which four parameters?",
        {
            "A": ("Building, Architecture, Network, Telecom", "Building, Architecture, Network, Telecom"),
            "B": ("Budget (Ngân sách), Authority (Thẩm quyền quyết định), Need (Nhu cầu thực tế), Timeline (Khung thời gian mua sắm).", "Budget, Authority, Need, and Timeline."),
            "C": ("Brand, Attitude, Name, Trust", "Brand, Attitude, Name, Trust"),
            "D": ("Bonus, Commission, Salary, Tax", "Bonus, Commission, Salary, Tax")
        },
        "B",
        "BANT giúp nhân viên kinh doanh sàng lọc sớm các đầu mối: Khách hàng có tiền không? Người tiếp xúc có quyền duyệt không? Nhu cầu có cấp bách không? Khi nào họ cần giải pháp?",
        "BANT ensures sales resources focus on high-probability opportunities where funding is allocated, stakeholders have authority, business pain exists, and a deadline is set.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 244-249", ["bant", "lead-qualification", "b2b-pipeline"]
    ),
    (
        "q-08-09", "Specific Asset Investments", "hard", "single_choice",
        "Khái niệm 'Đầu tư vào Tài sản Đặc thù' (Specific Asset Investments / Idiosyncratic Investments) trong quan hệ đối tác B2B có tác động gì đến mối quan hệ?",
        "What structural impact do 'Idiosyncratic / Relation-Specific Asset Investments' exert on B2B partnership stability?",
        {
            "A": ("Làm cho hai công ty ngay lập tức hủy bỏ mọi hợp đồng giao dịch.", "Inducing both enterprises to immediately terminate all commercial contracts."),
            "B": ("Tạo ra cam kết gắn kết mạnh mẽ và gia tăng chi phí chuyển đổi (Switching Costs) vì các tài sản này (như dây chuyền chuyên dụng, phần mềm tùy biến riêng) sẽ mất hầu hết giá trị nếu quan hệ bị đổ vỡ.", "Fostering mutual commitment and erecting steep switching barriers because specialized assets (custom tooling, co-developed software) lose value outside the partnership."),
            "C": ("Cho phép một bên đơn phương chiếm đoạt toàn bộ tài sản của bên kia.", "Permitting one partner to unilaterally expropriate the other's corporate assets."),
            "D": ("Làm giảm chất lượng sản phẩm xuống mức tối thiểu.", "Depressing finished product quality metrics to minimum thresholds.")
        },
        "B",
        "Khi một nhà cung ứng đầu tư hàng triệu USD thiết kế khuôn mẫu độc quyền chỉ phục vụ riêng cho một hãng xe, cả hai bên đều có động lực to lớn để duy trì quan hệ lâu dài để thu hồi vốn.",
        "Specific investments function as economic 'hostages' that signal long-term dedication, binding partners together because abandoning the relationship destroys asset value.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 241-246", ["specific-assets", "commitment", "transaction-cost-economics"]
    ),
    (
        "q-08-10", "Collaborative Planning (CPFR)", "medium", "single_choice",
        "Mô hình 'Hoạch định, Dự báo và Bổ sung Hàng hóa Phối hợp' (CPFR - Collaborative Planning, Forecasting, and Replenishment) giữa nhà bán lẻ và nhà sản xuất mang lại lợi ích gì?",
        "In B2B supply chain CRM, what operational benefit does Collaborative Planning, Forecasting, and Replenishment (CPFR) deliver?",
        {
            "A": ("Tăng chi phí lưu kho lên gấp 10 lần để đảm bảo không bao giờ hết hàng.", "Increasing warehouse carrying costs tenfold to guarantee infinite shelf stock."),
            "B": ("Chia sẻ dữ liệu bán hàng thời gian thực từ điểm bán (POS), phối hợp dự báo nhu cầu chính xác, giảm thiểu hiện tượng 'Hiệu ứng Chiếc roi da' (Bullwhip Effect) và tối ưu hóa lượng tồn kho.", "Sharing real-time POS telemetry, coordinating demand forecasts, dampening the Bullwhip Effect, and optimizing inventory levels across the value chain."),
            "C": ("Bắt buộc người tiêu dùng phải thanh toán tiền trước 1 năm.", "Forcing retail consumers to pay one year in advance for packaged goods."),
            "D": ("Đóng cửa toàn bộ các kho phân phối trung gian.", "Shuttering all regional distribution logistics hubs.")
        },
        "B",
        "CPFR kết nối luồng thông tin giữa CRM của nhà sản xuất và hệ thống bán lẻ (như mô hình Walmart và P&G), giúp hàng hóa tự động được bổ sung khi quầy kệ vơi đi.",
        "CPFR replaces speculative guesswork with verified POS consumption data, smoothing order volatility and eliminating stockouts while paring down excess safety stock.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 248-253", ["cpfr", "bullwhip-effect", "supply-chain-integration"]
    ),
    (
        "q-08-11", "Trust and Commitment Model", "hard", "single_choice",
        "Theo mô hình kinh điển Morgan & Hunt (KMV Model) được dẫn trong Baran & Galka, hai biến số trung gian then chốt (Key Mediating Variables) quyết định sự thành công của mối quan hệ B2B là:",
        "According to the classic Morgan & Hunt (1994) KMV framework cited in Baran & Galka, which two Key Mediating Variables govern successful B2B relationship marketing?",
        {
            "A": ("Giá cả (Price) và Quảng cáo (Advertising)", "Price and Advertising"),
            "B": ("Niềm tin (Trust) và Sự cam kết (Relationship Commitment)", "Trust and Relationship Commitment"),
            "C": ("Lợi nhuận ngắn hạn và Số lượng luật sư", "Short-Term Profit and Attorney Counts"),
            "D": ("Độ tuổi của giám đốc và Vốn điều lệ", "Executive Age and Registered Corporate Capital")
        },
        "B",
        "Morgan & Hunt chứng minh rằng Niềm tin và Cam kết là trung tâm của mọi mối quan hệ đối tác bền vững; chúng giúp giảm hành vi cơ hội và thúc đẩy hợp tác tự nguyện.",
        "The KMV model establishes that Trust and Commitment directly mediate cooperation, acquiescence, and low propensity to leave, replacing opportunism with shared purpose.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 240-245", ["kmv-model", "morgan-hunt", "trust-and-commitment"]
    ),
    (
        "q-08-12", "Account-Based Marketing (ABM)", "medium", "single_choice",
        "Chiến lược 'Tiếp thị Dựa trên Tài khoản Trọng điểm' (Account-Based Marketing - ABM) trong B2B CRM được định nghĩa là:",
        "What defines an 'Account-Based Marketing' (ABM) strategy in B2B enterprise CRM?",
        {
            "A": ("Gửi thư quảng cáo đại trà đến hàng triệu địa chỉ email cá nhân ngẫu nhiên trên mạng.", "Blasting generic promotional mass mailings to millions of unverified consumer addresses."),
            "B": ("Phương pháp tiếp cận coi mỗi khách hàng doanh nghiệp mục tiêu như một 'thị trường riêng biệt gồm một khách hàng' (Market of One), phối hợp nhịp nhàng giữa Bán hàng và Marketing để thiết kế thông điệp cá nhân hóa cao cho các bên liên quan trong tài khoản đó.", "Treating individual target enterprise accounts as dedicated markets-of-one, orchestrating sales and marketing to deliver hyper-tailored messaging to specific decision-makers within that firm."),
            "C": ("Chiến dịch giảm giá 50% cho tất cả các đơn hàng thanh toán bằng tiền mặt.", "A blanket 50% discount promotional blitz on all orders settled in physical cash."),
            "D": ("Việc xóa bỏ hoàn toàn phòng marketing và chỉ giữ lại phòng kế toán.", "The complete abolition of the marketing division in favor of accounting.")
        },
        "B",
        "ABM tập trung toàn bộ nguồn lực vào danh sách các tài khoản doanh nghiệp chiến lược (Tier 1 accounts), thiết kế nội dung giải quyết đúng 'nỗi đau' của công ty đó.",
        "ABM flips the traditional broad-reach funnel, concentrating customized campaigns and bespoke content on a pre-selected roster of high-yield corporate accounts.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 254-258", ["abm", "account-based-marketing", "b2b-strategy"]
    ),
    (
        "q-08-13", "Value-in-Use vs Value-in-Exchange", "hard", "single_choice",
        "Theo Lý thuyết Logic Dịch vụ Thống trị (Service-Dominant Logic - Vargo & Lusch) trong B2B CRM, sự chuyển đổi từ 'Giá trị trong Trao đổi' (Value-in-Exchange) sang 'Giá trị trong Sử dụng' (Value-in-Use) có ý nghĩa gì?",
        "Under the Service-Dominant (S-D) Logic framework cited in modern CRM literature, what does the transition from 'Value-in-Exchange' to 'Value-in-Use' signify?",
        {
            "A": ("Doanh nghiệp chỉ quan tâm đến giá trị sản phẩm tại kho hàng trước khi xuất xưởng.", "Enterprises care only about product valuation at warehouse storage prior to shipment."),
            "B": ("Giá trị không nằm ở bản thân sản phẩm vật lý tại thời điểm chuyển giao tiền và hàng (Exchange), mà chỉ thực sự được tạo ra và đo lường trong quá trình khách hàng sử dụng, ứng dụng giải pháp để giải quyết vấn đề thực tế trong hoạt động của họ (Use).", "Value is not embedded in physical goods at transaction cutover (exchange); it is co-created and realized only as the client utilizes the solution in daily operational practice (use)."),
            "C": ("Mọi sản phẩm phải được cho thuê miễn phí mà không được bán đứt.", "All enterprise equipment must be leased for free without asset sales."),
            "D": ("Khách hàng phải trả thêm tiền mỗi lần bật công tắc máy móc.", "Clients must remit micropayments every time machinery power switches are flipped.")
        },
        "B",
        "Value-in-Use đòi hỏi nhà cung cấp B2B phải đồng hành cùng khách hàng trong suốt vòng đời sử dụng, hỗ trợ bảo trì, đào tạo và tối ưu hóa để đảm bảo khách hàng đạt được kết quả mong muốn.",
        "Value-in-Use shifts provider accountability from transactional drop-shipping to lifecycle customer success, ensuring solutions continuously yield operational productivity.",
        "Baran & Galka (2017)", "Chapter 8 & 14", "pp. 242-246, 435-440", ["sd-logic", "value-in-use", "customer-success"]
    ),
    (
        "q-08-14", "B2B Contract Renewal Economics", "medium", "single_choice",
        "Tại sao trong các hợp đồng cung cấp dịch vụ B2B định kỳ (như bảo trì hệ thống hoặc thuê phần mềm SaaS), tỷ lệ gia hạn hợp đồng (Renewal Rate / Gross Retention) lại là chỉ số sinh mệnh của công ty cung cấp?",
        "Why is Contract Renewal Rate (Gross Retention) considered the lifeblood metric for B2B recurring enterprise service providers?",
        {
            "A": ("Vì công ty không bao giờ tuyển dụng thêm nhân viên bán hàng mới.", "Because service providers never hire additional new sales representatives."),
            "B": ("Vì chi phí thu hút một khách hàng doanh nghiệp ban đầu thường rất lớn và phải mất từ 1 đến 2 năm doanh thu định kỳ mới hoàn vốn (CAC Payback Period); nếu khách hàng không gia hạn, công ty sẽ chịu lỗ nặng trên thương vụ đó.", "Because high enterprise CAC means accounts take 12–24 months of subscription margin to reach cash breakeven (CAC Payback); non-renewals represent direct sunk capital losses."),
            "C": ("Vì pháp luật yêu cầu các hợp đồng B2B phải được gia hạn vô điều kiện trong 100 năm.", "Because corporate statutes mandate automatic 100-year contract renewals unconditionally."),
            "D": ("Vì khách hàng cũ không bao giờ cần sự hỗ trợ của đội ngũ kỹ thuật.", "Because renewed accounts never require post-sales technical customer support.")
        },
        "B",
        "Trong mô hình doanh thu định kỳ, lợi nhuận thực sự chỉ xuất hiện từ lần gia hạn thứ 2 và thứ 3 trở đi sau khi đã bù đắp xong chi phí thu hút khách hàng ban đầu.",
        "Enterprise subscription profitability is back-weighted; failing to secure year-two and year-three renewals means the firm exits accounts before recouping heavy upfront CAC.",
        "Baran & Galka (2017)", "Chapter 8 & 10", "pp. 250-255, 315-320", ["renewal-rate", "cac-payback", "b2b-economics"]
    ),
    (
        "q-08-15", "Customer Success Management (CSM)", "medium", "single_choice",
        "Bộ phận 'Quản trị Thành công của Khách hàng' (Customer Success Management - CSM) trong các công ty công nghệ B2B có nhiệm vụ trọng tâm là gì?",
        "What is the core proactive responsibility of a Customer Success Management (CSM) organization in B2B enterprise technology firms?",
        {
            "A": ("Chỉ ngồi chờ khách hàng gọi điện phàn nàn sự cố rồi mới đi sửa chữa.", "Passively waiting for incoming customer complaint tickets before dispatching repair staff."),
            "B": ("Chủ động đồng hành, hướng dẫn khách hàng khai thác tối đa giá trị của phần mềm, giám sát mức độ sử dụng tính năng (Product Adoption), ngăn ngừa nguy cơ rời bỏ sớm và xúc tiến gia hạn, mở rộng hợp đồng.", "Proactively guiding clients to realize maximum software value, monitoring feature telemetry, preempting churn risks, and driving seamless renewals and account expansion."),
            "C": ("Gửi thư đòi nợ và tính lãi phạt chậm thanh toán cho khách hàng.", "Mailing formal debt collection demands and computing overdue interest penalties."),
            "D": ("Tổ chức các sự kiện khiêu vũ cho nhân viên bán hàng.", "Coordinating weekly ballroom dance competitions for sales department staff.")
        },
        "B",
        "CSM khác với Support truyền thống: Support mang tính 'bị động chữa cháy' khi có lỗi; CSM mang tính 'chủ động nuôi dưỡng' giúp khách hàng đạt được mục tiêu kinh doanh của họ.",
        "Unlike reactive technical support that responds to tickets, Customer Success is proactive and outcome-driven, driving continuous product adoption and business value realization.",
        "Baran & Galka (2017)", "Chapter 8 & 14", "pp. 252-257, 438-442", ["csm", "customer-success", "retention"]
    ),
    (
        "q-08-16", "Inter-Firm Information Systems", "hard", "single_choice",
        "Hệ thống Thông tin Liên Doanh nghiệp (Inter-Organizational Information Systems - IOIS / EDI) mang lại lợi thế cạnh tranh gắn kết B2B nhờ cơ chế nào?",
        "How do Inter-Organizational Information Systems (IOIS / EDI) solidify enduring B2B competitive advantage?",
        {
            "A": ("Bằng cách cho phép giám đốc hai công ty nhắn tin tán gẫu miễn phí qua mạng xã hội.", "By allowing corporate executives to exchange casual social media instant messages."),
            "B": ("Tự động hóa luồng trao đổi đơn hàng, vận đơn và hóa đơn điện tử trực tiếp giữa hai hệ thống ERP/CRM, giảm thiểu sai sót do con người, rút ngắn chu kỳ đặt hàng và thiết lập rào cản chuyển đổi kỹ thuật rất cao.", "Automating direct purchase order, dispatch advice, and electronic invoice interchange between partner ERP/CRM databases, slashing cycle times and locking in deep structural integration."),
            "C": ("Bằng cách chia sẻ toàn bộ mật khẩu tài khoản ngân hàng của hai bên.", "By publicly sharing all commercial corporate bank account authorization passwords."),
            "D": ("Bằng cách yêu cầu nhân viên hai bên phải ký cam kết không được kết hôn với người ngoài.", "By mandating that staff across both firms sign non-intermarriage pacts.")
        },
        "B",
        "Khi hệ thống CNTT của hai doanh nghiệp đã được 'hàn gắn' sâu sắc với nhau, chi phí và sự phiền toái để chuyển sang nhà cung ứng khác trở nên vô cùng tốn kém.",
        "Automated inter-firm EDI integration eliminates paper friction and embeds structural switching costs that make supplier replacement operationally disruptive.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 244-249", ["iois", "edi", "structural-bonds", "b2b-integration"]
    ),
    (
        "q-08-17", "Co-Opetition in Platform Ecosystems", "hard", "single_choice",
        "Hiện tượng 'Vừa hợp tác vừa cạnh tranh' (Co-opetition) trong hệ sinh thái số của Amazon (Case GAFA) được minh họa rõ nét nhất qua trường hợp nào?",
        "In the GAFA case analysis, which scenario best illustrates the dynamic of 'Co-opetition' on Amazon's digital platform?",
        {
            "A": ("Amazon hợp nhất toàn bộ các nhà xuất bản sách truyền thống thành một công ty con duy nhất.", "Amazon acquiring all global paper book publishers into a single wholly-owned subsidiary."),
            "B": ("Amazon vừa cung cấp sàn thương mại (Marketplace) và dịch vụ kho vận (FBA) cho các nhà bán hàng bên thứ ba (hợp tác), vừa sử dụng dữ liệu bán chạy của chính các nhà bán hàng này để tung ra các sản phẩm nhãn hàng riêng Amazon Basics cạnh tranh trực tiếp với họ (cạnh tranh).", "Amazon providing marketplace infrastructure and logistics (FBA) to third-party merchants (collaboration), while leveraging aggregate sales data to launch private-label Amazon Basics products competing directly against them (competition)."),
            "C": ("Amazon miễn phí 100% tiền thuê máy chủ AWS cho các đối thủ cạnh tranh đám mây.", "Amazon granting 100% free cloud compute credits to competing public cloud vendors."),
            "D": ("Amazon ngừng hoàn toàn việc giao hàng bằng máy bay và tàu thủy.", "Amazon terminating all air cargo and marine freight transport operations.")
        },
        "B",
        "Co-opetition là bản chất phức tạp của các nền tảng công nghệ: thu hút đối tác tham gia để tạo mạng lưới phong phú, đồng thời khai thác dữ liệu để cạnh tranh lại chính đối tác.",
        "Amazon's platform model embodies co-opetition: nurturing third-party marketplace partners while analyzing merchant demand signals to release competing private-label lines.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 1", "pp. 14-22", ["co-opetition", "amazon-case", "platform-governance"]
    ),
    (
        "q-08-18", "B2B Expansion Metrics", "medium", "single_choice",
        "Chỉ số 'Tỷ lệ Duy trì Doanh thu Ròng' (Net Revenue Retention - NRR) trong quản trị khách hàng B2B đo lường điều gì?",
        "What does Net Revenue Retention (NRR / Net Dollar Retention) measure in B2B customer relationship portfolio management?",
        {
            "A": ("Tổng số tiền thuế doanh nghiệp phải đóng cho nhà nước sau khi trừ khấu hao.", "Total corporate income tax owed to government revenues after deducting depreciation."),
            "B": ("Tỷ lệ phần trăm doanh thu định kỳ được duy trì từ tập khách hàng hiện tại qua một khoảng thời gian (bao gồm cả doanh thu bán thêm/mở rộng trừ đi doanh thu sụt giảm và hủy hợp đồng); NRR > 100% chứng minh doanh nghiệp tự tăng trưởng ngay cả khi không có khách hàng mới.", "The percentage of recurring revenue retained from an existing cohort over a defined timeframe (factoring in expansion/upsell minus contractions and churn); NRR > 100% indicates organic expansion without new logo acquisition."),
            "C": ("Số lượng khách hàng mới đăng ký tài khoản dùng thử miễn phí trong tuần.", "The quantity of prospective trial accounts registered for free trials weekly."),
            "D": ("Tỷ lệ hoàn tiền cho các sản phẩm bị vỡ hỏng trong quá trình vận chuyển.", "The percentage of cash refunded for goods damaged during shipping logistics.")
        },
        "B",
        "NRR là thước đo vàng của mô hình SaaS: nếu NRR đạt 120%, điều đó có nghĩa là dù không tìm được thêm một khách hàng mới nào, doanh thu công ty vẫn tự động tăng trưởng 20% mỗi năm nhờ khách hàng cũ mua thêm.",
        "An NRR exceeding 100% proves product-market fit and powerful net expansion velocity, demonstrating that existing cohort upgrades more than offset attrition losses.",
        "Baran & Galka (2017)", "Chapter 8 & 10", "pp. 252-256, 318-324", ["nrr", "net-revenue-retention", "expansion-revenue"]
    ),
    (
        "q-08-19", "Relationship Termination Ethics", "medium", "single_choice",
        "Khi một khách hàng doanh nghiệp B2B liên tục gây lỗ và không có triển vọng cải thiện, doanh nghiệp nên tiến hành quy trình 'Chấm dứt Mối quan hệ' (Customer Divestment / 'Firing' Customers) như thế nào là chuyên nghiệp nhất?",
        "When a B2B corporate account is permanently unprofitable with no turnaround path, how should professional 'Customer Divestment' ('Firing the Customer') be conducted?",
        {
            "A": ("Đột ngột cắt nguồn điện và ngắt toàn bộ dịch vụ của khách hàng mà không có bất kỳ thông báo nào.", "Abruptly severing service connections and disabling accounts without warning."),
            "B": ("Thông báo minh bạch trước một khoảng thời gian hợp lý, điều chỉnh lại bảng giá phản ánh đúng chi phí phục vụ thực tế (nếu khách chấp nhận thì tiếp tục, nếu từ chối thì tự rời đi), và hỗ trợ bàn giao dữ liệu sang nhà cung ứng khác phù hợp hơn.", "Providing transparent advance notice, repricing contracts to reflect true servicing costs (allowing the client to accept or self-select out), and assisting transition to an alternative vendor."),
            "C": ("Cử bảo vệ đến văn phòng khách hàng để gây rối và xúc phạm nhân viên của họ.", "Dispatching security staff to customer offices to harass personnel."),
            "D": ("Đăng tải toàn bộ hợp đồng mật của khách hàng lên các trang mạng xã hội.", "Publishing confidential customer contractual terms on public internet forums.")
        },
        "B",
        "Sa thải khách hàng phải được thực hiện có đạo đức và chuyên nghiệp; tăng giá theo đúng chi phí phục vụ hoặc giới thiệu đối tác thay thế giúp bảo vệ danh tiếng thương hiệu.",
        "Ethical customer offboarding reprices contracts to restore margin viability while offering graceful transition off-ramps, preserving corporate market reputation.",
        "Baran & Galka (2017)", "Chapter 10", "pp. 336-340", ["customer-divestment", "firing-customers", "ethics"]
    ),
    (
        "q-08-20", "Service Level Agreements in B2B", "medium", "single_choice",
        "Trong các hợp đồng B2B CRM, Cam kết Mức độ Dịch vụ (SLA) về 'Thời gian Phản hồi và Khắc phục Sự cố' (Response & Resolution Time) thường được thiết kế dựa trên tiêu chí nào?",
        "In B2B customer contracts, how are Service Level Agreement (SLA) response and resolution time commitments structured?",
        {
            "A": ("Áp dụng một khung thời gian cố định 48 giờ cho mọi vấn đề bất kể nặng nhẹ.", "Applying a flat 48-hour response window universally to all issues regardless of severity."),
            "B": ("Phân cấp thời gian cam kết dựa trên Mức độ Nghiêm trọng của sự cố (Severity Levels: ví dụ Sev-1 phản hồi trong 15 phút và có mặt trong 1 giờ; Sev-3 phản hồi trong 24 giờ) kết hợp với cấp độ phân hạng của khách hàng (Tier).", "Tiered response times based on incident severity (e.g., Sev-1 immediate response within 15 minutes; Sev-3 within 24 hours), cross-indexed against account priority tier."),
            "C": ("Chỉ phản hồi khi ban giám đốc của khách hàng trực tiếp gửi công văn.", "Responding solely when the client board of directors submits formal petitions."),
            "D": ("Không cam kết bất kỳ thời gian cụ thể nào và tùy thuộc vào sự thuận tiện của kỹ sư.", "Offering zero time commitments, subject purely to individual engineer availability.")
        },
        "B",
        "SLA theo mức độ nghiêm trọng đảm bảo các sự cố tê liệt hệ thống được ưu tiên giải quyết khẩn cấp với sự huy động tối đa nguồn lực.",
        "Severity-tiered SLAs align rapid-response escalation workflows with real business impact, mitigating catastrophic downtime for premier client operations.",
        "Baran & Galka (2017)", "Chapter 8", "pp. 248-252", ["sla", "incident-management", "b2b-contracts"]
    )
]

for item in e8:
    questions_batch3.append(make_q(
        item[0], "EXAM-08", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

print(f"Total questions generated in batch 3: {len(questions_batch3)}")

with open(Path(r"C:\Kiến thức cần học\CRM\output\scratch\q_batch3.json"), "w", encoding="utf-8") as f:
    json.dump(questions_batch3, f, ensure_ascii=False, indent=2)
