from data_structures.linked_lists.list_class import Node
#
# class Queue:
#     def __init__(self):
#         self._head = None # Con trỏ quản lí đầu hàng ( Nới lấy dữ liệu ra )
#         self._tail = None # Con trỏ quản lí cuối hàng ( Nới lấy dữ liệu vào )
#         self._size = 0 # Số lượng phần tử trong queue
#
#     # Hàm kiểm tra xem QUEUE có rỗng ko nếu = 0 thì True
#     def is_empty(self):
#         return self._size == 0
#
#     # Thêm một phần tử mới vào cuối hàng đợi
#     def enqueue(self, value):
#         node = Node(value)
#         if self.is_empty(): # nếu hàng đợi rỗng thì cả 2 sẽ trỏ vào node
#             self._head = self._tail = node
#         else: # trường hợp hàng đợi đã có phần tử
#             self._tail.next = node # nối vào cuối hàng đợi
#             self._tail = node # cập nhật
#
#         self._size = self._size + 1 # cộng vào hàng đợi
#
#     # Lấy và xóa phần tử ở đầu hàng đợi
#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError("Hàng đợi đang rỗng")
#
#         # Lưu lại giá trị của node đầu tiên để trả về
#         value = self._head.value
#         # Chuyển sang node kế
#         self._head = self._head.next
#
#         # Nếu chuyển sang mà là rỗng thì tail đồng thời cũng phải đưa về none để đồng bộ
#         if self._head is None:
#             self._tail = None
#
#         # lấy và xóa phần tử đó trong hàng đợi
#         self._size = self._size - 1
#
#         # trả về ok
#         return value
#
#     # Xem giá trị ở đầu hàng
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("Hàng đợi rỗng")
#         return self._head.value
#
#     # Hàm len để xử lí tổng phần tử
#     def __len__(self):
#         return self._size
#
#     def __iter__(self):
#         current = self._head  # Bắt đầu từ đầu hàng
#         while current is not None:
#             yield current.value  # Trả về giá trị của node hiện tại
#             current = current.next  # Nhảy sang node tiếp theo
#
#
# q = Queue()
# q.enqueue("Nguyễn Tấn")
# q.enqueue("Nguyễn Tấnn")
# q.enqueue("Nguyễn Tấnnn")
# print(f"Danh sách hàng đợi hiện tại: {list(q)}")
# print(f"Xem thằng đứng đầu hàng là ai: {q.peek()} là người đứng đầu hàng")
# print(f"Số phần tử trong hàng đợi hiện tại: {len(q)}")
# print(f"Lấy ra thằng đứng đầu tiên: {q.dequeue()} và hàng đợi còn lại: {list(q)}. Lấy xong thì còn: {len(q)} phần tử")
#
#
#
# class Queue:
#     def __init__(self):
#         self._head = None
#         self._tail = None
#         self.size = 0
#
#     def is_empty(self):
#         return self.size == 0
#
#     def enqueue(self, value):
#         node = Node(value)
#         if self.is_empty():
#             self._head = self._tail = node
#         else:
#             self._tail.next = node
#             self._tail = node
#
#         self.size += 1
#
#     def dequeue(self):
#         if self.is_empty():
#             raise IndexError("Queue is empty")
#
#         value = self._head.value
#         self._head = self._head.next
#
#         if self._head is None:
#             self._tail = None
#
#         self.size -= 1
#
#         return value
#
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("Queue is empty")
#         return self._head.value
#
#     def __iter__(self):
#         current = self._head
#         while current is not None:
#             yield current.value
#             current = current.next
#
#     def __len__(self):
#         return self.size
#
#


# class Queue:
#     def __init__(self):
#         self._head = None
#         self._tail = None
#         self._size = 0
#
#     def is_empty(self):
#         return self._size == 0
#
#     def enqueue(self, value):
#         node = Node(value)
#         if self.is_empty():
#             self._head = self._tail = node
#         else:
#             self._tail.next = node
#             self._tail = node
#
#         self._size += 1
#
#     def dequeue(self):
#         if self.is_empty():
#             return None
#
#         value = self._head.value
#         self._head = self._head.next
#
#         if self._head is None:
#             self._tail = None
#
#         self._size -= 1
#         return value
#
#     def peek(self):
#         if self.is_empty():
#             return None
#         return self._head.value
#
#     def __iter__(self):
#         current = self._head
#         while current is not None:
#             yield current.value
#             current = current.next
#
#     def __len__(self):
#         return self._size
#
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# print(f'Danh sách ban đầu: {list(queue)}')
# print(f"Lấy thằng {queue.dequeue()} ra và danh sách còn lại {list(queue)}")
# print(f"Test xem thằng đầu tiên: {queue.peek()}")

class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node

        self.size = self.size + 1

    def dequeue(self):
        if self.is_empty():
            return None
        value = self._head.value
        self._head = self._head.next

        if self._head is None:
            self._tail = None

        self.size = self.size - 1

        return value

    def peek(self):
        return self._head.value

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value
            current = current.next

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(f"Danh sach hien tai la: {list(queue)}")
print(f"thang vao dau tien va ra dau tien se la thang {queue.peek()}")
print(f"thang ra truoc {queue.dequeue()} va danh sach con lai {list(queue)}")




