from punto1 import DoublyLinkedList
from punto2 import LinkedList
from punto3 import DoublyLinkedListPunto3
from punto3 import parking_lot
parking_lot()



from double_linked_list import DoublyLinkedList
inst_dll = DoublyLinkedList()
inst_dll.add_node_at_end('A')
inst_dll.add_node_at_end('B')
inst_dll.add_node_at_start('C')
inst_dll.add_node_at_end('D')
inst_dll.add_node_at_end('E')
inst_dll.print_list()
inst_dll.add_node_in_position(5, "Prueba")
inst_dll.print_list()
inst_dll.add_node_in_position(1, "NewNode1")
inst_dll.add_node_in_position(2, "NewNode2")
inst_dll.print_list()
print('\nEliminar cuarto nodo')
inst_dll.remove_node_by_position(4)
inst_dll.print_list()
print('\nEliminar segundo nodo')
inst_dll.remove_node_by_position(2)
inst_dll.print_list()
print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()

print('\nEliminar último nodo')
inst_dll.remove_node_by_position(5)
inst_dll.print_list()

print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()

print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()

print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()

print('\nEliminar primer nodo')
inst_dll.remove_node_by_position(1)
inst_dll.print_list()

print('\nAñadiendo nodos nuevamente')
inst_dll.add_node_at_start("a")
inst_dll.add_node_at_start("2")
inst_dll.add_node_at_start("3")
inst_dll.add_node_at_start("0")
inst_dll.add_node_at_start("-6")
inst_dll.add_node_at_start("1")
inst_dll.add_node_at_start("A")
inst_dll.add_node_at_start("3")
inst_dll.add_node_at_start("0")
inst_dll.add_node_at_start("0")
inst_dll.print_list()
inst_dll.reverse()
inst_dll.print_list()
inst_dll.sort_asc()
inst_dll.print_list()
inst_dll.has_duplicates_with_information_v2()

inst_dll.calculate_complexity(inst_dll.add_node_at_end)

