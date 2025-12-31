class Node:
    __slots__ = ('value', 'left', 'right')

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, value):
        parent, prev = self.find_parent(self.root, None, value)

        if not parent:
            self.root = Node(value)
        else:
            if value <= parent.value:
                parent.left = Node(value)
            else:
                parent.right = Node(value)

        self.size = self.size + 1


    def find_parent(self, node, prev, value, to_remove=False):
        if not node:
            return prev, None

        if to_remove:
            if value == node.value:
                return node, prev

        if value <= node.value:
            if node.left:
                node, prev = self.find_parent(node.left, node, value, to_remove)
            return node, prev

        if node.right:
            node, prev = self.find_parent(node.right, node, value, to_remove)
        return node , prev

    def remove(self, value):
        curr , parent = self.find_parent(self.root, None, value, True)

        if (not curr or curr.value != value):
            raise ValueError()

        if not parent:
            self.root = self.remove_root(self.root, True)


    def remove_root(self, root, left=True):
        if not root:

