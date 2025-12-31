# 🗄️ B+ Tree (Cây B+)

## 1. ❓ B+ Tree là gì?

**B+ Tree** là một cấu trúc cây đa nhánh (N-ary tree), là phiên bản nâng cấp của **B-Tree**. Nó được thiết kế đặc biệt để lưu trữ dữ liệu trên **ổ đĩa cứng (Disk/SSD)** thay vì RAM.

Khác biệt lớn nhất:
*   **B-Tree:** Lưu dữ liệu ở cả nút trong và nút lá.
*   **B+ Tree:** Chỉ lưu **khóa (keys)** để dẫn đường ở nút trong. Tất cả **dữ liệu thật (records)** đều nằm ở **nút lá**.

---

## 2. 📐 Cấu trúc đặc biệt

```text
INDEX SET (Chỉ chứa Key dẫn đường)
           [ 30  |  60 ]
          /      |      \
    [10|20]   [40|50]   [70|80]  <-- Nút trong
       |         |         | 
=======|=========|=========|======
DATA SET (Chứa dữ liệu thật & Liên kết)
  
[10,15] -> [20,25] -> [30,35] -> ... -> [80,90]
```

**Đặc điểm nhận dạng:**
1.  **Cây rất lùn và bè (Wide & Shallow):** Mỗi nút có thể chứa hàng trăm/nghìn con. Điều này giúp giảm số lần đọc ổ cứng.
2.  **Lá liên kết (Linked Leaves):** Tất cả các nút lá được nối với nhau bằng danh sách liên kết. Điều này cho phép duyệt tuần tự (Range Scan) cực nhanh.

---

## 3. ⚙️ Tại sao B+ Tree thắng thế trong Database?

Giả sử bạn cần tìm tất cả khách hàng có ID từ 100 đến 500:

*   **Với BST/Red-Black Tree:** Bạn phải nhảy cóc qua lại giữa các nhánh cây (Random Access) -> Rất chậm trên ổ cứng quay (HDD).
*   **Với B+ Tree:**
    1.  Tìm ID 100 (mất O(log n)).
    2.  Từ lá chứa 100, cứ thế đi theo con trỏ `next` sang phải cho đến khi gặp 500. (Sequential Access) -> **Siêu nhanh**.

---

## 4. 🌍 Ứng dụng thực tế (Critical)

Gần như mọi hệ quản trị cơ sở dữ liệu (DBMS) đều dùng B+ Tree làm cấu trúc chỉ mục (Indexing) mặc định:

| Hệ thống | Sử dụng |
|----------|---------|
| **MySQL (InnoDB)** | Primary Key Index được tổ chức dạng B+ Tree. |
| **PostgreSQL** | Index mặc định (B-Tree của Postgres thực chất là biến thể B+ Tree). |
| **NTFS / ext4** | Các hệ thống tập tin (File Systems) dùng B+ Tree để quản lý thư mục và file. |

---

## 5. 🔑 Tổng kết

*   B+ Tree tối ưu cho việc **đọc/ghi trên ổ cứng**.
*   **Nút trong** chỉ là bản đồ chỉ đường. **Nút lá** mới chứa kho báu.
*   Hỗ trợ truy vấn khoảng (Range Query) tuyệt vời nhờ danh sách liên kết ở đáy.
*   Đây là lý do tại sao câu lệnh SQL `SELECT * FROM table WHERE id BETWEEN 1 AND 100` chạy nhanh như gió.
