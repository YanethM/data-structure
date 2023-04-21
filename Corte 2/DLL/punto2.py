class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def add_missing_nodes(self, linked_list):
        # Pedir al usuario el valor de los nodos faltantes
        attempts = 3
        missing_node_attempts = 0
        next_node_attempts = 0
        missing_node_data = None
        next_node_data = None
        while attempts > 0:
            if missing_node_attempts < 3:
                try:
                    missing_node_data = int(input("Ingrese el valor del nodo faltante (32): "))
                    if missing_node_data != 32:
                        raise ValueError
                    missing_node_attempts = 3
                except ValueError:
                    missing_node_attempts += 1
                    attempts -= 1
                    print("Intentos restantes:", 3 - missing_node_attempts)
            elif next_node_attempts < 3:
                try:
                    next_node_data = int(input("Ingrese el valor del siguiente nodo faltante (39): "))
                    if next_node_data != 39:
                        raise ValueError
                    next_node_attempts = 3
                except ValueError:
                    next_node_attempts += 1
                    attempts -= 1
                    print("Intentos restantes:", 3 - next_node_attempts)
            else:
                print("Se han agotado los intentos.")
                return None
        
        # Agregar los nodos faltantes a la lista
        current_data = self.head.data
        is_missing_node = False
        while current_data < next_node_data:
            current_data += 7
            if current_data == missing_node_data:
                self.add_node(missing_node_data)
                is_missing_node = True
            if is_missing_node and current_data != missing_node_data:
                is_missing_node = False
            if is_missing_node:
                self.add_node(current_data)
        self.print_list()
# Crear la lista enlazada
linked_list = LinkedList()
linked_list.add_node(4)
linked_list.add_node(11)
linked_list.add_node(18)
linked_list.add_node(46)
linked_list.add_node(53)
linked_list.add_node(60)

# Agregar los nodos faltantes a la lista
linked_list.add_missing_nodes(linked_list)