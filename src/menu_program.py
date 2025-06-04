from .helpers.insertion_service import *

def create_product():
    """
    Está función se encarga de recibir los datos para gestionar la creación de un nuevo producto.
    Recolecta los datos necesarios para la inserción en base de datos los
    No recibe argumentos.
    """
    print("""
===================================
        Creación de producto
===================================
""")
    tipo = input('Diga el tipo: ')
    nombre = input('Diga el nombre: ')
    precio = int(input('Diga el precio: '))
    ingredientes = input('Diga los ongredientes(arena de maiz, carne de lomo, etc.):')
    disponibilidad = input('Está disponible? (si/no)')

    print(f"""
===================================
        Creación de producto
===================================
¿Quieres guardar el producto?
    Tipo: {tipo}.
    Nombre: {nombre}.
    Precio: {precio}.
    Ingredientes: {ingredientes}.
    Disponible: {disponibilidad}.

Presiona 'S' para guardar o 'N' para eliminar el producto
""")

    option_cp = input('> ')
    if (option_cp.lower() == 's'):
        create_new_product(tipo.capitalize(), nombre.capitalize(), precio, ingredientes, disponibilidad.lower())
    elif (option_cp.lower() == 'n'):
        print('\n Gracias, vovleras al menú principal.\n')
    else:
        print('Opción no valida.')