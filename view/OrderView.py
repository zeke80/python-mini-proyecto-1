from View import View

class OrderView(View):
    def __init__(self, options: dict):
        super().__init__(options)

    def display_main_message(self):
        print('**************************')
        print('*     SANDWICHES UCAB    *')
        print('**************************\n')
        print('Creacion de ordenes:\n')

    def display_request_message(self):
        print('Indique la opcion con que desea continuar: ', end='')

    def display_error_message(self):
        print('=> Debe ingresar una opcion valida')
    