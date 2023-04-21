class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        # Verificar si el dato cumple con el patrón
        if self.tail is None:
            if data % 2 == 0:
                self.head = self.tail = Node(data)
        else:
            if (data - self.tail.data) % 2 == 1:
                new_node = Node(data)
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


    
my_list = DoublyLinkedList() 
my_list.add_node(2) 
my_list.add_node(5) 
my_list.add_node(10) 
my_list.add_node(17) 
my_list.add_node(26)
''' Verificar que no añada el 36 '''
my_list.add_node(36) 
my_list.add_node(37) 
my_list.add_node(50) 
my_list.add_node(65) 
my_list.add_node(82) 
my_list.print_list()
