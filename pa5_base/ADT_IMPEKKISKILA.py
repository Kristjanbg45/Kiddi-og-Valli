import os
os.chdir("C:\Users\krist\github\SRAD\Kiddi-og-Valli")


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedListMap:
    def __init__(self):
        self.head = None
    
    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node
    
    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None
    
    def update(self, key, value):
        current = self.head
        while current:
            if current.key == key:
                current.value = value
                return
            current = current.next
    
    def remove(self, key):
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
    
    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(f"{current.key}: {current.value}")
            current = current.next
        return "{" + ", ".join(values) + "}"




#array

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].key == key:
            return mid
        elif arr[mid].key < key:
            low = mid + 1
        else:
            high = mid - 1
    return None

class ArrayListMap:
    def __init__(self):
        self.arr = []
    
    def insert(self, key, value):
        self.arr.append(Node(key, value))
        self.arr.sort(key=lambda node: node.key)
    
    def find(self, key):
        index = binary_search(self.arr, key)
        if index is not None:
            return self.arr[index].value
        return None
    
    def update(self, key, value):
        index = binary_search(self.arr, key)
        if index is not None:
            self.arr[index].value = value
    
    def remove(self, key):
        index = binary_search(self.arr, key)
        if index is not None:
            del self.arr[index]
    
    def __len__(self):
        return len(self.arr)
    
    def __str__(self):
        return "{" + ", ".join(f"{node.key}: {node.value}" for node in self.arr) + "}"


#s.readlines