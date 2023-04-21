'''
    Data type: list practice
    Date: 25/01/23
'''
# 1. Declarar la clase
class ListPractice:
    #2. Crear función inicializadora de la clase
    def __init__(self):
        #Definir las variables globales de la clase
        self.student_name = ""
        self.courses_list = ['POO', 'TAD']

    #3. Función customizada
    def show_info_list(self):
        # Imprimir el contenido de la lista courses_list
        print(self.courses_list)
        # Cantidad de elementos que tiene la lista
        print(len(self.courses_list))
    
    #4. Función que solicita al usuario ingresar información
    def input_data_courses(self):
        # 1. Declaramos una variable a nivel de método
        print('Ingrese la sgte información:')
        # Solicitud de texto
        self.student_name = input('Nombre: ')
        # Solicitud de número entero
        courses_number = int(input('Cantidad asignaturas: '))
        #Validamos si el courses_number es menor que el tamaño actual de la lista
        if courses_number <= len(self.courses_list):
            print(' >> Error: Cursos a inscribir es menor o igual que 2 <<')
        else:
            # Solicitar nombre de las asignaturas al usuario
            for course in range(courses_number):
                # Variable que almacena el nombre de la asignatura
                course_name = input('Nombre asignatura: ')
                # Añadimos nuevo elemento al final de la lista append()
                self.courses_list.append(course_name)
            # Imprimir contenido de la lista
            print(self.courses_list)




