class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedListPunto3:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def remove_node(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.prev is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                elif current.next is None:
                    self.tail = current.prev
                    if self.tail is not None:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

def parking_lot():
    # Crear la lista enlazada con los estacionamientos
    parking_list = DoublyLinkedListPunto3()
    parking_list.add_node(16)
    parking_list.add_node(6)
    parking_list.add_node(68)
    parking_list.add_node(88)
    parking_list.add_node(None) # Este es el estacionamiento a adivinar
    parking_list.add_node(98)

    # Pedir al usuario que indique si quiere retirar un vehículo y en caso afirmativo, cuál estacionamiento desea retirar
    response = input("¿Desea retirar un vehículo? (s/n): ")
    if response.lower() == "s":
        try:
            parking_number = int(input("Ingrese el número de estacionamiento que desea retirar: "))
            if 16 <= parking_number <= 98 and parking_number % 10 in [6, 8]:
                if parking_list.remove_node(parking_number):
                    print("El vehículo ha sido retirado correctamente.")
                    parking_list.print_list()
                else:
                    print("El número de estacionamiento ingresado no existe en la lista.")
            else:
                print("El número de estacionamiento ingresado no es válido.")
        except ValueError:
            print("Debe ingresar un número válido.")
    else:
        parking_list.print_list()

if __name__ == "__main__":
    parking_lot()