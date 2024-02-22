class NotFound(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def __str__(self):
        return ", ".join(str(self.arr[i]) for i in range(self.size))

    def find(self, value):
        for i in range(1, len(self.arr)):
            if self.arr[i - 1] > self.arr[i]:
                return self.linear_search(value)
        return self.recursive_binary_search(value, 0, self.size - 1)

    def recursive_binary_search(self, value, low, high):
        if low > high:
            raise NotFound()

        mid = (low + high) // 2

        if self.arr[mid] == value:
            return mid
        elif self.arr[mid] > value:
            return self.recursive_binary_search(value, low, mid - 1)
        else:
            return self.recursive_binary_search(value, mid + 1, high)

    def linear_search(self, value):
        for i in range(len(self.arr)):
            if self.arr[i] == value:
                return i
        return -1

# Test case
my_list = ArrayList()
my_list.arr = [1, 3, 5, 7, 9]  # Assuming a sorted list for binary search

try:
    result = my_list.find(5)
    print(f"The value 5 is found at index {result}.")
except NotFound:
    print("The value 5 is not present in the list.")