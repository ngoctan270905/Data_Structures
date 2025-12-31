# 🔴⚫ Cây Đỏ-Đen (Red-Black Tree)

## 1. ❓ Red-Black Tree là gì?

**Red-Black Tree** là một dạng **Cây nhị phân tìm kiếm tự cân bằng (Self-balancing BST)**.

Nó giải quyết vấn đề của BST thường: Không bao giờ để cây bị lệch thành đường thẳng. Nó đảm bảo chiều cao của cây luôn ở mức ~`O(log n)` bất kể bạn thêm dữ liệu theo thứ tự nào.

---

## 2. 👮 5 Quy tắc bất di bất dịch

Để giữ cân bằng, cây buộc mỗi nút phải tuân thủ 5 luật (nghe có vẻ phức tạp nhưng mục đích chỉ là để cây không quá cao):

1.  **Màu sắc:** Mỗi nút chỉ có thể là **ĐỎ (Red)** hoặc **ĐEN (Black)**.
2.  **Gốc (Root):** Nút gốc luôn luôn là **ĐEN**.
3.  **Lá ảo (NIL):** Tất cả các lá (NULL) được coi là màu **ĐEN**.
4.  **Luật Đỏ:** Nếu một nút là ĐỎ, thì cả 2 con của nó phải là ĐEN (Không bao giờ có 2 nút ĐỎ nối tiếp nhau).
5.  **Chiều cao Đen:** Mọi đường đi từ một nút bất kỳ xuống các lá của nó phải đi qua cùng một số lượng nút ĐEN.

---

## 3. 📐 Minh họa

```text
         [10, ⚫]
        /       \
    [5, 🔴]    [20, ⚫]
    /    \        \
[3, ⚫] [8, ⚫]   [30, 🔴]
```
*Lưu ý: Không có 2 nút Đỏ nào cạnh nhau.*

Khi bạn thêm hoặc xóa nút, nếu các luật trên bị vi phạm, cây sẽ tự sửa chữa bằng 2 thao tác:
1.  **Đổi màu (Recoloring)**.
2.  **Xoay cây (Rotation):** Xoay trái hoặc xoay phải cấu trúc.

---

## 4. ⚙️ Hiệu năng

Do cây luôn gần như cân bằng, hiệu năng luôn ổn định:

| Thao tác | Trung bình | Tệ nhất |
|----------|------------|---------|
| **Tìm kiếm** | O(log n) | O(log n) |
| **Thêm** | O(log n) | O(log n) |
| **Xóa** | O(log n) | O(log n) |

---

## 5. 🌍 Ứng dụng thực tế (Rất phổ biến)

| Ứng dụng | Mô tả |
|---------|------|
| Thư viện chuẩn | `TreeMap`, `TreeSet` (Java), `std::map` (C++) |
| Index trong database | Lưu trữ dữ liệu có thứ tự và cân bằng |
| File system | Quản lý inode, directory entries |
| Kernel / OS | Quản lý tiến trình, timer, scheduler |
| Ordered cache | Lưu dữ liệu có thứ tự và truy cập nhanh |
| Nền tảng cho B-Tree | Tiền đề để hiểu cây đa nhánh |

---

## 6. 🔑 Tổng kết

*   Nó là BST phiên bản "không bao giờ lệch".
*   Quy tắc về màu Đỏ/Đen giúp đảm bảo đường đi dài nhất không bao giờ dài gấp đôi đường đi ngắn nhất.
*   Dùng cái này khi bạn cần tìm kiếm nhanh và dữ liệu thay đổi liên tục (thêm/xóa nhiều).
