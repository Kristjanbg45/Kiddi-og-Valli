from my_linked_list import LinkedList

class Stack:
    def __init__(self):
        # Pick one of these to use.
        # Stack must have the container you dont choose for Queue
        
        self.container = LinkedList()


    def push(self, data):
        self.container.push_back(data)
    
    def pop(self):
        if self.container:
            if self.container.get_size() > 0:
                return self.container.pop_back()
        return None
    
    def get_size(self):
        if self.container:
            return self.container.get_size()
        return 0
    
    def __str__(self):
        if self.container:
            return str(self.container)
        return ""


if __name__ == "__main__":
    print("STACK TESTS")
    print("\n")
    stack = Stack()
    print(stack)
    print("size: " + str(stack.get_size()))
    print(stack.pop())
    stack.push("A")
    print(stack)
    print("size: " + str(stack.get_size()))
    stack.push("B")
    print(stack)
    print("size: " + str(stack.get_size()))
    stack.push("C")
    print(stack)
    print("size: " + str(stack.get_size()))