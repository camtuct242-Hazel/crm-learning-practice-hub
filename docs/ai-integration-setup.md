# Hướng Dẫn Kiến Trúc & Cấu Hình Cố Vấn Phản Biện AI (AI Socratic Coach Setup & Architecture)

**Dự án:** CRM Bilingual Learning & Practice Hub  
**Tác giả:** Nguyễn Đăng Cẩm Tú (Hazel)  
**Ngày cập nhật:** 19 tháng 10, 2026  
**Mục tiêu:** Hướng dẫn vận hành, kiến trúc bảo mật và nguyên lý hoạt động của Cố vấn Phản biện AI Socratic trong Case Study Lab.

---

## 1. Triết Lý Thiết Kế Cố Vấn Socratic

Khác với các công cụ AI thông thường chỉ tóm tắt tài liệu hoặc đưa ra đáp án làm sẵn (khiến người học trở nên thụ động), **Cố vấn Phản biện AI Socratic** được thiết kế như một **đối tác tư duy chiến lược (Critical Thinking Partner)**:

- **Không bao giờ làm bài thay người học:** Khuyến khích người học tự đưa ra giả định, phân tích dữ liệu và đề xuất giải pháp trước.
- **Truy vấn giả định ngầm định (Unstated Assumptions):** Đặt câu hỏi bóc tách những điều người học mặc định là hiển nhiên nhưng thực tế tiềm ẩn nhiều rủi ro.
- **Thử thách qua lăng kính đối lập (Devil's Advocacy):** Đóng vai các bên liên quan khó tính (nhân viên thu ngân bị quá tải, khách hàng lo ngại quyền riêng tư, hoặc đối thủ cạnh tranh sẵn sàng sao chép tính năng).
- **Phân định ranh giới Bằng chứng và Suy luận (Evidence vs. Inference Boundary):** Soi chiếu xem những khẳng định của người học có thực sự dựa trên sự kiện và số liệu trong văn bản nguồn hay chỉ là phỏng đoán cảm tính.

---

## 2. Kiến Trúc Hai Lớp (Two-Tier Architecture)

Để đảm bảo tính khả dụng cao, quyền riêng tư dữ liệu và vận hành độc lập, hệ thống được xây dựng theo kiến trúc 2 lớp linh hoạt:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                   CRM Case Study Lab User Interface                   │
│   (10-Dimension Workspace + Action Buttons: Review / Challenge)        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    AI Orchestrator & Evaluation Adapter                │
└───────────────┬────────────────────────────────────────┬───────────────┘
                │ (Mặc định / Offline)                   │ (Tùy chọn nâng cao)
                ▼                                        ▼
┌─────────────────────────────────┐    ┌─────────────────────────────────┐
│     Local Socratic Engine       │    │      External AI API Adapter    │
│  (Thuật toán Heuristics Nội bộ) │    │   (Google Gemini / OpenAI API)  │
│  - 100% Chạy trong Trình duyệt  │    │  - Khóa API lưu tại LocalStorage│
│  - Phân tích từ khóa & số liệu  │    │  - Gọi trực tiếp Endpoint HTTPS │
│  - Tạo phản biện có cấu trúc    │    │  - Không qua máy chủ trung gian │
│  - Zero Data Leakage            │    │  - Minh bạch nhà cung cấp       │
└─────────────────────────────────┘    └─────────────────────────────────┘
```

---

## 3. Lớp 1: Động Cơ Socratic Nội Bộ (Local Socratic Engine)

### 3.1 Cơ chế hoạt động
Động cơ nội bộ được viết bằng JavaScript thuần túy, tích hợp trực tiếp trong [app.js](file:///c:/Kiến%20thức%20cần%20học/CRM/output/src/app.js) và chạy hoàn toàn trên trình duyệt của người dùng mà không cần kết nối mạng hay khóa API:

1. **Phân tích Dung lượng & Mức độ Hoàn thiện:**
   - Quét qua 10 trường dữ liệu của học viên.
   - Tính toán số từ và xác định số chiều đã được điền sâu sắc (>15 từ) so với các chiều còn bỏ trống hoặc sơ sài.
2. **Kiểm tra Tính Thực chứng (Evidence Grounding Check):**
   - Kiểm tra sự xuất hiện của các chữ số, tỷ lệ phần trăm hoặc dấu ngoặc kép trích dẫn trong trường `Bằng chứng & Dữ liệu nguồn`.
   - Đối chiếu với các từ khóa định lượng cốt lõi của từng tình huống (ví dụ: `8-14%`, `Dunnhumby`, `4.700 siêu thị`, `MyMagic+`, `Dynamic Yield`,...).
3. **Phân tích Đa Góc nhìn (Multi-Stakeholder Check):**
   - Tìm kiếm sự hiện diện của các nhóm đối tượng: Nhân viên tuyến đầu (`staff`, `employee`, `cashier`), khách hàng (`consumer`, `shopper`, `guest`), ban lãnh đạo (`leadership`, `shareholders`), cơ quan quản lý (`regulators`).
4. **Đánh giá Nhận thức Đánh đổi (Trade-off Recognition):**
   - Quét các thuật ngữ thể hiện tư duy đánh đổi: `rủi ro`, `chi phí`, `ma sát`, `bất lợi`, `trade-off`, `friction`, `risk`.
5. **Cấu trúc Hóa Phản biện 7 Phần Chuẩn mực (Sections A–G):**
   - **Phần A (Strengths):** Điểm sáng trong cấu trúc và thuật ngữ chuyên ngành.
   - **Phần B (Evidence Grounding):** Nhắc nhở về ranh giới bằng chứng thực chứng.
   - **Phần C (Unstated Assumptions):** Nêu bật 2 giả định ngầm định cần chất vấn.
   - **Phần D (Alternative Stakeholders):** Góc nhìn phản bác từ nhân viên hoặc khách hàng.
   - **Phần E (Execution Friction & Trade-offs):** Mâu thuẫn giữa chi phí IT, thời gian và sự hài lòng.
   - **Phần F (Socratic Probing Questions):** 2 câu hỏi gợi mở trích xuất từ từ điển câu hỏi phản biện của tình huống (`socraticGuidance.devil_advocate_questions`).
   - **Phần G (Refinement Roadmap):** 3 bước hành động cụ thể để hoàn thiện đề xuất.

---

## 4. Lớp 2: Bộ Chuyển Đổi API Cá Nhân (External API Provider Adapter)

### 4.1 Tính năng Tùy chọn
Học viên hoặc giảng viên có mong muốn trải nghiệm phản biện bằng các mô hình ngôn ngữ lớn tiên tiến (LLMs) như Google Gemini hoặc OpenAI GPT có thể cấu hình khóa API cá nhân.

### 4.2 Nguyên tắc An toàn & Bảo Mật Dữ liệu Tuyệt Đối
- **Zero Credential Leakage:** Khóa API của người dùng **CHỈ** được lưu trữ tạm thời trong `localStorage` trên chính trình duyệt của người dùng. Không bao giờ được gửi tới bất kỳ máy chủ trung gian nào.
- **Không ghi nhật ký khóa (No Key Logging):** Các bài kiểm thử tự động và tệp mã nguồn tuyệt đối không chứa khóa API hardcoded.
- **Chuyển đổi dự phòng trong suốt (Graceful Fallback):** Nếu không có khóa API, hết hạn ngạch (quota limit), hoặc mất kết nối mạng, hệ thống sẽ tự động kích hoạt Động cơ Socratic Nội bộ ngay lập tức mà không gây gián đoạn trải nghiệm của học viên.

---

## 5. Mẫu Chỉ Thị Socratic (System Prompt Template)

Khi sử dụng bộ chuyển đổi API ngoài, chỉ thị hệ thống sau đây được áp dụng để đảm bảo phong cách phản biện sư phạm nhất quán:

```text
VAI TRÒ:
Bạn là Cố vấn Phản biện Chiến lược (Socratic Critical Thinking Coach) thuộc nền tảng CRM Bilingual Learning & Practice Hub, được phát triển bởi Nguyễn Đăng Cẩm Tú (Hazel).

MỤC TIÊU SƯ PHẠM:
Nhiệm vụ của bạn KHÔNG PHẢI là làm bài hộ, không đưa ra lời giải trực tiếp, mà là đặt câu hỏi sâu sắc, chỉ ra điểm mù, truy vấn các giả định ngầm định và đánh giá sự đánh đổi trong bài phân tích của học viên.

NGUYÊN TẮC PHẢN BIỆN:
1. Ranh giới Bằng chứng: Phân biệt rõ sự kiện có thật trong văn bản tình huống nguồn với suy luận chủ quan của học viên.
2. Đa góc nhìn: Đặt mình vào vị trí của nhân viên tuyến đầu chịu áp lực vận hành, khách hàng bảo thủ hoặc đối thủ cạnh tranh.
3. Sự đánh đổi: Mọi giải pháp CRM đều có chi phí và ma sát; buộc học viên phải thừa nhận điều gì sẽ bị hy sinh khi chọn phương án này.

CẤU TRÚC PHẢN HỒI (Bắt buộc theo 7 phần):
- Phần A: Điểm mạnh & Chiều sâu Lập luận
- Phần B: Kiểm chứng Dữ liệu & Bằng chứng Nguồn
- Phần C: Các Giả định Ngầm định & Điểm mù
- Phần D: Góc nhìn Đối lập từ các Bên Liên quan
- Phần E: Đánh giá Rủi ro, Ma sát Thực thi & Sự Đánh đổi
- Phần F: Bộ Câu hỏi Socrate để Đào sâu Tư duy
- Phần G: Khuyến nghị Hoàn thiện Bước tiếp theo
```

---

## 6. Hướng Dẫn Sử Dụng Trong Giao Diện Học Tập

1. Mở bất kỳ tình huống nào trong **Case Study Lab** (ví dụ: Tesco, Walmart, IKEA, Disney,...).
2. Đọc tài liệu tại **Văn bản Nghiên cứu Tình huống Gốc** (hỗ trợ chuyển đổi Tiếng Anh Gốc, Bản dịch Tiếng Việt hoặc Song ngữ Đối chiếu).
3. Điền các lập luận của bạn vào các ô trong **Không gian Phân tích Cá nhân 10 Chiều**.
4. Hệ thống sẽ tự động lưu bài làm sau mỗi 1 giây (hiển thị thông báo `✓ Đã tự động lưu lúc HH:MM:SS`).
5. Cuộn xuống phần **Cố vấn Phản biện AI** và nhấn:
   - `🔍 Đánh giá Toàn diện Bài phân tích`: để nhận xét cấu trúc và bằng chứng.
   - `⚔️ Phản biện & Thử thách Khuyến nghị`: để đối mặt với các phản biện khó từ chuyên gia.
6. Sau khi suy ngẫm và hoàn thiện bài làm, cuộn lên phần **Gợi ý Phân tích & Lời giải Mẫu** và nhấn `[🔓 Mở xem Gợi ý]` để đối chiếu kết quả.
7. Nhấn `📥 Xuất Báo cáo (.md)` trong thanh công cụ để tải về toàn bộ bài phân tích và phản biện phục vụ nghiên cứu và trình bày.
