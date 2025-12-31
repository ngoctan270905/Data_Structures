from data_structures.stack_and_queue.stack_class import Stack

# class MyQueue:
#     def __init__(self):
#         self.stack_in = Stack() # cửa vào
#         self.stack_out = Stack() # cửa ra
#
#     def enqueue(self, value): # thêm vào cuối hàng đợi
#         self.stack_in.push(value)
#
#     def _transfer(self):
#         if self.stack_out.is_empty():
#             while not self.stack_in.is_empty():
#                 item = self.stack_in.pop() 4 3 2 1
#                 self.stack_out.push(item)
#
#     def is_empty(self):
#         return self.stack_out.is_empty() and self.stack_in.is_empty()
#
#     def dequeue(self):
#         if self.is_empty():
#             return "Hàng đợi trống"
#
#         self._transfer()
#         return self.stack_out.pop()
#
#     def peek(self): # xem phần tử ở đầu hàng đợi
#         if self.is_empty():
#             return "Rỗng"
#         self._transfer()
#         return self.stack_out.peek()
#
#
#
# # Khởi tạo Queue
# q = MyQueue()
#
# # 1. Test Enqueue (Thêm dữ liệu)
# print("--- Test Enqueue ---")
# q.enqueue("A")
# q.enqueue("B")
# q.enqueue("C")
# print("Đã thêm A, B, C")
#
# # 2. Test Peek (Xem người đầu tiên)
# print(f"Người đứng đầu hàng: {q.peek()}") # Kỳ vọng: A
#
# # 3. Test Dequeue (Lấy ra lần lượt)
# print("--- Test Dequeue ---")
# print(f"Lấy ra: {q.dequeue()}") # Kỳ vọng: A
# print(f"Lấy ra: {q.dequeue()}") # Kỳ vọng: B
#
# # 4. Test Enqueue mới khi đang có đồ ở stack_out
# print("--- Thêm người mới khi đang dở dang ---")
# q.enqueue("D")
# print(f"Lấy ra: {q.dequeue()}") # Kỳ vọng: C (vì C vào trước D)
# print(f"Lấy ra: {q.dequeue()}") # Kỳ vọng: D
#
# # 5. Test Hàng trống
# print(f"Lấy tiếp khi hết sạch: {q.dequeue()}") # Kỳ vọng: Hàng đợi trống

# class MyQueue:
#     def __init__(self):
#         self.stack_in = Stack()
#         self.stack_out = Stack()
#
#     def is_empty(self):
#         return self.stack_in.is_empty() and self.stack_out.is_empty()
#
#     def enqueue(self, value):
#         self.stack_in.push(value)
#
#     def transfer(self):
#         if self.stack_out.is_empty():
#             while not self.stack_in.is_empty():
#                 item = self.stack_in.pop()
#                 self.stack_out.push(item)
#
#     def dequeue(self):
#         if self.is_empty():
#             return None
#         self.transfer()
#         return self.stack_out.pop()
#
#     def peek(self):
#         if self.is_empty():
#             return None
#         self.transfer()
#         return self.stack_out.peek()
#
# m = MyQueue()
# m.enqueue(1)
# m.enqueue(2)
# m.enqueue(3)
# print(f"Nguoiwf dung dau hang la: {m.peek()}")
#
# # Hàm sắp xếp
# def sort_stack(input_stack):
#     temp_stack = Stack()
#     print("input stack ban đầu:", list(input_stack))
#     # Lặp input stack nếu ko phải rỗng
#     while not input_stack.is_empty():
#         print("input stack trước pop:", list(input_stack))
#         # Lấy phần tử top của input stack gắn vào current_val
#         current_val = input_stack.pop()
#         print(f"Pop xóa đi top của input stack: {list(input_stack)}")
#         print(f"Gía trị của current_val: {current_val}")
#
#         # Lặp tem_stack nếu ko rỗng và value top của tem stack > current_val
#         while not temp_stack.is_empty() and temp_stack.peek() > current_val:
#             print(f"Gía trị của temp_stack: {list(temp_stack)}")
#             input_stack.push(temp_stack.pop())
#             print(f"Lấy top của temp_stack và gán vào top của input_stack :{list(temp_stack)}")
#             print(f"Lấy top của temp stack cho vào input_stack: {list(input_stack)}")
#
#         temp_stack.push(current_val)
#         print(f"Push vào temp_stack: {list(temp_stack)}")
#         print(f"Danh sách tem stack hiện tại: {list(temp_stack)}")
#         print(f"----------")
#
#     return temp_stack
#
# # --- Test ---
# s = Stack()
# s.push(5)
# s.push(1)
# s.push(10)
#
# print("Stack trước khi sắp xếp (đỉnh -> đáy):", list(s))
#
# sorted_s = sort_stack(s)
#
# print("Stack sau khi sắp xếp (nhỏ -> lớn):", list(sorted_s))
#
# print("s:", list(s))
# print("sorted_s:", list(sorted_s))


def hanoi_towers(n, source, target, auxiliary, source_name, target_name, aux_name):
    """
    n: số lượng đĩa
    source: cọc nguồn (Stack)
    target: cọc đích (Stack)
    auxiliary: cọc trung gian (Stack)
    """
    # ĐIỀU KIỆN DỪNG: Nếu chỉ còn 1 đĩa, nhấc thẳng từ nguồn sang đích
    if n == 1:
        disk = source.pop()
        target.push(disk)
        print(f"Di chuyển đĩa {disk} từ {source_name} -> {target_name}")
        return

    # BƯỚC 1: Chuyển n-1 đĩa từ Nguồn sang Trung gian (mượn Đích làm chỗ dựa)
    hanoi_towers(n - 1, source, auxiliary, target, source_name, aux_name, target_name)

    # BƯỚC 2: Chuyển đĩa lớn nhất còn lại từ Nguồn sang Đích
    disk = source.pop()
    target.push(disk)
    print(f"Di chuyển đĩa {disk} từ {source_name} -> {target_name}")

    # BƯỚC 3: Chuyển n-1 đĩa từ Trung gian sang Đích (mượn Nguồn làm chỗ dựa)
    hanoi_towers(n - 1, auxiliary, target, source, aux_name, target_name, source_name)

# --- Chạy thử ---
# Khởi tạo 3 cái cọc
peg_A = Stack()
peg_B = Stack()
peg_C = Stack()

# Thêm 3 đĩa vào cọc A (số lớn nằm dưới)
for disk in [3, 2, 1]:
    peg_A.push(disk)

print("Bắt đầu giải tháp Hà Nội với 3 đĩa:")
hanoi_towers(3, peg_A, peg_C, peg_B, "Cọc A", "Cọc C", "Cọc B")

print("\nKết quả tại Cọc C (đỉnh -> đáy):", list(peg_C))
