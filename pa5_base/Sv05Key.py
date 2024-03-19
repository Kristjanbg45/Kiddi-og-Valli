class MyHashableKey:
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value

    def __eq__(self, other):
        return (self.int_value == other.int_value) and (self.string_value == other.string_value)

    def __hash__(self):
        # Simple hash function for demonstration; customize for better distribution
        hash_base = 31
        result = 1
        result = hash_base * result + self.int_value
        result = hash_base * result + hash(self.string_value)
        return result
