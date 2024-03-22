class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node:
    def __init__(self, key, data, next=None):
        self.key = key
        self.data = data
        self.next = next

class Bucket:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException("Key already exists.")
        new_node = Node(key, data, self.head)
        self.head = new_node
        self.size += 1

    def update(self, key, data):
        current = self.head
        while current:
            if current.key == key:
                current.data = data
                return
            current = current.next
        raise NotFoundException("Key not found.")

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.data
            current = current.next
        raise NotFoundException("Key not found.")

    def contains(self, key):
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def remove(self, key):
        current = self.head
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        raise NotFoundException("Key not found.")

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.size


class HashMap:
    def __init__(self, initial_capacity=10):
        self.buckets = []
        for i in range(initial_capacity):
            self.buckets.append(Bucket())
        self.size = 0

    def hash_function(self, key):
        return hash(key) % len(self.buckets)

    def insert(self, key, data):
        index = self.hash_function(key)
        try:
            self.buckets[index].insert(key, data)
            self.size += 1
            if self.size > 1.2 * len(self.buckets):
                self.rebuild()
        except ItemExistsException:
            raise ItemExistsException("Key already exists.")

    def update(self, key, data):
        index = self.hash_function(key)
        self.buckets[index].update(key, data)

    def find(self, key):
        index = self.hash_function(key)
        return self.buckets[index].find(key)

    def contains(self, key):
        index = self.hash_function(key)
        return self.buckets[index].contains(key)

    def remove(self, key):
        index = self.hash_function(key)
        self.buckets[index].remove(key)
        self.size -= 1

    def __setitem__(self, key, data):
        try:
            self.update(key, data)
        except NotFoundException:
            self.insert(key, data)

    def __getitem__(self, key):
        return self.find(key)

    def __len__(self):
        return self.size

    def rebuild(self):
        old_buckets = self.buckets
        self.buckets = []
        for i in range(2 * len(old_buckets)):
            self.buckets.append(Bucket())
        self.size = 0
        for bucket in old_buckets:
            current = bucket.head
            while current:
                self.insert(current.key, current.data)
                current = current.next
