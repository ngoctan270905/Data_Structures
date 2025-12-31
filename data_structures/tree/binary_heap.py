import random

class BinaryHeap:
    def __init__(self, arr=None):
        # Giữ số 0 giả ở đầu để tính Cha = i // 2, Con = 2 * i
        self._list = [0]

        # Nếu có array thì sẽ lặp toàn bộ các value trong mảng và insert vào self._list
        if arr:
            for value in arr:
                self.insert(value)

    # Hàm insert vào
    def insert(self, value):
        self._list.append(value)
        self._bubble_up(len(self._list) - 1)



    # Xem phần tử nhỏ nhất trong list
    def peek_min(self):
        if self.is_empty():
            raise ValueError("Heap trống")
        return  self._list[1]

    def extract_min(self):
        if self.is_empty():
            raise ValueError("Heap trống")

        min_val = self._list[1]

        # Nếu chỉ 1 phần tử tính cả phần tử giá thì pop nó ra
        if len(self._list) == 2:
            return self._list.pop()

        self._list[1] = self._list.pop()
        self._bubble_down(1)
        return min_val



    # Hàm kiểm tra rỗng
    def is_empty(self):
        return len(self._list) == 1

    # Hàm len
    def __len__(self):
        return len(self._list) - 1

    # Hàm hoán đổi
    def _swap(self, i, j):
        self._list[i], self._list[j] = self._list[j], self._list[i]

    def _bubble_up(self, idx):
        """
            Sửa heap sau khi INSERT:
            Đẩy phần tử mới thêm lên trên cho đến khi
            không còn vi phạm luật min-heap (cha <= con)
        """

        # Chỉ chạy vòng lặp nếu index > 1 thì con = index : 2
        while idx > 1:
            parent = idx // 2
            # Và nếu con < cha thì swap đảo ngược lại
            if self._list[idx] < self._list[parent]:
                self._swap(idx, parent)

                idx = parent
            else:
                break

    def _bubble_down(self, idx):
        # Lặp nếu còn ít nhất 1 con bên trái
        while 2 * idx < len(self._list):
            left = 2 * idx
            right = 2 * idx + 1
            smallest = left

            if right < len(self._list) and self._list[right] < self._list[left]:
                smallest = right

            if self._list[idx] > self._list[smallest]:
                self._swap(idx, smallest)
                idx = smallest
            else:
                break

    def __iter__(self):
        yield from iter(self._list[1:])

def test_heap():
    bh = BinaryHeap()
    values = random.sample(range(-15, 15), 30)
    for v in values:
        bh.insert(v)
        print(list(bh))

    for v in iter(bh):
        print(v)


test_heap()



