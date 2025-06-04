from .helpers.insertion_service import *
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
        print(tabulate(all, headers='keys', tablefmt='rounded_grid'))
    else: 
        print('¡¡No hay productos registrados!!')