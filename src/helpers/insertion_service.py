<<<<<<< HEAD
from .insertionFunc import *


def create_new_product(typo, name, price, ingredients, dispo):
    """

    """
    datos = abrierJSON()
    nuevo_pro = { 
        "tipo": typo,
        "nombre": name,
        "precio": int(price),
        "ingredientes": ingredients,
        "disponibilidad": dispo
    }
    datos.append(nuevo_pro)
    saved = guardarDatos(datos)
    if (saved):
        print(f"¡¡La empanada {name} creo correctamente como nuevo producto!!")
    else:
        print('La operación no fue posible')

def show_product(id):
    pass

=======
from ..helpers.insertionFunc import *

def create_new_product():
    pass

def show_all_products():
    datas = abrierJSON()
    if (datas):
        return datas
    else:
        return False

def filter_name(name):
    productos = abrierJSON()
    all = []
    for pr in range(len(productos)):
        if (productos[pr]['nombre'].lower() == name.lower()):
            all.append(productos[pr])
    if (all is not None):
        return all
    else: 
        return False

>>>>>>> showProduct
def update_product(id, data):
    pass

def delete_product(id):
    pass