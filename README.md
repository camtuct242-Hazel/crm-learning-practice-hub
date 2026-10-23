# CRM Bilingual Learning & Practice Hub

An authoritative, source-grounded bilingual Customer Relationship Management (CRM) learning platform built directly on the verified textbooks and business case studies in `references/`.

---

## 📌 Project Overview & Author Attribution

- **Project:** CRM Learning & Practice Hub
- **Author:** Nguyễn Đăng Cẩm Tú (Hazel)
- **Nature of Project:** An independent bilingual learning and practice project designed to support systematic study, concept mastery, and exam preparation in Customer Relationship Management. (This is an independent academic study tool and not an official product of the textbook authors, publishers, or analyzed corporations).

### Learning Objectives Supported
The platform supports deep, structured bilingual CRM learning through:
- **Comprehensive Knowledge Library:** Chapter-by-chapter structured notes preserving the pedagogical sequence and terminology of Baran & Galka (2017) and Kostojohn et al. (2011).
- **Bilingual CRM Glossary & Flashcards:** 52 rigorous definitions with formulas and 40 spaced-repetition interactive flashcards.
- **Enterprise Case Studies:** 10 real-world business cases (Tesco, Google, Amazon, Apple, Meta, Disney, Airbnb, McDonald's, Walmart, IKEA) analyzed with structured problem-solving frameworks.
- **200 Validated Practice Questions & 10 Curated Exams:** Exactly 200 questions with 4 balanced options, comprehensive bilingual rationales, and exact source citations.
- **Bilingual Learning Modes:** Instant zero-reload switching between Vietnamese (`vi`) and English (`en`), preserving all in-progress quiz states, flashcard queues, and personal case notes.

---

## 1. Quick Start

### Option A: Direct Browser Preview (Zero dependencies)
Simply double-click or open `output/index.html` in any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox).

```text
file:///C:/Kiến thức cần học/CRM/output/index.html
```

### Option B: Local Web Server
If you prefer running via a local HTTP server:

```powershell
cd "C:\Kiến thức cần học\CRM\output"
uv run python -m http.server 3000
```
Then navigate to: `http://localhost:3000`

---

## 2. Platform Architecture & Features

### Core Modules
1. **Dashboard (Bảng Điều khiển):** Central learning cockpit tracking completed chapters, flashcard masteries, exam scores, and quick actions.
2. **Knowledge Library (Thư viện Tri thức):** Structured, source-grounded chapter notes preserving the chapter order of both textbooks (Baran & Galka 2017; Kostojohn et al. 2011). Features custom subtopic cards, custom bullet icons, and reading time metrics.
3. **Bilingual Glossary (Thuật ngữ Anh - Việt):** 52 comprehensive CRM concepts with exact definitions, operational context, formulas, and source page citations with instant search.
4. **Smart Flashcards (Thẻ Ghi nhớ Thông minh):** 40 interactive 3D flip-card practice items with 4-level spaced repetition self-rating (Again, Hard, Good, Easy) and keyboard navigation (`Space` to flip, `Left/Right` arrows).
5. **10 Curated Comprehensive Exams (10 Đề thi Chuẩn hóa):** Exactly 10 exams with 20 distinct questions each (200 questions total) covering targeted knowledge domains with real-time scoring and source-grounded rationales.
6. **Random Practice Generator (Bộ Luyện đề Ngẫu nhiên):** Configurable question count (10, 20, 30), difficulty levels (All, Easy, Medium, Hard), and immediate vs. exam feedback modes drawing from the 200 validated questions.
7. **Business Case Study Lab (Phòng Nghiên cứu Tình huống):** 10 world-class enterprise cases (Walmart, IKEA, Disney, Airbnb, McDonald's, Chanel, Nike, Estée Lauder, GAFA, and Tesco) analyzed through a 10-step problem-solving framework, discussion questions, model rubrics, and personal student notes storage.
8. **Progress Analytics (Đánh giá Tiến độ Học tập):** Visual breakdown of curriculum coverage, exam score history, and flashcard mastery.
9. **Settings & Data Management (Cài đặt & Dữ liệu):** Language selection, export/import progress data (JSON), and safe progress reset.

### Bilingual Toggle
The platform defaults to **Vietnamese (`vi`)** with a prominent header toggle (`Tiếng Việt | English`).
- Switching languages is instant and reactive.
- Language switching never reloads the page.
- In-progress exam answers, active flashcard queues, and user notes are strictly preserved across language transitions.

---

## 3. Automated Quality Assurance & Testing

Run the full automated test suite using `uv`:

```powershell
uv run python -m unittest discover -s output/tests -p "test_*.py" -v
```

All 15 test assertions pass with 100% success:
- Exactly 200 questions with 200 unique IDs and verifiable source page citations.
- Exactly 10 curated exams with 20 distinct questions each.
- Balanced answer key distribution (50 A, 50 B, 50 C, 50 D).
- 100% bilingual parity across questions, curriculum, cases, glossary, flashcards, and UI.
- Language switching state preservation under active exam conditions.
- Source manifest integrity against physical reference PDFs.

To run the live headless browser interaction test suite:

```powershell
uv run python output/scratch/run_edge_test.py
```
All 30 browser integration tests pass with 100% success in Microsoft Edge headless.
