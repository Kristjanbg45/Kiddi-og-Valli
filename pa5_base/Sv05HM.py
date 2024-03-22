  
class HASH:
    def __init__(self, int_value, string_value):
        self.capacity = 10
        self.max_load_factor = 1.2
        self.size = 0
        self.buckets = []
        for i in range(self.capacity):
            self.buckets.append(i.bucket())

    def hash_function(self, key):
        return hash(key) % self.capacity
    
    def insert(self, key, value):
       pass 

    def __getitem__(self, key):
        for i in range(self.capacity):
            if self.buckets[i].key == key:
                return self.buckets[i].value

    def __setitem__(self, key, value):
        for i in range(self.capacity):
            if self.buckets[i].key == key:
                self.buckets[i].value = value
        


    def __len__(self):
        return self.size
    