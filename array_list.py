class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class NotOrdered(Exception):
    pass

class ArrayList:
    def __init__(self):
        # TODO: remove 'pass' and implement functionality
        self.capacity = 4
        self.arr = [None] * self.capacity
        self.size = 0
        

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        # Returns a string with all items from the array
        # ○ Have a comma and a space between them
        # ■ but no brackets ([ ]) around them
        # TODO: remove 'pass' and implement functionality
        return_string = ""
        for i in range(self.size):
            return_string += str(self.arr[i])
        return return_string
    
#ffjjfjfjfjf
    

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # Inserts an item into the list before the first item
        # TODO: remove 'pass' and implement functionality
        self.resize()
        for i in range(self.size):
            if self.size == 0:
                self.arr[0] = value
            self.arr[i] = self.arr[i-1]
        self.arr[0] = value
        self.size += 1

    # #Time complexity: O(n) - linear time in size of list
    # def insert(self, value, index):
    #     # Inserts an item into the list at a specific location, not overwriting other items
    #     # ○ If the index is not within the current list, raise IndexOutOfBounds()
    #     # ○ It should be possible to add to the front and back of the list, and anywhere in between
    #     # TODO: remove 'pass' and implement functionality
    def insert(self, value, index):
        # Inserts an item into the list at a specific location, not overwriting other items
        # If the index is not within the current list, raise IndexOutOfBounds()
        if index < 0 or index > self.size:
            raise IndexError("out of bounds")
        self.resize()
        for i in range(self.size, index, -1, -1):
            self.arr[i + 1] = self .arr[i]
        self.arr[index] = value
        self.size += 1



    #Time complexity: O(1) - constant time
    def append(self, value):
        """ Inserts an item at the end of the list """
        # Adds an item to the list after the last item
        # ● set_at(self, value, index)
        # ○ Sets the value at a specific location to a specific value
        # ■ Overwrites the current value there
        # ■ If the index is not within the current list, raise IndexOutOfBounds()
        # 
        # TODO: remove 'pass' and implement functionality
        if(self.size >= self.capacity):
            return None
        self.arr[self.size] = value
        self.size += 1 
        
       
    #valli

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        pass
    #valli

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        #get the first index of the array
        for x in self.arr:
            print(x)

    


    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        pass
    #kiddi

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        pass
    #valli
        
    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        if self.size >= self.capacity:
            self.capacity = self.capacity * 2

        return self.capacity
    #kiddi
     

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        #  TODO: remove 'pass' and implement functionality
    #Time complexity: O(1) - constant time
        if index < 0 or index >= self.size:
            raise IndexOutOfBounds()
        elif index == self.size - 1:
            self.size -= 1
        else:
            for i in range(index, self.size - 1):
                self.arr[i] = self.arr[i+1]
            self.size -= 1
    #kiddi



    def clear(self):
        # TODO: remove 'pass' and implement functionality
        pass

    #valli

    #Time complexity: O(n) - linear time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #kiddi

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarithmic time in size of list
    def find(self, value):
        # TODO: remove 'pass' and implement functionality
        raise NotFound()
    
    #valli

    #Time complexity: O(n) - linear time in size of list
    def remove_value(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #kiddi


if __name__ == "__main__":
    #Kristján Tests.

    my_list = ArrayList()
    my_list.insert(2,2)
    print(my_list)

    # my_list2 = ArrayList()
    # my_list2.prepend(2)
    # print(my_list2)

    # my_list3 = ArrayList()
    # my_list3.append(2)
    # print(my_list3)

    # my_list4 = ArrayList()
    # my_list4.remove_at(2)
    # print(my_list4)
    # print("hi")

    # my_list5 = ArrayList()
    # my_list5.insert_ordered(2)
    # print(my_list5)

    # my_list6 = ArrayList()
    # my_list6.find(2)
    # print(my_list6)

    # my_list7 = ArrayList()
    # my_list7.remove_value(2)
    # print(my_list7)

    # my_list8 = ArrayList()
    # my_list8.clear()
    # print(my_list8)

    # my_list9 = ArrayList()
    # my_list9.get_last()
    # print(my_list9)

    # my_list10 = ArrayList()
    # my_list10.get_at(2)
    # print(my_list10)

    # my_list11 = ArrayList()
    # my_list11.get_first()
    # print(my_list11)

    # my_list12 = ArrayList()
    # my_list12.set_at(2,2)
    # print(my_list12)




    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level



    #here im testing the insert function and printing the outcome
    print("Testing insert function")
    print(my_list.insert(2, 2))


    arr_lis = ArrayList()
    print(str(arr_lis))






















def modulus(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    #TODO: remove 'pass' and implement functionality
    pass


def how_many(lis1, lis2):
    #TODO: remove 'pass' and implement functionality
    pass


# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_modulus(num1, num2):
    print("The modulus of " + str(num1) + " and " + str(num2) + " is " + str(modulus(num1, num2)))

def test_how_many(lis1, lis2):
    print(str(how_many(lis1, lis2)) + " of the items in " + str(lis1) + " are also in " + str(lis2))

def run_recursion_program():

    print("\nTESTING MODULUS:\n")

    test_modulus(8, 3)
    test_modulus(9, 3)
    test_modulus(10, 3)
    test_modulus(11, 3)
    test_modulus(8, 2)
    test_modulus(0, 7)
    test_modulus(15, 5)
    test_modulus(128, 16)
    test_modulus(128, 15)

    print("\nTESTING HOW MANY:\n")

    test_how_many(['a', 'f', 'd', 't'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['a', 'b', 'f', 'g', 'a', 't', 'c'], ['a', 'b', 'c', 'd', 'e'])
    test_how_many(['f', 'g', 't'], ['a', 'b', 'c', 'd', 'e'])


if __name__ == "__main__":
    run_recursion_program()

# TESTING MODULUS:

# The modulus of 8 and 3 is 2
# The modulus of 9 and 3 is 0
# The modulus of 10 and 3 is 1
# The modulus of 11 and 3 is 2
# The modulus of 8 and 2 is 0
# The modulus of 0 and 7 is 0
# The modulus of 15 and 5 is 0
# The modulus of 128 and 16 is 0
# The modulus of 128 and 15 is 8

# TESTING HOW MANY:

# 2 of the items in ['a', 'f', 'd', 't'] are also in ['a', 'b', 'c', 'd', 'e']
# 4 of the items in ['a', 'b', 'f', 'g', 'a', 't', 'c'] are also in ['a', 'b', 'c', 'd', 'e']
# 0 of the items in ['f', 'g', 't'] are also in ['a', 'b', 'c', 'd', 'e']
    


    
f1 = open("out.txt")
f2 = open("expected_out.txt")
f3 = open("out_diff.txt", "w+")

line_number = 1
for line1, line2 in zip(f1, f2):
    if line1.strip() != line2.strip():
        print("Difference in line " + str(line_number))
        f3.write("Difference in line " + str(line_number) + "\n")
    line_number += 1

f1.close()
f2.close()
f3.close()