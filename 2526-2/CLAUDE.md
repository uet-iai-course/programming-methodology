# CLAUDE.md — Học kì 2, năm học 2025-2026

> Đọc kèm [`../CLAUDE.md`](../CLAUDE.md) (workflow + git) và [`../SLIDE_STYLE_GUIDE.md`](../SLIDE_STYLE_GUIDE.md) (tiêu chuẩn slide). File này chỉ chứa **đặc thù học kì 2 2025-2026**.

## Lịch giảng và trạng thái

| Tuần | Bài | File | Trạng thái |
|------|-----|------|------------|
| 1 | 1a Giới thiệu, 1b Máy trừu tượng | `lecture-01a-*.html`, `lecture-01b-*.html` | ✅ Done |
| 2 | 2a Cú pháp, 2b Tên-môi trường, 2c Bộ nhớ | `lecture-02*.html` | ✅ Done |
| 3 | 3a Cấu trúc điều khiển, 3b Trừu tượng hoá | `lecture-03*.html` | ✅ Done |
| 4 | Tổ chức và trừu tượng hoá dữ liệu | `lecture-04-*.html` | ✅ Done |
| 5 | Giới thiệu OOP | `lecture-05-introduction-to-OOP.html` | ✅ Done |
| 6 | Nguyên tắc thiết kế OOP (SOLID) | `lecture-06-OOP-design-principles.html` | ✅ Done |
| 7 | Mẫu thiết kế OOP | `lecture-07-OOP-design-patterns.html` | ✅ Done |
| 8 | Giới thiệu lập trình hàm | `lecture-08-introduction-to-FP.html` | ✅ Done |
| 9 | Lập trình hàm nâng cao | `lecture-09-advanced-FP.html` | ✅ Done (PR #12) |
| 10 | Các mẫu hình lập trình khác | `lecture-10-other-programming-paradigms.html` | 🚧 PR #13 in progress |

## Reading map (giáo trình)

- **PLPP** = *Programming Languages: Principles and Paradigms* (Gabbrielli, Martini, Giallorenzo)
- **OOP** = *Object Oriented Programming in C++* (Robert Lafore)
- **FP** = *Functional Programming in C++* (Ivan Čukić)
- **ASD** = *Agile Software Development, Principles, Patterns, and Practices* (Robert C. Martin)
- **HFDP** = *Head First Design Patterns*

Tuần 8 + 9: PLPP Ch.11 (gộp `rowspan="2"` ở `index.html`).
Tuần 10: PLPP Ch.12-16.

## Đặc thù conventions từng bài

### Lec08-09 — Lập trình hàm
- Pseudocode ML-style với keyword `lambda` (xem `SLIDE_STYLE_GUIDE` mục Code blocks).
- Custom highlight.js language `mlpseudo` đăng ký trong `lecture-09-advanced-FP.html`.
- Bỏ phần SECD machine — không dạy.
- Dịch *"Lambda calculus"* → **"Phép tính lambda"** (chữ thường lambda).
- Có cây AST + cây quy giản SVG cho ví dụ 3, 5, 7.

### Lec10 — 3 paradigm khác
- **Logic**: Prolog + CLP(FD). Code Sudoku đơn giản hoá (bỏ `khoi/3` đệ quy).
- **Song song**: code C++ với `std::thread`/`std::atomic`/`std::mutex`. Có Amdahl SVG, ví dụ đèn giao thông cho race/deadlock/starvation.
- **AI**: workflow practical + agent loop + context engineering + công cụ thực tế 2026 (Copilot, Cursor, Claude Code, Cline, Aider).
- Hook **AlphaGo** dẫn dắt cả bài; closing có timeline AlphaGo → AlphaFold → ChatGPT → Claude Code.
- Custom highlight.js language `prolog` đăng ký trong file lec10.
- CSS class `.sudoku-grid` và `.sudoku-grid--lg` đã định nghĩa trong `lecture-style.css`.

### Hook story đã dùng
- Lec09: AXD301 (Erlang switch viễn thông, 9-nines uptime, 1M LOC)
- Lec10: AlphaGo (3 paradigm cùng giải Cờ Vây)

Khi tạo bài mới, tham khảo các hook này để hình dung phong cách.

## Trạng thái branch hiện tại

- `main`: tất cả bài đã merge.
- `lec10-draft`: PR #13, đang polish layout từng slide theo phản hồi.

## Nguồn tham khảo đặc biệt

- VnExpress 75% Google AI code: hook cho lec10 §3 (AI lập trình là hiện trạng).
- Pichai Q3/2024 earnings: số liệu chính xác *"more than 25%"*.

## Quy tắc deploy

- GitHub Pages tự deploy nhánh `main`.
- URL deploy: `https://uet-iai-course.github.io/programming-methodology/2526-2/lecture-NN-*.html`.
- Local preview: `cd 2526-2 && python3 -m http.server 8765` rồi mở `http://localhost:8765/lecture-NN-*.html#/section/vertical`.
