# class NotFound(Exception):
#     pass

# class ArrayList:
#     def __init__(self):
#         self.capacity = 4
#         self.arr = [5] * self.capacity
#         self.size = 8

#     def __str__(self):
#         return ", ".join(str(self.arr[i]) for i in range(self.size))

#     def find(self, value):
#         if self.size == 0:
#             raise NotFound()
#         return self.recursive_binary_search(value, 0, self.size - 1)

#     def recursive_binary_search(self, value, low, high):
       

#         mid = (low + high) // 2

#         if self.arr[mid] == value:
#             return mid
#         elif self.arr[mid] > value:
#             return self.recursive_binary_search(value, low, mid - 1)
#         else:
#             return self.recursive_binary_search(value, mid + 1, high)

#     def linear_search(self, value):
#         for i in range(len(self.arr)):
#             if self.arr[i] == value:
#                 return i
#         return -1

# # Example of using recursive_binary_search
# my_list = ArrayList()
# my_list.arr = [1, 3, 5, 7, 9, 11, 13, 15]  # Assuming a sorted list for binary search

# try:
#     result = my_list.recursive_binary_search(15, 0, my_list.size - 1)
#     print(f"The value 7 is found at index {result}.")
# except NotFound:
#     print("The value 7 is not present in the list.")

def modulus(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    # TODO: remove 'pass' and implement functionality
    if b > a:
        return a
    else:
        return modulus(a - b, b)

print(modulus(14,4))