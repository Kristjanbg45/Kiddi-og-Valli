from array_deque import ArrayDeque
from my_linked_list import LinkedList
from my_stack import Stack
from my_queue import Queue

print("\nTESTING LINKED_LIST\n")

lis = LinkedList()
lis.push_back(3)
lis.push_back(1)
lis.push_back(6)
lis.push_back(9)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
lis.push_front(11)
lis.push_front(16)
lis.push_front(13)
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_front())
print(lis.pop_front())
print(lis.pop_back())
print(lis.pop_back())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)
print(lis.pop_back())
print(lis.pop_front())
print("container of size: " + str(lis.get_size()) + ":")
print(lis)


print("\nTESTING QUEUE\n")

queue = Queue()
queue.add(2)
queue.add(4)
queue.add(7)
print("the data structure is of size: " + str(queue.get_size()))
print(queue.remove())
print(queue.remove())
print(queue.remove())
print(queue.remove())
print("the data structure is of size: " + str(queue.get_size()))

print("\nTESTING STACK\n")

stack = Stack()
stack.push(2)
stack.push(4)
stack.push(7)
print("the data structure is of size: " + str(stack.get_size()))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("the data structure is of size: " + str(stack.get_size()))





print("\nKIDDITESTQUEUE\n")
# Import the Queue class
from my_queue import Queue

# Create a queue instance
queue = Queue()

# Add some elements to the queue
queue.add(1)
queue.add(2)
queue.add(3)

# Print the size of the queue
print("Size of the queue:", queue.get_size())  # Expected output: 3

# Remove and print elements from the queue until it's empty
print("Removing elements from the queue:")
while queue.get_size() > 0:
    print(queue.remove())

# Add more elements to the queue
queue.add(4)
queue.add(5)
queue.add(6)

# Print the size of the queue
print("Size of the queue:", queue.get_size())  # Expected output: 3

# Print the contents of the queue
print("Contents of the queue:", queue)  # Expected output: Contents of the queue: 4 5 6


print("\nKIDDITESTSTACK\n")

# Import the Stack class
from my_stack import Stack

# Create a stack instance
stack = Stack()

# Add some elements to the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Print the size of the stack
print("Size of the stack:", stack.get_size())  # Expected output: 3

# Remove and print elements from the stack until it's empty
print("Popping elements from the stack:")
while stack.get_size() > 0:
    print(stack.pop())

# Add more elements to the stack
stack.push(4)
stack.push(5)
stack.push(6)

# Print the size of the stack
print("Size of the stack:", stack.get_size())  # Expected output: 3

# Print the contents of the stack
print("Contents of the stack:", stack)  # Expected output: Contents of the stack: 4 5 6