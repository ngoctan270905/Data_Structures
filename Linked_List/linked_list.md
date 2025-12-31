# 🔗 Danh Sách Liên Kết (Linked Lists)

## 1. 🌍 Ứng dụng trong thực tế

| Ứng dụng | Mô tả |
|----------|-------|
| Quản lý bộ nhớ | Dùng nội bộ để quản lý các khối bộ nhớ trống |
| Hoàn tác / Làm lại (Undo/Redo) | Các trình soạn thảo dùng danh sách liên kết để theo dõi lịch sử hành động |
| Chức năng Back/Forward trình duyệt | Sử dụng danh sách liên kết đôi để di chuyển giữa các trang đã truy cập |
| Danh sách phát nhạc / video | Dễ dàng thêm và xóa bài hát/video |
| Bộ nhớ đệm LRU | Danh sách liên kết đôi được dùng để theo dõi thứ tự sử dụng |
| Xử lý va chạm bảng băm (Hash table) | Xử lý va chạm bằng cách dùng danh sách liên kết (chaining) |
| Lập lịch tiến trình OS | Duy trì danh sách các tiến trình động |

---

## 2. ❓ Danh Sách Liên Kết là gì?

Một **Danh Sách Liên Kết** là một cấu trúc dữ liệu tuyến tính, trong đó mỗi phần tử (nút/node) chứa:
- Một **giá trị (value)**
- Một **tham chiếu (con trỏ)** đến nút tiếp theo

Khác với mảng (array), danh sách liên kết:
- **Không yêu cầu bộ nhớ liền kề**
- Cho phép **chèn và xóa hiệu quả**
- **Không hỗ trợ truy cập trực tiếp qua chỉ số (index)**

---

## 3. 📑 Các loại Danh Sách Liên Kết

### 🔹 Danh Sách Liên Kết Đơn (Singly Linked List)
Mỗi nút chỉ chứa dữ liệu và con trỏ đến nút tiếp theo.

```text
 HEAD
  ↓
┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐
│ Data │ Next │───→│ Data │ Next │───→│ Data │ NULL │
└──────┴──────┘    └──────┴──────┘    └──────┴──────┘
```

- **Đặc điểm:** Chỉ duyệt được một chiều (xuôi).
- **Ưu điểm:** Cài đặt đơn giản, ít tốn bộ nhớ.
- **Nhược điểm:** Không thể quay lui về nút trước đó; việc xóa nút cần biết nút đứng trước.

### 🔹 Danh Sách Liên Kết Đôi (Doubly Linked List)
Mỗi nút chứa dữ liệu và hai con trỏ: một trỏ về nút trước (`Prev`), một trỏ đến nút sau (`Next`).

```text
       HEAD
        ↓
      ┌──────┬──────┬──────┐    ┌──────┬──────┬──────┐
NULL ←┤ Prev │ Data │ Next │ ⇄  │ Prev │ Data │ Next │→ NULL
      └──────┴──────┴──────┘    └──────┴──────┴──────┘
```

- **Đặc điểm:** Duyệt được cả hai chiều (xuôi và ngược).
- **Ưu điểm:** Linh hoạt; xóa một nút là O(1) nếu đã nắm giữ tham chiếu tới nút đó.
- **Nhược điểm:** Tốn nhiều bộ nhớ hơn cho con trỏ `Prev`; code phức tạp hơn.

### 🔹 Danh Sách Liên Kết Vòng (Circular Linked List)
Nút cuối cùng trỏ ngược lại nút đầu tiên thay vì `NULL`. Có thể là vòng đơn hoặc vòng đôi.

```text
 HEAD
  ↓
┌──────┬──────┐    ┌──────┬──────┐    ┌──────┬──────┐
│ Data │ Next │───→│ Data │ Next │───→│ Data │ Next │──┐
└──────┴──────┘    └──────┴──────┘    └──────┴──────┘  │
   ↑                                                   │
   └───────────────────────────────────────────────────┘
```

- **Đặc điểm:** Không có giá trị `NULL` trong danh sách.
- **Ứng dụng:** Hữu ích cho các ứng dụng lặp lại vòng tròn như lập lịch Round Robin, danh sách phát nhạc lặp lại.

---

## 4. ⚖️ So sánh Danh Sách Liên Kết và Mảng

| Đặc điểm | Mảng (Array) | Danh Sách Liên Kết |
|----------|--------------|--------------------|
| Bố trí bộ nhớ | Liền kề (Contiguous) | Không liền kề |
| Truy cập theo chỉ số | O(1) | O(n) |
| Chèn / Xóa | O(n) | O(1) (nếu đã biết nút) |
| Chi phí bộ nhớ | Thấp | Cao hơn (do chứa con trỏ) |

---

## 5. ⚙️ Các thao tác cốt lõi

### Chèn (Insert)
- Tại đầu (head): O(1)
- Tại cuối (tail): O(1) (nếu có con trỏ tail)
- Tại vị trí bất kỳ: O(n)

### Xóa (Delete)
- Theo giá trị: O(n)
- Khi biết tham chiếu nút: O(1)

### Tìm kiếm (Search)
- O(n)

---

## 6. 💡 Tại sao Danh Sách Liên Kết lại quan trọng?

Danh sách liên kết quan trọng vì:
- Chúng giới thiệu tư duy dựa trên con trỏ
- Tạo nền tảng cho nhiều cấu trúc dữ liệu nâng cao
- Xuất hiện trong các hệ thống thực tế như bộ nhớ đệm (caches), bộ lập lịch (schedulers), và bộ phân bổ bộ nhớ

Hiểu sâu về danh sách liên kết là điều cần thiết trước khi chuyển sang cây (trees) và đồ thị (graphs).

---

## 7. 🔑 Những điểm chính cần nhớ

- Danh sách liên kết đánh đổi tốc độ truy cập nhanh để lấy sự linh hoạt trong sử dụng bộ nhớ
- Chúng vượt trội trong việc chèn và xóa
- Nhiều cấu trúc dữ liệu nâng cao được xây dựng dựa trên danh sách liên kết