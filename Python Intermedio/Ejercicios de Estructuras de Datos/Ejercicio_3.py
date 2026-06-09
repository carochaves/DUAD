class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current, data):

        if data < current.data:

            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursive(current.left, data)

        else:

            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursive(current.right, data)

    def print_tree(self):
        self._print_recursive(self.root)

    def _print_recursive(self, node):

        if node is not None:

            print(node.data)

            self._print_recursive(node.left)
            self._print_recursive(node.right)