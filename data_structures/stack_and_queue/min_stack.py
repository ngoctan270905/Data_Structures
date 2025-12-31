from data_structures.stack_and_queue.stack_class import Stack

class MinStack:
    def __init__(self):
        self.main_stack = Stack() # stack chính lưu dữ liệu
        self.min_stack = Stack()  # stack phụ lưu giá trị nhỏ nhất

    # thêm phần tử vào nhánh main
    def push(self, value):
        self.main_stack.push(value)

        # Nếu stack phụ đang trống hoặc value đó bằng với min hiện tại thì sẽ lưu giá trị đó vào stack min
        if self.min_stack.is_empty() or value <= self.min_stack.peek():
            self.min_stack.push(value)

    # Lấy phần tử đầu tiên
    def pop(self):
        # Nếu stack chính đang rỗng thì trả về None
        if self.main_stack.is_empty():
            return None

        # Lấy phần tử trên đỉnh ra khỏi stack chính
        removed_value = self.main_stack.pop()

        # Nếu phần tử này = với lại phần tử đầu tiên của min thì lấy ra cả phần tử đầu tiên của min
        if removed_value == self.min_stack.peek():
            self.min_stack.pop()

        return removed_value # trả về phần tử đó

    # Xem giá trị nhỏ nhất
    def get_min(self):
        # Nếu stack phụ đang rỗng trả về None
        if self.min_stack.is_empty():
            return None
        return self.min_stack.peek()

# --- Test ---
ms = MinStack()
ms.push(5)
ms.push(5)
ms.push(10)
ms.push(3)
ms.push(15)

print(f"Min hiện tại: {ms.get_min()}") # Kết quả: 1
print(ms.pop())
print(ms.pop())
print(ms.pop())
print(ms.pop())
print(ms.pop())
print(f"Min sau khi pop: {ms.get_min()}") # Kết quả: 2




