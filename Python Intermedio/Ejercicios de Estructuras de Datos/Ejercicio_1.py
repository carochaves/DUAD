class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            raise Exception("El stack está vacío")

        removed_data = self.top.data
        self.top = self.top.next

        return removed_data

    def print_stack(self):
        current = self.top

        while current:
            print(current.data)
            current = current.next