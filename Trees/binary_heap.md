# 🌲 Binary Heap (Đống Nhị Phân)

## 1. 🌍 Ứng dụng trong thực tế

| Ứng dụng | Mô tả |
|----------|-------|
| Hàng đợi ưu tiên (Priority Queue) | Luôn lấy ra phần tử có độ ưu tiên cao nhất/thấp nhất |
| Lập lịch tác vụ (Job Scheduling) | Hệ điều hành chọn tiến trình tiếp theo dựa trên độ ưu tiên |
| Hệ thống quản lý tác vụ | Xử lý các tác vụ khẩn cấp trước các tác vụ thường |
| Thuật toán đồ thị (Dijkstra, Prim) | Tìm đường đi ngắn nhất hoặc cây khung nhỏ nhất hiệu quả |
| Heap Sort | Thuật toán sắp xếp dựa trên cấu trúc Heap với độ phức tạp O(n log n) |
| Quản lý băng thông mạng | Ưu tiên các gói tin quan trọng trong luồng dữ liệu |

---

## 2. ❓ Binary Heap là gì?

**Binary Heap** là một **cây nhị phân hoàn chỉnh (complete binary tree)** thỏa mãn **tính chất Heap (Heap Property)**. 

Nó thường được cài đặt bằng **mảng (array)** thay vì dùng các con trỏ node như cây thông thường để tối ưu bộ nhớ cache.

Có hai loại chính:
1.  **Min Heap (Đống nhỏ nhất):** Giá trị của nút cha luôn **nhỏ hơn hoặc bằng** các nút con. Phần tử nhỏ nhất luôn nằm ở gốc (root).
2.  **Max Heap (Đống lớn nhất):** Giá trị của nút cha luôn **lớn hơn hoặc bằng** các nút con. Phần tử lớn nhất luôn nằm ở gốc.

---

## 3. 📐 Cấu trúc và Tính chất

Để một cây được gọi là Binary Heap, nó phải thỏa mãn 2 điều kiện:

### 1️⃣ Tính chất Cấu trúc (Structure Property)
*   Phải là một **cây nhị phân hoàn chỉnh**: Tất cả các tầng của cây phải được lấp đầy hoàn toàn, ngoại trừ tầng cuối cùng.
*   Ở tầng cuối cùng, các nút phải được điền từ **trái sang phải**.

### 2️⃣ Tính chất Heap (Heap Order Property)
Mối quan hệ giữa cha và con phải luôn đúng:

**Min Heap:**
```text
       [10]
      /    \
   [15]    [30]
   /  \    /
 [40] [50][100]
```
*(Mọi nút cha đều nhỏ hơn con của nó)*

**Max Heap:**
```text
       [100]
      /     \
   [40]     [50]
   /  \     /
 [10] [15] [30]
```
*(Mọi nút cha đều lớn hơn con của nó)*

⚠️ **Lưu ý:** Heap **không đảm bảo thứ tự** giữa con trái và con phải (khác với Binary Search Tree).

---

## 4. 🔢 Biểu diễn mảng (Array Representation)

Vì là cây nhị phân hoàn chỉnh, Heap có thể ánh xạ hoàn hảo vào một mảng mà không lãng phí ô nhớ.

Giả sử nút đang xét có chỉ số (index) là `i` (bắt đầu từ 0):

| Vị trí | Công thức chỉ số |
| :--- | :--- |
| **Nút cha (Parent)** | `(i - 1) / 2` (lấy phần nguyên) |
| **Con trái (Left Child)** | `2 * i + 1` |
| **Con phải (Right Child)** | `2 * i + 2` |

**Ví dụ trực quan:**

Cây:
```text
      1
    /   \
   3     6
  / \   /
 5   9 8
```

Mảng tương ứng:
```text
Index:  [0] [1] [2] [3] [4] [5]
Value:   1   3   6   5   9   8
```
- Node `3` ở index `1`.
- Con trái: `2*1 + 1` = index `3` (giá trị 5).
- Con phải: `2*1 + 2` = index `4` (giá trị 9).

---

## 5. ⚙️ Các thao tác cốt lõi & Độ phức tạp

| Thao tác | Mô tả | Độ phức tạp |
|----------|-------|-------------|
| **Peek** | Xem phần tử ở gốc (Max hoặc Min) | O(1) |
| **Insert (Push)** | Thêm phần tử mới vào cuối mảng, sau đó **Heapify Up** (vun đống lên) | O(log n) |
| **Extract (Pop)** | Lấy phần tử gốc ra, đưa phần tử cuối lên thế chỗ, sau đó **Heapify Down** (vun đống xuống) | O(log n) |
| **Build Heap** | Tạo Heap từ mảng vô trật tự | O(n) |
| **Search** | Tìm một giá trị bất kỳ (không phải gốc) | O(n) |

---

## 6. ⚖️ So sánh Binary Heap vs Binary Search Tree (BST)

| Đặc điểm | Binary Heap | Binary Search Tree (BST) |
|----------|-------------|--------------------------|
| **Mục tiêu** | Tìm Min/Max nhanh nhất | Tìm kiếm, sắp xếp dữ liệu |
| **Cấu trúc** | Cây hoàn chỉnh (Complete Tree) | Cây bất kỳ (có thể bị lệch) |
| **Thứ tự** | Cha ưu tiên hơn con | Trái < Cha < Phải |
| **Bộ nhớ** | Mảng (tiết kiệm, cache tốt) | Con trỏ (tốn thêm bộ nhớ) |
| **Tìm Max/Min** | O(1) | O(log n) (hoặc O(n) nếu cây lệch) |
| **Tìm kiếm (Search)** | O(n) | O(log n) |

---

## 7. 💡 Tại sao Binary Heap lại quan trọng?

1.  **Hiệu suất:** Truy cập phần tử ưu tiên nhất ngay lập tức (O(1)).
2.  **Bộ nhớ:** Cài đặt bằng mảng giúp tiết kiệm bộ nhớ con trỏ và tận dụng tốt Cache của CPU (Locality of reference).
3.  **Nền tảng thuật toán:** Là trái tim của nhiều thuật toán quan trọng như Dijkstra (tìm đường đi ngắn nhất) hay Prim (cây khung).

---

## 8. 🔑 Những điểm chính cần nhớ

- Binary Heap **không dùng để tìm kiếm** (Search là O(n)), mà dùng để **quản lý thứ tự ưu tiên**.
- Luôn là **Cây nhị phân hoàn chỉnh**.
- Hai thao tác quan trọng nhất là **Heapify Up** (khi thêm) và **Heapify Down** (khi xóa).
- Mảng là cách cài đặt chuẩn mực cho Heap.
