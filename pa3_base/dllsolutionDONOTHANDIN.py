
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def prepend(self, data):
        new_node = Node(data)
        # check if the list is empty
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = new_node
            self.__tail = new_node
        else:
            # when there is atleast one node
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node  # new_node is our new head node
        self.__size += 1

    def append(self, data):
        new_node = Node(data)
        # check if the list is empty
        if self.__size == 0 and not self.__head and not self.__tail:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node  # new_node is our new tail node
        self.__size += 1

    def add_before(self, key, data):
        # check for empty data structure
        if self.__size == 0 and not self.__head and not self.__tail:
            print("Please add some data to your List.")
        else:
            # when we have atleast one node
            new_node = Node(data)
            current_node = self.__head
            previous_node = None
            while current_node:
                # add before the head node
                if current_node.data == key:
                    if not previous_node:  # if the previous node is None
                        new_node.next = current_node
                        current_node.prev = new_node
                        self.__head = new_node  # the "new_node" is our new head node
                    else:
                        # adding before any node BUT the head node
                        previous_node.next = new_node
                        new_node.prev = previous_node
                        new_node.next = current_node
                        current_node.prev = new_node
                    self.__size += 1
                    return   # to avoid infinite loop
                else:
                    # if the data does not match
                    previous_node = current_node
                    current_node = current_node.next

    def add_after(self, key, data):
        # check for empty data structure
        if self.__size == 0 and not self.__head and not self.__tail:
            print("Please add some data to your List.")
        else:
            # when we have atleast one node
            new_node = Node(data)
            current_node = self.__head
            while current_node:
                if current_node.data == key:
                    # add after the tail node
                    if not current_node.next:  # if "current_node.next" points to None
                        current_node.next = new_node
                        new_node.prev = current_node
                        self.__tail = new_node  # new node is not the tail node of our list
                    else:
                        # adding after any node BUT the tail node
                        next_node = current_node.next
                        current_node.next = new_node
                        new_node.prev = current_node
                        new_node.next = next_node
                        next_node.prev = new_node
                    self.__size += 1
                    return   # to avoid infinite loop
                else:
                    current_node = current_node.next

    def remove(self, data):
        # when there is no node
        if self.__size == 0 and not self.__head and not self.__tail:  # the code should work without checking for head and tail nodes
            print("No data to remove")
        # when the list contains 1 node
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
            self.__size -= 1
        # when the list contains more than one node
        elif self.__size > 1:
            current_node = self.__head
            previous_node = None
            while current_node:  # while the current node is not None
                if current_node.data == data:
                    # removing the head node
                    if not previous_node:
                        next_node = current_node.next
                        next_node.prev = None   # the head always points towards a None
                        current_node.next = None
                        del current_node
                        self.__head = next_node
                    # removing the tail node
                    elif not current_node.next:  # when the next node to the current node is a None (tail node)
                        previous_node.next = None
                        current_node.prev = None
                        del current_node
                        self.__tail = previous_node
                    # removing any random node BUT not the head and the tail nodes
                    else:
                        next_node = current_node.next
                        current_node.prev = None
                        current_node.next = None
                        del current_node
                        previous_node.next = next_node
                        next_node.prev = previous_node
                    self.__size -= 1
                    return   # avoiding an infinite loop
                else:
                    # traversing to the next node
                    # if the data is not matched
                    previous_node = current_node
                    current_node = current_node.next

    def find(self, data):
        current_node = self.__head
        while current_node:  # while the current node is not None
            if current_node.data == data:
                print(f"{data} found.")
                return
            else:
                current_node = current_node.next
        else:
            print(f"{data} not found.")

    def traverse_fw(self):
        current_node = self.__head
        while current_node:   # while the current node is not None
            print(current_node.data)
            current_node = current_node.next

    def traverse_bw(self):
        current_node = self.__tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev

    def list_size(self):
        return self.__size


if __name__ == "__main__":
    myList = Doubly()
    myList.append(1)
    myList.append(2)
    myList.append(3)

    myList.prepend(0)
    myList.prepend(-1)
    myList.prepend(-2)

    myList.add_before(-2, -3)
    myList.add_before(0, -0.5)

    myList.add_after(3, 4)
    myList.add_after(0, 0.5)

    myList.remove(-3)
    myList.remove(0)
    myList.remove(4)

    myList.traverse_fw()
    print()
    myList.traverse_bw()
    print()

    print("Size:", myList.list_size())

    myList.find(0.5)