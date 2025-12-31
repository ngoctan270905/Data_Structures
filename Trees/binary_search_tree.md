# 🔍 Cây Nhị Phân Tìm Kiếm (Binary Search Tree - BST)

## 1. 🌍 Ứng dụng trong thực tế

Mặc dù trong thực tế người ta thường dùng các phiên bản tự cân bằng (như AVL, Red-Black Tree), nhưng nguyên lý của BST vẫn là cốt lõi cho các ứng dụng sau:

| Ứng dụng | Mô tả |
|---------|------|
| Lưu trữ dữ liệu có thứ tự | Duy trì dữ liệu luôn ở trạng thái đã sắp xếp |
| Symbol table | Lưu key–value có thể tìm kiếm nhanh |
| Index trong database (mức khái niệm) | Cơ sở cho các cây cân bằng như B-Tree, B+ Tree |
| Range query | Tìm các giá trị nằm trong một khoảng |
| Ranking / ordered data | Quản lý dữ liệu theo thứ tự |
| Nền tảng cho cây cân bằng | Cơ sở để học AVL Tree, Red-Black Tree |

---

## 3. ❓ BST là gì?

**BST** là một bước nâng cấp của Cây Nhị Phân, trong đó các nút được sắp xếp theo một quy tắc nghiêm ngặt để tối ưu hóa việc tìm kiếm:

**Quy tắc vàng:**
- Tất cả các nút ở **nhánh bên trái** phải nhỏ hơn nút cha.
- Tất cả các nút ở **nhánh bên phải** phải lớn hơn nút cha.
- Quy tắc này áp dụng đệ quy cho mọi nút trên cây.

---

## 3. 📐 Cấu trúc minh họa

Nhờ quy tắc trên, dữ liệu trong BST luôn ở trạng thái "sắp xếp một nửa", giúp việc tìm kiếm cực nhanh.

```text
       [ 8 ]          <-- Gốc (Root)
      /     \
   [ 3 ]    [ 10 ]    <-- 3 < 8; 10 > 8
   /   \      \
 [ 1 ] [ 6 ]   [ 14 ]
       /   \    /
     [ 4 ] [ 7 ][ 13 ]
```

**Cách tìm số 7:**
1. Bắt đầu từ `8` -> `7 < 8` -> Sang trái.
2. Gặp `3` -> `7 > 3` -> Sang phải.
3. Gặp `6` -> `7 > 6` -> Sang phải.
4. Thấy `7`! (Chỉ mất 4 bước thay vì duyệt toàn bộ).

---

## 4. ⚙️ Các thao tác cốt lõi & Độ phức phức tạp

| Thao tác | Trung bình | Tệ nhất (Cây lệch) |
|----------|------------|--------------------|
| **Tìm kiếm (Search)** | O(log n) | O(n) |
| **Thêm (Insert)** | O(log n) | O(n) |
| **Xóa (Delete)** | O(log n) | O(n) |

⚠️ **Vấn đề "Cây lệch":** Nếu bạn thêm dữ liệu đã sắp xếp (ví dụ: 1, 2, 3, 4, 5), BST sẽ biến thành một đường thẳng (Skewed Tree). Khi đó, nó không khác gì một Danh sách liên kết và mất sạch ưu thế về tốc độ.

---

## 5. 🚶 Duyệt cây BST (In-order Traversal)

Một đặc điểm cực kỳ thú vị của BST: Nếu bạn duyệt cây theo phương pháp **In-order (Trái -> Gốc -> Phải)**, bạn sẽ thu được một dãy số **đã được sắp xếp tăng dần**.

**Ví dụ với cây ở trên:** `1, 3, 4, 6, 7, 8, 10, 13, 14`.

---

## 6. ⚖️ So sánh BST với các cấu trúc khác

| Đặc điểm | Binary Tree | Binary Search Tree | Binary Heap |
|----------|-------------|--------------------|-------------|
| **Thứ tự** | Không có | Trái < Cha < Phải | Cha > Con (Max-heap) |
| **Tìm kiếm** | O(n) | O(log n) | O(n) |
| **Truy cập Min/Max** | O(n) | O(log n) | O(1) |
| **Ứng dụng** | Cấu trúc cơ bản | Tìm kiếm dữ liệu | Hàng đợi ưu tiên |

---

## 7. 💡 Tại sao BST lại quan trọng?

1.  **Cơ sở của tính hiệu quả:** Nó là nền tảng cho các loại cây tự cân bằng như **AVL** và **Red-Black Tree**.
2.  **Dễ cài đặt:** Code đơn giản hơn nhiều so với các cấu trúc cây phức tạp.
3.  **Linh hoạt:** Hỗ trợ tốt các thao tác thêm/xóa/tìm kiếm trên dữ liệu động.

---

## 8. 🔑 Những điểm chính cần nhớ

- BST = Cây nhị phân + Quy tắc sắp xếp.
- Luôn nhớ: **Trái nhỏ hơn, Phải lớn hơn**.
- Hiệu năng phụ thuộc hoàn toàn vào **độ cân bằng** của cây.
- Duyệt In-order sẽ cho kết quả đã sắp xếp.