from node2 import Node


def add(head_node, data):
    new_node = Node(data, head_node)
    return new_node

def string_func(head_node):
    if head_node == None:
        return ""
    ret_string = ""
    while head_node != None:
        ret_string += str(head_node.data) + ", "
        head_node = head_node.next
    ret_string = ret_string.strip(", ")
    return ret_string


my_node = Node(12)
my_node = add(my_node, 42)
print(my_node)
print(string_func(my_node))