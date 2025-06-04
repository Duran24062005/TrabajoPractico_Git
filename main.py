from src.helpers.insertionFunc import abrierJSON
from src.menu_program import *


def EmpanadasDonaPepa():
    """
    Menu Principal de programa.
    No recibe argumentos.
    No tiene retorno.
    """
    program = True
    while program:
        print("""
===========================
    Empanadas Doña Pepa
===========================
Elija una Opción:
    1. Crear Producto
    2. Ver todos los Productos
    3. Filtrar por nombre
    4. Actualizar Producto
    5. Eliinar Producto
    6. Salir
===========================
""")
        entrada = int(input("> "))

        if (entrada == 1):
            print(abrierJSON())

        elif (entrada == 2):
            show_products()

        elif (entrada == 3):
            filter_by_name()

        elif (entrada == 4):
            pass

        elif (entrada == 5):
            pass

        elif (entrada == 6):
            print("""
¿Estas seguro? 
    Presiona 'S' si quieres salir o 'N' si no.
""")
            election = input('> ')
            if (election.lower() == 's'):
                print('¡¡Gracias por visitarnos!!')
                break
            elif (election.lower() == 'n'):
                print('¡¡De acuerdo, volvamos!!\n')
                continue
            else:
                print("Opción no valida, por favor seleccione otra.")

        else:
            print("Opción no valida, por favor seleccione otra.")


if __name__=="__main__":
    EmpanadasDonaPepa()