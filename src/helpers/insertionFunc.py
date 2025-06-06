import json


def abrierJSON():
    """
        Función para abrir el json de los productos.
        No recibe argumentos.
        Retorna la lista de los productos registrados en el JSON
    """
    datas = []
    with open('./src/db/products.json', 'r') as data:
        datas = json.load(data)
    return datas

def guardarDatos(info):
    """
    Función para guardar todos los datos en el JSON
    Recibe como parametros los datos a insertar
    Retorna True si la oparción se ralizó con exito o False si no se realizó con exito.
    """
    with open('./src/db/products.json', 'w') as openFile:
        json.dump(info, openFile, indent=4, ensure_ascii=False)
    return True


def guardarUnDato():
    datos = abrierJSON()

    nuevo_dato = {
        "tipo": "res",
        "precio": 5000
    }
    datos.append(nuevo_dato)
    dataSaved = guardarDatos(datos)
    if (dataSaved):
        print('Envío exitoso.')
    else:
        print('No fue posible')

# guardarUnDato()