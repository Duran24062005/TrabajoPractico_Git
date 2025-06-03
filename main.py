def EmpanadasDonaPepa():
    """Menu Principal"""
    program = True
    while program:
        print("""
===========================
    Empanadas Doña Pepa
===========================
Elija una Opción:
    1. Crear Producto
    2. Ver Producto
    3. Actualizar Producto
    4. Eliinar Producto
    5. Salir
===========================
""")
        entrada = int(input("> "))

        if (entrada == 1):
            print('hoola')

        elif (entrada == 2):
            pass

        elif (entrada == 3):
            pass

        elif (entrada == 4):
            pass

        elif (entrada == 5):
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