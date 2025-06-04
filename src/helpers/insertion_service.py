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

def update_product(id, data):
    pass

def delete_product(id):
    pass