# General tree (25%)
# Implement the following functions inside the general tree class containing numbers.
# (10%) find_smallest(self)
# ● Finds and returns the smallest value in the tree
# (10%) sum_tree(self)
# ● Adds and returns all numbers in the tree
# (5%) odd_number_list(self)
# ● Returns a list of all numbers in the tree

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class GeneralTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            self.root.children.append(new_node)

    def find_smallest(self):
        return self._find_smallest(self.root)

    def _find_smallest(self, node):
        if not node:
            return float('inf')
        smallest = node.value
        for child in node.children:
            smallest = min(smallest, self._find_smallest(child))
        return smallest

    def sum_tree(self):
        return self._sum_tree(self.root)

    def _sum_tree(self, node):
        if not node:
            return 0
        total = node.value
        for child in node.children:
            total += self._sum_tree(child)
        return total

    def odd_number_list(self):
        return self._odd_number_list(self.root)

    def _odd_number_list(self, node):
        if not node:
            return []
        numbers = [node.value] if node.value % 2 else []
        for child in node.children:
            numbers.extend(self._odd_number_list(child))
        return numbers
    
# Test
tree = GeneralTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)
tree.insert(63)
tree.insert(60)
tree.insert(70)
tree.insert(80)
tree.insert(90)
tree.insert(100)

print(tree.find_smallest()) # 10
print(tree.sum_tree()) # 550
print(tree.odd_number_list()) # [10, 30, 50, 70, 90]

print("All tests passed.")
