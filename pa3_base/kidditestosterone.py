from dll import DLL  # Assuming the DLL class is defined in a module named dll_module

def test_insert():
    dll = DLL()
    dll.insert(None, 10)

    dll.insert(10, 20)  

 

def test_remove():
    dll = DLL()
    dll.insert(None, 10)
    dll.insert(10, 20)
    dll.insert(20, 30)

    dll.remove(20) 


    dll.remove(10)  


def test_sort():
    dll = DLL()
    dll.insert(None, 30)
    dll.insert(30, 10)
    dll.insert(10, 20)

    dll.sort(dll.get_first_node(), dll.get_last_node()) 



if __name__ == "__main__":
    test_insert()
    test_remove()
    test_sort()
    print("All tests passed successfully nice job kristján you are so beutyful man thinking about programs!")
