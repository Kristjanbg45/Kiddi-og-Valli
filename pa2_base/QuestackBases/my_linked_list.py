class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_front(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1
    
    def pop_front(self):
        if not self.head:
            return None
        value = self.head.data
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.size -= 1
        return value
    
    def push_back(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def pop_back(self):
        if not self.tail:
            return None
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
            self.tail = prev
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return current.data

    def get_size(self):
        return self.size

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return ' '.join(result)
        
# # Example usage:
# linked_list = LinkedList()
# linked_list.push_back(1)
# linked_list.push_back(2)
# linked_list.push_back(3)
# print(linked_list)  # Output: 1 2 3
# print(linked_list.pop_front())  # Output: 1
# print(linked_list.pop_back())  # Output: 3
# print(linked_list.get_size())  # Output: 1
# print(linked_list)  # Output: 2