# 🌳 Cây Nhị Phân (Binary Tree)

---

## 1. ❓ Cây Nhị Phân là gì?

**Cây Nhị Phân (Binary Tree)** là một cấu trúc dữ liệu phân cấp, trong đó mỗi nút (node) có **tối đa 2 con**, được gọi là **Con Trái (Left Child)** và **Con Phải (Right Child)**.

⚠️ **Đặc điểm quan trọng:** 
Cây nhị phân "thuần túy" chỉ quy định về **hình dáng cấu trúc**, không có quy tắc về giá trị (không bắt buộc trái nhỏ hơn phải). Nó chủ yếu đóng vai trò là **nền tảng lý thuyết** để xây dựng các cấu trúc thực dụng hơn như BST, AVL, hay Heap.

---

## 2. 📖 Thuật ngữ cơ bản

- **Gốc (Root):** Nút trên cùng, không có cha.
- **Lá (Leaf):** Nút không có con nào cả.
- **Nút trong (Internal Node):** Nút có ít nhất 1 con.
- **Chiều cao (Height):** Số cạnh từ nút đó đến lá xa nhất.
- **Độ sâu (Depth):** Số cạnh từ gốc đến nút đó.

---

## 3. 📑 Các loại Cây Nhị Phân cơ bản

### 🔹 Full Binary Tree
Mọi nút đều có **0 hoặc 2 con**. Không bao giờ có nút chỉ có 1 con.

### 🔹 Complete Binary Tree
Tất cả các tầng đều đầy, trừ tầng cuối cùng. Các nút tầng cuối phải điền từ **trái sang phải**.

### 🔹 Perfect Binary Tree
Mọi nút trong đều có 2 con và tất cả các lá đều nằm ở cùng một tầng.

### 🔹 Skewed Binary Tree (Cây lệch)
Mọi nút chỉ có 1 con duy nhất. Cấu trúc này bị thoái hóa thành **Danh sách liên kết**, làm mất đi ưu thế của cây.

---

## 4. 🚶 Các phương pháp Duyệt Cây (Traversal)

Đây là phần quan trọng nhất khi làm việc với cây:

1.  **Pre-order (Tiền thứ tự):** Gốc → Trái → Phải
2.  **In-order (Trung thứ tự):** Trái → Gốc → Phải
3.  **Post-order (Hậu thứ tự):** Trái → Phải → Gốc
4.  **Level-order (Duyệt theo tầng):** Sử dụng Queue để duyệt từng tầng từ trên xuống dưới.

---

## 5. ⚖️ So sánh với các cấu trúc phái sinh

| Đặc điểm | Binary Tree | BST (Tìm kiếm) | Heap (Đống) |
|----------|-------------|----------------|-------------|
| **Quy tắc giá trị** | Không có | Trái < Gốc < Phải | Cha > Con (Max-heap) |
| **Mục đích** | Học thuật / Cơ bản | Tìm kiếm nhanh | Hàng đợi ưu tiên |
| **Cài đặt** | Con trỏ | Con trỏ | Mảng (Array) |

---

## 6. 🔑 Tổng kết

- Đừng dùng Cây nhị phân thường để tìm kiếm dữ liệu (vì hiệu suất tìm kiếm là O(n)).
- Hãy coi nó là **bước đệm** để học về đệ quy và các cấu trúc cây phức tạp hơn.
- Nắm vững các cách duyệt cây (Traversal) vì chúng sẽ được tái sử dụng ở mọi loại cây sau này.