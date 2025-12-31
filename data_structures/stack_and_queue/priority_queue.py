import random
from data_structures.tree.binary_heap import BinaryHeap

class PriorityQueue:
    def __init__(self):
        self._heap = BinaryHeap() # Instance

    # Hàm nhìn phần tử nhỏ nhất
    def peek(self):
        return self._heap.peek_min()

    # Hàm kiểm tra rỗng
    def is_empty(self):
        return self._heap.is_empty()

    # Hàm thêm phần tử vào hàng đợi
    def enqueue(self, value):
        self._heap.insert(value)

    # Hàm xóa phần tử khỏi hàng đợi
    def dequeue(self):
        return self._heap.extract_min()

    def __iter__(self):
        yield from iter(self._heap)

    def __len__(self):
        return len(self._heap)


# --- TEST ---
def test_priority_queue():
    pq = PriorityQueue()
    # Tạo danh sách số ngẫu nhiên
    values = [10, 5, 20, 1, 15]
    print(f"Dữ liệu đưa vào: {values}")

    for v in values:
        pq.enqueue(v)

    print(f"Hàng đợi (theo cấu trúc Heap): {list(pq)}")
    print("\nLấy ra theo thứ tự ưu tiên (Min-Heap):")

    while not pq.is_empty():
        # Bây giờ x sẽ nhận được giá trị thay vì None
        x = pq.dequeue()
        print(f"Lấy ra: {x}")


if __name__ == "__main__":
    test_priority_queue()