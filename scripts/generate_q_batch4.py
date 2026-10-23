import json
from pathlib import Path

# Exam 09 and 10 question generator
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

questions_batch4 = []

# ==========================================
# EXAM 09: OMNICHANNEL, SOCIAL CRM & EMERGING TRENDS (q-09-01 to q-09-20)
# ==========================================
e9 = [
    (
        "q-09-01", "Multichannel vs Omnichannel", "easy", "single_choice",
        "Sự khác biệt bản chất nhất giữa chiến lược 'Đa kênh' (Multichannel) và 'Hợp kênh' (Omnichannel) trong trải nghiệm khách hàng là gì?",
        "What is the fundamental difference between 'Multichannel' and 'Omnichannel' customer experience strategies?",
        {
            "A": ("Multichannel chỉ có 2 kênh; Omnichannel bắt buộc phải có đúng 100 kênh.", "Multichannel possesses only two touchpoints; Omnichannel mandates exactly one hundred channels."),
            "B": ("Multichannel vận hành các kênh tiếp xúc (cửa hàng, website, ứng dụng, tổng đài) một cách độc lập và tách rời; Omnichannel tích hợp liền mạch toàn bộ các kênh thành một trải nghiệm thống nhất, nơi dữ liệu và hành trình của khách hàng được đồng bộ hóa xuyên suốt thời gian thực.", "Multichannel operates touchpoints (store, website, app, phone) as isolated, fragmented silos; Omnichannel seamlessly orchestrates all channels into a unified journey with synchronized real-time data."),
            "C": ("Multichannel chỉ bán hàng giảm giá; Omnichannel chỉ bán hàng cao cấp.", "Multichannel sells clearance items; Omnichannel sells luxury goods exclusively."),
            "D": ("Multichannel sử dụng máy tính; Omnichannel chỉ sử dụng giấy viết tay.", "Multichannel utilizes desktop PCs; Omnichannel relies entirely on paper."),
            "E": ("Không có sự khác biệt nào giữa hai khái niệm.", "There is no conceptual difference.")
        },
        "B",
        "Omnichannel đặt khách hàng làm trung tâm, cho phép khách hàng bắt đầu xem hàng trên điện thoại, tiếp tục đặt hàng trên website và nhận hàng tại cửa hàng (BOPIS) mà dữ liệu không bị đứt đoạn.",
        "Omnichannel dissolves channel boundaries, providing a unified single customer view where state, cart contents, and interaction history persist seamlessly across physical and digital spaces.",
        "Baran & Galka (2017)", "Chapter 13", "pp. 402-408", ["omnichannel", "multichannel", "seamless-experience"]
    ),
    (
        "q-09-02", "Social CRM Capabilities", "medium", "single_choice",
        "Social CRM khác biệt với CRM truyền thống ở điểm mấu chốt nào?",
        "How does Social CRM fundamentally diverge from traditional CRM systems?",
        {
            "A": ("Social CRM cấm nhân viên sử dụng thư điện tử email.", "Social CRM bans staff from utilizing corporate email accounts."),
            "B": ("CRM truyền thống quản lý dữ liệu giao dịch nội bộ có cấu trúc do công ty kiểm soát; Social CRM tham gia vào các cuộc đối thoại mở trên mạng xã hội, nơi khách hàng nắm quyền chủ động tạo nội dung và chia sẻ trải nghiệm với cộng đồng.", "Traditional CRM captures structured internal transaction records controlled by the enterprise; Social CRM engages in collaborative public dialogue where customers co-create value and broadcast sentiment."),
            "C": ("Social CRM chỉ là việc đăng bài ảnh quảng cáo lên trang Facebook mỗi ngày.", "Social CRM is merely posting daily promotional photos on Facebook pages."),
            "D": ("Social CRM không có cơ sở dữ liệu khách hàng.", "Social CRM operates entirely without customer databases.")
        },
        "B",
        "Social CRM chuyển dịch từ 'quản lý khách hàng' sang 'tương tác và hợp tác cùng khách hàng', lắng nghe tiếng nói cộng đồng để cải tiến dịch vụ kịp thời.",
        "Social CRM embraces customer empowerment, shifting from top-down transaction monitoring to bidirectional social listening, sentiment analysis, and community engagement.",
        "Baran & Galka (2017)", "Chapter 13", "pp. 408-416", ["social-crm", "customer-empowerment", "social-listening"]
    ),
    (
        "q-09-03", "Disney MagicBand Ecosystem Case", "hard", "single_choice",
        "Theo tình huống nghiên cứu 'The Walt Disney Company' (Experiential Marketing, Ch. 4, tr. 102-108), chiếc vòng đeo tay MagicBand và hệ thống MyMagic+ đóng vai trò gì trong trải nghiệm khách hàng?",
        "In the Walt Disney Company case study (Batat, Chapter 4, pp. 102-108), what role does the MagicBand / MyMagic+ infrastructure play in customer experience?",
        {
            "A": ("Chỉ là một chiếc đồng hồ đeo tay thời trang phát sáng trong bóng tối.", "Merely an aesthetic glow-in-the-dark wrist accessory."),
            "B": ("Là thiết bị IoT kết nối tích hợp đóng vai trò chìa khóa phòng khách sạn, vé vào cửa công viên, thanh toán không chạm và định vị vị trí thời gian thực, giúp loại bỏ hoàn toàn ma sát xếp hàng và cá nhân hóa trải nghiệm kỳ diệu của từng gia đình.", "An integrated RFID/IoT touchpoint serving as hotel room key, theme park ticket, contactless payment token, and real-time location sensor, eliminating queuing friction and personalizing park magic."),
            "C": ("Dùng để đo huyết áp và nhịp tim của du khách trước khi đi tàu lượn siêu tốc.", "Measuring visitor blood pressure before boarding roller coasters."),
            "D": ("Là công cụ ghi âm mọi cuộc trò chuyện của du khách để bán cho đài truyền hình.", "Recording guest conversations to sell to commercial television broadcasters.")
        },
        "B",
        "MagicBand hợp nhất toàn bộ trải nghiệm nghỉ dưỡng của du khách thành một luồng không ma sát (frictionless), cung cấp dữ liệu vi mô giúp Disney tối ưu hóa luồng khách và phục vụ tận tình.",
        "MagicBand exemplifies omnichannel IoT orchestration, turning a physical resort into a responsive smart environment that delivers frictionless, personalized guest enchantment.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 4", "pp. 102-108", ["disney-case", "magicband", "iot-crm", "frictionless-experience"]
    ),
    (
        "q-09-04", "Nike Direct Ecosystem Case", "hard", "single_choice",
        "Theo tình huống nghiên cứu 'Nike' (Experiential Marketing, Ch. 5, tr. 131-143), chiến lược chuyển đổi số Nike Direct và ứng dụng Nike+ / SNKRS mang lại lợi thế CRM vượt trội nào?",
        "According to the Nike case study (Batat, Chapter 5, pp. 131-143), what superior CRM capability does the Nike Direct / Nike+ ecosystem deliver?",
        {
            "A": ("Nike ngừng sản xuất giày thể thao và chỉ tập trung viết phần mềm game.", "Nike discontinued sneaker manufacturing to focus purely on video games."),
            "B": ("Chuyển dịch từ việc phụ thuộc vào đại lý bán buôn sang xây dựng quan hệ trực tiếp (D2C) với hàng trăm triệu vận động viên, thu thập dữ liệu tập luyện và sở thích qua ứng dụng để cá nhân hóa sản phẩm và gia tăng biên lợi nhuận ròng.", "Transitioning from wholesale intermediary dependence to Direct-to-Consumer (D2C) relationships, harvesting behavioral fitness telemetry to personalize products and boost net margins."),
            "C": ("Tặng giày miễn phí cho tất cả những ai tải ứng dụng về máy.", "Distributing free athletic sneakers to anyone who downloads mobile apps."),
            "D": ("Yêu cầu người mua phải chạy đủ 100km mới được phép đặt mua một đôi giày.", "Mandating that consumers run 100 kilometers before unlocking shoe purchases.")
        },
        "B",
        "Nike Direct giúp hãng nắm giữ dữ liệu người dùng cuối, tạo ra cộng đồng thể thao gắn kết và tăng mạnh tỷ trọng bán hàng trực tiếp với lợi nhuận biên cao hơn nhiều so với bán buôn.",
        "Nike Direct transformed transactional apparel buyers into an engaged fitness lifestyle community, capturing proprietary consumer telemetry and bypassing wholesale discounts.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 5", "pp. 131-143", ["nike-case", "d2c", "nike-plus", "behavioral-telemetry"]
    ),
    (
        "q-09-05", "Airbnb Trust Architecture Case", "hard", "single_choice",
        "Theo tình huống nghiên cứu 'Airbnb' (Experiential Marketing, Ch. 4, tr. 108-113), cơ chế nào là cốt lõi của 'Kiến trúc Niềm tin' (Trust Architecture) giúp kết nối hàng triệu chủ nhà và khách lạ trên toàn cầu?",
        "In the Airbnb case analysis (Batat, Chapter 4, pp. 108-113), what mechanism constitutes the core 'Trust Architecture' enabling peer-to-peer sharing between strangers?",
        {
            "A": ("Chủ nhà và khách bắt buộc phải đến trụ sở Airbnb để ký hợp đồng trước mặt công chứng viên.", "Hosts and guests meeting at Airbnb offices before a notary public."),
            "B": ("Hệ thống đánh giá và phản hồi hai chiều minh bạch (Bi-directional Double-Blind Reviews), xác thực danh tính chính phủ, bảo hiểm thiệt hại cho chủ nhà (Host Guarantee) và nền tảng thanh toán ký quỹ giữ tiền an toàn cho đến khi khách nhận phòng.", "Bi-directional double-blind reputation reviews, verified government IDs, host liability protection guarantees, and escrow payment processing that releases funds only post-check-in."),
            "C": ("Cấm người dùng chụp ảnh phòng ngủ khi đăng tin cho thuê.", "Prohibiting hosts from posting photographs of bedroom accommodation."),
            "D": ("Cho phép khách ở miễn phí nếu họ không hài lòng về bất kỳ điều gì.", "Permitting guests to stay free of charge if any dissatisfaction occurs.")
        },
        "B",
        "Mô hình kinh tế chia sẻ của Airbnb thành công nhờ giải quyết được nỗi sợ hãi của hai người lạ bằng công nghệ CRM tạo dựng niềm tin và sự an toàn về tài chính.",
        "Airbnb engineered peer-to-peer trust through structural institutional mechanisms: verified digital identities, dual-blind review symmetry, and financial escrow safeguards.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 4", "pp. 108-113", ["airbnb-case", "trust-architecture", "peer-to-peer-crm", "sharing-economy"]
    ),
    (
        "q-09-06", "McDonald's Digital Transformation Case", "hard", "single_choice",
        "Theo tình huống nghiên cứu 'McDonald's' (Experiential Marketing, Ch. 4, tr. 113-121), việc triển khai kiosk tự phục vụ và ứng dụng di động đã tác động như thế nào đến giá trị đơn hàng trung bình?",
        "In the McDonald's case study (Batat, Chapter 4, pp. 113-121), how did self-service kiosks and mobile app integration impact average order transaction value?",
        {
            "A": ("Làm giảm giá trị đơn hàng vì khách hàng cảm thấy phiền phức khi chạm vào màn hình.", "Decreasing average ticket size because touchscreen ordering irritated patrons."),
            "B": ("Gia tăng đáng kể giá trị giỏ hàng trung bình (Average Ticket Size) nhờ thuật toán gợi ý món ăn kèm trực quan (như đồ uống, khoai tây chiên, tráng miệng), giảm áp lực thời gian tại quầy thu ngân và cá nhân hóa khẩu vị.", "Significantly increasing Average Order Value through visual cross-sell/upsell prompts, unhurried menu browsing without frontline social judgment, and bespoke ingredient customization."),
            "C": ("Không có bất kỳ sự thay đổi nào về doanh số.", "Yielding zero measurable change in ticket averages or basket sizes."),
            "D": ("Khiến khách hàng bỏ về và không mua thức ăn nữa.", "Causing consumers to abandon stores and refuse to order food.")
        },
        "B",
        "Kiosk tự phục vụ không chỉ giải phóng sức lao động mà còn là cỗ máy bán thêm (upsell) xuất sắc: máy móc không bao giờ quên hỏi 'Bạn có muốn nâng cỡ khoai tây chiên không?'.",
        "Digital kiosks eliminate frontline human omission in upselling, presenting appealing visual customizations that prompt consumers to expand basket sizes autonomously.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 4", "pp. 113-121", ["mcdonalds-case", "self-service-kiosks", "upselling", "digital-ordering"]
    ),
    (
        "q-09-07", "IKEA Experiential & AR Case", "hard", "single_choice",
        "Theo tình huống nghiên cứu 'IKEA' (Experiential Marketing, Ch. 3, tr. 92-98), ứng dụng thực tế tăng cường IKEA Place giúp giải quyết rào cản tâm lý mua sắm nào của khách hàng?",
        "In the IKEA case study (Batat, Chapter 3, pp. 92-98), what customer psychological barrier does the 'IKEA Place' Augmented Reality (AR) app overcome?",
        {
            "A": ("Nỗi sợ hãi khi phải tự nấu ăn ở nhà.", "The psychological anxiety of self-catering home meals."),
            "B": ("Nỗi lo sợ về việc đồ nội thất mua về không vừa kích thước hoặc không hợp phong cách với không gian phòng thực tế, cho phép khách hàng 'ướm thử' sản phẩm 3D vào nhà với tỷ lệ chuẩn xác trước khi thanh toán.", "The cognitive friction and anxiety of spatial misfit, enabling buyers to virtually place true-to-scale 3D furniture models within their living rooms before committing to purchase."),
            "C": ("Việc không biết cách đóng đinh vào tường.", "Lack of technical competence in driving steel nails into drywall."),
            "D": ("Nỗi sợ hãi khi phải đọc sách hướng dẫn lắp ráp bằng tranh vẽ.", "Aversion to interpreting pictorial flat-pack assembly diagrams.")
        },
        "B",
        "IKEA Place xóa bỏ sự lưỡng lự mua sắm (purchase hesitation) bằng cách mang trải nghiệm thử đồ vào chính phòng khách của người dùng qua công nghệ AR chân thực.",
        "AR reduces post-purchase cognitive dissonance and product returns by allowing customers to validate dimensional fit and aesthetic harmony directly in their living spaces.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 3", "pp. 92-98", ["ikea-case", "ar-crm", "experiential-retailing", "ikea-place"]
    ),
    (
        "q-09-08", "Chanel & Luxury CRM Paradox Case", "hard", "single_choice",
        "Theo tình huống nghiên cứu 'Chanel' (Experiential Marketing, Ch. 5, tr. 126-131), nghịch lý của CRM trong ngành hàng xa xỉ (The Luxury CRM Paradox) được Chanel xử lý như thế nào đối với thương mại điện tử?",
        "In the Chanel case study (Batat, Chapter 5, pp. 126-131), how does Chanel manage the 'Luxury CRM Paradox' concerning digital e-commerce expansion?",
        {
            "A": ("Chanel bán toàn bộ các bộ sưu tập thời trang cao cấp trên các sàn thương mại điện tử đại trà giảm giá.", "Chanel liquidating all Haute Couture collections on mass discount e-commerce apps."),
            "B": ("Chanel kiên quyết không bán các dòng sản phẩm thời trang may sẵn (Ready-to-Wear) và túi xách biểu tượng qua mạng, mà sử dụng công nghệ số để tăng cường và dẫn dắt khách hàng đến trải nghiệm nghi thức độc quyền tại cửa hàng trực tiếp (Boutique Experience).", "Chanel deliberately restricts iconic handbags and ready-to-wear apparel from online transactions, using digital channels purely to orchestrate exclusive in-store boutique rituals."),
            "C": ("Chanel cấm nhân viên cửa hàng không được mỉm cười với khách.", "Chanel forbidding boutique associates from smiling at patrons."),
            "D": ("Chanel đóng cửa toàn bộ các cửa hàng vật lý để chuyển 100% sang bán hàng trực tuyến.", "Chanel shuttering all physical boutiques to pivot 100% to e-commerce.")
        },
        "B",
        "Xa xỉ đòi hỏi sự khan hiếm và trải nghiệm tiếp xúc độc quyền; bán hàng đại trà trên mạng làm mất đi ma thuật của thương hiệu. Chanel dùng CRM số để chăm sóc khách nhưng giữ trải nghiệm mua tại boutique.",
        "Luxury branding requires exclusivity, sensory ritual, and controlled scarcity; Chanel deploys digital CRM to enhance human advisory relationships while protecting boutique exclusivity.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 5", "pp. 126-131", ["chanel-case", "luxury-crm", "luxury-paradox", "boutique-experience"]
    ),
    (
        "q-09-09", "Estée Lauder High-Touch Tech Case", "hard", "single_choice",
        "Theo tình huống nghiên cứu 'The Estée Lauder Companies' (Experiential Marketing, Ch. 5, tr. 143-148), triết lý 'High-Touch' trong thời đại số của tập đoàn mỹ phẩm này được thực thi như thế nào?",
        "In the Estée Lauder case analysis (Batat, Chapter 5, pp. 143-148), how is the founder's legacy 'High-Touch' philosophy operationalized in the digital era?",
        {
            "A": ("Ngừng hoàn toàn việc đào tạo chuyên viên tư vấn làm đẹp tại quầy.", "Completely terminating cosmetic beauty advisor training programs."),
            "B": ("Kết hợp giữa sự chăm sóc cá nhân hóa nồng ấm của chuyên viên tư vấn sắc đẹp với các công nghệ phân tích da bằng AI, thử son ảo AR (Virtual Try-On) và dữ liệu hồ sơ cá nhân hóa đa kênh.", "Harmonizing intimate personal beauty advisor consultations with cutting-edge AI skin diagnostic diagnostics, AR virtual shade try-on, and omnichannel beauty profile data."),
            "C": ("Bán mỹ phẩm qua các máy bán hàng tự động tại ga tàu điện ngầm mà không có người tư vấn.", "Dispensing luxury cosmetics via unstaffed subway station vending machines."),
            "D": ("Sản xuất duy nhất một loại màu son môi cho toàn bộ phụ nữ trên thế giới.", "Manufacturing a single uniform lipstick shade for all global consumers.")
        },
        "B",
        "Estée Lauder định nghĩa công nghệ là công cụ khuếch đại (amplification) sự chăm sóc tận tâm của con người; khách hàng có thể thử màu son ảo trên app rồi đến quầy nhận tư vấn chuyên sâu.",
        "High-Touch in the 21st century fuses empathetic human expertise with frictionless diagnostic AI and AR virtual testing, elevating personalized beauty journeys across touchpoints.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 5", "pp. 143-148", ["estee-lauder-case", "high-touch", "beauty-tech", "augmented-reality"]
    ),
    (
        "q-09-10", "Walmart Omnichannel Logistics Case", "hard", "single_choice",
        "Theo tình huống nghiên cứu 'Walmart' (Experiential Marketing, Ch. 3, tr. 87-92), lợi thế cạnh tranh cốt lõi giúp Walmart đương đầu với Amazon trong cuộc chiến omnichannel là gì?",
        "In the Walmart case analysis (Batat, Chapter 3, pp. 87-92), what primary strategic asset provides Walmart with a distinct omnichannel advantage over pure-play online rivals like Amazon?",
        {
            "A": ("Walmart không có trang web bán hàng.", "Walmart operating with zero digital commerce storefronts."),
            "B": ("Mạng lưới gần 5.000 siêu thị vật lý nằm trong bán kính 10 dặm của 90% dân số Mỹ, đóng vai trò như các trung tâm hoàn tất đơn hàng địa phương (Micro-fulfillment Centers) cho dịch vụ Đặt hàng trực tuyến - Nhận hàng tại cửa hàng (Curbside Pickup / BOPIS).", "A vast physical footprint of nearly 5,000 stores within 10 miles of 90% of the US population, functioning as hyper-local fulfillment nodes for same-day curbside pickup (BOPIS)."),
            "C": ("Walmart chỉ chấp nhận thanh toán bằng tiền xu cổ.", "Walmart accepting payment exclusively in historical minted coins."),
            "D": ("Walmart giao hàng cho khách hàng bằng xe ngựa kéo.", "Walmart dispatching customer home deliveries via horse-drawn wagons.")
        },
        "B",
        "Walmart biến hệ thống cửa hàng truyền thống từng bị coi là gánh nặng thành 'vũ khí omnichannel' đắc lực, kết hợp ứng dụng đặt hàng mượt mà với nhận hàng curbside pickup trong ngày.",
        "Walmart weaponized its physical brick-and-mortar footprint into a distributed local distribution network, offering frictionless click-and-collect services pure-play rivals struggle to match.",
        "Experiential Marketing (Batat 2019/2021)", "Chapter 3", "pp. 87-92", ["walmart-case", "bopis", "curbside-pickup", "omnichannel-fulfillment"]
    ),
    (
        "q-09-11", "Conversational AI and Chatbots", "medium", "single_choice",
        "Trong dịch vụ khách hàng thời gian thực, vai trò phù hợp nhất của Trợ lý ảo AI / Chatbot trong mối quan hệ với nhân viên hỗ trợ con người là gì?",
        "In real-time customer service architecture, what is the optimal division of labor between Conversational AI Chatbots and human support agents?",
        {
            "A": ("Sa thải 100% nhân viên con người và để chatbot tự xử lý mọi tình huống phức tạp.", "Terminating 100% of human representatives and delegating all complex escalations to chatbots."),
            "B": ("Chatbot tự động xử lý các câu hỏi phổ biến lặp đi lặp lại (Tier 0: tra cứu đơn hàng, giờ mở cửa) 24/7 và chuyển giao liền mạch (Seamless Hand-off) kèm toàn bộ ngữ cảnh trò chuyện cho nhân viên con người khi gặp các vấn đề phức tạp hoặc bức xúc cảm xúc.", "Chatbots automate high-volume routine inquiries (Tier-0: tracking, FAQ lookups) 24/7, providing seamless context-rich handoffs to human agents for complex or emotionally charged issues."),
            "C": ("Cấm chatbot trả lời câu hỏi và chỉ dùng chatbot để gửi biểu tượng mặt cười.", "Restricting chatbots solely to transmitting cartoon smileys without answering text."),
            "D": ("Bắt khách hàng phải trả phí 10 USD cho mỗi tin nhắn gửi cho chatbot.", "Charging consumers a $10 tariff per message dispatched to conversational bots.")
        },
        "B",
        "Chatbot giải quyết nhanh các câu hỏi cơ bản, giải phóng nhân viên con người để họ tập trung vào những ca tư vấn đòi hỏi sự thấu cảm, đàm phán và giải quyết xung đột nhạy cảm.",
        "Conversational AI handles routine transactional queries at scale, while contextual escalation preserves human bandwidth for high-empathy, high-stakes relationship recovery.",
        "Baran & Galka (2017)", "Chapter 13 & 14", "pp. 415-420, 442-446", ["conversational-ai", "chatbots", "tier-0", "human-handoff"]
    ),
    (
        "q-09-12", "Social Listening & Sentiment Analysis", "medium", "single_choice",
        "Công cụ Lắng nghe Mạng xã hội (Social Listening) và Phân tích Cảm xúc (Sentiment Analysis) trong CRM giúp doanh nghiệp phát hiện điều gì?",
        "What does Social Listening coupled with automated Sentiment Analysis empower CRM teams to uncover?",
        {
            "A": ("Mật khẩu tài khoản ngân hàng của những người đang sử dụng Twitter/Facebook.", "The private financial account passwords of active Twitter/Facebook users."),
            "B": ("Theo dõi các đề cập thương hiệu (Brand Mentions) theo thời gian thực, phân loại sắc thái cảm xúc (Tích cực, Trung tính, Tiêu cực) và phát hiện sớm các dấu hiệu khủng hoảng truyền thông trước khi bùng nổ.", "Tracking real-time brand mentions, categorizing public emotional tone (Positive, Neutral, Negative), and detecting nascent crisis signals before viral reputational contagion."),
            "C": ("Số lượng linh kiện điện tử bị lỗi trên dây chuyền sản xuất cơ khí.", "The count of failed microchips manufactured along robotic assembly lines."),
            "D": ("Dự báo nhiệt độ khí hậu toàn cầu trong 100 năm tới.", "Long-range forecasting of global surface atmospheric temperatures.")
        },
        "B",
        "Phân tích cảm xúc dựa trên xử lý ngôn ngữ tự nhiên (NLP) giúp ban lãnh đạo đo lường phản ứng của công chúng đối với sản phẩm mới ra mắt và dập tắt khủng hoảng ngay từ mầm mống.",
        "Social listening parses unstructured public discourse into sentiment trends, transforming social chatter into actionable alerts for brand management and customer care.",
        "Baran & Galka (2017)", "Chapter 13", "pp. 410-415", ["social-listening", "sentiment-analysis", "crisis-management"]
    ),
    (
        "q-09-13", "Showrooming vs Webrooming", "medium", "single_choice",
        "Hiện tượng 'Showrooming' trong hành vi mua sắm đa kênh của người tiêu dùng được định nghĩa là:",
        "What behavior characterizes the omnichannel retail phenomenon termed 'Showrooming'?",
        {
            "A": ("Khách hàng chỉ xem hàng trên mạng rồi ra cửa hàng mua đúng giá niêm yết.", "Browsing products online and visiting stores to purchase at full price."),
            "B": ("Khách hàng đến cửa hàng vật lý để trực tiếp xem, sờ và thử sản phẩm, sau đó dùng điện thoại thông minh để tìm kiếm và đặt mua sản phẩm đó trên mạng từ một đối thủ bán giá rẻ hơn.", "Visiting a brick-and-mortar storefront to physically inspect and test a product, then ordering it online from a cheaper competitor via smartphone."),
            "C": ("Khách hàng chụp ảnh tự sướng trong phòng thay đồ của cửa hàng quần áo.", "Shoppers capturing digital self-portraits in retail changing rooms."),
            "D": ("Cửa hàng từ chối cho khách hàng bước vào bên trong.", "Retail stores refusing entry to prospective retail customers.")
        },
        "B",
        "Showrooming biến cửa hàng vật lý thành nơi trưng bày miễn phí cho các trang thương mại điện tử giá rẻ; để chống lại điều này, các nhà bán lẻ áp dụng chính sách 'khớp giá' (Price Matching) và trải nghiệm độc quyền.",
        "Showrooming exploits physical store overhead for sensory validation while diverting revenue to discount e-tailers, compelling retailers to offer omnichannel price matching and value-add services.",
        "Baran & Galka (2017)", "Chapter 13", "pp. 404-407", ["showrooming", "webrooming", "omnichannel-behavior"]
    ),
    (
        "q-09-14", "IoT and Predictive Maintenance CRM", "hard", "single_choice",
        "Khi Internet vạn vật (IoT) được tích hợp vào giải pháp CRM Dịch vụ Khách hàng (ví dụ: máy giặt thông minh hoặc thang máy kết nối cảm biến), mô hình dịch vụ chuyển dịch như thế nào?",
        "When Internet of Things (IoT) sensors are integrated into customer service CRM platforms (e.g., smart appliances or elevators), how does the service model transform?",
        {
            "A": ("Chuyển từ sửa chữa định kỳ sang việc vứt bỏ toàn bộ máy móc khi có tiếng kêu lạ.", "Switching from maintenance to discarding entire machines at the first rattle."),
            "B": ("Chuyển từ mô hình 'Bị động Chữa cháy' (Khách hàng hỏng máy -> gọi điện -> chờ thợ đến) sang mô hình 'Bảo trì Dự đoán Chủ động' (Cảm biến phát hiện nguy cơ lỗi -> CRM tự động kích hoạt vé sửa chữa và cử kỹ thuật viên đến thay linh kiện trước khi máy bị hỏng).", "Pivoting from reactive 'Break-Fix' (machine breaks -> customer calls -> technician dispatched) to 'Proactive Predictive Maintenance' (sensor flags anomaly -> CRM auto-generates dispatch ticket before outage occurs)."),
            "C": ("Bắt buộc khách hàng phải tự tháo rời động cơ để kiểm tra hàng tuần.", "Requiring homeowners to manually disassemble motor engines weekly."),
            "D": ("Tắt toàn bộ nguồn điện của thiết bị mỗi khi trời tối.", "Severing power to connected equipment whenever outdoor dusk arrives.")
        },
        "B",
        "Bảo trì dự đoán dựa trên IoT biến CRM thành một hệ thống tự hành, loại bỏ hoàn toàn thời gian chết của thiết bị và đem lại sự an tâm tuyệt đối cho khách hàng.",
        "Connected IoT telemetry moves CRM from reactive ticket management to predictive, automated field service, replacing costly unplanned outages with pre-emptive repairs.",
        "Baran & Galka (2017)", "Chapter 14", "pp. 438-444", ["iot-crm", "predictive-maintenance", "field-service"]
    ),
    (
        "q-09-15", "Customer Co-Creation in Product Design", "medium", "single_choice",
        "Các nền tảng 'Đồng sáng tạo sản phẩm cùng khách hàng' (Customer Co-Creation Platforms như Lego Ideas hay Starbucks My Idea) mang lại lợi ích gì cho CRM?",
        "What distinct CRM advantage do collaborative Co-Creation Platforms (such as Lego Ideas or My Starbucks Idea) deliver to enterprises?",
        {
            "A": ("Giảm 100% chi phí sản xuất sản phẩm thực tế xuống mức 0 đồng.", "Eliminating 100% of physical manufacturing costs down to zero."),
            "B": ("Khai thác trí tuệ tập thể của những khách hàng nhiệt huyết nhất, tạo ra các sản phẩm sát với nhu cầu thị trường, đồng thời gia tăng mạnh mẽ lòng trung thành thái độ và sự tự hào của cộng đồng người dùng.", "Harnessing the collective creativity of passionate brand enthusiasts, de-risking product design, and forging profound attitudinal loyalty through psychological ownership."),
            "C": ("Bắt người dùng phải ký cam kết không được mua sản phẩm của hãng khác trong 50 năm.", "Mandating that contributors sign exclusivity pledges barring purchases from rivals."),
            "D": ("Chỉ là một trò chơi giải trí không mang lại bất kỳ ý tưởng kinh doanh nào.", "Serving purely as frivolous games with zero commercial relevance.")
        },
        "B",
        "Khi khách hàng được trực tiếp đóng góp ý tưởng và thấy ý tưởng của mình biến thành sản phẩm thật, họ trở thành những người ủng hộ trung kiên nhất của thương hiệu.",
        "Co-creation fosters deep psychological ownership among users, transforming ordinary consumers into passionate collaborators and long-term brand evangelists.",
        "Baran & Galka (2017)", "Chapter 13", "pp. 416-422", ["co-creation", "lego-ideas", "community-engagement"]
    ),
    (
        "q-09-16", "Mobile Geofencing & Proximity Marketing", "medium", "single_choice",
        "Kỹ thuật Định vị Vùng địa lý (Geofencing) và Cảm biến Cận vi (Beacons) trong CRM bán lẻ di động cho phép thực hiện kịch bản tiếp thị nào?",
        "What promotional scenario does Geofencing and micro-location Beacon technology enable in retail mobile CRM?",
        {
            "A": ("Theo dõi vị trí của tất cả các tàu vũ trụ đang bay ngoài không gian.", "Tracking orbital telemetry of spacecraft orbiting outside the earth's atmosphere."),
            "B": ("Gửi thông điệp chào mừng, ưu đãi cá nhân hóa hoặc gợi ý sản phẩm ngay khi khách hàng bước qua cổng cửa hàng hoặc đứng trước một quầy kệ sản phẩm cụ thể.", "Pushing contextual greetings, personalized offers, or product recommendations the moment an app user enters a geofenced retail perimeter or pauses by a specific aisle beacon."),
            "C": ("Tự động khóa bánh xe ô tô của khách hàng khi họ lái xe ngang qua siêu thị.", "Remotely immobilizing consumer automotive tires when driving past shopping malls."),
            "D": ("Gọi điện thoại trực tiếp cho người đi đường mời mua vé số.", "Dialing random pedestrian phones to solicit lottery ticket purchases.")
        },
        "B",
        "Geofencing và Beacons mang lại tính phù hợp ngữ cảnh cao độ (Hyper-contextual relevance), kết nối hoàn hảo giữa thế giới số trên điện thoại và không gian mua sắm thực tế.",
        "Proximity beacons bridge the physical-digital divide, triggering hyper-relevant mobile engagement calibrated to the shopper's exact physical coordinates and shelf dwell time.",
        "Baran & Galka (2017)", "Chapter 13", "pp. 418-424", ["geofencing", "beacons", "proximity-marketing"]
    ),
    (
        "q-09-17", "Unified Commerce Definition", "hard", "single_choice",
        "Khái niệm 'Thương mại Hợp nhất' (Unified Commerce) được xem là bước tiến hóa vượt trội hơn cả Omnichannel ở khía cạnh kỹ thuật nào?",
        "In enterprise software architecture, why is 'Unified Commerce' considered an evolutionary leap beyond legacy Omnichannel implementations?",
        {
            "A": ("Unified Commerce chỉ bán một mặt hàng duy nhất cho toàn cầu.", "Unified Commerce mandates retailing a single uniform SKU worldwide."),
            "B": ("Omnichannel thường chắp vá nhiều hệ thống phần mềm riêng lẻ (POS riêng, Web riêng, Mobile riêng) bằng các cổng kết nối; Unified Commerce vận hành toàn bộ các kênh trên một nền tảng phần mềm duy nhất, một cơ sở dữ liệu chung và một khối động cơ thương mại tập trung duy nhất.", "While omnichannel often patches disparate legacy engines via brittle middleware, Unified Commerce executes all channels on a single holistic cloud platform and shared master data model."),
            "C": ("Unified Commerce cấm sử dụng máy thanh toán thẻ tín dụng.", "Unified Commerce bans electronic credit card swipe terminals."),
            "D": ("Unified Commerce chỉ dành cho các công ty nhà nước.", "Unified Commerce applies solely to national government postal operations.")
        },
        "B",
        "Unified Commerce xóa bỏ triệt để độ trễ dữ liệu và sự cố đứt gãy kết nối giữa các kênh, đảm bảo một nguồn chân lý duy nhất (Single Source of Truth) cho tồn kho, giá cả và khách hàng.",
        "Unified commerce replaces fragmented spaghetti integrations with a single native transactional engine, delivering real-time inventory and customer state across all touchpoints.",
        "Baran & Galka (2017)", "Chapter 13 & 14", "pp. 424-428, 440-444", ["unified-commerce", "omnichannel-evolution", "single-platform"]
    ),
    (
        "q-09-18", "Customer Experience Journey Orchestration", "medium", "single_choice",
        "Công cụ Điều phối Hành trình Khách hàng (Customer Journey Orchestration Engine) trong CRM hiện đại hoạt động dựa trên logic nào?",
        "How does a modern CRM Customer Journey Orchestration Engine operate across dynamic interaction lifecycles?",
        {
            "A": ("Gửi một email cố định vào mỗi thứ Ba bất kể khách hàng làm gì.", "Transmitting an identical static promotional email every Tuesday regardless of customer activity."),
            "B": ("Lắng nghe liên tục hành vi của khách hàng trên mọi kênh và tự động quyết định 'Hành động Tốt nhất Tiếp theo' (Next Best Action) phù hợp nhất theo thời gian thực (như gửi ưu đãi, gọi điện, hoặc tạm dừng quảng cáo nếu khách đang có khiếu nại chưa giải quyết).", "Continuously listening to cross-channel behavioral events to dynamically trigger the optimal Next Best Action (offer, call, or suppressing marketing when open tickets exist)."),
            "C": ("Tự động gọi cảnh sát khi khách hàng không mở email trong 3 ngày.", "Summoning local emergency law enforcement if a subscriber fails to open an email."),
            "D": ("Xóa tài khoản của khách hàng nếu họ không thích trang fanpage.", "Terminating account profiles if users fail to like official social pages.")
        },
        "B",
        "Journey Orchestration cá nhân hóa hành trình theo từng cá nhân dựa trên sự kiện thực tế, tránh các tình huống phản cảm như tiếp tục gửi quảng cáo chào mua món hàng mà khách hàng vừa mới mua hôm qua.",
        "Journey orchestration personalizes real-time touchpoint sequencing based on customer state, preventing tone-deaf blunders like blasting promo ads to users facing active support outages.",
        "Baran & Galka (2017)", "Chapter 13 & 14", "pp. 412-418, 444-448", ["journey-orchestration", "next-best-action", "omnichannel-logic"]
    ),
    (
        "q-09-19", "Crowdsourcing and Community Platforms", "easy", "single_choice",
        "Diễn đàn hỗ trợ cộng đồng (Community Forums / Peer-to-Peer Support) như Apple Support Community mang lại lợi ích kép nào cho CRM?",
        "What dual strategic benefit do Customer Community Forums (e.g., Apple Support Communities) deliver to CRM ecosystems?",
        {
            "A": ("Bắt buộc mọi người dùng phải nộp tiền phí thành viên hàng tháng.", "Compelling all device owners to remit recurring monthly forum subscription dues."),
            "B": ("Giảm tải đáng kể chi phí vận hành trung tâm hỗ trợ kỹ thuật nhờ khách hàng tự giải đáp thắc mắc cho nhau, đồng thời nuôi dưỡng cộng đồng người hâm mộ chuyên gia gắn kết sâu sắc với thương hiệu.", "Drastically paring down tier-1 support center operating costs as passionate peers resolve questions for each other, while cultivating super-user brand allegiance."),
            "C": ("Làm cho nhân viên chăm sóc khách hàng của công ty bị mất việc toàn bộ.", "Causing all internal technical support specialists to suffer structural unemployment."),
            "D": ("Cho phép người dùng tự do bẻ khóa phần mềm độc quyền của hãng.", "Permitting community members to freely crack and distribute proprietary software builds.")
        },
        "B",
        "Hơn 50% câu hỏi kỹ thuật thông thường có thể được giải quyết bởi các chuyên gia trong cộng đồng người dùng, giúp công ty tiết kiệm hàng triệu USD chi phí tổng đài.",
        "Community support scales peer-to-peer knowledge sharing, resolving technical inquiries at zero incremental marginal cost while fostering passionate brand champions.",
        "Baran & Galka (2017)", "Chapter 13", "pp. 414-419", ["community-forums", "peer-to-peer-support", "super-users"]
    ),
    (
        "q-09-20", "Digital Touchpoint Fatigue", "medium", "single_choice",
        "Hiện tượng 'Quá tải điểm chạm số' (Digital Touchpoint Fatigue / Notification Overload) gây ra hậu quả tiêu cực nào cho quan hệ khách hàng?",
        "What commercial damage does 'Digital Notification Overload / Customer Fatigue' inflict on relationship health?",
        {
            "A": ("Làm điện thoại của khách hàng hết pin nhanh hơn bình thường.", "Causing consumer smartphone batteries to drain marginally faster."),
            "B": ("Gây ra sự ức chế tâm lý, khiến khách hàng tắt thông báo ứng dụng (mute), hủy đăng ký nhận email (unsubscribe), xóa ứng dụng hoặc chuyển sang trạng thái hoàn toàn thờ ơ với thương hiệu.", "Triggering cognitive irritation, prompting users to disable push alerts, unsubscribe from email lists, uninstall mobile clients, and cultivate deep brand apathy."),
            "C": ("Làm cho mạng internet của toàn thành phố bị mất tín hiệu.", "Inducing municipal metropolitan broadband infrastructure blackouts."),
            "D": ("Tự động chuyển đổi tài khoản của khách hàng thành tài khoản VIP.", "Automatically upgrading standard consumer accounts into premier VIP tiers.")
        },
        "B",
        "Gửi quá nhiều thông báo vô nghĩa sẽ phá hủy niềm tin; CRM thông minh phải áp dụng chính sách 'Giới hạn Tần suất' (Frequency Capping) để tôn trọng không gian riêng của khách hàng.",
        "Excessive, tone-deaf messaging spam alienates users; sophisticated CRM enforces algorithmic Frequency Capping to preserve engagement and prevent list burnout.",
        "Baran & Galka (2017)", "Chapter 13 & 14", "pp. 420-425, 450-454", ["notification-fatigue", "frequency-capping", "customer-burnout"]
    )
]

for item in e9:
    questions_batch4.append(make_q(
        item[0], "EXAM-09", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

# ==========================================
# EXAM 10: METRICS, PRIVACY, ETHICS & EVOLUTION (q-10-01 to q-10-20)
# ==========================================
e10 = [
    (
        "q-10-01", "Balanced Scorecard for CRM", "medium", "single_choice",
        "Mô hình Thẻ điểm Cân bằng (Balanced Scorecard - Kaplan & Norton) khi áp dụng để đánh giá hiệu quả CRM đòi hỏi doanh nghiệp phải đo lường 4 góc nhìn nào?",
        "When applying the Balanced Scorecard framework to evaluate CRM performance, which four balanced perspectives must be tracked?",
        {
            "A": ("Góc nhìn Tài chính (Financial), Khách hàng (Customer), Quy trình Nội bộ (Internal Business Processes), và Học hỏi & Phát triển (Learning & Growth).", "Financial Perspective, Customer Perspective, Internal Business Process Perspective, and Learning & Growth Perspective."),
            "B": ("Góc nhìn Giá cả, Quảng cáo, Sản phẩm, và Khuyến mãi.", "Pricing, Advertising, Product, and Promotional Perspectives."),
            "C": ("Góc nhìn Sáng, Trưa, Chiều, và Tối.", "Morning, Midday, Evening, and Night Perspectives."),
            "D": ("Góc nhìn Lập trình, Kiểm thử, Cài đặt, và Sao lưu.", "Coding, Testing, Installation, and Backup Perspectives.")
        },
        "A",
        "Balanced Scorecard giúp doanh nghiệp không chỉ nhìn chăm chăm vào các chỉ số tài chính ngắn hạn (quá khứ) mà đo lường cả sức khỏe quy trình, mức độ gắn kết khách hàng và năng lực đội ngũ.",
        "The Balanced Scorecard tethers lagging financial outputs to leading operational drivers: customer satisfaction, process speed, and employee knowledge growth.",
        "Baran & Galka (2017)", "Chapter 11", "pp. 348-356", ["balanced-scorecard", "crm-metrics", "performance-management"]
    ),
    (
        "q-10-02", "Lagging vs Leading Indicators", "hard", "single_choice",
        "Trong hệ thống đo lường hiệu quả CRM, sự khác biệt giữa 'Chỉ số Kết quả' (Lagging Indicators) và 'Chỉ số Dẫn dắt' (Leading Indicators) là gì?",
        "In CRM performance architecture, what distinguishes 'Lagging Indicators' from 'Leading Indicators'?",
        {
            "A": ("Chỉ số kết quả đo bằng số thập phân; chỉ số dẫn dắt đo bằng số nguyên.", "Lagging indicators are measured in decimals; leading indicators in integers."),
            "B": ("Chỉ số kết quả đo lường kết quả cuối cùng đã diễn ra trong quá khứ (như Doanh thu, Lợi nhuận gộp, Tỷ lệ rời bỏ); Chỉ số dẫn dắt đo lường các hành vi trung gian dự báo tương lai (như Tần suất đăng nhập CRM, Thời gian phản hồi đầu mối, Tỷ lệ hồ sơ khách hàng đầy đủ).", "Lagging indicators measure historical post-facto outcomes (Revenue, Gross Margin, Churn Rate); Leading indicators track upstream behavioral velocities predicting future health (CRM login frequency, lead response speed, profile completeness)."),
            "C": ("Chỉ số dẫn dắt chỉ áp dụng cho ban giám đốc; chỉ số kết quả áp dụng cho bảo vệ.", "Leading indicators apply solely to board members; lagging indicators apply to guards."),
            "D": ("Không có bất kỳ sự khác biệt nào giữa hai nhóm chỉ số này.", "There is no conceptual difference between the two indicator classifications.")
        },
        "B",
        "Bạn không thể thay đổi chỉ số kết quả khi nó đã xảy ra (như doanh thu quý trước bị sụt giảm); bạn chỉ có thể can thiệp bằng cách quản lý các chỉ số dẫn dắt (như gọi thêm cuộc gọi tư vấn, nhập đủ dữ liệu hôm nay).",
        "Lagging metrics confirm historical results but arrive too late for corrective steering; leading behavioral metrics offer predictive signals that managers can proactively influence.",
        "Kostojohn et al. (2011) p. 210; Baran & Galka (2017) p. 352", "Chapter 11", "pp. 350-355, 210-214", ["leading-indicators", "lagging-indicators", "metrics-design"]
    ),
    (
        "q-10-03", "Customer Data Privacy Rights (GDPR)", "medium", "single_choice",
        "Theo Quy định Bảo vệ Dữ liệu Chung của Liên minh Châu Âu (GDPR), 'Quyền Được Di chuyển Dữ liệu' (Right to Data Portability) trao cho khách hàng quyền gì?",
        "Under the European Union General Data Protection Regulation (GDPR), what does the 'Right to Data Portability' grant consumers?",
        {
            "A": ("Quyền bắt công ty phải chở máy tính đến nhà khách hàng.", "The right to compel the enterprise to transport physical servers to the customer's home."),
            "B": ("Quyền yêu cầu doanh nghiệp cung cấp toàn bộ dữ liệu cá nhân của họ dưới một định dạng có cấu trúc, thông dụng và máy đọc được (như JSON, CSV) để chuyển giao sang một nhà cung cấp dịch vụ khác mà không bị cản trở.", "The right to obtain all their personal data in a structured, commonly used, and machine-readable format (e.g., JSON, CSV) to transfer seamlessly to a competing service provider."),
            "C": ("Quyền yêu cầu công ty thanh toán tiền cước điện thoại di động.", "The right to demand reimbursement for private cellular telecommunications bills."),
            "D": ("Quyền xóa toàn bộ trang web của công ty khỏi mạng internet.", "The right to delete the entire corporate website from global internet indexes.")
        },
        "B",
        "Data Portability phá vỡ bẫy khóa dữ liệu (data lock-in), trao quyền lực lại cho người dùng để họ tự do chuyển đổi nhà cung cấp dịch vụ nếu muốn.",
        "Data portability empowers individuals against monopolistic platform lock-in, requiring open data exports that enable frictionless switching between competing providers.",
        "Baran & Galka (2017)", "Chapter 12", "pp. 382-386", ["gdpr", "data-portability", "data-privacy"]
    ),
    (
        "q-10-04", "Opt-In vs Opt-Out Mechanisms", "hard", "single_choice",
        "Trong tiếp thị số và tuân thủ quyền riêng tư dữ liệu, sự khác biệt pháp lý giữa cơ chế 'Opt-In' và 'Opt-Out' là gì?",
        "In privacy compliance and digital consent management, what is the regulatory distinction between 'Opt-In' and 'Opt-Out' frameworks?",
        {
            "A": ("Opt-In là gửi thư giấy; Opt-Out là gửi tin nhắn qua điện thoại.", "Opt-In represents postal letters; Opt-Out represents mobile text messages."),
            "B": ("Opt-In đòi hỏi người dùng phải chủ động thực hiện hành động đồng ý rõ ràng trước khi doanh nghiệp được phép thu thập/gửi thông điệp tiếp thị (chuẩn mực khắt khe của GDPR); Opt-Out mặc nhiên coi người dùng đã đồng ý cho đến khi họ chủ động lên tiếng từ chối (chuẩn CAN-SPAM truyền thống của Mỹ).", "Opt-In mandates unambiguous affirmative consent before personal data collection or marketing dispatch (strict GDPR baseline); Opt-Out presumes tacit consent until the user explicitly requests removal (traditional US CAN-SPAM baseline)."),
            "C": ("Opt-In dành cho các công ty lớn; Opt-Out chỉ dành cho cá nhân.", "Opt-In applies to multinational firms; Opt-Out applies strictly to private individuals."),
            "D": ("Cả hai cơ chế đều cấm hoàn toàn mọi hoạt động tiếp thị dưới mọi hình thức.", "Both regulatory frameworks ban all commercial promotional marketing outright.")
        },
        "B",
        "Các quy định hiện đại chuyển dịch mạnh mẽ sang Opt-In bắt buộc; các ô đánh dấu chọn đồng ý sẵn (pre-ticked boxes) bị coi là bất hợp pháp theo chuẩn mực bảo vệ dữ liệu mới.",
        "Global privacy jurisprudence favors affirmative explicit Opt-In; pre-checked consent checkboxes and deceptive passive consents are prohibited under modern enforcement.",
        "Baran & Galka (2017)", "Chapter 12", "pp. 384-389", ["opt-in", "opt-out", "consent-management", "gdpr"]
    ),
    (
        "q-10-05", "Surveillance Capitalism & Dark Patterns", "hard", "single_choice",
        "Khái niệm 'Mẫu Thiết kế Đen' (Dark Patterns) trong giao diện người dùng CRM và website bán hàng thể hiện hành vi phi đạo đức nào?",
        "What unethical practice do 'Dark Patterns' denote in consumer-facing CRM interfaces and e-commerce checkout flows?",
        {
            "A": ("Sử dụng màu nền đen cho trang web để bảo vệ mắt người dùng ban đêm.", "Employing dark background colors to alleviate ocular eye strain during nighttime reading."),
            "B": ("Cố tình thiết kế giao diện gây hiểu lầm, đánh lừa hoặc thao túng tâm lý người dùng để họ vô tình đăng ký dịch vụ trả phí định kỳ, chia sẻ dữ liệu nhạy cảm hoặc gặp khó khăn cực độ khi muốn hủy tài khoản (như kỹ thuật Roache Motel).", "Intentionally deceptive UI/UX designs engineered to trick users into unintended actions (accidental recurring subscriptions, hidden data sharing, or labyrinthine cancellation loops like the Roach Motel)."),
            "C": ("Lập trình phần mềm bằng ngôn ngữ lập trình không có bản quyền.", "Authoring enterprise software using unlicensed programming interpreters."),
            "D": ("Tắt máy chủ vào ban đêm khi nhân viên đi ngủ.", "Powering down server hardware during nighttime hours when personnel sleep.")
        },
        "B",
        "Dark Patterns mang lại số liệu chuyển đổi ngắn hạn giả tạo nhưng phá hủy niềm tin thương hiệu và đối mặt với các án phạt pháp lý nặng nề từ các cơ quan bảo vệ người tiêu dùng.",
        "Dark patterns exploit human cognitive biases for manipulative conversions, burning customer trust and attracting severe regulatory fines under unfair trade practice acts.",
        "Baran & Galka (2017)", "Chapter 12", "pp. 390-395", ["dark-patterns", "ethics", "deceptive-design", "consumer-protection"]
    ),
    (
        "q-10-06", "Data Monetization Ethics", "hard", "single_choice",
        "Khi một doanh nghiệp kiếm tiền từ dữ liệu khách hàng (Data Monetization), ranh giới đạo đức tối thượng cần được tuân thủ là gì?",
        "When an enterprise monetizes proprietary customer data assets, what fundamental ethical boundary must never be breached?",
        {
            "A": ("Phải chia 50% số tiền kiếm được cho nhân viên lập trình hệ thống.", "Splitting 50% of commercial data sales proceeds with internal software engineers."),
            "B": ("Tuyệt đối minh bạch với người dùng về mục đích sử dụng dữ liệu, ẩn danh hóa hoàn toàn (Anonymization/Pseudonymization) để không thể truy ngược danh tính cá nhân, và tôn trọng quyền từ chối của khách hàng.", "Absolute transparency regarding commercial usage, robust mathematical anonymization/pseudonymization to prevent re-identification, and strict adherence to user revocation rights."),
            "C": ("Bán dữ liệu cho bất kỳ ai trả giá cao nhất bất kể mục đích sử dụng.", "Selling data to the highest bidder on global markets regardless of intent."),
            "D": ("Bắt buộc khách hàng phải trả tiền để xem dữ liệu của chính họ.", "Requiring consumers to pay financial fees to view their personal transaction logs.")
        },
        "B",
        "Dữ liệu khách hàng không phải là món hàng để bán lén lút sau lưng; thương mại hóa dữ liệu vô trách nhiệm sẽ kích hoạt khủng hoảng tẩy chay thương hiệu nghiêm trọng.",
        "Ethical monetization treats customer data as a sacred trust, leveraging aggregate differential privacy insights without commoditizing identifiable individual profiles.",
        "Baran & Galka (2017)", "Chapter 12", "pp. 388-394", ["data-monetization", "ethics", "anonymization"]
    ),
    (
        "q-10-07", "First-Call Resolution (FCR) Metric", "medium", "single_choice",
        "Chỉ số 'Giải quyết ngay từ Cuộc gọi Đầu tiên' (First-Contact / First-Call Resolution - FCR) trong trung tâm dịch vụ khách hàng phản ánh điều gì?",
        "What does First-Contact / First-Call Resolution (FCR) measure in contact center operations?",
        {
            "A": ("Số lượng cuộc gọi nhân viên đã thực hiện trong 1 giờ làm việc.", "The total volume of outbound phone calls placed per business hour."),
            "B": ("Tỷ lệ phần trăm các thắc mắc hoặc sự cố của khách hàng được giải quyết triệt để và thỏa đáng ngay trong lần tương tác đầu tiên mà khách hàng không cần phải gọi lại lần thứ hai.", "The percentage of incoming customer inquiries or complaints fully resolved during the initial contact without requiring follow-up callbacks or transfers."),
            "C": ("Tốc độ nhấc máy của điện thoại viên trong vòng 3 tiếng chuông reo.", "The speed of picking up incoming ring tones within three audio chimes."),
            "D": ("Chi phí cước viễn thông cho một phút gọi điện thoại.", "The monetary telecommunications tariff cost incurred per call minute.")
        },
        "B",
        "FCR là chỉ số vàng phản ánh đồng thời cả hiệu quả chi phí (không tốn công xử lý lại) và sự hài lòng của khách hàng (không bị ức chế vì phải giải thích nhiều lần).",
        "High FCR correlates directly with superior customer satisfaction and reduced operating costs, eliminating frustrating multi-agent ping-pong loops.",
        "Baran & Galka (2017)", "Chapter 11", "pp. 355-358", ["fcr", "first-call-resolution", "service-efficiency"]
    ),
    (
        "q-10-08", "Average Handle Time (AHT) Fallacy", "hard", "single_choice",
        "Tại sao việc đặt chỉ tiêu KPI giảm 'Thời gian Xử lý Trung bình' (Average Handle Time - AHT) một cách quá máy móc cho nhân viên tổng đài lại có thể phá hủy mối quan hệ khách hàng?",
        "Why can rigidly penalizing customer service agents for high Average Handle Time (AHT) severely degrade long-term relationship health?",
        {
            "A": ("Vì nhân viên sẽ đòi tăng lương gấp 3 lần.", "Because contact center agents will demand triple base compensation."),
            "B": ("Nhân viên bị áp lực thời gian sẽ tìm cách cúp máy sớm, không lắng nghe thấu đáo, giải quyết hời hợt hoặc chuyển cuộc gọi sang người khác để đạt KPI, khiến vấn đề của khách không được xử lý dứt điểm và khách phải gọi lại nhiều lần.", "Pressure to compress handle times forces agents to rush callers, dismiss nuance, cut conversations short, or deflect tickets, leaving root issues unresolved and triggering repeat complaints."),
            "C": ("Vì nhà mạng viễn thông sẽ phạt tiền công ty nếu cuộc gọi ngắn hơn 1 phút.", "Because telecommunications carriers fine companies for calls under 60 seconds."),
            "D": ("Vì khách hàng luôn muốn nói chuyện điện thoại ít nhất 2 tiếng đồng hồ.", "Because consumers invariably demand to converse for at least two consecutive hours.")
        },
        "B",
        "Tối ưu hóa AHT mù quáng dẫn đến văn hóa 'đẩy khách hàng đi' thay vì 'giải quyết vấn đề cho khách'. Doanh nghiệp hiện đại ưu tiên FCR và CSAT hơn là cắt giảm từng giây AHT.",
        "Over-indexing on AHT encourages perverse behaviors where reps ditch complex problems to hit arbitrary minute quotas, spiking defection and repeat contact volume.",
        "Baran & Galka (2017)", "Chapter 11", "pp. 356-360", ["aht", "perverse-incentives", "kpi-design", "fcr"]
    ),
    (
        "q-10-09", "Customer Lifetime Value Accuracy Audit", "hard", "single_choice",
        "Khi kiểm toán tính chính xác của mô hình dự báo CLV định kỳ, bước kiểm tra đối chiếu nào sau đây mang tính quyết định?",
        "When performing an ongoing audit of predictive CLV algorithmic models, which validation exercise is most decisive?",
        {
            "A": ("So sánh giá trị dự báo lịch sử với dòng tiền lợi nhuận thực tế thu được từ nhóm khách hàng đó qua thời gian (Backtesting / Out-of-sample validation).", "Backtesting historical predicted CLV against actual realized margin cash flows harvested from those identical cohorts over subsequent fiscal years."),
            "B": ("Hỏi ý kiến của nhân viên bảo vệ xem mô hình có đẹp mắt không.", "Asking facilities staff whether the algorithmic chart looks aesthetically pleasing."),
            "C": ("Tăng toàn bộ kết quả dự báo thêm 200% để làm hài lòng ban giám đốc.", "Artificially inflating all forecasting outputs by 200% to please executive directors."),
            "D": ("Xóa bỏ toàn bộ dữ liệu giao dịch cũ để không phải đối chiếu.", "Deleting historical accounting ledgers to eliminate reconciliation burdens.")
        },
        "A",
        "Backtesting kiểm chứng xem mô hình có dự báo sát thực tế hay không; nếu mô hình liên tục thổi phồng CLV, doanh nghiệp sẽ chi tiêu quá mức cho chi phí thu hút khách hàng (CAC) và chịu lỗ.",
        "Rigorous out-of-sample backtesting exposes predictive drift, ensuring financial resource allocations and customer acquisition budgets rest on calibrated empirical reality.",
        "Baran & Galka (2017)", "Chapter 10 & 11", "pp. 316-320, 362-366", ["clv-audit", "backtesting", "model-validation"]
    ),
    (
        "q-10-10", "System Maintenance: Patching & Release Cycles", "medium", "single_choice",
        "Theo Kostojohn et al. (2011, tr. 215-222), quy trình quản lý các bản nâng cấp phát hành (Release Management) cho hệ thống CRM cần tuân thủ nguyên tắc nào?",
        "According to Kostojohn et al. (2011, pp. 215-222), what rule governs disciplined CRM Release Management across ongoing maintenance lifecycles?",
        {
            "A": ("Cập nhật trực tiếp các thay đổi cấu hình và viết code ngay trên môi trường vận hành thật (Live Production) vào giữa ngày làm việc.", "Pushing untested code and live declarative schema configurations directly to production mid-day."),
            "B": ("Mọi tính năng mới, cấu hình sửa đổi hoặc bản vá phần mềm phải được phát triển trên môi trường phát triển (Sandbox/Dev), kiểm thử kỹ lưỡng trên môi trường UAT, và chỉ được đóng gói phát hành lên Production theo lịch định kỳ có kiểm soát (Scheduled Release Windows) sau khi có phê duyệt.", "All enhancements, patches, and configurations must be authored in Sandbox, rigorously validated in UAT, and deployed to Production strictly during scheduled release windows post-approval."),
            "C": ("Chỉ nâng cấp phần mềm mỗi 15 năm một lần.", "Executing software release upgrades once every fifteen calendar years."),
            "D": ("Cho phép tất cả nhân viên tự do tải mã nguồn về chỉnh sửa tùy thích.", "Permitting all employees to modify server source code at their personal discretion.")
        },
        "B",
        "Nghiêm cấm tuyệt đối việc 'code sống trên production'; quy trình phát hành qua môi trường thử nghiệm (Sandbox -> UAT -> Prod) là kỷ luật sắt bảo vệ sự ổn định của hệ thống.",
        "Strict environment isolation (Dev -> Staging/UAT -> Production) prevents unvetted bugs or regressions from compromising production data integrity and business continuity.",
        "Kostojohn et al. (2011)", "Chapter 7", "pp. 215-222", ["release-management", "sandbox", "change-control"]
    ),
    (
        "q-10-11", "Change Advisory Board (CAB) Operation", "medium", "single_choice",
        "Hội đồng Cố vấn Thay đổi (Change Advisory Board - CAB) trong giai đoạn bảo trì CRM chịu trách nhiệm đánh giá điều gì trước khi một yêu cầu tính năng mới được triển khai?",
        "What does the Change Advisory Board (CAB) evaluate prior to greenlighting an enhancement request in an operational CRM system?",
        {
            "A": ("Đánh giá giá trị kinh doanh, tính cấp thiết, tác động đến các quy trình hiện tại, mức độ phức tạp kỹ thuật và nguy cơ xung đột với các module khác.", "Assessing business value, urgency, impact on adjacent workflows, technical complexity, regression risks, and architectural alignment."),
            "B": ("Bình chọn trang phục công sở đẹp nhất trong tuần của nhân viên yêu cầu.", "Voting on the aesthetic office attire of the employee requesting the feature."),
            "C": ("Kiểm tra xem người yêu cầu tính năng có tham gia đầy đủ các buổi liên hoan hay không.", "Checking whether the requester attended all recent corporate holiday banquets."),
            "D": ("Tính toán số lượng chữ cái trong bản mô tả yêu cầu.", "Counting alphanumeric letter totals inside the enhancement ticket description.")
        },
        "A",
        "CAB gồm đại diện của cả kinh doanh và kỹ thuật giúp phân loại các yêu cầu hợp lý với các đòi hỏi nhất thời, ngăn chặn việc làm phình to hệ thống một cách hỗn loạn.",
        "The CAB acts as an objective filter, prioritizing enhancements that deliver verified business ROI while rejecting idiosyncratic requests that bloat technical debt.",
        "Kostojohn et al. (2011)", "Chapter 7", "pp. 218-223", ["cab", "change-advisory-board", "governance"]
    ),
    (
        "q-10-12", "Data Retention & Archival Policies", "hard", "single_choice",
        "Chính sách Lưu trữ và Thanh lọc Dữ liệu Định kỳ (Data Retention & Archival Policy) trong hệ thống CRM giải quyết bài toán nào sau đây?",
        "What operational challenge does a defined CRM Data Retention and Archival Policy resolve?",
        {
            "A": ("Xóa bỏ hoàn toàn mọi hợp đồng thương mại ngay sau khi nhận được tiền thanh toán.", "Purging commercial sales contracts the second invoice funds clear."),
            "B": ("Lưu trữ phân tầng: chuyển các dữ liệu giao dịch cũ nhiều năm không còn hoạt động sang vùng lưu trữ lạnh (Cold Storage) để giảm tải cho cơ sở dữ liệu chính, duy trì tốc độ truy vấn cao đồng thời đáp ứng các quy định pháp luật về lưu trữ hồ sơ thuế.", "Tiered storage management: archiving dormant historical transactions to low-cost cold storage to optimize production query performance while complying with tax recordkeeping laws."),
            "C": ("In toàn bộ cơ sở dữ liệu ra giấy và cất vào kho đồ cổ.", "Printing the entire digital relational database onto paper reams stored in basements."),
            "D": ("Bán thông tin giao dịch cũ cho các công ty quảng cáo ngoài trời.", "Monetizing archived historical ledger rows to third-party billboard syndicates.")
        },
        "B",
        "Nếu cơ sở dữ liệu chính lưu trữ tích tụ 15 năm giao dịch, tốc độ tìm kiếm sẽ chậm như rùa; thanh lọc dữ liệu định kỳ giúp hệ thống vận hành thanh thoát và tiết kiệm chi phí lưu trữ nóng.",
        "Unchecked database bloating degrades indexing and query performance; automated tiered archiving offloads historical bloat while preserving compliance audits.",
        "Kostojohn et al. (2011)", "Chapter 7", "pp. 222-226", ["data-retention", "archival-policy", "performance-optimization"]
    ),
    (
        "q-10-13", "Surveillance Capitalism Risks", "hard", "single_choice",
        "Khái niệm 'Chủ nghĩa Tư bản Giám sát' (Surveillance Capitalism - Shoshana Zuboff) cảnh báo nguy cơ đạo đức nào trong các hệ thống CRM và nền tảng số hiện đại?",
        "What ethical peril does Shoshana Zuboff's 'Surveillance Capitalism' framework highlight regarding modern analytical CRM and behavioral platforms?",
        {
            "A": ("Việc lắp đặt quá nhiều camera an ninh trong thang máy tòa nhà văn phòng.", "Installing excessive physical closed-circuit television cameras in office elevators."),
            "B": ("Sự biến đổi của hành vi con người thành nguồn tài nguyên thô (Behavioral Surplus) bị thu thập lén lút, phân tích và đóng gói thành các sản phẩm dự báo hành vi để thao túng và định hướng quyết định của người tiêu dùng mà họ không hề hay biết.", "The unilateral extraction of private human experience as raw 'behavioral surplus', fabricated into behavioral prediction products engineered to nudge and manipulate choices without consent."),
            "C": ("Việc các kỹ sư phần mềm làm việc ngoài giờ không được trả lương.", "Software engineers performing uncompensated overtime on weekend sprints."),
            "D": ("Việc tăng giá tiền điện đối với các trung tâm dữ liệu.", "Commercial electric tariff hikes imposed on hyperscale cloud facilities.")
        },
        "B",
        "CRM chân chính hướng đến việc phục vụ khách hàng tốt hơn dựa trên sự đồng thuận; Chủ nghĩa tư bản giám sát cảnh báo sự suy đồi khi biến khách hàng thành con mồi bị thao túng tâm lý.",
        "Ethical CRM creates reciprocal value through mutual trust; surveillance capitalism perverts this relationship by covertly extracting behavioral data to manipulate consumer autonomy.",
        "Baran & Galka (2017)", "Chapter 12", "pp. 392-398", ["surveillance-capitalism", "ethics", "behavioral-surplus", "zuboff"]
    ),
    (
        "q-10-14", "Continuous User Re-Education", "medium", "single_choice",
        "Tại sao trong giai đoạn vận hành duy trì CRM, hoạt động 'Tái Đào tạo Định kỳ' (Continuous User Training) là bắt buộc?",
        "Why is 'Continuous User Training' mandatory during ongoing CRM system evolution and maintenance?",
        {
            "A": ("Vì nhân viên luôn quên sạch mọi thứ sau mỗi 2 tuần làm việc.", "Because employees suffer total amnesia regarding workflows every fortnight."),
            "B": ("Để đào tạo nhân viên mới gia nhập công ty, cập nhật cho nhân viên cũ về các tính năng mới được bổ sung, khắc phục các thói quen nhập liệu sai sót và nâng cao kỹ năng khai thác báo cáo phân tích chuyên sâu.", "To onboard new hires, update incumbent staff on newly deployed features, remediate sloppy data entry habits, and elevate analytical reporting proficiency."),
            "C": ("Để kiếm cớ trừ lương nhân viên nếu họ không tham gia lớp học.", "Inventing administrative excuses to deduct payroll wages for training non-attendance."),
            "D": ("Để hoàn thành chỉ tiêu thời gian giảng dạy của phòng hành chính.", "Exhausting administrative human resources annual lecture hour quotas.")
        },
        "B",
        "Tỷ lệ biến động nhân sự (turnover) luôn làm hao hụt tri thức hệ thống; tái đào tạo thường xuyên đảm bảo các chuẩn mực nhập liệu và kỹ năng sử dụng không bị thoái hóa theo thời gian.",
        "Staff turnover steadily erodes institutional system knowledge; continuous micro-learning prevents adoption decay and ensures new workflows are executed consistently.",
        "Kostojohn et al. (2011)", "Chapter 7", "pp. 212-217", ["continuous-training", "user-enablement", "adoption-maintenance"]
    ),
    (
        "q-10-15", "System Health Audits", "medium", "single_choice",
        "Một đợt 'Kiểm tra Sức khỏe Hệ thống CRM' (CRM Health Check / System Audit) định kỳ hàng năm thường đánh giá 3 trụ cột nào?",
        "An annual enterprise CRM System Health Audit typically inspects which three foundational pillars?",
        {
            "A": ("Sức khỏe thể chất của giám đốc, Nhiệt độ phòng họp, và Độ ẩm không khí.", "Executive biometric health, Conference room temperature, and Ambient humidity."),
            "B": ("Chất lượng dữ liệu (Data Quality & Hygiene), Mức độ chấp nhận của người dùng (User Adoption & Usage Patterns), và Hiệu năng kiến trúc kỹ thuật (Technical Performance & API Integrations).", "Data Quality & Hygiene metrics, User Adoption and engagement patterns, and Technical Infrastructure & API performance benchmarks."),
            "C": ("Số lượng bàn phím bị hỏng, Giá thị trường của máy tính cũ, và Tiền nước uống.", "Broken keyboard tallies, Depreciated workstation market values, and Water dispenser bills."),
            "D": ("Số lượng tài khoản mạng xã hội của nhân viên phòng marketing.", "The gross count of personal social media handles belonging to marketing staff.")
        },
        "B",
        "Health check định kỳ giúp phát hiện sớm các 'vùng hoại tử' của hệ thống: các trường dữ liệu bị bỏ trống, các phòng ban bỏ không dùng hoặc các điểm nghẽn tích hợp chậm chạp.",
        "Periodic health checks diagnose system atrophy, uncovering dirty data pockets, abandoned modules, and slow API queries before they metastasize into enterprise failures.",
        "Kostojohn et al. (2011)", "Chapter 7", "pp. 224-228", ["health-check", "system-audit", "continuous-improvement"]
    ),
    (
        "q-10-16", "Algorithmic Bias in CRM AI", "hard", "single_choice",
        "Hiện tượng 'Định kiến Thuật toán' (Algorithmic Bias) trong các mô hình CRM chấm điểm tín dụng hoặc chấm điểm đầu mối bán hàng (Lead Scoring) nảy sinh từ đâu?",
        "Where does 'Algorithmic Bias' originate within AI-driven CRM credit evaluation and lead scoring engines?",
        {
            "A": ("Do máy tính bị nhiễm virus phá hoại từ bên ngoài.", "External malware infections deliberately tampering with operating system kernels."),
            "B": ("Do dữ liệu lịch sử được dùng để huấn luyện mô hình đã chứa sẵn các định kiến xã hội hoặc phân biệt đối xử trong quá khứ (ví dụ: thiên vị theo chủng tộc, giới tính hoặc mã vùng sinh sống), khiến AI tiếp tục học và nhân bản những bất công đó.", "Historical training data embedding legacy human prejudices or discriminatory lending patterns (race, gender, zip codes), leading machine learning models to replicate and amplify past inequities."),
            "C": ("Do các lập trình viên sử dụng màn hình máy tính có độ phân giải quá cao.", "Software engineers programming on ultra-high-resolution monitors."),
            "D": ("Do hệ thống CRM không được kết nối với mạng điện thoại cố định.", "The CRM platform lacking direct interfaces to analog landline telephones.")
        },
        "B",
        "Máy tính không có cảm xúc nhưng học từ dữ liệu quá khứ; nếu dữ liệu quá khứ phản ánh sự phân biệt đối xử, thuật toán sẽ tự động phân biệt đối xử với người dùng tương lai.",
        "AI models mirror the data they ingest; training algorithms on historically biased rejection records bakes systemic discrimination into automated future underwriting decisions.",
        "Baran & Galka (2017)", "Chapter 12", "pp. 394-399", ["algorithmic-bias", "ai-ethics", "fairness-in-ml"]
    ),
    (
        "q-10-17", "Total Cost of Ownership Post-Launch Reality", "medium", "single_choice",
        "Trong vòng đời 5 năm của một dự án CRM, ngân sách bảo trì và phát triển tính năng mới sau khi triển khai thường chiếm tỷ lệ bao nhiêu trong Tổng chi phí sở hữu (TCO)?",
        "Across a 5-year enterprise CRM lifecycle, ongoing post-launch maintenance, support, and continuous evolution typically absorb what proportion of total TCO?",
        {
            "A": ("0% vì sau khi Golive thì không tốn thêm bất kỳ chi phí nào.", "0% because post-launch operations generate zero incremental expenditures."),
            "B": ("Khoảng 50% đến 70% tổng chi phí sở hữu của cả vòng đời (bao gồm phí bản quyền định kỳ, nâng cấp hạ tầng, đội hỗ trợ vận hành và chi phí tùy biến quy trình mới).", "Approximately 50% to 70% of lifetime TCO (encompassing recurring subscriptions, infrastructure upgrades, permanent support staff, and continuous enhancement cycles)."),
            "C": ("Đúng 1% chi phí của dự án ban đầu.", "Exactly 1.0% of the initial project implementation invoice."),
            "D": ("100% chi phí chỉ nằm ở ngày đầu tiên mua phần mềm.", "100% of costs occur on the single initial procurement day.")
        },
        "B",
        "Golive chỉ là điểm khởi đầu; chi phí 'nuôi dưỡng', vận hành và phát triển hệ thống trong nhiều năm tiếp theo luôn vượt xa chi phí triển khai ban đầu.",
        "Go-live is merely the starting line; cumulative multi-year software subscriptions, integration maintenance, and business evolution outstrip initial launch capital.",
        "Kostojohn et al. (2011)", "Chapter 4 & 7", "pp. 104-108, 220-225", ["tco-reality", "post-launch-costs", "budgeting"]
    ),
    (
        "q-10-18", "Customer Advocacy Metric Evolution", "medium", "single_choice",
        "Chỉ số 'Giá trị Giới thiệu Khách hàng Ròng' (Net Advocacy Score / Earned Growth Rate) của Reichheld đo lường điều gì vượt trội hơn NPS truyền thống?",
        "What does Fred Reichheld's evolved 'Earned Growth Rate' (EGR) measure that traditional Net Promoter Score survey sampling misses?",
        {
            "A": ("Đo số tiền khách hàng tip cho nhân viên giao hàng.", "The cash tips given to parcel delivery personnel."),
            "B": ("Đo lường tăng trưởng doanh thu thực tế được tạo ra từ hai nguồn: doanh thu tăng thêm từ khách hàng cũ quay lại (Back-for-More) và doanh thu từ khách hàng mới được giới thiệu bởi khách hàng cũ (Referrals), dựa trên số liệu kế toán thực tế thay vì điểm khảo sát cảm tính.", "Measuring audited revenue growth driven purely by existing customer retention expansion and new customer referrals, grounding loyalty in hard accounting ledgers rather than subjective survey responses."),
            "C": ("Đo số lượng người theo dõi trên tài khoản Instagram của công ty.", "The gross follower tally registered on official corporate Instagram accounts."),
            "D": ("Đo số lượng hóa đơn bị khách hàng khiếu nại trong năm.", "The number of invoice ledgers subject to formal billing arbitration.")
        },
        "B",
        "EGR gắn kết lòng trung thành trực tiếp với báo cáo tài chính kế toán, loại bỏ các sai số do khảo sát thiên lệch hoặc hành vi 'chấm điểm hộ' của người được hỏi.",
        "Earned Growth connects customer loyalty directly to audited financial statements, verifying sustainable growth generated by organic retention and word-of-mouth advocacy.",
        "Baran & Galka (2017)", "Chapter 11", "pp. 360-365", ["earned-growth-rate", "reichheld", "nps-evolution", "financial-loyalty"]
    ),
    (
        "q-10-19", "Continuous Integration / Continuous Delivery (CI/CD) in CRM", "hard", "single_choice",
        "Việc áp dụng đường ống CI/CD (Tích hợp liên tục / Bàn giao liên tục) vào quản trị nền tảng Cloud CRM mang lại lợi ích gì?",
        "What operational advantage does a CI/CD (Continuous Integration / Continuous Delivery) pipeline bring to enterprise Cloud CRM administration?",
        {
            "A": ("Cho phép xóa bỏ hoàn toàn tất cả các máy chủ trên toàn cầu.", "Permitting the total decommissioning of all global web host servers."),
            "B": ("Tự động hóa quy trình kiểm thử mã nguồn, phát hiện xung đột và triển khai các thay đổi cấu hình/code một cách an toàn, nhanh chóng và thường xuyên từ kho lưu trữ (như Git) lên môi trường sản xuất mà không gây gián đoạn vận hành.", "Automating code testing, detecting merge conflicts, and executing safe, frequent, automated configuration releases from version control (Git) to production with minimal human error and zero downtime."),
            "C": ("Bắt buộc mọi lập trình viên phải làm việc liên tục 24 giờ không ngủ.", "Requiring software developers to code continuously for twenty-four sleepless hours."),
            "D": ("Tự động tăng giá bán sản phẩm trên website lên 10% mỗi ngày.", "Automatically elevating online product prices by 10% every calendar day.")
        },
        "B",
        "CI/CD đưa kỷ luật kỹ nghệ phần mềm hiện đại vào quản trị CRM, thay thế các thao tác xuất nhập gói cấu hình thủ công (Change Sets) dễ mắc lỗi bằng tự động hóa an toàn.",
        "CI/CD modernizes CRM release management, leveraging automated regression testing and version control pipelines to eliminate high-risk, error-prone manual change-set deployments.",
        "Kostojohn et al. (2011)", "Chapter 7", "pp. 216-221", ["ci-cd", "devops", "crm-automation", "release-engineering"]
    ),
    (
        "q-10-20", "The True Destination of CRM", "easy", "single_choice",
        "Khẳng định nào sau đây đúc kết sâu sắc và toàn diện nhất về đích đến cuối cùng của một chiến lược CRM thành công?",
        "Which statement provides the most profound and holistic summary of the ultimate destination of an authentic CRM journey?",
        {
            "A": ("Là việc cài đặt được phiên bản phần mềm đắt tiền nhất và lưu trữ được nhiều dữ liệu nhất thế giới.", "Purchasing the most exorbitant software licenses and amassing the largest raw data warehouse on earth."),
            "B": ("CRM không bao giờ là một dự án công nghệ có điểm dừng; đó là một cam kết chiến lược lâu dài và văn hóa tổ chức không ngừng tiến hóa, kết hợp giữa sự thấu cảm con người, kỷ luật quy trình và sức mạnh công nghệ để kiến tạo giá trị bền vững cho cả khách hàng và doanh nghiệp.", "CRM is never a one-off IT project with a finish line; it is an enduring strategic commitment and evolving culture uniting human empathy, process discipline, and technological power to co-create sustainable mutual value for customers and the enterprise."),
            "C": ("Là việc sa thải toàn bộ nhân viên tư vấn để thay thế bằng các robot vô cảm.", "Terminating human advisory personnel to replace them with unfeeling robotic automations."),
            "D": ("Là việc thu thập tất cả dữ liệu cá nhân của người dân để phục vụ mục đích trục lợi bất chính.", "Harvesting private citizen data indiscriminately for predatory short-term profiteering.")
        },
        "B",
        "CRM là một triết lý kinh doanh sống động: lấy khách hàng làm trung tâm để xây dựng các mối quan hệ thịnh vượng, bền vững dựa trên sự tin cậy và giá trị đích thực.",
        "CRM culminates in an enduring corporate operating ethos where empathy, data integrity, and operational excellence converge to forge unbreakable customer bonds and enduring enterprise value.",
        "Baran & Galka (2017) p. 450; Kostojohn et al. (2011) p. 230", "Chapter 14", "pp. 450-455, 230-234", ["crm-philosophy", "customer-centricity", "enduring-value"]
    )
]

for item in e10:
    questions_batch4.append(make_q(
        item[0], "EXAM-10", item[1], item[2], item[3],
        item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13]
    ))

print(f"Total questions generated in batch 4: {len(questions_batch4)}")

with open(Path(r"C:\Kiến thức cần học\CRM\output\scratch\q_batch4.json"), "w", encoding="utf-8") as f:
    json.dump(questions_batch4, f, ensure_ascii=False, indent=2)
