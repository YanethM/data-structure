from single_linked_list import SingleLinkedList
from prueba import Prueba
inst_sll = SingleLinkedList()
inst_prueba = Prueba()

# Ingresamos como parametro el valor del nodo

inst_prueba.comparar()
""" Métodos para añadir nodo """
inst_sll.create_node_sll_ends("Batman")
inst_sll.create_node_sll_ends('Robin')
inst_sll.create_node_sll_ends('Gatubela')
inst_sll.create_node_sll_ends('Deadpool')
inst_sll.create_node_sll_ends("Wolverine")
inst_sll.create_node_sll_unshift("Hulk")
# | Hulk | Batman | Robin | Wolverine
inst_sll.show_list()

""" Métodos de eliminar """
print('---------------------------------------------------')
print('     >> Eliminar último nodo <<')
inst_sll.delete_node_sll_pop()
inst_sll.show_list()

# | Hulk | Batman | Robin |

print('---------------------------------------------------')
print('\n     >> Eliminar primer nodo <<')
inst_sll.shift_node_sll()
inst_sll.show_list()
# | Batman | Robin |

print('---------------------------------------------------')
print('\n     >> Consultar valor de nodo <<')
inst_sll.get_node_value(1)
inst_sll.get_node_value(2)

print('---------------------------------------------------')
print('\n     >> Actualizar valor de nodo <<')
inst_sll.update_node_value(1, "Linterna verde")
inst_sll.show_list()

print('---------------------------------------------------')
print('\n     >> Eliminar nodo expecifico<<')
inst_sll.remove_node(3)
inst_sll.show_list()

print('ordanar')
inst_sll.medium_node()
inst_sll.show_list()
