import json
from pathlib import Path

fc_path = Path("output/data/flashcards.json")
with open(fc_path, "r", encoding="utf-8") as f:
    cards = json.load(f)

existing_ids = {c["id"] for c in cards}

new_cards = [
    # Domain 1: Foundations & Strategy
    {
        "id": "fc-013",
        "topic": "Strategy",
        "chapter_id": "mod-baran-ch02",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Tại sao chiến lược CRM phải xuất phát từ Chiến lược Kinh doanh Tổng thể thay vì do bộ phận IT khởi xướng đơn độc?",
            "en": "Why must a CRM strategy originate from Corporate Business Strategy rather than being initiated solely by IT?"
        },
        "back": {
            "vi": "Vì CRM là chiến lược định hình lại trải nghiệm khách hàng và tạo lợi thế cạnh tranh; công nghệ chỉ là công cụ hỗ trợ để đạt được các mục tiêu kinh doanh (doanh thu, giữ chân, thị phần).",
            "en": "Because CRM reshapes customer experience to drive competitive advantage; technology is merely an enabler to serve business objectives (revenue, retention, share)."
        },
        "hint": {
            "vi": "Công nghệ phục vụ kinh doanh, không phải ngược lại.",
            "en": "Technology serves business goals, not the other way around."
        },
        "difficulty": "medium",
        "tags": ["strategy", "alignment", "baran-ch2"],
        "source": { "document": "Baran & Galka (2017) pp. 35-42" }
    },
    {
        "id": "fc-014",
        "topic": "Customer Portfolio",
        "chapter_id": "mod-baran-ch03",
        "card_type": "definition_to_term",
        "front": {
            "vi": "Phương pháp phân tích và phân loại cơ sở khách hàng thành các nhóm giá trị khác nhau để phân bổ nguồn lực phục vụ một cách tối ưu được gọi là gì?",
            "en": "What is the strategic methodology of analyzing and segmenting a customer base into value tiers to optimize resource allocation?"
        },
        "back": {
            "vi": "Quản trị Danh mục Khách hàng (Customer Portfolio Management - CPM)",
            "en": "Customer Portfolio Management (CPM)"
        },
        "hint": {
            "vi": "Phân chia khách hàng thành các nhóm như Platinum, Gold, Iron, Lead.",
            "en": "Segments customer base into tiers like Platinum, Gold, Iron, and Lead."
        },
        "difficulty": "medium",
        "tags": ["cpm", "segmentation", "baran-ch3"],
        "source": { "document": "Baran & Galka (2017) pp. 68-75" }
    },
    # Domain 2: Organization & Governance
    {
        "id": "fc-015",
        "topic": "Governance",
        "chapter_id": "mod-fund-ch02",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Vai trò chiến lược quan trọng nhất của Ban Chỉ đạo Dự án CRM (Steering Committee) là gì?",
            "en": "What is the most critical strategic function of the CRM Steering Committee?"
        },
        "back": {
            "vi": "Cung cấp định hướng chiến lược, giải quyết xung đột lợi ích giữa các phòng ban, phê duyệt ngân sách và bảo đảm dự án bám sát mục tiêu kinh doanh dài hạn.",
            "en": "Providing executive strategic vision, resolving cross-silo friction, approving budgets, and keeping the initiative tethered to business objectives."
        },
        "hint": {
            "vi": "Quy tụ lãnh đạo cấp cao để phá vỡ các rào cản phòng ban.",
            "en": "Unites senior leadership to dismantle departmental silos."
        },
        "difficulty": "medium",
        "tags": ["governance", "steering-committee", "kostojohn-ch2"],
        "source": { "document": "Kostojohn et al. (2011) pp. 32-38" }
    },
    {
        "id": "fc-016",
        "topic": "Change Management",
        "chapter_id": "mod-fund-ch02",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Đại sứ phòng ban (Departmental Champions / Super Users) có vai trò gì trong sự thành công của CRM?",
            "en": "What role do Departmental Champions (Super Users) play in CRM implementation success?"
        },
        "back": {
            "vi": "Họ kết hợp hiểu biết nghiệp vụ sâu sắc với uy tín nội bộ, đóng vai trò cầu nối chuyển tải yêu cầu người dùng, huấn luyện đồng nghiệp tại chỗ và thúc đẩy tỷ lệ tiếp nhận (adoption).",
            "en": "They combine deep domain workflow knowledge with peer respect, translating requirements, providing on-the-ground floor coaching, and driving user adoption."
        },
        "hint": {
            "vi": "Những người dùng nòng cốt hỗ trợ đồng nghiệp vượt qua sức ỳ thay đổi.",
            "en": "Respected operational peers who coach colleagues through change resistance."
        },
        "difficulty": "easy",
        "tags": ["champions", "super-users", "adoption", "kostojohn-ch2"],
        "source": { "document": "Kostojohn et al. (2011) pp. 39-43" }
    },
    {
        "id": "fc-017",
        "topic": "Culture",
        "chapter_id": "mod-baran-ch04",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Tác hại nghiêm trọng nhất của hiện tượng 'Ốc đảo phòng ban' (Functional Silos) đối với CRM là gì?",
            "en": "What is the most severe operational harm inflicted by 'Functional Silos' on CRM initiatives?"
        },
        "back": {
            "vi": "Dữ liệu bị phân mảnh giữa Bán hàng, Tiếp thị và Dịch vụ, ngăn cản việc xây dựng Chân dung khách hàng 360 độ (SCV), dẫn đến trải nghiệm khách hàng đứt gãy và mâu thuẫn.",
            "en": "Data is fragmented across Sales, Marketing, and Service silos, preventing a Single Customer View (SCV) and generating jarring, contradictory customer touchpoints."
        },
        "hint": {
            "vi": "Khách hàng phải lặp lại thông tin nhiều lần cho các phòng ban khác nhau.",
            "en": "Forces customers to repeat their history across fragmented touchpoints."
        },
        "difficulty": "medium",
        "tags": ["silos", "scv", "culture", "baran-ch4"],
        "source": { "document": "Baran & Galka (2017) pp. 102-108" }
    },
    # Domain 3: Data Architecture & Analytics
    {
        "id": "fc-018",
        "topic": "Data Architecture",
        "chapter_id": "mod-baran-ch05",
        "card_type": "definition_to_term",
        "front": {
            "vi": "Hồ sơ tổng hợp, nhất quán và phi trùng lặp tập hợp mọi tương tác, giao dịch và lịch sử của khách hàng từ mọi điểm chạm được gọi là gì?",
            "en": "What is the consolidated master profile aggregating all customer transactions, touchpoints, and tickets into a single unified record called?"
        },
        "back": {
            "vi": "Chân dung Khách hàng 360 độ (Single Customer View - SCV)",
            "en": "Single Customer View (SCV / 360-degree view)"
        },
        "hint": {
            "vi": "Góc nhìn toàn cảnh 360 độ về khách hàng.",
            "en": "360-degree view of customer history."
        },
        "difficulty": "easy",
        "tags": ["scv", "data-architecture", "baran-ch5"],
        "source": { "document": "Baran & Galka (2017) pp. 140-148" }
    },
    {
        "id": "fc-019",
        "topic": "Data Hygiene",
        "chapter_id": "mod-baran-ch05",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Tốc độ suy thoái tự nhiên hàng năm của cơ sở dữ liệu khách hàng (Data Decay) là bao nhiêu và do đâu?",
            "en": "What is the average annual natural Customer Data Decay rate and what drives it?"
        },
        "back": {
            "vi": "Khoảng 15% đến 20% mỗi năm do thay đổi địa chỉ chỗ ở, chuyển đổi công tác, đổi số điện thoại, kết hôn hoặc qua đời.",
            "en": "Approximately 15% to 20% annually, driven by residential moves, career transitions, phone changes, marital status shifts, or death."
        },
        "hint": {
            "vi": "Từ 15 đến 20% dữ liệu biến thành 'dữ liệu chết' nếu không làm sạch.",
            "en": "15–20% of contact records degrade naturally every single year."
        },
        "difficulty": "medium",
        "tags": ["data-decay", "data-hygiene", "baran-ch5"],
        "source": { "document": "Baran & Galka (2017) pp. 150-155" }
    },
    {
        "id": "fc-020",
        "topic": "Analytics",
        "chapter_id": "mod-baran-ch07",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Trong mô hình RFM, biến số nào có trọng số dự báo cao nhất về khả năng khách hàng sẽ tiếp tục mua hàng trong tương lai gần?",
            "en": "In the RFM segmentation framework, which variable carries the highest predictive weight for immediate future purchase propensity?"
        },
        "back": {
            "vi": "Tính gần đây của giao dịch (Recency - R): khách hàng vừa mua gần đây luôn có xác suất phản hồi cao hơn nhiều so với khách hàng đã lâu không tương tác.",
            "en": "Recency (R): accounts that purchased most recently demonstrate dramatically higher response rates than dormant past spenders."
        },
        "hint": {
            "vi": "Chữ R trong RFM.",
            "en": "The 'R' in RFM."
        },
        "difficulty": "medium",
        "tags": ["rfm", "recency", "predictive-analytics", "baran-ch7"],
        "source": { "document": "Baran & Galka (2017) pp. 214-219" }
    },
    # Domain 4: Technology & Architecture
    {
        "id": "fc-021",
        "topic": "Technology",
        "chapter_id": "mod-fund-ch04",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Sự khác biệt cốt lõi giữa 'Cấu hình' (Configuration) và 'Tùy biến' (Customization) trong công nghệ CRM là gì?",
            "en": "What is the key technical difference between 'Configuration' and 'Customization' in CRM platforms?"
        },
        "back": {
            "vi": "Cấu hình là điều chỉnh các thiết lập sẵn có bằng giao diện kéo thả không cần code; Tùy biến là viết thêm mã nguồn tùy biến mở rộng tính năng ngoài giới hạn mặc định.",
            "en": "Configuration adjusts built-in declarative settings without code; Customization involves writing proprietary code to extend capabilities beyond native limits."
        },
        "hint": {
            "vi": "Cấu hình = Declarative; Tùy biến = Custom Code.",
            "en": "Configuration = declarative clicks; Customization = writing custom code."
        },
        "difficulty": "medium",
        "tags": ["configuration", "customization", "technical-debt", "kostojohn-ch4"],
        "source": { "document": "Kostojohn et al. (2011) pp. 104-107" }
    },
    {
        "id": "fc-022",
        "topic": "Architecture",
        "chapter_id": "mod-baran-ch06",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Đặc trưng then chốt của Kiến trúc Đa người thuê (Multi-Tenant Architecture) trong Cloud CRM là gì?",
            "en": "What is the defining characteristic of Multi-Tenant Architecture in Cloud CRM?"
        },
        "back": {
            "vi": "Nhiều tổ chức khách hàng cùng dùng chung một phiên bản ứng dụng và hạ tầng phần cứng, nhưng dữ liệu của từng khách hàng được phân tách logic an toàn tuyệt đối.",
            "en": "Multiple client organizations share a common application instance and underlying hardware, while each company's data remains logically segregated and secured."
        },
        "hint": {
            "vi": "Dùng chung hạ tầng nhưng phân tách dữ liệu bảo mật.",
            "en": "Shared infrastructure with strict logical data isolation."
        },
        "difficulty": "hard",
        "tags": ["multi-tenancy", "cloud-crm", "architecture", "baran-ch6"],
        "source": { "document": "Baran & Galka (2017) pp. 180-184" }
    },
    # Domain 5: Roadmap & Planning
    {
        "id": "fc-023",
        "topic": "Implementation Planning",
        "chapter_id": "mod-fund-ch05",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Tại sao triển khai phân kỳ (Phased Rollout) luôn được ưu tiên hơn phương pháp triển khai toàn bộ cùng lúc (Big Bang)?",
            "en": "Why is a Phased Rollout strategy preferred over a 'Big Bang' deployment in enterprise CRM?"
        },
        "back": {
            "vi": "Giảm thiểu rủi ro vận hành, sớm mang lại giá trị thấy được (Quick Wins), tạo điều kiện tiếp thu phản hồi thực tế từ người dùng và điều chỉnh lộ trình kịp thời.",
            "en": "Isolates operational risk, delivers early quick wins, incorporates user feedback continuously, and allows roadmap adjustments before full deployment."
        },
        "hint": {
            "vi": "Chia nhỏ để kiểm soát rủi ro và đạt thắng lợi sớm.",
            "en": "De-risks implementation and delivers iterative early wins."
        },
        "difficulty": "easy",
        "tags": ["phased-rollout", "big-bang", "risk-management", "kostojohn-ch5"],
        "source": { "document": "Kostojohn et al. (2011) pp. 128-134" }
    },
    {
        "id": "fc-024",
        "topic": "Project Governance",
        "chapter_id": "mod-fund-ch05",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Hiện tượng 'Phình phạm vi' (Scope Creep) trong dự án CRM là gì và làm thế nào để kiểm soát nó?",
            "en": "What is 'Scope Creep' in CRM projects and how is it rigorously controlled?"
        },
        "back": {
            "vi": "Sự gia tăng không kiểm soát của các yêu cầu tính năng mới ngoài kế hoạch ban đầu; kiểm soát bằng quy trình Quản lý Yêu cầu Thay đổi chính thức (Formal Change Control) do Ban Chỉ đạo phê duyệt.",
            "en": "Uncontrolled expansion of project requirements beyond original budget and schedule; managed through a formal Change Control process governed by the Steering Committee."
        },
        "hint": {
            "vi": "Các yêu cầu mới phải đưa vào Backlog đánh giá tác động thay vì làm ngay.",
            "en": "New feature requests must be vetted in backlogs, not added ad-hoc."
        },
        "difficulty": "medium",
        "tags": ["scope-creep", "change-control", "governance", "kostojohn-ch5"],
        "source": { "document": "Kostojohn et al. (2011) pp. 136-141" }
    },
    # Domain 6: Execution & Testing
    {
        "id": "fc-025",
        "topic": "Testing",
        "chapter_id": "mod-fund-ch06",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Mục tiêu tối hậu của Kiểm thử Chấp nhận Người dùng (User Acceptance Testing - UAT) là gì?",
            "en": "What is the primary objective of User Acceptance Testing (UAT) in CRM rollout?"
        },
        "back": {
            "vi": "Để người dùng nghiệp vụ thực tế xác nhận hệ thống hỗ trợ chính xác và đầy đủ các quy trình công việc hàng ngày của họ trước khi ký biên bản nghiệm thu đưa vào vận hành.",
            "en": "To allow business end-users to validate that configured workflows faithfully support daily operational duties before signing off on live production launch."
        },
        "hint": {
            "vi": "Xác nhận của người dùng nghiệp vụ, không phải của lập trình viên.",
            "en": "Business validation and operational sign-off by real end-users."
        },
        "difficulty": "medium",
        "tags": ["uat", "testing", "sign-off", "kostojohn-ch6"],
        "source": { "document": "Kostojohn et al. (2011) pp. 165-170" }
    },
    {
        "id": "fc-026",
        "topic": "Launch Management",
        "chapter_id": "mod-fund-ch06",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Cuộc họp Go/No-Go Decision Gate trước ngày Golive CRM dựa trên các tiêu chí cốt lõi nào?",
            "en": "On what criteria is the executive Go/No-Go Decision Gate determined prior to CRM go-live?"
        },
        "back": {
            "vi": "Không còn lỗi nghiêm trọng cấp độ 1 (Severity 1 / Blocker bugs), kết quả UAT được ký duyệt 100%, nạp dữ liệu delta sẵn sàng, và kế hoạch hỗ trợ Hypercare đã sẵn sàng.",
            "en": "Zero open Severity-1 blocker bugs, signed UAT certificates, validated delta migration readiness, and active hypercare floor support staffing."
        },
        "hint": {
            "vi": "0 lỗi Sev-1, UAT pass, Data ready, Hypercare ready.",
            "en": "Zero blocker bugs and full operational sign-off."
        },
        "difficulty": "hard",
        "tags": ["go-no-go", "hypercare", "cutover", "kostojohn-ch6"],
        "source": { "document": "Kostojohn et al. (2011) pp. 172-176" }
    },
    # Domain 7: Loyalty & Retention
    {
        "id": "fc-027",
        "topic": "Loyalty",
        "chapter_id": "mod-baran-ch09",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Nghịch lý Khắc phục Dịch vụ (Service Recovery Paradox) là gì?",
            "en": "What is the Service Recovery Paradox?"
        },
        "back": {
            "vi": "Khách hàng gặp sự cố dịch vụ nhưng sau đó được doanh nghiệp xử lý thỏa đáng và đền bù vượt mong đợi có thể trở nên trung thành và hài lòng hơn cả khách hàng chưa từng gặp sự cố.",
            "en": "A customer who experiences a service failure that is resolved exceptionally well can develop higher loyalty and satisfaction than if no failure had occurred at all."
        },
        "hint": {
            "vi": "Sự cố được giải quyết xuất sắc tạo ra niềm tin sâu sắc hơn.",
            "en": "Masterful recovery can forge deeper bonds than zero-defect history."
        },
        "difficulty": "medium",
        "tags": ["service-recovery", "paradox", "complaints", "baran-ch9"],
        "source": { "document": "Baran & Galka (2017) pp. 290-295" }
    },
    {
        "id": "fc-028",
        "topic": "Metrics",
        "chapter_id": "mod-baran-ch09",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Điểm số Nỗ lực của Khách hàng (Customer Effort Score - CES) đo lường điều gì và có tác động ra sao đến việc giữ chân?",
            "en": "What does Customer Effort Score (CES) measure and how does it relate to retention?"
        },
        "back": {
            "vi": "Đo mức độ dễ dàng mà khách hàng trải qua khi giải quyết sự cố; nghiên cứu chứng minh giảm thiểu nỗ lực của khách hàng giữ chân khách hiệu quả hơn cố gắng gây bất ngờ.",
            "en": "Measures ease of issue resolution; research shows minimizing customer effort builds loyalty far more effectively than attempting to delight customers."
        },
        "hint": {
            "vi": "Làm cho mọi thứ trở nên nhẹ nhàng, không tốn sức (Effortless).",
            "en": "Effortless experience prevents customer defection."
        },
        "difficulty": "medium",
        "tags": ["ces", "effortless-experience", "metrics", "baran-ch9"],
        "source": { "document": "Baran & Galka (2017) pp. 285-288" }
    },
    {
        "id": "fc-029",
        "topic": "Retention Economics",
        "chapter_id": "mod-baran-ch10",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Theo nghiên cứu của Reichheld & Sasser, tăng tỷ lệ giữ chân khách hàng thêm 5% có thể giúp tăng lợi nhuận bao nhiêu?",
            "en": "According to Reichheld & Sasser, a 5% increase in customer retention can boost profits by how much?"
        },
        "back": {
            "vi": "Từ 25% đến 95%, nhờ chi phí phục vụ khách hàng cũ giảm, giao dịch định kỳ tăng và giới thiệu khách hàng mới miễn phí.",
            "en": "Between 25% and 95%, driven by lower servicing costs, recurring purchases, price premiums, and zero-cost referrals."
        },
        "hint": {
            "vi": "Đòn bẩy lợi nhuận từ 25% đến 95%.",
            "en": "Leverage of 25% to 95% profit surge."
        },
        "difficulty": "hard",
        "tags": ["retention-economics", "reichheld", "profit-leverage", "baran-ch10"],
        "source": { "document": "Baran & Galka (2017) pp. 310-316" }
    },
    # Domain 8: B2B CRM
    {
        "id": "fc-030",
        "topic": "B2B CRM",
        "chapter_id": "mod-baran-ch08",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Trung tâm Mua hàng (Buying Center / DMU) trong B2B bao gồm 6 vai trò tiêu biểu nào?",
            "en": "What are the six typical stakeholder roles comprising an enterprise Buying Center (DMU)?"
        },
        "back": {
            "vi": "1. Người khởi xướng (Initiator)\n2. Người sử dụng (User)\n3. Người ảnh hưởng (Influencer)\n4. Người gác cổng (Gatekeeper)\n5. Người quyết định (Decider)\n6. Người mua/đàm phán (Buyer)",
            "en": "1. Initiator\n2. User\n3. Influencer\n4. Gatekeeper\n5. Decider\n6. Buyer"
        },
        "hint": {
            "vi": "6 vai trò từ người đề xuất, thẩm định kỹ thuật, duyệt giá đến ký hợp đồng.",
            "en": "6 roles spanning user need, technical review, budget approval, and contract signing."
        },
        "difficulty": "medium",
        "tags": ["buying-center", "dmu", "b2b-crm", "baran-ch8"],
        "source": { "document": "Baran & Galka (2017) pp. 238-245" }
    },
    {
        "id": "fc-031",
        "topic": "B2B Metrics",
        "chapter_id": "mod-baran-ch08",
        "card_type": "definition_to_term",
        "front": {
            "vi": "Chỉ số đo lường tỷ lệ phần trăm doanh thu định kỳ được duy trì và tăng trưởng từ nhóm khách hàng hiện tại (bao gồm mở rộng trừ đi thu hẹp và rời bỏ) được gọi là gì?",
            "en": "What metric measures the percentage of recurring revenue retained from existing accounts, factoring expansions minus churn?"
        },
        "back": {
            "vi": "Tỷ lệ Duy trì Doanh thu Ròng (Net Revenue Retention - NRR / Net Dollar Retention)",
            "en": "Net Revenue Retention (NRR / Net Dollar Retention)"
        },
        "hint": {
            "vi": "Thước đo vàng của mô hình SaaS; NRR > 100% chứng minh doanh nghiệp tự tăng trưởng.",
            "en": "Gold standard SaaS metric; NRR > 100% indicates organic expansion."
        },
        "difficulty": "hard",
        "tags": ["nrr", "b2b-metrics", "saas", "baran-ch8"],
        "source": { "document": "Baran & Galka (2017) pp. 252-256" }
    },
    # Domain 9: Omnichannel & Social CRM
    {
        "id": "fc-032",
        "topic": "Omnichannel",
        "chapter_id": "mod-baran-ch13",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Sự khác biệt bản chất giữa Multichannel và Omnichannel là gì?",
            "en": "What is the core distinction between Multichannel and Omnichannel?"
        },
        "back": {
            "vi": "Multichannel vận hành các kênh riêng rẽ độc lập; Omnichannel tích hợp liền mạch toàn bộ các kênh thành một trải nghiệm duy nhất với dữ liệu và ngữ cảnh đồng bộ thời gian thực.",
            "en": "Multichannel operates isolated touchpoint silos; Omnichannel orchestrates all touchpoints into a unified customer journey with synchronized real-time data."
        },
        "hint": {
            "vi": "Multichannel = Nhiều kênh tách rời; Omnichannel = Hợp nhất liền mạch.",
            "en": "Multichannel = separate channels; Omnichannel = unified continuous journey."
        },
        "difficulty": "easy",
        "tags": ["omnichannel", "multichannel", "seamless", "baran-ch13"],
        "source": { "document": "Baran & Galka (2017) pp. 402-408" }
    },
    {
        "id": "fc-033",
        "topic": "Case Application",
        "chapter_id": "mod-baran-ch13",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Trong tình huống Disney MyMagic+, chiếc vòng MagicBand minh họa nguyên lý Omnichannel IoT nào?",
            "en": "In the Disney MyMagic+ case, how does the MagicBand illustrate Omnichannel IoT principles?"
        },
        "back": {
            "vi": "Hợp nhất mọi điểm chạm (chìa khóa phòng, vé vào cổng, thanh toán không chạm, FastPass) vào một thiết bị IoT duy nhất, loại bỏ hoàn toàn ma sát xếp hàng và cá nhân hóa trải nghiệm theo thời gian thực.",
            "en": "Consolidates all touchpoints (room key, park ticket, payment, FastPass) into a single IoT device, eliminating queue friction and personalizing park magic in real time."
        },
        "hint": {
            "vi": "Trải nghiệm không ma sát (Frictionless Experience) qua IoT.",
            "en": "Frictionless experience orchestrating physical resort spaces."
        },
        "difficulty": "hard",
        "tags": ["disney-case", "magicband", "iot", "omnichannel"],
        "source": { "document": "Experiential Marketing (Batat) pp. 102-108" }
    },
    # Domain 10: Metrics, Privacy & Maintenance
    {
        "id": "fc-034",
        "topic": "Metrics",
        "chapter_id": "mod-baran-ch11",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Tại sao chỉ số dẫn dắt (Leading Indicators) lại quan trọng hơn chỉ số kết quả (Lagging Indicators) trong điều hành CRM hàng ngày?",
            "en": "Why are Leading Indicators more vital than Lagging Indicators for day-to-day CRM operational management?"
        },
        "back": {
            "vi": "Chỉ số kết quả (doanh thu, churn) là kết quả đã rồi trong quá khứ không thể thay đổi; chỉ số dẫn dắt (tần suất liên hệ, dữ liệu hoàn thiện, mức độ đăng nhập) là hành vi dự báo có thể tác động và điều chỉnh kịp thời.",
            "en": "Lagging metrics (revenue, churn) reflect past outcomes that cannot be undone; leading metrics (login rate, profile completeness, response velocity) provide steerable predictive signals."
        },
        "hint": {
            "vi": "Chỉ số dẫn dắt giúp can thiệp chủ động trước khi kết quả xấu xảy ra.",
            "en": "Leading signals allow proactive steering before financial losses materialize."
        },
        "difficulty": "medium",
        "tags": ["leading-indicators", "lagging-indicators", "metrics", "baran-ch11"],
        "source": { "document": "Baran & Galka (2017) pp. 350-355" }
    },
    {
        "id": "fc-035",
        "topic": "Privacy & GDPR",
        "chapter_id": "mod-baran-ch12",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "'Quyền được lãng quên' (Right to be Forgotten) theo chuẩn GDPR đặt ra yêu cầu kỹ thuật nào cho kiến trúc CRM?",
            "en": "What technical requirement does GDPR's 'Right to be Forgotten' mandate for CRM architectures?"
        },
        "back": {
            "vi": "Hệ thống phải có khả năng xóa bỏ hoặc ẩn danh hóa vĩnh viễn toàn bộ dữ liệu định danh cá nhân của khách hàng trên tất cả các bảng cơ sở dữ liệu liên kết khi nhận được yêu cầu hợp lệ.",
            "en": "The system must support cascading permanent erasure or anonymization of all personal identifiable data across all relational tables upon verified customer request."
        },
        "hint": {
            "vi": "Xóa sạch dữ liệu cá nhân trên mọi bảng liên kết khi khách hàng yêu cầu.",
            "en": "Permanent cascading data erasure upon request."
        },
        "difficulty": "hard",
        "tags": ["gdpr", "right-to-be-forgotten", "privacy", "baran-ch12"],
        "source": { "document": "Baran & Galka (2017) pp. 380-388" }
    },
    {
        "id": "fc-036",
        "topic": "Ethics",
        "chapter_id": "mod-baran-ch12",
        "card_type": "definition_to_term",
        "front": {
            "vi": "Các thủ thuật thiết kế giao diện cố tình đánh lừa hoặc thao túng người dùng thực hiện các hành động bất lợi cho họ (như tự động gia hạn, khó hủy tài khoản) được gọi là gì?",
            "en": "What are deceptive UI/UX designs engineered to trick users into unintended actions (e.g., hidden subscriptions, cancellation mazes) called?"
        },
        "back": {
            "vi": "Mẫu Thiết kế Giao diện Đen (Dark Patterns)",
            "en": "Dark Patterns"
        },
        "hint": {
            "vi": "Thiết kế giao diện mang tính thao túng, phi đạo đức.",
            "en": "Manipulative and deceptive digital interface patterns."
        },
        "difficulty": "easy",
        "tags": ["dark-patterns", "ethics", "ux", "baran-ch12"],
        "source": { "document": "Baran & Galka (2017) pp. 390-395" }
    },
    {
        "id": "fc-037",
        "topic": "Maintenance",
        "chapter_id": "mod-fund-ch07",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Quy tắc cách ly môi trường nghiêm ngặt trong quản trị phát hành (Release Management) CRM quy định điều gì?",
            "en": "What rule governs strict environment isolation in CRM Release Management?"
        },
        "back": {
            "vi": "Nghiêm cấm viết code hoặc chỉnh sửa cấu hình trực tiếp trên môi trường vận hành thật (Live Production); mọi thay đổi phải đi qua chu trình: Sandbox (Dev) -> UAT (Kiểm thử) -> Scheduled Production Release.",
            "en": "Prohibits developing directly on live production; all code and configurations must progress through isolated tiers: Sandbox (Dev) -> UAT (Testing) -> Scheduled Production Release."
        },
        "hint": {
            "vi": "Không bao giờ code trực tiếp trên Production.",
            "en": "Never build or test directly on live Production."
        },
        "difficulty": "medium",
        "tags": ["release-management", "sandbox", "governance", "kostojohn-ch7"],
        "source": { "document": "Kostojohn et al. (2011) pp. 215-222" }
    },
    {
        "id": "fc-038",
        "topic": "Governance",
        "chapter_id": "mod-fund-ch07",
        "card_type": "definition_to_term",
        "front": {
            "vi": "Hội đồng liên phòng ban chịu trách nhiệm đánh giá, ưu tiên và phê duyệt các yêu cầu thay đổi tính năng sau khi hệ thống CRM đã đi vào vận hành được gọi là gì?",
            "en": "What is the cross-functional body responsible for reviewing, prioritizing, and approving post-launch CRM enhancement requests called?"
        },
        "back": {
            "vi": "Hội đồng Cố vấn Thay đổi (Change Advisory Board - CAB)",
            "en": "Change Advisory Board (CAB)"
        },
        "hint": {
            "vi": "Viết tắt là CAB.",
            "en": "Abbreviated as CAB."
        },
        "difficulty": "medium",
        "tags": ["cab", "governance", "change-advisory-board", "kostojohn-ch7"],
        "source": { "document": "Kostojohn et al. (2011) pp. 218-223" }
    },
    {
        "id": "fc-039",
        "topic": "Service Operations",
        "chapter_id": "mod-baran-ch11",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Tại sao việc áp đặt KPI giảm Thời gian Xử lý Trung bình (AHT) một cách máy móc lại gây nguy hiểm cho trải nghiệm khách hàng?",
            "en": "Why can rigidly imposing Average Handle Time (AHT) reduction targets damage customer experience?"
        },
        "back": {
            "vi": "Khiến nhân viên vội vàng cúp máy, giải quyết hời hợt hoặc chuyển cuộc gọi để đạt KPI thời gian, khiến gốc rễ vấn đề không được giải quyết và khách hàng phải gọi lại nhiều lần.",
            "en": "Forces reps to rush callers, dismiss nuance, or bounce tickets to meet minute quotas, leaving root issues unresolved and triggering repeat customer complaints."
        },
        "hint": {
            "vi": "Nhanh chưa chắc đã tốt nếu không giải quyết dứt điểm vấn đề (FCR).",
            "en": "Speed without resolution quality degrades overall customer satisfaction."
        },
        "difficulty": "hard",
        "tags": ["aht", "kpi", "contact-center", "baran-ch11"],
        "source": { "document": "Baran & Galka (2017) pp. 356-360" }
    },
    {
        "id": "fc-040",
        "topic": "CRM Philosophy",
        "chapter_id": "mod-baran-ch14",
        "card_type": "concept_to_explanation",
        "front": {
            "vi": "Đích đến tối hậu của một chiến lược CRM thành công là gì?",
            "en": "What is the ultimate destination of an authentic CRM journey?"
        },
        "back": {
            "vi": "CRM không phải là một dự án công nghệ có điểm dừng; đó là một cam kết chiến lược và văn hóa tổ chức liên tục tiến hóa, lấy khách hàng làm trung tâm để kiến tạo giá trị thịnh vượng bền vững cho cả khách hàng và doanh nghiệp.",
            "en": "CRM is not a one-off IT project with a finish line; it is an enduring strategic commitment and evolving culture uniting people, process, and technology to co-create sustainable mutual value."
        },
        "hint": {
            "vi": "CRM là một hành trình liên tục, không phải là đích đến tĩnh.",
            "en": "An ongoing cultural and strategic commitment, not a static software tool."
        },
        "difficulty": "easy",
        "tags": ["crm-philosophy", "customer-centricity", "baran-ch14", "kostojohn-ch7"],
        "source": { "document": "Baran & Galka (2017) p. 450; Kostojohn (2011) p. 230" }
    }
]

added_fc = 0
for nc in new_cards:
    if nc["id"] not in existing_ids:
        cards.append(nc)
        existing_ids.add(nc["id"])
        added_fc += 1

with open(fc_path, "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print(f"Added {added_fc} new flashcards. Total flashcards now: {len(cards)}")
