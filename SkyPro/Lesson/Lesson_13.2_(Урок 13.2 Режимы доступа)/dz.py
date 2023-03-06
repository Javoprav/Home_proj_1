class Node:
    """класс узла"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """Добавление элемента """
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        """Добавление элемента """
        remove = self.top
        self.top = self.top.next_node
        return remove.data


node1 = Node({'id': 1})
node2 = Node({'id': 2})
node1.next_node = node2
print(node1.next_node)
print(node1.next_node.next_node)