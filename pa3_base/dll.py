
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__current_position = None

    def insert(self, key, data):
        """Inserts an item with that value in front of the node at the current position
                ■ The new node is now in the current position"""
        if self.__size == 0 and not self.__head and not self.__tail:
            return
        else:
            new_node = Node(data)
            current_node = self.__head
            previous_node = None
            while current_node:
                if current_node.data == key:
                    if not previous_node: 
                        new_node.next = current_node
                        current_node.prev = new_node
                        self.__head = new_node 
                    else:
                        previous_node.next = new_node
                        new_node.prev = previous_node
                        new_node.next = current_node
                        current_node.prev = new_node
                    self.__size += 1
                    return
                else:
                    previous_node = current_node
                    current_node = current_node.next

    def remove(self, data):
        """Removes the node at the current position if there is one (otherwise does nothing)
                ■ The node behind the removed node is now in the current position"""
        if self.__size == 0 and not self.__head and not self.__tail:  # the code should work without checking for head and tail nodes
            return 
        
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
            self.__size -= 1

        elif self.__size > 1:
            current_node = self.__head
            previous_node = None
            while current_node:  
                if current_node.data == data:
                   
                    if not previous_node:
                        next_node = current_node.next
                        next_node.prev = None   
                        current_node.next = None
                        del current_node
                        self.__head = next_node
                    elif not current_node.next:
                        previous_node.next = None
                        current_node.prev = None
                        del current_node
                        self.__tail = previous_node
                    else:
                        next_node = current_node.next
                        current_node.prev = None
                        current_node.next = None
                        del current_node
                        previous_node.next = next_node
                        next_node.prev = previous_node
                    self.__size -= 1
                    return  
                else:
                    previous_node = current_node
                    current_node = current_node.next

    def get_value(self):
        """ Returns the value of the item at the current position in the list (None if not item)"""
        if self.__current_position:
            return self.__current_position.data
        else:
            return None

    def move_to_next(self):
        """Moves the current position one item closer to the tail/trailer
                ■ Do nothing if at end of list"""
        if self.__current_position and self.__current_position.next:
            self.__current_position = self.__current_position.next

    def move_to_prev(self):
        """Moves the current position one item closer to the head/header
                ■ Do nothing if at beginning"""
        if self.__current_position and self.__current_position.prev:
            self.__current_position = self.__current_position.prev

    def move_to_pos(self, pos):
        """Moves the current position to item #position in the list
                ■ The first actual data item is #0
                ■ Do nothing if position not between beginning and end (including both)"""
        if pos < 0 or pos >= self.__size: 
            return  
        else:
            current_node = self.__head
            index = 0
            while current_node and index < pos:
                current_node = current_node.next
                index += 1
            self.__current_position = current_node

    def clear(self):
        """Clears all nodes from the list"""
        current_node = self.__head
        while current_node:
            next_node = current_node.next
            current_node.prev = None  
            current_node.next = None  
            current_node = next_node  
        self.__head = None
        self.__tail = None  
        self.__size = 0  
        

    def get_first_node(self):
        """Returns the first Node of the list
                ■ The headers next pointer should be pointing to this node
                ■ Returns the node, not the value inside it
            If list is empty, return None"""
        if self.__size == 0:
            return None
        else:
            return self.__head

    def get_last_node(self):
        """Returns the last Node of the list
                ■ The tailers prev pointer should be pointing to this node
                ■ Returns the node, not the value inside it
            If list is empty, return None"""
        if self.__size == 0:
            return None
        else:
            return self.__tail

    def partition(self, low, high):
        """Takes in two nodes from the list as a parameter
                ■ You can fetch these nodes with get_first_node and get_last_node
            Uses low as a pivot
                ■ Loops from low to high and moves all nodes smaller than low so they are
            ahead(left side) of the low node.
            Example:
            ■ List before partition: 10 7 7 14 10 15 1 8 2 4 13 7 11 8 8 13
            ● Low is 10 which is also a pivot
            ● High is 13
            ■ List after partition: 7 7 1 8 2 4 7 8 8 10 14 10 15 13 11 13
            ■ Note: The list is not sorted but all elements left of 10 are smaller then 10
            and all elements right of 10 are bigger(or equal)
            ● The order of elements above and below pivot doesn’t matter, only
            that they are on the correct side of the pivot
            After partitioning current position should point towards the pivot
            Partition will only be tested with valid low and high nodes"""
        
        x = high.data
        z = low.prev
        y = low
         
        while(y != high):
            if(y.data <= x):
                z = low if(z == None) else z.next
 
                temp = z.data
                z.data = y.data
                y.data = temp
            y = y.next
                         
        z = low if (z == None) else z.next;  
        temp = z.data
        z.data = high.data
        high.data = temp
        return z
    

            

    def sort(self, low, high):
        """Order the items in the list with any method that uses only your DLL structure
            ■ No moving everything to another structure, sorting and then moving back!
            After sorting reset the current position to the beginning of the list
            5% Bonus for implementing sort using quicksort
            ■ Partition comes in handy when implementing quicksort"""
        if(high != None and low != high and low != high.next):
            temp = self.partition(low, high)
            self.sort(low,temp.prev)
            self.sort(temp.next, high)

    def __len__(self):
        """Returns the number of items in the list"""
        return self.__size

    def __str__(self):
        """Returns string with all the items in the list with a single space between them"""
        ret_str = ""
        current_node = self.__head
        while current_node:
            ret_str += str(current_node.data) + " "
            current_node = current_node.next
        return ret_str.strip()

if __name__ == "__main__":
    #create tests here if you want
    #tests in other files will be used for grading so its better to just make a new test file.
    pass
    
