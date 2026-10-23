# Báo Cáo Nâng Cấp Phòng Nghiên Cứu Tình Huống Doanh Nghiệp (Case Study Lab Enhancement Report)

**Dự án:** CRM Bilingual Learning & Practice Hub  
**Tác giả:** Nguyễn Đăng Cẩm Tú (Hazel)  
**Ngày hoàn thành:** 19 tháng 10, 2026  
**Thư mục làm việc:** `C:\Kiến thức cần học\CRM\output`  
**Trạng thái kiểm thử:** 15/15 Kiểm thử Đơn vị Python PASS | 48/48 Kiểm thử Tích hợp Trình duyệt Headless Edge PASS (100%)  

---

## 1. Mục Tiêu & Triết Lý Sư Phạm Nâng Cấp

Phòng Nghiên cứu Tình huống (Case Study Lab) được nâng cấp toàn diện dựa trên 3 nguyên lý sư phạm cốt lõi:

1. **Bảo tồn Tuyệt đối Văn bản Nguồn (Authoritative Source Fidelity):**
   - Không tóm tắt thu gọn hay giản lược làm mất đi tính chân thực của tài liệu học thuật gốc.
   - Toàn bộ 10 tình huống doanh nghiệp được trích xuất nguyên văn tiếng Anh (Verbatim Source) từ 5 tệp PDF tham khảo, với tổng dung lượng **120.682 ký tự tiếng Anh** kết hợp bản dịch tiếng Việt học thuật toàn văn **146.308 ký tự tiếng Việt** (tổng khối lượng văn bản học thuật song ngữ đạt trên 266.000 ký tự).
   - Thiết lập chuẩn xác **2 chế độ đọc độc lập**: `🇬🇧 Tiếng Anh Gốc (Original English)` và `🇻🇳 Bản dịch Tiếng Việt Toàn văn`. Loại bỏ triệt để mọi đoạn trích tiếng Anh thừa trong bản dịch tiếng Việt, cũng như các câu gợi ý lỗi thời `*(Xem toàn bộ bản gốc tiếng Anh ở chế độ song ngữ bên trên)*`.

2. **Rèn Luyện Tư Duy Phản Biện Độc Lập Trước Khi Xem Lời Giải (Independent Critical Thinking First):**
   - Thiết lập **Không gian Phân tích Cá nhân 10 Chiều Chuẩn mực (10-Dimension Learner Workspace)** giúp học viên tiếp cận bài toán kinh doanh như một nhà tư vấn chiến lược thực thụ.
   - **Lời giải mẫu & Khung đánh giá được ẨN MẶC ĐỊNH (Hidden by default)** với thông điệp sư phạm rõ ràng, khuyến khích học viên tự lập luận trước khi mở xem gợi ý đối chiếu.

3. **Cố Vấn Phản Biện AI (AI Socratic Coach & Critical Thinking Partner):**
   - Đóng vai trò người phản biện sắc sảo ("Devil's Advocate"), không đưa đáp án sẵn mà đặt các câu hỏi truy vấn giả định ngầm định, chỉ ra điểm mù, đo lường sự đánh đổi (trade-offs) và ranh giới giữa bằng chứng thực chứng và suy luận chủ quan.
   - Kiến trúc động cơ Socratic nội bộ (Local Socratic Heuristics Engine) chạy offline hoàn toàn miễn phí, minh bạch, bảo vệ dữ liệu tuyệt đối (Zero Credential Leakage).

---

## 2. Bản Đồ 10 Tình Huống Doanh Nghiệp & Tình Trạng Nguồn

| Mã Case | Doanh nghiệp | Tiêu đề Học thuật Gốc | Giáo trình Nguồn | Trang sách | Bản gốc EN | Bản dịch VI | Độ phủ bản dịch | Tình trạng Kiểm định |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `CASE-TESCO-01` | **Tesco PLC** | Customer Orientation at Tesco (Case Study 5) | *Customer Relationship Management* | 173–183 | 19.698 chars | 22.429 chars | 100% Toàn văn | **PASS (Edge Verified)** |
| `CASE-WALMART-01` | **Walmart** | Company Case 8: Walmart's top priority: focus on customer experience & digitized shopping | *Experiential Marketing* | 87–92 | 15.158 chars | 18.105 chars | 100% Toàn văn | **PASS (Edge Verified)** |
| `CASE-IKEA-01` | **IKEA** | Company Case 9: How is Ikea advancing the experience of its customers? | *Experiential Marketing* | 92–98 | 10.333 chars | 12.929 chars | 100% Toàn văn | **PASS (Edge Verified)** |
| `CASE-DISNEY-01` | **The Walt Disney Company** | Company Case 10: How does Disney create a magical customer experience? | *Experiential Marketing* | 102–108 | 9.367 chars | 11.828 chars | 100% Toàn văn | **PASS (Edge Verified)** |
| `CASE-AIRBNB-01` | **Airbnb** | Company Case 11: Airbnb's customer experience is revolutionizing hospitality | *Experiential Marketing* | 108–113 | 10.030 chars | 12.507 chars | 100% Toàn văn | **PASS (Edge Verified)** |
| `CASE-MCDONALD-01` | **McDonald's** | Company Case 12: How is McDonald's improving fast-food experience online and offline? | *Experiential Marketing* | 113–121 | 10.551 chars | 12.739 chars | 100% Toàn văn | **PASS (Edge Verified)** |
| `CASE-CHANEL-01` | **Chanel** | Company Case 13: Chanel: experiential luxury brand that makes fairytale real | *Experiential Marketing* | 126–131 | 10.184 chars | 12.666 chars | 100% Toàn văn | **PASS (Edge Verified)** |
| `CASE-NIKE-01` | **Nike** | Company Case 14: Nike's focus on digitized shopping as integral part of CX | *Experiential Marketing* | 131–143 | 10.538 chars | 12.628 chars | 100% Toàn văn | **PASS (Edge Verified)** |
| `CASE-ESTEE-01` | **Estée Lauder** | Company Case 15: How is Estée Lauder advancing the beauty experience? | *Experiential Marketing* | 143–148 | 10.406 chars | 12.548 chars | 100% Toàn văn | **PASS (Edge Verified)** |
| `CASE-GAFA-SYNTHESIS` | **The Big Four (GAFA)** | Chapter 1: The 'Big Four' digital firms: GAFA and customer experience | *Experiential Marketing* | 2–30 | 14.417 chars | 17.929 chars | 100% Toàn văn | **PASS (Edge Verified)** |

- **Tổng dung lượng văn bản nguyên văn tiếng Anh:** **120.682 ký tự**.
- **Tổng dung lượng bản dịch tiếng Việt học thuật toàn văn:** **146.308 ký tự**.
- **Tỷ lệ bao phủ dịch thuật:** **100% Toàn diện**.
- **Hiện tượng đoạn trích tiếng Anh thừa trong bản dịch tiếng Việt:** **0% (Đã khắc phục triệt để)**.

---

## 3. Kiến Trúc Không Gian Phân Tích Cá Nhân 10 Chiều

Mỗi tình huống cung cấp cho người học một khung làm việc có cấu trúc cao với 10 chiều phân tích chiến lược:

1. **Xác định Vấn đề & Bối cảnh Chiến lược (Strategic Problem & Context):** Nhận diện bài toán cốt lõi, triệu chứng bên ngoài và tác động lên trải nghiệm khách hàng.
2. **Bằng chứng & Dữ liệu Nguồn Thực chứng (Empirical Evidence & Source Data):** Thu thập số liệu, trích dẫn sự kiện có thật trong văn bản nguồn để làm cơ sở cho lập luận.
3. **Các Bên Liên quan & Đa Góc nhìn (Stakeholders & Multi-Perspective Analysis):** Phân tích kỳ vọng và điểm đau của khách hàng, nhân viên tuyến đầu, cấp quản lý và đối tác.
4. **Phân tích Nguyên nhân Gốc rễ (Root Cause Analysis - 5 Whys / Ishikawa):** Đào sâu nguồn gốc vấn đề ở tầng quy trình, văn hóa tổ chức hoặc kiến trúc công nghệ.
5. **Các Phương án Chiến lược Thay thế (Strategic Alternative Options):** Đề xuất 2–3 phương án hành động có tính khả thi và cạnh tranh.
6. **Tiêu chí Đánh giá & So sánh Đánh đổi (Evaluation Criteria & Trade-offs):** Thiết lập tiêu chí so sánh (chi phí, độ phức tạp IT, rủi ro văn hóa, tác động lên CLV).
7. **Khuyến nghị Giải pháp Tối ưu (Optimal Recommendation):** Lựa chọn phương án tối ưu với tuyên bố giá trị và luận cứ bảo vệ sắc bén.
8. **Kế hoạch Triển khai & Lộ trình Thực thi (Phased Implementation Plan):** Xây dựng lộ trình theo các giai đoạn Ngắn hạn – Trung hạn – Dài hạn.
9. **Quản trị Rủi ro, Ma sát Vận hành & Dự phòng (Friction, Trade-offs & Mitigations):** Nhận diện rủi ro thực thi, ma sát tổ chức và xây dựng kế hoạch dự phòng.
10. **Chỉ số Đo lường Thành công (Quantitative Success Metrics & KPIs):** Thiết lập các chỉ số định lượng cụ thể (CSAT, NPS, CLV, Tỷ lệ rời bỏ, Doanh thu trung bình).
- **Ghi chú & Tóm lược Điều hành (Executive Summary):** Tổng hợp thông điệp cốt lõi gửi tới ban lãnh đạo.

### Cơ Chế Lưu Trữ & Đồng Bộ Trạng Thái
- **Tự động lưu với cơ chế Debounce (1.000ms):** Khi người học nhập liệu, trạng thái được cập nhật mượt mà và lưu vào `localStorage['crm_user_progress'].caseWorkspaces[caseId]`. Chỉ số thời gian lưu tự động hiển thị tức thời mà không làm mất con trỏ soạn thảo của người dùng.
- **Tương thích ngược 100% (Backward Compatibility):** Tự động đồng bộ hóa với trường dữ liệu cũ `caseNotes[caseId]`, đảm bảo các ghi chú đã lưu trước đây của người dùng không bao giờ bị mất mát.
- **Xuất Báo cáo Markdown:** Tích hợp nút `📥 Xuất Báo cáo (.md)` cho phép tải về toàn bộ phân tích 10 chiều kèm phản biện AI dưới dạng tài liệu Markdown chuẩn hóa.

---

## 4. Cơ Chế Hiển Thị Tài Liệu & Ẩn Lời Giải Mẫu

### 4.1. Động Cơ Phân Tích & Hiển Thị Tài Liệu Học Thuật (Document Formatting Engine)
- **Hỗ trợ Bảng dữ liệu Markdown chuẩn hóa (`| ... | ... |`):** Trình diễn các bảng phân tích chiến lược, bảng so sánh 5 chiều, bảng 4Ps/5Ps một cách trực quan qua lớp CSS `.study-table-wrap` và `.study-table` theo đúng phong cách Pastel Yellow thanh lịch.
- **Tự động kích hoạt liên kết Web (Active URL Linkification):** Hàm `parseInline` nhận diện tự động các địa chỉ URL học thuật và nguồn kiểm chứng, chuyển hóa thành liên kết ngoài an toàn (`target="_blank" rel="noopener noreferrer"`).
- **Cấu trúc phân cấp tài liệu rõ ràng:** Phân biệt rõ các cấp đề mục `#`, `##`, `###`, `####`, khối trích dẫn học thuật (`> `), đường phân cách ngang (`---`) và danh sách gạch đầu dòng.

### 4.2. Cơ Chế Ẩn Lời Giải Mẫu & Sư Phạm Đối Chiếu
- **Ẩn mặc định (Hidden by default):** Không gian lời giải mẫu không hiển thị ngay khi mở trang.
- **Nút bật mở trực quan (Accessible Disclosure Toggle):** Người học chủ động nhấn `[🔓 Mở xem Gợi ý Phân tích & Lời giải Mẫu]` khi đã sẵn sàng đối chiếu.
- **Biểu ngữ cảnh báo sư phạm (Pedagogical Disclaimer Banner):** Nhắc nhở người học rằng trong quản trị chiến lược không có đáp án duy nhất đúng; lời giải mẫu chỉ là hệ quy chiếu phương pháp luận để người học tự soi chiếu và mài sắc tư duy.

---

## 5. Động Cơ Cố Vấn Phản Biện AI (AI Socratic Coach)

Động cơ Socratic được thiết kế với 2 hành động tương tác chính:
- **`🔍 Đánh giá Toàn diện Bài phân tích` (`Review My Analysis`):** Đánh giá cấu trúc, chiều sâu lập luận và ranh giới bằng chứng.
- **`⚔️ Phản biện & Thử thách Khuyến nghị` (`Challenge My Recommendation`):** Đóng vai trò phản biện, chất vấn tính khả thi và đưa ra kịch bản đối lập.

### 7 Cấu Phần Phản Biện Chuẩn Mực (Sections A–G)
- **Phần A (Strengths):** Điểm sáng trong lập luận, mức độ bao phủ các chiều chiến lược và thuật ngữ CRM chuyên sâu.
- **Phần B (Evidence Grounding):** Phân biệt ranh giới giữa sự kiện định lượng từ tài liệu gốc và suy luận chủ quan; cảnh báo khi thiếu số liệu kiểm chứng.
- **Phần C (Unstated Assumptions):** Bóc tách các giả định ngầm định thiếu cơ sở (ví dụ: ngầm định người dùng sẽ tự động cài app, ngầm định nhân viên không phản kháng).
- **Phần D (Stakeholders):** Đặt bài toán dưới lăng kính của nhân viên tuyến đầu, khách hàng bảo thủ hoặc đối thủ cạnh tranh.
- **Phần E (Trade-offs & Friction):** Phân tích ma sát vận hành và sự đánh đổi (ví dụ: High-Tech vs High-Touch, chi phí IT vs biên lợi nhuận).
- **Phần F (Socratic Probing):** Bộ câu hỏi gợi mở đào sâu từ chuyên gia để người học tự suy ngẫm.
- **Phần G (Next Steps):** Lộ trình 3 bước hành động cụ thể để hoàn thiện bài thuyết trình trước ban điều hành.

---

## 6. Kết Quả Kiểm Thử & Nghiệm Thu Hệ Thống

1. **Kiểm thử Đơn vị Python (15/15 tests PASS):**
   - File kiểm thử: `output/tests/test_hub_validation.py` (11 tests) và `output/tests/test_phase2_state.py` (4 tests).
   - Kiểm tra tính đầy đủ của 10 case, metadata nguồn, các bước quy trình, câu hỏi thảo luận, không có trường trống và dữ liệu đồng bộ với `data-store.js` (1.356.937 bytes).
2. **Kiểm thử Tích hợp Trình duyệt Headless Edge (48/48 Case Tests PASS - 100%):**
   - File kịch bản kiểm thử: `output/scratch/test_browser_case_interactions.html` chạy qua `output/scratch/run_case_edge_test.py`.
   - **Xác thực độ dài & độ đầy đủ bản dịch:** Kiểm chứng độ dài tiếng Anh và tiếng Việt của cả 10 tình huống (Walmart > 15.000 chars EN & 18.000 chars VI, Airbnb > 10.000 chars EN & 12.000 chars VI, Tesco > 19.000 chars EN & 22.000 chars VI, GAFA > 14.000 chars EN & 17.000 chars VI).
   - **Xác thực định dạng tài liệu:** Render bảng Markdown thành HTML `<table class="study-table">`, chuyển đổi URL thành thẻ `<a>` có thể click.
   - **Xác thực sư phạm:** Lời giải mẫu ẩn mặc định (`display: none` trên container); chỉ hiển thị sau khi click nút mở.
   - **Xác thực không gian làm việc 10 chiều:** Nhập liệu và lưu trữ thành công vào `localStorage`, khôi phục chính xác khi chuyển đổi tab/case.
   - **Xác thực động cơ AI Socratic Coach:** Phân tích hoàn chỉnh tạo đủ 7 cấu phần A–G với khuyến nghị chuyên sâu.
   - **Xác thực chuyển đổi ngôn ngữ:** Chuyển đổi giữa Tiếng Việt và English mượt mà, bảo toàn 100% dữ liệu đã nhập.
3. **Kiểm thử Bảo tồn Nhận diện & Nền tảng:**
   - Xác nhận bảo tồn 100% nhận diện tác giả Nguyễn Đăng Cẩm Tú (Hazel), hệ thống Pastel Yellow, 21 chương học tập, 52 thuật ngữ, 40 flashcards, 200 câu hỏi trắc nghiệm và 10 đề thi chuẩn mực.
