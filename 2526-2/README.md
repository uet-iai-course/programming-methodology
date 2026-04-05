# Phương pháp luận lập trình — Học kì 2, năm học 2025-2026

**@Giảng viên:** Vui lòng cập nhật các file `lecture-*.html` cho từng buổi học khi cần. Có thể dùng các bài giảng hiện có làm mẫu để giữ thống nhất về bố cục và phong cách trình bày.

## Nội dung học kì

| Tuần | Bài giảng | Ghi chú |
|------|-----------|---------|
| 1 | Bài 1a: Giới thiệu học phần; Bài 1b: Máy trừu tượng | Đọc trước Giáo trình Chương 1: Abstract Machines |
| 2 | Bài 2a: Cú pháp và ngữ nghĩa; Bài 2b: Tên và môi trường; Bài 2c: Quản lý bộ nhớ | Đọc trước Giáo trình Chương 2.1-2.2; Chương 4; Chương 5 |
| 3 | Bài 3a: Cấu trúc điều khiển; Bài 3b: Trừu tượng hóa điều khiển | Đọc trước Giáo trình Chương 6; Chương 7 |
| 4 | Bài 4: Tổ chức và trừu tượng hóa dữ liệu | Đọc trước Giáo trình Chương 8; Chương 9 |
| 5 | Bài 5: Giới thiệu lập trình hướng đối tượng | Đọc trước Giáo trình Chương 10: Object-Oriented Programming |
| 6 | Bài 6: Các nguyên tắc thiết kế OOP | Đọc trước *Agile Software Development, Principles, Patterns, and Practices* - Phần 2, Chương 7-12 |
| 7 | Bài 7: Mẫu thiết kế OOP | Đọc trước *Head First Design Patterns* - Chương 13 |
| 8 | Bài 8: Giới thiệu lập trình hàm | *(chưa có ghi chú)* |
| 9 | Bài 9: Lập trình hàm nâng cao | *(chưa có ghi chú)* |
| 10 | Bài 10: Các mẫu hình lập trình khác | *(chưa có ghi chú)* |

## Chạy slide

Thư mục này chứa slide bài giảng viết bằng Reveal.js, có thể serve qua GitHub Pages hoặc máy chủ web cục bộ.
Hai cách chạy dưới đây dùng hai cổng mặc định khác nhau theo cấu hình hiện tại: Node.js dùng `8000`, còn ví dụ Python dưới đây dùng `8765`.

### Cách 1: Node.js (hỗ trợ ghi chú giảng viên & tự động tải lại)

1. Cài [Node.js](https://nodejs.org/) (phiên bản `>= 18` theo `package.json`).
2. Trong thư mục `2526-2`, chạy `npm install` để cài dependencies nếu cần.
3. Chạy lệnh sau từ thư mục `2526-2` để khởi động server với root là thư mục cha:
   ```bash
   npm start -- --root=.. --port=8000
   ```
   > **Lưu ý:** cần dùng `--root=..` vì `index.html` của học kì tham chiếu đến `../index-pages.css` (nằm ở thư mục cha). Nếu chạy `npm start` bình thường mà không có `--root=..`, CSS sẽ không load được.
4. Mở trình duyệt và truy cập http://localhost:8000/2526-2/.

### Cách 2: Python (không cần cài thêm gì)

```bash
# Neu dang o thu muc goc cua repo
cd 2526-2
python3 -m http.server 8765
# Mo http://localhost:8765
```

### Serve qua GitHub Pages

Không cần cấu hình gì thêm. Chỉ cần push thay đổi lên nhánh `main`, GitHub Pages sẽ tự động serve nội dung.

## Tài nguyên minh hoạ

Hình minh hoạ cho các bài giảng được lưu trực tiếp trong thư mục `img/lec-*/`.
Hiện tại repo này không có các thư mục `scripts/` để sinh lại hình tự động như repo môn Học máy; khi cần cập nhật hình, hãy chỉnh sửa hoặc thay thế trực tiếp các file trong `img/`.
