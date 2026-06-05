from InquirerPy import inquirer
from views import Utilities
import sys

def mostrar_menu(titulo: str, menu, mensaje_vacio: str = "No hay opciones existentes"):

    if len(menu) != 0:

        var = Utilities.opciones(
            f"\n=== {titulo} ===",
            [opcion for opcion in menu],
        )
        return var

    else:
        var = Utilities.opciones(
            mensaje_vacio,
            ["salir"]
        )

        if var == "salir": sys.exit()


def opciones(mensaje:str, arr:list):
    var = inquirer.select(
        message=mensaje,
        choices=arr
        ).execute()

    return var