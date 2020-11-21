from view.View import View
from model.Order import Order


class CloneSandwichView(View):
    def __init__(self, options: dict):
        super().__init__(options)

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Clonar sandwich:\n')
    
    def start_display(self):
        self.clean_screen()
        self.display_main_message()
        if len(self.options) == 1:
            self.display_empty()
        else:
            self.display_options_menu()
            self.display_request_message()

    def display_request_message(self):
        print('Indique el numero del sandwich que desea clonar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')
    
    def display_finish_message(self):
        print('\nClonacion exitosa\n', end='')
        print('************************************')
        print('\nPresione ENTER para continuar: ', end='')
    
    def display_request_quantity(self):
        print('Indique cuantas copias del sandwich desea agregar (n > 0): ',end='')

    def display_empty(self):
        print('\nNo se encuentran sandwiches en la orden para clonar')
        print('Favor agregar un sandwich primero')
        print('************************************')
        print('\nPresione ENTER para continuar: ', end='')

    def display_options_menu(self):
        for command,option in self.options.items():
            if command == 'q':
                continue
            print(f'( {command} )    {option}')
        print(f'( q )    Salir')
        print()           
        