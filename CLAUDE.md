# CLAUDE.md — Hướng dẫn cho Claude Code

Repo này chứa slide bài giảng môn **Phương pháp luận lập trình** tại Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN. Slide viết bằng [Reveal.js](https://revealjs.com/), trình bày tiếng Việt cho sinh viên năm 2-3.

> **Convention thiết kế / nội dung slide**: đọc [`SLIDE_STYLE_GUIDE.md`](./SLIDE_STYLE_GUIDE.md). File CLAUDE.md này chỉ chứa quy tắc làm việc với repo (workflow, git, "đừng làm gì").

## Cấu trúc repo

```
.
├── index.html              # Trang chủ liệt kê các năm học
├── index-pages.css         # CSS cho các trang index
├── README.md
├── CLAUDE.md               # File này
├── SLIDE_STYLE_GUIDE.md    # Tiêu chuẩn thiết kế slide (đọc nếu sửa nội dung slide)
├── XXXX-X/                 # Mỗi học kì 1 thư mục, ví dụ 2526-2 = HK2 2025-2026
│   ├── README.md
│   ├── CLAUDE.md           # Convention riêng cho học kì
│   ├── index.html
│   ├── lecture-*.html      # Slide từng bài
│   ├── lecture-style.css
│   ├── img/, plugin/, revealjs/
│   └── package.json
└── prompts/                # Prompt templates hỗ trợ biên soạn slide
    └── *.md
```

Khi làm việc với 1 học kì cụ thể, đọc thêm `XXXX-X/CLAUDE.md` để biết trạng thái và đặc thù của học kì đó.

## Run local

```bash
cd XXXX-X
python3 -m http.server 8765    # Đơn giản nhất
# hoặc: npm start -- --root=.. --port=8000   (Node.js, hỗ trợ speaker notes + auto-reload)
```

GitHub Pages auto-deploy khi push lên `main`.

## Git workflow

- **Branch convention**: `lec{NN}-draft` cho draft của bài N (ví dụ `lec10-draft`).
- **Đừng tự push** — chỉ push khi user yêu cầu rõ ràng.
- **Commit message format**:
  ```
  Lec{NN} §{section} ({tên section}): {tóm tắt ngắn}

  - Bullet list mô tả thay đổi (tiếng Việt).
  - …

  Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
  ```
- PR base: `main`. Tiêu đề PR ngắn (<70 ký tự), body có Summary + Test plan.
- Trước khi commit: verify `<section>` / `</section>` tag balance bằng `grep -c`.

## Quy tắc tuyệt đối — "ĐỪNG"

Đây là những quy tắc về **cách làm việc**. Quy tắc về **nội dung slide** xem [`SLIDE_STYLE_GUIDE.md`](./SLIDE_STYLE_GUIDE.md).

1. ❌ **Đừng tự push** lên remote — chỉ commit local. User sẽ ra lệnh push.
2. ❌ **Đừng tạo file documentation/README.md mới** trừ khi user yêu cầu.
3. ❌ **Đừng skip pre-commit hooks** (`--no-verify`).
4. ❌ **Đừng amend commit cũ** — luôn tạo commit mới. Chỉ amend khi user yêu cầu rõ.
5. ❌ **Đừng tạo slide mới** trừ khi user yêu cầu rõ. Sửa slide hiện có ưu tiên hơn thêm slide.

## Khi không chắc

- Hỏi user trước khi: thêm slide mới, thay đổi structure lớn, đụng vào content khác slide đang sửa.
- User-pause = dừng commit/push, đợi instruction tiếp.
- Auto mode = thực hiện ngay, ít interrupt.
- Khi user nói "xấu" mà không nói cụ thể: phân tích hiện trạng (font, layout, balance, visual unity) rồi đề xuất 2-3 phương án để user chọn.

## Đọc thêm

- [`SLIDE_STYLE_GUIDE.md`](./SLIDE_STYLE_GUIDE.md) — tiêu chuẩn thiết kế slide (color, pattern, wording, code block, badge…).
- [`glossaries.yaml`](./glossaries.yaml) — bảng thuật ngữ Anh-Việt chuẩn xuyên suốt các deck.
- [`prompts/`](./prompts/) — prompt templates cho biên soạn slide.
- `XXXX-X/CLAUDE.md` — đặc thù của học kì cụ thể (lịch giảng, trạng thái, conventions cụ thể).
