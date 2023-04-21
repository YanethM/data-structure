from colorama import Fore,init
init()

class Superheros:
    def __init__(self):
        self.marvel_universe = []
        self.dc_universe = []
        self.menu_option = 0
    
    def initial_menu(self):
        print(Fore.BLUE + 'Seleccione una opción del menú'+ Fore.RESET)
        while True:
            try:
                self.menu_option = int(input('      1. Marvel\n      2. D.C.\n      3. Salir\n' + Fore.YELLOW + '>>>' + Fore.RESET))
                if self.menu_option < 1 or self.menu_option > 3:
                    print('Opción incorrecta')
                elif self.menu_option == 1:
                    print('Marvel')
                elif self.menu_option == 2:
                    print('D.C.')
                else:
                    print(Fore.RED + 'Salir' + Fore.RESET)
                    break
            except ValueError:
                print('Error en la opción indicada')
