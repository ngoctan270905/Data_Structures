from data_structures.linked_lists.list_class import Node

# class Stack:
#     def __init__(self):
#         self._top = None
#         self._size = 0
#     # kiểm tra tồn tại
#     def is_empty(self):
#         return self._size == 0
#
#     # Thêm phần tử vào đỉnh stack
#     def push(self, value):
#         node = Node(value, self._top) # tạo node mới
#         # thêm node vào đỉnh
#         self._top = node
#         self._size = self._size + 1
#
#     # lấy và xóa phần tử khỏi đỉnh stack
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("Stack rỗng")
#
#         value = self._top.value # lưu giá trị
#         self._top = self._top.next # nối xuống dưới
#         self._size = self._size - 1
#         return value
#
#     # xem phần tử trên đỉnh
#     def peek(self):
#         if self.is_empty():
#             raise IndexError("Stack rỗng")
#         return self._top.value
#
#     def __iter__(self):
#         current = self._top # đỉnh
#         while current is not None:
#             yield current.value # trả về
#             current = current.next # xuống node dưới
#
#     def __len__(self):
#         return self._size
#
# stack = Stack()
# stack.push("Nguyễn Tấn")
# stack.push("Nguyễn Tấnn")
# stack.push("Nguyễn Tấnnn")
# stack.push("Nguyễn Tấnnnn")
# print(f"Danh sách Stack hiện tại là: {list(stack)}")
# print(f"Thằng thêm cuối cùng là: {stack.peek()} và thằng sẽ ra trước là: {stack.pop()}. Còn lại {len(stack)}")


# class Stack:
#     def __init__(self):
#         self._top = None
#         self._size = 0
#
#     def is_empty(self):
#         return self._size == 0
#
#     def push(self, value):
#         node = Node(value, self._top)
#
#         self._top = node
#
#         self._size += 1
#
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("Stack is empty")
#
#         value = self._top.value
#         self._top = self._top.next
#         self._size -= 1
#         return value
#
#     def peek(self):
#         return self._top
#
#     def __iter__(self):
#         current = self._top
#         while current is not None:
#             yield current.value
#             current = current.next
#
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# print(f"Danh sach hien tai la: {list(stack)}")
#
# print(f"Lay ra so {stack.pop()} va danh sach con lai la{list(stack)}")

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        node = Node(value, self.top)

        self.top = node
        self.size = self.size + 1

    def pop(self):
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next

        self.size = self.size - 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def __iter__(self):
        current = self.top
        while current is not None:
            yield current.value
            current = current.next

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(f"Danh sach hien tai la: {list(stack)}")
print(f"Thu lay thang tren dinh ra: {stack.pop()} va danh sach con lai la {list(stack)}")








