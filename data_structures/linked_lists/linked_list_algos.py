from data_structures.linked_lists.list_class import LinkedList, Node

# Remove duplicates
def remove_duplicates(ll: LinkedList) -> None:
    seen = set()
    current = ll._head
    prev = None

    while current:

        # --------------- GIÁ TRỊ CHƯA XUẤT HIỆN -----------------
        if current.value not in seen:
            seen.add(current.value) # đánh dấu đã gặp
            print(f"Đã ghi nhớ node: {current.value} ")
            prev = current
            current = current.next

        # ---------------- GÍA TRỊ BỊ TRÙNG -----------
        else:
            print(f"Node {current.value} này trùng rồi nhé nhưng nó là head nên sẽ giữ nguyên")
            xoa = current.value
            # ----- Nếu Node cần xóa chính là head ---------
            if current == ll._head:

                ll._head = current.next # nếu node là head = current thì rời node sang current
                current = ll._head


            else:
                print(f"Sẽ xóa 1 ở đằng sau")
                prev.next = current.next # bỏ qua current
                current = current.next

            ll._len = ll._len - 1
            print(f"Đã xóa node trùng {xoa} ")



ll = LinkedList()
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
for value in values:
    ll.insert(value)
print(f"Danh sách ban đầu: {list(ll)}")
remove_duplicates(ll)
print(f"Danh sách sau khi check: {list(ll)}")


# Find nth last element
def nth_from_end(linked_list: LinkedList, n: int):
    first = linked_list._head
    second = linked_list._head

    # Dịch frist trước
    for _ in range(n - 1):
        print(f"Đi vào đây")
        if not first:
            return None
        print(f"First đủ độ dài")
        first = first.next
        print(f"First sau khi dịch là: {first.value}")

    if not first:
        return None

    # Chỉ lặp khi first.next là node hợp lệ khi == None sẽ dừng lại
    while first.next:
        first = first.next
        second = second.next

    return second.value

linked_list = LinkedList()
values = [1, 2, 3, 4, 5]

for value in values:
    linked_list.insert(value)

print(f"ds trớc {list(linked_list)}")
print(nth_from_end(linked_list, 1))


# Remove node given only its object
def remove_node(node: Node):
    # Nếu không có node hoặc ko có node next
    if not node or not node.next:
        raise Exception("Lỗi")
    # Copy bản sao của next sang node hin tại
    node.value = node.next.value
    node.next = node.next.next

ll = LinkedList()
values = [1,2,3,4,5]
for value in values:
    ll.insert(value)

print(f"Danh sách ban đầu: {list(ll)}")
cur = ll._head

while cur and cur.value != 4:
    cur = cur.next

remove_node(cur)
print("Sau khi xóa:", list(ll))










