class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            new_node.next = self.current
            new_node.prev = self.current.prev
            if self.current.prev:
                self.current.prev.next = new_node
            self.current.prev = new_node
            if self.current == self.head:
                self.head = new_node

    def remove(self):
        if self.current:
            if self.current.prev:
                self.current.prev.next = self.current.next
            if self.current.next:
                self.current.next.prev = self.current.prev
            if self.current == self.head:
                self.head = self.current.next
            if self.current == self.tail:
                self.tail = self.current.prev
            self.current = self.current.prev

    def get_value(self):
        if self.current:
            return self.current.data
        else:
            return None

    def move_to_next(self):
        if self.current and self.current.next:
            self.current = self.current.next

    def move_to_prev(self):
        if self.current and self.current.prev:
            self.current = self.current.prev

    def move_to_pos(self, pos):
        current_node = self.head
        count = 0
        while current_node and count != pos:
            current_node = current_node.next
            count += 1
        if count == pos:
            self.current = current_node

    def clear(self):
        self.head = None
        self.tail = None
        self.current = None

    def get_first_node(self):
        return self.head

    def get_last_node(self):
        return self.tail

    def partition(self, low, high):
        pivot = low.data
        left = low
        right = low.next

        while right != high.next:
            if right.data < pivot:
                left = left.next
                left.data, right.data = right.data, left.data
            right = right.next 

        low.data, left.data = left.data, low.data
        self.current = left

    def sort(self):
        def _quicksort(low, high):
            if low != high and high != None and low != None and low != high.next:
                partition_node = self.partition(low, high)
                _quicksort(low, partition_node.prev)
                _quicksort(partition_node.next, high)

        _quicksort(self.head, self.tail)

        # Reset current to the beginning of the list
        self.current = self.head

    def __len__(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def __str__(self):
        ret_str = ""
        current_node = self.head
        while current_node:
            ret_str += str(current_node.data) + " "
            current_node = current_node.next
        return ret_str.strip()

if __name__ == "__main__":
    # Testing the DLL implementation
    dll = DLL()
    dll.insert(10)
    dll.insert(7)
    dll.insert(7)
    dll.insert(14)
    dll.insert(10)
    dll.insert(15)
    dll.insert(1)
    dll.insert(8)
    dll.insert(2)
    dll.insert(4)
    dll.insert(13)
    dll.insert(7)
    dll.insert(11)
    dll.insert(8)
    dll.insert(8)
    dll.insert(13)
    
    print("List before sorting:")
    print(dll)
    
    dll.sort()
    
    print("List after sorting:")
    print(dll)
