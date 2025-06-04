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

def update_product(id, data):
    pass

def delete_product(id):
    pass