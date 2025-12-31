import math
import random
import sys

from data_structures.tree.binary_heap import BinaryHeap

# arr = [5, 3, 4,1, 2,3]
# insertion_sort(arr)
# Sắp xếp chèn
# def insertion_sort(arr):
#     for j in range(1, len(arr)):
#         key = arr[j]
#         print("\n==============================")
#         print(f"BẮT ĐẦU vòng j = {j}")
#         print(f"👉 key = {key} (đang giữ TRONG BIẾN, chưa chèn)")
#         print(f"Mảng ban đầu: {arr}")
#
#         i = j - 1
#         print(f"i bắt đầu = {i}")
#
#         # Dịch chuyển các phần tử lớn hơn key sang phải
#         while i >= 0 and arr[i] > key:
#             print(f"\narr[{i}] = {arr[i]} > key ({key}) ❌")
#             print(f"➡️ Dịch arr[{i}] = {arr[i]} sang arr[{i+1}]")
#
#             arr[i + 1] = arr[i]
#             print(f"Mảng SAU khi dịch: {arr}")
#             print(f"⚠️ key = {key} VẪN NẰM TRONG BIẾN, CHƯA VÀO MẢNG")
#
#             i -= 1
#             print(f"i giảm xuống = {i}")
#
#         print("\n--- KẾT THÚC while ---")
#         print(f"Vị trí trống để chèn key là i+1 = {i+1}")
#         print(f"Chèn key = {key} vào arr[{i+1}]")
#
#         # Chèn key vào vị trí đúng
#         arr[i + 1] = key
#         print(f"✅ Mảng sau khi chèn key: {arr}")
#
#     print("\n==============================")
#     print(f"MẢNG ĐÃ SẮP XẾP: {arr}")
#     return arr
# arr = [5, 3, 4,1, 2,3]
# insertion_sort(arr)



# def insertion_sort(arr):
#     for j in range(1, len(arr)):
#         key = arr[j] # key = 3
#         i = j - 1 # i = 0
#
#         while i >= 0 and arr[i] > key:
#             arr[i + 1] = arr[i] # mảng = 5 5 4
#             i = i - 1 # i = -1
#
#         arr[i + 1] = key # 3 5 4
#     print(f"Mảng đã sắp xếp: {arr}")
#     return arr
#


# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         min_idx = i
#
# def _swap(arr, i, j):
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp
#     return arr

# def _swap(arr, i, j):
#     print(f"👉 SWAP: đổi arr[{i}] = {arr[i]} với arr[{j}] = {arr[j]}")
#     arr[i], arr[j] = arr[j], arr[i]
#     print(f"👉 Mảng sau swap: {arr}")
#     return arr


# arr = [2, 4, 1, 3]
# selection_sort(arr)

# def selection_sort(arr):
#     print(f"MẢNG BAN ĐẦU: {arr}")
#
#     for i in range(len(arr) - 1): # i = 0 1 2
#         print("\n==============================")
#         print(f"BẮT ĐẦU VÒNG NGOÀI")
#         print(f"i = {i}")
#         print(f"Giả sử arr[{i}] = {arr[i]} là nhỏ nhất")
#
#         min_idx = i # i = 0
#         print(f"min_idx = {min_idx}") # = 0
#
#         for j in range(i + 1, len(arr)): #(1 , 4) = 1 2 3
#             print(f"\nSo sánh:")
#             print(f"j = {j}")
#             print(f"arr[{j}] = {arr[j]}")
#             print(f"arr[min_idx] = arr[{min_idx}] = {arr[min_idx]}")
#             # 4 < 0
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#                 print(f"👉 arr[{j}] nhỏ hơn → cập nhật min_idx = {min_idx}")
#             else:
#                 print("👉 Không nhỏ hơn → giữ nguyên min_idx")
#
#         print("\n--- KẾT THÚC vòng trong ---")
#         print(f"Giá trị nhỏ nhất tìm được:")
#         print(f"min_idx = {min_idx}, giá trị = {arr[min_idx]}")
#
#         print(f"➡️ Swap arr[{i}] với arr[{min_idx}]")
#         arr = _swap(arr, i, min_idx)
#         print(f"Mảng sau swap: {arr}")
#
#     print("\n==============================")
#     print(f"MẢNG ĐÃ SẮP XẾP: {arr}")
#     return arr
#
#
# arr = [2, 4, 1, 3]
# selection_sort(arr)

# def selection_sort(arr):
#     for i in range(len(arr) - 1):
#         min_idx = i
#
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#
#         arr = _swap(arr, i, min_idx)
#     print(f"mảng : {arr}")
#     return arr
#
# def _swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]
#     return arr
#
# arr = [2, 1]
# selection_sort(arr)

# def merge_sort(arr):
#     print("\n=== BẮT ĐẦU MERGE SORT ===")
#     print("Input:", arr)
#     return _merge_sort_helper(arr, 0, len(arr) - 1)
#
#
# def _merge_sort_helper(arr, p, r):
#     print(f"\nGọi _merge_sort_helper(arr, p={p}, r={r})")
#
#     if p < r:
#         q = (p + r) // 2
#         print(f"Chia: q = ({p} + {r}) // 2 = {q}")
#         print(f"Chia: p={p}, q={q}, r={r}")
#
#         print("→ Gọi nửa trái")
#         _merge_sort_helper(arr, p, q)
#
#         print("→ Gọi nửa phải")
#         _merge_sort_helper(arr, q + 1, r)
#
#         print("→ Gọi merge")
#         merge(arr, p, q, r)
#
#     print(f"Kết quả đoạn [{p}:{r}] → {arr[p:r+1]}")
#     return arr
#
#
# def merge(arr, p, q, r):
#     print(f"\nMERGE p={p}, q={q}, r={r}")
#
#     left = arr[p:q + 1] + [float('inf')]
#     right = arr[q + 1:r + 1] + [float('inf')]
#
#     print("Left :", left)
#     print("Right:", right)
#
#     i = j = 0
#
#     for k in range(p, r + 1):
#         print(f"\nSo sánh left[{i}]={left[i]} và right[{j}]={right[j]}")
#
#         if left[i] < right[j]:
#             arr[k] = left[i]
#             print(f"→ Gán arr[{k}] = {left[i]} (từ left)")
#             i += 1
#         else:
#             arr[k] = right[j]
#             print(f"→ Gán arr[{k}] = {right[j]} (từ right)")
#             j += 1
#
#         print("Arr hiện tại:", arr)
#
#     print("MERGE XONG:", arr[p:r+1])
#     return arr
#
#
# # TEST
# arr = [1, 3, 4, 2, 6, 5]
# merge_sort(arr)


# def heap_sort(arr):
#     heap = BinaryHeap(arr) # khởi tạo min heap
#     result = [] # Tạo mảng rỗng để chứa các phần tử đã sắp xếp
#
#     while not heap.is_empty():
#         result.append(heap.extract_min())
#     print(f"Result : {result}")
#     return result
#
# arr = [1, 3, 5, 7, 2, 4]
# heap_sort(arr)

# def _swap(arr, i, j):
#     print(f"    🔁 Swap arr[{i}]={arr[i]} ↔ arr[{j}]={arr[j]}")
#     temp = arr[i]
#     arr[i] = arr[j]
#     arr[j] = temp
#     print(f"    👉 Sau swap: {arr}")
#     return arr
#
#
# def quick_sort(arr):
#     print("=== BẮT ĐẦU QUICK SORT ===")
#     print(f"Input: {arr}\n")
#     result = _quick_sort_helper(arr, 0, len(arr) - 1)
#     print("\n=== KẾT THÚC QUICK SORT ===")
#     return result
#
#
# def _partition(arr, p, r):
#     print(f"\n📌 PARTITION: p={p}, r={r}")
#     x = arr[r]
#     print(f"👉 Chọn pivot = arr[{r}] = {x}")
#
#     i = p - 1
#     print(f"👉 Khởi tạo i = {i}")
#
#     for j in range(p, r):
#         print(f"  🔍 So sánh arr[{j}]={arr[j]} với pivot={x}")
#         if arr[j] <= x:
#             i += 1
#             print(f"    ✔ arr[{j}] <= pivot → i tăng thành {i}")
#             arr = _swap(arr, i, j)
#         else:
#             print(f"    ❌ arr[{j}] > pivot → bỏ qua")
#
#     print(f"👉 Đưa pivot về đúng vị trí: swap arr[{i+1}] và arr[{r}]")
#     arr = _swap(arr, i + 1, r)
#
#     print(f"✅ Pivot {x} ở vị trí index {i+1}")
#     print(f"👉 Mảng sau partition: {arr}")
#
#     return i + 1, arr
#
#
# def _quick_sort_helper(arr, p, r):
#     print(f"\n🔁 Gọi quick_sort_helper(p={p}, r={r})")
#
#     if p < r:
#         print(f"👉 p < r → tiếp tục chia")
#         q, arr = _partition(arr, p, r)
#
#         print(f"\n➡️ Đệ quy TRÁI: p={p}, r={q-1}")
#         arr = _quick_sort_helper(arr, p, q - 1)
#
#         print(f"\n➡️ Đệ quy PHẢI: p={q+1}, r={r}")
#         arr = _quick_sort_helper(arr, q + 1, r)
#     else:
#         print(f"⛔ p >= r → dừng (đoạn 1 phần tử hoặc rỗng)")
#
#     print(f"🔚 Trả về đoạn [{p}:{r}] → {arr}")
#     return arr
#
# arr = [1, 3, 5, 2]
# quick_sort(arr)

def counting_sort(arr, upper=None, lower=0):
    '''
    Counting Sort
    - Chỉ dùng khi dữ liệu là số nguyên
    - Giá trị nằm trong một khoảng hữu hạn [lower, upper]
    - Độ phức tạp: O(n)
    '''

    # Nếu mảng rỗng hoặc chỉ có 1 phần tử thì không cần sort
    if len(arr) <= 1:
        return arr

    # Nếu không truyền upper (và lower) vào
    # thì tự động tìm min (lower) và max (upper) của mảng
    if not upper:
        lower, upper = _find_bounds(arr)

    # Tạo mảng đếm c
    # Độ dài = số lượng giá trị có thể xuất hiện = upper - lower + 1
    # Ban đầu tất cả đều = 0
    c = [0 for _ in range(lower, upper + 1)]

    # ĐẾM SỐ LẦN XUẤT HIỆN CỦA MỖI GIÁ TRỊ
    for value in arr:
        # value - lower để ánh xạ giá trị thật → index trong mảng c
        c[value - lower] += 1

    # CHUYỂN c THÀNH MẢNG CỘNG DỒN (prefix sum)
    # Sau bước này:
    # c[i] = số phần tử <= (i + lower)
    for i in range(1, upper - lower + 1):
        c[i] += c[i - 1]

    # Tạo mảng kết quả b (copy từ arr để giữ kích thước)
    b = arr[:]

    # DUYỆT NGƯỢC arr ĐỂ GIỮ TÍNH STABLE
    for i in range(len(arr) - 1, -1, -1):
        # Xác định vị trí đúng của arr[i] trong mảng b
        b[c[arr[i] - lower] - 1] = arr[i]

        # Giảm bộ đếm vì đã đặt xong 1 phần tử
        c[arr[i] - lower] -= 1

    # Trả về mảng đã được sắp xếp
    return b


def _find_bounds(arr):
    # Khởi tạo lower = +∞
    # Đảm bảo phần tử đầu tiên trong arr chắc chắn nhỏ hơn lower
    lower = float('inf')

    # Khởi tạo upper = -∞
    # Đảm bảo phần tử đầu tiên trong arr chắc chắn lớn hơn upper
    upper = float('-inf')

    # Duyệt từng phần tử trong mảng
    for value in arr:

        # Nếu tìm được giá trị nhỏ hơn lower hiện tại
        # thì cập nhật lower
        if value < lower:
            lower = value

        # Nếu tìm được giá trị lớn hơn upper hiện tại
        # thì cập nhật upper
        if value > upper:
            upper = value

    # Sau vòng lặp:
    # lower = giá trị nhỏ nhất trong mảng
    # upper = giá trị lớn nhất trong mảng
    return lower, upper















