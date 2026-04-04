# Phương pháp luận lập trình — Trường Đại học Công nghệ, ĐHQGHN

Tài liệu slide bài giảng cho môn **Phương pháp luận lập trình** tại Viện Trí tuệ Nhân tạo (IAI), Trường Đại học Công nghệ (UET), ĐHQGHN.

Slide bài giảng được xây dựng bằng [Reveal.js](https://revealjs.com/). Ngoài nội dung bài giảng theo từng năm học, repo còn chứa một số prompt Markdown trong thư mục `prompts/` để hỗ trợ biên soạn, rút gọn và rà soát slide.

## Các năm học

| Năm học | Học kì | Thư mục |
|---------|--------|---------|
| 2025-2026 | 2 | [`2526-2/`](2526-2/) |

> Mỗi năm học mới sẽ được thêm vào dưới dạng một thư mục riêng (ví dụ: `2627-1/`).

## Cấu trúc mỗi năm học

> Cấu trúc dưới đây chỉ mang tính khái quát; một số thư mục có thể có thêm tài nguyên, plugin hoặc file cấu hình phụ trợ.

```text
.
├── index.html                  # Trang chủ liệt kê các năm học
├── XXXX-X/
│   ├── index.html              # Trang chủ của năm học
│   ├── lecture-*.html          # Slide bài giảng (Reveal.js)
│   ├── lecture-style.css       # CSS dùng chung cho các slide
│   ├── img/                    # Hình minh hoạ cho bài giảng
│   ├── plugin/                 # Plugin Reveal.js được dùng trực tiếp
│   ├── revealjs/               # Mã nguồn/tài nguyên Reveal.js được vendor
│   ├── package.json            # Cấu hình npm cho việc serve/build
│   └── gulpfile.js             # Tác vụ phục vụ slide cục bộ
└── prompts/
    └── *.md                    # Prompt hỗ trợ biên soạn và chỉnh sửa slide
```

## Thêm năm học mới

1. Tạo thư mục mới (ví dụ: `2627-1/`) bằng cách copy từ năm học gần nhất.
2. Cập nhật `index.html` ở root để thêm link tới năm học mới.
3. Bổ sung dòng tương ứng trong bảng "Các năm học" của file `README.md` này.
4. Cập nhật `README.md` trong thư mục năm học mới cho đúng lịch giảng dạy và hướng dẫn sử dụng.
