from InquirerPy import inquirer
from models import navegacion

def mostrar_menu(titulo: str, menu):

    if len(menu) != 0:

        var = opciones(
            f"\n=== {titulo} ===",
            [opcion for opcion in menu],
        )
        return var

    else:
        opciones("", ["Atras"])
        navegacion.navegacion.pop()
        navegacion.navegacion[-1]()


def opciones(mensaje:str, arr:list):
    
    var = inquirer.select(
        message=mensaje,
        choices=arr
        ).execute()

    return var


def faltan_datos(datos):
    print(f"No hay {datos} registradas, por favor registra un {datos} primero.")


def pedir_dato_str(mensaje):
    return input(mensaje)


def pedir_dato_int(mensaje):
    return int(input(mensaje))

def pedir_dato_float(mensaje):
    return float(input(mensaje))

def mostrar_texto_simple(mensaje):
    print(mensaje)