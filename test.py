class ArrayList:
    def __init__(self):
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0

    def resize(self):
        if self.size >= self.capacity:
            self.capacity *= 2
            new_arr = [None] * self.capacity
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr

    def insert_ordered(self, value):
        self.resize()
        if self.size == 0:
            self.arr[0] = value
            self.size += 1
        else:
            index_to_insert = 0
            for i in range(self.size):
                if value < self.arr[i]:
                    # Shift elements to make space for the new value
                    for j in range(self.size, i, -1):
                        self.arr[j] = self.arr[j - 1]
                    # Insert the value at the correct position
                    self.arr[i] = value
                    self.size += 1
                    break
                index_to_insert = i + 1
            else:
                # If the value is greater than or equal to all existing elements, insert at the end
                self.arr[index_to_insert] = value
                self.size += 1

# Example usage
arr_list = ArrayList()
arr_list.insert_ordered(3)
arr_list.insert_ordered(1)
arr_list.insert_ordered(2)
arr_list.insert_ordered(5)
arr_list.insert_ordered(4)

# Print the resulting ArrayList outside of the method
print(arr_list.arr)

