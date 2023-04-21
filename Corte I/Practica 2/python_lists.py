'''
    List methods
    Date: 27/01/23
'''
class ListMethods:
    #1. Método inicializador de la clase
    def __init__(self):
        # Definimos una lista vacía
        self.pets = []
        self.vehicles = list()

    #2. Método para añadir elementos en la lista
    def add_list_elements(self):
        # ['dog', 'cat']
        self.pets.append('dog')
        self.pets.append('cat')
        print(self.pets)

    #3. Método que solicita valores al usuario
    def input_data_vehicles_list(self):
        # Variables locales: vehicles_number, vehicle_type
        vehicles_number = int(input('Cúantos vehiculos tienes?'))
        # Recorrer una lista
        for vehicle_item in range(vehicles_number):
            vehicle_type = input('Tipo de vehiculo: ')
            # Añadimos el vehiculo a la lista
            self.vehicles.append(vehicle_type)
        # Imprimir toda la lista
        print(self.vehicles)
        # Imprimir último, penúltimo y antepúltimo elemento de la lista
        print(self.vehicles[-1], self.vehicles[-2])

    #4. Extraer subconjunto de una lista
    def show_collection_data_list(self):
        # Desde posición 2 hasta 3
        print(self.vehicles[-1:-3:4])
        # Todos los elementos de la lista
        print(self.vehicles[:])
        # Elementos desde un indice específico: 2 [2,3,...]
        print(self.vehicles[2:])
        # Elementos hasta un indice específico: 2 [0,1,2]
        print(self.vehicles[:2])
        # Acceder a TODOS los elementos de 2 en 2
        print(self.vehicles[::2])
        # Acceder a un SUBCONJUNTO de elementos de 2 en 2
        print(self.vehicles[1:5:2])
        


    #5. Iterar los elementos de una lista con for
    def iteration_list(self):
        for item in self.vehicles:
            print(item)
        #Validar si la lista contiene un valor específico
        if "carro".capitalize() in self.vehicles:
            print("Si se encontro valor")
        else:
            print("No se encontro el valor")

    #6. Añadir varios elementos al final de la lista
    def add_elements(self):
        self.vehicles.extend(['Avión', 'Tractomula', 'Otro medio'])
        print(self.vehicles)
    
    #7. Añadir un elemento en posición específica de la lista
    def add_specific_element(self):
        self.vehicles.insert(0, 'Moto')
        print(self.vehicles)

    #8. Eliminar último elemento de la lista
    def remove_last_element(self):
        self.vehicles.pop()
        print(self.vehicles)

    #9. Eliminar elemento de posición específica
    def remove_specific_element(self):
        # Primer elemento
        self.vehicles.pop(0)
        print(self.vehicles)

    #10. Eliminar todos los elementos de la lista
    """ def remove_all_elements(self):
        self.vehicles.clear() """

    #11. Eliminar de la lista un valor especifico: 'Tractomula'
    def remove_element_by_name(self):
        self.vehicles.remove("tractomula".capitalize())
        print(self.vehicles)

    #12. Eliminar todas las coincidencias de valor en la lista
    def remove_all_match_elements(self):
        new_list = list(filter(('Tractomula').__ne__, self.vehicles))
        print(new_list)






    
    


            



