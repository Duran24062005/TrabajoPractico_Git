from .helpers.insertion_service import *
<<<<<<< HEAD

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
=======
from tabulate import tabulate



def show_products():
    print("""
==============================
    Ver todos los productos
==============================
""")
    products = show_all_products()
    if (products):
        print(tabulate(products, headers='keys', tablefmt='rounded_grid'))
    else:
        print("\n¡¡No hay productos registrado, por favor registre!!")



def filter_by_name():
    print("""
==============================
      Filtrar por nombre
==============================
""")
    nombre = input('Diga el nombre del producto: ')
    productos = filter_name(nombre)
    
    if (all is not None):
        print(tabulate(productos, headers='keys', tablefmt='rounded_grid'))
    else: 
        print('¡¡No hay productos registrados!!')
>>>>>>> showProduct
